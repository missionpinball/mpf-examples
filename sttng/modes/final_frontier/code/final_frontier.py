from mpf.system.modes import Mode

class FinalFrontier(Mode):
    def mode_init(self):
        pass

    def mode_stop(self):
        self.machine.events.post('final_frontier_complete')