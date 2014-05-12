import RPi.GPIO as GPIO
import time
import sys
import network

SERVER_IP = sys.argv[1]

LED = 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
gotResponse = False

def heard(phrase):
  global gotResponse
  print "heard:" + phrase

  for a in phrase:
    if a == "\r" or a == "\n":
      pass # skip it
    elif a == "0":
      GPIO.output(LED, False)
    else:
      GPIO.output(LED, True)
  gotResponse = True

while True:
  while True:
    try:
      print "connecting to switch server"
      network.call(SERVER_IP, whenHearCall=heard)
      break
    except:
      print "refused"
      time.sleep(1)

  print "connected"

  while network.isConnected():
    gotResponse = False
    print "polling"
    network.say("?")

    while network.isConnected() and not gotResponse:
      print "waiting"  
      time.sleep(1)

  print "connection closed"