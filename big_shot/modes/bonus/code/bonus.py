# TODO
# Bonus count is double what it should be (2 lights on ball 1 should score 2k, not 4k) (Not all the time?)
# Lights don't count down...they just turn off.
# General erratic behavior
# pop empty list error - bonus mode code ran before score reels finished game scoring

from mpf.system.mode import Mode


class Bonus(Mode):

    def mode_start(self, **kwargs):

        if not self.machine.mode_controller.is_active('base'):
            self.machine.events.post("bonus_complete")
            self.stop()

        self.bonus_lights = list()
        self.bonus_value = 0
        self.prepare_bonus()

    def prepare_bonus(self):
        self.log.debug("Entering the Big Shot Bonus Sequence")

        if self.machine.game.tilted:
            self.log.debug("Ball has tilted. No bonus for you!")
            return

        self.set_bonus_value()

    def set_bonus_value(self):
        # Figures out what the bonus score value is based on what ball this is
        # and how many balls the game is set to.

        balls_remaining = (self.machine.config['game']['balls_per_game'] -
                           self.machine.game.player.vars['ball'])

        if balls_remaining > 1:
            self.bonus_value = (self.config['scoring']
                                ['bonusvalue']['score'])
        elif balls_remaining == 1:
            self.bonus_value = (self.config['scoring']
                                ['secondtolastbonusvalue']['score'])
        else:
            self.bonus_value = (self.config['scoring']
                                ['lastbonusvalue']['score'])
        self.calculate_bonus()

    def calculate_bonus(self, **kwargs):
        # calculate the bonus value for this ball
        for target in self.machine.drop_target_banks['Solids'].drop_targets:
            if target.complete:
                self.log.debug("Drop Target '%s' is down", target.name)
                self.bonus_lights.append(
                    self.machine.shots[target.name].config['light'][0])

        if self.machine.lights['l_ball8'].state['brightness']:
            self.log.debug("Eight Ball Target was hit")
            self.bonus_lights.append(self.machine.lights['l_ball8'])

        for target in self.machine.drop_target_banks['Stripes'].drop_targets:
            if target.complete:
                self.log.debug("Drop Target '%s' is down", target.name)
                self.bonus_lights.append(
                    self.machine.shots[target.name].config['light'][0])

        #self.log.debug("Bonus Lights: %s", self.bonus_lights)

        self.check_score_reels()

    def check_score_reels(self, **kwargs):
        self.reels = self.machine.score_reel_controller.active_scorereelgroup

        # Check to see if any of the score reels are busy
        if not self.reels.valid:
            self.log.debug("Found a score reel group that's not valid. "
                           "We'll wait...")
            self.add_mode_event_handler(
                'scorereelgroup_{}_valid'.format(self.reels.name),
                self.start_bonus)

        else:
            self.log.debug("Reels are valid. Starting now")
            # If they're not busy, start the bonus now
            self.start_bonus()

    def start_bonus(self, **kwargs):
        # remove the handler that we used to wait for the score reels to be done
        self.machine.events.remove_handler(self.start_bonus)

        # add the handler that will advance through these bonus steps
        self.add_mode_event_handler(
            'scorereelgroup_{}_valid'.format(self.reels.name), self.bonus_step)

        # do the first bonus step to kick off this process
        self.bonus_step()

    def bonus_step(self, **kwargs):
        # automatically called when the score reels are valid

        print "------------ entering bonus_step", self.machine.tick_num

        if self.bonus_lights:
            # sets the "pause" between bonus scores, then does the bonus step
            self.delay.add(ms=200, callback=self.do_bonus_step)
            #print(self.bonus_lights)

        else:
            self.bonus_done()

    def do_bonus_step(self):
        #print(self.bonus_lights)
        this_light = self.bonus_lights.pop()
        this_light.off(force=True)
        print "-------- turning off light", this_light, self.machine.tick_num

        self.machine.scoring.add(self.bonus_value)
        #self.log.debug("Turning off %s", this_light)



        # if this is the 8 ball, also turn off the top 8 ball lane light
        if this_light.name == 'l_ball8':
            self.machine.lights['l_eightBall500'].off(force=True)
            self.machine.lights['l_eightBallHole'].off(force=True)

    def bonus_done(self):
        self.log.debug("Bonus is done.")
        self.machine.events.post("bonus_complete")
        # Remove any event handlers we were waiting for
        #self.machine.events.remove_handler(self.bonus_step)

    def mode_stop(self, **kwargs):
        pass