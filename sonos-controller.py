#!/usr/bin/env python
import soco
from time import sleep

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

play(ROOM)
sleep(3)
pause(ROOM)