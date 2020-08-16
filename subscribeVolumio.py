import unirest

unirest.post("http://localhost:3000/api/v1/pushNotificationUrls", params={"url": "http://localhost:9000"})



