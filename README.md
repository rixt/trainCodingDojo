# Coding Dojo with Lego train
This coding dojo is inspired by Youtube channel [Arduino Lego Trains](https://www.youtube.com/channel/UCyvLxhkuFuukFxgYQx2eB9g) and the site [Internet of lego](http://www.internetoflego.com/lego-train-automation-ir-power-functions-with-nodejs-and-lirc).

## Hardware
Raspberry Pi 3 Model B

### Electronics
Black = Ground (GND), Red = 5V (VCC), Yellow / Blue = Signal (GPIO / DI / DO)

GPIO = GPIO on Raspberry Pi

![alt tag](https://cloud.githubusercontent.com/assets/623892/25093760/f9a756fe-2393-11e7-9ca2-ef39c5051143.jpg)
1. 5V and ground connect to IR-remote (5)
2. Power and signal cable for motor. 3-pole contactor to motor controller (4). Yellow to GPIO 25, Blue to GPIO 23 and 24
3. Cabel to Lego motor. Connected to motor controller (4)
4. Motor controller (Dual H Bridge Stepper Motor Drive Controller Board Module For Arduino L298N CF). Control for the gear motor. Supplies motor and IR-remote with 5V
5. IR-remote (Infrared-led 5mm, 1.35v, 100ma, 925mm). Resistors for regulating the current. You can buy premade on eBay
6. Photo resistor sensor module detector board
7. Signal connects to GPIO22 and DI on IR-remote

## Software

## Raspbian
Operating system used on the PI.

### LIRC
LIRC is need to controll the train with IR. Follow the instructions from Internet of Lego
http://www.internetoflego.com/lego-train-automation-ir-power-functions-with-nodejs-and-lirc/

LIRC is a package that allows you to decode and send infra-red signals of many (but not all) commonly used remote controls.

### Lego-LIRC
LEGO Power Functions LIRC (Linux Infrared Remote Control)

https://github.com/dspinellis/lego-lirc

## Controll train
The IR-remote is controlled with LIRC.

### List all possible commands
irsend LIST LEGO_Single_Output ""

### Drive the train forward and stop
irsend SEND_ONCE LEGO_Single_Output 1B_4
irsend SEND_ONCE LEGO_Single_Output 1B_BRAKE

## Reference
#### Description of the RaspberryPi pinout
https://pinout.xyz/

#### RASPBERRY PI WITH LINUX LESSONS
http://www.toptechboy.com/raspberry-pi-with-linux-lessons/

#### Controll LIRC from NodeJS
https://github.com/alexbain/lirc_node
https://github.com/alexbain/lirc_web
https://github.com/pmgration/node-infrared
