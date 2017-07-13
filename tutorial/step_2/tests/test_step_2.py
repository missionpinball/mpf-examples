"""Contains tests for Step 2 of the MPF tutorial."""

from mpf.tests.MpfMachineTestCase import MpfMachineTestCase


class TestTutorialMachine(MpfMachineTestCase):

    """Contains tests for the MPF machine config"""

    def test_step_2_mpf_startup(self):
        """Tests Step 2 of the tutorial"""

        # At this point, the machine config is blank, which means that other
        # than MPF starting and the attract mode running, nothing is really
        # happening. So let's just check that the attract mode is running and
        # that's it.

        self.assertModeRunning('attract')

        # asserts that a mode called 'attract' is running, and fails the test
        # if not.
