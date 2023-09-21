"""Template file you can customize to build your own machine-specific Scriptlets.
"""

from mpf.core.custom_code import CustomCode


class YourScriptletName(CustomCode):  # Change `YourScriptletName` to whatever you want!
    """To 'activate' this code:
        1. Copy it to your machine_files/<your_machine_name>/code/ folder
        2. Add an entry to the 'custom_code:' section of your machine config files
        3. That entry should be 'your_hacket_file_name.YourScriptletName'
    """

    def on_load(self):
        """Called automatically when this code is loaded."""
        pass
