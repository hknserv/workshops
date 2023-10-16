---
title: EECS Day EE Lab Instructions
author: Bryan Ngo
---

# Introduction

Welcome to the EECS Day Electrical Engineering lab!
In this lab you are going to have a sneak peek into the life of an EECS student by building an interesting electronic circuit with us - a speed-controlled binary counter!
These instructions will guide you through the purpose of our circuit, what electrical components we will be using and how to put them together.
For any further questions, refer to the lab instructors (we don't bite).

First, let's understand what a counting system is.
In daily life we use the decimal system, which has 10 different digit symbols (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) and whenever we need to count a quantity greater than our amount of symbols we increase our symbol to the left by one and reset our digit.
This is called [positional notation](https://en.wikipedia.org/wiki/Positional_notation).
Similarly, a binary system has 2 different digits (0, 1) and works the same way as the decimal system.

Let's go through an example. For the sake of notation, whenever a number is written in binary we put the prefix `0b` before the number.
Suppose we count from decimal 0 to decimal 7.
We start with 0 = `0b000` and 1 = `0b001`.
You can see for the right-most digit we are out of symbols so we go to the left one and add 1, so 2 = `0b010` and 3 = `0b011`.
We are again left with no symbols on both right-most digits so we proceed the same way: 4 = `0b100`, 5 = `0b101`, 6 = `0b110`, 7 = `0b111`!

Why is binary so important?
Every computer you use is composed of billions of tiny devices called transistors.
These transistors are single operation machines that, given an input, return either True or False.
You see how we can model our transistors as binary numbers?
Let True be `0b1` and False be `0b0` - our computers count in binary!

In our circuits we will have four LEDs (light emitting diodes), and each LED will behave as one binary digit (or bit), so having all of them off represents `0b0000` and all of them on represents the number `0b1111` (convince yourself this equals 15).
If we simply turn on our circuit, our counter may count from 0 to 15 too fast for us to appreciate, thus we will control its speed using a potentiometer.

# Materials

Read through all the materials and let us know if anything in the below list is missing from your lab materials:

|                               Problem                              |                                                                                                                                                            Solution                                                                                                                                                            |
|:------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| ![](https://cdn.sparkfun.com//assets/parts/3/3/8/0/09590-01.jpg)     | LED (4x): A light emitting diode which lights up when electricity passes through it. Attention: The LED legs have different lengths, the long one being the positive one and the short one being negative; the orientation matte                                                                                               |
| ![](https://www.jameco.com/Jameco/Products/ProdImag/2237191.jpg)     | Resistor (4x): A resistor is a device that restricts the flow of electric current into our LEDs preventing them from overloading. The strength of a resistor is controlled by its resistance, in our case it is 1 kΩ or kilo-ohm. To verify yours is correct check the color strips are, in order, brown, black, red and gold. |
| ![](https://www.newark.com/productimages/standard/en_US/4435012.jpg) | Potentiometer (1x): A device that controls the voltage passing through it. In other words, it is a resistor you can change the value of! The lonely pin is the output. From the two-pin side, the pin close to the marking is the input and the other one should be connected to ground.                                       |
| ![](https://cdn-shop.adafruit.com/970x728/3591-00.jpg)               | Microcontroller (1x): Our [Adafruit ESP32 Feather](https://www.adafruit.com/product/3591) has an embedded computer that will control our circuit. We will go into more detail later. Note the Micro-USB port on the top.                                                                                                       |
| ![](https://m.media-amazon.com/images/I/61p+QTbMf5L.jpg)             | Breadboard (1x): A platform full of holes where you can stick wires and components to organize your circuit and prevent them from falling out. We will go into more detail later.                                                                                                                                              |
| ![](https://m.media-amazon.com/images/I/414Fn43RXVL._AC_SY580_.jpg)  | Wires (At least 10).                                                                                                                                                                                                                                                                                                           |


# Microcontroller & Breadboard

Our microcontroller contains all the fancy tools we will need to make this circuit work.
It contains a computer and pins that can serve as the interface between the computer and our circuit.
Don't worry about software or coding the microcontroller, we will be uploading it for you.
If you want to see the code running on your ESP32, [here](counter.ino) is a link. Here is a breakdown of what pins we will be using:

- `3V`: This is a pin which provides power to the potentiometer, specifically 3.3 V, despite the name. Notice that for the LEDs we will get electricity elsewhere.
- `GND`: This is our ground terminal, indicated by the negative sign. Think of electricity as a bunch of electrons running through the wires. The electrons have to travel somewhere to complete the circuit, which is the purpose of ground. All our components in the circuit connect here.
- `A0`, `A1`, `A5`, `21`: These are our analog output pins, which the computer is able to control the voltage level of. We will use them to power the LEDs,
- `32`: This is an analog input, which we will use to measure the voltage from the potentiometer.

The breadboard is the second most important part of the circuit, and any good circuit design starts on the breadboard.
First, on both sides we have the **Positive (+)** and **Negative (-)** rails.
They are connected to each other columnwise, and we connect the negative column to `GND` and the positive to any constant power source.
The other holes are connected in rows, though this connection does not cross the middle divide, as you can see in:

![](https://designbuildcode.weebly.com/uploads/2/5/7/4/25741451/breeadboard_orig.png)

# Instructions

![](https://i.imgur.com/LGPVaAz.png)
![](https://i.imgur.com/ghscsdA.png)

_Note: the image and its circuit diagram is representative of what we are trying to do but does not include every component._

1. Plug wire between negative columns of both sides.
2. Position resistors on 29b to 29g, 27b to 27g, 25b to 25g, and  23b to 23g.
3. Position LED on 29j (long pin) to negative, 27j (long pin) to negative, 25j (long pin) to negative and 23j (long pin) to negative.
4. Position potentiometer on 22d, 20d and 21f.
5. On the left side, connect row 29 to 16, row 27 to 10, row 25 to 6 and row 23 to 5. Also connect row 2 to the positive rail, row 4 to negative rail, row 20 to the positive rail and row 22 to the negative rail.
6. On the right side connect row 21 to 13.
7. **Come up to us so that we can program your microcontroller and give you a cable to power it!**
8. Position microcontroller in between the middle divider with the RST pin on 1c.
9. Connect the Micro-USB cable to the AC adapter and plug it in!

Be sure to press down the microcontroller while it is on, since the connection between it and the breadboard may be loose.

Use a screwdriver to turn the potentiometer clockwise and counterclockwise. What happens?


