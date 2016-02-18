# Attract mode for Big Shot

import inspect #329
from mpf.system.light_controller import Playlist
import mpf.modes.attract.code.attract


class Attract(mpf.modes.attract.code.attract.Attract):

    def mode_start(self, **kwargs):

        super(Attract, self).mode_start(**kwargs)

        for light in self.machine.lights.items_tagged('GI'):
            #print light
            light.on()


        # In Big Shot, the ball sitting in the plunger lane does not sit on a
        # switch, so if the machine starts with the ball in the plunger lane,
        # we need to trick the ball controller into thinking there's a ball
        # if self.machine.ball_controller.num_balls_known == 0:
        #      self.log.debug("No balls known, changing live et. al. to 1")
        #      self.machine.ball_controller.num_balls_known = 1

        self.machine.ball_devices.playfield.balls = 1

        # register for classic / modern notification
        #self.machine.events.add_handler('enable_classic_mode',
        #                                self.enable_classic_mode)
        #self.machine.events.add_handler('enable_modern_mode',
        #                                self.enable_modern_mode)

        # set initial classic / modern mode
        #if self.machine.classic_mode:
        #    self.enable_classic_mode()
        #else:
        #    self.enable_modern_mode()

        # Setup and start the modern shows. These play at all times. In classic
        # mode, the modern shows are still 'playing' under the boring classic
        # lights which are just off.

        self.modern_playlist = Playlist(self.machine)
        self.modern_playlist.add_show(step_num=1,
                               show=self.machine.shows['playfield_rack_snake'],
                               tocks_per_sec=10,
                               num_repeats=2,
                               repeat=True)
        self.modern_playlist.add_show(step_num=2,
                               show=self.machine.shows['playfield_rack_sweep'],
                               tocks_per_sec=10,
                               num_repeats=2,
                               repeat=True)
        self.modern_playlist.step_settings(step=1,
                        trigger_show=self.machine.shows['playfield_rack_snake'])
        self.modern_playlist.step_settings(step=2,
                        trigger_show=self.machine.shows['playfield_rack_sweep'])

        # Gabe added this to have a separate show playlist for the backbox

        self.modern_backbox_playlist = Playlist(self.machine)
        self.modern_backbox_playlist.add_show(step_num=1,
                                show=self.machine.shows['backbox_match_snake'],
                                tocks_per_sec=10,
                                num_repeats=2,
                                repeat=True)
        self.modern_backbox_playlist.add_show(step_num=2,
                                show=self.machine.shows['backbox_match_sparkle'],
                                tocks_per_sec=10,
                                num_repeats=6,
                                repeat=True)
        self.modern_backbox_playlist.add_show(step_num=3,
                                show=self.machine.shows['backbox_match_wipe'],
                                tocks_per_sec=10,
                                num_repeats=1,
                                repeat=True)
        self.modern_backbox_playlist.add_show(step_num=4,
                                show=self.machine.shows['backbox_wipe'],
                                tocks_per_sec=7,
                                num_repeats=2,
                                repeat=True)
        self.modern_backbox_playlist.step_settings(step=1,
                            trigger_show=self.machine.shows['backbox_match_snake'])
        self.modern_backbox_playlist.step_settings(step=2,
                            trigger_show=self.machine.shows['backbox_match_sparkle'])
        self.modern_backbox_playlist.step_settings(step=3,
                            trigger_show=self.machine.shows['backbox_match_wipe'])
        self.modern_backbox_playlist.step_settings(step=4,
                            trigger_show=self.machine.shows['backbox_wipe'])

        self.machine.shows['top_lanes_sweep'].play(
            repeat=True, tocks_per_sec=5)
        self.machine.shows['pop_8_alternate'].play(
            repeat=True, tocks_per_sec=5)
        self.machine.shows['mid_lights_bounce'].play(
            repeat=True, tocks_per_sec=5)
        # self.machine.shows['backbox_match_snake'].play(
        #    repeat=True, tocks_per_sec=13)
        self.modern_playlist.start()
        self.modern_backbox_playlist.start()


        self.machine.events.add_handler('sw_leftFlipper',
                                        self.demo_music)
        #                                self.demo_music('leftFlip'))
        #self.machine.events.add_handler('sw_rightFlipper',
        #                                self.demo_music('rightFlip'))

    # def enable_classic_mode(self):
    #     self.machine.shows['classic_overlay'].play(
    #         repeat=False, hold=True, tocks_per_sec=1, priority=200)
    #     # pass
    #
    # def enable_modern_mode(self):
    #     self.machine.shows['classic_overlay'].stop(hold=False, reset=True)
    #     # pass

    def mode_stop(self, **kwargs):
        self.machine.shows['top_lanes_sweep'].stop()
        self.machine.shows['pop_8_alternate'].stop()
        self.machine.shows['mid_lights_bounce'].stop()
        self.modern_playlist.stop()
        self.modern_backbox_playlist.stop()
        self.machine.shows['classic_overlay'].stop()

        #self.machine.events.remove_handler(self.enable_classic_mode)
        #self.machine.events.remove_handler(self.enable_modern_mode)
        self.machine.events.remove_handler(self.demo_music)

#    def demo_music(self, demoEvent):
    def demo_music(self):
        # Define a show
        #if demoEvent == 'leftFlip':
        show_name = 'ipanema'
        tocks_per_sec = 20

        #if demoEvent == 'rightFlip':
        #    show_name = 'ipanema'
        #    tocks_per_sec = 30
        #else:
        #    pass
        # Now play it
        self.machine.shows[show_name].play(repeat=False,
                                           tocks_per_sec=tocks_per_sec)
