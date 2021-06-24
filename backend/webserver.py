from flask import Flask, Response, request
from sqlHandler import lookup_auth_token,insert_mmr_and_general_match_information
app = Flask(__name__)

@app.route("/", methods=["Post"])
def payload():

	if not request.headers.get('X-Auth-Token') or request.headers['X-Auth-Token'] is None:
		print("Missing access token")
		return Response(response="Access denied", status=403)
	user,db,enabled=lookup_auth_token(request.headers['X-Auth-Token'])
	if not user:
		print("Received invalid access token")
		print(request.headers['X-Auth-Token'])
		return Response(response="Access denied", status=403)
	print("Received a request from "+user)
	if not enabled:
		print("Received expired access token")
		print(request.headers['X-Auth-Token'])
		return Response(response="Access denied", status=403)
	data = request.json
	if not all(isinstance(i, int) for i in
	       [data['mmr'], data['match_id'], data['timestamp'], data['player_hero_id'], data['duration']]) and not isinstance(
		data['player_has_won'], bool):
		print("Missing data")
		print(data)
		return Response(response="Missing or faulty data", status=403)
	insert_mmr_and_general_match_information(data, db)
	return Response(response="OK", status=200)