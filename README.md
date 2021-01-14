# Ambient-TV-Light
Ambient light around the TV that matches the screen.

## Demo:

TODO: add gif

Youtube Videos:
* [Fluid](https://www.youtube.com/watch?v=qC0vDKVPCrw)
* [Netflix Intro](https://www.youtube.com/watch?v=6Jg_rkKtJgo)
* [Color Wheel](https://www.youtube.com/watch?v=8u4UzzJZAUg)

## Required Parts:
Links provided are the items I used.

* [Raspberry Pi](https://www.amazon.com/gp/product/B07TD42S27/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1) 
  * [Micro HDMI to HDMI](https://www.amazon.com/gp/product/B07TTKD38N/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1)
  * [USB C Power Supply](https://www.amazon.com/gp/product/B07TYQRXTK/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)
  * Micro SD Card with [Raspberry Pi OS installed](https://www.raspberrypi.org/software/) _(Can be purchased pre-installed)_
  * Optional (Recommended): [Pi Case](https://www.amazon.com/gp/product/B07D3S4KBK/ref=ppx_yo_dt_b_asin_title_o03_s01?ie=UTF8&th=1)
  * Mouse
  * Keyboard
  
* Monitor/TV

* USB Capture Device (_with 4k pass-through preferred_)
  * Extra HDMI Cable
  * Optional: HDMI Splitter
  * Optional: HDMI Switch
  
* [LED Strip](https://www.amazon.com/gp/product/B01CNL6LLA/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1) _**IMPORTANT:** Ensure the power supply has the correct voltage for LED strip)_
  * [LED Power Supply](https://www.amazon.com/gp/product/B06Y64QLBM/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)
  * [Male to Female Wires](https://www.amazon.com/gp/product/B01EV70C78/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)
 
* Optional: Two Smart Plugs (_to turn on LED Strip and Raspberry Pi, Turn on LED Strip first)_

## Setup
  
### Setup Pi
1. Install Raspberry Pi OS to a Micro SD Card
2. Insert Micro SD into Raspberry Pi
3. Setup Raspberry Pi
4. Install OpenCV 2 on Raspberry Pi
5. Clone this repository onto Raspberry Pi

### Setup Autorun Python Script on Reboot
Open a terminal and type:
```sudo crontab -e```<br />
```1```<br />
press: enter<br />
Scroll to the bottom of the file and add the following line:<br />
```@reboot sudo python /home/pi/Ambient-TV-Light/rgb_kmeans.py```<br />
press: CTLR + X<br />
press: y<br />
press: enter<br />

### Wiring
See diagram below
![](/wiring.png)

### Connecting the Components
See diagram below
![](/components.png)

## Running the System
1. Turn source on
2. Connect LED Strip Power
3. Connect Raspberry Pi Power
