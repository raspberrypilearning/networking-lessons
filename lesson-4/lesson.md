# Lesson 4 - Domain Name System (DNS)

In this lesson, the students will use the Raspberry Pi to learn about the Domain Name System (DNS) on an isolated network.

## Introduction

It is recommended that all students complete the previous DHCP lesson before attempting this. It is important to complete the lessons in this order because understanding DNS requires the understanding of its relationship to DHCP. Please note that DNS is a fairly complex subject and this resource is only an introduction to the concept. It is not intended to be a comprehensive guide. Distributed DNS is not covered in detail but it will be briefly discussed.

For the majority of the lesson, it is suggested that work is carried out by students in pairs. The Ethernet hub or switch should remain completely isolated, without any Ethernet cables connecting it into the main school network.

## Learning objectives

- Understand what the Domain Name System (DNS) is
- Know the role it plays in the overall structure of a computer network and the internet

## Learning outcomes

### All students are able to:

- Understand the need for DNS in a computer network and the Internet
- Use a DNS server to connect to a network resource/server

### Most students are able to:

- Understand the internal logic of a DNS server
- Understand the relationship of DNS to DHCP

## Lesson summary

- A discussion of the logical process followed by a DNS service
- Setting up one Raspberry Pi to be a DNS server
- Use other Raspberry Pis to perform DNS queries
- Testing the network

## Lesson introduction

Computer networks can grow to be very large. The internet is the largest network of computers in the world. It's so big, in fact, that the number of computers on the internet is impossible to know. Imagine how difficult it would be if we needed to remember the IP address for every web server we wanted to visit? Additionally, you may have noticed that it can be a bit tricky to remember IP addresses. They are comprised of four 8-bit numbers separated by dots; for example, `192.168.0.146`. Human beings often find it difficult to remember a sequence of numbers like this.

How can we make it easier for people to connect to network servers without having to remember the IP address numbers?

This is what a Domain Name System (DNS) server is for. Its primary function is to provide the service of translating easily memorable domain or host names (like google.com or raspberrypi.org) into IP addresses and vice versa.

When you type an address into your browser your computer has to contact a DNS server to ask for the IP address that corresponds to it. The DNS server searches its database for the name, finds the corresponding IP address and then returns it to the client. This process is called a **DNS query**.

The client then communicates directly with the server using the IP address returned by the DNS query.

## Starter activity

A computing unplugged activity is quite good to get across the logical process followed by the DNS service.

Begin by nominating one student to be the DNS server. Give each remaining student a number card. The DNS server should write down the names of all the students along with their number. This list represents the database of names held by the DNS service.

Suppose, for the sake of argument, that all the remaining students are web servers hosting a website. One of the students now wants to type `http://dave` into their web browser. This is how the DNS query would proceed:

- HOST: "Hello DNS server, can you give me an IP address for the name 'dave' please?"
- DNS: "I have 'dave' down as `201.72.165.69`"
- HOST: "Hello `201.72.165.69`, please give me your home page."
- `201.72.165.69`: "Here is my home page."

That seems pretty simple, doesn't it? Now consider this scenario. Nominate one more student to also be a DNS server and give them responsibility for half of the list of names. This is also how the DNS query could proceed:

- HOST: "Hello DNS server, can you give me an IP address for the name 'dave' please?"
- DNS1: "I don't seem to have 'dave', hold on a minute!"
- DNS1: "DNS2, do you have an IP address for the name 'dave' please?"
- DNS2: "DNS1, I have 'dave' down as `201.72.165.69`"
- DNS1: "HOST, I have found 'dave' to be `201.72.165.69`"
- HOST: "Hello `201.72.165.69`, please give me your home page."
- `201.72.165.69`: "Here is my home page."

So in this scenario the first DNS server didn't have 'dave' in its database, but it passed on the query to a second DNS server that did. This is what is known as an **iterative DNS query**. The second DNS server responded to the first and the first responded to the original host/client with the IP address information. The answer was fed back along the chain, so to speak.

Consider how something like this might work on the internet. Real internet DNS distributes the responsibility of remembering what name corresponds to an IP address to a network of many DNS servers around the world.

What actually happens is that there are DNS servers dedicated to different domain name levels. For example, there will be one for `.com`, another for `.org`, and another for `.co.uk`. So when you type in an address like `raspberrypi.org` the query will pass through several DNS servers before the answer gets back to you.

Once an iterative DNS query has been resolved, the first DNS server will cache the result to remember it for later. That way, if the same name is asked for again it already has the answer and can rapidly respond without having to consult other DNS servers.

### What about DHCP?

Before finishing off consider what might happen if we brought back the DHCP server from the previous lesson. When using DHCP, it is possible for the IP address of a computer to change. When a host shuts down and releases its IP address back to the DHCP server, that address could then be given out to another host joining the network. That might then lead to a situation where the DNS name no longer matches the right IP address!

Consider what can be done to solve this problem.

## Main practical activity

This requires the use of the DHCP server Raspberry Pi from the previous lesson. The software we're going to use is the same `dnsmasq` service from that lesson, so we don't need to install anything else this time. Ensure that this Pi is easily distinguishable from the others.

If you have a web server available, first do a quick exercise where the students load the home page in a browser using the IP address only. Open the Chromium browser and enter the IP address of the web server prefixed with `http://` into the address bar.

If you need to find out the IP address of the web server you can use the `ifconfig` command on the web server Pi itself. The address will be under `eth0` on the second line after `inet addr`. Everyone should be able to load the page correctly.

### On the server Pi only

**Note:** Because only one Raspberry Pi will be the DNS server, this part of the activity is best carried out by one person with all the other students observing.

The `dnsmasq` program can actually provide both DHCP and DNS services, so all we need to do now is configure it. Enter the following command into a terminal (under the Accessories sub-menu) to edit the `dnsmasq` configuration file:

```bash
sudo nano /etc/dnsmasq.conf
```

DNS doesn't have a broadcast system for locating it as DHCP does, so the clients/hosts need to be told the DNS server IP address. An easy solution is to make the DHCP server pass this information to the hosts at the same time as their IP address.

Because both DNS and DHCP services are going to be provided by the same Pi, the DNS IP address will be the static IP that was given to the server Raspberry Pi in the previous lesson. Add the line below to the end of the file:

```
dhcp-option=6,192.168.0.1
```

Next we need to specify where the lookup database for DNS queries is located. Often this is quite a serious database platform, but for this exercise we're just going to use a simple text file to demonstrate the concept.

Add these two lines to the configuration file:

```
no-hosts
addn-hosts=/etc/hosts.dnsmasq
```

The `no-hosts` line is telling `dnsmasq` to ignore the default system `/etc/hosts` file for DNS queries. The next line is specifying the file `/etc/hosts.dnsmasq` as the lookup file for DNS queries (we will create this in a moment).

So to double-check everything, this is how `dnsmasq.conf` should look now:

```
interface=eth0
dhcp-range=192.168.0.2,192.168.0.254,255.255.255.0,12h
dhcp-option=6,192.168.0.1
no-hosts
addn-hosts=/etc/hosts.dnsmasq
```

Press `Ctrl + o` then `Enter` to save, followed by `Ctrl + x` to quit nano.

Next we need to create our lookup table for host names. Enter the following command into your terminal window:

```bash
sudo nano /etc/hosts.dnsmasq
```

You should now be editing a blank file. There is an expected format that must be followed here. The format is `IP<tab>hostname`; note the use of the tab keyboard key.

Enter the following line for example (this will give our server the DNS name of **serverpi**):

```
192.168.0.1    serverpi
```

Press `Ctrl + o` then `Enter` to save followed by `Ctrl + x` to quit nano. Before we reactivate the DNS/DHCP server, make sure the server Pi is the only device connected to the practise hub/switch; unplug all other Ethernet connections. Enter the following command to restart the `dnsmasq` service:

```bash
sudo service dnsmasq restart
```

The server is now active and listening for requests from client host computers.

When we set up our static IP address for our DHCP server last lesson, we already told it to use itself as the DNS server. If you open the `dhcpcd.conf` file by typing the following into your terminal:

```bash
sudo nano /etc/dhcpcd.conf
```

Scroll down to the bottom of the file and you should see the following configuration for your static IP address:

```
interface eth0

static ip_address=192.168.0.1/24
static routers=192.168.0.1
static domain_name_servers=192.168.0.1
```

The line `static domain_name_servers=192.168.0.1` is telling our DNS and DHCP server to use itself as the Domain Name Server for this network interface.

Press `Ctrl + x` to quit nano. Now enter the following command to restart the networking service:

```bash
sudo service networking restart
```

### On all the remaining client Pis

Before reconnecting any remaining client Pis to the hub/switch, check that their `/etc/dhcpcd.conf` files are configured to get an IP address from a DHCP server. They should still be configured this way from the previous lesson.

You can now go ahead and start reconnecting them to the hub/switch; they should immediately acquire an IP address from the DHCP server. Check this by using the command `ifconfig` again; the IP addresses given out should be randomly selected from the range specified on the server.

You should find that everyone can enter the command `ping serverpi` and get a response from the IP address.

### One step further: the web server!

Assuming you're using one or more Raspberry Pi [web servers](http://www.raspberrypi.org/documentation/remote-access/web-server/apache.md), it would be great to get to the point where you can type a name into a browser and see a home page load. This is the next task!

Before we change anything, we need to consider the problem of DHCP IP address allocations changing and becoming out of sync with the DNS server lookup table. This was touched on in the starter activity.

There is a convention in networking where server computers (as in providing some kind of service) have static IP addresses. That way, the IP address can be entered into the DNS lookup database without worrying about it changing at some point in the future.

We need to be careful here: if we just manually assign a static IP address, there is a possibility that the DHCP server could hand that same IP address out to another computer joining the network. To avoid that, we can change the range of IP addresses the DHCP server will give out. If we start the DHCP range at a higher number, we can leave ourselves a block of non-DHCP IP addresses that we can freely assign as static addresses for servers.

### Back on the server Pi again

Enter the following command to edit the `dnsmasq` configuration file:

```bash
sudo nano /etc/dnsmasq.conf
```

You'll see the `dhcp-range` line shows the first IP address (currently `192.168.0.2`) followed by the last one (currently `192.168.0.254`). Change the first IP address to be **.51** so that we can have the lower 50 for static IP addresses.

The line should now look like this:

```
dhcp-range=192.168.0.51,192.168.0.254,255.255.255.0,12h
```

Now we can safely assign a static IP address to our web server. There are actually two ways we can achieve this.  One is to edit the `/etc/dhcpcd.conf` file on the web server itself; or we can configure the DHCP server to recognise it by its MAC address and always assign it the same IP address. The latter is the more elegant way because it will also send the DNS server configuration settings via the DHCP offer; it also puts all the control in the hands of the server.

You'll need to look up the MAC address on the web server Pi for this. This can be found by entering the `ifconfig` command on it; look under `eth0` and on the first line just after `HWaddr` (hardware address). The MAC address will be something like `b8:27:eb:aa:bb:cc`.

Add that MAC address into the following line of the `dnsmasq` configuration file on the DNS server Pi. For example, to always assign `192.168.0.20`:

```bash
sudo nano /etc/dnsmasq.conf
```
and now add this line to end of your `dnsmasq.conf` file:

```
dhcp-host=b8:27:eb:aa:bb:cc,192.168.0.20
```

Press `Ctrl + o` then `Enter` to save followed by `Ctrl + x` to quit nano.

Now we just need to choose a name for the web server and add it into the `hosts.dnsmasq` file:

```bash
sudo nano /etc/hosts.dnsmasq
```

Add a new line to the file following the expected format. For example:

```
192.168.0.1    serverpi
192.168.0.20   webserverpi
```

Press `Ctrl + o` then `Enter` to save followed by `Ctrl + x` to quit nano. Enter the following command to restart the `dnsmasq` service:

```bash
sudo service dnsmasq restart
```

### On the web server Pi

We now just need to make the web server Pi release and renew its IP address from the DHCP server; it should then end up with the static IP that we have chosen to match the DNS entry. Enter the following commands to do this:

```bash
sudo dhcpcd --release
sudo dhcpcd --request
```

Double-check that the correct IP address was given by the DHCP server; use the `ifconfig` command for this. The address will be under `eth0` on the second line after `inet addr`. If it is not correct then go back and check the server Pi configuration files for mistakes, restart `dnsmasq`, and repeat the above two commands.

### On all the remaining client Pis

The remaining client Pis should now all be able to enter the address `http://webserverpi` into their web browser and see the home page load. In doing so, they will all be performing successful DNS queries against the server.  The command `ping webserverpi` should also work.

## Plenary

Students can now be invited to discuss similarities between the practical exercise and the starter activity.

It can be fun to add a few more web servers into the network, giving them both static IP addresses and DNS lookup entries. Follow the same process above to do this.

For each web server added you need to:

- Add a line into `/etc/dnsmasq.conf` to give the server a static IP address based on its MAC address
- Add a DNS lookup entry into `/etc/hosts.dnsmasq`
- Restart the `dnsmasq` service with the command: `sudo service dnsmasq restart`
- Use `sudo dhcpcd --release` and `sudo dhcpcd --request` on the web server itself
- Finally, you can then ping the server or load its home page using the DNS name from the other client Pis

## Homework

Homework will be to conduct your own research into how iterative DNS queries work on the internet. Try to find out what the following DNS servers are and what their job is:

- Local DNS server
- Root DNS server
- Top level domain DNS server
- Authoritative DNS server

Write 100 words on how a DNS query passes between all of the above.
