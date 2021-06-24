import urllib.request
import urllib.parse
import json
from os import environ as environment


def open_url_and_return_json(url):
	f = urllib.request.urlopen(url)
	jsoned = json.loads(f.read().decode('utf-8'))
	return jsoned


def get_match_information(match_id):#If I ever forget to run this script after a match I can manually enter a id and save it anyway
	print("Getting last match id")
	if not match_id:
		general_information = open_url_and_return_json("https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/"
		                                               "V001/?account_id=" + environment['STEAM_ACCOUNT_ID'] + "&key=" + environment['STEAM_API_KEY'] + "&matches_requested=1")
		match_id = general_information['result']['matches'][0]['match_id']

	hero_ids = []
	match_information = open_url_and_return_json("https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?"
	                                             "match_id=" + str(match_id) + "&key=" + environment['STEAM_API_KEY'])
	player_radiant = True
	for entry in match_information['result']['players']:
		if entry['account_id'] == int(environment['STEAM_ACCOUNT_ID']):
			player_hero_id = entry['hero_id']
			if entry['player_slot'] > 4:
				player_radiant = False

	radiant_win = match_information['result']['radiant_win']
	player_has_won = False
	if player_radiant and radiant_win or not player_radiant and not radiant_win:
		player_has_won = True

	duration = match_information['result']['duration']
	start_time = match_information['result']['start_time']
	radiant_score = match_information['result']['radiant_score']
	dire_score = match_information['result']['dire_score']

	return {'match_id': match_id, 'radiant_win': radiant_win, 'duration': duration,
	        'timestamp': start_time, 'radiant_score': radiant_score, 'dire_score': dire_score,
	        'player_hero_id': player_hero_id
		, 'player_has_won': player_has_won, 'player_radiant': player_radiant}


if __name__ == "__main__":
	print(get_match_information(5450379063))
