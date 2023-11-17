# FishFeeder
Bill of materials:
  - Tower Pro SG92R Micro Servo
  - Raspberry Pi Pico (Or other similarly sized Microcontroller)
  - 3D Printed Parts

Upload the micropython code to the raspberry pi. It is currently set to feed twice every 24 hours by shifting the microservo left and right to move the feeding arm. Assemble by stacking the parts in the order of the image, and hold together with two rods plus super glue. 

Parts have been designed such that they don't need supports. Consider printing the arm at 95-97% size if the parts don't fit together.

This is a remix of a model by a user named Jo_5 on thingiverse, modified to function with the smaller Micro Servo and a Raspberry Pi instead of an Arduino. I have since been unable to find the original creator. 

3d Model:
![3d Model](https://github.com/twu425/FishFeeder/assets/82834362/f47fb8ee-0366-41aa-8b15-10d429774c65)

Wiring Diagram (Very simple thanks to the micro servo working with the pico's 3v supply):
![diagram](https://github.com/twu425/FishFeeder/assets/82834362/f6daffde-ed97-4cbb-bc52-2c50461fc6b7)

Assembled Model:


Notes: Make sure your house doesn't have ants. My original prototype was unceremoniously decomissioned after my sister sprayed bug killer all over the electronics. 
