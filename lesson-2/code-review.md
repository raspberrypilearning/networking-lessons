# Code review

Rearrange the blocks of Python code below in the correct order. It's similar to part of the the chat program that you wrote in Lesson 1. The lines beginning with a hash (`#`) are comments to help understand what each code block does.

----------
```python
#decide if the Raspberry Pi will be a server (no IP address given) or a client
    if (len(sys.argv) >= 2):
      network.call(sys.argv[1], whenHearCall=heard)
    else:  
      network.wait(whenHearCall=heard)
```

----------
```python
#a function that prints a message
def heard(phrase):
  print("them:" + phrase)
```

----------

```python
#The main part of the program - send a message
while network.isConnected():
  #phrase = raw_input() #python2
  phrase = input() # python3
  print("me:" + phrase)
  network.say(phrase)
 ```

----------

```python
#import modules so that you can use functions from other programs
import network
import sys
```

----------
