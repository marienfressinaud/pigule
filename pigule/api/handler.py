import socketserver
import json
import threading
import os

from pigule.api.server import ApiServer
import pigule.api.answer_creators as answer_creators


server_manager = None


# TODO: check how to test a stream request handler
class ApiHandler(socketserver.StreamRequestHandler):
    def setup(self):
        socketserver.StreamRequestHandler.setup(self)
        self.is_running = False
        self.api_server = ApiServer(server_manager)

    def start(self):
        if self.is_running:
            return
        self.is_running = True

    def stop(self):
        if not self.is_running:
            return
        self.is_running = False

    def read_data(self):
        # TODO: give possibility to read from several lines
        return json.loads(self.rfile.readline().decode('utf-8'))

    def send(self, data):
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def get_answer_from_data(self, data):
        api_server_method_name = data['type'].lower()
        if 'type' not in data:
            answer = answer_creators.error(
                'data must contain a `type` field'
            )
        elif hasattr(self.api_server, api_server_method_name):
            answer = getattr(self.api_server, api_server_method_name)()
        else:
            answer = answer_creators.error(
                '{} is not a valid data type'.format(data['type'])
            )

        return answer

    def handle(self):
        self.start()
        while self.is_running:
            try:
                data = self.read_data()
                answer = self.get_answer_from_data(data)
            except ValueError:
                answer = answer_creators.error(
                    'data is not a valid JSON object'
                )

            self.send(answer)

            if answer['type'] == 'QUIT':
                self.stop()


def setup(manager):
    global server_manager
    server_manager = manager

    host = os.getenv('PIGULE_SERVER_NAME', 'localhost')
    port = int(os.getenv('PIGULE_SERVER_PORT', '9998'))
    tcp_server = socketserver.ThreadingTCPServer((host, port), ApiHandler)

    server_thread = threading.Thread(target=tcp_server.serve_forever)
    server_thread.daemon = True
    server_thread.stop = tcp_server.shutdown

    return server_thread
