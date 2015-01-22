# Lesson 2 - The Internet of Things: how do computers control other computers?

By 2020 there will be [50bn things](http://share.cisco.com/internet-of-things.html) connected to the internet, from cows to fridges to cars. This is known as the Internet of Things. In this lesson students will build the simplest Thing - a button that lights an LED across a network.

Students will be aware of how widespread and important networks are from lesson 1. They should be comfortable with terms used in that lesson, such as IP address, server, and client. The plenary could be used as a refresher.

## Learning objectives

- Know that a computer server can send data to another computer on a network
- Know that data received over a network can cause something to happen on the client computer beyond displaying a screen message

## Learning outcomes

### All students are able to:

- Explain that computers on a network can send data to each other, and that this data can make the receiving computer do something
- Use a simple program to control hardware across a network

### Most students are able to:

- Hack a program to make it do something usefully different

### Some students are able to:

- Adapt a program to make a Raspberry Pi control hardware on another Pi to behave in a specific way

## Lesson summary

- Introduction to physical, networked computing
- Extends Lesson 1 but controls hardware on the client machine instead of screen messaging
- Control another Raspberry Pi's GPIO pins over a network

## Starter

This can be done on paper or as drag and drop on an interactive whiteboard.

1. Students have one minute to rearrange the Python code on the [Lesson 2 code review](lesson-2-code-review.md) into the correct order.
1. Show the program running. Discuss what goes where and why, e.g. importing modules, functions, while loops etc.
1. Show video of PA's [Raspberry Pi competition](https://www.youtube.com/watch?v=x_-ngDlclw0) for schools and explain that all of the projects rely on a server controlling some physical aspect of a Raspberry Pi e.g. sensors, displays, pumps, camera etc.

## Main development

1. Explain that the students will connect two Raspberry Pis in a similar way to lesson 1, but this time they will control hardware instead of sending text.
1. Students should set up the network and control LEDs on another Pi using the [Student Instructions](student-instructions-2.md).
1. Extension ideas (AKA **encourage hacking!**): add screen messages for feedback, change how the LED flashes, change the physical button (e.g. a "pressure pad" made out of foil), add another LED (advanced).
1. *Optional*: If you will be using the SD cards again on a network, students will need to undo their changes to the `interfaces` file. Ask them to do this as per the 'Cleanup' section of the student instructions.

## Plenary

Ask each group to stand up and explain what changes they made to their program and how they did it. Display their code on screen if you have the capability, and ask them to explain the logic and any syntax of their hacks.

## Homework

1. Show students the source of the "[50bn things](http://share.cisco.com/internet-of-things.html)" quote.
1. Ask them to research and prepare a speed talk (1 minute) for next lesson, either arguing that the IoT is a good thing or a bad thing (no fence sitting!). If they want to use slides they should be pictures only, no words.
1. Next lesson pick several at "random" to stand up and give their talk, giving equal time to each side of the argument. The class votes on which wins.
