from mpf.tests.MpfMachineTestCase import MpfMachineTestCase


class TestSimpleGame(MpfMachineTestCase):

    def get_platform(self):
        return 'smart_virtual'

    def testSimpleGame(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(20)
        self.assertEqual(1, self.machine.playfield.balls)
        self.assertEqual(1, self.machine.game.num_players)
        self.assertEqual(1, self.machine.game.player.ball)

        self.machine.default_platform.add_ball_to_device(self.machine.ball_devices.trough)
        self.advance_time_and_run(20)
        self.assertEqual(1, self.machine.playfield.balls)
        self.assertEqual(1, self.machine.game.num_players)
        self.assertEqual(2, self.machine.game.player.ball)

        self.machine.default_platform.add_ball_to_device(self.machine.ball_devices.trough)
        self.advance_time_and_run(20)
        self.assertEqual(1, self.machine.playfield.balls)
        self.assertEqual(1, self.machine.game.num_players)
        self.assertEqual(3, self.machine.game.player.ball)

        self.machine.default_platform.add_ball_to_device(self.machine.ball_devices.trough)
        self.advance_time_and_run(20)
        self.assertIsNone(self.machine.game)
        self.assertEqual(0, self.machine.playfield.balls)
