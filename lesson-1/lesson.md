# Lesson 1 - How do computers communicate?

In this lesson students will build a simple network and use it to communicate, via a network chat program. The students will learn how to network two Raspberry Pis, and then write a small program in Python that allows them to send messages to each other.

If the students are not confident with setting up the Raspberry Pi, and editing and running Python programs, you might want to try a scheme of work such as the [Turing Test](https://www.raspberrypi.org/learning/turing-test-lessons/) first.

## Learning objectives

- Know that a computer network consists of two or more computers (or devices) connected together
- Know that each computer has a unique IP address, that allows other computers to find it and send data to it

## Learning outcomes

### All students are able to:

- Explain that a computer network is two or more computers joined together
- Use a simple program to send messages between two computers

### Most students are able to:

- Explain that every computer on a network needs a unique address called an IP address
- Make simple changes to their program, such as changing screen prompts and adding welcome messages

### Some students are able to:

- Make more complex changes to their program, such as sending responses to keywords

## Lesson summary

- An introduction to simple computer networks
- Networking the Raspberry Pis
- Writing the chat program

## Homework

In the **previous** lesson ask the students to watch [this video on basic networking](http://www.youtube.com/watch?v=kNJZ-v263zc). Then, they research and write down what they understand by the following terms: computer network, IP address, server, client, and LAN. They will need to understand these terms for this lesson, without their homework in front of them.

## Starter

This starter is a quick-fire "ideas" round to introduce students to the ubiquity of networks, and why they are useful (or in their eyes, essential!).

1. Introduce the idea that computer networks are everywhere. In groups of two or three, ask the students to write down as many networked devices (or uses for networking) as they can in two minutes. Give them one or two examples to get them started.

1. Ask the groups to circle any of the devices on their list that they have used since they got up this morning. They have one minute to do this.

1. The group **touching** the most networked devices after 30 seconds wins. They are allowed to get devices from their bags, get out of their chairs and so on. **TIP:** This is particularly effective (and manic!) if you have a 30 second music clip and they have to freeze when the music stops.

1. Ask each group for one device they have chosen and briefly discuss them. Add a few not-so-obvious ones such as bank ATMs and speed cameras. Emphasise that the modern world relies on computer networks, and that they will now build their own.

## Main development

The concepts that the students learned from the homework will be used and consolidated as they complete the tasks.

1. Students should set up the network and send messages using the [Student Worksheet](worksheet.md).

1. **Optional**: If you will be using the SD cards again on a network, students will need to undo their changes to the `/etc/dhcpcd.conf` file. Ask them to do this as per the 'Cleanup' section of the [How to set up up your Raspberry Pi to have a static IP address](https://www.raspberrypi.org/learning/networking-lessons/rpi-static-ip-address/) guide.

## Plenary

Write the following list of words on the board:

- Server
- Client
- Computer network
- IP address
- Static IP address
- LAN

Select a student randomly from the class. They must select one of the words/terms from the board, stand up and point to someone else in the class who must then explain what the word means. That person then chooses the next person to explain one of the terms.
