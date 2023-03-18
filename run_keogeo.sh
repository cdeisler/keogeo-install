#!/bin/bash

cd /home/kiosk


#sudo ./retroarch -L /home/kiosk/libretro-super/dist/unix/fbneo_libretro.so /home/kiosk/roms/arcade/kof96.zip
sudo ./retroarch/retroarch -L /home/kiosk/libretro-super/dist/unix/fbneo_libretro.so /home/kiosk/keogeo/roms/fbneo/kof98.zip && python3 /home/kiosk/keogeo/testSecondDisplay.py
#sudo ./retroarch/retroarch -L /home/kiosk/libretro-super/dist/unix/fbneo_libretro.so /home/kiosk/keogeo/roms/fbneo/kof98.zip


#sudo apt-get install -y python3-pyqt5




