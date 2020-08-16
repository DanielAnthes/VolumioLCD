from flask import Flask, request
import json
from displaySongInfo import Display
import unirest
from signal import signal, SIGINT


app = Flask(__name__)
disp = Display()
unirest.post("http://localhost:3000/api/v1/pushNotificationUrls", params={"url": "http://localhost:9000"}) # make sure flask server receives updates from volumio

@app.route('/', methods=['POST'])
def home():
	try:
		data = request.data
		data_dict = json.loads(data)
		data_dict = data_dict['data']
		disp.update(str(data_dict['title']), str(data_dict['artist']))
	except:
		pass
	return ""

def interrupt_handler(signal_received, frame):
	disp.shutdown()
	print("quitting")
	exit(0)

signal(SIGINT, interrupt_handler) # make sure display is reset on interrupt
app.run(debug=False, port=9000)
