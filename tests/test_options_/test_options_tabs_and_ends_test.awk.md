[37m#!/bin/awk -f[39;49;00m$
$
[36mBEGIN[39;49;00m {$
  [37m# It is not possible to define output file names here because[39;49;00m$
  [37m# FILENAME is not define in the BEGIN section[39;49;00m$
  n = [33m""[39;49;00m;$
  [34mprintf[39;49;00m [33m"Generating data files ..."[39;49;00m;$
  network_max_bandwidth_in_byte = [34m10000000[39;49;00m;$
  network_max_packet_per_second = [34m1000000[39;49;00m;$
  last3 = [34m0[39;49;00m;$
  last4 = [34m0[39;49;00m;$
  last5 = [34m0[39;49;00m;$
  last6 = [34m0[39;49;00m;$
}$
{$
  [34mif[39;49;00m ($[34m1[39;49;00m ~ [33m/Average/[39;49;00m)$
    { [37m# Skip the Average values[39;49;00m$
      n = [33m""[39;49;00m;$
      [34mnext[39;49;00m;$
    }$
$
  [34mif[39;49;00m ($[34m2[39;49;00m ~ [33m/all/[39;49;00m)$
    { [37m# This is the cpu info[39;49;00m$
      [34mprint[39;49;00m $[34m3[39;49;00m > [36mFILENAME[39;49;00m[33m".cpu.user.dat"[39;49;00m;$
[37m#^I  print $4 > FILENAME".cpu.nice.dat";[39;49;00m$
      [34mprint[39;49;00m $[34m5[39;49;00m > [36mFILENAME[39;49;00m[33m".cpu.system.dat"[39;49;00m;$
[37m#     print $6 > FILENAME".cpu.iowait.dat";[39;49;00m$
      [34mprint[39;49;00m $[34m7[39;49;00m > [36mFILENAME[39;49;00m[33m".cpu.idle.dat"[39;49;00m;$
      [34mprint[39;49;00m [34m100[39;49;00m-$[34m7[39;49;00m > [36mFILENAME[39;49;00m[33m".cpu.busy.dat"[39;49;00m;$
    }$
  [34mif[39;49;00m ($[34m2[39;49;00m ~ [33m/eth0/[39;49;00m)$
    { [37m# This is the eth0 network info[39;49;00m$
      [34mif[39;49;00m ($[34m3[39;49;00m > network_max_packet_per_second)$
^I[34mprint[39;49;00m last3 > [36mFILENAME[39;49;00m[33m".net.rxpck.dat"[39;49;00m; [37m# Total number of packets received per second.[39;49;00m$
      [34melse[39;49;00m$
^I{$
^I  last3 = $[34m3[39;49;00m;$
^I  [34mprint[39;49;00m $[34m3[39;49;00m > [36mFILENAME[39;49;00m[33m".net.rxpck.dat"[39;49;00m; [37m# Total number of packets received per second.[39;49;00m$
^I}$
      [34mif[39;49;00m ($[34m4[39;49;00m > network_max_packet_per_second)$
^I[34mprint[39;49;00m last4 > [36mFILENAME[39;49;00m[33m".net.txpck.dat"[39;49;00m; [37m# Total number of packets transmitted per second.[39;49;00m$
      [34melse[39;49;00m$
^I{$
^I  last4 = $[34m4[39;49;00m;$
^I  [34mprint[39;49;00m $[34m4[39;49;00m > [36mFILENAME[39;49;00m[33m".net.txpck.dat"[39;49;00m; [37m# Total number of packets transmitted per second.[39;49;00m$
^I}$
      [34mif[39;49;00m ($[34m5[39;49;00m > network_max_bandwidth_in_byte)$
^I[34mprint[39;49;00m last5 > [36mFILENAME[39;49;00m[33m".net.rxbyt.dat"[39;49;00m; [37m# Total number of bytes received per second.[39;49;00m$
      [34melse[39;49;00m$
^I{$
^I  last5 = $[34m5[39;49;00m;$
^I  [34mprint[39;49;00m $[34m5[39;49;00m > [36mFILENAME[39;49;00m[33m".net.rxbyt.dat"[39;49;00m; [37m# Total number of bytes received per second.[39;49;00m$
^I}$
      [34mif[39;49;00m ($[34m6[39;49;00m > network_max_bandwidth_in_byte)$
^I[34mprint[39;49;00m last6 > [36mFILENAME[39;49;00m[33m".net.txbyt.dat"[39;49;00m; [37m# Total number of bytes transmitted per second.[39;49;00m$
      [34melse[39;49;00m$
^I{$
^I  last6 = $[34m6[39;49;00m;$
^I  [34mprint[39;49;00m $[34m6[39;49;00m > [36mFILENAME[39;49;00m[33m".net.txbyt.dat"[39;49;00m; [37m# Total number of bytes transmitted per second.[39;49;00m$
^I}$
[37m#     print $7 > FILENAME".net.rxcmp.dat"; # Number of compressed packets received per second (for cslip etc.).[39;49;00m$
[37m#     print $8 > FILENAME".net.txcmp.dat"; # Number of compressed packets transmitted per second.[39;49;00m$
[37m#     print $9 > FILENAME".net.rxmcst.dat"; # Number of multicast packets received per second.[39;49;00m$
    }$
$
  [37m# Detect which is the next info to be parsed[39;49;00m$
  [34mif[39;49;00m ($[34m2[39;49;00m ~ [33m/proc|cswch|tps|kbmemfree|totsck/[39;49;00m)$
    {$
      n = $[34m2[39;49;00m;$
    }$
$
  [37m# Only get lines with numbers (real data !)[39;49;00m$
  [34mif[39;49;00m ($[34m2[39;49;00m ~ [33m/[0-9]/[39;49;00m)$
    {$
      [34mif[39;49;00m (n == [33m"proc/s"[39;49;00m)$
^I{ [37m# This is the proc/s info[39;49;00m$
^I  [34mprint[39;49;00m $[34m2[39;49;00m > [36mFILENAME[39;49;00m[33m".proc.dat"[39;49;00m;$
[37m#^I  n = "";[39;49;00m$
^I}$
      [34mif[39;49;00m (n == [33m"cswch/s"[39;49;00m)$
^I{ [37m# This is the context switches per second info[39;49;00m$
^I  [34mprint[39;49;00m $[34m2[39;49;00m > [36mFILENAME[39;49;00m[33m".ctxsw.dat"[39;49;00m;$
[37m#^I  n = "";[39;49;00m$
^I}$
      [34mif[39;49;00m (n == [33m"tps"[39;49;00m)$
^I{ [37m# This is the disk info[39;49;00m$
^I  [34mprint[39;49;00m $[34m2[39;49;00m > [36mFILENAME[39;49;00m[33m".disk.tps.dat"[39;49;00m; [37m# total transfers per second[39;49;00m$
^I  [34mprint[39;49;00m $[34m3[39;49;00m > [36mFILENAME[39;49;00m[33m".disk.rtps.dat"[39;49;00m; [37m# read requests per second[39;49;00m$
^I  [34mprint[39;49;00m $[34m4[39;49;00m > [36mFILENAME[39;49;00m[33m".disk.wtps.dat"[39;49;00m; [37m# write requests per second[39;49;00m$
^I  [34mprint[39;49;00m $[34m5[39;49;00m > [36mFILENAME[39;49;00m[33m".disk.brdps.dat"[39;49;00m; [37m# block reads per second[39;49;00m$
^I  [34mprint[39;49;00m $[34m6[39;49;00m > [36mFILENAME[39;49;00m[33m".disk.bwrps.dat"[39;49;00m; [37m# block writes per second[39;49;00m$
[37m#^I  n = "";[39;49;00m$
^I}$
      [34mif[39;49;00m (n == [33m"kbmemfree"[39;49;00m)$
^I{ [37m# This is the mem info[39;49;00m$
^I  [34mprint[39;49;00m $[34m2[39;49;00m > [36mFILENAME[39;49;00m[33m".mem.kbmemfree.dat"[39;49;00m; [37m# Amount of free memory available in kilobytes.[39;49;00m$
^I  [34mprint[39;49;00m $[34m3[39;49;00m > [36mFILENAME[39;49;00m[33m".mem.kbmemused.dat"[39;49;00m; [37m# Amount of used memory in kilobytes. This does not take into account memory used by the kernel itself.[39;49;00m$
^I  [34mprint[39;49;00m $[34m4[39;49;00m > [36mFILENAME[39;49;00m[33m".mem.memused.dat"[39;49;00m; [37m# Percentage of used memory.[39;49;00m$
[37m#         It appears the kbmemshrd has been removed from the sysstat output - ntolia[39;49;00m$
[37m#^I  print $X > FILENAME".mem.kbmemshrd.dat"; # Amount of memory shared by the system in kilobytes.  Always zero with 2.4 kernels.[39;49;00m$
[37m#^I  print $5 > FILENAME".mem.kbbuffers.dat"; # Amount of memory used as buffers by the kernel in kilobytes.[39;49;00m$
^I  [34mprint[39;49;00m $[34m6[39;49;00m > [36mFILENAME[39;49;00m[33m".mem.kbcached.dat"[39;49;00m; [37m# Amount of memory used to cache data by the kernel in kilobytes.[39;49;00m$
[37m#^I  print $7 > FILENAME".mem.kbswpfree.dat"; # Amount of free swap space in kilobytes.[39;49;00m$
[37m#^I  print $8 > FILENAME".mem.kbswpused.dat"; # Amount of used swap space in kilobytes.[39;49;00m$
^I  [34mprint[39;49;00m $[34m9[39;49;00m > [36mFILENAME[39;49;00m[33m".mem.swpused.dat"[39;49;00m; [37m# Percentage of used swap space.[39;49;00m$
[37m#^I  n = "";[39;49;00m$
 ^I}$
      [34mif[39;49;00m (n == [33m"totsck"[39;49;00m)$
^I{ [37m# This is the socket info[39;49;00m$
^I  [34mprint[39;49;00m $[34m2[39;49;00m > [36mFILENAME[39;49;00m[33m".sock.totsck.dat"[39;49;00m; [37m# Total number of used sockets.[39;49;00m$
^I  [34mprint[39;49;00m $[34m3[39;49;00m > [36mFILENAME[39;49;00m[33m".sock.tcpsck.dat"[39;49;00m; [37m# Number of TCP sockets currently in use.[39;49;00m$
[37m#^I  print $4 > FILENAME".sock.udpsck.dat"; # Number of UDP sockets currently in use.[39;49;00m$
[37m#^I  print $5 > FILENAME".sock.rawsck.dat"; # Number of RAW sockets currently in use.[39;49;00m$
[37m#^I  print $6 > FILENAME".sock.ip-frag.dat"; # Number of IP fragments currently in use.[39;49;00m$
[37m#^I  n = "";[39;49;00m$
 ^I}$
    }$
}$
[36mEND[39;49;00m {$
  [34mprint[39;49;00m [33m" '"[39;49;00m [36mFILENAME[39;49;00m [33m"' done."[39;49;00m;$
}$
