[37m############################################################################[39;49;00m$
[37m#[39;49;00m$
[37m#       File:     kaleid.icn[39;49;00m$
[37m#[39;49;00m$
[37m#       Subject:  Program to produce kaleidoscope[39;49;00m$
[37m#[39;49;00m$
[37m#       Author:   Stephen B. Wampler[39;49;00m$
[37m#[39;49;00m$
[37m#       Date:     May 2, 2001[39;49;00m$
[37m#[39;49;00m$
[37m############################################################################[39;49;00m$
[37m#[39;49;00m$
[37m#   This file is in the public domain.[39;49;00m$
[37m#[39;49;00m$
[37m############################################################################[39;49;00m$
[37m#[39;49;00m$
[37m#    Lots of options, most easily set by with the interface after[39;49;00m$
[37m#    startup.  The only one that isn't set that way is -wn where 'n' is[39;49;00m$
[37m#    the size of the kaleidoscope window (default is 600 square).[39;49;00m$
[37m#[39;49;00m$
[37m#    Terminology (and options):[39;49;00m$
[37m#[39;49;00m$
[37m#       Window_size (-wN): How big of a display window to use.[39;49;00m$
[37m#           At the current time, this can only be set via a[39;49;00m$
[37m#           command line argument.[39;49;00m$
[37m#[39;49;00m$
[37m#       Density (-dN): How many circles per octant to keep on display[39;49;00m$
[37m#           at any one time.  There is NO LIMIT to the density.[39;49;00m$
[37m#[39;49;00m$
[37m#       Duration (-lN): How long to keep drawing circles (measured in[39;49;00m$
[37m#           in circles) once the density is reached.  There is NO LIMIT[39;49;00m$
[37m#           to the duration.[39;49;00m$
[37m#[39;49;00m$
[37m#       MaxRadius (-MN): Maximum radius of any circle.[39;49;00m$
[37m#[39;49;00m$
[37m#       MinRadius (-mN): Preferred minimum radius.  Circles with centers[39;49;00m$
[37m#           near the edge have their radii forced down to fit entirely[39;49;00m$
[37m#           on the display[39;49;00m$
[37m#[39;49;00m$
[37m#       MaxOffset (-XN): Maximum offset from center of display (may wrap).[39;49;00m$
[37m#[39;49;00m$
[37m#       MinOffset (-xN): Minimum offset[39;49;00m$
[37m#[39;49;00m$
[37m#       Skew (-sN): Shift probability of placing a circle at a 'typical'[39;49;00m$
[37m#           offset.[39;49;00m$
[37m#[39;49;00m$
[37m#       Fill (-F): Turns off filling the circles.[39;49;00m$
[37m#[39;49;00m$
[37m#       Clear (-C): After the duration, reduces density back to 0 before[39;49;00m$
[37m#           quitting.[39;49;00m$
[37m#[39;49;00m$
[37m#       Random Seed: (-rN): Sets the random number seed.[39;49;00m$
[37m#[39;49;00m$
[37m# Thanks to Jon Lipp for help on using vidgets, and to Mary Camaron[39;49;00m$
[37m#   for her Interface Builder.[39;49;00m$
[37m#[39;49;00m$
[37m############################################################################[39;49;00m$
[37m#[39;49;00m$
[37m#  Requires:  Version 9 graphics[39;49;00m$
[37m#[39;49;00m$
[37m############################################################################[39;49;00m$
[37m#[39;49;00m$
[37m#  Links:  vidgets, vslider, vtext, vbuttons, vradio, wopen, xcompat[39;49;00m$
[37m#[39;49;00m$
[37m############################################################################[39;49;00m$
$
[34mlink[39;49;00m vidgets$
[34mlink[39;49;00m vslider$
[34mlink[39;49;00m vtext$
[34mlink[39;49;00m vbuttons$
[34mlink[39;49;00m vradio$
[34mlink[39;49;00m wopen$
[34mlink[39;49;00m xcompat$
$
[34mglobal[39;49;00m Clear, fill, duration, density, maxoff, minoff$
[34mglobal[39;49;00m maxradius, minradius, r_seed, skew, win_size, mid_win$
[34mglobal[39;49;00m root, check1, mainwin, use_dialog$
[34mglobal[39;49;00m draw_circle$
$
[34mglobal[39;49;00m du_v, de_v, rs_v, sk_v$
$
[34mprocedure[39;49;00m [32mmain[39;49;00m ([31margs[39;49;00m)$
$
   draw_circle := [32mDrawCircle[39;49;00m$
$
   init_globs()$
   process_args([32margs[39;49;00m)$
$
   [34mif[39;49;00m \use_dialog [34mthen[39;49;00m {        [37m# have vidgets, so use them for args.[39;49;00m$
      mainwin := WOpen([33m"label=Kaleidoscope"[39;49;00m, [33m"width=404"[39;49;00m, [33m"height=313"[39;49;00m, $
                       [33m"font=6x12"[39;49;00m) |$
                 [32mstop[39;49;00m ([33m"bad mainwin"[39;49;00m)$
      root := ui (mainwin)$
      GetEvents (root, quit)$
      }$
   [34melse[39;49;00m {                       [37m# just rely on command line arguments[39;49;00m$
      kaleidoscope(r_seed)$
      }$
$
[34mend[39;49;00m$
$
[34mprocedure[39;49;00m [32minit_globs[39;49;00m()$
$
   duration := [34m500[39;49;00m                    [37m# set default characteristics[39;49;00m$
   density := [34m30[39;49;00m$
   win_size := [34m600[39;49;00m$
   minoff := [34m1[39;49;00m$
   maxradius := [34m150[39;49;00m$
   minradius := [34m1[39;49;00m$
   skew := [34m1[39;49;00m$
   fill := [33m"On"[39;49;00m$
   draw_circle := [32mFillCircle[39;49;00m$
   Clear := [33m"Off"[39;49;00m$
   r_seed := [32mmap[39;49;00m([33m"HhMmYy"[39;49;00m, [33m"Hh:Mm:Yy"[39;49;00m, [34m&clock[39;49;00m)$
   [37m# See if the Vidget library is available or not[39;49;00m$
   [34mif[39;49;00m \VSet [34mthen[39;49;00m use_dialog := [33m"yes"[39;49;00m$
            [34melse[39;49;00m use_dialog := [34m&null[39;49;00m$
$
[34mend[39;49;00m$
$
[34mprocedure[39;49;00m [32mprocess_args[39;49;00m([31margs[39;49;00m)$
   [34mlocal[39;49;00m arg$
$
   [37m# really only needed if you don't use the dialog box[39;49;00m$
   [34mevery[39;49;00m arg := ![32margs[39;49;00m [34mdo[39;49;00m [34mcase[39;49;00m arg[[34m1[39;49;00m+:[34m2[39;49;00m] [34mof[39;49;00m {$
      [33m"-w"[39;49;00m : win_size := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])       [37m# window size[39;49;00m$
      [33m"-d"[39;49;00m : density := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])        [37m# density of circles[39;49;00m$
      [33m"-l"[39;49;00m : duration := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])       [37m# duration[39;49;00m$
      [33m"-M"[39;49;00m : maxradius := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])      [37m# maximum radius[39;49;00m$
      [33m"-m"[39;49;00m : minradius := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])      [37m# minimum radius[39;49;00m$
      [33m"-X"[39;49;00m : maxoff := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])         [37m# maximum offset[39;49;00m$
      [33m"-x"[39;49;00m : minoff := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])         [37m# minimum offset[39;49;00m$
      [33m"-s"[39;49;00m : skew := [32mnumeric[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])           [37m# set skewedness[39;49;00m$
      [33m"-F"[39;49;00m : fill := [34m&null[39;49;00m                       [37m# turn off fill[39;49;00m$
      [33m"-C"[39;49;00m : Clear := [33m"yes"[39;49;00m                      [37m# turn on clear mode[39;49;00m$
      [33m"-r"[39;49;00m : r_seed := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])         [37m# random seed[39;49;00m$
      [33m"-h"[39;49;00m : [32mstop[39;49;00m([33m"usage: kal [-wn] [-dn] [-ln] [-Mn] [-mn] [-Xn] [-xn] _[39;49;00m$
[33m                     [-sn] [-F] [-C] [-rn]"[39;49;00m)$
      }$
   [37m# adjust parameters that depend on the window size...[39;49;00m$
   mid_win := win_size/[34m2[39;49;00m$
   maxoff := win_size[34m-1[39;49;00m$
[34mend[39;49;00m$
$
[37m# Lorraine Callahan's kaleidoscope program, translated into icon.[39;49;00m$
[37m#  (some of the things she did were too sophisticated for me[39;49;00m$
[37m#   to spend time to figure out, so the output is square instead of[39;49;00m$
[37m#   round), and I use 'xor' to draw instead of writing to separate[39;49;00m$
[37m#   bit planes.[39;49;00m$
$
[34mglobal[39;49;00m putcircle, clrcircle$
$
[34mprocedure[39;49;00m [32mkaleidoscope[39;49;00m([31mr[39;49;00m)$
   [34mlocal[39;49;00m colors$
$
   [37m# What colors to use?  This can be changed to whatever![39;49;00m$
   colors := [[33m"red"[39;49;00m,[33m"green"[39;49;00m,[33m"blue"[39;49;00m,[33m"cyan"[39;49;00m,[33m"magenta"[39;49;00m,[33m"yellow"[39;49;00m]$
$
   [34m&window[39;49;00m := WOpen([33m"label=Kaleidoscope: 'q' quits"[39;49;00m, [33m"width="[39;49;00m||win_size,$
                                  [33m"height="[39;49;00m||win_size, [33m"bg=black"[39;49;00m)$
   [32mWAttrib[39;49;00m([33m"drawop=xor"[39;49;00m)$
$
   [37m# Create two *indentical* sequences of circles, one to use when[39;49;00m$
   [37m#   when drawing, one for erasing.  (Since 'xor' is used to[39;49;00m$
   [37m#   place them, these both just draw the circles!)[39;49;00m$
$
   putcircle := [34mcreate[39;49;00m {                [37m# draws sequence of circles[39;49;00m$
      [34m&random[39;49;00m :=: r$
      |{$
       [32mFg[39;49;00m(?colors)$
       outcircle()$
       [34m&random[39;49;00m <-> r$
       }$
      }$
$
   clrcircle := [34mcreate[39;49;00m {                [37m# erases sequence of circles[39;49;00m$
      [34m&random[39;49;00m :=: r$
      |{$
       [32mFg[39;49;00m(?colors)$
       outcircle()$
       [34m&random[39;49;00m <-> r$
       }$
      }$
$
   [34mevery[39;49;00m [34m1[39;49;00m [34mto[39;49;00m density [34mdo[39;49;00m @putcircle     [37m# fill screen to density[39;49;00m$
$
   [34mevery[39;49;00m [34m1[39;49;00m [34mto[39;49;00m duration [34mdo[39;49;00m {             [37m# maintain steady state[39;49;00m$
      @putcircle$
      @clrcircle$
      [34mif[39;49;00m *[32mPending[39;49;00m([34m&window[39;49;00m) > [34m0[39;49;00m [34mthen[39;49;00m [34mbreak[39;49;00m$
      }$
$
   [34mevery[39;49;00m (Clear == [33m"On"[39;49;00m) & [34m1[39;49;00m [34mto[39;49;00m density [34mdo[39;49;00m @clrcircle$
$
   [32mclose[39;49;00m([34m&window[39;49;00m)$
[34mend[39;49;00m$
$
$
[34mprocedure[39;49;00m [32moutcircle[39;49;00m()                   [37m# select a circle at random,[39;49;00m$
[34mlocal[39;49;00m radius, xoff, yoff                [37m#  draw it in kaleidoscopic form[39;49;00m$
$
        [37m# get a random center point and radius[39;49;00m$
   xoff := (?(maxoff - minoff) + minoff) % mid_win$
   yoff := (?(maxoff - minoff) + minoff) % mid_win$
   radius := ?[34m0[39;49;00m ^ skew$
        [37m# force radius to 'fit'[39;49;00m$
   radius := ((maxradius-minradius) * radius + minradius) %$
             (mid_win - ((xoff < yoff)|xoff))$
$
        [37m# put into all 8 octants[39;49;00m$
   draw_circle(mid_win+xoff, mid_win+yoff, radius)$
   draw_circle(mid_win+xoff, mid_win-yoff, radius)$
   draw_circle(mid_win-xoff, mid_win+yoff, radius)$
   draw_circle(mid_win-xoff, mid_win-yoff, radius)$
$
   draw_circle(mid_win+yoff, mid_win+xoff, radius)$
   draw_circle(mid_win+yoff, mid_win-xoff, radius)$
   draw_circle(mid_win-yoff, mid_win+xoff, radius)$
   draw_circle(mid_win-yoff, mid_win-xoff, radius)$
$
   [34mreturn[39;49;00m$
[34mend[39;49;00m$
$
$
[37m############################################################################[39;49;00m$
[37m#[39;49;00m$
[37m#   Vidget-based user interface -- developed originally using Mary[39;49;00m$
[37m#       Camaron's XIB program.  Don't expect this to be very readable -[39;49;00m$
[37m#       you should have to play with it![39;49;00m$
[37m#[39;49;00m$
[37m############################################################################[39;49;00m$
[34mprocedure[39;49;00m [32mui[39;49;00m ([31mwin[39;49;00m)$
   [34mlocal[39;49;00m cv1, cv2, cv3, cv4$
   [34mlocal[39;49;00m $
         radio_button2, $
         radio_button1, $
         text_input6, $
         text_input5, $
         slider4, $
         slider3, $
         text_input4, $
         text_input3, $
         slider2, $
         slider1 $
$
   /win := WOpen([33m"label=ui"[39;49;00m, [33m"width=404"[39;49;00m, [33m"height=313"[39;49;00m, [33m"font=6x12"[39;49;00m) | $
           [32mstop[39;49;00m ([33m"bad win"[39;49;00m)$
   root := Vroot_frame (win)$
$
   VInsert (root, Vmessage(win, win_size/[34m2[39;49;00m), [34m168[39;49;00m, [34m98[39;49;00m)$
   VInsert (root, Vmessage(win, [33m"1"[39;49;00m), [34m108[39;49;00m, [34m97[39;49;00m)$
$
   VInsert (root, sk_v := Vtext(win,[33m"Skew:\\=1"[39;49;00m,get_skew,,[34m6[39;49;00m), [34m280[39;49;00m, [34m39[39;49;00m)$
$
   VInsert (root, du_v := Vtext(win, [33m"Duration:\\="[39;49;00m||duration, get_duration,,[34m9[39;49;00m),$
                [34m237[39;49;00m, [34m15[39;49;00m)$
$
   VInsert (root, Vmessage(win, [33m"Clear at end?"[39;49;00m), [34m232[39;49;00m, [34m145[39;49;00m)$
   VInsert (root, Vmessage(win, [33m"Fill?"[39;49;00m), [34m105[39;49;00m, [34m142[39;49;00m)$
   VInsert (root, Vmessage(win,[33m"Quit?"[39;49;00m), [34m267[39;49;00m, [34m259[39;49;00m)$
   VInsert (root, Vmessage(win,[33m"Display it?"[39;49;00m), [34m26[39;49;00m, [34m260[39;49;00m)$
$
   VInsert (root, Vcheckbox(win, do_quit, [33m"check2"[39;49;00m,[34m20[39;49;00m), [34m305[39;49;00m, [34m255[39;49;00m, [34m20[39;49;00m, [34m20[39;49;00m)$
$
   VInsert (root, check1:=Vcheckbox(win, do_display, [33m"check1"[39;49;00m,[34m20[39;49;00m),$
                [34m106[39;49;00m, [34m258[39;49;00m, [34m20[39;49;00m, [34m20[39;49;00m)$
$
   radio_button2 := Vradio_buttons (win, [[33m"On"[39;49;00m, [33m"Off"[39;49;00m], get_clear, , V_CIRCLE)$
   VSet(radio_button2,Clear)$
   VInsert (root, radio_button2, [34m253[39;49;00m, [34m165[39;49;00m)$
$
   radio_button1 := Vradio_buttons (win, [[33m"On"[39;49;00m, [33m"Off"[39;49;00m], get_fill, , V_CIRCLE)$
   VSet(radio_button1,fill)$
   VInsert (root, radio_button1, [34m99[39;49;00m, [34m165[39;49;00m)$
$
   cv1 := Vcoupler()$
   VAddClient(cv1, get_max_offset)$
   text_input6 := Vtext (win, [33m"Max Offset:\\="[39;49;00m||(win_size[34m-1[39;49;00m), cv1, , [34m3[39;49;00m)$
   VAddClient(cv1, text_input6)$
   slider4 := Vhoriz_slider (win, cv1, [33m"slider4"[39;49;00m, [34m70[39;49;00m, [34m12[39;49;00m, [34m0[39;49;00m,$
                         win_size[34m-1[39;49;00m, win_size[34m-1[39;49;00m, )$
   VAddClient(cv1, slider4)$
   VInsert (root, text_input6, [34m196[39;49;00m, [34m103[39;49;00m)$
   VInsert (root, slider4, [34m306[39;49;00m, [34m106[39;49;00m)$
$
   cv2 := Vcoupler()$
   VAddClient(cv2, get_min_offset)$
   text_input5 := Vtext (win, [33m"Min Offset\\=1"[39;49;00m, cv2, , [34m3[39;49;00m)$
   VAddClient(cv2, text_input5)$
   slider3 := Vhoriz_slider (win, cv2, [33m"slider3"[39;49;00m, [34m70[39;49;00m, [34m12[39;49;00m, [34m1[39;49;00m, win_size[34m-1[39;49;00m, [34m1[39;49;00m, )$
   VAddClient(cv2, slider3)$
   VInsert (root, text_input5, [34m201[39;49;00m, [34m80[39;49;00m)$
   VInsert (root, slider3, [34m307[39;49;00m, [34m82[39;49;00m)$
$
   cv3 := Vcoupler()$
   VAddClient(cv3, get_max_radius)$
   text_input4 := Vtext (win, [33m"Max Radius\\="[39;49;00m||(win_size/[34m4[39;49;00m), cv3, , [34m3[39;49;00m)$
   VAddClient(cv3, text_input4)$
   slider2 := Vhoriz_slider (win, cv3, [33m"slider2"[39;49;00m, [34m70[39;49;00m, [34m12[39;49;00m, [34m1[39;49;00m, win_size/[34m2[39;49;00m,$
         win_size/[34m4[39;49;00m, )$
   VAddClient(cv3, slider2)$
   VInsert (root, text_input4, [34m10[39;49;00m, [34m104[39;49;00m)$
   VInsert (root, slider2, [34m110[39;49;00m, [34m108[39;49;00m)$
$
   cv4 := Vcoupler()$
   VAddClient(cv4, get_min_radius)$
   text_input3 := Vtext (win, [33m"Min Radius\\=1"[39;49;00m, cv4, , [34m3[39;49;00m)$
   VAddClient(cv4, text_input3)$
   slider1 := Vhoriz_slider (win, cv4, [33m"slider1"[39;49;00m, [34m70[39;49;00m, [34m12[39;49;00m, [34m1[39;49;00m, win_size/[34m2[39;49;00m, [34m1[39;49;00m, )$
   VAddClient(cv4, slider1)$
   VInsert (root, text_input3, [34m10[39;49;00m, [34m81[39;49;00m)$
   VInsert (root, slider1, [34m110[39;49;00m, [34m84[39;49;00m)$
$
   VInsert (root, rs_v := Vtext(win,[33m"Random Seed:\\="[39;49;00m||r_seed, get_random,, [34m11[39;49;00m),$
              [34m30[39;49;00m, [34m41[39;49;00m)$
   VInsert (root, de_v := Vtext(win,[33m"Density:\\="[39;49;00m||density, get_density,,[34m8[39;49;00m),$
              [34m71[39;49;00m, [34m16[39;49;00m)$
$
   VResize (root)$
   [34mreturn[39;49;00m root$
[34mend[39;49;00m$
$
[34mprocedure[39;49;00m [32mget_skew[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   skew := value$
[34mend[39;49;00m$
$
[34mprocedure[39;49;00m [32mget_duration[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   duration := value$
[34mend[39;49;00m$
$
[34mprocedure[39;49;00m [32mdo_quit[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   [32mstop[39;49;00m()$
[34mend[39;49;00m$
$
[34mprocedure[39;49;00m [32mdo_display[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   r_seed   := [32mnumeric[39;49;00m(rs_v[34m.[39;49;00mdata)$
   duration := [32minteger[39;49;00m(du_v[34m.[39;49;00mdata)$
   density  := [32minteger[39;49;00m(de_v[34m.[39;49;00mdata)$
   skew     := [32minteger[39;49;00m(sk_v[34m.[39;49;00mdata)$
   kaleidoscope(r_seed)$
   wit[34m.[39;49;00mcallback[34m.[39;49;00mvalue := [34m&null[39;49;00m$
   VDraw(check1)$
[34mend[39;49;00m$
$
[34mprocedure[39;49;00m [32mget_clear[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   Clear := value$
[34mend[39;49;00m$
$
[34mprocedure[39;49;00m [32mget_fill[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   fill := value$
   [34mif[39;49;00m fill == [33m"Off"[39;49;00m [34mthen[39;49;00m draw_circle := [32mDrawCircle[39;49;00m$
   [34melse[39;49;00m draw_circle := [32mFillCircle[39;49;00m$
[34mend[39;49;00m$
$
[34mprocedure[39;49;00m [32mget_max_offset[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   maxoff := value$
[34mend[39;49;00m$
$
[34mprocedure[39;49;00m [32mget_min_offset[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   minoff := value$
[34mend[39;49;00m$
$
[34mprocedure[39;49;00m [32mget_max_radius[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   maxradius := value$
[34mend[39;49;00m$
$
[34mprocedure[39;49;00m [32mget_min_radius[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   minradius := value$
[34mend[39;49;00m$
$
[34mprocedure[39;49;00m [32mget_random[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   r_seed := [32minteger[39;49;00m(value)$
[34mend[39;49;00m$
$
[34mprocedure[39;49;00m [32mget_density[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   density := [32minteger[39;49;00m(value)$
[34mend[39;49;00m$
$
[34mprocedure[39;49;00m [32mquit[39;49;00m([31me[39;49;00m)$
   [34mif[39;49;00m e === [33m"q"[39;49;00m [34mthen[39;49;00m [32mstop[39;49;00m ([33m"Exiting Kaleidoscope"[39;49;00m)$
[34mend[39;49;00m$
