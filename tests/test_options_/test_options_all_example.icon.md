     1^I[37m############################################################################[39;49;00m$
     2^I[37m#[39;49;00m$
     3^I[37m#       File:     kaleid.icn[39;49;00m$
     4^I[37m#[39;49;00m$
     5^I[37m#       Subject:  Program to produce kaleidoscope[39;49;00m$
     6^I[37m#[39;49;00m$
     7^I[37m#       Author:   Stephen B. Wampler[39;49;00m$
     8^I[37m#[39;49;00m$
     9^I[37m#       Date:     May 2, 2001[39;49;00m$
    10^I[37m#[39;49;00m$
    11^I[37m############################################################################[39;49;00m$
    12^I[37m#[39;49;00m$
    13^I[37m#   This file is in the public domain.[39;49;00m$
    14^I[37m#[39;49;00m$
    15^I[37m############################################################################[39;49;00m$
    16^I[37m#[39;49;00m$
    17^I[37m#    Lots of options, most easily set by with the interface after[39;49;00m$
    18^I[37m#    startup.  The only one that isn't set that way is -wn where 'n' is[39;49;00m$
    19^I[37m#    the size of the kaleidoscope window (default is 600 square).[39;49;00m$
    20^I[37m#[39;49;00m$
    21^I[37m#    Terminology (and options):[39;49;00m$
    22^I[37m#[39;49;00m$
    23^I[37m#       Window_size (-wN): How big of a display window to use.[39;49;00m$
    24^I[37m#           At the current time, this can only be set via a[39;49;00m$
    25^I[37m#           command line argument.[39;49;00m$
    26^I[37m#[39;49;00m$
    27^I[37m#       Density (-dN): How many circles per octant to keep on display[39;49;00m$
    28^I[37m#           at any one time.  There is NO LIMIT to the density.[39;49;00m$
    29^I[37m#[39;49;00m$
    30^I[37m#       Duration (-lN): How long to keep drawing circles (measured in[39;49;00m$
    31^I[37m#           in circles) once the density is reached.  There is NO LIMIT[39;49;00m$
    32^I[37m#           to the duration.[39;49;00m$
    33^I[37m#[39;49;00m$
    34^I[37m#       MaxRadius (-MN): Maximum radius of any circle.[39;49;00m$
    35^I[37m#[39;49;00m$
    36^I[37m#       MinRadius (-mN): Preferred minimum radius.  Circles with centers[39;49;00m$
    37^I[37m#           near the edge have their radii forced down to fit entirely[39;49;00m$
    38^I[37m#           on the display[39;49;00m$
    39^I[37m#[39;49;00m$
    40^I[37m#       MaxOffset (-XN): Maximum offset from center of display (may wrap).[39;49;00m$
    41^I[37m#[39;49;00m$
    42^I[37m#       MinOffset (-xN): Minimum offset[39;49;00m$
    43^I[37m#[39;49;00m$
    44^I[37m#       Skew (-sN): Shift probability of placing a circle at a 'typical'[39;49;00m$
    45^I[37m#           offset.[39;49;00m$
    46^I[37m#[39;49;00m$
    47^I[37m#       Fill (-F): Turns off filling the circles.[39;49;00m$
    48^I[37m#[39;49;00m$
    49^I[37m#       Clear (-C): After the duration, reduces density back to 0 before[39;49;00m$
    50^I[37m#           quitting.[39;49;00m$
    51^I[37m#[39;49;00m$
    52^I[37m#       Random Seed: (-rN): Sets the random number seed.[39;49;00m$
    53^I[37m#[39;49;00m$
    54^I[37m# Thanks to Jon Lipp for help on using vidgets, and to Mary Camaron[39;49;00m$
    55^I[37m#   for her Interface Builder.[39;49;00m$
    56^I[37m#[39;49;00m$
    57^I[37m############################################################################[39;49;00m$
    58^I[37m#[39;49;00m$
    59^I[37m#  Requires:  Version 9 graphics[39;49;00m$
    60^I[37m#[39;49;00m$
    61^I[37m############################################################################[39;49;00m$
    62^I[37m#[39;49;00m$
    63^I[37m#  Links:  vidgets, vslider, vtext, vbuttons, vradio, wopen, xcompat[39;49;00m$
    64^I[37m#[39;49;00m$
    65^I[37m############################################################################[39;49;00m$
    66^I$
    67^I[34mlink[39;49;00m vidgets$
    68^I[34mlink[39;49;00m vslider$
    69^I[34mlink[39;49;00m vtext$
    70^I[34mlink[39;49;00m vbuttons$
    71^I[34mlink[39;49;00m vradio$
    72^I[34mlink[39;49;00m wopen$
    73^I[34mlink[39;49;00m xcompat$
    74^I$
    75^I[34mglobal[39;49;00m Clear, fill, duration, density, maxoff, minoff$
    76^I[34mglobal[39;49;00m maxradius, minradius, r_seed, skew, win_size, mid_win$
    77^I[34mglobal[39;49;00m root, check1, mainwin, use_dialog$
    78^I[34mglobal[39;49;00m draw_circle$
    79^I$
    80^I[34mglobal[39;49;00m du_v, de_v, rs_v, sk_v$
    81^I$
    82^I[34mprocedure[39;49;00m [32mmain[39;49;00m ([31margs[39;49;00m)$
    83^I$
    84^I   draw_circle := [32mDrawCircle[39;49;00m$
    85^I$
    86^I   init_globs()$
    87^I   process_args([32margs[39;49;00m)$
    88^I$
    89^I   [34mif[39;49;00m \use_dialog [34mthen[39;49;00m {        [37m# have vidgets, so use them for args.[39;49;00m$
    90^I      mainwin := WOpen([33m"label=Kaleidoscope"[39;49;00m, [33m"width=404"[39;49;00m, [33m"height=313"[39;49;00m, $
    91^I                       [33m"font=6x12"[39;49;00m) |$
    92^I                 [32mstop[39;49;00m ([33m"bad mainwin"[39;49;00m)$
    93^I      root := ui (mainwin)$
    94^I      GetEvents (root, quit)$
    95^I      }$
    96^I   [34melse[39;49;00m {                       [37m# just rely on command line arguments[39;49;00m$
    97^I      kaleidoscope(r_seed)$
    98^I      }$
    99^I$
   100^I[34mend[39;49;00m$
   101^I$
   102^I[34mprocedure[39;49;00m [32minit_globs[39;49;00m()$
   103^I$
   104^I   duration := [34m500[39;49;00m                    [37m# set default characteristics[39;49;00m$
   105^I   density := [34m30[39;49;00m$
   106^I   win_size := [34m600[39;49;00m$
   107^I   minoff := [34m1[39;49;00m$
   108^I   maxradius := [34m150[39;49;00m$
   109^I   minradius := [34m1[39;49;00m$
   110^I   skew := [34m1[39;49;00m$
   111^I   fill := [33m"On"[39;49;00m$
   112^I   draw_circle := [32mFillCircle[39;49;00m$
   113^I   Clear := [33m"Off"[39;49;00m$
   114^I   r_seed := [32mmap[39;49;00m([33m"HhMmYy"[39;49;00m, [33m"Hh:Mm:Yy"[39;49;00m, [34m&clock[39;49;00m)$
   115^I   [37m# See if the Vidget library is available or not[39;49;00m$
   116^I   [34mif[39;49;00m \VSet [34mthen[39;49;00m use_dialog := [33m"yes"[39;49;00m$
   117^I            [34melse[39;49;00m use_dialog := [34m&null[39;49;00m$
   118^I$
   119^I[34mend[39;49;00m$
   120^I$
   121^I[34mprocedure[39;49;00m [32mprocess_args[39;49;00m([31margs[39;49;00m)$
   122^I   [34mlocal[39;49;00m arg$
   123^I$
   124^I   [37m# really only needed if you don't use the dialog box[39;49;00m$
   125^I   [34mevery[39;49;00m arg := ![32margs[39;49;00m [34mdo[39;49;00m [34mcase[39;49;00m arg[[34m1[39;49;00m+:[34m2[39;49;00m] [34mof[39;49;00m {$
   126^I      [33m"-w"[39;49;00m : win_size := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])       [37m# window size[39;49;00m$
   127^I      [33m"-d"[39;49;00m : density := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])        [37m# density of circles[39;49;00m$
   128^I      [33m"-l"[39;49;00m : duration := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])       [37m# duration[39;49;00m$
   129^I      [33m"-M"[39;49;00m : maxradius := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])      [37m# maximum radius[39;49;00m$
   130^I      [33m"-m"[39;49;00m : minradius := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])      [37m# minimum radius[39;49;00m$
   131^I      [33m"-X"[39;49;00m : maxoff := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])         [37m# maximum offset[39;49;00m$
   132^I      [33m"-x"[39;49;00m : minoff := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])         [37m# minimum offset[39;49;00m$
   133^I      [33m"-s"[39;49;00m : skew := [32mnumeric[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])           [37m# set skewedness[39;49;00m$
   134^I      [33m"-F"[39;49;00m : fill := [34m&null[39;49;00m                       [37m# turn off fill[39;49;00m$
   135^I      [33m"-C"[39;49;00m : Clear := [33m"yes"[39;49;00m                      [37m# turn on clear mode[39;49;00m$
   136^I      [33m"-r"[39;49;00m : r_seed := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])         [37m# random seed[39;49;00m$
   137^I      [33m"-h"[39;49;00m : [32mstop[39;49;00m([33m"usage: kal [-wn] [-dn] [-ln] [-Mn] [-mn] [-Xn] [-xn] _[39;49;00m$
   138^I[33m                     [-sn] [-F] [-C] [-rn]"[39;49;00m)$
   139^I      }$
   140^I   [37m# adjust parameters that depend on the window size...[39;49;00m$
   141^I   mid_win := win_size/[34m2[39;49;00m$
   142^I   maxoff := win_size[34m-1[39;49;00m$
   143^I[34mend[39;49;00m$
   144^I$
   145^I[37m# Lorraine Callahan's kaleidoscope program, translated into icon.[39;49;00m$
   146^I[37m#  (some of the things she did were too sophisticated for me[39;49;00m$
   147^I[37m#   to spend time to figure out, so the output is square instead of[39;49;00m$
   148^I[37m#   round), and I use 'xor' to draw instead of writing to separate[39;49;00m$
   149^I[37m#   bit planes.[39;49;00m$
   150^I$
   151^I[34mglobal[39;49;00m putcircle, clrcircle$
   152^I$
   153^I[34mprocedure[39;49;00m [32mkaleidoscope[39;49;00m([31mr[39;49;00m)$
   154^I   [34mlocal[39;49;00m colors$
   155^I$
   156^I   [37m# What colors to use?  This can be changed to whatever![39;49;00m$
   157^I   colors := [[33m"red"[39;49;00m,[33m"green"[39;49;00m,[33m"blue"[39;49;00m,[33m"cyan"[39;49;00m,[33m"magenta"[39;49;00m,[33m"yellow"[39;49;00m]$
   158^I$
   159^I   [34m&window[39;49;00m := WOpen([33m"label=Kaleidoscope: 'q' quits"[39;49;00m, [33m"width="[39;49;00m||win_size,$
   160^I                                  [33m"height="[39;49;00m||win_size, [33m"bg=black"[39;49;00m)$
   161^I   [32mWAttrib[39;49;00m([33m"drawop=xor"[39;49;00m)$
   162^I$
   163^I   [37m# Create two *indentical* sequences of circles, one to use when[39;49;00m$
   164^I   [37m#   when drawing, one for erasing.  (Since 'xor' is used to[39;49;00m$
   165^I   [37m#   place them, these both just draw the circles!)[39;49;00m$
   166^I$
   167^I   putcircle := [34mcreate[39;49;00m {                [37m# draws sequence of circles[39;49;00m$
   168^I      [34m&random[39;49;00m :=: r$
   169^I      |{$
   170^I       [32mFg[39;49;00m(?colors)$
   171^I       outcircle()$
   172^I       [34m&random[39;49;00m <-> r$
   173^I       }$
   174^I      }$
   175^I$
   176^I   clrcircle := [34mcreate[39;49;00m {                [37m# erases sequence of circles[39;49;00m$
   177^I      [34m&random[39;49;00m :=: r$
   178^I      |{$
   179^I       [32mFg[39;49;00m(?colors)$
   180^I       outcircle()$
   181^I       [34m&random[39;49;00m <-> r$
   182^I       }$
   183^I      }$
   184^I$
   185^I   [34mevery[39;49;00m [34m1[39;49;00m [34mto[39;49;00m density [34mdo[39;49;00m @putcircle     [37m# fill screen to density[39;49;00m$
   186^I$
   187^I   [34mevery[39;49;00m [34m1[39;49;00m [34mto[39;49;00m duration [34mdo[39;49;00m {             [37m# maintain steady state[39;49;00m$
   188^I      @putcircle$
   189^I      @clrcircle$
   190^I      [34mif[39;49;00m *[32mPending[39;49;00m([34m&window[39;49;00m) > [34m0[39;49;00m [34mthen[39;49;00m [34mbreak[39;49;00m$
   191^I      }$
   192^I$
   193^I   [34mevery[39;49;00m (Clear == [33m"On"[39;49;00m) & [34m1[39;49;00m [34mto[39;49;00m density [34mdo[39;49;00m @clrcircle$
   194^I$
   195^I   [32mclose[39;49;00m([34m&window[39;49;00m)$
   196^I[34mend[39;49;00m$
   197^I$
   198^I$
   199^I[34mprocedure[39;49;00m [32moutcircle[39;49;00m()                   [37m# select a circle at random,[39;49;00m$
   200^I[34mlocal[39;49;00m radius, xoff, yoff                [37m#  draw it in kaleidoscopic form[39;49;00m$
   201^I$
   202^I        [37m# get a random center point and radius[39;49;00m$
   203^I   xoff := (?(maxoff - minoff) + minoff) % mid_win$
   204^I   yoff := (?(maxoff - minoff) + minoff) % mid_win$
   205^I   radius := ?[34m0[39;49;00m ^ skew$
   206^I        [37m# force radius to 'fit'[39;49;00m$
   207^I   radius := ((maxradius-minradius) * radius + minradius) %$
   208^I             (mid_win - ((xoff < yoff)|xoff))$
   209^I$
   210^I        [37m# put into all 8 octants[39;49;00m$
   211^I   draw_circle(mid_win+xoff, mid_win+yoff, radius)$
   212^I   draw_circle(mid_win+xoff, mid_win-yoff, radius)$
   213^I   draw_circle(mid_win-xoff, mid_win+yoff, radius)$
   214^I   draw_circle(mid_win-xoff, mid_win-yoff, radius)$
   215^I$
   216^I   draw_circle(mid_win+yoff, mid_win+xoff, radius)$
   217^I   draw_circle(mid_win+yoff, mid_win-xoff, radius)$
   218^I   draw_circle(mid_win-yoff, mid_win+xoff, radius)$
   219^I   draw_circle(mid_win-yoff, mid_win-xoff, radius)$
   220^I$
   221^I   [34mreturn[39;49;00m$
   222^I[34mend[39;49;00m$
   223^I$
   224^I$
   225^I[37m############################################################################[39;49;00m$
   226^I[37m#[39;49;00m$
   227^I[37m#   Vidget-based user interface -- developed originally using Mary[39;49;00m$
   228^I[37m#       Camaron's XIB program.  Don't expect this to be very readable -[39;49;00m$
   229^I[37m#       you should have to play with it![39;49;00m$
   230^I[37m#[39;49;00m$
   231^I[37m############################################################################[39;49;00m$
   232^I[34mprocedure[39;49;00m [32mui[39;49;00m ([31mwin[39;49;00m)$
   233^I   [34mlocal[39;49;00m cv1, cv2, cv3, cv4$
   234^I   [34mlocal[39;49;00m $
   235^I         radio_button2, $
   236^I         radio_button1, $
   237^I         text_input6, $
   238^I         text_input5, $
   239^I         slider4, $
   240^I         slider3, $
   241^I         text_input4, $
   242^I         text_input3, $
   243^I         slider2, $
   244^I         slider1 $
   245^I$
   246^I   /win := WOpen([33m"label=ui"[39;49;00m, [33m"width=404"[39;49;00m, [33m"height=313"[39;49;00m, [33m"font=6x12"[39;49;00m) | $
   247^I           [32mstop[39;49;00m ([33m"bad win"[39;49;00m)$
   248^I   root := Vroot_frame (win)$
   249^I$
   250^I   VInsert (root, Vmessage(win, win_size/[34m2[39;49;00m), [34m168[39;49;00m, [34m98[39;49;00m)$
   251^I   VInsert (root, Vmessage(win, [33m"1"[39;49;00m), [34m108[39;49;00m, [34m97[39;49;00m)$
   252^I$
   253^I   VInsert (root, sk_v := Vtext(win,[33m"Skew:\\=1"[39;49;00m,get_skew,,[34m6[39;49;00m), [34m280[39;49;00m, [34m39[39;49;00m)$
   254^I$
   255^I   VInsert (root, du_v := Vtext(win, [33m"Duration:\\="[39;49;00m||duration, get_duration,,[34m9[39;49;00m),$
   256^I                [34m237[39;49;00m, [34m15[39;49;00m)$
   257^I$
   258^I   VInsert (root, Vmessage(win, [33m"Clear at end?"[39;49;00m), [34m232[39;49;00m, [34m145[39;49;00m)$
   259^I   VInsert (root, Vmessage(win, [33m"Fill?"[39;49;00m), [34m105[39;49;00m, [34m142[39;49;00m)$
   260^I   VInsert (root, Vmessage(win,[33m"Quit?"[39;49;00m), [34m267[39;49;00m, [34m259[39;49;00m)$
   261^I   VInsert (root, Vmessage(win,[33m"Display it?"[39;49;00m), [34m26[39;49;00m, [34m260[39;49;00m)$
   262^I$
   263^I   VInsert (root, Vcheckbox(win, do_quit, [33m"check2"[39;49;00m,[34m20[39;49;00m), [34m305[39;49;00m, [34m255[39;49;00m, [34m20[39;49;00m, [34m20[39;49;00m)$
   264^I$
   265^I   VInsert (root, check1:=Vcheckbox(win, do_display, [33m"check1"[39;49;00m,[34m20[39;49;00m),$
   266^I                [34m106[39;49;00m, [34m258[39;49;00m, [34m20[39;49;00m, [34m20[39;49;00m)$
   267^I$
   268^I   radio_button2 := Vradio_buttons (win, [[33m"On"[39;49;00m, [33m"Off"[39;49;00m], get_clear, , V_CIRCLE)$
   269^I   VSet(radio_button2,Clear)$
   270^I   VInsert (root, radio_button2, [34m253[39;49;00m, [34m165[39;49;00m)$
   271^I$
   272^I   radio_button1 := Vradio_buttons (win, [[33m"On"[39;49;00m, [33m"Off"[39;49;00m], get_fill, , V_CIRCLE)$
   273^I   VSet(radio_button1,fill)$
   274^I   VInsert (root, radio_button1, [34m99[39;49;00m, [34m165[39;49;00m)$
   275^I$
   276^I   cv1 := Vcoupler()$
   277^I   VAddClient(cv1, get_max_offset)$
   278^I   text_input6 := Vtext (win, [33m"Max Offset:\\="[39;49;00m||(win_size[34m-1[39;49;00m), cv1, , [34m3[39;49;00m)$
   279^I   VAddClient(cv1, text_input6)$
   280^I   slider4 := Vhoriz_slider (win, cv1, [33m"slider4"[39;49;00m, [34m70[39;49;00m, [34m12[39;49;00m, [34m0[39;49;00m,$
   281^I                         win_size[34m-1[39;49;00m, win_size[34m-1[39;49;00m, )$
   282^I   VAddClient(cv1, slider4)$
   283^I   VInsert (root, text_input6, [34m196[39;49;00m, [34m103[39;49;00m)$
   284^I   VInsert (root, slider4, [34m306[39;49;00m, [34m106[39;49;00m)$
   285^I$
   286^I   cv2 := Vcoupler()$
   287^I   VAddClient(cv2, get_min_offset)$
   288^I   text_input5 := Vtext (win, [33m"Min Offset\\=1"[39;49;00m, cv2, , [34m3[39;49;00m)$
   289^I   VAddClient(cv2, text_input5)$
   290^I   slider3 := Vhoriz_slider (win, cv2, [33m"slider3"[39;49;00m, [34m70[39;49;00m, [34m12[39;49;00m, [34m1[39;49;00m, win_size[34m-1[39;49;00m, [34m1[39;49;00m, )$
   291^I   VAddClient(cv2, slider3)$
   292^I   VInsert (root, text_input5, [34m201[39;49;00m, [34m80[39;49;00m)$
   293^I   VInsert (root, slider3, [34m307[39;49;00m, [34m82[39;49;00m)$
   294^I$
   295^I   cv3 := Vcoupler()$
   296^I   VAddClient(cv3, get_max_radius)$
   297^I   text_input4 := Vtext (win, [33m"Max Radius\\="[39;49;00m||(win_size/[34m4[39;49;00m), cv3, , [34m3[39;49;00m)$
   298^I   VAddClient(cv3, text_input4)$
   299^I   slider2 := Vhoriz_slider (win, cv3, [33m"slider2"[39;49;00m, [34m70[39;49;00m, [34m12[39;49;00m, [34m1[39;49;00m, win_size/[34m2[39;49;00m,$
   300^I         win_size/[34m4[39;49;00m, )$
   301^I   VAddClient(cv3, slider2)$
   302^I   VInsert (root, text_input4, [34m10[39;49;00m, [34m104[39;49;00m)$
   303^I   VInsert (root, slider2, [34m110[39;49;00m, [34m108[39;49;00m)$
   304^I$
   305^I   cv4 := Vcoupler()$
   306^I   VAddClient(cv4, get_min_radius)$
   307^I   text_input3 := Vtext (win, [33m"Min Radius\\=1"[39;49;00m, cv4, , [34m3[39;49;00m)$
   308^I   VAddClient(cv4, text_input3)$
   309^I   slider1 := Vhoriz_slider (win, cv4, [33m"slider1"[39;49;00m, [34m70[39;49;00m, [34m12[39;49;00m, [34m1[39;49;00m, win_size/[34m2[39;49;00m, [34m1[39;49;00m, )$
   310^I   VAddClient(cv4, slider1)$
   311^I   VInsert (root, text_input3, [34m10[39;49;00m, [34m81[39;49;00m)$
   312^I   VInsert (root, slider1, [34m110[39;49;00m, [34m84[39;49;00m)$
   313^I$
   314^I   VInsert (root, rs_v := Vtext(win,[33m"Random Seed:\\="[39;49;00m||r_seed, get_random,, [34m11[39;49;00m),$
   315^I              [34m30[39;49;00m, [34m41[39;49;00m)$
   316^I   VInsert (root, de_v := Vtext(win,[33m"Density:\\="[39;49;00m||density, get_density,,[34m8[39;49;00m),$
   317^I              [34m71[39;49;00m, [34m16[39;49;00m)$
   318^I$
   319^I   VResize (root)$
   320^I   [34mreturn[39;49;00m root$
   321^I[34mend[39;49;00m$
   322^I$
   323^I[34mprocedure[39;49;00m [32mget_skew[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   324^I   skew := value$
   325^I[34mend[39;49;00m$
   326^I$
   327^I[34mprocedure[39;49;00m [32mget_duration[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   328^I   duration := value$
   329^I[34mend[39;49;00m$
   330^I$
   331^I[34mprocedure[39;49;00m [32mdo_quit[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   332^I   [32mstop[39;49;00m()$
   333^I[34mend[39;49;00m$
   334^I$
   335^I[34mprocedure[39;49;00m [32mdo_display[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   336^I   r_seed   := [32mnumeric[39;49;00m(rs_v[34m.[39;49;00mdata)$
   337^I   duration := [32minteger[39;49;00m(du_v[34m.[39;49;00mdata)$
   338^I   density  := [32minteger[39;49;00m(de_v[34m.[39;49;00mdata)$
   339^I   skew     := [32minteger[39;49;00m(sk_v[34m.[39;49;00mdata)$
   340^I   kaleidoscope(r_seed)$
   341^I   wit[34m.[39;49;00mcallback[34m.[39;49;00mvalue := [34m&null[39;49;00m$
   342^I   VDraw(check1)$
   343^I[34mend[39;49;00m$
   344^I$
   345^I[34mprocedure[39;49;00m [32mget_clear[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   346^I   Clear := value$
   347^I[34mend[39;49;00m$
   348^I$
   349^I[34mprocedure[39;49;00m [32mget_fill[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   350^I   fill := value$
   351^I   [34mif[39;49;00m fill == [33m"Off"[39;49;00m [34mthen[39;49;00m draw_circle := [32mDrawCircle[39;49;00m$
   352^I   [34melse[39;49;00m draw_circle := [32mFillCircle[39;49;00m$
   353^I[34mend[39;49;00m$
   354^I$
   355^I[34mprocedure[39;49;00m [32mget_max_offset[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   356^I   maxoff := value$
   357^I[34mend[39;49;00m$
   358^I$
   359^I[34mprocedure[39;49;00m [32mget_min_offset[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   360^I   minoff := value$
   361^I[34mend[39;49;00m$
   362^I$
   363^I[34mprocedure[39;49;00m [32mget_max_radius[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   364^I   maxradius := value$
   365^I[34mend[39;49;00m$
   366^I$
   367^I[34mprocedure[39;49;00m [32mget_min_radius[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   368^I   minradius := value$
   369^I[34mend[39;49;00m$
   370^I$
   371^I[34mprocedure[39;49;00m [32mget_random[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   372^I   r_seed := [32minteger[39;49;00m(value)$
   373^I[34mend[39;49;00m$
   374^I$
   375^I[34mprocedure[39;49;00m [32mget_density[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   376^I   density := [32minteger[39;49;00m(value)$
   377^I[34mend[39;49;00m$
   378^I$
   379^I[34mprocedure[39;49;00m [32mquit[39;49;00m([31me[39;49;00m)$
   380^I   [34mif[39;49;00m e === [33m"q"[39;49;00m [34mthen[39;49;00m [32mstop[39;49;00m ([33m"Exiting Kaleidoscope"[39;49;00m)$
   381^I[34mend[39;49;00m$
