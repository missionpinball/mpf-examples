from mpf.core.modes import Mode

class TimeRift(Mode):
    def mode_init(self):
        pass

    def mode_stop(self):
        self.machine.events.post('return_to_mission_control')
        