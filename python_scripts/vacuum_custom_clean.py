"""
Take input from a number of input_select and then tell Roborock to clean those rooms

miiocli vacuum --ip 10.0.0.10 --token $(cat ~/homeassistant/secrets.yaml | grep -F roborock_token | awk ' {print $2 }') get_room_mapping

OR use sensor.roborock_current_room attribute "room_number" to get rooms
"""

rooms = {'Dining Room':22,'Kitchen':24,'Living Room':23,'Office':21,'Guest Bedroom':26,'Guest Bathroom':19,'Hallway':16,"Bethany's Office":20,'Master Bedroom':18,'Master Bathroom':27, 'Back Bathroom':17, 'Back Bedroom':25}

segments = []

# Iterate through input_selects and find rooms to clean
for i in range(1,11):
    state = hass.states.get("input_select.vacuum_custom_clean_" + str(i)).state
    if str(state) != "None":
      segments.append(rooms[state])

# Only call the service if at least one room is selected
if len(segments) > 0:
  service_data = {"entity_id": "vacuum.roborock_s4", "segments": segments}
  hass.services.call("xiaomi_miio", "vacuum_clean_segment", service_data, False)
