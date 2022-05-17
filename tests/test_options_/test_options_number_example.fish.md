     1	[37m# -----------------------------------------------------------------------------[39;49;00m
     2	[37m# Fishshell Samples[39;49;00m
     3	[37m#  |- Theme / bobthefish[39;49;00m
     4	[37m#  |- Function / funced[39;49;00m
     5	[37m#  |- Configuration / config.fish[39;49;00m
     6	[37m# -----------------------------------------------------------------------------[39;49;00m
     7
     8	[37m# name: bobthefish[39;49;00m
     9	[37m#[39;49;00m
    10	[37m# bobthefish is a Powerline-style, Git-aware fish theme optimized for awesome.[39;49;00m
    11	[37m#[39;49;00m
    12	[37m# You will probably need a Powerline-patched font for this to work:[39;49;00m
    13	[37m#[39;49;00m
    14	[37m#     https://powerline.readthedocs.org/en/latest/fontpatching.html[39;49;00m
    15	[37m#[39;49;00m
    16	[37m# I recommend picking one of these:[39;49;00m
    17	[37m#[39;49;00m
    18	[37m#     https://github.com/Lokaltog/powerline-fonts[39;49;00m
    19	[37m#[39;49;00m
    20	[37m# You can override some default options in your config.fish:[39;49;00m
    21	[37m#[39;49;00m
    22	[37m#     set -g theme_display_user yes[39;49;00m
    23	[37m#     set -g default_user your_normal_user[39;49;00m
    24
    25	[34mset[39;49;00m -g __bobthefish_current_bg NONE
    26
    27	[37m# Powerline glyphs[39;49;00m
    28	[34mset[39;49;00m __bobthefish_branch_glyph            [33m\u[39;49;00mE0A0
    29	[34mset[39;49;00m __bobthefish_ln_glyph                [33m\u[39;49;00mE0A1
    30	[34mset[39;49;00m __bobthefish_padlock_glyph           [33m\u[39;49;00mE0A2
    31	[34mset[39;49;00m __bobthefish_right_black_arrow_glyph [33m\u[39;49;00mE0B0
    32	[34mset[39;49;00m __bobthefish_right_arrow_glyph       [33m\u[39;49;00mE0B1
    33	[34mset[39;49;00m __bobthefish_left_black_arrow_glyph  [33m\u[39;49;00mE0B2
    34	[34mset[39;49;00m __bobthefish_left_arrow_glyph        [33m\u[39;49;00mE0B3
    35
    36	[37m# Additional glyphs[39;49;00m
    37	[34mset[39;49;00m __bobthefish_detached_glyph          [33m\u[39;49;00m27A6
    38	[34mset[39;49;00m __bobthefish_nonzero_exit_glyph      [33m'! '[39;49;00m
    39	[34mset[39;49;00m __bobthefish_superuser_glyph         [33m'$ '[39;49;00m
    40	[34mset[39;49;00m __bobthefish_bg_job_glyph            [33m'% '[39;49;00m
    41	[34mset[39;49;00m __bobthefish_hg_glyph                [33m\u[39;49;00m263F
    42
    43	[37m# Python glyphs[39;49;00m
    44	[34mset[39;49;00m __bobthefish_superscript_glyph       [33m\u[39;49;00m00B9 [33m\u[39;49;00m00B2 [33m\u[39;49;00m00B3
    45	[34mset[39;49;00m __bobthefish_virtualenv_glyph        [33m\u[39;49;00m25F0
    46	[34mset[39;49;00m __bobthefish_pypy_glyph              [33m\u[39;49;00m1D56
    47
    48	[37m# Colors[39;49;00m
    49	[34mset[39;49;00m __bobthefish_lt_green   addc10
    50	[34mset[39;49;00m __bobthefish_med_green  189303
    51	[34mset[39;49;00m __bobthefish_dk_green   0c4801
    52
    53	[34mset[39;49;00m __bobthefish_lt_red     C99
    54	[34mset[39;49;00m __bobthefish_med_red    ce000f
    55	[34mset[39;49;00m __bobthefish_dk_red     600
    56
    57	[34mset[39;49;00m __bobthefish_slate_blue 255e87
    58
    59	[34mset[39;49;00m __bobthefish_lt_orange  f6b117
    60	[34mset[39;49;00m __bobthefish_dk_orange  3a2a03
    61
    62	[34mset[39;49;00m __bobthefish_dk_grey    333
    63	[34mset[39;49;00m __bobthefish_med_grey   999
    64	[34mset[39;49;00m __bobthefish_lt_grey    ccc
    65
    66	[34mset[39;49;00m __bobthefish_dk_brown   4d2600
    67	[34mset[39;49;00m __bobthefish_med_brown  803F00
    68	[34mset[39;49;00m __bobthefish_lt_brown   BF5E00
    69
    70	[34mset[39;49;00m __bobthefish_dk_blue    1E2933
    71	[34mset[39;49;00m __bobthefish_med_blue   275379
    72	[34mset[39;49;00m __bobthefish_lt_blue    326D9E
    73
    74	[37m# ===========================[39;49;00m
    75	[37m# Helper methods[39;49;00m
    76	[37m# ===========================[39;49;00m
    77
    78	[34mfunction[39;49;00m __bobthefish_in_git -d [33m'Check whether pwd is inside a git repo'[39;49;00m
    79	  [36mcommand [39;49;00mwhich git > /dev/null 2>&1; [34mand[39;49;00m [36mcommand [39;49;00mgit rev-parse --is-inside-work-tree >/dev/null 2>&1
    80	[34mend[39;49;00m
    81
    82	[34mfunction[39;49;00m __bobthefish_in_hg -d [33m'Check whether pwd is inside a hg repo'[39;49;00m
    83	  [36mcommand [39;49;00mwhich hg > /dev/null 2>&1; [34mand[39;49;00m [36mcommand [39;49;00mhg stat > /dev/null 2>&1
    84	[34mend[39;49;00m
    85
    86	[34mfunction[39;49;00m __bobthefish_git_branch -d [33m'Get the current git branch (or commitish)'[39;49;00m
    87	  [34mset[39;49;00m -l ref ([36mcommand [39;49;00mgit symbolic-ref HEAD 2> /dev/null)
    88	  [34mif[39;49;00m [ [31m$status[39;49;00m -gt [34m0[39;49;00m ]
    89	    [34mset[39;49;00m -l branch ([36mcommand [39;49;00mgit show-ref --head -s --abbrev |head -n1 2> /dev/null)
    90	    [34mset[39;49;00m ref [33m"[39;49;00m[31m$__bobthefish_detached_glyph[39;49;00m[33m [39;49;00m[31m$branch[39;49;00m[33m"[39;49;00m
    91	  [34mend[39;49;00m
    92	  [34mecho[39;49;00m [31m$ref[39;49;00m | sed  [33m"[39;49;00m[33ms-refs/heads/-[39;49;00m[31m$__bobthefish_branch_glyph[39;49;00m[33m -[39;49;00m[33m"[39;49;00m
    93	[34mend[39;49;00m
    94
    95	[34mfunction[39;49;00m __bobthefish_hg_branch -d [33m'Get the current hg branch'[39;49;00m
    96	  [34mset[39;49;00m -l branch (hg branch ^/dev/null)
    97	  [34mset[39;49;00m -l book [33m" @ "[39;49;00m(hg book | grep [33m\*[39;49;00m | cut -d[33m\ [39;49;00m -f3)
    98	  [34mecho[39;49;00m [33m"[39;49;00m[31m$__bobthefish_branch_glyph[39;49;00m[33m [39;49;00m[31m$branch[39;49;00m[31m$book[39;49;00m[33m"[39;49;00m
    99	[34mend[39;49;00m
   100
   101	[34mfunction[39;49;00m __bobthefish_pretty_parent -d [33m'Print a parent directory, shortened to fit the prompt'[39;49;00m
   102	  [34mecho[39;49;00m -n (dirname [31m$argv[39;49;00m[1]) | sed -e [33m's|/private||'[39;49;00m -e [33m"[39;49;00m[33ms|^[39;49;00m[31m$HOME[39;49;00m[33m|~|[39;49;00m[33m"[39;49;00m -e [33m's-/\(\.\{0,1\}[^/]\)\([^/]*\)-/\1-g'[39;49;00m -e [33m's|/$||'[39;49;00m
   103	[34mend[39;49;00m
   104
   105	[34mfunction[39;49;00m __bobthefish_git_project_dir -d [33m'Print the current git project base directory'[39;49;00m
   106	  [36mcommand [39;49;00mgit rev-parse --show-toplevel 2>/dev/null
   107	[34mend[39;49;00m
   108
   109	[34mfunction[39;49;00m __bobthefish_hg_project_dir -d [33m'Print the current hg project base directory'[39;49;00m
   110	  [36mcommand [39;49;00mhg root 2>/dev/null
   111	[34mend[39;49;00m
   112
   113	[34mfunction[39;49;00m __bobthefish_project_pwd -d [33m'Print the working directory relative to project root'[39;49;00m
   114	  [34mecho[39;49;00m [33m"[39;49;00m[31m$PWD[39;49;00m[33m"[39;49;00m | sed -e [33m"[39;49;00m[33ms*[39;49;00m[31m$argv[39;49;00m[33m[1]**g[39;49;00m[33m"[39;49;00m -e [33m's*^/**'[39;49;00m
   115	[34mend[39;49;00m
   116
   117
   118	[37m# ===========================[39;49;00m
   119	[37m# Segment functions[39;49;00m
   120	[37m# ===========================[39;49;00m
   121
   122	[34mfunction[39;49;00m __bobthefish_start_segment -d [33m'Start a prompt segment'[39;49;00m
   123	  [36mset_color[39;49;00m -b [31m$argv[39;49;00m[1]
   124	  [36mset_color[39;49;00m [31m$argv[39;49;00m[2]
   125	  [34mif[39;49;00m [ [33m"[39;49;00m[31m$__bobthefish_current_bg[39;49;00m[33m"[39;49;00m = [33m'NONE'[39;49;00m ]
   126	    [37m# If there's no background, just start one[39;49;00m
   127	    [34mecho[39;49;00m -n [33m' '[39;49;00m
   128	  [34melse[39;49;00m
   129	    [37m# If there's already a background...[39;49;00m
   130	    [34mif[39;49;00m [ [33m"[39;49;00m[31m$argv[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m = [33m"[39;49;00m[31m$__bobthefish_current_bg[39;49;00m[33m"[39;49;00m ]
   131	      [37m# and it's the same color, draw a separator[39;49;00m
   132	      [34mecho[39;49;00m -n [33m"[39;49;00m[31m$__bobthefish_right_arrow_glyph[39;49;00m[33m [39;49;00m[33m"[39;49;00m
   133	    [34melse[39;49;00m
   134	      [37m# otherwise, draw the end of the previous segment and the start of the next[39;49;00m
   135	      [36mset_color[39;49;00m [31m$__bobthefish_current_bg[39;49;00m
   136	      [34mecho[39;49;00m -n [33m"[39;49;00m[31m$__bobthefish_right_black_arrow_glyph[39;49;00m[33m [39;49;00m[33m"[39;49;00m
   137	      [36mset_color[39;49;00m [31m$argv[39;49;00m[2]
   138	    [34mend[39;49;00m
   139	  [34mend[39;49;00m
   140	  [34mset[39;49;00m __bobthefish_current_bg [31m$argv[39;49;00m[1]
   141	[34mend[39;49;00m
   142
   143	[34mfunction[39;49;00m __bobthefish_path_segment -d [33m'Display a shortened form of a directory'[39;49;00m
   144	  [34mif[39;49;00m [34mtest[39;49;00m -w [33m"[39;49;00m[31m$argv[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m
   145	    __bobthefish_start_segment [31m$__bobthefish_dk_grey[39;49;00m [31m$__bobthefish_med_grey[39;49;00m
   146	  [34melse[39;49;00m
   147	    __bobthefish_start_segment [31m$__bobthefish_dk_red[39;49;00m [31m$__bobthefish_lt_red[39;49;00m
   148	  [34mend[39;49;00m
   149
   150	  [34mset[39;49;00m -l directory
   151	  [34mset[39;49;00m -l parent
   152
   153	  [34mswitch[39;49;00m [33m"[39;49;00m[31m$argv[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m
   154	    [34mcase[39;49;00m /
   155	      [34mset[39;49;00m directory [33m'/'[39;49;00m
   156	    [34mcase[39;49;00m [33m"[39;49;00m[31m$HOME[39;49;00m[33m"[39;49;00m
   157	      [34mset[39;49;00m directory [33m'~'[39;49;00m
   158	    [34mcase[39;49;00m [33m'*'[39;49;00m
   159	      [34mset[39;49;00m parent    (__bobthefish_pretty_parent [33m"[39;49;00m[31m$argv[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m)
   160	      [34mset[39;49;00m parent    [33m"[39;49;00m[31m$parent[39;49;00m[33m/[39;49;00m[33m"[39;49;00m
   161	      [34mset[39;49;00m directory (basename [33m"[39;49;00m[31m$argv[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m)
   162	  [34mend[39;49;00m
   163
   164	  [34mtest[39;49;00m [33m"[39;49;00m[31m$parent[39;49;00m[33m"[39;49;00m; [34mand[39;49;00m [34mecho[39;49;00m -n -s [33m"[39;49;00m[31m$parent[39;49;00m[33m"[39;49;00m
   165	  [36mset_color [39;49;00mfff --bold
   166	  [34mecho[39;49;00m -n [33m"[39;49;00m[31m$directory[39;49;00m[33m [39;49;00m[33m"[39;49;00m
   167	  [36mset_color [39;49;00mnormal
   168	[34mend[39;49;00m
   169
   170	[34mfunction[39;49;00m __bobthefish_finish_segments -d [33m'Close open prompt segments'[39;49;00m
   171	  [34mif[39;49;00m [ -n [31m$__bobthefish_current_bg[39;49;00m -a [31m$__bobthefish_current_bg[39;49;00m != [33m'NONE'[39;49;00m ]
   172	    [36mset_color[39;49;00m -b normal
   173	    [36mset_color[39;49;00m [31m$__bobthefish_current_bg[39;49;00m
   174	    [34mecho[39;49;00m -n [33m"[39;49;00m[31m$__bobthefish_right_black_arrow_glyph[39;49;00m[33m [39;49;00m[33m"[39;49;00m
   175	    [36mset_color [39;49;00mnormal
   176	  [34mend[39;49;00m
   177	  [34mset[39;49;00m -g __bobthefish_current_bg NONE
   178	[34mend[39;49;00m
   179
   180
   181	[37m# ===========================[39;49;00m
   182	[37m# Theme components[39;49;00m
   183	[37m# ===========================[39;49;00m
   184
   185	[34mfunction[39;49;00m __bobthefish_prompt_status -d [33m'Display symbols for a non zero exit status, root and background jobs'[39;49;00m
   186	  [34mset[39;49;00m -l nonzero
   187	  [34mset[39;49;00m -l superuser
   188	  [34mset[39;49;00m -l bg_jobs
   189
   190	  [37m# Last exit was nonzero[39;49;00m
   191	  [34mif[39;49;00m [ [31m$status[39;49;00m -ne [34m0[39;49;00m ]
   192	    [34mset[39;49;00m nonzero [31m$__bobthefish_nonzero_exit_glyph[39;49;00m
   193	  [34mend[39;49;00m
   194
   195	  [37m# if superuser (uid == 0)[39;49;00m
   196	  [34mset[39;49;00m -l uid (id -u [31m$USER[39;49;00m)
   197	  [34mif[39;49;00m [ [31m$uid[39;49;00m -eq [34m0[39;49;00m ]
   198	    [34mset[39;49;00m superuser [31m$__bobthefish_superuser_glyph[39;49;00m
   199	  [34mend[39;49;00m
   200
   201	  [37m# Jobs display[39;49;00m
   202	  [34mif[39;49;00m [ ([36mjobs[39;49;00m -l | wc -l) -gt [34m0[39;49;00m ]
   203	    [34mset[39;49;00m bg_jobs [31m$__bobthefish_bg_job_glyph[39;49;00m
   204	  [34mend[39;49;00m
   205
   206	  [34mset[39;49;00m -l status_flags [33m"[39;49;00m[31m$nonzero[39;49;00m[31m$superuser[39;49;00m[31m$bg_jobs[39;49;00m[33m"[39;49;00m
   207
   208	  [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$nonzero[39;49;00m[33m"[39;49;00m -o [33m"[39;49;00m[31m$superuser[39;49;00m[33m"[39;49;00m -o [33m"[39;49;00m[31m$bg_jobs[39;49;00m[33m"[39;49;00m
   209	    __bobthefish_start_segment fff 000
   210	    [34mif[39;49;00m [ [33m"[39;49;00m[31m$nonzero[39;49;00m[33m"[39;49;00m ]
   211	      [36mset_color[39;49;00m [31m$__bobthefish_med_red[39;49;00m --bold
   212	      [34mecho[39;49;00m -n [31m$__bobthefish_nonzero_exit_glyph[39;49;00m
   213	    [34mend[39;49;00m
   214
   215	    [34mif[39;49;00m [ [33m"[39;49;00m[31m$superuser[39;49;00m[33m"[39;49;00m ]
   216	      [36mset_color[39;49;00m [31m$__bobthefish_med_green[39;49;00m --bold
   217	      [34mecho[39;49;00m -n [31m$__bobthefish_superuser_glyph[39;49;00m
   218	    [34mend[39;49;00m
   219
   220	    [34mif[39;49;00m [ [33m"[39;49;00m[31m$bg_jobs[39;49;00m[33m"[39;49;00m ]
   221	      [36mset_color[39;49;00m [31m$__bobthefish_slate_blue[39;49;00m --bold
   222	      [34mecho[39;49;00m -n [31m$__bobthefish_bg_job_glyph[39;49;00m
   223	    [34mend[39;49;00m
   224
   225	    [36mset_color [39;49;00mnormal
   226	  [34mend[39;49;00m
   227	[34mend[39;49;00m
   228
   229	[34mfunction[39;49;00m __bobthefish_prompt_user -d [33m'Display actual user if different from $default_user'[39;49;00m
   230	  [34mif[39;49;00m [ [33m"[39;49;00m[31m$theme_display_user[39;49;00m[33m"[39;49;00m = [33m'yes'[39;49;00m ]
   231	    [34mif[39;49;00m [ [33m"[39;49;00m[31m$USER[39;49;00m[33m"[39;49;00m != [33m"[39;49;00m[31m$default_user[39;49;00m[33m"[39;49;00m -o -n [33m"[39;49;00m[31m$SSH_CLIENT[39;49;00m[33m"[39;49;00m ]
   232	      __bobthefish_start_segment [31m$__bobthefish_lt_grey[39;49;00m [31m$__bobthefish_slate_blue[39;49;00m
   233	      [34mecho[39;49;00m -n -s (whoami) [33m'@'[39;49;00m (hostname | cut -d . -f 1) [33m' '[39;49;00m
   234	    [34mend[39;49;00m
   235	  [34mend[39;49;00m
   236	[34mend[39;49;00m
   237
   238	[34mfunction[39;49;00m __bobthefish_prompt_hg -d [33m'Display the actual hg state'[39;49;00m
   239	  [34mset[39;49;00m -l dirty   ([36mcommand [39;49;00mhg stat; [34mor[39;49;00m [34mecho[39;49;00m -n [33m'*'[39;49;00m)
   240
   241	  [34mset[39;49;00m -l flags [33m"[39;49;00m[31m$dirty[39;49;00m[33m"[39;49;00m
   242	  [34mtest[39;49;00m [33m"[39;49;00m[31m$flags[39;49;00m[33m"[39;49;00m; [34mand[39;49;00m [34mset[39;49;00m flags [33m""[39;49;00m
   243
   244	  [34mset[39;49;00m -l flag_bg [31m$__bobthefish_lt_green[39;49;00m
   245	  [34mset[39;49;00m -l flag_fg [31m$__bobthefish_dk_green[39;49;00m
   246	  [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$dirty[39;49;00m[33m"[39;49;00m
   247	    [34mset[39;49;00m flag_bg [31m$__bobthefish_med_red[39;49;00m
   248	    [34mset[39;49;00m flag_fg fff
   249	  [34mend[39;49;00m
   250
   251	  __bobthefish_path_segment (__bobthefish_hg_project_dir)
   252
   253	  __bobthefish_start_segment [31m$flag_bg[39;49;00m [31m$flag_fg[39;49;00m
   254	  [34mecho[39;49;00m -n -s [31m$__bobthefish_hg_glyph[39;49;00m [33m' '[39;49;00m
   255
   256	  __bobthefish_start_segment [31m$flag_bg[39;49;00m [31m$flag_fg[39;49;00m
   257	  [36mset_color[39;49;00m [31m$flag_fg[39;49;00m --bold
   258	  [34mecho[39;49;00m -n -s (__bobthefish_hg_branch) [31m$flags[39;49;00m [33m' '[39;49;00m
   259	  [36mset_color [39;49;00mnormal
   260
   261	  [34mset[39;49;00m -l project_pwd  (__bobthefish_project_pwd (__bobthefish_hg_project_dir))
   262	  [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$project_pwd[39;49;00m[33m"[39;49;00m
   263	    [34mif[39;49;00m [34mtest[39;49;00m -w [33m"[39;49;00m[31m$PWD[39;49;00m[33m"[39;49;00m
   264	      __bobthefish_start_segment [34m333[39;49;00m 999
   265	    [34melse[39;49;00m
   266	      __bobthefish_start_segment [31m$__bobthefish_med_red[39;49;00m [31m$__bobthefish_lt_red[39;49;00m
   267	    [34mend[39;49;00m
   268
   269	    [34mecho[39;49;00m -n -s [31m$project_pwd[39;49;00m [33m' '[39;49;00m
   270	  [34mend[39;49;00m
   271	[34mend[39;49;00m
   272
   273	[37m# TODO: clean up the fugly $ahead business[39;49;00m
   274	[34mfunction[39;49;00m __bobthefish_prompt_git -d [33m'Display the actual git state'[39;49;00m
   275	  [34mset[39;49;00m -l dirty   ([36mcommand [39;49;00mgit diff --no-ext-diff --quiet --exit-code; [34mor[39;49;00m [34mecho[39;49;00m -n [33m'*'[39;49;00m)
   276	  [34mset[39;49;00m -l staged  ([36mcommand [39;49;00mgit diff --cached --no-ext-diff --quiet --exit-code; [34mor[39;49;00m [34mecho[39;49;00m -n [33m'~'[39;49;00m)
   277	  [34mset[39;49;00m -l stashed ([36mcommand [39;49;00mgit rev-parse --verify refs/stash > /dev/null 2>&1; [34mand[39;49;00m [34mecho[39;49;00m -n [33m'$'[39;49;00m)
   278	  [34mset[39;49;00m -l ahead   ([36mcommand [39;49;00mgit branch -v 2> /dev/null | grep -Eo [33m'^\* [^ ]* *[^ ]* *\[[^]]*\]'[39;49;00m | grep -Eo [33m'\[[^]]*\]$'[39;49;00m | awk [33m'ORS="";/ahead/ {print "+"} /behind/ {print "-"}'[39;49;00m | sed -e [33m's/+-/±/'[39;49;00m)
   279
   280	  [34mset[39;49;00m -l new ([36mcommand [39;49;00mgit ls-files --other --exclude-standard);
   281	  [34mtest[39;49;00m [33m"[39;49;00m[31m$new[39;49;00m[33m"[39;49;00m; [34mand[39;49;00m [34mset[39;49;00m new [33m'…'[39;49;00m
   282
   283	  [34mset[39;49;00m -l flags   [33m"[39;49;00m[31m$dirty[39;49;00m[31m$staged[39;49;00m[31m$stashed[39;49;00m[31m$ahead[39;49;00m[31m$new[39;49;00m[33m"[39;49;00m
   284	  [34mtest[39;49;00m [33m"[39;49;00m[31m$flags[39;49;00m[33m"[39;49;00m; [34mand[39;49;00m [34mset[39;49;00m flags [33m"[39;49;00m[33m [39;49;00m[31m$flags[39;49;00m[33m"[39;49;00m
   285
   286	  [34mset[39;49;00m -l flag_bg [31m$__bobthefish_lt_green[39;49;00m
   287	  [34mset[39;49;00m -l flag_fg [31m$__bobthefish_dk_green[39;49;00m
   288	  [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$dirty[39;49;00m[33m"[39;49;00m -o [33m"[39;49;00m[31m$staged[39;49;00m[33m"[39;49;00m
   289	    [34mset[39;49;00m flag_bg [31m$__bobthefish_med_red[39;49;00m
   290	    [34mset[39;49;00m flag_fg fff
   291	  [34melse[39;49;00m
   292	    [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$stashed[39;49;00m[33m"[39;49;00m
   293	      [34mset[39;49;00m flag_bg [31m$__bobthefish_lt_orange[39;49;00m
   294	      [34mset[39;49;00m flag_fg [31m$__bobthefish_dk_orange[39;49;00m
   295	    [34mend[39;49;00m
   296	  [34mend[39;49;00m
   297
   298	  __bobthefish_path_segment (__bobthefish_git_project_dir)
   299
   300	  __bobthefish_start_segment [31m$flag_bg[39;49;00m [31m$flag_fg[39;49;00m
   301	  [36mset_color[39;49;00m [31m$flag_fg[39;49;00m --bold
   302	  [34mecho[39;49;00m -n -s (__bobthefish_git_branch) [31m$flags[39;49;00m [33m' '[39;49;00m
   303	  [36mset_color [39;49;00mnormal
   304
   305	  [34mset[39;49;00m -l project_pwd  (__bobthefish_project_pwd (__bobthefish_git_project_dir))
   306	  [34mif[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$project_pwd[39;49;00m[33m"[39;49;00m
   307	    [34mif[39;49;00m [34mtest[39;49;00m -w [33m"[39;49;00m[31m$PWD[39;49;00m[33m"[39;49;00m
   308	      __bobthefish_start_segment [34m333[39;49;00m 999
   309	    [34melse[39;49;00m
   310	      __bobthefish_start_segment [31m$__bobthefish_med_red[39;49;00m [31m$__bobthefish_lt_red[39;49;00m
   311	    [34mend[39;49;00m
   312
   313	    [34mecho[39;49;00m -n -s [31m$project_pwd[39;49;00m [33m' '[39;49;00m
   314	  [34mend[39;49;00m
   315	[34mend[39;49;00m
   316
   317	[34mfunction[39;49;00m __bobthefish_prompt_dir -d [33m'Display a shortened form of the current directory'[39;49;00m
   318	  __bobthefish_path_segment [33m"[39;49;00m[31m$PWD[39;49;00m[33m"[39;49;00m
   319	[34mend[39;49;00m
   320
   321	[34mfunction[39;49;00m __bobthefish_in_virtualfish_virtualenv
   322	  [34mset[39;49;00m -q VIRTUAL_ENV
   323	[34mend[39;49;00m
   324
   325	[34mfunction[39;49;00m __bobthefish_virtualenv_python_version -d [33m'Get current python version'[39;49;00m
   326	  [34mswitch[39;49;00m (readlink (which python))
   327	    [34mcase[39;49;00m python2
   328	      [34mecho[39;49;00m [31m$__bobthefish_superscript_glyph[39;49;00m[2]
   329	    [34mcase[39;49;00m python3
   330	      [34mecho[39;49;00m [31m$__bobthefish_superscript_glyph[39;49;00m[3]
   331	    [34mcase[39;49;00m pypy
   332	      [34mecho[39;49;00m [31m$__bobthefish_pypy_glyph[39;49;00m
   333	    [34mend[39;49;00m
   334	[34mend[39;49;00m
   335
   336	[34mfunction[39;49;00m __bobthefish_virtualenv -d [33m'Get the current virtualenv'[39;49;00m
   337	  [34mecho[39;49;00m [31m$__bobthefish_virtualenv_glyph[39;49;00m(__bobthefish_virtualenv_python_version) (basename [33m"[39;49;00m[31m$VIRTUAL_ENV[39;49;00m[33m"[39;49;00m)
   338	[34mend[39;49;00m
   339
   340	[34mfunction[39;49;00m __bobthefish_prompt_virtualfish -d [33m"Display activated virtual environment (only for virtualfish, virtualenv's activate.fish changes prompt by itself)"[39;49;00m
   341	  [34mset[39;49;00m flag_bg [31m$__bobthefish_lt_blue[39;49;00m
   342	  [34mset[39;49;00m flag_fg [31m$__bobthefish_dk_blue[39;49;00m
   343	  __bobthefish_start_segment [31m$flag_bg[39;49;00m [31m$flag_fg[39;49;00m
   344	  [36mset_color[39;49;00m [31m$flag_fg[39;49;00m --bold
   345	  [34mecho[39;49;00m -n -s (__bobthefish_virtualenv) [31m$flags[39;49;00m [33m' '[39;49;00m
   346	  [36mset_color [39;49;00mnormal
   347	[34mend[39;49;00m
   348
   349
   350	[37m# ===========================[39;49;00m
   351	[37m# Apply theme[39;49;00m
   352	[37m# ===========================[39;49;00m
   353
   354	[34mfunction[39;49;00m [36mfish_prompt[39;49;00m -d [33m'bobthefish, a fish theme optimized for awesome'[39;49;00m
   355	  __bobthefish_prompt_status
   356	  __bobthefish_prompt_user
   357	  [34mif[39;49;00m __bobthefish_in_virtualfish_virtualenv
   358	    __bobthefish_prompt_virtualfish
   359	  [34mend[39;49;00m
   360	  [34mif[39;49;00m __bobthefish_in_git       [37m# TODO: do this right.[39;49;00m
   361	    __bobthefish_prompt_git    [37m# if something is in both git and hg, check the length of[39;49;00m
   362	  [34melse[39;49;00m [34mif[39;49;00m __bobthefish_in_hg   [37m# __bobthefish_git_project_dir vs __bobthefish_hg_project_dir[39;49;00m
   363	    __bobthefish_prompt_hg     [37m# and pick the longer of the two.[39;49;00m
   364	  [34melse[39;49;00m
   365	    __bobthefish_prompt_dir
   366	  [34mend[39;49;00m
   367	  __bobthefish_finish_segments
   368	[34mend[39;49;00m
   369
   370	[37m# -----------------------------------------------------------------------------[39;49;00m
   371	[37m# funced - edit a function interactively[39;49;00m
   372	[37m#[39;49;00m
   373	[37m# Synopsis[39;49;00m
   374	[37m#[39;49;00m
   375	[37m#   funced [OPTIONS] NAME[39;49;00m
   376	[37m#[39;49;00m
   377	[37m# Description[39;49;00m
   378	[37m#[39;49;00m
   379	[37m#   funced provides an interface to edit the definition of the function NAME.[39;49;00m
   380	[37m# -----------------------------------------------------------------------------[39;49;00m
   381
   382	[34mfunction[39;49;00m [36mfunced[39;49;00m --description [33m'Edit function definition'[39;49;00m
   383	    [34mset[39;49;00m -l editor [31m$EDITOR[39;49;00m
   384	    [34mset[39;49;00m -l interactive
   385	    [34mset[39;49;00m -l funcname
   386	    [34mwhile[39;49;00m [34mset[39;49;00m -q argv[1]
   387	        [34mswitch[39;49;00m [31m$argv[39;49;00m[1]
   388	            [34mcase[39;49;00m -h --help
   389	                __fish_print_help [36mfunced[39;49;00m
   390	[36m                [39;49;00m[34mreturn[39;49;00m 0
   391
   392	            [34mcase[39;49;00m -e --editor
   393	                [34mset[39;49;00m editor [31m$argv[39;49;00m[2]
   394	                [34mset[39;49;00m -e argv[2]
   395
   396	            [34mcase[39;49;00m -i --interactive
   397	                [34mset[39;49;00m interactive 1
   398
   399	            [34mcase[39;49;00m --
   400	                [34mset[39;49;00m funcname [31m$funcname[39;49;00m [31m$argv[39;49;00m[2]
   401	                [34mset[39;49;00m -e argv[2]
   402
   403	            [34mcase[39;49;00m [33m'-*'[39;49;00m
   404	                [36mset_color [39;49;00mred
   405	                [36mprintf[39;49;00m (_ [33m"%s: Unknown option %s\n"[39;49;00m) [36mfunced[39;49;00m [31m$argv[39;49;00m[1]
   406	                [36mset_color [39;49;00mnormal
   407	                [34mreturn[39;49;00m 1
   408
   409	            [34mcase[39;49;00m [33m'*'[39;49;00m [33m'.*'[39;49;00m
   410	                [34mset[39;49;00m funcname [31m$funcname[39;49;00m [31m$argv[39;49;00m[1]
   411	        [34mend[39;49;00m
   412	        [34mset[39;49;00m -e argv[1]
   413	    [34mend[39;49;00m
   414
   415	    [34mif[39;49;00m [34mbegin[39;49;00m; [34mset[39;49;00m -q funcname[2]; [34mor[39;49;00m [34mnot[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$funcname[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m; [34mend[39;49;00m
   416	        [36mset_color [39;49;00mred
   417	        _ [33m"funced: You must specify one function name[39;49;00m
   418	[33m"[39;49;00m
   419	        [36mset_color [39;49;00mnormal
   420	        [34mreturn[39;49;00m 1
   421	    [34mend[39;49;00m
   422
   423	    [34mset[39;49;00m -l init
   424	    [34mswitch[39;49;00m [31m$funcname[39;49;00m
   425	        [34mcase[39;49;00m [33m'-*'[39;49;00m
   426	        [34mset[39;49;00m init [34mfunction[39;49;00m -- [31m$funcname[39;49;00m[33m\n[39;49;00m[33m\n[39;49;00mend
   427	        [34mcase[39;49;00m [33m'*'[39;49;00m
   428	        [34mset[39;49;00m init [34mfunction[39;49;00m [31m$funcname[39;49;00m[33m\n[39;49;00m[33m\n[39;49;00mend
   429	    [34mend[39;49;00m
   430
   431	    [37m# Break editor up to get its first command (i.e. discard flags)[39;49;00m
   432	    [34mif[39;49;00m [34mtest[39;49;00m -n [33m"[39;49;00m[31m$editor[39;49;00m[33m"[39;49;00m
   433	        [34mset[39;49;00m -l editor_cmd
   434	        [36meval [39;49;00m[34mset[39;49;00m editor_cmd [31m$editor[39;49;00m
   435	        [34mif[39;49;00m [34mnot[39;49;00m [36mtype[39;49;00m -f [33m"[39;49;00m[31m$editor_cmd[39;49;00m[33m[1][39;49;00m[33m"[39;49;00m >/dev/null
   436	            _ [33m"[39;49;00m[33mfunced: The value for \$EDITOR '[39;49;00m[31m$editor[39;49;00m[33m' could not be used because the command '[39;49;00m[31m$editor_cmd[39;49;00m[33m[1]' could not be found[39;49;00m
   437	[33m    [39;49;00m[33m"[39;49;00m
   438	            [34mset[39;49;00m editor [36mfish[39;49;00m
   439	[36m        [39;49;00m[34mend[39;49;00m
   440	    [34mend[39;49;00m
   441
   442	    [37m# If no editor is specified, use fish[39;49;00m
   443	    [34mif[39;49;00m [34mtest[39;49;00m -z [33m"[39;49;00m[31m$editor[39;49;00m[33m"[39;49;00m
   444	        [34mset[39;49;00m editor [36mfish[39;49;00m
   445	[36m    [39;49;00m[34mend[39;49;00m
   446
   447	    [34mif[39;49;00m [34mbegin[39;49;00m; [34mset[39;49;00m -q interactive[1]; [34mor[39;49;00m [34mtest[39;49;00m [33m"[39;49;00m[31m$editor[39;49;00m[33m"[39;49;00m = [36mfish[39;49;00m; [34mend[39;49;00m
   448	        [34mset[39;49;00m -l IFS
   449	        [34mif[39;49;00m [36mfunctions[39;49;00m -q -- [31m$funcname[39;49;00m
   450	            [37m# Shadow IFS here to avoid array splitting in command substitution[39;49;00m
   451	            [34mset[39;49;00m init ([36mfunctions[39;49;00m -- [31m$funcname[39;49;00m | [36mfish_indent[39;49;00m --no-indent)
   452	        [34mend[39;49;00m
   453
   454	        [34mset[39;49;00m -l prompt [33m'printf "%s%s%s> " (set_color green) '[39;49;00m[31m$funcname[39;49;00m[33m' (set_color normal)'[39;49;00m
   455	        [37m# Unshadow IFS since the fish_title breaks otherwise[39;49;00m
   456	        [34mset[39;49;00m -e IFS
   457	        [34mif[39;49;00m [36mread[39;49;00m -p [31m$prompt[39;49;00m -c [33m"[39;49;00m[31m$init[39;49;00m[33m"[39;49;00m -s cmd
   458	            [37m# Shadow IFS _again_ to avoid array splitting in command substitution[39;49;00m
   459	            [34mset[39;49;00m -l IFS
   460	            [36meval[39;49;00m ([34mecho[39;49;00m -n [31m$cmd[39;49;00m | [36mfish_indent[39;49;00m)
   461	        [34mend[39;49;00m
   462	        [34mreturn[39;49;00m 0
   463	    [34mend[39;49;00m
   464
   465	    [34mset[39;49;00m -q TMPDIR; [34mor[39;49;00m [34mset[39;49;00m -l TMPDIR /tmp
   466	    [34mset[39;49;00m -l tmpname ([36mprintf[39;49;00m [33m"[39;49;00m[31m$TMPDIR[39;49;00m[33m/fish_funced_%d_%d.fish[39;49;00m[33m"[39;49;00m %self ([36mrandom[39;49;00m))
   467	    [34mwhile[39;49;00m [34mtest[39;49;00m -f [31m$tmpname[39;49;00m
   468	        [34mset[39;49;00m tmpname ([36mprintf[39;49;00m [33m"[39;49;00m[31m$TMPDIR[39;49;00m[33m/fish_funced_%d_%d.fish[39;49;00m[33m"[39;49;00m %self ([36mrandom[39;49;00m))
   469	    [34mend[39;49;00m
   470
   471	    [34mif[39;49;00m [36mfunctions[39;49;00m -q -- [31m$funcname[39;49;00m
   472	        [36mfunctions[39;49;00m -- [31m$funcname[39;49;00m > [31m$tmpname[39;49;00m
   473	    [34melse[39;49;00m
   474	        [34mecho[39;49;00m [31m$init[39;49;00m > [31m$tmpname[39;49;00m
   475	    [34mend[39;49;00m
   476	    [34mif[39;49;00m [36meval[39;49;00m [31m$editor[39;49;00m [31m$tmpname[39;49;00m
   477	        . [31m$tmpname[39;49;00m
   478	    [34mend[39;49;00m
   479	    [34mset[39;49;00m -l stat [31m$status[39;49;00m
   480	    rm -f [31m$tmpname[39;49;00m >/dev/null
   481	    [34mreturn[39;49;00m [31m$stat[39;49;00m
   482	[34mend[39;49;00m
   483
   484	[37m# -----------------------------------------------------------------------------[39;49;00m
   485	[37m# Main file for fish command completions. This file contains various[39;49;00m
   486	[37m# common helper functions for the command completions. All actual[39;49;00m
   487	[37m# completions are located in the completions subdirectory.[39;49;00m
   488	[37m## -----------------------------------------------------------------------------[39;49;00m
   489
   490	[37m#[39;49;00m
   491	[37m# Set default field separators[39;49;00m
   492	[37m#[39;49;00m
   493
   494	[34mset[39;49;00m -g IFS [33m\n[39;49;00m[33m\ [39;49;00m[33m\t[39;49;00m
   495
   496	[37m#[39;49;00m
   497	[37m# Set default search paths for completions and shellscript functions[39;49;00m
   498	[37m# unless they already exist[39;49;00m
   499	[37m#[39;49;00m
   500
   501	[34mset[39;49;00m -l configdir ~/.config
   502
   503	[34mif[39;49;00m [34mset[39;49;00m -q XDG_CONFIG_HOME
   504	  [34mset[39;49;00m configdir [31m$XDG_CONFIG_HOME[39;49;00m
   505	[34mend[39;49;00m
   506
   507	[37m# __fish_datadir, __fish_sysconfdir, __fish_help_dir, __fish_bin_dir[39;49;00m
   508	[37m# are expected to have been set up by read_init from fish.cpp[39;49;00m
   509
   510	[37m# Set up function and completion paths. Make sure that the fish[39;49;00m
   511	[37m# default functions/completions are included in the respective path.[39;49;00m
   512
   513	[34mif[39;49;00m [34mnot[39;49;00m [34mset[39;49;00m -q fish_function_path
   514	  [34mset[39;49;00m fish_function_path [31m$configdir[39;49;00m/fish/functions    [31m$__fish_sysconfdir[39;49;00m/functions    [31m$__fish_datadir[39;49;00m/functions
   515	[34mend[39;49;00m
   516
   517	[34mif[39;49;00m [34mnot[39;49;00m [36mcontains[39;49;00m [31m$__fish_datadir[39;49;00m/functions [31m$fish_function_path[39;49;00m
   518	  [34mset[39;49;00m fish_function_path[-1] [31m$__fish_datadir[39;49;00m/functions
   519	[34mend[39;49;00m
   520
   521	[34mif[39;49;00m [34mnot[39;49;00m [34mset[39;49;00m -q fish_complete_path
   522	  [34mset[39;49;00m fish_complete_path [31m$configdir[39;49;00m/fish/completions  [31m$__fish_sysconfdir[39;49;00m/completions  [31m$__fish_datadir[39;49;00m/completions
   523	[34mend[39;49;00m
   524
   525	[34mif[39;49;00m [34mnot[39;49;00m [36mcontains[39;49;00m [31m$__fish_datadir[39;49;00m/completions [31m$fish_complete_path[39;49;00m
   526	  [34mset[39;49;00m fish_complete_path[-1] [31m$__fish_datadir[39;49;00m/completions
   527	[34mend[39;49;00m
   528
   529	[37m#[39;49;00m
   530	[37m# This is a Solaris-specific test to modify the PATH so that[39;49;00m
   531	[37m# Posix-conformant tools are used by default. It is separate from the[39;49;00m
   532	[37m# other PATH code because this directory needs to be prepended, not[39;49;00m
   533	[37m# appended, since it contains POSIX-compliant replacements for various[39;49;00m
   534	[37m# system utilities.[39;49;00m
   535	[37m#[39;49;00m
   536
   537	[34mif[39;49;00m [34mtest[39;49;00m -d /usr/xpg4/bin
   538	  [34mif[39;49;00m [34mnot[39;49;00m [36mcontains[39;49;00m /usr/xpg4/bin [31m$PATH[39;49;00m
   539	    [34mset[39;49;00m PATH /usr/xpg4/bin [31m$PATH[39;49;00m
   540	  [34mend[39;49;00m
   541	[34mend[39;49;00m
   542
   543	[37m#[39;49;00m
   544	[37m# Add a few common directories to path, if they exists. Note that pure[39;49;00m
   545	[37m# console programs like makedep sometimes live in /usr/X11R6/bin, so we[39;49;00m
   546	[37m# want this even for text-only terminals.[39;49;00m
   547	[37m#[39;49;00m
   548
   549	[34mset[39;49;00m -l path_list /bin /usr/bin /usr/X11R6/bin /usr/local/bin [31m$__fish_bin_dir[39;49;00m
   550
   551	[37m# Root should also have the sbin directories in the path[39;49;00m
   552	[34mswitch[39;49;00m [31m$USER[39;49;00m
   553	  [34mcase[39;49;00m root
   554	  [34mset[39;49;00m path_list [31m$path_list[39;49;00m /sbin /usr/sbin /usr/local/sbin
   555	[34mend[39;49;00m
   556
   557	[34mfor[39;49;00m i [34min[39;49;00m [31m$path_list[39;49;00m
   558	  [34mif[39;49;00m [34mnot[39;49;00m [36mcontains[39;49;00m [31m$i[39;49;00m [31m$PATH[39;49;00m
   559	    [34mif[39;49;00m [34mtest[39;49;00m -d [31m$i[39;49;00m
   560	      [34mset[39;49;00m PATH [31m$PATH[39;49;00m [31m$i[39;49;00m
   561	    [34mend[39;49;00m
   562	  [34mend[39;49;00m
   563	[34mend[39;49;00m
   564
   565	[37m#[39;49;00m
   566	[37m# Launch debugger on SIGTRAP[39;49;00m
   567	[37m#[39;49;00m
   568	[34mfunction[39;49;00m fish_sigtrap_handler --on-signal TRAP --no-scope-shadowing --description [33m"Signal handler for the TRAP signal. Lanches a debug prompt."[39;49;00m
   569	  [36mbreakpoint[39;49;00m
   570	[34mend[39;49;00m
   571
   572	[37m#[39;49;00m
   573	[37m# Whenever a prompt is displayed, make sure that interactive[39;49;00m
   574	[37m# mode-specific initializations have been performed.[39;49;00m
   575	[37m# This handler removes itself after it is first called.[39;49;00m
   576	[37m#[39;49;00m
   577	[34mfunction[39;49;00m __fish_on_interactive --on-event [36mfish_prompt[39;49;00m
   578	[36m  [39;49;00m__fish_config_interactive
   579	  [36mfunctions[39;49;00m -e __fish_on_interactive
   580	[34mend[39;49;00m
