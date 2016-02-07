import pigule.archetypes as archetypes

import pigule.api.answer_creators as answer_creators


class ApiServer:
    def __init__(self, manager):
        self.manager = manager

    def create_master_cell(self):
        archetypes.create_master_cell(self.manager)
        return answer_creators.new_master_cell()

    def show_state(self):
        cells = list(self.manager.entities())
        return answer_creators.state(len(cells))

    def quit(self):
        return answer_creators.quit()
