from mpf.tests.MpfMachineTestCase import MpfMachineTestCase


class TestSimpleGame(MpfMachineTestCase):

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
        self.assertIsNone(self.machine.game)
