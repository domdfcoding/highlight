     1	[37m#[39;49;00m$
     2	[37m# $Id: button.icn,v 1.7 2006-07-09 23:43:07 rparlett Exp $[39;49;00m$
     3	[37m#[39;49;00m$
     4	[37m# This file is in the public domain.[39;49;00m$
     5	[37m#[39;49;00m$
     6	[37m# Author: Robert Parlett (parlett@dial.pipex.com)[39;49;00m$
     7	[37m#[39;49;00m$
     8	$
     9	[34mpackage[39;49;00m gui$
    10	[34mlink[39;49;00m graphics$
    11	$
    12	[34m$include[39;49;00m [33m"guih.icn"[39;49;00m$
    13	$
    14	$
    15	[37m#[39;49;00m$
    16	[37m# This is the parent class of the button classes, including[39;49;00m$
    17	[37m# checkboxes.[39;49;00m$
    18	[37m#[39;49;00m$
    19	[37m# A {Button} produces a BUTTON_PRESS_EVENT when the button is[39;49;00m$
    20	[37m# depressed, and code BUTTON_RELEASE_EVENT when it is released,[39;49;00m$
    21	[37m# as well as an ACTION_EVENT.[39;49;00m$
    22	[37m# [39;49;00m$
    23	[37m# By default, when a button holds the keyboard focus a dashed[39;49;00m$
    24	[37m# line appears just within the button.  Then, when return is[39;49;00m$
    25	[37m# pressed an ACTION_EVENT is generated.  The method[39;49;00m$
    26	[37m# {Dialog.set_initial_focus()} can be used to have the button[39;49;00m$
    27	[37m# have the focus when the dialog is first displayed.[39;49;00m$
    28	[37m#[39;49;00m$
    29	[37m# Buttons also repeatedly produce a BUTTON_HELD_EVENT whilst they[39;49;00m$
    30	[37m# are held down, rather like a repeating keyboard press.  The[39;49;00m$
    31	[37m# delay between the initial repeat event and subsequent repeat[39;49;00m$
    32	[37m# events is set in the parent dialog (see above).[39;49;00m$
    33	[37m#[39;49;00m$
    34	[34mclass[39;49;00m [32mButton[39;49;00m : [32mToggle[39;49;00m : [32mComponent[39;49;00m($
    35	   [31mis_down[39;49;00m,                 [37m#               [39;49;00m$
    36	   [31mis_held[39;49;00m,                 [37m#               [39;49;00m$
    37	   [31mis_checked_flag[39;49;00m,         [37m#                       [39;49;00m$
    38	   [31mlabel[39;49;00m,$
    39	   [31mimg_up[39;49;00m,                  [37m#              [39;49;00m$
    40	   [31mimg_down[39;49;00m,                [37m#                [39;49;00m$
    41	   [31mimg_w[39;49;00m,                   [37m#             [39;49;00m$
    42	   [31mimg_h[39;49;00m,                   [37m#             [39;49;00m$
    43	   [31mparent_check_box_group[39;49;00m,  [37m#[39;49;00m$
    44	   [31mparent_button_group[39;49;00m,     [37m#                           [39;49;00m$
    45	   [31mrepeat_delay[39;49;00m,$
    46	   [31mno_keyboard_flag[39;49;00m,        [37m#[39;49;00m$
    47	   [31mtoggles_flag[39;49;00m$
    48	   )$
    49	$
    50	   [34mmethod[39;49;00m [32mset_parent_button_group[39;49;00m([31mx[39;49;00m)$
    51	      [34mreturn[39;49;00m self[34m.[39;49;00mparent_button_group := x$
    52	   [34mend[39;49;00m$
    53	$
    54	   [37m#[39;49;00m$
    55	   [37m# Invoking this method disables the keyboard control over the[39;49;00m$
    56	   [37m# button described above.  No dashed line will ever appear in[39;49;00m$
    57	   [37m# the button display and return will have no effect on the[39;49;00m$
    58	   [37m# button even if it has the focus.[39;49;00m$
    59	   [37m#[39;49;00m$
    60	   [34mmethod[39;49;00m [32mset_no_keyboard[39;49;00m()$
    61	      self[34m.[39;49;00mno_keyboard_flag := [34m1[39;49;00m$
    62	      self[34m.[39;49;00maccepts_focus_flag := [34m&null[39;49;00m$
    63	   [34mend[39;49;00m$
    64	   $
    65	   [37m#[39;49;00m$
    66	   [37m# Clear the no keyboard behaviour (the default)[39;49;00m$
    67	   [37m#[39;49;00m$
    68	   [34mmethod[39;49;00m [32mclear_no_keyboard[39;49;00m()$
    69	      self[34m.[39;49;00mno_keyboard_flag := [34m&null[39;49;00m$
    70	      self[34m.[39;49;00maccepts_focus_flag := [34m1[39;49;00m$
    71	   [34mend[39;49;00m$
    72	$
    73	   [34mmethod[39;49;00m [32mtick[39;49;00m()$
    74	      [34mif[39;49;00m dispatcher[34m.[39;49;00mcurr_time_of_day() > self[34m.[39;49;00mrepeat_delay [34mthen[39;49;00m$
    75	         fire(BUTTON_HELD_EVENT)$
    76	   [34mend[39;49;00m$
    77	$
    78	   [34mmethod[39;49;00m [32mgo_down[39;49;00m()$
    79	      self[34m.[39;49;00mis_down := [34m1[39;49;00m$
    80	      set_ticker(self[34m.[39;49;00mparent_dialog[34m.[39;49;00mrepeat_rate)$
    81	   [34mend[39;49;00m$
    82	$
    83	   [34mmethod[39;49;00m [32mgo_up[39;49;00m()$
    84	      self[34m.[39;49;00mis_down := [34m&null[39;49;00m$
    85	      stop_ticker()$
    86	   [34mend[39;49;00m$
    87	$
    88	   [34mmethod[39;49;00m [32mhandle_press[39;49;00m([31me[39;49;00m)$
    89	      [34mlocal[39;49;00m b$
    90	      [34mif[39;49;00m self[34m.[39;49;00min_region() [34mthen[39;49;00m {$
    91	         go_down()$
    92	         self[34m.[39;49;00mrepeat_delay := dispatcher[34m.[39;49;00mcurr_time_of_day() + self[34m.[39;49;00mparent_dialog[34m.[39;49;00mrepeat_delay$
    93	         self[34m.[39;49;00mis_held := [34m1[39;49;00m$
    94	         [34mevery[39;49;00m b := !(\self[34m.[39;49;00mparent_button_group)[34m.[39;49;00mbuttons [34mdo[39;49;00m {$
    95	            [34mif[39;49;00m b[34m.[39;49;00mis_unhidden() [34mthen[39;49;00m {$
    96	               b[34m.[39;49;00mis_held := [34m1[39;49;00m$
    97	               b[34m.[39;49;00mrepeat_delay := self[34m.[39;49;00mrepeat_delay$
    98	            }$
    99	         }$
   100	         self[34m.[39;49;00minvalidate()$
   101	         fire(BUTTON_PRESS_EVENT, e)$
   102	      }$
   103	   [34mend[39;49;00m$
   104	$
   105	   [34mmethod[39;49;00m [32mhandle_drag[39;49;00m([31me[39;49;00m)$
   106	      [34mif[39;49;00m \self[34m.[39;49;00mis_held [34mthen[39;49;00m {$
   107	         [37m#[39;49;00m$
   108	         [37m# Button held down; toggle on/off as it goes over the button [39;49;00m$
   109	         [37m#[39;49;00m$
   110	         [34mif[39;49;00m self[34m.[39;49;00min_region() [34mthen[39;49;00m {$
   111	            [34mif[39;49;00m /self[34m.[39;49;00mis_down [34mthen[39;49;00m {$
   112	               go_down()$
   113	               invalidate()$
   114	            }$
   115	         } [34melse[39;49;00m {$
   116	            [34mif[39;49;00m \self[34m.[39;49;00mis_down [34mthen[39;49;00m {$
   117	               go_up()$
   118	               invalidate()$
   119	            }$
   120	         }$
   121	      }$
   122	   [34mend[39;49;00m$
   123	$
   124	   [34mmethod[39;49;00m [32mhandle_release[39;49;00m([31me[39;49;00m)$
   125	      [34mif[39;49;00m \self[34m.[39;49;00mis_held [34mthen[39;49;00m {$
   126	         self[34m.[39;49;00mis_held := [34m&null[39;49;00m$
   127	         [34mif[39;49;00m \self[34m.[39;49;00mis_down [34mthen[39;49;00m {$
   128	            go_up()$
   129	            fire(BUTTON_RELEASE_EVENT, e)$
   130	            on_action(e)$
   131	         }$
   132	      }$
   133	   [34mend[39;49;00m$
   134	$
   135	   [34mmethod[39;49;00m [32mon_action[39;49;00m([31me[39;49;00m)$
   136	      [34mif[39;49;00m \self[34m.[39;49;00mtoggles_flag [34mthen[39;49;00m {$
   137	         [34mif[39;49;00m \self[34m.[39;49;00mparent_check_box_group [34mthen[39;49;00m$
   138	            self[34m.[39;49;00mparent_check_box_group[34m.[39;49;00mset_which_one(self)$
   139	         [34melse[39;49;00m$
   140	            self[34m.[39;49;00mtoggle_is_checked()$
   141	      }$
   142	      self[34m.[39;49;00minvalidate()$
   143	      fire(ACTION_EVENT, e)$
   144	   [34mend[39;49;00m$
   145	$
   146	   [34mmethod[39;49;00m [32mhandle_accel[39;49;00m([31me[39;49;00m)$
   147	      self[34m.[39;49;00mComponent[34m.[39;49;00mhandle_accel(e)$
   148	      on_action(e)$
   149	   [34mend[39;49;00m$
   150	$
   151	   [34mmethod[39;49;00m [32mhandle_default[39;49;00m([31me[39;49;00m)$
   152	      [34mif[39;49;00m \self[34m.[39;49;00mhas_focus [34mthen[39;49;00m {$
   153	         [34mif[39;49;00m /self[34m.[39;49;00mno_keyboard_flag & e == ([33m"\r"[39;49;00m | [33m"\l"[39;49;00m | [33m" "[39;49;00m) [34mthen[39;49;00m {$
   154	            on_action(e)$
   155	         }$
   156	      }$
   157	   [34mend[39;49;00m$
   158	$
   159	   [34mmethod[39;49;00m [32mhandle_event[39;49;00m([31me[39;49;00m)$
   160	      [34mif[39;49;00m e === ([34m&lpress[39;49;00m | [34m&rpress[39;49;00m | [34m&mpress[39;49;00m) [34mthen[39;49;00m {$
   161	         handle_press(e)$
   162	      } [34melse[39;49;00m [34mif[39;49;00m e === ([34m&ldrag[39;49;00m | [34m&rdrag[39;49;00m | [34m&mdrag[39;49;00m) [34mthen[39;49;00m {$
   163	         handle_drag(e)$
   164	      } [34melse[39;49;00m [34mif[39;49;00m e === ([34m&lrelease[39;49;00m | [34m&rrelease[39;49;00m | [34m&mrelease[39;49;00m) [34mthen[39;49;00m {$
   165	         handle_release(e)$
   166	      } [34melse[39;49;00m $
   167	         handle_default(e)$
   168	   [34mend[39;49;00m$
   169	$
   170	   [37m#[39;49;00m$
   171	   [37m# Set the up/down images (if any) to the strings provided,[39;49;00m$
   172	   [37m# which should be in Icon image format.[39;49;00m$
   173	   [37m# The two images must have the same dimensions.[39;49;00m$
   174	   [37m# @param x   The up image[39;49;00m$
   175	   [37m# @param y   The down image[39;49;00m$
   176	   [37m#[39;49;00m$
   177	   [34mmethod[39;49;00m [32mset_imgs[39;49;00m([31mx[39;49;00m, [31my[39;49;00m)$
   178	      self[34m.[39;49;00mimg_up := x$
   179	      self[34m.[39;49;00mimg_w := img_width(x) = img_width(y) | fatal([33m"Image widths differ"[39;49;00m)$
   180	      self[34m.[39;49;00mimg_h := img_height(x) = img_height(y) | fatal([33m"Image heights differ"[39;49;00m)$
   181	$
   182	      self[34m.[39;49;00mimg_down := y$
   183	$
   184	      [34mreturn[39;49;00m$
   185	   [34mend[39;49;00m$
   186	$
   187	   [37m#[39;49;00m$
   188	   [37m# Set the image (if any) to the given string, which should be in Icon image[39;49;00m$
   189	   [37m# format.[39;49;00m$
   190	   [37m# @param x   The image[39;49;00m$
   191	   [37m#[39;49;00m$
   192	   [34mmethod[39;49;00m [32mset_img[39;49;00m([31mx[39;49;00m)$
   193	      self[34m.[39;49;00mimg_up := self[34m.[39;49;00mimg_down := x$
   194	      self[34m.[39;49;00mimg_w := img_width(x)$
   195	      self[34m.[39;49;00mimg_h := img_height(x)$
   196	      [34mreturn[39;49;00m x$
   197	   [34mend[39;49;00m$
   198	$
   199	   [37m#[39;49;00m$
   200	   [37m# Toggle the checked status of the button.  This method, and[39;49;00m$
   201	   [37m# the following two methods, may be[39;49;00m$
   202	   [37m# inappropriate for non-toggle styles of button.[39;49;00m$
   203	   [37m#[39;49;00m$
   204	   [34mmethod[39;49;00m [32mtoggle_is_checked[39;49;00m()$
   205	      self[34m.[39;49;00mToggle[34m.[39;49;00mtoggle_is_checked()$
   206	      self[34m.[39;49;00minvalidate()$
   207	   [34mend[39;49;00m$
   208	$
   209	   [37m#[39;49;00m$
   210	   [37m# Set the status to checked.[39;49;00m$
   211	   [37m#[39;49;00m$
   212	   [34mmethod[39;49;00m [32mset_is_checked[39;49;00m()$
   213	      self[34m.[39;49;00mToggle[34m.[39;49;00mset_is_checked()$
   214	      self[34m.[39;49;00minvalidate()$
   215	   [34mend[39;49;00m$
   216	$
   217	   [37m#[39;49;00m$
   218	   [37m# Set the status to unchecked.[39;49;00m$
   219	   [37m#[39;49;00m$
   220	   [34mmethod[39;49;00m [32mclear_is_checked[39;49;00m()$
   221	      self[34m.[39;49;00mToggle[34m.[39;49;00mclear_is_checked()$
   222	      self[34m.[39;49;00minvalidate()$
   223	   [34mend[39;49;00m$
   224	$
   225	   [37m#[39;49;00m$
   226	   [37m# Set the button so that when it is pressed, it toggles[39;49;00m$
   227	   [37m# between two states, as indicated by the is_checked[39;49;00m$
   228	   [37m# flag.[39;49;00m$
   229	   [37m#[39;49;00m$
   230	   [37m# Instances of Checkbox have this flag on by default, but [39;49;00m$
   231	   [37m# TextButton and IconButton do not.  When the flag is on,[39;49;00m$
   232	   [37m# the latter classes indicate their checked status by[39;49;00m$
   233	   [37m# showing the button as being "down".[39;49;00m$
   234	   [37m#[39;49;00m$
   235	   [34mmethod[39;49;00m [32mset_toggles[39;49;00m()$
   236	      self[34m.[39;49;00mtoggles_flag := [34m1[39;49;00m$
   237	      self[34m.[39;49;00minvalidate()$
   238	   [34mend[39;49;00m$
   239	$
   240	   [37m#[39;49;00m$
   241	   [37m# Clear the toggles flag.[39;49;00m$
   242	   [37m#[39;49;00m$
   243	   [34mmethod[39;49;00m [32mclear_toggles[39;49;00m()$
   244	      self[34m.[39;49;00mtoggles_flag := [34m&null[39;49;00m$
   245	      self[34m.[39;49;00minvalidate()$
   246	   [34mend[39;49;00m$
   247	$
   248	   [37m#[39;49;00m$
   249	   [37m# Set the label of the button, if any.[39;49;00m$
   250	   [37m# @param x   The label[39;49;00m$
   251	   [37m#[39;49;00m$
   252	   [34mmethod[39;49;00m [32mset_label[39;49;00m([31mx[39;49;00m)$
   253	      self[34m.[39;49;00mlabel := x$
   254	      self[34m.[39;49;00minvalidate()$
   255	      [34mreturn[39;49;00m x$
   256	   [34mend[39;49;00m$
   257	$
   258	   [34mmethod[39;49;00m [32mset_one[39;49;00m([31mattr[39;49;00m, [31mval[39;49;00m)$
   259	      [34mcase[39;49;00m attr [34mof[39;49;00m {$
   260	         [33m"label"[39;49;00m : set_label(string_val(attr, val))$
   261	         [33m"is_checked"[39;49;00m :$
   262	            [34mif[39;49;00m test_flag(attr, val) [34mthen[39;49;00m$
   263	               set_is_checked()$
   264	            [34melse[39;49;00m$
   265	               clear_is_checked()$
   266	         [33m"toggles"[39;49;00m :$
   267	            [34mif[39;49;00m test_flag(attr, val) [34mthen[39;49;00m$
   268	               set_toggles()$
   269	            [34melse[39;49;00m$
   270	               clear_toggles()$
   271	         [33m"no_keyboard"[39;49;00m :$
   272	            [34mif[39;49;00m test_flag(attr, val) [34mthen[39;49;00m$
   273	               set_no_keyboard()$
   274	            [34melse[39;49;00m$
   275	               clear_no_keyboard()$
   276	         [34mdefault[39;49;00m: self[34m.[39;49;00mComponent[34m.[39;49;00mset_one(attr, val)$
   277	      }$
   278	   [34mend[39;49;00m$
   279	$
   280	   [34minitially[39;49;00m()$
   281	      self[34m.[39;49;00mComponent[34m.[39;49;00m[34minitially[39;49;00m()$
   282	      self[34m.[39;49;00maccepts_focus_flag := [34m1[39;49;00m$
   283	[34mend[39;49;00m$
