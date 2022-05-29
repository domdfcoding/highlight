Using lexer <pygments.lexers.DgLexer with {'ensurenl': False, 'tabsize': 0}>
[34mimport[39;49;00m [33m'[39;49;00m[33m/re[39;49;00m[33m'[39;49;00m
[34mimport[39;49;00m [33m'[39;49;00m[33m/sys[39;49;00m[33m'[39;49;00m


[37m# IPv6address    =  hexpart [ ":" IPv4address ][39;49;00m
[37m# IPv4address    =  1*3DIGIT "." 1*3DIGIT "." 1*3DIGIT "." 1*3DIGIT[39;49;00m
[37m# hexpart        =  [ hexseq ] [ "::" [ hexseq ] ][39;49;00m
[37m# hexseq         =  hex4 *( ":" hex4)[39;49;00m
[37m# hex4           =  1*4HEXDIG[39;49;00m
hexpart = [33mr'[39;49;00m[33m({0}|)(?:::({0}|)|)[39;49;00m[33m'[39;49;00m.format [33mr'[39;49;00m[33m(?:[[39;49;00m[33m\[39;49;00m[33mda-f]{1,4})(?::[[39;49;00m[33m\[39;49;00m[33mda-f]{1,4})*[39;49;00m[33m'[39;49;00m
addrv4  = [33mr'[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33md{1,3})[39;49;00m[33m\[39;49;00m[33m.([39;49;00m[33m\[39;49;00m[33md{1,3})[39;49;00m[33m\[39;49;00m[33m.([39;49;00m[33m\[39;49;00m[33md{1,3})[39;49;00m[33m\[39;49;00m[33m.([39;49;00m[33m\[39;49;00m[33md{1,3})[39;49;00m[33m'[39;49;00m
addrv6  = re.compile $ [33mr'[39;49;00m[33m(?i)(?:{})(?::{})?$[39;49;00m[33m'[39;49;00m.format hexpart addrv4


[37m# Parse a base-N number given a list of its digits.[39;49;00m
[37m#[39;49;00m
[37m# :param q: the number of digits in that numeral system[39;49;00m
[37m#[39;49;00m
[37m# :param digits: an iterable of integers in range [0..q][39;49;00m
[37m#[39;49;00m
[37m# :return: a decimal integer[39;49;00m
[37m#[39;49;00m
base_n = q digits -> foldl (x y -> x * q + y) [34m0[39;49;00m digits


[37m# Parse a sequence of hexadecimal numbers[39;49;00m
[37m#[39;49;00m
[37m# :param q: a string of colon-separated base-16 integers[39;49;00m
[37m#[39;49;00m
[37m# :return: an iterable of Python ints[39;49;00m
[37m#[39;49;00m
unhex = q -> q [35mand[39;49;00m [36mmap[39;49;00m (p -> [36mint[39;49;00m p [34m16[39;49;00m) (q.split [33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m)


[37m# Parse an IPv6 address as specified in RFC 4291.[39;49;00m
[37m#[39;49;00m
[37m# :param address: a string, obviously.[39;49;00m
[37m#[39;49;00m
[37m# :return: an integer which, written in binary form, points to the same node.[39;49;00m
[37m#[39;49;00m
inet_pton6 = address ->
  [34mnot[39;49;00m (match = addrv6.match address) => [34mraise[39;49;00m $ [36mValueError[39;49;00m [33m'[39;49;00m[33mnot a valid IPv6 address[39;49;00m[33m'[39;49;00m
  start, end, *ipv4 = match.groups!

  is_ipv4 = [34mnot[39;49;00m $ [36mNone[39;49;00m [35min[39;49;00m ipv4
  shift   = ([34m7[39;49;00m - start.count [33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m - [34m2[39;49;00m * is_ipv4) * [34m16[39;49;00m

  (end [35mis[39;49;00m [36mNone[39;49;00m [35mand[39;49;00m shift) [35mor[39;49;00m shift < [34m0[39;49;00m => [34mraise[39;49;00m $ [36mValueError[39;49;00m [33m'[39;49;00m[33mnot a valid IPv6 address[39;49;00m[33m'[39;49;00m
  hexaddr = (base_n [34m0x10000[39;49;00m (unhex start) << shift) + base_n [34m0x10000[39;49;00m (unhex $ end [35mor[39;49;00m [33m'[39;49;00m[33m'[39;49;00m)
  [34mif[39;49;00m (is_ipv4 => (hexaddr << [34m32[39;49;00m) + base_n [34m0x100[39;49;00m ([36mmap[39;49;00m [36mint[39;49;00m ipv4)) ([34motherwise[39;49;00m => hexaddr)


inet6_type = q -> [34mif[39;49;00m
  q == [34m0[39;49;00m => [33m'[39;49;00m[33munspecified[39;49;00m[33m'[39;49;00m
  q == [34m1[39;49;00m => [33m'[39;49;00m[33mloopback[39;49;00m[33m'[39;49;00m
  (q >>  [34m32[39;49;00m)              == [34m0x000000000000ffff[39;49;00m => [33m'[39;49;00m[33mIPv4-mapped[39;49;00m[33m'[39;49;00m
  (q >>  [34m64[39;49;00m)              == [34m0xfe80000000000000[39;49;00m => [33m'[39;49;00m[33mlink-local[39;49;00m[33m'[39;49;00m
  (q >> [34m120[39;49;00m)              != [34m0x00000000000000ff[39;49;00m => [33m'[39;49;00m[33mgeneral unicast[39;49;00m[33m'[39;49;00m
  (q >> [34m112[39;49;00m) % ([34m1[39;49;00m << [34m4[39;49;00m)   == [34m0x0000000000000000[39;49;00m => [33m'[39;49;00m[33mmulticast w/ reserved scope value[39;49;00m[33m'[39;49;00m
  (q >> [34m112[39;49;00m) % ([34m1[39;49;00m << [34m4[39;49;00m)   == [34m0x000000000000000f[39;49;00m => [33m'[39;49;00m[33mmulticast w/ reserved scope value[39;49;00m[33m'[39;49;00m
  (q >> [34m112[39;49;00m) % ([34m1[39;49;00m << [34m4[39;49;00m)   == [34m0x0000000000000001[39;49;00m => [33m'[39;49;00m[33minterface-local multicast[39;49;00m[33m'[39;49;00m
  (q >> [34m112[39;49;00m) % ([34m1[39;49;00m << [34m4[39;49;00m)   == [34m0x0000000000000004[39;49;00m => [33m'[39;49;00m[33madmin-local multicast[39;49;00m[33m'[39;49;00m
  (q >> [34m112[39;49;00m) % ([34m1[39;49;00m << [34m4[39;49;00m)   == [34m0x0000000000000005[39;49;00m => [33m'[39;49;00m[33msite-local multicast[39;49;00m[33m'[39;49;00m
  (q >> [34m112[39;49;00m) % ([34m1[39;49;00m << [34m4[39;49;00m)   == [34m0x0000000000000008[39;49;00m => [33m'[39;49;00m[33morganization-local multicast[39;49;00m[33m'[39;49;00m
  (q >> [34m112[39;49;00m) % ([34m1[39;49;00m << [34m4[39;49;00m)   == [34m0x000000000000000e[39;49;00m => [33m'[39;49;00m[33mglobal multicast[39;49;00m[33m'[39;49;00m
  (q >> [34m112[39;49;00m) % ([34m1[39;49;00m << [34m4[39;49;00m)   != [34m0x0000000000000002[39;49;00m => [33m'[39;49;00m[33mmulticast w/ unknown scope value[39;49;00m[33m'[39;49;00m
  (q >>  [34m24[39;49;00m) % ([34m1[39;49;00m << [34m112[39;49;00m) == [34m0x00000000000001ff[39;49;00m => [33m'[39;49;00m[33msolicited-node multicast[39;49;00m[33m'[39;49;00m
  [34motherwise[39;49;00m => [33m'[39;49;00m[33mlink-local multicast[39;49;00m[33m'[39;49;00m


[36mprint[39;49;00m $ (x -> inet6_type x, [36mhex[39;49;00m x) $ inet_pton6 $ sys.stdin.read!.strip!
