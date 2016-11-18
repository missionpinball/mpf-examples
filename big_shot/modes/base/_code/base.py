from mpf.core.mode import Mode


class Base(Mode):

    def mode_init(self):
        self.queue = None

    def mode_start(self, **kwargs):
        self.add_mode_event_handler('collect_special', self.collect_special)
        self.add_mode_event_handler('sw_eightball', self.switch_eight_ball_lights)
        self.add_mode_event_handler('ball_ending', self.ball_ending)
        self.add_mode_event_handler('bonus_complete', self.bonus_complete)
        self.add_mode_event_handler('drop1_down', self.solid_target_hit)
        self.add_mode_event_handler('drop2_down', self.solid_target_hit)
        self.add_mode_event_handler('drop3_down', self.solid_target_hit)
        self.add_mode_event_handler('drop4_down', self.solid_target_hit)
        self.add_mode_event_handler('drop5_down', self.solid_target_hit)
        self.add_mode_event_handler('drop6_down', self.solid_target_hit)
        self.add_mode_event_handler('drop7_down', self.solid_target_hit)
        self.add_mode_event_handler('drop9_down', self.stripe_target_hit)
        self.add_mode_event_handler('drop10_down', self.stripe_target_hit)
        self.add_mode_event_handler('drop11_down', self.stripe_target_hit)
        self.add_mode_event_handler('drop12_down', self.stripe_target_hit)
        self.add_mode_event_handler('drop13_down', self.stripe_target_hit)
        self.add_mode_event_handler('drop14_down', self.stripe_target_hit)
        self.add_mode_event_handler('drop15_down', self.stripe_target_hit)
        self.set_bonus_lights()
        self.set_eight_ball_lights()

    def set_bonus_lights(self, **kwargs):
        # Used to set the proper playfield light to show the bonus value for
        # that ball

        balls_remaining = (self.machine.config['game']['balls_per_game'] -
                           self.machine.game.player.vars['ball'])

        if balls_remaining > 1:
            self.machine.lights['l_bonus1k'].on()
            self.machine.lights['l_bonus2k'].off()
            self.machine.lights['l_bonus3k'].off()
        elif balls_remaining == 1:
            self.machine.lights['l_bonus1k'].off()
            self.machine.lights['l_bonus2k'].on()
            self.machine.lights['l_bonus3k'].off()
        else:
            self.machine.lights['l_bonus1k'].off()
            self.machine.lights['l_bonus2k'].off()
            self.machine.lights['l_bonus3k'].on()

    def collect_special(self, **kwargs):
        # self.machine.coils.c_knocker.pulse() # Added to coil config
        self.machine.game.award_extra_ball()
        self.set_eight_ball_lights()

    def switch_eight_ball_lights(self, **kwargs):
        self.machine.lights['l_eightball500'].off()
        self.machine.lights['l_eightballhole'].off()
        self.machine.lights['l_ball8'].on()

    def set_eight_ball_lights(self,**kwargs):
        self.machine.lights['l_eightball500'].on()
        self.machine.lights['l_eightballhole'].on()
        self.machine.lights['l_ball8'].off()

    def mode_stop(self, **kwargs):
        pass

    def ball_ending(self, queue, **kwargs):
        self.queue = queue
        queue.wait()

    def bonus_complete(self, **kwargs):
        self.stop()
        self.queue.clear()

    def solid_target_hit(self, **kwargs):  # gabe

        if not self.machine.classic_mode:

            self.machine.shows['solid_target_hit'].play(repeat=False,
                                                       tocks_per_sec=25,
                                                       priority=1001)

    def stripe_target_hit(self, **kwargs):  # gabe

        if not self.machine.classic_mode:

            self.machine.shows['stripe_target_hit'].play(repeat=False,
                                                       tocks_per_sec=25,
                                                       priority=1001)