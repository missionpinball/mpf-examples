from mpf.system.modes import Mode
import inspect

class Base(Mode):
    def mode_init(self, **kwargs):
    #    self.player = None
        pass

    def mode_start(self, **kwargs):
        self.add_mode_event_handler('targets_all_targets_lit_complete', self.blinkenlites)
        self.log.debug("seattle")
        pass


        for led in self.machine.leds:
            self.machine.light_controller.run_script(script=self.machine.light_controller.registered_light_scripts['flash'],
                                                    leds=led.name,
                                                    priority=4,
                                                    blend=False,
                                                    tocks_per_sec=1,
                                                    repeat=False)


    def blinkenlites(self):
        self.log.debug("++++++++++ blinkenlites")

        for led in self.machine.leds:
            self.machine.light_controller.run_script(script=self.machine.light_controller.registered_light_scripts['flash'],
                                                    leds=led,
                                                    priority=4,
                                                    blend=False,
                                                    tocks_per_sec=1,
                                                    repeat=False)
            self.log.debug("++++++++++ Turning on %s", led)
        # self.machine.lights[self.mission_lights[index]].off()
        pass
    def mode_stop(self):
        pass
