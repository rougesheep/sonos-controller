#!/usr/bin/env python
import soco
import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler

PORT = 8000
ROOM = 'Bedroom'

def play(sonos):
	for device in soco.discover():
		if device.player_name == sonos:
			device.partymode()
			device.play()

def pause(sonos):
	for device in soco.discover():
		if device.player_name == sonos:
			device.partymode()
			device.pause()

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(s):
		request = False
		if s.path == '/play':
			request = 'PLAY'
			play(ROOM)
		elif s.path == '/pause':
			request = 'PAUSE'
			pause(ROOM)

		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		s.wfile.write("<html><head><title>Sonos Controller</title></head>")
		s.wfile.write("<body><h1>Sonos Controller</h1>")
		s.wfile.write("<p>")
		if request:
			s.wfile.write("%s on room %s" % (request, ROOM))
		else:
			s.wfile.write("Call either /play or /pause")
		s.wfile.write("</p>")
		s.wfile.write("</body></html>")

print "Start Server on Port %s" % PORT
httpd = SocketServer.TCPServer(("", PORT), MyHandler)
try:
	httpd.serve_forever()
except KeyboardInterrupt:
	pass
httpd.server_close()
print "Server Stopped"
