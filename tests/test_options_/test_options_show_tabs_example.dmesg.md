[34m[    0.000000] [39;49;00m[34mLinux version 5.0.9-arch1-1-ARCH (builduser@heftig-18307) (gcc version 8.3.0 (GCC)) #1 SMP PREEMPT Sat Apr 20 15:[39;49;00m00:46 UTC 2019
[34m[    0.000000] [39;49;00m[34mCommand line:[39;49;00m initrd=\initramfs-linux.img root=/dev/nvme0n1p1 nouveau.noaccel=1 rw
[34m[    0.000000] [39;49;00m[34mKERNEL supported cpus:[39;49;00m
[34m[    0.000000] [39;49;00m  Intel GenuineIntel
[34m[    0.000000] [39;49;00m  AMD AuthenticAMD
[34m[    0.000000] [39;49;00m  Hygon HygonGenuine
[34m[    0.000000] [39;49;00m  Centaur CentaurHauls
[34m[    0.000000] [39;49;00m[34mx86/fpu:[39;49;00m Supporting XSAVE feature 0x001: 'x87 floating point registers'
[34m[    0.000000] [39;49;00m[34mx86/fpu:[39;49;00m Supporting XSAVE feature 0x002: 'SSE registers'
[34m[    0.000000] [39;49;00m[34mx86/fpu:[39;49;00m Supporting XSAVE feature 0x004: 'AVX registers'
[34m[    0.000000] [39;49;00m[34mx86/fpu:[39;49;00m Supporting XSAVE feature 0x008: 'MPX bounds registers'
[34m[    0.000000] [39;49;00m[34mx86/fpu:[39;49;00m Supporting XSAVE feature 0x010: 'MPX CSR'
[34m[    0.000000] [39;49;00m[34mx86/fpu:[39;49;00m xstate_offset[2]:  576, xstate_sizes[2]:  256
[34m[    0.000000] [39;49;00m[34mx86/fpu:[39;49;00m xstate_offset[3]:  832, xstate_sizes[3]:   64
[34m[    0.000000] [39;49;00m[34mx86/fpu:[39;49;00m xstate_offset[4]:  896, xstate_sizes[4]:   64
[34m[    0.000000] [39;49;00m[34mx86/fpu:[39;49;00m Enabled xstate features 0x1f, context size is 960 bytes, using 'compacted' format.
[34m[    2.663456] [39;49;00m[34mtpm_crb MSFT0101:[39;49;00m[91m00: [Firmware Bug]: ACPI region does not cover the entire command/response buffer. [mem 0xfed40000-0xfed4087f flags 0x200] vs fed40080 f80[39;49;00m
[34m[    2.663514] [39;49;00m[34mtpm_crb MSFT0101:[39;49;00m[91m00: [Firmware Bug]: ACPI region does not cover the entire command/response buffer. [mem 0xfed40000-0xfed4087f flags 0x200] vs fed40080 f80[39;49;00m
[34m[    2.664809] [39;49;00m[34mBluetooth:[39;49;00m Core ver 2.22
[34m[    2.664820] [39;49;00m[34mNET:[39;49;00m Registered protocol family 31
[34m[ 3134.452501] [39;49;00m[34musb 2-2:[39;49;00m new SuperSpeed Gen 1 USB device number 2 using xhci_hcd
[34m[ 3134.471506] [39;49;00m[34musb 2-2:[39;49;00m New USB device found, idVendor=0781, idProduct=cfd2, bcdDevice= 0.02
[34m[ 3134.471508] [39;49;00m[34musb 2-2:[39;49;00m New USB device strings: Mfr=3, Product=4, SerialNumber=2

kern  :notice: [    0.000000] Linux version 5.0.9-arch1-1-ARCH (builduser@heftig-18307) (gcc version 8.3.0 (GCC)) #1 SMP PREEMPT Sat Apr 20 15:00:46 UTC 2019
kern  :info  : [    0.000000] Command line: initrd=\initramfs-linux.img root=/dev/nvme0n1p1 nouveau.noaccel=1 rw
kern  :info  : [    0.000000] KERNEL supported cpus:
kern  :info  : [    0.000000]   Intel GenuineIntel
kern  :info  : [    0.000000]   AMD AuthenticAMD
kern  :info  : [    0.000000]   Hygon HygonGenuine
kern  :info  : [    0.000000]   Centaur CentaurHauls
kern  :info  : [    0.000000] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
kern  :info  : [    0.000000] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
kern  :info  : [    0.000000] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
kern  :info  : [    0.000000] x86/fpu: Supporting XSAVE feature 0x008: 'MPX bounds registers'
kern  :info  : [    0.000000] x86/fpu: Supporting XSAVE feature 0x010: 'MPX CSR'
kern  :info  : [    0.000000] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
kern  :info  : [    0.000000] x86/fpu: xstate_offset[3]:  832, xstate_sizes[3]:   64
kern  :info  : [    0.000000] x86/fpu: xstate_offset[4]:  896, xstate_sizes[4]:   64
kern  :info  : [    0.000000] x86/fpu: Enabled xstate features 0x1f, context size is 960 bytes, using 'compacted' format.
kern  :info  : [    0.000000] BIOS-provided physical RAM map:
kern  :info  : [    0.000000] BIOS-e820: [mem 0x0000000000000000-0x0000000000057fff] usable
kern  :info  : [    2.382262] EXT4-fs (nvme0n1p1): re-mounted. Opts: (null)
kern  :notice: [    2.389774] random: systemd-random-: uninitialized urandom read (512 bytes read)
kern  :info  : [    2.397148] usb 1-10: New USB device found, idVendor=8087, idProduct=0aa7, bcdDevice= 0.01
kern  :info  : [    2.397150] usb 1-10: New USB device strings: Mfr=0, Product=0, SerialNumber=0
kern  :info  : [    2.519599] usb 1-12: new high-speed USB device number 4 using xhci_hcd
kern  :crit  : [18706.135478] mce: CPU6: Package temperature above threshold, cpu clock throttled (total events = 79)
kern  :crit  : [18706.135479] mce: CPU3: Package temperature above threshold, cpu clock throttled (total events = 79)
kern  :crit  : [18706.135484] mce: CPU4: Package temperature above threshold, cpu clock throttled (total events = 79)
kern  :info  : [18706.136450] mce: CPU4: Core temperature/speed normal
[04m[91mk[39;49;00m[04m[91me[39;49;00m[04m[91mr[39;49;00m[04m[91mn[39;49;00m[04m[91m [39;49;00m[04m[91m [39;49;00m[04m[91m:[39;49;00m[04m[91mi[39;49;00m[04m[91mn[39;49;00m[04m[91mf[39;49;00m[04m[91mo[39;49;00m[04m[91m [39;49;00m[04m[91m [39;49;00m[04m[91m:[39;49;00m[04m[91m [39;49;00m[34m[18706.136451] [39;49;00m[34mmce:[39;49;00m[04m[91m [39;49;00m[04m[91mC[39;49;00m[04m[91mP[39;49;00m[04m[91mU[39;49;00m[04m[91m1[39;49;00m[04m[91m:[39;49;00m[04m[91m [39;49;00m[04m[91mP[39;49;00m[04m[91ma[39;49;00m[04m[91mc[39;49;00m[04m[91mk[39;49;00m[04m[91ma[39;49;00m[04m[91mg[39;49;00m[04m[91me[39;49;00m[04m[91m [39;49;00m[04m[91mt[39;49;00m[04m[91me[39;49;00m[04m[91mm[39;49;00m[04m[91mp[39;49;00m[04m[91me[39;49;00m[04m[91mr[39;49;00m[04m[91ma[39;49;00m[04m[91mt[39;49;00m[04m[91mu[39;49;00m[04m[91mr[39;49;00m[04m[91me[39;49;00m[04m[91m/[39;49;00m[04m[91ms[39;49;00m[04m[91mp[39;49;00m[04m[91me[39;49;00m[04m[91me[39;49;00m[04m[91md[39;49;00m[04m[91m [39;49;00m[04m[91mn[39;49;00m[04m[91mo[39;49;00m[04m[91mr[39;49;00m[04m[91mm[39;49;00m[04m[91ma[39;49;00m[04m[91ml[39;49;00m
