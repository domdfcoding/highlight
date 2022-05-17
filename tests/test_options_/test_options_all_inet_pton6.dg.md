     1^I[34mimport[39;49;00m [33m'[39;49;00m[33m/re[39;49;00m[33m'[39;49;00m$
     2^I[34mimport[39;49;00m [33m'[39;49;00m[33m/sys[39;49;00m[33m'[39;49;00m$
     3^I$
     4^I$
     5^I[37m# IPv6address    =  hexpart [ ":" IPv4address ][39;49;00m$
     6^I[37m# IPv4address    =  1*3DIGIT "." 1*3DIGIT "." 1*3DIGIT "." 1*3DIGIT[39;49;00m$
     7^I[37m# hexpart        =  [ hexseq ] [ "::" [ hexseq ] ][39;49;00m$
     8^I[37m# hexseq         =  hex4 *( ":" hex4)[39;49;00m$
     9^I[37m# hex4           =  1*4HEXDIG[39;49;00m$
    10^Ihexpart = [33mr'[39;49;00m[33m({0}|)(?:::({0}|)|)[39;49;00m[33m'[39;49;00m.format [33mr'[39;49;00m[33m(?:[[39;49;00m[33m\[39;49;00m[33mda-f]{1,4})(?::[[39;49;00m[33m\[39;49;00m[33mda-f]{1,4})*[39;49;00m[33m'[39;49;00m$
    11^Iaddrv4  = [33mr'[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33md{1,3})[39;49;00m[33m\[39;49;00m[33m.([39;49;00m[33m\[39;49;00m[33md{1,3})[39;49;00m[33m\[39;49;00m[33m.([39;49;00m[33m\[39;49;00m[33md{1,3})[39;49;00m[33m\[39;49;00m[33m.([39;49;00m[33m\[39;49;00m[33md{1,3})[39;49;00m[33m'[39;49;00m$
    12^Iaddrv6  = re.compile $ [33mr'[39;49;00m[33m(?i)(?:{})(?::{})?$[39;49;00m[33m'[39;49;00m.format hexpart addrv4$
    13^I$
    14^I$
    15^I[37m# Parse a base-N number given a list of its digits.[39;49;00m$
    16^I[37m#[39;49;00m$
    17^I[37m# :param q: the number of digits in that numeral system[39;49;00m$
    18^I[37m#[39;49;00m$
    19^I[37m# :param digits: an iterable of integers in range [0..q][39;49;00m$
    20^I[37m#[39;49;00m$
    21^I[37m# :return: a decimal integer[39;49;00m$
    22^I[37m#[39;49;00m$
    23^Ibase_n = q digits -> foldl (x y -> x * q + y) [34m0[39;49;00m digits$
    24^I$
    25^I$
    26^I[37m# Parse a sequence of hexadecimal numbers[39;49;00m$
    27^I[37m#[39;49;00m$
    28^I[37m# :param q: a string of colon-separated base-16 integers[39;49;00m$
    29^I[37m#[39;49;00m$
    30^I[37m# :return: an iterable of Python ints[39;49;00m$
    31^I[37m#[39;49;00m$
    32^Iunhex = q -> q [35mand[39;49;00m [36mmap[39;49;00m (p -> [36mint[39;49;00m p [34m16[39;49;00m) (q.split [33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m)$
    33^I$
    34^I$
    35^I[37m# Parse an IPv6 address as specified in RFC 4291.[39;49;00m$
    36^I[37m#[39;49;00m$
    37^I[37m# :param address: a string, obviously.[39;49;00m$
    38^I[37m#[39;49;00m$
    39^I[37m# :return: an integer which, written in binary form, points to the same node.[39;49;00m$
    40^I[37m#[39;49;00m$
    41^Iinet_pton6 = address ->$
    42^I  [34mnot[39;49;00m (match = addrv6.match address) => [34mraise[39;49;00m $ [36mValueError[39;49;00m [33m'[39;49;00m[33mnot a valid IPv6 address[39;49;00m[33m'[39;49;00m$
    43^I  start, end, *ipv4 = match.groups!$
    44^I$
    45^I  is_ipv4 = [34mnot[39;49;00m $ [36mNone[39;49;00m [35min[39;49;00m ipv4$
    46^I  shift   = ([34m7[39;49;00m - start.count [33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m - [34m2[39;49;00m * is_ipv4) * [34m16[39;49;00m$
    47^I$
    48^I  (end [35mis[39;49;00m [36mNone[39;49;00m [35mand[39;49;00m shift) [35mor[39;49;00m shift < [34m0[39;49;00m => [34mraise[39;49;00m $ [36mValueError[39;49;00m [33m'[39;49;00m[33mnot a valid IPv6 address[39;49;00m[33m'[39;49;00m$
    49^I  hexaddr = (base_n [34m0x10000[39;49;00m (unhex start) << shift) + base_n [34m0x10000[39;49;00m (unhex $ end [35mor[39;49;00m [33m'[39;49;00m[33m'[39;49;00m)$
    50^I  [34mif[39;49;00m (is_ipv4 => (hexaddr << [34m32[39;49;00m) + base_n [34m0x100[39;49;00m ([36mmap[39;49;00m [36mint[39;49;00m ipv4)) ([34motherwise[39;49;00m => hexaddr)$
    51^I$
    52^I$
    53^Iinet6_type = q -> [34mif[39;49;00m$
    54^I  q == [34m0[39;49;00m => [33m'[39;49;00m[33munspecified[39;49;00m[33m'[39;49;00m$
    55^I  q == [34m1[39;49;00m => [33m'[39;49;00m[33mloopback[39;49;00m[33m'[39;49;00m$
    56^I  (q >>  [34m32[39;49;00m)              == [34m0x000000000000ffff[39;49;00m => [33m'[39;49;00m[33mIPv4-mapped[39;49;00m[33m'[39;49;00m$
    57^I  (q >>  [34m64[39;49;00m)              == [34m0xfe80000000000000[39;49;00m => [33m'[39;49;00m[33mlink-local[39;49;00m[33m'[39;49;00m$
    58^I  (q >> [34m120[39;49;00m)              != [34m0x00000000000000ff[39;49;00m => [33m'[39;49;00m[33mgeneral unicast[39;49;00m[33m'[39;49;00m$
    59^I  (q >> [34m112[39;49;00m) % ([34m1[39;49;00m << [34m4[39;49;00m)   == [34m0x0000000000000000[39;49;00m => [33m'[39;49;00m[33mmulticast w/ reserved scope value[39;49;00m[33m'[39;49;00m$
    60^I  (q >> [34m112[39;49;00m) % ([34m1[39;49;00m << [34m4[39;49;00m)   == [34m0x000000000000000f[39;49;00m => [33m'[39;49;00m[33mmulticast w/ reserved scope value[39;49;00m[33m'[39;49;00m$
    61^I  (q >> [34m112[39;49;00m) % ([34m1[39;49;00m << [34m4[39;49;00m)   == [34m0x0000000000000001[39;49;00m => [33m'[39;49;00m[33minterface-local multicast[39;49;00m[33m'[39;49;00m$
    62^I  (q >> [34m112[39;49;00m) % ([34m1[39;49;00m << [34m4[39;49;00m)   == [34m0x0000000000000004[39;49;00m => [33m'[39;49;00m[33madmin-local multicast[39;49;00m[33m'[39;49;00m$
    63^I  (q >> [34m112[39;49;00m) % ([34m1[39;49;00m << [34m4[39;49;00m)   == [34m0x0000000000000005[39;49;00m => [33m'[39;49;00m[33msite-local multicast[39;49;00m[33m'[39;49;00m$
    64^I  (q >> [34m112[39;49;00m) % ([34m1[39;49;00m << [34m4[39;49;00m)   == [34m0x0000000000000008[39;49;00m => [33m'[39;49;00m[33morganization-local multicast[39;49;00m[33m'[39;49;00m$
    65^I  (q >> [34m112[39;49;00m) % ([34m1[39;49;00m << [34m4[39;49;00m)   == [34m0x000000000000000e[39;49;00m => [33m'[39;49;00m[33mglobal multicast[39;49;00m[33m'[39;49;00m$
    66^I  (q >> [34m112[39;49;00m) % ([34m1[39;49;00m << [34m4[39;49;00m)   != [34m0x0000000000000002[39;49;00m => [33m'[39;49;00m[33mmulticast w/ unknown scope value[39;49;00m[33m'[39;49;00m$
    67^I  (q >>  [34m24[39;49;00m) % ([34m1[39;49;00m << [34m112[39;49;00m) == [34m0x00000000000001ff[39;49;00m => [33m'[39;49;00m[33msolicited-node multicast[39;49;00m[33m'[39;49;00m$
    68^I  [34motherwise[39;49;00m => [33m'[39;49;00m[33mlink-local multicast[39;49;00m[33m'[39;49;00m$
    69^I$
    70^I$
    71^I[36mprint[39;49;00m $ (x -> inet6_type x, [36mhex[39;49;00m x) $ inet_pton6 $ sys.stdin.read!.strip!$
