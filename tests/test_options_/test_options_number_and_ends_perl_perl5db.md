     1	=head1[37m [39;49;00mNAME[37m [39;49;00m[37m[39;49;00m$
     2	[37m[39;49;00m$
     3	perl5db.pl[37m [39;49;00m-[37m [39;49;00mthe[37m [39;49;00mperl[37m [39;49;00mdebugger[37m[39;49;00m$
     4	[37m[39;49;00m$
     5	=head1[37m [39;49;00mSYNOPSIS[37m[39;49;00m$
     6	[37m[39;49;00m$
     7	[37m    [39;49;00mperl[37m [39;49;00m-d[37m  [39;49;00myour_Perl_script[37m[39;49;00m$
     8	[37m[39;49;00m$
     9	=head1[37m [39;49;00mDESCRIPTION[37m[39;49;00m$
    10	[37m[39;49;00m$
    11	After[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00mroutine[37m [39;49;00mis[37m [39;49;00mover,[37m [39;49;00mwe[37m [39;49;00mdon[04m[91m'[39;49;00mt[37m [39;49;00mhave[37m [39;49;00muser[37m [39;49;00mcode[37m [39;49;00mexecuting[37m [39;49;00min[37m [39;49;00mthe[37m [39;49;00mdebugger[04m[91m'[39;49;00ms[37m[39;49;00m$
    12	context,[37m [39;49;00mso[37m [39;49;00mwe[37m [39;49;00mcan[37m [39;49;00muse[37m [39;49;00mC<my>[37m [39;49;00mfreely.[37m[39;49;00m$
    13	[37m[39;49;00m$
    14	=cut[37m[39;49;00m$
    15	[37m[39;49;00m$
    16	[36m#[39;49;00m[36m############################################# Begin lexical danger zone[39;49;00m[36m[39;49;00m$
    17	[37m[39;49;00m$
    18	[36m#[39;49;00m[36m 'my' variables used here could leak into (that is, be visible in)[39;49;00m[36m[39;49;00m$
    19	[36m#[39;49;00m[36m the context that the code being evaluated is executing in. This means that[39;49;00m[36m[39;49;00m$
    20	[36m#[39;49;00m[36m the code could modify the debugger's variables.[39;49;00m[36m[39;49;00m$
    21	[36m#[39;49;00m[36m[39;49;00m$
    22	[36m#[39;49;00m[36m Fiddling with the debugger's context could be Bad. We insulate things as[39;49;00m[36m[39;49;00m$
    23	[36m#[39;49;00m[36m much as we can.[39;49;00m[36m[39;49;00m$
    24	[37m[39;49;00m$
    25	sub[37m [39;49;00meval[37m [39;49;00m{[37m[39;49;00m$
    26	[37m[39;49;00m$
    27	[37m    [39;49;00m[36m#[39;49;00m[36m 'my' would make it visible from user code[39;49;00m[36m[39;49;00m$
    28	[37m    [39;49;00m[36m#[39;49;00m[36m    but so does local! --tchrist[39;49;00m[36m[39;49;00m$
    29	[37m    [39;49;00m[36m#[39;49;00m[36m Remember: this localizes @DB::res, not @main::res.[39;49;00m[36m[39;49;00m$
    30	[37m    [39;49;00mlocal[37m [39;49;00m[04m[91m@[39;49;00mres;[37m[39;49;00m$
    31	[37m    [39;49;00m{[37m[39;49;00m$
    32	[37m[39;49;00m$
    33	[37m        [39;49;00m[36m#[39;49;00m[36m Try to keep the user code from messing  with us. Save these so that[39;49;00m[36m[39;49;00m$
    34	[37m        [39;49;00m[36m#[39;49;00m[36m even if the eval'ed code changes them, we can put them back again.[39;49;00m[36m[39;49;00m$
    35	[37m        [39;49;00m[36m#[39;49;00m[36m Needed because the user could refer directly to the debugger's[39;49;00m[36m[39;49;00m$
    36	[37m        [39;49;00m[36m#[39;49;00m[36m package globals (and any 'my' variables in this containing scope)[39;49;00m[36m[39;49;00m$
    37	[37m        [39;49;00m[36m#[39;49;00m[36m inside the eval(), and we want to try to stay safe.[39;49;00m[36m[39;49;00m$
    38	[37m        [39;49;00mlocal[37m [39;49;00m$otrace[37m  [39;49;00m=[37m [39;49;00m$trace;[37m[39;49;00m$
    39	[37m        [39;49;00mlocal[37m [39;49;00m$osingle[37m [39;49;00m=[37m [39;49;00m$single;[37m[39;49;00m$
    40	[37m        [39;49;00mlocal[37m [39;49;00m$od[37m      [39;49;00m=[37m [39;49;00m$^D;[37m[39;49;00m$
    41	[37m[39;49;00m$
    42	[37m        [39;49;00m[36m#[39;49;00m[36m Untaint the incoming eval() argument.[39;49;00m[36m[39;49;00m$
    43	[37m        [39;49;00m{[37m [39;49;00m($evalarg)[37m [39;49;00m=[37m [39;49;00m$evalarg[37m [39;49;00m=~[37m [39;49;00m/(.*)/s;[37m [39;49;00m}[37m[39;49;00m$
    44	[37m[39;49;00m$
    45	[37m        [39;49;00m[36m#[39;49;00m[36m $usercontext built in DB::DB near the comment[39;49;00m[36m[39;49;00m$
    46	[37m        [39;49;00m[36m#[39;49;00m[36m "set up the context for DB::eval ..."[39;49;00m[36m[39;49;00m$
    47	[37m        [39;49;00m[36m#[39;49;00m[36m Evaluate and save any results.[39;49;00m[36m[39;49;00m$
    48	[37m        [39;49;00m[04m[91m@[39;49;00mres[37m [39;49;00m=[37m [39;49;00meval[37m [39;49;00m[33m"[39;49;00m[33m$usercontext $evalarg;[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m  [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00m[33m'[39;49;00m[33m\n[39;49;00m[33m'[39;49;00m[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mnice[37m [39;49;00mrecursive[37m [39;49;00mdebug[37m[39;49;00m$
    49	[37m[39;49;00m$
    50	[37m        [39;49;00m[36m#[39;49;00m[36m Restore those old values.[39;49;00m[36m[39;49;00m$
    51	[37m        [39;49;00m$trace[37m  [39;49;00m=[37m [39;49;00m$otrace;[37m[39;49;00m$
    52	[37m        [39;49;00m$single[37m [39;49;00m=[37m [39;49;00m$osingle;[37m[39;49;00m$
    53	[37m        [39;49;00m$^D[37m     [39;49;00m=[37m [39;49;00m$od;[37m[39;49;00m$
    54	[37m    [39;49;00m}[37m[39;49;00m$
    55	[37m[39;49;00m$
    56	[37m    [39;49;00m[36m#[39;49;00m[36m Save the current value of $@, and preserve it in the debugger's copy[39;49;00m[36m[39;49;00m$
    57	[37m    [39;49;00m[36m#[39;49;00m[36m of the saved precious globals.[39;49;00m[36m[39;49;00m$
    58	[37m    [39;49;00mmy[37m [39;49;00m$at[37m [39;49;00m=[37m [39;49;00m$[04m[91m@[39;49;00m;[37m[39;49;00m$
    59	[37m[39;49;00m$
    60	[37m    [39;49;00m[36m#[39;49;00m[36m Since we're only saving $@, we only have to localize the array element[39;49;00m[36m[39;49;00m$
    61	[37m    [39;49;00m[36m#[39;49;00m[36m that it will be stored in.[39;49;00m[36m[39;49;00m$
    62	[37m    [39;49;00mlocal[37m [39;49;00m$saved[[34m0[39;49;00m];[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mPreserve[37m [39;49;00mthe[37m [39;49;00mold[37m [39;49;00mvalue[37m [39;49;00mof[37m [39;49;00m$[04m[91m@[39;49;00m[37m[39;49;00m$
    63	[37m    [39;49;00meval[37m [39;49;00m{[37m [39;49;00m&DB::save[37m [39;49;00m};[37m[39;49;00m$
    64	[37m[39;49;00m$
    65	[37m    [39;49;00m[36m#[39;49;00m[36m Now see whether we need to report an error back to the user.[39;49;00m[36m[39;49;00m$
    66	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m($at)[37m [39;49;00m{[37m[39;49;00m$
    67	[37m        [39;49;00mlocal[37m [39;49;00m$[04m[91m\[39;49;00m[37m [39;49;00m=[37m [39;49;00m[04m[91m'[39;49;00m[04m[91m'[39;49;00m;[37m[39;49;00m$
    68	[37m        [39;49;00mprint[37m [39;49;00m$OUT[37m [39;49;00m$at;[37m[39;49;00m$
    69	[37m    [39;49;00m}[37m[39;49;00m$
    70	[37m[39;49;00m$
    71	[37m    [39;49;00m[36m#[39;49;00m[36m Display as required by the caller. $onetimeDump and $onetimedumpDepth[39;49;00m[36m[39;49;00m$
    72	[37m    [39;49;00m[36m#[39;49;00m[36m are package globals.[39;49;00m[36m[39;49;00m$
    73	[37m    [39;49;00melsif[37m [39;49;00m($onetimeDump)[37m [39;49;00m{[37m[39;49;00m$
    74	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m$onetimeDump[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mdump[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
    75	[37m            [39;49;00mlocal[37m [39;49;00m$option{dumpDepth}[37m [39;49;00m=[37m [39;49;00m$onetimedumpDepth[37m[39;49;00m$
    76	[37m              [39;49;00m[34mif[39;49;00m[37m [39;49;00mdefined[37m [39;49;00m$onetimedumpDepth;[37m[39;49;00m$
    77	[37m            [39;49;00mdumpit([37m [39;49;00m$OUT,[37m [39;49;00m[04m[91m\[39;49;00m[04m[91m@[39;49;00mres[37m [39;49;00m);[37m[39;49;00m$
    78	[37m        [39;49;00m}[37m[39;49;00m$
    79	[37m        [39;49;00melsif[37m [39;49;00m([37m [39;49;00m$onetimeDump[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mmethods[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
    80	[37m            [39;49;00mmethods([37m [39;49;00m$res[[34m0[39;49;00m][37m [39;49;00m);[37m[39;49;00m$
    81	[37m        [39;49;00m}[37m[39;49;00m$
    82	[37m    [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00melsif[37m [39;49;00m($onetimeDump)[37m[39;49;00m$
    83	[37m    [39;49;00m[04m[91m@[39;49;00mres;[37m[39;49;00m$
    84	}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00msub[37m [39;49;00meval[37m[39;49;00m$
    85	[37m[39;49;00m$
    86	[36m#[39;49;00m[36m############################################# End lexical danger zone[39;49;00m[36m[39;49;00m$
    87	[37m[39;49;00m$
    88	[36m#[39;49;00m[36m After this point it is safe to introduce lexicals.[39;49;00m[36m[39;49;00m$
    89	[36m#[39;49;00m[36m The code being debugged will be executing in its own context, and[39;49;00m[36m[39;49;00m$
    90	[36m#[39;49;00m[36m can't see the inside of the debugger.[39;49;00m[36m[39;49;00m$
    91	[36m#[39;49;00m[36m[39;49;00m$
    92	[36m#[39;49;00m[36m However, one should not overdo it: leave as much control from outside as[39;49;00m[36m[39;49;00m$
    93	[36m#[39;49;00m[36m possible. If you make something a lexical, it's not going to be addressable[39;49;00m[36m[39;49;00m$
    94	[36m#[39;49;00m[36m from outside the debugger even if you know its name.[39;49;00m[36m[39;49;00m$
    95	[37m[39;49;00m$
    96	[36m#[39;49;00m[36m This file is automatically included if you do perl -d.[39;49;00m[36m[39;49;00m$
    97	[36m#[39;49;00m[36m It's probably not useful to include this yourself.[39;49;00m[36m[39;49;00m$
    98	[36m#[39;49;00m[36m[39;49;00m$
    99	[36m#[39;49;00m[36m Before venturing further into these twisty passages, it is[39;49;00m[36m[39;49;00m$
   100	[36m#[39;49;00m[36m wise to read the perldebguts man page or risk the ire of dragons.[39;49;00m[36m[39;49;00m$
   101	[36m#[39;49;00m[36m[39;49;00m$
   102	[36m#[39;49;00m[36m (It should be noted that perldebguts will tell you a lot about[39;49;00m[36m[39;49;00m$
   103	[36m#[39;49;00m[36m the underlying mechanics of how the debugger interfaces into the[39;49;00m[36m[39;49;00m$
   104	[36m#[39;49;00m[36m Perl interpreter, but not a lot about the debugger itself. The new[39;49;00m[36m[39;49;00m$
   105	[36m#[39;49;00m[36m comments in this code try to address this problem.)[39;49;00m[36m[39;49;00m$
   106	[37m[39;49;00m$
   107	[36m#[39;49;00m[36m Note that no subroutine call is possible until &DB::sub is defined[39;49;00m[36m[39;49;00m$
   108	[36m#[39;49;00m[36m (for subroutines defined outside of the package DB). In fact the same is[39;49;00m[36m[39;49;00m$
   109	[36m#[39;49;00m[36m true if $deep is not defined.[39;49;00m[36m[39;49;00m$
   110	[37m[39;49;00m$
   111	[36m#[39;49;00m[36m Enhanced by ilya@math.ohio-state.edu (Ilya Zakharevich)[39;49;00m[36m[39;49;00m$
   112	[37m[39;49;00m$
   113	[36m#[39;49;00m[36m modified Perl debugger, to be run from Emacs in perldb-mode[39;49;00m[36m[39;49;00m$
   114	[36m#[39;49;00m[36m Ray Lischner (uunet!mntgfx!lisch) as of 5 Nov 1990[39;49;00m[36m[39;49;00m$
   115	[36m#[39;49;00m[36m Johan Vromans -- upgrade to 4.0 pl 10[39;49;00m[36m[39;49;00m$
   116	[36m#[39;49;00m[36m Ilya Zakharevich -- patches after 5.001 (and some before ;-)[39;49;00m[36m[39;49;00m$
   117	[37m[39;49;00m$
   118	[36m#[39;49;00m[36m (We have made efforts to  clarify the comments in the change log[39;49;00m[36m[39;49;00m$
   119	[36m#[39;49;00m[36m in other places; some of them may seem somewhat obscure as they[39;49;00m[36m[39;49;00m$
   120	[36m#[39;49;00m[36m were originally written, and explaining them away from the code[39;49;00m[36m[39;49;00m$
   121	[36m#[39;49;00m[36m in question seems conterproductive.. -JM)[39;49;00m[36m[39;49;00m$
   122	[37m[39;49;00m$
   123	=head1[37m [39;49;00mDEBUGGER[37m [39;49;00mINITIALIZATION[37m[39;49;00m$
   124	[37m[39;49;00m$
   125	The[37m [39;49;00mdebugger[37m [39;49;00mstarts[37m [39;49;00mup[37m [39;49;00min[37m [39;49;00mphases.[37m[39;49;00m$
   126	[37m[39;49;00m$
   127	=head2[37m [39;49;00mBASIC[37m [39;49;00mSETUP[37m[39;49;00m$
   128	[37m[39;49;00m$
   129	First,[37m [39;49;00mit[37m [39;49;00minitializes[37m [39;49;00mthe[37m [39;49;00menvironment[37m [39;49;00mit[37m [39;49;00mwants[37m [39;49;00mto[37m [39;49;00mrun[37m [39;49;00min:[37m [39;49;00mturning[37m [39;49;00moff[37m[39;49;00m$
   130	warnings[37m [39;49;00mduring[37m [39;49;00mits[37m [39;49;00mown[37m [39;49;00mcompilation,[37m [39;49;00mdefining[37m [39;49;00mvariables[37m [39;49;00mwhich[37m [39;49;00mit[37m [39;49;00mwill[37m [39;49;00mneed[37m[39;49;00m$
   131	to[37m [39;49;00mavoid[37m [39;49;00mwarnings[37m [39;49;00mlater,[37m [39;49;00msetting[37m [39;49;00mitself[37m [39;49;00mup[37m [39;49;00mto[37m [39;49;00mnot[37m [39;49;00mexit[37m [39;49;00mwhen[37m [39;49;00mthe[37m [39;49;00mprogram[37m[39;49;00m$
   132	terminates,[37m [39;49;00mand[37m [39;49;00mdefaulting[37m [39;49;00mto[37m [39;49;00mprinting[37m [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mvalues[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mthe[37m [39;49;00mC<r>[37m [39;49;00mcommand.[37m[39;49;00m$
   133	[37m[39;49;00m$
   134	=cut[37m[39;49;00m$
   135	[37m[39;49;00m$
   136	[36m#[39;49;00m[36m Needed for the statement after exec():[39;49;00m[36m[39;49;00m$
   137	[36m#[39;49;00m[36m[39;49;00m$
   138	[36m#[39;49;00m[36m This BEGIN block is simply used to switch off warnings during debugger[39;49;00m[36m[39;49;00m$
   139	[36m#[39;49;00m[36m compiliation. Probably it would be better practice to fix the warnings,[39;49;00m[36m[39;49;00m$
   140	[36m#[39;49;00m[36m but this is how it's done at the moment.[39;49;00m[36m[39;49;00m$
   141	[37m[39;49;00m$
   142	BEGIN[37m [39;49;00m{[37m[39;49;00m$
   143	[37m    [39;49;00m$ini_warn[37m [39;49;00m=[37m [39;49;00m$^W;[37m[39;49;00m$
   144	[37m    [39;49;00m$^W[37m       [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   145	}[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mSwitch[37m [39;49;00mcompilation[37m [39;49;00mwarnings[37m [39;49;00moff[37m [39;49;00muntil[37m [39;49;00manother[37m [39;49;00mBEGIN.[37m[39;49;00m$
   146	[37m[39;49;00m$
   147	[36m#[39;49;00m[36m test if assertions are supported and actived:[39;49;00m[36m[39;49;00m$
   148	BEGIN[37m [39;49;00m{[37m[39;49;00m$
   149	[37m    [39;49;00m$ini_assertion[37m [39;49;00m=[37m [39;49;00meval[37m [39;49;00m[33m"[39;49;00m[33msub asserting_test : assertion {1}; 1[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   150	[37m[39;49;00m$
   151	[37m    [39;49;00m[36m#[39;49;00m[36m $ini_assertion = undef => assertions unsupported,[39;49;00m[36m[39;49;00m$
   152	[37m    [39;49;00m[36m#[39;49;00m[36m        "       = 1     => assertions supported[39;49;00m[36m[39;49;00m$
   153	[37m    [39;49;00m[36m#[39;49;00m[36m print "\$ini_assertion=$ini_assertion\n";[39;49;00m[36m[39;49;00m$
   154	}[37m[39;49;00m$
   155	[37m[39;49;00m$
   156	local[37m [39;49;00m($^W)[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mSwitch[37m [39;49;00mrun-time[37m [39;49;00mwarnings[37m [39;49;00moff[37m [39;49;00mduring[37m [39;49;00minit.[37m[39;49;00m$
   157	[37m[39;49;00m$
   158	=head2[37m [39;49;00mTHREADS[37m [39;49;00mSUPPORT[37m[39;49;00m$
   159	[37m[39;49;00m$
   160	If[37m [39;49;00mwe[37m [39;49;00mare[37m [39;49;00mrunning[37m [39;49;00munder[37m [39;49;00ma[37m [39;49;00mthreaded[37m [39;49;00mPerl,[37m [39;49;00mwe[37m [39;49;00mrequire[37m [39;49;00mthreads[37m [39;49;00mand[37m [39;49;00mthreads::shared[37m[39;49;00m$
   161	[34mif[39;49;00m[37m [39;49;00mthe[37m [39;49;00menvironment[37m [39;49;00mvariable[37m [39;49;00mC<PERL5DB_THREADED>[37m [39;49;00mis[37m [39;49;00mset,[37m [39;49;00mto[37m [39;49;00menable[37m [39;49;00mproper[37m[39;49;00m$
   162	threaded[37m [39;49;00mdebugger[37m [39;49;00mcontrol.[37m  [39;49;00mC<-dt>[37m [39;49;00mcan[37m [39;49;00malso[37m [39;49;00mbe[37m [39;49;00mused[37m [39;49;00mto[37m [39;49;00mset[37m [39;49;00m[34mthis[39;49;00m.[37m[39;49;00m$
   163	[37m[39;49;00m$
   164	Each[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00m[34mthread[39;49;00m[37m [39;49;00mwill[37m [39;49;00mbe[37m [39;49;00mannounced[37m [39;49;00mand[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mprompt[37m [39;49;00mwill[37m [39;49;00malways[37m [39;49;00minform[37m[39;49;00m$
   165	you[37m [39;49;00mof[37m [39;49;00meach[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00m[34mthread[39;49;00m[37m [39;49;00mcreated.[37m  [39;49;00mIt[37m [39;49;00mwill[37m [39;49;00malso[37m [39;49;00mindicate[37m [39;49;00mthe[37m [39;49;00m[34mthread[39;49;00m[37m [39;49;00mid[37m [39;49;00min[37m [39;49;00mwhich[37m[39;49;00m$
   166	we[37m [39;49;00mare[37m [39;49;00mcurrently[37m [39;49;00mrunning[37m [39;49;00mwithin[37m [39;49;00mthe[37m [39;49;00mprompt[37m [39;49;00mlike[37m [39;49;00m[34mthis[39;49;00m:[37m[39;49;00m$
   167	[37m[39;49;00m$
   168	[37m	[39;49;00m[tid][37m [39;49;00mDB<$i>[37m[39;49;00m$
   169	[37m[39;49;00m$
   170	Where[37m [39;49;00mC<[tid]>[37m [39;49;00mis[37m [39;49;00man[37m [39;49;00minteger[37m [39;49;00m[34mthread[39;49;00m[37m [39;49;00mid[37m [39;49;00mand[37m [39;49;00mC<$i>[37m [39;49;00mis[37m [39;49;00mthe[37m [39;49;00mfamiliar[37m [39;49;00mdebugger[37m[39;49;00m$
   171	command[37m [39;49;00mprompt.[37m  [39;49;00mThe[37m [39;49;00mprompt[37m [39;49;00mwill[37m [39;49;00mshow:[37m [39;49;00mC<[[34m0[39;49;00m]>[37m [39;49;00mwhen[37m [39;49;00mrunning[37m [39;49;00munder[37m [39;49;00mthreads,[37m [39;49;00mbut[37m[39;49;00m$
   172	not[37m [39;49;00mactually[37m [39;49;00min[37m [39;49;00ma[37m [39;49;00m[34mthread[39;49;00m.[37m  [39;49;00mC<[tid]>[37m [39;49;00mis[37m [39;49;00mconsistent[37m [39;49;00mwith[37m [39;49;00mC<gdb>[37m [39;49;00musage.[37m[39;49;00m$
   173	[37m[39;49;00m$
   174	While[37m [39;49;00mrunning[37m [39;49;00munder[37m [39;49;00mthreads,[37m [39;49;00mwhen[37m [39;49;00myou[37m [39;49;00mset[37m [39;49;00mor[37m [39;49;00m[34mdelete[39;49;00m[37m [39;49;00ma[37m [39;49;00mbreakpoint[37m [39;49;00m(etc.),[37m [39;49;00m[34mthis[39;49;00m[37m[39;49;00m$
   175	will[37m [39;49;00mapply[37m [39;49;00mto[37m [39;49;00mall[37m [39;49;00mthreads,[37m [39;49;00mnot[37m [39;49;00mjust[37m [39;49;00mthe[37m [39;49;00mcurrently[37m [39;49;00mrunning[37m [39;49;00mone.[37m  [39;49;00mWhen[37m [39;49;00myou[37m [39;49;00mare[37m [39;49;00m[37m[39;49;00m$
   176	in[37m [39;49;00ma[37m [39;49;00mcurrently[37m [39;49;00mexecuting[37m [39;49;00m[34mthread[39;49;00m,[37m [39;49;00myou[37m [39;49;00mwill[37m [39;49;00mstay[37m [39;49;00mthere[37m [39;49;00muntil[37m [39;49;00mit[37m [39;49;00mcompletes.[37m  [39;49;00mWith[37m[39;49;00m$
   177	the[37m [39;49;00mcurrent[37m [39;49;00mimplementation[37m [39;49;00mit[37m [39;49;00mis[37m [39;49;00mnot[37m [39;49;00mcurrently[37m [39;49;00mpossible[37m [39;49;00mto[37m [39;49;00mhop[37m [39;49;00mfrom[37m [39;49;00mone[37m [39;49;00m[34mthread[39;49;00m[37m[39;49;00m$
   178	to[37m [39;49;00manother.[37m[39;49;00m$
   179	[37m[39;49;00m$
   180	The[37m [39;49;00mC<e>[37m [39;49;00mand[37m [39;49;00mC<E>[37m [39;49;00mcommands[37m [39;49;00mare[37m [39;49;00mcurrently[37m [39;49;00mfairly[37m [39;49;00mminimal[37m [39;49;00m-[37m [39;49;00msee[37m [39;49;00mC<h[37m [39;49;00me>[37m [39;49;00mand[37m [39;49;00mC<h[37m [39;49;00mE>.[37m[39;49;00m$
   181	[37m[39;49;00m$
   182	Note[37m [39;49;00mthat[37m [39;49;00mthreading[37m [39;49;00msupport[37m [39;49;00mwas[37m [39;49;00mbuilt[37m [39;49;00minto[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mas[37m [39;49;00mof[37m [39;49;00mPerl[37m [39;49;00mversion[37m[39;49;00m$
   183	C<[34m5.8[39;49;00m[34m.6[39;49;00m>[37m [39;49;00mand[37m [39;49;00mdebugger[37m [39;49;00mversion[37m [39;49;00mC<[34m1.2[39;49;00m[34m.8[39;49;00m>.[37m[39;49;00m$
   184	[37m[39;49;00m$
   185	=cut[37m[39;49;00m$
   186	[37m[39;49;00m$
   187	BEGIN[37m [39;49;00m{[37m[39;49;00m$
   188	[37m  [39;49;00m[36m#[39;49;00m[36m ensure we can share our non-threaded variables or no-op[39;49;00m[36m[39;49;00m$
   189	[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m($ENV{PERL5DB_THREADED})[37m [39;49;00m{[37m[39;49;00m$
   190	[37m	[39;49;00mrequire[37m [39;49;00mthreads;[37m[39;49;00m$
   191	[37m	[39;49;00mrequire[37m [39;49;00mthreads::shared;[37m[39;49;00m$
   192	[37m	[39;49;00m[34mimport[39;49;00m[37m [39;49;00mthreads::shared[37m [39;49;00m[32mqw[39;49;00m(share);[37m[39;49;00m$
   193	[37m	[39;49;00m$DBGR;[37m[39;49;00m$
   194	[37m	[39;49;00mshare([04m[91m\[39;49;00m$DBGR);[37m[39;49;00m$
   195	[37m	[39;49;00mlock($DBGR);[37m[39;49;00m$
   196	[37m	[39;49;00mprint[37m [39;49;00m[33m"[39;49;00m[33mThreads support enabled[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   197	[37m  [39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
   198	[37m	[39;49;00m*lock[37m  [39;49;00m=[37m [39;49;00msub(*)[37m [39;49;00m{};[37m[39;49;00m$
   199	[37m	[39;49;00m*share[37m [39;49;00m=[37m [39;49;00msub(*)[37m [39;49;00m{};[37m[39;49;00m$
   200	[37m  [39;49;00m}[37m[39;49;00m$
   201	}[37m[39;49;00m$
   202	[37m[39;49;00m$
   203	[36m#[39;49;00m[36m This would probably be better done with "use vars", but that wasn't around[39;49;00m[36m[39;49;00m$
   204	[36m#[39;49;00m[36m when this code was originally written. (Neither was "use strict".) And on[39;49;00m[36m[39;49;00m$
   205	[36m#[39;49;00m[36m the principle of not fiddling with something that was working, this was[39;49;00m[36m[39;49;00m$
   206	[36m#[39;49;00m[36m left alone.[39;49;00m[36m[39;49;00m$
   207	warn([37m               [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mDo[37m [39;49;00mnot[37m [39;49;00m;-)[37m[39;49;00m$
   208	[37m    [39;49;00m[36m#[39;49;00m[36m These variables control the execution of 'dumpvar.pl'.[39;49;00m[36m[39;49;00m$
   209	[37m    [39;49;00m$dumpvar::hashDepth,[37m[39;49;00m$
   210	[37m    [39;49;00m$dumpvar::arrayDepth,[37m[39;49;00m$
   211	[37m    [39;49;00m$dumpvar::dumpDBFiles,[37m[39;49;00m$
   212	[37m    [39;49;00m$dumpvar::dumpPackages,[37m[39;49;00m$
   213	[37m    [39;49;00m$dumpvar::quoteHighBit,[37m[39;49;00m$
   214	[37m    [39;49;00m$dumpvar::printUndef,[37m[39;49;00m$
   215	[37m    [39;49;00m$dumpvar::globPrint,[37m[39;49;00m$
   216	[37m    [39;49;00m$dumpvar::usageOnly,[37m[39;49;00m$
   217	[37m[39;49;00m$
   218	[37m    [39;49;00m[36m#[39;49;00m[36m used to save @ARGV and extract any debugger-related flags.[39;49;00m[36m[39;49;00m$
   219	[37m    [39;49;00m[04m[91m@[39;49;00mARGS,[37m[39;49;00m$
   220	[37m[39;49;00m$
   221	[37m    [39;49;00m[36m#[39;49;00m[36m used to control die() reporting in diesignal()[39;49;00m[36m[39;49;00m$
   222	[37m    [39;49;00m$Carp::CarpLevel,[37m[39;49;00m$
   223	[37m[39;49;00m$
   224	[37m    [39;49;00m[36m#[39;49;00m[36m used to prevent multiple entries to diesignal()[39;49;00m[36m[39;49;00m$
   225	[37m    [39;49;00m[36m#[39;49;00m[36m (if for instance diesignal() itself dies)[39;49;00m[36m[39;49;00m$
   226	[37m    [39;49;00m$panic,[37m[39;49;00m$
   227	[37m[39;49;00m$
   228	[37m    [39;49;00m[36m#[39;49;00m[36m used to prevent the debugger from running nonstop[39;49;00m[36m[39;49;00m$
   229	[37m    [39;49;00m[36m#[39;49;00m[36m after a restart[39;49;00m[36m[39;49;00m$
   230	[37m    [39;49;00m$second_time,[37m[39;49;00m$
   231	[37m  [39;49;00m)[37m[39;49;00m$
   232	[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   233	[37m[39;49;00m$
   234	foreach[37m [39;49;00mmy[37m [39;49;00m$k[37m [39;49;00m(keys[37m [39;49;00m(%INC))[37m [39;49;00m{[37m[39;49;00m$
   235	[37m	[39;49;00m&share([04m[91m\[39;49;00m$main::{[04m[91m'[39;49;00m_<[04m[91m'[39;49;00m.$filename});[37m[39;49;00m$
   236	};[37m[39;49;00m$
   237	[37m[39;49;00m$
   238	[36m#[39;49;00m[36m Command-line + PERLLIB:[39;49;00m[36m[39;49;00m$
   239	[36m#[39;49;00m[36m Save the contents of @INC before they are modified elsewhere.[39;49;00m[36m[39;49;00m$
   240	[04m[91m@[39;49;00mini_INC[37m [39;49;00m=[37m [39;49;00m[04m[91m@[39;49;00mINC;[37m[39;49;00m$
   241	[37m[39;49;00m$
   242	[36m#[39;49;00m[36m This was an attempt to clear out the previous values of various[39;49;00m[36m[39;49;00m$
   243	[36m#[39;49;00m[36m trapped errors. Apparently it didn't help. XXX More info needed![39;49;00m[36m[39;49;00m$
   244	[36m#[39;49;00m[36m $prevwarn = $prevdie = $prevbus = $prevsegv = ''; # Does not help?![39;49;00m[36m[39;49;00m$
   245	[37m[39;49;00m$
   246	[36m#[39;49;00m[36m We set these variables to safe values. We don't want to blindly turn[39;49;00m[36m[39;49;00m$
   247	[36m#[39;49;00m[36m off warnings, because other packages may still want them.[39;49;00m[36m[39;49;00m$
   248	$trace[37m [39;49;00m=[37m [39;49;00m$signal[37m [39;49;00m=[37m [39;49;00m$single[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mUninitialized[37m [39;49;00mwarning[37m [39;49;00msuppression[37m[39;49;00m$
   249	[37m                                   [39;49;00m[36m#[39;49;00m[36m (local $^W cannot help - other packages!).[39;49;00m[36m[39;49;00m$
   250	[37m[39;49;00m$
   251	[36m#[39;49;00m[36m Default to not exiting when program finishes; print the return[39;49;00m[36m[39;49;00m$
   252	[36m#[39;49;00m[36m value when the 'r' command is used to return from a subroutine.[39;49;00m[36m[39;49;00m$
   253	$inhibit_exit[37m [39;49;00m=[37m [39;49;00m$option{PrintRet}[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
   254	[37m[39;49;00m$
   255	=head1[37m [39;49;00mOPTION[37m [39;49;00mPROCESSING[37m[39;49;00m$
   256	[37m[39;49;00m$
   257	The[37m [39;49;00mdebugger[04m[91m'[39;49;00ms[37m [39;49;00moptions[37m [39;49;00mare[37m [39;49;00mactually[37m [39;49;00mspread[37m [39;49;00mout[37m [39;49;00mover[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mitself[37m [39;49;00mand[37m [39;49;00m[37m[39;49;00m$
   258	C<dumpvar.pl>;[37m [39;49;00msome[37m [39;49;00mof[37m [39;49;00mthese[37m [39;49;00mare[37m [39;49;00mvariables[37m [39;49;00mto[37m [39;49;00mbe[37m [39;49;00mset,[37m [39;49;00m[34mwhile[39;49;00m[37m [39;49;00mothers[37m [39;49;00mare[37m [39;49;00m[37m[39;49;00m$
   259	subs[37m [39;49;00mto[37m [39;49;00mbe[37m [39;49;00mcalled[37m [39;49;00mwith[37m [39;49;00ma[37m [39;49;00mvalue.[37m [39;49;00mTo[37m [39;49;00m[34mtry[39;49;00m[37m [39;49;00mto[37m [39;49;00mmake[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00ma[37m [39;49;00mlittle[37m [39;49;00measier[37m [39;49;00mto[37m[39;49;00m$
   260	manage,[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00muses[37m [39;49;00ma[37m [39;49;00mfew[37m [39;49;00mdata[37m [39;49;00mstructures[37m [39;49;00mto[37m [39;49;00mdefine[37m [39;49;00mwhat[37m [39;49;00moptions[37m[39;49;00m$
   261	are[37m [39;49;00mlegal[37m [39;49;00mand[37m [39;49;00mhow[37m [39;49;00mthey[37m [39;49;00mare[37m [39;49;00mto[37m [39;49;00mbe[37m [39;49;00mprocessed.[37m[39;49;00m$
   262	[37m[39;49;00m$
   263	First,[37m [39;49;00mthe[37m [39;49;00mC<[04m[91m@[39;49;00moptions>[37m [39;49;00marray[37m [39;49;00mdefines[37m [39;49;00mthe[37m [39;49;00mI<names>[37m [39;49;00mof[37m [39;49;00mall[37m [39;49;00mthe[37m [39;49;00moptions[37m [39;49;00mthat[37m[39;49;00m$
   264	are[37m [39;49;00mto[37m [39;49;00mbe[37m [39;49;00maccepted.[37m[39;49;00m$
   265	[37m[39;49;00m$
   266	=cut[37m[39;49;00m$
   267	[37m[39;49;00m$
   268	[04m[91m@[39;49;00moptions[37m [39;49;00m=[37m [39;49;00mqw([37m[39;49;00m$
   269	[37m  [39;49;00mCommandSet[37m[39;49;00m$
   270	[37m  [39;49;00mhashDepth[37m    [39;49;00marrayDepth[37m    [39;49;00mdumpDepth[37m[39;49;00m$
   271	[37m  [39;49;00mDumpDBFiles[37m  [39;49;00mDumpPackages[37m  [39;49;00mDumpReused[37m[39;49;00m$
   272	[37m  [39;49;00mcompactDump[37m  [39;49;00mveryCompact[37m   [39;49;00mquote[37m[39;49;00m$
   273	[37m  [39;49;00mHighBit[37m      [39;49;00mundefPrint[37m    [39;49;00mglobPrint[37m[39;49;00m$
   274	[37m  [39;49;00mPrintRet[37m     [39;49;00mUsageOnly[37m     [39;49;00mframe[37m[39;49;00m$
   275	[37m  [39;49;00mAutoTrace[37m    [39;49;00mTTY[37m           [39;49;00mnoTTY[37m[39;49;00m$
   276	[37m  [39;49;00mReadLine[37m     [39;49;00mNonStop[37m       [39;49;00mLineInfo[37m[39;49;00m$
   277	[37m  [39;49;00mmaxTraceLen[37m  [39;49;00mrecallCommand[37m [39;49;00mShellBang[37m[39;49;00m$
   278	[37m  [39;49;00mpager[37m        [39;49;00mtkRunning[37m     [39;49;00mornaments[37m[39;49;00m$
   279	[37m  [39;49;00msignalLevel[37m  [39;49;00mwarnLevel[37m     [39;49;00mdieLevel[37m[39;49;00m$
   280	[37m  [39;49;00minhibit_exit[37m [39;49;00mImmediateStop[37m [39;49;00mbareStringify[37m[39;49;00m$
   281	[37m  [39;49;00mCreateTTY[37m    [39;49;00mRemotePort[37m    [39;49;00mwindowSize[37m[39;49;00m$
   282	[37m  [39;49;00mDollarCaretP[37m [39;49;00mOnlyAssertions[37m [39;49;00mWarnAssertions[37m[39;49;00m$
   283	);[37m[39;49;00m$
   284	[37m[39;49;00m$
   285	[04m[91m@[39;49;00mRememberOnROptions[37m [39;49;00m=[37m [39;49;00mqw(DollarCaretP[37m [39;49;00mOnlyAssertions);[37m[39;49;00m$
   286	[37m[39;49;00m$
   287	=pod[37m[39;49;00m$
   288	[37m[39;49;00m$
   289	Second,[37m [39;49;00mC<optionVars>[37m [39;49;00mlists[37m [39;49;00mthe[37m [39;49;00mvariables[37m [39;49;00mthat[37m [39;49;00meach[37m [39;49;00moption[37m [39;49;00muses[37m [39;49;00mto[37m [39;49;00msave[37m [39;49;00mits[37m[39;49;00m$
   290	state.[37m[39;49;00m$
   291	[37m[39;49;00m$
   292	=cut[37m[39;49;00m$
   293	[37m[39;49;00m$
   294	[32m%option[39;49;00mVars[37m [39;49;00m=[37m [39;49;00m([37m[39;49;00m$
   295	[37m    [39;49;00mhashDepth[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::hashDepth,[37m[39;49;00m$
   296	[37m    [39;49;00marrayDepth[37m    [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::arrayDepth,[37m[39;49;00m$
   297	[37m    [39;49;00mCommandSet[37m    [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$CommandSet,[37m[39;49;00m$
   298	[37m    [39;49;00mDumpDBFiles[37m   [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::dumpDBFiles,[37m[39;49;00m$
   299	[37m    [39;49;00mDumpPackages[37m  [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::dumpPackages,[37m[39;49;00m$
   300	[37m    [39;49;00mDumpReused[37m    [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::dumpReused,[37m[39;49;00m$
   301	[37m    [39;49;00mHighBit[37m       [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::quoteHighBit,[37m[39;49;00m$
   302	[37m    [39;49;00mundefPrint[37m    [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::printUndef,[37m[39;49;00m$
   303	[37m    [39;49;00mglobPrint[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::globPrint,[37m[39;49;00m$
   304	[37m    [39;49;00mUsageOnly[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::usageOnly,[37m[39;49;00m$
   305	[37m    [39;49;00mCreateTTY[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$CreateTTY,[37m[39;49;00m$
   306	[37m    [39;49;00mbareStringify[37m [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::bareStringify,[37m[39;49;00m$
   307	[37m    [39;49;00mframe[37m         [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$frame,[37m[39;49;00m$
   308	[37m    [39;49;00mAutoTrace[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$trace,[37m[39;49;00m$
   309	[37m    [39;49;00minhibit_exit[37m  [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$inhibit_exit,[37m[39;49;00m$
   310	[37m    [39;49;00mmaxTraceLen[37m   [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$maxtrace,[37m[39;49;00m$
   311	[37m    [39;49;00mImmediateStop[37m [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$ImmediateStop,[37m[39;49;00m$
   312	[37m    [39;49;00mRemotePort[37m    [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$remoteport,[37m[39;49;00m$
   313	[37m    [39;49;00mwindowSize[37m    [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$window,[37m[39;49;00m$
   314	[37m    [39;49;00mWarnAssertions[37m [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$warnassertions,[37m[39;49;00m$
   315	);[37m[39;49;00m$
   316	[37m[39;49;00m$
   317	=pod[37m[39;49;00m$
   318	[37m[39;49;00m$
   319	Third,[37m [39;49;00mC<[32m%option[39;49;00mAction>[37m [39;49;00mdefines[37m [39;49;00mthe[37m [39;49;00msubroutine[37m [39;49;00mto[37m [39;49;00mbe[37m [39;49;00mcalled[37m [39;49;00mto[37m [39;49;00mprocess[37m [39;49;00meach[37m[39;49;00m$
   320	option.[37m[39;49;00m$
   321	[37m[39;49;00m$
   322	=cut[37m [39;49;00m[37m[39;49;00m$
   323	[37m[39;49;00m$
   324	[32m%option[39;49;00mAction[37m [39;49;00m=[37m [39;49;00m([37m[39;49;00m$
   325	[37m    [39;49;00mcompactDump[37m   [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&dumpvar::compactDump,[37m[39;49;00m$
   326	[37m    [39;49;00mveryCompact[37m   [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&dumpvar::veryCompact,[37m[39;49;00m$
   327	[37m    [39;49;00mquote[37m         [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&dumpvar::quote,[37m[39;49;00m$
   328	[37m    [39;49;00mTTY[37m           [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&TTY,[37m[39;49;00m$
   329	[37m    [39;49;00mnoTTY[37m         [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&noTTY,[37m[39;49;00m$
   330	[37m    [39;49;00mReadLine[37m      [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&ReadLine,[37m[39;49;00m$
   331	[37m    [39;49;00mNonStop[37m       [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&NonStop,[37m[39;49;00m$
   332	[37m    [39;49;00mLineInfo[37m      [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&LineInfo,[37m[39;49;00m$
   333	[37m    [39;49;00mrecallCommand[37m [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&recallCommand,[37m[39;49;00m$
   334	[37m    [39;49;00mShellBang[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&shellBang,[37m[39;49;00m$
   335	[37m    [39;49;00mpager[37m         [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&pager,[37m[39;49;00m$
   336	[37m    [39;49;00msignalLevel[37m   [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&signalLevel,[37m[39;49;00m$
   337	[37m    [39;49;00mwarnLevel[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&warnLevel,[37m[39;49;00m$
   338	[37m    [39;49;00mdieLevel[37m      [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&dieLevel,[37m[39;49;00m$
   339	[37m    [39;49;00mtkRunning[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&tkRunning,[37m[39;49;00m$
   340	[37m    [39;49;00mornaments[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&ornaments,[37m[39;49;00m$
   341	[37m    [39;49;00mRemotePort[37m    [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&RemotePort,[37m[39;49;00m$
   342	[37m    [39;49;00mDollarCaretP[37m  [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&DollarCaretP,[37m[39;49;00m$
   343	[37m    [39;49;00mOnlyAssertions=>[37m [39;49;00m[04m[91m\[39;49;00m&OnlyAssertions,[37m[39;49;00m$
   344	);[37m[39;49;00m$
   345	[37m[39;49;00m$
   346	=pod[37m[39;49;00m$
   347	[37m[39;49;00m$
   348	Last,[37m [39;49;00mthe[37m [39;49;00mC<[32m%option[39;49;00mRequire>[37m [39;49;00mnotes[37m [39;49;00mmodules[37m [39;49;00mthat[37m [39;49;00mmust[37m [39;49;00mbe[37m [39;49;00mC<require>d[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00man[37m[39;49;00m$
   349	option[37m [39;49;00mis[37m [39;49;00mused.[37m[39;49;00m$
   350	[37m[39;49;00m$
   351	=cut[37m[39;49;00m$
   352	[37m[39;49;00m$
   353	[36m#[39;49;00m[36m Note that this list is not complete: several options not listed here[39;49;00m[36m[39;49;00m$
   354	[36m#[39;49;00m[36m actually require that dumpvar.pl be loaded for them to work, but are[39;49;00m[36m[39;49;00m$
   355	[36m#[39;49;00m[36m not in the table. A subsequent patch will correct this problem; for[39;49;00m[36m[39;49;00m$
   356	[36m#[39;49;00m[36m the moment, we're just recommenting, and we are NOT going to change[39;49;00m[36m[39;49;00m$
   357	[36m#[39;49;00m[36m function.[39;49;00m[36m[39;49;00m$
   358	[32m%option[39;49;00mRequire[37m [39;49;00m=[37m [39;49;00m([37m[39;49;00m$
   359	[37m    [39;49;00mcompactDump[37m [39;49;00m=>[37m [39;49;00m[04m[91m'[39;49;00mdumpvar.pl[04m[91m'[39;49;00m,[37m[39;49;00m$
   360	[37m    [39;49;00mveryCompact[37m [39;49;00m=>[37m [39;49;00m[04m[91m'[39;49;00mdumpvar.pl[04m[91m'[39;49;00m,[37m[39;49;00m$
   361	[37m    [39;49;00mquote[37m       [39;49;00m=>[37m [39;49;00m[04m[91m'[39;49;00mdumpvar.pl[04m[91m'[39;49;00m,[37m[39;49;00m$
   362	);[37m[39;49;00m$
   363	[37m[39;49;00m$
   364	=pod[37m[39;49;00m$
   365	[37m[39;49;00m$
   366	There[37m [39;49;00mare[37m [39;49;00ma[37m [39;49;00mnumber[37m [39;49;00mof[37m [39;49;00minitialization-related[37m [39;49;00mvariables[37m [39;49;00mwhich[37m [39;49;00mcan[37m [39;49;00mbe[37m [39;49;00mset[37m[39;49;00m$
   367	by[37m [39;49;00mputting[37m [39;49;00mcode[37m [39;49;00mto[37m [39;49;00mset[37m [39;49;00mthem[37m [39;49;00min[37m [39;49;00ma[37m [39;49;00mBEGIN[37m [39;49;00mblock[37m [39;49;00min[37m [39;49;00mthe[37m [39;49;00mC<PERL5DB>[37m [39;49;00menvironment[37m[39;49;00m$
   368	variable.[37m [39;49;00mThese[37m [39;49;00mare:[37m[39;49;00m$
   369	[37m[39;49;00m$
   370	=over[37m [39;49;00m[34m4[39;49;00m[37m[39;49;00m$
   371	[37m[39;49;00m$
   372	=item[37m [39;49;00mC<$rl>[37m [39;49;00m-[37m [39;49;00mreadline[37m [39;49;00mcontrol[37m [39;49;00mXXX[37m [39;49;00mneeds[37m [39;49;00mmore[37m [39;49;00mexplanation[37m[39;49;00m$
   373	[37m[39;49;00m$
   374	=item[37m [39;49;00mC<$warnLevel>[37m [39;49;00m-[37m [39;49;00mwhether[37m [39;49;00mor[37m [39;49;00mnot[37m [39;49;00mdebugger[37m [39;49;00mtakes[37m [39;49;00mover[37m [39;49;00mwarning[37m [39;49;00mhandling[37m[39;49;00m$
   375	[37m[39;49;00m$
   376	=item[37m [39;49;00mC<$dieLevel>[37m [39;49;00m-[37m [39;49;00mwhether[37m [39;49;00mor[37m [39;49;00mnot[37m [39;49;00mdebugger[37m [39;49;00mtakes[37m [39;49;00mover[37m [39;49;00mdie[37m [39;49;00mhandling[37m[39;49;00m$
   377	[37m[39;49;00m$
   378	=item[37m [39;49;00mC<$signalLevel>[37m [39;49;00m-[37m [39;49;00mwhether[37m [39;49;00mor[37m [39;49;00mnot[37m [39;49;00mdebugger[37m [39;49;00mtakes[37m [39;49;00mover[37m [39;49;00msignal[37m [39;49;00mhandling[37m[39;49;00m$
   379	[37m[39;49;00m$
   380	=item[37m [39;49;00mC<$pre>[37m [39;49;00m-[37m [39;49;00mpreprompt[37m [39;49;00mactions[37m [39;49;00m(array[37m [39;49;00mreference)[37m[39;49;00m$
   381	[37m[39;49;00m$
   382	=item[37m [39;49;00mC<$post>[37m [39;49;00m-[37m [39;49;00mpostprompt[37m [39;49;00mactions[37m [39;49;00m(array[37m [39;49;00mreference)[37m[39;49;00m$
   383	[37m[39;49;00m$
   384	=item[37m [39;49;00mC<$pretype>[37m[39;49;00m$
   385	[37m[39;49;00m$
   386	=item[37m [39;49;00mC<$CreateTTY>[37m [39;49;00m-[37m [39;49;00mwhether[37m [39;49;00mor[37m [39;49;00mnot[37m [39;49;00mto[37m [39;49;00mcreate[37m [39;49;00ma[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mTTY[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00mdebugger[37m[39;49;00m$
   387	[37m[39;49;00m$
   388	=item[37m [39;49;00mC<$CommandSet>[37m [39;49;00m-[37m [39;49;00mwhich[37m [39;49;00mcommand[37m [39;49;00mset[37m [39;49;00mto[37m [39;49;00muse[37m [39;49;00m(defaults[37m [39;49;00mto[37m [39;49;00m[34mnew[39;49;00m,[37m [39;49;00mdocumented[37m [39;49;00mset)[37m[39;49;00m$
   389	[37m[39;49;00m$
   390	=back[37m[39;49;00m$
   391	[37m[39;49;00m$
   392	=cut[37m[39;49;00m$
   393	[37m[39;49;00m$
   394	[36m#[39;49;00m[36m These guys may be defined in $ENV{PERL5DB} :[39;49;00m[36m[39;49;00m$
   395	$rl[37m          [39;49;00m=[37m [39;49;00m[34m1[39;49;00m[37m     [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$rl;[37m[39;49;00m$
   396	$warnLevel[37m   [39;49;00m=[37m [39;49;00m[34m1[39;49;00m[37m     [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$warnLevel;[37m[39;49;00m$
   397	$dieLevel[37m    [39;49;00m=[37m [39;49;00m[34m1[39;49;00m[37m     [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$dieLevel;[37m[39;49;00m$
   398	$signalLevel[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m[37m     [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$signalLevel;[37m[39;49;00m$
   399	$pre[37m         [39;49;00m=[37m [39;49;00m[][37m    [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$pre;[37m[39;49;00m$
   400	$post[37m        [39;49;00m=[37m [39;49;00m[][37m    [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$post;[37m[39;49;00m$
   401	$pretype[37m     [39;49;00m=[37m [39;49;00m[][37m    [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$pretype;[37m[39;49;00m$
   402	$CreateTTY[37m   [39;49;00m=[37m [39;49;00m[34m3[39;49;00m[37m     [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$CreateTTY;[37m[39;49;00m$
   403	$CommandSet[37m  [39;49;00m=[37m [39;49;00m[04m[91m'[39;49;00m[34m580[39;49;00m[04m[91m'[39;49;00m[37m [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$CommandSet;[37m[39;49;00m$
   404	[37m[39;49;00m$
   405	share($rl);[37m[39;49;00m$
   406	share($warnLevel);[37m[39;49;00m$
   407	share($dieLevel);[37m[39;49;00m$
   408	share($signalLevel);[37m[39;49;00m$
   409	share($pre);[37m[39;49;00m$
   410	share($post);[37m[39;49;00m$
   411	share($pretype);[37m[39;49;00m$
   412	share($rl);[37m[39;49;00m$
   413	share($CreateTTY);[37m[39;49;00m$
   414	share($CommandSet);[37m[39;49;00m$
   415	[37m[39;49;00m$
   416	=pod[37m[39;49;00m$
   417	[37m[39;49;00m$
   418	The[37m [39;49;00m[34mdefault[39;49;00m[37m [39;49;00mC<die>,[37m [39;49;00mC<warn>,[37m [39;49;00mand[37m [39;49;00mC<signal>[37m [39;49;00mhandlers[37m [39;49;00mare[37m [39;49;00mset[37m [39;49;00mup.[37m[39;49;00m$
   419	[37m[39;49;00m$
   420	=cut[37m[39;49;00m$
   421	[37m[39;49;00m$
   422	warnLevel($warnLevel);[37m[39;49;00m$
   423	dieLevel($dieLevel);[37m[39;49;00m$
   424	signalLevel($signalLevel);[37m[39;49;00m$
   425	[37m[39;49;00m$
   426	=pod[37m[39;49;00m$
   427	[37m[39;49;00m$
   428	The[37m [39;49;00mpager[37m [39;49;00mto[37m [39;49;00mbe[37m [39;49;00mused[37m [39;49;00mis[37m [39;49;00mneeded[37m [39;49;00mnext.[37m [39;49;00mWe[37m [39;49;00m[34mtry[39;49;00m[37m [39;49;00mto[37m [39;49;00mget[37m [39;49;00mit[37m [39;49;00mfrom[37m [39;49;00mthe[37m[39;49;00m$
   429	environment[37m [39;49;00mfirst.[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00mit[04m[91m'[39;49;00ms[37m [39;49;00mnot[37m [39;49;00mdefined[37m [39;49;00mthere,[37m [39;49;00mwe[37m [39;49;00m[34mtry[39;49;00m[37m [39;49;00mto[37m [39;49;00mfind[37m [39;49;00mit[37m [39;49;00min[37m[39;49;00m$
   430	the[37m [39;49;00mPerl[37m [39;49;00mC<Config.pm>.[37m  [39;49;00mIf[37m [39;49;00mit[04m[91m'[39;49;00ms[37m [39;49;00mnot[37m [39;49;00mthere,[37m [39;49;00mwe[37m [39;49;00m[34mdefault[39;49;00m[37m [39;49;00mto[37m [39;49;00mC<more>.[37m [39;49;00mWe[37m[39;49;00m$
   431	then[37m [39;49;00mcall[37m [39;49;00mthe[37m [39;49;00mC<pager()>[37m [39;49;00mfunction[37m [39;49;00mto[37m [39;49;00msave[37m [39;49;00mthe[37m [39;49;00mpager[37m [39;49;00mname.[37m[39;49;00m$
   432	[37m[39;49;00m$
   433	=cut[37m[39;49;00m$
   434	[37m[39;49;00m$
   435	[36m#[39;49;00m[36m This routine makes sure $pager is set up so that '|' can use it.[39;49;00m[36m[39;49;00m$
   436	pager([37m[39;49;00m$
   437	[37m[39;49;00m$
   438	[37m    [39;49;00m[36m#[39;49;00m[36m If PAGER is defined in the environment, use it.[39;49;00m[36m[39;49;00m$
   439	[37m    [39;49;00mdefined[37m [39;49;00m$ENV{PAGER}[37m[39;49;00m$
   440	[37m    [39;49;00m?[37m [39;49;00m$ENV{PAGER}[37m[39;49;00m$
   441	[37m[39;49;00m$
   442	[37m      [39;49;00m[36m#[39;49;00m[36m If not, see if Config.pm defines it.[39;49;00m[36m[39;49;00m$
   443	[37m    [39;49;00m:[37m [39;49;00meval[37m [39;49;00m{[37m [39;49;00mrequire[37m [39;49;00mConfig[37m [39;49;00m}[37m[39;49;00m$
   444	[37m      [39;49;00m&&[37m [39;49;00mdefined[37m [39;49;00m$Config::Config{pager}[37m[39;49;00m$
   445	[37m    [39;49;00m?[37m [39;49;00m$Config::Config{pager}[37m[39;49;00m$
   446	[37m[39;49;00m$
   447	[37m      [39;49;00m[36m#[39;49;00m[36m If not, fall back to 'more'.[39;49;00m[36m[39;49;00m$
   448	[37m    [39;49;00m:[37m [39;49;00m[04m[91m'[39;49;00mmore[04m[91m'[39;49;00m[37m[39;49;00m$
   449	[37m  [39;49;00m)[37m[39;49;00m$
   450	[37m  [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$pager;[37m[39;49;00m$
   451	[37m[39;49;00m$
   452	=pod[37m[39;49;00m$
   453	[37m[39;49;00m$
   454	We[37m [39;49;00mset[37m [39;49;00mup[37m [39;49;00mthe[37m [39;49;00mcommand[37m [39;49;00mto[37m [39;49;00mbe[37m [39;49;00mused[37m [39;49;00mto[37m [39;49;00maccess[37m [39;49;00mthe[37m [39;49;00mman[37m [39;49;00mpages,[37m [39;49;00mthe[37m [39;49;00mcommand[37m[39;49;00m$
   455	recall[37m [39;49;00mcharacter[37m [39;49;00m(C<!>[37m [39;49;00munless[37m [39;49;00motherwise[37m [39;49;00mdefined)[37m [39;49;00mand[37m [39;49;00mthe[37m [39;49;00mshell[37m [39;49;00mescape[37m[39;49;00m$
   456	character[37m [39;49;00m(C<!>[37m [39;49;00munless[37m [39;49;00motherwise[37m [39;49;00mdefined).[37m [39;49;00mYes,[37m [39;49;00mthese[37m [39;49;00m[34mdo[39;49;00m[37m [39;49;00mconflict,[37m [39;49;00mand[37m[39;49;00m$
   457	neither[37m [39;49;00mworks[37m [39;49;00min[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mat[37m [39;49;00mthe[37m [39;49;00mmoment.[37m[39;49;00m$
   458	[37m[39;49;00m$
   459	=cut[37m[39;49;00m$
   460	[37m[39;49;00m$
   461	setman();[37m[39;49;00m$
   462	[37m[39;49;00m$
   463	[36m#[39;49;00m[36m Set up defaults for command recall and shell escape (note:[39;49;00m[36m[39;49;00m$
   464	[36m#[39;49;00m[36m these currently don't work in linemode debugging).[39;49;00m[36m[39;49;00m$
   465	&recallCommand([33m"[39;49;00m[33m![39;49;00m[33m"[39;49;00m)[37m [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$prc;[37m[39;49;00m$
   466	&shellBang([33m"[39;49;00m[33m![39;49;00m[33m"[39;49;00m)[37m     [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$psh;[37m[39;49;00m$
   467	[37m[39;49;00m$
   468	=pod[37m[39;49;00m$
   469	[37m[39;49;00m$
   470	We[37m [39;49;00mthen[37m [39;49;00mset[37m [39;49;00mup[37m [39;49;00mthe[37m [39;49;00mgigantic[37m [39;49;00mstring[37m [39;49;00mcontaining[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mhelp.[37m[39;49;00m$
   471	We[37m [39;49;00malso[37m [39;49;00mset[37m [39;49;00mthe[37m [39;49;00mlimit[37m [39;49;00mon[37m [39;49;00mthe[37m [39;49;00mnumber[37m [39;49;00mof[37m [39;49;00marguments[37m [39;49;00mwe[04m[91m'[39;49;00mll[37m [39;49;00mdisplay[37m [39;49;00mduring[37m [39;49;00ma[37m[39;49;00m$
   472	trace.[37m[39;49;00m$
   473	[37m[39;49;00m$
   474	=cut[37m[39;49;00m$
   475	[37m[39;49;00m$
   476	sethelp();[37m[39;49;00m$
   477	[37m[39;49;00m$
   478	[36m#[39;49;00m[36m If we didn't get a default for the length of eval[39;49;00m[36m/[39;49;00m[36mstack trace args,[39;49;00m[36m[39;49;00m$
   479	[36m#[39;49;00m[36m set it here.[39;49;00m[36m[39;49;00m$
   480	$maxtrace[37m [39;49;00m=[37m [39;49;00m[34m400[39;49;00m[37m [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$maxtrace;[37m[39;49;00m$
   481	[37m[39;49;00m$
   482	=head2[37m [39;49;00mSETTING[37m [39;49;00mUP[37m [39;49;00mTHE[37m [39;49;00mDEBUGGER[37m [39;49;00mGREETING[37m[39;49;00m$
   483	[37m[39;49;00m$
   484	The[37m [39;49;00mdebugger[37m [39;49;00mI<greeting>[37m [39;49;00mhelps[37m [39;49;00mto[37m [39;49;00minform[37m [39;49;00mthe[37m [39;49;00muser[37m [39;49;00mhow[37m [39;49;00mmany[37m [39;49;00mdebuggers[37m [39;49;00mare[37m[39;49;00m$
   485	running,[37m [39;49;00mand[37m [39;49;00mwhether[37m [39;49;00mthe[37m [39;49;00mcurrent[37m [39;49;00mdebugger[37m [39;49;00mis[37m [39;49;00mthe[37m [39;49;00mprimary[37m [39;49;00mor[37m [39;49;00ma[37m [39;49;00mchild.[37m[39;49;00m$
   486	[37m[39;49;00m$
   487	If[37m [39;49;00mwe[37m [39;49;00mare[37m [39;49;00mthe[37m [39;49;00mprimary,[37m [39;49;00mwe[37m [39;49;00mjust[37m [39;49;00mhang[37m [39;49;00monto[37m [39;49;00mour[37m [39;49;00mpid[37m [39;49;00mso[37m [39;49;00mwe[04m[91m'[39;49;00mll[37m [39;49;00mhave[37m [39;49;00mit[37m [39;49;00mwhen[37m[39;49;00m$
   488	or[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mwe[37m [39;49;00mstart[37m [39;49;00ma[37m [39;49;00mchild[37m [39;49;00mdebugger.[37m [39;49;00mIf[37m [39;49;00mwe[37m [39;49;00mare[37m [39;49;00ma[37m [39;49;00mchild,[37m [39;49;00mwe[04m[91m'[39;49;00mll[37m [39;49;00mset[37m [39;49;00mthings[37m [39;49;00mup[37m[39;49;00m$
   489	so[37m [39;49;00mwe[04m[91m'[39;49;00mll[37m [39;49;00mhave[37m [39;49;00ma[37m [39;49;00munique[37m [39;49;00mgreeting[37m [39;49;00mand[37m [39;49;00mso[37m [39;49;00mthe[37m [39;49;00mparent[37m [39;49;00mwill[37m [39;49;00mgive[37m [39;49;00mus[37m [39;49;00mour[37m [39;49;00mown[37m[39;49;00m$
   490	TTY[37m [39;49;00mlater.[37m[39;49;00m$
   491	[37m[39;49;00m$
   492	We[37m [39;49;00msave[37m [39;49;00mthe[37m [39;49;00mcurrent[37m [39;49;00mcontents[37m [39;49;00mof[37m [39;49;00mthe[37m [39;49;00mC<PERLDB_PIDS>[37m [39;49;00menvironment[37m [39;49;00mvariable[37m[39;49;00m$
   493	because[37m [39;49;00mwe[37m [39;49;00mmess[37m [39;49;00maround[37m [39;49;00mwith[37m [39;49;00mit.[37m [39;49;00mWe[04m[91m'[39;49;00mll[37m [39;49;00malso[37m [39;49;00mneed[37m [39;49;00mto[37m [39;49;00mhang[37m [39;49;00monto[37m [39;49;00mit[37m [39;49;00mbecause[37m[39;49;00m$
   494	we[04m[91m'[39;49;00mll[37m [39;49;00mneed[37m [39;49;00mit[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mwe[37m [39;49;00mrestart.[37m[39;49;00m$
   495	[37m[39;49;00m$
   496	Child[37m [39;49;00mdebuggers[37m [39;49;00mmake[37m [39;49;00ma[37m [39;49;00mlabel[37m [39;49;00mout[37m [39;49;00mof[37m [39;49;00mthe[37m [39;49;00mcurrent[37m [39;49;00mPID[37m [39;49;00mstructure[37m [39;49;00mrecorded[37m [39;49;00min[37m[39;49;00m$
   497	PERLDB_PIDS[37m [39;49;00mplus[37m [39;49;00mthe[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPID.[37m [39;49;00mThey[37m [39;49;00malso[37m [39;49;00mmark[37m [39;49;00mthemselves[37m [39;49;00mas[37m [39;49;00mnot[37m [39;49;00mhaving[37m [39;49;00ma[37m [39;49;00mTTY[37m[39;49;00m$
   498	yet[37m [39;49;00mso[37m [39;49;00mthe[37m [39;49;00mparent[37m [39;49;00mwill[37m [39;49;00mgive[37m [39;49;00mthem[37m [39;49;00mone[37m [39;49;00mlater[37m [39;49;00mvia[37m [39;49;00mC<resetterm()>.[37m[39;49;00m$
   499	[37m[39;49;00m$
   500	=cut[37m[39;49;00m$
   501	[37m[39;49;00m$
   502	[36m#[39;49;00m[36m Save the current contents of the environment; we're about to[39;49;00m[36m[39;49;00m$
   503	[36m#[39;49;00m[36m much with it. We'll need this if we have to restart.[39;49;00m[36m[39;49;00m$
   504	$ini_pids[37m [39;49;00m=[37m [39;49;00m$ENV{PERLDB_PIDS};[37m[39;49;00m$
   505	[37m[39;49;00m$
   506	[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00mdefined[37m [39;49;00m$ENV{PERLDB_PIDS}[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   507	[37m[39;49;00m$
   508	[37m    [39;49;00m[36m#[39;49;00m[36m We're a child. Make us a label out of the current PID structure[39;49;00m[36m[39;49;00m$
   509	[37m    [39;49;00m[36m#[39;49;00m[36m recorded in PERLDB_PIDS plus our (new) PID. Mark us as not having[39;49;00m[36m[39;49;00m$
   510	[37m    [39;49;00m[36m#[39;49;00m[36m a term yet so the parent will give us one later via resetterm().[39;49;00m[36m[39;49;00m$
   511	[37m    [39;49;00m$pids[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m[$ENV{PERLDB_PIDS}][39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   512	[37m    [39;49;00m$ENV{PERLDB_PIDS}[37m [39;49;00m.=[37m [39;49;00m[33m"[39;49;00m[33m->$$[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   513	[37m    [39;49;00m$term_pid[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
   514	}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(defined[37m [39;49;00m$ENV{PERLDB_PIDS...[37m[39;49;00m$
   515	[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
   516	[37m[39;49;00m$
   517	[37m    [39;49;00m[36m#[39;49;00m[36m We're the parent PID. Initialize PERLDB_PID in case we end up with a[39;49;00m[36m[39;49;00m$
   518	[37m    [39;49;00m[36m#[39;49;00m[36m child debugger, and mark us as the parent, so we'll know to set up[39;49;00m[36m[39;49;00m$
   519	[37m    [39;49;00m[36m#[39;49;00m[36m more TTY's is we have to.[39;49;00m[36m[39;49;00m$
   520	[37m    [39;49;00m$ENV{PERLDB_PIDS}[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m$$[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   521	[37m    [39;49;00m$pids[37m             [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m{pid=$$}[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   522	[37m    [39;49;00m$term_pid[37m         [39;49;00m=[37m [39;49;00m$$;[37m[39;49;00m$
   523	}[37m[39;49;00m$
   524	[37m[39;49;00m$
   525	$pidprompt[37m [39;49;00m=[37m [39;49;00m[04m[91m'[39;49;00m[04m[91m'[39;49;00m;[37m[39;49;00m$
   526	[37m[39;49;00m$
   527	[36m#[39;49;00m[36m Sets up $emacs as a synonym for $slave_editor.[39;49;00m[36m[39;49;00m$
   528	*emacs[37m [39;49;00m=[37m [39;49;00m$slave_editor[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m$slave_editor;[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mMay[37m [39;49;00mbe[37m [39;49;00mused[37m [39;49;00min[37m [39;49;00mafterinit()...[37m[39;49;00m$
   529	[37m[39;49;00m$
   530	=head2[37m [39;49;00mREADING[37m [39;49;00mTHE[37m [39;49;00mRC[37m [39;49;00m[36mFILE[39;49;00m[37m[39;49;00m$
   531	[37m[39;49;00m$
   532	The[37m [39;49;00mdebugger[37m [39;49;00mwill[37m [39;49;00mread[37m [39;49;00ma[37m [39;49;00mfile[37m [39;49;00mof[37m [39;49;00minitialization[37m [39;49;00moptions[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00msupplied.[37m [39;49;00mIf[37m    [39;49;00m[37m[39;49;00m$
   533	running[37m [39;49;00minteractively,[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00mis[37m [39;49;00mC<.perldb>;[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mnot,[37m [39;49;00mit[04m[91m'[39;49;00ms[37m [39;49;00mC<perldb.ini>.[37m[39;49;00m$
   534	[37m[39;49;00m$
   535	=cut[37m      [39;49;00m[37m[39;49;00m$
   536	[37m[39;49;00m$
   537	[36m#[39;49;00m[36m As noted, this test really doesn't check accurately that the debugger[39;49;00m[36m[39;49;00m$
   538	[36m#[39;49;00m[36m is running at a terminal or not.[39;49;00m[36m[39;49;00m$
   539	[37m[39;49;00m$
   540	[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m-e[37m [39;49;00m[33m"[39;49;00m[33m/dev/tty[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m                      [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00mis[37m [39;49;00mthe[37m [39;49;00mwrong[37m [39;49;00mmetric![37m[39;49;00m$
   541	[37m    [39;49;00m$rcfile[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m.perldb[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   542	}[37m[39;49;00m$
   543	[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
   544	[37m    [39;49;00m$rcfile[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mperldb.ini[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   545	}[37m[39;49;00m$
   546	[37m[39;49;00m$
   547	=pod[37m[39;49;00m$
   548	[37m[39;49;00m$
   549	The[37m [39;49;00mdebugger[37m [39;49;00mdoes[37m [39;49;00ma[37m [39;49;00msafety[37m [39;49;00mtest[37m [39;49;00mof[37m [39;49;00mthe[37m [39;49;00mfile[37m [39;49;00mto[37m [39;49;00mbe[37m [39;49;00mread.[37m [39;49;00mIt[37m [39;49;00mmust[37m [39;49;00mbe[37m [39;49;00mowned[37m[39;49;00m$
   550	either[37m [39;49;00mby[37m [39;49;00mthe[37m [39;49;00mcurrent[37m [39;49;00muser[37m [39;49;00mor[37m [39;49;00mroot,[37m [39;49;00mand[37m [39;49;00mmust[37m [39;49;00monly[37m [39;49;00mbe[37m [39;49;00mwritable[37m [39;49;00mby[37m [39;49;00mthe[37m [39;49;00mowner.[37m[39;49;00m$
   551	[37m[39;49;00m$
   552	=cut[37m[39;49;00m$
   553	[37m[39;49;00m$
   554	[36m#[39;49;00m[36m This wraps a safety test around "do" to read and evaluate the init file.[39;49;00m[36m[39;49;00m$
   555	[36m#[39;49;00m[36m[39;49;00m$
   556	[36m#[39;49;00m[36m This isn't really safe, because there's a race[39;49;00m[36m[39;49;00m$
   557	[36m#[39;49;00m[36m between checking and opening.  The solution is to[39;49;00m[36m[39;49;00m$
   558	[36m#[39;49;00m[36m open and fstat the handle, but then you have to read and[39;49;00m[36m[39;49;00m$
   559	[36m#[39;49;00m[36m eval the contents.  But then the silly thing gets[39;49;00m[36m[39;49;00m$
   560	[36m#[39;49;00m[36m your lexical scope, which is unfortunate at best.[39;49;00m[36m[39;49;00m$
   561	sub[37m [39;49;00msafe_do[37m [39;49;00m{[37m[39;49;00m$
   562	[37m    [39;49;00mmy[37m [39;49;00m$file[37m [39;49;00m=[37m [39;49;00mshift;[37m[39;49;00m$
   563	[37m[39;49;00m$
   564	[37m    [39;49;00m[36m#[39;49;00m[36m Just exactly what part of the word "CORE::" don't you understand?[39;49;00m[36m[39;49;00m$
   565	[37m    [39;49;00mlocal[37m [39;49;00m$SIG{__WARN__};[37m[39;49;00m$
   566	[37m    [39;49;00mlocal[37m [39;49;00m$SIG{__DIE__};[37m[39;49;00m$
   567	[37m[39;49;00m$
   568	[37m    [39;49;00munless[37m [39;49;00m([37m [39;49;00mis_safe_file($file)[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   569	[37m        [39;49;00mCORE::warn[37m [39;49;00m<<EO_GRIPE;[37m[39;49;00m$
   570	perldb:[37m [39;49;00mMust[37m [39;49;00mnot[37m [39;49;00msource[37m [39;49;00minsecure[37m [39;49;00mrcfile[37m [39;49;00m$file.[37m[39;49;00m$
   571	[37m        [39;49;00mYou[37m [39;49;00mor[37m [39;49;00mthe[37m [39;49;00msuperuser[37m [39;49;00mmust[37m [39;49;00mbe[37m [39;49;00mthe[37m [39;49;00mowner,[37m [39;49;00mand[37m [39;49;00mit[37m [39;49;00mmust[37m [39;49;00mnot[37m [39;49;00m[37m[39;49;00m$
   572	[37m        [39;49;00mbe[37m [39;49;00mwritable[37m [39;49;00mby[37m [39;49;00manyone[37m [39;49;00mbut[37m [39;49;00mits[37m [39;49;00mowner.[37m[39;49;00m$
   573	EO_GRIPE[37m[39;49;00m$
   574	[37m        [39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
   575	[37m    [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00munless[37m [39;49;00m(is_safe_file($file...[37m[39;49;00m$
   576	[37m[39;49;00m$
   577	[37m    [39;49;00m[34mdo[39;49;00m[37m [39;49;00m$file;[37m[39;49;00m$
   578	[37m    [39;49;00mCORE::warn([33m"[39;49;00m[33mperldb: couldn't parse $file: $@[39;49;00m[33m"[39;49;00m)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m$[04m[91m@[39;49;00m;[37m[39;49;00m$
   579	}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00msub[37m [39;49;00msafe_do[37m[39;49;00m$
   580	[37m[39;49;00m$
   581	[36m#[39;49;00m[36m This is the safety test itself.[39;49;00m[36m[39;49;00m$
   582	[36m#[39;49;00m[36m[39;49;00m$
   583	[36m#[39;49;00m[36m Verifies that owner is either real user or superuser and that no[39;49;00m[36m[39;49;00m$
   584	[36m#[39;49;00m[36m one but owner may write to it.  This function is of limited use[39;49;00m[36m[39;49;00m$
   585	[36m#[39;49;00m[36m when called on a path instead of upon a handle, because there are[39;49;00m[36m[39;49;00m$
   586	[36m#[39;49;00m[36m no guarantees that filename (by dirent) whose file (by ino) is[39;49;00m[36m[39;49;00m$
   587	[36m#[39;49;00m[36m eventually accessed is the same as the one tested.[39;49;00m[36m[39;49;00m$
   588	[36m#[39;49;00m[36m Assumes that the file's existence is not in doubt.[39;49;00m[36m[39;49;00m$
   589	sub[37m [39;49;00mis_safe_file[37m [39;49;00m{[37m[39;49;00m$
   590	[37m    [39;49;00mmy[37m [39;49;00m$path[37m [39;49;00m=[37m [39;49;00mshift;[37m[39;49;00m$
   591	[37m    [39;49;00mstat($path)[37m [39;49;00m||[37m [39;49;00m[34mreturn[39;49;00m;[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mmysteriously[37m [39;49;00mvaporized[37m[39;49;00m$
   592	[37m    [39;49;00mmy[37m [39;49;00m([37m [39;49;00m$dev,[37m [39;49;00m$ino,[37m [39;49;00m$mode,[37m [39;49;00m$nlink,[37m [39;49;00m$uid,[37m [39;49;00m$gid[37m [39;49;00m)[37m [39;49;00m=[37m [39;49;00mstat(_);[37m[39;49;00m$
   593	[37m[39;49;00m$
   594	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m$uid[37m [39;49;00m!=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m$uid[37m [39;49;00m!=[37m [39;49;00m$<;[37m[39;49;00m$
   595	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m$mode[37m [39;49;00m&[37m [39;49;00m[34m022[39;49;00m;[37m[39;49;00m$
   596	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
   597	}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00msub[37m [39;49;00mis_safe_file[37m[39;49;00m$
   598	[37m[39;49;00m$
   599	[36m#[39;49;00m[36m If the rcfile (whichever one we decided was the right one to read)[39;49;00m[36m[39;49;00m$
   600	[36m#[39;49;00m[36m exists, we safely do it.[39;49;00m[36m[39;49;00m$
   601	[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m-f[37m [39;49;00m$rcfile[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   602	[37m    [39;49;00msafe_do([33m"[39;49;00m[33m./$rcfile[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   603	}[37m[39;49;00m$
   604	[37m[39;49;00m$
   605	[36m#[39;49;00m[36m If there isn't one here, try the user's home directory.[39;49;00m[36m[39;49;00m$
   606	elsif[37m [39;49;00m([37m [39;49;00mdefined[37m [39;49;00m$ENV{HOME}[37m [39;49;00m&&[37m [39;49;00m-f[37m [39;49;00m[33m"[39;49;00m[33m$ENV{HOME}/$rcfile[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   607	[37m    [39;49;00msafe_do([33m"[39;49;00m[33m$ENV{HOME}/$rcfile[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   608	}[37m[39;49;00m$
   609	[37m[39;49;00m$
   610	[36m#[39;49;00m[36m Else try the login directory.[39;49;00m[36m[39;49;00m$
   611	elsif[37m [39;49;00m([37m [39;49;00mdefined[37m [39;49;00m$ENV{LOGDIR}[37m [39;49;00m&&[37m [39;49;00m-f[37m [39;49;00m[33m"[39;49;00m[33m$ENV{LOGDIR}/$rcfile[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   612	[37m    [39;49;00msafe_do([33m"[39;49;00m[33m$ENV{LOGDIR}/$rcfile[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   613	}[37m[39;49;00m$
   614	[37m[39;49;00m$
   615	[36m#[39;49;00m[36m If the PERLDB_OPTS variable has options in it, parse those out next.[39;49;00m[36m[39;49;00m$
   616	[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00mdefined[37m [39;49;00m$ENV{PERLDB_OPTS}[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   617	[37m    [39;49;00mparse_options([37m [39;49;00m$ENV{PERLDB_OPTS}[37m [39;49;00m);[37m[39;49;00m$
   618	}[37m[39;49;00m$
   619	[37m[39;49;00m$
   620	=pod[37m[39;49;00m$
   621	[37m[39;49;00m$
   622	The[37m [39;49;00mlast[37m [39;49;00mthing[37m [39;49;00mwe[37m [39;49;00m[34mdo[39;49;00m[37m [39;49;00mduring[37m [39;49;00minitialization[37m [39;49;00mis[37m [39;49;00mdetermine[37m [39;49;00mwhich[37m [39;49;00msubroutine[37m [39;49;00mis[37m[39;49;00m$
   623	to[37m [39;49;00mbe[37m [39;49;00mused[37m [39;49;00mto[37m [39;49;00mobtain[37m [39;49;00ma[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mterminal[37m [39;49;00mwhen[37m [39;49;00ma[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mdebugger[37m [39;49;00mis[37m [39;49;00mstarted.[37m [39;49;00mRight[37m [39;49;00mnow,[37m[39;49;00m$
   624	the[37m [39;49;00mdebugger[37m [39;49;00monly[37m [39;49;00mhandles[37m [39;49;00mX[37m [39;49;00mWindows[37m [39;49;00mand[37m [39;49;00mOS/[34m2.[39;49;00m[37m[39;49;00m$
   625	[37m[39;49;00m$
   626	=cut[37m[39;49;00m$
   627	[37m[39;49;00m$
   628	[36m#[39;49;00m[36m Set up the get_fork_TTY subroutine to be aliased to the proper routine.[39;49;00m[36m[39;49;00m$
   629	[36m#[39;49;00m[36m Works if you're running an xterm or xterm-like window, or you're on[39;49;00m[36m[39;49;00m$
   630	[36m#[39;49;00m[36m OS[39;49;00m[36m/[39;49;00m[36m2. This may need some expansion: for instance, this doesn't handle[39;49;00m[36m[39;49;00m$
   631	[36m#[39;49;00m[36m OS X Terminal windows.[39;49;00m[36m[39;49;00m$
   632	[37m[39;49;00m$
   633	[34mif[39;49;00m[37m [39;49;00m([37m[39;49;00m$
   634	[37m    [39;49;00mnot[37m [39;49;00mdefined[37m [39;49;00m&get_fork_TTY[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mno[37m [39;49;00mroutine[37m [39;49;00mexists,[37m[39;49;00m$
   635	[37m    [39;49;00mand[37m [39;49;00mdefined[37m [39;49;00m$ENV{TERM}[37m       [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mand[37m [39;49;00mwe[37m [39;49;00mknow[37m [39;49;00mwhat[37m [39;49;00mkind[37m[39;49;00m$
   636	[37m                                 [39;49;00m[36m#[39;49;00m[36m of terminal this is,[39;49;00m[36m[39;49;00m$
   637	[37m    [39;49;00mand[37m [39;49;00m$ENV{TERM}[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mxterm[04m[91m'[39;49;00m[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mand[37m [39;49;00mit[04m[91m'[39;49;00ms[37m [39;49;00man[37m [39;49;00mxterm,[37m[39;49;00m$
   638	[36m#[39;49;00m[36m   and defined $ENV{WINDOWID}   # and we know what window this is, <- wrong metric[39;49;00m[36m[39;49;00m$
   639	[37m    [39;49;00mand[37m [39;49;00mdefined[37m [39;49;00m$ENV{DISPLAY}[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mand[37m [39;49;00mwhat[37m [39;49;00mdisplay[37m [39;49;00mit[04m[91m'[39;49;00ms[37m [39;49;00mon,[37m[39;49;00m$
   640	[37m  [39;49;00m)[37m[39;49;00m$
   641	{[37m[39;49;00m$
   642	[37m    [39;49;00m*get_fork_TTY[37m [39;49;00m=[37m [39;49;00m[04m[91m\[39;49;00m&xterm_get_fork_TTY;[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00muse[37m [39;49;00mthe[37m [39;49;00mxterm[37m [39;49;00mversion[37m[39;49;00m$
   643	}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(not[37m [39;49;00mdefined[37m [39;49;00m&get_fork_TTY...[37m[39;49;00m$
   644	elsif[37m [39;49;00m([37m [39;49;00m$^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mos2[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m                     [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mIf[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00mis[37m [39;49;00mOS/[34m2[39;49;00m,[37m[39;49;00m$
   645	[37m    [39;49;00m*get_fork_TTY[37m [39;49;00m=[37m [39;49;00m[04m[91m\[39;49;00m&os2_get_fork_TTY;[37m      [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00muse[37m [39;49;00mthe[37m [39;49;00mOS/[34m2[39;49;00m[37m [39;49;00mversion[37m[39;49;00m$
   646	}[37m[39;49;00m$
   647	[37m[39;49;00m$
   648	[36m#[39;49;00m[36m untaint $^O, which may have been tainted by the last statement.[39;49;00m[36m[39;49;00m$
   649	[36m#[39;49;00m[36m see bug [perl #24674][39;49;00m[36m[39;49;00m$
   650	$^O[37m [39;49;00m=~[37m [39;49;00mm/^(.*)[04m[91m\[39;49;00mz/;[37m[39;49;00m$
   651	$^O[37m [39;49;00m=[37m [39;49;00m$1;[37m[39;49;00m$
   652	[37m[39;49;00m$
   653	[36m#[39;49;00m[36m Here begin the unreadable code.  It needs fixing.[39;49;00m[36m[39;49;00m$
   654	[37m[39;49;00m$
   655	=head2[37m [39;49;00mRESTART[37m [39;49;00mPROCESSING[37m[39;49;00m$
   656	[37m[39;49;00m$
   657	This[37m [39;49;00msection[37m [39;49;00mhandles[37m [39;49;00mthe[37m [39;49;00mrestart[37m [39;49;00mcommand.[37m [39;49;00mWhen[37m [39;49;00mthe[37m [39;49;00mC<R>[37m [39;49;00mcommand[37m [39;49;00mis[37m [39;49;00minvoked,[37m [39;49;00mit[37m[39;49;00m$
   658	tries[37m [39;49;00mto[37m [39;49;00mcapture[37m [39;49;00mall[37m [39;49;00mof[37m [39;49;00mthe[37m [39;49;00mstate[37m [39;49;00mit[37m [39;49;00mcan[37m [39;49;00minto[37m [39;49;00menvironment[37m [39;49;00mvariables,[37m [39;49;00mand[37m[39;49;00m$
   659	then[37m [39;49;00msets[37m [39;49;00mC<PERLDB_RESTART>.[37m [39;49;00mWhen[37m [39;49;00mwe[37m [39;49;00mstart[37m [39;49;00mexecuting[37m [39;49;00magain,[37m [39;49;00mwe[37m [39;49;00mcheck[37m [39;49;00mto[37m [39;49;00msee[37m[39;49;00m$
   660	[34mif[39;49;00m[37m [39;49;00mC<PERLDB_RESTART>[37m [39;49;00mis[37m [39;49;00mthere;[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mso,[37m [39;49;00mwe[37m [39;49;00mreload[37m [39;49;00mall[37m [39;49;00mthe[37m [39;49;00minformation[37m [39;49;00mthat[37m[39;49;00m$
   661	the[37m [39;49;00mR[37m [39;49;00mcommand[37m [39;49;00mstuffed[37m [39;49;00minto[37m [39;49;00mthe[37m [39;49;00menvironment[37m [39;49;00mvariables.[37m[39;49;00m$
   662	[37m[39;49;00m$
   663	[37m  [39;49;00mPERLDB_RESTART[37m   [39;49;00m-[37m [39;49;00mflag[37m [39;49;00monly,[37m [39;49;00mcontains[37m [39;49;00mno[37m [39;49;00mrestart[37m [39;49;00mdata[37m [39;49;00mitself.[37m       [39;49;00m[37m[39;49;00m$
   664	[37m  [39;49;00mPERLDB_HIST[37m      [39;49;00m-[37m [39;49;00mcommand[37m [39;49;00mhistory,[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mit[04m[91m'[39;49;00ms[37m [39;49;00mavailable[37m[39;49;00m$
   665	[37m  [39;49;00mPERLDB_ON_LOAD[37m   [39;49;00m-[37m [39;49;00mbreakpoints[37m [39;49;00mset[37m [39;49;00mby[37m [39;49;00mthe[37m [39;49;00mrc[37m [39;49;00mfile[37m[39;49;00m$
   666	[37m  [39;49;00mPERLDB_POSTPONE[37m  [39;49;00m-[37m [39;49;00msubs[37m [39;49;00mthat[37m [39;49;00mhave[37m [39;49;00mbeen[37m [39;49;00mloaded/not[37m [39;49;00mexecuted,[37m [39;49;00mand[37m [39;49;00mhave[37m [39;49;00mactions[37m[39;49;00m$
   667	[37m  [39;49;00mPERLDB_VISITED[37m   [39;49;00m-[37m [39;49;00mfiles[37m [39;49;00mthat[37m [39;49;00mhad[37m [39;49;00mbreakpoints[37m[39;49;00m$
   668	[37m  [39;49;00mPERLDB_FILE_...[37m  [39;49;00m-[37m [39;49;00mbreakpoints[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00ma[37m [39;49;00mfile[37m[39;49;00m$
   669	[37m  [39;49;00mPERLDB_OPT[37m       [39;49;00m-[37m [39;49;00mactive[37m [39;49;00moptions[37m[39;49;00m$
   670	[37m  [39;49;00mPERLDB_INC[37m       [39;49;00m-[37m [39;49;00mthe[37m [39;49;00moriginal[37m [39;49;00m[04m[91m@[39;49;00mINC[37m[39;49;00m$
   671	[37m  [39;49;00mPERLDB_PRETYPE[37m   [39;49;00m-[37m [39;49;00mpreprompt[37m [39;49;00mdebugger[37m [39;49;00mactions[37m[39;49;00m$
   672	[37m  [39;49;00mPERLDB_PRE[37m       [39;49;00m-[37m [39;49;00mpreprompt[37m [39;49;00mPerl[37m [39;49;00mcode[37m[39;49;00m$
   673	[37m  [39;49;00mPERLDB_POST[37m      [39;49;00m-[37m [39;49;00mpost-prompt[37m [39;49;00mPerl[37m [39;49;00mcode[37m[39;49;00m$
   674	[37m  [39;49;00mPERLDB_TYPEAHEAD[37m [39;49;00m-[37m [39;49;00mtypeahead[37m [39;49;00mcaptured[37m [39;49;00mby[37m [39;49;00mreadline()[37m[39;49;00m$
   675	[37m[39;49;00m$
   676	We[37m [39;49;00mchug[37m [39;49;00mthrough[37m [39;49;00mall[37m [39;49;00mthese[37m [39;49;00mvariables[37m [39;49;00mand[37m [39;49;00mplug[37m [39;49;00mthe[37m [39;49;00mvalues[37m [39;49;00msaved[37m [39;49;00min[37m [39;49;00mthem[37m[39;49;00m$
   677	back[37m [39;49;00minto[37m [39;49;00mthe[37m [39;49;00mappropriate[37m [39;49;00mspots[37m [39;49;00min[37m [39;49;00mthe[37m [39;49;00mdebugger.[37m[39;49;00m$
   678	[37m[39;49;00m$
   679	=cut[37m[39;49;00m$
   680	[37m[39;49;00m$
   681	[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00mexists[37m [39;49;00m$ENV{PERLDB_RESTART}[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   682	[37m[39;49;00m$
   683	[37m    [39;49;00m[36m#[39;49;00m[36m We're restarting, so we don't need the flag that says to restart anymore.[39;49;00m[36m[39;49;00m$
   684	[37m    [39;49;00m[34mdelete[39;49;00m[37m [39;49;00m$ENV{PERLDB_RESTART};[37m[39;49;00m$
   685	[37m[39;49;00m$
   686	[37m    [39;49;00m[36m#[39;49;00m[36m $restart = 1;[39;49;00m[36m[39;49;00m$
   687	[37m    [39;49;00m[04m[91m@[39;49;00mhist[37m          [39;49;00m=[37m [39;49;00mget_list([04m[91m'[39;49;00mPERLDB_HIST[04m[91m'[39;49;00m);[37m[39;49;00m$
   688	[37m    [39;49;00m[32m%break_on_load[39;49;00m[37m [39;49;00m=[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_ON_LOAD[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   689	[37m    [39;49;00m[32m%postponed[39;49;00m[37m     [39;49;00m=[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_POSTPONE[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   690	[37m[39;49;00m$
   691	[37m	[39;49;00mshare([04m[91m@[39;49;00mhist);[37m[39;49;00m$
   692	[37m	[39;49;00mshare([04m[91m@[39;49;00mtruehist);[37m[39;49;00m$
   693	[37m	[39;49;00mshare([32m%break_on_load[39;49;00m);[37m[39;49;00m$
   694	[37m	[39;49;00mshare([32m%postponed[39;49;00m);[37m[39;49;00m$
   695	[37m[39;49;00m$
   696	[37m    [39;49;00m[36m#[39;49;00m[36m restore breakpoints[39;49;00m[36m/[39;49;00m[36mactions[39;49;00m[36m[39;49;00m$
   697	[37m    [39;49;00mmy[37m [39;49;00m[04m[91m@[39;49;00mhad_breakpoints[37m [39;49;00m=[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_VISITED[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   698	[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m..[37m [39;49;00m$[36m#had_breakpoints[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   699	[37m        [39;49;00mmy[37m [39;49;00m[32m%pf[39;49;00m[37m [39;49;00m=[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_FILE_$_[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   700	[37m        [39;49;00m$postponed_file{[37m [39;49;00m$had_breakpoints[$_][37m [39;49;00m}[37m [39;49;00m=[37m [39;49;00m[04m[91m\[39;49;00m[32m%pf[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m[32m%pf[39;49;00m;[37m[39;49;00m$
   701	[37m    [39;49;00m}[37m[39;49;00m$
   702	[37m[39;49;00m$
   703	[37m    [39;49;00m[36m#[39;49;00m[36m restore options[39;49;00m[36m[39;49;00m$
   704	[37m    [39;49;00mmy[37m [39;49;00m[32m%opt[39;49;00m[37m [39;49;00m=[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_OPT[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   705	[37m    [39;49;00mmy[37m [39;49;00m([37m [39;49;00m$opt,[37m [39;49;00m$val[37m [39;49;00m);[37m[39;49;00m$
   706	[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m([37m [39;49;00m([37m [39;49;00m$opt,[37m [39;49;00m$val[37m [39;49;00m)[37m [39;49;00m=[37m [39;49;00meach[37m [39;49;00m[32m%opt[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   707	[37m        [39;49;00m$val[37m [39;49;00m=~[37m [39;49;00ms/[[04m[91m\[39;49;00m[04m[91m\[39;49;00m[04m[91m\[39;49;00m[04m[91m'[39;49;00m]/[04m[91m\[39;49;00m[04m[91m\[39;49;00m$1/g;[37m[39;49;00m$
   708	[37m        [39;49;00mparse_options([33m"[39;49;00m[33m$opt'$val'[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   709	[37m    [39;49;00m}[37m[39;49;00m$
   710	[37m[39;49;00m$
   711	[37m    [39;49;00m[36m#[39;49;00m[36m restore original @INC[39;49;00m[36m[39;49;00m$
   712	[37m    [39;49;00m[04m[91m@[39;49;00mINC[37m     [39;49;00m=[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_INC[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   713	[37m    [39;49;00m[04m[91m@[39;49;00mini_INC[37m [39;49;00m=[37m [39;49;00m[04m[91m@[39;49;00mINC;[37m[39;49;00m$
   714	[37m[39;49;00m$
   715	[37m    [39;49;00m[36m#[39;49;00m[36m return pre[39;49;00m[36m/[39;49;00m[36mpostprompt actions and typeahead buffer[39;49;00m[36m[39;49;00m$
   716	[37m    [39;49;00m$pretype[37m   [39;49;00m=[37m [39;49;00m[[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_PRETYPE[39;49;00m[33m"[39;49;00m)[37m [39;49;00m];[37m[39;49;00m$
   717	[37m    [39;49;00m$pre[37m       [39;49;00m=[37m [39;49;00m[[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_PRE[39;49;00m[33m"[39;49;00m)[37m [39;49;00m];[37m[39;49;00m$
   718	[37m    [39;49;00m$post[37m      [39;49;00m=[37m [39;49;00m[[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_POST[39;49;00m[33m"[39;49;00m)[37m [39;49;00m];[37m[39;49;00m$
   719	[37m    [39;49;00m[04m[91m@[39;49;00mtypeahead[37m [39;49;00m=[37m [39;49;00mget_list([37m [39;49;00m[33m"[39;49;00m[33mPERLDB_TYPEAHEAD[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[04m[91m@[39;49;00mtypeahead[37m [39;49;00m);[37m[39;49;00m$
   720	}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(exists[37m [39;49;00m$ENV{PERLDB_RESTART...[37m[39;49;00m$
   721	[37m[39;49;00m$
   722	=head2[37m [39;49;00mSETTING[37m [39;49;00mUP[37m [39;49;00mTHE[37m [39;49;00mTERMINAL[37m[39;49;00m$
   723	[37m[39;49;00m$
   724	Now,[37m [39;49;00mwe[04m[91m'[39;49;00mll[37m [39;49;00mdecide[37m [39;49;00mhow[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mis[37m [39;49;00mgoing[37m [39;49;00mto[37m [39;49;00minteract[37m [39;49;00mwith[37m [39;49;00mthe[37m [39;49;00muser.[37m[39;49;00m$
   725	If[37m [39;49;00mthere[04m[91m'[39;49;00ms[37m [39;49;00mno[37m [39;49;00mTTY,[37m [39;49;00mwe[37m [39;49;00mset[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mto[37m [39;49;00mrun[37m [39;49;00mnon-stop;[37m [39;49;00mthere[04m[91m'[39;49;00ms[37m [39;49;00mnot[37m [39;49;00mgoing[37m[39;49;00m$
   726	to[37m [39;49;00mbe[37m [39;49;00manyone[37m [39;49;00mthere[37m [39;49;00mto[37m [39;49;00menter[37m [39;49;00mcommands.[37m[39;49;00m$
   727	[37m[39;49;00m$
   728	=cut[37m[39;49;00m$
   729	[37m[39;49;00m$
   730	[34mif[39;49;00m[37m [39;49;00m($notty)[37m [39;49;00m{[37m[39;49;00m$
   731	[37m    [39;49;00m$runnonstop[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
   732	[37m	[39;49;00mshare($runnonstop);[37m[39;49;00m$
   733	}[37m[39;49;00m$
   734	[37m[39;49;00m$
   735	=pod[37m[39;49;00m$
   736	[37m[39;49;00m$
   737	If[37m [39;49;00mthere[37m [39;49;00mis[37m [39;49;00ma[37m [39;49;00mTTY,[37m [39;49;00mwe[37m [39;49;00mhave[37m [39;49;00mto[37m [39;49;00mdetermine[37m [39;49;00mwho[37m [39;49;00mit[37m [39;49;00mbelongs[37m [39;49;00mto[37m [39;49;00mbefore[37m [39;49;00mwe[37m [39;49;00mcan[37m[39;49;00m$
   738	proceed.[37m [39;49;00mIf[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00mis[37m [39;49;00ma[37m [39;49;00mslave[37m [39;49;00meditor[37m [39;49;00mor[37m [39;49;00mgraphical[37m [39;49;00mdebugger[37m [39;49;00m(denoted[37m [39;49;00mby[37m[39;49;00m$
   739	the[37m [39;49;00mfirst[37m [39;49;00mcommand-line[37m [39;49;00m[34mswitch[39;49;00m[37m [39;49;00mbeing[37m [39;49;00m[04m[91m'[39;49;00m-emacs[04m[91m'[39;49;00m),[37m [39;49;00mwe[37m [39;49;00mshift[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00moff[37m [39;49;00mand[37m[39;49;00m$
   740	set[37m [39;49;00mC<$rl>[37m [39;49;00mto[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m(XXX[37m [39;49;00mostensibly[37m [39;49;00mto[37m [39;49;00m[34mdo[39;49;00m[37m [39;49;00mstraight[37m [39;49;00mreads).[37m[39;49;00m$
   741	[37m[39;49;00m$
   742	=cut[37m[39;49;00m$
   743	[37m[39;49;00m$
   744	[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
   745	[37m[39;49;00m$
   746	[37m    [39;49;00m[36m#[39;49;00m[36m Is Perl being run from a slave editor or graphical debugger?[39;49;00m[36m[39;49;00m$
   747	[37m    [39;49;00m[36m#[39;49;00m[36m If so, don't use readline, and set $slave_editor = 1.[39;49;00m[36m[39;49;00m$
   748	[37m    [39;49;00m$slave_editor[37m [39;49;00m=[37m[39;49;00m$
   749	[37m      [39;49;00m([37m [39;49;00m([37m [39;49;00mdefined[37m [39;49;00m$main::ARGV[[34m0[39;49;00m][37m [39;49;00m)[37m [39;49;00mand[37m [39;49;00m([37m [39;49;00m$main::ARGV[[34m0[39;49;00m][37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00m-emacs[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m);[37m[39;49;00m$
   750	[37m    [39;49;00m$rl[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00mshift([04m[91m@[39;49;00mmain::ARGV)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m$slave_editor;[37m[39;49;00m$
   751	[37m[39;49;00m$
   752	[37m    [39;49;00m[36m#[39;49;00m[36mrequire Term::ReadLine;[39;49;00m[36m[39;49;00m$
   753	[37m[39;49;00m$
   754	=pod[37m[39;49;00m$
   755	[37m[39;49;00m$
   756	We[37m [39;49;00mthen[37m [39;49;00mdetermine[37m [39;49;00mwhat[37m [39;49;00mthe[37m [39;49;00mconsole[37m [39;49;00mshould[37m [39;49;00mbe[37m [39;49;00mon[37m [39;49;00mvarious[37m [39;49;00msystems:[37m[39;49;00m$
   757	[37m[39;49;00m$
   758	=over[37m [39;49;00m[34m4[39;49;00m[37m[39;49;00m$
   759	[37m[39;49;00m$
   760	=item[37m [39;49;00m*[37m [39;49;00mCygwin[37m [39;49;00m-[37m [39;49;00mWe[37m [39;49;00muse[37m [39;49;00mC<stdin>[37m [39;49;00minstead[37m [39;49;00mof[37m [39;49;00ma[37m [39;49;00mseparate[37m [39;49;00mdevice.[37m[39;49;00m$
   761	[37m[39;49;00m$
   762	=cut[37m[39;49;00m$
   763	[37m[39;49;00m$
   764	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m$^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mcygwin[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   765	[37m[39;49;00m$
   766	[37m        [39;49;00m[36m#[39;49;00m[36m [39;49;00m[36m/[39;49;00m[36mdev[39;49;00m[36m/[39;49;00m[36mtty is binary. use stdin for textmode[39;49;00m[36m[39;49;00m$
   767	[37m        [39;49;00mundef[37m [39;49;00m$console;[37m[39;49;00m$
   768	[37m    [39;49;00m}[37m[39;49;00m$
   769	[37m[39;49;00m$
   770	=item[37m [39;49;00m*[37m [39;49;00mUnix[37m [39;49;00m-[37m [39;49;00muse[37m [39;49;00mC</dev/tty>.[37m[39;49;00m$
   771	[37m[39;49;00m$
   772	=cut[37m[39;49;00m$
   773	[37m[39;49;00m$
   774	[37m    [39;49;00melsif[37m [39;49;00m([37m [39;49;00m-e[37m [39;49;00m[33m"[39;49;00m[33m/dev/tty[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   775	[37m        [39;49;00m$console[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m/dev/tty[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   776	[37m    [39;49;00m}[37m[39;49;00m$
   777	[37m[39;49;00m$
   778	=item[37m [39;49;00m*[37m [39;49;00mWindows[37m [39;49;00mor[37m [39;49;00mMSDOS[37m [39;49;00m-[37m [39;49;00muse[37m [39;49;00mC<con>.[37m[39;49;00m$
   779	[37m[39;49;00m$
   780	=cut[37m[39;49;00m$
   781	[37m[39;49;00m$
   782	[37m    [39;49;00melsif[37m [39;49;00m([37m [39;49;00m$^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mdos[04m[91m'[39;49;00m[37m [39;49;00mor[37m [39;49;00m-e[37m [39;49;00m[33m"[39;49;00m[33mcon[39;49;00m[33m"[39;49;00m[37m [39;49;00mor[37m [39;49;00m$^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mMSWin32[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   783	[37m        [39;49;00m$console[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mcon[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   784	[37m    [39;49;00m}[37m[39;49;00m$
   785	[37m[39;49;00m$
   786	=item[37m [39;49;00m*[37m [39;49;00mMacOS[37m [39;49;00m-[37m [39;49;00muse[37m [39;49;00mC<Dev:Console:Perl[37m [39;49;00mDebug>[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00mis[37m [39;49;00mthe[37m [39;49;00mMPW[37m [39;49;00mversion;[37m [39;49;00mC<Dev:[37m[39;49;00m$
   787	Console>[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mnot.[37m[39;49;00m$
   788	[37m[39;49;00m$
   789	Note[37m [39;49;00mthat[37m [39;49;00mMac[37m [39;49;00mOS[37m [39;49;00mX[37m [39;49;00mreturns[37m [39;49;00mC<darwin>,[37m [39;49;00mnot[37m [39;49;00mC<MacOS>.[37m [39;49;00mAlso[37m [39;49;00mnote[37m [39;49;00mthat[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mdoesn[04m[91m'[39;49;00mt[37m [39;49;00m[34mdo[39;49;00m[37m [39;49;00manything[37m [39;49;00mspecial[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mC<darwin>.[37m [39;49;00mMaybe[37m [39;49;00mit[37m [39;49;00mshould.[37m[39;49;00m$
   790	[37m[39;49;00m$
   791	=cut[37m[39;49;00m$
   792	[37m[39;49;00m$
   793	[37m    [39;49;00melsif[37m [39;49;00m([37m [39;49;00m$^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mMacOS[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   794	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m$MacPerl::Version[37m [39;49;00m!~[37m [39;49;00m/MPW/[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   795	[37m            [39;49;00m$console[37m [39;49;00m=[37m[39;49;00m$
   796	[37m              [39;49;00m[33m"[39;49;00m[33mDev:Console:Perl Debug[39;49;00m[33m"[39;49;00m;[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mSeparate[37m [39;49;00mwindow[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mapplication[37m[39;49;00m$
   797	[37m        [39;49;00m}[37m[39;49;00m$
   798	[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
   799	[37m            [39;49;00m$console[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mDev:Console[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   800	[37m        [39;49;00m}[37m[39;49;00m$
   801	[37m    [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00melsif[37m [39;49;00m($^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mMacOS[04m[91m'[39;49;00m)[37m[39;49;00m$
   802	[37m[39;49;00m$
   803	=item[37m [39;49;00m*[37m [39;49;00mVMS[37m [39;49;00m-[37m [39;49;00muse[37m [39;49;00mC<sys$command>.[37m[39;49;00m$
   804	[37m[39;49;00m$
   805	=cut[37m[39;49;00m$
   806	[37m[39;49;00m$
   807	[37m    [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
   808	[37m[39;49;00m$
   809	[37m        [39;49;00m[36m#[39;49;00m[36m everything else is ...[39;49;00m[36m[39;49;00m$
   810	[37m        [39;49;00m$console[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33msys[39;49;00m[33m\[39;49;00m[33m$command[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   811	[37m    [39;49;00m}[37m[39;49;00m$
   812	[37m[39;49;00m$
   813	=pod[37m[39;49;00m$
   814	[37m[39;49;00m$
   815	=back[37m[39;49;00m$
   816	[37m[39;49;00m$
   817	Several[37m [39;49;00mother[37m [39;49;00msystems[37m [39;49;00mdon[04m[91m'[39;49;00mt[37m [39;49;00muse[37m [39;49;00ma[37m [39;49;00mspecific[37m [39;49;00mconsole.[37m [39;49;00mWe[37m [39;49;00mC<undef[37m [39;49;00m$console>[37m[39;49;00m$
   818	[34mfor[39;49;00m[37m [39;49;00mthose[37m [39;49;00m(Windows[37m [39;49;00m[34musing[39;49;00m[37m [39;49;00ma[37m [39;49;00mslave[37m [39;49;00meditor/graphical[37m [39;49;00mdebugger,[37m [39;49;00mNetWare,[37m [39;49;00mOS/[34m2[39;49;00m[37m[39;49;00m$
   819	with[37m [39;49;00ma[37m [39;49;00mslave[37m [39;49;00meditor,[37m [39;49;00mEpoc).[37m[39;49;00m$
   820	[37m[39;49;00m$
   821	=cut[37m[39;49;00m$
   822	[37m[39;49;00m$
   823	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m([37m [39;49;00m$^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mMSWin32[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00mand[37m [39;49;00m([37m [39;49;00m$slave_editor[37m [39;49;00mor[37m [39;49;00mdefined[37m [39;49;00m$ENV{EMACS}[37m [39;49;00m)[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   824	[37m[39;49;00m$
   825	[37m        [39;49;00m[36m#[39;49;00m[36m [39;49;00m[36m/[39;49;00m[36mdev[39;49;00m[36m/[39;49;00m[36mtty is binary. use stdin for textmode[39;49;00m[36m[39;49;00m$
   826	[37m        [39;49;00m$console[37m [39;49;00m=[37m [39;49;00mundef;[37m[39;49;00m$
   827	[37m    [39;49;00m}[37m[39;49;00m$
   828	[37m[39;49;00m$
   829	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m$^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mNetWare[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   830	[37m[39;49;00m$
   831	[37m        [39;49;00m[36m#[39;49;00m[36m [39;49;00m[36m/[39;49;00m[36mdev[39;49;00m[36m/[39;49;00m[36mtty is binary. use stdin for textmode[39;49;00m[36m[39;49;00m$
   832	[37m        [39;49;00m$console[37m [39;49;00m=[37m [39;49;00mundef;[37m[39;49;00m$
   833	[37m    [39;49;00m}[37m[39;49;00m$
   834	[37m[39;49;00m$
   835	[37m    [39;49;00m[36m#[39;49;00m[36m In OS[39;49;00m[36m/[39;49;00m[36m2, we need to use STDIN to get textmode too, even though[39;49;00m[36m[39;49;00m$
   836	[37m    [39;49;00m[36m#[39;49;00m[36m it pretty much looks like Unix otherwise.[39;49;00m[36m[39;49;00m$
   837	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00mdefined[37m [39;49;00m$ENV{OS2_SHELL}[37m [39;49;00mand[37m [39;49;00m([37m [39;49;00m$slave_editor[37m [39;49;00mor[37m [39;49;00m$ENV{WINDOWID}[37m [39;49;00m)[37m [39;49;00m)[37m[39;49;00m$
   838	[37m    [39;49;00m{[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mIn[37m [39;49;00mOS/[34m2[39;49;00m[37m[39;49;00m$
   839	[37m        [39;49;00m$console[37m [39;49;00m=[37m [39;49;00mundef;[37m[39;49;00m$
   840	[37m    [39;49;00m}[37m[39;49;00m$
   841	[37m[39;49;00m$
   842	[37m    [39;49;00m[36m#[39;49;00m[36m EPOC also falls into the 'got to use STDIN' camp.[39;49;00m[36m[39;49;00m$
   843	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m$^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mepoc[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   844	[37m        [39;49;00m$console[37m [39;49;00m=[37m [39;49;00mundef;[37m[39;49;00m$
   845	[37m    [39;49;00m}[37m[39;49;00m$
   846	[37m[39;49;00m$
   847	=pod[37m[39;49;00m$
   848	[37m[39;49;00m$
   849	If[37m [39;49;00mthere[37m [39;49;00mis[37m [39;49;00ma[37m [39;49;00mTTY[37m [39;49;00mhanging[37m [39;49;00maround[37m [39;49;00mfrom[37m [39;49;00ma[37m [39;49;00mparent,[37m [39;49;00mwe[37m [39;49;00muse[37m [39;49;00mthat[37m [39;49;00mas[37m [39;49;00mthe[37m [39;49;00mconsole.[37m[39;49;00m$
   850	[37m[39;49;00m$
   851	=cut[37m[39;49;00m$
   852	[37m[39;49;00m$
   853	[37m    [39;49;00m$console[37m [39;49;00m=[37m [39;49;00m$tty[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mdefined[37m [39;49;00m$tty;[37m[39;49;00m$
   854	[37m[39;49;00m$
   855	=head2[37m [39;49;00mSOCKET[37m [39;49;00mHANDLING[37m   [39;49;00m[37m[39;49;00m$
   856	[37m[39;49;00m$
   857	The[37m [39;49;00mdebugger[37m [39;49;00mis[37m [39;49;00mcapable[37m [39;49;00mof[37m [39;49;00mopening[37m [39;49;00ma[37m [39;49;00msocket[37m [39;49;00mand[37m [39;49;00mcarrying[37m [39;49;00mout[37m [39;49;00ma[37m [39;49;00mdebugging[37m[39;49;00m$
   858	session[37m [39;49;00mover[37m [39;49;00mthe[37m [39;49;00msocket.[37m[39;49;00m$
   859	[37m[39;49;00m$
   860	If[37m [39;49;00mC<RemotePort>[37m [39;49;00mwas[37m [39;49;00mdefined[37m [39;49;00min[37m [39;49;00mthe[37m [39;49;00moptions,[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00massumes[37m [39;49;00mthat[37m [39;49;00mit[37m[39;49;00m$
   861	should[37m [39;49;00m[34mtry[39;49;00m[37m [39;49;00mto[37m [39;49;00mstart[37m [39;49;00ma[37m [39;49;00mdebugging[37m [39;49;00msession[37m [39;49;00mon[37m [39;49;00mthat[37m [39;49;00mport.[37m [39;49;00mIt[37m [39;49;00mbuilds[37m [39;49;00mthe[37m [39;49;00msocket[37m[39;49;00m$
   862	and[37m [39;49;00mthen[37m [39;49;00mtries[37m [39;49;00mto[37m [39;49;00mconnect[37m [39;49;00mthe[37m [39;49;00minput[37m [39;49;00mand[37m [39;49;00moutput[37m [39;49;00mfilehandles[37m [39;49;00mto[37m [39;49;00mit.[37m[39;49;00m$
   863	[37m[39;49;00m$
   864	=cut[37m[39;49;00m$
   865	[37m[39;49;00m$
   866	[37m    [39;49;00m[36m#[39;49;00m[36m Handle socket stuff.[39;49;00m[36m[39;49;00m$
   867	[37m[39;49;00m$
   868	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00mdefined[37m [39;49;00m$remoteport[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   869	[37m[39;49;00m$
   870	[37m        [39;49;00m[36m#[39;49;00m[36m If RemotePort was defined in the options, connect input and output[39;49;00m[36m[39;49;00m$
   871	[37m        [39;49;00m[36m#[39;49;00m[36m to the socket.[39;49;00m[36m[39;49;00m$
   872	[37m        [39;49;00mrequire[37m [39;49;00mIO::Socket;[37m[39;49;00m$
   873	[37m        [39;49;00m$OUT[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mIO::Socket::INET([37m[39;49;00m$
   874	[37m            [39;49;00mTimeout[37m  [39;49;00m=>[37m [39;49;00m[04m[91m'[39;49;00m[34m10[39;49;00m[04m[91m'[39;49;00m,[37m[39;49;00m$
   875	[37m            [39;49;00mPeerAddr[37m [39;49;00m=>[37m [39;49;00m$remoteport,[37m[39;49;00m$
   876	[37m            [39;49;00mProto[37m    [39;49;00m=>[37m [39;49;00m[04m[91m'[39;49;00mtcp[04m[91m'[39;49;00m,[37m[39;49;00m$
   877	[37m        [39;49;00m);[37m[39;49;00m$
   878	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m!$OUT[37m [39;49;00m)[37m [39;49;00m{[37m [39;49;00mdie[37m [39;49;00m[33m"[39;49;00m[33mUnable to connect to remote host: $remoteport[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m [39;49;00m}[37m[39;49;00m$
   879	[37m        [39;49;00m$IN[37m [39;49;00m=[37m [39;49;00m$OUT;[37m[39;49;00m$
   880	[37m    [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(defined[37m [39;49;00m$remoteport)[37m[39;49;00m$
   881	[37m[39;49;00m$
   882	=pod[37m[39;49;00m$
   883	[37m[39;49;00m$
   884	If[37m [39;49;00mno[37m [39;49;00mC<RemotePort>[37m [39;49;00mwas[37m [39;49;00mdefined,[37m [39;49;00mand[37m [39;49;00mwe[37m [39;49;00mwant[37m [39;49;00mto[37m [39;49;00mcreate[37m [39;49;00ma[37m [39;49;00mTTY[37m [39;49;00mon[37m [39;49;00mstartup,[37m[39;49;00m$
   885	[34mthis[39;49;00m[37m [39;49;00mis[37m [39;49;00mprobably[37m [39;49;00ma[37m [39;49;00msituation[37m [39;49;00mwhere[37m [39;49;00mmultiple[37m [39;49;00mdebuggers[37m [39;49;00mare[37m [39;49;00mrunning[37m [39;49;00m([34mfor[39;49;00m[37m [39;49;00mexample,[37m[39;49;00m$
   886	a[37m [39;49;00mbackticked[37m [39;49;00mcommand[37m [39;49;00mthat[37m [39;49;00mstarts[37m [39;49;00mup[37m [39;49;00manother[37m [39;49;00mdebugger).[37m [39;49;00mWe[37m [39;49;00mcreate[37m [39;49;00ma[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mIN[37m [39;49;00mand[37m[39;49;00m$
   887	OUT[37m [39;49;00mfilehandle,[37m [39;49;00mand[37m [39;49;00m[34mdo[39;49;00m[37m [39;49;00mthe[37m [39;49;00mnecessary[37m [39;49;00mmojo[37m [39;49;00mto[37m [39;49;00mcreate[37m [39;49;00ma[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mTTY[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mwe[37m [39;49;00mknow[37m [39;49;00mhow[37m[39;49;00m$
   888	and[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mwe[37m [39;49;00mcan.[37m[39;49;00m$
   889	[37m[39;49;00m$
   890	=cut[37m[39;49;00m$
   891	[37m[39;49;00m$
   892	[37m    [39;49;00m[36m#[39;49;00m[36m Non-socket.[39;49;00m[36m[39;49;00m$
   893	[37m    [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
   894	[37m[39;49;00m$
   895	[37m        [39;49;00m[36m#[39;49;00m[36m Two debuggers running (probably a system or a backtick that invokes[39;49;00m[36m[39;49;00m$
   896	[37m        [39;49;00m[36m#[39;49;00m[36m the debugger itself under the running one). create a new IN and OUT[39;49;00m[36m[39;49;00m$
   897	[37m        [39;49;00m[36m#[39;49;00m[36m filehandle, and do the necessary mojo to create a new tty if we[39;49;00m[36m[39;49;00m$
   898	[37m        [39;49;00m[36m#[39;49;00m[36m know how, and we can.[39;49;00m[36m[39;49;00m$
   899	[37m        [39;49;00mcreate_IN_OUT([34m4[39;49;00m)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m$CreateTTY[37m [39;49;00m&[37m [39;49;00m[34m4[39;49;00m;[37m[39;49;00m$
   900	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m($console)[37m [39;49;00m{[37m[39;49;00m$
   901	[37m[39;49;00m$
   902	[37m            [39;49;00m[36m#[39;49;00m[36m If we have a console, check to see if there are separate ins and[39;49;00m[36m[39;49;00m$
   903	[37m            [39;49;00m[36m#[39;49;00m[36m outs to open. (They are assumed identiical if not.)[39;49;00m[36m[39;49;00m$
   904	[37m[39;49;00m$
   905	[37m            [39;49;00mmy[37m [39;49;00m([37m [39;49;00m$i,[37m [39;49;00m$o[37m [39;49;00m)[37m [39;49;00m=[37m [39;49;00msplit[37m [39;49;00m/,/,[37m [39;49;00m$console;[37m[39;49;00m$
   906	[37m            [39;49;00m$o[37m [39;49;00m=[37m [39;49;00m$i[37m [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$o;[37m[39;49;00m$
   907	[37m[39;49;00m$
   908	[37m            [39;49;00m[36m#[39;49;00m[36m read[39;49;00m[36m/[39;49;00m[36mwrite on in, or just read, or read on STDIN.[39;49;00m[36m[39;49;00m$
   909	[37m            [39;49;00mopen([37m [39;49;00mIN,[37m      [39;49;00m[33m"[39;49;00m[33m+<$i[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
   910	[37m              [39;49;00m||[37m [39;49;00mopen([37m [39;49;00mIN,[37m [39;49;00m[33m"[39;49;00m[33m<$i[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
   911	[37m              [39;49;00m||[37m [39;49;00mopen([37m [39;49;00mIN,[37m [39;49;00m[33m"[39;49;00m[33m<&STDIN[39;49;00m[33m"[39;49;00m[37m [39;49;00m);[37m[39;49;00m$
   912	[37m[39;49;00m$
   913	[37m            [39;49;00m[36m#[39;49;00m[36m read[39;49;00m[36m/[39;49;00m[36mwrite[39;49;00m[36m/[39;49;00m[36mcreate[39;49;00m[36m/[39;49;00m[36mclobber out, or write[39;49;00m[36m/[39;49;00m[36mcreate[39;49;00m[36m/[39;49;00m[36mclobber out,[39;49;00m[36m[39;49;00m$
   914	[37m            [39;49;00m[36m#[39;49;00m[36m or merge with STDERR, or merge with STDOUT.[39;49;00m[36m[39;49;00m$
   915	[37m                 [39;49;00mopen([37m [39;49;00mOUT,[37m [39;49;00m[33m"[39;49;00m[33m+>$o[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
   916	[37m              [39;49;00m||[37m [39;49;00mopen([37m [39;49;00mOUT,[37m [39;49;00m[33m"[39;49;00m[33m>$o[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
   917	[37m              [39;49;00m||[37m [39;49;00mopen([37m [39;49;00mOUT,[37m [39;49;00m[33m"[39;49;00m[33m>&STDERR[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
   918	[37m              [39;49;00m||[37m [39;49;00mopen([37m [39;49;00mOUT,[37m [39;49;00m[33m"[39;49;00m[33m>&STDOUT[39;49;00m[33m"[39;49;00m[37m [39;49;00m);[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mso[37m [39;49;00mwe[37m [39;49;00mdon[04m[91m'[39;49;00mt[37m [39;49;00mdongle[37m [39;49;00mstdout[37m[39;49;00m$
   919	[37m[39;49;00m$
   920	[37m        [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m($console)[37m[39;49;00m$
   921	[37m        [39;49;00melsif[37m [39;49;00m([37m [39;49;00mnot[37m [39;49;00mdefined[37m [39;49;00m$console[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   922	[37m[39;49;00m$
   923	[37m            [39;49;00m[36m#[39;49;00m[36m No console. Open STDIN.[39;49;00m[36m[39;49;00m$
   924	[37m            [39;49;00mopen([37m [39;49;00mIN,[37m [39;49;00m[33m"[39;49;00m[33m<&STDIN[39;49;00m[33m"[39;49;00m[37m [39;49;00m);[37m[39;49;00m$
   925	[37m[39;49;00m$
   926	[37m            [39;49;00m[36m#[39;49;00m[36m merge with STDERR, or with STDOUT.[39;49;00m[36m[39;49;00m$
   927	[37m            [39;49;00mopen([37m [39;49;00mOUT,[37m      [39;49;00m[33m"[39;49;00m[33m>&STDERR[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
   928	[37m              [39;49;00m||[37m [39;49;00mopen([37m [39;49;00mOUT,[37m [39;49;00m[33m"[39;49;00m[33m>&STDOUT[39;49;00m[33m"[39;49;00m[37m [39;49;00m);[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mso[37m [39;49;00mwe[37m [39;49;00mdon[04m[91m'[39;49;00mt[37m [39;49;00mdongle[37m [39;49;00mstdout[37m[39;49;00m$
   929	[37m            [39;49;00m$console[37m [39;49;00m=[37m [39;49;00m[04m[91m'[39;49;00mSTDIN/OUT[04m[91m'[39;49;00m;[37m[39;49;00m$
   930	[37m        [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00melsif[37m [39;49;00m(not[37m [39;49;00mdefined[37m [39;49;00m$console)[37m[39;49;00m$
   931	[37m[39;49;00m$
   932	[37m        [39;49;00m[36m#[39;49;00m[36m Keep copies of the filehandles so that when the pager runs, it[39;49;00m[36m[39;49;00m$
   933	[37m        [39;49;00m[36m#[39;49;00m[36m can close standard input without clobbering ours.[39;49;00m[36m[39;49;00m$
   934	[37m        [39;49;00m$IN[37m [39;49;00m=[37m [39;49;00m[04m[91m\[39;49;00m*IN,[37m [39;49;00m$OUT[37m [39;49;00m=[37m [39;49;00m[04m[91m\[39;49;00m*OUT[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m$console[37m [39;49;00mor[37m [39;49;00mnot[37m [39;49;00mdefined[37m [39;49;00m$console;[37m[39;49;00m$
   935	[37m    [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00melsif[37m [39;49;00m(from[37m [39;49;00m[34mif[39;49;00m(defined[37m [39;49;00m$remoteport))[37m[39;49;00m$
   936	[37m[39;49;00m$
   937	[37m    [39;49;00m[36m#[39;49;00m[36m Unbuffer DB::OUT. We need to see responses right away.[39;49;00m[36m[39;49;00m$
   938	[37m    [39;49;00mmy[37m [39;49;00m$previous[37m [39;49;00m=[37m [39;49;00mselect($OUT);[37m[39;49;00m$
   939	[37m    [39;49;00m$|[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m                                  [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mDB::OUT[37m[39;49;00m$
   940	[37m    [39;49;00mselect($previous);[37m[39;49;00m$
   941	[37m[39;49;00m$
   942	[37m    [39;49;00m[36m#[39;49;00m[36m Line info goes to debugger output unless pointed elsewhere.[39;49;00m[36m[39;49;00m$
   943	[37m    [39;49;00m[36m#[39;49;00m[36m Pointing elsewhere makes it possible for slave editors to[39;49;00m[36m[39;49;00m$
   944	[37m    [39;49;00m[36m#[39;49;00m[36m keep track of file and position. We have both a filehandle[39;49;00m[36m[39;49;00m$
   945	[37m    [39;49;00m[36m#[39;49;00m[36m and a I[39;49;00m[36m/[39;49;00m[36mO description to keep track of.[39;49;00m[36m[39;49;00m$
   946	[37m    [39;49;00m$LINEINFO[37m [39;49;00m=[37m [39;49;00m$OUT[37m     [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$LINEINFO;[37m[39;49;00m$
   947	[37m    [39;49;00m$lineinfo[37m [39;49;00m=[37m [39;49;00m$console[37m [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$lineinfo;[37m[39;49;00m$
   948	[37m	[39;49;00m[36m#[39;49;00m[36m share($LINEINFO); # <- unable to share globs[39;49;00m[36m[39;49;00m$
   949	[37m	[39;49;00mshare($lineinfo);[37m   [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00m[37m[39;49;00m$
   950	[37m[39;49;00m$
   951	=pod[37m[39;49;00m$
   952	[37m[39;49;00m$
   953	To[37m [39;49;00mfinish[37m [39;49;00minitialization,[37m [39;49;00mwe[37m [39;49;00mshow[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mgreeting,[37m[39;49;00m$
   954	and[37m [39;49;00mthen[37m [39;49;00mcall[37m [39;49;00mthe[37m [39;49;00mC<afterinit()>[37m [39;49;00msubroutine[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mthere[37m [39;49;00mis[37m [39;49;00mone.[37m[39;49;00m$
   955	[37m[39;49;00m$
   956	=cut[37m[39;49;00m$
   957	[37m[39;49;00m$
   958	[37m    [39;49;00m[36m#[39;49;00m[36m Show the debugger greeting.[39;49;00m[36m[39;49;00m$
   959	[37m    [39;49;00m$header[37m [39;49;00m=~[37m [39;49;00ms/.Header:[37m [39;49;00m([^,]+),v([04m[91m\[39;49;00ms+[04m[91m\[39;49;00mS+[04m[91m\[39;49;00ms+[04m[91m\[39;49;00mS+).*$/$1$2/;[37m[39;49;00m$
   960	[37m    [39;49;00munless[37m [39;49;00m($runnonstop)[37m [39;49;00m{[37m[39;49;00m$
   961	[37m        [39;49;00mlocal[37m [39;49;00m$[04m[91m\[39;49;00m[37m [39;49;00m=[37m [39;49;00m[04m[91m'[39;49;00m[04m[91m'[39;49;00m;[37m[39;49;00m$
   962	[37m        [39;49;00mlocal[37m [39;49;00m$,[37m [39;49;00m=[37m [39;49;00m[04m[91m'[39;49;00m[04m[91m'[39;49;00m;[37m[39;49;00m$
   963	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m$term_pid[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00m[34m-1[39;49;00m[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   964	[37m            [39;49;00mprint[37m [39;49;00m$OUT[37m [39;49;00m[33m"[39;49;00m[33m\n[39;49;00m[33mDaughter DB session started...[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   965	[37m        [39;49;00m}[37m[39;49;00m$
   966	[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
   967	[37m            [39;49;00mprint[37m [39;49;00m$OUT[37m [39;49;00m[33m"[39;49;00m[33m\n[39;49;00m[33mLoading DB routines from $header[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   968	[37m            [39;49;00mprint[37m [39;49;00m[32m$OUT[39;49;00m[37m [39;49;00m([37m[39;49;00m$
   969	[37m                [39;49;00m[33m"[39;49;00m[33mEditor support [39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
   970	[37m                [39;49;00m$slave_editor[37m [39;49;00m?[37m [39;49;00m[33m"[39;49;00m[33menabled[39;49;00m[33m"[39;49;00m[37m [39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33mavailable[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m.[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   971	[37m            [39;49;00m);[37m[39;49;00m$
   972	[37m            [39;49;00mprint[37m [39;49;00m$OUT[37m[39;49;00m$
   973	[33m"[39;49;00m[33m\n[39;49;00m[33mEnter h or `h h' for help, or `$doccmd perldebug' for more help.[39;49;00m[33m\n[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   974	[37m        [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m($term_pid[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00m[34m-1[39;49;00m[04m[91m'[39;49;00m)[37m[39;49;00m$
   975	[37m    [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00munless[37m [39;49;00m($runnonstop)[37m[39;49;00m$
   976	}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m($notty)[37m[39;49;00m$
   977	[37m[39;49;00m$
   978	[36m#[39;49;00m[36m XXX This looks like a bug to me.[39;49;00m[36m[39;49;00m$
   979	[36m#[39;49;00m[36m Why copy to @ARGS and then futz with @args?[39;49;00m[36m[39;49;00m$
   980	[04m[91m@[39;49;00mARGS[37m [39;49;00m=[37m [39;49;00m[04m[91m@[39;49;00mARGV;[37m[39;49;00m$
   981	[34mfor[39;49;00m[37m [39;49;00m([04m[91m@[39;49;00margs)[37m [39;49;00m{[37m[39;49;00m$
   982	[37m    [39;49;00m[36m#[39;49;00m[36m Make sure backslashes before single quotes are stripped out, and[39;49;00m[36m[39;49;00m$
   983	[37m    [39;49;00m[36m#[39;49;00m[36m keep args unless they are numeric (XXX why?)[39;49;00m[36m[39;49;00m$
   984	[37m    [39;49;00m[36m#[39;49;00m[36m s[39;49;00m[36m/[39;49;00m[36m\'[39;49;00m[36m/[39;49;00m[36m\\\'[39;49;00m[36m/[39;49;00m[36mg;                      # removed while not justified understandably[39;49;00m[36m[39;49;00m$
   985	[37m    [39;49;00m[36m#[39;49;00m[36m s[39;49;00m[36m/[39;49;00m[36m(.*)[39;49;00m[36m/[39;49;00m[36m'$1'[39;49;00m[36m/[39;49;00m[36m unless [39;49;00m[36m/[39;49;00m[36m^-?[\d.]+$[39;49;00m[36m/[39;49;00m[36m; # ditto[39;49;00m[36m[39;49;00m$
   986	}[37m[39;49;00m$
   987	[37m[39;49;00m$
   988	[36m#[39;49;00m[36m If there was an afterinit() sub defined, call it. It will get[39;49;00m[36m[39;49;00m$
   989	[36m#[39;49;00m[36m executed in our scope, so it can fiddle with debugger globals.[39;49;00m[36m[39;49;00m$
   990	[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00mdefined[37m [39;49;00m&afterinit[37m [39;49;00m)[37m [39;49;00m{[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mMay[37m [39;49;00mbe[37m [39;49;00mdefined[37m [39;49;00min[37m [39;49;00m$rcfile[37m[39;49;00m$
   991	[37m    [39;49;00m&afterinit();[37m[39;49;00m$
   992	}[37m[39;49;00m$
   993	[37m[39;49;00m$
   994	[36m#[39;49;00m[36m Inform us about "Stack dump during die enabled ..." in dieLevel().[39;49;00m[36m[39;49;00m$
   995	$I_m_init[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;$
