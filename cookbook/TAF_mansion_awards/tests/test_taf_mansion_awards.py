from mpf.tests.MpfMachineTestCase import MpfMachineTestCase


class TestTafMansionAwards(MpfMachineTestCase):

    def _start_single_player_game(self, secs_since_plunge):
        self.hit_and_release_switch('start')

        # game should be running
        self.assertIsNotNone(self.machine.game)
        self.assertEqual(1, self.machine.game.player.ball)

        # advance enough time for the balls to eject and stuff
        self.advance_time_and_run()

        # ball should be sitting in the plunger lane
        self.assertEqual(self.machine.ball_devices.drain.balls, 0)
        self.assertEqual(self.machine.ball_devices.trough.balls, 2)
        self.assertEqual(self.machine.ball_devices.plunger_lane.balls, 1)

        # playfield expects a ball
        self.assertEqual(1, self.machine.playfield.available_balls)

        # but its not there yet
        self.assertEqual(0, self.machine.playfield.balls)

        # after 20s it's still not there
        self.advance_time_and_run(20)
        self.assertEqual(0, self.machine.playfield.balls)

        # player mechanically ejects
        self.machine.switch_controller.process_switch('plunger_lane', 0, True)
        self.advance_time_and_run(secs_since_plunge)  # plunger timeout is 3s

    # def test_single_player_game_start(self):
    #     self._start_single_player_game(4)
    #
    #     # 4 secs since plunge means ball is on the pf
    #     self.assertEqual(1, self.machine.playfield.balls)
    #     self.assertEqual(self.machine.ball_devices.drain.balls, 0)
    #     self.assertEqual(self.machine.ball_devices.trough.balls, 2)
    #     self.assertEqual(self.machine.ball_devices.plunger_lane.balls, 0)
    #
    #     self.assertModeRunning('mansion_awards')

    def test_taf_mansion_awards(self):
        self._start_single_player_game(4)

        # make sure the selected achievement knows it's selected
        self.assertEqual(
            self.machine.achievement_groups.mansion_awards._selected_member.state,
            'selected')

        # The initial selected achievement should be one of these 2
        self.assertIn(
            self.machine.achievement_groups.mansion_awards._selected_member,
                      [self.machine.achievements.mamushka,
                       self.machine.achievements.hit_cousin_it])

        # it's light should be flashing
        self.assertLightFlashing(
            self.machine.achievement_groups.mansion_awards._selected_member.config['show_tokens']['lights'])

        # There should be 11 more enabled achievements
        enabled_achievements = [x for x in self.machine.achievements if
                                 x.state == 'enabled']

        self.assertEqual(len(enabled_achievements), 11)

        # all those lights should be off
        for ach in enabled_achievements:
            self.assertLightOff(ach.config['show_tokens']['lights'])

        # Tour the mansion should be disabled
        self.assertEqual(self.machine.achievements.tour_mansion.state,
                         "disabled")

        # The mansion_awards group should be enabled
        self.assertTrue(self.machine.achievement_groups.mansion_awards.enabled)

        # the chair lights should be on
        self.assertLightOn('electric_chair_red')
        self.assertLightOn('electric_chair_yellow')

        # pop bumper hits should change the selected award

        # create a list of all the mansion achievements
        achievements = set(
            self.machine.achievement_groups.mansion_awards.config['achievements'][:])

        # now hit the pop bumper a bunch of times and make sure all the awards
        # are selected
        while achievements:
            self.hit_and_release_switch('upper_left_jet')
            achievements.discard(
                self.machine.achievement_groups.mansion_awards._selected_member)

        # let's shoot the electric chair to get the selected award
        selected_achievement = self.machine.achievement_groups.mansion_awards._selected_member
        self.hit_switch_and_run('electric_chair', 1)

        # that one should be complete now
        self.assertEqual(selected_achievement.state, 'completed')

        # new one should be selected
        new_selected_achievement = self.machine.achievement_groups.mansion_awards._selected_member

        self.assertNotEqual(selected_achievement, new_selected_achievement)
