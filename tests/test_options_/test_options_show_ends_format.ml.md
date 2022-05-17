[37m(*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*)[39;49;00m$
[37m(*[39;49;00m[37m                                                                     [39;49;00m[37m*)[39;49;00m$
[37m(*[39;49;00m[37m                           Objective Caml                            [39;49;00m[37m*)[39;49;00m$
[37m(*[39;49;00m[37m                                                                     [39;49;00m[37m*)[39;49;00m$
[37m(*[39;49;00m[37m            Pierre Weis, projet Cristal, INRIA Rocquencourt          [39;49;00m[37m*)[39;49;00m$
[37m(*[39;49;00m[37m                                                                     [39;49;00m[37m*)[39;49;00m$
[37m(*[39;49;00m[37m  Copyright 1996 Institut National de Recherche en Informatique et   [39;49;00m[37m*)[39;49;00m$
[37m(*[39;49;00m[37m  en Automatique.  All rights reserved.  This file is distributed    [39;49;00m[37m*)[39;49;00m$
[37m(*[39;49;00m[37m  under the terms of the GNU Library General Public License, with    [39;49;00m[37m*)[39;49;00m$
[37m(*[39;49;00m[37m  the special exception on linking described in file ../LICENSE.     [39;49;00m[37m*)[39;49;00m$
[37m(*[39;49;00m[37m                                                                     [39;49;00m[37m*)[39;49;00m$
[37m(*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*)[39;49;00m$
$
[37m(*[39;49;00m[37m $Id: format.ml,v 1.65 2005/09/26 10:13:08 weis Exp $ [39;49;00m[37m*)[39;49;00m$
$
[37m(*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m  Data structures definitions.[39;49;00m$
[37m[39;49;00m$
[37m [39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*)[39;49;00m$
$
[34mtype[39;49;00m size;;$
$
[34mexternal[39;49;00m size_of_int : [36mint[39;49;00m -> size = [33m"[39;49;00m[33m%identity[39;49;00m[33m"[39;49;00m;;$
[34mexternal[39;49;00m int_of_size : size -> [36mint[39;49;00m = [33m"[39;49;00m[33m%identity[39;49;00m[33m"[39;49;00m;;$
$
[37m(*[39;49;00m[37m Tokens are one of the following : [39;49;00m[37m*)[39;49;00m$
$
[34mtype[39;49;00m pp_token =$
| [04m[32mPp_text[39;49;00m [34mof[39;49;00m [36mstring[39;49;00m            [37m(*[39;49;00m[37m normal text [39;49;00m[37m*)[39;49;00m$
| [04m[32mPp_break[39;49;00m [34mof[39;49;00m [36mint[39;49;00m * [36mint[39;49;00m        [37m(*[39;49;00m[37m complete break [39;49;00m[37m*)[39;49;00m$
| [04m[32mPp_tbreak[39;49;00m [34mof[39;49;00m [36mint[39;49;00m * [36mint[39;49;00m       [37m(*[39;49;00m[37m go to next tabulation [39;49;00m[37m*)[39;49;00m$
| [04m[32mPp_stab[39;49;00m                      [37m(*[39;49;00m[37m set a tabulation [39;49;00m[37m*)[39;49;00m$
| [04m[32mPp_begin[39;49;00m [34mof[39;49;00m [36mint[39;49;00m * block_type [37m(*[39;49;00m[37m beginning of a block [39;49;00m[37m*)[39;49;00m$
| [04m[32mPp_end[39;49;00m                       [37m(*[39;49;00m[37m end of a block [39;49;00m[37m*)[39;49;00m$
| [04m[32mPp_tbegin[39;49;00m [34mof[39;49;00m tblock          [37m(*[39;49;00m[37m beginning of a tabulation block [39;49;00m[37m*)[39;49;00m$
| [04m[32mPp_tend[39;49;00m                      [37m(*[39;49;00m[37m end of a tabulation block [39;49;00m[37m*)[39;49;00m$
| [04m[32mPp_newline[39;49;00m                   [37m(*[39;49;00m[37m to force a newline inside a block [39;49;00m[37m*)[39;49;00m$
| [04m[32mPp_if_newline[39;49;00m                [37m(*[39;49;00m[37m to do something only if this very[39;49;00m$
[37m                                  line has been broken [39;49;00m[37m*)[39;49;00m$
| [04m[32mPp_open_tag[39;49;00m [34mof[39;49;00m [36mstring[39;49;00m        [37m(*[39;49;00m[37m opening a tag name [39;49;00m[37m*)[39;49;00m$
| [04m[32mPp_close_tag[39;49;00m                 [37m(*[39;49;00m[37m closing the most recently opened tag [39;49;00m[37m*)[39;49;00m$
$
[35mand[39;49;00m tag = [36mstring[39;49;00m$
$
[35mand[39;49;00m block_type =$
| [04m[32mPp_hbox[39;49;00m   [37m(*[39;49;00m[37m Horizontal block no line breaking [39;49;00m[37m*)[39;49;00m$
| [04m[32mPp_vbox[39;49;00m   [37m(*[39;49;00m[37m Vertical block each break leads to a new line [39;49;00m[37m*)[39;49;00m$
| [04m[32mPp_hvbox[39;49;00m  [37m(*[39;49;00m[37m Horizontal-vertical block: same as vbox, except if this block[39;49;00m$
[37m               is small enough to fit on a single line [39;49;00m[37m*)[39;49;00m$
| [04m[32mPp_hovbox[39;49;00m [37m(*[39;49;00m[37m Horizontal or Vertical block: breaks lead to new line[39;49;00m$
[37m               only when necessary to print the content of the block [39;49;00m[37m*)[39;49;00m$
| [04m[32mPp_box[39;49;00m    [37m(*[39;49;00m[37m Horizontal or Indent block: breaks lead to new line[39;49;00m$
[37m               only when necessary to print the content of the block, or[39;49;00m$
[37m               when it leads to a new indentation of the current line [39;49;00m[37m*)[39;49;00m$
| [04m[32mPp_fits[39;49;00m   [37m(*[39;49;00m[37m Internal usage: when a block fits on a single line [39;49;00m[37m*)[39;49;00m$
$
[35mand[39;49;00m tblock = [04m[32mPp_tbox[39;49;00m [34mof[39;49;00m [36mint[39;49;00m [36mlist[39;49;00m ref  [37m(*[39;49;00m[37m Tabulation box [39;49;00m[37m*)[39;49;00m$
;;$
$
[37m(*[39;49;00m[37m The Queue:[39;49;00m$
[37m   contains all formatting elements.[39;49;00m$
[37m   elements are tuples [39;49;00m[37m([39;49;00m[37msize, token, length[39;49;00m[37m)[39;49;00m[37m, where[39;49;00m$
[37m   size is set when the size of the block is known[39;49;00m$
[37m   len is the declared length of the token. [39;49;00m[37m*)[39;49;00m$
[34mtype[39;49;00m pp_queue_elem = {$
  [34mmutable[39;49;00m elem_size : size; token : pp_token; length : [36mint[39;49;00m$
};;$
$
[37m(*[39;49;00m[37m Scan stack:[39;49;00m$
[37m   each element is [39;49;00m[37m([39;49;00m[37mleft_total, queue element[39;49;00m[37m)[39;49;00m[37m where left_total[39;49;00m$
[37m   is the value of pp_left_total when the element has been enqueued. [39;49;00m[37m*)[39;49;00m$
[34mtype[39;49;00m pp_scan_elem = [04m[32mScan_elem[39;49;00m [34mof[39;49;00m [36mint[39;49;00m * pp_queue_elem;;$
$
[37m(*[39;49;00m[37m Formatting stack:[39;49;00m$
[37m   used to break the lines while printing tokens.[39;49;00m$
[37m   The formatting stack contains the description of[39;49;00m$
[37m   the currently active blocks. [39;49;00m[37m*)[39;49;00m$
[34mtype[39;49;00m pp_format_elem = [04m[32mFormat_elem[39;49;00m [34mof[39;49;00m block_type * [36mint[39;49;00m;;$
$
[37m(*[39;49;00m[37m General purpose queues, used in the formatter. [39;49;00m[37m*)[39;49;00m$
[34mtype[39;49;00m [34m'[39;49;00ma queue_elem = | [04m[32mNil[39;49;00m | [04m[32mCons[39;49;00m [34mof[39;49;00m [34m'[39;49;00ma queue_cell$
[35mand[39;49;00m [34m'[39;49;00ma queue_cell = {[34mmutable[39;49;00m head : [34m'[39;49;00ma; [34mmutable[39;49;00m tail : [34m'[39;49;00ma queue_elem};;$
$
[34mtype[39;49;00m [34m'[39;49;00ma queue = {$
 [34mmutable[39;49;00m insert : [34m'[39;49;00ma queue_elem;$
 [34mmutable[39;49;00m body : [34m'[39;49;00ma queue_elem$
};;$
$
[37m(*[39;49;00m[37m The formatter specific tag handling functions. [39;49;00m[37m*)[39;49;00m$
[34mtype[39;49;00m formatter_tag_functions = {$
 mark_open_tag : tag -> [36mstring[39;49;00m;$
 mark_close_tag : tag -> [36mstring[39;49;00m;$
 print_open_tag : tag -> [36munit[39;49;00m;$
 print_close_tag : tag -> [36munit[39;49;00m;$
$
};;$
$
[37m(*[39;49;00m[37m A formatter with all its machinery. [39;49;00m[37m*)[39;49;00m$
[34mtype[39;49;00m formatter = {$
 [34mmutable[39;49;00m pp_scan_stack : pp_scan_elem [36mlist[39;49;00m;$
 [34mmutable[39;49;00m pp_format_stack : pp_format_elem [36mlist[39;49;00m;$
 [34mmutable[39;49;00m pp_tbox_stack : tblock [36mlist[39;49;00m;$
 [34mmutable[39;49;00m pp_tag_stack : tag [36mlist[39;49;00m;$
 [34mmutable[39;49;00m pp_mark_stack : tag [36mlist[39;49;00m;$
 [37m(*[39;49;00m[37m Global variables: default initialization is[39;49;00m$
[37m    set_margin 78[39;49;00m$
[37m    set_min_space_left 0. [39;49;00m[37m*)[39;49;00m$
 [37m(*[39;49;00m[37m Value of right margin. [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_margin : [36mint[39;49;00m;$
 [37m(*[39;49;00m[37m Minimal space left before margin, when opening a block. [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_min_space_left : [36mint[39;49;00m;$
 [37m(*[39;49;00m[37m Maximum value of indentation:[39;49;00m$
[37m    no blocks can be opened further. [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_max_indent : [36mint[39;49;00m;$
 [37m(*[39;49;00m[37m Space remaining on the current line. [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_space_left : [36mint[39;49;00m;$
 [37m(*[39;49;00m[37m Current value of indentation. [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_current_indent : [36mint[39;49;00m;$
 [37m(*[39;49;00m[37m True when the line has been broken by the pretty-printer. [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_is_new_line : [36mbool[39;49;00m;$
 [37m(*[39;49;00m[37m Total width of tokens already printed. [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_left_total : [36mint[39;49;00m;$
 [37m(*[39;49;00m[37m Total width of tokens ever put in queue. [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_right_total : [36mint[39;49;00m;$
 [37m(*[39;49;00m[37m Current number of opened blocks. [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_curr_depth : [36mint[39;49;00m;$
 [37m(*[39;49;00m[37m Maximum number of blocks which can be simultaneously opened. [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_max_boxes : [36mint[39;49;00m;$
 [37m(*[39;49;00m[37m Ellipsis string. [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_ellipsis : [36mstring[39;49;00m;$
 [37m(*[39;49;00m[37m Output function. [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_output_function : [36mstring[39;49;00m -> [36mint[39;49;00m -> [36mint[39;49;00m -> [36munit[39;49;00m;$
 [37m(*[39;49;00m[37m Flushing function. [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_flush_function : [36munit[39;49;00m -> [36munit[39;49;00m;$
 [37m(*[39;49;00m[37m Output of new lines. [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_output_newline : [36munit[39;49;00m -> [36munit[39;49;00m;$
 [37m(*[39;49;00m[37m Output of indentation spaces. [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_output_spaces : [36mint[39;49;00m -> [36munit[39;49;00m;$
 [37m(*[39;49;00m[37m Are tags printed ? [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_print_tags : [36mbool[39;49;00m;$
 [37m(*[39;49;00m[37m Are tags marked ? [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_mark_tags : [36mbool[39;49;00m;$
 [37m(*[39;49;00m[37m Find opening and closing markers of tags. [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_mark_open_tag : tag -> [36mstring[39;49;00m;$
 [34mmutable[39;49;00m pp_mark_close_tag : tag -> [36mstring[39;49;00m;$
 [34mmutable[39;49;00m pp_print_open_tag : tag -> [36munit[39;49;00m;$
 [34mmutable[39;49;00m pp_print_close_tag : tag -> [36munit[39;49;00m;$
 [37m(*[39;49;00m[37m The pretty-printer queue. [39;49;00m[37m*)[39;49;00m$
 [34mmutable[39;49;00m pp_queue : pp_queue_elem queue$
};;$
$
[37m(*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m  Auxilliaries and basic functions.[39;49;00m$
[37m[39;49;00m$
[37m [39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*)[39;49;00m$
$
$
[37m(*[39;49;00m[37m Queues auxilliaries. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m make_queue [36m()[39;49;00m = {insert = [04m[32mNil[39;49;00m; body = [04m[32mNil[39;49;00m};;$
$
[34mlet[39;49;00m clear_queue q = q.insert <- [04m[32mNil[39;49;00m; q.body <- [04m[32mNil[39;49;00m;;$
$
[34mlet[39;49;00m add_queue x q =$
 [34mlet[39;49;00m c = [04m[32mCons[39;49;00m {head = x; tail = [04m[32mNil[39;49;00m} [34min[39;49;00m$
 [34mmatch[39;49;00m q [34mwith[39;49;00m$
 | {insert = [04m[32mCons[39;49;00m cell} -> q.insert <- c; cell.tail <- c$
 [37m(*[39;49;00m[37m Invariant: when insert is Nil body should be Nil. [39;49;00m[37m*)[39;49;00m$
 | _ -> q.insert <- c; q.body <- c;;$
$
[34mexception[39;49;00m [04m[32mEmpty_queue[39;49;00m;;$
$
[34mlet[39;49;00m peek_queue = [34mfunction[39;49;00m$
 | {body = [04m[32mCons[39;49;00m {head = x}} -> x$
 | _ -> [34mraise[39;49;00m [04m[32mEmpty_queue[39;49;00m;;$
$
[34mlet[39;49;00m take_queue = [34mfunction[39;49;00m$
 | {body = [04m[32mCons[39;49;00m {head = x; tail = tl}} [34mas[39;49;00m q ->$
    q.body <- tl;$
    [34mif[39;49;00m tl = [04m[32mNil[39;49;00m [34mthen[39;49;00m q.insert <- [04m[32mNil[39;49;00m; [37m(*[39;49;00m[37m Maintain the invariant. [39;49;00m[37m*)[39;49;00m$
    x$
 | _ -> [34mraise[39;49;00m [04m[32mEmpty_queue[39;49;00m;;$
$
[37m(*[39;49;00m[37m Enter a token in the pretty-printer queue. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_enqueue state ({length = len} [34mas[39;49;00m token) =$
    state.pp_right_total <- state.pp_right_total + len;$
    add_queue token state.pp_queue;;$
$
[34mlet[39;49;00m pp_clear_queue state =$
    state.pp_left_total <- [34m1[39;49;00m; state.pp_right_total <- [34m1[39;49;00m;$
    clear_queue state.pp_queue;;$
$
[37m(*[39;49;00m[37m Pp_infinity: large value for default tokens size.[39;49;00m$
[37m[39;49;00m$
[37m   Pp_infinity is documented as being greater than 1e10; to avoid[39;49;00m$
[37m   confusion about the word ``greater'', we choose pp_infinity greater[39;49;00m$
[37m   than 1e10 + 1; for correct handling of tests in the algorithm,[39;49;00m$
[37m   pp_infinity must be even one more than 1e10 + 1; let's stand on the[39;49;00m$
[37m   safe side by choosing 1.e10+10.[39;49;00m$
[37m[39;49;00m$
[37m   Pp_infinity could probably be 1073741823 that is 2^30 - 1, that is[39;49;00m$
[37m   the minimal upper bound for integers; now that max_int is defined,[39;49;00m$
[37m   this limit could also be defined as max_int - 1.[39;49;00m$
[37m[39;49;00m$
[37m   However, before setting pp_infinity to something around max_int, we[39;49;00m$
[37m   must carefully double-check all the integer arithmetic operations[39;49;00m$
[37m   that involve pp_infinity, since any overflow would wreck havoc the[39;49;00m$
[37m   pretty-printing algorithm's invariants. Given that this arithmetic[39;49;00m$
[37m   correctness check is difficult and error prone and given that 1e10[39;49;00m$
[37m   + 1 is in practice large enough, there is no need to attempt to set[39;49;00m$
[37m   pp_infinity to the theoretically maximum limit. Is it not worth the[39;49;00m$
[37m   burden ! [39;49;00m[37m*)[39;49;00m$
$
[34mlet[39;49;00m pp_infinity = [34m1000000010[39;49;00m;;$
$
[37m(*[39;49;00m[37m Output functions for the formatter. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_output_string state s = state.pp_output_function s [34m0[39;49;00m ([04m[36mString[39;49;00m.length s)$
[35mand[39;49;00m pp_output_newline state = state.pp_output_newline [36m()[39;49;00m;;$
$
[34mlet[39;49;00m pp_display_blanks state n = state.pp_output_spaces n;;$
$
[37m(*[39;49;00m[37m To format a break, indenting a new line. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m break_new_line state offset width =$
    pp_output_newline state;$
    state.pp_is_new_line <- [36mtrue[39;49;00m;$
    [34mlet[39;49;00m indent = state.pp_margin - width + offset [34min[39;49;00m$
    [37m(*[39;49;00m[37m Don't indent more than pp_max_indent. [39;49;00m[37m*)[39;49;00m$
    [34mlet[39;49;00m real_indent = min state.pp_max_indent indent [34min[39;49;00m$
    state.pp_current_indent <- real_indent;$
    state.pp_space_left <- state.pp_margin - state.pp_current_indent;$
    pp_display_blanks state state.pp_current_indent;;$
$
[37m(*[39;49;00m[37m To force a line break inside a block: no offset is added. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m break_line state width = break_new_line state [34m0[39;49;00m width;;$
$
[37m(*[39;49;00m[37m To format a break that fits on the current line. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m break_same_line state width =$
    state.pp_space_left <- state.pp_space_left - width;$
    pp_display_blanks state width;;$
$
[37m(*[39;49;00m[37m To indent no more than pp_max_indent, if one tries to open a block[39;49;00m$
[37m   beyond pp_max_indent, then the block is rejected on the left[39;49;00m$
[37m   by simulating a break. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_force_break_line state =$
    [34mmatch[39;49;00m state.pp_format_stack [34mwith[39;49;00m$
    | [04m[32mFormat_elem[39;49;00m (bl_ty, width) :: _ ->$
        [34mif[39;49;00m width > state.pp_space_left [34mthen[39;49;00m$
         ([34mmatch[39;49;00m bl_ty [34mwith[39;49;00m$
          | [04m[32mPp_fits[39;49;00m -> [36m()[39;49;00m | [04m[32mPp_hbox[39;49;00m -> [36m()[39;49;00m | _ -> break_line state width)$
    | _ -> pp_output_newline state;;$
$
[37m(*[39;49;00m[37m To skip a token, if the previous line has been broken. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_skip_token state =$
    [37m(*[39;49;00m[37m When calling pp_skip_token the queue cannot be empty. [39;49;00m[37m*)[39;49;00m$
    [34mmatch[39;49;00m take_queue state.pp_queue [34mwith[39;49;00m$
    {elem_size = size; length = len} ->$
       state.pp_left_total <- state.pp_left_total - len;$
       state.pp_space_left <- state.pp_space_left + int_of_size size;;$
$
[37m(*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m  The main pretting printing functions.[39;49;00m$
[37m[39;49;00m$
[37m [39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*)[39;49;00m$
$
[37m(*[39;49;00m[37m To format a token. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m format_pp_token state size = [34mfunction[39;49;00m$
$
  | [04m[32mPp_text[39;49;00m s ->$
      state.pp_space_left <- state.pp_space_left - size;$
      pp_output_string state s;$
      state.pp_is_new_line <- [36mfalse[39;49;00m$
$
  | [04m[32mPp_begin[39;49;00m (off, ty) ->$
      [34mlet[39;49;00m insertion_point = state.pp_margin - state.pp_space_left [34min[39;49;00m$
      [34mif[39;49;00m insertion_point > state.pp_max_indent [34mthen[39;49;00m$
         [37m(*[39;49;00m[37m can't open a block right there. [39;49;00m[37m*)[39;49;00m$
         [34mbegin[39;49;00m pp_force_break_line state [34mend[39;49;00m;$
      [34mlet[39;49;00m offset = state.pp_space_left - off [34min[39;49;00m$
      [34mlet[39;49;00m bl_type =$
       [34mbegin[39;49;00m [34mmatch[39;49;00m ty [34mwith[39;49;00m$
        | [04m[32mPp_vbox[39;49;00m -> [04m[32mPp_vbox[39;49;00m$
        | _ -> [34mif[39;49;00m size > state.pp_space_left [34mthen[39;49;00m ty [34melse[39;49;00m [04m[32mPp_fits[39;49;00m$
       [34mend[39;49;00m [34min[39;49;00m$
       state.pp_format_stack <-$
        [04m[32mFormat_elem[39;49;00m (bl_type, offset) :: state.pp_format_stack$
$
  | [04m[32mPp_end[39;49;00m ->$
      [34mbegin[39;49;00m [34mmatch[39;49;00m state.pp_format_stack [34mwith[39;49;00m$
        | x :: (y :: l [34mas[39;49;00m ls) -> state.pp_format_stack <- ls$
        | _ -> [36m()[39;49;00m [37m(*[39;49;00m[37m No more block to close. [39;49;00m[37m*)[39;49;00m$
      [34mend[39;49;00m$
$
  | [04m[32mPp_tbegin[39;49;00m ([04m[32mPp_tbox[39;49;00m _ [34mas[39;49;00m tbox) ->$
      state.pp_tbox_stack <- tbox :: state.pp_tbox_stack$
$
  | [04m[32mPp_tend[39;49;00m ->$
      [34mbegin[39;49;00m [34mmatch[39;49;00m state.pp_tbox_stack [34mwith[39;49;00m$
        | x :: ls -> state.pp_tbox_stack <- ls$
        | _ -> [36m()[39;49;00m [37m(*[39;49;00m[37m No more tabulation block to close. [39;49;00m[37m*)[39;49;00m$
      [34mend[39;49;00m$
$
  | [04m[32mPp_stab[39;49;00m ->$
     [34mbegin[39;49;00m [34mmatch[39;49;00m state.pp_tbox_stack [34mwith[39;49;00m$
     | [04m[32mPp_tbox[39;49;00m tabs :: _ ->$
        [34mlet[39;49;00m [34mrec[39;49;00m add_tab n = [34mfunction[39;49;00m$
          | [36m[][39;49;00m -> [n]$
          | x :: l [34mas[39;49;00m ls -> [34mif[39;49;00m n < x [34mthen[39;49;00m n :: ls [34melse[39;49;00m x :: add_tab n l [34min[39;49;00m$
        tabs := add_tab (state.pp_margin - state.pp_space_left) !tabs$
     | _ -> [36m()[39;49;00m [37m(*[39;49;00m[37m No opened tabulation block. [39;49;00m[37m*)[39;49;00m$
     [34mend[39;49;00m$
$
  | [04m[32mPp_tbreak[39;49;00m (n, off) ->$
      [34mlet[39;49;00m insertion_point = state.pp_margin - state.pp_space_left [34min[39;49;00m$
      [34mbegin[39;49;00m [34mmatch[39;49;00m state.pp_tbox_stack [34mwith[39;49;00m$
      | [04m[32mPp_tbox[39;49;00m tabs :: _ ->$
         [34mlet[39;49;00m [34mrec[39;49;00m find n = [34mfunction[39;49;00m$
           | x :: l -> [34mif[39;49;00m x >= n [34mthen[39;49;00m x [34melse[39;49;00m find n l$
           | [36m[][39;49;00m -> [34mraise[39;49;00m [04m[32mNot_found[39;49;00m [34min[39;49;00m$
         [34mlet[39;49;00m tab =$
             [34mmatch[39;49;00m !tabs [34mwith[39;49;00m$
             | x :: l ->$
                [34mbegin[39;49;00m [34mtry[39;49;00m find insertion_point !tabs [34mwith[39;49;00m [04m[32mNot_found[39;49;00m -> x [34mend[39;49;00m$
             | _ -> insertion_point [34min[39;49;00m$
         [34mlet[39;49;00m offset = tab - insertion_point [34min[39;49;00m$
         [34mif[39;49;00m offset >= [34m0[39;49;00m [34mthen[39;49;00m break_same_line state (offset + n) [34melse[39;49;00m$
          break_new_line state (tab + off) state.pp_margin$
      | _ -> [36m()[39;49;00m [37m(*[39;49;00m[37m No opened tabulation block. [39;49;00m[37m*)[39;49;00m$
      [34mend[39;49;00m$
$
  | [04m[32mPp_newline[39;49;00m ->$
     [34mbegin[39;49;00m [34mmatch[39;49;00m state.pp_format_stack [34mwith[39;49;00m$
     | [04m[32mFormat_elem[39;49;00m (_, width) :: _ -> break_line state width$
     | _ -> pp_output_newline state$
     [34mend[39;49;00m$
$
  | [04m[32mPp_if_newline[39;49;00m ->$
     [34mif[39;49;00m state.pp_current_indent != state.pp_margin - state.pp_space_left$
     [34mthen[39;49;00m pp_skip_token state$
$
  | [04m[32mPp_break[39;49;00m (n, off) ->$
     [34mbegin[39;49;00m [34mmatch[39;49;00m state.pp_format_stack [34mwith[39;49;00m$
     | [04m[32mFormat_elem[39;49;00m (ty, width) :: _ ->$
        [34mbegin[39;49;00m [34mmatch[39;49;00m ty [34mwith[39;49;00m$
        | [04m[32mPp_hovbox[39;49;00m ->$
           [34mif[39;49;00m size > state.pp_space_left$
           [34mthen[39;49;00m break_new_line state off width$
           [34melse[39;49;00m break_same_line state n$
        | [04m[32mPp_box[39;49;00m ->$
           [37m(*[39;49;00m[37m Have the line just been broken here ? [39;49;00m[37m*)[39;49;00m$
           [34mif[39;49;00m state.pp_is_new_line [34mthen[39;49;00m break_same_line state n [34melse[39;49;00m$
           [34mif[39;49;00m size > state.pp_space_left$
            [34mthen[39;49;00m break_new_line state off width [34melse[39;49;00m$
           [37m(*[39;49;00m[37m break the line here leads to new indentation ? [39;49;00m[37m*)[39;49;00m$
           [34mif[39;49;00m state.pp_current_indent > state.pp_margin - width + off$
           [34mthen[39;49;00m break_new_line state off width$
           [34melse[39;49;00m break_same_line state n$
        | [04m[32mPp_hvbox[39;49;00m -> break_new_line state off width$
        | [04m[32mPp_fits[39;49;00m -> break_same_line state n$
        | [04m[32mPp_vbox[39;49;00m -> break_new_line state off width$
        | [04m[32mPp_hbox[39;49;00m -> break_same_line state n$
        [34mend[39;49;00m$
     | _ -> [36m()[39;49;00m [37m(*[39;49;00m[37m No opened block. [39;49;00m[37m*)[39;49;00m$
     [34mend[39;49;00m$
$
   | [04m[32mPp_open_tag[39;49;00m tag_name ->$
      [34mlet[39;49;00m marker = state.pp_mark_open_tag tag_name [34min[39;49;00m$
      pp_output_string state marker;$
      state.pp_mark_stack <- tag_name :: state.pp_mark_stack$
$
   | [04m[32mPp_close_tag[39;49;00m ->$
      [34mbegin[39;49;00m [34mmatch[39;49;00m state.pp_mark_stack [34mwith[39;49;00m$
      | tag_name :: tags ->$
          [34mlet[39;49;00m marker = state.pp_mark_close_tag tag_name [34min[39;49;00m$
          pp_output_string state marker;$
          state.pp_mark_stack <- tags$
      | _ -> [36m()[39;49;00m [37m(*[39;49;00m[37m No more tag to close. [39;49;00m[37m*)[39;49;00m$
      [34mend[39;49;00m;;$
$
[37m(*[39;49;00m[37m Print if token size is known or printing is delayed.[39;49;00m$
[37m   Size is known when not negative.[39;49;00m$
[37m   Printing is delayed when the text waiting in the queue requires[39;49;00m$
[37m   more room to format than exists on the current line. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m [34mrec[39;49;00m advance_left state =$
    [34mtry[39;49;00m$
     [34mmatch[39;49;00m peek_queue state.pp_queue [34mwith[39;49;00m$
      {elem_size = size; token = tok; length = len} ->$
       [34mlet[39;49;00m size = int_of_size size [34min[39;49;00m$
       [34mif[39;49;00m not$
        (size < [34m0[39;49;00m &&$
         (state.pp_right_total - state.pp_left_total < state.pp_space_left))$
        [34mthen[39;49;00m [34mbegin[39;49;00m$
         ignore(take_queue state.pp_queue);$
         format_pp_token state ([34mif[39;49;00m size < [34m0[39;49;00m [34mthen[39;49;00m pp_infinity [34melse[39;49;00m size) tok;$
         state.pp_left_total <- len + state.pp_left_total;$
         advance_left state$
        [34mend[39;49;00m$
    [34mwith[39;49;00m [04m[32mEmpty_queue[39;49;00m -> [36m()[39;49;00m;;$
$
[34mlet[39;49;00m enqueue_advance state tok = pp_enqueue state tok; advance_left state;;$
$
[37m(*[39;49;00m[37m To enqueue a string : try to advance. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m make_queue_elem size tok len =$
 {elem_size = size; token = tok; length = len};;$
$
[34mlet[39;49;00m enqueue_string_as state size s =$
  [34mlet[39;49;00m len = int_of_size size [34min[39;49;00m$
  enqueue_advance state (make_queue_elem size ([04m[32mPp_text[39;49;00m s) len);;$
$
[34mlet[39;49;00m enqueue_string state s =$
  [34mlet[39;49;00m len = [04m[36mString[39;49;00m.length s [34min[39;49;00m$
  enqueue_string_as state (size_of_int len) s;;$
$
[37m(*[39;49;00m[37m Routines for scan stack[39;49;00m$
[37m   determine sizes of blocks. [39;49;00m[37m*)[39;49;00m$
$
[37m(*[39;49;00m[37m The scan_stack is never empty. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m scan_stack_bottom =$
  [34mlet[39;49;00m q_elem = make_queue_elem (size_of_int (-[34m1[39;49;00m)) ([04m[32mPp_text[39;49;00m [33m"[39;49;00m[33m"[39;49;00m) [34m0[39;49;00m [34min[39;49;00m$
  [[04m[32mScan_elem[39;49;00m (-[34m1[39;49;00m, q_elem)];;$
$
[37m(*[39;49;00m[37m Set size of blocks on scan stack:[39;49;00m$
[37m   if ty = true then size of break is set else size of block is set;[39;49;00m$
[37m   in each case pp_scan_stack is popped. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m clear_scan_stack state = state.pp_scan_stack <- scan_stack_bottom;;$
$
[37m(*[39;49;00m[37m Pattern matching on scan stack is exhaustive,[39;49;00m$
[37m   since scan_stack is never empty.[39;49;00m$
[37m   Pattern matching on token in scan stack is also exhaustive,[39;49;00m$
[37m   since scan_push is used on breaks and opening of boxes. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m set_size state ty =$
    [34mmatch[39;49;00m state.pp_scan_stack [34mwith[39;49;00m$
    | [04m[32mScan_elem[39;49;00m$
        (left_tot,$
         ({elem_size = size; token = tok} [34mas[39;49;00m queue_elem)) :: t ->$
       [34mlet[39;49;00m size = int_of_size size [34min[39;49;00m$
       [37m(*[39;49;00m[37m test if scan stack contains any data that is not obsolete. [39;49;00m[37m*)[39;49;00m$
       [34mif[39;49;00m left_tot < state.pp_left_total [34mthen[39;49;00m clear_scan_stack state [34melse[39;49;00m$
        [34mbegin[39;49;00m [34mmatch[39;49;00m tok [34mwith[39;49;00m$
        | [04m[32mPp_break[39;49;00m (_, _) | [04m[32mPp_tbreak[39;49;00m (_, _) ->$
           [34mif[39;49;00m ty [34mthen[39;49;00m$
            [34mbegin[39;49;00m$
             queue_elem.elem_size <- size_of_int (state.pp_right_total + size);$
             state.pp_scan_stack <- t$
            [34mend[39;49;00m$
        | [04m[32mPp_begin[39;49;00m (_, _) ->$
           [34mif[39;49;00m not ty [34mthen[39;49;00m$
            [34mbegin[39;49;00m$
             queue_elem.elem_size <- size_of_int (state.pp_right_total + size);$
             state.pp_scan_stack <- t$
            [34mend[39;49;00m$
        | _ -> [36m()[39;49;00m [37m(*[39;49;00m[37m scan_push is only used for breaks and boxes. [39;49;00m[37m*)[39;49;00m$
        [34mend[39;49;00m$
    | _ -> [36m()[39;49;00m [37m(*[39;49;00m[37m scan_stack is never empty. [39;49;00m[37m*)[39;49;00m;;$
$
[37m(*[39;49;00m[37m Push a token on scan stack. If b is true set_size is called. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m scan_push state b tok =$
    pp_enqueue state tok;$
    [34mif[39;49;00m b [34mthen[39;49;00m set_size state [36mtrue[39;49;00m;$
    state.pp_scan_stack <-$
     [04m[32mScan_elem[39;49;00m (state.pp_right_total, tok) :: state.pp_scan_stack;;$
$
[37m(*[39;49;00m[37m To open a new block :[39;49;00m$
[37m   the user may set the depth bound pp_max_boxes[39;49;00m$
[37m   any text nested deeper is printed as the ellipsis string. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_open_box_gen state indent br_ty =$
    state.pp_curr_depth <- state.pp_curr_depth + [34m1[39;49;00m;$
    [34mif[39;49;00m state.pp_curr_depth < state.pp_max_boxes [34mthen[39;49;00m$
      [34mlet[39;49;00m elem =$
        make_queue_elem$
          (size_of_int (- state.pp_right_total))$
          ([04m[32mPp_begin[39;49;00m (indent, br_ty))$
          [34m0[39;49;00m [34min[39;49;00m$
      scan_push state [36mfalse[39;49;00m elem [34melse[39;49;00m$
    [34mif[39;49;00m state.pp_curr_depth = state.pp_max_boxes$
    [34mthen[39;49;00m enqueue_string state state.pp_ellipsis;;$
$
[37m(*[39;49;00m[37m The box which is always opened. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_open_sys_box state = pp_open_box_gen state [34m0[39;49;00m [04m[32mPp_hovbox[39;49;00m;;$
$
[37m(*[39;49;00m[37m Close a block, setting sizes of its subblocks. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_close_box state [36m()[39;49;00m =$
    [34mif[39;49;00m state.pp_curr_depth > [34m1[39;49;00m [34mthen[39;49;00m$
     [34mbegin[39;49;00m$
      [34mif[39;49;00m state.pp_curr_depth < state.pp_max_boxes [34mthen[39;49;00m$
       [34mbegin[39;49;00m$
        pp_enqueue state$
          {elem_size = size_of_int [34m0[39;49;00m; token = [04m[32mPp_end[39;49;00m; length = [34m0[39;49;00m};$
        set_size state [36mtrue[39;49;00m; set_size state [36mfalse[39;49;00m$
       [34mend[39;49;00m;$
      state.pp_curr_depth <- state.pp_curr_depth - [34m1[39;49;00m;$
     [34mend[39;49;00m;;$
$
[37m(*[39;49;00m[37m Open a tag, pushing it on the tag stack. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_open_tag state tag_name =$
    [34mif[39;49;00m state.pp_print_tags [34mthen[39;49;00m [34mbegin[39;49;00m$
      state.pp_tag_stack <- tag_name :: state.pp_tag_stack;$
      state.pp_print_open_tag tag_name [34mend[39;49;00m;$
    [34mif[39;49;00m state.pp_mark_tags [34mthen[39;49;00m$
      pp_enqueue state$
        {elem_size = size_of_int [34m0[39;49;00m; token = [04m[32mPp_open_tag[39;49;00m tag_name; length = [34m0[39;49;00m};;$
$
[37m(*[39;49;00m[37m Close a tag, popping it from the tag stack. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_close_tag state [36m()[39;49;00m =$
    [34mif[39;49;00m state.pp_mark_tags [34mthen[39;49;00m$
      pp_enqueue state$
        {elem_size = size_of_int [34m0[39;49;00m; token = [04m[32mPp_close_tag[39;49;00m; length = [34m0[39;49;00m};$
    [34mif[39;49;00m state.pp_print_tags [34mthen[39;49;00m$
      [34mbegin[39;49;00m [34mmatch[39;49;00m state.pp_tag_stack [34mwith[39;49;00m$
      | tag_name :: tags ->$
          state.pp_print_close_tag tag_name;$
          state.pp_tag_stack <- tags$
      | _ -> [36m()[39;49;00m [37m(*[39;49;00m[37m No more tag to close. [39;49;00m[37m*)[39;49;00m$
      [34mend[39;49;00m;;$
$
[34mlet[39;49;00m pp_set_print_tags state b = state.pp_print_tags <- b;;$
[34mlet[39;49;00m pp_set_mark_tags state b = state.pp_mark_tags <- b;;$
[34mlet[39;49;00m pp_get_print_tags state [36m()[39;49;00m = state.pp_print_tags;;$
[34mlet[39;49;00m pp_get_mark_tags state [36m()[39;49;00m = state.pp_mark_tags;;$
[34mlet[39;49;00m pp_set_tags state b = pp_set_print_tags state b; pp_set_mark_tags state b;;$
$
[34mlet[39;49;00m pp_get_formatter_tag_functions state [36m()[39;49;00m = {$
   mark_open_tag = state.pp_mark_open_tag;$
   mark_close_tag = state.pp_mark_close_tag;$
   print_open_tag = state.pp_print_open_tag;$
   print_close_tag = state.pp_print_close_tag;$
};;$
$
[34mlet[39;49;00m pp_set_formatter_tag_functions state {$
     mark_open_tag = mot;$
     mark_close_tag = mct;$
     print_open_tag = pot;$
     print_close_tag = pct;$
  } =$
   state.pp_mark_open_tag <- mot;$
   state.pp_mark_close_tag <- mct;$
   state.pp_print_open_tag <- pot;$
   state.pp_print_close_tag <- pct;;$
$
[37m(*[39;49;00m[37m Initialize pretty-printer. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_rinit state =$
    pp_clear_queue state;$
    clear_scan_stack state;$
    state.pp_format_stack <- [36m[][39;49;00m;$
    state.pp_tbox_stack <- [36m[][39;49;00m;$
    state.pp_tag_stack <- [36m[][39;49;00m;$
    state.pp_mark_stack <- [36m[][39;49;00m;$
    state.pp_current_indent <- [34m0[39;49;00m;$
    state.pp_curr_depth <- [34m0[39;49;00m;$
    state.pp_space_left <- state.pp_margin;$
    pp_open_sys_box state;;$
$
[37m(*[39;49;00m[37m Flushing pretty-printer queue. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_flush_queue state b =$
    [34mwhile[39;49;00m state.pp_curr_depth > [34m1[39;49;00m [34mdo[39;49;00m$
     pp_close_box state [36m()[39;49;00m$
    [34mdone[39;49;00m;$
    state.pp_right_total <- pp_infinity;$
    advance_left state;$
    [34mif[39;49;00m b [34mthen[39;49;00m pp_output_newline state;$
    pp_rinit state;;$
$
[37m(*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m  Procedures to format objects, and use boxes[39;49;00m$
[37m[39;49;00m$
[37m [39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*)[39;49;00m$
$
[37m(*[39;49;00m[37m To format a string. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_print_as_size state size s =$
  [34mif[39;49;00m state.pp_curr_depth < state.pp_max_boxes$
  [34mthen[39;49;00m enqueue_string_as state size s;;$
$
[34mlet[39;49;00m pp_print_as state isize s =$
  pp_print_as_size state (size_of_int isize) s;;$
$
[34mlet[39;49;00m pp_print_string state s =$
  pp_print_as state ([04m[36mString[39;49;00m.length s) s;;$
$
[37m(*[39;49;00m[37m To format an integer. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_print_int state i = pp_print_string state (string_of_int i);;$
$
[37m(*[39;49;00m[37m To format a float. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_print_float state f = pp_print_string state (string_of_float f);;$
$
[37m(*[39;49;00m[37m To format a boolean. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_print_bool state b = pp_print_string state (string_of_bool b);;$
$
[37m(*[39;49;00m[37m To format a char. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_print_char state c =$
  [34mlet[39;49;00m s = [04m[36mString[39;49;00m.create [34m1[39;49;00m [34min[39;49;00m$
  s.[[34m0[39;49;00m] <- c;$
  pp_print_as state [34m1[39;49;00m s;;$
$
[37m(*[39;49;00m[37m Opening boxes. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_open_hbox state [36m()[39;49;00m = pp_open_box_gen state [34m0[39;49;00m [04m[32mPp_hbox[39;49;00m$
[35mand[39;49;00m pp_open_vbox state indent = pp_open_box_gen state indent [04m[32mPp_vbox[39;49;00m$
$
[35mand[39;49;00m pp_open_hvbox state indent = pp_open_box_gen state indent [04m[32mPp_hvbox[39;49;00m$
[35mand[39;49;00m pp_open_hovbox state indent = pp_open_box_gen state indent [04m[32mPp_hovbox[39;49;00m$
[35mand[39;49;00m pp_open_box state indent = pp_open_box_gen state indent [04m[32mPp_box[39;49;00m;;$
$
[37m(*[39;49;00m[37m Print a new line after printing all queued text[39;49;00m$
[37m   [39;49;00m[37m([39;49;00m[37msame for print_flush but without a newline[39;49;00m[37m)[39;49;00m[37m. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_print_newline state [36m()[39;49;00m =$
    pp_flush_queue state [36mtrue[39;49;00m; state.pp_flush_function [36m()[39;49;00m$
[35mand[39;49;00m pp_print_flush state [36m()[39;49;00m =$
    pp_flush_queue state [36mfalse[39;49;00m; state.pp_flush_function [36m()[39;49;00m;;$
$
[37m(*[39;49;00m[37m To get a newline when one does not want to close the current block. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_force_newline state [36m()[39;49;00m =$
  [34mif[39;49;00m state.pp_curr_depth < state.pp_max_boxes [34mthen[39;49;00m$
    enqueue_advance state (make_queue_elem (size_of_int [34m0[39;49;00m) [04m[32mPp_newline[39;49;00m [34m0[39;49;00m);;$
$
[37m(*[39;49;00m[37m To format something if the line has just been broken. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_print_if_newline state [36m()[39;49;00m =$
  [34mif[39;49;00m state.pp_curr_depth < state.pp_max_boxes [34mthen[39;49;00m$
    enqueue_advance state (make_queue_elem (size_of_int [34m0[39;49;00m) [04m[32mPp_if_newline[39;49;00m [34m0[39;49;00m);;$
$
[37m(*[39;49;00m[37m Breaks: indicate where a block may be broken.[39;49;00m$
[37m   If line is broken then offset is added to the indentation of the current[39;49;00m$
[37m   block else [39;49;00m[37m([39;49;00m[37mthe value of[39;49;00m[37m)[39;49;00m[37m width blanks are printed.[39;49;00m$
[37m   To do [39;49;00m[37m([39;49;00m[37m?[39;49;00m[37m)[39;49;00m[37m : add a maximum width and offset value. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_print_break state width offset =$
  [34mif[39;49;00m state.pp_curr_depth < state.pp_max_boxes [34mthen[39;49;00m$
    [34mlet[39;49;00m elem =$
      make_queue_elem$
        (size_of_int (- state.pp_right_total))$
        ([04m[32mPp_break[39;49;00m (width, offset))$
        width [34min[39;49;00m$
    scan_push state [36mtrue[39;49;00m elem;;$
$
[34mlet[39;49;00m pp_print_space state [36m()[39;49;00m = pp_print_break state [34m1[39;49;00m [34m0[39;49;00m$
[35mand[39;49;00m pp_print_cut state [36m()[39;49;00m = pp_print_break state [34m0[39;49;00m [34m0[39;49;00m;;$
$
[37m(*[39;49;00m[37m Tabulation boxes. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_open_tbox state [36m()[39;49;00m =$
  state.pp_curr_depth <- state.pp_curr_depth + [34m1[39;49;00m;$
  [34mif[39;49;00m state.pp_curr_depth < state.pp_max_boxes [34mthen[39;49;00m$
    [34mlet[39;49;00m elem =$
      make_queue_elem (size_of_int [34m0[39;49;00m) ([04m[32mPp_tbegin[39;49;00m ([04m[32mPp_tbox[39;49;00m (ref [36m[][39;49;00m))) [34m0[39;49;00m [34min[39;49;00m$
    enqueue_advance state elem;;$
$
[37m(*[39;49;00m[37m Close a tabulation block. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_close_tbox state [36m()[39;49;00m =$
  [34mif[39;49;00m state.pp_curr_depth > [34m1[39;49;00m [34mthen[39;49;00m [34mbegin[39;49;00m$
   [34mif[39;49;00m state.pp_curr_depth < state.pp_max_boxes [34mthen[39;49;00m$
     [34mlet[39;49;00m elem = make_queue_elem (size_of_int [34m0[39;49;00m) [04m[32mPp_tend[39;49;00m [34m0[39;49;00m [34min[39;49;00m$
     enqueue_advance state elem;$
     state.pp_curr_depth <- state.pp_curr_depth - [34m1[39;49;00m [34mend[39;49;00m;;$
$
[37m(*[39;49;00m[37m Print a tabulation break. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_print_tbreak state width offset =$
  [34mif[39;49;00m state.pp_curr_depth < state.pp_max_boxes [34mthen[39;49;00m$
    [34mlet[39;49;00m elem =$
      make_queue_elem$
        (size_of_int (- state.pp_right_total))$
        ([04m[32mPp_tbreak[39;49;00m (width, offset))$
        width [34min[39;49;00m$
    scan_push state [36mtrue[39;49;00m elem;;$
$
[34mlet[39;49;00m pp_print_tab state [36m()[39;49;00m = pp_print_tbreak state [34m0[39;49;00m [34m0[39;49;00m;;$
$
[34mlet[39;49;00m pp_set_tab state [36m()[39;49;00m =$
  [34mif[39;49;00m state.pp_curr_depth < state.pp_max_boxes [34mthen[39;49;00m$
    [34mlet[39;49;00m elem =$
      make_queue_elem (size_of_int [34m0[39;49;00m) [04m[32mPp_stab[39;49;00m [34m0[39;49;00m [34min[39;49;00m$
    enqueue_advance state elem;;$
$
[37m(*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m  Procedures to control the pretty-printers[39;49;00m$
[37m[39;49;00m$
[37m [39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*)[39;49;00m$
$
[37m(*[39;49;00m[37m Fit max_boxes. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_set_max_boxes state n = [34mif[39;49;00m n > [34m1[39;49;00m [34mthen[39;49;00m state.pp_max_boxes <- n;;$
$
[37m(*[39;49;00m[37m To know the current maximum number of boxes allowed. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_get_max_boxes state [36m()[39;49;00m = state.pp_max_boxes;;$
$
[34mlet[39;49;00m pp_over_max_boxes state [36m()[39;49;00m = state.pp_curr_depth = state.pp_max_boxes;;$
$
[37m(*[39;49;00m[37m Ellipsis. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_set_ellipsis_text state s = state.pp_ellipsis <- s$
[35mand[39;49;00m pp_get_ellipsis_text state [36m()[39;49;00m = state.pp_ellipsis;;$
$
[37m(*[39;49;00m[37m To set the margin of pretty-printer. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_limit n =$
  [34mif[39;49;00m n < pp_infinity [34mthen[39;49;00m n [34melse[39;49;00m pred pp_infinity;;$
$
[34mlet[39;49;00m pp_set_min_space_left state n =$
  [34mif[39;49;00m n >= [34m1[39;49;00m [34mthen[39;49;00m$
    [34mlet[39;49;00m n = pp_limit n [34min[39;49;00m$
    state.pp_min_space_left <- n;$
    state.pp_max_indent <- state.pp_margin - state.pp_min_space_left;$
    pp_rinit state;;$
$
[37m(*[39;49;00m[37m Initially, we have :[39;49;00m$
[37m  pp_max_indent = pp_margin - pp_min_space_left, and[39;49;00m$
[37m  pp_space_left = pp_margin. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m pp_set_max_indent state n =$
  pp_set_min_space_left state (state.pp_margin - n);;$
[34mlet[39;49;00m pp_get_max_indent state [36m()[39;49;00m = state.pp_max_indent;;$
$
[34mlet[39;49;00m pp_set_margin state n =$
  [34mif[39;49;00m n >= [34m1[39;49;00m [34mthen[39;49;00m$
    [34mlet[39;49;00m n = pp_limit n [34min[39;49;00m$
    state.pp_margin <- n;$
    [34mlet[39;49;00m new_max_indent =$
        [37m(*[39;49;00m[37m Try to maintain max_indent to its actual value. [39;49;00m[37m*)[39;49;00m$
        [34mif[39;49;00m state.pp_max_indent <= state.pp_margin$
        [34mthen[39;49;00m state.pp_max_indent [34melse[39;49;00m$
        [37m(*[39;49;00m[37m If possible maintain pp_min_space_left to its actual value,[39;49;00m$
[37m           if this leads to a too small max_indent, take half of the[39;49;00m$
[37m           new margin, if it is greater than 1. [39;49;00m[37m*)[39;49;00m$
         max (max (state.pp_margin - state.pp_min_space_left)$
                  (state.pp_margin / [34m2[39;49;00m)) [34m1[39;49;00m [34min[39;49;00m$
    [37m(*[39;49;00m[37m Rebuild invariants. [39;49;00m[37m*)[39;49;00m$
    pp_set_max_indent state new_max_indent;;$
$
[34mlet[39;49;00m pp_get_margin state [36m()[39;49;00m = state.pp_margin;;$
$
[34mlet[39;49;00m pp_set_formatter_output_functions state f g =$
  state.pp_output_function <- f; state.pp_flush_function <- g;;$
[34mlet[39;49;00m pp_get_formatter_output_functions state [36m()[39;49;00m =$
  (state.pp_output_function, state.pp_flush_function);;$
$
[34mlet[39;49;00m pp_set_all_formatter_output_functions state$
    ~out:f ~flush:g ~newline:h ~spaces:i =$
  pp_set_formatter_output_functions state f g;$
  state.pp_output_newline <- ([34mfunction[39;49;00m [36m()[39;49;00m -> h [36m()[39;49;00m);$
  state.pp_output_spaces <- ([34mfunction[39;49;00m n -> i n);;$
[34mlet[39;49;00m pp_get_all_formatter_output_functions state [36m()[39;49;00m =$
  (state.pp_output_function, state.pp_flush_function,$
   state.pp_output_newline, state.pp_output_spaces);;$
$
[34mlet[39;49;00m pp_set_formatter_out_channel state os =$
  state.pp_output_function <- output os;$
  state.pp_flush_function <- ([34mfun[39;49;00m [36m()[39;49;00m -> flush os);;$
$
[37m(*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m  Creation of specific formatters[39;49;00m$
[37m[39;49;00m$
[37m [39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*)[39;49;00m$
$
[34mlet[39;49;00m default_pp_mark_open_tag s = [33m"[39;49;00m[33m<[39;49;00m[33m"[39;49;00m ^ s ^ [33m"[39;49;00m[33m>[39;49;00m[33m"[39;49;00m;;$
[34mlet[39;49;00m default_pp_mark_close_tag s = [33m"[39;49;00m[33m</[39;49;00m[33m"[39;49;00m ^ s ^ [33m"[39;49;00m[33m>[39;49;00m[33m"[39;49;00m;;$
$
[34mlet[39;49;00m default_pp_print_open_tag s = [36m()[39;49;00m;;$
[34mlet[39;49;00m default_pp_print_close_tag = default_pp_print_open_tag;;$
$
[34mlet[39;49;00m pp_make_formatter f g h i =$
 [37m(*[39;49;00m[37m The initial state of the formatter contains a dummy box. [39;49;00m[37m*)[39;49;00m$
 [34mlet[39;49;00m pp_q = make_queue [36m()[39;49;00m [34min[39;49;00m$
 [34mlet[39;49;00m sys_tok =$
   make_queue_elem (size_of_int (-[34m1[39;49;00m)) ([04m[32mPp_begin[39;49;00m ([34m0[39;49;00m, [04m[32mPp_hovbox[39;49;00m)) [34m0[39;49;00m [34min[39;49;00m$
 add_queue sys_tok pp_q;$
 [34mlet[39;49;00m sys_scan_stack =$
     ([04m[32mScan_elem[39;49;00m ([34m1[39;49;00m, sys_tok)) :: scan_stack_bottom [34min[39;49;00m$
 {pp_scan_stack = sys_scan_stack;$
  pp_format_stack = [36m[][39;49;00m;$
  pp_tbox_stack = [36m[][39;49;00m;$
  pp_tag_stack = [36m[][39;49;00m;$
  pp_mark_stack = [36m[][39;49;00m;$
  pp_margin = [34m78[39;49;00m;$
  pp_min_space_left = [34m10[39;49;00m;$
  pp_max_indent = [34m78[39;49;00m - [34m10[39;49;00m;$
  pp_space_left = [34m78[39;49;00m;$
  pp_current_indent = [34m0[39;49;00m;$
  pp_is_new_line = [36mtrue[39;49;00m;$
  pp_left_total = [34m1[39;49;00m;$
  pp_right_total = [34m1[39;49;00m;$
  pp_curr_depth = [34m1[39;49;00m;$
  pp_max_boxes = max_int;$
  pp_ellipsis = [33m"[39;49;00m[33m.[39;49;00m[33m"[39;49;00m;$
  pp_output_function = f;$
  pp_flush_function = g;$
  pp_output_newline = h;$
  pp_output_spaces = i;$
  pp_print_tags = [36mfalse[39;49;00m;$
  pp_mark_tags = [36mfalse[39;49;00m;$
  pp_mark_open_tag = default_pp_mark_open_tag;$
  pp_mark_close_tag = default_pp_mark_close_tag;$
  pp_print_open_tag = default_pp_print_open_tag;$
  pp_print_close_tag = default_pp_print_close_tag;$
  pp_queue = pp_q$
 };;$
$
[37m(*[39;49;00m[37m Default function to output spaces. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m blank_line = [04m[36mString[39;49;00m.make [34m80[39;49;00m [33m' '[39;49;00m;;$
[34mlet[39;49;00m [34mrec[39;49;00m display_blanks state n =$
    [34mif[39;49;00m n > [34m0[39;49;00m [34mthen[39;49;00m$
    [34mif[39;49;00m n <= [34m80[39;49;00m [34mthen[39;49;00m state.pp_output_function blank_line [34m0[39;49;00m n [34melse[39;49;00m$
     [34mbegin[39;49;00m$
      state.pp_output_function blank_line [34m0[39;49;00m [34m80[39;49;00m;$
      display_blanks state (n - [34m80[39;49;00m)$
     [34mend[39;49;00m;;$
$
[37m(*[39;49;00m[37m Default function to output new lines. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m display_newline state [36m()[39;49;00m = state.pp_output_function [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m [34m0[39;49;00m  [34m1[39;49;00m;;$
$
[34mlet[39;49;00m make_formatter f g =$
  [34mlet[39;49;00m ff = pp_make_formatter f g ignore ignore [34min[39;49;00m$
  ff.pp_output_newline <- display_newline ff;$
  ff.pp_output_spaces <- display_blanks ff;$
  ff;;$
$
[34mlet[39;49;00m formatter_of_out_channel oc =$
  make_formatter (output oc) ([34mfun[39;49;00m [36m()[39;49;00m -> flush oc);;$
$
[34mlet[39;49;00m formatter_of_buffer b =$
  make_formatter ([04m[36mBuffer[39;49;00m.add_substring b) ignore;;$
$
[34mlet[39;49;00m stdbuf = [04m[36mBuffer[39;49;00m.create [34m512[39;49;00m;;$
$
[34mlet[39;49;00m str_formatter = formatter_of_buffer stdbuf;;$
[34mlet[39;49;00m std_formatter = formatter_of_out_channel stdout;;$
[34mlet[39;49;00m err_formatter = formatter_of_out_channel stderr;;$
$
[34mlet[39;49;00m flush_str_formatter [36m()[39;49;00m =$
  pp_flush_queue str_formatter [36mfalse[39;49;00m;$
  [34mlet[39;49;00m s = [04m[36mBuffer[39;49;00m.contents stdbuf [34min[39;49;00m$
  [04m[36mBuffer[39;49;00m.reset stdbuf;$
  s;;$
$
[37m(*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m  Basic functions on the standard formatter[39;49;00m$
[37m[39;49;00m$
[37m [39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*)[39;49;00m$
$
[34mlet[39;49;00m open_hbox = pp_open_hbox std_formatter$
[35mand[39;49;00m open_vbox = pp_open_vbox std_formatter$
[35mand[39;49;00m open_hvbox = pp_open_hvbox std_formatter$
[35mand[39;49;00m open_hovbox = pp_open_hovbox std_formatter$
[35mand[39;49;00m open_box = pp_open_box std_formatter$
[35mand[39;49;00m close_box = pp_close_box std_formatter$
[35mand[39;49;00m open_tag = pp_open_tag std_formatter$
[35mand[39;49;00m close_tag = pp_close_tag std_formatter$
[35mand[39;49;00m print_as = pp_print_as std_formatter$
[35mand[39;49;00m print_string = pp_print_string std_formatter$
[35mand[39;49;00m print_int = pp_print_int std_formatter$
[35mand[39;49;00m print_float = pp_print_float std_formatter$
[35mand[39;49;00m print_char = pp_print_char std_formatter$
[35mand[39;49;00m print_bool = pp_print_bool std_formatter$
[35mand[39;49;00m print_break = pp_print_break std_formatter$
[35mand[39;49;00m print_cut = pp_print_cut std_formatter$
[35mand[39;49;00m print_space = pp_print_space std_formatter$
[35mand[39;49;00m force_newline = pp_force_newline std_formatter$
[35mand[39;49;00m print_flush = pp_print_flush std_formatter$
[35mand[39;49;00m print_newline = pp_print_newline std_formatter$
[35mand[39;49;00m print_if_newline = pp_print_if_newline std_formatter$
$
[35mand[39;49;00m open_tbox = pp_open_tbox std_formatter$
[35mand[39;49;00m close_tbox = pp_close_tbox std_formatter$
[35mand[39;49;00m print_tbreak = pp_print_tbreak std_formatter$
$
[35mand[39;49;00m set_tab = pp_set_tab std_formatter$
[35mand[39;49;00m print_tab = pp_print_tab std_formatter$
$
[35mand[39;49;00m set_margin = pp_set_margin std_formatter$
[35mand[39;49;00m get_margin = pp_get_margin std_formatter$
$
[35mand[39;49;00m set_max_indent = pp_set_max_indent std_formatter$
[35mand[39;49;00m get_max_indent = pp_get_max_indent std_formatter$
$
[35mand[39;49;00m set_max_boxes = pp_set_max_boxes std_formatter$
[35mand[39;49;00m get_max_boxes = pp_get_max_boxes std_formatter$
[35mand[39;49;00m over_max_boxes = pp_over_max_boxes std_formatter$
$
[35mand[39;49;00m set_ellipsis_text = pp_set_ellipsis_text std_formatter$
[35mand[39;49;00m get_ellipsis_text = pp_get_ellipsis_text std_formatter$
$
[35mand[39;49;00m set_formatter_out_channel =$
    pp_set_formatter_out_channel std_formatter$
$
[35mand[39;49;00m set_formatter_output_functions =$
    pp_set_formatter_output_functions std_formatter$
[35mand[39;49;00m get_formatter_output_functions =$
    pp_get_formatter_output_functions std_formatter$
$
[35mand[39;49;00m set_all_formatter_output_functions =$
    pp_set_all_formatter_output_functions std_formatter$
[35mand[39;49;00m get_all_formatter_output_functions =$
    pp_get_all_formatter_output_functions std_formatter$
$
[35mand[39;49;00m set_formatter_tag_functions =$
    pp_set_formatter_tag_functions std_formatter$
[35mand[39;49;00m get_formatter_tag_functions =$
    pp_get_formatter_tag_functions std_formatter$
[35mand[39;49;00m set_print_tags =$
    pp_set_print_tags std_formatter$
[35mand[39;49;00m get_print_tags =$
    pp_get_print_tags std_formatter$
[35mand[39;49;00m set_mark_tags =$
    pp_set_mark_tags std_formatter$
[35mand[39;49;00m get_mark_tags =$
    pp_get_mark_tags std_formatter$
[35mand[39;49;00m set_tags =$
    pp_set_tags std_formatter$
;;$
$
$
[37m(*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m  Printf implementation.[39;49;00m$
[37m[39;49;00m$
[37m [39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*)[39;49;00m$
$
[37m(*[39;49;00m[37m Error messages when processing formats. [39;49;00m[37m*)[39;49;00m$
$
[37m(*[39;49;00m[37m Trailer: giving up at character number ... [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m giving_up mess fmt i =$
  [33m"[39;49;00m[33mfprintf: [39;49;00m[33m"[39;49;00m ^ mess ^ [33m"[39;49;00m[33m ``[39;49;00m[33m"[39;49;00m ^ fmt ^ [33m"[39;49;00m[33m'', [39;49;00m[33m\[39;49;00m$
[33m   giving up at character number [39;49;00m[33m"[39;49;00m ^ string_of_int i ^$
  ([34mif[39;49;00m i < [04m[36mString[39;49;00m.length fmt$
   [34mthen[39;49;00m [33m"[39;49;00m[33m ([39;49;00m[33m"[39;49;00m ^ [04m[36mString[39;49;00m.make [34m1[39;49;00m fmt.[i] ^ [33m"[39;49;00m[33m).[39;49;00m[33m"[39;49;00m$
   [34melse[39;49;00m [04m[36mString[39;49;00m.make [34m1[39;49;00m [33m'.'[39;49;00m);;$
$
[37m(*[39;49;00m[37m When an invalid format deserves a special error explanation. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m format_invalid_arg mess fmt i = invalid_arg (giving_up mess fmt i);;$
$
[37m(*[39;49;00m[37m Standard invalid format. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m invalid_format fmt i = format_invalid_arg [33m"[39;49;00m[33mbad format[39;49;00m[33m"[39;49;00m fmt i;;$
$
[37m(*[39;49;00m[37m Cannot find a valid integer into that format. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m invalid_integer fmt i =$
  invalid_arg (giving_up [33m"[39;49;00m[33mbad integer specification[39;49;00m[33m"[39;49;00m fmt i);;$
$
[37m(*[39;49;00m[37m Finding an integer out of a sub-string of the format. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m format_int_of_string fmt i s =$
  [34mlet[39;49;00m sz =$
    [34mtry[39;49;00m int_of_string s [34mwith[39;49;00m$
    | [04m[32mFailure[39;49;00m s -> invalid_integer fmt i [34min[39;49;00m$
  size_of_int sz;;$
$
[37m(*[39;49;00m[37m Getting strings out of buffers. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m get_buffer_out b =$
 [34mlet[39;49;00m s = [04m[36mBuffer[39;49;00m.contents b [34min[39;49;00m$
 [04m[36mBuffer[39;49;00m.reset b;$
 s;;$
$
[37m(*[39;49;00m[37m [ppf] is supposed to be a pretty-printer that outputs in buffer [b]:[39;49;00m$
[37m   to extract contents of [ppf] as a string we flush [ppf] and get the string[39;49;00m$
[37m   out of [b]. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m string_out b ppf =$
 pp_flush_queue ppf [36mfalse[39;49;00m;$
 get_buffer_out b;;$
$
[37m(*[39;49;00m[37m Applies [printer] to a formatter that outputs on a fresh buffer,[39;49;00m$
[37m   then returns the resulting material. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m exstring printer arg =$
 [34mlet[39;49;00m b = [04m[36mBuffer[39;49;00m.create [34m512[39;49;00m [34min[39;49;00m$
 [34mlet[39;49;00m ppf = formatter_of_buffer b [34min[39;49;00m$
 printer ppf arg;$
 string_out b ppf;;$
$
[37m(*[39;49;00m[37m To turn out a character accumulator into the proper string result. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m implode_rev s0 = [34mfunction[39;49;00m$
  | [36m[][39;49;00m -> s0$
  | l -> [04m[36mString[39;49;00m.concat [33m"[39;49;00m[33m"[39;49;00m ([04m[36mList[39;49;00m.rev (s0 :: l));;$
$
[34mexternal[39;49;00m format_to_string : ([34m'[39;49;00ma, [34m'[39;49;00mb, [34m'[39;49;00mc, [34m'[39;49;00md) format4 -> [36mstring[39;49;00m = [33m"[39;49;00m[33m%identity[39;49;00m[33m"[39;49;00m;;$
$
[37m(*[39;49;00m[37m [fprintf_out] is the printf-like function generator: given the[39;49;00m$
[37m   - [str] flag that tells if we are printing into a string,[39;49;00m$
[37m   - the [out] function that has to be called at the end of formatting,[39;49;00m$
[37m   it generates a [fprintf] function that takes as arguments a [ppf][39;49;00m$
[37m   formatter and a printing format to print the rest of arguments[39;49;00m$
[37m   according to the format.[39;49;00m$
[37m   Regular [fprintf]-like functions of this module are obtained via partial[39;49;00m$
[37m   applications of [fprintf_out]. [39;49;00m[37m*)[39;49;00m$
[34mlet[39;49;00m mkprintf str get_out =$
  [34mlet[39;49;00m [34mrec[39;49;00m kprintf k fmt =$
    [34mlet[39;49;00m fmt = format_to_string fmt [34min[39;49;00m$
    [34mlet[39;49;00m len = [04m[36mString[39;49;00m.length fmt [34min[39;49;00m$
$
    [34mlet[39;49;00m kpr fmt v =$
      [34mlet[39;49;00m ppf = get_out fmt [34min[39;49;00m$
      [34mlet[39;49;00m print_as = ref [04m[32mNone[39;49;00m [34min[39;49;00m$
      [34mlet[39;49;00m pp_print_as_char c =$
          [34mmatch[39;49;00m !print_as [34mwith[39;49;00m$
          | [04m[32mNone[39;49;00m -> pp_print_char ppf c$
          | [04m[32mSome[39;49;00m size ->$
             pp_print_as_size ppf size ([04m[36mString[39;49;00m.make [34m1[39;49;00m c);$
             print_as := [04m[32mNone[39;49;00m$
      [35mand[39;49;00m pp_print_as_string s =$
          [34mmatch[39;49;00m !print_as [34mwith[39;49;00m$
          | [04m[32mNone[39;49;00m -> pp_print_string ppf s$
          | [04m[32mSome[39;49;00m size ->$
             pp_print_as_size ppf size s;$
             print_as := [04m[32mNone[39;49;00m [34min[39;49;00m$
$
      [34mlet[39;49;00m [34mrec[39;49;00m doprn n i =$
        [34mif[39;49;00m i >= len [34mthen[39;49;00m [04m[36mObj[39;49;00m.magic (k ppf) [34melse[39;49;00m$
        [34mmatch[39;49;00m fmt.[i] [34mwith[39;49;00m$
        | [33m'%'[39;49;00m ->$
            [04m[36mPrintf[39;49;00m.scan_format fmt v n i cont_s cont_a cont_t cont_f cont_m$
        | [33m'@'[39;49;00m ->$
            [34mlet[39;49;00m i = succ i [34min[39;49;00m$
            [34mif[39;49;00m i >= len [34mthen[39;49;00m invalid_format fmt i [34melse[39;49;00m$
            [34mbegin[39;49;00m [34mmatch[39;49;00m fmt.[i] [34mwith[39;49;00m$
            | [33m'['[39;49;00m ->$
               do_pp_open_box ppf n (succ i)$
            | [33m']'[39;49;00m ->$
               pp_close_box ppf [36m()[39;49;00m;$
               doprn n (succ i)$
            | [33m'{'[39;49;00m ->$
               do_pp_open_tag ppf n (succ i)$
            | [33m'}'[39;49;00m ->$
               pp_close_tag ppf [36m()[39;49;00m;$
               doprn n (succ i)$
            | [33m' '[39;49;00m ->$
               pp_print_space ppf [36m()[39;49;00m;$
               doprn n (succ i)$
            | [33m','[39;49;00m ->$
               pp_print_cut ppf [36m()[39;49;00m;$
               doprn n (succ i)$
            | [33m'?'[39;49;00m ->$
               pp_print_flush ppf [36m()[39;49;00m;$
               doprn n (succ i)$
            | [33m'.'[39;49;00m ->$
               pp_print_newline ppf [36m()[39;49;00m;$
               doprn n (succ i)$
            | [33m'\n'[39;49;00m ->$
               pp_force_newline ppf [36m()[39;49;00m;$
               doprn n (succ i)$
            | [33m';'[39;49;00m ->$
               do_pp_break ppf n (succ i)$
            | [33m'<'[39;49;00m ->$
               [34mlet[39;49;00m got_size size n i =$
                 print_as := [04m[32mSome[39;49;00m size;$
                 doprn n (skip_gt i) [34min[39;49;00m$
               get_int n (succ i) got_size$
            | [33m'@'[39;49;00m [34mas[39;49;00m c ->$
               pp_print_as_char c;$
               doprn n (succ i)$
            | c -> invalid_format fmt i$
            [34mend[39;49;00m$
        | c ->$
           pp_print_as_char c;$
           doprn n (succ i)$
$
      [35mand[39;49;00m cont_s n s i =$
        pp_print_as_string s; doprn n i$
      [35mand[39;49;00m cont_a n printer arg i =$
        [34mif[39;49;00m str [34mthen[39;49;00m$
          pp_print_as_string (([04m[36mObj[39;49;00m.magic printer : [36munit[39;49;00m -> _ -> [36mstring[39;49;00m) [36m()[39;49;00m arg)$
        [34melse[39;49;00m$
          printer ppf arg;$
        doprn n i$
      [35mand[39;49;00m cont_t n printer i =$
        [34mif[39;49;00m str [34mthen[39;49;00m$
          pp_print_as_string (([04m[36mObj[39;49;00m.magic printer : [36munit[39;49;00m -> [36mstring[39;49;00m) [36m()[39;49;00m)$
        [34melse[39;49;00m$
          printer ppf;$
        doprn n i$
      [35mand[39;49;00m cont_f n i =$
        pp_print_flush ppf [36m()[39;49;00m; doprn n i$
$
      [35mand[39;49;00m cont_m n sfmt i =$
        kprintf ([04m[36mObj[39;49;00m.magic ([34mfun[39;49;00m _ -> doprn n i)) sfmt$
$
      [35mand[39;49;00m get_int n i c =$
       [34mif[39;49;00m i >= len [34mthen[39;49;00m invalid_integer fmt i [34melse[39;49;00m$
       [34mmatch[39;49;00m fmt.[i] [34mwith[39;49;00m$
       | [33m' '[39;49;00m -> get_int n (succ i) c$
       | [33m'%'[39;49;00m ->$
          [34mlet[39;49;00m cont_s n s i = c (format_int_of_string fmt i s) n i$
          [35mand[39;49;00m cont_a n printer arg i = invalid_integer fmt i$
          [35mand[39;49;00m cont_t n printer i = invalid_integer fmt i$
          [35mand[39;49;00m cont_f n i = invalid_integer fmt i$
          [35mand[39;49;00m cont_m n sfmt i = invalid_integer fmt i [34min[39;49;00m$
          [04m[36mPrintf[39;49;00m.scan_format fmt v n i cont_s cont_a cont_t cont_f cont_m$
       | _ ->$
          [34mlet[39;49;00m [34mrec[39;49;00m get j =$
           [34mif[39;49;00m j >= len [34mthen[39;49;00m invalid_integer fmt j [34melse[39;49;00m$
           [34mmatch[39;49;00m fmt.[j] [34mwith[39;49;00m$
           | [33m'0'[39;49;00m .. [33m'9'[39;49;00m | [33m'-'[39;49;00m -> get (succ j)$
           | _ ->$
             [34mlet[39;49;00m size =$
             [34mif[39;49;00m j = i [34mthen[39;49;00m size_of_int [34m0[39;49;00m [34melse[39;49;00m$
                format_int_of_string fmt j ([04m[36mString[39;49;00m.sub fmt i (j - i)) [34min[39;49;00m$
             c size n j [34min[39;49;00m$
          get i$
$
      [35mand[39;49;00m skip_gt i =$
       [34mif[39;49;00m i >= len [34mthen[39;49;00m invalid_format fmt i [34melse[39;49;00m$
       [34mmatch[39;49;00m fmt.[i] [34mwith[39;49;00m$
       | [33m' '[39;49;00m -> skip_gt (succ i)$
       | [33m'>'[39;49;00m -> succ i$
       | _ -> invalid_format fmt i$
$
      [35mand[39;49;00m get_box_kind i =$
       [34mif[39;49;00m i >= len [34mthen[39;49;00m [04m[32mPp_box[39;49;00m, i [34melse[39;49;00m$
       [34mmatch[39;49;00m fmt.[i] [34mwith[39;49;00m$
       | [33m'h'[39;49;00m ->$
          [34mlet[39;49;00m i = succ i [34min[39;49;00m$
          [34mif[39;49;00m i >= len [34mthen[39;49;00m [04m[32mPp_hbox[39;49;00m, i [34melse[39;49;00m$
          [34mbegin[39;49;00m [34mmatch[39;49;00m fmt.[i] [34mwith[39;49;00m$
          | [33m'o'[39;49;00m ->$
             [34mlet[39;49;00m i = succ i [34min[39;49;00m$
             [34mif[39;49;00m i >= len [34mthen[39;49;00m format_invalid_arg [33m"[39;49;00m[33mbad box format[39;49;00m[33m"[39;49;00m fmt i [34melse[39;49;00m$
             [34mbegin[39;49;00m [34mmatch[39;49;00m fmt.[i] [34mwith[39;49;00m$
             | [33m'v'[39;49;00m -> [04m[32mPp_hovbox[39;49;00m, succ i$
             | c ->$
                format_invalid_arg$
                  ([33m"[39;49;00m[33mbad box name ho[39;49;00m[33m"[39;49;00m ^ [04m[36mString[39;49;00m.make [34m1[39;49;00m c) fmt i [34mend[39;49;00m$
          | [33m'v'[39;49;00m -> [04m[32mPp_hvbox[39;49;00m, succ i$
          | c -> [04m[32mPp_hbox[39;49;00m, i$
          [34mend[39;49;00m$
       | [33m'b'[39;49;00m -> [04m[32mPp_box[39;49;00m, succ i$
       | [33m'v'[39;49;00m -> [04m[32mPp_vbox[39;49;00m, succ i$
       | _ -> [04m[32mPp_box[39;49;00m, i$
$
      [35mand[39;49;00m get_tag_name n i c =$
       [34mlet[39;49;00m [34mrec[39;49;00m get accu n i j =$
        [34mif[39;49;00m j >= len$
        [34mthen[39;49;00m c (implode_rev ([04m[36mString[39;49;00m.sub fmt i (j - i)) accu) n j [34melse[39;49;00m$
        [34mmatch[39;49;00m fmt.[j] [34mwith[39;49;00m$
        | [33m'>'[39;49;00m -> c (implode_rev ([04m[36mString[39;49;00m.sub fmt i (j - i)) accu) n j$
        | [33m'%'[39;49;00m ->$
          [34mlet[39;49;00m s0 = [04m[36mString[39;49;00m.sub fmt i (j - i) [34min[39;49;00m$
          [34mlet[39;49;00m cont_s n s i = get (s :: s0 :: accu) n i i$
          [35mand[39;49;00m cont_a n printer arg i =$
            [34mlet[39;49;00m s =$
              [34mif[39;49;00m str$
              [34mthen[39;49;00m ([04m[36mObj[39;49;00m.magic printer : [36munit[39;49;00m -> _ -> [36mstring[39;49;00m) [36m()[39;49;00m arg$
              [34melse[39;49;00m exstring printer arg [34min[39;49;00m$
            get (s :: s0 :: accu) n i i$
          [35mand[39;49;00m cont_t n printer i =$
            [34mlet[39;49;00m s =$
              [34mif[39;49;00m str$
              [34mthen[39;49;00m ([04m[36mObj[39;49;00m.magic printer : [36munit[39;49;00m -> [36mstring[39;49;00m) [36m()[39;49;00m$
              [34melse[39;49;00m exstring ([34mfun[39;49;00m ppf [36m()[39;49;00m -> printer ppf) [36m()[39;49;00m [34min[39;49;00m$
            get (s :: s0 :: accu) n i i$
          [35mand[39;49;00m cont_f n i =$
            format_invalid_arg [33m"[39;49;00m[33mbad tag name specification[39;49;00m[33m"[39;49;00m fmt i$
          [35mand[39;49;00m cont_m n sfmt i =$
            format_invalid_arg [33m"[39;49;00m[33mbad tag name specification[39;49;00m[33m"[39;49;00m fmt i [34min[39;49;00m$
          [04m[36mPrintf[39;49;00m.scan_format fmt v n j cont_s cont_a cont_t cont_f cont_m$
        | c -> get accu n i (succ j) [34min[39;49;00m$
       get [36m[][39;49;00m n i i$
$
      [35mand[39;49;00m do_pp_break ppf n i =$
       [34mif[39;49;00m i >= len [34mthen[39;49;00m [34mbegin[39;49;00m pp_print_space ppf [36m()[39;49;00m; doprn n i [34mend[39;49;00m [34melse[39;49;00m$
       [34mmatch[39;49;00m fmt.[i] [34mwith[39;49;00m$
       | [33m'<'[39;49;00m ->$
          [34mlet[39;49;00m [34mrec[39;49;00m got_nspaces nspaces n i =$
            get_int n i (got_offset nspaces)$
          [35mand[39;49;00m got_offset nspaces offset n i =$
            pp_print_break ppf (int_of_size nspaces) (int_of_size offset);$
            doprn n (skip_gt i) [34min[39;49;00m$
          get_int n (succ i) got_nspaces$
       | c -> pp_print_space ppf [36m()[39;49;00m; doprn n i$
$
      [35mand[39;49;00m do_pp_open_box ppf n i =$
       [34mif[39;49;00m i >= len [34mthen[39;49;00m [34mbegin[39;49;00m pp_open_box_gen ppf [34m0[39;49;00m [04m[32mPp_box[39;49;00m; doprn n i [34mend[39;49;00m [34melse[39;49;00m$
       [34mmatch[39;49;00m fmt.[i] [34mwith[39;49;00m$
       | [33m'<'[39;49;00m ->$
          [34mlet[39;49;00m kind, i = get_box_kind (succ i) [34min[39;49;00m$
          [34mlet[39;49;00m got_size size n i =$
            pp_open_box_gen ppf (int_of_size size) kind;$
            doprn n (skip_gt i) [34min[39;49;00m$
          get_int n i got_size$
       | c -> pp_open_box_gen ppf [34m0[39;49;00m [04m[32mPp_box[39;49;00m; doprn n i$
$
      [35mand[39;49;00m do_pp_open_tag ppf n i =$
       [34mif[39;49;00m i >= len [34mthen[39;49;00m [34mbegin[39;49;00m pp_open_tag ppf [33m"[39;49;00m[33m"[39;49;00m; doprn n i [34mend[39;49;00m [34melse[39;49;00m$
       [34mmatch[39;49;00m fmt.[i] [34mwith[39;49;00m$
       | [33m'<'[39;49;00m ->$
          [34mlet[39;49;00m got_name tag_name n i =$
            pp_open_tag ppf tag_name;$
            doprn n (skip_gt i) [34min[39;49;00m$
          get_tag_name n (succ i) got_name$
       | c -> pp_open_tag ppf [33m"[39;49;00m[33m"[39;49;00m; doprn n i [34min[39;49;00m$
$
      doprn ([04m[36mPrintf[39;49;00m.index_of_int [34m0[39;49;00m) [34m0[39;49;00m [34min[39;49;00m$
$
   [04m[36mPrintf[39;49;00m.kapr kpr fmt [34min[39;49;00m$
$
  kprintf;;$
$
[37m(*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m  Defining [fprintf] and various flavors of [fprintf].[39;49;00m$
[37m[39;49;00m$
[37m [39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*[39;49;00m[37m*)[39;49;00m$
$
[34mlet[39;49;00m kfprintf k ppf = mkprintf [36mfalse[39;49;00m ([34mfun[39;49;00m _ -> ppf) k;;$
$
[34mlet[39;49;00m fprintf ppf = kfprintf ignore ppf;;$
[34mlet[39;49;00m printf fmt = fprintf std_formatter fmt;;$
[34mlet[39;49;00m eprintf fmt = fprintf err_formatter fmt;;$
$
[34mlet[39;49;00m kbprintf k b =$
  mkprintf [36mfalse[39;49;00m ([34mfun[39;49;00m _ -> formatter_of_buffer b) k;;$
$
[34mlet[39;49;00m bprintf b = kbprintf ignore b;;$
$
[34mlet[39;49;00m ksprintf k =$
  [34mlet[39;49;00m b = [04m[36mBuffer[39;49;00m.create [34m512[39;49;00m [34min[39;49;00m$
  [34mlet[39;49;00m k ppf = k (string_out b ppf) [34min[39;49;00m$
  mkprintf [36mtrue[39;49;00m ([34mfun[39;49;00m _ -> formatter_of_buffer b) k;;$
$
[34mlet[39;49;00m kprintf = ksprintf;;$
$
[34mlet[39;49;00m sprintf fmt = ksprintf ([34mfun[39;49;00m s -> s) fmt;;$
$
at_exit print_flush;;$
