# network.py  2013 @whaleygeek

try:
  import thread
except ImportError:
  import _thread as thread #python3
  
import socket
import time


# CONFIGURATION ################################################################

SERVER_HOST     = "0.0.0.0"
PORT            = 8888
BUFFER_SIZE     = 1024

def trace(msg):
  pass # print("network:" + msg)

  
# MULTI-INSTANCED INTERFACE ####################################################
#
# This is a class based interface, where you can have multiple instances
# of open sockets, either or both of server and client sockets.
    
class Connection():
  def defaultWhenHungupHandler(self):
    print("CONNECTION LOST")
    self.connected = False

  port              = PORT        # default, overridable
  interface         = SERVER_HOST # default, not yet overridable
  whenHungupHandler = defaultWhenHungupHandler # default, overridable
  connected         = False       # TODO 'state'

  myHandle          = None
  peerHandle        = None
  threadHandle      = None
  startOfPacket     = None
  endOfPacket       = None

    
  def trace(self, msg):
    trace(msg)
  
  
  def whenHungUp(self, thenCallFunction):
    if thenCallFunction == None:
      self.whenHungupHandler = self.defaultWhenHungupHandler
    else:
      self.whenHungupHandler = thenCallFunction
    
    
  # client calling server
  def call(self, addr, whenHearCall, port=None):
    self.trace("call:" + addr)
    if (port != None):
      self.port = port
    else:
      self.port = PORT
      
    self.peerHandle = _clientOpen(addr, self.port)
    self.connected = True
    self.threadHandle = _startListenerThread(self.peerHandle, addr, whenHearCall, self.whenHungupHandler, self.endOfPacket)   
  
  
  # server waiting for client
  def wait(self, whenHearCall, port=None):
    self.trace("wait")
    if (port != None):
      self.port = port
    else:
      self.port = PORT
    
    # blocking wait
    self.myHandle = _serverWait(self.interface, self.port)
    self.peerHandle, addr = _serverAccept(self.myHandle)
    self.connected = True
    self.threadHandle = _startListenerThread(self.peerHandle, addr, whenHearCall, self.whenHungupHandler, self.endOfPacket)
     
      
  def isConnected(self):
    self.trace("isConnected:" + str(self.connected))
    return self.connected
  
  
  def say(self, data):
    self.trace("say:" + data)
    if (self.peerHandle == None):
      self.trace("say called hangup")
      self.hangUp()
    else:
      if (self.startOfPacket != None):
        data = self.startOfPacket + data
        
      if (self.endOfPacket != None):
        data = data + self.endOfPacket

      _send(self.peerHandle, data)        
  
  
  def hangUp(self):
    self.trace("hangup")
    self.whenHungupHandler()
    self.connected = False
    
    if (self.threadHandle != None):
      _stopListenerThread(self.threadHandle)
      self.threadHandle = None

    if (self.peerHandle != None):
      _close(self.peerHandle)
      self.peerHandle = None
    if (self.myHandle != None):
      _close(self.myHandle)
      self.myHandle = None
      

class TextConnection(Connection):
  def __init__(self):
    self.endOfPacket = "\r\n"
  

class BinaryConnection(Connection):
  def __init__(self):
    self.endOfPacket = None
      
      
# BINDING TO THREADING API ######################################################      
# intentionally static (non class instanced)

def _startListenerThread(handle, addr, whenHearFn, hangUpFn, packetiser):
  return thread.start_new_thread(_listenerThreadBody, (handle, addr, whenHearFn, hangUpFn, packetiser))


def _stopListenerThread(threadHandle):
  trace("_stopListenerThread")
  #TODO tell threadHandle to stop
  pass


def _listenerThreadBody(handle, addr, whenHearFn, hangUpFn=None, packetiser=None):
  trace("_listenerThreadBody:" + str(addr))
  buffer = ""

  while True:
    try:
      data = _receive(handle, hangUpFn)
      if (data == None or len(data) == 0):
        trace("threadbody none or 0-data, called hangup")
        if hangUpFn != None:
          hangUpFn()
        return
    except:
      trace("threadBody exception hangup")
      if hangUpFn != None:
        hangUpFn()
      return  

    # TODO use packetiser to do this if present
    # but need a way to manage buffer state (by-val or by-ref)
    data = data.decode('utf-8') #python3    
    if (packetiser == None):
      if (whenHearFn != None):
        whenHearFn(data)
    else:
      for ch in data:
        if (ch == "\r"):
          pass # strip it

        elif (ch != "\n"):
          buffer += ch # buffer it

        else:
          #TODO if user code throws exception, don't want to hangup
          if (whenHearFn != None):
            whenHearFn(buffer) # process a line of data
          buffer=""

      
# BINDING TO LOWER LEVEL SOCKETS API ###########################################
# intentionally static (non class instanced)
  
def _clientOpen(addr, port):
  trace("open:" + addr)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((addr, port))
  return s  


def _serverWait(addr, port):
  trace("wait connection")
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((addr, port))
  s.listen(1)
  return s
  
  
def _serverAccept(handle):
  trace("accept")
  handle2, addr = handle.accept()
  trace("Connected by:"+ str(addr))
  return handle2, addr


def _close(handle):
  trace("close")
  handle.close()  


def _send(handle, data):
  trace("send:" + data)
  data = data.encode('utf-8') #python3  
  handle.sendall(data)


def _receive(handle, hangUpFn=None):
  trace("receive")
  try:
    data = handle.recv(BUFFER_SIZE)
    if (data == None):
      trace("receive data none hangup")
      if (hangUpFn != None):
        hangUpFn()
  except:
    if (hangUpFn != None):
      hangUpFn()
      return None
  return data
  
  
# SINGLE-INSTANCED MODULE LEVEL INTERFACE ######################################
#
# This is the interface aimed at kids, so they can avoid classes and objects.
# It is single instanced, but works very well.


conn = TextConnection()
  
def whenHungUp(thenCallFunction):
  conn.whenHungUp(thenCallFunction)
   
def call(addr, whenHearCall=None, port=None):
  conn.call(addr, whenHearCall, port=port)
  
def wait(whenHearCall, port=None):
  conn.wait(whenHearCall, port)   
      
def isConnected():
  return conn.isConnected()
  
def say(data):
  conn.say(data)
  
def hangUp():
  conn.hangUp()
  
# END

