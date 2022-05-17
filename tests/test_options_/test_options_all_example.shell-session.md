     1^I[01m[user@linuxbox imx-bootlets-src-10.05.02]$ [39;49;00mmake [31mCROSS_COMPILE[39;49;00m=arm-none-eabi-  clean$
     2^Irm -rf *.sb$
     3^Irm -f sd_mmc_bootstream.raw$
     4^Irm -f linux_prep/board/*.o$
     5^I...$
     6^IFiles:$
     7^Irm -f power_prep.o eabi.o$
     8^IBuild output:$
     9^Imake[1]: Leaving directory `/home/...'$
    10^I[01m[user@linuxbox imx-bootlets-src-10.05.02]$ [39;49;00mmake [31mCROSS_COMPILE[39;49;00m=arm-none-eabi-$
    11^Imake[1]: Entering directory `/home/...'$
    12^I...$
    13^I[01m#[39;49;00m@echo [33m"generating U-Boot boot stream image"[39;49;00m$
    14^I[01m#[39;49;00melftosb2 -z -c ./uboot_prebuilt.db -o imx23_uboot.sb$
    15^Iecho "generating kernel bootstream file sd_mmc_bootstream.raw"$
    16^Igenerating kernel bootstream file sd_mmc_bootstream.raw$
    17^I[01m#[39;49;00mPlease use cfimager to burn xxx_linux.sb. The below way will no$
    18^I[01m#[39;49;00mwork at imx28 platform.$
    19^I> test$
    20^I[01m$ [39;49;00m[36mtest[39;49;00m$
    21^Irm -f sd_mmc_bootstream.raw$
    22^I[01m[user@linuxbox imx-bootlets-src-10.05.02]$[39;49;00m$
    23^I[01mpi@raspberrypi ~ $ [39;49;00msudo sh -c [33m"echo 17 > /sys/class/gpio/export"[39;49;00m$
    24^I[01mpi@raspberrypi ~ $ [39;49;00msudo sh -c [33m"echo out > /sys/class/gpio/gpio17/direction"[39;49;00m$
    25^I[01mpi@raspberrypi ~ $ [39;49;00msudo sh -c [33m"echo 1 > /sys/class/gpio/gpio17/value"[39;49;00m$
    26^I[01mpi@raspberrypi ~ $ [39;49;00msudo sh -c [33m"echo 0 > /sys/class/gpio/gpio17/value"[39;49;00m$
    27^I[01mpi@raspberrypi ~ $[39;49;00m$
    28^I[01m[user@linuxbox ~]$ [39;49;00m[37m# copy other stuff to the SD card[39;49;00m$
    29^I[01mroot@imx233-olinuxino-micro:~# [39;49;00mlsmod$
    30^I  Not tainted$
    31^I[01m[user@linuxbox ~]$ [39;49;00mtail -n [34m2[39;49;00m /mnt/rpi/etc/inittab$
    32^I[01m#[39;49;00mSpawn a getty on Raspberry Pi serial line$
    33^IT0:23:respawn:/sbin/getty -L ttyAMA0 115200 vt100$
    34^I[01mpi@raspberrypi:~/Adafruit-WebIDE$ [39;49;00mmkdir tmp$
    35^I[01mpi@raspberrypi:~/Adafruit-WebIDE$ [39;49;00mnpm config [36mset[39;49;00m tmp tmp$
    36^I[01mpi@raspberrypi:~/Adafruit-WebIDE$ [39;49;00mnpm install$
    37^I[01mpi@raspberrypi ~/Adafruit-WebIDE $ [39;49;00mifconfig eth0$
    38^Ieth0      Link encap:Ethernet  HWaddr b5:33:ff:33:ee:aq$
    39^I          inet addr:10.42.0.60  Bcast:10.42.0.255  Mask:255.255.255.0$
    40^I          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1$
    41^I          RX packets:21867 errors:0 dropped:0 overruns:0 frame:0$
    42^I          TX packets:8684 errors:0 dropped:0 overruns:0 carrier:0$
    43^I          collisions:0 txqueuelen:1000$
    44^I$
