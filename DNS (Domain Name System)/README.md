Domain Name System (DNS)
==================

This learning resource describes a practical exercise where the Raspberry Pi is used to demonstrate the Domain Name System (DNS) on an isolated network.

![](./images/cover.jpg)

## Introduction

It is recommended that the previous [DHCP lesson](../DHCP%20(Dynamic%20Host%20Configuration%20Protocol)/) has been completed by all students before attempting this. It is important to complete them in this order because understanding DNS requires the understanding of its relationship to DHCP. Please note that DNS is a fairly complex subject and this resource is only an introduction to the concepts. It is not intended to be a comprehensive guide. Distributed DNS is not covered but will be touched on.

You may have noticed that it can be a bit tricky to remember IP addresses. They are comprised of four 8-bit numbers separated by dots. For example: `192.168.0.146`. Human beings often find it difficult to remember a sequence of numbers like this and find it a lot easier to remember a word or a name instead.

When we want to access resources on our network such as a web server we currently have to remember the IP address. How can we make it easier for people to connect to network servers without having to remember the IP address numbers?

## Learning Objectives

- Understand what the Domain Name System (DNS) is
- Know the role it plays in the overall structure of a computer network and the Internet

## Learning Outcomes

### All students are able to:

- Understand the need for DNS in a computer network and the Internet
- Use DNS server to connect to a network resource/server

### Most students are able to:

- Understand the internal logic of a DNS server
- Understand the relationship of DNS to DHCP

## Lesson Summary

- A discussion of the logical process followed by a DNS service
- Setting up one Raspberry Pi to be a DNS server
- Use other Raspberry Pi's to perform DNS queries
- Testing the network

## Resources

For the majority of the lesson, it is suggested that work is carried out by students in pairs. The Ethernet hub or switch should remain completely isolated without any Ethernet cables connecting it into the main school network.

- The DHCP server Raspberry Pi from the previous lesson;
- One or more Raspberry Pis with a [web server](https://github.com/raspberrypi/documentation/blob/master/remote-access/web-server/apache.md) running (optional); 
- A Raspberry Pi per pair of students;
- An Ethernet cable per pair;
- NOOBS SD card with Raspbian installed per pair;
- A keyboard and mouse connected to the RPi per pair;
- A monitor connected to the RPi per pair;
- An Ethernet hub or switch with enough ports to connect all the RPis;
- A set of cards with a selection of numbers on them (starter activity)
- A piece of paper and a pen or pencil (starter activity)

## Lesson introduction

Computer networks can grow very large. The Internet is the largest network of computers in the world. It's so big in fact that the number of computers on the Internet is impossible to know. Imagine how difficult it would be if we needed to remember the IP address for every web server we wanted to visit?

This is what a DNS server is for. It stands for Domain Name System. It's primary function is to provide the service of translating easily memorable domain or host names (like google.com or raspberrypi.org) into IP addresses (and vice versa). So it's a bit like a telephone directory where you can look up a phone number that you need.

When you type an address into your browser your computer has to contact a DNS server to ask for the IP address that corresponds to it. The DNS server searches its database for the name, finds the corresponding IP address and then returns it to the client. This process is called a *DNS query*.

The client then communicates directly with the server using the IP address returned by the DNS query.

## Starter activity

A computing unplugged activity is quite good to get across the logical process followed by the DNS service.

Begin by nominating one student to be the DNS server. Give each remaining student a number card. The DNS server should write down the names of all the students along with their number. This list represents the database of names held by the DNS service.

Suppose, for the sake of argument, that all the remaining students are web servers hosting a website. One of the students now wants to type `http://dave` into their web browser. This is how the DNS query would happen:

- HOST: "Hello DNS server, can you give me an IP address for the name 'dave' please?"
- DNS: "I have 'dave' down as 201.72.165.69"
- HOST: "Hello 201.72.165.69, please give me your home page."
- 201.72.165.69: "Here is my home page."

That seems pretty simple doesn't it? Now consider this scenario. Nominate one more student to also be a DNS server and give them responsibility for half of the list of names. This is also how the DNS query could go:

- HOST: "Hello DNS server, can you give me an IP address for the name 'dave' please?"
- DNS1: "I don't seem to have 'dave', hold on a minute!"
- DNS1: "DNS2, do you have an IP address for the name 'dave' please?"
- DNS2: "DNS1, I have 'dave' down as 201.72.165.69"
- DNS1: "HOST, I have found 'dave' to be 201.72.165.69"
- HOST: "Hello 201.72.165.69, please give me your home page."
- 201.72.165.69: "Here is my home page."

So in this scenario the first DNS server didn't have 'dave' in its database but it passed on the query to a second DNS server that did. This is what is known as an *iterative DNS query*. The second DNS server responded to the first and the first responed to the original host/client with the IP address information. So the answer was fed back along the chain, so to speak.

Consider how something like this might work on the Internet. Real Internet DNS distributes the responsibility of remembering what name is for an IP address to a network of many DNS servers around the world.

What actually happens is that there are DNS servers dedicated to different domain name levels. For example there will be one for `.com`, another for `.org` and another for `.co.uk`. So when you type in an address like `raspberrypi.org` the query will pass through several DNS servers before the answer gets back to you.

Once an iterative DNS query has been resolved the first DNS server will cache the result, that is to remember it for later. That way if the same name is asked for again it already has the answer and can rapidly respond without having to consult other DNS servers.

### What about DHCP?

Before finishing off consider what might happen if we brought back the DHCP server from the previous lesson. When using DHCP it is possible for the IP address of a computer to change. When a host shuts down and releases its IP address back to the DHCP server that address could then be given out to another host which is joining the network. That might then lead to a situation where the DNS name no longer matches the right IP address!

Consider what can be done to resolve this problem.

## Main practical activity

This requires the use of the DHCP server Raspberry Pi from the previous lesson. The software we're going to use is the same **dnsmasq** service from the that lesson, so we don't need to install anything else this time.  Ensure that this Pi is easily distinguishable from the others.

If you have a web server available first do a quick exercise where the students load the home page in a browser using the IP address only. Firstly load the Raspberry Pi desktop with the `startx` command, open the Midori browser and enter the IP address of the web server into the address bar.

If you need to find out the IP address of the web server you can use the `ifconfig` command on the web server Pi itself. The address will be under `eth0` on the second line after `inet addr`. Everyone should be able to load the page correctly.

### On the server Pi only

**Note:** Because only one Raspberry Pi will be the DNS server this part of the activity is best carried out by one person with all the other students observing.

The dnsmasq program can actually provide both DHCP and DNS services. So all we need to do now is configure it. Enter the following command to edit the dnsmasq configuration file:

`sudo nano /etc/dnsmasq.conf`

DNS doesn't have a broadcast system for finding it like DHCP does so the clients/hosts need to be told the DNS server IP address. An easy solution is to make the DHCP server pass this information to the hosts at the same time as their IP address.

Because both DNS and DHCP services are going to be provided by the same Pi the DNS IP address will be the static IP that was given to the server Raspberry Pi in the previous lesson. Add the line below to the end of the file:

```
dhcp-option=6,192.168.0.1
```

Next we need to specify where the look up database for DNS queries is. Often this is quite a serious database platform but for this exercise we're just going to use a simple text file to demonstrate the concept.

Now append these two lines:

```
no-hosts
addn-hosts=/etc/hosts.dnsmasq
```

The `no-hosts` line is telling dnsmasq to ignore the default system `/etc/hosts` file for DNS queries. The next line is specifying the file `/etc/hosts.dnsmasq` as the look up file for DNS queries (we will create this in a moment).

So to double check everything, this is how `dnsmasq.conf` should look now:

```
interface=eth0
dhcp-range=192.168.0.2,192.168.0.254,255.255.255.0,12h
dhcp-option=6,192.168.0.1
no-hosts
addn-hosts=/etc/hosts.dnsmasq
```

Press `Ctrl – O, Enter` to save followed by `Ctrl – X` to quit out of nano.

Next we need to create our lookup table for host names. Enter the following command:

`sudo nano /etc/hosts.dnsmasq`

You should now be editing a blank file. There is an expected format that must be followed here. The format is `IP<tab>hostname`, note the use of the tab keyboard key.

Enter the following line for example (this will give our server the DNS name of *serverpi*):

```
192.160.0.1    serverpi
```

Press `Ctrl – O, Enter` to save followed by `Ctrl – X` to quit out of nano. Before we reactivate the DNS/DHCP server make sure the server Pi is the only device connected to the practise hub/switch. Unplug all other Ethernet connections. Enter the following command to restart the dnsmasq service:

`sudo service dnsmasq restart`

The server is now active and listening for requests from client host computers.

There is one more thing we need to do. Because our server is set up with a static IP address the DHCP server will never actually tell *itself* to use its own DNS server. So there is one more file we need to change to make that work.

`sudo nano /etc/resolv.conf`

This file should have the following line only:

```
nameserver 127.0.0.1
```

You could also use 192.168.0.1 here instead but 127.0.0.1 is a generic way to reference the local computer regardless of what its IP address is. So if we changed the static IP to something else we wouldn't need to come and edit `resolv.conf` again.

Press `Ctrl – O, Enter` to save followed by `Ctrl – X` to quit out of nano. Now enter the following command to restart the networking service:

`sudo service networking restart`

### On all the remaining client Pi's

Before reconnecting any remaining client Pi’s to the hub/switch check that their `/etc/network/interfaces` files are configured to get an IP address from a DHCP server. They should still be configured this way from the previous lesson.

You can now go ahead and start reconnecting them to the hub/switch. They should immediately acquire an IP address from the DHCP server. Check this by using the command `ifconfig` again, the IP addresses given out should be randomly selected from the range specified on the server.

You should find that everyone can enter the command `ping serverpi` and get a response from the IP address.

### One step further: the web server!

Assuming you're using one or more Raspberry Pi [web servers](https://github.com/raspberrypi/documentation/blob/master/remote-access/web-server/apache.md) it would be great to get to point of typing a name into a browser and seeing a home page load. This is the next task!

Before we change anything we need to consider the problem of DHCP IP address allocations changing and becoming out of sync with the DNS server look up table. This was touched on in the starter activity.

There is a convention in networking where server computers (as in providing some kind of service) have static IP addresses. That way the IP address can be entered into the DNS look up database without worrying about it changing at some point in the future.

We need to be careful here! If we just manually assign a static IP address there is a possibility that the DHCP server could hand that same IP address out to another computer joining the network. To avoid that we can change the *range* of IP addresses the DHCP server will give out. If we start the DHCP range at a higher number we can leave ourselves a block of non DHCP IP addresses that we can be free to assign as static addresses for servers.

### Back on the server Pi again

Enter the following command to edit the dnsmasq configuration file:

`sudo nano /etc/dnsmasq.conf`

You'll see the `dhcp-range` line shows the first IP address, currently 192.168.0.2, followed by the last one, currently 192.168.0.254. Change the first IP address to be *.51* so that we can have the lower 50 IP addresses to use for static IP.

The line should now look like this:

```
dhcp-range=192.168.0.51,192.168.0.254,255.255.255.0,12h
```

## Plenary

## Homework
