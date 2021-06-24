import mariadb
from os import environ as environment


def insert_mmr_and_general_match_information(data,db):
	connection = mariadb.connect(host=environment['SQL_SERVER'], user=environment['API_INSERT_'], password=environment['API_INSERT_PW'], database=environment['API_INSERT_DB'])
	try:
		print("Connecting to "+db)
		with connection.cursor() as cursor:
			cursor.execute("insert into `mmr`(`mmr`, `matchId`, `heroId`, `win`,`playerRadiant`) values (?,?,?,?,?)",
			               (data['mmr'], data['match_id'], data['player_hero_id'], data['player_has_won'],
			                data['player_radiant']))
			cursor.execute(
				"insert into `matches`(`matchId`, `radiant_win`, `duration`, `date`, `radiant_score`, `dire_score`)"
				" values (?,?,?,FROM_UNIXTIME(?),?,?)", (
					data['match_id'], data['radiant_win'], data['duration'], data['timestamp'], data['radiant_score'],
					data['dire_score']))

		connection.commit()

	except Exception as e:
		print(e)

	finally:
		connection.close()

def lookup_auth_token(token):
	connection = mariadb.connect(host=environment['SQL_SERVER'], user=environment['API_LOOKUP_USER'], password=environment['API_LOOKUP_PW'], database=environment['API_LOOKUP_DB'])
	try:
		with connection.cursor() as cursor:
			sql="SELECT user,db,enabled FROM apiKey where apiKey=?"
			data=(token,)
			cursor.execute(sql,data)
			response=cursor.fetchone()
			if response is None:
				return None, None, None
			return response[0], response[1], response[2]
	except Exception as e:
		print(e)
	finally:
		connection.close()

if __name__ == '__main__':
	print(lookup_auth_token(1234))