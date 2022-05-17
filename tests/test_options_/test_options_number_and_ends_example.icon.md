     1	[37m############################################################################[39;49;00m$
     2	[37m#[39;49;00m$
     3	[37m#       File:     kaleid.icn[39;49;00m$
     4	[37m#[39;49;00m$
     5	[37m#       Subject:  Program to produce kaleidoscope[39;49;00m$
     6	[37m#[39;49;00m$
     7	[37m#       Author:   Stephen B. Wampler[39;49;00m$
     8	[37m#[39;49;00m$
     9	[37m#       Date:     May 2, 2001[39;49;00m$
    10	[37m#[39;49;00m$
    11	[37m############################################################################[39;49;00m$
    12	[37m#[39;49;00m$
    13	[37m#   This file is in the public domain.[39;49;00m$
    14	[37m#[39;49;00m$
    15	[37m############################################################################[39;49;00m$
    16	[37m#[39;49;00m$
    17	[37m#    Lots of options, most easily set by with the interface after[39;49;00m$
    18	[37m#    startup.  The only one that isn't set that way is -wn where 'n' is[39;49;00m$
    19	[37m#    the size of the kaleidoscope window (default is 600 square).[39;49;00m$
    20	[37m#[39;49;00m$
    21	[37m#    Terminology (and options):[39;49;00m$
    22	[37m#[39;49;00m$
    23	[37m#       Window_size (-wN): How big of a display window to use.[39;49;00m$
    24	[37m#           At the current time, this can only be set via a[39;49;00m$
    25	[37m#           command line argument.[39;49;00m$
    26	[37m#[39;49;00m$
    27	[37m#       Density (-dN): How many circles per octant to keep on display[39;49;00m$
    28	[37m#           at any one time.  There is NO LIMIT to the density.[39;49;00m$
    29	[37m#[39;49;00m$
    30	[37m#       Duration (-lN): How long to keep drawing circles (measured in[39;49;00m$
    31	[37m#           in circles) once the density is reached.  There is NO LIMIT[39;49;00m$
    32	[37m#           to the duration.[39;49;00m$
    33	[37m#[39;49;00m$
    34	[37m#       MaxRadius (-MN): Maximum radius of any circle.[39;49;00m$
    35	[37m#[39;49;00m$
    36	[37m#       MinRadius (-mN): Preferred minimum radius.  Circles with centers[39;49;00m$
    37	[37m#           near the edge have their radii forced down to fit entirely[39;49;00m$
    38	[37m#           on the display[39;49;00m$
    39	[37m#[39;49;00m$
    40	[37m#       MaxOffset (-XN): Maximum offset from center of display (may wrap).[39;49;00m$
    41	[37m#[39;49;00m$
    42	[37m#       MinOffset (-xN): Minimum offset[39;49;00m$
    43	[37m#[39;49;00m$
    44	[37m#       Skew (-sN): Shift probability of placing a circle at a 'typical'[39;49;00m$
    45	[37m#           offset.[39;49;00m$
    46	[37m#[39;49;00m$
    47	[37m#       Fill (-F): Turns off filling the circles.[39;49;00m$
    48	[37m#[39;49;00m$
    49	[37m#       Clear (-C): After the duration, reduces density back to 0 before[39;49;00m$
    50	[37m#           quitting.[39;49;00m$
    51	[37m#[39;49;00m$
    52	[37m#       Random Seed: (-rN): Sets the random number seed.[39;49;00m$
    53	[37m#[39;49;00m$
    54	[37m# Thanks to Jon Lipp for help on using vidgets, and to Mary Camaron[39;49;00m$
    55	[37m#   for her Interface Builder.[39;49;00m$
    56	[37m#[39;49;00m$
    57	[37m############################################################################[39;49;00m$
    58	[37m#[39;49;00m$
    59	[37m#  Requires:  Version 9 graphics[39;49;00m$
    60	[37m#[39;49;00m$
    61	[37m############################################################################[39;49;00m$
    62	[37m#[39;49;00m$
    63	[37m#  Links:  vidgets, vslider, vtext, vbuttons, vradio, wopen, xcompat[39;49;00m$
    64	[37m#[39;49;00m$
    65	[37m############################################################################[39;49;00m$
    66	$
    67	[34mlink[39;49;00m vidgets$
    68	[34mlink[39;49;00m vslider$
    69	[34mlink[39;49;00m vtext$
    70	[34mlink[39;49;00m vbuttons$
    71	[34mlink[39;49;00m vradio$
    72	[34mlink[39;49;00m wopen$
    73	[34mlink[39;49;00m xcompat$
    74	$
    75	[34mglobal[39;49;00m Clear, fill, duration, density, maxoff, minoff$
    76	[34mglobal[39;49;00m maxradius, minradius, r_seed, skew, win_size, mid_win$
    77	[34mglobal[39;49;00m root, check1, mainwin, use_dialog$
    78	[34mglobal[39;49;00m draw_circle$
    79	$
    80	[34mglobal[39;49;00m du_v, de_v, rs_v, sk_v$
    81	$
    82	[34mprocedure[39;49;00m [32mmain[39;49;00m ([31margs[39;49;00m)$
    83	$
    84	   draw_circle := [32mDrawCircle[39;49;00m$
    85	$
    86	   init_globs()$
    87	   process_args([32margs[39;49;00m)$
    88	$
    89	   [34mif[39;49;00m \use_dialog [34mthen[39;49;00m {        [37m# have vidgets, so use them for args.[39;49;00m$
    90	      mainwin := WOpen([33m"label=Kaleidoscope"[39;49;00m, [33m"width=404"[39;49;00m, [33m"height=313"[39;49;00m, $
    91	                       [33m"font=6x12"[39;49;00m) |$
    92	                 [32mstop[39;49;00m ([33m"bad mainwin"[39;49;00m)$
    93	      root := ui (mainwin)$
    94	      GetEvents (root, quit)$
    95	      }$
    96	   [34melse[39;49;00m {                       [37m# just rely on command line arguments[39;49;00m$
    97	      kaleidoscope(r_seed)$
    98	      }$
    99	$
   100	[34mend[39;49;00m$
   101	$
   102	[34mprocedure[39;49;00m [32minit_globs[39;49;00m()$
   103	$
   104	   duration := [34m500[39;49;00m                    [37m# set default characteristics[39;49;00m$
   105	   density := [34m30[39;49;00m$
   106	   win_size := [34m600[39;49;00m$
   107	   minoff := [34m1[39;49;00m$
   108	   maxradius := [34m150[39;49;00m$
   109	   minradius := [34m1[39;49;00m$
   110	   skew := [34m1[39;49;00m$
   111	   fill := [33m"On"[39;49;00m$
   112	   draw_circle := [32mFillCircle[39;49;00m$
   113	   Clear := [33m"Off"[39;49;00m$
   114	   r_seed := [32mmap[39;49;00m([33m"HhMmYy"[39;49;00m, [33m"Hh:Mm:Yy"[39;49;00m, [34m&clock[39;49;00m)$
   115	   [37m# See if the Vidget library is available or not[39;49;00m$
   116	   [34mif[39;49;00m \VSet [34mthen[39;49;00m use_dialog := [33m"yes"[39;49;00m$
   117	            [34melse[39;49;00m use_dialog := [34m&null[39;49;00m$
   118	$
   119	[34mend[39;49;00m$
   120	$
   121	[34mprocedure[39;49;00m [32mprocess_args[39;49;00m([31margs[39;49;00m)$
   122	   [34mlocal[39;49;00m arg$
   123	$
   124	   [37m# really only needed if you don't use the dialog box[39;49;00m$
   125	   [34mevery[39;49;00m arg := ![32margs[39;49;00m [34mdo[39;49;00m [34mcase[39;49;00m arg[[34m1[39;49;00m+:[34m2[39;49;00m] [34mof[39;49;00m {$
   126	      [33m"-w"[39;49;00m : win_size := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])       [37m# window size[39;49;00m$
   127	      [33m"-d"[39;49;00m : density := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])        [37m# density of circles[39;49;00m$
   128	      [33m"-l"[39;49;00m : duration := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])       [37m# duration[39;49;00m$
   129	      [33m"-M"[39;49;00m : maxradius := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])      [37m# maximum radius[39;49;00m$
   130	      [33m"-m"[39;49;00m : minradius := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])      [37m# minimum radius[39;49;00m$
   131	      [33m"-X"[39;49;00m : maxoff := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])         [37m# maximum offset[39;49;00m$
   132	      [33m"-x"[39;49;00m : minoff := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])         [37m# minimum offset[39;49;00m$
   133	      [33m"-s"[39;49;00m : skew := [32mnumeric[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])           [37m# set skewedness[39;49;00m$
   134	      [33m"-F"[39;49;00m : fill := [34m&null[39;49;00m                       [37m# turn off fill[39;49;00m$
   135	      [33m"-C"[39;49;00m : Clear := [33m"yes"[39;49;00m                      [37m# turn on clear mode[39;49;00m$
   136	      [33m"-r"[39;49;00m : r_seed := [32minteger[39;49;00m(arg[[34m3[39;49;00m:[34m0[39;49;00m])         [37m# random seed[39;49;00m$
   137	      [33m"-h"[39;49;00m : [32mstop[39;49;00m([33m"usage: kal [-wn] [-dn] [-ln] [-Mn] [-mn] [-Xn] [-xn] _[39;49;00m$
   138	[33m                     [-sn] [-F] [-C] [-rn]"[39;49;00m)$
   139	      }$
   140	   [37m# adjust parameters that depend on the window size...[39;49;00m$
   141	   mid_win := win_size/[34m2[39;49;00m$
   142	   maxoff := win_size[34m-1[39;49;00m$
   143	[34mend[39;49;00m$
   144	$
   145	[37m# Lorraine Callahan's kaleidoscope program, translated into icon.[39;49;00m$
   146	[37m#  (some of the things she did were too sophisticated for me[39;49;00m$
   147	[37m#   to spend time to figure out, so the output is square instead of[39;49;00m$
   148	[37m#   round), and I use 'xor' to draw instead of writing to separate[39;49;00m$
   149	[37m#   bit planes.[39;49;00m$
   150	$
   151	[34mglobal[39;49;00m putcircle, clrcircle$
   152	$
   153	[34mprocedure[39;49;00m [32mkaleidoscope[39;49;00m([31mr[39;49;00m)$
   154	   [34mlocal[39;49;00m colors$
   155	$
   156	   [37m# What colors to use?  This can be changed to whatever![39;49;00m$
   157	   colors := [[33m"red"[39;49;00m,[33m"green"[39;49;00m,[33m"blue"[39;49;00m,[33m"cyan"[39;49;00m,[33m"magenta"[39;49;00m,[33m"yellow"[39;49;00m]$
   158	$
   159	   [34m&window[39;49;00m := WOpen([33m"label=Kaleidoscope: 'q' quits"[39;49;00m, [33m"width="[39;49;00m||win_size,$
   160	                                  [33m"height="[39;49;00m||win_size, [33m"bg=black"[39;49;00m)$
   161	   [32mWAttrib[39;49;00m([33m"drawop=xor"[39;49;00m)$
   162	$
   163	   [37m# Create two *indentical* sequences of circles, one to use when[39;49;00m$
   164	   [37m#   when drawing, one for erasing.  (Since 'xor' is used to[39;49;00m$
   165	   [37m#   place them, these both just draw the circles!)[39;49;00m$
   166	$
   167	   putcircle := [34mcreate[39;49;00m {                [37m# draws sequence of circles[39;49;00m$
   168	      [34m&random[39;49;00m :=: r$
   169	      |{$
   170	       [32mFg[39;49;00m(?colors)$
   171	       outcircle()$
   172	       [34m&random[39;49;00m <-> r$
   173	       }$
   174	      }$
   175	$
   176	   clrcircle := [34mcreate[39;49;00m {                [37m# erases sequence of circles[39;49;00m$
   177	      [34m&random[39;49;00m :=: r$
   178	      |{$
   179	       [32mFg[39;49;00m(?colors)$
   180	       outcircle()$
   181	       [34m&random[39;49;00m <-> r$
   182	       }$
   183	      }$
   184	$
   185	   [34mevery[39;49;00m [34m1[39;49;00m [34mto[39;49;00m density [34mdo[39;49;00m @putcircle     [37m# fill screen to density[39;49;00m$
   186	$
   187	   [34mevery[39;49;00m [34m1[39;49;00m [34mto[39;49;00m duration [34mdo[39;49;00m {             [37m# maintain steady state[39;49;00m$
   188	      @putcircle$
   189	      @clrcircle$
   190	      [34mif[39;49;00m *[32mPending[39;49;00m([34m&window[39;49;00m) > [34m0[39;49;00m [34mthen[39;49;00m [34mbreak[39;49;00m$
   191	      }$
   192	$
   193	   [34mevery[39;49;00m (Clear == [33m"On"[39;49;00m) & [34m1[39;49;00m [34mto[39;49;00m density [34mdo[39;49;00m @clrcircle$
   194	$
   195	   [32mclose[39;49;00m([34m&window[39;49;00m)$
   196	[34mend[39;49;00m$
   197	$
   198	$
   199	[34mprocedure[39;49;00m [32moutcircle[39;49;00m()                   [37m# select a circle at random,[39;49;00m$
   200	[34mlocal[39;49;00m radius, xoff, yoff                [37m#  draw it in kaleidoscopic form[39;49;00m$
   201	$
   202	        [37m# get a random center point and radius[39;49;00m$
   203	   xoff := (?(maxoff - minoff) + minoff) % mid_win$
   204	   yoff := (?(maxoff - minoff) + minoff) % mid_win$
   205	   radius := ?[34m0[39;49;00m ^ skew$
   206	        [37m# force radius to 'fit'[39;49;00m$
   207	   radius := ((maxradius-minradius) * radius + minradius) %$
   208	             (mid_win - ((xoff < yoff)|xoff))$
   209	$
   210	        [37m# put into all 8 octants[39;49;00m$
   211	   draw_circle(mid_win+xoff, mid_win+yoff, radius)$
   212	   draw_circle(mid_win+xoff, mid_win-yoff, radius)$
   213	   draw_circle(mid_win-xoff, mid_win+yoff, radius)$
   214	   draw_circle(mid_win-xoff, mid_win-yoff, radius)$
   215	$
   216	   draw_circle(mid_win+yoff, mid_win+xoff, radius)$
   217	   draw_circle(mid_win+yoff, mid_win-xoff, radius)$
   218	   draw_circle(mid_win-yoff, mid_win+xoff, radius)$
   219	   draw_circle(mid_win-yoff, mid_win-xoff, radius)$
   220	$
   221	   [34mreturn[39;49;00m$
   222	[34mend[39;49;00m$
   223	$
   224	$
   225	[37m############################################################################[39;49;00m$
   226	[37m#[39;49;00m$
   227	[37m#   Vidget-based user interface -- developed originally using Mary[39;49;00m$
   228	[37m#       Camaron's XIB program.  Don't expect this to be very readable -[39;49;00m$
   229	[37m#       you should have to play with it![39;49;00m$
   230	[37m#[39;49;00m$
   231	[37m############################################################################[39;49;00m$
   232	[34mprocedure[39;49;00m [32mui[39;49;00m ([31mwin[39;49;00m)$
   233	   [34mlocal[39;49;00m cv1, cv2, cv3, cv4$
   234	   [34mlocal[39;49;00m $
   235	         radio_button2, $
   236	         radio_button1, $
   237	         text_input6, $
   238	         text_input5, $
   239	         slider4, $
   240	         slider3, $
   241	         text_input4, $
   242	         text_input3, $
   243	         slider2, $
   244	         slider1 $
   245	$
   246	   /win := WOpen([33m"label=ui"[39;49;00m, [33m"width=404"[39;49;00m, [33m"height=313"[39;49;00m, [33m"font=6x12"[39;49;00m) | $
   247	           [32mstop[39;49;00m ([33m"bad win"[39;49;00m)$
   248	   root := Vroot_frame (win)$
   249	$
   250	   VInsert (root, Vmessage(win, win_size/[34m2[39;49;00m), [34m168[39;49;00m, [34m98[39;49;00m)$
   251	   VInsert (root, Vmessage(win, [33m"1"[39;49;00m), [34m108[39;49;00m, [34m97[39;49;00m)$
   252	$
   253	   VInsert (root, sk_v := Vtext(win,[33m"Skew:\\=1"[39;49;00m,get_skew,,[34m6[39;49;00m), [34m280[39;49;00m, [34m39[39;49;00m)$
   254	$
   255	   VInsert (root, du_v := Vtext(win, [33m"Duration:\\="[39;49;00m||duration, get_duration,,[34m9[39;49;00m),$
   256	                [34m237[39;49;00m, [34m15[39;49;00m)$
   257	$
   258	   VInsert (root, Vmessage(win, [33m"Clear at end?"[39;49;00m), [34m232[39;49;00m, [34m145[39;49;00m)$
   259	   VInsert (root, Vmessage(win, [33m"Fill?"[39;49;00m), [34m105[39;49;00m, [34m142[39;49;00m)$
   260	   VInsert (root, Vmessage(win,[33m"Quit?"[39;49;00m), [34m267[39;49;00m, [34m259[39;49;00m)$
   261	   VInsert (root, Vmessage(win,[33m"Display it?"[39;49;00m), [34m26[39;49;00m, [34m260[39;49;00m)$
   262	$
   263	   VInsert (root, Vcheckbox(win, do_quit, [33m"check2"[39;49;00m,[34m20[39;49;00m), [34m305[39;49;00m, [34m255[39;49;00m, [34m20[39;49;00m, [34m20[39;49;00m)$
   264	$
   265	   VInsert (root, check1:=Vcheckbox(win, do_display, [33m"check1"[39;49;00m,[34m20[39;49;00m),$
   266	                [34m106[39;49;00m, [34m258[39;49;00m, [34m20[39;49;00m, [34m20[39;49;00m)$
   267	$
   268	   radio_button2 := Vradio_buttons (win, [[33m"On"[39;49;00m, [33m"Off"[39;49;00m], get_clear, , V_CIRCLE)$
   269	   VSet(radio_button2,Clear)$
   270	   VInsert (root, radio_button2, [34m253[39;49;00m, [34m165[39;49;00m)$
   271	$
   272	   radio_button1 := Vradio_buttons (win, [[33m"On"[39;49;00m, [33m"Off"[39;49;00m], get_fill, , V_CIRCLE)$
   273	   VSet(radio_button1,fill)$
   274	   VInsert (root, radio_button1, [34m99[39;49;00m, [34m165[39;49;00m)$
   275	$
   276	   cv1 := Vcoupler()$
   277	   VAddClient(cv1, get_max_offset)$
   278	   text_input6 := Vtext (win, [33m"Max Offset:\\="[39;49;00m||(win_size[34m-1[39;49;00m), cv1, , [34m3[39;49;00m)$
   279	   VAddClient(cv1, text_input6)$
   280	   slider4 := Vhoriz_slider (win, cv1, [33m"slider4"[39;49;00m, [34m70[39;49;00m, [34m12[39;49;00m, [34m0[39;49;00m,$
   281	                         win_size[34m-1[39;49;00m, win_size[34m-1[39;49;00m, )$
   282	   VAddClient(cv1, slider4)$
   283	   VInsert (root, text_input6, [34m196[39;49;00m, [34m103[39;49;00m)$
   284	   VInsert (root, slider4, [34m306[39;49;00m, [34m106[39;49;00m)$
   285	$
   286	   cv2 := Vcoupler()$
   287	   VAddClient(cv2, get_min_offset)$
   288	   text_input5 := Vtext (win, [33m"Min Offset\\=1"[39;49;00m, cv2, , [34m3[39;49;00m)$
   289	   VAddClient(cv2, text_input5)$
   290	   slider3 := Vhoriz_slider (win, cv2, [33m"slider3"[39;49;00m, [34m70[39;49;00m, [34m12[39;49;00m, [34m1[39;49;00m, win_size[34m-1[39;49;00m, [34m1[39;49;00m, )$
   291	   VAddClient(cv2, slider3)$
   292	   VInsert (root, text_input5, [34m201[39;49;00m, [34m80[39;49;00m)$
   293	   VInsert (root, slider3, [34m307[39;49;00m, [34m82[39;49;00m)$
   294	$
   295	   cv3 := Vcoupler()$
   296	   VAddClient(cv3, get_max_radius)$
   297	   text_input4 := Vtext (win, [33m"Max Radius\\="[39;49;00m||(win_size/[34m4[39;49;00m), cv3, , [34m3[39;49;00m)$
   298	   VAddClient(cv3, text_input4)$
   299	   slider2 := Vhoriz_slider (win, cv3, [33m"slider2"[39;49;00m, [34m70[39;49;00m, [34m12[39;49;00m, [34m1[39;49;00m, win_size/[34m2[39;49;00m,$
   300	         win_size/[34m4[39;49;00m, )$
   301	   VAddClient(cv3, slider2)$
   302	   VInsert (root, text_input4, [34m10[39;49;00m, [34m104[39;49;00m)$
   303	   VInsert (root, slider2, [34m110[39;49;00m, [34m108[39;49;00m)$
   304	$
   305	   cv4 := Vcoupler()$
   306	   VAddClient(cv4, get_min_radius)$
   307	   text_input3 := Vtext (win, [33m"Min Radius\\=1"[39;49;00m, cv4, , [34m3[39;49;00m)$
   308	   VAddClient(cv4, text_input3)$
   309	   slider1 := Vhoriz_slider (win, cv4, [33m"slider1"[39;49;00m, [34m70[39;49;00m, [34m12[39;49;00m, [34m1[39;49;00m, win_size/[34m2[39;49;00m, [34m1[39;49;00m, )$
   310	   VAddClient(cv4, slider1)$
   311	   VInsert (root, text_input3, [34m10[39;49;00m, [34m81[39;49;00m)$
   312	   VInsert (root, slider1, [34m110[39;49;00m, [34m84[39;49;00m)$
   313	$
   314	   VInsert (root, rs_v := Vtext(win,[33m"Random Seed:\\="[39;49;00m||r_seed, get_random,, [34m11[39;49;00m),$
   315	              [34m30[39;49;00m, [34m41[39;49;00m)$
   316	   VInsert (root, de_v := Vtext(win,[33m"Density:\\="[39;49;00m||density, get_density,,[34m8[39;49;00m),$
   317	              [34m71[39;49;00m, [34m16[39;49;00m)$
   318	$
   319	   VResize (root)$
   320	   [34mreturn[39;49;00m root$
   321	[34mend[39;49;00m$
   322	$
   323	[34mprocedure[39;49;00m [32mget_skew[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   324	   skew := value$
   325	[34mend[39;49;00m$
   326	$
   327	[34mprocedure[39;49;00m [32mget_duration[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   328	   duration := value$
   329	[34mend[39;49;00m$
   330	$
   331	[34mprocedure[39;49;00m [32mdo_quit[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   332	   [32mstop[39;49;00m()$
   333	[34mend[39;49;00m$
   334	$
   335	[34mprocedure[39;49;00m [32mdo_display[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   336	   r_seed   := [32mnumeric[39;49;00m(rs_v[34m.[39;49;00mdata)$
   337	   duration := [32minteger[39;49;00m(du_v[34m.[39;49;00mdata)$
   338	   density  := [32minteger[39;49;00m(de_v[34m.[39;49;00mdata)$
   339	   skew     := [32minteger[39;49;00m(sk_v[34m.[39;49;00mdata)$
   340	   kaleidoscope(r_seed)$
   341	   wit[34m.[39;49;00mcallback[34m.[39;49;00mvalue := [34m&null[39;49;00m$
   342	   VDraw(check1)$
   343	[34mend[39;49;00m$
   344	$
   345	[34mprocedure[39;49;00m [32mget_clear[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   346	   Clear := value$
   347	[34mend[39;49;00m$
   348	$
   349	[34mprocedure[39;49;00m [32mget_fill[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   350	   fill := value$
   351	   [34mif[39;49;00m fill == [33m"Off"[39;49;00m [34mthen[39;49;00m draw_circle := [32mDrawCircle[39;49;00m$
   352	   [34melse[39;49;00m draw_circle := [32mFillCircle[39;49;00m$
   353	[34mend[39;49;00m$
   354	$
   355	[34mprocedure[39;49;00m [32mget_max_offset[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   356	   maxoff := value$
   357	[34mend[39;49;00m$
   358	$
   359	[34mprocedure[39;49;00m [32mget_min_offset[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   360	   minoff := value$
   361	[34mend[39;49;00m$
   362	$
   363	[34mprocedure[39;49;00m [32mget_max_radius[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   364	   maxradius := value$
   365	[34mend[39;49;00m$
   366	$
   367	[34mprocedure[39;49;00m [32mget_min_radius[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   368	   minradius := value$
   369	[34mend[39;49;00m$
   370	$
   371	[34mprocedure[39;49;00m [32mget_random[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   372	   r_seed := [32minteger[39;49;00m(value)$
   373	[34mend[39;49;00m$
   374	$
   375	[34mprocedure[39;49;00m [32mget_density[39;49;00m ([31mwit[39;49;00m, [31mvalue[39;49;00m)$
   376	   density := [32minteger[39;49;00m(value)$
   377	[34mend[39;49;00m$
   378	$
   379	[34mprocedure[39;49;00m [32mquit[39;49;00m([31me[39;49;00m)$
   380	   [34mif[39;49;00m e === [33m"q"[39;49;00m [34mthen[39;49;00m [32mstop[39;49;00m ([33m"Exiting Kaleidoscope"[39;49;00m)$
   381	[34mend[39;49;00m$
