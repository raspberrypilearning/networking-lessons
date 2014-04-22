Dynamic Host Configuration Protocol (DHCP)
==================
This learning resource describes a practical exercise where the Raspberry Pi is used to demonstrate Dynamic Host Configuration Protocol on an isolated network.

![](./images/cover.jpg)

## Introduction

By now it will be clear that repeatedly changing the `/etc/network/interfaces` file is time consuming and laborious. There are a number of disadvantages to all computers on the network having static IP addresses. Consider what would happen when you want to add even more computers to your network.

- Users must manually allocate IP addresses 
- Users must ensure that no two computers have the same address
- It is time consuming to edit the configuration file on every computer
- Poor for mobile devices like laptops which frequently join and leave the network

How can we make this easier?

## Learning Objectives

- Understand what Dynamic Host Configuration Protocol (DHCP) is
- Know the role it plays in the overall structure of a computer network

## Learning Outcomes

### All students are able to:

- Understand the need for DHCP in a computer network
- Use a DHCP server to acquire an IP address for a Raspberry Pi

### Most students are able to:

- Understand the internal logic of a DHCP server

## Lesson Summary

- A discussion of the logical process followed by a DHCP service
- Setting up one Raspberry Pi to be a DHCP server
- Use other Raspberry Pi's to get IP addresses from the server
- Testing the network

## Lesson introduction

Firstly go over the concept of a computer *server*. A server is essentially a computer who's main purpose is to provide a service. A web server, for instance, provides the *service* of transmitting web pages, images and files to you over the Internet. A Minecraft server provides the service of preserving the 3D world, remembering what blocks are where and allowing the players to see each other. **Servers** are computers that are dedicated to a task (but they can be dedicated to more than one).

Wouldn't it be great if we could have a server that would take care of allocating IP addresses on our network and remembering who owns what address?

This is exactly what DHCP is for. It stands for Dynamic Host Configuration Protocol. *Dynamic* meaning to constantly change, *Host* is just another word for a computer, *Configuration* meaning to configure your network settings and *Protocol* meaning a set of rules that define how to do things. D-H-C-P.

## Starter activity

A computing unplugged activity is quite good to get across the logical process followed by the DHCP service.

You wil need:
- A set of cards with a selection of numbers on them
- A piece of paper
- A pen or pencil

Begin by nominating one student to be the DHCP server. They own the set of cards, paper and pen/pencil. The remaining students are now going to be the dynamic hosts (constantly changing computers) on the network.

The DHCP server has a set of rules that must be followed, this is the protocol part of the name. One of the hosts now wants to join the network (who's name is *Dave*). This is how the conversation should go:

- HOST: "Hello I am *Dave*, is there a DHCP server out there?"
- DHCP: "Yes I am here *Dave*. I can offer you address X."
- HOST: "DHCP server, can I take address X please."
- DHCP: "*Dave*, here is address X. You may keep it for 12 hours."
  
The DHCP server hands over an address card to *Dave* and writes his name on the paper along with the address that was given, the time *when* it was given and the length of the lease (12 hours). The time it was given is used to keep track of the age of the lease.

Stop for a moment and consider if there was any part of this conversation that was unexpected?
When a computer joins a network it has no way of knowing if a DHCP server is available - so it sends out a broadcast signal to the whole network asking if one is there. If one *is* available it will reply to the host offering an address. The host then officially requests the address. The part you might not have expected is that the address is given with a lease time, in this case 12 hours. Consider why this might be and continue below.

Now let's suppose *Dave* wants to leave the network or is shutting down.  The conversation would go like this:

- HOST: "DHCP server, I am *Dave* and I and am giving my IP address back to you"
- DHCP: "Thank you *Dave*, goodbye"

*Dave* then hands his address card back to the DHCP server. The DHCP server puts the card back with the others and crosses his name out from the piece of paper. That address card could now be given out to another computer/host that joins the network.

Now consider what might happen if *Dave* didn't shut down cleanly, suppose the power cable was suddenly unplugged and he didn't get a chance to neatly give his address back to the DHCP server, or he decided to just run off with it! What would happen then? The DHCP server won't give out the same address twice so would the address be forever lost in limbo?

This is where the lease time comes in! The address *will* be in limbo but only until the lease time expires. After 12 hours of time goes by this will happen:

- DHCP: *Dave* are you there? The 12 hour lease time on your IP address has expired, do you wish to renew it?
- ...no reply...
- DHCP: I can now safely give that address to another host.

The DHCP server makes a new card with that address on, puts it with the others and crosses *Dave* off the list on the paper.

So that is how this problem is dealt with, all addresses are given out with a time limit attached to them so that in the event of hosts crashing or suddenly leaving the network the DHCP server will slowly repossess those addresses as their lease times expire.

An alternative version of this conversation might be: 

- DHCP: Dave are you there? The 12 hour lease time on your IP address has expired, do you wish to renew it? 
- HOST: Yes I am *Dave* and would like to renew.
- DHCP: *Dave* you may keep the address for another 12 hours.

The DHCP server then updates the time at which the address was given to Dave on the paper. Note that not all DHCP servers will use a 12 hour lease, it can be either longer or shorter depending on the server in question.

## Main practical activity

Firstly select one Raspberry Pi to act as the DHCP server. It can be a good idea to either put a sticker on it or move it to a more prominent place to avoid any confusion later on. We'll need to install some software on this Pi, so for this first part you'll need to connect it to another LAN for Internet access.

**Note:** Because only one Raspberry Pi will be the DHCP server this part of the activity is best carried out by one person with all the other students watching. We do not need more than one DHCP server, in fact more than one can cause problems!

Enter the following commands:

```
sudo apt-get update
sudo apt-get install dnsmasq
```

Once that has finished you can disconnect from the LAN with Internet access and return to the original practice hub/switch.

By convention most DHCP servers have a static IP address which will be the first or lowest number in the IP address space for the network. For example most private networks use a local IP address space of `192.168.0.X` where `X` is a number that is different for each device. Following this convention our DHCP server will have a static IP address of `192.168.0.1`. Note the `.1` at the end. The IP addresses it can serve out will then range from `192.168.0.2`, `.3`, `.4` and so on up to `.254`.

So firstly let’s make the DHCP server Raspberry Pi have a static IP address as per this convention. To configure this we must edit the network interfaces file again. Enter the following command:

`sudo nano /etc/network/interfaces`

In this file `eth0` refers to the Raspberry Pi Ethernet port and `wlan0` refers to a wireless dongle if you are using one. Find the following line:

`iface eth0 inet dhcp`

This line is saying "for the interface `eth0` try to get an IP address from a DHCP server". So essentially this is making it a DHCP *client*, but we want to make this a DHCP *server* so this line must be disabled. Put a hash `#` character at the start of the line and add the following four lines below to configure the static IP address.  Just as you did in previous exercises.

```
# iface eth0 inet dhcp
auto eth0
iface eth0 inet static
address 192.168.0.1
netmask 255.255.255.0
```

Press `Ctrl – O` to save followed by `Ctrl – X` to quit out of nano.  Now enter the following command to restart the networking service on the Raspberry Pi:

`sudo service networking restart`

This Raspberry Pi will now always have the IP address `192.168.0.1`. You can double check this by entering the command `ifconfig`, the IP address should be shown on the second line just after `inet addr`.

Next we need to configure the DHCP server software, **dnsmasq**, that was installed earlier. We are going to explicitly specify a configuration file for the dnsmasq service so let’s first make a backup of the default config file and then save our one in its place. Enter the following commands:

```
cd /etc
sudo mv dnsmasq.conf dnsmasq.default
sudo nano dnsmasq.conf
```

You should now be editing a blank file. Copy and paste the following into it.

```
interface=eth0
dhcp-range=192.168.0.2,192.168.0.254,255.255.255.0,12h
dhcp-option=3,192.168.0.1
```

The first line tells dnsmasq to listen for DHCP requests on the Ethernet port of the Pi. The second line is specifying the range of IP addresses that can be given out, notice the `12h` at the end which specifies the lease time. The third line provides the default gateway setting for the client host computer (which is used for routing).

