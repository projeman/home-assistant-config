import appdaemon.plugins.hass.hassapi as hass

#
# App to respond to buttons on an Aeotec Minimote
#
# Args:
#
# Minimote can send up to 8 scenes. Odd numbered scenes are short presses of the buttons, even are long presses
#
# Args:
#
#scene_<id>_on - name of the entity to turn on when scene <id> is activated
#scene_<id>_off - name of the entity to turn off when scene <id> is activated. If the entity is a scene it will be turned on.
#scene_<id>_toggle - name of the entity to toggle when scene <id> is activated
#
# Each scene can have up to one of each type of action, or no actions - e.g. you can turn on one light and turn off another light for a particular scene if desired
#

class MiniMote(hass.Hass):

  def initialize(self):
    self.listen_event(self.zwave_event, "zwave_js_value_notification", node_id = self.args["node_id"])
    
  def zwave_event(self, event_name, data, kwargs):
    #self.log("Event: {}, data = {}, args = {}".format(event_name, data, kwargs))
    scene = data["value"]
    on = "scene_{}_on".format(scene)
    off = "scene_{}_off".format(scene)
    toggle = "scene_{}_toggle".format(scene)
    panic_mode = "off"

    if "panic_mode_boolean" in self.args:
      panic_mode = self.get_state(self.args["panic_mode_boolean"])
      panic_entity = self.args["panic_entity"]

    if panic_mode == "on":
      self.log("Panic Mode! Turning {} on".format(panic_entity))
      self.turn_on(panic_entity)
    
    elif on in self.args:
      self.log("Turning {} on".format(self.args[on]))
      self.turn_on(self.args[on])

    elif off in self.args:
      type, id = self.args[off].split(".")
      if type == "scene":
        self.log("Turning {} on".format(self.args[off]))
        self.turn_on(self.args[off])
      else:
        self.log("Turning {} off".format(self.args[off]))
        self.turn_off(self.args[off])

    elif toggle in self.args:
      self.log("Toggling {}".format(self.args[toggle]))
      self.toggle(self.args[toggle])
      
