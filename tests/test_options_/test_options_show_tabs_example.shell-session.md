[01m[user@linuxbox imx-bootlets-src-10.05.02]$ [39;49;00mmake [31mCROSS_COMPILE[39;49;00m=arm-none-eabi-  clean
rm -rf *.sb
rm -f sd_mmc_bootstream.raw
rm -f linux_prep/board/*.o
...
Files:
rm -f power_prep.o eabi.o
Build output:
make[1]: Leaving directory `/home/...'
[01m[user@linuxbox imx-bootlets-src-10.05.02]$ [39;49;00mmake [31mCROSS_COMPILE[39;49;00m=arm-none-eabi-
make[1]: Entering directory `/home/...'
...
[01m#[39;49;00m@echo [33m"generating U-Boot boot stream image"[39;49;00m
[01m#[39;49;00melftosb2 -z -c ./uboot_prebuilt.db -o imx23_uboot.sb
echo "generating kernel bootstream file sd_mmc_bootstream.raw"
generating kernel bootstream file sd_mmc_bootstream.raw
[01m#[39;49;00mPlease use cfimager to burn xxx_linux.sb. The below way will no
[01m#[39;49;00mwork at imx28 platform.
> test
[01m$ [39;49;00m[36mtest[39;49;00m
rm -f sd_mmc_bootstream.raw
[01m[user@linuxbox imx-bootlets-src-10.05.02]$[39;49;00m
[01mpi@raspberrypi ~ $ [39;49;00msudo sh -c [33m"echo 17 > /sys/class/gpio/export"[39;49;00m
[01mpi@raspberrypi ~ $ [39;49;00msudo sh -c [33m"echo out > /sys/class/gpio/gpio17/direction"[39;49;00m
[01mpi@raspberrypi ~ $ [39;49;00msudo sh -c [33m"echo 1 > /sys/class/gpio/gpio17/value"[39;49;00m
[01mpi@raspberrypi ~ $ [39;49;00msudo sh -c [33m"echo 0 > /sys/class/gpio/gpio17/value"[39;49;00m
[01mpi@raspberrypi ~ $[39;49;00m
[01m[user@linuxbox ~]$ [39;49;00m[37m# copy other stuff to the SD card[39;49;00m
[01mroot@imx233-olinuxino-micro:~# [39;49;00mlsmod
  Not tainted
[01m[user@linuxbox ~]$ [39;49;00mtail -n [34m2[39;49;00m /mnt/rpi/etc/inittab
[01m#[39;49;00mSpawn a getty on Raspberry Pi serial line
T0:23:respawn:/sbin/getty -L ttyAMA0 115200 vt100
[01mpi@raspberrypi:~/Adafruit-WebIDE$ [39;49;00mmkdir tmp
[01mpi@raspberrypi:~/Adafruit-WebIDE$ [39;49;00mnpm config [36mset[39;49;00m tmp tmp
[01mpi@raspberrypi:~/Adafruit-WebIDE$ [39;49;00mnpm install
[01mpi@raspberrypi ~/Adafruit-WebIDE $ [39;49;00mifconfig eth0
eth0      Link encap:Ethernet  HWaddr b5:33:ff:33:ee:aq
          inet addr:10.42.0.60  Bcast:10.42.0.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:21867 errors:0 dropped:0 overruns:0 frame:0
          TX packets:8684 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
