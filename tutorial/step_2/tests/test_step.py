"""Contains tests for the MPF tutorial."""

from mpf.tests.MpfMachineTestCase import MpfMachineTestCase


class TestTutorialMachine(MpfMachineTestCase):

    """Contains tests for the MPF machine config"""

    def test_attract(self):
        """Test that machine starts attract."""
        self.assertModeRunning('attract')
