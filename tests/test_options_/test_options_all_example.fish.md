     1^I[37m# -----------------------------------------------------------------------------[39;49;00m$
     2^I[37m# Fishshell Samples[39;49;00m$
     3^I[37m#  |- Theme / bobthefish[39;49;00m$
     4^I[37m#  |- Function / funced[39;49;00m$
     5^I[37m#  |- Configuration / config.fish[39;49;00m$
     6^I[37m# -----------------------------------------------------------------------------[39;49;00m$
     7^I$
     8^I[37m# name: bobthefish[39;49;00m$
     9^I[37m#[39;49;00m$
    10^I[37m# bobthefish is a Powerline-style, Git-aware fish theme optimized for awesome.[39;49;00m$
    11^I[37m#[39;49;00m$
    12^I[37m# You will probably need a Powerline-patched font for this to work:[39;49;00m$
    13^I[37m#[39;49;00m$
    14^I[37m#     https://powerline.readthedocs.org/en/latest/fontpatching.html[39;49;00m$
    15^I[37m#[39;49;00m$
    16^I[37m# I recommend picking one of these:[39;49;00m$
    17^I[37m#[39;49;00m$
    18^I[37m#     https://github.com/Lokaltog/powerline-fonts[39;49;00m$
    19^I[37m#[39;49;00m$
    20^I[37m# You can override some default options in your config.fish:[39;49;00m$
    21^I[37m#[39;49;00m$
    22^I[37m#     set -g theme_display_user yes[39;49;00m$
    23^I[37m#     set -g default_user your_normal_user[39;49;00m$
    24^I$
    25^I[34mset[39;49;00m -g __bobthefish_current_bg NONE$
    26^I$
    27^I[37m# Powerline glyphs[39;49;00m$
    28^I[34mset[39;49;00m __bobthefish_branch_glyph            [33m\u[39;49;00mE0A0$
    29^I[34mset[39;49;00m __bobthefish_ln_glyph                [33m\u[39;49;00mE0A1$
    30^I[34mset[39;49;00m __bobthefish_padlock_glyph           [33m\u[39;49;00mE0A2$
    31^I[34mset[39;49;00m __bobthefish_right_black_arrow_glyph [33m\u[39;49;00mE0B0$
    32^I[34mset[39;49;00m __bobthefish_right_arrow_glyph       [33m\u[39;49;00mE0B1$
    33^I[34mset[39;49;00m __bobthefish_left_black_arrow_glyph  [33m\u[39;49;00mE0B2$
    34^I[34mset[39;49;00m __bobthefish_left_arrow_glyph        [33m\u[39;49;00mE0B3$
    35^I$
    36^I[37m# Additional glyphs[39;49;00m$
    37^I[34mset[39;49;00m __bobthefish_detached_glyph          [33m\u[39;49;00m27A6$
    38^I[34mset[39;49;00m __bobthefish_nonzero_exit_glyph      [33m'! '[39;49;00m$
    39^I[34mset[39;49;00m __bobthefish_superuser_glyph         [33m'$ '[39;49;00m$
    40^I[34mset[39;49;00m __bobthefish_bg_job_glyph            [33m'% '[39;49;00m$
    41^I[34mset[39;49;00m __bobthefish_hg_glyph                [33m\u[39;49;00m263F$
    42^I$
    43^I[37m# Python glyphs[39;49;00m$
    44^I[34mset[39;49;00m __bobthefish_superscript_glyph       [33m\u[39;49;00m00B9 [33m\u[39;49;00m00B2 [33m\u[39;49;00m00B3$
    45^I[34mset[39;49;00m __bobthefish_virtualenv_glyph        [33m\u[39;49;00m25F0$
    46^I[34mset[39;49;00m __bobthefish_pypy_glyph              [33m\u[39;49;00m1D56$
    47^I$
    48^I[37m# Colors[39;49;00m$
    49^I[34mset[39;49;00m __bobthefish_lt_green   addc10$
    50^I[34mset[39;49;00m __bobthefish_med_green  189303$
    51^I[34mset[39;49;00m __bobthefish_dk_green   0c4801$
    52^I$
    53^I[34mset[39;49;00m __bobthefish_lt_red     C99$
    54^I[34mset[39;49;00m __bobthefish_med_red    ce000f$
    55^I[34mset[39;49;00m __bobthefish_dk_red     600$
    56^I$
    57^I[34mset[39;49;00m __bobthefish_slate_blue 255e87$
    58^I$
    59^I[34mset[39;49;00m __bobthefish_lt_orange  f6b117$
    60^I[34mset[39;49;00m __bobthefish_dk_orange  3a2a03$
    61^I$
    62^I[34mset[39;49;00m __bobthefish_dk_grey    333$
    63^I[34mset[39;49;00m __bobthefish_med_grey   999$
    64^I[34mset[39;49;00m __bobthefish_lt_grey    ccc$
    65^I$
    66^I[34mset[39;49;00m __bobthefish_dk_brown   4d2600$
    67^I[34mset[39;49;00m __bobthefish_med_brown  803F00$
    68^I[34mset[39;49;00m __bobthefish_lt_brown   BF5E00$
    69^I$
    70^I[34mset[39;49;00m __bobthefish_dk_blue    1E2933$
    71^I[34mset[39;49;00m __bobthefish_med_blue   275379$
    72^I[34mset[39;49;00m __bobthefish_lt_blue    326D9E$
    73^I$
    74^I[37m# ===========================[39;49;00m$
    75^I[37m# Helper methods[39;49;00m$
    76^I[37m# ===========================[39;49;00m$
    77^I$
    78^I[34mfunction[39;49;00m __bobthefish_in_git -d [33m'Check whether pwd is inside a git repo'[39;49;00m$
    79^I  [36mcommand [39;49;00mwhich git > /dev/null 2>&1; [34mand[39;49;00m [36mcommand [39;49;00mgit rev-parse --is-inside-work-tree >/dev/null 2>&1$
    80^I[34mend[39;49;00m$
    81^I$
    82^I[34mfunction[39;49;00m __bobthefish_in_hg -d [33m'Check whether pwd is inside a hg repo'[39;49;00m$
    83^I  [36mcommand [39;49;00mwhich hg > /dev/null 2>&1; [34mand[39;49;00m [36mcommand [39;49;00mhg stat > /dev/null 2>&1$
    84^I[34mend[39;49;00m$
    85^I$
    86^I[34mfunction[39;49;00m __bobthefish_git_branch -d [33m'Get the current git branch (or commitish)'[39;49;00m$
    87^I  [34mset[39;49;00m -l ref ([36mcommand [39;49;00mgit symbolic-ref HEAD 2> /dev/null)$
    88^I  [34mif[39;49;00m [ [31m$status[39;49;00m -gt [34m0[39;49;00m ]$
    89^I    [34mset[39;49;00m -l branch ([36mcommand [39;49;00mgit show-ref --head -s --abbrev |head -n1 2> /dev/null)$
    90^I    [34mset[39;49;00m ref [33m"[39;49;00m[31m$__bobthefish_detached_glyph[39;49;00m[33m [39;49;00m[31m$branch[39;49;00m[33m"[39;49;00m$
    91^I  [34mend[39;49;00m$
    92^I  [34mecho[39;49;00m [31m$ref[39;49;00m | sed  [33m"[39;49;00m[33ms-refs/heads/-[39;49;00m[31m$__bobthefish_branch_glyph[39;49;00m[33m -[39;49;00m[33m"[39;49;00m$
    93^I[34mend[39;49;00m$
    94^I$
    95^I[34mfunction[39;49;00m __bobthefish_hg_branch -d [33m'Get the current hg branch'[39;49;00m$
    96^I  [34mset[39;49;00m -l branch (hg branch ^/dev/null)$
    97^I  [34mset[39;49;00m -l book [33m" @ "[39;49;00m(hg book | grep [33m\*[39;49;00m | cut -d[33m\ [39;49;00m -f3)$
    98^I  [34mecho[39;49;00m [33m"[39;49;00m[31m$__bobthefish_branch_glyph[39;49;00m[33m [39;49;00m[31m$branch[39;49;00m[31m$book[39;49;00m[33m"[39;49;00m$
    99^I[34mend[39;49;00m$
   100^I$
   101^I[34mfunction[39;49;00m __bobthefish_pretty_parent -d [33m'Print a parent directory, shortened to fit the prompt'[39;49;00m$
   102^I  [34mecho[39;49;00m -n (dirname [31m$argv[39;49;00m[1]) | sed -e [33m's|/private||'[39;49;00m -e [33m"[39;49;00m[33ms|^[39;49;00m[31m$HOME[39;49;00m[33m|~|[39;49;00m[33m"[39;49;00m -e [33m's-/\(\.\{0,1\}[^/]\)\([^/]*\)-/\1-g'[39;49;00m -e [33m's|/$||'[39;49;00m$
   103^I[34mend[39;49;00m$
   104^I$
   105^I[34mfunction[39;49;00m __bobthefish_git_project_dir -d [33m'Print the current git project base directory'[39;49;00m$
   106^I  [36mcommand [39;49;00mgit rev-parse --show-toplevel 2>/dev/null$
   107^I[34mend[39;49;00m$
   108^I$
   109^I[34mfunction[39;49;00m __bobthefish_hg_project_dir -d [33m'Print the current hg project base directory'[39;49;00m$
   110^I  [36mcommand [39;49;00mhg root 2>/dev/null$
   111^I[34mend[39;49;00m$
   112^I$
   113^I[34mfunction[39;49;00m __bobthefish_project_pwd -d [33m'Print the working directory relative to project root'[39;49;00m$
   114^I  [34mecho[39;49;00m [33m"[39;49;00m[31m$PWD[39;49;00m[33m"[39;49;00m | sed -e [33m"[39;49;00m[33ms*[39;49;00m[31m$argv[39;49;00m[33m[1]**g[39;49;00m[33m"[39;49;00m -e [33m's*^/**'[39;49;00m$
   115^I[34mend[39;49;00m$
   116^I$
   117^I$
   118^I[37m# ===========================[39;49;00m$
   119^I[37m# Segment functions[39;49;00m$
   120^I[37m# ===========================[39;49;00m$
   121^I$
   122^I[34mfunction[39;49;00m __bobthefish_start_segment -d [33m'Start a prompt segment'[39;49;00m$
   123^I  [36mset_color[39;49;00m -b [31m$argv[39;49;00m[1]$
   124^I  [36mset_color[39;49;00m [31m$argv[39;49;00m[2]$
   125^I  [34mif[39;49;00m [ [33m"[39;49;00m[31m$__bobthefish_current_bg[39;49;00m[33m"[39;49;00m = [33m'NONE'[39;49;00m ]$
   126^I    [37m# If there's no background, just start one[39;49;00m$
   127^I    [34mecho[39;49;00m -n [33m' '[39;49;00m$
   128^I  [34melse[39;49;00m$
   129^I    [37m# If there's already a background...[39;49;00m$
   130^I    [34mif[39;49;00m [ [33m"[39;49;00m[31m$argv[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m = [33m"[39;49;00m[31m$__bobthefish_current_bg[39;49;00m[33m"[39;49;00m ]$
   131^I      [37m# and it's the same color, draw a separator[39;49;00m$
   132^I      [34mecho[39;49;00m -n [33m"[39;49;00m[31m$__bobthefish_right_arrow_glyph[39;49;00m[33m [39;49;00m[33m"[39;49;00m$
   133^I    [34melse[39;49;00m$
   134^I      [37m# otherwise, draw the end of the previous segment and the start of the next[39;49;00m$
   135^I      [36mset_color[39;49;00m [31m$__bobthefish_current_bg[39;49;00m$
   136^I      [34mecho[39;49;00m -n [33m"[39;49;00m[31m$__bobthefish_right_black_arrow_glyph[39;49;00m[33m [39;49;00m[33m"[39;49;00m$
   137^I      [36mset_color[39;49;00m [31m$argv[39;49;00m[2]$
   138^I    [34mend[39;49;00m$
   139^I  [34mend[39;49;00m$
   140^I  [34mset[39;49;00m __bobthefish_current_bg [31m$argv[39;49;00m[1]$
   141^I[34mend[39;49;00m$
   142^I$
   143^I[34mfunction[39;49;00m __bobthefish_path_segment -d [33m'Display a shortened form of a directory'[39;49;00m$
   144^I  [34mif[39;49;00m [34mtest[39;49;00m -w [33m"[39;49;00m[31m$argv[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m$
   145^I    __bobthefish_start_segment [31m$__bobthefish_dk_grey[39;49;00m [31m$__bobthefish_med_grey[39;49;00m$
   146^I  [34melse[39;49;00m$
   147^I    __bobthefish_start_segment [31m$__bobthefish_dk_red[39;49;00m [31m$__bobthefish_lt_red[39;49;00m$
   148^I  [34mend[39;49;00m$
   149^I$
   150^I  [34mset[39;49;00m -l directory$
   151^I  [34mset[39;49;00m -l parent$
   152^I$
   153^I  [34mswitch[39;49;00m [33m"[39;49;00m[31m$argv[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m$
   154^I    [34mcase[39;49;00m /$
   155^I      [34mset[39;49;00m directory [33m'/'[39;49;00m$
   156^I    [34mcase[39;49;00m [33m"[39;49;00m[31m$HOME[39;49;00m[33m"[39;49;00m$
   157^I      [34mset[39;49;00m directory [33m'~'[39;49;00m$
   158^I    [34mcase[39;49;00m [33m'*'[39;49;00m$
   159^I      [34mset[39;49;00m parent    (__bobthefish_pretty_parent [33m"[39;49;00m[31m$argv[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m)$
   160^I      [34mset[39;49;00m parent    [33m"[39;49;00m[31m$parent[39;49;00m[33m/[39;49;00m[33m"[39;49;00m$
   161^I      [34mset[39;49;00m directory (basename [33m"[39;49;00m[31m$argv[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m)$
   162^I  [34mend[39;49;00m$
   163^I$
   164^I  [34mtest[39;49;00m [33m"[39;49;00m[31m$parent[39;49;00m[33m"[39;49;00m; [34mand[39;49;00m [34mecho[39;49;00m -n -s [33m"[39;49;00m[31m$parent[39;49;00m[33m"[39;49;00m$
   165^I  [36mset_color [39;49;00mfff --bold$
   166^I  [34mecho[39;49;00m -n [33m"[39;49;00m[31m$directory[39;49;00m[33m [39;49;00m[33m"[39;49;00m$
   167^I  [36mset_color [39;49;00mnormal$
   168^I[34mend[39;49;00m$
   169^I$
   170^I[34mfunction[39;49;00m __bobthefish_finish_segments -d [33m'Close open prompt segments'[39;49;00m$
   171^I  [34mif[39;49;00m [ -n [31m$__bobthefish_current_bg[39;49;00m -a [31m$__bobthefish_current_bg[39;49;00m != [33m'NONE'[39;49;00m ]$
   172^I    [36mset_color[39;49;00m -b normal$
   173^I    [36mset_color[39;49;00m [31m$__bobthefish_current_bg[39;49;00m$
   174^I    [34mecho[39;49;00m -n [33m"[39;49;00m[31m$__bobthefish_right_black_arrow_glyph[39;49;00m[33m [39;49;00m[33m"[39;49;00m$
   175^I    [36mset_color [39;49;00mnormal$
   176^I  [34mend[39;49;00m$
   177^I  [34mset[39;49;00m -g __bobthefish_current_bg NONE$
   178^I[34mend[39;49;00m$
   179^I$
   180^I$
   181^I[37m# ===========================[39;49;00m$
   182^I[37m# Theme components[39;49;00m$
   183^I[37m# ===========================[39;49;00m$
   184^I$
   185^I[34mfunction[39;49;00m __bobthefish_prompt_status -d [33m'Display symbols for a non zero exit status, root and background jobs'[39;49;00m$
   186^I  [34mset[39;49;00m -l nonzero$
   187^I  [34mset[39;49;00m -l superuser$
   188^I  [34mset[39;49;00m -l bg_jobs$
   189^I$
   190^I  [37m# Last exit was nonzero[39;49;00m$
   191^I  [34mif[39;49;00m [ [31m$status[39;49;00m -ne [34m0[39;49;00m ]$
   192^I    [34mset[39;49;00m nonzero [31m$__bobthefish_nonzero_exit_glyph[39;49;00m$
   193^I  [34mend[39;49;00m$
   194^I$
   195^I  [37m# if superuser (uid == 0)[39;49;00m$
   196^I  [34mset[39;49;00m -l uid (id -u [31m$USER[39;49;00m)$
   197^I  [34mif[39;49;00m [ [31m$uid[39;49;00m -eq [34m0[39;49;00m ]$
   198^I    [34mset[39;49;00m superuser [31m$__bobthefish_superuser_glyph[39;49;00m$
   199^I  [34mend[39;49;00m$
   200^I$
   201^I  [37m# Jobs display[39;49;00m$
   202^I  [34mif[39;49;00m [ ([36mjobs[39;49;00m -l | wc -l) -gt [34m0[39;49;00m ]$
   203^I    [34mset[39;49;00m bg_jobs [31m$__bobthefish_bg_job_glyph[39;49;00m$
   204^I  [34mend[39;49;00m$
   205^I$
   206^I  [34mset[39;49;00m -l status_flags [33m"[39;49;00m[31m$nonzero[39;49;00m[31m$superuser[39;49;00m[31m$bg_jobs[39;49;00m[33m"[39;49;00m$
   207^I$
   208^I  [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$nonzero[39;49;00m[33m"[39;49;00m -o [33m"[39;49;00m[31m$superuser[39;49;00m[33m"[39;49;00m -o [33m"[39;49;00m[31m$bg_jobs[39;49;00m[33m"[39;49;00m$
   209^I    __bobthefish_start_segment fff 000$
   210^I    [34mif[39;49;00m [ [33m"[39;49;00m[31m$nonzero[39;49;00m[33m"[39;49;00m ]$
   211^I      [36mset_color[39;49;00m [31m$__bobthefish_med_red[39;49;00m --bold$
   212^I      [34mecho[39;49;00m -n [31m$__bobthefish_nonzero_exit_glyph[39;49;00m$
   213^I    [34mend[39;49;00m$
   214^I$
   215^I    [34mif[39;49;00m [ [33m"[39;49;00m[31m$superuser[39;49;00m[33m"[39;49;00m ]$
   216^I      [36mset_color[39;49;00m [31m$__bobthefish_med_green[39;49;00m --bold$
   217^I      [34mecho[39;49;00m -n [31m$__bobthefish_superuser_glyph[39;49;00m$
   218^I    [34mend[39;49;00m$
   219^I$
   220^I    [34mif[39;49;00m [ [33m"[39;49;00m[31m$bg_jobs[39;49;00m[33m"[39;49;00m ]$
   221^I      [36mset_color[39;49;00m [31m$__bobthefish_slate_blue[39;49;00m --bold$
   222^I      [34mecho[39;49;00m -n [31m$__bobthefish_bg_job_glyph[39;49;00m$
   223^I    [34mend[39;49;00m$
   224^I$
   225^I    [36mset_color [39;49;00mnormal$
   226^I  [34mend[39;49;00m$
   227^I[34mend[39;49;00m$
   228^I$
   229^I[34mfunction[39;49;00m __bobthefish_prompt_user -d [33m'Display actual user if different from $default_user'[39;49;00m$
   230^I  [34mif[39;49;00m [ [33m"[39;49;00m[31m$theme_display_user[39;49;00m[33m"[39;49;00m = [33m'yes'[39;49;00m ]$
   231^I    [34mif[39;49;00m [ [33m"[39;49;00m[31m$USER[39;49;00m[33m"[39;49;00m != [33m"[39;49;00m[31m$default_user[39;49;00m[33m"[39;49;00m -o -n [33m"[39;49;00m[31m$SSH_CLIENT[39;49;00m[33m"[39;49;00m ]$
   232^I      __bobthefish_start_segment [31m$__bobthefish_lt_grey[39;49;00m [31m$__bobthefish_slate_blue[39;49;00m$
   233^I      [34mecho[39;49;00m -n -s (whoami) [33m'@'[39;49;00m (hostname | cut -d . -f 1) [33m' '[39;49;00m$
   234^I    [34mend[39;49;00m$
   235^I  [34mend[39;49;00m$
   236^I[34mend[39;49;00m$
   237^I$
   238^I[34mfunction[39;49;00m __bobthefish_prompt_hg -d [33m'Display the actual hg state'[39;49;00m$
   239^I  [34mset[39;49;00m -l dirty   ([36mcommand [39;49;00mhg stat; [34mor[39;49;00m [34mecho[39;49;00m -n [33m'*'[39;49;00m)$
   240^I$
   241^I  [34mset[39;49;00m -l flags [33m"[39;49;00m[31m$dirty[39;49;00m[33m"[39;49;00m$
   242^I  [34mtest[39;49;00m [33m"[39;49;00m[31m$flags[39;49;00m[33m"[39;49;00m; [34mand[39;49;00m [34mset[39;49;00m flags [33m""[39;49;00m$
   243^I$
   244^I  [34mset[39;49;00m -l flag_bg [31m$__bobthefish_lt_green[39;49;00m$
   245^I  [34mset[39;49;00m -l flag_fg [31m$__bobthefish_dk_green[39;49;00m$
   246^I  [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$dirty[39;49;00m[33m"[39;49;00m$
   247^I    [34mset[39;49;00m flag_bg [31m$__bobthefish_med_red[39;49;00m$
   248^I    [34mset[39;49;00m flag_fg fff$
   249^I  [34mend[39;49;00m$
   250^I$
   251^I  __bobthefish_path_segment (__bobthefish_hg_project_dir)$
   252^I$
   253^I  __bobthefish_start_segment [31m$flag_bg[39;49;00m [31m$flag_fg[39;49;00m$
   254^I  [34mecho[39;49;00m -n -s [31m$__bobthefish_hg_glyph[39;49;00m [33m' '[39;49;00m$
   255^I$
   256^I  __bobthefish_start_segment [31m$flag_bg[39;49;00m [31m$flag_fg[39;49;00m$
   257^I  [36mset_color[39;49;00m [31m$flag_fg[39;49;00m --bold$
   258^I  [34mecho[39;49;00m -n -s (__bobthefish_hg_branch) [31m$flags[39;49;00m [33m' '[39;49;00m$
   259^I  [36mset_color [39;49;00mnormal$
   260^I$
   261^I  [34mset[39;49;00m -l project_pwd  (__bobthefish_project_pwd (__bobthefish_hg_project_dir))$
   262^I  [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$project_pwd[39;49;00m[33m"[39;49;00m$
   263^I    [34mif[39;49;00m [34mtest[39;49;00m -w [33m"[39;49;00m[31m$PWD[39;49;00m[33m"[39;49;00m$
   264^I      __bobthefish_start_segment [34m333[39;49;00m 999$
   265^I    [34melse[39;49;00m$
   266^I      __bobthefish_start_segment [31m$__bobthefish_med_red[39;49;00m [31m$__bobthefish_lt_red[39;49;00m$
   267^I    [34mend[39;49;00m$
   268^I$
   269^I    [34mecho[39;49;00m -n -s [31m$project_pwd[39;49;00m [33m' '[39;49;00m$
   270^I  [34mend[39;49;00m$
   271^I[34mend[39;49;00m$
   272^I$
   273^I[37m# TODO: clean up the fugly $ahead business[39;49;00m$
   274^I[34mfunction[39;49;00m __bobthefish_prompt_git -d [33m'Display the actual git state'[39;49;00m$
   275^I  [34mset[39;49;00m -l dirty   ([36mcommand [39;49;00mgit diff --no-ext-diff --quiet --exit-code; [34mor[39;49;00m [34mecho[39;49;00m -n [33m'*'[39;49;00m)$
   276^I  [34mset[39;49;00m -l staged  ([36mcommand [39;49;00mgit diff --cached --no-ext-diff --quiet --exit-code; [34mor[39;49;00m [34mecho[39;49;00m -n [33m'~'[39;49;00m)$
   277^I  [34mset[39;49;00m -l stashed ([36mcommand [39;49;00mgit rev-parse --verify refs/stash > /dev/null 2>&1; [34mand[39;49;00m [34mecho[39;49;00m -n [33m'$'[39;49;00m)$
   278^I  [34mset[39;49;00m -l ahead   ([36mcommand [39;49;00mgit branch -v 2> /dev/null | grep -Eo [33m'^\* [^ ]* *[^ ]* *\[[^]]*\]'[39;49;00m | grep -Eo [33m'\[[^]]*\]$'[39;49;00m | awk [33m'ORS="";/ahead/ {print "+"} /behind/ {print "-"}'[39;49;00m | sed -e [33m's/+-/±/'[39;49;00m)$
   279^I$
   280^I  [34mset[39;49;00m -l new ([36mcommand [39;49;00mgit ls-files --other --exclude-standard);$
   281^I  [34mtest[39;49;00m [33m"[39;49;00m[31m$new[39;49;00m[33m"[39;49;00m; [34mand[39;49;00m [34mset[39;49;00m new [33m'…'[39;49;00m$
   282^I$
   283^I  [34mset[39;49;00m -l flags   [33m"[39;49;00m[31m$dirty[39;49;00m[31m$staged[39;49;00m[31m$stashed[39;49;00m[31m$ahead[39;49;00m[31m$new[39;49;00m[33m"[39;49;00m$
   284^I  [34mtest[39;49;00m [33m"[39;49;00m[31m$flags[39;49;00m[33m"[39;49;00m; [34mand[39;49;00m [34mset[39;49;00m flags [33m"[39;49;00m[33m [39;49;00m[31m$flags[39;49;00m[33m"[39;49;00m$
   285^I$
   286^I  [34mset[39;49;00m -l flag_bg [31m$__bobthefish_lt_green[39;49;00m$
   287^I  [34mset[39;49;00m -l flag_fg [31m$__bobthefish_dk_green[39;49;00m$
   288^I  [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$dirty[39;49;00m[33m"[39;49;00m -o [33m"[39;49;00m[31m$staged[39;49;00m[33m"[39;49;00m$
   289^I    [34mset[39;49;00m flag_bg [31m$__bobthefish_med_red[39;49;00m$
   290^I    [34mset[39;49;00m flag_fg fff$
   291^I  [34melse[39;49;00m$
   292^I    [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$stashed[39;49;00m[33m"[39;49;00m$
   293^I      [34mset[39;49;00m flag_bg [31m$__bobthefish_lt_orange[39;49;00m$
   294^I      [34mset[39;49;00m flag_fg [31m$__bobthefish_dk_orange[39;49;00m$
   295^I    [34mend[39;49;00m$
   296^I  [34mend[39;49;00m$
   297^I$
   298^I  __bobthefish_path_segment (__bobthefish_git_project_dir)$
   299^I$
   300^I  __bobthefish_start_segment [31m$flag_bg[39;49;00m [31m$flag_fg[39;49;00m$
   301^I  [36mset_color[39;49;00m [31m$flag_fg[39;49;00m --bold$
   302^I  [34mecho[39;49;00m -n -s (__bobthefish_git_branch) [31m$flags[39;49;00m [33m' '[39;49;00m$
   303^I  [36mset_color [39;49;00mnormal$
   304^I$
   305^I  [34mset[39;49;00m -l project_pwd  (__bobthefish_project_pwd (__bobthefish_git_project_dir))$
   306^I  [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$project_pwd[39;49;00m[33m"[39;49;00m$
   307^I    [34mif[39;49;00m [34mtest[39;49;00m -w [33m"[39;49;00m[31m$PWD[39;49;00m[33m"[39;49;00m$
   308^I      __bobthefish_start_segment [34m333[39;49;00m 999$
   309^I    [34melse[39;49;00m$
   310^I      __bobthefish_start_segment [31m$__bobthefish_med_red[39;49;00m [31m$__bobthefish_lt_red[39;49;00m$
   311^I    [34mend[39;49;00m$
   312^I$
   313^I    [34mecho[39;49;00m -n -s [31m$project_pwd[39;49;00m [33m' '[39;49;00m$
   314^I  [34mend[39;49;00m$
   315^I[34mend[39;49;00m$
   316^I$
   317^I[34mfunction[39;49;00m __bobthefish_prompt_dir -d [33m'Display a shortened form of the current directory'[39;49;00m$
   318^I  __bobthefish_path_segment [33m"[39;49;00m[31m$PWD[39;49;00m[33m"[39;49;00m$
   319^I[34mend[39;49;00m$
   320^I$
   321^I[34mfunction[39;49;00m __bobthefish_in_virtualfish_virtualenv$
   322^I  [34mset[39;49;00m -q VIRTUAL_ENV$
   323^I[34mend[39;49;00m$
   324^I$
   325^I[34mfunction[39;49;00m __bobthefish_virtualenv_python_version -d [33m'Get current python version'[39;49;00m$
   326^I  [34mswitch[39;49;00m (readlink (which python))$
   327^I    [34mcase[39;49;00m python2$
   328^I      [34mecho[39;49;00m [31m$__bobthefish_superscript_glyph[39;49;00m[2]$
   329^I    [34mcase[39;49;00m python3$
   330^I      [34mecho[39;49;00m [31m$__bobthefish_superscript_glyph[39;49;00m[3]$
   331^I    [34mcase[39;49;00m pypy$
   332^I      [34mecho[39;49;00m [31m$__bobthefish_pypy_glyph[39;49;00m$
   333^I    [34mend[39;49;00m$
   334^I[34mend[39;49;00m$
   335^I$
   336^I[34mfunction[39;49;00m __bobthefish_virtualenv -d [33m'Get the current virtualenv'[39;49;00m$
   337^I  [34mecho[39;49;00m [31m$__bobthefish_virtualenv_glyph[39;49;00m(__bobthefish_virtualenv_python_version) (basename [33m"[39;49;00m[31m$VIRTUAL_ENV[39;49;00m[33m"[39;49;00m)$
   338^I[34mend[39;49;00m$
   339^I$
   340^I[34mfunction[39;49;00m __bobthefish_prompt_virtualfish -d [33m"Display activated virtual environment (only for virtualfish, virtualenv's activate.fish changes prompt by itself)"[39;49;00m$
   341^I  [34mset[39;49;00m flag_bg [31m$__bobthefish_lt_blue[39;49;00m$
   342^I  [34mset[39;49;00m flag_fg [31m$__bobthefish_dk_blue[39;49;00m$
   343^I  __bobthefish_start_segment [31m$flag_bg[39;49;00m [31m$flag_fg[39;49;00m$
   344^I  [36mset_color[39;49;00m [31m$flag_fg[39;49;00m --bold$
   345^I  [34mecho[39;49;00m -n -s (__bobthefish_virtualenv) [31m$flags[39;49;00m [33m' '[39;49;00m$
   346^I  [36mset_color [39;49;00mnormal$
   347^I[34mend[39;49;00m$
   348^I$
   349^I$
   350^I[37m# ===========================[39;49;00m$
   351^I[37m# Apply theme[39;49;00m$
   352^I[37m# ===========================[39;49;00m$
   353^I$
   354^I[34mfunction[39;49;00m [36mfish_prompt[39;49;00m -d [33m'bobthefish, a fish theme optimized for awesome'[39;49;00m$
   355^I  __bobthefish_prompt_status$
   356^I  __bobthefish_prompt_user$
   357^I  [34mif[39;49;00m __bobthefish_in_virtualfish_virtualenv$
   358^I    __bobthefish_prompt_virtualfish$
   359^I  [34mend[39;49;00m$
   360^I  [34mif[39;49;00m __bobthefish_in_git       [37m# TODO: do this right.[39;49;00m$
   361^I    __bobthefish_prompt_git    [37m# if something is in both git and hg, check the length of[39;49;00m$
   362^I  [34melse[39;49;00m [34mif[39;49;00m __bobthefish_in_hg   [37m# __bobthefish_git_project_dir vs __bobthefish_hg_project_dir[39;49;00m$
   363^I    __bobthefish_prompt_hg     [37m# and pick the longer of the two.[39;49;00m$
   364^I  [34melse[39;49;00m$
   365^I    __bobthefish_prompt_dir$
   366^I  [34mend[39;49;00m$
   367^I  __bobthefish_finish_segments$
   368^I[34mend[39;49;00m$
   369^I$
   370^I[37m# -----------------------------------------------------------------------------[39;49;00m$
   371^I[37m# funced - edit a function interactively[39;49;00m$
   372^I[37m#[39;49;00m$
   373^I[37m# Synopsis[39;49;00m$
   374^I[37m#[39;49;00m$
   375^I[37m#   funced [OPTIONS] NAME[39;49;00m$
   376^I[37m#[39;49;00m$
   377^I[37m# Description[39;49;00m$
   378^I[37m#[39;49;00m$
   379^I[37m#   funced provides an interface to edit the definition of the function NAME.[39;49;00m$
   380^I[37m# -----------------------------------------------------------------------------[39;49;00m$
   381^I$
   382^I[34mfunction[39;49;00m [36mfunced[39;49;00m --description [33m'Edit function definition'[39;49;00m$
   383^I    [34mset[39;49;00m -l editor [31m$EDITOR[39;49;00m$
   384^I    [34mset[39;49;00m -l interactive$
   385^I    [34mset[39;49;00m -l funcname$
   386^I    [34mwhile[39;49;00m [34mset[39;49;00m -q argv[1]$
   387^I        [34mswitch[39;49;00m [31m$argv[39;49;00m[1]$
   388^I            [34mcase[39;49;00m -h --help$
   389^I                __fish_print_help [36mfunced[39;49;00m$
   390^I[36m                [39;49;00m[34mreturn[39;49;00m 0$
   391^I$
   392^I            [34mcase[39;49;00m -e --editor$
   393^I                [34mset[39;49;00m editor [31m$argv[39;49;00m[2]$
   394^I                [34mset[39;49;00m -e argv[2]$
   395^I$
   396^I            [34mcase[39;49;00m -i --interactive$
   397^I                [34mset[39;49;00m interactive 1$
   398^I$
   399^I            [34mcase[39;49;00m --$
   400^I                [34mset[39;49;00m funcname [31m$funcname[39;49;00m [31m$argv[39;49;00m[2]$
   401^I                [34mset[39;49;00m -e argv[2]$
   402^I$
   403^I            [34mcase[39;49;00m [33m'-*'[39;49;00m$
   404^I                [36mset_color [39;49;00mred$
   405^I                [36mprintf[39;49;00m (_ [33m"%s: Unknown option %s\n"[39;49;00m) [36mfunced[39;49;00m [31m$argv[39;49;00m[1]$
   406^I                [36mset_color [39;49;00mnormal$
   407^I                [34mreturn[39;49;00m 1$
   408^I$
   409^I            [34mcase[39;49;00m [33m'*'[39;49;00m [33m'.*'[39;49;00m$
   410^I                [34mset[39;49;00m funcname [31m$funcname[39;49;00m [31m$argv[39;49;00m[1]$
   411^I        [34mend[39;49;00m$
   412^I        [34mset[39;49;00m -e argv[1]$
   413^I    [34mend[39;49;00m$
   414^I$
   415^I    [34mif[39;49;00m [34mbegin[39;49;00m; [34mset[39;49;00m -q funcname[2]; [34mor[39;49;00m [34mnot[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$funcname[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m; [34mend[39;49;00m$
   416^I        [36mset_color [39;49;00mred$
   417^I        _ [33m"funced: You must specify one function name[39;49;00m$
   418^I[33m"[39;49;00m$
   419^I        [36mset_color [39;49;00mnormal$
   420^I        [34mreturn[39;49;00m 1$
   421^I    [34mend[39;49;00m$
   422^I$
   423^I    [34mset[39;49;00m -l init$
   424^I    [34mswitch[39;49;00m [31m$funcname[39;49;00m$
   425^I        [34mcase[39;49;00m [33m'-*'[39;49;00m$
   426^I        [34mset[39;49;00m init [34mfunction[39;49;00m -- [31m$funcname[39;49;00m[33m\n[39;49;00m[33m\n[39;49;00mend$
   427^I        [34mcase[39;49;00m [33m'*'[39;49;00m$
   428^I        [34mset[39;49;00m init [34mfunction[39;49;00m [31m$funcname[39;49;00m[33m\n[39;49;00m[33m\n[39;49;00mend$
   429^I    [34mend[39;49;00m$
   430^I$
   431^I    [37m# Break editor up to get its first command (i.e. discard flags)[39;49;00m$
   432^I    [34mif[39;49;00m [34mtest[39;49;00m -n [33m"[39;49;00m[31m$editor[39;49;00m[33m"[39;49;00m$
   433^I        [34mset[39;49;00m -l editor_cmd$
   434^I        [36meval [39;49;00m[34mset[39;49;00m editor_cmd [31m$editor[39;49;00m$
   435^I        [34mif[39;49;00m [34mnot[39;49;00m [36mtype[39;49;00m -f [33m"[39;49;00m[31m$editor_cmd[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m >/dev/null$
   436^I            _ [33m"[39;49;00m[33mfunced: The value for \$EDITOR '[39;49;00m[31m$editor[39;49;00m[33m' could not be used because the command '[39;49;00m[31m$editor_cmd[39;49;00m[33m[1]' could not be found[39;49;00m$
   437^I[33m    [39;49;00m[33m"[39;49;00m$
   438^I            [34mset[39;49;00m editor [36mfish[39;49;00m$
   439^I[36m        [39;49;00m[34mend[39;49;00m$
   440^I    [34mend[39;49;00m$
   441^I$
   442^I    [37m# If no editor is specified, use fish[39;49;00m$
   443^I    [34mif[39;49;00m [34mtest[39;49;00m -z [33m"[39;49;00m[31m$editor[39;49;00m[33m"[39;49;00m$
   444^I        [34mset[39;49;00m editor [36mfish[39;49;00m$
   445^I[36m    [39;49;00m[34mend[39;49;00m$
   446^I$
   447^I    [34mif[39;49;00m [34mbegin[39;49;00m; [34mset[39;49;00m -q interactive[1]; [34mor[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$editor[39;49;00m[33m"[39;49;00m = [36mfish[39;49;00m; [34mend[39;49;00m$
   448^I        [34mset[39;49;00m -l IFS$
   449^I        [34mif[39;49;00m [36mfunctions[39;49;00m -q -- [31m$funcname[39;49;00m$
   450^I            [37m# Shadow IFS here to avoid array splitting in command substitution[39;49;00m$
   451^I            [34mset[39;49;00m init ([36mfunctions[39;49;00m -- [31m$funcname[39;49;00m | [36mfish_indent[39;49;00m --no-indent)$
   452^I        [34mend[39;49;00m$
   453^I$
   454^I        [34mset[39;49;00m -l prompt [33m'printf "%s%s%s> " (set_color green) '[39;49;00m[31m$funcname[39;49;00m[33m' (set_color normal)'[39;49;00m$
   455^I        [37m# Unshadow IFS since the fish_title breaks otherwise[39;49;00m$
   456^I        [34mset[39;49;00m -e IFS$
   457^I        [34mif[39;49;00m [36mread[39;49;00m -p [31m$prompt[39;49;00m -c [33m"[39;49;00m[31m$init[39;49;00m[33m"[39;49;00m -s cmd$
   458^I            [37m# Shadow IFS _again_ to avoid array splitting in command substitution[39;49;00m$
   459^I            [34mset[39;49;00m -l IFS$
   460^I            [36meval[39;49;00m ([34mecho[39;49;00m -n [31m$cmd[39;49;00m | [36mfish_indent[39;49;00m)$
   461^I        [34mend[39;49;00m$
   462^I        [34mreturn[39;49;00m 0$
   463^I    [34mend[39;49;00m$
   464^I$
   465^I    [34mset[39;49;00m -q TMPDIR; [34mor[39;49;00m [34mset[39;49;00m -l TMPDIR /tmp$
   466^I    [34mset[39;49;00m -l tmpname ([36mprintf[39;49;00m [33m"[39;49;00m[31m$TMPDIR[39;49;00m[33m/fish_funced_%d_%d.fish[39;49;00m[33m"[39;49;00m %self ([36mrandom[39;49;00m))$
   467^I    [34mwhile[39;49;00m [34mtest[39;49;00m -f [31m$tmpname[39;49;00m$
   468^I        [34mset[39;49;00m tmpname ([36mprintf[39;49;00m [33m"[39;49;00m[31m$TMPDIR[39;49;00m[33m/fish_funced_%d_%d.fish[39;49;00m[33m"[39;49;00m %self ([36mrandom[39;49;00m))$
   469^I    [34mend[39;49;00m$
   470^I$
   471^I    [34mif[39;49;00m [36mfunctions[39;49;00m -q -- [31m$funcname[39;49;00m$
   472^I        [36mfunctions[39;49;00m -- [31m$funcname[39;49;00m > [31m$tmpname[39;49;00m$
   473^I    [34melse[39;49;00m$
   474^I        [34mecho[39;49;00m [31m$init[39;49;00m > [31m$tmpname[39;49;00m$
   475^I    [34mend[39;49;00m$
   476^I    [34mif[39;49;00m [36meval[39;49;00m [31m$editor[39;49;00m [31m$tmpname[39;49;00m$
   477^I        . [31m$tmpname[39;49;00m$
   478^I    [34mend[39;49;00m$
   479^I    [34mset[39;49;00m -l stat [31m$status[39;49;00m$
   480^I    rm -f [31m$tmpname[39;49;00m >/dev/null$
   481^I    [34mreturn[39;49;00m [31m$stat[39;49;00m$
   482^I[34mend[39;49;00m$
   483^I$
   484^I[37m# -----------------------------------------------------------------------------[39;49;00m$
   485^I[37m# Main file for fish command completions. This file contains various[39;49;00m$
   486^I[37m# common helper functions for the command completions. All actual[39;49;00m$
   487^I[37m# completions are located in the completions subdirectory.[39;49;00m$
   488^I[37m## -----------------------------------------------------------------------------[39;49;00m$
   489^I$
   490^I[37m#[39;49;00m$
   491^I[37m# Set default field separators[39;49;00m$
   492^I[37m#[39;49;00m$
   493^I$
   494^I[34mset[39;49;00m -g IFS [33m\n[39;49;00m[33m\ [39;49;00m[33m\t[39;49;00m$
   495^I$
   496^I[37m#[39;49;00m$
   497^I[37m# Set default search paths for completions and shellscript functions[39;49;00m$
   498^I[37m# unless they already exist[39;49;00m$
   499^I[37m#[39;49;00m$
   500^I$
   501^I[34mset[39;49;00m -l configdir ~/.config$
   502^I$
   503^I[34mif[39;49;00m [34mset[39;49;00m -q XDG_CONFIG_HOME$
   504^I  [34mset[39;49;00m configdir [31m$XDG_CONFIG_HOME[39;49;00m$
   505^I[34mend[39;49;00m$
   506^I$
   507^I[37m# __fish_datadir, __fish_sysconfdir, __fish_help_dir, __fish_bin_dir[39;49;00m$
   508^I[37m# are expected to have been set up by read_init from fish.cpp[39;49;00m$
   509^I$
   510^I[37m# Set up function and completion paths. Make sure that the fish[39;49;00m$
   511^I[37m# default functions/completions are included in the respective path.[39;49;00m$
   512^I$
   513^I[34mif[39;49;00m [34mnot[39;49;00m [34mset[39;49;00m -q fish_function_path$
   514^I  [34mset[39;49;00m fish_function_path [31m$configdir[39;49;00m/fish/functions    [31m$__fish_sysconfdir[39;49;00m/functions    [31m$__fish_datadir[39;49;00m/functions$
   515^I[34mend[39;49;00m$
   516^I$
   517^I[34mif[39;49;00m [34mnot[39;49;00m [36mcontains[39;49;00m [31m$__fish_datadir[39;49;00m/functions [31m$fish_function_path[39;49;00m$
   518^I  [34mset[39;49;00m fish_function_path[-1] [31m$__fish_datadir[39;49;00m/functions$
   519^I[34mend[39;49;00m$
   520^I$
   521^I[34mif[39;49;00m [34mnot[39;49;00m [34mset[39;49;00m -q fish_complete_path$
   522^I  [34mset[39;49;00m fish_complete_path [31m$configdir[39;49;00m/fish/completions  [31m$__fish_sysconfdir[39;49;00m/completions  [31m$__fish_datadir[39;49;00m/completions$
   523^I[34mend[39;49;00m$
   524^I$
   525^I[34mif[39;49;00m [34mnot[39;49;00m [36mcontains[39;49;00m [31m$__fish_datadir[39;49;00m/completions [31m$fish_complete_path[39;49;00m$
   526^I  [34mset[39;49;00m fish_complete_path[-1] [31m$__fish_datadir[39;49;00m/completions$
   527^I[34mend[39;49;00m$
   528^I$
   529^I[37m#[39;49;00m$
   530^I[37m# This is a Solaris-specific test to modify the PATH so that[39;49;00m$
   531^I[37m# Posix-conformant tools are used by default. It is separate from the[39;49;00m$
   532^I[37m# other PATH code because this directory needs to be prepended, not[39;49;00m$
   533^I[37m# appended, since it contains POSIX-compliant replacements for various[39;49;00m$
   534^I[37m# system utilities.[39;49;00m$
   535^I[37m#[39;49;00m$
   536^I$
   537^I[34mif[39;49;00m [34mtest[39;49;00m -d /usr/xpg4/bin$
   538^I  [34mif[39;49;00m [34mnot[39;49;00m [36mcontains[39;49;00m /usr/xpg4/bin [31m$PATH[39;49;00m$
   539^I    [34mset[39;49;00m PATH /usr/xpg4/bin [31m$PATH[39;49;00m$
   540^I  [34mend[39;49;00m$
   541^I[34mend[39;49;00m$
   542^I$
   543^I[37m#[39;49;00m$
   544^I[37m# Add a few common directories to path, if they exists. Note that pure[39;49;00m$
   545^I[37m# console programs like makedep sometimes live in /usr/X11R6/bin, so we[39;49;00m$
   546^I[37m# want this even for text-only terminals.[39;49;00m$
   547^I[37m#[39;49;00m$
   548^I$
   549^I[34mset[39;49;00m -l path_list /bin /usr/bin /usr/X11R6/bin /usr/local/bin [31m$__fish_bin_dir[39;49;00m$
   550^I$
   551^I[37m# Root should also have the sbin directories in the path[39;49;00m$
   552^I[34mswitch[39;49;00m [31m$USER[39;49;00m$
   553^I  [34mcase[39;49;00m root$
   554^I  [34mset[39;49;00m path_list [31m$path_list[39;49;00m /sbin /usr/sbin /usr/local/sbin$
   555^I[34mend[39;49;00m$
   556^I$
   557^I[34mfor[39;49;00m i [34min[39;49;00m [31m$path_list[39;49;00m$
   558^I  [34mif[39;49;00m [34mnot[39;49;00m [36mcontains[39;49;00m [31m$i[39;49;00m [31m$PATH[39;49;00m$
   559^I    [34mif[39;49;00m [34mtest[39;49;00m -d [31m$i[39;49;00m$
   560^I      [34mset[39;49;00m PATH [31m$PATH[39;49;00m [31m$i[39;49;00m$
   561^I    [34mend[39;49;00m$
   562^I  [34mend[39;49;00m$
   563^I[34mend[39;49;00m$
   564^I$
   565^I[37m#[39;49;00m$
   566^I[37m# Launch debugger on SIGTRAP[39;49;00m$
   567^I[37m#[39;49;00m$
   568^I[34mfunction[39;49;00m fish_sigtrap_handler --on-signal TRAP --no-scope-shadowing --description [33m"Signal handler for the TRAP signal. Lanches a debug prompt."[39;49;00m$
   569^I  [36mbreakpoint[39;49;00m$
   570^I[34mend[39;49;00m$
   571^I$
   572^I[37m#[39;49;00m$
   573^I[37m# Whenever a prompt is displayed, make sure that interactive[39;49;00m$
   574^I[37m# mode-specific initializations have been performed.[39;49;00m$
   575^I[37m# This handler removes itself after it is first called.[39;49;00m$
   576^I[37m#[39;49;00m$
   577^I[34mfunction[39;49;00m __fish_on_interactive --on-event [36mfish_prompt[39;49;00m$
   578^I[36m  [39;49;00m__fish_config_interactive$
   579^I  [36mfunctions[39;49;00m -e __fish_on_interactive$
   580^I[34mend[39;49;00m$
