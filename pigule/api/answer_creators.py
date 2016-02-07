def new_master_cell():
    return {
        'type': 'NEW_MASTER_CELL',
    }


def state(cell_number):
    return {
        'type': 'STATE',
        'payload': {
            'cells_number': cell_number,
        }
    }


def error(error_msg):
    return {
        'type': 'ERROR',
        'error': error_msg,
    }


def quit():
    return {
        'type': 'QUIT',
    }
