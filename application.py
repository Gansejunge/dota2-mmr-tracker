import api_call
import sqlHandler
import screenshot

data = api_call.get_match_information(None)
data['mmr'] = screenshot.process_screenshot()
print("API calls successful")
# data['mmr'] = 5120
print("Image recognition successful, got " + str(data['mmr']) + " mmr")
if all(isinstance(i, int) for i in
       [data['mmr'], data['match_id'], data['timestamp'], data['player_hero_id'], data['duration']]) and isinstance(
		data['player_has_won'], bool):
	sqlHandler.insert_mmr_and_general_match_information(data)
	for num, heroId in enumerate(data['hero_ids']):
		hero_radiant = True
		if num > 4:
			hero_radiant = False
		sqlHandler.insert_hero_id_for_specific_match(data['match_id'], heroId, hero_radiant)
	print("Done")
else:
	print("Error")
