# Attract mode Scriptlet for Bullseye

from mpf.system.scriptlet import Scriptlet
from mpf.system.light_controller import Playlist


class Attract(Scriptlet):

    def on_load(self):
        self.machine.events.add_handler('machineflow_Attract_start', self.start)
        self.machine.events.add_handler('machineflow_Attract_stop', self.stop)

    def start(self):
        # In Bullseye, the ball sitting in the plunger lane does not sit on a
        # switch, so if the machine starts with the ball in the plunger lane,
        # we need to trick the ball controller into thinking there's a ball
        # Only problem is that the ball controller doesn't work this way anymore.
        # Need to find a way to add a ball to the playfield ball count, I guess?
        # if self.machine.ball_controller.num_balls_known == 0:
        #     self.log.debug("No balls known, changing live et. al. to 1")
        #     self.machine.ball_controller._num_balls_live = 1
        #     self.machine.ball_controller.num_balls_known = 1
        #     self.machine.ball_controller._num_balls_desired_live = 1
        # for gi in self.machine.gi:
        #     gi.on()
        self.modern_playlist = Playlist(self.machine)
        self.modern_playlist.add_show(step_num=1,
                               show=self.machine.shows['dart_board_alternate'],
                               tocks_per_sec=4,
                               num_repeats=5,
                               repeat=True)
        self.modern_playlist.add_show(step_num=2,
                               show=self.machine.shows['dart_board_spiral'],
                               tocks_per_sec=28,
                               num_repeats=5,
                               repeat=True)
        self.modern_playlist.step_settings(step=1,
                        trigger_show=self.machine.shows['dart_board_alternate'])
        self.modern_playlist.step_settings(step=2,
                        trigger_show=self.machine.shows['dart_board_spiral'])
        self.modern_playlist.start()

    def stop(self):
        self.modern_playlist.stop()
