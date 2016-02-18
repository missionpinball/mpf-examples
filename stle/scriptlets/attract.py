# Attract mode Scriptlet for STLE

from mpf.system.scriptlet import Scriptlet
from mpf.system.show_controller import Playlist


class Attract(Scriptlet):

    def on_load(self):
        self.machine.events.add_handler('machineflow_Attract_start', self.start)
        self.machine.events.add_handler('machineflow_Attract_stop', self.stop)

    def stop(self):
        pass