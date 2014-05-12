# Lesson 2 - The Internet of Things--how do computers control other computers? 

##Introduction
By 2020 there will be [50bn things] connected to the internet, from cows to fridges to cars. This is known as the Internet of Things. In this lesson students will build the simplest Thing - a button that lights an LED across a network.

Students will be aware of how widespread and important networks are from lesson 1. They should be comfortable with the terms such as IP, server, client etc used in that lesson. The plenary could be used as a refresher.

## Learning Objectives

- Know that a computer server can send data to another computer on a network
- Know that data received over a network can cause something to happen on the client computer beyond displaying a screen message

## Learning Outcomes

###All students are able to:

- explain that computers on a network can send data to each other and that this data can make the receiving computer do something
- use a simple program to control hardware across a network

###Most students are able to:

- hack a program to make it do something usefully different

###Some students are able to:

- adapt a program to make a Raspberry Pi control hardware on another Pi behave in a specific way

## Lesson Summary

- Introduction to physical, networked computing
- Extends Lesson 1 but controls hardware on the client machine instead of screen messaging
- Control another Raspberry Pi's GPIO pins over a network

## Starter
This can be done on paper or as drag and drop on an interactive whiteboard.
1. Students have one minute to rearrange the Python code on [Lesson-2-code-review] into the correct order. 
2. Show the program running. Discuss what goes where and why, e.g. importing modules; functions; while loops etc. 
3. Show video of PA's [Raspberry Pi competition] for schools and explain that every one of the projects relies on a server controlling some physical aspect of a Raspberry Pi e.g. sensors, displays, pumps, camera etc. 




## Main Development

1. Explain that the students will connect two Raspberry Pis in a similar way to lesson 1, but this time they will control hardware instead of sending text. 
2. Students set up network and control LEDs on another Pi using the [Student Instructions].
3. Extension ideas (aka **encourage hacking!**): add screen messages for feedback; change how the LED flashes; change the physical button e.g. a "pressure pad" out of foil add another LED (advanced).
4. (Optional). If you will be using the SD cards again on a network, student will need to revert their changes to the `interfaces` file. Ask them to do this as per the 'Cleanup' section of the student instructions.

## Plenary
Ask each group to stand up and explain what changes they made to their program and how they did it. Display their code on screen if you have the capability and ask them to explain the logic and any syntax of their hacks.

## Homework
1. Show students the source of the "[50bn things]" quote. 
2. Ask them to research and prepare a speed talk (1 minute) for next lesson either arguing that the IoT is a good thing or a bad thing (no fence sitting!). If they want to use slides, pictures only, no words. 
3. Next lesson pick several at "random" to stand up and give their talk, equal time to each side of the argument. Class votes on which wins.

[50bn things]: http://share.cisco.com/internet-of-things.html
[Student Instructions]: student-instructions-2.md
[Lesson-2-code-review]: Lesson-2-code-review.md
[Raspberry Pi competition]: https://www.youtube.com/watch?v=x_-ngDlclw0


