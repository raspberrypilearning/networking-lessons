# Setting up a chat network on two Raspberry Pis

## Student worksheet

In this lesson, you will set up two Raspberry Pis to form a network, and use Python code to send messages between them. There are two steps to this: configuring the network and writing the program.

## Network configuration

Before the Raspberry Pis can communicate, they need to be connected together via a network. Normally, when a device connects to a network, it is assigned a unique identifier called an IP address. As we only have two Raspberry Pis, we have to give each Pi its own IP address.

1. Follow the [static IP address setup guide](../rpi-static-ip-address.md) to configure the IP address.

1. Repeat this procedure with your other Raspberry Pi, giving this one the IP address `192.168.0.3`.

**Tip:** Use a Post-it note to physically label the Raspberry Pis with their IP addresses, otherwise things will get confusing later!

### Testing your network

1. Connect the two Raspberry Pis with an Ethernet cable
1. On the Raspberry Pi that has the IP address ending `.2`, open a terminal from the **Accessories** menu folder
1. In the terminal window which opens type:

    ```bash
    ping 192.168.0.3 -c5
    ```

You should see something like this:

```
PING 192.168.0.3 (192.168.0.3) 56(84) bytes of data.
64 bytes from 192.168.0.3: icmp_req=1 ttl=128 time=3.46 ms
[...four more PINGs ...]

--- 192.168.0.3 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4007ms
rtt min/avg/max/mdev = 3.466/3.788/4.380/0.322 ms
```

If not, check your edits and the network cable. Once the Raspberry Pis are successfully networked, you are ready to write the chat program.

## Setting up the chat program

1. Open a terminal from the **Accessories** menu folder 
1. Create a new file with the nano editor by typing `nano chat.py`.
1. Type in the following program:

**Tip:** The nano text editor does not auto-indent your code in the same way as the IDLE editor. You will need to put the indents in manually. Choose a number of spaces for your indents, or use the tab key.

    ```python
    # A simple internet-chat application

    import network
    import sys

    def heard(phrase):
      print("them:" + phrase)

    if (len(sys.argv) >= 2):
      network.call(sys.argv[1], whenHearCall=heard)
    else:  
      network.wait(whenHearCall=heard)

    while network.isConnected():
      #phrase = raw_input() #python2
      phrase = input() # python3
      print("me:" + phrase)
      network.say(phrase)
    ```

1. Save the file with `ctrl + o` and then press `enter`, then exit nano with `ctrl + x`.

1. Set the first Raspberry Pi up as a **server** by typing:

    ```bash
    python3 chat.py
    ```
    into your terminal window.

1. The second Raspberry Pi will be the **client**. You need to tell it the IP address of the server that you want to connect to. For example, to connect to a Raspberry Pi that has the IP address ending in `.2.`, type:

    ```bash
    python3 chat.py 192.168.0.2
    ```
    into your terminal window.

1. You should now be able to type messages on either Raspberry Pi, and they will appear on the other screen when you press the `enter` key.

Try it! Send messages from the server to the client and vice versa.

### Things to think about when sending messages:

- What is happening on the screen?
- What is physically happening to the messages when you press the `enter` key?
- How do the messages know where to go?

### Things to try:

- Can you break the program by sending messages too fast, or at the same time?
- What happens if you stop the server program by pressing `ctrl + c`?
- Edit `chat.py` to change the 'me:' and 'them:' messages that appear to your own names.

## What next? 

- Display a welcome message when your program starts.
- Display a welcome message for your caller when they connect.
- Display an increasing message counter for 'me:' and 'them:' on each message.
- When you type in a certain letter or word, get the program to expand this to a whole sentence that is sent to your caller.
- When the word "random" is typed, send one of a number of different random messages to your caller.
- When certain words are received from your caller, automatically send a whole phrase back to them, with different phrases for different words.
- If the teacher asks you to, change the network configuration back to a dynamic IP address as shown in the "Clean up" section of [static IP address setup guide](../rpi-static-ip-address.md).
