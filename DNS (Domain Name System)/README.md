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

## Lesson Summary

- A discussion of the logical process followed by a DNS service
- Setting up one Raspberry Pi to be a DNS server
- Use other Raspberry Pi's to perform DNS queries
- Testing the network

## Resources

For the majority of the lesson, it is suggested that work is carried out by students in pairs. The Ethernet hub or switch should remain completely isolated without any Ethernet cables connecting it into the main school network.

- The DHCP server Raspberry Pi from the previous lesson;
- One or more Raspberry Pis with a [Wordpress server](http://www.raspberrypi.org/learning/web-server-wordpress/) running (optional); 
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

Begin by nominating one student to be the DNS server. Give each remaining student a number card. The DNS server must write down the names of all the students along with their number. This list represents the database of names held by the DNS service.

Suppose, for the sake of argument, that all the remaining students are web servers hosting a website. One of the students now wants to type `http://dave` into their web browser. This is how the DNS query would happen:

- HOST: "Hello DNS server, can you give me an IP address for the name 'dave' please?"
- DNS: "I have 'dave' down as X"
- HOST: "Hello X, please give me your home page."
- X: "Here is my home page."

That seems pretty simple doesn't it? Now consider this scenario. Nominate one more student to also be a DNS server and give them responsibility for half of the list of names. This is also how the DNS query could go:

- HOST: "Hello DNS server, can you give me an IP address for the name 'dave' please?"
- DNS1: "I don't seem to have 'dave', hold on a minute!"
- DNS1: "DNS2, do you have an IP address for the name 'dave' please?"
- DNS2: "DNS1, I have 'dave' down as X"
- DNS1: "HOST, I have found 'dave' to be X"
- HOST: "Hello X, please give me your home page."
- X: "Here is my home page."

So in this scenario the first DNS server didn't have 'dave' in its database but it passed on the query to a second DNS server that did. This is what is known as an *iterative DNS query*. The second DNS server responded to the first and the first responed to the original host/client with the IP address information. So the answer was fed back along the chain, so to speak.

Consider how something like this might work on the Internet. Real Internet DNS distributes the responsibility of remembering what name is for an IP address to a network of many DNS servers around the world.

What actually happens is that there are DNS servers dedicated to different domain name levels. For example there will be one for `.com`, another for `.org` and another for `.co.uk`. So when you type in an address like `raspberrypi.org` the query will pass through several DNS servers before the answer gets back to you.

## Main practical activity

## Plenary

## Homework
