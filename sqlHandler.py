import mariadb

from config import SQL_DATABASE_IP,SQL_USER,SQL_PASSWORD,SQL_DATABASE_NAME

def insert_mmr_and_general_match_information(data):
	connection = mariadb.connect(host=SQL_DATABASE_IP, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE_NAME)
	try:
		print("Connecting to DB")
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


def insert_hero_id_for_specific_match(match_id, heroId, hero_radiant):
	connection = mariadb.connect(host=SQL_DATABASE_IP, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE_NAME)
	try:
		with connection.cursor() as cursor:
			cursor.execute("insert into `matchesHeroes`(`matchId`,`heroId`, `heroRadiant`)"
			               " values (?,?,?)", (match_id, heroId, hero_radiant))
		connection.commit()

	except Exception as e:
		print(e)

	finally:
		connection.close()
