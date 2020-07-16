# MMR - Save your rating history

This was created so I could track my rank in Dota2 and visualise it in Grafana. It takes a screenshot of the stats page, uploads that to [ocr.space](https://ocr.space/) which has a free API.  Afterwards the Dota2 Steam API is queried to save the matchId,duration,heroID and saves it to a SQL database.
This is mostly on here so I don't lose my project, if there is demand I'll upload the table schematics and add more information. 