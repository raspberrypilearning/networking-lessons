Dynamic Host Configuration Protocol (DHCP)
==================
This learning resource describes a practical exercise where the Raspberry Pi is used to demonstrate Dynamic Host Configuration Protocol on an isolated network.

![](./images/cover.jpg)

## Introduction

By now it will be clear that repeatedly changing the `/etc/network/interfaces` file is time consuming and laborious. There are a number of disadvantages to all computers on the a network having static IP addresses. Consider what would happen when you want to add even more computers to your network.

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

The DHCP server has a set of rules that must be followed, this is the protocol part of the name. One of the hosts now wants to join the network. This is how the conversation should go:

- HOST: "Hello is there a DHCP server out there?"
- DHCP: "Yes I am here"
- HOST: "I am *Dave*, please can I have an IP address?"
- DHCP: "*Dave* here is your address. You may keep it for 12 hours."
  
The DHCP server hands over an address card to *Dave* and writes his name on the paper along with the address that was given, the time it was given out and the lease time. In this case 12 hours.

Stop for a moment and consider if there was any part of this conversation that was unexpected?
When a computer joins a network it has no way of knowing if a DHCP server is available - so it sends out a broadcast signal to the whole network asking if one is there. If one *is* available it will reply to the host. The host then asks to be given an address. The part you might not have expected is that the address is given with a lease time, in this case 12 hours. Consider why this might be and continue below.
