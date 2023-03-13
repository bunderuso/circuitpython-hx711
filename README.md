# circuitpython-hx711
Circuitpython driver for the HX711 24-Bit Analog-to-Digital Converter

Based on the Micropython driver created by Sergey Piskunov

# Changes made between Micropython and Circuitpython
Libraries in the hx711.py file have been updated to work with the Circuitpython equivalents. 
Logic has been modified slightly to ensure pins can be addressed correctly.

# Current limitations
The pins are hardcoded to GP4 and GP5 in the hx711.py file. Goal is to remove this limitation to allow any pin to be used.
The example folder has not been updated to Circuitpython standards
