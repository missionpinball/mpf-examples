# Mission Control mode file for STTNG


import random
import inspect #329
from mpf.system.modes import Mode


class MissionControl(Mode):

    def mode_init(self):
        self.player = None
        self.running_script = None

        self.mission_lights = ['l_shipMode1', 'l_shipMode2', 'l_shipMode3',
                               'l_shipMode4', 'l_shipMode5', 'l_shipMode6',
                               'l_shipMode7', 'l_finalFrontier']
        self.mission_events = ['start_mode_time_rift', 'start_mode_worm_hole',
                               'start_mode_search_the_galaxy',
                               'start_mode_battle_simulation',
                               'start_mode_qs_challenge', 'start_mode_rescue',
                               'start_mode_asteroid_threat',
                               'start_mode_final_frontier']

        self.flash_start_mission = None

        self.add_mode_event_handler('player_add_success', self.player_init)
        ### REMOVE THIS AFTER TESTING MODES
     #   self.add_mode_event_handler('sw_buyIn', self.mission_shortcut)

    #def mission_shortcut(self):
     #   self.machine.events.post('start_mode_time_rift')

    def player_init(self, player, **kwargs):
        # We're gonna go left to right here, so:
        # 0 = Time Rift
        # 1 = Worm Hole
        # 2 = Search the Galaxy
        # 3 = Battle Simulation
        # 4 = Q's Challenge
        # 5 = Rescue
        # 6 = Asteroid Threat
        # 7 = Final Frontier

        # Need to add provisions in the rotator for re-doing missions, but this
        # is fine for now. Re-doing missions is only a Command Decision thing
        # anyway.

        player.missions_complete = [0]*7

        # Need to add competition logic here whenever that becomes a thing

        player.mission_lit = random.randrange(0,6,1)

    def mode_start(self):
        #self.player = self.machine.game.player
        self.add_mode_event_handler('return_to_mission_control',
                                    self.enable_mission_select)
        self.add_mode_event_handler('final_frontier_complete',
                                    self.reset_after_final_frontier)
        self.enable_mission_select()


        # We probably need something else that runs when a mission ends and this
        # mode is started up again. We need it to automatically rotate to the
        # next mission (light, list changed to 1, etc...) as well as to set the
        # last mission played to 2
        #
        # This is probably the thing that also keeps track of Final Frontier. So
        # maybe this goes into the mission_rotator method?

    def mode_stop(self):
        #self.machine.events.remove_handler(self.mission_started)
        #self.machine.events.remove_handler(self.command_decision)
        #self.machine.events.remove_handler(self.mission_rotate)
        #self.machine.events.remove_handler(self.enable_mission_select)
        #self.machine.events.remove_handler(self.reset_after_final_frontier)
        self.light_start_mission(False)

    def reset_after_final_frontier(self):
        self.player.missions_complete = None
        self.player.mission_lit = None
        self.player_init(self.player)
        self.enable_mission_select()

    def mission_rotate(self, direction='right', allow_completed=False):
        if self.player.missions_complete.count(0):
            index=self.player.mission_lit
            if direction == 'right':
                index += 1
                if index == 7:
                    index = 0
                if not allow_completed:
                    while self.player.missions_complete[index]:
                        index += 1
                        if index == 7:
                            index = 0
            else:
                index -= 1
                if index == -1:
                    index = 6
                if not allow_completed:
                    while self.player.missions_complete[index]:
                        index -= 1
                        if index == -1:
                            index = 6
        else:
            index = 7

        self.update_lit(index)

    def update_lit(self, index):
        self.player.mission_lit = index
        self.update_lights()

    def update_lights(self):

        #self.log.info('UDL old running script: %s:', self.running_script)

        if self.running_script:
            #self.log.info('UDL stopping current running script')
            self.running_script.stop()
        for index, value in enumerate(self.player.missions_complete):
            if value:
                #self.log.info("I'm turning ON light %s",
                #              self.mission_lights[index])
                self.machine.lights[self.mission_lights[index]].on()
            else:
                #self.log.info("I'm turning off light %s",
                #              self.mission_lights[index])
                self.machine.lights[self.mission_lights[index]].off()

        self.running_script = self.machine.light_controller.run_script(
            lightname=self.mission_lights[self.player.mission_lit],
            script=self.machine.light_controller.registered_light_scripts['flash'],
            tps='2'
        )
        #self.log.info('UDL new running script: %s', self.running_script)

    def mission_started(self):
        self.light_start_mission(False)
        self.machine.events.post(self.mission_events[self.player.mission_lit])

        if not self.player.mission_lit == 7:
            self.player.missions_complete[self.player.mission_lit] += 1

        self.machine.events.remove_handler(self.mission_started)
        self.machine.events.remove_handler(self.command_decision)
        self.machine.events.remove_handler(self.mission_rotate)

        #self.machine.events.post('mission_control_mission_started')

        # Need the code here to:
        #
        # Find the list item that contains a 1 and start the mode associated
        # with that mission
        #
        # I guess that means we need a lookup table or set of if-thens to say:
        # "if player.mission_states = 1, post an event that starts worm hole"
        #
        # Additionally, we have to check for Final Frontier. So perhaps that
        # runs first, like: If Final Frontier is enabled, post an event to start
        # that mode. Else, find the index in mission_states that = 1 and start
        # that.

    def light_start_mission(self, lit=True):
        if lit:
 #           self.flash_start_mission = self.machine.light_controller.run_script(
 #               lightname='l_startMission',
 #               script=self.machine.light_controller.light_scripts['flash'],
 #               tps=8
            self.flash_start_mission = self.machine.light_controller.run_script(script=self.machine.light_controller.registered_light_scripts['flash'],
                light = 'l_startMission',
                tps = '8',
                blend = False,
                repeat = True,
                priority = '9000'
            )
        else:
            self.flash_start_mission.stop()
            self.machine.lights['l_startMission'].off()

    def enable_mission_select(self):
        # is this the final frontier event?
        # self.player_init(player=self.player)
        # if not,
        self.add_mode_event_handler('sw_start_mission',
                                        self.mission_started)
        self.add_mode_event_handler('sw_command_decision',
                                        self.command_decision)
        self.add_mode_event_handler('sw_advance_mission',
                                        self.mission_rotate)
        self.light_start_mission()
        self.mission_rotate()


    def command_decision(self):
        pass
        # This is here as an extra challenge that we don't need to address
        # currently. In STTNG, when Command Decision is lit and hit, the player
        # gets a menu to choose which mission they want to play. Consider this
        # extra credit for later.
