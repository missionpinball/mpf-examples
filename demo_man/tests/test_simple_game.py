from mpf.tests.MpfMachineTestCase import FullMachineTestCase


class TestSimpleGame(FullMachineTestCase):

    def getMachinePath(self):
        return "demo_man"

    def test_single_player_game(self):
        self.hit_and_release_switch("s_start")
        # game should be running
        self.assertIsNotNone(self.machine.game)
        self.assertEqual(1, self.machine.game.player.ball)
        # playfield expects a ball
        self.assertEqual(1, self.machine.playfield.available_balls)
        # but its not there yet
        self.assertEqual(0, self.machine.playfield.balls)

        # after 20 its there
        self.advance_time_and_run(20)
        self.assertEqual(1, self.machine.playfield.balls)

        self.assertTextOnTopSlide("BALL 1    FREE PLAY")

        # make some points
        self.hit_and_release_switch("s_left_jet")
        self.hit_and_release_switch("s_left_jet")
        self.hit_and_release_switch("s_left_jet")
        self.hit_and_release_switch("s_left_jet")
        self.advance_time_and_run()
        self.assertEqual(4 * 75020, self.machine.game.player.score)
        self.assertTextOnTopSlide("300,080")

        # ball drains
        self.machine.default_platform.add_ball_to_device(self.machine.ball_devices.trough)
        # wait for highscore display
        self.advance_time_and_run(10)
        self.assertEqual(0, self.machine.playfield.balls)
        self.assertEqual(2, self.machine.game.player.ball)

        # and it should eject a new ball to the pf
        self.advance_time_and_run(20)
        self.assertEqual(1, self.machine.playfield.balls)

        # ball drains again
        self.machine.default_platform.add_ball_to_device(self.machine.ball_devices.trough)
        # wait for highscore display
        self.advance_time_and_run(10)
        self.assertEqual(0, self.machine.playfield.balls)
        self.assertEqual(3, self.machine.game.player.ball)

        # and it should eject a new ball to the pf
        self.advance_time_and_run(20)
        self.assertEqual(1, self.machine.playfield.balls)

        # ball drains again. game should end
        self.machine.default_platform.add_ball_to_device(self.machine.ball_devices.trough)
        self.advance_time_and_run(10)

        # enter high score
        self.assertSlideOnTop("high_score_enter_initials")
        self.hit_and_release_switch("s_flipper_lower_right")
        self.hit_and_release_switch("s_flipper_lower_right")
        self.hit_and_release_switch("s_start")  # C
        self.advance_time_and_run()
        self.hit_and_release_switch("s_flipper_lower_right")
        self.hit_and_release_switch("s_start")  # CD
        self.advance_time_and_run()
        self.hit_and_release_switch("s_flipper_lower_right")
        self.hit_and_release_switch("s_start")  # CDE

        self.advance_time_and_run(10)
        self.assertIsNone(self.machine.game)
