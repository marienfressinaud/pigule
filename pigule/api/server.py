import pigule.archetypes as archetypes


# TODO: refactor to facilitate tests
class ApiServer:
    def __init__(self, manager):
        self.manager = manager

    def handle(self, data):
        if data['type'] == 'CREATE_MASTER_CELL':
            return self.create_master_cell()
        else:
            return self.error('{} is not a valid data type'.format(data['type']))

    def create_master_cell(self):
        archetypes.create_master_cell(self.manager)
        return {
            'type': 'NEW_MASTER_CELL'
        }

    def error(self, error_msg):
        return {
            'type': 'ERROR',
            'error': error_msg
        }
