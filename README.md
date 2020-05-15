# Retroarch Entries Maker for ulaunch

<p align="center">
<img src="/Logo/Logo_round.png" width="40%">
</p>

[French Version](/French_Version/README.md)

Note : English is not my first language, so excuse me if there are some mistakes

# Requirement :
Before starting, you have to install the [latest Python release](https://www.python.org/downloads/) and I recommend you to install the latest Ant Renamer release.
# How To Use:
First of all, create a folder anywhere on your computer and put all your roms inside. Next, create another folder named "Icons" inside your roms folder and put all your games icons inside. Make sure that your images have decent size (I recommend 256x256), if it's not the case, you can resize multiple files by using Photoshop's Automatisation. Then, start Ant Renamer, drag and drop all your roms in the main box:

![](/Pics_How_To_Use/Ant-Renamer-1.png)

Then, go to the Actions tab and select Enumeration. Inside the Mask box, put:

> %num%-%name%%ext%

Then set the number of digits to 3 (if you have more than 1000 files, set it to 4), that will prevent bugs when the script assign icons with roms due to the difference between your software and python alphabetical classification (especially between Windows and Python, idk if this difference exists on Linux and Mac), and press GO:

![](/Pics_How_To_Use/Ant-Renamer-2.png)

Now, return to the Files tab, remove all files inside and drag and drop your icons. You can use the blue arrows at the top of the window to match icons order with roms order. Then go back to the Actions tab and select Enumeration. Now put in the Mask box :

> %num%%ext%

And set the number of digits to 1 and press GO:

![](/Pics_How_To_Use/Ant-Renamer-3.png)

Now all your files are ready! Start Retroarch_Entry_Maker.py. If you have already generated entries, it will tell you if you want to delete previous files, I recommend to say yes if you don't want to have two entries for the same game. Then, when it says:

> Enter your roms directory: 

Just copy-paste your roms directory path, for example:

> C:\Users\user\Desktop\roms

Note : You can replace "\\" by "/" if you want

Then press Enter and wait until it says "Done!" and press Enter again.

Now go into the "output" folder and copy-paste "Roms" and "ulaunch" folders at the root of your SD Card. You're now 
ready to play your games by launching AMS!

# Supported extensions: 
-----Amstrad CPC-----

.dsk

.sna

.kcr

---------DOS---------

.exe

.com

.bat

.conf

---------MSX---------

.rom

.mx1

.mx2

.cas

----Intellivision----

.int

---------NES---------

.nes

.fds

---------SNES--------

.smc

.sfc

.swc

---------GBA---------

.gba

---------GBC---------

.gbc

.cgb

.sgb

----------GB---------

.gb

.dmg

----Master System----

.sms

-------GameGear------

.gg

-------Genesis-------

.sg

.smd

.gen

------Megadrive------

.md

---------MAME--------

.chd

---------N64---------

.n64

.v64

.z64

.u1

.ndd

---------PS1---------

.bin

.img

-----Pokemon Mini----

.min

------Atari 7800-----

.a78

------Atari 2600-----

.a26

-------Vectrex-------

.vec

--------Saturn-------

.ccd

.mds

---------PSP---------

.iso

.cso
