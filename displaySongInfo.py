from RPLCD.gpio import CharLCD
from RPi import GPIO
import time
from threading import Lock

DISPLAY_LENGTH = 16

class Display:

	def __init__(self):
		self.lcd = CharLCD(cols=16, rows=2, pin_rs=36, pin_e=11, pins_data=[33, 31, 29, 32], numbering_mode=GPIO.BOARD)
		self.lock = Lock()
		self.title = ""
		self.artist = ""

	def _updateDisplay(self):
		with self.lock:
			self.lcd.clear()
			self.lcd.cursor_pos = (0,0)
			if len(self.title) > 16:
				title = self.title[0:16]
			else:
				title = self.title
			if len(self.artist) > 16:
				artist = self.artist[0:16]
			else:
				artist = self.artist
			time.sleep(1)
			self.lcd.write_string(title + "\n\r" + artist)

	def update(self, title, artist):
		assert type(self.title) is str, 'malformed title'
		assert type(self.artist) is str, 'malformed artist'
		updated = False # only refresh screen if state has changed
		if not self.title == title:
			self.title = title
			updated = True
		if not self.artist == artist:
			self.artist = artist
			updated = True
		if updated:
			self._updateDisplay()

	def shutdown(self):
		self.lcd.clear()
		self.lcd.close(clear=True)

if __name__ == '__main__':
	disp = Display()
	disp.displaySongInfo("Darude", "Sandstorm")
	time.sleep(2)
	disp.displaySongInfo("Never Gonna Give You Up", "Rick Astley")
	time.sleep(2)
	disp.shutdown()
