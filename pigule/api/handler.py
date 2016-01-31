import socketserver
import json
import threading
import os


server_manager = None


# TODO: check how to test a stream request handler
class ApiHandler(socketserver.StreamRequestHandler):
    def setup(self):
        socketserver.StreamRequestHandler.setup(self)
        self.is_running = False

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

    def handle(self):
        # TODO: refactor handle method
        self.start()
        while self.is_running:
            try:
                data = self.read_data()
            except ValueError:
                self.send_error('data is not a valid JSON object')
                continue

            if 'type' not in data:
                self.send_error('data must contain a `type` field')
            elif data['type'] == 'QUIT':
                self.stop()

    def send_error(self, error_msg):
        # TODO: define a method to build data "auto-magically"
        data = {
            'type': 'ERROR',
            'error': 'INVALID REQUEST: {}'.format(error_msg)
        }
        self.send(data)


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
