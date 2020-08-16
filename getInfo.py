import unirest

def getSongInfo():
	response = unirest.get("http://localhost:3000/api/v1/getState")
	title = response.body["title"]
	artist = response.body["artist"]
	return title, artist
