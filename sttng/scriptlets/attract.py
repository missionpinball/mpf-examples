# Attract mode Scriptlet for STTNG

from mpf.system.scriptlet import Scriptlet
from mpf.system.light_controller import Playlist


class Attract(Scriptlet):

    def on_load(self):
        self.machine.events.add_handler('machineflow_Attract_start', self.start)
        self.machine.events.add_handler('machineflow_Attract_stop', self.stop)
                # Register the switch handler for the diverter PWM testing switch
#        self.machine.switch_controller.add_switch_handler(
#            switch_name='s_buyIn', state=1, ms=0,
#            callback=self.enable_diverter)
#        self.machine.switch_controller.add_switch_handler(
#            switch_name='s_buyIn', state=0, ms=0,
#            callback=self.disable_diverter)

    def start(self):
#        self.machine.lights['lt_jackpot'].off()

#        for gi in self.machine.gi:
#            print("&&&&&& ", gi.name)
#            gi.off()

#        self.machine.lights['lt_jackpot'].on()

        for gi in self.machine.gi:
            gi.on()

        # Need to add some logic here, like "if not sw_leftLock = active then"

        if self.machine.balldevices['bd_leftVUK'].balls > 1:
            self.machine.balldevices['bd_leftVUK'].eject(
                self.machine.balldevices['bd_leftVUK'].balls-1)
        elif not self.machine.balldevices['bd_leftVUK'].balls:
            self.machine.balldevices['bd_leftVUK'].request_ball()

        if self.machine.balldevices['bd_leftCannonVUK'].balls > 1:
            self.machine.balldevices['bd_leftCannonVUK'].eject(
                self.machine.balldevices['bd_leftCannonVUK'].balls-1)
        elif not self.machine.balldevices['bd_leftCannonVUK'].balls:
            self.machine.balldevices['bd_leftCannonVUK'].request_ball()

        if self.machine.balldevices['bd_rightCannonVUK'].balls > 1:
            self.machine.balldevices['bd_rightCannonVUK'].eject(
                self.machine.balldevices['bd_rightCannonVUK'].balls-1)
        elif not self.machine.balldevices['bd_rightCannonVUK'].balls:
            self.machine.balldevices['bd_rightCannonVUK'].request_ball()

    def stop(self):
        pass

    def enable_diverter(self):
        self.machine.coils['c_underDivertorBottom'].pwm(1,2)

    def disable_diverter(self):
        self.machine.coils['c_underDivertorBottom'].disable()
