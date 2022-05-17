[37m######## This example from excerpt of <http://www.catb.org/esr/terminfo/>:[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m#^IVersion 11.0.1[39;49;00m[37m[39;49;00m
[37m#^I$Date: 2000/03/02 15:51:11 $[39;49;00m[37m[39;49;00m
[37m#^Itermcap syntax[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m######## ANSI, UNIX CONSOLE, AND SPECIAL TYPES[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# This section describes terminal classes and brands that are still[39;49;00m[37m[39;49;00m
[37m# quite common.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m#### Specials[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# Special "terminals".  These are used to label tty lines when you don't[39;49;00m[37m[39;49;00m
[37m# know what kind of terminal is on it.  The characteristics of an unknown[39;49;00m[37m[39;49;00m
[37m# terminal are the lowest common denominator - they look about like a ti 700.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[94mdumb[39;49;00m|[36m80-column dumb tty[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mbl[39;49;00m=^G:[04m[32mcr[39;49;00m=^M:[04m[32mdo[39;49;00m=^J:[04m[32msf[39;49;00m=^J:[37m[39;49;00m
[94munknown[39;49;00m|[36munknown terminal type[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mgn[39;49;00m:[04m[32mtc[39;49;00m=dumb:[37m[39;49;00m
[94mlpr[39;49;00m|[36mprinter[39;49;00m|[36mline printer[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mbs[39;49;00m:[04m[32mhc[39;49;00m:[04m[32mos[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m66[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mbl[39;49;00m=^G:[04m[32mcr[39;49;00m=^M:[04m[32mdo[39;49;00m=^J:[04m[32mff[39;49;00m=^L:[04m[32mle[39;49;00m=^H:[04m[32msf[39;49;00m=^J:[37m[39;49;00m
[94mglasstty[39;49;00m|[36mclassic glass tty interpreting ASCII control characters[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbs[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mbl[39;49;00m=^G:[04m[32mcl[39;49;00m=^L:[04m[32mcr[39;49;00m=^M:[04m[32mdo[39;49;00m=^J:[04m[32mkd[39;49;00m=^J:[04m[32mkl[39;49;00m=^H:[04m[32mle[39;49;00m=^H:[04m[32mnw[39;49;00m=^M^J:[04m[32mta[39;49;00m=^I:[37m[39;49;00m
[94mvanilla[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mbs[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mbl[39;49;00m=^G:[04m[32mcr[39;49;00m=^M:[04m[32mdo[39;49;00m=^J:[04m[32msf[39;49;00m=^J:[37m[39;49;00m
[37m[39;49;00m
[37m#### ANSI.SYS/ISO 6429/ECMA-48 Capabilities[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# See the end-of-file comment for more on these.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# ANSI capabilities are broken up into pieces, so that a terminal[39;49;00m[37m[39;49;00m
[37m# implementing some ANSI subset can use many of them.[39;49;00m[37m[39;49;00m
[94mansi+local1[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mdo[39;49;00m=\E[B:[04m[32mle[39;49;00m=\E[D:[04m[32mnd[39;49;00m=\E[C:[04m[32mup[39;49;00m=\E[A:[37m[39;49;00m
[94mansi+local[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mUP[39;49;00m=\E[%dA:[04m[32mtc[39;49;00m=ansi+local1:[37m[39;49;00m
[94mansi+tabs[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mbt[39;49;00m=\E[Z:[04m[32mct[39;49;00m=\E[2g:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:[37m[39;49;00m
[94mansi+inittabs[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mtc[39;49;00m=ansi+tabs:[37m[39;49;00m
[94mansi+erase[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[J:[37m[39;49;00m
[94mansi+rca[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mch[39;49;00m=\E[%+^AG:[04m[32mcv[39;49;00m=\E[%+^Ad:[37m[39;49;00m
[94mansi+cup[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mho[39;49;00m=\E[H:[37m[39;49;00m
[94mansi+rep[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m..rp[39;49;00m=%p1%c\E[%p2%{1}%-%db:[37m[39;49;00m
[94mansi+idl1[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mal[39;49;00m=\E[L:[04m[32mdl[39;49;00m=\E[M:[37m[39;49;00m
[94mansi+idl[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mtc[39;49;00m=ansi+idl1:[37m[39;49;00m
[94mansi+idc[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mIC[39;49;00m=\E[%d@:[04m[32mdc[39;49;00m=\E[P:[04m[32mei[39;49;00m=\E6:[04m[32mic[39;49;00m=\E[@:[04m[32mim[39;49;00m=\E6:[37m[39;49;00m
[94mansi+arrows[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[H:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[37m[39;49;00m
[94mansi+sgr[39;49;00m|[36mansi graphic renditions[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmb[39;49;00m=\E[5m:[04m[32mme[39;49;00m=\E[0m:[04m[32mmk[39;49;00m=\E[8m:[04m[32mmr[39;49;00m=\E[7m:[37m[39;49;00m
[94mansi+sgrso[39;49;00m|[36mansi standout only[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mse[39;49;00m=\E[m:[04m[32mso[39;49;00m=\E[7m:[37m[39;49;00m
[94mansi+sgrul[39;49;00m|[36mansi underline only[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mue[39;49;00m=\E[m:[04m[32mus[39;49;00m=\E[4m:[37m[39;49;00m
[94mansi+sgrbold[39;49;00m|[36mansi graphic renditions; assuming terminal has bold; not dim[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\E[1m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[%?%p1%t7;%;%?%p2%t4;%;%?%p3%t7;%;%?%p4%t5;%;%?%p6%t1;%;m:[04m[32mtc[39;49;00m=ansi+sgr:[04m[32mtc[39;49;00m=ansi+sgrso:[04m[32mtc[39;49;00m=ansi+sgrul:[37m[39;49;00m
[94mansi+sgrdim[39;49;00m|[36mansi graphic renditions; assuming terminal has dim; not bold[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmh[39;49;00m=\E[2m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[%?%p1%t7;%;%?%p2%t4;%;%?%p3%t7;%;%?%p4%t5;%;%?%p5%t2;%;m:[04m[32mtc[39;49;00m=ansi+sgr:[04m[32mtc[39;49;00m=ansi+sgrso:[04m[32mtc[39;49;00m=ansi+sgrul:[37m[39;49;00m
[94mansi+pp[39;49;00m|[36mansi printer port[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mpf[39;49;00m=\E[4i:[04m[32mpo[39;49;00m=\E[5i:[04m[32mps[39;49;00m=\E[0i:[37m[39;49;00m
[94mansi+csr[39;49;00m|[36mansi scroll-region plus cursor save & restore[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mrc[39;49;00m=\E8:[04m[32msc[39;49;00m=\E7:[37m[39;49;00m
[37m[39;49;00m
[37m# The IBM PC alternate character set.  Plug this into any Intel console entry.[39;49;00m[37m[39;49;00m
[37m# We use \E[11m for rmacs rather than \E[12m so the <acsc> string can use the[39;49;00m[37m[39;49;00m
[37m# ROM graphics for control characters such as the diamond, up- and down-arrow.[39;49;00m[37m[39;49;00m
[37m# This works with the System V, Linux, and BSDI consoles.  It's a safe bet this[39;49;00m[37m[39;49;00m
[37m# will work with any Intel console, they all seem to have inherited \E[11m[39;49;00m[37m[39;49;00m
[37m# from the ANSI.SYS de-facto standard.[39;49;00m[37m[39;49;00m
[94mklone+acs[39;49;00m|[36malternate character set for ansi.sys displays[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mac[39;49;00m=+\020\054\021-\030.^Y0\333`\004a\261f\370g\361h\260j\331k\277l\332m\300n\305o~p\304q\304r\304s_t\303u\264v\301w\302x\263y\363z\362{\343|\330}\234~\376:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mae[39;49;00m=\E[10m:[04m[32mas[39;49;00m=\E[11m:[37m[39;49;00m
[37m[39;49;00m
[37m# Highlight controls corresponding to the ANSI.SYS standard.  Most [39;49;00m[37m[39;49;00m
[37m# console drivers for Intel boxes obey these.  Makes the same assumption[39;49;00m[37m[39;49;00m
[37m# about \E[11m as klone+acs.  True ANSI/ECMA-48 would have :se=\E[27m:,[39;49;00m[37m[39;49;00m
[37m# :ue=\E[24m:, but this isn't a documented feature of ANSI.SYS.[39;49;00m[37m[39;49;00m
[94mklone+sgr[39;49;00m|[36mattribute control for ansi.sys displays[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mS2[39;49;00m=\E[11m:[04m[32mS3[39;49;00m=\E[10m:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[0;10m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmk[39;49;00m=\E[8m:[04m[32mmr[39;49;00m=\E[7m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[0;10%?%p1%t;7%;%?%p2%t;4%;%?%p3%t;7%;%?%p4%t;5%;%?%p6%t;1%;%?%p7%t;8%;%?%p9%t;11%;m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mse[39;49;00m=\E[m:[04m[32mso[39;49;00m=\E[7m:[04m[32mue[39;49;00m=\E[m:[04m[32mus[39;49;00m=\E[4m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=klone+acs:[37m[39;49;00m
[37m[39;49;00m
[37m# Highlight controls corresponding to the ANSI.SYS standard.  *All*[39;49;00m[37m[39;49;00m
[37m# console drivers for Intel boxes obey these.  Does not assume \E[11m will[39;49;00m[37m[39;49;00m
[37m# work; uses \E[12m instead, which is pretty bulletproof but loses you the ACS[39;49;00m[37m[39;49;00m
[37m# diamond and arrow characters under curses.[39;49;00m[37m[39;49;00m
[94mklone+sgr-dumb[39;49;00m|[36mattribute control for ansi.sys displays (no ESC [ 11 m)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mas[39;49;00m=\E[12m:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[0;10m:[04m[32mmk[39;49;00m=\E[8m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmr[39;49;00m=\E[7m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[0;10%?%p1%t;7%;%?%p2%t;4%;%?%p3%t;7%;%?%p4%t;5%;%?%p6%t;1%;%?%p7%t;8%;%?%p9%t;12%;m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mse[39;49;00m=\E[m:[04m[32mso[39;49;00m=\E[7m:[04m[32mue[39;49;00m=\E[m:[04m[32mus[39;49;00m=\E[4m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=klone+acs:[37m[39;49;00m
[37m[39;49;00m
[37m# KOI8-R (RFC1489) acs (alternate character set)[39;49;00m[37m[39;49;00m
[37m# From: Qing Long <qinglong@Bolizm.ihep.su>, 24 Feb 1996.[39;49;00m[37m[39;49;00m
[94mklone+koi8acs[39;49;00m|[36malternate character set for ansi.sys displays with KOI8 charset[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mac[39;49;00m=+\020\054\021-\036.^_0\215`\004a\237f\234g\232h\222i\220j\205k\203l\202m\204n\212o\213p\216q\0r\217s\214t\206u\207v\210w\211x\201y\230z\231{\267|\274}L~\225:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mae[39;49;00m=\E[10m:[04m[32mas[39;49;00m=\E[11m:[37m[39;49;00m
[37m[39;49;00m
[37m# ANSI.SYS color control.  The setab/setaf caps depend on the coincidence[39;49;00m[37m[39;49;00m
[37m# between SVr4/XPG4's color numbers and ANSI.SYS attributes.  Here are longer[39;49;00m[37m[39;49;00m
[37m# but equivalent strings that don't rely on that coincidence:[39;49;00m[37m[39;49;00m
[37m# setb=\E[4%?%p1%{1}%=%t4%e%p1%{3}%=%t6%e%p1%{4}%=%t1%e%p1%{6}%=%t3%e%p1%d%;m,[39;49;00m[37m[39;49;00m
[37m# setf=\E[3%?%p1%{1}%=%t4%e%p1%{3}%=%t6%e%p1%{4}%=%t1%e%p1%{6}%=%t3%e%p1%d%;m,[39;49;00m[37m[39;49;00m
[37m# The DOS 5 manual asserts that these sequences meet the ISO 6429 standard.[39;49;00m[37m[39;49;00m
[37m# They match a subset of ECMA-48.[39;49;00m[37m[39;49;00m
[94mklone+color[39;49;00m|[36mcolor control for ansi.sys and ISO6429-compatible displays[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mCo[39;49;00m#[34m8[39;49;00m:[04m[32mNC[39;49;00m#[34m3[39;49;00m:[04m[32mpa[39;49;00m#[34m64[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAB[39;49;00m=\E[4%p1%dm:[04m[32mAF[39;49;00m=\E[3%p1%dm:[04m[32mop[39;49;00m=\E[37;40m:[37m[39;49;00m
[37m[39;49;00m
[37m# This is better than klone+color, it doesn't assume white-on-black as the[39;49;00m[37m[39;49;00m
[37m# default color pair,  but many `ANSI' terminals don't grok the <op> cap.[39;49;00m[37m[39;49;00m
[94mecma+color[39;49;00m|[36mcolor control for ECMA-48-compatible terminals[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mCo[39;49;00m#[34m8[39;49;00m:[04m[32mNC[39;49;00m#[34m3[39;49;00m:[04m[32mpa[39;49;00m#[34m64[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAB[39;49;00m=\E[4%p1%dm:[04m[32mAF[39;49;00m=\E[3%p1%dm:[04m[32mop[39;49;00m=\E[39;49m:[37m[39;49;00m
[37m[39;49;00m
[37m# Attribute control for ECMA-48-compatible terminals[39;49;00m[37m[39;49;00m
[94mecma+sgr[39;49;00m|[36mattribute capabilities for true ECMA-48 terminals[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mse[39;49;00m=\E[27m:[04m[32mue[39;49;00m=\E[24m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=klone+sgr:[37m[39;49;00m
[37m[39;49;00m
[37m# For comparison, here are all the capabilities implied by the Intel[39;49;00m[37m[39;49;00m
[37m# Binary Compatibility Standard (level 2) that fit within terminfo.[39;49;00m[37m[39;49;00m
[37m# For more detail on this rather pathetic standard, see the comments[39;49;00m[37m[39;49;00m
[37m# near the end of this file.[39;49;00m[37m[39;49;00m
[94mibcs2[39;49;00m|[36mIntel Binary Compatibility Standard prescriptions[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mIC[39;49;00m=\E[%d@:[04m[32mLE[39;49;00m=\E[%dD:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mRA[39;49;00m=\E[?7l:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mS1[39;49;00m=\E=%p1%dg:[04m[32mSA[39;49;00m=\E[?7h:[04m[32mSF[39;49;00m=\E[%dS:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mSR[39;49;00m=\E[%dT:[04m[32mUP[39;49;00m=\E[%dA:[04m[32mbt[39;49;00m=\E[Z:[04m[32mch[39;49;00m=\E[%i%dG:[04m[32mcl[39;49;00m=\Ec:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mct[39;49;00m=\E[g:[04m[32mcv[39;49;00m=\E[%i%dd:[04m[32mec[39;49;00m=\E[%dX:[04m[32mei[39;49;00m=:[04m[32mim[39;49;00m=:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mrc[39;49;00m=\E7:[04m[32msc[39;49;00m=\E7:[04m[32mst[39;49;00m=\EH:[37m[39;49;00m
[37m[39;49;00m
[37m#### ANSI/ECMA-48 terminals and terminal emulators[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# See near the end of this file for details on ANSI conformance.[39;49;00m[37m[39;49;00m
[37m# Don't mess with these entries!  Lots of other entries depend on them![39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# This section lists entries in a least-capable to most-capable order.[39;49;00m[37m[39;49;00m
[37m# if you're in doubt about what `ANSI' matches yours, try them in that[39;49;00m[37m[39;49;00m
[37m# order and back off from the first that breaks.[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# ansi-mr is for ANSI terminals with ONLY relative cursor addressing[39;49;00m[37m[39;49;00m
[37m# and more than one page of memory.  It uses local motions instead of[39;49;00m[37m[39;49;00m
[37m# direct cursor addressing, and makes almost no assumptions. It does[39;49;00m[37m[39;49;00m
[37m# assume auto margins, no padding and/or xon/xoff, and a 24x80 screen.[39;49;00m[37m[39;49;00m
[94mansi-mr[39;49;00m|[36mmem rel cup ansi[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mtc[39;49;00m=vanilla:[04m[32mtc[39;49;00m=ansi+erase:[04m[32mtc[39;49;00m=ansi+local1:[37m[39;49;00m
[37m[39;49;00m
[37m# ansi-mini is a bare minimum ANSI terminal. This should work on anything, but [39;49;00m[37m[39;49;00m
[37m# beware of screen size problems and memory relative cursor addressing.[39;49;00m[37m[39;49;00m
[94mansi-mini[39;49;00m|[36mminimum ansi standard terminal[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mtc[39;49;00m=vanilla:[04m[32mtc[39;49;00m=ansi+cup:[04m[32mtc[39;49;00m=ansi+erase:[37m[39;49;00m
[37m[39;49;00m
[37m# ansi-mtabs adds relative addressing and minimal tab support [39;49;00m[37m[39;49;00m
[94mansi-mtabs[39;49;00m|[36many ansi terminal with pessimistic assumptions[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mta[39;49;00m=^I:[04m[32mtc[39;49;00m=ansi+local1:[04m[32mtc[39;49;00m=ansi-mini:[37m[39;49;00m
[37m[39;49;00m
[37m# ANSI X3.64 from emory!mlhhh (Hugh Hansard) via BRL[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# The following is an entry for the full ANSI 3.64 (1977).  It lacks[39;49;00m[37m[39;49;00m
[37m# padding, but most terminals using the standard are "fast" enough[39;49;00m[37m[39;49;00m
[37m# not to require any -- even at 9600 bps.  If you encounter problems,[39;49;00m[37m[39;49;00m
[37m# try including the padding specifications.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# Note: the :as: and :ae: specifications are not implemented here, for[39;49;00m[37m[39;49;00m
[37m# the available termcap documentation does not make clear WHICH alternate[39;49;00m[37m[39;49;00m
[37m# character set to specify.  ANSI 3.64 seems to make allowances for several.[39;49;00m[37m[39;49;00m
[37m# Please make the appropriate adjustments to fit your needs -- that is[39;49;00m[37m[39;49;00m
[37m# if you will be using alternate character sets.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# There are very few terminals running the full ANSI 3.64 standard,[39;49;00m[37m[39;49;00m
[37m# so I could only test this entry on one verified terminal (Visual 102).[39;49;00m[37m[39;49;00m
[37m# I would appreciate the results on other terminals sent to me.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# Please report comments, changes, and problems to:[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# U.S. MAIL:   Hugh Hansard[39;49;00m[37m[39;49;00m
[37m#              Box: 22830[39;49;00m[37m[39;49;00m
[37m#              Emory University[39;49;00m[37m[39;49;00m
[37m#              Atlanta, GA. 30322.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# USENET {akgua,msdc,sb1,sb6,gatech}!emory!mlhhh.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# (Added vt100 :rc:,:sc: to quiet a tic warning --esr)[39;49;00m[37m[39;49;00m
[94mansi77[39;49;00m|[36mansi 3.64 standard 1977 version[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbs[39;49;00m:[04m[32mmi[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mal[39;49;00m=5*\E[L:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[;H\E[2J:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=5*\E[M:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mdo[39;49;00m=\E[B:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:[04m[32mim[39;49;00m=\E[4h:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[H:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mnd[39;49;00m=\E[C:[04m[32mnw[39;49;00m=^M\ED:[04m[32mrc[39;49;00m=\E8:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[m:[04m[32msf[39;49;00m=\ED:[04m[32mso[39;49;00m=\E[7m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32msr[39;49;00m=\EM:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:[37m[39;49;00m
[37m[39;49;00m
[37m# Procomm and some other ANSI emulations don't recognize all of the ANSI-[39;49;00m[37m[39;49;00m
[37m# standard capabilities.  This entry deletes :UP:, :RI:, :DO:, :LE:, and [39;49;00m[37m[39;49;00m
[37m# <vpa>/<hpa> capabilities, forcing curses to use repetitions of :up:, [39;49;00m[37m[39;49;00m
[37m# :nd:, :do: and :le:.  Also deleted :IC: and :ic:, as QModem up to [39;49;00m[37m[39;49;00m
[37m# 5.03 doesn't recognize these.  Finally, we delete :rp: and :sr:, which seem[39;49;00m[37m[39;49;00m
[37m# to confuse many emulators.  On the other hand, we can count on these programs[39;49;00m[37m[39;49;00m
[37m# doing :ae:/:as:/:sa:. Older versions of this entry featured [39;49;00m[37m[39;49;00m
[37m# <invis=\E[9m>, but <invis=\E[8m> now seems to be more common under[39;49;00m[37m[39;49;00m
[37m# ANSI.SYS influence.[39;49;00m[37m[39;49;00m
[37m# From: Eric S. Raymond <esr@snark.thyrsus.com> Oct 30 1995[39;49;00m[37m[39;49;00m
[94mpcansi-m[39;49;00m|[36mpcansi-mono[39;49;00m|[36mibm-pc terminal programs claiming to be ansi (mono mode)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbs[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mms[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mal[39;49;00m=\E[L:[04m[32mbl[39;49;00m=^G:[04m[32mbt[39;49;00m=\E[Z:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[J:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mct[39;49;00m=\E[2g:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=\E[B:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mho[39;49;00m=\E[H:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[H:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mle[39;49;00m=\E[D:[04m[32mnd[39;49;00m=\E[C:[04m[32msf[39;49;00m=^J:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:[04m[32mup[39;49;00m=\E[A:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=klone+sgr-dumb:[37m[39;49;00m
[94mpcansi-25-m[39;49;00m|[36mpcansi25m[39;49;00m|[36mibm-pc terminal programs with 25 lines (mono mode)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:[04m[32mtc[39;49;00m=pcansi-m:[37m[39;49;00m
[94mpcansi-33-m[39;49;00m|[36mpcansi33m[39;49;00m|[36mibm-pc terminal programs with 33 lines (mono mode)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m33[39;49;00m:[04m[32mtc[39;49;00m=pcansi-m:[37m[39;49;00m
[94mpcansi-43-m[39;49;00m|[36mansi43m[39;49;00m|[36mibm-pc terminal programs with 43 lines (mono mode)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m43[39;49;00m:[04m[32mtc[39;49;00m=pcansi-m:[37m[39;49;00m
[37m# The color versions.  All PC emulators do color...[39;49;00m[37m[39;49;00m
[94mpcansi[39;49;00m|[36mibm-pc terminal programs claiming to be ansi[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=klone+color:[04m[32mtc[39;49;00m=pcansi-m:[37m[39;49;00m
[94mpcansi-25[39;49;00m|[36mpcansi25[39;49;00m|[36mibm-pc terminal programs with 25 lines[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:[04m[32mtc[39;49;00m=pcansi:[37m[39;49;00m
[94mpcansi-33[39;49;00m|[36mpcansi33[39;49;00m|[36mibm-pc terminal programs with 33 lines[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m33[39;49;00m:[04m[32mtc[39;49;00m=pcansi:[37m[39;49;00m
[94mpcansi-43[39;49;00m|[36mpcansi43[39;49;00m|[36mibm-pc terminal programs with 43 lines[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m43[39;49;00m:[04m[32mtc[39;49;00m=pcansi:[37m[39;49;00m
[37m[39;49;00m
[37m# ansi-m -- full ANSI X3.64 with ANSI.SYS-compatible attributes, no color.[39;49;00m[37m[39;49;00m
[37m# If you want pound signs rather than dollars, replace `B' with `A'[39;49;00m[37m[39;49;00m
[37m# in the <s0ds>, <s1ds>, <s2ds>, and <s3ds> capabilities.[39;49;00m[37m[39;49;00m
[37m# From: Eric S. Raymond <esr@snark.thyrsus.com> Nov 6 1995[39;49;00m[37m[39;49;00m
[94mansi-m[39;49;00m|[36mansi-mono[39;49;00m|[36mANSI X3.64-1979 terminal with ANSI.SYS compatible attributes[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m5i[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mIC[39;49;00m=\E[%d@:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mSF[39;49;00m=\E[%dS:[04m[32mSR[39;49;00m=\E[%dT:[04m[32mUP[39;49;00m=\E[%dA:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcb[39;49;00m=\E[1K:[04m[32mch[39;49;00m=\E[%i%dG:[04m[32mct[39;49;00m=\E[2g:[04m[32mcv[39;49;00m=\E[%i%dd:[04m[32mec[39;49;00m=\E[%dX:[04m[32mei[39;49;00m=:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mim[39;49;00m=:[04m[32mkB[39;49;00m=\E[Z:[04m[32mkI[39;49;00m=\E[L:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mnw[39;49;00m=\r\E[S:[04m[32mpf[39;49;00m=\E[4i:[04m[32mpo[39;49;00m=\E[5i:[04m[32m..rp[39;49;00m=%p1%c\E[%p2%{1}%-%db:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32ms0[39;49;00m=\E(B:[04m[32ms1[39;49;00m=\E)B:[04m[32ms2[39;49;00m=\E*B:[04m[32ms3[39;49;00m=\E+B:[04m[32mta[39;49;00m=\E[I:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=pcansi-m:[37m[39;49;00m
[37m[39;49;00m
[37m# ansi -- this terminfo expresses the largest subset of X3.64 that will fit in[39;49;00m[37m[39;49;00m
[37m# standard terminfo.  Assumes ANSI.SYS-compatible attributes and color.[39;49;00m[37m[39;49;00m
[37m# From: Eric S. Raymond <esr@snark.thyrsus.com> Nov 6 1995[39;49;00m[37m[39;49;00m
[94mansi[39;49;00m|[36mansi/pc-term compatible with color[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mu6[39;49;00m=\E[%i%d;%dR:[04m[32mu7[39;49;00m=\E[6n:[04m[32m..u8[39;49;00m=\E[?%[;0123456789]c:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mu9[39;49;00m=\E[c:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=ecma+color:[04m[32mtc[39;49;00m=klone+sgr:[04m[32mtc[39;49;00m=ansi-m:[37m[39;49;00m
[37m[39;49;00m
[37m# ansi-generic is a vanilla ANSI terminal. This is assumed to implement [39;49;00m[37m[39;49;00m
[37m# all the normal ANSI stuff with no extensions. It assumes [39;49;00m[37m[39;49;00m
[37m# insert/delete line/char is there, so it won't work with [39;49;00m[37m[39;49;00m
[37m# vt100 clones. It assumes video attributes for bold, blink, [39;49;00m[37m[39;49;00m
[37m# underline, and reverse, which won't matter much if the terminal [39;49;00m[37m[39;49;00m
[37m# can't do some of those. Padding is assumed to be zero, which [39;49;00m[37m[39;49;00m
[37m# shouldn't hurt since xon/xoff is assumed.[39;49;00m[37m[39;49;00m
[94mansi-generic[39;49;00m|[36mgeneric ansi standard terminal[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mtc[39;49;00m=vanilla:[04m[32mtc[39;49;00m=ansi+csr:[04m[32mtc[39;49;00m=ansi+cup:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=ansi+rca:[04m[32mtc[39;49;00m=ansi+erase:[04m[32mtc[39;49;00m=ansi+tabs:[04m[32mtc[39;49;00m=ansi+local:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=ansi+idc:[04m[32mtc[39;49;00m=ansi+idl:[04m[32mtc[39;49;00m=ansi+rep:[04m[32mtc[39;49;00m=ansi+sgrbold:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=ansi+arrows:[37m[39;49;00m
[37m[39;49;00m
[37m#### Linux consoles[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# This entry is good for the 1.2.13 or later version of the Linux console.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# ***************************************************************************[39;49;00m[37m[39;49;00m
[37m# *                                                                         *[39;49;00m[37m[39;49;00m
[37m# *                           WARNING:                                      *[39;49;00m[37m[39;49;00m
[37m# * Linuxes come with a default keyboard mapping kcbt=^I.  This entry, in   *[39;49;00m[37m[39;49;00m
[37m# * response to user requests, assumes kcbt=\E[Z, the ANSI/ECMA reverse-tab *[39;49;00m[37m[39;49;00m
[37m# * character. Here are the keymap replacement lines that will set this up: *[39;49;00m[37m[39;49;00m
[37m# *                                                                         *[39;49;00m[37m[39;49;00m
[37m#^Ikeycode  15 = Tab             Tab[39;49;00m[37m[39;49;00m
[37m#^I^Ialt     keycode  15 = Meta_Tab[39;49;00m[37m[39;49;00m
[37m#^I^Ishift^Ikeycode  15 = F26[39;49;00m[37m[39;49;00m
[37m#^Istring F26 ="\033[Z"[39;49;00m[37m[39;49;00m
[37m# *                                                                         *[39;49;00m[37m[39;49;00m
[37m# * This has to use a key slot which is unfortunate (any unused one will    *[39;49;00m[37m[39;49;00m
[37m# * do, F26 is the higher-numbered one).  The change ought to be built      *[39;49;00m[37m[39;49;00m
[37m# * into the kernel tables.                                                 *[39;49;00m[37m[39;49;00m
[37m# *                                                                         *[39;49;00m[37m[39;49;00m
[37m# ***************************************************************************[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# The 1.3.x kernels add color-change capabilities; if yours doesn't have this[39;49;00m[37m[39;49;00m
[37m# and it matters, turn off <ccc>.  The %02x escape used to implement this is[39;49;00m[37m[39;49;00m
[37m# not back-portable to SV curses and not supported in ncurses versions before[39;49;00m[37m[39;49;00m
[37m# 1.9.9. All linux kernels since 1.2.13 (at least) set the screen size[39;49;00m[37m[39;49;00m
[37m# themselves; this entry assumes that capability.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# This entry is good for the 1.2.13 or later version of the Linux console.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# ***************************************************************************[39;49;00m[37m[39;49;00m
[37m# *                                                                         *[39;49;00m[37m[39;49;00m
[37m# *                           WARNING:                                      *[39;49;00m[37m[39;49;00m
[37m# * Linuxes come with a default keyboard mapping kcbt=^I.  This entry, in   *[39;49;00m[37m[39;49;00m
[37m# * response to user requests, assumes kcbt=\E[Z, the ANSI/ECMA reverse-tab *[39;49;00m[37m[39;49;00m
[37m# * character. Here are the keymap replacement lines that will set this up: *[39;49;00m[37m[39;49;00m
[37m# *                                                                         *[39;49;00m[37m[39;49;00m
[37m#^Ikeycode  15 = Tab             Tab[39;49;00m[37m[39;49;00m
[37m#^I^Ialt     keycode  15 = Meta_Tab[39;49;00m[37m[39;49;00m
[37m#^I^Ishift^Ikeycode  15 = F26[39;49;00m[37m[39;49;00m
[37m#^Istring F26 ="\033[Z"[39;49;00m[37m[39;49;00m
[37m# *                                                                         *[39;49;00m[37m[39;49;00m
[37m# * This has to use a key slot which is unfortunate (any unused one will    *[39;49;00m[37m[39;49;00m
[37m# * do, F26 is the higher-numbered one).  The change ought to be built      *[39;49;00m[37m[39;49;00m
[37m# * into the kernel tables.                                                 *[39;49;00m[37m[39;49;00m
[37m# *                                                                         *[39;49;00m[37m[39;49;00m
[37m# ***************************************************************************[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# The 1.3.x kernels add color-change capabilities; if yours doesn't have this[39;49;00m[37m[39;49;00m
[37m# and it matters, turn off <ccc>.  The %02x escape used to implement this is[39;49;00m[37m[39;49;00m
[37m# not back-portable to SV curses and not supported in ncurses versions before[39;49;00m[37m[39;49;00m
[37m# 1.9.9. All linux kernels since 1.2.13 (at least) set the screen size[39;49;00m[37m[39;49;00m
[37m# themselves; this entry assumes that capability.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# The 2.2.x kernels add a private mode that sets the cursor type; use that to[39;49;00m[37m[39;49;00m
[37m# get a block cursor for cvvis.[39;49;00m[37m[39;49;00m
[37m# reported by Frank Heckenbach <frank@g-n-u.de>.[39;49;00m[37m[39;49;00m
[37m# (untranslatable capabilities removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m
[37m# (sgr removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m
[37m# (terminfo-only capabilities suppressed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m
[94mlinux[39;49;00m|[36mlinux console[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32meo[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mms[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mIC[39;49;00m=\E[%d@:[04m[32mK2[39;49;00m=\E[G:[04m[32mal[39;49;00m=\E[L:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mct[39;49;00m=\E[3g:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=^J:[04m[32mec[39;49;00m=\E[%dX:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:[04m[32mic[39;49;00m=\E[@:[04m[32mim[39;49;00m=\E[4h:[04m[32mk1[39;49;00m=\E[[A:[04m[32mk2[39;49;00m=\E[[B:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk3[39;49;00m=\E[[C:[04m[32mk4[39;49;00m=\E[[D:[04m[32mk5[39;49;00m=\E[[E:[04m[32mk6[39;49;00m=\E[17~:[04m[32mk7[39;49;00m=\E[18~:[04m[32mk8[39;49;00m=\E[19~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk9[39;49;00m=\E[20~:[04m[32mkD[39;49;00m=\E[3~:[04m[32mkI[39;49;00m=\E[2~:[04m[32mkN[39;49;00m=\E[6~:[04m[32mkP[39;49;00m=\E[5~:[04m[32mkb[39;49;00m=\177:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[1~:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mmh[39;49;00m=\E[2m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mnw[39;49;00m=^M^J:[04m[32mrc[39;49;00m=\E8:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[27m:[04m[32msf[39;49;00m=^J:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32msr[39;49;00m=\EM:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[24m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mvb[39;49;00m=200\E[?5h\E[?5l:[04m[32mve[39;49;00m=\E[?25h\E[?0c:[04m[32mvi[39;49;00m=\E[?25l\E[?1c:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mvs[39;49;00m=\E[?25h\E[?8c:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=klone+sgr:[04m[32mtc[39;49;00m=ecma+color:[37m[39;49;00m
[94mlinux-m[39;49;00m|[36mLinux console no color[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mCo@[39;49;00m:[04m[32mpa@[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAB@[39;49;00m:[04m[32mAF@[39;49;00m:[04m[32mSb@[39;49;00m:[04m[32mSf@[39;49;00m:[04m[32mtc[39;49;00m=linux:[37m[39;49;00m
[94mlinux-c-nc[39;49;00m|[36mlinux console 1.3.x hack for ncurses only[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcc[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m..Ic[39;49;00m=\E]P%p1%x%p2%{255}%*%{1000}%/%02x%p3%{255}%*%{1000}%/%02x%p4%{255}%*%{1000}%/%02x:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32moc[39;49;00m=\E]R:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=linux:[37m[39;49;00m
[37m# From: Dennis Henriksen <opus@osrl.dk>, 9 July 1996[39;49;00m[37m[39;49;00m
[94mlinux-c[39;49;00m|[36mlinux console 1.3.6+ with private palette for each virtual console[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcc[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mCo[39;49;00m#[34m8[39;49;00m:[04m[32mpa[39;49;00m#[34m64[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m..Ic[39;49;00m=\E]P%?%p1%{9}%>%t%p1%{10}%-%'a'%+%c%e%p1%d%;%p2%{255}%&%Pr%gr%{16}%/%Px%?%gx%{9}%>%t%gx%{10}%-%'A'%+%c%e%gx%d%;%gr%{15}%&%Px%?%gx%{9}%>%t%gx%{10}%-%'A'%+%c%e%gx%d%;%p3%{255}%&%Pr%gr%{16}%/%Px%?%gx%{9}%>%t%gx%{10}%-%'A'%+%c%e%gx%d%;%gr%{15}%&%Px%?%gx%{9}%>%t%gx%{10}%-%'A'%+%c%e%gx%d%;%p4%{255}%&%Pr%gr%{16}%/%Px%?%gx%{9}%>%t%gx%{10}%-%'A'%+%c%e%gx%d%;%gr%{15}%&%Px%?%gx%{9}%>%t%gx%{10}%-%'A'%+%c%e%gx%d%;:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32moc[39;49;00m=\E]R:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=linux:[37m[39;49;00m
[37m[39;49;00m
[37m# See the note on ICH/ICH1 VERSUS RMIR/SMIR near the end of file[39;49;00m[37m[39;49;00m
[94mlinux-nic[39;49;00m|[36mlinux with ich/ich1 suppressed for non-curses programs[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mIC@[39;49;00m:[04m[32mei[39;49;00m=:[04m[32mic@[39;49;00m:[04m[32mim[39;49;00m=:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=linux:[37m[39;49;00m
[37m[39;49;00m
[37m# This assumes you have used setfont(8) to load one of the Linux koi8-r fonts.[39;49;00m[37m[39;49;00m
[37m# acsc entry from Pavel Roskin" <pavel@absolute.spb.su>, 29 Sep 1997.[39;49;00m[37m[39;49;00m
[94mlinux-koi8[39;49;00m|[36mlinux with koi8 alternate character set[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mac[39;49;00m=+\020\054\021-\030.^Y0\215`\004a\221f\234g\237h\220i\276j\205k\203l\202m\204n\212o~p\0q\0r\0s_t\206u\207v\211w\210x\201y\230z\231{\267|\274~\224:[04m[32mtc[39;49;00m=linux:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=klone+koi8acs:[37m[39;49;00m
[37m[39;49;00m
[37m# Another entry for KOI8-r with Qing Long's acsc.[39;49;00m[37m[39;49;00m
[37m# (which one better complies with the standard?)[39;49;00m[37m[39;49;00m
[94mlinux-koi8r[39;49;00m|[36mlinux with koi8-r alternate character set[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=linux:[04m[32mtc[39;49;00m=klone+koi8acs:[37m[39;49;00m
[37m[39;49;00m
[37m# Entry for the latin1 and latin2 fonts[39;49;00m[37m[39;49;00m
[94mlinux-lat[39;49;00m|[36mlinux with latin1 or latin2 alternate character set[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mac[39;49;00m=+\020\054\021-\030.^Y0\333`\004a\013f\370g\361h\260i\316j\211k\214l\206m\203n\305o~p\304q\212r\304s_t\207u\215v\301w\302x\205y\363z\362{\343|\330}\234~\376:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=linux:[37m[39;49;00m
[37m[39;49;00m
[37m#### NetBSD consoles[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# pcvt termcap database entries (corresponding to release 3.31)[39;49;00m[37m[39;49;00m
[37m# Author's last edit-date: [Fri Sep 15 20:29:10 1995][39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# (For the terminfo master file, I translated these into terminfo syntax.[39;49;00m[37m[39;49;00m
[37m# Then I dropped all the pseudo-HP entries. we don't want and can't use[39;49;00m[37m[39;49;00m
[37m# the :Xs: flag. Then I split :is: into a size-independent :i1: and a[39;49;00m[37m[39;49;00m
[37m# size-dependent :is:.  Finally, I added <rmam>/<smam> -- esr)[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# NOTE: :ic: has been taken out of this entry. for reference, it should[39;49;00m[37m[39;49;00m
[37m# be <ich1=\E[@>.  For discussion, see ICH/ICH1 VERSUS RMIR/SMIR below.[39;49;00m[37m[39;49;00m
[37m# (esr: added :vi: and :ve: to resolve NetBSD Problem Report #4583)[39;49;00m[37m[39;49;00m
[94mpcvtXX[39;49;00m|[36mpcvt vt200 emulator (DEC VT220)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mkm[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mms[39;49;00m:[04m[32mxn[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mIC[39;49;00m=\E[%d@:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRA[39;49;00m=\E[?7l:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mSA[39;49;00m=\E[?7h:[04m[32mSF[39;49;00m=\E[%dS:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mSR[39;49;00m=\E[%dT:[04m[32mUP[39;49;00m=\E[%dA:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mac[39;49;00m=++\054\054--..00``aaffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz~~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mae[39;49;00m=\E(B:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=\E(0:[04m[32mbl[39;49;00m=^G:[04m[32mcb[39;49;00m=\E[1K:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcl[39;49;00m=\E[H\E[J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mct[39;49;00m=\E[3g:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=\E[B:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mi1[39;49;00m=\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:[04m[32mim[39;49;00m=\E[4h:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk1[39;49;00m=\E[17~:[04m[32mk2[39;49;00m=\E[18~:[04m[32mk3[39;49;00m=\E[19~:[04m[32mk4[39;49;00m=\E[20~:[04m[32mk5[39;49;00m=\E[21~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk6[39;49;00m=\E[23~:[04m[32mk7[39;49;00m=\E[24~:[04m[32mk8[39;49;00m=\E[25~:[04m[32mkD[39;49;00m=\E[3~:[04m[32mkH[39;49;00m=\E[4~:[04m[32mkI[39;49;00m=\E[2~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkN[39;49;00m=\E[6~:[04m[32mkP[39;49;00m=\E[5~:[04m[32mkb[39;49;00m=\177:[04m[32mkd[39;49;00m=\EOB:[04m[32mke[39;49;00m=\E[?1l\E>:[04m[32mkh[39;49;00m=\E[1~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkl[39;49;00m=\EOD:[04m[32mkr[39;49;00m=\EOC:[04m[32mks[39;49;00m=\E[?1h\E=:[04m[32mku[39;49;00m=\EOA:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mnw[39;49;00m=\EE:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mr1[39;49;00m=\Ec\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:[04m[32mrc[39;49;00m=\E8:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mrf[39;49;00m=/usr/share/tabset/vt100:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[27m:[04m[32msf[39;49;00m=\ED:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[24m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mve[39;49;00m=\E[?25h:[04m[32mvi[39;49;00m=\E[?25l:[37m[39;49;00m
[37m[39;49;00m
[37m#^INetBSD/FreeBSD vt220 terminal emulator console (pc keyboard & monitor)[39;49;00m[37m[39;49;00m
[37m#^Itermcap entries for pure VT220-Emulation and 25, 28, 35, 40, 43 and[39;49;00m[37m[39;49;00m
[37m#^I50 lines entries; 80 columns[39;49;00m[37m[39;49;00m
[94mpcvt25[39;49;00m|[36mdec vt220 emulation with 25 lines[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;25r\E[25;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m
[94mpcvt28[39;49;00m|[36mdec vt220 emulation with 28 lines[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m28[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;28r\E[28;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m
[94mpcvt35[39;49;00m|[36mdec vt220 emulation with 35 lines[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m35[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;35r\E[35;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m
[94mpcvt40[39;49;00m|[36mdec vt220 emulation with 40 lines[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m40[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;40r\E[40;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m
[94mpcvt43[39;49;00m|[36mdec vt220 emulation with 43 lines[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m43[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;43r\E[43;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m
[94mpcvt50[39;49;00m|[36mdec vt220 emulation with 50 lines[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;50r\E[50;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m
[37m[39;49;00m
[37m#^INetBSD/FreeBSD vt220 terminal emulator console (pc keyboard & monitor)[39;49;00m[37m[39;49;00m
[37m#^Itermcap entries for pure VT220-Emulation and 25, 28, 35, 40, 43 and[39;49;00m[37m[39;49;00m
[37m#^I50 lines entries; 132 columns[39;49;00m[37m[39;49;00m
[94mpcvt25w[39;49;00m|[36mdec vt220 emulation with 25 lines and 132 cols[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;25r\E[25;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m
[94mpcvt28w[39;49;00m|[36mdec vt220 emulation with 28 lines and 132 cols[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m28[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;28r\E[28;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m
[94mpcvt35w[39;49;00m|[36mdec vt220 emulation with 35 lines and 132 cols[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m35[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;35r\E[35;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m
[94mpcvt40w[39;49;00m|[36mdec vt220 emulation with 40 lines and 132 cols[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m40[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;40r\E[40;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m
[94mpcvt43w[39;49;00m|[36mdec vt220 emulation with 43 lines and 132 cols[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m43[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;43r\E[43;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m
[94mpcvt50w[39;49;00m|[36mdec vt220 emulation with 50 lines and 132 cols[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;50r\E[50;1H:[04m[32mtc[39;49;00m=pcvtXX:[37m[39;49;00m
[37m[39;49;00m
[37m# Terminfo entries to enable the use of the ncurses library in colour on a[39;49;00m[37m[39;49;00m
[37m# NetBSD-arm32 console (only tested on a RiscPC).[39;49;00m[37m[39;49;00m
[37m# Created by Dave Millen <dmill@globalnet.co.uk> 22.07.98[39;49;00m[37m[39;49;00m
[37m# modified codes for setf/setb to setaf/setab, then to klone+color, corrected[39;49;00m[37m[39;49;00m
[37m# typo in invis - TD[39;49;00m[37m[39;49;00m
[94marm100[39;49;00m|[36marm100-am[39;49;00m|[36mArm(RiscPC) ncurses compatible (for 640x480)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mms[39;49;00m:[04m[32mut[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m30[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m@8[39;49;00m=\E[M:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mK1[39;49;00m=\E[q:[04m[32mK2[39;49;00m=\E[r:[04m[32mK3[39;49;00m=\E[s:[04m[32mK4[39;49;00m=\E[p:[04m[32mK5[39;49;00m=\E[n:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRA[39;49;00m=\E[?7l:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mSA[39;49;00m=\E[?7h:[04m[32mUP[39;49;00m=\E[%dA:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mac[39;49;00m=``aaffggjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mae[39;49;00m=^O:[04m[32mas[39;49;00m=^N:[04m[32mbl[39;49;00m=^G:[04m[32mcb[39;49;00m=\E[1K:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[J:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mct[39;49;00m=\E[3g:[04m[32mdo[39;49;00m=^J:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32meA[39;49;00m=\E(B\E)0:[04m[32mho[39;49;00m=\E[H:[04m[32mk0[39;49;00m=\E[y:[04m[32mk1[39;49;00m=\E[P:[04m[32mk2[39;49;00m=\E[Q:[04m[32mk3[39;49;00m=\E[R:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk4[39;49;00m=\E[S:[04m[32mk5[39;49;00m=\E[t:[04m[32mk6[39;49;00m=\E[u:[04m[32mk7[39;49;00m=\E[v:[04m[32mk8[39;49;00m=\E[l:[04m[32mk9[39;49;00m=\E[w:[04m[32mk;[39;49;00m=\E[x:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mke[39;49;00m=\E[?1l\E>:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mks[39;49;00m=\E[?1h\E=:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m\017:[04m[32mmk[39;49;00m=\E[8m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmr[39;49;00m=\E[6m:[04m[32mnd[39;49;00m=\E[C:[04m[32mr2[39;49;00m=\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mrc[39;49;00m=\E8:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[0%?%p1%p6%|%t;1%;%?%p2%t;4%;%?%p1%p3%|%t;7%;%?%p4%t;5%;m%?%p9%t\016%e\017%;:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[m:[04m[32msf[39;49;00m=^J:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=ecma+sgr:[04m[32mtc[39;49;00m=klone+color:[37m[39;49;00m
[94marm100-w[39;49;00m|[36marm100-wam[39;49;00m|[36mArm(RiscPC) ncurses compatible (for 1024x768)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:[04m[32mtc[39;49;00m=arm100:[37m[39;49;00m
[37m[39;49;00m
[37m# NetBSD/x68k console vt200 emulator. This port runs on a 68K machine[39;49;00m[37m[39;49;00m
[37m# manufactured by Sharp for the Japenese market.[39;49;00m[37m[39;49;00m
[37m# From Minoura Makoto <minoura@netlaputa.or.jp>, 12 May 1996[39;49;00m[37m[39;49;00m
[94mx68k[39;49;00m|[36mx68k-ite[39;49;00m|[36mNetBSD/x68k ITE[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m96[39;49;00m:[04m[32mli[39;49;00m#[34m32[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m%1[39;49;00m=\E[28~:[04m[32mkC[39;49;00m=\E[9~:[04m[32mtc[39;49;00m=vt220:[37m[39;49;00m
[37m[39;49;00m
[37m# <tv@pobox.com>:[39;49;00m[37m[39;49;00m
[37m# Entry for the DNARD OpenFirmware console, close to ANSI but not quite.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# (still unfinished, but good enough so far.)[39;49;00m[37m[39;49;00m
[94mofcons[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mbw[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m30[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\233%dL:[04m[32mDC[39;49;00m=\233%dP:[04m[32mDL[39;49;00m=\233%dM:[04m[32mDO[39;49;00m=\233%dB:[04m[32mIC[39;49;00m=\233%d@:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\233%dD:[04m[32mRI[39;49;00m=\233%dC:[04m[32mUP[39;49;00m=\233%dA:[04m[32mal[39;49;00m=\233L:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\233J:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mce[39;49;00m=\233K:[04m[32mcl[39;49;00m=^L:[04m[32mcm[39;49;00m=\233%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mdc[39;49;00m=\233P:[04m[32mdl[39;49;00m=\233M:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mdo[39;49;00m=\233B:[04m[32mei[39;49;00m=:[04m[32mic[39;49;00m=\233@:[04m[32mim[39;49;00m=:[04m[32mk1[39;49;00m=\2330P:[04m[32mk2[39;49;00m=\2330Q:[04m[32mk3[39;49;00m=\2330W:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk4[39;49;00m=\2330x:[04m[32mk5[39;49;00m=\2330t:[04m[32mk6[39;49;00m=\2330u:[04m[32mk7[39;49;00m=\2330q:[04m[32mk8[39;49;00m=\2330r:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk9[39;49;00m=\2330p:[04m[32mk;[39;49;00m=\2330M:[04m[32mkD[39;49;00m=\233P:[04m[32mkN[39;49;00m=\233/:[04m[32mkP[39;49;00m=\233?:[04m[32mkb[39;49;00m=^H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkd[39;49;00m=\233B:[04m[32mkl[39;49;00m=\233D:[04m[32mkr[39;49;00m=\233C:[04m[32mku[39;49;00m=\233A:[04m[32mle[39;49;00m=\233D:[04m[32mmb[39;49;00m=\2337;2m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\2331m:[04m[32mme[39;49;00m=\2330m:[04m[32mmh[39;49;00m=\2332m:[04m[32mmk[39;49;00m=\2338m:[04m[32mmr[39;49;00m=\2337m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mnd[39;49;00m=\233C:[04m[32mnw[39;49;00m=^M^J:[04m[32mse[39;49;00m=\2330m:[04m[32msf[39;49;00m=^J:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\2330m:[04m[32mup[39;49;00m=\233A:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mvb[39;49;00m=^G:[37m[39;49;00m
[37m[39;49;00m
[37m# NetBSD "wscons" emulator in vt220 mode[39;49;00m[37m[39;49;00m
[37m# These are micro-minimal and probably need to be redone for real[39;49;00m[37m[39;49;00m
[37m# after the manner of the pcvt entries.[39;49;00m[37m[39;49;00m
[94mwsvt25[39;49;00m|[36mNetBSD wscons in 25 line DEC VT220 mode[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:[04m[32mtc[39;49;00m=vt220:[37m[39;49;00m
[37m[39;49;00m
[94mwsvt25m[39;49;00m|[36mNetBSD wscons in 25 line DEC VT220 mode with Meta[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkm[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:[04m[32mtc[39;49;00m=vt220:[37m[39;49;00m
[37m[39;49;00m
[37m# `rasterconsole' provided by 4.4BSD, NetBSD and OpenBSD on SPARC, and [39;49;00m[37m[39;49;00m
[37m# DECstation/pmax.[39;49;00m[37m[39;49;00m
[94mrcons[39;49;00m|[36mBSD rasterconsole[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=sun-il:[37m[39;49;00m
[37m# Color version of above. Color currenly only provided by NetBSD.[39;49;00m[37m[39;49;00m
[94mrcons-color[39;49;00m|[36mBSD rasterconsole with ANSI color[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mut[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mCo[39;49;00m#[34m8[39;49;00m:[04m[32mpa[39;49;00m#[34m64[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAB[39;49;00m=\E[4%dm:[04m[32mAF[39;49;00m=\E[3%dm:[04m[32mop[39;49;00m=\E[m:[04m[32mtc[39;49;00m=rcons:[37m[39;49;00m
[37m[39;49;00m
[37m#### FreeBSD console entries[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# From: Andrey Chernov <ache@astral.msk.su> 29 Mar 1996[39;49;00m[37m[39;49;00m
[37m# Andrey Chernov maintains the FreeBSD termcap distributions.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# Note: Users of FreeBSD 2.1.0 and older versions must either upgrade[39;49;00m[37m[39;49;00m
[37m# or comment out the :cb: capability in the console entry.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# Alexander Lukyanov reports:[39;49;00m[37m[39;49;00m
[37m# I have seen FreeBSD-2.1.5R... The old el1 bug changed, but it is still there.[39;49;00m[37m[39;49;00m
[37m# Now el1 clears not only to the line beginning, but also a large chunk[39;49;00m[37m[39;49;00m
[37m# of previous line. But there is another bug - ech does not work at all.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# for syscons[39;49;00m[37m[39;49;00m
[37m# common entry without semigraphics[39;49;00m[37m[39;49;00m
[37m# Bug: The <op> capability resets attributes.[39;49;00m[37m[39;49;00m
[37m# Bug? The ech and el1 attributes appear to move the cursor in some cases; for[39;49;00m[37m[39;49;00m
[37m# instance el1 does if the cursor is moved to the right margin first.  Removed[39;49;00m[37m[39;49;00m
[37m# by T.Dickey 97/5/3 (ech=\E[%p1%dX, el1=\E[1K)[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# Setting colors turns off reverse; we cannot guarantee order, so use ncv.[39;49;00m[37m[39;49;00m
[37m# Note that this disables standout with color.[39;49;00m[37m[39;49;00m
[94mcons25w[39;49;00m|[36mansiw[39;49;00m|[36mansi80x25-raw[39;49;00m|[36mfreebsd console (25-line raw mode)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mNP[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbw[39;49;00m:[04m[32meo[39;49;00m:[04m[32mms[39;49;00m:[04m[32mut[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mCo[39;49;00m#[34m8[39;49;00m:[04m[32mNC[39;49;00m#[34m21[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:[04m[32mpa[39;49;00m#[34m64[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m@7[39;49;00m=\E[F:[04m[32mAB[39;49;00m=\E[4%p1%dm:[04m[32mAF[39;49;00m=\E[3%p1%dm:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mF1[39;49;00m=\E[W:[04m[32mF2[39;49;00m=\E[X:[04m[32mIC[39;49;00m=\E[%d@:[04m[32mK2[39;49;00m=\E[E:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mSF[39;49;00m=\E[%dS:[04m[32mSR[39;49;00m=\E[%dT:[04m[32mUP[39;49;00m=\E[%dA:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mal[39;49;00m=\E[L:[04m[32mbl[39;49;00m=^G:[04m[32mbt[39;49;00m=\E[Z:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mch[39;49;00m=\E[%i%d`:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcl[39;49;00m=\E[H\E[J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcv[39;49;00m=\E[%i%dd:[04m[32mdc[39;49;00m=\E[P:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=\E[B:[04m[32mei[39;49;00m=:[04m[32mho[39;49;00m=\E[H:[04m[32mic[39;49;00m=\E[@:[04m[32mim[39;49;00m=:[04m[32mk1[39;49;00m=\E[M:[04m[32mk2[39;49;00m=\E[N:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk3[39;49;00m=\E[O:[04m[32mk4[39;49;00m=\E[P:[04m[32mk5[39;49;00m=\E[Q:[04m[32mk6[39;49;00m=\E[R:[04m[32mk7[39;49;00m=\E[S:[04m[32mk8[39;49;00m=\E[T:[04m[32mk9[39;49;00m=\E[U:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk;[39;49;00m=\E[V:[04m[32mkB[39;49;00m=\E[Z:[04m[32mkD[39;49;00m=\177:[04m[32mkI[39;49;00m=\E[L:[04m[32mkN[39;49;00m=\E[G:[04m[32mkP[39;49;00m=\E[I:[04m[32mkb[39;49;00m=^H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[H:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:[04m[32mmh[39;49;00m=\E[30;1m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mnw[39;49;00m=\E[E:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mop[39;49;00m=\E[x:[04m[32mr1[39;49;00m=\E[x\E[m\Ec:[04m[32mse[39;49;00m=\E[m:[04m[32msf[39;49;00m=\E[S:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\E[T:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mta[39;49;00m=^I:[04m[32mup[39;49;00m=\E[A:[04m[32mve[39;49;00m=\E[=0C:[04m[32mvs[39;49;00m=\E[=1C:[37m[39;49;00m
[94mcons25[39;49;00m|[36mansis[39;49;00m|[36mansi80x25[39;49;00m|[36mfreebsd console (25-line ansi mode)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mac[39;49;00m=-\030.^Y0\333`\004a\260f\370g\361h\261i\025j\331k\277l\332m\300n\305q\304t\303u\264v\301w\302x\263y\363z\362~\371:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=cons25w:[37m[39;49;00m
[94mcons25-m[39;49;00m|[36mansis-mono[39;49;00m|[36mansi80x25-mono[39;49;00m|[36mfreebsd console (25-line mono ansi mode)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mCo@[39;49;00m:[04m[32mpa@[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAB@[39;49;00m:[04m[32mAF@[39;49;00m:[04m[32mmd@[39;49;00m:[04m[32mmh@[39;49;00m:[04m[32mop@[39;49;00m:[04m[32mue[39;49;00m=\E[m:[04m[32mus[39;49;00m=\E[4m:[04m[32mtc[39;49;00m=cons25:[37m[39;49;00m
[94mcons30[39;49;00m|[36mansi80x30[39;49;00m|[36mfreebsd console (30-line ansi mode)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m30[39;49;00m:[04m[32mtc[39;49;00m=cons25:[37m[39;49;00m
[94mcons30-m[39;49;00m|[36mansi80x30-mono[39;49;00m|[36mfreebsd console (30-line mono ansi mode)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m30[39;49;00m:[04m[32mtc[39;49;00m=cons25-m:[37m[39;49;00m
[94mcons43[39;49;00m|[36mansi80x43[39;49;00m|[36mfreebsd console (43-line ansi mode)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m43[39;49;00m:[04m[32mtc[39;49;00m=cons25:[37m[39;49;00m
[94mcons43-m[39;49;00m|[36mansi80x43-mono[39;49;00m|[36mfreebsd console (43-line mono ansi mode)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m43[39;49;00m:[04m[32mtc[39;49;00m=cons25-m:[37m[39;49;00m
[94mcons50[39;49;00m|[36mansil[39;49;00m|[36mansi80x50[39;49;00m|[36mfreebsd console (50-line ansi mode)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:[04m[32mtc[39;49;00m=cons25:[37m[39;49;00m
[94mcons50-m[39;49;00m|[36mansil-mono[39;49;00m|[36mansi80x50-mono[39;49;00m|[36mfreebsd console (50-line mono ansi mode)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:[04m[32mtc[39;49;00m=cons25-m:[37m[39;49;00m
[94mcons60[39;49;00m|[36mansi80x60[39;49;00m|[36mfreebsd console (60-line ansi mode)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m60[39;49;00m:[04m[32mtc[39;49;00m=cons25:[37m[39;49;00m
[94mcons60-m[39;49;00m|[36mansi80x60-mono[39;49;00m|[36mfreebsd console (60-line mono ansi mode)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m60[39;49;00m:[04m[32mtc[39;49;00m=cons25-m:[37m[39;49;00m
[94mcons25r[39;49;00m|[36mpc3r[39;49;00m|[36mibmpc3r[39;49;00m|[36mcons25-koi8-r[39;49;00m|[36mfreebsd console w/koi8-r cyrillic[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mac[39;49;00m=-\030.^Y0\215`\004a\220f\234h\221i\025j\205k\203l\202m\204n\212q\0t\206u\207v\211w\210x\201y\230z\231~\225:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=cons25w:[37m[39;49;00m
[94mcons25r-m[39;49;00m|[36mpc3r-m[39;49;00m|[36mibmpc3r-mono[39;49;00m|[36mcons25-koi8r-m[39;49;00m|[36mfreebsd console w/koi8-r cyrillic (mono)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mCo@[39;49;00m:[04m[32mpa@[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAB@[39;49;00m:[04m[32mAF@[39;49;00m:[04m[32mop@[39;49;00m:[04m[32mue[39;49;00m=\E[m:[04m[32mus[39;49;00m=\E[4m:[04m[32mtc[39;49;00m=cons25r:[37m[39;49;00m
[94mcons50r[39;49;00m|[36mcons50-koi8r[39;49;00m|[36mfreebsd console w/koi8-r cyrillic (50 lines)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:[04m[32mtc[39;49;00m=cons25r:[37m[39;49;00m
[94mcons50r-m[39;49;00m|[36mcons50-koi8r-m[39;49;00m|[36mfreebsd console w/koi8-r cyrillic (50-line mono)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:[04m[32mtc[39;49;00m=cons25r-m:[37m[39;49;00m
[94mcons60r[39;49;00m|[36mcons60-koi8r[39;49;00m|[36mfreebsd console w/koi8-r cyrillic (60 lines)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m60[39;49;00m:[04m[32mtc[39;49;00m=cons25r:[37m[39;49;00m
[94mcons60r-m[39;49;00m|[36mcons60-koi8r-m[39;49;00m|[36mfreebsd console w/koi8-r cyrillic (60-line mono)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m60[39;49;00m:[04m[32mtc[39;49;00m=cons25r-m:[37m[39;49;00m
[37m# ISO 8859-1 FreeBSD console[39;49;00m[37m[39;49;00m
[94mcons25l1[39;49;00m|[36mcons25-iso8859[39;49;00m|[36mfreebsd console w/iso 8859-1 chars[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mac[39;49;00m=+\253\054\273-\030.\031`\201a\202f\207g\210i\247j\213k\214l\215m\216n\217o\220p\221q\222r\223s\224t\225u\226v\227w\230x\231y\232z\233~\237:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=cons25w:[37m[39;49;00m
[94mcons25l1-m[39;49;00m|[36mcons25-iso-m[39;49;00m|[36mfreebsd console w/iso 8859-1 chars (mono)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mCo@[39;49;00m:[04m[32mpa@[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAB@[39;49;00m:[04m[32mAF@[39;49;00m:[04m[32mmd@[39;49;00m:[04m[32mmh@[39;49;00m:[04m[32mop@[39;49;00m:[04m[32mue[39;49;00m=\E[m:[04m[32mus[39;49;00m=\E[4m:[04m[32mtc[39;49;00m=cons25l1:[37m[39;49;00m
[94mcons50l1[39;49;00m|[36mcons50-iso8859[39;49;00m|[36mfreebsd console w/iso 8859-1 chars (50 lines)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:[04m[32mtc[39;49;00m=cons25l1:[37m[39;49;00m
[94mcons50l1-m[39;49;00m|[36mcons50-iso-m[39;49;00m|[36mfreebsd console w/iso 8859-1 chars (50-line mono)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m50[39;49;00m:[04m[32mtc[39;49;00m=cons25l1-m:[37m[39;49;00m
[94mcons60l1[39;49;00m|[36mcons60-iso[39;49;00m|[36mfreebsd console w/iso 8859-1 chars (60 lines)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m60[39;49;00m:[04m[32mtc[39;49;00m=cons25l1:[37m[39;49;00m
[94mcons60l1-m[39;49;00m|[36mcons60-iso-m[39;49;00m|[36mfreebsd console w/iso 8859-1 chars (60-line mono)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m60[39;49;00m:[04m[32mtc[39;49;00m=cons25l1-m:[37m[39;49;00m
[37m[39;49;00m
[37m#### 386BSD and BSD/OS Consoles[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# This was the original 386BSD console entry (I think).  [39;49;00m[37m[39;49;00m
[37m# Some places it's named oldpc3|oldibmpc3.[39;49;00m[37m[39;49;00m
[37m# From: Alex R.N. Wetmore <aw2t@andrew.cmu.edu>[39;49;00m[37m[39;49;00m
[94morigpc3[39;49;00m|[36morigibmpc3[39;49;00m|[36mIBM PC 386BSD Console[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbw[39;49;00m:[04m[32meo[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mac[39;49;00m=j\331k\277l\332m\300n\305q\304t\303u\264v\301w\302x\263:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\Ec:[04m[32mcm[39;49;00m=\E[%i%2;%2H:[04m[32mdo[39;49;00m=\E[B:[04m[32mho[39;49;00m=\E[H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[Y:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mmd[39;49;00m=\E[7m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mme[39;49;00m=\E[m\E[1;0x\E[2;7x:[04m[32mnd[39;49;00m=\E[C:[04m[32mse[39;49;00m=\E[1;0x\E[2;7x:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32msf[39;49;00m=\E[S:[04m[32mso[39;49;00m=\E[1;7x\E[2;0x:[04m[32msr[39;49;00m=\E[T:[04m[32mue[39;49;00m=\E[1;0x\E[2;7x:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[1;7x\E[2;0x:[37m[39;49;00m
[37m[39;49;00m
[37m# description of BSD/386 console emulator in version 1.0 (supplied by BSDI)[39;49;00m[37m[39;49;00m
[94moldpc3[39;49;00m|[36moldibmpc3[39;49;00m|[36mold IBM PC BSD/386 Console[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkm[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mal[39;49;00m=\E[L:[04m[32mbl[39;49;00m=^G:[04m[32mcr[39;49;00m=^M:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=^J:[04m[32mkH[39;49;00m=\E[F:[04m[32mkI[39;49;00m=\E[L:[04m[32mkN[39;49;00m=\E[G:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkP[39;49;00m=\E[I:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[H:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\E[=15F:[04m[32mme[39;49;00m=\E[=R:[04m[32mmh[39;49;00m=\E[=8F:[04m[32mnw[39;49;00m=^M^J:[04m[32msf[39;49;00m=^J:[04m[32mta[39;49;00m=^I:[37m[39;49;00m
[37m[39;49;00m
[37m# Description of BSD/OS console emulator in version 1.1, 2.0, 2.1[39;49;00m[37m[39;49;00m
[37m# Note, the emulator supports many of the additional console features[39;49;00m[37m[39;49;00m
[37m# listed in the iBCS2 (e.g. character-set selection) though not all[39;49;00m[37m[39;49;00m
[37m# are described here.  This entry really ought to be upgraded.[39;49;00m[37m[39;49;00m
[37m# Also note, the console will also work with fewer lines after doing[39;49;00m[37m[39;49;00m
[37m# "stty rows NN", e.g. to use 24 lines.[39;49;00m[37m[39;49;00m
[37m# (Color support from Kevin Rosenberg <kevin@cyberport.com>, 2 May 1996) [39;49;00m[37m[39;49;00m
[37m# Bug: The <op> capability resets attributes.[39;49;00m[37m[39;49;00m
[94mbsdos-pc-nobold[39;49;00m|[36mBSD/OS PC console w/o bold[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32meo[39;49;00m:[04m[32mkm[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRI[39;49;00m=\E[%dC:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mUP[39;49;00m=\E[%dA:[04m[32mal[39;49;00m=\E[L:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\Ec:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=^J:[04m[32mho[39;49;00m=\E[H:[04m[32mkH[39;49;00m=\E[F:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkI[39;49;00m=\E[L:[04m[32mkN[39;49;00m=\E[G:[04m[32mkP[39;49;00m=\E[I:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[H:[04m[32mkl[39;49;00m=\E[D:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mnd[39;49;00m=\E[C:[04m[32mnw[39;49;00m=^M^J:[04m[32mrc[39;49;00m=\E8:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[0;10%?%p1%t;7%;%?%p3%t;7%;%?%p4%t;5%;%?%p6%t;1%;%?%p7%t;8%;%?%p9%t;11%;m%?%p5%t\E[=8F%;:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32msc[39;49;00m=\E7:[04m[32msf[39;49;00m=^J:[04m[32mta[39;49;00m=^I:[04m[32mup[39;49;00m=\E[A:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=klone+sgr:[04m[32mtc[39;49;00m=klone+color:[37m[39;49;00m
[94mbsdos-pc[39;49;00m|[36mIBM PC BSD/OS Console[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[0;10%?%p1%t;7%;%?%p2%t;1%;%?%p3%t;7%;%?%p4%t;5%;%?%p6%t;1%;%?%p7%t;8%;%?%p9%t;11%;m:[04m[32mtc[39;49;00m=bsdos-pc-nobold:[37m[39;49;00m
[37m[39;49;00m
[37m# Old names for BSD/OS PC console used in releases before 4.1. [39;49;00m[37m[39;49;00m
[94mpc3[39;49;00m|[36mBSD/OS on the PC Console[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=bsdos-pc-nobold:[37m[39;49;00m
[94mibmpc3[39;49;00m|[36mpc3-bold[39;49;00m|[36mBSD/OS on the PC Console with bold instead of underline[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=bsdos-pc:[37m[39;49;00m
[37m [39;49;00m[37m[39;49;00m
[37m# BSD/OS on the SPARC [39;49;00m[37m[39;49;00m
[94mbsdos-sparc[39;49;00m|[36mSun SPARC BSD/OS Console[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=sun:[37m[39;49;00m
[37m^I [39;49;00m[37m[39;49;00m
[37m# BSD/OS on the PowerPC [39;49;00m[37m[39;49;00m
[94mbsdos-ppc[39;49;00m|[36mPowerPC BSD/OS Console[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=bsdos-pc:[37m[39;49;00m
[37m[39;49;00m
[37m#### DEC VT100 and compatibles[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# DEC terminals from the vt100 forward are collected here. Older DEC terminals[39;49;00m[37m[39;49;00m
[37m# and micro consoles can be found in the `obsolete' section.  More details on[39;49;00m[37m[39;49;00m
[37m# the relationship between the VT100 and ANSI X3.64/ISO 6429/ECMA-48 may be[39;49;00m[37m[39;49;00m
[37m# found near the end of this file.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# Except where noted, these entries are DEC's official terminfos.[39;49;00m[37m[39;49;00m
[37m# Contact Bill Hedberg <hedberg@hannah.enet.dec.com> of Terminal Support[39;49;00m[37m[39;49;00m
[37m# Engineering for more information.  Updated terminfos and termcaps [39;49;00m[37m[39;49;00m
[37m# are kept available at ftp://gatekeeper.dec.com/pub/DEC/termcaps.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# In October 1995 DEC sold its terminals business, including the VT and Dorio[39;49;00m[37m[39;49;00m
[37m# line and trademark, to SunRiver Data Systems.  SunRiver has since changed[39;49;00m[37m[39;49;00m
[37m# its name to Boundless Technologies; see http://www.boundless.com.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# NOTE:  Any VT100 emulation, whether in hardware or software, almost[39;49;00m[37m[39;49;00m
[37m# certainly includes what DEC called the `Level 1 editing extension' codes;[39;49;00m[37m[39;49;00m
[37m# only the very oldest VT100s lacked these and there probably aren't any of[39;49;00m[37m[39;49;00m
[37m# those left alive.  To capture these, use one of the VT102 entries.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# Note that the :xn: glitch in vt100 is not quite the same as on the Concept,[39;49;00m[37m[39;49;00m
[37m# since the cursor is left in a different position while in the[39;49;00m[37m[39;49;00m
[37m# weird state (concept at beginning of next line, vt100 at end[39;49;00m[37m[39;49;00m
[37m# of this line) so all versions of vi before 3.7 don't handle[39;49;00m[37m[39;49;00m
[37m# :xn: right on vt100. The correct way to handle :xn: is when[39;49;00m[37m[39;49;00m
[37m# you output the char in column 80, immediately output CR LF[39;49;00m[37m[39;49;00m
[37m# and then assume you are in column 1 of the next line. If :xn:[39;49;00m[37m[39;49;00m
[37m# is on, am should be on too.[39;49;00m[37m[39;49;00m
[37m# [39;49;00m[37m[39;49;00m
[37m# I assume you have smooth scroll off or are at a slow enough baud[39;49;00m[37m[39;49;00m
[37m# rate that it doesn't matter (1200? or less). Also this assumes[39;49;00m[37m[39;49;00m
[37m# that you set auto-nl to "on", if you set it off use vt100-nam [39;49;00m[37m[39;49;00m
[37m# below.[39;49;00m[37m[39;49;00m
[37m# [39;49;00m[37m[39;49;00m
[37m# The padding requirements listed here are guesses. It is strongly[39;49;00m[37m[39;49;00m
[37m# recommended that xon/xoff be enabled, as this is assumed here.[39;49;00m[37m[39;49;00m
[37m# [39;49;00m[37m[39;49;00m
[37m# The vt100 uses <rs2> and <rf> rather than :is:/:ct:/:st: because the [39;49;00m[37m[39;49;00m
[37m# tab settings are in non-volatile memory and don't need to be [39;49;00m[37m[39;49;00m
[37m# reset upon login. Also setting the number of columns glitches [39;49;00m[37m[39;49;00m
[37m# the screen annoyingly. You can type "reset" to get them set.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# The VT100 series terminals have cursor ("arrows") keys which can operate[39;49;00m[37m[39;49;00m
[37m# in two different modes: Cursor Mode and Application Mode.  Cursor Mode[39;49;00m[37m[39;49;00m
[37m# is the reset state, and is assumed to be the normal state.  Application[39;49;00m[37m[39;49;00m
[37m# Mode is the "set" state.  In Cursor Mode, the cursor keys transmit[39;49;00m[37m[39;49;00m
[37m# "Esc [ {code}" sequences, conforming to ANSI standards.  In Application[39;49;00m[37m[39;49;00m
[37m# Mode, the cursor keys transmit "Esc O <code>" sequences.  Application Mode[39;49;00m[37m[39;49;00m
[37m# was provided primarily as an aid to the porting of VT52 applications.  It is[39;49;00m[37m[39;49;00m
[37m# assumed that the cursor keys are normally in Cursor Mode, and expected that[39;49;00m[37m[39;49;00m
[37m# applications such as vi will always transmit the :ks: string.  Therefore,[39;49;00m[37m[39;49;00m
[37m# the definitions for the cursor keys are made to match what the terminal[39;49;00m[37m[39;49;00m
[37m# transmits after the :ks: string is transmitted.  If the :ks: string[39;49;00m[37m[39;49;00m
[37m# is a null string or is not defined, then cursor keys are assumed to be in[39;49;00m[37m[39;49;00m
[37m# "Cursor Mode", and the cursor keys definitions should match that assumption,[39;49;00m[37m[39;49;00m
[37m# else the appication may fail.  It is also expected that applications will[39;49;00m[37m[39;49;00m
[37m# always transmit the :ke: string to the terminal before they exit.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# The VT100 series terminals have an auxilliary keypad, commonly referred to as[39;49;00m[37m[39;49;00m
[37m# the "Numeric Keypad", because it is a cluster of numeric and function keys.[39;49;00m[37m[39;49;00m
[37m# The Numeric Keypad which can operate in two different modes: Numeric Mode and[39;49;00m[37m[39;49;00m
[37m# Application Mode.  Numeric Mode is the reset state, and is assumed to be[39;49;00m[37m[39;49;00m
[37m# the normal state.  Application Mode is the "set" state.  In Numeric Mode,[39;49;00m[37m[39;49;00m
[37m# the numeric and punctuation keys transmit ASCII 7-bit characters, and the [39;49;00m[37m[39;49;00m
[37m# Enter key transmits the same as the Return key (Note: the Return key[39;49;00m[37m[39;49;00m
[37m# can be configured to send either LF (\015) or CR LF).  In Application Mode,[39;49;00m[37m[39;49;00m
[37m# all the keypad keys transmit "Esc O {code}" sequences.  The PF1 - PF4 keys[39;49;00m[37m[39;49;00m
[37m# always send the same "Esc O {code}" sequences.  It is assumed that the keypad[39;49;00m[37m[39;49;00m
[37m# is normally in Numeric Mode.  If an application requires that the keypad be[39;49;00m[37m[39;49;00m
[37m# in Application Mode then it is expected that the user, or the application,[39;49;00m[37m[39;49;00m
[37m# will set the TERM environment variable to point to a terminfo entry which has[39;49;00m[37m[39;49;00m
[37m# defined the :ks: string to include the codes that switch the keypad into[39;49;00m[37m[39;49;00m
[37m# Application Mode, and the terminfo entry will also define function key[39;49;00m[37m[39;49;00m
[37m# fields to match the Application Mode control codes.  If the :ks: string[39;49;00m[37m[39;49;00m
[37m# is a null string or is not defined, then the keypad is assumed to be in[39;49;00m[37m[39;49;00m
[37m# Numeric Mode.  If the :ks: string switches the keypad into Application[39;49;00m[37m[39;49;00m
[37m# Mode, it is expected that the :ke: string will contain the control codes[39;49;00m[37m[39;49;00m
[37m# necessary to reset the keypad to "Normal" mode, and it is also expected that[39;49;00m[37m[39;49;00m
[37m# applications which transmit the :ks: string will also always transmit the[39;49;00m[37m[39;49;00m
[37m# :ke: string to the terminal before they exit.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# Here's a diagram of the VT100 keypad keys with their bindings.[39;49;00m[37m[39;49;00m
[37m# The top line is the name of the key (some DEC keyboards have the keys[39;49;00m[37m[39;49;00m
[37m# labelled somewhat differently, like GOLD instead of PF1, but this is[39;49;00m[37m[39;49;00m
[37m# the most "official" name).  The second line is the escape sequence it[39;49;00m[37m[39;49;00m
[37m# generates in Application Keypad mode (where "$" means the ESC[39;49;00m[37m[39;49;00m
[37m# character).  The third line contains two items, first the mapping of[39;49;00m[37m[39;49;00m
[37m# the key in terminfo, and then in termcap.[39;49;00m[37m[39;49;00m
[37m#   _______________________________________[39;49;00m[37m[39;49;00m
[37m#  |   PF1   |   PF2   |   PF3   |   PF4   |[39;49;00m[37m[39;49;00m
[37m#  |   $OP   |   $OQ   |   $OR   |   $OS   |[39;49;00m[37m[39;49;00m
[37m#  |_kf1__k1_|_kf2__k2_|_kf3__k3_|_kf4__k4_|[39;49;00m[37m[39;49;00m
[37m#  |    7         8         9         -    |[39;49;00m[37m[39;49;00m
[37m#  |   $Ow   |   $Ox   |   $Oy   |   $Om   |[39;49;00m[37m[39;49;00m
[37m#  |_kf9__k9_|_kf10_k;_|_kf0__k0_|_________|[39;49;00m[37m[39;49;00m
[37m#  |    4    |    5    |    6    |    ,    |[39;49;00m[37m[39;49;00m
[37m#  |   $Ot   |   $Ou   |   $Ov   |   $Ol   |[39;49;00m[37m[39;49;00m
[37m#  |_kf5__k5_|_kf6__k6_|_kf7__k7_|_kf8__k8_|[39;49;00m[37m[39;49;00m
[37m#  |    1    |    2    |    3    |         |[39;49;00m[37m[39;49;00m
[37m#  |   $Oq   |   $Or   |   $Os   |  enter  |[39;49;00m[37m[39;49;00m
[37m#  |_ka1__K1_|_kb2__K2_|_ka3__K3_|  $OM    |[39;49;00m[37m[39;49;00m
[37m#  |         0         |   .     |         |[39;49;00m[37m[39;49;00m
[37m#  |        $Op        |  $On    |         |[39;49;00m[37m[39;49;00m
[37m#  |___kc1_______K4____|_kc3__K5_|_kent_@8_|[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# And here, for those of you with orphaned VT100s lacking documentation, is[39;49;00m[37m[39;49;00m
[37m# a description of the soft switches invoked when you do `Set Up'.[39;49;00m[37m[39;49;00m
[37m# [39;49;00m[37m[39;49;00m
[37m#  Scroll 0-Jump               Shifted 3   0-#[39;49;00m[37m[39;49;00m
[37m#  |      1-Smooth             |           1-British pound sign[39;49;00m[37m[39;49;00m
[37m#  | Autorepeat 0-Off          | Wrap Around 0-Off[39;49;00m[37m[39;49;00m
[37m#  | |          1-On           | |           1-On[39;49;00m[37m[39;49;00m
[37m#  | | Screen 0-Dark Bkg       | | New Line 0-Off[39;49;00m[37m[39;49;00m
[37m#  | | |      1-Light Bkg      | | |        1-On[39;49;00m[37m[39;49;00m
[37m#  | | | Cursor 0-Underline    | | | Interlace 0-Off[39;49;00m[37m[39;49;00m
[37m#  | | | |      1-Block        | | | |         1-On[39;49;00m[37m[39;49;00m
[37m#  | | | |                     | | | |[39;49;00m[37m[39;49;00m
[37m#  1 1 0 1       1 1 1 1       0 1 0 0       0 0 1 0       <--Standard Settings[39;49;00m[37m[39;49;00m
[37m#                | | | |                     | | | |[39;49;00m[37m[39;49;00m
[37m#                | | | Auto XON/XOFF 0-Off   | | | Power 0-60 Hz[39;49;00m[37m[39;49;00m
[37m#                | | |               1-On    | | |       1-50 Hz[39;49;00m[37m[39;49;00m
[37m#                | | Ansi/VT52 0-VT52        | | Bits Per Char. 0-7 Bits[39;49;00m[37m[39;49;00m
[37m#                | |           1-ANSI        | |                1-8 Bits[39;49;00m[37m[39;49;00m
[37m#                | Keyclick 0-Off            | Parity 0-Off[39;49;00m[37m[39;49;00m
[37m#                |          1-On             |        1-On[39;49;00m[37m[39;49;00m
[37m#                Margin Bell 0-Off           Parity Sense 0-Odd[39;49;00m[37m[39;49;00m
[37m#                            1-On                         1-Even[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# The following SET-UP modes are assumed for normal operation:[39;49;00m[37m[39;49;00m
[37m#^IANSI_MODE^IAUTO_XON/XOFF_ON^INEWLINE_OFF^I80_COLUMNS[39;49;00m[37m[39;49;00m
[37m#^IWRAP_AROUND_ON  JUMP_SCROLL_OFF[39;49;00m[37m[39;49;00m
[37m# Other SET-UP modes may be set for operator convenience or communication[39;49;00m[37m[39;49;00m
[37m# requirements; I recommend[39;49;00m[37m[39;49;00m
[37m#^IAUTOREPEAT_ON^IBLOCK_CURSOR^IMARGIN_BELL_OFF    SHIFTED_3_#[39;49;00m[37m[39;49;00m
[37m# Unless you have a graphics add-on such as Digital Engineering's VT640[39;49;00m[37m[39;49;00m
[37m# (and even then, whenever it can be arranged!) you should set[39;49;00m[37m[39;49;00m
[37m#^IINTERLACE_OFF[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# (vt100: I added <rmam>/<smam> based on the init string, also :bs:. -- esr)[39;49;00m[37m[39;49;00m
[94mvt100[39;49;00m|[36mvt100-am[39;49;00m|[36mdec vt100 (w/advanced video)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbs[39;49;00m:[04m[32mms[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m@8[39;49;00m=\EOM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mK1[39;49;00m=\EOq:[04m[32mK2[39;49;00m=\EOr:[04m[32mK3[39;49;00m=\EOs:[04m[32mK4[39;49;00m=\EOp:[04m[32mK5[39;49;00m=\EOn:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRA[39;49;00m=\E[?7l:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mSA[39;49;00m=\E[?7h:[04m[32mUP[39;49;00m=\E[%dA:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mac[39;49;00m=``aaffggjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mae[39;49;00m=^O:[04m[32mas[39;49;00m=^N:[04m[32mbl[39;49;00m=^G:[04m[32mcb[39;49;00m=\E[1K:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[J:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mct[39;49;00m=\E[3g:[04m[32mdo[39;49;00m=^J:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32meA[39;49;00m=\E(B\E)0:[04m[32mho[39;49;00m=\E[H:[04m[32mk0[39;49;00m=\EOy:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:[04m[32mk3[39;49;00m=\EOR:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk4[39;49;00m=\EOS:[04m[32mk5[39;49;00m=\EOt:[04m[32mk6[39;49;00m=\EOu:[04m[32mk7[39;49;00m=\EOv:[04m[32mk8[39;49;00m=\EOl:[04m[32mk9[39;49;00m=\EOw:[04m[32mk;[39;49;00m=\EOx:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\EOB:[04m[32mke[39;49;00m=\E[?1l\E>:[04m[32mkl[39;49;00m=\EOD:[04m[32mkr[39;49;00m=\EOC:[04m[32mks[39;49;00m=\E[?1h\E=:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mku[39;49;00m=\EOA:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m\017:[04m[32mmr[39;49;00m=\E[7m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mnd[39;49;00m=\E[C:[04m[32mr2[39;49;00m=\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:[04m[32mrc[39;49;00m=\E8:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[0%?%p1%p6%|%t;1%;%?%p2%t;4%;%?%p1%p3%|%t;7%;%?%p4%t;5%;m%?%p9%t\016%e\017%;:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[m:[04m[32msf[39;49;00m=^J:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:[37m[39;49;00m
[94mvt100nam[39;49;00m|[36mvt100-nam[39;49;00m|[36mvt100 no automargins[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam@[39;49;00m:[04m[32mxn@[39;49;00m:[04m[32mtc[39;49;00m=vt100-am:[37m[39;49;00m
[94mvt100-vb[39;49;00m|[36mdec vt100 (w/advanced video) & no beep[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mbl@[39;49;00m:[04m[32mvb[39;49;00m=\E[?5h\E[?5l:[04m[32mtc[39;49;00m=vt100:[37m[39;49;00m
[37m[39;49;00m
[37m# Ordinary vt100 in 132 column ("wide") mode.[39;49;00m[37m[39;49;00m
[94mvt100-w[39;49;00m|[36mvt100-w-am[39;49;00m|[36mdec vt100 132 cols (w/advanced video)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mr2[39;49;00m=\E>\E[?3h\E[?4l\E[?5l\E[?8h:[04m[32mtc[39;49;00m=vt100-am:[37m[39;49;00m
[94mvt100-w-nam[39;49;00m|[36mvt100-nam-w[39;49;00m|[36mdec vt100 132 cols (w/advanced video no automargin)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m14[39;49;00m:[04m[32mvt@[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mr2[39;49;00m=\E>\E[?3h\E[?4l\E[?5l\E[?8h:[04m[32mtc[39;49;00m=vt100-nam:[37m[39;49;00m
[37m[39;49;00m
[37m# vt100 with no advanced video.[39;49;00m[37m[39;49;00m
[94mvt100-nav[39;49;00m|[36mvt100 without advanced video option[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32msg[39;49;00m#[34m1[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmb@[39;49;00m:[04m[32mmd@[39;49;00m:[04m[32mme@[39;49;00m:[04m[32mmr@[39;49;00m:[04m[32msa@[39;49;00m:[04m[32mse[39;49;00m=\E[m:[04m[32mso[39;49;00m=\E[7m:[04m[32mue@[39;49;00m:[04m[32mus@[39;49;00m:[04m[32mtc[39;49;00m=vt100:[37m[39;49;00m
[94mvt100-nav-w[39;49;00m|[36mvt100-w-nav[39;49;00m|[36mdec vt100 132 cols 14 lines (no advanced video option)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mli[39;49;00m#[34m14[39;49;00m:[04m[32mtc[39;49;00m=vt100-nav:[37m[39;49;00m
[37m[39;49;00m
[37m# vt100 with one of the 24 lines used as a status line.[39;49;00m[37m[39;49;00m
[37m# We put the status line on the top.[39;49;00m[37m[39;49;00m
[94mvt100-s[39;49;00m|[36mvt100-s-top[39;49;00m|[36mvt100-top-s[39;49;00m|[36mvt100 for use with top sysline[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mes[39;49;00m:[04m[32mhs[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m23[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcl[39;49;00m=\E[2;1H\E[J:[04m[32mcm[39;49;00m=\E[%i%+^A;%dH:[04m[32mcs[39;49;00m=\E[%i%i%d;%dr:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mds[39;49;00m=\E7\E[1;24r\E8:[04m[32mfs[39;49;00m=\E8:[04m[32mho[39;49;00m=\E[2;1H:[04m[32mis[39;49;00m=\E7\E[2;24r\E8:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mts[39;49;00m=\E7\E[1;%p1%dH\E[1K:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt100-am:[37m[39;49;00m
[37m[39;49;00m
[37m# Status line at bottom. [39;49;00m[37m[39;49;00m
[37m# Clearing the screen will clobber status line.[39;49;00m[37m[39;49;00m
[94mvt100-s-bot[39;49;00m|[36mvt100-bot-s[39;49;00m|[36mvt100 for use with bottom sysline[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mes[39;49;00m:[04m[32mhs[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m23[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mds[39;49;00m=\E7\E[1;24r\E8:[04m[32mfs[39;49;00m=\E8:[04m[32mis[39;49;00m=\E[1;23r\E[23;1H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mts[39;49;00m=\E7\E[24;%p1%dH\E[1K:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt100-am:[37m[39;49;00m
[37m[39;49;00m
[37m# Most of the `vt100' emulators out there actually emulate a vt102[39;49;00m[37m[39;49;00m
[37m# This entry (or vt102-nsgr) is probably the right thing to use for[39;49;00m[37m[39;49;00m
[37m# these.  [39;49;00m[37m[39;49;00m
[94mvt102[39;49;00m|[36mdec vt102[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmi[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mal[39;49;00m=\E[L:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mei[39;49;00m=\E[4l:[04m[32mim[39;49;00m=\E[4h:[04m[32mtc[39;49;00m=vt100:[37m[39;49;00m
[94mvt102-w[39;49;00m|[36mdec vt102 in wide mode[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mr3[39;49;00m=\E[?3h:[04m[32mtc[39;49;00m=vt102:[37m[39;49;00m
[37m[39;49;00m
[37m# Many brain-dead PC comm programs that pretend to be `vt100-compatible'[39;49;00m[37m[39;49;00m
[37m# fail to interpret the ^O and ^N escapes properly.  Symptom: the :me:[39;49;00m[37m[39;49;00m
[37m# string in the canonical vt100 entry above leaves the screen littered[39;49;00m[37m[39;49;00m
[37m# with little  snowflake or star characters (IBM PC ROM character \017 = ^O)[39;49;00m[37m[39;49;00m
[37m# after highlight turnoffs.  This entry should fix that, and even leave[39;49;00m[37m[39;49;00m
[37m# ACS support working, at the cost of making multiple-highlight changes [39;49;00m[37m[39;49;00m
[37m# slightly more expensive.[39;49;00m[37m[39;49;00m
[37m# From: Eric S. Raymond <esr@snark.thyrsus.com> July 22 1995[39;49;00m[37m[39;49;00m
[94mvt102-nsgr[39;49;00m|[36mvt102 no sgr (use if you see snowflakes after highlight changes)[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mme[39;49;00m=\E[m:[04m[32msa@[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt102:[37m[39;49;00m
[37m[39;49;00m
[37m# VT125 Graphics CRT.  Clear screen also erases graphics[39;49;00m[37m[39;49;00m
[94mvt125[39;49;00m|[36mvt125 graphics terminal[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcl[39;49;00m=\E[H\E[2J\EPpS(E)\E\:[04m[32mtc[39;49;00m=vt100:[37m[39;49;00m
[37m[39;49;00m
[37m# This isn't a DEC entry, it came from University of Wisconsin.[39;49;00m[37m[39;49;00m
[37m# (vt131: I added <rmam>/<smam> based on the init string, also :bs: -- esr)[39;49;00m[37m[39;49;00m
[94mvt131[39;49;00m|[36mdec vt131[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbs[39;49;00m:[04m[32mxn[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mRA[39;49;00m=\E[?7h:[04m[32mSA[39;49;00m=\E[?7h:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=50\E[J:[04m[32mce[39;49;00m=3\E[K:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcl[39;49;00m=50\E[;H\E[2J:[04m[32mcm[39;49;00m=5\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mdo[39;49;00m=^J:[04m[32mho[39;49;00m=\E[H:[04m[32mis[39;49;00m=\E[1;24r\E[24;1H:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\EOB:[04m[32mke[39;49;00m=\E[?1l\E>:[04m[32mkl[39;49;00m=\EOD:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkr[39;49;00m=\EOC:[04m[32mks[39;49;00m=\E[?1h\E=:[04m[32mku[39;49;00m=\EOA:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=2\E[5m:[04m[32mmd[39;49;00m=2\E[1m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mme[39;49;00m=2\E[m:[04m[32mmr[39;49;00m=2\E[7m:[04m[32mnd[39;49;00m=2\E[C:[04m[32mnw[39;49;00m=^M^J:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mr1[39;49;00m=\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:[04m[32mrc[39;49;00m=\E8:[04m[32msc[39;49;00m=\E7:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mse[39;49;00m=2\E[m:[04m[32mso[39;49;00m=2\E[7m:[04m[32msr[39;49;00m=5\EM:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=2\E[m:[04m[32mup[39;49;00m=2\E[A:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mus[39;49;00m=2\E[4m:[37m[39;49;00m
[37m[39;49;00m
[37m# vt132 - like vt100 but slower and has ins/del line and such.[39;49;00m[37m[39;49;00m
[37m# I'm told that :im:/:ei: are backwards in the terminal from the[39;49;00m[37m[39;49;00m
[37m# manual and from the ANSI standard, this describes the actual [39;49;00m[37m[39;49;00m
[37m# terminal. I've never actually used a vt132 myself, so this [39;49;00m[37m[39;49;00m
[37m# is untested.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[94mvt132[39;49;00m|[36mDEC vt132[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mxn[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mal[39;49;00m=\E[L:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mei[39;49;00m=\E[4h:[04m[32mim[39;49;00m=\E[4l:[04m[32mip[39;49;00m=:[04m[32msf[39;49;00m=\n:[04m[32mtc[39;49;00m=vt100:[37m[39;49;00m
[37m[39;49;00m
[37m# This vt220 description maps F5--F9 to the second block of function keys[39;49;00m[37m[39;49;00m
[37m# at the top of the keyboard.  The "DO" key is used as F10 to avoid conflict[39;49;00m[37m[39;49;00m
[37m# with the key marked (ESC) on the vt220.  See vt220d for an alternate mapping.[39;49;00m[37m[39;49;00m
[37m# PF1--PF4 are used as F1--F4.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[94mvt220-old[39;49;00m|[36mvt200-old[39;49;00m|[36mDEC VT220 in vt100 emulation mode[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbs[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mpt[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m@7[39;49;00m=\E[4~:[04m[32mRA[39;49;00m=\E[?7l:[04m[32mSA[39;49;00m=\E[?7h:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mac[39;49;00m=``aaffggjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mae[39;49;00m=\E(B:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=\E(0:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcl[39;49;00m=\E[H\E[2J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=\E[B:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mif[39;49;00m=/usr/share/tabset/vt100:[04m[32mim[39;49;00m=\E[4h:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[1;24r\E[24;1H:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk5[39;49;00m=\E[17~:[04m[32mk6[39;49;00m=\E[18~:[04m[32mk7[39;49;00m=\E[19~:[04m[32mk8[39;49;00m=\E[20~:[04m[32mk9[39;49;00m=\E[21~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk;[39;49;00m=\E[29~:[04m[32mkD[39;49;00m=\E[3~:[04m[32mkI[39;49;00m=\E[2~:[04m[32mkN[39;49;00m=\E[6~:[04m[32mkP[39;49;00m=\E[5~:[04m[32mkb[39;49;00m=^H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[1~:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mnl[39;49;00m=^J:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mr2[39;49;00m=\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:[04m[32mrc[39;49;00m=\E8:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mrf[39;49;00m=/usr/share/tabset/vt100:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[0%?%p6%t;1%;%?%p2%t;4%;%?%p4%t;5%;%?%p1%p3%|%t;7%;m%?%p9%t\E(0%e\E(B%;:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[27m:[04m[32msf[39;49;00m=20\ED:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=14\EM:[04m[32mta[39;49;00m=^I:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mue[39;49;00m=\E[24m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:[04m[32mve[39;49;00m=\E[?25h:[04m[32mvi[39;49;00m=\E[?25l:[37m[39;49;00m
[37m[39;49;00m
[37m# A much better description of the VT200/220; used to be vt220-8[39;49;00m[37m[39;49;00m
[37m# (untranslatable capabilities removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m
[37m# (sgr removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m
[37m# (terminfo-only capabilities suppressed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m
[94mvt220[39;49;00m|[36mvt200[39;49;00m|[36mdec vt220[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbs[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mms[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mIC[39;49;00m=\E[%d@:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mUP[39;49;00m=\E[%dA:[04m[32mae[39;49;00m=^O:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=^N:[04m[32mbl[39;49;00m=^G:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mct[39;49;00m=\E[3g:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=^J:[04m[32mec[39;49;00m=\E[%dX:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:[04m[32mif[39;49;00m=/usr/share/tabset/vt100:[04m[32mim[39;49;00m=\E[4h:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[?7h\E[>\E[?1h\E F\E[?4l:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:[04m[32mk3[39;49;00m=\EOR:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk4[39;49;00m=\EOS:[04m[32mk6[39;49;00m=\E[17~:[04m[32mk7[39;49;00m=\E[18~:[04m[32mk8[39;49;00m=\E[19~:[04m[32mk9[39;49;00m=\E[20~:[04m[32mkI[39;49;00m=\E[2~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkN[39;49;00m=\E[6~:[04m[32mkP[39;49;00m=\E[5~:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkh[39;49;00m=\E[H:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mnw[39;49;00m=\EE:[04m[32mrc[39;49;00m=\E8:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[27m:[04m[32msf[39;49;00m=\ED:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[24m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:[04m[32mvb[39;49;00m=\E[?5h\E[?5l:[37m[39;49;00m
[94mvt220-w[39;49;00m|[36mvt200-w[39;49;00m|[36mDEC vt220 in wide mode[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mr3[39;49;00m=\E[?3h:[04m[32mtc[39;49;00m=vt220:[37m[39;49;00m
[37m# (untranslatable capabilities removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m
[37m# (sgr removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m
[37m# (terminfo-only capabilities suppressed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m
[94mvt220-8bit[39;49;00m|[36mvt220-8[39;49;00m|[36mvt200-8bit[39;49;00m|[36mvt200-8[39;49;00m|[36mdec vt220/200 in 8-bit mode[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mbs[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mms[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\233%dL:[04m[32mDC[39;49;00m=\233%dP:[04m[32mDL[39;49;00m=\233%dM:[04m[32mDO[39;49;00m=\233%dB:[04m[32mIC[39;49;00m=\233%d@:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\233%dD:[04m[32mRI[39;49;00m=\233%dC:[04m[32mUP[39;49;00m=\233%dA:[04m[32mae[39;49;00m=^O:[04m[32mal[39;49;00m=\233L:[04m[32mas[39;49;00m=^N:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\233J:[04m[32mce[39;49;00m=\233K:[04m[32mcl[39;49;00m=\233H\233J:[04m[32mcm[39;49;00m=\233%i%d;%dH:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\233%i%d;%dr:[04m[32mct[39;49;00m=\2333g:[04m[32mdc[39;49;00m=\233P:[04m[32mdl[39;49;00m=\233M:[04m[32mdo[39;49;00m=^J:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mec[39;49;00m=\233%dX:[04m[32mei[39;49;00m=\2334l:[04m[32mho[39;49;00m=\233H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mif[39;49;00m=/usr/share/tabset/vt100:[04m[32mim[39;49;00m=\2334h:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\233?7h\233>\233?1h\E F\233?4l:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:[04m[32mk6[39;49;00m=\23317~:[04m[32mk7[39;49;00m=\23318~:[04m[32mk8[39;49;00m=\23319~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk9[39;49;00m=\23320~:[04m[32mkI[39;49;00m=\2332~:[04m[32mkN[39;49;00m=\2336~:[04m[32mkP[39;49;00m=\2335~:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\233B:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkh[39;49;00m=\233H:[04m[32mkl[39;49;00m=\233D:[04m[32mkr[39;49;00m=\233C:[04m[32mku[39;49;00m=\233A:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\2335m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\2331m:[04m[32mme[39;49;00m=\233m:[04m[32mmr[39;49;00m=\2337m:[04m[32mnd[39;49;00m=\233C:[04m[32mnw[39;49;00m=\EE:[04m[32mrc[39;49;00m=\E8:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\23327m:[04m[32msf[39;49;00m=\ED:[04m[32mso[39;49;00m=\2337m:[04m[32msr[39;49;00m=\EM:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mue[39;49;00m=\23324m:[04m[32mup[39;49;00m=\233A:[04m[32mus[39;49;00m=\2334m:[04m[32mvb[39;49;00m=\233?5h\233?5l:[37m[39;49;00m
[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# vt220d:[39;49;00m[37m[39;49;00m
[37m# This vt220 description regards F6--F10 as the second block of function keys[39;49;00m[37m[39;49;00m
[37m# at the top of the keyboard.  This mapping follows the description given[39;49;00m[37m[39;49;00m
[37m# in the VT220 Programmer Reference Manual and agrees with the labeling[39;49;00m[37m[39;49;00m
[37m# on some terminals that emulate the vt220.  There is no support for an F5.[39;49;00m[37m[39;49;00m
[37m# See vt220 for an alternate mapping. [39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[94mvt220d[39;49;00m|[36mDEC VT220 in vt100 mode with DEC function key labeling[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mF1[39;49;00m=\E[23~:[04m[32mF2[39;49;00m=\E[24~:[04m[32mF3[39;49;00m=\E[25~:[04m[32mF4[39;49;00m=\E[26~:[04m[32mF5[39;49;00m=\E[28~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mF6[39;49;00m=\E[29~:[04m[32mF7[39;49;00m=\E[31~:[04m[32mF8[39;49;00m=\E[32~:[04m[32mF9[39;49;00m=\E[33~:[04m[32mFA[39;49;00m=\E[34~:[04m[32mk5@[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk6[39;49;00m=\E[17~:[04m[32mk7[39;49;00m=\E[18~:[04m[32mk8[39;49;00m=\E[19~:[04m[32mk9[39;49;00m=\E[20~:[04m[32mk;[39;49;00m=\E[21~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt220-old:[37m[39;49;00m
[37m[39;49;00m
[94mvt220-nam[39;49;00m|[36mv200-nam[39;49;00m|[36mVT220 in vt100 mode with no auto margins[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam@[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mr2[39;49;00m=\E>\E[?3l\E[?4l\E[?5l\E[?7l\E[?8h:[04m[32mtc[39;49;00m=vt220:[37m[39;49;00m
[37m[39;49;00m
[37m# vt220 termcap written Tue Oct 25 20:41:10 1988 by Alex Latzko[39;49;00m[37m[39;49;00m
[37m# (not an official DEC entry!)[39;49;00m[37m[39;49;00m
[37m# The problem with real vt220 terminals is they don't send escapes when in[39;49;00m[37m[39;49;00m
[37m# in vt220 mode.  This can be gotten around two ways.  1> don't send[39;49;00m[37m[39;49;00m
[37m# escapes or 2> put the vt220 into vt100 mode and use all the nifty[39;49;00m[37m[39;49;00m
[37m# features of vt100 advanced video which it then has.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# This entry takes the view of putting a vt220 into vt100 mode so[39;49;00m[37m[39;49;00m
[37m# you can use the escape key in emacs and everything else which needs it.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# You probably don't want to use this on a VMS machine since VMS will think[39;49;00m[37m[39;49;00m
[37m# it has a vt220 and will get fouled up coming out of emacs[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# From: Alexander Latzko <latzko@marsenius.rutgers.edu>, 30 Dec 1996[39;49;00m[37m[39;49;00m
[37m# (Added vt100 :rc:,:sc: to quiet a tic warning -- esr)[39;49;00m[37m[39;49;00m
[94mvt200-js[39;49;00m|[36mvt220-js[39;49;00m|[36mdec vt200 series with jump scroll[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mal[39;49;00m=\E[L:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdm[39;49;00m=:[04m[32mdo[39;49;00m=^J:[04m[32med[39;49;00m=:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:[04m[32mim[39;49;00m=\E[4h:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E[61"p\E[H\E[?3l\E[?4l\E[?1l\E[?5l\E[?6l\E[?7h\E[?8h\E[?25h\E>\E[m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\EOB:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mke[39;49;00m=\E[?1l\E>:[04m[32mkl[39;49;00m=\EOD:[04m[32mkr[39;49;00m=\EOC:[04m[32mks[39;49;00m=\E[?1h\E=:[04m[32mku[39;49;00m=\EOA:[04m[32mle[39;49;00m=^H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mnw[39;49;00m=^M\ED:[04m[32mr1[39;49;00m=\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:[04m[32mrc[39;49;00m=\E8:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mrf[39;49;00m=/usr/lib/tabset/vt100:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=5\E[27m:[04m[32msf[39;49;00m=\ED:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mso[39;49;00m=5\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[24m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:[37m[39;49;00m
[37m [39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m# This was DEC's vt320.  Use the purpose-built one below instead [39;49;00m[37m[39;49;00m
[37m#vt320|DEC VT320 in vt100 emulation mode,[39;49;00m[37m[39;49;00m
[37m#^Iuse=vt220,[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# Use v320n for SCO's LYRIX.  Otherwise, use Adam Thompson's vt320-nam.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[94mvt320nam[39;49;00m|[36mv320n[39;49;00m|[36mDEC VT320 in vt100 emul. mode with NO AUTO WRAP mode[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam@[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mr2[39;49;00m=\E>\E[?3l\E[?4l\E[?5l\E[?7l\E[?8h:[04m[32mtc[39;49;00m=vt220:[37m[39;49;00m
[37m[39;49;00m
[37m# These entries are not DEC's official ones, they were purpose-built for the [39;49;00m[37m[39;49;00m
[37m# VT320.  Here are the designer's notes:[39;49;00m[37m[39;49;00m
[37m# <kel> is end on a PC kbd.  Actually 'select' on a VT.  Mapped to [39;49;00m[37m[39;49;00m
[37m# 'Erase to End of Field'... since nothing seems to use 'end' anyways...[39;49;00m[37m[39;49;00m
[37m# khome is Home on a PC kbd.  Actually 'FIND' on a VT.[39;49;00m[37m[39;49;00m
[37m# Things that use <knxt> usually use tab anyways... and things that don't use[39;49;00m[37m[39;49;00m
[37m# tab usually use <knxt> instead...[39;49;00m[37m[39;49;00m
[37m# kprv is same as tab - Backtab is useless...[39;49;00m[37m[39;49;00m
[37m# I left out :sa: because of its RIDICULOUS complexity,[39;49;00m[37m[39;49;00m
[37m# and the resulting fact that it causes the termcap translation of the entry[39;49;00m[37m[39;49;00m
[37m# to SMASH the 1k-barrier...[39;49;00m[37m[39;49;00m
[37m# From: Adam Thompson <athompso@pangea.ca> Sept 10 1995[39;49;00m[37m[39;49;00m
[37m# (vt320: uncommented :fs:, comnmmented out <kslt> to avoid a conflict --esr) [39;49;00m[37m[39;49;00m
[37m# (untranslatable capabilities removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m
[37m# (sgr removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m
[37m# (terminfo-only capabilities suppressed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m
[94mvt320[39;49;00m|[36mvt300[39;49;00m|[36mdec vt320 7 bit terminal[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mes[39;49;00m:[04m[32mhs[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mms[39;49;00m:[04m[32mxn[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mws[39;49;00m#[34m80[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mIC[39;49;00m=\E[%d@:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mK1[39;49;00m=\EOw:[04m[32mK2[39;49;00m=\EOu:[04m[32mK3[39;49;00m=\EOy:[04m[32mK4[39;49;00m=\EOq:[04m[32mK5[39;49;00m=\EOs:[04m[32mLE[39;49;00m=\E[%dD:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mUP[39;49;00m=\E[%dA:[04m[32mae[39;49;00m=\E(B:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=\E(0:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[2J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mct[39;49;00m=\E[3g:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=^J:[04m[32mec[39;49;00m=\E[%dX:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mei[39;49;00m=\E[4l:[04m[32mfs[39;49;00m=\E[0$}:[04m[32mho[39;49;00m=\E[H:[04m[32mim[39;49;00m=\E[4h:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E>\E[?3l\E[?4l\E[5?l\E[?7h\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:[04m[32mk6[39;49;00m=\E[17~:[04m[32mk7[39;49;00m=\E[18~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk8[39;49;00m=\E[19~:[04m[32mk9[39;49;00m=\E[20~:[04m[32mkD[39;49;00m=\E[3~:[04m[32mkI[39;49;00m=\E[2~:[04m[32mkN[39;49;00m=\E[6~:[04m[32mkP[39;49;00m=\E[5~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkb[39;49;00m=\177:[04m[32mkd[39;49;00m=\EOB:[04m[32mke[39;49;00m=\E[?1l\E>:[04m[32mkh[39;49;00m=\E[1~:[04m[32mkl[39;49;00m=\EOD:[04m[32mkr[39;49;00m=\EOC:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mks[39;49;00m=\E[?1h\E=:[04m[32mku[39;49;00m=\EOA:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mnw[39;49;00m=\EE:[04m[32mrc[39;49;00m=\E8:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[m:[04m[32msf[39;49;00m=\ED:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:[04m[32mts[39;49;00m=\E[1$}\E[H\E[K:[04m[32mue[39;49;00m=\E[m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:[04m[32mve[39;49;00m=\E[?25h:[04m[32mvi[39;49;00m=\E[?25l:[37m[39;49;00m
[94mvt320-nam[39;49;00m|[36mvt300-nam[39;49;00m|[36mdec vt320 7 bit terminal with no am to make SAS happy[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam@[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E>\E[?3l\E[?4l\E[5?l\E[?7l\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mr2[39;49;00m=\E>\E[?3l\E[?4l\E[5?l\E[?7l\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt320:[37m[39;49;00m
[37m# We have to init 132-col mode, not 80-col mode.[39;49;00m[37m[39;49;00m
[94mvt320-w[39;49;00m|[36mvt300-w[39;49;00m|[36mdec vt320 wide 7 bit terminal[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m132[39;49;00m:[04m[32mws[39;49;00m#[34m132[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E>\E[?3h\E[?4l\E[5?l\E[?7h\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mr2[39;49;00m=\E>\E[?3h\E[?4l\E[5?l\E[?7h\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt320:[37m[39;49;00m
[94mvt320-w-nam[39;49;00m|[36mvt300-w-nam[39;49;00m|[36mdec vt320 wide 7 bit terminal with no am[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam@[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E>\E[?3h\E[?4l\E[5?l\E[?7l\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mr2[39;49;00m=\E>\E[?3h\E[?4l\E[5?l\E[?7l\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt320-w:[37m[39;49;00m
[37m[39;49;00m
[37m# VT330 and VT340 -- These are ReGIS and SIXEL graphics terminals[39;49;00m[37m[39;49;00m
[37m#   which are pretty much a superset of the VT320.  They have the[39;49;00m[37m[39;49;00m
[37m#   host writable status line, yet another different DRCS matrix size,[39;49;00m[37m[39;49;00m
[37m#   and such, but they add the DEC Technical character set, Multiple text[39;49;00m[37m[39;49;00m
[37m#   pages, selectable length pages, and the like.  The difference between[39;49;00m[37m[39;49;00m
[37m#   the vt330 and vt340 is that the latter has only 2 planes and a monochrome[39;49;00m[37m[39;49;00m
[37m#   monitor, the former has 4 planes and a color monitor.  These terminals[39;49;00m[37m[39;49;00m
[37m#   support VT131 and ANSI block mode, but as with much of these things,[39;49;00m[37m[39;49;00m
[37m#   termcap/terminfo doesn't deal with these features.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# Note that this entry is are set up in what was the standard way for GNU[39;49;00m[37m[39;49;00m
[37m# Emacs v18 terminal modes to deal with the cursor keys in that the arrow[39;49;00m[37m[39;49;00m
[37m# keys were switched into application mode at the same time the numeric pad[39;49;00m[37m[39;49;00m
[37m# is switched into application mode.  This changes the definitions of the[39;49;00m[37m[39;49;00m
[37m# arrow keys.  Emacs v19 is smarter and mines its keys directly out of [39;49;00m[37m[39;49;00m
[37m# your termcap or terminfo entry,[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# From: Daniel Glasser <dag@persoft.persoft.com>, 13 Oct 1993[39;49;00m[37m[39;49;00m
[37m# (vt340: string capability "sb=\E[M" corrected to "sr";[39;49;00m[37m[39;49;00m
[37m# also, added <rmam>/<smam> based on the init string -- esr)[39;49;00m[37m[39;49;00m
[94mvt340[39;49;00m|[36mdec-vt340[39;49;00m|[36mvt330[39;49;00m|[36mdec-vt330[39;49;00m|[36mdec vt340 graphics terminal with 24 line page[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mes[39;49;00m:[04m[32mhs[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mms[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mIC[39;49;00m=\E[%d@:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRA[39;49;00m=\E[?7l:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mSA[39;49;00m=\E[?7h:[04m[32mUP[39;49;00m=\E[%dA:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mac[39;49;00m=``aaffggjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mae[39;49;00m=^O:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=^N:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:[04m[32mcl[39;49;00m=\E[H\E[J:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mct[39;49;00m=\E[3g:[04m[32mdc[39;49;00m=\E[P:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=^J:[04m[32mds[39;49;00m=\E[2$~\r\E[1$}\E[K\E[$}:[04m[32mei[39;49;00m=\E[4l:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mfs[39;49;00m=\E[$}:[04m[32mho[39;49;00m=\E[H:[04m[32mim[39;49;00m=\E[4h:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E<\E F\E>\E[?1h\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:[04m[32mk6[39;49;00m=\E[17~:[04m[32mk7[39;49;00m=\E[18~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk8[39;49;00m=\E[19~:[04m[32mk9[39;49;00m=\E[20~:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\EOB:[04m[32mke[39;49;00m=\E[?1l\E>:[04m[32mkl[39;49;00m=\EOD:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkr[39;49;00m=\EOC:[04m[32mks[39;49;00m=\E[?1h\E=:[04m[32mku[39;49;00m=\EOA:[04m[32ml1[39;49;00m=pf1:[04m[32ml2[39;49;00m=pf2:[04m[32ml3[39;49;00m=pf3:[04m[32ml4[39;49;00m=pf4:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mnw[39;49;00m=^M\ED:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mr1[39;49;00m=\E[?3l:[04m[32mrc[39;49;00m=\E8:[04m[32mrf[39;49;00m=/usr/share/tabset/vt300:[04m[32msc[39;49;00m=\E7:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mse[39;49;00m=\E[27m:[04m[32msf[39;49;00m=\ED:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mts[39;49;00m=\E[2$~\E[1$}\E[1;%dH:[04m[32mue[39;49;00m=\E[24m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mvb[39;49;00m=200\E[?5h\E[?5l:[04m[32mve[39;49;00m=\E[?25h:[04m[32mvi[39;49;00m=\E[?25l:[04m[32mvs[39;49;00m=\E[?25h:[37m[39;49;00m
[37m[39;49;00m
[37m# DEC doesn't supply a vt400 description, so we add Daniel Glasser's[39;49;00m[37m[39;49;00m
[37m# (originally written with vt420 as its primary name, and usable for it).[39;49;00m[37m[39;49;00m
[37m# [39;49;00m[37m[39;49;00m
[37m# VT400/420 -- This terminal is a superset of the vt320.  It adds the multiple [39;49;00m[37m[39;49;00m
[37m#    text pages and long text pages with selectable length of the vt340, along[39;49;00m[37m[39;49;00m
[37m#    with left and right margins, rectangular area text copy, fill, and erase[39;49;00m[37m[39;49;00m
[37m#    operations, selected region character attribute change operations,[39;49;00m[37m[39;49;00m
[37m#    page memory and rectangle checksums, insert/delete column, reception[39;49;00m[37m[39;49;00m
[37m#    macros, and other features too numerous to remember right now.  TERMCAP[39;49;00m[37m[39;49;00m
[37m#    can only take advantage of a few of these added features.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# Note that this entry is are set up in what was the standard way for GNU[39;49;00m[37m[39;49;00m
[37m# Emacs v18 terminal modes to deal with the cursor keys in that the arrow[39;49;00m[37m[39;49;00m
[37m# keys were switched into application mode at the same time the numeric pad[39;49;00m[37m[39;49;00m
[37m# is switched into application mode.  This changes the definitions of the[39;49;00m[37m[39;49;00m
[37m# arrow keys.  Emacs v19 is smarter and mines its keys directly out of [39;49;00m[37m[39;49;00m
[37m# your termcap entry,[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# From: Daniel Glasser <dag@persoft.persoft.com>, 13 Oct 1993[39;49;00m[37m[39;49;00m
[37m# (vt400: string capability ":sb=\E[M:" corrected to ":sr=\E[M:";[39;49;00m[37m[39;49;00m
[37m# also, added <rmam>/<smam> based on the init string -- esr)[39;49;00m[37m[39;49;00m
[37m# (untranslatable capabilities removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m
[37m# (sgr removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m
[37m# (terminfo-only capabilities suppressed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m
[94mvt400[39;49;00m|[36mvt400-24[39;49;00m|[36mdec-vt400[39;49;00m|[36mdec vt400 24x80 column autowrap[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mes[39;49;00m:[04m[32mhs[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mms[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mit[39;49;00m#[34m8[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mAL[39;49;00m=\E[%dL:[04m[32mDC[39;49;00m=\E[%dP:[04m[32mDL[39;49;00m=\E[%dM:[04m[32mDO[39;49;00m=\E[%dB:[04m[32mIC[39;49;00m=\E[%d@:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mLE[39;49;00m=\E[%dD:[04m[32mRI[39;49;00m=\E[%dC:[04m[32mUP[39;49;00m=\E[%dA:[04m[32mae[39;49;00m=^O:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=^N:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcd[39;49;00m=10\E[J:[04m[32mce[39;49;00m=4\E[K:[04m[32mcl[39;49;00m=10\E[H\E[J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcs[39;49;00m=\E[%i%d;%dr:[04m[32mct[39;49;00m=\E[3g:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=^J:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mds[39;49;00m=\E[2$~\r\E[1$}\E[K\E[$}:[04m[32mei[39;49;00m=\E[4l:[04m[32mfs[39;49;00m=\E[$}:[04m[32mho[39;49;00m=\E[H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mic[39;49;00m=\E[@:[04m[32mim[39;49;00m=\E[4h:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mis[39;49;00m=\E<\E F\E>\E[?1h\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h\E[1;24r\E[24;1H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:[04m[32mk6[39;49;00m=\E[17~:[04m[32mk7[39;49;00m=\E[18~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk8[39;49;00m=\E[19~:[04m[32mk9[39;49;00m=\E[20~:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\EOB:[04m[32mke[39;49;00m=\E[?1l\E>:[04m[32mkl[39;49;00m=\EOD:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkr[39;49;00m=\EOC:[04m[32mks[39;49;00m=\E[?1h\E=:[04m[32mku[39;49;00m=\EOA:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mme[39;49;00m=\E[m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mnw[39;49;00m=^M\ED:[04m[32mrc[39;49;00m=\E8:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[27m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32msf[39;49;00m=\ED:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mst[39;49;00m=\EH:[04m[32mta[39;49;00m=^I:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mts[39;49;00m=\E[2$~\E[1$}\E[1;%dH:[04m[32mue[39;49;00m=\E[24m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mvb[39;49;00m=200\E[?5h\E[?5l:[04m[32mve[39;49;00m=\E[?25h:[04m[32mvi[39;49;00m=\E[?25l:[04m[32mvs[39;49;00m=\E[?25h:[37m[39;49;00m
[37m[39;49;00m
[37m# (vt420: I removed :k0:, it collided with <kf10>.  I also restored[39;49;00m[37m[39;49;00m
[37m# a missing :sc: -- esr)[39;49;00m[37m[39;49;00m
[94mvt420[39;49;00m|[36mDEC VT420[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m*6[39;49;00m=\E[4~:[04m[32m@0[39;49;00m=\E[1~:[04m[32mRA[39;49;00m=\E[?7l:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mS5[39;49;00m=\E[?0;0r\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mSA[39;49;00m=\E[?7h:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mac[39;49;00m=``aaffggjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mae[39;49;00m=\E(B:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=\E(0:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcl[39;49;00m=\E[H\E[2J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=\E[B:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mi2[39;49;00m=\E[?67h\E[64;1"p:[04m[32mif[39;49;00m=/usr/share/tabset/vt300:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mim[39;49;00m=\E[4h:[04m[32mis[39;49;00m=\E[1;24r\E[24;1H:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:[04m[32mk3[39;49;00m=\EOR:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk4[39;49;00m=\EOS:[04m[32mk5[39;49;00m=\E[17~:[04m[32mk6[39;49;00m=\E[18~:[04m[32mk7[39;49;00m=\E[19~:[04m[32mk8[39;49;00m=\E[20~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk9[39;49;00m=\E[21~:[04m[32mk;[39;49;00m=\E[29~:[04m[32mkD[39;49;00m=\E[3~:[04m[32mkI[39;49;00m=\E[2~:[04m[32mkN[39;49;00m=\E[6~:[04m[32mkP[39;49;00m=\E[5~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mke[39;49;00m=\E>:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mks[39;49;00m=\E=:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmb[39;49;00m=\E[5m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mr3[39;49;00m=\E[?67h\E[64;1"p:[04m[32mrc[39;49;00m=\E8:[04m[32mrf[39;49;00m=/usr/share/tabset/vt300:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m..sa[39;49;00m=\E[0%?%p6%t;1%;%?%p2%t;4%;%?%p4%t;5%;%?%p1%p3%|%t;7%;m%?%p9%t\E(0%e\E(B%;:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[m:[04m[32msf[39;49;00m=\ED:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:[37m[39;49;00m
[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# DEC VT220 and up support DECUDK (user-defined keys).  DECUDK (i.e., pfx)[39;49;00m[37m[39;49;00m
[37m# takes two parameters, the key and the string.  Translating the key is[39;49;00m[37m[39;49;00m
[37m# straightforward (keys 1-5 are not defined on real terminals, though some[39;49;00m[37m[39;49;00m
[37m# emulators define these):[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m#               if (key < 16) then  value = key;[39;49;00m[37m[39;49;00m
[37m#               else if (key < 21) then value = key + 1; [39;49;00m[37m[39;49;00m
[37m#               else if (key < 25) then value = key + 2;[39;49;00m[37m[39;49;00m
[37m#               else if (key < 27) then value = key + 3;[39;49;00m[37m[39;49;00m
[37m#               else if (key < 30) then value = key + 4;[39;49;00m[37m[39;49;00m
[37m#               else value = key + 5;[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# The string must be the hexadecimal equivalent, e.g., "5052494E" for "PRINT". [39;49;00m[37m[39;49;00m
[37m# There's no provision in terminfo for emitting a string in this format, so the[39;49;00m[37m[39;49;00m
[37m# application has to know it.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[94mvt420pc[39;49;00m|[36mDEC VT420 w/PC keyboard[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m@7[39;49;00m=\E[4~:[04m[32mF1[39;49;00m=\E[23~:[04m[32mF2[39;49;00m=\E[24~:[04m[32mF3[39;49;00m=\E[11;2~:[04m[32mF4[39;49;00m=\E[12;2~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mF5[39;49;00m=\E[13;2~:[04m[32mF6[39;49;00m=\E[14;2~:[04m[32mF7[39;49;00m=\E[15;2~:[04m[32mF8[39;49;00m=\E[17;2~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mF9[39;49;00m=\E[18;2~:[04m[32mFA[39;49;00m=\E[19;2~:[04m[32mFB[39;49;00m=\E[20;2~:[04m[32mFC[39;49;00m=\E[21;2~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mFD[39;49;00m=\E[23;2~:[04m[32mFE[39;49;00m=\E[24;2~:[04m[32mFF[39;49;00m=\E[23~:[04m[32mFG[39;49;00m=\E[24~:[04m[32mFH[39;49;00m=\E[25~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mFI[39;49;00m=\E[26~:[04m[32mFJ[39;49;00m=\E[28~:[04m[32mFK[39;49;00m=\E[29~:[04m[32mFL[39;49;00m=\E[31~:[04m[32mFM[39;49;00m=\E[32~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mFN[39;49;00m=\E[33~:[04m[32mFO[39;49;00m=\E[34~:[04m[32mFP[39;49;00m=\E[35~:[04m[32mFQ[39;49;00m=\E[36~:[04m[32mFR[39;49;00m=\E[23;2~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mFS[39;49;00m=\E[24;2~:[04m[32mFT[39;49;00m=\E[25;2~:[04m[32mFU[39;49;00m=\E[26;2~:[04m[32mFV[39;49;00m=\E[28;2~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mFW[39;49;00m=\E[29;2~:[04m[32mFX[39;49;00m=\E[31;2~:[04m[32mFY[39;49;00m=\E[32;2~:[04m[32mFZ[39;49;00m=\E[33;2~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mFa[39;49;00m=\E[34;2~:[04m[32mFb[39;49;00m=\E[35;2~:[04m[32mFc[39;49;00m=\E[36;2~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mS6[39;49;00m=USR_TERM\072vt420pcdos\072:[04m[32mk1[39;49;00m=\E[11~:[04m[32mk2[39;49;00m=\E[12~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk3[39;49;00m=\E[13~:[04m[32mk4[39;49;00m=\E[14~:[04m[32mk5[39;49;00m=\E[15~:[04m[32mk6[39;49;00m=\E[17~:[04m[32mk7[39;49;00m=\E[18~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk8[39;49;00m=\E[19~:[04m[32mk9[39;49;00m=\E[20~:[04m[32mk;[39;49;00m=\E[21~:[04m[32mkD[39;49;00m=\177:[04m[32mkh[39;49;00m=\E[H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m..px[39;49;00m=\EP1;1|%?%{16}%p1%>%t%{0}%e%{21}%p1%>%t%{1}%e%{25}%p1%>%t%{2}%e%{27}%p1%>%t%{3}%e%{30}%p1%>%t%{4}%e%{5}%;%p1%+%d/%p2%s\E\:[04m[32mtc[39;49;00m=vt420:[37m[39;49;00m
[37m[39;49;00m
[94mvt420pcdos[39;49;00m|[36mDEC VT420 w/PC for DOS Merge[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mli[39;49;00m#[34m25[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mS1[39;49;00m=%?%p2%{19}%=%t\E\023\021%e%p2%{32}%<%t\E%p2%c%e%p2%{127}%=%t\E\177%e%p2%c%;:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mS4[39;49;00m=\E[?1;2r\E[34h:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mS5[39;49;00m=\E[?0;0r\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:[04m[32mS6@[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mme[39;49;00m=\E[m:[04m[32msa@[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt420pc:[37m[39;49;00m
[37m[39;49;00m
[94mvt420f[39;49;00m|[36mDEC VT420 with VT kbd; VT400 mode; F1-F5 used as Fkeys[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mF1[39;49;00m=\E[23~:[04m[32mF2[39;49;00m=\E[24~:[04m[32mF3[39;49;00m=\E[25~:[04m[32mF4[39;49;00m=\E[26~:[04m[32mF5[39;49;00m=\E[28~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mF6[39;49;00m=\E[29~:[04m[32mF7[39;49;00m=\E[31~:[04m[32mF8[39;49;00m=\E[32~:[04m[32mF9[39;49;00m=\E[33~:[04m[32mFA[39;49;00m=\E[34~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk1[39;49;00m=\E[11~:[04m[32mk2[39;49;00m=\E[12~:[04m[32mk3[39;49;00m=\E[13~:[04m[32mk4[39;49;00m=\E[14~:[04m[32mk5[39;49;00m=\E[15~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk6[39;49;00m=\E[17~:[04m[32mk7[39;49;00m=\E[18~:[04m[32mk8[39;49;00m=\E[19~:[04m[32mk9[39;49;00m=\E[20~:[04m[32mk;[39;49;00m=\E[21~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkD[39;49;00m=\177:[04m[32mkh[39;49;00m=\E[H:[04m[32ml1[39;49;00m=\EOP:[04m[32ml2[39;49;00m=\EOQ:[04m[32ml3[39;49;00m=\EOR:[04m[32ml4[39;49;00m=\EOS:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt420:[37m[39;49;00m
[37m[39;49;00m
[94mvt510[39;49;00m|[36mDEC VT510[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt420:[37m[39;49;00m
[94mvt510pc[39;49;00m|[36mDEC VT510 w/PC keyboard[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt420pc:[37m[39;49;00m
[94mvt510pcdos[39;49;00m|[36mDEC VT510 w/PC for DOS Merge[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mtc[39;49;00m=vt420pcdos:[37m[39;49;00m
[37m[39;49;00m
[37m# VT520/VT525[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# The VT520 is a monochrome text terminal capable of managing up to[39;49;00m[37m[39;49;00m
[37m# four independent sessions in the terminal.  It has multiple ANSI[39;49;00m[37m[39;49;00m
[37m# emulations (VT520, VT420, VT320, VT220, VT100, VT PCTerm, SCO Console)[39;49;00m[37m[39;49;00m
[37m# and ASCII emulations (WY160/60, PCTerm, 50/50+, 150/120, TVI 950,[39;49;00m[37m[39;49;00m
[37m# 925 910+, ADDS A2).  This terminfo data is for the ANSI emulations only.[39;49;00m[37m[39;49;00m
[37m#[39;49;00m[37m[39;49;00m
[37m# Terminal Set-Up is entered by pressing [F3], [Caps Lock]/[F3] or[39;49;00m[37m[39;49;00m
[37m# [Alt]/[Print Screen] depending upon which keyboard and which[39;49;00m[37m[39;49;00m
[37m# terminal mode is being used.  If Set-Up has been disabled or[39;49;00m[37m[39;49;00m
[37m# assigned to an unknown key, Set-Up may be entered by pressing[39;49;00m[37m[39;49;00m
[37m# [F3] as the first key after power up, regardless of keyboard type.[39;49;00m[37m[39;49;00m
[37m# (vt520: I added <rmam>/<smam> based on the init string, also :sc: -- esr)[39;49;00m[37m[39;49;00m
[37m# (untranslatable capabilities removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m
[94mvt520[39;49;00m|[36mDEC VT520[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m*6[39;49;00m=\E[4~:[04m[32m@0[39;49;00m=\E[1~:[04m[32mRA[39;49;00m=\E[?7l:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mS5[39;49;00m=\E[?0;0r\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mSA[39;49;00m=\E[?7h:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mac[39;49;00m=``aaffggjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mae[39;49;00m=\E(B:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=\E(0:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcl[39;49;00m=\E[H\E[2J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=\E[B:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mi2[39;49;00m=\E[?67h\E[64;1"p:[04m[32mif[39;49;00m=/usr/share/tabset/vt300:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mim[39;49;00m=\E[4h:[04m[32mis[39;49;00m=\E[1;24r\E[24;1H:[04m[32mk0[39;49;00m=\E[29~:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:[04m[32mk5[39;49;00m=\E[17~:[04m[32mk6[39;49;00m=\E[18~:[04m[32mk7[39;49;00m=\E[19~:[04m[32mk8[39;49;00m=\E[20~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk9[39;49;00m=\E[21~:[04m[32mk;[39;49;00m=\E[29~:[04m[32mkD[39;49;00m=\E[3~:[04m[32mkI[39;49;00m=\E[2~:[04m[32mkN[39;49;00m=\E[6~:[04m[32mkP[39;49;00m=\E[5~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mr3[39;49;00m=\E[?67h\E[64;1"p:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mrc[39;49;00m=\E8:[04m[32mrf[39;49;00m=/usr/share/tabset/vt300:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[m:[04m[32msf[39;49;00m=\ED:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:[37m[39;49;00m
[37m[39;49;00m
[37m# (vt525: I added <rmam>/<smam> based on the init string;[39;49;00m[37m[39;49;00m
[37m# removed :se:=\E[m, :ue:=\E[m, added :sc: -- esr)[39;49;00m[37m[39;49;00m
[37m# (untranslatable capabilities removed to fit entry within 1023 bytes)[39;49;00m[37m[39;49;00m
[94mvt525[39;49;00m|[36mDEC VT525[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mam[39;49;00m:[04m[32mmi[39;49;00m:[04m[32mxn[39;49;00m:[04m[32mxo[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mco[39;49;00m#[34m80[39;49;00m:[04m[32mli[39;49;00m#[34m24[39;49;00m:[04m[32mvt[39;49;00m#[34m3[39;49;00m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32m*6[39;49;00m=\E[4~:[04m[32m@0[39;49;00m=\E[1~:[04m[32mRA[39;49;00m=\E[?7l:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mS5[39;49;00m=\E[?0;0r\E>\E[?3l\E[?4l\E[?5l\E[?7h\E[?8h:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mSA[39;49;00m=\E[?7h:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mac[39;49;00m=``aaffggjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mae[39;49;00m=\E(B:[04m[32mal[39;49;00m=\E[L:[04m[32mas[39;49;00m=\E(0:[04m[32mbl[39;49;00m=^G:[04m[32mcd[39;49;00m=\E[J:[04m[32mce[39;49;00m=\E[K:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mcl[39;49;00m=\E[H\E[2J:[04m[32mcm[39;49;00m=\E[%i%d;%dH:[04m[32mcr[39;49;00m=^M:[04m[32mcs[39;49;00m=\E[%i%d;%dr:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mdc[39;49;00m=\E[P:[04m[32mdl[39;49;00m=\E[M:[04m[32mdo[39;49;00m=\E[B:[04m[32mei[39;49;00m=\E[4l:[04m[32mho[39;49;00m=\E[H:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mi2[39;49;00m=\E[?67h\E[64;1"p:[04m[32mif[39;49;00m=/usr/share/tabset/vt300:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mim[39;49;00m=\E[4h:[04m[32mis[39;49;00m=\E[1;24r\E[24;1H:[04m[32mk0[39;49;00m=\E[29~:[04m[32mk1[39;49;00m=\EOP:[04m[32mk2[39;49;00m=\EOQ:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk3[39;49;00m=\EOR:[04m[32mk4[39;49;00m=\EOS:[04m[32mk5[39;49;00m=\E[17~:[04m[32mk6[39;49;00m=\E[18~:[04m[32mk7[39;49;00m=\E[19~:[04m[32mk8[39;49;00m=\E[20~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mk9[39;49;00m=\E[21~:[04m[32mk;[39;49;00m=\E[29~:[04m[32mkD[39;49;00m=\E[3~:[04m[32mkI[39;49;00m=\E[2~:[04m[32mkN[39;49;00m=\E[6~:[04m[32mkP[39;49;00m=\E[5~:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mkb[39;49;00m=^H:[04m[32mkd[39;49;00m=\E[B:[04m[32mkl[39;49;00m=\E[D:[04m[32mkr[39;49;00m=\E[C:[04m[32mku[39;49;00m=\E[A:[04m[32mle[39;49;00m=^H:[04m[32mmb[39;49;00m=\E[5m:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mmd[39;49;00m=\E[1m:[04m[32mme[39;49;00m=\E[m:[04m[32mmr[39;49;00m=\E[7m:[04m[32mnd[39;49;00m=\E[C:[04m[32mr3[39;49;00m=\E[?67h\E[64;1"p:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mrc[39;49;00m=\E8:[04m[32mrf[39;49;00m=/usr/share/tabset/vt300:[04m[32msc[39;49;00m=\E7:[04m[32mse[39;49;00m=\E[m:[04m[32msf[39;49;00m=\ED:\[37m[39;49;00m
[37m^I[39;49;00m:[04m[32mso[39;49;00m=\E[7m:[04m[32msr[39;49;00m=\EM:[04m[32mta[39;49;00m=^I:[04m[32mue[39;49;00m=\E[m:[04m[32mup[39;49;00m=\E[A:[04m[32mus[39;49;00m=\E[4m:
