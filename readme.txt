bikeshare_getbikedata.py is the part of the script that just grabs the station IDs and availabe bikes from the bikeshrae site and turns it into a dictionary.  It is the first block of the program.

bikeshare_getwmata.py is the part of the script that just grabs the metro statio status. It is the section block of the program.  THIS IS AN OLD SCRIPT - BETTER TO USE WMATA_PULL.PY

bikeshare_respondtodata.py adds a conditional response based on the data, and also allows you to pick which stations you want to focus on.

bikeshare.py is the most mature functional version of the program. It is designed to stand alone.  The other scripts are just stand alone portions of the program that I built to figure out how they work.  I'm leaving them here because when I was learning how to do this I wished these sorts of functional program fragments were out there for me.

wmata_pull.py - downloads the json version of U st. data and prints line/destination/time for first train

wmata_parse.py - sets variables for the relevant data points in wmata data

h.py - sets neopixel connected to arduino based on H parameter

l.py - sets neopizel connected to arduino based on L parameter

arduino-two-light - makes arduino respond to "H" or "L" serial command

light-true.py - you can pick the light display at the prompt.  However, there is no way to change it once it has been picked.  Question asked here: http://stackoverflow.com/questions/38422701/interrupt-while-loop-with-user-input-controlling-neopixels-via-arduino-and-pyth
