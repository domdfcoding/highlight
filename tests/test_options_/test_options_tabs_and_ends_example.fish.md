[37m# -----------------------------------------------------------------------------[39;49;00m$
[37m# Fishshell Samples[39;49;00m$
[37m#  |- Theme / bobthefish[39;49;00m$
[37m#  |- Function / funced[39;49;00m$
[37m#  |- Configuration / config.fish[39;49;00m$
[37m# -----------------------------------------------------------------------------[39;49;00m$
$
[37m# name: bobthefish[39;49;00m$
[37m#[39;49;00m$
[37m# bobthefish is a Powerline-style, Git-aware fish theme optimized for awesome.[39;49;00m$
[37m#[39;49;00m$
[37m# You will probably need a Powerline-patched font for this to work:[39;49;00m$
[37m#[39;49;00m$
[37m#     https://powerline.readthedocs.org/en/latest/fontpatching.html[39;49;00m$
[37m#[39;49;00m$
[37m# I recommend picking one of these:[39;49;00m$
[37m#[39;49;00m$
[37m#     https://github.com/Lokaltog/powerline-fonts[39;49;00m$
[37m#[39;49;00m$
[37m# You can override some default options in your config.fish:[39;49;00m$
[37m#[39;49;00m$
[37m#     set -g theme_display_user yes[39;49;00m$
[37m#     set -g default_user your_normal_user[39;49;00m$
$
[34mset[39;49;00m -g __bobthefish_current_bg NONE$
$
[37m# Powerline glyphs[39;49;00m$
[34mset[39;49;00m __bobthefish_branch_glyph            [33m\u[39;49;00mE0A0$
[34mset[39;49;00m __bobthefish_ln_glyph                [33m\u[39;49;00mE0A1$
[34mset[39;49;00m __bobthefish_padlock_glyph           [33m\u[39;49;00mE0A2$
[34mset[39;49;00m __bobthefish_right_black_arrow_glyph [33m\u[39;49;00mE0B0$
[34mset[39;49;00m __bobthefish_right_arrow_glyph       [33m\u[39;49;00mE0B1$
[34mset[39;49;00m __bobthefish_left_black_arrow_glyph  [33m\u[39;49;00mE0B2$
[34mset[39;49;00m __bobthefish_left_arrow_glyph        [33m\u[39;49;00mE0B3$
$
[37m# Additional glyphs[39;49;00m$
[34mset[39;49;00m __bobthefish_detached_glyph          [33m\u[39;49;00m27A6$
[34mset[39;49;00m __bobthefish_nonzero_exit_glyph      [33m'! '[39;49;00m$
[34mset[39;49;00m __bobthefish_superuser_glyph         [33m'$ '[39;49;00m$
[34mset[39;49;00m __bobthefish_bg_job_glyph            [33m'% '[39;49;00m$
[34mset[39;49;00m __bobthefish_hg_glyph                [33m\u[39;49;00m263F$
$
[37m# Python glyphs[39;49;00m$
[34mset[39;49;00m __bobthefish_superscript_glyph       [33m\u[39;49;00m00B9 [33m\u[39;49;00m00B2 [33m\u[39;49;00m00B3$
[34mset[39;49;00m __bobthefish_virtualenv_glyph        [33m\u[39;49;00m25F0$
[34mset[39;49;00m __bobthefish_pypy_glyph              [33m\u[39;49;00m1D56$
$
[37m# Colors[39;49;00m$
[34mset[39;49;00m __bobthefish_lt_green   addc10$
[34mset[39;49;00m __bobthefish_med_green  189303$
[34mset[39;49;00m __bobthefish_dk_green   0c4801$
$
[34mset[39;49;00m __bobthefish_lt_red     C99$
[34mset[39;49;00m __bobthefish_med_red    ce000f$
[34mset[39;49;00m __bobthefish_dk_red     600$
$
[34mset[39;49;00m __bobthefish_slate_blue 255e87$
$
[34mset[39;49;00m __bobthefish_lt_orange  f6b117$
[34mset[39;49;00m __bobthefish_dk_orange  3a2a03$
$
[34mset[39;49;00m __bobthefish_dk_grey    333$
[34mset[39;49;00m __bobthefish_med_grey   999$
[34mset[39;49;00m __bobthefish_lt_grey    ccc$
$
[34mset[39;49;00m __bobthefish_dk_brown   4d2600$
[34mset[39;49;00m __bobthefish_med_brown  803F00$
[34mset[39;49;00m __bobthefish_lt_brown   BF5E00$
$
[34mset[39;49;00m __bobthefish_dk_blue    1E2933$
[34mset[39;49;00m __bobthefish_med_blue   275379$
[34mset[39;49;00m __bobthefish_lt_blue    326D9E$
$
[37m# ===========================[39;49;00m$
[37m# Helper methods[39;49;00m$
[37m# ===========================[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_in_git -d [33m'Check whether pwd is inside a git repo'[39;49;00m$
  [36mcommand [39;49;00mwhich git > /dev/null 2>&1; [34mand[39;49;00m [36mcommand [39;49;00mgit rev-parse --is-inside-work-tree >/dev/null 2>&1$
[34mend[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_in_hg -d [33m'Check whether pwd is inside a hg repo'[39;49;00m$
  [36mcommand [39;49;00mwhich hg > /dev/null 2>&1; [34mand[39;49;00m [36mcommand [39;49;00mhg stat > /dev/null 2>&1$
[34mend[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_git_branch -d [33m'Get the current git branch (or commitish)'[39;49;00m$
  [34mset[39;49;00m -l ref ([36mcommand [39;49;00mgit symbolic-ref HEAD 2> /dev/null)$
  [34mif[39;49;00m [ [31m$status[39;49;00m -gt [34m0[39;49;00m ]$
    [34mset[39;49;00m -l branch ([36mcommand [39;49;00mgit show-ref --head -s --abbrev |head -n1 2> /dev/null)$
    [34mset[39;49;00m ref [33m"[39;49;00m[31m$__bobthefish_detached_glyph[39;49;00m[33m [39;49;00m[31m$branch[39;49;00m[33m"[39;49;00m$
  [34mend[39;49;00m$
  [34mecho[39;49;00m [31m$ref[39;49;00m | sed  [33m"[39;49;00m[33ms-refs/heads/-[39;49;00m[31m$__bobthefish_branch_glyph[39;49;00m[33m -[39;49;00m[33m"[39;49;00m$
[34mend[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_hg_branch -d [33m'Get the current hg branch'[39;49;00m$
  [34mset[39;49;00m -l branch (hg branch ^/dev/null)$
  [34mset[39;49;00m -l book [33m" @ "[39;49;00m(hg book | grep [33m\*[39;49;00m | cut -d[33m\ [39;49;00m -f3)$
  [34mecho[39;49;00m [33m"[39;49;00m[31m$__bobthefish_branch_glyph[39;49;00m[33m [39;49;00m[31m$branch[39;49;00m[31m$book[39;49;00m[33m"[39;49;00m$
[34mend[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_pretty_parent -d [33m'Print a parent directory, shortened to fit the prompt'[39;49;00m$
  [34mecho[39;49;00m -n (dirname [31m$argv[39;49;00m[1]) | sed -e [33m's|/private||'[39;49;00m -e [33m"[39;49;00m[33ms|^[39;49;00m[31m$HOME[39;49;00m[33m|~|[39;49;00m[33m"[39;49;00m -e [33m's-/\(\.\{0,1\}[^/]\)\([^/]*\)-/\1-g'[39;49;00m -e [33m's|/$||'[39;49;00m$
[34mend[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_git_project_dir -d [33m'Print the current git project base directory'[39;49;00m$
  [36mcommand [39;49;00mgit rev-parse --show-toplevel 2>/dev/null$
[34mend[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_hg_project_dir -d [33m'Print the current hg project base directory'[39;49;00m$
  [36mcommand [39;49;00mhg root 2>/dev/null$
[34mend[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_project_pwd -d [33m'Print the working directory relative to project root'[39;49;00m$
  [34mecho[39;49;00m [33m"[39;49;00m[31m$PWD[39;49;00m[33m"[39;49;00m | sed -e [33m"[39;49;00m[33ms*[39;49;00m[31m$argv[39;49;00m[33m[1]**g[39;49;00m[33m"[39;49;00m -e [33m's*^/**'[39;49;00m$
[34mend[39;49;00m$
$
$
[37m# ===========================[39;49;00m$
[37m# Segment functions[39;49;00m$
[37m# ===========================[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_start_segment -d [33m'Start a prompt segment'[39;49;00m$
  [36mset_color[39;49;00m -b [31m$argv[39;49;00m[1]$
  [36mset_color[39;49;00m [31m$argv[39;49;00m[2]$
  [34mif[39;49;00m [ [33m"[39;49;00m[31m$__bobthefish_current_bg[39;49;00m[33m"[39;49;00m = [33m'NONE'[39;49;00m ]$
    [37m# If there's no background, just start one[39;49;00m$
    [34mecho[39;49;00m -n [33m' '[39;49;00m$
  [34melse[39;49;00m$
    [37m# If there's already a background...[39;49;00m$
    [34mif[39;49;00m [ [33m"[39;49;00m[31m$argv[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m = [33m"[39;49;00m[31m$__bobthefish_current_bg[39;49;00m[33m"[39;49;00m ]$
      [37m# and it's the same color, draw a separator[39;49;00m$
      [34mecho[39;49;00m -n [33m"[39;49;00m[31m$__bobthefish_right_arrow_glyph[39;49;00m[33m [39;49;00m[33m"[39;49;00m$
    [34melse[39;49;00m$
      [37m# otherwise, draw the end of the previous segment and the start of the next[39;49;00m$
      [36mset_color[39;49;00m [31m$__bobthefish_current_bg[39;49;00m$
      [34mecho[39;49;00m -n [33m"[39;49;00m[31m$__bobthefish_right_black_arrow_glyph[39;49;00m[33m [39;49;00m[33m"[39;49;00m$
      [36mset_color[39;49;00m [31m$argv[39;49;00m[2]$
    [34mend[39;49;00m$
  [34mend[39;49;00m$
  [34mset[39;49;00m __bobthefish_current_bg [31m$argv[39;49;00m[1]$
[34mend[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_path_segment -d [33m'Display a shortened form of a directory'[39;49;00m$
  [34mif[39;49;00m [34mtest[39;49;00m -w [33m"[39;49;00m[31m$argv[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m$
    __bobthefish_start_segment [31m$__bobthefish_dk_grey[39;49;00m [31m$__bobthefish_med_grey[39;49;00m$
  [34melse[39;49;00m$
    __bobthefish_start_segment [31m$__bobthefish_dk_red[39;49;00m [31m$__bobthefish_lt_red[39;49;00m$
  [34mend[39;49;00m$
$
  [34mset[39;49;00m -l directory$
  [34mset[39;49;00m -l parent$
$
  [34mswitch[39;49;00m [33m"[39;49;00m[31m$argv[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m$
    [34mcase[39;49;00m /$
      [34mset[39;49;00m directory [33m'/'[39;49;00m$
    [34mcase[39;49;00m [33m"[39;49;00m[31m$HOME[39;49;00m[33m"[39;49;00m$
      [34mset[39;49;00m directory [33m'~'[39;49;00m$
    [34mcase[39;49;00m [33m'*'[39;49;00m$
      [34mset[39;49;00m parent    (__bobthefish_pretty_parent [33m"[39;49;00m[31m$argv[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m)$
      [34mset[39;49;00m parent    [33m"[39;49;00m[31m$parent[39;49;00m[33m/[39;49;00m[33m"[39;49;00m$
      [34mset[39;49;00m directory (basename [33m"[39;49;00m[31m$argv[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m)$
  [34mend[39;49;00m$
$
  [34mtest[39;49;00m [33m"[39;49;00m[31m$parent[39;49;00m[33m"[39;49;00m; [34mand[39;49;00m [34mecho[39;49;00m -n -s [33m"[39;49;00m[31m$parent[39;49;00m[33m"[39;49;00m$
  [36mset_color [39;49;00mfff --bold$
  [34mecho[39;49;00m -n [33m"[39;49;00m[31m$directory[39;49;00m[33m [39;49;00m[33m"[39;49;00m$
  [36mset_color [39;49;00mnormal$
[34mend[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_finish_segments -d [33m'Close open prompt segments'[39;49;00m$
  [34mif[39;49;00m [ -n [31m$__bobthefish_current_bg[39;49;00m -a [31m$__bobthefish_current_bg[39;49;00m != [33m'NONE'[39;49;00m ]$
    [36mset_color[39;49;00m -b normal$
    [36mset_color[39;49;00m [31m$__bobthefish_current_bg[39;49;00m$
    [34mecho[39;49;00m -n [33m"[39;49;00m[31m$__bobthefish_right_black_arrow_glyph[39;49;00m[33m [39;49;00m[33m"[39;49;00m$
    [36mset_color [39;49;00mnormal$
  [34mend[39;49;00m$
  [34mset[39;49;00m -g __bobthefish_current_bg NONE$
[34mend[39;49;00m$
$
$
[37m# ===========================[39;49;00m$
[37m# Theme components[39;49;00m$
[37m# ===========================[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_prompt_status -d [33m'Display symbols for a non zero exit status, root and background jobs'[39;49;00m$
  [34mset[39;49;00m -l nonzero$
  [34mset[39;49;00m -l superuser$
  [34mset[39;49;00m -l bg_jobs$
$
  [37m# Last exit was nonzero[39;49;00m$
  [34mif[39;49;00m [ [31m$status[39;49;00m -ne [34m0[39;49;00m ]$
    [34mset[39;49;00m nonzero [31m$__bobthefish_nonzero_exit_glyph[39;49;00m$
  [34mend[39;49;00m$
$
  [37m# if superuser (uid == 0)[39;49;00m$
  [34mset[39;49;00m -l uid (id -u [31m$USER[39;49;00m)$
  [34mif[39;49;00m [ [31m$uid[39;49;00m -eq [34m0[39;49;00m ]$
    [34mset[39;49;00m superuser [31m$__bobthefish_superuser_glyph[39;49;00m$
  [34mend[39;49;00m$
$
  [37m# Jobs display[39;49;00m$
  [34mif[39;49;00m [ ([36mjobs[39;49;00m -l | wc -l) -gt [34m0[39;49;00m ]$
    [34mset[39;49;00m bg_jobs [31m$__bobthefish_bg_job_glyph[39;49;00m$
  [34mend[39;49;00m$
$
  [34mset[39;49;00m -l status_flags [33m"[39;49;00m[31m$nonzero[39;49;00m[31m$superuser[39;49;00m[31m$bg_jobs[39;49;00m[33m"[39;49;00m$
$
  [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$nonzero[39;49;00m[33m"[39;49;00m -o [33m"[39;49;00m[31m$superuser[39;49;00m[33m"[39;49;00m -o [33m"[39;49;00m[31m$bg_jobs[39;49;00m[33m"[39;49;00m$
    __bobthefish_start_segment fff 000$
    [34mif[39;49;00m [ [33m"[39;49;00m[31m$nonzero[39;49;00m[33m"[39;49;00m ]$
      [36mset_color[39;49;00m [31m$__bobthefish_med_red[39;49;00m --bold$
      [34mecho[39;49;00m -n [31m$__bobthefish_nonzero_exit_glyph[39;49;00m$
    [34mend[39;49;00m$
$
    [34mif[39;49;00m [ [33m"[39;49;00m[31m$superuser[39;49;00m[33m"[39;49;00m ]$
      [36mset_color[39;49;00m [31m$__bobthefish_med_green[39;49;00m --bold$
      [34mecho[39;49;00m -n [31m$__bobthefish_superuser_glyph[39;49;00m$
    [34mend[39;49;00m$
$
    [34mif[39;49;00m [ [33m"[39;49;00m[31m$bg_jobs[39;49;00m[33m"[39;49;00m ]$
      [36mset_color[39;49;00m [31m$__bobthefish_slate_blue[39;49;00m --bold$
      [34mecho[39;49;00m -n [31m$__bobthefish_bg_job_glyph[39;49;00m$
    [34mend[39;49;00m$
$
    [36mset_color [39;49;00mnormal$
  [34mend[39;49;00m$
[34mend[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_prompt_user -d [33m'Display actual user if different from $default_user'[39;49;00m$
  [34mif[39;49;00m [ [33m"[39;49;00m[31m$theme_display_user[39;49;00m[33m"[39;49;00m = [33m'yes'[39;49;00m ]$
    [34mif[39;49;00m [ [33m"[39;49;00m[31m$USER[39;49;00m[33m"[39;49;00m != [33m"[39;49;00m[31m$default_user[39;49;00m[33m"[39;49;00m -o -n [33m"[39;49;00m[31m$SSH_CLIENT[39;49;00m[33m"[39;49;00m ]$
      __bobthefish_start_segment [31m$__bobthefish_lt_grey[39;49;00m [31m$__bobthefish_slate_blue[39;49;00m$
      [34mecho[39;49;00m -n -s (whoami) [33m'@'[39;49;00m (hostname | cut -d . -f 1) [33m' '[39;49;00m$
    [34mend[39;49;00m$
  [34mend[39;49;00m$
[34mend[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_prompt_hg -d [33m'Display the actual hg state'[39;49;00m$
  [34mset[39;49;00m -l dirty   ([36mcommand [39;49;00mhg stat; [34mor[39;49;00m [34mecho[39;49;00m -n [33m'*'[39;49;00m)$
$
  [34mset[39;49;00m -l flags [33m"[39;49;00m[31m$dirty[39;49;00m[33m"[39;49;00m$
  [34mtest[39;49;00m [33m"[39;49;00m[31m$flags[39;49;00m[33m"[39;49;00m; [34mand[39;49;00m [34mset[39;49;00m flags [33m""[39;49;00m$
$
  [34mset[39;49;00m -l flag_bg [31m$__bobthefish_lt_green[39;49;00m$
  [34mset[39;49;00m -l flag_fg [31m$__bobthefish_dk_green[39;49;00m$
  [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$dirty[39;49;00m[33m"[39;49;00m$
    [34mset[39;49;00m flag_bg [31m$__bobthefish_med_red[39;49;00m$
    [34mset[39;49;00m flag_fg fff$
  [34mend[39;49;00m$
$
  __bobthefish_path_segment (__bobthefish_hg_project_dir)$
$
  __bobthefish_start_segment [31m$flag_bg[39;49;00m [31m$flag_fg[39;49;00m$
  [34mecho[39;49;00m -n -s [31m$__bobthefish_hg_glyph[39;49;00m [33m' '[39;49;00m$
$
  __bobthefish_start_segment [31m$flag_bg[39;49;00m [31m$flag_fg[39;49;00m$
  [36mset_color[39;49;00m [31m$flag_fg[39;49;00m --bold$
  [34mecho[39;49;00m -n -s (__bobthefish_hg_branch) [31m$flags[39;49;00m [33m' '[39;49;00m$
  [36mset_color [39;49;00mnormal$
$
  [34mset[39;49;00m -l project_pwd  (__bobthefish_project_pwd (__bobthefish_hg_project_dir))$
  [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$project_pwd[39;49;00m[33m"[39;49;00m$
    [34mif[39;49;00m [34mtest[39;49;00m -w [33m"[39;49;00m[31m$PWD[39;49;00m[33m"[39;49;00m$
      __bobthefish_start_segment [34m333[39;49;00m 999$
    [34melse[39;49;00m$
      __bobthefish_start_segment [31m$__bobthefish_med_red[39;49;00m [31m$__bobthefish_lt_red[39;49;00m$
    [34mend[39;49;00m$
$
    [34mecho[39;49;00m -n -s [31m$project_pwd[39;49;00m [33m' '[39;49;00m$
  [34mend[39;49;00m$
[34mend[39;49;00m$
$
[37m# TODO: clean up the fugly $ahead business[39;49;00m$
[34mfunction[39;49;00m __bobthefish_prompt_git -d [33m'Display the actual git state'[39;49;00m$
  [34mset[39;49;00m -l dirty   ([36mcommand [39;49;00mgit diff --no-ext-diff --quiet --exit-code; [34mor[39;49;00m [34mecho[39;49;00m -n [33m'*'[39;49;00m)$
  [34mset[39;49;00m -l staged  ([36mcommand [39;49;00mgit diff --cached --no-ext-diff --quiet --exit-code; [34mor[39;49;00m [34mecho[39;49;00m -n [33m'~'[39;49;00m)$
  [34mset[39;49;00m -l stashed ([36mcommand [39;49;00mgit rev-parse --verify refs/stash > /dev/null 2>&1; [34mand[39;49;00m [34mecho[39;49;00m -n [33m'$'[39;49;00m)$
  [34mset[39;49;00m -l ahead   ([36mcommand [39;49;00mgit branch -v 2> /dev/null | grep -Eo [33m'^\* [^ ]* *[^ ]* *\[[^]]*\]'[39;49;00m | grep -Eo [33m'\[[^]]*\]$'[39;49;00m | awk [33m'ORS="";/ahead/ {print "+"} /behind/ {print "-"}'[39;49;00m | sed -e [33m's/+-/±/'[39;49;00m)$
$
  [34mset[39;49;00m -l new ([36mcommand [39;49;00mgit ls-files --other --exclude-standard);$
  [34mtest[39;49;00m [33m"[39;49;00m[31m$new[39;49;00m[33m"[39;49;00m; [34mand[39;49;00m [34mset[39;49;00m new [33m'…'[39;49;00m$
$
  [34mset[39;49;00m -l flags   [33m"[39;49;00m[31m$dirty[39;49;00m[31m$staged[39;49;00m[31m$stashed[39;49;00m[31m$ahead[39;49;00m[31m$new[39;49;00m[33m"[39;49;00m$
  [34mtest[39;49;00m [33m"[39;49;00m[31m$flags[39;49;00m[33m"[39;49;00m; [34mand[39;49;00m [34mset[39;49;00m flags [33m"[39;49;00m[33m [39;49;00m[31m$flags[39;49;00m[33m"[39;49;00m$
$
  [34mset[39;49;00m -l flag_bg [31m$__bobthefish_lt_green[39;49;00m$
  [34mset[39;49;00m -l flag_fg [31m$__bobthefish_dk_green[39;49;00m$
  [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$dirty[39;49;00m[33m"[39;49;00m -o [33m"[39;49;00m[31m$staged[39;49;00m[33m"[39;49;00m$
    [34mset[39;49;00m flag_bg [31m$__bobthefish_med_red[39;49;00m$
    [34mset[39;49;00m flag_fg fff$
  [34melse[39;49;00m$
    [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$stashed[39;49;00m[33m"[39;49;00m$
      [34mset[39;49;00m flag_bg [31m$__bobthefish_lt_orange[39;49;00m$
      [34mset[39;49;00m flag_fg [31m$__bobthefish_dk_orange[39;49;00m$
    [34mend[39;49;00m$
  [34mend[39;49;00m$
$
  __bobthefish_path_segment (__bobthefish_git_project_dir)$
$
  __bobthefish_start_segment [31m$flag_bg[39;49;00m [31m$flag_fg[39;49;00m$
  [36mset_color[39;49;00m [31m$flag_fg[39;49;00m --bold$
  [34mecho[39;49;00m -n -s (__bobthefish_git_branch) [31m$flags[39;49;00m [33m' '[39;49;00m$
  [36mset_color [39;49;00mnormal$
$
  [34mset[39;49;00m -l project_pwd  (__bobthefish_project_pwd (__bobthefish_git_project_dir))$
  [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$project_pwd[39;49;00m[33m"[39;49;00m$
    [34mif[39;49;00m [34mtest[39;49;00m -w [33m"[39;49;00m[31m$PWD[39;49;00m[33m"[39;49;00m$
      __bobthefish_start_segment [34m333[39;49;00m 999$
    [34melse[39;49;00m$
      __bobthefish_start_segment [31m$__bobthefish_med_red[39;49;00m [31m$__bobthefish_lt_red[39;49;00m$
    [34mend[39;49;00m$
$
    [34mecho[39;49;00m -n -s [31m$project_pwd[39;49;00m [33m' '[39;49;00m$
  [34mend[39;49;00m$
[34mend[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_prompt_dir -d [33m'Display a shortened form of the current directory'[39;49;00m$
  __bobthefish_path_segment [33m"[39;49;00m[31m$PWD[39;49;00m[33m"[39;49;00m$
[34mend[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_in_virtualfish_virtualenv$
  [34mset[39;49;00m -q VIRTUAL_ENV$
[34mend[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_virtualenv_python_version -d [33m'Get current python version'[39;49;00m$
  [34mswitch[39;49;00m (readlink (which python))$
    [34mcase[39;49;00m python2$
      [34mecho[39;49;00m [31m$__bobthefish_superscript_glyph[39;49;00m[2]$
    [34mcase[39;49;00m python3$
      [34mecho[39;49;00m [31m$__bobthefish_superscript_glyph[39;49;00m[3]$
    [34mcase[39;49;00m pypy$
      [34mecho[39;49;00m [31m$__bobthefish_pypy_glyph[39;49;00m$
    [34mend[39;49;00m$
[34mend[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_virtualenv -d [33m'Get the current virtualenv'[39;49;00m$
  [34mecho[39;49;00m [31m$__bobthefish_virtualenv_glyph[39;49;00m(__bobthefish_virtualenv_python_version) (basename [33m"[39;49;00m[31m$VIRTUAL_ENV[39;49;00m[33m"[39;49;00m)$
[34mend[39;49;00m$
$
[34mfunction[39;49;00m __bobthefish_prompt_virtualfish -d [33m"Display activated virtual environment (only for virtualfish, virtualenv's activate.fish changes prompt by itself)"[39;49;00m$
  [34mset[39;49;00m flag_bg [31m$__bobthefish_lt_blue[39;49;00m$
  [34mset[39;49;00m flag_fg [31m$__bobthefish_dk_blue[39;49;00m$
  __bobthefish_start_segment [31m$flag_bg[39;49;00m [31m$flag_fg[39;49;00m$
  [36mset_color[39;49;00m [31m$flag_fg[39;49;00m --bold$
  [34mecho[39;49;00m -n -s (__bobthefish_virtualenv) [31m$flags[39;49;00m [33m' '[39;49;00m$
  [36mset_color [39;49;00mnormal$
[34mend[39;49;00m$
$
$
[37m# ===========================[39;49;00m$
[37m# Apply theme[39;49;00m$
[37m# ===========================[39;49;00m$
$
[34mfunction[39;49;00m [36mfish_prompt[39;49;00m -d [33m'bobthefish, a fish theme optimized for awesome'[39;49;00m$
  __bobthefish_prompt_status$
  __bobthefish_prompt_user$
  [34mif[39;49;00m __bobthefish_in_virtualfish_virtualenv$
    __bobthefish_prompt_virtualfish$
  [34mend[39;49;00m$
  [34mif[39;49;00m __bobthefish_in_git       [37m# TODO: do this right.[39;49;00m$
    __bobthefish_prompt_git    [37m# if something is in both git and hg, check the length of[39;49;00m$
  [34melse[39;49;00m [34mif[39;49;00m __bobthefish_in_hg   [37m# __bobthefish_git_project_dir vs __bobthefish_hg_project_dir[39;49;00m$
    __bobthefish_prompt_hg     [37m# and pick the longer of the two.[39;49;00m$
  [34melse[39;49;00m$
    __bobthefish_prompt_dir$
  [34mend[39;49;00m$
  __bobthefish_finish_segments$
[34mend[39;49;00m$
$
[37m# -----------------------------------------------------------------------------[39;49;00m$
[37m# funced - edit a function interactively[39;49;00m$
[37m#[39;49;00m$
[37m# Synopsis[39;49;00m$
[37m#[39;49;00m$
[37m#   funced [OPTIONS] NAME[39;49;00m$
[37m#[39;49;00m$
[37m# Description[39;49;00m$
[37m#[39;49;00m$
[37m#   funced provides an interface to edit the definition of the function NAME.[39;49;00m$
[37m# -----------------------------------------------------------------------------[39;49;00m$
$
[34mfunction[39;49;00m [36mfunced[39;49;00m --description [33m'Edit function definition'[39;49;00m$
    [34mset[39;49;00m -l editor [31m$EDITOR[39;49;00m$
    [34mset[39;49;00m -l interactive$
    [34mset[39;49;00m -l funcname$
    [34mwhile[39;49;00m [34mset[39;49;00m -q argv[1]$
        [34mswitch[39;49;00m [31m$argv[39;49;00m[1]$
            [34mcase[39;49;00m -h --help$
                __fish_print_help [36mfunced[39;49;00m$
[36m                [39;49;00m[34mreturn[39;49;00m 0$
$
            [34mcase[39;49;00m -e --editor$
                [34mset[39;49;00m editor [31m$argv[39;49;00m[2]$
                [34mset[39;49;00m -e argv[2]$
$
            [34mcase[39;49;00m -i --interactive$
                [34mset[39;49;00m interactive 1$
$
            [34mcase[39;49;00m --$
                [34mset[39;49;00m funcname [31m$funcname[39;49;00m [31m$argv[39;49;00m[2]$
                [34mset[39;49;00m -e argv[2]$
$
            [34mcase[39;49;00m [33m'-*'[39;49;00m$
                [36mset_color [39;49;00mred$
                [36mprintf[39;49;00m (_ [33m"%s: Unknown option %s\n"[39;49;00m) [36mfunced[39;49;00m [31m$argv[39;49;00m[1]$
                [36mset_color [39;49;00mnormal$
                [34mreturn[39;49;00m 1$
$
            [34mcase[39;49;00m [33m'*'[39;49;00m [33m'.*'[39;49;00m$
                [34mset[39;49;00m funcname [31m$funcname[39;49;00m [31m$argv[39;49;00m[1]$
        [34mend[39;49;00m$
        [34mset[39;49;00m -e argv[1]$
    [34mend[39;49;00m$
$
    [34mif[39;49;00m [34mbegin[39;49;00m; [34mset[39;49;00m -q funcname[2]; [34mor[39;49;00m [34mnot[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$funcname[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m; [34mend[39;49;00m$
        [36mset_color [39;49;00mred$
        _ [33m"funced: You must specify one function name[39;49;00m$
[33m"[39;49;00m$
        [36mset_color [39;49;00mnormal$
        [34mreturn[39;49;00m 1$
    [34mend[39;49;00m$
$
    [34mset[39;49;00m -l init$
    [34mswitch[39;49;00m [31m$funcname[39;49;00m$
        [34mcase[39;49;00m [33m'-*'[39;49;00m$
        [34mset[39;49;00m init [34mfunction[39;49;00m -- [31m$funcname[39;49;00m[33m\n[39;49;00m[33m\n[39;49;00mend$
        [34mcase[39;49;00m [33m'*'[39;49;00m$
        [34mset[39;49;00m init [34mfunction[39;49;00m [31m$funcname[39;49;00m[33m\n[39;49;00m[33m\n[39;49;00mend$
    [34mend[39;49;00m$
$
    [37m# Break editor up to get its first command (i.e. discard flags)[39;49;00m$
    [34mif[39;49;00m [34mtest[39;49;00m -n [33m"[39;49;00m[31m$editor[39;49;00m[33m"[39;49;00m$
        [34mset[39;49;00m -l editor_cmd$
        [36meval [39;49;00m[34mset[39;49;00m editor_cmd [31m$editor[39;49;00m$
        [34mif[39;49;00m [34mnot[39;49;00m [36mtype[39;49;00m -f [33m"[39;49;00m[31m$editor_cmd[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m >/dev/null$
            _ [33m"[39;49;00m[33mfunced: The value for \$EDITOR '[39;49;00m[31m$editor[39;49;00m[33m' could not be used because the command '[39;49;00m[31m$editor_cmd[39;49;00m[33m[1]' could not be found[39;49;00m$
[33m    [39;49;00m[33m"[39;49;00m$
            [34mset[39;49;00m editor [36mfish[39;49;00m$
[36m        [39;49;00m[34mend[39;49;00m$
    [34mend[39;49;00m$
$
    [37m# If no editor is specified, use fish[39;49;00m$
    [34mif[39;49;00m [34mtest[39;49;00m -z [33m"[39;49;00m[31m$editor[39;49;00m[33m"[39;49;00m$
        [34mset[39;49;00m editor [36mfish[39;49;00m$
[36m    [39;49;00m[34mend[39;49;00m$
$
    [34mif[39;49;00m [34mbegin[39;49;00m; [34mset[39;49;00m -q interactive[1]; [34mor[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$editor[39;49;00m[33m"[39;49;00m = [36mfish[39;49;00m; [34mend[39;49;00m$
        [34mset[39;49;00m -l IFS$
        [34mif[39;49;00m [36mfunctions[39;49;00m -q -- [31m$funcname[39;49;00m$
            [37m# Shadow IFS here to avoid array splitting in command substitution[39;49;00m$
            [34mset[39;49;00m init ([36mfunctions[39;49;00m -- [31m$funcname[39;49;00m | [36mfish_indent[39;49;00m --no-indent)$
        [34mend[39;49;00m$
$
        [34mset[39;49;00m -l prompt [33m'printf "%s%s%s> " (set_color green) '[39;49;00m[31m$funcname[39;49;00m[33m' (set_color normal)'[39;49;00m$
        [37m# Unshadow IFS since the fish_title breaks otherwise[39;49;00m$
        [34mset[39;49;00m -e IFS$
        [34mif[39;49;00m [36mread[39;49;00m -p [31m$prompt[39;49;00m -c [33m"[39;49;00m[31m$init[39;49;00m[33m"[39;49;00m -s cmd$
            [37m# Shadow IFS _again_ to avoid array splitting in command substitution[39;49;00m$
            [34mset[39;49;00m -l IFS$
            [36meval[39;49;00m ([34mecho[39;49;00m -n [31m$cmd[39;49;00m | [36mfish_indent[39;49;00m)$
        [34mend[39;49;00m$
        [34mreturn[39;49;00m 0$
    [34mend[39;49;00m$
$
    [34mset[39;49;00m -q TMPDIR; [34mor[39;49;00m [34mset[39;49;00m -l TMPDIR /tmp$
    [34mset[39;49;00m -l tmpname ([36mprintf[39;49;00m [33m"[39;49;00m[31m$TMPDIR[39;49;00m[33m/fish_funced_%d_%d.fish[39;49;00m[33m"[39;49;00m %self ([36mrandom[39;49;00m))$
    [34mwhile[39;49;00m [34mtest[39;49;00m -f [31m$tmpname[39;49;00m$
        [34mset[39;49;00m tmpname ([36mprintf[39;49;00m [33m"[39;49;00m[31m$TMPDIR[39;49;00m[33m/fish_funced_%d_%d.fish[39;49;00m[33m"[39;49;00m %self ([36mrandom[39;49;00m))$
    [34mend[39;49;00m$
$
    [34mif[39;49;00m [36mfunctions[39;49;00m -q -- [31m$funcname[39;49;00m$
        [36mfunctions[39;49;00m -- [31m$funcname[39;49;00m > [31m$tmpname[39;49;00m$
    [34melse[39;49;00m$
        [34mecho[39;49;00m [31m$init[39;49;00m > [31m$tmpname[39;49;00m$
    [34mend[39;49;00m$
    [34mif[39;49;00m [36meval[39;49;00m [31m$editor[39;49;00m [31m$tmpname[39;49;00m$
        . [31m$tmpname[39;49;00m$
    [34mend[39;49;00m$
    [34mset[39;49;00m -l stat [31m$status[39;49;00m$
    rm -f [31m$tmpname[39;49;00m >/dev/null$
    [34mreturn[39;49;00m [31m$stat[39;49;00m$
[34mend[39;49;00m$
$
[37m# -----------------------------------------------------------------------------[39;49;00m$
[37m# Main file for fish command completions. This file contains various[39;49;00m$
[37m# common helper functions for the command completions. All actual[39;49;00m$
[37m# completions are located in the completions subdirectory.[39;49;00m$
[37m## -----------------------------------------------------------------------------[39;49;00m$
$
[37m#[39;49;00m$
[37m# Set default field separators[39;49;00m$
[37m#[39;49;00m$
$
[34mset[39;49;00m -g IFS [33m\n[39;49;00m[33m\ [39;49;00m[33m\t[39;49;00m$
$
[37m#[39;49;00m$
[37m# Set default search paths for completions and shellscript functions[39;49;00m$
[37m# unless they already exist[39;49;00m$
[37m#[39;49;00m$
$
[34mset[39;49;00m -l configdir ~/.config$
$
[34mif[39;49;00m [34mset[39;49;00m -q XDG_CONFIG_HOME$
  [34mset[39;49;00m configdir [31m$XDG_CONFIG_HOME[39;49;00m$
[34mend[39;49;00m$
$
[37m# __fish_datadir, __fish_sysconfdir, __fish_help_dir, __fish_bin_dir[39;49;00m$
[37m# are expected to have been set up by read_init from fish.cpp[39;49;00m$
$
[37m# Set up function and completion paths. Make sure that the fish[39;49;00m$
[37m# default functions/completions are included in the respective path.[39;49;00m$
$
[34mif[39;49;00m [34mnot[39;49;00m [34mset[39;49;00m -q fish_function_path$
  [34mset[39;49;00m fish_function_path [31m$configdir[39;49;00m/fish/functions    [31m$__fish_sysconfdir[39;49;00m/functions    [31m$__fish_datadir[39;49;00m/functions$
[34mend[39;49;00m$
$
[34mif[39;49;00m [34mnot[39;49;00m [36mcontains[39;49;00m [31m$__fish_datadir[39;49;00m/functions [31m$fish_function_path[39;49;00m$
  [34mset[39;49;00m fish_function_path[-1] [31m$__fish_datadir[39;49;00m/functions$
[34mend[39;49;00m$
$
[34mif[39;49;00m [34mnot[39;49;00m [34mset[39;49;00m -q fish_complete_path$
  [34mset[39;49;00m fish_complete_path [31m$configdir[39;49;00m/fish/completions  [31m$__fish_sysconfdir[39;49;00m/completions  [31m$__fish_datadir[39;49;00m/completions$
[34mend[39;49;00m$
$
[34mif[39;49;00m [34mnot[39;49;00m [36mcontains[39;49;00m [31m$__fish_datadir[39;49;00m/completions [31m$fish_complete_path[39;49;00m$
  [34mset[39;49;00m fish_complete_path[-1] [31m$__fish_datadir[39;49;00m/completions$
[34mend[39;49;00m$
$
[37m#[39;49;00m$
[37m# This is a Solaris-specific test to modify the PATH so that[39;49;00m$
[37m# Posix-conformant tools are used by default. It is separate from the[39;49;00m$
[37m# other PATH code because this directory needs to be prepended, not[39;49;00m$
[37m# appended, since it contains POSIX-compliant replacements for various[39;49;00m$
[37m# system utilities.[39;49;00m$
[37m#[39;49;00m$
$
[34mif[39;49;00m [34mtest[39;49;00m -d /usr/xpg4/bin$
  [34mif[39;49;00m [34mnot[39;49;00m [36mcontains[39;49;00m /usr/xpg4/bin [31m$PATH[39;49;00m$
    [34mset[39;49;00m PATH /usr/xpg4/bin [31m$PATH[39;49;00m$
  [34mend[39;49;00m$
[34mend[39;49;00m$
$
[37m#[39;49;00m$
[37m# Add a few common directories to path, if they exists. Note that pure[39;49;00m$
[37m# console programs like makedep sometimes live in /usr/X11R6/bin, so we[39;49;00m$
[37m# want this even for text-only terminals.[39;49;00m$
[37m#[39;49;00m$
$
[34mset[39;49;00m -l path_list /bin /usr/bin /usr/X11R6/bin /usr/local/bin [31m$__fish_bin_dir[39;49;00m$
$
[37m# Root should also have the sbin directories in the path[39;49;00m$
[34mswitch[39;49;00m [31m$USER[39;49;00m$
  [34mcase[39;49;00m root$
  [34mset[39;49;00m path_list [31m$path_list[39;49;00m /sbin /usr/sbin /usr/local/sbin$
[34mend[39;49;00m$
$
[34mfor[39;49;00m i [34min[39;49;00m [31m$path_list[39;49;00m$
  [34mif[39;49;00m [34mnot[39;49;00m [36mcontains[39;49;00m [31m$i[39;49;00m [31m$PATH[39;49;00m$
    [34mif[39;49;00m [34mtest[39;49;00m -d [31m$i[39;49;00m$
      [34mset[39;49;00m PATH [31m$PATH[39;49;00m [31m$i[39;49;00m$
    [34mend[39;49;00m$
  [34mend[39;49;00m$
[34mend[39;49;00m$
$
[37m#[39;49;00m$
[37m# Launch debugger on SIGTRAP[39;49;00m$
[37m#[39;49;00m$
[34mfunction[39;49;00m fish_sigtrap_handler --on-signal TRAP --no-scope-shadowing --description [33m"Signal handler for the TRAP signal. Lanches a debug prompt."[39;49;00m$
  [36mbreakpoint[39;49;00m$
[34mend[39;49;00m$
$
[37m#[39;49;00m$
[37m# Whenever a prompt is displayed, make sure that interactive[39;49;00m$
[37m# mode-specific initializations have been performed.[39;49;00m$
[37m# This handler removes itself after it is first called.[39;49;00m$
[37m#[39;49;00m$
[34mfunction[39;49;00m __fish_on_interactive --on-event [36mfish_prompt[39;49;00m$
[36m  [39;49;00m__fish_config_interactive$
  [36mfunctions[39;49;00m -e __fish_on_interactive$
[34mend[39;49;00m$
