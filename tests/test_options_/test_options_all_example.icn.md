     1^I[37m#[39;49;00m$
     2^I[37m# $Id: button.icn,v 1.7 2006-07-09 23:43:07 rparlett Exp $[39;49;00m$
     3^I[37m#[39;49;00m$
     4^I[37m# This file is in the public domain.[39;49;00m$
     5^I[37m#[39;49;00m$
     6^I[37m# Author: Robert Parlett (parlett@dial.pipex.com)[39;49;00m$
     7^I[37m#[39;49;00m$
     8^I$
     9^I[34mpackage[39;49;00m gui$
    10^I[34mlink[39;49;00m graphics$
    11^I$
    12^I[34m$include[39;49;00m [33m"guih.icn"[39;49;00m$
    13^I$
    14^I$
    15^I[37m#[39;49;00m$
    16^I[37m# This is the parent class of the button classes, including[39;49;00m$
    17^I[37m# checkboxes.[39;49;00m$
    18^I[37m#[39;49;00m$
    19^I[37m# A {Button} produces a BUTTON_PRESS_EVENT when the button is[39;49;00m$
    20^I[37m# depressed, and code BUTTON_RELEASE_EVENT when it is released,[39;49;00m$
    21^I[37m# as well as an ACTION_EVENT.[39;49;00m$
    22^I[37m# [39;49;00m$
    23^I[37m# By default, when a button holds the keyboard focus a dashed[39;49;00m$
    24^I[37m# line appears just within the button.  Then, when return is[39;49;00m$
    25^I[37m# pressed an ACTION_EVENT is generated.  The method[39;49;00m$
    26^I[37m# {Dialog.set_initial_focus()} can be used to have the button[39;49;00m$
    27^I[37m# have the focus when the dialog is first displayed.[39;49;00m$
    28^I[37m#[39;49;00m$
    29^I[37m# Buttons also repeatedly produce a BUTTON_HELD_EVENT whilst they[39;49;00m$
    30^I[37m# are held down, rather like a repeating keyboard press.  The[39;49;00m$
    31^I[37m# delay between the initial repeat event and subsequent repeat[39;49;00m$
    32^I[37m# events is set in the parent dialog (see above).[39;49;00m$
    33^I[37m#[39;49;00m$
    34^I[34mclass[39;49;00m [32mButton[39;49;00m : [32mToggle[39;49;00m : [32mComponent[39;49;00m($
    35^I   [31mis_down[39;49;00m,                 [37m#               [39;49;00m$
    36^I   [31mis_held[39;49;00m,                 [37m#               [39;49;00m$
    37^I   [31mis_checked_flag[39;49;00m,         [37m#                       [39;49;00m$
    38^I   [31mlabel[39;49;00m,$
    39^I   [31mimg_up[39;49;00m,                  [37m#              [39;49;00m$
    40^I   [31mimg_down[39;49;00m,                [37m#                [39;49;00m$
    41^I   [31mimg_w[39;49;00m,                   [37m#             [39;49;00m$
    42^I   [31mimg_h[39;49;00m,                   [37m#             [39;49;00m$
    43^I   [31mparent_check_box_group[39;49;00m,  [37m#[39;49;00m$
    44^I   [31mparent_button_group[39;49;00m,     [37m#                           [39;49;00m$
    45^I   [31mrepeat_delay[39;49;00m,$
    46^I   [31mno_keyboard_flag[39;49;00m,        [37m#[39;49;00m$
    47^I   [31mtoggles_flag[39;49;00m$
    48^I   )$
    49^I$
    50^I   [34mmethod[39;49;00m [32mset_parent_button_group[39;49;00m([31mx[39;49;00m)$
    51^I      [34mreturn[39;49;00m self[34m.[39;49;00mparent_button_group := x$
    52^I   [34mend[39;49;00m$
    53^I$
    54^I   [37m#[39;49;00m$
    55^I   [37m# Invoking this method disables the keyboard control over the[39;49;00m$
    56^I   [37m# button described above.  No dashed line will ever appear in[39;49;00m$
    57^I   [37m# the button display and return will have no effect on the[39;49;00m$
    58^I   [37m# button even if it has the focus.[39;49;00m$
    59^I   [37m#[39;49;00m$
    60^I   [34mmethod[39;49;00m [32mset_no_keyboard[39;49;00m()$
    61^I      self[34m.[39;49;00mno_keyboard_flag := [34m1[39;49;00m$
    62^I      self[34m.[39;49;00maccepts_focus_flag := [34m&null[39;49;00m$
    63^I   [34mend[39;49;00m$
    64^I   $
    65^I   [37m#[39;49;00m$
    66^I   [37m# Clear the no keyboard behaviour (the default)[39;49;00m$
    67^I   [37m#[39;49;00m$
    68^I   [34mmethod[39;49;00m [32mclear_no_keyboard[39;49;00m()$
    69^I      self[34m.[39;49;00mno_keyboard_flag := [34m&null[39;49;00m$
    70^I      self[34m.[39;49;00maccepts_focus_flag := [34m1[39;49;00m$
    71^I   [34mend[39;49;00m$
    72^I$
    73^I   [34mmethod[39;49;00m [32mtick[39;49;00m()$
    74^I      [34mif[39;49;00m dispatcher[34m.[39;49;00mcurr_time_of_day() > self[34m.[39;49;00mrepeat_delay [34mthen[39;49;00m$
    75^I         fire(BUTTON_HELD_EVENT)$
    76^I   [34mend[39;49;00m$
    77^I$
    78^I   [34mmethod[39;49;00m [32mgo_down[39;49;00m()$
    79^I      self[34m.[39;49;00mis_down := [34m1[39;49;00m$
    80^I      set_ticker(self[34m.[39;49;00mparent_dialog[34m.[39;49;00mrepeat_rate)$
    81^I   [34mend[39;49;00m$
    82^I$
    83^I   [34mmethod[39;49;00m [32mgo_up[39;49;00m()$
    84^I      self[34m.[39;49;00mis_down := [34m&null[39;49;00m$
    85^I      stop_ticker()$
    86^I   [34mend[39;49;00m$
    87^I$
    88^I   [34mmethod[39;49;00m [32mhandle_press[39;49;00m([31me[39;49;00m)$
    89^I      [34mlocal[39;49;00m b$
    90^I      [34mif[39;49;00m self[34m.[39;49;00min_region() [34mthen[39;49;00m {$
    91^I         go_down()$
    92^I         self[34m.[39;49;00mrepeat_delay := dispatcher[34m.[39;49;00mcurr_time_of_day() + self[34m.[39;49;00mparent_dialog[34m.[39;49;00mrepeat_delay$
    93^I         self[34m.[39;49;00mis_held := [34m1[39;49;00m$
    94^I         [34mevery[39;49;00m b := !(\self[34m.[39;49;00mparent_button_group)[34m.[39;49;00mbuttons [34mdo[39;49;00m {$
    95^I            [34mif[39;49;00m b[34m.[39;49;00mis_unhidden() [34mthen[39;49;00m {$
    96^I               b[34m.[39;49;00mis_held := [34m1[39;49;00m$
    97^I               b[34m.[39;49;00mrepeat_delay := self[34m.[39;49;00mrepeat_delay$
    98^I            }$
    99^I         }$
   100^I         self[34m.[39;49;00minvalidate()$
   101^I         fire(BUTTON_PRESS_EVENT, e)$
   102^I      }$
   103^I   [34mend[39;49;00m$
   104^I$
   105^I   [34mmethod[39;49;00m [32mhandle_drag[39;49;00m([31me[39;49;00m)$
   106^I      [34mif[39;49;00m \self[34m.[39;49;00mis_held [34mthen[39;49;00m {$
   107^I         [37m#[39;49;00m$
   108^I         [37m# Button held down; toggle on/off as it goes over the button [39;49;00m$
   109^I         [37m#[39;49;00m$
   110^I         [34mif[39;49;00m self[34m.[39;49;00min_region() [34mthen[39;49;00m {$
   111^I            [34mif[39;49;00m /self[34m.[39;49;00mis_down [34mthen[39;49;00m {$
   112^I               go_down()$
   113^I               invalidate()$
   114^I            }$
   115^I         } [34melse[39;49;00m {$
   116^I            [34mif[39;49;00m \self[34m.[39;49;00mis_down [34mthen[39;49;00m {$
   117^I               go_up()$
   118^I               invalidate()$
   119^I            }$
   120^I         }$
   121^I      }$
   122^I   [34mend[39;49;00m$
   123^I$
   124^I   [34mmethod[39;49;00m [32mhandle_release[39;49;00m([31me[39;49;00m)$
   125^I      [34mif[39;49;00m \self[34m.[39;49;00mis_held [34mthen[39;49;00m {$
   126^I         self[34m.[39;49;00mis_held := [34m&null[39;49;00m$
   127^I         [34mif[39;49;00m \self[34m.[39;49;00mis_down [34mthen[39;49;00m {$
   128^I            go_up()$
   129^I            fire(BUTTON_RELEASE_EVENT, e)$
   130^I            on_action(e)$
   131^I         }$
   132^I      }$
   133^I   [34mend[39;49;00m$
   134^I$
   135^I   [34mmethod[39;49;00m [32mon_action[39;49;00m([31me[39;49;00m)$
   136^I      [34mif[39;49;00m \self[34m.[39;49;00mtoggles_flag [34mthen[39;49;00m {$
   137^I         [34mif[39;49;00m \self[34m.[39;49;00mparent_check_box_group [34mthen[39;49;00m$
   138^I            self[34m.[39;49;00mparent_check_box_group[34m.[39;49;00mset_which_one(self)$
   139^I         [34melse[39;49;00m$
   140^I            self[34m.[39;49;00mtoggle_is_checked()$
   141^I      }$
   142^I      self[34m.[39;49;00minvalidate()$
   143^I      fire(ACTION_EVENT, e)$
   144^I   [34mend[39;49;00m$
   145^I$
   146^I   [34mmethod[39;49;00m [32mhandle_accel[39;49;00m([31me[39;49;00m)$
   147^I      self[34m.[39;49;00mComponent[34m.[39;49;00mhandle_accel(e)$
   148^I      on_action(e)$
   149^I   [34mend[39;49;00m$
   150^I$
   151^I   [34mmethod[39;49;00m [32mhandle_default[39;49;00m([31me[39;49;00m)$
   152^I      [34mif[39;49;00m \self[34m.[39;49;00mhas_focus [34mthen[39;49;00m {$
   153^I         [34mif[39;49;00m /self[34m.[39;49;00mno_keyboard_flag & e == ([33m"\r"[39;49;00m | [33m"\l"[39;49;00m | [33m" "[39;49;00m) [34mthen[39;49;00m {$
   154^I            on_action(e)$
   155^I         }$
   156^I      }$
   157^I   [34mend[39;49;00m$
   158^I$
   159^I   [34mmethod[39;49;00m [32mhandle_event[39;49;00m([31me[39;49;00m)$
   160^I      [34mif[39;49;00m e === ([34m&lpress[39;49;00m | [34m&rpress[39;49;00m | [34m&mpress[39;49;00m) [34mthen[39;49;00m {$
   161^I         handle_press(e)$
   162^I      } [34melse[39;49;00m [34mif[39;49;00m e === ([34m&ldrag[39;49;00m | [34m&rdrag[39;49;00m | [34m&mdrag[39;49;00m) [34mthen[39;49;00m {$
   163^I         handle_drag(e)$
   164^I      } [34melse[39;49;00m [34mif[39;49;00m e === ([34m&lrelease[39;49;00m | [34m&rrelease[39;49;00m | [34m&mrelease[39;49;00m) [34mthen[39;49;00m {$
   165^I         handle_release(e)$
   166^I      } [34melse[39;49;00m $
   167^I         handle_default(e)$
   168^I   [34mend[39;49;00m$
   169^I$
   170^I   [37m#[39;49;00m$
   171^I   [37m# Set the up/down images (if any) to the strings provided,[39;49;00m$
   172^I   [37m# which should be in Icon image format.[39;49;00m$
   173^I   [37m# The two images must have the same dimensions.[39;49;00m$
   174^I   [37m# @param x   The up image[39;49;00m$
   175^I   [37m# @param y   The down image[39;49;00m$
   176^I   [37m#[39;49;00m$
   177^I   [34mmethod[39;49;00m [32mset_imgs[39;49;00m([31mx[39;49;00m, [31my[39;49;00m)$
   178^I      self[34m.[39;49;00mimg_up := x$
   179^I      self[34m.[39;49;00mimg_w := img_width(x) = img_width(y) | fatal([33m"Image widths differ"[39;49;00m)$
   180^I      self[34m.[39;49;00mimg_h := img_height(x) = img_height(y) | fatal([33m"Image heights differ"[39;49;00m)$
   181^I$
   182^I      self[34m.[39;49;00mimg_down := y$
   183^I$
   184^I      [34mreturn[39;49;00m$
   185^I   [34mend[39;49;00m$
   186^I$
   187^I   [37m#[39;49;00m$
   188^I   [37m# Set the image (if any) to the given string, which should be in Icon image[39;49;00m$
   189^I   [37m# format.[39;49;00m$
   190^I   [37m# @param x   The image[39;49;00m$
   191^I   [37m#[39;49;00m$
   192^I   [34mmethod[39;49;00m [32mset_img[39;49;00m([31mx[39;49;00m)$
   193^I      self[34m.[39;49;00mimg_up := self[34m.[39;49;00mimg_down := x$
   194^I      self[34m.[39;49;00mimg_w := img_width(x)$
   195^I      self[34m.[39;49;00mimg_h := img_height(x)$
   196^I      [34mreturn[39;49;00m x$
   197^I   [34mend[39;49;00m$
   198^I$
   199^I   [37m#[39;49;00m$
   200^I   [37m# Toggle the checked status of the button.  This method, and[39;49;00m$
   201^I   [37m# the following two methods, may be[39;49;00m$
   202^I   [37m# inappropriate for non-toggle styles of button.[39;49;00m$
   203^I   [37m#[39;49;00m$
   204^I   [34mmethod[39;49;00m [32mtoggle_is_checked[39;49;00m()$
   205^I      self[34m.[39;49;00mToggle[34m.[39;49;00mtoggle_is_checked()$
   206^I      self[34m.[39;49;00minvalidate()$
   207^I   [34mend[39;49;00m$
   208^I$
   209^I   [37m#[39;49;00m$
   210^I   [37m# Set the status to checked.[39;49;00m$
   211^I   [37m#[39;49;00m$
   212^I   [34mmethod[39;49;00m [32mset_is_checked[39;49;00m()$
   213^I      self[34m.[39;49;00mToggle[34m.[39;49;00mset_is_checked()$
   214^I      self[34m.[39;49;00minvalidate()$
   215^I   [34mend[39;49;00m$
   216^I$
   217^I   [37m#[39;49;00m$
   218^I   [37m# Set the status to unchecked.[39;49;00m$
   219^I   [37m#[39;49;00m$
   220^I   [34mmethod[39;49;00m [32mclear_is_checked[39;49;00m()$
   221^I      self[34m.[39;49;00mToggle[34m.[39;49;00mclear_is_checked()$
   222^I      self[34m.[39;49;00minvalidate()$
   223^I   [34mend[39;49;00m$
   224^I$
   225^I   [37m#[39;49;00m$
   226^I   [37m# Set the button so that when it is pressed, it toggles[39;49;00m$
   227^I   [37m# between two states, as indicated by the is_checked[39;49;00m$
   228^I   [37m# flag.[39;49;00m$
   229^I   [37m#[39;49;00m$
   230^I   [37m# Instances of Checkbox have this flag on by default, but [39;49;00m$
   231^I   [37m# TextButton and IconButton do not.  When the flag is on,[39;49;00m$
   232^I   [37m# the latter classes indicate their checked status by[39;49;00m$
   233^I   [37m# showing the button as being "down".[39;49;00m$
   234^I   [37m#[39;49;00m$
   235^I   [34mmethod[39;49;00m [32mset_toggles[39;49;00m()$
   236^I      self[34m.[39;49;00mtoggles_flag := [34m1[39;49;00m$
   237^I      self[34m.[39;49;00minvalidate()$
   238^I   [34mend[39;49;00m$
   239^I$
   240^I   [37m#[39;49;00m$
   241^I   [37m# Clear the toggles flag.[39;49;00m$
   242^I   [37m#[39;49;00m$
   243^I   [34mmethod[39;49;00m [32mclear_toggles[39;49;00m()$
   244^I      self[34m.[39;49;00mtoggles_flag := [34m&null[39;49;00m$
   245^I      self[34m.[39;49;00minvalidate()$
   246^I   [34mend[39;49;00m$
   247^I$
   248^I   [37m#[39;49;00m$
   249^I   [37m# Set the label of the button, if any.[39;49;00m$
   250^I   [37m# @param x   The label[39;49;00m$
   251^I   [37m#[39;49;00m$
   252^I   [34mmethod[39;49;00m [32mset_label[39;49;00m([31mx[39;49;00m)$
   253^I      self[34m.[39;49;00mlabel := x$
   254^I      self[34m.[39;49;00minvalidate()$
   255^I      [34mreturn[39;49;00m x$
   256^I   [34mend[39;49;00m$
   257^I$
   258^I   [34mmethod[39;49;00m [32mset_one[39;49;00m([31mattr[39;49;00m, [31mval[39;49;00m)$
   259^I      [34mcase[39;49;00m attr [34mof[39;49;00m {$
   260^I         [33m"label"[39;49;00m : set_label(string_val(attr, val))$
   261^I         [33m"is_checked"[39;49;00m :$
   262^I            [34mif[39;49;00m test_flag(attr, val) [34mthen[39;49;00m$
   263^I               set_is_checked()$
   264^I            [34melse[39;49;00m$
   265^I               clear_is_checked()$
   266^I         [33m"toggles"[39;49;00m :$
   267^I            [34mif[39;49;00m test_flag(attr, val) [34mthen[39;49;00m$
   268^I               set_toggles()$
   269^I            [34melse[39;49;00m$
   270^I               clear_toggles()$
   271^I         [33m"no_keyboard"[39;49;00m :$
   272^I            [34mif[39;49;00m test_flag(attr, val) [34mthen[39;49;00m$
   273^I               set_no_keyboard()$
   274^I            [34melse[39;49;00m$
   275^I               clear_no_keyboard()$
   276^I         [34mdefault[39;49;00m: self[34m.[39;49;00mComponent[34m.[39;49;00mset_one(attr, val)$
   277^I      }$
   278^I   [34mend[39;49;00m$
   279^I$
   280^I   [34minitially[39;49;00m()$
   281^I      self[34m.[39;49;00mComponent[34m.[39;49;00m[34minitially[39;49;00m()$
   282^I      self[34m.[39;49;00maccepts_focus_flag := [34m1[39;49;00m$
   283^I[34mend[39;49;00m$
