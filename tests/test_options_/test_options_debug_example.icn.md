Using lexer <pygments.lexers.UniconLexer with {'ensurenl': False, 'tabsize': 0}>
[37m#[39;49;00m
[37m# $Id: button.icn,v 1.7 2006-07-09 23:43:07 rparlett Exp $[39;49;00m
[37m#[39;49;00m
[37m# This file is in the public domain.[39;49;00m
[37m#[39;49;00m
[37m# Author: Robert Parlett (parlett@dial.pipex.com)[39;49;00m
[37m#[39;49;00m

[34mpackage[39;49;00m gui
[34mlink[39;49;00m graphics

[34m$include[39;49;00m [33m"guih.icn"[39;49;00m


[37m#[39;49;00m
[37m# This is the parent class of the button classes, including[39;49;00m
[37m# checkboxes.[39;49;00m
[37m#[39;49;00m
[37m# A {Button} produces a BUTTON_PRESS_EVENT when the button is[39;49;00m
[37m# depressed, and code BUTTON_RELEASE_EVENT when it is released,[39;49;00m
[37m# as well as an ACTION_EVENT.[39;49;00m
[37m# [39;49;00m
[37m# By default, when a button holds the keyboard focus a dashed[39;49;00m
[37m# line appears just within the button.  Then, when return is[39;49;00m
[37m# pressed an ACTION_EVENT is generated.  The method[39;49;00m
[37m# {Dialog.set_initial_focus()} can be used to have the button[39;49;00m
[37m# have the focus when the dialog is first displayed.[39;49;00m
[37m#[39;49;00m
[37m# Buttons also repeatedly produce a BUTTON_HELD_EVENT whilst they[39;49;00m
[37m# are held down, rather like a repeating keyboard press.  The[39;49;00m
[37m# delay between the initial repeat event and subsequent repeat[39;49;00m
[37m# events is set in the parent dialog (see above).[39;49;00m
[37m#[39;49;00m
[34mclass[39;49;00m [32mButton[39;49;00m : [32mToggle[39;49;00m : [32mComponent[39;49;00m(
   [31mis_down[39;49;00m,                 [37m#               [39;49;00m
   [31mis_held[39;49;00m,                 [37m#               [39;49;00m
   [31mis_checked_flag[39;49;00m,         [37m#                       [39;49;00m
   [31mlabel[39;49;00m,
   [31mimg_up[39;49;00m,                  [37m#              [39;49;00m
   [31mimg_down[39;49;00m,                [37m#                [39;49;00m
   [31mimg_w[39;49;00m,                   [37m#             [39;49;00m
   [31mimg_h[39;49;00m,                   [37m#             [39;49;00m
   [31mparent_check_box_group[39;49;00m,  [37m#[39;49;00m
   [31mparent_button_group[39;49;00m,     [37m#                           [39;49;00m
   [31mrepeat_delay[39;49;00m,
   [31mno_keyboard_flag[39;49;00m,        [37m#[39;49;00m
   [31mtoggles_flag[39;49;00m
   )

   [34mmethod[39;49;00m [32mset_parent_button_group[39;49;00m([31mx[39;49;00m)
      [34mreturn[39;49;00m self[34m.[39;49;00mparent_button_group := x
   [34mend[39;49;00m

   [37m#[39;49;00m
   [37m# Invoking this method disables the keyboard control over the[39;49;00m
   [37m# button described above.  No dashed line will ever appear in[39;49;00m
   [37m# the button display and return will have no effect on the[39;49;00m
   [37m# button even if it has the focus.[39;49;00m
   [37m#[39;49;00m
   [34mmethod[39;49;00m [32mset_no_keyboard[39;49;00m()
      self[34m.[39;49;00mno_keyboard_flag := [34m1[39;49;00m
      self[34m.[39;49;00maccepts_focus_flag := [34m&null[39;49;00m
   [34mend[39;49;00m

   [37m#[39;49;00m
   [37m# Clear the no keyboard behaviour (the default)[39;49;00m
   [37m#[39;49;00m
   [34mmethod[39;49;00m [32mclear_no_keyboard[39;49;00m()
      self[34m.[39;49;00mno_keyboard_flag := [34m&null[39;49;00m
      self[34m.[39;49;00maccepts_focus_flag := [34m1[39;49;00m
   [34mend[39;49;00m

   [34mmethod[39;49;00m [32mtick[39;49;00m()
      [34mif[39;49;00m dispatcher[34m.[39;49;00mcurr_time_of_day() > self[34m.[39;49;00mrepeat_delay [34mthen[39;49;00m
         fire(BUTTON_HELD_EVENT)
   [34mend[39;49;00m

   [34mmethod[39;49;00m [32mgo_down[39;49;00m()
      self[34m.[39;49;00mis_down := [34m1[39;49;00m
      set_ticker(self[34m.[39;49;00mparent_dialog[34m.[39;49;00mrepeat_rate)
   [34mend[39;49;00m

   [34mmethod[39;49;00m [32mgo_up[39;49;00m()
      self[34m.[39;49;00mis_down := [34m&null[39;49;00m
      stop_ticker()
   [34mend[39;49;00m

   [34mmethod[39;49;00m [32mhandle_press[39;49;00m([31me[39;49;00m)
      [34mlocal[39;49;00m b
      [34mif[39;49;00m self[34m.[39;49;00min_region() [34mthen[39;49;00m {
         go_down()
         self[34m.[39;49;00mrepeat_delay := dispatcher[34m.[39;49;00mcurr_time_of_day() + self[34m.[39;49;00mparent_dialog[34m.[39;49;00mrepeat_delay
         self[34m.[39;49;00mis_held := [34m1[39;49;00m
         [34mevery[39;49;00m b := !(\self[34m.[39;49;00mparent_button_group)[34m.[39;49;00mbuttons [34mdo[39;49;00m {
            [34mif[39;49;00m b[34m.[39;49;00mis_unhidden() [34mthen[39;49;00m {
               b[34m.[39;49;00mis_held := [34m1[39;49;00m
               b[34m.[39;49;00mrepeat_delay := self[34m.[39;49;00mrepeat_delay
            }
         }
         self[34m.[39;49;00minvalidate()
         fire(BUTTON_PRESS_EVENT, e)
      }
   [34mend[39;49;00m

   [34mmethod[39;49;00m [32mhandle_drag[39;49;00m([31me[39;49;00m)
      [34mif[39;49;00m \self[34m.[39;49;00mis_held [34mthen[39;49;00m {
         [37m#[39;49;00m
         [37m# Button held down; toggle on/off as it goes over the button [39;49;00m
         [37m#[39;49;00m
         [34mif[39;49;00m self[34m.[39;49;00min_region() [34mthen[39;49;00m {
            [34mif[39;49;00m /self[34m.[39;49;00mis_down [34mthen[39;49;00m {
               go_down()
               invalidate()
            }
         } [34melse[39;49;00m {
            [34mif[39;49;00m \self[34m.[39;49;00mis_down [34mthen[39;49;00m {
               go_up()
               invalidate()
            }
         }
      }
   [34mend[39;49;00m

   [34mmethod[39;49;00m [32mhandle_release[39;49;00m([31me[39;49;00m)
      [34mif[39;49;00m \self[34m.[39;49;00mis_held [34mthen[39;49;00m {
         self[34m.[39;49;00mis_held := [34m&null[39;49;00m
         [34mif[39;49;00m \self[34m.[39;49;00mis_down [34mthen[39;49;00m {
            go_up()
            fire(BUTTON_RELEASE_EVENT, e)
            on_action(e)
         }
      }
   [34mend[39;49;00m

   [34mmethod[39;49;00m [32mon_action[39;49;00m([31me[39;49;00m)
      [34mif[39;49;00m \self[34m.[39;49;00mtoggles_flag [34mthen[39;49;00m {
         [34mif[39;49;00m \self[34m.[39;49;00mparent_check_box_group [34mthen[39;49;00m
            self[34m.[39;49;00mparent_check_box_group[34m.[39;49;00mset_which_one(self)
         [34melse[39;49;00m
            self[34m.[39;49;00mtoggle_is_checked()
      }
      self[34m.[39;49;00minvalidate()
      fire(ACTION_EVENT, e)
   [34mend[39;49;00m

   [34mmethod[39;49;00m [32mhandle_accel[39;49;00m([31me[39;49;00m)
      self[34m.[39;49;00mComponent[34m.[39;49;00mhandle_accel(e)
      on_action(e)
   [34mend[39;49;00m

   [34mmethod[39;49;00m [32mhandle_default[39;49;00m([31me[39;49;00m)
      [34mif[39;49;00m \self[34m.[39;49;00mhas_focus [34mthen[39;49;00m {
         [34mif[39;49;00m /self[34m.[39;49;00mno_keyboard_flag & e == ([33m"\r"[39;49;00m | [33m"\l"[39;49;00m | [33m" "[39;49;00m) [34mthen[39;49;00m {
            on_action(e)
         }
      }
   [34mend[39;49;00m

   [34mmethod[39;49;00m [32mhandle_event[39;49;00m([31me[39;49;00m)
      [34mif[39;49;00m e === ([34m&lpress[39;49;00m | [34m&rpress[39;49;00m | [34m&mpress[39;49;00m) [34mthen[39;49;00m {
         handle_press(e)
      } [34melse[39;49;00m [34mif[39;49;00m e === ([34m&ldrag[39;49;00m | [34m&rdrag[39;49;00m | [34m&mdrag[39;49;00m) [34mthen[39;49;00m {
         handle_drag(e)
      } [34melse[39;49;00m [34mif[39;49;00m e === ([34m&lrelease[39;49;00m | [34m&rrelease[39;49;00m | [34m&mrelease[39;49;00m) [34mthen[39;49;00m {
         handle_release(e)
      } [34melse[39;49;00m
         handle_default(e)
   [34mend[39;49;00m

   [37m#[39;49;00m
   [37m# Set the up/down images (if any) to the strings provided,[39;49;00m
   [37m# which should be in Icon image format.[39;49;00m
   [37m# The two images must have the same dimensions.[39;49;00m
   [37m# @param x   The up image[39;49;00m
   [37m# @param y   The down image[39;49;00m
   [37m#[39;49;00m
   [34mmethod[39;49;00m [32mset_imgs[39;49;00m([31mx[39;49;00m, [31my[39;49;00m)
      self[34m.[39;49;00mimg_up := x
      self[34m.[39;49;00mimg_w := img_width(x) = img_width(y) | fatal([33m"Image widths differ"[39;49;00m)
      self[34m.[39;49;00mimg_h := img_height(x) = img_height(y) | fatal([33m"Image heights differ"[39;49;00m)

      self[34m.[39;49;00mimg_down := y

      [34mreturn[39;49;00m
   [34mend[39;49;00m

   [37m#[39;49;00m
   [37m# Set the image (if any) to the given string, which should be in Icon image[39;49;00m
   [37m# format.[39;49;00m
   [37m# @param x   The image[39;49;00m
   [37m#[39;49;00m
   [34mmethod[39;49;00m [32mset_img[39;49;00m([31mx[39;49;00m)
      self[34m.[39;49;00mimg_up := self[34m.[39;49;00mimg_down := x
      self[34m.[39;49;00mimg_w := img_width(x)
      self[34m.[39;49;00mimg_h := img_height(x)
      [34mreturn[39;49;00m x
   [34mend[39;49;00m

   [37m#[39;49;00m
   [37m# Toggle the checked status of the button.  This method, and[39;49;00m
   [37m# the following two methods, may be[39;49;00m
   [37m# inappropriate for non-toggle styles of button.[39;49;00m
   [37m#[39;49;00m
   [34mmethod[39;49;00m [32mtoggle_is_checked[39;49;00m()
      self[34m.[39;49;00mToggle[34m.[39;49;00mtoggle_is_checked()
      self[34m.[39;49;00minvalidate()
   [34mend[39;49;00m

   [37m#[39;49;00m
   [37m# Set the status to checked.[39;49;00m
   [37m#[39;49;00m
   [34mmethod[39;49;00m [32mset_is_checked[39;49;00m()
      self[34m.[39;49;00mToggle[34m.[39;49;00mset_is_checked()
      self[34m.[39;49;00minvalidate()
   [34mend[39;49;00m

   [37m#[39;49;00m
   [37m# Set the status to unchecked.[39;49;00m
   [37m#[39;49;00m
   [34mmethod[39;49;00m [32mclear_is_checked[39;49;00m()
      self[34m.[39;49;00mToggle[34m.[39;49;00mclear_is_checked()
      self[34m.[39;49;00minvalidate()
   [34mend[39;49;00m

   [37m#[39;49;00m
   [37m# Set the button so that when it is pressed, it toggles[39;49;00m
   [37m# between two states, as indicated by the is_checked[39;49;00m
   [37m# flag.[39;49;00m
   [37m#[39;49;00m
   [37m# Instances of Checkbox have this flag on by default, but [39;49;00m
   [37m# TextButton and IconButton do not.  When the flag is on,[39;49;00m
   [37m# the latter classes indicate their checked status by[39;49;00m
   [37m# showing the button as being "down".[39;49;00m
   [37m#[39;49;00m
   [34mmethod[39;49;00m [32mset_toggles[39;49;00m()
      self[34m.[39;49;00mtoggles_flag := [34m1[39;49;00m
      self[34m.[39;49;00minvalidate()
   [34mend[39;49;00m

   [37m#[39;49;00m
   [37m# Clear the toggles flag.[39;49;00m
   [37m#[39;49;00m
   [34mmethod[39;49;00m [32mclear_toggles[39;49;00m()
      self[34m.[39;49;00mtoggles_flag := [34m&null[39;49;00m
      self[34m.[39;49;00minvalidate()
   [34mend[39;49;00m

   [37m#[39;49;00m
   [37m# Set the label of the button, if any.[39;49;00m
   [37m# @param x   The label[39;49;00m
   [37m#[39;49;00m
   [34mmethod[39;49;00m [32mset_label[39;49;00m([31mx[39;49;00m)
      self[34m.[39;49;00mlabel := x
      self[34m.[39;49;00minvalidate()
      [34mreturn[39;49;00m x
   [34mend[39;49;00m

   [34mmethod[39;49;00m [32mset_one[39;49;00m([31mattr[39;49;00m, [31mval[39;49;00m)
      [34mcase[39;49;00m attr [34mof[39;49;00m {
         [33m"label"[39;49;00m : set_label(string_val(attr, val))
         [33m"is_checked"[39;49;00m :
            [34mif[39;49;00m test_flag(attr, val) [34mthen[39;49;00m
               set_is_checked()
            [34melse[39;49;00m
               clear_is_checked()
         [33m"toggles"[39;49;00m :
            [34mif[39;49;00m test_flag(attr, val) [34mthen[39;49;00m
               set_toggles()
            [34melse[39;49;00m
               clear_toggles()
         [33m"no_keyboard"[39;49;00m :
            [34mif[39;49;00m test_flag(attr, val) [34mthen[39;49;00m
               set_no_keyboard()
            [34melse[39;49;00m
               clear_no_keyboard()
         [34mdefault[39;49;00m: self[34m.[39;49;00mComponent[34m.[39;49;00mset_one(attr, val)
      }
   [34mend[39;49;00m

   [34minitially[39;49;00m()
      self[34m.[39;49;00mComponent[34m.[39;49;00m[34minitially[39;49;00m()
      self[34m.[39;49;00maccepts_focus_flag := [34m1[39;49;00m
[34mend[39;49;00m
