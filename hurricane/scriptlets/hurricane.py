# General scriptlet for Hurricane

from mpf.system.scriptlet import Scriptlet


class Hurricane(Scriptlet):

    def on_load(self):

        self.machine.events.add_handler('ball_started', self.ball_started)
        self.machine.events.add_handler('ball_ending', self.ball_ending)

    def ball_started(self, **kwargs):
        # Hurricane uses the GI07 relay to enable / disable the flippers.
        self.machine.gi['flipperEnable'].on()

    def ball_ending(self, **kwargs):
        # Hurricane uses the GI07 relay to enable / disable the flippers.
        self.machine.gi['flipperEnable'].off()
        self.machine.coils['ferrisWheels'].disable()
