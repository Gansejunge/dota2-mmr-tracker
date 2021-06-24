from requests import request
import api_call
import screenshot
from os import environ as environment

def get_match_data():
	headers = {'X-Auth-Token': environment['AUTH_TOKEN']}
	data = api_call.get_match_information(None)
	data['mmr'] = screenshot.process_screenshot()
	print("API calls successful")
	print("Image recognition successful, got " + str(data['mmr']) + " mmr")
	if all(isinstance(i, int) for i in
	       [data['mmr'], data['match_id'], data['timestamp'], data['player_hero_id'], data['duration']]) and isinstance(
		data['player_has_won'], bool):
		response = request("POST", 'https://dota2.gansejunge.com/trackMMR', data=data, headers=headers)

if __name__ == '__main__':
	get_match_data()