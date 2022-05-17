     1^I[37m######## This example from excerpt of <http://www.catb.org/esr/terminfo/>:[39;49;00m[37m[39;49;00m$
     2^I[37m#[39;49;00m[37m[39;49;00m$
     3^I[37m#^IVersion 11.0.1[39;49;00m[37m[39;49;00m$
     4^I[37m#^I$Date: 2000/03/02 15:51:11 $[39;49;00m[37m[39;49;00m$
     5^I[37m#^Itermcap syntax[39;49;00m[37m[39;49;00m$
     6^I[37m#[39;49;00m[37m[39;49;00m$
     7^I[37m[39;49;00m$
     8^I[37m######## ANSI, UNIX CONSOLE, AND SPECIAL TYPES[39;49;00m[37m[39;49;00m$
     9^I[37m#[39;49;00m[37m[39;49;00m$
    10^I[37m# This section describes terminal classes and brands that are still[39;49;00m[37m[39;49;00m$
    11^I[37m# quite common.[39;49;00m[37m[39;49;00m$
    12^I[37m#[39;49;00m[37m[39;49;00m$
    13^I[37m[39;49;00m$
    14^I[37m#### Specials[39;49;00m[37m[39;49;00m$
    15^I[37m#[39;49;00m[37m[39;49;00m$
    16^I[37m# Special "terminals".  These are used to label tty lines when you don't[39;49;00m[37m[39;49;00m$
    17^I[37m# know what kind of terminal is on it.  The characteristics of an unknown[39;49;00m[37m[39;49;00m$
    18^I[37m# terminal are the lowest common denominator - they look about like a ti 700.[39;49;00m[37m[39;49;00m$
    19^I[37m#[39;49;00m[37m[39;49;00m$
    20^I[37m[39;49;00m$
    21^I[94mdumb[39;49;00m|[36m80-column dumb tty[39;49;00m:\[37m[39;49;00m$
    22^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:\[37m[39;49;00m$
    23^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:\[37m[39;49;00m$
    24^I[37m^I[39;49;00m:[04m[32mbl[39;49;00m=^G:[04m[32mcr[39;49;00m=^M:[04m[32mdo[39;49;00m=^J:[04m[32msf[39;49;00m=^J:[37m[39;49;00m$
    25^I[94munknown[39;49;00m|[36munknown terminal type[39;49;00m:\[37m[39;49;00m$
    26^I[37m^I[39;49;00m:[04m[32mgn[39;49;00m:[04m[32mtc[39;49;00m=dumb:[37m[39;49;00m$
    27^I[94mlpr[39;49;00m|[36mprinter[39;49;00m|[36mline printer[39;49;00m:\[37m[39;49;00m$
    28^I[37m^I[39;49;00m:[04m[32mbs[39;49;00m:[04m[32mhc[39;49;00m:[04m[32mos[39;49;00m:\[37m[39;49;00m$
    29^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m66[39;49;00m:\[37m[39;49;00m$
    30^I[37m^I[39;49;00m:[04m[32mbl[39;49;00m=^G:[04m[32mcr[39;49;00m=^M:[04m[32mdo[39;49;00m=^J:[04m[32mff[39;49;00m=^L:[04m[32mle[39;49;00m=^H:[04m[32msf[39;49;00m=^J:[37m[39;49;00m$
    31^I[94mglasstty[39;49;00m|[36mclassic glass tty interpreting ASCII control characters[39;49;00m:\[37m[39;49;00m$
    32^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbs[39;49;00m:\[37m[39;49;00m$
    33^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:\[37m[39;49;00m$
    34^I[37m^I[39;49;00m:[04m[32mbl[39;49;00m=^G:[04m[32mcl[39;49;00m=^L:[04m[32mcr[39;49;00m=^M:[04m[32mdo[39;49;00m=^J:[04m[32mkd[39;49;00m=^J:[04m[32mkl[39;49;00m=^H:[04m[32mle[39;49;00m=^H:[04m[32mnw[39;49;00m=^M^J:[04m[32mta[39;49;00m=^I:[37m[39;49;00m$
    35^I[94mvanilla[39;49;00m:\[37m[39;49;00m$
    36^I[37m^I[39;49;00m:[04m[32mbs[39;49;00m:\[37m[39;49;00m$
    37^I[37m^I[39;49;00m:[04m[32mbl[39;49;00m=^G:[04m[32mcr[39;49;00m=^M:[04m[32mdo[39;49;00m=^J:[04m[32msf[39;49;00m=^J:[37m[39;49;00m$
    38^I[37m[39;49;00m$
    39^I[37m#### ANSI.SYS/ISO 6429/ECMA-48 Capabilities[39;49;00m[37m[39;49;00m$
    40^I[37m#[39;49;00m[37m[39;49;00m$
    41^I[37m# See the end-of-file comment for more on these.[39;49;00m[37m[39;49;00m$
    42^I[37m#[39;49;00m[37m[39;49;00m$
    43^I[37m[39;49;00m$
    44^I[37m# ANSI capabilities are broken up into pieces, so that a terminal[39;49;00m[37m[39;49;00m$
    45^I[37m# implementing some ANSI subset can use many of them.[39;49;00m[37m[39;49;00m$
    46^I[94mansi+local1[39;49;00m:\[37m[39;49;00m$
    47^I[37m^I[39;49;00m:[04m[32mdo[39;49;00m=\E[B:[04m[32mle[39;49;00m=\E[D:[04m[32mnd[39;49;00m=\E[C:[04m[32mup[39;49;00m=\E[A:[37m[39;49;00m$
    48^I[94mansi+local[39;49;00m:\[37m[39;49;00m$
    49^I[37m^I[39;49;00m:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mUP[39;49;00m=\E[%dA:[04m[32mtc[39;49;00m=ansi+local1:[37m[39;49;00m$
    50^I[94mansi+tabs[39;49;00m:\[37m[39;49;00m$
    51^I[37m^I[39;49;00m:[04m[32mbt[39;49;00m=\E[Z:[04m[32mct[39;49;00m=\E[2g:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:[37m[39;49;00m$
    52^I[94mansi+inittabs[39;49;00m:\[37m[39;49;00m$
    53^I[37m^I[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mtc[39;49;00m=ansi+tabs:[37m[39;49;00m$
    54^I[94mansi+erase[39;49;00m:\[37m[39;49;00m$
    55^I[37m^I[39;49;00m:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[J:[37m[39;49;00m$
    56^I[94mansi+rca[39;49;00m:\[37m[39;49;00m$
    57^I[37m^I[39;49;00m:[04m[32mch[39;49;00m=\E[%+^AG:[04m[32mcv[39;49;00m=\E[%+^Ad:[37m[39;49;00m$
    58^I[94mansi+cup[39;49;00m:\[37m[39;49;00m$
    59^I[37m^I[39;49;00m:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mho[39;49;00m=\E[H:[37m[39;49;00m$
    60^I[94mansi+rep[39;49;00m:\[37m[39;49;00m$
    61^I[37m^I[39;49;00m:[04m[32m..rp[39;49;00m=%p1%c\E[%p2%{1}%-%db:[37m[39;49;00m$
    62^I[94mansi+idl1[39;49;00m:\[37m[39;49;00m$
    63^I[37m^I[39;49;00m:[04m[32mal[39;49;00m=\E[L:[04m[32mdl[39;49;00m=\E[M:[37m[39;49;00m$
    64^I[94mansi+idl[39;49;00m:\[37m[39;49;00m$
    65^I[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mtc[39;49;00m=ansi+idl1:[37m[39;49;00m$
    66^I[94mansi+idc[39;49;00m:\[37m[39;49;00m$
    67^I[37m^I[39;49;00m:[04m[32mIC[39;49;00m=\E[%d@:[04m[32mdc[39;49;00m=\E[P:[04m[32mei[39;49;00m=\E6:[04m[32mic[39;49;00m=\E[@:[04m[32mim[39;49;00m=\E6:[37m[39;49;00m$
    68^I[94mansi+arrows[39;49;00m:\[37m[39;49;00m$
    69^I[37m^I[39;49;00m:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[H:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[37m[39;49;00m$
    70^I[94mansi+sgr[39;49;00m|[36mansi graphic renditions[39;49;00m:\[37m[39;49;00m$
    71^I[37m^I[39;49;00m:[04m[32mmb[39;49;00m=\E[5m:[04m[32mme[39;49;00m=\E[0m:[04m[32mmk[39;49;00m=\E[8m:[04m[32mmr[39;49;00m=\E[7m:[37m[39;49;00m$
    72^I[94mansi+sgrso[39;49;00m|[36mansi standout only[39;49;00m:\[37m[39;49;00m$
    73^I[37m^I[39;49;00m:[04m[32mse[39;49;00m=\E[m:[04m[32mso[39;49;00m=\E[7m:[37m[39;49;00m$
    74^I[94mansi+sgrul[39;49;00m|[36mansi underline only[39;49;00m:\[37m[39;49;00m$
    75^I[37m^I[39;49;00m:[04m[32mue[39;49;00m=\E[m:[04m[32mus[39;49;00m=\E[4m:[37m[39;49;00m$
    76^I[94mansi+sgrbold[39;49;00m|[36mansi graphic renditions; assuming terminal has bold; not dim[39;49;00m:\[37m[39;49;00m$
    77^I[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\E[1m:\[37m[39;49;00m$
    78^I[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[%?%p1%t7;%;%?%p2%t4;%;%?%p3%t7;%;%?%p4%t5;%;%?%p6%t1;%;m:[04m[32mtc[39;49;00m=ansi+sgr:[04m[32mtc[39;49;00m=ansi+sgrso:[04m[32mtc[39;49;00m=ansi+sgrul:[37m[39;49;00m$
    79^I[94mansi+sgrdim[39;49;00m|[36mansi graphic renditions; assuming terminal has dim; not bold[39;49;00m:\[37m[39;49;00m$
    80^I[37m^I[39;49;00m:[04m[32mmh[39;49;00m=\E[2m:\[37m[39;49;00m$
    81^I[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[%?%p1%t7;%;%?%p2%t4;%;%?%p3%t7;%;%?%p4%t5;%;%?%p5%t2;%;m:[04m[32mtc[39;49;00m=ansi+sgr:[04m[32mtc[39;49;00m=ansi+sgrso:[04m[32mtc[39;49;00m=ansi+sgrul:[37m[39;49;00m$
    82^I[94mansi+pp[39;49;00m|[36mansi printer port[39;49;00m:\[37m[39;49;00m$
    83^I[37m^I[39;49;00m:[04m[32mpf[39;49;00m=\E[4i:[04m[32mpo[39;49;00m=\E[5i:[04m[32mps[39;49;00m=\E[0i:[37m[39;49;00m$
    84^I[94mansi+csr[39;49;00m|[36mansi scroll-region plus cursor save & restore[39;49;00m:\[37m[39;49;00m$
    85^I[37m^I[39;49;00m:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mrc[39;49;00m=\E8:[04m[32msc[39;49;00m=\E7:[37m[39;49;00m$
    86^I[37m[39;49;00m$
    87^I[37m# The IBM PC alternate character set.  Plug this into any Intel console entry.[39;49;00m[37m[39;49;00m$
    88^I[37m# We use \E[11m for rmacs rather than \E[12m so the <acsc> string can use the[39;49;00m[37m[39;49;00m$
    89^I[37m# ROM graphics for control characters such as the diamond, up- and down-arrow.[39;49;00m[37m[39;49;00m$
    90^I[37m# This works with the System V, Linux, and BSDI consoles.  It's a safe bet this[39;49;00m[37m[39;49;00m$
    91^I[37m# will work with any Intel console, they all seem to have inherited \E[11m[39;49;00m[37m[39;49;00m$
    92^I[37m# from the ANSI.SYS de-facto standard.[39;49;00m[37m[39;49;00m$
    93^I[94mklone+acs[39;49;00m|[36malternate character set for ansi.sys displays[39;49;00m:\[37m[39;49;00m$
    94^I[37m^I[39;49;00m:[04m[32mac[39;49;00m=+\020\054\021-\030.^Y0\333`\004a\261f\370g\361h\260j\331k\277l\332m\300n\305o~p\304q\304r\304s_t\303u\264v\301w\302x\263y\363z\362{\343|\330}\234~\376:\[37m[39;49;00m$
    95^I[37m^I[39;49;00m:[04m[32mae[39;49;00m=\E[10m:[04m[32mas[39;49;00m=\E[11m:[37m[39;49;00m$
    96^I[37m[39;49;00m$
    97^I[37m# Highlight controls corresponding to the ANSI.SYS standard.  Most [39;49;00m[37m[39;49;00m$
    98^I[37m# console drivers for Intel boxes obey these.  Makes the same assumption[39;49;00m[37m[39;49;00m$
    99^I[37m# about \E[11m as klone+acs.  True ANSI/ECMA-48 would have :se=\E[27m:,[39;49;00m[37m[39;49;00m$
   100^I[37m# :ue=\E[24m:, but this isn't a documented feature of ANSI.SYS.[39;49;00m[37m[39;49;00m$
   101^I[94mklone+sgr[39;49;00m|[36mattribute control for ansi.sys displays[39;49;00m:\[37m[39;49;00m$
   102^I[37m^I[39;49;00m:[04m[32mS2[39;49;00m=\E[11m:[04m[32mS3[39;49;00m=\E[10m:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[0;10m:\[37m[39;49;00m$
   103^I[37m^I[39;49;00m:[04m[32mmk[39;49;00m=\E[8m:[04m[32mmr[39;49;00m=\E[7m:\[37m[39;49;00m$
   104^I[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[0;10%?%p1%t;7%;%?%p2%t;4%;%?%p3%t;7%;%?%p4%t;5%;%?%p6%t;1%;%?%p7%t;8%;%?%p9%t;11%;m:\[37m[39;49;00m$
   105^I[37m^I[39;49;00m:[04m[32mse[39;49;00m=\E[m:[04m[32mso[39;49;00m=\E[7m:[04m[32mue[39;49;00m=\E[m:[04m[32mus[39;49;00m=\E[4m:\[37m[39;49;00m$
   106^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=klone+acs:[37m[39;49;00m$
   107^I[37m[39;49;00m$
   108^I[37m# Highlight controls corresponding to the ANSI.SYS standard.  *All*[39;49;00m[37m[39;49;00m$
   109^I[37m# console drivers for Intel boxes obey these.  Does not assume \E[11m will[39;49;00m[37m[39;49;00m$
   110^I[37m# work; uses \E[12m instead, which is pretty bulletproof but loses you the ACS[39;49;00m[37m[39;49;00m$
   111^I[37m# diamond and arrow characters under curses.[39;49;00m[37m[39;49;00m$
   112^I[94mklone+sgr-dumb[39;49;00m|[36mattribute control for ansi.sys displays (no ESC [ 11 m)[39;49;00m:\[37m[39;49;00m$
   113^I[37m^I[39;49;00m:[04m[32mas[39;49;00m=\E[12m:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[0;10m:[04m[32mmk[39;49;00m=\E[8m:\[37m[39;49;00m$
   114^I[37m^I[39;49;00m:[04m[32mmr[39;49;00m=\E[7m:\[37m[39;49;00m$
   115^I[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[0;10%?%p1%t;7%;%?%p2%t;4%;%?%p3%t;7%;%?%p4%t;5%;%?%p6%t;1%;%?%p7%t;8%;%?%p9%t;12%;m:\[37m[39;49;00m$
   116^I[37m^I[39;49;00m:[04m[32mse[39;49;00m=\E[m:[04m[32mso[39;49;00m=\E[7m:[04m[32mue[39;49;00m=\E[m:[04m[32mus[39;49;00m=\E[4m:\[37m[39;49;00m$
   117^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=klone+acs:[37m[39;49;00m$
   118^I[37m[39;49;00m$
   119^I[37m# KOI8-R (RFC1489) acs (alternate character set)[39;49;00m[37m[39;49;00m$
   120^I[37m# From: Qing Long <qinglong@Bolizm.ihep.su>, 24 Feb 1996.[39;49;00m[37m[39;49;00m$
   121^I[94mklone+koi8acs[39;49;00m|[36malternate character set for ansi.sys displays with KOI8 charset[39;49;00m:\[37m[39;49;00m$
   122^I[37m^I[39;49;00m:[04m[32mac[39;49;00m=+\020\054\021-\036.^_0\215`\004a\237f\234g\232h\222i\220j\205k\203l\202m\204n\212o\213p\216q\0r\217s\214t\206u\207v\210w\211x\201y\230z\231{\267|\274}L~\225:\[37m[39;49;00m$
   123^I[37m^I[39;49;00m:[04m[32mae[39;49;00m=\E[10m:[04m[32mas[39;49;00m=\E[11m:[37m[39;49;00m$
   124^I[37m[39;49;00m$
   125^I[37m# ANSI.SYS color control.  The setab/setaf caps depend on the coincidence[39;49;00m[37m[39;49;00m$
   126^I[37m# between SVr4/XPG4's color numbers and ANSI.SYS attributes.  Here are longer[39;49;00m[37m[39;49;00m$
   127^I[37m# but equivalent strings that don't rely on that coincidence:[39;49;00m[37m[39;49;00m$
   128^I[37m# setb=\E[4%?%p1%{1}%=%t4%e%p1%{3}%=%t6%e%p1%{4}%=%t1%e%p1%{6}%=%t3%e%p1%d%;m,[39;49;00m[37m[39;49;00m$
   129^I[37m# setf=\E[3%?%p1%{1}%=%t4%e%p1%{3}%=%t6%e%p1%{4}%=%t1%e%p1%{6}%=%t3%e%p1%d%;m,[39;49;00m[37m[39;49;00m$
   130^I[37m# The DOS 5 manual asserts that these sequences meet the ISO 6429 standard.[39;49;00m[37m[39;49;00m$
   131^I[37m# They match a subset of ECMA-48.[39;49;00m[37m[39;49;00m$
   132^I[94mklone+color[39;49;00m|[36mcolor control for ansi.sys and ISO6429-compatible displays[39;49;00m:\[37m[39;49;00m$
   133^I[37m^I[39;49;00m:[04m[32mCo[39;49;00m#[34m8[39;49;00m:[04m[32mNC[39;49;00m#[34m3[39;49;00m:[04m[32mpa[39;49;00m#[34m64[39;49;00m:\[37m[39;49;00m$
   134^I[37m^I[39;49;00m:[04m[32mAB[39;49;00m=\E[4%p1%dm:[04m[32mAF[39;49;00m=\E[3%p1%dm:[04m[32mop[39;49;00m=\E[37;40m:[37m[39;49;00m$
   135^I[37m[39;49;00m$
   136^I[37m# This is better than klone+color, it doesn't assume white-on-black as the[39;49;00m[37m[39;49;00m$
   137^I[37m# default color pair,  but many `ANSI' terminals don't grok the <op> cap.[39;49;00m[37m[39;49;00m$
   138^I[94mecma+color[39;49;00m|[36mcolor control for ECMA-48-compatible terminals[39;49;00m:\[37m[39;49;00m$
   139^I[37m^I[39;49;00m:[04m[32mCo[39;49;00m#[34m8[39;49;00m:[04m[32mNC[39;49;00m#[34m3[39;49;00m:[04m[32mpa[39;49;00m#[34m64[39;49;00m:\[37m[39;49;00m$
   140^I[37m^I[39;49;00m:[04m[32mAB[39;49;00m=\E[4%p1%dm:[04m[32mAF[39;49;00m=\E[3%p1%dm:[04m[32mop[39;49;00m=\E[39;49m:[37m[39;49;00m$
   141^I[37m[39;49;00m$
   142^I[37m# Attribute control for ECMA-48-compatible terminals[39;49;00m[37m[39;49;00m$
   143^I[94mecma+sgr[39;49;00m|[36mattribute capabilities for true ECMA-48 terminals[39;49;00m:\[37m[39;49;00m$
   144^I[37m^I[39;49;00m:[04m[32mse[39;49;00m=\E[27m:[04m[32mue[39;49;00m=\E[24m:\[37m[39;49;00m$
   145^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=klone+sgr:[37m[39;49;00m$
   146^I[37m[39;49;00m$
   147^I[37m# For comparison, here are all the capabilities implied by the Intel[39;49;00m[37m[39;49;00m$
   148^I[37m# Binary Compatibility Standard (level 2) that fit within terminfo.[39;49;00m[37m[39;49;00m$
   149^I[37m# For more detail on this rather pathetic standard, see the comments[39;49;00m[37m[39;49;00m$
   150^I[37m# near the end of this file.[39;49;00m[37m[39;49;00m$
   151^I[94mibcs2[39;49;00m|[36mIntel Binary Compatibility Standard prescriptions[39;49;00m:\[37m[39;49;00m$
   152^I[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mIC[39;49;00m=\E[%d@:[04m[32mLE[39;49;00m=\E[%dD:\[37m[39;49;00m$
   153^I[37m^I[39;49;00m:[04m[32mRA[39;49;00m=\E[?7l:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mS1[39;49;00m=\E=%p1%dg:[04m[32mSA[39;49;00m=\E[?7h:[04m[32mSF[39;49;00m=\E[%dS:\[37m[39;49;00m$
   154^I[37m^I[39;49;00m:[04m[32mSR[39;49;00m=\E[%dT:[04m[32mUP[39;49;00m=\E[%dA:[04m[32mbt[39;49;00m=\E[Z:[04m[32mch[39;49;00m=\E[%i%dG:[04m[32mcl[39;49;00m=\Ec:\[37m[39;49;00m$
   155^I[37m^I[39;49;00m:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mct[39;49;00m=\E[g:[04m[32mcv[39;49;00m=\E[%i%dd:[04m[32mec[39;49;00m=\E[%dX:[04m[32mei[39;49;00m=:[04m[32mim[39;49;00m=:\[37m[39;49;00m$
   156^I[37m^I[39;49;00m:[04m[32mrc[39;49;00m=\E7:[04m[32msc[39;49;00m=\E7:[04m[32mst[39;49;00m=\EH:[37m[39;49;00m$
   157^I[37m[39;49;00m$
   158^I[37m#### ANSI/ECMA-48 terminals and terminal emulators[39;49;00m[37m[39;49;00m$
   159^I[37m#[39;49;00m[37m[39;49;00m$
   160^I[37m# See near the end of this file for details on ANSI conformance.[39;49;00m[37m[39;49;00m$
   161^I[37m# Don't mess with these entries!  Lots of other entries depend on them![39;49;00m[37m[39;49;00m$
   162^I[37m#[39;49;00m[37m[39;49;00m$
   163^I[37m# This section lists entries in a least-capable to most-capable order.[39;49;00m[37m[39;49;00m$
   164^I[37m# if you're in doubt about what `ANSI' matches yours, try them in that[39;49;00m[37m[39;49;00m$
   165^I[37m# order and back off from the first that breaks.[39;49;00m[37m[39;49;00m$
   166^I[37m[39;49;00m$
   167^I[37m# ansi-mr is for ANSI terminals with ONLY relative cursor addressing[39;49;00m[37m[39;49;00m$
   168^I[37m# and more than one page of memory.  It uses local motions instead of[39;49;00m[37m[39;49;00m$
   169^I[37m# direct cursor addressing, and makes almost no assumptions. It does[39;49;00m[37m[39;49;00m$
   170^I[37m# assume auto margins, no padding and/or xon/xoff, and a 24x80 screen.[39;49;00m[37m[39;49;00m$
   171^I[94mansi-mr[39;49;00m|[36mmem rel cup ansi[39;49;00m:\[37m[39;49;00m$
   172^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m$
   173^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mtc[39;49;00m=vanilla:[04m[32mtc[39;49;00m=ansi+erase:[04m[32mtc[39;49;00m=ansi+local1:[37m[39;49;00m$
   174^I[37m[39;49;00m$
   175^I[37m# ansi-mini is a bare minimum ANSI terminal. This should work on anything, but [39;49;00m[37m[39;49;00m$
   176^I[37m# beware of screen size problems and memory relative cursor addressing.[39;49;00m[37m[39;49;00m$
   177^I[94mansi-mini[39;49;00m|[36mminimum ansi standard terminal[39;49;00m:\[37m[39;49;00m$
   178^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m$
   179^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mtc[39;49;00m=vanilla:[04m[32mtc[39;49;00m=ansi+cup:[04m[32mtc[39;49;00m=ansi+erase:[37m[39;49;00m$
   180^I[37m[39;49;00m$
   181^I[37m# ansi-mtabs adds relative addressing and minimal tab support [39;49;00m[37m[39;49;00m$
   182^I[94mansi-mtabs[39;49;00m|[36many ansi terminal with pessimistic assumptions[39;49;00m:\[37m[39;49;00m$
   183^I[37m^I[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:\[37m[39;49;00m$
   184^I[37m^I[39;49;00m:[04m[32mta[39;49;00m=^I:[04m[32mtc[39;49;00m=ansi+local1:[04m[32mtc[39;49;00m=ansi-mini:[37m[39;49;00m$
   185^I[37m[39;49;00m$
   186^I[37m# ANSI X3.64 from emory!mlhhh (Hugh Hansard) via BRL[39;49;00m[37m[39;49;00m$
   187^I[37m#[39;49;00m[37m[39;49;00m$
   188^I[37m# The following is an entry for the full ANSI 3.64 (1977).  It lacks[39;49;00m[37m[39;49;00m$
   189^I[37m# padding, but most terminals using the standard are "fast" enough[39;49;00m[37m[39;49;00m$
   190^I[37m# not to require any -- even at 9600 bps.  If you encounter problems,[39;49;00m[37m[39;49;00m$
   191^I[37m# try including the padding specifications.[39;49;00m[37m[39;49;00m$
   192^I[37m#[39;49;00m[37m[39;49;00m$
   193^I[37m# Note: the :as: and :ae: specifications are not implemented here, for[39;49;00m[37m[39;49;00m$
   194^I[37m# the available termcap documentation does not make clear WHICH alternate[39;49;00m[37m[39;49;00m$
   195^I[37m# character set to specify.  ANSI 3.64 seems to make allowances for several.[39;49;00m[37m[39;49;00m$
   196^I[37m# Please make the appropriate adjustments to fit your needs -- that is[39;49;00m[37m[39;49;00m$
   197^I[37m# if you will be using alternate character sets.[39;49;00m[37m[39;49;00m$
   198^I[37m#[39;49;00m[37m[39;49;00m$
   199^I[37m# There are very few terminals running the full ANSI 3.64 standard,[39;49;00m[37m[39;49;00m$
   200^I[37m# so I could only test this entry on one verified terminal (Visual 102).[39;49;00m[37m[39;49;00m$
   201^I[37m# I would appreciate the results on other terminals sent to me.[39;49;00m[37m[39;49;00m$
   202^I[37m#[39;49;00m[37m[39;49;00m$
   203^I[37m# Please report comments, changes, and problems to:[39;49;00m[37m[39;49;00m$
   204^I[37m#[39;49;00m[37m[39;49;00m$
   205^I[37m# U.S. MAIL:   Hugh Hansard[39;49;00m[37m[39;49;00m$
   206^I[37m#              Box: 22830[39;49;00m[37m[39;49;00m$
   207^I[37m#              Emory University[39;49;00m[37m[39;49;00m$
   208^I[37m#              Atlanta, GA. 30322.[39;49;00m[37m[39;49;00m$
   209^I[37m#[39;49;00m[37m[39;49;00m$
   210^I[37m# USENET {akgua,msdc,sb1,sb6,gatech}!emory!mlhhh.[39;49;00m[37m[39;49;00m$
   211^I[37m#[39;49;00m[37m[39;49;00m$
   212^I[37m# (Added vt100 :rc:,:sc: to quiet a tic warning --esr)[39;49;00m[37m[39;49;00m$
   213^I[94mansi77[39;49;00m|[36mansi 3.64 standard 1977 version[39;49;00m:\[37m[39;49;00m$
   214^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbs[39;49;00m:[04m[32mmi[39;49;00m:\[37m[39;49;00m$
   215^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:\[37m[39;49;00m$
   216^I[37m^I[39;49;00m:[04m[32mal[39;49;00m=5*\E[L:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[;H\E[2J:\[37m[39;49;00m$
   217^I[37m^I[39;49;00m:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=5*\E[M:\[37m[39;49;00m$
   218^I[37m^I[39;49;00m:[04m[32mdo[39;49;00m=\E[B:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:[04m[32mim[39;49;00m=\E[4h:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:\[37m[39;49;00m$
   219^I[37m^I[39;49;00m:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[H:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:\[37m[39;49;00m$
   220^I[37m^I[39;49;00m:[04m[32mnd[39;49;00m=\E[C:[04m[32mnw[39;49;00m=^M\ED:[04m[32mrc[39;49;00m=\E8:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[m:[04m[32msf[39;49;00m=\ED:[04m[32mso[39;49;00m=\E[7m:\[37m[39;49;00m$
   221^I[37m^I[39;49;00m:[04m[32msr[39;49;00m=\EM:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:[37m[39;49;00m$
   222^I[37m[39;49;00m$
   223^I[37m# Procomm and some other ANSI emulations don't recognize all of the ANSI-[39;49;00m[37m[39;49;00m$
   224^I[37m# standard capabilities.  This entry deletes :UP:, :RI:, :DO:, :LE:, and [39;49;00m[37m[39;49;00m$
   225^I[37m# <vpa>/<hpa> capabilities, forcing curses to use repetitions of :up:, [39;49;00m[37m[39;49;00m$
   226^I[37m# :nd:, :do: and :le:.  Also deleted :IC: and :ic:, as QModem up to [39;49;00m[37m[39;49;00m$
   227^I[37m# 5.03 doesn't recognize these.  Finally, we delete :rp: and :sr:, which seem[39;49;00m[37m[39;49;00m$
   228^I[37m# to confuse many emulators.  On the other hand, we can count on these programs[39;49;00m[37m[39;49;00m$
   229^I[37m# doing :ae:/:as:/:sa:. Older versions of this entry featured [39;49;00m[37m[39;49;00m$
   230^I[37m# <invis=\E[9m>, but <invis=\E[8m> now seems to be more common under[39;49;00m[37m[39;49;00m$
   231^I[37m# ANSI.SYS influence.[39;49;00m[37m[39;49;00m$
   232^I[37m# From: Eric S. Raymond <esr@snark.thyrsus.com> Oct 30 1995[39;49;00m[37m[39;49;00m$
   233^I[94mpcansi-m[39;49;00m|[36mpcansi-mono[39;49;00m|[36mibm-pc terminal programs claiming to be ansi (mono mode)[39;49;00m:\[37m[39;49;00m$
   234^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbs[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mms[39;49;00m:\[37m[39;49;00m$
   235^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:\[37m[39;49;00m$
   236^I[37m^I[39;49;00m:[04m[32mal[39;49;00m=\E[L:[04m[32mbl[39;49;00m=^G:[04m[32mbt[39;49;00m=\E[Z:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[J:\[37m[39;49;00m$
   237^I[37m^I[39;49;00m:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mct[39;49;00m=\E[2g:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=\E[B:\[37m[39;49;00m$
   238^I[37m^I[39;49;00m:[04m[32mho[39;49;00m=\E[H:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[H:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:\[37m[39;49;00m$
   239^I[37m^I[39;49;00m:[04m[32mle[39;49;00m=\E[D:[04m[32mnd[39;49;00m=\E[C:[04m[32msf[39;49;00m=^J:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:[04m[32mup[39;49;00m=\E[A:\[37m[39;49;00m$
   240^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=klone+sgr-dumb:[37m[39;49;00m$
   241^I[94mpcansi-25-m[39;49;00m|[36mpcansi25m[39;49;00m|[36mibm-pc terminal programs with 25 lines (mono mode)[39;49;00m:\[37m[39;49;00m$
   242^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:[04m[32mtc[39;49;00m=pcansi-m:[37m[39;49;00m$
   243^I[94mpcansi-33-m[39;49;00m|[36mpcansi33m[39;49;00m|[36mibm-pc terminal programs with 33 lines (mono mode)[39;49;00m:\[37m[39;49;00m$
   244^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m33[39;49;00m:[04m[32mtc[39;49;00m=pcansi-m:[37m[39;49;00m$
   245^I[94mpcansi-43-m[39;49;00m|[36mansi43m[39;49;00m|[36mibm-pc terminal programs with 43 lines (mono mode)[39;49;00m:\[37m[39;49;00m$
   246^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m43[39;49;00m:[04m[32mtc[39;49;00m=pcansi-m:[37m[39;49;00m$
   247^I[37m# The color versions.  All PC emulators do color...[39;49;00m[37m[39;49;00m$
   248^I[94mpcansi[39;49;00m|[36mibm-pc terminal programs claiming to be ansi[39;49;00m:\[37m[39;49;00m$
   249^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=klone+color:[04m[32mtc[39;49;00m=pcansi-m:[37m[39;49;00m$
   250^I[94mpcansi-25[39;49;00m|[36mpcansi25[39;49;00m|[36mibm-pc terminal programs with 25 lines[39;49;00m:\[37m[39;49;00m$
   251^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:[04m[32mtc[39;49;00m=pcansi:[37m[39;49;00m$
   252^I[94mpcansi-33[39;49;00m|[36mpcansi33[39;49;00m|[36mibm-pc terminal programs with 33 lines[39;49;00m:\[37m[39;49;00m$
   253^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m33[39;49;00m:[04m[32mtc[39;49;00m=pcansi:[37m[39;49;00m$
   254^I[94mpcansi-43[39;49;00m|[36mpcansi43[39;49;00m|[36mibm-pc terminal programs with 43 lines[39;49;00m:\[37m[39;49;00m$
   255^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m43[39;49;00m:[04m[32mtc[39;49;00m=pcansi:[37m[39;49;00m$
   256^I[37m[39;49;00m$
   257^I[37m# ansi-m -- full ANSI X3.64 with ANSI.SYS-compatible attributes, no color.[39;49;00m[37m[39;49;00m$
   258^I[37m# If you want pound signs rather than dollars, replace `B' with `A'[39;49;00m[37m[39;49;00m$
   259^I[37m# in the <s0ds>, <s1ds>, <s2ds>, and <s3ds> capabilities.[39;49;00m[37m[39;49;00m$
   260^I[37m# From: Eric S. Raymond <esr@snark.thyrsus.com> Nov 6 1995[39;49;00m[37m[39;49;00m$
   261^I[94mansi-m[39;49;00m|[36mansi-mono[39;49;00m|[36mANSI X3.64-1979 terminal with ANSI.SYS compatible attributes[39;49;00m:\[37m[39;49;00m$
   262^I[37m^I[39;49;00m:[04m[32m5i[39;49;00m:\[37m[39;49;00m$
   263^I[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mIC[39;49;00m=\E[%d@:\[37m[39;49;00m$
   264^I[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mSF[39;49;00m=\E[%dS:[04m[32mSR[39;49;00m=\E[%dT:[04m[32mUP[39;49;00m=\E[%dA:\[37m[39;49;00m$
   265^I[37m^I[39;49;00m:[04m[32mcb[39;49;00m=\E[1K:[04m[32mch[39;49;00m=\E[%i%dG:[04m[32mct[39;49;00m=\E[2g:[04m[32mcv[39;49;00m=\E[%i%dd:[04m[32mec[39;49;00m=\E[%dX:[04m[32mei[39;49;00m=:\[37m[39;49;00m$
   266^I[37m^I[39;49;00m:[04m[32mim[39;49;00m=:[04m[32mkB[39;49;00m=\E[Z:[04m[32mkI[39;49;00m=\E[L:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:\[37m[39;49;00m$
   267^I[37m^I[39;49;00m:[04m[32mnw[39;49;00m=\r\E[S:[04m[32mpf[39;49;00m=\E[4i:[04m[32mpo[39;49;00m=\E[5i:[04m[32m..rp[39;49;00m=%p1%c\E[%p2%{1}%-%db:\[37m[39;49;00m$
   268^I[37m^I[39;49;00m:[04m[32ms0[39;49;00m=\E(B:[04m[32ms1[39;49;00m=\E)B:[04m[32ms2[39;49;00m=\E*B:[04m[32ms3[39;49;00m=\E+B:[04m[32mta[39;49;00m=\E[I:\[37m[39;49;00m$
   269^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=pcansi-m:[37m[39;49;00m$
   270^I[37m[39;49;00m$
   271^I[37m# ansi -- this terminfo expresses the largest subset of X3.64 that will fit in[39;49;00m[37m[39;49;00m$
   272^I[37m# standard terminfo.  Assumes ANSI.SYS-compatible attributes and color.[39;49;00m[37m[39;49;00m$
   273^I[37m# From: Eric S. Raymond <esr@snark.thyrsus.com> Nov 6 1995[39;49;00m[37m[39;49;00m$
   274^I[94mansi[39;49;00m|[36mansi/pc-term compatible with color[39;49;00m:\[37m[39;49;00m$
   275^I[37m^I[39;49;00m:[04m[32mu6[39;49;00m=\E[%i%d;%dR:[04m[32mu7[39;49;00m=\E[6n:[04m[32m..u8[39;49;00m=\E[?%[;0123456789]c:\[37m[39;49;00m$
   276^I[37m^I[39;49;00m:[04m[32mu9[39;49;00m=\E[c:\[37m[39;49;00m$
   277^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=ecma+color:[04m[32mtc[39;49;00m=klone+sgr:[04m[32mtc[39;49;00m=ansi-m:[37m[39;49;00m$
   278^I[37m[39;49;00m$
   279^I[37m# ansi-generic is a vanilla ANSI terminal. This is assumed to implement [39;49;00m[37m[39;49;00m$
   280^I[37m# all the normal ANSI stuff with no extensions. It assumes [39;49;00m[37m[39;49;00m$
   281^I[37m# insert/delete line/char is there, so it won't work with [39;49;00m[37m[39;49;00m$
   282^I[37m# vt100 clones. It assumes video attributes for bold, blink, [39;49;00m[37m[39;49;00m$
   283^I[37m# underline, and reverse, which won't matter much if the terminal [39;49;00m[37m[39;49;00m$
   284^I[37m# can't do some of those. Padding is assumed to be zero, which [39;49;00m[37m[39;49;00m$
   285^I[37m# shouldn't hurt since xon/xoff is assumed.[39;49;00m[37m[39;49;00m$
   286^I[94mansi-generic[39;49;00m|[36mgeneric ansi standard terminal[39;49;00m:\[37m[39;49;00m$
   287^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m$
   288^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mtc[39;49;00m=vanilla:[04m[32mtc[39;49;00m=ansi+csr:[04m[32mtc[39;49;00m=ansi+cup:\[37m[39;49;00m$
   289^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=ansi+rca:[04m[32mtc[39;49;00m=ansi+erase:[04m[32mtc[39;49;00m=ansi+tabs:[04m[32mtc[39;49;00m=ansi+local:\[37m[39;49;00m$
   290^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=ansi+idc:[04m[32mtc[39;49;00m=ansi+idl:[04m[32mtc[39;49;00m=ansi+rep:[04m[32mtc[39;49;00m=ansi+sgrbold:\[37m[39;49;00m$
   291^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=ansi+arrows:[37m[39;49;00m$
   292^I[37m[39;49;00m$
   293^I[37m#### Linux consoles[39;49;00m[37m[39;49;00m$
   294^I[37m#[39;49;00m[37m[39;49;00m$
   295^I[37m[39;49;00m$
   296^I[37m# This entry is good for the 1.2.13 or later version of the Linux console.[39;49;00m[37m[39;49;00m$
   297^I[37m#[39;49;00m[37m[39;49;00m$
   298^I[37m# ***************************************************************************[39;49;00m[37m[39;49;00m$
   299^I[37m# *                                                                         *[39;49;00m[37m[39;49;00m$
   300^I[37m# *                           WARNING:                                      *[39;49;00m[37m[39;49;00m$
   301^I[37m# * Linuxes come with a default keyboard mapping kcbt=^I.  This entry, in   *[39;49;00m[37m[39;49;00m$
   302^I[37m# * response to user requests, assumes kcbt=\E[Z, the ANSI/ECMA reverse-tab *[39;49;00m[37m[39;49;00m$
   303^I[37m# * character. Here are the keymap replacement lines that will set this up: *[39;49;00m[37m[39;49;00m$
   304^I[37m# *                                                                         *[39;49;00m[37m[39;49;00m$
   305^I[37m#^Ikeycode  15 = Tab             Tab[39;49;00m[37m[39;49;00m$
   306^I[37m#^I^Ialt     keycode  15 = Meta_Tab[39;49;00m[37m[39;49;00m$
   307^I[37m#^I^Ishift^Ikeycode  15 = F26[39;49;00m[37m[39;49;00m$
   308^I[37m#^Istring F26 ="\033[Z"[39;49;00m[37m[39;49;00m$
   309^I[37m# *                                                                         *[39;49;00m[37m[39;49;00m$
   310^I[37m# * This has to use a key slot which is unfortunate (any unused one will    *[39;49;00m[37m[39;49;00m$
   311^I[37m# * do, F26 is the higher-numbered one).  The change ought to be built      *[39;49;00m[37m[39;49;00m$
   312^I[37m# * into the kernel tables.                                                 *[39;49;00m[37m[39;49;00m$
   313^I[37m# *                                                                         *[39;49;00m[37m[39;49;00m$
   314^I[37m# ***************************************************************************[39;49;00m[37m[39;49;00m$
   315^I[37m#[39;49;00m[37m[39;49;00m$
   316^I[37m# The 1.3.x kernels add color-change capabilities; if yours doesn't have this[39;49;00m[37m[39;49;00m$
   317^I[37m# and it matters, turn off <ccc>.  The %02x escape used to implement this is[39;49;00m[37m[39;49;00m$
   318^I[37m# not back-portable to SV curses and not supported in ncurses versions before[39;49;00m[37m[39;49;00m$
   319^I[37m# 1.9.9. All linux kernels since 1.2.13 (at least) set the screen size[39;49;00m[37m[39;49;00m$
   320^I[37m# themselves; this entry assumes that capability.[39;49;00m[37m[39;49;00m$
   321^I[37m#[39;49;00m[37m[39;49;00m$
   322^I[37m# This entry is good for the 1.2.13 or later version of the Linux console.[39;49;00m[37m[39;49;00m$
   323^I[37m#[39;49;00m[37m[39;49;00m$
   324^I[37m# ***************************************************************************[39;49;00m[37m[39;49;00m$
   325^I[37m# *                                                                         *[39;49;00m[37m[39;49;00m$
   326^I[37m# *                           WARNING:                                      *[39;49;00m[37m[39;49;00m$
   327^I[37m# * Linuxes come with a default keyboard mapping kcbt=^I.  This entry, in   *[39;49;00m[37m[39;49;00m$
   328^I[37m# * response to user requests, assumes kcbt=\E[Z, the ANSI/ECMA reverse-tab *[39;49;00m[37m[39;49;00m$
   329^I[37m# * character. Here are the keymap replacement lines that will set this up: *[39;49;00m[37m[39;49;00m$
   330^I[37m# *                                                                         *[39;49;00m[37m[39;49;00m$
   331^I[37m#^Ikeycode  15 = Tab             Tab[39;49;00m[37m[39;49;00m$
   332^I[37m#^I^Ialt     keycode  15 = Meta_Tab[39;49;00m[37m[39;49;00m$
   333^I[37m#^I^Ishift^Ikeycode  15 = F26[39;49;00m[37m[39;49;00m$
   334^I[37m#^Istring F26 ="\033[Z"[39;49;00m[37m[39;49;00m$
   335^I[37m# *                                                                         *[39;49;00m[37m[39;49;00m$
   336^I[37m# * This has to use a key slot which is unfortunate (any unused one will    *[39;49;00m[37m[39;49;00m$
   337^I[37m# * do, F26 is the higher-numbered one).  The change ought to be built      *[39;49;00m[37m[39;49;00m$
   338^I[37m# * into the kernel tables.                                                 *[39;49;00m[37m[39;49;00m$
   339^I[37m# *                                                                         *[39;49;00m[37m[39;49;00m$
   340^I[37m# ***************************************************************************[39;49;00m[37m[39;49;00m$
   341^I[37m#[39;49;00m[37m[39;49;00m$
   342^I[37m# The 1.3.x kernels add color-change capabilities; if yours doesn't have this[39;49;00m[37m[39;49;00m$
   343^I[37m# and it matters, turn off <ccc>.  The %02x escape used to implement this is[39;49;00m[37m[39;49;00m$
   344^I[37m# not back-portable to SV curses and not supported in ncurses versions before[39;49;00m[37m[39;49;00m$
   345^I[37m# 1.9.9. All linux kernels since 1.2.13 (at least) set the screen size[39;49;00m[37m[39;49;00m$
   346^I[37m# themselves; this entry assumes that capability.[39;49;00m[37m[39;49;00m$
   347^I[37m#[39;49;00m[37m[39;49;00m$
   348^I[37m# The 2.2.x kernels add a private mode that sets the cursor type; use that to[39;49;00m[37m[39;49;00m$
   349^I[37m# get a block cursor for cvvis.[39;49;00m[37m[39;49;00m$
   350^I[37m# reported by Frank Heckenbach <frank@g-n-u.de>.[39;49;00m[37m[39;49;00m$
   351^I[37m# (untranslatable capabilities removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m$
   352^I[37m# (sgr removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m$
   353^I[37m# (terminfo-only capabilities suppressed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m$
   354^I[94mlinux[39;49;00m|[36mlinux console[39;49;00m:\[37m[39;49;00m$
   355^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32meo[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mms[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m$
   356^I[37m^I[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:\[37m[39;49;00m$
   357^I[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mIC[39;49;00m=\E[%d@:[04m[32mK2[39;49;00m=\E[G:[04m[32mal[39;49;00m=\E[L:\[37m[39;49;00m$
   358^I[37m^I[39;49;00m:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:\[37m[39;49;00m$
   359^I[37m^I[39;49;00m:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mct[39;49;00m=\E[3g:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=^J:[04m[32mec[39;49;00m=\E[%dX:\[37m[39;49;00m$
   360^I[37m^I[39;49;00m:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:[04m[32mic[39;49;00m=\E[@:[04m[32mim[39;49;00m=\E[4h:[04m[32mk1[39;49;00m=\E[[A:[04m[32mk2[39;49;00m=\E[[B:\[37m[39;49;00m$
   361^I[37m^I[39;49;00m:[04m[32mk3[39;49;00m=\E[[C:[04m[32mk4[39;49;00m=\E[[D:[04m[32mk5[39;49;00m=\E[[E:[04m[32mk6[39;49;00m=\E[17~:[04m[32mk7[39;49;00m=\E[18~:[04m[32mk8[39;49;00m=\E[19~:\[37m[39;49;00m$
   362^I[37m^I[39;49;00m:[04m[32mk9[39;49;00m=\E[20~:[04m[32mkD[39;49;00m=\E[3~:[04m[32mkI[39;49;00m=\E[2~:[04m[32mkN[39;49;00m=\E[6~:[04m[32mkP[39;49;00m=\E[5~:[04m[32mkb[39;49;00m=\177:\[37m[39;49;00m$
   363^I[37m^I[39;49;00m:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[1~:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mmh[39;49;00m=\E[2m:\[37m[39;49;00m$
   364^I[37m^I[39;49;00m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mnw[39;49;00m=^M^J:[04m[32mrc[39;49;00m=\E8:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[27m:[04m[32msf[39;49;00m=^J:\[37m[39;49;00m$
   365^I[37m^I[39;49;00m:[04m[32msr[39;49;00m=\EM:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[24m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:\[37m[39;49;00m$
   366^I[37m^I[39;49;00m:[04m[32mvb[39;49;00m=200\E[?5h\E[?5l:[04m[32mve[39;49;00m=\E[?25h\E[?0c:[04m[32mvi[39;49;00m=\E[?25l\E[?1c:\[37m[39;49;00m$
   367^I[37m^I[39;49;00m:[04m[32mvs[39;49;00m=\E[?25h\E[?8c:\[37m[39;49;00m$
   368^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=klone+sgr:[04m[32mtc[39;49;00m=ecma+color:[37m[39;49;00m$
   369^I[94mlinux-m[39;49;00m|[36mLinux console no color[39;49;00m:\[37m[39;49;00m$
   370^I[37m^I[39;49;00m:[04m[32mCo@[39;49;00m:[04m[32mpa@[39;49;00m:\[37m[39;49;00m$
   371^I[37m^I[39;49;00m:[04m[32mAB@[39;49;00m:[04m[32mAF@[39;49;00m:[04m[32mSb@[39;49;00m:[04m[32mSf@[39;49;00m:[04m[32mtc[39;49;00m=linux:[37m[39;49;00m$
   372^I[94mlinux-c-nc[39;49;00m|[36mlinux console 1.3.x hack for ncurses only[39;49;00m:\[37m[39;49;00m$
   373^I[37m^I[39;49;00m:[04m[32mcc[39;49;00m:\[37m[39;49;00m$
   374^I[37m^I[39;49;00m:[04m[32m..Ic[39;49;00m=\E]P%p1%x%p2%{255}%*%{1000}%/%02x%p3%{255}%*%{1000}%/%02x%p4%{255}%*%{1000}%/%02x:\[37m[39;49;00m$
   375^I[37m^I[39;49;00m:[04m[32moc[39;49;00m=\E]R:\[37m[39;49;00m$
   376^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=linux:[37m[39;49;00m$
   377^I[37m# From: Dennis Henriksen <opus@osrl.dk>, 9 July 1996[39;49;00m[37m[39;49;00m$
   378^I[94mlinux-c[39;49;00m|[36mlinux console 1.3.6+ with private palette for each virtual console[39;49;00m:\[37m[39;49;00m$
   379^I[37m^I[39;49;00m:[04m[32mcc[39;49;00m:\[37m[39;49;00m$
   380^I[37m^I[39;49;00m:[04m[32mCo[39;49;00m#[34m8[39;49;00m:[04m[32mpa[39;49;00m#[34m64[39;49;00m:\[37m[39;49;00m$
   381^I[37m^I[39;49;00m:[04m[32m..Ic[39;49;00m=\E]P%?%p1%{9}%>%t%p1%{10}%-%'a'%+%c%e%p1%d%;%p2%{255}%&%Pr%gr%{16}%/%Px%?%gx%{9}%>%t%gx%{10}%-%'A'%+%c%e%gx%d%;%gr%{15}%&%Px%?%gx%{9}%>%t%gx%{10}%-%'A'%+%c%e%gx%d%;%p3%{255}%&%Pr%gr%{16}%/%Px%?%gx%{9}%>%t%gx%{10}%-%'A'%+%c%e%gx%d%;%gr%{15}%&%Px%?%gx%{9}%>%t%gx%{10}%-%'A'%+%c%e%gx%d%;%p4%{255}%&%Pr%gr%{16}%/%Px%?%gx%{9}%>%t%gx%{10}%-%'A'%+%c%e%gx%d%;%gr%{15}%&%Px%?%gx%{9}%>%t%gx%{10}%-%'A'%+%c%e%gx%d%;:\[37m[39;49;00m$
   382^I[37m^I[39;49;00m:[04m[32moc[39;49;00m=\E]R:\[37m[39;49;00m$
   383^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=linux:[37m[39;49;00m$
   384^I[37m[39;49;00m$
   385^I[37m# See the note on ICH/ICH1 VERSUS RMIR/SMIR near the end of file[39;49;00m[37m[39;49;00m$
   386^I[94mlinux-nic[39;49;00m|[36mlinux with ich/ich1 suppressed for non-curses programs[39;49;00m:\[37m[39;49;00m$
   387^I[37m^I[39;49;00m:[04m[32mIC@[39;49;00m:[04m[32mei[39;49;00m=:[04m[32mic@[39;49;00m:[04m[32mim[39;49;00m=:\[37m[39;49;00m$
   388^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=linux:[37m[39;49;00m$
   389^I[37m[39;49;00m$
   390^I[37m# This assumes you have used setfont(8) to load one of the Linux koi8-r fonts.[39;49;00m[37m[39;49;00m$
   391^I[37m# acsc entry from Pavel Roskin" <pavel@absolute.spb.su>, 29 Sep 1997.[39;49;00m[37m[39;49;00m$
   392^I[94mlinux-koi8[39;49;00m|[36mlinux with koi8 alternate character set[39;49;00m:\[37m[39;49;00m$
   393^I[37m^I[39;49;00m:[04m[32mac[39;49;00m=+\020\054\021-\030.^Y0\215`\004a\221f\234g\237h\220i\276j\205k\203l\202m\204n\212o~p\0q\0r\0s_t\206u\207v\211w\210x\201y\230z\231{\267|\274~\224:[04m[32mtc[39;49;00m=linux:\[37m[39;49;00m$
   394^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=klone+koi8acs:[37m[39;49;00m$
   395^I[37m[39;49;00m$
   396^I[37m# Another entry for KOI8-r with Qing Long's acsc.[39;49;00m[37m[39;49;00m$
   397^I[37m# (which one better complies with the standard?)[39;49;00m[37m[39;49;00m$
   398^I[94mlinux-koi8r[39;49;00m|[36mlinux with koi8-r alternate character set[39;49;00m:\[37m[39;49;00m$
   399^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=linux:[04m[32mtc[39;49;00m=klone+koi8acs:[37m[39;49;00m$
   400^I[37m[39;49;00m$
   401^I[37m# Entry for the latin1 and latin2 fonts[39;49;00m[37m[39;49;00m$
   402^I[94mlinux-lat[39;49;00m|[36mlinux with latin1 or latin2 alternate character set[39;49;00m:\[37m[39;49;00m$
   403^I[37m^I[39;49;00m:[04m[32mac[39;49;00m=+\020\054\021-\030.^Y0\333`\004a\013f\370g\361h\260i\316j\211k\214l\206m\203n\305o~p\304q\212r\304s_t\207u\215v\301w\302x\205y\363z\362{\343|\330}\234~\376:\[37m[39;49;00m$
   404^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=linux:[37m[39;49;00m$
   405^I[37m[39;49;00m$
   406^I[37m#### NetBSD consoles[39;49;00m[37m[39;49;00m$
   407^I[37m#[39;49;00m[37m[39;49;00m$
   408^I[37m# pcvt termcap database entries (corresponding to release 3.31)[39;49;00m[37m[39;49;00m$
   409^I[37m# Author's last edit-date: [Fri Sep 15 20:29:10 1995][39;49;00m[37m[39;49;00m$
   410^I[37m#[39;49;00m[37m[39;49;00m$
   411^I[37m# (For the terminfo master file, I translated these into terminfo syntax.[39;49;00m[37m[39;49;00m$
   412^I[37m# Then I dropped all the pseudo-HP entries. we don't want and can't use[39;49;00m[37m[39;49;00m$
   413^I[37m# the :Xs: flag. Then I split :is: into a size-independent :i1: and a[39;49;00m[37m[39;49;00m$
   414^I[37m# size-dependent :is:.  Finally, I added <rmam>/<smam> -- esr)[39;49;00m[37m[39;49;00m$
   415^I[37m[39;49;00m$
   416^I[37m# NOTE: :ic: has been taken out of this entry. for reference, it should[39;49;00m[37m[39;49;00m$
   417^I[37m# be <ich1=\E[@>.  For discussion, see ICH/ICH1 VERSUS RMIR/SMIR below.[39;49;00m[37m[39;49;00m$
   418^I[37m# (esr: added :vi: and :ve: to resolve NetBSD Problem Report #4583)[39;49;00m[37m[39;49;00m$
   419^I[94mpcvtXX[39;49;00m|[36mpcvt vt200 emulator (DEC VT220)[39;49;00m:\[37m[39;49;00m$
   420^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mkm[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mms[39;49;00m:[04m[32mxn[39;49;00m:\[37m[39;49;00m$
   421^I[37m^I[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m$
   422^I[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mIC[39;49;00m=\E[%d@:\[37m[39;49;00m$
   423^I[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRA[39;49;00m=\E[?7l:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mSA[39;49;00m=\E[?7h:[04m[32mSF[39;49;00m=\E[%dS:\[37m[39;49;00m$
   424^I[37m^I[39;49;00m:[04m[32mSR[39;49;00m=\E[%dT:[04m[32mUP[39;49;00m=\E[%dA:\[37m[39;49;00m$
   425^I[37m^I[39;49;00m:[04m[32mac[39;49;00m=++\054\054--..00``aaffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz~~:\[37m[39;49;00m$
   426^I[37m^I[39;49;00m:[04m[32mae[39;49;00m=\E(B:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=\E(0:[04m[32mbl[39;49;00m=^G:[04m[32mcb[39;49;00m=\E[1K:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:\[37m[39;49;00m$
   427^I[37m^I[39;49;00m:[04m[32mcl[39;49;00m=\E[H\E[J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:\[37m[39;49;00m$
   428^I[37m^I[39;49;00m:[04m[32mct[39;49;00m=\E[3g:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=\E[B:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:\[37m[39;49;00m$
   429^I[37m^I[39;49;00m:[04m[32mi1[39;49;00m=\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:[04m[32mim[39;49;00m=\E[4h:\[37m[39;49;00m$
   430^I[37m^I[39;49;00m:[04m[32mk1[39;49;00m=\E[17~:[04m[32mk2[39;49;00m=\E[18~:[04m[32mk3[39;49;00m=\E[19~:[04m[32mk4[39;49;00m=\E[20~:[04m[32mk5[39;49;00m=\E[21~:\[37m[39;49;00m$
   431^I[37m^I[39;49;00m:[04m[32mk6[39;49;00m=\E[23~:[04m[32mk7[39;49;00m=\E[24~:[04m[32mk8[39;49;00m=\E[25~:[04m[32mkD[39;49;00m=\E[3~:[04m[32mkH[39;49;00m=\E[4~:[04m[32mkI[39;49;00m=\E[2~:\[37m[39;49;00m$
   432^I[37m^I[39;49;00m:[04m[32mkN[39;49;00m=\E[6~:[04m[32mkP[39;49;00m=\E[5~:[04m[32mkb[39;49;00m=\177:[04m[32mkd[39;49;00m=\EOB:[04m[32mke[39;49;00m=\E[?1l\E>:[04m[32mkh[39;49;00m=\E[1~:\[37m[39;49;00m$
   433^I[37m^I[39;49;00m:[04m[32mkl[39;49;00m=\EOD:[04m[32mkr[39;49;00m=\EOC:[04m[32mks[39;49;00m=\E[?1h\E=:[04m[32mku[39;49;00m=\EOA:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:\[37m[39;49;00m$
   434^I[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mnw[39;49;00m=\EE:\[37m[39;49;00m$
   435^I[37m^I[39;49;00m:[04m[32mr1[39;49;00m=\Ec\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:[04m[32mrc[39;49;00m=\E8:\[37m[39;49;00m$
   436^I[37m^I[39;49;00m:[04m[32mrf[39;49;00m=/usr/share/tabset/vt100:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[27m:[04m[32msf[39;49;00m=\ED:\[37m[39;49;00m$
   437^I[37m^I[39;49;00m:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[24m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:\[37m[39;49;00m$
   438^I[37m^I[39;49;00m:[04m[32mve[39;49;00m=\E[?25h:[04m[32mvi[39;49;00m=\E[?25l:[37m[39;49;00m$
   439^I[37m[39;49;00m$
   440^I[37m#^INetBSD/FreeBSD vt220 terminal emulator console (pc keyboard & monitor)[39;49;00m[37m[39;49;00m$
   441^I[37m#^Itermcap entries for pure VT220-Emulation and 25, 28, 35, 40, 43 and[39;49;00m[37m[39;49;00m$
   442^I[37m#^I50 lines entries; 80 columns[39;49;00m[37m[39;49;00m$
   443^I[94mpcvt25[39;49;00m|[36mdec vt220 emulation with 25 lines[39;49;00m:\[37m[39;49;00m$
   444^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:\[37m[39;49;00m$
   445^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;25r\E[25;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m$
   446^I[94mpcvt28[39;49;00m|[36mdec vt220 emulation with 28 lines[39;49;00m:\[37m[39;49;00m$
   447^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m28[39;49;00m:\[37m[39;49;00m$
   448^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;28r\E[28;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m$
   449^I[94mpcvt35[39;49;00m|[36mdec vt220 emulation with 35 lines[39;49;00m:\[37m[39;49;00m$
   450^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m35[39;49;00m:\[37m[39;49;00m$
   451^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;35r\E[35;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m$
   452^I[94mpcvt40[39;49;00m|[36mdec vt220 emulation with 40 lines[39;49;00m:\[37m[39;49;00m$
   453^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m40[39;49;00m:\[37m[39;49;00m$
   454^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;40r\E[40;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m$
   455^I[94mpcvt43[39;49;00m|[36mdec vt220 emulation with 43 lines[39;49;00m:\[37m[39;49;00m$
   456^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m43[39;49;00m:\[37m[39;49;00m$
   457^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;43r\E[43;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m$
   458^I[94mpcvt50[39;49;00m|[36mdec vt220 emulation with 50 lines[39;49;00m:\[37m[39;49;00m$
   459^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:\[37m[39;49;00m$
   460^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;50r\E[50;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m$
   461^I[37m[39;49;00m$
   462^I[37m#^INetBSD/FreeBSD vt220 terminal emulator console (pc keyboard & monitor)[39;49;00m[37m[39;49;00m$
   463^I[37m#^Itermcap entries for pure VT220-Emulation and 25, 28, 35, 40, 43 and[39;49;00m[37m[39;49;00m$
   464^I[37m#^I50 lines entries; 132 columns[39;49;00m[37m[39;49;00m$
   465^I[94mpcvt25w[39;49;00m|[36mdec vt220 emulation with 25 lines and 132 cols[39;49;00m:\[37m[39;49;00m$
   466^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:\[37m[39;49;00m$
   467^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;25r\E[25;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m$
   468^I[94mpcvt28w[39;49;00m|[36mdec vt220 emulation with 28 lines and 132 cols[39;49;00m:\[37m[39;49;00m$
   469^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m28[39;49;00m:\[37m[39;49;00m$
   470^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;28r\E[28;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m$
   471^I[94mpcvt35w[39;49;00m|[36mdec vt220 emulation with 35 lines and 132 cols[39;49;00m:\[37m[39;49;00m$
   472^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m35[39;49;00m:\[37m[39;49;00m$
   473^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;35r\E[35;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m$
   474^I[94mpcvt40w[39;49;00m|[36mdec vt220 emulation with 40 lines and 132 cols[39;49;00m:\[37m[39;49;00m$
   475^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m40[39;49;00m:\[37m[39;49;00m$
   476^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;40r\E[40;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m$
   477^I[94mpcvt43w[39;49;00m|[36mdec vt220 emulation with 43 lines and 132 cols[39;49;00m:\[37m[39;49;00m$
   478^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m43[39;49;00m:\[37m[39;49;00m$
   479^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;43r\E[43;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m$
   480^I[94mpcvt50w[39;49;00m|[36mdec vt220 emulation with 50 lines and 132 cols[39;49;00m:\[37m[39;49;00m$
   481^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:\[37m[39;49;00m$
   482^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;50r\E[50;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m$
   483^I[37m[39;49;00m$
   484^I[37m# Terminfo entries to enable the use of the ncurses library in colour on a[39;49;00m[37m[39;49;00m$
   485^I[37m# NetBSD-arm32 console (only tested on a RiscPC).[39;49;00m[37m[39;49;00m$
   486^I[37m# Created by Dave Millen <dmill@globalnet.co.uk> 22.07.98[39;49;00m[37m[39;49;00m$
   487^I[37m# modified codes for setf/setb to setaf/setab, then to klone+color, corrected[39;49;00m[37m[39;49;00m$
   488^I[37m# typo in invis - TD[39;49;00m[37m[39;49;00m$
   489^I[94marm100[39;49;00m|[36marm100-am[39;49;00m|[36mArm(RiscPC) ncurses compatible (for 640x480)[39;49;00m:\[37m[39;49;00m$
   490^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mms[39;49;00m:[04m[32mut[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m$
   491^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m30[39;49;00m:\[37m[39;49;00m$
   492^I[37m^I[39;49;00m:[04m[32m@8[39;49;00m=\E[M:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mK1[39;49;00m=\E[q:[04m[32mK2[39;49;00m=\E[r:[04m[32mK3[39;49;00m=\E[s:[04m[32mK4[39;49;00m=\E[p:[04m[32mK5[39;49;00m=\E[n:\[37m[39;49;00m$
   493^I[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRA[39;49;00m=\E[?7l:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mSA[39;49;00m=\E[?7h:[04m[32mUP[39;49;00m=\E[%dA:\[37m[39;49;00m$
   494^I[37m^I[39;49;00m:[04m[32mac[39;49;00m=``aaffggjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~:\[37m[39;49;00m$
   495^I[37m^I[39;49;00m:[04m[32mae[39;49;00m=^O:[04m[32mas[39;49;00m=^N:[04m[32mbl[39;49;00m=^G:[04m[32mcb[39;49;00m=\E[1K:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[J:\[37m[39;49;00m$
   496^I[37m^I[39;49;00m:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mct[39;49;00m=\E[3g:[04m[32mdo[39;49;00m=^J:\[37m[39;49;00m$
   497^I[37m^I[39;49;00m:[04m[32meA[39;49;00m=\E(B\E)0:[04m[32mho[39;49;00m=\E[H:[04m[32mk0[39;49;00m=\E[y:[04m[32mk1[39;49;00m=\E[P:[04m[32mk2[39;49;00m=\E[Q:[04m[32mk3[39;49;00m=\E[R:\[37m[39;49;00m$
   498^I[37m^I[39;49;00m:[04m[32mk4[39;49;00m=\E[S:[04m[32mk5[39;49;00m=\E[t:[04m[32mk6[39;49;00m=\E[u:[04m[32mk7[39;49;00m=\E[v:[04m[32mk8[39;49;00m=\E[l:[04m[32mk9[39;49;00m=\E[w:[04m[32mk;[39;49;00m=\E[x:\[37m[39;49;00m$
   499^I[37m^I[39;49;00m:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mke[39;49;00m=\E[?1l\E>:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mks[39;49;00m=\E[?1h\E=:\[37m[39;49;00m$
   500^I[37m^I[39;49;00m:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m\017:[04m[32mmk[39;49;00m=\E[8m:\[37m[39;49;00m$
   501^I[37m^I[39;49;00m:[04m[32mmr[39;49;00m=\E[6m:[04m[32mnd[39;49;00m=\E[C:[04m[32mr2[39;49;00m=\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:\[37m[39;49;00m$
   502^I[37m^I[39;49;00m:[04m[32mrc[39;49;00m=\E8:\[37m[39;49;00m$
   503^I[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[0%?%p1%p6%|%t;1%;%?%p2%t;4%;%?%p1%p3%|%t;7%;%?%p4%t;5%;m%?%p9%t\016%e\017%;:\[37m[39;49;00m$
   504^I[37m^I[39;49;00m:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[m:[04m[32msf[39;49;00m=^J:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[m:\[37m[39;49;00m$
   505^I[37m^I[39;49;00m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:\[37m[39;49;00m$
   506^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=ecma+sgr:[04m[32mtc[39;49;00m=klone+color:[37m[39;49;00m$
   507^I[94marm100-w[39;49;00m|[36marm100-wam[39;49;00m|[36mArm(RiscPC) ncurses compatible (for 1024x768)[39;49;00m:\[37m[39;49;00m$
   508^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:[04m[32mtc[39;49;00m=arm100:[37m[39;49;00m$
   509^I[37m[39;49;00m$
   510^I[37m# NetBSD/x68k console vt200 emulator. This port runs on a 68K machine[39;49;00m[37m[39;49;00m$
   511^I[37m# manufactured by Sharp for the Japenese market.[39;49;00m[37m[39;49;00m$
   512^I[37m# From Minoura Makoto <minoura@netlaputa.or.jp>, 12 May 1996[39;49;00m[37m[39;49;00m$
   513^I[94mx68k[39;49;00m|[36mx68k-ite[39;49;00m|[36mNetBSD/x68k ITE[39;49;00m:\[37m[39;49;00m$
   514^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m96[39;49;00m:[04m[32mli[39;49;00m#[34m32[39;49;00m:\[37m[39;49;00m$
   515^I[37m^I[39;49;00m:[04m[32m%1[39;49;00m=\E[28~:[04m[32mkC[39;49;00m=\E[9~:[04m[32mtc[39;49;00m=vt220:[37m[39;49;00m$
   516^I[37m[39;49;00m$
   517^I[37m# <tv@pobox.com>:[39;49;00m[37m[39;49;00m$
   518^I[37m# Entry for the DNARD OpenFirmware console, close to ANSI but not quite.[39;49;00m[37m[39;49;00m$
   519^I[37m#[39;49;00m[37m[39;49;00m$
   520^I[37m# (still unfinished, but good enough so far.)[39;49;00m[37m[39;49;00m$
   521^I[94mofcons[39;49;00m:\[37m[39;49;00m$
   522^I[37m^I[39;49;00m:[04m[32mbw[39;49;00m:\[37m[39;49;00m$
   523^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m30[39;49;00m:\[37m[39;49;00m$
   524^I[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\233%dL:[04m[32mDC[39;49;00m=\233%dP:[04m[32mDL[39;49;00m=\233%dM:[04m[32mDO[39;49;00m=\233%dB:[04m[32mIC[39;49;00m=\233%d@:\[37m[39;49;00m$
   525^I[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\233%dD:[04m[32mRI[39;49;00m=\233%dC:[04m[32mUP[39;49;00m=\233%dA:[04m[32mal[39;49;00m=\233L:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\233J:\[37m[39;49;00m$
   526^I[37m^I[39;49;00m:[04m[32mce[39;49;00m=\233K:[04m[32mcl[39;49;00m=^L:[04m[32mcm[39;49;00m=\233%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mdc[39;49;00m=\233P:[04m[32mdl[39;49;00m=\233M:\[37m[39;49;00m$
   527^I[37m^I[39;49;00m:[04m[32mdo[39;49;00m=\233B:[04m[32mei[39;49;00m=:[04m[32mic[39;49;00m=\233@:[04m[32mim[39;49;00m=:[04m[32mk1[39;49;00m=\2330P:[04m[32mk2[39;49;00m=\2330Q:[04m[32mk3[39;49;00m=\2330W:\[37m[39;49;00m$
   528^I[37m^I[39;49;00m:[04m[32mk4[39;49;00m=\2330x:[04m[32mk5[39;49;00m=\2330t:[04m[32mk6[39;49;00m=\2330u:[04m[32mk7[39;49;00m=\2330q:[04m[32mk8[39;49;00m=\2330r:\[37m[39;49;00m$
   529^I[37m^I[39;49;00m:[04m[32mk9[39;49;00m=\2330p:[04m[32mk;[39;49;00m=\2330M:[04m[32mkD[39;49;00m=\233P:[04m[32mkN[39;49;00m=\233/:[04m[32mkP[39;49;00m=\233?:[04m[32mkb[39;49;00m=^H:\[37m[39;49;00m$
   530^I[37m^I[39;49;00m:[04m[32mkd[39;49;00m=\233B:[04m[32mkl[39;49;00m=\233D:[04m[32mkr[39;49;00m=\233C:[04m[32mku[39;49;00m=\233A:[04m[32mle[39;49;00m=\233D:[04m[32mmb[39;49;00m=\2337;2m:\[37m[39;49;00m$
   531^I[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\2331m:[04m[32mme[39;49;00m=\2330m:[04m[32mmh[39;49;00m=\2332m:[04m[32mmk[39;49;00m=\2338m:[04m[32mmr[39;49;00m=\2337m:\[37m[39;49;00m$
   532^I[37m^I[39;49;00m:[04m[32mnd[39;49;00m=\233C:[04m[32mnw[39;49;00m=^M^J:[04m[32mse[39;49;00m=\2330m:[04m[32msf[39;49;00m=^J:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\2330m:[04m[32mup[39;49;00m=\233A:\[37m[39;49;00m$
   533^I[37m^I[39;49;00m:[04m[32mvb[39;49;00m=^G:[37m[39;49;00m$
   534^I[37m[39;49;00m$
   535^I[37m# NetBSD "wscons" emulator in vt220 mode[39;49;00m[37m[39;49;00m$
   536^I[37m# These are micro-minimal and probably need to be redone for real[39;49;00m[37m[39;49;00m$
   537^I[37m# after the manner of the pcvt entries.[39;49;00m[37m[39;49;00m$
   538^I[94mwsvt25[39;49;00m|[36mNetBSD wscons in 25 line DEC VT220 mode[39;49;00m:\[37m[39;49;00m$
   539^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:[04m[32mtc[39;49;00m=vt220:[37m[39;49;00m$
   540^I[37m[39;49;00m$
   541^I[94mwsvt25m[39;49;00m|[36mNetBSD wscons in 25 line DEC VT220 mode with Meta[39;49;00m:\[37m[39;49;00m$
   542^I[37m^I[39;49;00m:[04m[32mkm[39;49;00m:\[37m[39;49;00m$
   543^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:[04m[32mtc[39;49;00m=vt220:[37m[39;49;00m$
   544^I[37m[39;49;00m$
   545^I[37m# `rasterconsole' provided by 4.4BSD, NetBSD and OpenBSD on SPARC, and [39;49;00m[37m[39;49;00m$
   546^I[37m# DECstation/pmax.[39;49;00m[37m[39;49;00m$
   547^I[94mrcons[39;49;00m|[36mBSD rasterconsole[39;49;00m:\[37m[39;49;00m$
   548^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=sun-il:[37m[39;49;00m$
   549^I[37m# Color version of above. Color currenly only provided by NetBSD.[39;49;00m[37m[39;49;00m$
   550^I[94mrcons-color[39;49;00m|[36mBSD rasterconsole with ANSI color[39;49;00m:\[37m[39;49;00m$
   551^I[37m^I[39;49;00m:[04m[32mut[39;49;00m:\[37m[39;49;00m$
   552^I[37m^I[39;49;00m:[04m[32mCo[39;49;00m#[34m8[39;49;00m:[04m[32mpa[39;49;00m#[34m64[39;49;00m:\[37m[39;49;00m$
   553^I[37m^I[39;49;00m:[04m[32mAB[39;49;00m=\E[4%dm:[04m[32mAF[39;49;00m=\E[3%dm:[04m[32mop[39;49;00m=\E[m:[04m[32mtc[39;49;00m=rcons:[37m[39;49;00m$
   554^I[37m[39;49;00m$
   555^I[37m#### FreeBSD console entries[39;49;00m[37m[39;49;00m$
   556^I[37m#[39;49;00m[37m[39;49;00m$
   557^I[37m# From: Andrey Chernov <ache@astral.msk.su> 29 Mar 1996[39;49;00m[37m[39;49;00m$
   558^I[37m# Andrey Chernov maintains the FreeBSD termcap distributions.[39;49;00m[37m[39;49;00m$
   559^I[37m#[39;49;00m[37m[39;49;00m$
   560^I[37m# Note: Users of FreeBSD 2.1.0 and older versions must either upgrade[39;49;00m[37m[39;49;00m$
   561^I[37m# or comment out the :cb: capability in the console entry.[39;49;00m[37m[39;49;00m$
   562^I[37m#[39;49;00m[37m[39;49;00m$
   563^I[37m# Alexander Lukyanov reports:[39;49;00m[37m[39;49;00m$
   564^I[37m# I have seen FreeBSD-2.1.5R... The old el1 bug changed, but it is still there.[39;49;00m[37m[39;49;00m$
   565^I[37m# Now el1 clears not only to the line beginning, but also a large chunk[39;49;00m[37m[39;49;00m$
   566^I[37m# of previous line. But there is another bug - ech does not work at all.[39;49;00m[37m[39;49;00m$
   567^I[37m#[39;49;00m[37m[39;49;00m$
   568^I[37m[39;49;00m$
   569^I[37m# for syscons[39;49;00m[37m[39;49;00m$
   570^I[37m# common entry without semigraphics[39;49;00m[37m[39;49;00m$
   571^I[37m# Bug: The <op> capability resets attributes.[39;49;00m[37m[39;49;00m$
   572^I[37m# Bug? The ech and el1 attributes appear to move the cursor in some cases; for[39;49;00m[37m[39;49;00m$
   573^I[37m# instance el1 does if the cursor is moved to the right margin first.  Removed[39;49;00m[37m[39;49;00m$
   574^I[37m# by T.Dickey 97/5/3 (ech=\E[%p1%dX, el1=\E[1K)[39;49;00m[37m[39;49;00m$
   575^I[37m#[39;49;00m[37m[39;49;00m$
   576^I[37m# Setting colors turns off reverse; we cannot guarantee order, so use ncv.[39;49;00m[37m[39;49;00m$
   577^I[37m# Note that this disables standout with color.[39;49;00m[37m[39;49;00m$
   578^I[94mcons25w[39;49;00m|[36mansiw[39;49;00m|[36mansi80x25-raw[39;49;00m|[36mfreebsd console (25-line raw mode)[39;49;00m:\[37m[39;49;00m$
   579^I[37m^I[39;49;00m:[04m[32mNP[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbw[39;49;00m:[04m[32meo[39;49;00m:[04m[32mms[39;49;00m:[04m[32mut[39;49;00m:\[37m[39;49;00m$
   580^I[37m^I[39;49;00m:[04m[32mCo[39;49;00m#[34m8[39;49;00m:[04m[32mNC[39;49;00m#[34m21[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:[04m[32mpa[39;49;00m#[34m64[39;49;00m:\[37m[39;49;00m$
   581^I[37m^I[39;49;00m:[04m[32m@7[39;49;00m=\E[F:[04m[32mAB[39;49;00m=\E[4%p1%dm:[04m[32mAF[39;49;00m=\E[3%p1%dm:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:\[37m[39;49;00m$
   582^I[37m^I[39;49;00m:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mF1[39;49;00m=\E[W:[04m[32mF2[39;49;00m=\E[X:[04m[32mIC[39;49;00m=\E[%d@:[04m[32mK2[39;49;00m=\E[E:\[37m[39;49;00m$
   583^I[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mSF[39;49;00m=\E[%dS:[04m[32mSR[39;49;00m=\E[%dT:[04m[32mUP[39;49;00m=\E[%dA:\[37m[39;49;00m$
   584^I[37m^I[39;49;00m:[04m[32mal[39;49;00m=\E[L:[04m[32mbl[39;49;00m=^G:[04m[32mbt[39;49;00m=\E[Z:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mch[39;49;00m=\E[%i%d`:\[37m[39;49;00m$
   585^I[37m^I[39;49;00m:[04m[32mcl[39;49;00m=\E[H\E[J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcv[39;49;00m=\E[%i%dd:[04m[32mdc[39;49;00m=\E[P:\[37m[39;49;00m$
   586^I[37m^I[39;49;00m:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=\E[B:[04m[32mei[39;49;00m=:[04m[32mho[39;49;00m=\E[H:[04m[32mic[39;49;00m=\E[@:[04m[32mim[39;49;00m=:[04m[32mk1[39;49;00m=\E[M:[04m[32mk2[39;49;00m=\E[N:\[37m[39;49;00m$
   587^I[37m^I[39;49;00m:[04m[32mk3[39;49;00m=\E[O:[04m[32mk4[39;49;00m=\E[P:[04m[32mk5[39;49;00m=\E[Q:[04m[32mk6[39;49;00m=\E[R:[04m[32mk7[39;49;00m=\E[S:[04m[32mk8[39;49;00m=\E[T:[04m[32mk9[39;49;00m=\E[U:\[37m[39;49;00m$
   588^I[37m^I[39;49;00m:[04m[32mk;[39;49;00m=\E[V:[04m[32mkB[39;49;00m=\E[Z:[04m[32mkD[39;49;00m=\177:[04m[32mkI[39;49;00m=\E[L:[04m[32mkN[39;49;00m=\E[G:[04m[32mkP[39;49;00m=\E[I:[04m[32mkb[39;49;00m=^H:\[37m[39;49;00m$
   589^I[37m^I[39;49;00m:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[H:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:\[37m[39;49;00m$
   590^I[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:[04m[32mmh[39;49;00m=\E[30;1m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mnw[39;49;00m=\E[E:\[37m[39;49;00m$
   591^I[37m^I[39;49;00m:[04m[32mop[39;49;00m=\E[x:[04m[32mr1[39;49;00m=\E[x\E[m\Ec:[04m[32mse[39;49;00m=\E[m:[04m[32msf[39;49;00m=\E[S:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\E[T:\[37m[39;49;00m$
   592^I[37m^I[39;49;00m:[04m[32mta[39;49;00m=^I:[04m[32mup[39;49;00m=\E[A:[04m[32mve[39;49;00m=\E[=0C:[04m[32mvs[39;49;00m=\E[=1C:[37m[39;49;00m$
   593^I[94mcons25[39;49;00m|[36mansis[39;49;00m|[36mansi80x25[39;49;00m|[36mfreebsd console (25-line ansi mode)[39;49;00m:\[37m[39;49;00m$
   594^I[37m^I[39;49;00m:[04m[32mac[39;49;00m=-\030.^Y0\333`\004a\260f\370g\361h\261i\025j\331k\277l\332m\300n\305q\304t\303u\264v\301w\302x\263y\363z\362~\371:\[37m[39;49;00m$
   595^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=cons25w:[37m[39;49;00m$
   596^I[94mcons25-m[39;49;00m|[36mansis-mono[39;49;00m|[36mansi80x25-mono[39;49;00m|[36mfreebsd console (25-line mono ansi mode)[39;49;00m:\[37m[39;49;00m$
   597^I[37m^I[39;49;00m:[04m[32mCo@[39;49;00m:[04m[32mpa@[39;49;00m:\[37m[39;49;00m$
   598^I[37m^I[39;49;00m:[04m[32mAB@[39;49;00m:[04m[32mAF@[39;49;00m:[04m[32mmd@[39;49;00m:[04m[32mmh@[39;49;00m:[04m[32mop@[39;49;00m:[04m[32mue[39;49;00m=\E[m:[04m[32mus[39;49;00m=\E[4m:[04m[32mtc[39;49;00m=cons25:[37m[39;49;00m$
   599^I[94mcons30[39;49;00m|[36mansi80x30[39;49;00m|[36mfreebsd console (30-line ansi mode)[39;49;00m:\[37m[39;49;00m$
   600^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m30[39;49;00m:[04m[32mtc[39;49;00m=cons25:[37m[39;49;00m$
   601^I[94mcons30-m[39;49;00m|[36mansi80x30-mono[39;49;00m|[36mfreebsd console (30-line mono ansi mode)[39;49;00m:\[37m[39;49;00m$
   602^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m30[39;49;00m:[04m[32mtc[39;49;00m=cons25-m:[37m[39;49;00m$
   603^I[94mcons43[39;49;00m|[36mansi80x43[39;49;00m|[36mfreebsd console (43-line ansi mode)[39;49;00m:\[37m[39;49;00m$
   604^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m43[39;49;00m:[04m[32mtc[39;49;00m=cons25:[37m[39;49;00m$
   605^I[94mcons43-m[39;49;00m|[36mansi80x43-mono[39;49;00m|[36mfreebsd console (43-line mono ansi mode)[39;49;00m:\[37m[39;49;00m$
   606^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m43[39;49;00m:[04m[32mtc[39;49;00m=cons25-m:[37m[39;49;00m$
   607^I[94mcons50[39;49;00m|[36mansil[39;49;00m|[36mansi80x50[39;49;00m|[36mfreebsd console (50-line ansi mode)[39;49;00m:\[37m[39;49;00m$
   608^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:[04m[32mtc[39;49;00m=cons25:[37m[39;49;00m$
   609^I[94mcons50-m[39;49;00m|[36mansil-mono[39;49;00m|[36mansi80x50-mono[39;49;00m|[36mfreebsd console (50-line mono ansi mode)[39;49;00m:\[37m[39;49;00m$
   610^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:[04m[32mtc[39;49;00m=cons25-m:[37m[39;49;00m$
   611^I[94mcons60[39;49;00m|[36mansi80x60[39;49;00m|[36mfreebsd console (60-line ansi mode)[39;49;00m:\[37m[39;49;00m$
   612^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m60[39;49;00m:[04m[32mtc[39;49;00m=cons25:[37m[39;49;00m$
   613^I[94mcons60-m[39;49;00m|[36mansi80x60-mono[39;49;00m|[36mfreebsd console (60-line mono ansi mode)[39;49;00m:\[37m[39;49;00m$
   614^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m60[39;49;00m:[04m[32mtc[39;49;00m=cons25-m:[37m[39;49;00m$
   615^I[94mcons25r[39;49;00m|[36mpc3r[39;49;00m|[36mibmpc3r[39;49;00m|[36mcons25-koi8-r[39;49;00m|[36mfreebsd console w/koi8-r cyrillic[39;49;00m:\[37m[39;49;00m$
   616^I[37m^I[39;49;00m:[04m[32mac[39;49;00m=-\030.^Y0\215`\004a\220f\234h\221i\025j\205k\203l\202m\204n\212q\0t\206u\207v\211w\210x\201y\230z\231~\225:\[37m[39;49;00m$
   617^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=cons25w:[37m[39;49;00m$
   618^I[94mcons25r-m[39;49;00m|[36mpc3r-m[39;49;00m|[36mibmpc3r-mono[39;49;00m|[36mcons25-koi8r-m[39;49;00m|[36mfreebsd console w/koi8-r cyrillic (mono)[39;49;00m:\[37m[39;49;00m$
   619^I[37m^I[39;49;00m:[04m[32mCo@[39;49;00m:[04m[32mpa@[39;49;00m:\[37m[39;49;00m$
   620^I[37m^I[39;49;00m:[04m[32mAB@[39;49;00m:[04m[32mAF@[39;49;00m:[04m[32mop@[39;49;00m:[04m[32mue[39;49;00m=\E[m:[04m[32mus[39;49;00m=\E[4m:[04m[32mtc[39;49;00m=cons25r:[37m[39;49;00m$
   621^I[94mcons50r[39;49;00m|[36mcons50-koi8r[39;49;00m|[36mfreebsd console w/koi8-r cyrillic (50 lines)[39;49;00m:\[37m[39;49;00m$
   622^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:[04m[32mtc[39;49;00m=cons25r:[37m[39;49;00m$
   623^I[94mcons50r-m[39;49;00m|[36mcons50-koi8r-m[39;49;00m|[36mfreebsd console w/koi8-r cyrillic (50-line mono)[39;49;00m:\[37m[39;49;00m$
   624^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:[04m[32mtc[39;49;00m=cons25r-m:[37m[39;49;00m$
   625^I[94mcons60r[39;49;00m|[36mcons60-koi8r[39;49;00m|[36mfreebsd console w/koi8-r cyrillic (60 lines)[39;49;00m:\[37m[39;49;00m$
   626^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m60[39;49;00m:[04m[32mtc[39;49;00m=cons25r:[37m[39;49;00m$
   627^I[94mcons60r-m[39;49;00m|[36mcons60-koi8r-m[39;49;00m|[36mfreebsd console w/koi8-r cyrillic (60-line mono)[39;49;00m:\[37m[39;49;00m$
   628^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m60[39;49;00m:[04m[32mtc[39;49;00m=cons25r-m:[37m[39;49;00m$
   629^I[37m# ISO 8859-1 FreeBSD console[39;49;00m[37m[39;49;00m$
   630^I[94mcons25l1[39;49;00m|[36mcons25-iso8859[39;49;00m|[36mfreebsd console w/iso 8859-1 chars[39;49;00m:\[37m[39;49;00m$
   631^I[37m^I[39;49;00m:[04m[32mac[39;49;00m=+\253\054\273-\030.\031`\201a\202f\207g\210i\247j\213k\214l\215m\216n\217o\220p\221q\222r\223s\224t\225u\226v\227w\230x\231y\232z\233~\237:\[37m[39;49;00m$
   632^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=cons25w:[37m[39;49;00m$
   633^I[94mcons25l1-m[39;49;00m|[36mcons25-iso-m[39;49;00m|[36mfreebsd console w/iso 8859-1 chars (mono)[39;49;00m:\[37m[39;49;00m$
   634^I[37m^I[39;49;00m:[04m[32mCo@[39;49;00m:[04m[32mpa@[39;49;00m:\[37m[39;49;00m$
   635^I[37m^I[39;49;00m:[04m[32mAB@[39;49;00m:[04m[32mAF@[39;49;00m:[04m[32mmd@[39;49;00m:[04m[32mmh@[39;49;00m:[04m[32mop@[39;49;00m:[04m[32mue[39;49;00m=\E[m:[04m[32mus[39;49;00m=\E[4m:[04m[32mtc[39;49;00m=cons25l1:[37m[39;49;00m$
   636^I[94mcons50l1[39;49;00m|[36mcons50-iso8859[39;49;00m|[36mfreebsd console w/iso 8859-1 chars (50 lines)[39;49;00m:\[37m[39;49;00m$
   637^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:[04m[32mtc[39;49;00m=cons25l1:[37m[39;49;00m$
   638^I[94mcons50l1-m[39;49;00m|[36mcons50-iso-m[39;49;00m|[36mfreebsd console w/iso 8859-1 chars (50-line mono)[39;49;00m:\[37m[39;49;00m$
   639^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:[04m[32mtc[39;49;00m=cons25l1-m:[37m[39;49;00m$
   640^I[94mcons60l1[39;49;00m|[36mcons60-iso[39;49;00m|[36mfreebsd console w/iso 8859-1 chars (60 lines)[39;49;00m:\[37m[39;49;00m$
   641^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m60[39;49;00m:[04m[32mtc[39;49;00m=cons25l1:[37m[39;49;00m$
   642^I[94mcons60l1-m[39;49;00m|[36mcons60-iso-m[39;49;00m|[36mfreebsd console w/iso 8859-1 chars (60-line mono)[39;49;00m:\[37m[39;49;00m$
   643^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m60[39;49;00m:[04m[32mtc[39;49;00m=cons25l1-m:[37m[39;49;00m$
   644^I[37m[39;49;00m$
   645^I[37m#### 386BSD and BSD/OS Consoles[39;49;00m[37m[39;49;00m$
   646^I[37m#[39;49;00m[37m[39;49;00m$
   647^I[37m[39;49;00m$
   648^I[37m# This was the original 386BSD console entry (I think).  [39;49;00m[37m[39;49;00m$
   649^I[37m# Some places it's named oldpc3|oldibmpc3.[39;49;00m[37m[39;49;00m$
   650^I[37m# From: Alex R.N. Wetmore <aw2t@andrew.cmu.edu>[39;49;00m[37m[39;49;00m$
   651^I[94morigpc3[39;49;00m|[36morigibmpc3[39;49;00m|[36mIBM PC 386BSD Console[39;49;00m:\[37m[39;49;00m$
   652^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbw[39;49;00m:[04m[32meo[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m$
   653^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:\[37m[39;49;00m$
   654^I[37m^I[39;49;00m:[04m[32mac[39;49;00m=j\331k\277l\332m\300n\305q\304t\303u\264v\301w\302x\263:\[37m[39;49;00m$
   655^I[37m^I[39;49;00m:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\Ec:[04m[32mcm[39;49;00m=\E[%i%2;%2H:[04m[32mdo[39;49;00m=\E[B:[04m[32mho[39;49;00m=\E[H:\[37m[39;49;00m$
   656^I[37m^I[39;49;00m:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[Y:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mmd[39;49;00m=\E[7m:\[37m[39;49;00m$
   657^I[37m^I[39;49;00m:[04m[32mme[39;49;00m=\E[m\E[1;0x\E[2;7x:[04m[32mnd[39;49;00m=\E[C:[04m[32mse[39;49;00m=\E[1;0x\E[2;7x:\[37m[39;49;00m$
   658^I[37m^I[39;49;00m:[04m[32msf[39;49;00m=\E[S:[04m[32mso[39;49;00m=\E[1;7x\E[2;0x:[04m[32msr[39;49;00m=\E[T:[04m[32mue[39;49;00m=\E[1;0x\E[2;7x:\[37m[39;49;00m$
   659^I[37m^I[39;49;00m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[1;7x\E[2;0x:[37m[39;49;00m$
   660^I[37m[39;49;00m$
   661^I[37m# description of BSD/386 console emulator in version 1.0 (supplied by BSDI)[39;49;00m[37m[39;49;00m$
   662^I[94moldpc3[39;49;00m|[36moldibmpc3[39;49;00m|[36mold IBM PC BSD/386 Console[39;49;00m:\[37m[39;49;00m$
   663^I[37m^I[39;49;00m:[04m[32mkm[39;49;00m:\[37m[39;49;00m$
   664^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:\[37m[39;49;00m$
   665^I[37m^I[39;49;00m:[04m[32mal[39;49;00m=\E[L:[04m[32mbl[39;49;00m=^G:[04m[32mcr[39;49;00m=^M:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=^J:[04m[32mkH[39;49;00m=\E[F:[04m[32mkI[39;49;00m=\E[L:[04m[32mkN[39;49;00m=\E[G:\[37m[39;49;00m$
   666^I[37m^I[39;49;00m:[04m[32mkP[39;49;00m=\E[I:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[H:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:\[37m[39;49;00m$
   667^I[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\E[=15F:[04m[32mme[39;49;00m=\E[=R:[04m[32mmh[39;49;00m=\E[=8F:[04m[32mnw[39;49;00m=^M^J:[04m[32msf[39;49;00m=^J:[04m[32mta[39;49;00m=^I:[37m[39;49;00m$
   668^I[37m[39;49;00m$
   669^I[37m# Description of BSD/OS console emulator in version 1.1, 2.0, 2.1[39;49;00m[37m[39;49;00m$
   670^I[37m# Note, the emulator supports many of the additional console features[39;49;00m[37m[39;49;00m$
   671^I[37m# listed in the iBCS2 (e.g. character-set selection) though not all[39;49;00m[37m[39;49;00m$
   672^I[37m# are described here.  This entry really ought to be upgraded.[39;49;00m[37m[39;49;00m$
   673^I[37m# Also note, the console will also work with fewer lines after doing[39;49;00m[37m[39;49;00m$
   674^I[37m# "stty rows NN", e.g. to use 24 lines.[39;49;00m[37m[39;49;00m$
   675^I[37m# (Color support from Kevin Rosenberg <kevin@cyberport.com>, 2 May 1996) [39;49;00m[37m[39;49;00m$
   676^I[37m# Bug: The <op> capability resets attributes.[39;49;00m[37m[39;49;00m$
   677^I[94mbsdos-pc-nobold[39;49;00m|[36mBSD/OS PC console w/o bold[39;49;00m:\[37m[39;49;00m$
   678^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32meo[39;49;00m:[04m[32mkm[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m$
   679^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:\[37m[39;49;00m$
   680^I[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRI[39;49;00m=\E[%dC:\[37m[39;49;00m$
   681^I[37m^I[39;49;00m:[04m[32mUP[39;49;00m=\E[%dA:[04m[32mal[39;49;00m=\E[L:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\Ec:\[37m[39;49;00m$
   682^I[37m^I[39;49;00m:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=^J:[04m[32mho[39;49;00m=\E[H:[04m[32mkH[39;49;00m=\E[F:\[37m[39;49;00m$
   683^I[37m^I[39;49;00m:[04m[32mkI[39;49;00m=\E[L:[04m[32mkN[39;49;00m=\E[G:[04m[32mkP[39;49;00m=\E[I:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[H:[04m[32mkl[39;49;00m=\E[D:\[37m[39;49;00m$
   684^I[37m^I[39;49;00m:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mnd[39;49;00m=\E[C:[04m[32mnw[39;49;00m=^M^J:[04m[32mrc[39;49;00m=\E8:\[37m[39;49;00m$
   685^I[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[0;10%?%p1%t;7%;%?%p3%t;7%;%?%p4%t;5%;%?%p6%t;1%;%?%p7%t;8%;%?%p9%t;11%;m%?%p5%t\E[=8F%;:\[37m[39;49;00m$
   686^I[37m^I[39;49;00m:[04m[32msc[39;49;00m=\E7:[04m[32msf[39;49;00m=^J:[04m[32mta[39;49;00m=^I:[04m[32mup[39;49;00m=\E[A:\[37m[39;49;00m$
   687^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=klone+sgr:[04m[32mtc[39;49;00m=klone+color:[37m[39;49;00m$
   688^I[94mbsdos-pc[39;49;00m|[36mIBM PC BSD/OS Console[39;49;00m:\[37m[39;49;00m$
   689^I[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[0;10%?%p1%t;7%;%?%p2%t;1%;%?%p3%t;7%;%?%p4%t;5%;%?%p6%t;1%;%?%p7%t;8%;%?%p9%t;11%;m:[04m[32mtc[39;49;00m=bsdos-pc-nobold:[37m[39;49;00m$
   690^I[37m[39;49;00m$
   691^I[37m# Old names for BSD/OS PC console used in releases before 4.1. [39;49;00m[37m[39;49;00m$
   692^I[94mpc3[39;49;00m|[36mBSD/OS on the PC Console[39;49;00m:\[37m[39;49;00m$
   693^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=bsdos-pc-nobold:[37m[39;49;00m$
   694^I[94mibmpc3[39;49;00m|[36mpc3-bold[39;49;00m|[36mBSD/OS on the PC Console with bold instead of underline[39;49;00m:\[37m[39;49;00m$
   695^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=bsdos-pc:[37m[39;49;00m$
   696^I[37m [39;49;00m[37m[39;49;00m$
   697^I[37m# BSD/OS on the SPARC [39;49;00m[37m[39;49;00m$
   698^I[94mbsdos-sparc[39;49;00m|[36mSun SPARC BSD/OS Console[39;49;00m:\[37m[39;49;00m$
   699^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=sun:[37m[39;49;00m$
   700^I[37m^I [39;49;00m[37m[39;49;00m$
   701^I[37m# BSD/OS on the PowerPC [39;49;00m[37m[39;49;00m$
   702^I[94mbsdos-ppc[39;49;00m|[36mPowerPC BSD/OS Console[39;49;00m:\[37m[39;49;00m$
   703^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=bsdos-pc:[37m[39;49;00m$
   704^I[37m[39;49;00m$
   705^I[37m#### DEC VT100 and compatibles[39;49;00m[37m[39;49;00m$
   706^I[37m#[39;49;00m[37m[39;49;00m$
   707^I[37m# DEC terminals from the vt100 forward are collected here. Older DEC terminals[39;49;00m[37m[39;49;00m$
   708^I[37m# and micro consoles can be found in the `obsolete' section.  More details on[39;49;00m[37m[39;49;00m$
   709^I[37m# the relationship between the VT100 and ANSI X3.64/ISO 6429/ECMA-48 may be[39;49;00m[37m[39;49;00m$
   710^I[37m# found near the end of this file.[39;49;00m[37m[39;49;00m$
   711^I[37m#[39;49;00m[37m[39;49;00m$
   712^I[37m# Except where noted, these entries are DEC's official terminfos.[39;49;00m[37m[39;49;00m$
   713^I[37m# Contact Bill Hedberg <hedberg@hannah.enet.dec.com> of Terminal Support[39;49;00m[37m[39;49;00m$
   714^I[37m# Engineering for more information.  Updated terminfos and termcaps [39;49;00m[37m[39;49;00m$
   715^I[37m# are kept available at ftp://gatekeeper.dec.com/pub/DEC/termcaps.[39;49;00m[37m[39;49;00m$
   716^I[37m#[39;49;00m[37m[39;49;00m$
   717^I[37m# In October 1995 DEC sold its terminals business, including the VT and Dorio[39;49;00m[37m[39;49;00m$
   718^I[37m# line and trademark, to SunRiver Data Systems.  SunRiver has since changed[39;49;00m[37m[39;49;00m$
   719^I[37m# its name to Boundless Technologies; see http://www.boundless.com.[39;49;00m[37m[39;49;00m$
   720^I[37m#[39;49;00m[37m[39;49;00m$
   721^I[37m[39;49;00m$
   722^I[37m# NOTE:  Any VT100 emulation, whether in hardware or software, almost[39;49;00m[37m[39;49;00m$
   723^I[37m# certainly includes what DEC called the `Level 1 editing extension' codes;[39;49;00m[37m[39;49;00m$
   724^I[37m# only the very oldest VT100s lacked these and there probably aren't any of[39;49;00m[37m[39;49;00m$
   725^I[37m# those left alive.  To capture these, use one of the VT102 entries.[39;49;00m[37m[39;49;00m$
   726^I[37m#[39;49;00m[37m[39;49;00m$
   727^I[37m# Note that the :xn: glitch in vt100 is not quite the same as on the Concept,[39;49;00m[37m[39;49;00m$
   728^I[37m# since the cursor is left in a different position while in the[39;49;00m[37m[39;49;00m$
   729^I[37m# weird state (concept at beginning of next line, vt100 at end[39;49;00m[37m[39;49;00m$
   730^I[37m# of this line) so all versions of vi before 3.7 don't handle[39;49;00m[37m[39;49;00m$
   731^I[37m# :xn: right on vt100. The correct way to handle :xn: is when[39;49;00m[37m[39;49;00m$
   732^I[37m# you output the char in column 80, immediately output CR LF[39;49;00m[37m[39;49;00m$
   733^I[37m# and then assume you are in column 1 of the next line. If :xn:[39;49;00m[37m[39;49;00m$
   734^I[37m# is on, am should be on too.[39;49;00m[37m[39;49;00m$
   735^I[37m# [39;49;00m[37m[39;49;00m$
   736^I[37m# I assume you have smooth scroll off or are at a slow enough baud[39;49;00m[37m[39;49;00m$
   737^I[37m# rate that it doesn't matter (1200? or less). Also this assumes[39;49;00m[37m[39;49;00m$
   738^I[37m# that you set auto-nl to "on", if you set it off use vt100-nam [39;49;00m[37m[39;49;00m$
   739^I[37m# below.[39;49;00m[37m[39;49;00m$
   740^I[37m# [39;49;00m[37m[39;49;00m$
   741^I[37m# The padding requirements listed here are guesses. It is strongly[39;49;00m[37m[39;49;00m$
   742^I[37m# recommended that xon/xoff be enabled, as this is assumed here.[39;49;00m[37m[39;49;00m$
   743^I[37m# [39;49;00m[37m[39;49;00m$
   744^I[37m# The vt100 uses <rs2> and <rf> rather than :is:/:ct:/:st: because the [39;49;00m[37m[39;49;00m$
   745^I[37m# tab settings are in non-volatile memory and don't need to be [39;49;00m[37m[39;49;00m$
   746^I[37m# reset upon login. Also setting the number of columns glitches [39;49;00m[37m[39;49;00m$
   747^I[37m# the screen annoyingly. You can type "reset" to get them set.[39;49;00m[37m[39;49;00m$
   748^I[37m#[39;49;00m[37m[39;49;00m$
   749^I[37m# The VT100 series terminals have cursor ("arrows") keys which can operate[39;49;00m[37m[39;49;00m$
   750^I[37m# in two different modes: Cursor Mode and Application Mode.  Cursor Mode[39;49;00m[37m[39;49;00m$
   751^I[37m# is the reset state, and is assumed to be the normal state.  Application[39;49;00m[37m[39;49;00m$
   752^I[37m# Mode is the "set" state.  In Cursor Mode, the cursor keys transmit[39;49;00m[37m[39;49;00m$
   753^I[37m# "Esc [ {code}" sequences, conforming to ANSI standards.  In Application[39;49;00m[37m[39;49;00m$
   754^I[37m# Mode, the cursor keys transmit "Esc O <code>" sequences.  Application Mode[39;49;00m[37m[39;49;00m$
   755^I[37m# was provided primarily as an aid to the porting of VT52 applications.  It is[39;49;00m[37m[39;49;00m$
   756^I[37m# assumed that the cursor keys are normally in Cursor Mode, and expected that[39;49;00m[37m[39;49;00m$
   757^I[37m# applications such as vi will always transmit the :ks: string.  Therefore,[39;49;00m[37m[39;49;00m$
   758^I[37m# the definitions for the cursor keys are made to match what the terminal[39;49;00m[37m[39;49;00m$
   759^I[37m# transmits after the :ks: string is transmitted.  If the :ks: string[39;49;00m[37m[39;49;00m$
   760^I[37m# is a null string or is not defined, then cursor keys are assumed to be in[39;49;00m[37m[39;49;00m$
   761^I[37m# "Cursor Mode", and the cursor keys definitions should match that assumption,[39;49;00m[37m[39;49;00m$
   762^I[37m# else the appication may fail.  It is also expected that applications will[39;49;00m[37m[39;49;00m$
   763^I[37m# always transmit the :ke: string to the terminal before they exit.[39;49;00m[37m[39;49;00m$
   764^I[37m#[39;49;00m[37m[39;49;00m$
   765^I[37m# The VT100 series terminals have an auxilliary keypad, commonly referred to as[39;49;00m[37m[39;49;00m$
   766^I[37m# the "Numeric Keypad", because it is a cluster of numeric and function keys.[39;49;00m[37m[39;49;00m$
   767^I[37m# The Numeric Keypad which can operate in two different modes: Numeric Mode and[39;49;00m[37m[39;49;00m$
   768^I[37m# Application Mode.  Numeric Mode is the reset state, and is assumed to be[39;49;00m[37m[39;49;00m$
   769^I[37m# the normal state.  Application Mode is the "set" state.  In Numeric Mode,[39;49;00m[37m[39;49;00m$
   770^I[37m# the numeric and punctuation keys transmit ASCII 7-bit characters, and the [39;49;00m[37m[39;49;00m$
   771^I[37m# Enter key transmits the same as the Return key (Note: the Return key[39;49;00m[37m[39;49;00m$
   772^I[37m# can be configured to send either LF (\015) or CR LF).  In Application Mode,[39;49;00m[37m[39;49;00m$
   773^I[37m# all the keypad keys transmit "Esc O {code}" sequences.  The PF1 - PF4 keys[39;49;00m[37m[39;49;00m$
   774^I[37m# always send the same "Esc O {code}" sequences.  It is assumed that the keypad[39;49;00m[37m[39;49;00m$
   775^I[37m# is normally in Numeric Mode.  If an application requires that the keypad be[39;49;00m[37m[39;49;00m$
   776^I[37m# in Application Mode then it is expected that the user, or the application,[39;49;00m[37m[39;49;00m$
   777^I[37m# will set the TERM environment variable to point to a terminfo entry which has[39;49;00m[37m[39;49;00m$
   778^I[37m# defined the :ks: string to include the codes that switch the keypad into[39;49;00m[37m[39;49;00m$
   779^I[37m# Application Mode, and the terminfo entry will also define function key[39;49;00m[37m[39;49;00m$
   780^I[37m# fields to match the Application Mode control codes.  If the :ks: string[39;49;00m[37m[39;49;00m$
   781^I[37m# is a null string or is not defined, then the keypad is assumed to be in[39;49;00m[37m[39;49;00m$
   782^I[37m# Numeric Mode.  If the :ks: string switches the keypad into Application[39;49;00m[37m[39;49;00m$
   783^I[37m# Mode, it is expected that the :ke: string will contain the control codes[39;49;00m[37m[39;49;00m$
   784^I[37m# necessary to reset the keypad to "Normal" mode, and it is also expected that[39;49;00m[37m[39;49;00m$
   785^I[37m# applications which transmit the :ks: string will also always transmit the[39;49;00m[37m[39;49;00m$
   786^I[37m# :ke: string to the terminal before they exit.[39;49;00m[37m[39;49;00m$
   787^I[37m#[39;49;00m[37m[39;49;00m$
   788^I[37m# Here's a diagram of the VT100 keypad keys with their bindings.[39;49;00m[37m[39;49;00m$
   789^I[37m# The top line is the name of the key (some DEC keyboards have the keys[39;49;00m[37m[39;49;00m$
   790^I[37m# labelled somewhat differently, like GOLD instead of PF1, but this is[39;49;00m[37m[39;49;00m$
   791^I[37m# the most "official" name).  The second line is the escape sequence it[39;49;00m[37m[39;49;00m$
   792^I[37m# generates in Application Keypad mode (where "$" means the ESC[39;49;00m[37m[39;49;00m$
   793^I[37m# character).  The third line contains two items, first the mapping of[39;49;00m[37m[39;49;00m$
   794^I[37m# the key in terminfo, and then in termcap.[39;49;00m[37m[39;49;00m$
   795^I[37m#   _______________________________________[39;49;00m[37m[39;49;00m$
   796^I[37m#  |   PF1   |   PF2   |   PF3   |   PF4   |[39;49;00m[37m[39;49;00m$
   797^I[37m#  |   $OP   |   $OQ   |   $OR   |   $OS   |[39;49;00m[37m[39;49;00m$
   798^I[37m#  |_kf1__k1_|_kf2__k2_|_kf3__k3_|_kf4__k4_|[39;49;00m[37m[39;49;00m$
   799^I[37m#  |    7         8         9         -    |[39;49;00m[37m[39;49;00m$
   800^I[37m#  |   $Ow   |   $Ox   |   $Oy   |   $Om   |[39;49;00m[37m[39;49;00m$
   801^I[37m#  |_kf9__k9_|_kf10_k;_|_kf0__k0_|_________|[39;49;00m[37m[39;49;00m$
   802^I[37m#  |    4    |    5    |    6    |    ,    |[39;49;00m[37m[39;49;00m$
   803^I[37m#  |   $Ot   |   $Ou   |   $Ov   |   $Ol   |[39;49;00m[37m[39;49;00m$
   804^I[37m#  |_kf5__k5_|_kf6__k6_|_kf7__k7_|_kf8__k8_|[39;49;00m[37m[39;49;00m$
   805^I[37m#  |    1    |    2    |    3    |         |[39;49;00m[37m[39;49;00m$
   806^I[37m#  |   $Oq   |   $Or   |   $Os   |  enter  |[39;49;00m[37m[39;49;00m$
   807^I[37m#  |_ka1__K1_|_kb2__K2_|_ka3__K3_|  $OM    |[39;49;00m[37m[39;49;00m$
   808^I[37m#  |         0         |   .     |         |[39;49;00m[37m[39;49;00m$
   809^I[37m#  |        $Op        |  $On    |         |[39;49;00m[37m[39;49;00m$
   810^I[37m#  |___kc1_______K4____|_kc3__K5_|_kent_@8_|[39;49;00m[37m[39;49;00m$
   811^I[37m#[39;49;00m[37m[39;49;00m$
   812^I[37m# And here, for those of you with orphaned VT100s lacking documentation, is[39;49;00m[37m[39;49;00m$
   813^I[37m# a description of the soft switches invoked when you do `Set Up'.[39;49;00m[37m[39;49;00m$
   814^I[37m# [39;49;00m[37m[39;49;00m$
   815^I[37m#  Scroll 0-Jump               Shifted 3   0-#[39;49;00m[37m[39;49;00m$
   816^I[37m#  |      1-Smooth             |           1-British pound sign[39;49;00m[37m[39;49;00m$
   817^I[37m#  | Autorepeat 0-Off          | Wrap Around 0-Off[39;49;00m[37m[39;49;00m$
   818^I[37m#  | |          1-On           | |           1-On[39;49;00m[37m[39;49;00m$
   819^I[37m#  | | Screen 0-Dark Bkg       | | New Line 0-Off[39;49;00m[37m[39;49;00m$
   820^I[37m#  | | |      1-Light Bkg      | | |        1-On[39;49;00m[37m[39;49;00m$
   821^I[37m#  | | | Cursor 0-Underline    | | | Interlace 0-Off[39;49;00m[37m[39;49;00m$
   822^I[37m#  | | | |      1-Block        | | | |         1-On[39;49;00m[37m[39;49;00m$
   823^I[37m#  | | | |                     | | | |[39;49;00m[37m[39;49;00m$
   824^I[37m#  1 1 0 1       1 1 1 1       0 1 0 0       0 0 1 0       <--Standard Settings[39;49;00m[37m[39;49;00m$
   825^I[37m#                | | | |                     | | | |[39;49;00m[37m[39;49;00m$
   826^I[37m#                | | | Auto XON/XOFF 0-Off   | | | Power 0-60 Hz[39;49;00m[37m[39;49;00m$
   827^I[37m#                | | |               1-On    | | |       1-50 Hz[39;49;00m[37m[39;49;00m$
   828^I[37m#                | | Ansi/VT52 0-VT52        | | Bits Per Char. 0-7 Bits[39;49;00m[37m[39;49;00m$
   829^I[37m#                | |           1-ANSI        | |                1-8 Bits[39;49;00m[37m[39;49;00m$
   830^I[37m#                | Keyclick 0-Off            | Parity 0-Off[39;49;00m[37m[39;49;00m$
   831^I[37m#                |          1-On             |        1-On[39;49;00m[37m[39;49;00m$
   832^I[37m#                Margin Bell 0-Off           Parity Sense 0-Odd[39;49;00m[37m[39;49;00m$
   833^I[37m#                            1-On                         1-Even[39;49;00m[37m[39;49;00m$
   834^I[37m#[39;49;00m[37m[39;49;00m$
   835^I[37m# The following SET-UP modes are assumed for normal operation:[39;49;00m[37m[39;49;00m$
   836^I[37m#^IANSI_MODE^IAUTO_XON/XOFF_ON^INEWLINE_OFF^I80_COLUMNS[39;49;00m[37m[39;49;00m$
   837^I[37m#^IWRAP_AROUND_ON  JUMP_SCROLL_OFF[39;49;00m[37m[39;49;00m$
   838^I[37m# Other SET-UP modes may be set for operator convenience or communication[39;49;00m[37m[39;49;00m$
   839^I[37m# requirements; I recommend[39;49;00m[37m[39;49;00m$
   840^I[37m#^IAUTOREPEAT_ON^IBLOCK_CURSOR^IMARGIN_BELL_OFF    SHIFTED_3_#[39;49;00m[37m[39;49;00m$
   841^I[37m# Unless you have a graphics add-on such as Digital Engineering's VT640[39;49;00m[37m[39;49;00m$
   842^I[37m# (and even then, whenever it can be arranged!) you should set[39;49;00m[37m[39;49;00m$
   843^I[37m#^IINTERLACE_OFF[39;49;00m[37m[39;49;00m$
   844^I[37m#[39;49;00m[37m[39;49;00m$
   845^I[37m# (vt100: I added <rmam>/<smam> based on the init string, also :bs:. -- esr)[39;49;00m[37m[39;49;00m$
   846^I[94mvt100[39;49;00m|[36mvt100-am[39;49;00m|[36mdec vt100 (w/advanced video)[39;49;00m:\[37m[39;49;00m$
   847^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbs[39;49;00m:[04m[32mms[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m$
   848^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m$
   849^I[37m^I[39;49;00m:[04m[32m@8[39;49;00m=\EOM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mK1[39;49;00m=\EOq:[04m[32mK2[39;49;00m=\EOr:[04m[32mK3[39;49;00m=\EOs:[04m[32mK4[39;49;00m=\EOp:[04m[32mK5[39;49;00m=\EOn:\[37m[39;49;00m$
   850^I[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRA[39;49;00m=\E[?7l:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mSA[39;49;00m=\E[?7h:[04m[32mUP[39;49;00m=\E[%dA:\[37m[39;49;00m$
   851^I[37m^I[39;49;00m:[04m[32mac[39;49;00m=``aaffggjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~:\[37m[39;49;00m$
   852^I[37m^I[39;49;00m:[04m[32mae[39;49;00m=^O:[04m[32mas[39;49;00m=^N:[04m[32mbl[39;49;00m=^G:[04m[32mcb[39;49;00m=\E[1K:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[J:\[37m[39;49;00m$
   853^I[37m^I[39;49;00m:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mct[39;49;00m=\E[3g:[04m[32mdo[39;49;00m=^J:\[37m[39;49;00m$
   854^I[37m^I[39;49;00m:[04m[32meA[39;49;00m=\E(B\E)0:[04m[32mho[39;49;00m=\E[H:[04m[32mk0[39;49;00m=\EOy:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:[04m[32mk3[39;49;00m=\EOR:\[37m[39;49;00m$
   855^I[37m^I[39;49;00m:[04m[32mk4[39;49;00m=\EOS:[04m[32mk5[39;49;00m=\EOt:[04m[32mk6[39;49;00m=\EOu:[04m[32mk7[39;49;00m=\EOv:[04m[32mk8[39;49;00m=\EOl:[04m[32mk9[39;49;00m=\EOw:[04m[32mk;[39;49;00m=\EOx:\[37m[39;49;00m$
   856^I[37m^I[39;49;00m:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\EOB:[04m[32mke[39;49;00m=\E[?1l\E>:[04m[32mkl[39;49;00m=\EOD:[04m[32mkr[39;49;00m=\EOC:[04m[32mks[39;49;00m=\E[?1h\E=:\[37m[39;49;00m$
   857^I[37m^I[39;49;00m:[04m[32mku[39;49;00m=\EOA:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m\017:[04m[32mmr[39;49;00m=\E[7m:\[37m[39;49;00m$
   858^I[37m^I[39;49;00m:[04m[32mnd[39;49;00m=\E[C:[04m[32mr2[39;49;00m=\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:[04m[32mrc[39;49;00m=\E8:\[37m[39;49;00m$
   859^I[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[0%?%p1%p6%|%t;1%;%?%p2%t;4%;%?%p1%p3%|%t;7%;%?%p4%t;5%;m%?%p9%t\016%e\017%;:\[37m[39;49;00m$
   860^I[37m^I[39;49;00m:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[m:[04m[32msf[39;49;00m=^J:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[m:\[37m[39;49;00m$
   861^I[37m^I[39;49;00m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:[37m[39;49;00m$
   862^I[94mvt100nam[39;49;00m|[36mvt100-nam[39;49;00m|[36mvt100 no automargins[39;49;00m:\[37m[39;49;00m$
   863^I[37m^I[39;49;00m:[04m[32mam@[39;49;00m:[04m[32mxn@[39;49;00m:[04m[32mtc[39;49;00m=vt100-am:[37m[39;49;00m$
   864^I[94mvt100-vb[39;49;00m|[36mdec vt100 (w/advanced video) & no beep[39;49;00m:\[37m[39;49;00m$
   865^I[37m^I[39;49;00m:[04m[32mbl@[39;49;00m:[04m[32mvb[39;49;00m=\E[?5h\E[?5l:[04m[32mtc[39;49;00m=vt100:[37m[39;49;00m$
   866^I[37m[39;49;00m$
   867^I[37m# Ordinary vt100 in 132 column ("wide") mode.[39;49;00m[37m[39;49;00m$
   868^I[94mvt100-w[39;49;00m|[36mvt100-w-am[39;49;00m|[36mdec vt100 132 cols (w/advanced video)[39;49;00m:\[37m[39;49;00m$
   869^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:\[37m[39;49;00m$
   870^I[37m^I[39;49;00m:[04m[32mr2[39;49;00m=\E>\E[?3h\E[?4l\E[?5l\E[?8h:[04m[32mtc[39;49;00m=vt100-am:[37m[39;49;00m$
   871^I[94mvt100-w-nam[39;49;00m|[36mvt100-nam-w[39;49;00m|[36mdec vt100 132 cols (w/advanced video no automargin)[39;49;00m:\[37m[39;49;00m$
   872^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m14[39;49;00m:[04m[32mvt@[39;49;00m:\[37m[39;49;00m$
   873^I[37m^I[39;49;00m:[04m[32mr2[39;49;00m=\E>\E[?3h\E[?4l\E[?5l\E[?8h:[04m[32mtc[39;49;00m=vt100-nam:[37m[39;49;00m$
   874^I[37m[39;49;00m$
   875^I[37m# vt100 with no advanced video.[39;49;00m[37m[39;49;00m$
   876^I[94mvt100-nav[39;49;00m|[36mvt100 without advanced video option[39;49;00m:\[37m[39;49;00m$
   877^I[37m^I[39;49;00m:[04m[32msg[39;49;00m#[34m1[39;49;00m:\[37m[39;49;00m$
   878^I[37m^I[39;49;00m:[04m[32mmb@[39;49;00m:[04m[32mmd@[39;49;00m:[04m[32mme@[39;49;00m:[04m[32mmr@[39;49;00m:[04m[32msa@[39;49;00m:[04m[32mse[39;49;00m=\E[m:[04m[32mso[39;49;00m=\E[7m:[04m[32mue@[39;49;00m:[04m[32mus@[39;49;00m:[04m[32mtc[39;49;00m=vt100:[37m[39;49;00m$
   879^I[94mvt100-nav-w[39;49;00m|[36mvt100-w-nav[39;49;00m|[36mdec vt100 132 cols 14 lines (no advanced video option)[39;49;00m:\[37m[39;49;00m$
   880^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m14[39;49;00m:[04m[32mtc[39;49;00m=vt100-nav:[37m[39;49;00m$
   881^I[37m[39;49;00m$
   882^I[37m# vt100 with one of the 24 lines used as a status line.[39;49;00m[37m[39;49;00m$
   883^I[37m# We put the status line on the top.[39;49;00m[37m[39;49;00m$
   884^I[94mvt100-s[39;49;00m|[36mvt100-s-top[39;49;00m|[36mvt100-top-s[39;49;00m|[36mvt100 for use with top sysline[39;49;00m:\[37m[39;49;00m$
   885^I[37m^I[39;49;00m:[04m[32mes[39;49;00m:[04m[32mhs[39;49;00m:\[37m[39;49;00m$
   886^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m23[39;49;00m:\[37m[39;49;00m$
   887^I[37m^I[39;49;00m:[04m[32mcl[39;49;00m=\E[2;1H\E[J:[04m[32mcm[39;49;00m=\E[%i%+^A;%dH:[04m[32mcs[39;49;00m=\E[%i%i%d;%dr:\[37m[39;49;00m$
   888^I[37m^I[39;49;00m:[04m[32mds[39;49;00m=\E7\E[1;24r\E8:[04m[32mfs[39;49;00m=\E8:[04m[32mho[39;49;00m=\E[2;1H:[04m[32mis[39;49;00m=\E7\E[2;24r\E8:\[37m[39;49;00m$
   889^I[37m^I[39;49;00m:[04m[32mts[39;49;00m=\E7\E[1;%p1%dH\E[1K:\[37m[39;49;00m$
   890^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt100-am:[37m[39;49;00m$
   891^I[37m[39;49;00m$
   892^I[37m# Status line at bottom. [39;49;00m[37m[39;49;00m$
   893^I[37m# Clearing the screen will clobber status line.[39;49;00m[37m[39;49;00m$
   894^I[94mvt100-s-bot[39;49;00m|[36mvt100-bot-s[39;49;00m|[36mvt100 for use with bottom sysline[39;49;00m:\[37m[39;49;00m$
   895^I[37m^I[39;49;00m:[04m[32mes[39;49;00m:[04m[32mhs[39;49;00m:\[37m[39;49;00m$
   896^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m23[39;49;00m:\[37m[39;49;00m$
   897^I[37m^I[39;49;00m:[04m[32mds[39;49;00m=\E7\E[1;24r\E8:[04m[32mfs[39;49;00m=\E8:[04m[32mis[39;49;00m=\E[1;23r\E[23;1H:\[37m[39;49;00m$
   898^I[37m^I[39;49;00m:[04m[32mts[39;49;00m=\E7\E[24;%p1%dH\E[1K:\[37m[39;49;00m$
   899^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt100-am:[37m[39;49;00m$
   900^I[37m[39;49;00m$
   901^I[37m# Most of the `vt100' emulators out there actually emulate a vt102[39;49;00m[37m[39;49;00m$
   902^I[37m# This entry (or vt102-nsgr) is probably the right thing to use for[39;49;00m[37m[39;49;00m$
   903^I[37m# these.  [39;49;00m[37m[39;49;00m$
   904^I[94mvt102[39;49;00m|[36mdec vt102[39;49;00m:\[37m[39;49;00m$
   905^I[37m^I[39;49;00m:[04m[32mmi[39;49;00m:\[37m[39;49;00m$
   906^I[37m^I[39;49;00m:[04m[32mal[39;49;00m=\E[L:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mei[39;49;00m=\E[4l:[04m[32mim[39;49;00m=\E[4h:[04m[32mtc[39;49;00m=vt100:[37m[39;49;00m$
   907^I[94mvt102-w[39;49;00m|[36mdec vt102 in wide mode[39;49;00m:\[37m[39;49;00m$
   908^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:\[37m[39;49;00m$
   909^I[37m^I[39;49;00m:[04m[32mr3[39;49;00m=\E[?3h:[04m[32mtc[39;49;00m=vt102:[37m[39;49;00m$
   910^I[37m[39;49;00m$
   911^I[37m# Many brain-dead PC comm programs that pretend to be `vt100-compatible'[39;49;00m[37m[39;49;00m$
   912^I[37m# fail to interpret the ^O and ^N escapes properly.  Symptom: the :me:[39;49;00m[37m[39;49;00m$
   913^I[37m# string in the canonical vt100 entry above leaves the screen littered[39;49;00m[37m[39;49;00m$
   914^I[37m# with little  snowflake or star characters (IBM PC ROM character \017 = ^O)[39;49;00m[37m[39;49;00m$
   915^I[37m# after highlight turnoffs.  This entry should fix that, and even leave[39;49;00m[37m[39;49;00m$
   916^I[37m# ACS support working, at the cost of making multiple-highlight changes [39;49;00m[37m[39;49;00m$
   917^I[37m# slightly more expensive.[39;49;00m[37m[39;49;00m$
   918^I[37m# From: Eric S. Raymond <esr@snark.thyrsus.com> July 22 1995[39;49;00m[37m[39;49;00m$
   919^I[94mvt102-nsgr[39;49;00m|[36mvt102 no sgr (use if you see snowflakes after highlight changes)[39;49;00m:\[37m[39;49;00m$
   920^I[37m^I[39;49;00m:[04m[32mme[39;49;00m=\E[m:[04m[32msa@[39;49;00m:\[37m[39;49;00m$
   921^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt102:[37m[39;49;00m$
   922^I[37m[39;49;00m$
   923^I[37m# VT125 Graphics CRT.  Clear screen also erases graphics[39;49;00m[37m[39;49;00m$
   924^I[94mvt125[39;49;00m|[36mvt125 graphics terminal[39;49;00m:\[37m[39;49;00m$
   925^I[37m^I[39;49;00m:[04m[32mcl[39;49;00m=\E[H\E[2J\EPpS(E)\E\:[04m[32mtc[39;49;00m=vt100:[37m[39;49;00m$
   926^I[37m[39;49;00m$
   927^I[37m# This isn't a DEC entry, it came from University of Wisconsin.[39;49;00m[37m[39;49;00m$
   928^I[37m# (vt131: I added <rmam>/<smam> based on the init string, also :bs: -- esr)[39;49;00m[37m[39;49;00m$
   929^I[94mvt131[39;49;00m|[36mdec vt131[39;49;00m:\[37m[39;49;00m$
   930^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbs[39;49;00m:[04m[32mxn[39;49;00m:\[37m[39;49;00m$
   931^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m$
   932^I[37m^I[39;49;00m:[04m[32mRA[39;49;00m=\E[?7h:[04m[32mSA[39;49;00m=\E[?7h:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=50\E[J:[04m[32mce[39;49;00m=3\E[K:\[37m[39;49;00m$
   933^I[37m^I[39;49;00m:[04m[32mcl[39;49;00m=50\E[;H\E[2J:[04m[32mcm[39;49;00m=5\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:\[37m[39;49;00m$
   934^I[37m^I[39;49;00m:[04m[32mdo[39;49;00m=^J:[04m[32mho[39;49;00m=\E[H:[04m[32mis[39;49;00m=\E[1;24r\E[24;1H:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:\[37m[39;49;00m$
   935^I[37m^I[39;49;00m:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\EOB:[04m[32mke[39;49;00m=\E[?1l\E>:[04m[32mkl[39;49;00m=\EOD:\[37m[39;49;00m$
   936^I[37m^I[39;49;00m:[04m[32mkr[39;49;00m=\EOC:[04m[32mks[39;49;00m=\E[?1h\E=:[04m[32mku[39;49;00m=\EOA:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=2\E[5m:[04m[32mmd[39;49;00m=2\E[1m:\[37m[39;49;00m$
   937^I[37m^I[39;49;00m:[04m[32mme[39;49;00m=2\E[m:[04m[32mmr[39;49;00m=2\E[7m:[04m[32mnd[39;49;00m=2\E[C:[04m[32mnw[39;49;00m=^M^J:\[37m[39;49;00m$
   938^I[37m^I[39;49;00m:[04m[32mr1[39;49;00m=\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:[04m[32mrc[39;49;00m=\E8:[04m[32msc[39;49;00m=\E7:\[37m[39;49;00m$
   939^I[37m^I[39;49;00m:[04m[32mse[39;49;00m=2\E[m:[04m[32mso[39;49;00m=2\E[7m:[04m[32msr[39;49;00m=5\EM:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=2\E[m:[04m[32mup[39;49;00m=2\E[A:\[37m[39;49;00m$
   940^I[37m^I[39;49;00m:[04m[32mus[39;49;00m=2\E[4m:[37m[39;49;00m$
   941^I[37m[39;49;00m$
   942^I[37m# vt132 - like vt100 but slower and has ins/del line and such.[39;49;00m[37m[39;49;00m$
   943^I[37m# I'm told that :im:/:ei: are backwards in the terminal from the[39;49;00m[37m[39;49;00m$
   944^I[37m# manual and from the ANSI standard, this describes the actual [39;49;00m[37m[39;49;00m$
   945^I[37m# terminal. I've never actually used a vt132 myself, so this [39;49;00m[37m[39;49;00m$
   946^I[37m# is untested.[39;49;00m[37m[39;49;00m$
   947^I[37m#[39;49;00m[37m[39;49;00m$
   948^I[94mvt132[39;49;00m|[36mDEC vt132[39;49;00m:\[37m[39;49;00m$
   949^I[37m^I[39;49;00m:[04m[32mxn[39;49;00m:\[37m[39;49;00m$
   950^I[37m^I[39;49;00m:[04m[32mal[39;49;00m=\E[L:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mei[39;49;00m=\E[4h:[04m[32mim[39;49;00m=\E[4l:[04m[32mip[39;49;00m=:[04m[32msf[39;49;00m=\n:[04m[32mtc[39;49;00m=vt100:[37m[39;49;00m$
   951^I[37m[39;49;00m$
   952^I[37m# This vt220 description maps F5--F9 to the second block of function keys[39;49;00m[37m[39;49;00m$
   953^I[37m# at the top of the keyboard.  The "DO" key is used as F10 to avoid conflict[39;49;00m[37m[39;49;00m$
   954^I[37m# with the key marked (ESC) on the vt220.  See vt220d for an alternate mapping.[39;49;00m[37m[39;49;00m$
   955^I[37m# PF1--PF4 are used as F1--F4.[39;49;00m[37m[39;49;00m$
   956^I[37m#[39;49;00m[37m[39;49;00m$
   957^I[94mvt220-old[39;49;00m|[36mvt200-old[39;49;00m|[36mDEC VT220 in vt100 emulation mode[39;49;00m:\[37m[39;49;00m$
   958^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbs[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mpt[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m$
   959^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m$
   960^I[37m^I[39;49;00m:[04m[32m@7[39;49;00m=\E[4~:[04m[32mRA[39;49;00m=\E[?7l:[04m[32mSA[39;49;00m=\E[?7h:\[37m[39;49;00m$
   961^I[37m^I[39;49;00m:[04m[32mac[39;49;00m=``aaffggjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~:\[37m[39;49;00m$
   962^I[37m^I[39;49;00m:[04m[32mae[39;49;00m=\E(B:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=\E(0:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:\[37m[39;49;00m$
   963^I[37m^I[39;49;00m:[04m[32mcl[39;49;00m=\E[H\E[2J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:\[37m[39;49;00m$
   964^I[37m^I[39;49;00m:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=\E[B:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:\[37m[39;49;00m$
   965^I[37m^I[39;49;00m:[04m[32mif[39;49;00m=/usr/share/tabset/vt100:[04m[32mim[39;49;00m=\E[4h:\[37m[39;49;00m$
   966^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;24r\E[24;1H:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:\[37m[39;49;00m$
   967^I[37m^I[39;49;00m:[04m[32mk5[39;49;00m=\E[17~:[04m[32mk6[39;49;00m=\E[18~:[04m[32mk7[39;49;00m=\E[19~:[04m[32mk8[39;49;00m=\E[20~:[04m[32mk9[39;49;00m=\E[21~:\[37m[39;49;00m$
   968^I[37m^I[39;49;00m:[04m[32mk;[39;49;00m=\E[29~:[04m[32mkD[39;49;00m=\E[3~:[04m[32mkI[39;49;00m=\E[2~:[04m[32mkN[39;49;00m=\E[6~:[04m[32mkP[39;49;00m=\E[5~:[04m[32mkb[39;49;00m=^H:\[37m[39;49;00m$
   969^I[37m^I[39;49;00m:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[1~:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:\[37m[39;49;00m$
   970^I[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mnl[39;49;00m=^J:\[37m[39;49;00m$
   971^I[37m^I[39;49;00m:[04m[32mr2[39;49;00m=\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:[04m[32mrc[39;49;00m=\E8:\[37m[39;49;00m$
   972^I[37m^I[39;49;00m:[04m[32mrf[39;49;00m=/usr/share/tabset/vt100:\[37m[39;49;00m$
   973^I[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[0%?%p6%t;1%;%?%p2%t;4%;%?%p4%t;5%;%?%p1%p3%|%t;7%;m%?%p9%t\E(0%e\E(B%;:\[37m[39;49;00m$
   974^I[37m^I[39;49;00m:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[27m:[04m[32msf[39;49;00m=20\ED:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=14\EM:[04m[32mta[39;49;00m=^I:\[37m[39;49;00m$
   975^I[37m^I[39;49;00m:[04m[32mue[39;49;00m=\E[24m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:[04m[32mve[39;49;00m=\E[?25h:[04m[32mvi[39;49;00m=\E[?25l:[37m[39;49;00m$
   976^I[37m[39;49;00m$
   977^I[37m# A much better description of the VT200/220; used to be vt220-8[39;49;00m[37m[39;49;00m$
   978^I[37m# (untranslatable capabilities removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m$
   979^I[37m# (sgr removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m$
   980^I[37m# (terminfo-only capabilities suppressed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m$
   981^I[94mvt220[39;49;00m|[36mvt200[39;49;00m|[36mdec vt220[39;49;00m:\[37m[39;49;00m$
   982^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbs[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mms[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m$
   983^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m$
   984^I[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mIC[39;49;00m=\E[%d@:\[37m[39;49;00m$
   985^I[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mUP[39;49;00m=\E[%dA:[04m[32mae[39;49;00m=^O:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=^N:[04m[32mbl[39;49;00m=^G:\[37m[39;49;00m$
   986^I[37m^I[39;49;00m:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:\[37m[39;49;00m$
   987^I[37m^I[39;49;00m:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mct[39;49;00m=\E[3g:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=^J:[04m[32mec[39;49;00m=\E[%dX:\[37m[39;49;00m$
   988^I[37m^I[39;49;00m:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:[04m[32mif[39;49;00m=/usr/share/tabset/vt100:[04m[32mim[39;49;00m=\E[4h:\[37m[39;49;00m$
   989^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[?7h\E[>\E[?1h\E F\E[?4l:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:[04m[32mk3[39;49;00m=\EOR:\[37m[39;49;00m$
   990^I[37m^I[39;49;00m:[04m[32mk4[39;49;00m=\EOS:[04m[32mk6[39;49;00m=\E[17~:[04m[32mk7[39;49;00m=\E[18~:[04m[32mk8[39;49;00m=\E[19~:[04m[32mk9[39;49;00m=\E[20~:[04m[32mkI[39;49;00m=\E[2~:\[37m[39;49;00m$
   991^I[37m^I[39;49;00m:[04m[32mkN[39;49;00m=\E[6~:[04m[32mkP[39;49;00m=\E[5~:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[H:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:\[37m[39;49;00m$
   992^I[37m^I[39;49;00m:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:\[37m[39;49;00m$
   993^I[37m^I[39;49;00m:[04m[32mnw[39;49;00m=\EE:[04m[32mrc[39;49;00m=\E8:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[27m:[04m[32msf[39;49;00m=\ED:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:\[37m[39;49;00m$
   994^I[37m^I[39;49;00m:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[24m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:[04m[32mvb[39;49;00m=\E[?5h\E[?5l:[37m[39;49;00m$
   995^I[94mvt220-w[39;49;00m|[36mvt200-w[39;49;00m|[36mDEC vt220 in wide mode[39;49;00m:\[37m[39;49;00m$
   996^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:\[37m[39;49;00m$
   997^I[37m^I[39;49;00m:[04m[32mr3[39;49;00m=\E[?3h:[04m[32mtc[39;49;00m=vt220:[37m[39;49;00m$
   998^I[37m# (untranslatable capabilities removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m$
   999^I[37m# (sgr removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m$
  1000^I[37m# (terminfo-only capabilities suppressed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m$
  1001^I[94mvt220-8bit[39;49;00m|[36mvt220-8[39;49;00m|[36mvt200-8bit[39;49;00m|[36mvt200-8[39;49;00m|[36mdec vt220/200 in 8-bit mode[39;49;00m:\[37m[39;49;00m$
  1002^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbs[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mms[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m$
  1003^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m$
  1004^I[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\233%dL:[04m[32mDC[39;49;00m=\233%dP:[04m[32mDL[39;49;00m=\233%dM:[04m[32mDO[39;49;00m=\233%dB:[04m[32mIC[39;49;00m=\233%d@:\[37m[39;49;00m$
  1005^I[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\233%dD:[04m[32mRI[39;49;00m=\233%dC:[04m[32mUP[39;49;00m=\233%dA:[04m[32mae[39;49;00m=^O:[04m[32mal[39;49;00m=\233L:[04m[32mas[39;49;00m=^N:\[37m[39;49;00m$
  1006^I[37m^I[39;49;00m:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\233J:[04m[32mce[39;49;00m=\233K:[04m[32mcl[39;49;00m=\233H\233J:[04m[32mcm[39;49;00m=\233%i%d;%dH:\[37m[39;49;00m$
  1007^I[37m^I[39;49;00m:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\233%i%d;%dr:[04m[32mct[39;49;00m=\2333g:[04m[32mdc[39;49;00m=\233P:[04m[32mdl[39;49;00m=\233M:[04m[32mdo[39;49;00m=^J:\[37m[39;49;00m$
  1008^I[37m^I[39;49;00m:[04m[32mec[39;49;00m=\233%dX:[04m[32mei[39;49;00m=\2334l:[04m[32mho[39;49;00m=\233H:\[37m[39;49;00m$
  1009^I[37m^I[39;49;00m:[04m[32mif[39;49;00m=/usr/share/tabset/vt100:[04m[32mim[39;49;00m=\2334h:\[37m[39;49;00m$
  1010^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\233?7h\233>\233?1h\E F\233?4l:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:\[37m[39;49;00m$
  1011^I[37m^I[39;49;00m:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:[04m[32mk6[39;49;00m=\23317~:[04m[32mk7[39;49;00m=\23318~:[04m[32mk8[39;49;00m=\23319~:\[37m[39;49;00m$
  1012^I[37m^I[39;49;00m:[04m[32mk9[39;49;00m=\23320~:[04m[32mkI[39;49;00m=\2332~:[04m[32mkN[39;49;00m=\2336~:[04m[32mkP[39;49;00m=\2335~:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\233B:\[37m[39;49;00m$
  1013^I[37m^I[39;49;00m:[04m[32mkh[39;49;00m=\233H:[04m[32mkl[39;49;00m=\233D:[04m[32mkr[39;49;00m=\233C:[04m[32mku[39;49;00m=\233A:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\2335m:\[37m[39;49;00m$
  1014^I[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\2331m:[04m[32mme[39;49;00m=\233m:[04m[32mmr[39;49;00m=\2337m:[04m[32mnd[39;49;00m=\233C:[04m[32mnw[39;49;00m=\EE:[04m[32mrc[39;49;00m=\E8:\[37m[39;49;00m$
  1015^I[37m^I[39;49;00m:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\23327m:[04m[32msf[39;49;00m=\ED:[04m[32mso[39;49;00m=\2337m:[04m[32msr[39;49;00m=\EM:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:\[37m[39;49;00m$
  1016^I[37m^I[39;49;00m:[04m[32mue[39;49;00m=\23324m:[04m[32mup[39;49;00m=\233A:[04m[32mus[39;49;00m=\2334m:[04m[32mvb[39;49;00m=\233?5h\233?5l:[37m[39;49;00m$
  1017^I[37m[39;49;00m$
  1018^I[37m#[39;49;00m[37m[39;49;00m$
  1019^I[37m# vt220d:[39;49;00m[37m[39;49;00m$
  1020^I[37m# This vt220 description regards F6--F10 as the second block of function keys[39;49;00m[37m[39;49;00m$
  1021^I[37m# at the top of the keyboard.  This mapping follows the description given[39;49;00m[37m[39;49;00m$
  1022^I[37m# in the VT220 Programmer Reference Manual and agrees with the labeling[39;49;00m[37m[39;49;00m$
  1023^I[37m# on some terminals that emulate the vt220.  There is no support for an F5.[39;49;00m[37m[39;49;00m$
  1024^I[37m# See vt220 for an alternate mapping. [39;49;00m[37m[39;49;00m$
  1025^I[37m#[39;49;00m[37m[39;49;00m$
  1026^I[94mvt220d[39;49;00m|[36mDEC VT220 in vt100 mode with DEC function key labeling[39;49;00m:\[37m[39;49;00m$
  1027^I[37m^I[39;49;00m:[04m[32mF1[39;49;00m=\E[23~:[04m[32mF2[39;49;00m=\E[24~:[04m[32mF3[39;49;00m=\E[25~:[04m[32mF4[39;49;00m=\E[26~:[04m[32mF5[39;49;00m=\E[28~:\[37m[39;49;00m$
  1028^I[37m^I[39;49;00m:[04m[32mF6[39;49;00m=\E[29~:[04m[32mF7[39;49;00m=\E[31~:[04m[32mF8[39;49;00m=\E[32~:[04m[32mF9[39;49;00m=\E[33~:[04m[32mFA[39;49;00m=\E[34~:[04m[32mk5@[39;49;00m:\[37m[39;49;00m$
  1029^I[37m^I[39;49;00m:[04m[32mk6[39;49;00m=\E[17~:[04m[32mk7[39;49;00m=\E[18~:[04m[32mk8[39;49;00m=\E[19~:[04m[32mk9[39;49;00m=\E[20~:[04m[32mk;[39;49;00m=\E[21~:\[37m[39;49;00m$
  1030^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt220-old:[37m[39;49;00m$
  1031^I[37m[39;49;00m$
  1032^I[94mvt220-nam[39;49;00m|[36mv200-nam[39;49;00m|[36mVT220 in vt100 mode with no auto margins[39;49;00m:\[37m[39;49;00m$
  1033^I[37m^I[39;49;00m:[04m[32mam@[39;49;00m:\[37m[39;49;00m$
  1034^I[37m^I[39;49;00m:[04m[32mr2[39;49;00m=\E>\E[?3l\E[?4l\E[?5l\E[?7l\E[?8h:[04m[32mtc[39;49;00m=vt220:[37m[39;49;00m$
  1035^I[37m[39;49;00m$
  1036^I[37m# vt220 termcap written Tue Oct 25 20:41:10 1988 by Alex Latzko[39;49;00m[37m[39;49;00m$
  1037^I[37m# (not an official DEC entry!)[39;49;00m[37m[39;49;00m$
  1038^I[37m# The problem with real vt220 terminals is they don't send escapes when in[39;49;00m[37m[39;49;00m$
  1039^I[37m# in vt220 mode.  This can be gotten around two ways.  1> don't send[39;49;00m[37m[39;49;00m$
  1040^I[37m# escapes or 2> put the vt220 into vt100 mode and use all the nifty[39;49;00m[37m[39;49;00m$
  1041^I[37m# features of vt100 advanced video which it then has.[39;49;00m[37m[39;49;00m$
  1042^I[37m#[39;49;00m[37m[39;49;00m$
  1043^I[37m# This entry takes the view of putting a vt220 into vt100 mode so[39;49;00m[37m[39;49;00m$
  1044^I[37m# you can use the escape key in emacs and everything else which needs it.[39;49;00m[37m[39;49;00m$
  1045^I[37m#[39;49;00m[37m[39;49;00m$
  1046^I[37m# You probably don't want to use this on a VMS machine since VMS will think[39;49;00m[37m[39;49;00m$
  1047^I[37m# it has a vt220 and will get fouled up coming out of emacs[39;49;00m[37m[39;49;00m$
  1048^I[37m#[39;49;00m[37m[39;49;00m$
  1049^I[37m# From: Alexander Latzko <latzko@marsenius.rutgers.edu>, 30 Dec 1996[39;49;00m[37m[39;49;00m$
  1050^I[37m# (Added vt100 :rc:,:sc: to quiet a tic warning -- esr)[39;49;00m[37m[39;49;00m$
  1051^I[94mvt200-js[39;49;00m|[36mvt220-js[39;49;00m|[36mdec vt200 series with jump scroll[39;49;00m:\[37m[39;49;00m$
  1052^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:\[37m[39;49;00m$
  1053^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:\[37m[39;49;00m$
  1054^I[37m^I[39;49;00m:[04m[32mal[39;49;00m=\E[L:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:\[37m[39;49;00m$
  1055^I[37m^I[39;49;00m:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdm[39;49;00m=:[04m[32mdo[39;49;00m=^J:[04m[32med[39;49;00m=:\[37m[39;49;00m$
  1056^I[37m^I[39;49;00m:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:[04m[32mim[39;49;00m=\E[4h:\[37m[39;49;00m$
  1057^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[61"p\E[H\E[?3l\E[?4l\E[?1l\E[?5l\E[?6l\E[?7h\E[?8h\E[?25h\E>\E[m:\[37m[39;49;00m$
  1058^I[37m^I[39;49;00m:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\EOB:\[37m[39;49;00m$
  1059^I[37m^I[39;49;00m:[04m[32mke[39;49;00m=\E[?1l\E>:[04m[32mkl[39;49;00m=\EOD:[04m[32mkr[39;49;00m=\EOC:[04m[32mks[39;49;00m=\E[?1h\E=:[04m[32mku[39;49;00m=\EOA:[04m[32mle[39;49;00m=^H:\[37m[39;49;00m$
  1060^I[37m^I[39;49;00m:[04m[32mnw[39;49;00m=^M\ED:[04m[32mr1[39;49;00m=\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:[04m[32mrc[39;49;00m=\E8:\[37m[39;49;00m$
  1061^I[37m^I[39;49;00m:[04m[32mrf[39;49;00m=/usr/lib/tabset/vt100:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=5\E[27m:[04m[32msf[39;49;00m=\ED:\[37m[39;49;00m$
  1062^I[37m^I[39;49;00m:[04m[32mso[39;49;00m=5\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[24m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:[37m[39;49;00m$
  1063^I[37m [39;49;00m[37m[39;49;00m$
  1064^I[37m[39;49;00m$
  1065^I[37m# This was DEC's vt320.  Use the purpose-built one below instead [39;49;00m[37m[39;49;00m$
  1066^I[37m#vt320|DEC VT320 in vt100 emulation mode,[39;49;00m[37m[39;49;00m$
  1067^I[37m#^Iuse=vt220,[39;49;00m[37m[39;49;00m$
  1068^I[37m[39;49;00m$
  1069^I[37m#[39;49;00m[37m[39;49;00m$
  1070^I[37m# Use v320n for SCO's LYRIX.  Otherwise, use Adam Thompson's vt320-nam.[39;49;00m[37m[39;49;00m$
  1071^I[37m#[39;49;00m[37m[39;49;00m$
  1072^I[94mvt320nam[39;49;00m|[36mv320n[39;49;00m|[36mDEC VT320 in vt100 emul. mode with NO AUTO WRAP mode[39;49;00m:\[37m[39;49;00m$
  1073^I[37m^I[39;49;00m:[04m[32mam@[39;49;00m:\[37m[39;49;00m$
  1074^I[37m^I[39;49;00m:[04m[32mr2[39;49;00m=\E>\E[?3l\E[?4l\E[?5l\E[?7l\E[?8h:[04m[32mtc[39;49;00m=vt220:[37m[39;49;00m$
  1075^I[37m[39;49;00m$
  1076^I[37m# These entries are not DEC's official ones, they were purpose-built for the [39;49;00m[37m[39;49;00m$
  1077^I[37m# VT320.  Here are the designer's notes:[39;49;00m[37m[39;49;00m$
  1078^I[37m# <kel> is end on a PC kbd.  Actually 'select' on a VT.  Mapped to [39;49;00m[37m[39;49;00m$
  1079^I[37m# 'Erase to End of Field'... since nothing seems to use 'end' anyways...[39;49;00m[37m[39;49;00m$
  1080^I[37m# khome is Home on a PC kbd.  Actually 'FIND' on a VT.[39;49;00m[37m[39;49;00m$
  1081^I[37m# Things that use <knxt> usually use tab anyways... and things that don't use[39;49;00m[37m[39;49;00m$
  1082^I[37m# tab usually use <knxt> instead...[39;49;00m[37m[39;49;00m$
  1083^I[37m# kprv is same as tab - Backtab is useless...[39;49;00m[37m[39;49;00m$
  1084^I[37m# I left out :sa: because of its RIDICULOUS complexity,[39;49;00m[37m[39;49;00m$
  1085^I[37m# and the resulting fact that it causes the termcap translation of the entry[39;49;00m[37m[39;49;00m$
  1086^I[37m# to SMASH the 1k-barrier...[39;49;00m[37m[39;49;00m$
  1087^I[37m# From: Adam Thompson <athompso@pangea.ca> Sept 10 1995[39;49;00m[37m[39;49;00m$
  1088^I[37m# (vt320: uncommented :fs:, comnmmented out <kslt> to avoid a conflict --esr) [39;49;00m[37m[39;49;00m$
  1089^I[37m# (untranslatable capabilities removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m$
  1090^I[37m# (sgr removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m$
  1091^I[37m# (terminfo-only capabilities suppressed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m$
  1092^I[94mvt320[39;49;00m|[36mvt300[39;49;00m|[36mdec vt320 7 bit terminal[39;49;00m:\[37m[39;49;00m$
  1093^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mes[39;49;00m:[04m[32mhs[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mms[39;49;00m:[04m[32mxn[39;49;00m:\[37m[39;49;00m$
  1094^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mws[39;49;00m#[34m80[39;49;00m:\[37m[39;49;00m$
  1095^I[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mIC[39;49;00m=\E[%d@:\[37m[39;49;00m$
  1096^I[37m^I[39;49;00m:[04m[32mK1[39;49;00m=\EOw:[04m[32mK2[39;49;00m=\EOu:[04m[32mK3[39;49;00m=\EOy:[04m[32mK4[39;49;00m=\EOq:[04m[32mK5[39;49;00m=\EOs:[04m[32mLE[39;49;00m=\E[%dD:\[37m[39;49;00m$
  1097^I[37m^I[39;49;00m:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mUP[39;49;00m=\E[%dA:[04m[32mae[39;49;00m=\E(B:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=\E(0:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:\[37m[39;49;00m$
  1098^I[37m^I[39;49;00m:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[2J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:\[37m[39;49;00m$
  1099^I[37m^I[39;49;00m:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mct[39;49;00m=\E[3g:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=^J:[04m[32mec[39;49;00m=\E[%dX:\[37m[39;49;00m$
  1100^I[37m^I[39;49;00m:[04m[32mei[39;49;00m=\E[4l:[04m[32mfs[39;49;00m=\E[0$}:[04m[32mho[39;49;00m=\E[H:[04m[32mim[39;49;00m=\E[4h:\[37m[39;49;00m$
  1101^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E>\E[?3l\E[?4l\E[5?l\E[?7h\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m$
  1102^I[37m^I[39;49;00m:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:[04m[32mk6[39;49;00m=\E[17~:[04m[32mk7[39;49;00m=\E[18~:\[37m[39;49;00m$
  1103^I[37m^I[39;49;00m:[04m[32mk8[39;49;00m=\E[19~:[04m[32mk9[39;49;00m=\E[20~:[04m[32mkD[39;49;00m=\E[3~:[04m[32mkI[39;49;00m=\E[2~:[04m[32mkN[39;49;00m=\E[6~:[04m[32mkP[39;49;00m=\E[5~:\[37m[39;49;00m$
  1104^I[37m^I[39;49;00m:[04m[32mkb[39;49;00m=\177:[04m[32mkd[39;49;00m=\EOB:[04m[32mke[39;49;00m=\E[?1l\E>:[04m[32mkh[39;49;00m=\E[1~:[04m[32mkl[39;49;00m=\EOD:[04m[32mkr[39;49;00m=\EOC:\[37m[39;49;00m$
  1105^I[37m^I[39;49;00m:[04m[32mks[39;49;00m=\E[?1h\E=:[04m[32mku[39;49;00m=\EOA:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:\[37m[39;49;00m$
  1106^I[37m^I[39;49;00m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mnw[39;49;00m=\EE:[04m[32mrc[39;49;00m=\E8:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[m:[04m[32msf[39;49;00m=\ED:\[37m[39;49;00m$
  1107^I[37m^I[39;49;00m:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:[04m[32mts[39;49;00m=\E[1$}\E[H\E[K:[04m[32mue[39;49;00m=\E[m:\[37m[39;49;00m$
  1108^I[37m^I[39;49;00m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:[04m[32mve[39;49;00m=\E[?25h:[04m[32mvi[39;49;00m=\E[?25l:[37m[39;49;00m$
  1109^I[94mvt320-nam[39;49;00m|[36mvt300-nam[39;49;00m|[36mdec vt320 7 bit terminal with no am to make SAS happy[39;49;00m:\[37m[39;49;00m$
  1110^I[37m^I[39;49;00m:[04m[32mam@[39;49;00m:\[37m[39;49;00m$
  1111^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E>\E[?3l\E[?4l\E[5?l\E[?7l\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m$
  1112^I[37m^I[39;49;00m:[04m[32mr2[39;49;00m=\E>\E[?3l\E[?4l\E[5?l\E[?7l\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m$
  1113^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt320:[37m[39;49;00m$
  1114^I[37m# We have to init 132-col mode, not 80-col mode.[39;49;00m[37m[39;49;00m$
  1115^I[94mvt320-w[39;49;00m|[36mvt300-w[39;49;00m|[36mdec vt320 wide 7 bit terminal[39;49;00m:\[37m[39;49;00m$
  1116^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mws[39;49;00m#[34m132[39;49;00m:\[37m[39;49;00m$
  1117^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E>\E[?3h\E[?4l\E[5?l\E[?7h\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m$
  1118^I[37m^I[39;49;00m:[04m[32mr2[39;49;00m=\E>\E[?3h\E[?4l\E[5?l\E[?7h\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m$
  1119^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt320:[37m[39;49;00m$
  1120^I[94mvt320-w-nam[39;49;00m|[36mvt300-w-nam[39;49;00m|[36mdec vt320 wide 7 bit terminal with no am[39;49;00m:\[37m[39;49;00m$
  1121^I[37m^I[39;49;00m:[04m[32mam@[39;49;00m:\[37m[39;49;00m$
  1122^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E>\E[?3h\E[?4l\E[5?l\E[?7l\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m$
  1123^I[37m^I[39;49;00m:[04m[32mr2[39;49;00m=\E>\E[?3h\E[?4l\E[5?l\E[?7l\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m$
  1124^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt320-w:[37m[39;49;00m$
  1125^I[37m[39;49;00m$
  1126^I[37m# VT330 and VT340 -- These are ReGIS and SIXEL graphics terminals[39;49;00m[37m[39;49;00m$
  1127^I[37m#   which are pretty much a superset of the VT320.  They have the[39;49;00m[37m[39;49;00m$
  1128^I[37m#   host writable status line, yet another different DRCS matrix size,[39;49;00m[37m[39;49;00m$
  1129^I[37m#   and such, but they add the DEC Technical character set, Multiple text[39;49;00m[37m[39;49;00m$
  1130^I[37m#   pages, selectable length pages, and the like.  The difference between[39;49;00m[37m[39;49;00m$
  1131^I[37m#   the vt330 and vt340 is that the latter has only 2 planes and a monochrome[39;49;00m[37m[39;49;00m$
  1132^I[37m#   monitor, the former has 4 planes and a color monitor.  These terminals[39;49;00m[37m[39;49;00m$
  1133^I[37m#   support VT131 and ANSI block mode, but as with much of these things,[39;49;00m[37m[39;49;00m$
  1134^I[37m#   termcap/terminfo doesn't deal with these features.[39;49;00m[37m[39;49;00m$
  1135^I[37m#[39;49;00m[37m[39;49;00m$
  1136^I[37m# Note that this entry is are set up in what was the standard way for GNU[39;49;00m[37m[39;49;00m$
  1137^I[37m# Emacs v18 terminal modes to deal with the cursor keys in that the arrow[39;49;00m[37m[39;49;00m$
  1138^I[37m# keys were switched into application mode at the same time the numeric pad[39;49;00m[37m[39;49;00m$
  1139^I[37m# is switched into application mode.  This changes the definitions of the[39;49;00m[37m[39;49;00m$
  1140^I[37m# arrow keys.  Emacs v19 is smarter and mines its keys directly out of [39;49;00m[37m[39;49;00m$
  1141^I[37m# your termcap or terminfo entry,[39;49;00m[37m[39;49;00m$
  1142^I[37m#[39;49;00m[37m[39;49;00m$
  1143^I[37m# From: Daniel Glasser <dag@persoft.persoft.com>, 13 Oct 1993[39;49;00m[37m[39;49;00m$
  1144^I[37m# (vt340: string capability "sb=\E[M" corrected to "sr";[39;49;00m[37m[39;49;00m$
  1145^I[37m# also, added <rmam>/<smam> based on the init string -- esr)[39;49;00m[37m[39;49;00m$
  1146^I[94mvt340[39;49;00m|[36mdec-vt340[39;49;00m|[36mvt330[39;49;00m|[36mdec-vt330[39;49;00m|[36mdec vt340 graphics terminal with 24 line page[39;49;00m:\[37m[39;49;00m$
  1147^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mes[39;49;00m:[04m[32mhs[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mms[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m$
  1148^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m$
  1149^I[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mIC[39;49;00m=\E[%d@:\[37m[39;49;00m$
  1150^I[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRA[39;49;00m=\E[?7l:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mSA[39;49;00m=\E[?7h:[04m[32mUP[39;49;00m=\E[%dA:\[37m[39;49;00m$
  1151^I[37m^I[39;49;00m:[04m[32mac[39;49;00m=``aaffggjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~:\[37m[39;49;00m$
  1152^I[37m^I[39;49;00m:[04m[32mae[39;49;00m=^O:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=^N:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[J:\[37m[39;49;00m$
  1153^I[37m^I[39;49;00m:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mct[39;49;00m=\E[3g:[04m[32mdc[39;49;00m=\E[P:\[37m[39;49;00m$
  1154^I[37m^I[39;49;00m:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=^J:[04m[32mds[39;49;00m=\E[2$~\r\E[1$}\E[K\E[$}:[04m[32mei[39;49;00m=\E[4l:\[37m[39;49;00m$
  1155^I[37m^I[39;49;00m:[04m[32mfs[39;49;00m=\E[$}:[04m[32mho[39;49;00m=\E[H:[04m[32mim[39;49;00m=\E[4h:\[37m[39;49;00m$
  1156^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E<\E F\E>\E[?1h\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m$
  1157^I[37m^I[39;49;00m:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:[04m[32mk6[39;49;00m=\E[17~:[04m[32mk7[39;49;00m=\E[18~:\[37m[39;49;00m$
  1158^I[37m^I[39;49;00m:[04m[32mk8[39;49;00m=\E[19~:[04m[32mk9[39;49;00m=\E[20~:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\EOB:[04m[32mke[39;49;00m=\E[?1l\E>:[04m[32mkl[39;49;00m=\EOD:\[37m[39;49;00m$
  1159^I[37m^I[39;49;00m:[04m[32mkr[39;49;00m=\EOC:[04m[32mks[39;49;00m=\E[?1h\E=:[04m[32mku[39;49;00m=\EOA:[04m[32ml1[39;49;00m=pf1:[04m[32ml2[39;49;00m=pf2:[04m[32ml3[39;49;00m=pf3:[04m[32ml4[39;49;00m=pf4:\[37m[39;49;00m$
  1160^I[37m^I[39;49;00m:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mnw[39;49;00m=^M\ED:\[37m[39;49;00m$
  1161^I[37m^I[39;49;00m:[04m[32mr1[39;49;00m=\E[?3l:[04m[32mrc[39;49;00m=\E8:[04m[32mrf[39;49;00m=/usr/share/tabset/vt300:[04m[32msc[39;49;00m=\E7:\[37m[39;49;00m$
  1162^I[37m^I[39;49;00m:[04m[32mse[39;49;00m=\E[27m:[04m[32msf[39;49;00m=\ED:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:\[37m[39;49;00m$
  1163^I[37m^I[39;49;00m:[04m[32mts[39;49;00m=\E[2$~\E[1$}\E[1;%dH:[04m[32mue[39;49;00m=\E[24m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:\[37m[39;49;00m$
  1164^I[37m^I[39;49;00m:[04m[32mvb[39;49;00m=200\E[?5h\E[?5l:[04m[32mve[39;49;00m=\E[?25h:[04m[32mvi[39;49;00m=\E[?25l:[04m[32mvs[39;49;00m=\E[?25h:[37m[39;49;00m$
  1165^I[37m[39;49;00m$
  1166^I[37m# DEC doesn't supply a vt400 description, so we add Daniel Glasser's[39;49;00m[37m[39;49;00m$
  1167^I[37m# (originally written with vt420 as its primary name, and usable for it).[39;49;00m[37m[39;49;00m$
  1168^I[37m# [39;49;00m[37m[39;49;00m$
  1169^I[37m# VT400/420 -- This terminal is a superset of the vt320.  It adds the multiple [39;49;00m[37m[39;49;00m$
  1170^I[37m#    text pages and long text pages with selectable length of the vt340, along[39;49;00m[37m[39;49;00m$
  1171^I[37m#    with left and right margins, rectangular area text copy, fill, and erase[39;49;00m[37m[39;49;00m$
  1172^I[37m#    operations, selected region character attribute change operations,[39;49;00m[37m[39;49;00m$
  1173^I[37m#    page memory and rectangle checksums, insert/delete column, reception[39;49;00m[37m[39;49;00m$
  1174^I[37m#    macros, and other features too numerous to remember right now.  TERMCAP[39;49;00m[37m[39;49;00m$
  1175^I[37m#    can only take advantage of a few of these added features.[39;49;00m[37m[39;49;00m$
  1176^I[37m#[39;49;00m[37m[39;49;00m$
  1177^I[37m# Note that this entry is are set up in what was the standard way for GNU[39;49;00m[37m[39;49;00m$
  1178^I[37m# Emacs v18 terminal modes to deal with the cursor keys in that the arrow[39;49;00m[37m[39;49;00m$
  1179^I[37m# keys were switched into application mode at the same time the numeric pad[39;49;00m[37m[39;49;00m$
  1180^I[37m# is switched into application mode.  This changes the definitions of the[39;49;00m[37m[39;49;00m$
  1181^I[37m# arrow keys.  Emacs v19 is smarter and mines its keys directly out of [39;49;00m[37m[39;49;00m$
  1182^I[37m# your termcap entry,[39;49;00m[37m[39;49;00m$
  1183^I[37m#[39;49;00m[37m[39;49;00m$
  1184^I[37m# From: Daniel Glasser <dag@persoft.persoft.com>, 13 Oct 1993[39;49;00m[37m[39;49;00m$
  1185^I[37m# (vt400: string capability ":sb=\E[M:" corrected to ":sr=\E[M:";[39;49;00m[37m[39;49;00m$
  1186^I[37m# also, added <rmam>/<smam> based on the init string -- esr)[39;49;00m[37m[39;49;00m$
  1187^I[37m# (untranslatable capabilities removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m$
  1188^I[37m# (sgr removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m$
  1189^I[37m# (terminfo-only capabilities suppressed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m$
  1190^I[94mvt400[39;49;00m|[36mvt400-24[39;49;00m|[36mdec-vt400[39;49;00m|[36mdec vt400 24x80 column autowrap[39;49;00m:\[37m[39;49;00m$
  1191^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mes[39;49;00m:[04m[32mhs[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mms[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m$
  1192^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m$
  1193^I[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mIC[39;49;00m=\E[%d@:\[37m[39;49;00m$
  1194^I[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mUP[39;49;00m=\E[%dA:[04m[32mae[39;49;00m=^O:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=^N:\[37m[39;49;00m$
  1195^I[37m^I[39;49;00m:[04m[32mcd[39;49;00m=10\E[J:[04m[32mce[39;49;00m=4\E[K:[04m[32mcl[39;49;00m=10\E[H\E[J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:\[37m[39;49;00m$
  1196^I[37m^I[39;49;00m:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mct[39;49;00m=\E[3g:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=^J:\[37m[39;49;00m$
  1197^I[37m^I[39;49;00m:[04m[32mds[39;49;00m=\E[2$~\r\E[1$}\E[K\E[$}:[04m[32mei[39;49;00m=\E[4l:[04m[32mfs[39;49;00m=\E[$}:[04m[32mho[39;49;00m=\E[H:\[37m[39;49;00m$
  1198^I[37m^I[39;49;00m:[04m[32mic[39;49;00m=\E[@:[04m[32mim[39;49;00m=\E[4h:\[37m[39;49;00m$
  1199^I[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E<\E F\E>\E[?1h\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m$
  1200^I[37m^I[39;49;00m:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:[04m[32mk6[39;49;00m=\E[17~:[04m[32mk7[39;49;00m=\E[18~:\[37m[39;49;00m$
  1201^I[37m^I[39;49;00m:[04m[32mk8[39;49;00m=\E[19~:[04m[32mk9[39;49;00m=\E[20~:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\EOB:[04m[32mke[39;49;00m=\E[?1l\E>:[04m[32mkl[39;49;00m=\EOD:\[37m[39;49;00m$
  1202^I[37m^I[39;49;00m:[04m[32mkr[39;49;00m=\EOC:[04m[32mks[39;49;00m=\E[?1h\E=:[04m[32mku[39;49;00m=\EOA:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:\[37m[39;49;00m$
  1203^I[37m^I[39;49;00m:[04m[32mme[39;49;00m=\E[m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mnw[39;49;00m=^M\ED:[04m[32mrc[39;49;00m=\E8:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[27m:\[37m[39;49;00m$
  1204^I[37m^I[39;49;00m:[04m[32msf[39;49;00m=\ED:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:\[37m[39;49;00m$
  1205^I[37m^I[39;49;00m:[04m[32mts[39;49;00m=\E[2$~\E[1$}\E[1;%dH:[04m[32mue[39;49;00m=\E[24m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:\[37m[39;49;00m$
  1206^I[37m^I[39;49;00m:[04m[32mvb[39;49;00m=200\E[?5h\E[?5l:[04m[32mve[39;49;00m=\E[?25h:[04m[32mvi[39;49;00m=\E[?25l:[04m[32mvs[39;49;00m=\E[?25h:[37m[39;49;00m$
  1207^I[37m[39;49;00m$
  1208^I[37m# (vt420: I removed :k0:, it collided with <kf10>.  I also restored[39;49;00m[37m[39;49;00m$
  1209^I[37m# a missing :sc: -- esr)[39;49;00m[37m[39;49;00m$
  1210^I[94mvt420[39;49;00m|[36mDEC VT420[39;49;00m:\[37m[39;49;00m$
  1211^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m$
  1212^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m$
  1213^I[37m^I[39;49;00m:[04m[32m*6[39;49;00m=\E[4~:[04m[32m@0[39;49;00m=\E[1~:[04m[32mRA[39;49;00m=\E[?7l:\[37m[39;49;00m$
  1214^I[37m^I[39;49;00m:[04m[32mS5[39;49;00m=\E[?0;0r\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:\[37m[39;49;00m$
  1215^I[37m^I[39;49;00m:[04m[32mSA[39;49;00m=\E[?7h:\[37m[39;49;00m$
  1216^I[37m^I[39;49;00m:[04m[32mac[39;49;00m=``aaffggjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~:\[37m[39;49;00m$
  1217^I[37m^I[39;49;00m:[04m[32mae[39;49;00m=\E(B:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=\E(0:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:\[37m[39;49;00m$
  1218^I[37m^I[39;49;00m:[04m[32mcl[39;49;00m=\E[H\E[2J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:\[37m[39;49;00m$
  1219^I[37m^I[39;49;00m:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=\E[B:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:\[37m[39;49;00m$
  1220^I[37m^I[39;49;00m:[04m[32mi2[39;49;00m=\E[?67h\E[64;1"p:[04m[32mif[39;49;00m=/usr/share/tabset/vt300:\[37m[39;49;00m$
  1221^I[37m^I[39;49;00m:[04m[32mim[39;49;00m=\E[4h:[04m[32mis[39;49;00m=\E[1;24r\E[24;1H:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:[04m[32mk3[39;49;00m=\EOR:\[37m[39;49;00m$
  1222^I[37m^I[39;49;00m:[04m[32mk4[39;49;00m=\EOS:[04m[32mk5[39;49;00m=\E[17~:[04m[32mk6[39;49;00m=\E[18~:[04m[32mk7[39;49;00m=\E[19~:[04m[32mk8[39;49;00m=\E[20~:\[37m[39;49;00m$
  1223^I[37m^I[39;49;00m:[04m[32mk9[39;49;00m=\E[21~:[04m[32mk;[39;49;00m=\E[29~:[04m[32mkD[39;49;00m=\E[3~:[04m[32mkI[39;49;00m=\E[2~:[04m[32mkN[39;49;00m=\E[6~:[04m[32mkP[39;49;00m=\E[5~:\[37m[39;49;00m$
  1224^I[37m^I[39;49;00m:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mke[39;49;00m=\E>:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mks[39;49;00m=\E=:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:\[37m[39;49;00m$
  1225^I[37m^I[39;49;00m:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:\[37m[39;49;00m$
  1226^I[37m^I[39;49;00m:[04m[32mr3[39;49;00m=\E[?67h\E[64;1"p:[04m[32mrc[39;49;00m=\E8:[04m[32mrf[39;49;00m=/usr/share/tabset/vt300:\[37m[39;49;00m$
  1227^I[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[0%?%p6%t;1%;%?%p2%t;4%;%?%p4%t;5%;%?%p1%p3%|%t;7%;m%?%p9%t\E(0%e\E(B%;:\[37m[39;49;00m$
  1228^I[37m^I[39;49;00m:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[m:[04m[32msf[39;49;00m=\ED:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[m:\[37m[39;49;00m$
  1229^I[37m^I[39;49;00m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:[37m[39;49;00m$
  1230^I[37m[39;49;00m$
  1231^I[37m#[39;49;00m[37m[39;49;00m$
  1232^I[37m# DEC VT220 and up support DECUDK (user-defined keys).  DECUDK (i.e., pfx)[39;49;00m[37m[39;49;00m$
  1233^I[37m# takes two parameters, the key and the string.  Translating the key is[39;49;00m[37m[39;49;00m$
  1234^I[37m# straightforward (keys 1-5 are not defined on real terminals, though some[39;49;00m[37m[39;49;00m$
  1235^I[37m# emulators define these):[39;49;00m[37m[39;49;00m$
  1236^I[37m#[39;49;00m[37m[39;49;00m$
  1237^I[37m#               if (key < 16) then  value = key;[39;49;00m[37m[39;49;00m$
  1238^I[37m#               else if (key < 21) then value = key + 1; [39;49;00m[37m[39;49;00m$
  1239^I[37m#               else if (key < 25) then value = key + 2;[39;49;00m[37m[39;49;00m$
  1240^I[37m#               else if (key < 27) then value = key + 3;[39;49;00m[37m[39;49;00m$
  1241^I[37m#               else if (key < 30) then value = key + 4;[39;49;00m[37m[39;49;00m$
  1242^I[37m#               else value = key + 5;[39;49;00m[37m[39;49;00m$
  1243^I[37m#[39;49;00m[37m[39;49;00m$
  1244^I[37m# The string must be the hexadecimal equivalent, e.g., "5052494E" for "PRINT". [39;49;00m[37m[39;49;00m$
  1245^I[37m# There's no provision in terminfo for emitting a string in this format, so the[39;49;00m[37m[39;49;00m$
  1246^I[37m# application has to know it.[39;49;00m[37m[39;49;00m$
  1247^I[37m#[39;49;00m[37m[39;49;00m$
  1248^I[94mvt420pc[39;49;00m|[36mDEC VT420 w/PC keyboard[39;49;00m:\[37m[39;49;00m$
  1249^I[37m^I[39;49;00m:[04m[32m@7[39;49;00m=\E[4~:[04m[32mF1[39;49;00m=\E[23~:[04m[32mF2[39;49;00m=\E[24~:[04m[32mF3[39;49;00m=\E[11;2~:[04m[32mF4[39;49;00m=\E[12;2~:\[37m[39;49;00m$
  1250^I[37m^I[39;49;00m:[04m[32mF5[39;49;00m=\E[13;2~:[04m[32mF6[39;49;00m=\E[14;2~:[04m[32mF7[39;49;00m=\E[15;2~:[04m[32mF8[39;49;00m=\E[17;2~:\[37m[39;49;00m$
  1251^I[37m^I[39;49;00m:[04m[32mF9[39;49;00m=\E[18;2~:[04m[32mFA[39;49;00m=\E[19;2~:[04m[32mFB[39;49;00m=\E[20;2~:[04m[32mFC[39;49;00m=\E[21;2~:\[37m[39;49;00m$
  1252^I[37m^I[39;49;00m:[04m[32mFD[39;49;00m=\E[23;2~:[04m[32mFE[39;49;00m=\E[24;2~:[04m[32mFF[39;49;00m=\E[23~:[04m[32mFG[39;49;00m=\E[24~:[04m[32mFH[39;49;00m=\E[25~:\[37m[39;49;00m$
  1253^I[37m^I[39;49;00m:[04m[32mFI[39;49;00m=\E[26~:[04m[32mFJ[39;49;00m=\E[28~:[04m[32mFK[39;49;00m=\E[29~:[04m[32mFL[39;49;00m=\E[31~:[04m[32mFM[39;49;00m=\E[32~:\[37m[39;49;00m$
  1254^I[37m^I[39;49;00m:[04m[32mFN[39;49;00m=\E[33~:[04m[32mFO[39;49;00m=\E[34~:[04m[32mFP[39;49;00m=\E[35~:[04m[32mFQ[39;49;00m=\E[36~:[04m[32mFR[39;49;00m=\E[23;2~:\[37m[39;49;00m$
  1255^I[37m^I[39;49;00m:[04m[32mFS[39;49;00m=\E[24;2~:[04m[32mFT[39;49;00m=\E[25;2~:[04m[32mFU[39;49;00m=\E[26;2~:[04m[32mFV[39;49;00m=\E[28;2~:\[37m[39;49;00m$
  1256^I[37m^I[39;49;00m:[04m[32mFW[39;49;00m=\E[29;2~:[04m[32mFX[39;49;00m=\E[31;2~:[04m[32mFY[39;49;00m=\E[32;2~:[04m[32mFZ[39;49;00m=\E[33;2~:\[37m[39;49;00m$
  1257^I[37m^I[39;49;00m:[04m[32mFa[39;49;00m=\E[34;2~:[04m[32mFb[39;49;00m=\E[35;2~:[04m[32mFc[39;49;00m=\E[36;2~:\[37m[39;49;00m$
  1258^I[37m^I[39;49;00m:[04m[32mS6[39;49;00m=USR_TERM\072vt420pcdos\072:[04m[32mk1[39;49;00m=\E[11~:[04m[32mk2[39;49;00m=\E[12~:\[37m[39;49;00m$
  1259^I[37m^I[39;49;00m:[04m[32mk3[39;49;00m=\E[13~:[04m[32mk4[39;49;00m=\E[14~:[04m[32mk5[39;49;00m=\E[15~:[04m[32mk6[39;49;00m=\E[17~:[04m[32mk7[39;49;00m=\E[18~:\[37m[39;49;00m$
  1260^I[37m^I[39;49;00m:[04m[32mk8[39;49;00m=\E[19~:[04m[32mk9[39;49;00m=\E[20~:[04m[32mk;[39;49;00m=\E[21~:[04m[32mkD[39;49;00m=\177:[04m[32mkh[39;49;00m=\E[H:\[37m[39;49;00m$
  1261^I[37m^I[39;49;00m:[04m[32m..px[39;49;00m=\EP1;1|%?%{16}%p1%>%t%{0}%e%{21}%p1%>%t%{1}%e%{25}%p1%>%t%{2}%e%{27}%p1%>%t%{3}%e%{30}%p1%>%t%{4}%e%{5}%;%p1%+%d/%p2%s\E\:[04m[32mtc[39;49;00m=vt420:[37m[39;49;00m$
  1262^I[37m[39;49;00m$
  1263^I[94mvt420pcdos[39;49;00m|[36mDEC VT420 w/PC for DOS Merge[39;49;00m:\[37m[39;49;00m$
  1264^I[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:\[37m[39;49;00m$
  1265^I[37m^I[39;49;00m:[04m[32mS1[39;49;00m=%?%p2%{19}%=%t\E\023\021%e%p2%{32}%<%t\E%p2%c%e%p2%{127}%=%t\E\177%e%p2%c%;:\[37m[39;49;00m$
  1266^I[37m^I[39;49;00m:[04m[32mS4[39;49;00m=\E[?1;2r\E[34h:\[37m[39;49;00m$
  1267^I[37m^I[39;49;00m:[04m[32mS5[39;49;00m=\E[?0;0r\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:[04m[32mS6@[39;49;00m:\[37m[39;49;00m$
  1268^I[37m^I[39;49;00m:[04m[32mme[39;49;00m=\E[m:[04m[32msa@[39;49;00m:\[37m[39;49;00m$
  1269^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt420pc:[37m[39;49;00m$
  1270^I[37m[39;49;00m$
  1271^I[94mvt420f[39;49;00m|[36mDEC VT420 with VT kbd; VT400 mode; F1-F5 used as Fkeys[39;49;00m:\[37m[39;49;00m$
  1272^I[37m^I[39;49;00m:[04m[32mF1[39;49;00m=\E[23~:[04m[32mF2[39;49;00m=\E[24~:[04m[32mF3[39;49;00m=\E[25~:[04m[32mF4[39;49;00m=\E[26~:[04m[32mF5[39;49;00m=\E[28~:\[37m[39;49;00m$
  1273^I[37m^I[39;49;00m:[04m[32mF6[39;49;00m=\E[29~:[04m[32mF7[39;49;00m=\E[31~:[04m[32mF8[39;49;00m=\E[32~:[04m[32mF9[39;49;00m=\E[33~:[04m[32mFA[39;49;00m=\E[34~:\[37m[39;49;00m$
  1274^I[37m^I[39;49;00m:[04m[32mk1[39;49;00m=\E[11~:[04m[32mk2[39;49;00m=\E[12~:[04m[32mk3[39;49;00m=\E[13~:[04m[32mk4[39;49;00m=\E[14~:[04m[32mk5[39;49;00m=\E[15~:\[37m[39;49;00m$
  1275^I[37m^I[39;49;00m:[04m[32mk6[39;49;00m=\E[17~:[04m[32mk7[39;49;00m=\E[18~:[04m[32mk8[39;49;00m=\E[19~:[04m[32mk9[39;49;00m=\E[20~:[04m[32mk;[39;49;00m=\E[21~:\[37m[39;49;00m$
  1276^I[37m^I[39;49;00m:[04m[32mkD[39;49;00m=\177:[04m[32mkh[39;49;00m=\E[H:[04m[32ml1[39;49;00m=\EOP:[04m[32ml2[39;49;00m=\EOQ:[04m[32ml3[39;49;00m=\EOR:[04m[32ml4[39;49;00m=\EOS:\[37m[39;49;00m$
  1277^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt420:[37m[39;49;00m$
  1278^I[37m[39;49;00m$
  1279^I[94mvt510[39;49;00m|[36mDEC VT510[39;49;00m:\[37m[39;49;00m$
  1280^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt420:[37m[39;49;00m$
  1281^I[94mvt510pc[39;49;00m|[36mDEC VT510 w/PC keyboard[39;49;00m:\[37m[39;49;00m$
  1282^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt420pc:[37m[39;49;00m$
  1283^I[94mvt510pcdos[39;49;00m|[36mDEC VT510 w/PC for DOS Merge[39;49;00m:\[37m[39;49;00m$
  1284^I[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt420pcdos:[37m[39;49;00m$
  1285^I[37m[39;49;00m$
  1286^I[37m# VT520/VT525[39;49;00m[37m[39;49;00m$
  1287^I[37m#[39;49;00m[37m[39;49;00m$
  1288^I[37m# The VT520 is a monochrome text terminal capable of managing up to[39;49;00m[37m[39;49;00m$
  1289^I[37m# four independent sessions in the terminal.  It has multiple ANSI[39;49;00m[37m[39;49;00m$
  1290^I[37m# emulations (VT520, VT420, VT320, VT220, VT100, VT PCTerm, SCO Console)[39;49;00m[37m[39;49;00m$
  1291^I[37m# and ASCII emulations (WY160/60, PCTerm, 50/50+, 150/120, TVI 950,[39;49;00m[37m[39;49;00m$
  1292^I[37m# 925 910+, ADDS A2).  This terminfo data is for the ANSI emulations only.[39;49;00m[37m[39;49;00m$
  1293^I[37m#[39;49;00m[37m[39;49;00m$
  1294^I[37m# Terminal Set-Up is entered by pressing [F3], [Caps Lock]/[F3] or[39;49;00m[37m[39;49;00m$
  1295^I[37m# [Alt]/[Print Screen] depending upon which keyboard and which[39;49;00m[37m[39;49;00m$
  1296^I[37m# terminal mode is being used.  If Set-Up has been disabled or[39;49;00m[37m[39;49;00m$
  1297^I[37m# assigned to an unknown key, Set-Up may be entered by pressing[39;49;00m[37m[39;49;00m$
  1298^I[37m# [F3] as the first key after power up, regardless of keyboard type.[39;49;00m[37m[39;49;00m$
  1299^I[37m# (vt520: I added <rmam>/<smam> based on the init string, also :sc: -- esr)[39;49;00m[37m[39;49;00m$
  1300^I[37m# (untranslatable capabilities removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m$
  1301^I[94mvt520[39;49;00m|[36mDEC VT520[39;49;00m:\[37m[39;49;00m$
  1302^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m$
  1303^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m$
  1304^I[37m^I[39;49;00m:[04m[32m*6[39;49;00m=\E[4~:[04m[32m@0[39;49;00m=\E[1~:[04m[32mRA[39;49;00m=\E[?7l:\[37m[39;49;00m$
  1305^I[37m^I[39;49;00m:[04m[32mS5[39;49;00m=\E[?0;0r\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:\[37m[39;49;00m$
  1306^I[37m^I[39;49;00m:[04m[32mSA[39;49;00m=\E[?7h:\[37m[39;49;00m$
  1307^I[37m^I[39;49;00m:[04m[32mac[39;49;00m=``aaffggjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~:\[37m[39;49;00m$
  1308^I[37m^I[39;49;00m:[04m[32mae[39;49;00m=\E(B:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=\E(0:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:\[37m[39;49;00m$
  1309^I[37m^I[39;49;00m:[04m[32mcl[39;49;00m=\E[H\E[2J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:\[37m[39;49;00m$
  1310^I[37m^I[39;49;00m:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=\E[B:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:\[37m[39;49;00m$
  1311^I[37m^I[39;49;00m:[04m[32mi2[39;49;00m=\E[?67h\E[64;1"p:[04m[32mif[39;49;00m=/usr/share/tabset/vt300:\[37m[39;49;00m$
  1312^I[37m^I[39;49;00m:[04m[32mim[39;49;00m=\E[4h:[04m[32mis[39;49;00m=\E[1;24r\E[24;1H:[04m[32mk0[39;49;00m=\E[29~:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:\[37m[39;49;00m$
  1313^I[37m^I[39;49;00m:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:[04m[32mk5[39;49;00m=\E[17~:[04m[32mk6[39;49;00m=\E[18~:[04m[32mk7[39;49;00m=\E[19~:[04m[32mk8[39;49;00m=\E[20~:\[37m[39;49;00m$
  1314^I[37m^I[39;49;00m:[04m[32mk9[39;49;00m=\E[21~:[04m[32mk;[39;49;00m=\E[29~:[04m[32mkD[39;49;00m=\E[3~:[04m[32mkI[39;49;00m=\E[2~:[04m[32mkN[39;49;00m=\E[6~:[04m[32mkP[39;49;00m=\E[5~:\[37m[39;49;00m$
  1315^I[37m^I[39;49;00m:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:\[37m[39;49;00m$
  1316^I[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mr3[39;49;00m=\E[?67h\E[64;1"p:\[37m[39;49;00m$
  1317^I[37m^I[39;49;00m:[04m[32mrc[39;49;00m=\E8:[04m[32mrf[39;49;00m=/usr/share/tabset/vt300:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[m:[04m[32msf[39;49;00m=\ED:\[37m[39;49;00m$
  1318^I[37m^I[39;49;00m:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:[37m[39;49;00m$
  1319^I[37m[39;49;00m$
  1320^I[37m# (vt525: I added <rmam>/<smam> based on the init string;[39;49;00m[37m[39;49;00m$
  1321^I[37m# removed :se:=\E[m, :ue:=\E[m, added :sc: -- esr)[39;49;00m[37m[39;49;00m$
  1322^I[37m# (untranslatable capabilities removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m$
  1323^I[94mvt525[39;49;00m|[36mDEC VT525[39;49;00m:\[37m[39;49;00m$
  1324^I[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m$
  1325^I[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m$
  1326^I[37m^I[39;49;00m:[04m[32m*6[39;49;00m=\E[4~:[04m[32m@0[39;49;00m=\E[1~:[04m[32mRA[39;49;00m=\E[?7l:\[37m[39;49;00m$
  1327^I[37m^I[39;49;00m:[04m[32mS5[39;49;00m=\E[?0;0r\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:\[37m[39;49;00m$
  1328^I[37m^I[39;49;00m:[04m[32mSA[39;49;00m=\E[?7h:\[37m[39;49;00m$
  1329^I[37m^I[39;49;00m:[04m[32mac[39;49;00m=``aaffggjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~:\[37m[39;49;00m$
  1330^I[37m^I[39;49;00m:[04m[32mae[39;49;00m=\E(B:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=\E(0:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:\[37m[39;49;00m$
  1331^I[37m^I[39;49;00m:[04m[32mcl[39;49;00m=\E[H\E[2J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:\[37m[39;49;00m$
  1332^I[37m^I[39;49;00m:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=\E[B:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:\[37m[39;49;00m$
  1333^I[37m^I[39;49;00m:[04m[32mi2[39;49;00m=\E[?67h\E[64;1"p:[04m[32mif[39;49;00m=/usr/share/tabset/vt300:\[37m[39;49;00m$
  1334^I[37m^I[39;49;00m:[04m[32mim[39;49;00m=\E[4h:[04m[32mis[39;49;00m=\E[1;24r\E[24;1H:[04m[32mk0[39;49;00m=\E[29~:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:\[37m[39;49;00m$
  1335^I[37m^I[39;49;00m:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:[04m[32mk5[39;49;00m=\E[17~:[04m[32mk6[39;49;00m=\E[18~:[04m[32mk7[39;49;00m=\E[19~:[04m[32mk8[39;49;00m=\E[20~:\[37m[39;49;00m$
  1336^I[37m^I[39;49;00m:[04m[32mk9[39;49;00m=\E[21~:[04m[32mk;[39;49;00m=\E[29~:[04m[32mkD[39;49;00m=\E[3~:[04m[32mkI[39;49;00m=\E[2~:[04m[32mkN[39;49;00m=\E[6~:[04m[32mkP[39;49;00m=\E[5~:\[37m[39;49;00m$
  1337^I[37m^I[39;49;00m:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:\[37m[39;49;00m$
  1338^I[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mr3[39;49;00m=\E[?67h\E[64;1"p:\[37m[39;49;00m$
  1339^I[37m^I[39;49;00m:[04m[32mrc[39;49;00m=\E8:[04m[32mrf[39;49;00m=/usr/share/tabset/vt300:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[m:[04m[32msf[39;49;00m=\ED:\[37m[39;49;00m$
  1340^I[37m^I[39;49;00m:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:$
