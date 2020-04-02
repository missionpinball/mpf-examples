"""Contains tests for the MPF tutorial."""

from mpf.tests.MpfMachineTestCase import MpfMachineTestCase


class TestTutorialMachine(MpfMachineTestCase):

    """Contains tests for the MPF machine config"""

    def test_attract(self):
        """Test that machine starts attract and can start a game."""
        self.assertModeRunning('attract')

        self.hit_switch_and_run("s_trough1", 1)
        self.hit_switch_and_run("s_trough2", 1)

        self.hit_and_release_switch("s_start")

        self.advance_time_and_run(5)
        self.assertModeRunning('game')
        self.assertModeRunning('base')
        self.assertModeNotRunning('attract')
