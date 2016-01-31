import pigule.archetypes as archetypes


# TODO: refactor to facilitate tests
class ApiServer:
    def __init__(self, manager):
        self.manager = manager

    def handle(self, data):
        if data['type'] == 'CREATE_MASTER_CELL':
            return self.create_master_cell()
        if data['type'] == 'SHOW_STATE':
            return self.state()
        else:
            return self.error('{} is not a valid data type'.format(data['type']))

    def create_master_cell(self):
        archetypes.create_master_cell(self.manager)
        return {
            'type': 'NEW_MASTER_CELL'
        }

    def state(self):
        cells = list(self.manager.entities())
        return {
            'type': 'STATE',
            'payload': {
                'cells_number': len(cells)
            }
        }

    def error(self, error_msg):
        return {
            'type': 'ERROR',
            'error': error_msg
        }
