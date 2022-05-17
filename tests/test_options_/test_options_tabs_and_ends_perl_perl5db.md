=head1[37m [39;49;00mNAME[37m [39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
perl5db.pl[37m [39;49;00m-[37m [39;49;00mthe[37m [39;49;00mperl[37m [39;49;00mdebugger[37m[39;49;00m$
[37m[39;49;00m$
=head1[37m [39;49;00mSYNOPSIS[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mperl[37m [39;49;00m-d[37m  [39;49;00myour_Perl_script[37m[39;49;00m$
[37m[39;49;00m$
=head1[37m [39;49;00mDESCRIPTION[37m[39;49;00m$
[37m[39;49;00m$
After[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00mroutine[37m [39;49;00mis[37m [39;49;00mover,[37m [39;49;00mwe[37m [39;49;00mdon[04m[91m'[39;49;00mt[37m [39;49;00mhave[37m [39;49;00muser[37m [39;49;00mcode[37m [39;49;00mexecuting[37m [39;49;00min[37m [39;49;00mthe[37m [39;49;00mdebugger[04m[91m'[39;49;00ms[37m[39;49;00m$
context,[37m [39;49;00mso[37m [39;49;00mwe[37m [39;49;00mcan[37m [39;49;00muse[37m [39;49;00mC<my>[37m [39;49;00mfreely.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m############################################# Begin lexical danger zone[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m 'my' variables used here could leak into (that is, be visible in)[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m the context that the code being evaluated is executing in. This means that[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m the code could modify the debugger's variables.[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m Fiddling with the debugger's context could be Bad. We insulate things as[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m much as we can.[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
sub[37m [39;49;00meval[37m [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m 'my' would make it visible from user code[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m    but so does local! --tchrist[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m Remember: this localizes @DB::res, not @main::res.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00mlocal[37m [39;49;00m[04m[91m@[39;49;00mres;[37m[39;49;00m$
[37m    [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m Try to keep the user code from messing  with us. Save these so that[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m even if the eval'ed code changes them, we can put them back again.[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m Needed because the user could refer directly to the debugger's[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m package globals (and any 'my' variables in this containing scope)[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m inside the eval(), and we want to try to stay safe.[39;49;00m[36m[39;49;00m$
[37m        [39;49;00mlocal[37m [39;49;00m$otrace[37m  [39;49;00m=[37m [39;49;00m$trace;[37m[39;49;00m$
[37m        [39;49;00mlocal[37m [39;49;00m$osingle[37m [39;49;00m=[37m [39;49;00m$single;[37m[39;49;00m$
[37m        [39;49;00mlocal[37m [39;49;00m$od[37m      [39;49;00m=[37m [39;49;00m$^D;[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m Untaint the incoming eval() argument.[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m{[37m [39;49;00m($evalarg)[37m [39;49;00m=[37m [39;49;00m$evalarg[37m [39;49;00m=~[37m [39;49;00m/(.*)/s;[37m [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m $usercontext built in DB::DB near the comment[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m "set up the context for DB::eval ..."[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m Evaluate and save any results.[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m[04m[91m@[39;49;00mres[37m [39;49;00m=[37m [39;49;00meval[37m [39;49;00m[33m"[39;49;00m[33m$usercontext $evalarg;[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m  [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00m[33m'[39;49;00m[33m\n[39;49;00m[33m'[39;49;00m[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mnice[37m [39;49;00mrecursive[37m [39;49;00mdebug[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m Restore those old values.[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m$trace[37m  [39;49;00m=[37m [39;49;00m$otrace;[37m[39;49;00m$
[37m        [39;49;00m$single[37m [39;49;00m=[37m [39;49;00m$osingle;[37m[39;49;00m$
[37m        [39;49;00m$^D[37m     [39;49;00m=[37m [39;49;00m$od;[37m[39;49;00m$
[37m    [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m Save the current value of $@, and preserve it in the debugger's copy[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m of the saved precious globals.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00mmy[37m [39;49;00m$at[37m [39;49;00m=[37m [39;49;00m$[04m[91m@[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m Since we're only saving $@, we only have to localize the array element[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m that it will be stored in.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00mlocal[37m [39;49;00m$saved[[34m0[39;49;00m];[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mPreserve[37m [39;49;00mthe[37m [39;49;00mold[37m [39;49;00mvalue[37m [39;49;00mof[37m [39;49;00m$[04m[91m@[39;49;00m[37m[39;49;00m$
[37m    [39;49;00meval[37m [39;49;00m{[37m [39;49;00m&DB::save[37m [39;49;00m};[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m Now see whether we need to report an error back to the user.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m($at)[37m [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00mlocal[37m [39;49;00m$[04m[91m\[39;49;00m[37m [39;49;00m=[37m [39;49;00m[04m[91m'[39;49;00m[04m[91m'[39;49;00m;[37m[39;49;00m$
[37m        [39;49;00mprint[37m [39;49;00m$OUT[37m [39;49;00m$at;[37m[39;49;00m$
[37m    [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m Display as required by the caller. $onetimeDump and $onetimedumpDepth[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m are package globals.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00melsif[37m [39;49;00m($onetimeDump)[37m [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m$onetimeDump[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mdump[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00mlocal[37m [39;49;00m$option{dumpDepth}[37m [39;49;00m=[37m [39;49;00m$onetimedumpDepth[37m[39;49;00m$
[37m              [39;49;00m[34mif[39;49;00m[37m [39;49;00mdefined[37m [39;49;00m$onetimedumpDepth;[37m[39;49;00m$
[37m            [39;49;00mdumpit([37m [39;49;00m$OUT,[37m [39;49;00m[04m[91m\[39;49;00m[04m[91m@[39;49;00mres[37m [39;49;00m);[37m[39;49;00m$
[37m        [39;49;00m}[37m[39;49;00m$
[37m        [39;49;00melsif[37m [39;49;00m([37m [39;49;00m$onetimeDump[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mmethods[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00mmethods([37m [39;49;00m$res[[34m0[39;49;00m][37m [39;49;00m);[37m[39;49;00m$
[37m        [39;49;00m}[37m[39;49;00m$
[37m    [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00melsif[37m [39;49;00m($onetimeDump)[37m[39;49;00m$
[37m    [39;49;00m[04m[91m@[39;49;00mres;[37m[39;49;00m$
}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00msub[37m [39;49;00meval[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m############################################# End lexical danger zone[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m After this point it is safe to introduce lexicals.[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m The code being debugged will be executing in its own context, and[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m can't see the inside of the debugger.[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m However, one should not overdo it: leave as much control from outside as[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m possible. If you make something a lexical, it's not going to be addressable[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m from outside the debugger even if you know its name.[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m This file is automatically included if you do perl -d.[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m It's probably not useful to include this yourself.[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m Before venturing further into these twisty passages, it is[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m wise to read the perldebguts man page or risk the ire of dragons.[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m (It should be noted that perldebguts will tell you a lot about[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m the underlying mechanics of how the debugger interfaces into the[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m Perl interpreter, but not a lot about the debugger itself. The new[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m comments in this code try to address this problem.)[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m Note that no subroutine call is possible until &DB::sub is defined[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m (for subroutines defined outside of the package DB). In fact the same is[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m true if $deep is not defined.[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m Enhanced by ilya@math.ohio-state.edu (Ilya Zakharevich)[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m modified Perl debugger, to be run from Emacs in perldb-mode[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m Ray Lischner (uunet!mntgfx!lisch) as of 5 Nov 1990[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m Johan Vromans -- upgrade to 4.0 pl 10[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m Ilya Zakharevich -- patches after 5.001 (and some before ;-)[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m (We have made efforts to  clarify the comments in the change log[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m in other places; some of them may seem somewhat obscure as they[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m were originally written, and explaining them away from the code[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m in question seems conterproductive.. -JM)[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
=head1[37m [39;49;00mDEBUGGER[37m [39;49;00mINITIALIZATION[37m[39;49;00m$
[37m[39;49;00m$
The[37m [39;49;00mdebugger[37m [39;49;00mstarts[37m [39;49;00mup[37m [39;49;00min[37m [39;49;00mphases.[37m[39;49;00m$
[37m[39;49;00m$
=head2[37m [39;49;00mBASIC[37m [39;49;00mSETUP[37m[39;49;00m$
[37m[39;49;00m$
First,[37m [39;49;00mit[37m [39;49;00minitializes[37m [39;49;00mthe[37m [39;49;00menvironment[37m [39;49;00mit[37m [39;49;00mwants[37m [39;49;00mto[37m [39;49;00mrun[37m [39;49;00min:[37m [39;49;00mturning[37m [39;49;00moff[37m[39;49;00m$
warnings[37m [39;49;00mduring[37m [39;49;00mits[37m [39;49;00mown[37m [39;49;00mcompilation,[37m [39;49;00mdefining[37m [39;49;00mvariables[37m [39;49;00mwhich[37m [39;49;00mit[37m [39;49;00mwill[37m [39;49;00mneed[37m[39;49;00m$
to[37m [39;49;00mavoid[37m [39;49;00mwarnings[37m [39;49;00mlater,[37m [39;49;00msetting[37m [39;49;00mitself[37m [39;49;00mup[37m [39;49;00mto[37m [39;49;00mnot[37m [39;49;00mexit[37m [39;49;00mwhen[37m [39;49;00mthe[37m [39;49;00mprogram[37m[39;49;00m$
terminates,[37m [39;49;00mand[37m [39;49;00mdefaulting[37m [39;49;00mto[37m [39;49;00mprinting[37m [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mvalues[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mthe[37m [39;49;00mC<r>[37m [39;49;00mcommand.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m Needed for the statement after exec():[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m This BEGIN block is simply used to switch off warnings during debugger[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m compiliation. Probably it would be better practice to fix the warnings,[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m but this is how it's done at the moment.[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
BEGIN[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00m$ini_warn[37m [39;49;00m=[37m [39;49;00m$^W;[37m[39;49;00m$
[37m    [39;49;00m$^W[37m       [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
}[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mSwitch[37m [39;49;00mcompilation[37m [39;49;00mwarnings[37m [39;49;00moff[37m [39;49;00muntil[37m [39;49;00manother[37m [39;49;00mBEGIN.[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m test if assertions are supported and actived:[39;49;00m[36m[39;49;00m$
BEGIN[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00m$ini_assertion[37m [39;49;00m=[37m [39;49;00meval[37m [39;49;00m[33m"[39;49;00m[33msub asserting_test : assertion {1}; 1[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m $ini_assertion = undef => assertions unsupported,[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m        "       = 1     => assertions supported[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m print "\$ini_assertion=$ini_assertion\n";[39;49;00m[36m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
local[37m [39;49;00m($^W)[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mSwitch[37m [39;49;00mrun-time[37m [39;49;00mwarnings[37m [39;49;00moff[37m [39;49;00mduring[37m [39;49;00minit.[37m[39;49;00m$
[37m[39;49;00m$
=head2[37m [39;49;00mTHREADS[37m [39;49;00mSUPPORT[37m[39;49;00m$
[37m[39;49;00m$
If[37m [39;49;00mwe[37m [39;49;00mare[37m [39;49;00mrunning[37m [39;49;00munder[37m [39;49;00ma[37m [39;49;00mthreaded[37m [39;49;00mPerl,[37m [39;49;00mwe[37m [39;49;00mrequire[37m [39;49;00mthreads[37m [39;49;00mand[37m [39;49;00mthreads::shared[37m[39;49;00m$
[34mif[39;49;00m[37m [39;49;00mthe[37m [39;49;00menvironment[37m [39;49;00mvariable[37m [39;49;00mC<PERL5DB_THREADED>[37m [39;49;00mis[37m [39;49;00mset,[37m [39;49;00mto[37m [39;49;00menable[37m [39;49;00mproper[37m[39;49;00m$
threaded[37m [39;49;00mdebugger[37m [39;49;00mcontrol.[37m  [39;49;00mC<-dt>[37m [39;49;00mcan[37m [39;49;00malso[37m [39;49;00mbe[37m [39;49;00mused[37m [39;49;00mto[37m [39;49;00mset[37m [39;49;00m[34mthis[39;49;00m.[37m[39;49;00m$
[37m[39;49;00m$
Each[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00m[34mthread[39;49;00m[37m [39;49;00mwill[37m [39;49;00mbe[37m [39;49;00mannounced[37m [39;49;00mand[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mprompt[37m [39;49;00mwill[37m [39;49;00malways[37m [39;49;00minform[37m[39;49;00m$
you[37m [39;49;00mof[37m [39;49;00meach[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00m[34mthread[39;49;00m[37m [39;49;00mcreated.[37m  [39;49;00mIt[37m [39;49;00mwill[37m [39;49;00malso[37m [39;49;00mindicate[37m [39;49;00mthe[37m [39;49;00m[34mthread[39;49;00m[37m [39;49;00mid[37m [39;49;00min[37m [39;49;00mwhich[37m[39;49;00m$
we[37m [39;49;00mare[37m [39;49;00mcurrently[37m [39;49;00mrunning[37m [39;49;00mwithin[37m [39;49;00mthe[37m [39;49;00mprompt[37m [39;49;00mlike[37m [39;49;00m[34mthis[39;49;00m:[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00m[tid][37m [39;49;00mDB<$i>[37m[39;49;00m$
[37m[39;49;00m$
Where[37m [39;49;00mC<[tid]>[37m [39;49;00mis[37m [39;49;00man[37m [39;49;00minteger[37m [39;49;00m[34mthread[39;49;00m[37m [39;49;00mid[37m [39;49;00mand[37m [39;49;00mC<$i>[37m [39;49;00mis[37m [39;49;00mthe[37m [39;49;00mfamiliar[37m [39;49;00mdebugger[37m[39;49;00m$
command[37m [39;49;00mprompt.[37m  [39;49;00mThe[37m [39;49;00mprompt[37m [39;49;00mwill[37m [39;49;00mshow:[37m [39;49;00mC<[[34m0[39;49;00m]>[37m [39;49;00mwhen[37m [39;49;00mrunning[37m [39;49;00munder[37m [39;49;00mthreads,[37m [39;49;00mbut[37m[39;49;00m$
not[37m [39;49;00mactually[37m [39;49;00min[37m [39;49;00ma[37m [39;49;00m[34mthread[39;49;00m.[37m  [39;49;00mC<[tid]>[37m [39;49;00mis[37m [39;49;00mconsistent[37m [39;49;00mwith[37m [39;49;00mC<gdb>[37m [39;49;00musage.[37m[39;49;00m$
[37m[39;49;00m$
While[37m [39;49;00mrunning[37m [39;49;00munder[37m [39;49;00mthreads,[37m [39;49;00mwhen[37m [39;49;00myou[37m [39;49;00mset[37m [39;49;00mor[37m [39;49;00m[34mdelete[39;49;00m[37m [39;49;00ma[37m [39;49;00mbreakpoint[37m [39;49;00m(etc.),[37m [39;49;00m[34mthis[39;49;00m[37m[39;49;00m$
will[37m [39;49;00mapply[37m [39;49;00mto[37m [39;49;00mall[37m [39;49;00mthreads,[37m [39;49;00mnot[37m [39;49;00mjust[37m [39;49;00mthe[37m [39;49;00mcurrently[37m [39;49;00mrunning[37m [39;49;00mone.[37m  [39;49;00mWhen[37m [39;49;00myou[37m [39;49;00mare[37m [39;49;00m[37m[39;49;00m$
in[37m [39;49;00ma[37m [39;49;00mcurrently[37m [39;49;00mexecuting[37m [39;49;00m[34mthread[39;49;00m,[37m [39;49;00myou[37m [39;49;00mwill[37m [39;49;00mstay[37m [39;49;00mthere[37m [39;49;00muntil[37m [39;49;00mit[37m [39;49;00mcompletes.[37m  [39;49;00mWith[37m[39;49;00m$
the[37m [39;49;00mcurrent[37m [39;49;00mimplementation[37m [39;49;00mit[37m [39;49;00mis[37m [39;49;00mnot[37m [39;49;00mcurrently[37m [39;49;00mpossible[37m [39;49;00mto[37m [39;49;00mhop[37m [39;49;00mfrom[37m [39;49;00mone[37m [39;49;00m[34mthread[39;49;00m[37m[39;49;00m$
to[37m [39;49;00manother.[37m[39;49;00m$
[37m[39;49;00m$
The[37m [39;49;00mC<e>[37m [39;49;00mand[37m [39;49;00mC<E>[37m [39;49;00mcommands[37m [39;49;00mare[37m [39;49;00mcurrently[37m [39;49;00mfairly[37m [39;49;00mminimal[37m [39;49;00m-[37m [39;49;00msee[37m [39;49;00mC<h[37m [39;49;00me>[37m [39;49;00mand[37m [39;49;00mC<h[37m [39;49;00mE>.[37m[39;49;00m$
[37m[39;49;00m$
Note[37m [39;49;00mthat[37m [39;49;00mthreading[37m [39;49;00msupport[37m [39;49;00mwas[37m [39;49;00mbuilt[37m [39;49;00minto[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mas[37m [39;49;00mof[37m [39;49;00mPerl[37m [39;49;00mversion[37m[39;49;00m$
C<[34m5.8[39;49;00m[34m.6[39;49;00m>[37m [39;49;00mand[37m [39;49;00mdebugger[37m [39;49;00mversion[37m [39;49;00mC<[34m1.2[39;49;00m[34m.8[39;49;00m>.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
BEGIN[37m [39;49;00m{[37m[39;49;00m$
[37m  [39;49;00m[36m#[39;49;00m[36m ensure we can share our non-threaded variables or no-op[39;49;00m[36m[39;49;00m$
[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m($ENV{PERL5DB_THREADED})[37m [39;49;00m{[37m[39;49;00m$
[37m^I[39;49;00mrequire[37m [39;49;00mthreads;[37m[39;49;00m$
[37m^I[39;49;00mrequire[37m [39;49;00mthreads::shared;[37m[39;49;00m$
[37m^I[39;49;00m[34mimport[39;49;00m[37m [39;49;00mthreads::shared[37m [39;49;00m[32mqw[39;49;00m(share);[37m[39;49;00m$
[37m^I[39;49;00m$DBGR;[37m[39;49;00m$
[37m^I[39;49;00mshare([04m[91m\[39;49;00m$DBGR);[37m[39;49;00m$
[37m^I[39;49;00mlock($DBGR);[37m[39;49;00m$
[37m^I[39;49;00mprint[37m [39;49;00m[33m"[39;49;00m[33mThreads support enabled[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
[37m  [39;49;00m}[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m^I[39;49;00m*lock[37m  [39;49;00m=[37m [39;49;00msub(*)[37m [39;49;00m{};[37m[39;49;00m$
[37m^I[39;49;00m*share[37m [39;49;00m=[37m [39;49;00msub(*)[37m [39;49;00m{};[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m This would probably be better done with "use vars", but that wasn't around[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m when this code was originally written. (Neither was "use strict".) And on[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m the principle of not fiddling with something that was working, this was[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m left alone.[39;49;00m[36m[39;49;00m$
warn([37m               [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mDo[37m [39;49;00mnot[37m [39;49;00m;-)[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m These variables control the execution of 'dumpvar.pl'.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m$dumpvar::hashDepth,[37m[39;49;00m$
[37m    [39;49;00m$dumpvar::arrayDepth,[37m[39;49;00m$
[37m    [39;49;00m$dumpvar::dumpDBFiles,[37m[39;49;00m$
[37m    [39;49;00m$dumpvar::dumpPackages,[37m[39;49;00m$
[37m    [39;49;00m$dumpvar::quoteHighBit,[37m[39;49;00m$
[37m    [39;49;00m$dumpvar::printUndef,[37m[39;49;00m$
[37m    [39;49;00m$dumpvar::globPrint,[37m[39;49;00m$
[37m    [39;49;00m$dumpvar::usageOnly,[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m used to save @ARGV and extract any debugger-related flags.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[04m[91m@[39;49;00mARGS,[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m used to control die() reporting in diesignal()[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m$Carp::CarpLevel,[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m used to prevent multiple entries to diesignal()[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m (if for instance diesignal() itself dies)[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m$panic,[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m used to prevent the debugger from running nonstop[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m after a restart[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m$second_time,[37m[39;49;00m$
[37m  [39;49;00m)[37m[39;49;00m$
[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
foreach[37m [39;49;00mmy[37m [39;49;00m$k[37m [39;49;00m(keys[37m [39;49;00m(%INC))[37m [39;49;00m{[37m[39;49;00m$
[37m^I[39;49;00m&share([04m[91m\[39;49;00m$main::{[04m[91m'[39;49;00m_<[04m[91m'[39;49;00m.$filename});[37m[39;49;00m$
};[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m Command-line + PERLLIB:[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m Save the contents of @INC before they are modified elsewhere.[39;49;00m[36m[39;49;00m$
[04m[91m@[39;49;00mini_INC[37m [39;49;00m=[37m [39;49;00m[04m[91m@[39;49;00mINC;[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m This was an attempt to clear out the previous values of various[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m trapped errors. Apparently it didn't help. XXX More info needed![39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m $prevwarn = $prevdie = $prevbus = $prevsegv = ''; # Does not help?![39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m We set these variables to safe values. We don't want to blindly turn[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m off warnings, because other packages may still want them.[39;49;00m[36m[39;49;00m$
$trace[37m [39;49;00m=[37m [39;49;00m$signal[37m [39;49;00m=[37m [39;49;00m$single[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mUninitialized[37m [39;49;00mwarning[37m [39;49;00msuppression[37m[39;49;00m$
[37m                                   [39;49;00m[36m#[39;49;00m[36m (local $^W cannot help - other packages!).[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m Default to not exiting when program finishes; print the return[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m value when the 'r' command is used to return from a subroutine.[39;49;00m[36m[39;49;00m$
$inhibit_exit[37m [39;49;00m=[37m [39;49;00m$option{PrintRet}[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
=head1[37m [39;49;00mOPTION[37m [39;49;00mPROCESSING[37m[39;49;00m$
[37m[39;49;00m$
The[37m [39;49;00mdebugger[04m[91m'[39;49;00ms[37m [39;49;00moptions[37m [39;49;00mare[37m [39;49;00mactually[37m [39;49;00mspread[37m [39;49;00mout[37m [39;49;00mover[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mitself[37m [39;49;00mand[37m [39;49;00m[37m[39;49;00m$
C<dumpvar.pl>;[37m [39;49;00msome[37m [39;49;00mof[37m [39;49;00mthese[37m [39;49;00mare[37m [39;49;00mvariables[37m [39;49;00mto[37m [39;49;00mbe[37m [39;49;00mset,[37m [39;49;00m[34mwhile[39;49;00m[37m [39;49;00mothers[37m [39;49;00mare[37m [39;49;00m[37m[39;49;00m$
subs[37m [39;49;00mto[37m [39;49;00mbe[37m [39;49;00mcalled[37m [39;49;00mwith[37m [39;49;00ma[37m [39;49;00mvalue.[37m [39;49;00mTo[37m [39;49;00m[34mtry[39;49;00m[37m [39;49;00mto[37m [39;49;00mmake[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00ma[37m [39;49;00mlittle[37m [39;49;00measier[37m [39;49;00mto[37m[39;49;00m$
manage,[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00muses[37m [39;49;00ma[37m [39;49;00mfew[37m [39;49;00mdata[37m [39;49;00mstructures[37m [39;49;00mto[37m [39;49;00mdefine[37m [39;49;00mwhat[37m [39;49;00moptions[37m[39;49;00m$
are[37m [39;49;00mlegal[37m [39;49;00mand[37m [39;49;00mhow[37m [39;49;00mthey[37m [39;49;00mare[37m [39;49;00mto[37m [39;49;00mbe[37m [39;49;00mprocessed.[37m[39;49;00m$
[37m[39;49;00m$
First,[37m [39;49;00mthe[37m [39;49;00mC<[04m[91m@[39;49;00moptions>[37m [39;49;00marray[37m [39;49;00mdefines[37m [39;49;00mthe[37m [39;49;00mI<names>[37m [39;49;00mof[37m [39;49;00mall[37m [39;49;00mthe[37m [39;49;00moptions[37m [39;49;00mthat[37m[39;49;00m$
are[37m [39;49;00mto[37m [39;49;00mbe[37m [39;49;00maccepted.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[04m[91m@[39;49;00moptions[37m [39;49;00m=[37m [39;49;00mqw([37m[39;49;00m$
[37m  [39;49;00mCommandSet[37m[39;49;00m$
[37m  [39;49;00mhashDepth[37m    [39;49;00marrayDepth[37m    [39;49;00mdumpDepth[37m[39;49;00m$
[37m  [39;49;00mDumpDBFiles[37m  [39;49;00mDumpPackages[37m  [39;49;00mDumpReused[37m[39;49;00m$
[37m  [39;49;00mcompactDump[37m  [39;49;00mveryCompact[37m   [39;49;00mquote[37m[39;49;00m$
[37m  [39;49;00mHighBit[37m      [39;49;00mundefPrint[37m    [39;49;00mglobPrint[37m[39;49;00m$
[37m  [39;49;00mPrintRet[37m     [39;49;00mUsageOnly[37m     [39;49;00mframe[37m[39;49;00m$
[37m  [39;49;00mAutoTrace[37m    [39;49;00mTTY[37m           [39;49;00mnoTTY[37m[39;49;00m$
[37m  [39;49;00mReadLine[37m     [39;49;00mNonStop[37m       [39;49;00mLineInfo[37m[39;49;00m$
[37m  [39;49;00mmaxTraceLen[37m  [39;49;00mrecallCommand[37m [39;49;00mShellBang[37m[39;49;00m$
[37m  [39;49;00mpager[37m        [39;49;00mtkRunning[37m     [39;49;00mornaments[37m[39;49;00m$
[37m  [39;49;00msignalLevel[37m  [39;49;00mwarnLevel[37m     [39;49;00mdieLevel[37m[39;49;00m$
[37m  [39;49;00minhibit_exit[37m [39;49;00mImmediateStop[37m [39;49;00mbareStringify[37m[39;49;00m$
[37m  [39;49;00mCreateTTY[37m    [39;49;00mRemotePort[37m    [39;49;00mwindowSize[37m[39;49;00m$
[37m  [39;49;00mDollarCaretP[37m [39;49;00mOnlyAssertions[37m [39;49;00mWarnAssertions[37m[39;49;00m$
);[37m[39;49;00m$
[37m[39;49;00m$
[04m[91m@[39;49;00mRememberOnROptions[37m [39;49;00m=[37m [39;49;00mqw(DollarCaretP[37m [39;49;00mOnlyAssertions);[37m[39;49;00m$
[37m[39;49;00m$
=pod[37m[39;49;00m$
[37m[39;49;00m$
Second,[37m [39;49;00mC<optionVars>[37m [39;49;00mlists[37m [39;49;00mthe[37m [39;49;00mvariables[37m [39;49;00mthat[37m [39;49;00meach[37m [39;49;00moption[37m [39;49;00muses[37m [39;49;00mto[37m [39;49;00msave[37m [39;49;00mits[37m[39;49;00m$
state.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[32m%option[39;49;00mVars[37m [39;49;00m=[37m [39;49;00m([37m[39;49;00m$
[37m    [39;49;00mhashDepth[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::hashDepth,[37m[39;49;00m$
[37m    [39;49;00marrayDepth[37m    [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::arrayDepth,[37m[39;49;00m$
[37m    [39;49;00mCommandSet[37m    [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$CommandSet,[37m[39;49;00m$
[37m    [39;49;00mDumpDBFiles[37m   [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::dumpDBFiles,[37m[39;49;00m$
[37m    [39;49;00mDumpPackages[37m  [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::dumpPackages,[37m[39;49;00m$
[37m    [39;49;00mDumpReused[37m    [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::dumpReused,[37m[39;49;00m$
[37m    [39;49;00mHighBit[37m       [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::quoteHighBit,[37m[39;49;00m$
[37m    [39;49;00mundefPrint[37m    [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::printUndef,[37m[39;49;00m$
[37m    [39;49;00mglobPrint[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::globPrint,[37m[39;49;00m$
[37m    [39;49;00mUsageOnly[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::usageOnly,[37m[39;49;00m$
[37m    [39;49;00mCreateTTY[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$CreateTTY,[37m[39;49;00m$
[37m    [39;49;00mbareStringify[37m [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$dumpvar::bareStringify,[37m[39;49;00m$
[37m    [39;49;00mframe[37m         [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$frame,[37m[39;49;00m$
[37m    [39;49;00mAutoTrace[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$trace,[37m[39;49;00m$
[37m    [39;49;00minhibit_exit[37m  [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$inhibit_exit,[37m[39;49;00m$
[37m    [39;49;00mmaxTraceLen[37m   [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$maxtrace,[37m[39;49;00m$
[37m    [39;49;00mImmediateStop[37m [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$ImmediateStop,[37m[39;49;00m$
[37m    [39;49;00mRemotePort[37m    [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$remoteport,[37m[39;49;00m$
[37m    [39;49;00mwindowSize[37m    [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$window,[37m[39;49;00m$
[37m    [39;49;00mWarnAssertions[37m [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m$warnassertions,[37m[39;49;00m$
);[37m[39;49;00m$
[37m[39;49;00m$
=pod[37m[39;49;00m$
[37m[39;49;00m$
Third,[37m [39;49;00mC<[32m%option[39;49;00mAction>[37m [39;49;00mdefines[37m [39;49;00mthe[37m [39;49;00msubroutine[37m [39;49;00mto[37m [39;49;00mbe[37m [39;49;00mcalled[37m [39;49;00mto[37m [39;49;00mprocess[37m [39;49;00meach[37m[39;49;00m$
option.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m [39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[32m%option[39;49;00mAction[37m [39;49;00m=[37m [39;49;00m([37m[39;49;00m$
[37m    [39;49;00mcompactDump[37m   [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&dumpvar::compactDump,[37m[39;49;00m$
[37m    [39;49;00mveryCompact[37m   [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&dumpvar::veryCompact,[37m[39;49;00m$
[37m    [39;49;00mquote[37m         [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&dumpvar::quote,[37m[39;49;00m$
[37m    [39;49;00mTTY[37m           [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&TTY,[37m[39;49;00m$
[37m    [39;49;00mnoTTY[37m         [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&noTTY,[37m[39;49;00m$
[37m    [39;49;00mReadLine[37m      [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&ReadLine,[37m[39;49;00m$
[37m    [39;49;00mNonStop[37m       [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&NonStop,[37m[39;49;00m$
[37m    [39;49;00mLineInfo[37m      [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&LineInfo,[37m[39;49;00m$
[37m    [39;49;00mrecallCommand[37m [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&recallCommand,[37m[39;49;00m$
[37m    [39;49;00mShellBang[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&shellBang,[37m[39;49;00m$
[37m    [39;49;00mpager[37m         [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&pager,[37m[39;49;00m$
[37m    [39;49;00msignalLevel[37m   [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&signalLevel,[37m[39;49;00m$
[37m    [39;49;00mwarnLevel[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&warnLevel,[37m[39;49;00m$
[37m    [39;49;00mdieLevel[37m      [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&dieLevel,[37m[39;49;00m$
[37m    [39;49;00mtkRunning[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&tkRunning,[37m[39;49;00m$
[37m    [39;49;00mornaments[37m     [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&ornaments,[37m[39;49;00m$
[37m    [39;49;00mRemotePort[37m    [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&RemotePort,[37m[39;49;00m$
[37m    [39;49;00mDollarCaretP[37m  [39;49;00m=>[37m [39;49;00m[04m[91m\[39;49;00m&DollarCaretP,[37m[39;49;00m$
[37m    [39;49;00mOnlyAssertions=>[37m [39;49;00m[04m[91m\[39;49;00m&OnlyAssertions,[37m[39;49;00m$
);[37m[39;49;00m$
[37m[39;49;00m$
=pod[37m[39;49;00m$
[37m[39;49;00m$
Last,[37m [39;49;00mthe[37m [39;49;00mC<[32m%option[39;49;00mRequire>[37m [39;49;00mnotes[37m [39;49;00mmodules[37m [39;49;00mthat[37m [39;49;00mmust[37m [39;49;00mbe[37m [39;49;00mC<require>d[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00man[37m[39;49;00m$
option[37m [39;49;00mis[37m [39;49;00mused.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m Note that this list is not complete: several options not listed here[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m actually require that dumpvar.pl be loaded for them to work, but are[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m not in the table. A subsequent patch will correct this problem; for[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m the moment, we're just recommenting, and we are NOT going to change[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m function.[39;49;00m[36m[39;49;00m$
[32m%option[39;49;00mRequire[37m [39;49;00m=[37m [39;49;00m([37m[39;49;00m$
[37m    [39;49;00mcompactDump[37m [39;49;00m=>[37m [39;49;00m[04m[91m'[39;49;00mdumpvar.pl[04m[91m'[39;49;00m,[37m[39;49;00m$
[37m    [39;49;00mveryCompact[37m [39;49;00m=>[37m [39;49;00m[04m[91m'[39;49;00mdumpvar.pl[04m[91m'[39;49;00m,[37m[39;49;00m$
[37m    [39;49;00mquote[37m       [39;49;00m=>[37m [39;49;00m[04m[91m'[39;49;00mdumpvar.pl[04m[91m'[39;49;00m,[37m[39;49;00m$
);[37m[39;49;00m$
[37m[39;49;00m$
=pod[37m[39;49;00m$
[37m[39;49;00m$
There[37m [39;49;00mare[37m [39;49;00ma[37m [39;49;00mnumber[37m [39;49;00mof[37m [39;49;00minitialization-related[37m [39;49;00mvariables[37m [39;49;00mwhich[37m [39;49;00mcan[37m [39;49;00mbe[37m [39;49;00mset[37m[39;49;00m$
by[37m [39;49;00mputting[37m [39;49;00mcode[37m [39;49;00mto[37m [39;49;00mset[37m [39;49;00mthem[37m [39;49;00min[37m [39;49;00ma[37m [39;49;00mBEGIN[37m [39;49;00mblock[37m [39;49;00min[37m [39;49;00mthe[37m [39;49;00mC<PERL5DB>[37m [39;49;00menvironment[37m[39;49;00m$
variable.[37m [39;49;00mThese[37m [39;49;00mare:[37m[39;49;00m$
[37m[39;49;00m$
=over[37m [39;49;00m[34m4[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
=item[37m [39;49;00mC<$rl>[37m [39;49;00m-[37m [39;49;00mreadline[37m [39;49;00mcontrol[37m [39;49;00mXXX[37m [39;49;00mneeds[37m [39;49;00mmore[37m [39;49;00mexplanation[37m[39;49;00m$
[37m[39;49;00m$
=item[37m [39;49;00mC<$warnLevel>[37m [39;49;00m-[37m [39;49;00mwhether[37m [39;49;00mor[37m [39;49;00mnot[37m [39;49;00mdebugger[37m [39;49;00mtakes[37m [39;49;00mover[37m [39;49;00mwarning[37m [39;49;00mhandling[37m[39;49;00m$
[37m[39;49;00m$
=item[37m [39;49;00mC<$dieLevel>[37m [39;49;00m-[37m [39;49;00mwhether[37m [39;49;00mor[37m [39;49;00mnot[37m [39;49;00mdebugger[37m [39;49;00mtakes[37m [39;49;00mover[37m [39;49;00mdie[37m [39;49;00mhandling[37m[39;49;00m$
[37m[39;49;00m$
=item[37m [39;49;00mC<$signalLevel>[37m [39;49;00m-[37m [39;49;00mwhether[37m [39;49;00mor[37m [39;49;00mnot[37m [39;49;00mdebugger[37m [39;49;00mtakes[37m [39;49;00mover[37m [39;49;00msignal[37m [39;49;00mhandling[37m[39;49;00m$
[37m[39;49;00m$
=item[37m [39;49;00mC<$pre>[37m [39;49;00m-[37m [39;49;00mpreprompt[37m [39;49;00mactions[37m [39;49;00m(array[37m [39;49;00mreference)[37m[39;49;00m$
[37m[39;49;00m$
=item[37m [39;49;00mC<$post>[37m [39;49;00m-[37m [39;49;00mpostprompt[37m [39;49;00mactions[37m [39;49;00m(array[37m [39;49;00mreference)[37m[39;49;00m$
[37m[39;49;00m$
=item[37m [39;49;00mC<$pretype>[37m[39;49;00m$
[37m[39;49;00m$
=item[37m [39;49;00mC<$CreateTTY>[37m [39;49;00m-[37m [39;49;00mwhether[37m [39;49;00mor[37m [39;49;00mnot[37m [39;49;00mto[37m [39;49;00mcreate[37m [39;49;00ma[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mTTY[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00mdebugger[37m[39;49;00m$
[37m[39;49;00m$
=item[37m [39;49;00mC<$CommandSet>[37m [39;49;00m-[37m [39;49;00mwhich[37m [39;49;00mcommand[37m [39;49;00mset[37m [39;49;00mto[37m [39;49;00muse[37m [39;49;00m(defaults[37m [39;49;00mto[37m [39;49;00m[34mnew[39;49;00m,[37m [39;49;00mdocumented[37m [39;49;00mset)[37m[39;49;00m$
[37m[39;49;00m$
=back[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m These guys may be defined in $ENV{PERL5DB} :[39;49;00m[36m[39;49;00m$
$rl[37m          [39;49;00m=[37m [39;49;00m[34m1[39;49;00m[37m     [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$rl;[37m[39;49;00m$
$warnLevel[37m   [39;49;00m=[37m [39;49;00m[34m1[39;49;00m[37m     [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$warnLevel;[37m[39;49;00m$
$dieLevel[37m    [39;49;00m=[37m [39;49;00m[34m1[39;49;00m[37m     [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$dieLevel;[37m[39;49;00m$
$signalLevel[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m[37m     [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$signalLevel;[37m[39;49;00m$
$pre[37m         [39;49;00m=[37m [39;49;00m[][37m    [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$pre;[37m[39;49;00m$
$post[37m        [39;49;00m=[37m [39;49;00m[][37m    [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$post;[37m[39;49;00m$
$pretype[37m     [39;49;00m=[37m [39;49;00m[][37m    [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$pretype;[37m[39;49;00m$
$CreateTTY[37m   [39;49;00m=[37m [39;49;00m[34m3[39;49;00m[37m     [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$CreateTTY;[37m[39;49;00m$
$CommandSet[37m  [39;49;00m=[37m [39;49;00m[04m[91m'[39;49;00m[34m580[39;49;00m[04m[91m'[39;49;00m[37m [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$CommandSet;[37m[39;49;00m$
[37m[39;49;00m$
share($rl);[37m[39;49;00m$
share($warnLevel);[37m[39;49;00m$
share($dieLevel);[37m[39;49;00m$
share($signalLevel);[37m[39;49;00m$
share($pre);[37m[39;49;00m$
share($post);[37m[39;49;00m$
share($pretype);[37m[39;49;00m$
share($rl);[37m[39;49;00m$
share($CreateTTY);[37m[39;49;00m$
share($CommandSet);[37m[39;49;00m$
[37m[39;49;00m$
=pod[37m[39;49;00m$
[37m[39;49;00m$
The[37m [39;49;00m[34mdefault[39;49;00m[37m [39;49;00mC<die>,[37m [39;49;00mC<warn>,[37m [39;49;00mand[37m [39;49;00mC<signal>[37m [39;49;00mhandlers[37m [39;49;00mare[37m [39;49;00mset[37m [39;49;00mup.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
warnLevel($warnLevel);[37m[39;49;00m$
dieLevel($dieLevel);[37m[39;49;00m$
signalLevel($signalLevel);[37m[39;49;00m$
[37m[39;49;00m$
=pod[37m[39;49;00m$
[37m[39;49;00m$
The[37m [39;49;00mpager[37m [39;49;00mto[37m [39;49;00mbe[37m [39;49;00mused[37m [39;49;00mis[37m [39;49;00mneeded[37m [39;49;00mnext.[37m [39;49;00mWe[37m [39;49;00m[34mtry[39;49;00m[37m [39;49;00mto[37m [39;49;00mget[37m [39;49;00mit[37m [39;49;00mfrom[37m [39;49;00mthe[37m[39;49;00m$
environment[37m [39;49;00mfirst.[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00mit[04m[91m'[39;49;00ms[37m [39;49;00mnot[37m [39;49;00mdefined[37m [39;49;00mthere,[37m [39;49;00mwe[37m [39;49;00m[34mtry[39;49;00m[37m [39;49;00mto[37m [39;49;00mfind[37m [39;49;00mit[37m [39;49;00min[37m[39;49;00m$
the[37m [39;49;00mPerl[37m [39;49;00mC<Config.pm>.[37m  [39;49;00mIf[37m [39;49;00mit[04m[91m'[39;49;00ms[37m [39;49;00mnot[37m [39;49;00mthere,[37m [39;49;00mwe[37m [39;49;00m[34mdefault[39;49;00m[37m [39;49;00mto[37m [39;49;00mC<more>.[37m [39;49;00mWe[37m[39;49;00m$
then[37m [39;49;00mcall[37m [39;49;00mthe[37m [39;49;00mC<pager()>[37m [39;49;00mfunction[37m [39;49;00mto[37m [39;49;00msave[37m [39;49;00mthe[37m [39;49;00mpager[37m [39;49;00mname.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m This routine makes sure $pager is set up so that '|' can use it.[39;49;00m[36m[39;49;00m$
pager([37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m If PAGER is defined in the environment, use it.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00mdefined[37m [39;49;00m$ENV{PAGER}[37m[39;49;00m$
[37m    [39;49;00m?[37m [39;49;00m$ENV{PAGER}[37m[39;49;00m$
[37m[39;49;00m$
[37m      [39;49;00m[36m#[39;49;00m[36m If not, see if Config.pm defines it.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m:[37m [39;49;00meval[37m [39;49;00m{[37m [39;49;00mrequire[37m [39;49;00mConfig[37m [39;49;00m}[37m[39;49;00m$
[37m      [39;49;00m&&[37m [39;49;00mdefined[37m [39;49;00m$Config::Config{pager}[37m[39;49;00m$
[37m    [39;49;00m?[37m [39;49;00m$Config::Config{pager}[37m[39;49;00m$
[37m[39;49;00m$
[37m      [39;49;00m[36m#[39;49;00m[36m If not, fall back to 'more'.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m:[37m [39;49;00m[04m[91m'[39;49;00mmore[04m[91m'[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m)[37m[39;49;00m$
[37m  [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$pager;[37m[39;49;00m$
[37m[39;49;00m$
=pod[37m[39;49;00m$
[37m[39;49;00m$
We[37m [39;49;00mset[37m [39;49;00mup[37m [39;49;00mthe[37m [39;49;00mcommand[37m [39;49;00mto[37m [39;49;00mbe[37m [39;49;00mused[37m [39;49;00mto[37m [39;49;00maccess[37m [39;49;00mthe[37m [39;49;00mman[37m [39;49;00mpages,[37m [39;49;00mthe[37m [39;49;00mcommand[37m[39;49;00m$
recall[37m [39;49;00mcharacter[37m [39;49;00m(C<!>[37m [39;49;00munless[37m [39;49;00motherwise[37m [39;49;00mdefined)[37m [39;49;00mand[37m [39;49;00mthe[37m [39;49;00mshell[37m [39;49;00mescape[37m[39;49;00m$
character[37m [39;49;00m(C<!>[37m [39;49;00munless[37m [39;49;00motherwise[37m [39;49;00mdefined).[37m [39;49;00mYes,[37m [39;49;00mthese[37m [39;49;00m[34mdo[39;49;00m[37m [39;49;00mconflict,[37m [39;49;00mand[37m[39;49;00m$
neither[37m [39;49;00mworks[37m [39;49;00min[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mat[37m [39;49;00mthe[37m [39;49;00mmoment.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
setman();[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m Set up defaults for command recall and shell escape (note:[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m these currently don't work in linemode debugging).[39;49;00m[36m[39;49;00m$
&recallCommand([33m"[39;49;00m[33m![39;49;00m[33m"[39;49;00m)[37m [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$prc;[37m[39;49;00m$
&shellBang([33m"[39;49;00m[33m![39;49;00m[33m"[39;49;00m)[37m     [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$psh;[37m[39;49;00m$
[37m[39;49;00m$
=pod[37m[39;49;00m$
[37m[39;49;00m$
We[37m [39;49;00mthen[37m [39;49;00mset[37m [39;49;00mup[37m [39;49;00mthe[37m [39;49;00mgigantic[37m [39;49;00mstring[37m [39;49;00mcontaining[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mhelp.[37m[39;49;00m$
We[37m [39;49;00malso[37m [39;49;00mset[37m [39;49;00mthe[37m [39;49;00mlimit[37m [39;49;00mon[37m [39;49;00mthe[37m [39;49;00mnumber[37m [39;49;00mof[37m [39;49;00marguments[37m [39;49;00mwe[04m[91m'[39;49;00mll[37m [39;49;00mdisplay[37m [39;49;00mduring[37m [39;49;00ma[37m[39;49;00m$
trace.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
sethelp();[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m If we didn't get a default for the length of eval[39;49;00m[36m/[39;49;00m[36mstack trace args,[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m set it here.[39;49;00m[36m[39;49;00m$
$maxtrace[37m [39;49;00m=[37m [39;49;00m[34m400[39;49;00m[37m [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$maxtrace;[37m[39;49;00m$
[37m[39;49;00m$
=head2[37m [39;49;00mSETTING[37m [39;49;00mUP[37m [39;49;00mTHE[37m [39;49;00mDEBUGGER[37m [39;49;00mGREETING[37m[39;49;00m$
[37m[39;49;00m$
The[37m [39;49;00mdebugger[37m [39;49;00mI<greeting>[37m [39;49;00mhelps[37m [39;49;00mto[37m [39;49;00minform[37m [39;49;00mthe[37m [39;49;00muser[37m [39;49;00mhow[37m [39;49;00mmany[37m [39;49;00mdebuggers[37m [39;49;00mare[37m[39;49;00m$
running,[37m [39;49;00mand[37m [39;49;00mwhether[37m [39;49;00mthe[37m [39;49;00mcurrent[37m [39;49;00mdebugger[37m [39;49;00mis[37m [39;49;00mthe[37m [39;49;00mprimary[37m [39;49;00mor[37m [39;49;00ma[37m [39;49;00mchild.[37m[39;49;00m$
[37m[39;49;00m$
If[37m [39;49;00mwe[37m [39;49;00mare[37m [39;49;00mthe[37m [39;49;00mprimary,[37m [39;49;00mwe[37m [39;49;00mjust[37m [39;49;00mhang[37m [39;49;00monto[37m [39;49;00mour[37m [39;49;00mpid[37m [39;49;00mso[37m [39;49;00mwe[04m[91m'[39;49;00mll[37m [39;49;00mhave[37m [39;49;00mit[37m [39;49;00mwhen[37m[39;49;00m$
or[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mwe[37m [39;49;00mstart[37m [39;49;00ma[37m [39;49;00mchild[37m [39;49;00mdebugger.[37m [39;49;00mIf[37m [39;49;00mwe[37m [39;49;00mare[37m [39;49;00ma[37m [39;49;00mchild,[37m [39;49;00mwe[04m[91m'[39;49;00mll[37m [39;49;00mset[37m [39;49;00mthings[37m [39;49;00mup[37m[39;49;00m$
so[37m [39;49;00mwe[04m[91m'[39;49;00mll[37m [39;49;00mhave[37m [39;49;00ma[37m [39;49;00munique[37m [39;49;00mgreeting[37m [39;49;00mand[37m [39;49;00mso[37m [39;49;00mthe[37m [39;49;00mparent[37m [39;49;00mwill[37m [39;49;00mgive[37m [39;49;00mus[37m [39;49;00mour[37m [39;49;00mown[37m[39;49;00m$
TTY[37m [39;49;00mlater.[37m[39;49;00m$
[37m[39;49;00m$
We[37m [39;49;00msave[37m [39;49;00mthe[37m [39;49;00mcurrent[37m [39;49;00mcontents[37m [39;49;00mof[37m [39;49;00mthe[37m [39;49;00mC<PERLDB_PIDS>[37m [39;49;00menvironment[37m [39;49;00mvariable[37m[39;49;00m$
because[37m [39;49;00mwe[37m [39;49;00mmess[37m [39;49;00maround[37m [39;49;00mwith[37m [39;49;00mit.[37m [39;49;00mWe[04m[91m'[39;49;00mll[37m [39;49;00malso[37m [39;49;00mneed[37m [39;49;00mto[37m [39;49;00mhang[37m [39;49;00monto[37m [39;49;00mit[37m [39;49;00mbecause[37m[39;49;00m$
we[04m[91m'[39;49;00mll[37m [39;49;00mneed[37m [39;49;00mit[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mwe[37m [39;49;00mrestart.[37m[39;49;00m$
[37m[39;49;00m$
Child[37m [39;49;00mdebuggers[37m [39;49;00mmake[37m [39;49;00ma[37m [39;49;00mlabel[37m [39;49;00mout[37m [39;49;00mof[37m [39;49;00mthe[37m [39;49;00mcurrent[37m [39;49;00mPID[37m [39;49;00mstructure[37m [39;49;00mrecorded[37m [39;49;00min[37m[39;49;00m$
PERLDB_PIDS[37m [39;49;00mplus[37m [39;49;00mthe[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPID.[37m [39;49;00mThey[37m [39;49;00malso[37m [39;49;00mmark[37m [39;49;00mthemselves[37m [39;49;00mas[37m [39;49;00mnot[37m [39;49;00mhaving[37m [39;49;00ma[37m [39;49;00mTTY[37m[39;49;00m$
yet[37m [39;49;00mso[37m [39;49;00mthe[37m [39;49;00mparent[37m [39;49;00mwill[37m [39;49;00mgive[37m [39;49;00mthem[37m [39;49;00mone[37m [39;49;00mlater[37m [39;49;00mvia[37m [39;49;00mC<resetterm()>.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m Save the current contents of the environment; we're about to[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m much with it. We'll need this if we have to restart.[39;49;00m[36m[39;49;00m$
$ini_pids[37m [39;49;00m=[37m [39;49;00m$ENV{PERLDB_PIDS};[37m[39;49;00m$
[37m[39;49;00m$
[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00mdefined[37m [39;49;00m$ENV{PERLDB_PIDS}[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m We're a child. Make us a label out of the current PID structure[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m recorded in PERLDB_PIDS plus our (new) PID. Mark us as not having[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m a term yet so the parent will give us one later via resetterm().[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m$pids[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m[$ENV{PERLDB_PIDS}][39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m$ENV{PERLDB_PIDS}[37m [39;49;00m.=[37m [39;49;00m[33m"[39;49;00m[33m->$$[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m$term_pid[37m [39;49;00m=[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(defined[37m [39;49;00m$ENV{PERLDB_PIDS...[37m[39;49;00m$
[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m We're the parent PID. Initialize PERLDB_PID in case we end up with a[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m child debugger, and mark us as the parent, so we'll know to set up[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m more TTY's is we have to.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m$ENV{PERLDB_PIDS}[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m$$[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m$pids[37m             [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m{pid=$$}[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m$term_pid[37m         [39;49;00m=[37m [39;49;00m$$;[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
$pidprompt[37m [39;49;00m=[37m [39;49;00m[04m[91m'[39;49;00m[04m[91m'[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m Sets up $emacs as a synonym for $slave_editor.[39;49;00m[36m[39;49;00m$
*emacs[37m [39;49;00m=[37m [39;49;00m$slave_editor[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m$slave_editor;[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mMay[37m [39;49;00mbe[37m [39;49;00mused[37m [39;49;00min[37m [39;49;00mafterinit()...[37m[39;49;00m$
[37m[39;49;00m$
=head2[37m [39;49;00mREADING[37m [39;49;00mTHE[37m [39;49;00mRC[37m [39;49;00m[36mFILE[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
The[37m [39;49;00mdebugger[37m [39;49;00mwill[37m [39;49;00mread[37m [39;49;00ma[37m [39;49;00mfile[37m [39;49;00mof[37m [39;49;00minitialization[37m [39;49;00moptions[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00msupplied.[37m [39;49;00mIf[37m    [39;49;00m[37m[39;49;00m$
running[37m [39;49;00minteractively,[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00mis[37m [39;49;00mC<.perldb>;[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mnot,[37m [39;49;00mit[04m[91m'[39;49;00ms[37m [39;49;00mC<perldb.ini>.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m      [39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m As noted, this test really doesn't check accurately that the debugger[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m is running at a terminal or not.[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m-e[37m [39;49;00m[33m"[39;49;00m[33m/dev/tty[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m                      [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00mis[37m [39;49;00mthe[37m [39;49;00mwrong[37m [39;49;00mmetric![37m[39;49;00m$
[37m    [39;49;00m$rcfile[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m.perldb[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
}[37m[39;49;00m$
[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00m$rcfile[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mperldb.ini[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
=pod[37m[39;49;00m$
[37m[39;49;00m$
The[37m [39;49;00mdebugger[37m [39;49;00mdoes[37m [39;49;00ma[37m [39;49;00msafety[37m [39;49;00mtest[37m [39;49;00mof[37m [39;49;00mthe[37m [39;49;00mfile[37m [39;49;00mto[37m [39;49;00mbe[37m [39;49;00mread.[37m [39;49;00mIt[37m [39;49;00mmust[37m [39;49;00mbe[37m [39;49;00mowned[37m[39;49;00m$
either[37m [39;49;00mby[37m [39;49;00mthe[37m [39;49;00mcurrent[37m [39;49;00muser[37m [39;49;00mor[37m [39;49;00mroot,[37m [39;49;00mand[37m [39;49;00mmust[37m [39;49;00monly[37m [39;49;00mbe[37m [39;49;00mwritable[37m [39;49;00mby[37m [39;49;00mthe[37m [39;49;00mowner.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m This wraps a safety test around "do" to read and evaluate the init file.[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m This isn't really safe, because there's a race[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m between checking and opening.  The solution is to[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m open and fstat the handle, but then you have to read and[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m eval the contents.  But then the silly thing gets[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m your lexical scope, which is unfortunate at best.[39;49;00m[36m[39;49;00m$
sub[37m [39;49;00msafe_do[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mmy[37m [39;49;00m$file[37m [39;49;00m=[37m [39;49;00mshift;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m Just exactly what part of the word "CORE::" don't you understand?[39;49;00m[36m[39;49;00m$
[37m    [39;49;00mlocal[37m [39;49;00m$SIG{__WARN__};[37m[39;49;00m$
[37m    [39;49;00mlocal[37m [39;49;00m$SIG{__DIE__};[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00munless[37m [39;49;00m([37m [39;49;00mis_safe_file($file)[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00mCORE::warn[37m [39;49;00m<<EO_GRIPE;[37m[39;49;00m$
perldb:[37m [39;49;00mMust[37m [39;49;00mnot[37m [39;49;00msource[37m [39;49;00minsecure[37m [39;49;00mrcfile[37m [39;49;00m$file.[37m[39;49;00m$
[37m        [39;49;00mYou[37m [39;49;00mor[37m [39;49;00mthe[37m [39;49;00msuperuser[37m [39;49;00mmust[37m [39;49;00mbe[37m [39;49;00mthe[37m [39;49;00mowner,[37m [39;49;00mand[37m [39;49;00mit[37m [39;49;00mmust[37m [39;49;00mnot[37m [39;49;00m[37m[39;49;00m$
[37m        [39;49;00mbe[37m [39;49;00mwritable[37m [39;49;00mby[37m [39;49;00manyone[37m [39;49;00mbut[37m [39;49;00mits[37m [39;49;00mowner.[37m[39;49;00m$
EO_GRIPE[37m[39;49;00m$
[37m        [39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00munless[37m [39;49;00m(is_safe_file($file...[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mdo[39;49;00m[37m [39;49;00m$file;[37m[39;49;00m$
[37m    [39;49;00mCORE::warn([33m"[39;49;00m[33mperldb: couldn't parse $file: $@[39;49;00m[33m"[39;49;00m)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m$[04m[91m@[39;49;00m;[37m[39;49;00m$
}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00msub[37m [39;49;00msafe_do[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m This is the safety test itself.[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m Verifies that owner is either real user or superuser and that no[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m one but owner may write to it.  This function is of limited use[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m when called on a path instead of upon a handle, because there are[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m no guarantees that filename (by dirent) whose file (by ino) is[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m eventually accessed is the same as the one tested.[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m Assumes that the file's existence is not in doubt.[39;49;00m[36m[39;49;00m$
sub[37m [39;49;00mis_safe_file[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mmy[37m [39;49;00m$path[37m [39;49;00m=[37m [39;49;00mshift;[37m[39;49;00m$
[37m    [39;49;00mstat($path)[37m [39;49;00m||[37m [39;49;00m[34mreturn[39;49;00m;[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mmysteriously[37m [39;49;00mvaporized[37m[39;49;00m$
[37m    [39;49;00mmy[37m [39;49;00m([37m [39;49;00m$dev,[37m [39;49;00m$ino,[37m [39;49;00m$mode,[37m [39;49;00m$nlink,[37m [39;49;00m$uid,[37m [39;49;00m$gid[37m [39;49;00m)[37m [39;49;00m=[37m [39;49;00mstat(_);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m$uid[37m [39;49;00m!=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m$uid[37m [39;49;00m!=[37m [39;49;00m$<;[37m[39;49;00m$
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m$mode[37m [39;49;00m&[37m [39;49;00m[34m022[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00msub[37m [39;49;00mis_safe_file[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m If the rcfile (whichever one we decided was the right one to read)[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m exists, we safely do it.[39;49;00m[36m[39;49;00m$
[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m-f[37m [39;49;00m$rcfile[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00msafe_do([33m"[39;49;00m[33m./$rcfile[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m If there isn't one here, try the user's home directory.[39;49;00m[36m[39;49;00m$
elsif[37m [39;49;00m([37m [39;49;00mdefined[37m [39;49;00m$ENV{HOME}[37m [39;49;00m&&[37m [39;49;00m-f[37m [39;49;00m[33m"[39;49;00m[33m$ENV{HOME}/$rcfile[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00msafe_do([33m"[39;49;00m[33m$ENV{HOME}/$rcfile[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m Else try the login directory.[39;49;00m[36m[39;49;00m$
elsif[37m [39;49;00m([37m [39;49;00mdefined[37m [39;49;00m$ENV{LOGDIR}[37m [39;49;00m&&[37m [39;49;00m-f[37m [39;49;00m[33m"[39;49;00m[33m$ENV{LOGDIR}/$rcfile[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00msafe_do([33m"[39;49;00m[33m$ENV{LOGDIR}/$rcfile[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m If the PERLDB_OPTS variable has options in it, parse those out next.[39;49;00m[36m[39;49;00m$
[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00mdefined[37m [39;49;00m$ENV{PERLDB_OPTS}[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mparse_options([37m [39;49;00m$ENV{PERLDB_OPTS}[37m [39;49;00m);[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
=pod[37m[39;49;00m$
[37m[39;49;00m$
The[37m [39;49;00mlast[37m [39;49;00mthing[37m [39;49;00mwe[37m [39;49;00m[34mdo[39;49;00m[37m [39;49;00mduring[37m [39;49;00minitialization[37m [39;49;00mis[37m [39;49;00mdetermine[37m [39;49;00mwhich[37m [39;49;00msubroutine[37m [39;49;00mis[37m[39;49;00m$
to[37m [39;49;00mbe[37m [39;49;00mused[37m [39;49;00mto[37m [39;49;00mobtain[37m [39;49;00ma[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mterminal[37m [39;49;00mwhen[37m [39;49;00ma[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mdebugger[37m [39;49;00mis[37m [39;49;00mstarted.[37m [39;49;00mRight[37m [39;49;00mnow,[37m[39;49;00m$
the[37m [39;49;00mdebugger[37m [39;49;00monly[37m [39;49;00mhandles[37m [39;49;00mX[37m [39;49;00mWindows[37m [39;49;00mand[37m [39;49;00mOS/[34m2.[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m Set up the get_fork_TTY subroutine to be aliased to the proper routine.[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m Works if you're running an xterm or xterm-like window, or you're on[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m OS[39;49;00m[36m/[39;49;00m[36m2. This may need some expansion: for instance, this doesn't handle[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m OS X Terminal windows.[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[34mif[39;49;00m[37m [39;49;00m([37m[39;49;00m$
[37m    [39;49;00mnot[37m [39;49;00mdefined[37m [39;49;00m&get_fork_TTY[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mno[37m [39;49;00mroutine[37m [39;49;00mexists,[37m[39;49;00m$
[37m    [39;49;00mand[37m [39;49;00mdefined[37m [39;49;00m$ENV{TERM}[37m       [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mand[37m [39;49;00mwe[37m [39;49;00mknow[37m [39;49;00mwhat[37m [39;49;00mkind[37m[39;49;00m$
[37m                                 [39;49;00m[36m#[39;49;00m[36m of terminal this is,[39;49;00m[36m[39;49;00m$
[37m    [39;49;00mand[37m [39;49;00m$ENV{TERM}[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mxterm[04m[91m'[39;49;00m[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mand[37m [39;49;00mit[04m[91m'[39;49;00ms[37m [39;49;00man[37m [39;49;00mxterm,[37m[39;49;00m$
[36m#[39;49;00m[36m   and defined $ENV{WINDOWID}   # and we know what window this is, <- wrong metric[39;49;00m[36m[39;49;00m$
[37m    [39;49;00mand[37m [39;49;00mdefined[37m [39;49;00m$ENV{DISPLAY}[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mand[37m [39;49;00mwhat[37m [39;49;00mdisplay[37m [39;49;00mit[04m[91m'[39;49;00ms[37m [39;49;00mon,[37m[39;49;00m$
[37m  [39;49;00m)[37m[39;49;00m$
{[37m[39;49;00m$
[37m    [39;49;00m*get_fork_TTY[37m [39;49;00m=[37m [39;49;00m[04m[91m\[39;49;00m&xterm_get_fork_TTY;[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00muse[37m [39;49;00mthe[37m [39;49;00mxterm[37m [39;49;00mversion[37m[39;49;00m$
}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(not[37m [39;49;00mdefined[37m [39;49;00m&get_fork_TTY...[37m[39;49;00m$
elsif[37m [39;49;00m([37m [39;49;00m$^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mos2[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m                     [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mIf[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00mis[37m [39;49;00mOS/[34m2[39;49;00m,[37m[39;49;00m$
[37m    [39;49;00m*get_fork_TTY[37m [39;49;00m=[37m [39;49;00m[04m[91m\[39;49;00m&os2_get_fork_TTY;[37m      [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00muse[37m [39;49;00mthe[37m [39;49;00mOS/[34m2[39;49;00m[37m [39;49;00mversion[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m untaint $^O, which may have been tainted by the last statement.[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m see bug [perl #24674][39;49;00m[36m[39;49;00m$
$^O[37m [39;49;00m=~[37m [39;49;00mm/^(.*)[04m[91m\[39;49;00mz/;[37m[39;49;00m$
$^O[37m [39;49;00m=[37m [39;49;00m$1;[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m Here begin the unreadable code.  It needs fixing.[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
=head2[37m [39;49;00mRESTART[37m [39;49;00mPROCESSING[37m[39;49;00m$
[37m[39;49;00m$
This[37m [39;49;00msection[37m [39;49;00mhandles[37m [39;49;00mthe[37m [39;49;00mrestart[37m [39;49;00mcommand.[37m [39;49;00mWhen[37m [39;49;00mthe[37m [39;49;00mC<R>[37m [39;49;00mcommand[37m [39;49;00mis[37m [39;49;00minvoked,[37m [39;49;00mit[37m[39;49;00m$
tries[37m [39;49;00mto[37m [39;49;00mcapture[37m [39;49;00mall[37m [39;49;00mof[37m [39;49;00mthe[37m [39;49;00mstate[37m [39;49;00mit[37m [39;49;00mcan[37m [39;49;00minto[37m [39;49;00menvironment[37m [39;49;00mvariables,[37m [39;49;00mand[37m[39;49;00m$
then[37m [39;49;00msets[37m [39;49;00mC<PERLDB_RESTART>.[37m [39;49;00mWhen[37m [39;49;00mwe[37m [39;49;00mstart[37m [39;49;00mexecuting[37m [39;49;00magain,[37m [39;49;00mwe[37m [39;49;00mcheck[37m [39;49;00mto[37m [39;49;00msee[37m[39;49;00m$
[34mif[39;49;00m[37m [39;49;00mC<PERLDB_RESTART>[37m [39;49;00mis[37m [39;49;00mthere;[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mso,[37m [39;49;00mwe[37m [39;49;00mreload[37m [39;49;00mall[37m [39;49;00mthe[37m [39;49;00minformation[37m [39;49;00mthat[37m[39;49;00m$
the[37m [39;49;00mR[37m [39;49;00mcommand[37m [39;49;00mstuffed[37m [39;49;00minto[37m [39;49;00mthe[37m [39;49;00menvironment[37m [39;49;00mvariables.[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00mPERLDB_RESTART[37m   [39;49;00m-[37m [39;49;00mflag[37m [39;49;00monly,[37m [39;49;00mcontains[37m [39;49;00mno[37m [39;49;00mrestart[37m [39;49;00mdata[37m [39;49;00mitself.[37m       [39;49;00m[37m[39;49;00m$
[37m  [39;49;00mPERLDB_HIST[37m      [39;49;00m-[37m [39;49;00mcommand[37m [39;49;00mhistory,[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mit[04m[91m'[39;49;00ms[37m [39;49;00mavailable[37m[39;49;00m$
[37m  [39;49;00mPERLDB_ON_LOAD[37m   [39;49;00m-[37m [39;49;00mbreakpoints[37m [39;49;00mset[37m [39;49;00mby[37m [39;49;00mthe[37m [39;49;00mrc[37m [39;49;00mfile[37m[39;49;00m$
[37m  [39;49;00mPERLDB_POSTPONE[37m  [39;49;00m-[37m [39;49;00msubs[37m [39;49;00mthat[37m [39;49;00mhave[37m [39;49;00mbeen[37m [39;49;00mloaded/not[37m [39;49;00mexecuted,[37m [39;49;00mand[37m [39;49;00mhave[37m [39;49;00mactions[37m[39;49;00m$
[37m  [39;49;00mPERLDB_VISITED[37m   [39;49;00m-[37m [39;49;00mfiles[37m [39;49;00mthat[37m [39;49;00mhad[37m [39;49;00mbreakpoints[37m[39;49;00m$
[37m  [39;49;00mPERLDB_FILE_...[37m  [39;49;00m-[37m [39;49;00mbreakpoints[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00ma[37m [39;49;00mfile[37m[39;49;00m$
[37m  [39;49;00mPERLDB_OPT[37m       [39;49;00m-[37m [39;49;00mactive[37m [39;49;00moptions[37m[39;49;00m$
[37m  [39;49;00mPERLDB_INC[37m       [39;49;00m-[37m [39;49;00mthe[37m [39;49;00moriginal[37m [39;49;00m[04m[91m@[39;49;00mINC[37m[39;49;00m$
[37m  [39;49;00mPERLDB_PRETYPE[37m   [39;49;00m-[37m [39;49;00mpreprompt[37m [39;49;00mdebugger[37m [39;49;00mactions[37m[39;49;00m$
[37m  [39;49;00mPERLDB_PRE[37m       [39;49;00m-[37m [39;49;00mpreprompt[37m [39;49;00mPerl[37m [39;49;00mcode[37m[39;49;00m$
[37m  [39;49;00mPERLDB_POST[37m      [39;49;00m-[37m [39;49;00mpost-prompt[37m [39;49;00mPerl[37m [39;49;00mcode[37m[39;49;00m$
[37m  [39;49;00mPERLDB_TYPEAHEAD[37m [39;49;00m-[37m [39;49;00mtypeahead[37m [39;49;00mcaptured[37m [39;49;00mby[37m [39;49;00mreadline()[37m[39;49;00m$
[37m[39;49;00m$
We[37m [39;49;00mchug[37m [39;49;00mthrough[37m [39;49;00mall[37m [39;49;00mthese[37m [39;49;00mvariables[37m [39;49;00mand[37m [39;49;00mplug[37m [39;49;00mthe[37m [39;49;00mvalues[37m [39;49;00msaved[37m [39;49;00min[37m [39;49;00mthem[37m[39;49;00m$
back[37m [39;49;00minto[37m [39;49;00mthe[37m [39;49;00mappropriate[37m [39;49;00mspots[37m [39;49;00min[37m [39;49;00mthe[37m [39;49;00mdebugger.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00mexists[37m [39;49;00m$ENV{PERLDB_RESTART}[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m We're restarting, so we don't need the flag that says to restart anymore.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[34mdelete[39;49;00m[37m [39;49;00m$ENV{PERLDB_RESTART};[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m $restart = 1;[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[04m[91m@[39;49;00mhist[37m          [39;49;00m=[37m [39;49;00mget_list([04m[91m'[39;49;00mPERLDB_HIST[04m[91m'[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00m[32m%break_on_load[39;49;00m[37m [39;49;00m=[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_ON_LOAD[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00m[32m%postponed[39;49;00m[37m     [39;49;00m=[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_POSTPONE[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m[39;49;00m$
[37m^I[39;49;00mshare([04m[91m@[39;49;00mhist);[37m[39;49;00m$
[37m^I[39;49;00mshare([04m[91m@[39;49;00mtruehist);[37m[39;49;00m$
[37m^I[39;49;00mshare([32m%break_on_load[39;49;00m);[37m[39;49;00m$
[37m^I[39;49;00mshare([32m%postponed[39;49;00m);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m restore breakpoints[39;49;00m[36m/[39;49;00m[36mactions[39;49;00m[36m[39;49;00m$
[37m    [39;49;00mmy[37m [39;49;00m[04m[91m@[39;49;00mhad_breakpoints[37m [39;49;00m=[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_VISITED[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m..[37m [39;49;00m$[36m#had_breakpoints[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00mmy[37m [39;49;00m[32m%pf[39;49;00m[37m [39;49;00m=[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_FILE_$_[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m        [39;49;00m$postponed_file{[37m [39;49;00m$had_breakpoints[$_][37m [39;49;00m}[37m [39;49;00m=[37m [39;49;00m[04m[91m\[39;49;00m[32m%pf[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m[32m%pf[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m restore options[39;49;00m[36m[39;49;00m$
[37m    [39;49;00mmy[37m [39;49;00m[32m%opt[39;49;00m[37m [39;49;00m=[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_OPT[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mmy[37m [39;49;00m([37m [39;49;00m$opt,[37m [39;49;00m$val[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m([37m [39;49;00m([37m [39;49;00m$opt,[37m [39;49;00m$val[37m [39;49;00m)[37m [39;49;00m=[37m [39;49;00meach[37m [39;49;00m[32m%opt[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00m$val[37m [39;49;00m=~[37m [39;49;00ms/[[04m[91m\[39;49;00m[04m[91m\[39;49;00m[04m[91m\[39;49;00m[04m[91m'[39;49;00m]/[04m[91m\[39;49;00m[04m[91m\[39;49;00m$1/g;[37m[39;49;00m$
[37m        [39;49;00mparse_options([33m"[39;49;00m[33m$opt'$val'[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m restore original @INC[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[04m[91m@[39;49;00mINC[37m     [39;49;00m=[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_INC[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00m[04m[91m@[39;49;00mini_INC[37m [39;49;00m=[37m [39;49;00m[04m[91m@[39;49;00mINC;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m return pre[39;49;00m[36m/[39;49;00m[36mpostprompt actions and typeahead buffer[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m$pretype[37m   [39;49;00m=[37m [39;49;00m[[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_PRETYPE[39;49;00m[33m"[39;49;00m)[37m [39;49;00m];[37m[39;49;00m$
[37m    [39;49;00m$pre[37m       [39;49;00m=[37m [39;49;00m[[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_PRE[39;49;00m[33m"[39;49;00m)[37m [39;49;00m];[37m[39;49;00m$
[37m    [39;49;00m$post[37m      [39;49;00m=[37m [39;49;00m[[37m [39;49;00mget_list([33m"[39;49;00m[33mPERLDB_POST[39;49;00m[33m"[39;49;00m)[37m [39;49;00m];[37m[39;49;00m$
[37m    [39;49;00m[04m[91m@[39;49;00mtypeahead[37m [39;49;00m=[37m [39;49;00mget_list([37m [39;49;00m[33m"[39;49;00m[33mPERLDB_TYPEAHEAD[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[04m[91m@[39;49;00mtypeahead[37m [39;49;00m);[37m[39;49;00m$
}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(exists[37m [39;49;00m$ENV{PERLDB_RESTART...[37m[39;49;00m$
[37m[39;49;00m$
=head2[37m [39;49;00mSETTING[37m [39;49;00mUP[37m [39;49;00mTHE[37m [39;49;00mTERMINAL[37m[39;49;00m$
[37m[39;49;00m$
Now,[37m [39;49;00mwe[04m[91m'[39;49;00mll[37m [39;49;00mdecide[37m [39;49;00mhow[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mis[37m [39;49;00mgoing[37m [39;49;00mto[37m [39;49;00minteract[37m [39;49;00mwith[37m [39;49;00mthe[37m [39;49;00muser.[37m[39;49;00m$
If[37m [39;49;00mthere[04m[91m'[39;49;00ms[37m [39;49;00mno[37m [39;49;00mTTY,[37m [39;49;00mwe[37m [39;49;00mset[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mto[37m [39;49;00mrun[37m [39;49;00mnon-stop;[37m [39;49;00mthere[04m[91m'[39;49;00ms[37m [39;49;00mnot[37m [39;49;00mgoing[37m[39;49;00m$
to[37m [39;49;00mbe[37m [39;49;00manyone[37m [39;49;00mthere[37m [39;49;00mto[37m [39;49;00menter[37m [39;49;00mcommands.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[34mif[39;49;00m[37m [39;49;00m($notty)[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00m$runnonstop[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[37m^I[39;49;00mshare($runnonstop);[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
=pod[37m[39;49;00m$
[37m[39;49;00m$
If[37m [39;49;00mthere[37m [39;49;00mis[37m [39;49;00ma[37m [39;49;00mTTY,[37m [39;49;00mwe[37m [39;49;00mhave[37m [39;49;00mto[37m [39;49;00mdetermine[37m [39;49;00mwho[37m [39;49;00mit[37m [39;49;00mbelongs[37m [39;49;00mto[37m [39;49;00mbefore[37m [39;49;00mwe[37m [39;49;00mcan[37m[39;49;00m$
proceed.[37m [39;49;00mIf[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00mis[37m [39;49;00ma[37m [39;49;00mslave[37m [39;49;00meditor[37m [39;49;00mor[37m [39;49;00mgraphical[37m [39;49;00mdebugger[37m [39;49;00m(denoted[37m [39;49;00mby[37m[39;49;00m$
the[37m [39;49;00mfirst[37m [39;49;00mcommand-line[37m [39;49;00m[34mswitch[39;49;00m[37m [39;49;00mbeing[37m [39;49;00m[04m[91m'[39;49;00m-emacs[04m[91m'[39;49;00m),[37m [39;49;00mwe[37m [39;49;00mshift[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00moff[37m [39;49;00mand[37m[39;49;00m$
set[37m [39;49;00mC<$rl>[37m [39;49;00mto[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m(XXX[37m [39;49;00mostensibly[37m [39;49;00mto[37m [39;49;00m[34mdo[39;49;00m[37m [39;49;00mstraight[37m [39;49;00mreads).[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m Is Perl being run from a slave editor or graphical debugger?[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m If so, don't use readline, and set $slave_editor = 1.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m$slave_editor[37m [39;49;00m=[37m[39;49;00m$
[37m      [39;49;00m([37m [39;49;00m([37m [39;49;00mdefined[37m [39;49;00m$main::ARGV[[34m0[39;49;00m][37m [39;49;00m)[37m [39;49;00mand[37m [39;49;00m([37m [39;49;00m$main::ARGV[[34m0[39;49;00m][37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00m-emacs[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00m$rl[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00mshift([04m[91m@[39;49;00mmain::ARGV)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m$slave_editor;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36mrequire Term::ReadLine;[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
=pod[37m[39;49;00m$
[37m[39;49;00m$
We[37m [39;49;00mthen[37m [39;49;00mdetermine[37m [39;49;00mwhat[37m [39;49;00mthe[37m [39;49;00mconsole[37m [39;49;00mshould[37m [39;49;00mbe[37m [39;49;00mon[37m [39;49;00mvarious[37m [39;49;00msystems:[37m[39;49;00m$
[37m[39;49;00m$
=over[37m [39;49;00m[34m4[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
=item[37m [39;49;00m*[37m [39;49;00mCygwin[37m [39;49;00m-[37m [39;49;00mWe[37m [39;49;00muse[37m [39;49;00mC<stdin>[37m [39;49;00minstead[37m [39;49;00mof[37m [39;49;00ma[37m [39;49;00mseparate[37m [39;49;00mdevice.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m$^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mcygwin[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m [39;49;00m[36m/[39;49;00m[36mdev[39;49;00m[36m/[39;49;00m[36mtty is binary. use stdin for textmode[39;49;00m[36m[39;49;00m$
[37m        [39;49;00mundef[37m [39;49;00m$console;[37m[39;49;00m$
[37m    [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
=item[37m [39;49;00m*[37m [39;49;00mUnix[37m [39;49;00m-[37m [39;49;00muse[37m [39;49;00mC</dev/tty>.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00melsif[37m [39;49;00m([37m [39;49;00m-e[37m [39;49;00m[33m"[39;49;00m[33m/dev/tty[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00m$console[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m/dev/tty[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
=item[37m [39;49;00m*[37m [39;49;00mWindows[37m [39;49;00mor[37m [39;49;00mMSDOS[37m [39;49;00m-[37m [39;49;00muse[37m [39;49;00mC<con>.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00melsif[37m [39;49;00m([37m [39;49;00m$^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mdos[04m[91m'[39;49;00m[37m [39;49;00mor[37m [39;49;00m-e[37m [39;49;00m[33m"[39;49;00m[33mcon[39;49;00m[33m"[39;49;00m[37m [39;49;00mor[37m [39;49;00m$^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mMSWin32[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00m$console[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mcon[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
=item[37m [39;49;00m*[37m [39;49;00mMacOS[37m [39;49;00m-[37m [39;49;00muse[37m [39;49;00mC<Dev:Console:Perl[37m [39;49;00mDebug>[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m[34mthis[39;49;00m[37m [39;49;00mis[37m [39;49;00mthe[37m [39;49;00mMPW[37m [39;49;00mversion;[37m [39;49;00mC<Dev:[37m[39;49;00m$
Console>[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mnot.[37m[39;49;00m$
[37m[39;49;00m$
Note[37m [39;49;00mthat[37m [39;49;00mMac[37m [39;49;00mOS[37m [39;49;00mX[37m [39;49;00mreturns[37m [39;49;00mC<darwin>,[37m [39;49;00mnot[37m [39;49;00mC<MacOS>.[37m [39;49;00mAlso[37m [39;49;00mnote[37m [39;49;00mthat[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mdoesn[04m[91m'[39;49;00mt[37m [39;49;00m[34mdo[39;49;00m[37m [39;49;00manything[37m [39;49;00mspecial[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mC<darwin>.[37m [39;49;00mMaybe[37m [39;49;00mit[37m [39;49;00mshould.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00melsif[37m [39;49;00m([37m [39;49;00m$^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mMacOS[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m$MacPerl::Version[37m [39;49;00m!~[37m [39;49;00m/MPW/[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00m$console[37m [39;49;00m=[37m[39;49;00m$
[37m              [39;49;00m[33m"[39;49;00m[33mDev:Console:Perl Debug[39;49;00m[33m"[39;49;00m;[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mSeparate[37m [39;49;00mwindow[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mapplication[37m[39;49;00m$
[37m        [39;49;00m}[37m[39;49;00m$
[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00m$console[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mDev:Console[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
[37m        [39;49;00m}[37m[39;49;00m$
[37m    [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00melsif[37m [39;49;00m($^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mMacOS[04m[91m'[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
=item[37m [39;49;00m*[37m [39;49;00mVMS[37m [39;49;00m-[37m [39;49;00muse[37m [39;49;00mC<sys$command>.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m everything else is ...[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m$console[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33msys[39;49;00m[33m\[39;49;00m[33m$command[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
=pod[37m[39;49;00m$
[37m[39;49;00m$
=back[37m[39;49;00m$
[37m[39;49;00m$
Several[37m [39;49;00mother[37m [39;49;00msystems[37m [39;49;00mdon[04m[91m'[39;49;00mt[37m [39;49;00muse[37m [39;49;00ma[37m [39;49;00mspecific[37m [39;49;00mconsole.[37m [39;49;00mWe[37m [39;49;00mC<undef[37m [39;49;00m$console>[37m[39;49;00m$
[34mfor[39;49;00m[37m [39;49;00mthose[37m [39;49;00m(Windows[37m [39;49;00m[34musing[39;49;00m[37m [39;49;00ma[37m [39;49;00mslave[37m [39;49;00meditor/graphical[37m [39;49;00mdebugger,[37m [39;49;00mNetWare,[37m [39;49;00mOS/[34m2[39;49;00m[37m[39;49;00m$
with[37m [39;49;00ma[37m [39;49;00mslave[37m [39;49;00meditor,[37m [39;49;00mEpoc).[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m([37m [39;49;00m$^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mMSWin32[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00mand[37m [39;49;00m([37m [39;49;00m$slave_editor[37m [39;49;00mor[37m [39;49;00mdefined[37m [39;49;00m$ENV{EMACS}[37m [39;49;00m)[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m [39;49;00m[36m/[39;49;00m[36mdev[39;49;00m[36m/[39;49;00m[36mtty is binary. use stdin for textmode[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m$console[37m [39;49;00m=[37m [39;49;00mundef;[37m[39;49;00m$
[37m    [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m$^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mNetWare[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m [39;49;00m[36m/[39;49;00m[36mdev[39;49;00m[36m/[39;49;00m[36mtty is binary. use stdin for textmode[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m$console[37m [39;49;00m=[37m [39;49;00mundef;[37m[39;49;00m$
[37m    [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m In OS[39;49;00m[36m/[39;49;00m[36m2, we need to use STDIN to get textmode too, even though[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m it pretty much looks like Unix otherwise.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00mdefined[37m [39;49;00m$ENV{OS2_SHELL}[37m [39;49;00mand[37m [39;49;00m([37m [39;49;00m$slave_editor[37m [39;49;00mor[37m [39;49;00m$ENV{WINDOWID}[37m [39;49;00m)[37m [39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m{[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mIn[37m [39;49;00mOS/[34m2[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m$console[37m [39;49;00m=[37m [39;49;00mundef;[37m[39;49;00m$
[37m    [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m EPOC also falls into the 'got to use STDIN' camp.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m$^O[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00mepoc[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00m$console[37m [39;49;00m=[37m [39;49;00mundef;[37m[39;49;00m$
[37m    [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
=pod[37m[39;49;00m$
[37m[39;49;00m$
If[37m [39;49;00mthere[37m [39;49;00mis[37m [39;49;00ma[37m [39;49;00mTTY[37m [39;49;00mhanging[37m [39;49;00maround[37m [39;49;00mfrom[37m [39;49;00ma[37m [39;49;00mparent,[37m [39;49;00mwe[37m [39;49;00muse[37m [39;49;00mthat[37m [39;49;00mas[37m [39;49;00mthe[37m [39;49;00mconsole.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m$console[37m [39;49;00m=[37m [39;49;00m$tty[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mdefined[37m [39;49;00m$tty;[37m[39;49;00m$
[37m[39;49;00m$
=head2[37m [39;49;00mSOCKET[37m [39;49;00mHANDLING[37m   [39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
The[37m [39;49;00mdebugger[37m [39;49;00mis[37m [39;49;00mcapable[37m [39;49;00mof[37m [39;49;00mopening[37m [39;49;00ma[37m [39;49;00msocket[37m [39;49;00mand[37m [39;49;00mcarrying[37m [39;49;00mout[37m [39;49;00ma[37m [39;49;00mdebugging[37m[39;49;00m$
session[37m [39;49;00mover[37m [39;49;00mthe[37m [39;49;00msocket.[37m[39;49;00m$
[37m[39;49;00m$
If[37m [39;49;00mC<RemotePort>[37m [39;49;00mwas[37m [39;49;00mdefined[37m [39;49;00min[37m [39;49;00mthe[37m [39;49;00moptions,[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00massumes[37m [39;49;00mthat[37m [39;49;00mit[37m[39;49;00m$
should[37m [39;49;00m[34mtry[39;49;00m[37m [39;49;00mto[37m [39;49;00mstart[37m [39;49;00ma[37m [39;49;00mdebugging[37m [39;49;00msession[37m [39;49;00mon[37m [39;49;00mthat[37m [39;49;00mport.[37m [39;49;00mIt[37m [39;49;00mbuilds[37m [39;49;00mthe[37m [39;49;00msocket[37m[39;49;00m$
and[37m [39;49;00mthen[37m [39;49;00mtries[37m [39;49;00mto[37m [39;49;00mconnect[37m [39;49;00mthe[37m [39;49;00minput[37m [39;49;00mand[37m [39;49;00moutput[37m [39;49;00mfilehandles[37m [39;49;00mto[37m [39;49;00mit.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m Handle socket stuff.[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00mdefined[37m [39;49;00m$remoteport[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m If RemotePort was defined in the options, connect input and output[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m to the socket.[39;49;00m[36m[39;49;00m$
[37m        [39;49;00mrequire[37m [39;49;00mIO::Socket;[37m[39;49;00m$
[37m        [39;49;00m$OUT[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mIO::Socket::INET([37m[39;49;00m$
[37m            [39;49;00mTimeout[37m  [39;49;00m=>[37m [39;49;00m[04m[91m'[39;49;00m[34m10[39;49;00m[04m[91m'[39;49;00m,[37m[39;49;00m$
[37m            [39;49;00mPeerAddr[37m [39;49;00m=>[37m [39;49;00m$remoteport,[37m[39;49;00m$
[37m            [39;49;00mProto[37m    [39;49;00m=>[37m [39;49;00m[04m[91m'[39;49;00mtcp[04m[91m'[39;49;00m,[37m[39;49;00m$
[37m        [39;49;00m);[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m!$OUT[37m [39;49;00m)[37m [39;49;00m{[37m [39;49;00mdie[37m [39;49;00m[33m"[39;49;00m[33mUnable to connect to remote host: $remoteport[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m [39;49;00m}[37m[39;49;00m$
[37m        [39;49;00m$IN[37m [39;49;00m=[37m [39;49;00m$OUT;[37m[39;49;00m$
[37m    [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(defined[37m [39;49;00m$remoteport)[37m[39;49;00m$
[37m[39;49;00m$
=pod[37m[39;49;00m$
[37m[39;49;00m$
If[37m [39;49;00mno[37m [39;49;00mC<RemotePort>[37m [39;49;00mwas[37m [39;49;00mdefined,[37m [39;49;00mand[37m [39;49;00mwe[37m [39;49;00mwant[37m [39;49;00mto[37m [39;49;00mcreate[37m [39;49;00ma[37m [39;49;00mTTY[37m [39;49;00mon[37m [39;49;00mstartup,[37m[39;49;00m$
[34mthis[39;49;00m[37m [39;49;00mis[37m [39;49;00mprobably[37m [39;49;00ma[37m [39;49;00msituation[37m [39;49;00mwhere[37m [39;49;00mmultiple[37m [39;49;00mdebuggers[37m [39;49;00mare[37m [39;49;00mrunning[37m [39;49;00m([34mfor[39;49;00m[37m [39;49;00mexample,[37m[39;49;00m$
a[37m [39;49;00mbackticked[37m [39;49;00mcommand[37m [39;49;00mthat[37m [39;49;00mstarts[37m [39;49;00mup[37m [39;49;00manother[37m [39;49;00mdebugger).[37m [39;49;00mWe[37m [39;49;00mcreate[37m [39;49;00ma[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mIN[37m [39;49;00mand[37m[39;49;00m$
OUT[37m [39;49;00mfilehandle,[37m [39;49;00mand[37m [39;49;00m[34mdo[39;49;00m[37m [39;49;00mthe[37m [39;49;00mnecessary[37m [39;49;00mmojo[37m [39;49;00mto[37m [39;49;00mcreate[37m [39;49;00ma[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mTTY[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mwe[37m [39;49;00mknow[37m [39;49;00mhow[37m[39;49;00m$
and[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mwe[37m [39;49;00mcan.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m Non-socket.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m Two debuggers running (probably a system or a backtick that invokes[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m the debugger itself under the running one). create a new IN and OUT[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m filehandle, and do the necessary mojo to create a new tty if we[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m know how, and we can.[39;49;00m[36m[39;49;00m$
[37m        [39;49;00mcreate_IN_OUT([34m4[39;49;00m)[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m$CreateTTY[37m [39;49;00m&[37m [39;49;00m[34m4[39;49;00m;[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m($console)[37m [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[36m#[39;49;00m[36m If we have a console, check to see if there are separate ins and[39;49;00m[36m[39;49;00m$
[37m            [39;49;00m[36m#[39;49;00m[36m outs to open. (They are assumed identiical if not.)[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00mmy[37m [39;49;00m([37m [39;49;00m$i,[37m [39;49;00m$o[37m [39;49;00m)[37m [39;49;00m=[37m [39;49;00msplit[37m [39;49;00m/,/,[37m [39;49;00m$console;[37m[39;49;00m$
[37m            [39;49;00m$o[37m [39;49;00m=[37m [39;49;00m$i[37m [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$o;[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[36m#[39;49;00m[36m read[39;49;00m[36m/[39;49;00m[36mwrite on in, or just read, or read on STDIN.[39;49;00m[36m[39;49;00m$
[37m            [39;49;00mopen([37m [39;49;00mIN,[37m      [39;49;00m[33m"[39;49;00m[33m+<$i[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m||[37m [39;49;00mopen([37m [39;49;00mIN,[37m [39;49;00m[33m"[39;49;00m[33m<$i[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m||[37m [39;49;00mopen([37m [39;49;00mIN,[37m [39;49;00m[33m"[39;49;00m[33m<&STDIN[39;49;00m[33m"[39;49;00m[37m [39;49;00m);[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[36m#[39;49;00m[36m read[39;49;00m[36m/[39;49;00m[36mwrite[39;49;00m[36m/[39;49;00m[36mcreate[39;49;00m[36m/[39;49;00m[36mclobber out, or write[39;49;00m[36m/[39;49;00m[36mcreate[39;49;00m[36m/[39;49;00m[36mclobber out,[39;49;00m[36m[39;49;00m$
[37m            [39;49;00m[36m#[39;49;00m[36m or merge with STDERR, or merge with STDOUT.[39;49;00m[36m[39;49;00m$
[37m                 [39;49;00mopen([37m [39;49;00mOUT,[37m [39;49;00m[33m"[39;49;00m[33m+>$o[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m||[37m [39;49;00mopen([37m [39;49;00mOUT,[37m [39;49;00m[33m"[39;49;00m[33m>$o[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m||[37m [39;49;00mopen([37m [39;49;00mOUT,[37m [39;49;00m[33m"[39;49;00m[33m>&STDERR[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m||[37m [39;49;00mopen([37m [39;49;00mOUT,[37m [39;49;00m[33m"[39;49;00m[33m>&STDOUT[39;49;00m[33m"[39;49;00m[37m [39;49;00m);[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mso[37m [39;49;00mwe[37m [39;49;00mdon[04m[91m'[39;49;00mt[37m [39;49;00mdongle[37m [39;49;00mstdout[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m($console)[37m[39;49;00m$
[37m        [39;49;00melsif[37m [39;49;00m([37m [39;49;00mnot[37m [39;49;00mdefined[37m [39;49;00m$console[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[36m#[39;49;00m[36m No console. Open STDIN.[39;49;00m[36m[39;49;00m$
[37m            [39;49;00mopen([37m [39;49;00mIN,[37m [39;49;00m[33m"[39;49;00m[33m<&STDIN[39;49;00m[33m"[39;49;00m[37m [39;49;00m);[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[36m#[39;49;00m[36m merge with STDERR, or with STDOUT.[39;49;00m[36m[39;49;00m$
[37m            [39;49;00mopen([37m [39;49;00mOUT,[37m      [39;49;00m[33m"[39;49;00m[33m>&STDERR[39;49;00m[33m"[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m||[37m [39;49;00mopen([37m [39;49;00mOUT,[37m [39;49;00m[33m"[39;49;00m[33m>&STDOUT[39;49;00m[33m"[39;49;00m[37m [39;49;00m);[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mso[37m [39;49;00mwe[37m [39;49;00mdon[04m[91m'[39;49;00mt[37m [39;49;00mdongle[37m [39;49;00mstdout[37m[39;49;00m$
[37m            [39;49;00m$console[37m [39;49;00m=[37m [39;49;00m[04m[91m'[39;49;00mSTDIN/OUT[04m[91m'[39;49;00m;[37m[39;49;00m$
[37m        [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00melsif[37m [39;49;00m(not[37m [39;49;00mdefined[37m [39;49;00m$console)[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m Keep copies of the filehandles so that when the pager runs, it[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m[36m#[39;49;00m[36m can close standard input without clobbering ours.[39;49;00m[36m[39;49;00m$
[37m        [39;49;00m$IN[37m [39;49;00m=[37m [39;49;00m[04m[91m\[39;49;00m*IN,[37m [39;49;00m$OUT[37m [39;49;00m=[37m [39;49;00m[04m[91m\[39;49;00m*OUT[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m$console[37m [39;49;00mor[37m [39;49;00mnot[37m [39;49;00mdefined[37m [39;49;00m$console;[37m[39;49;00m$
[37m    [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00melsif[37m [39;49;00m(from[37m [39;49;00m[34mif[39;49;00m(defined[37m [39;49;00m$remoteport))[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m Unbuffer DB::OUT. We need to see responses right away.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00mmy[37m [39;49;00m$previous[37m [39;49;00m=[37m [39;49;00mselect($OUT);[37m[39;49;00m$
[37m    [39;49;00m$|[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m                                  [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00m[34mfor[39;49;00m[37m [39;49;00mDB::OUT[37m[39;49;00m$
[37m    [39;49;00mselect($previous);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m Line info goes to debugger output unless pointed elsewhere.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m Pointing elsewhere makes it possible for slave editors to[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m keep track of file and position. We have both a filehandle[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m and a I[39;49;00m[36m/[39;49;00m[36mO description to keep track of.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m$LINEINFO[37m [39;49;00m=[37m [39;49;00m$OUT[37m     [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$LINEINFO;[37m[39;49;00m$
[37m    [39;49;00m$lineinfo[37m [39;49;00m=[37m [39;49;00m$console[37m [39;49;00munless[37m [39;49;00mdefined[37m [39;49;00m$lineinfo;[37m[39;49;00m$
[37m^I[39;49;00m[36m#[39;49;00m[36m share($LINEINFO); # <- unable to share globs[39;49;00m[36m[39;49;00m$
[37m^I[39;49;00mshare($lineinfo);[37m   [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
=pod[37m[39;49;00m$
[37m[39;49;00m$
To[37m [39;49;00mfinish[37m [39;49;00minitialization,[37m [39;49;00mwe[37m [39;49;00mshow[37m [39;49;00mthe[37m [39;49;00mdebugger[37m [39;49;00mgreeting,[37m[39;49;00m$
and[37m [39;49;00mthen[37m [39;49;00mcall[37m [39;49;00mthe[37m [39;49;00mC<afterinit()>[37m [39;49;00msubroutine[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00mthere[37m [39;49;00mis[37m [39;49;00mone.[37m[39;49;00m$
[37m[39;49;00m$
=cut[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m Show the debugger greeting.[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m$header[37m [39;49;00m=~[37m [39;49;00ms/.Header:[37m [39;49;00m([^,]+),v([04m[91m\[39;49;00ms+[04m[91m\[39;49;00mS+[04m[91m\[39;49;00ms+[04m[91m\[39;49;00mS+).*$/$1$2/;[37m[39;49;00m$
[37m    [39;49;00munless[37m [39;49;00m($runnonstop)[37m [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00mlocal[37m [39;49;00m$[04m[91m\[39;49;00m[37m [39;49;00m=[37m [39;49;00m[04m[91m'[39;49;00m[04m[91m'[39;49;00m;[37m[39;49;00m$
[37m        [39;49;00mlocal[37m [39;49;00m$,[37m [39;49;00m=[37m [39;49;00m[04m[91m'[39;49;00m[04m[91m'[39;49;00m;[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m$term_pid[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00m[34m-1[39;49;00m[04m[91m'[39;49;00m[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00mprint[37m [39;49;00m$OUT[37m [39;49;00m[33m"[39;49;00m[33m\n[39;49;00m[33mDaughter DB session started...[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
[37m        [39;49;00m}[37m[39;49;00m$
[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00mprint[37m [39;49;00m$OUT[37m [39;49;00m[33m"[39;49;00m[33m\n[39;49;00m[33mLoading DB routines from $header[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
[37m            [39;49;00mprint[37m [39;49;00m[32m$OUT[39;49;00m[37m [39;49;00m([37m[39;49;00m$
[37m                [39;49;00m[33m"[39;49;00m[33mEditor support [39;49;00m[33m"[39;49;00m,[37m[39;49;00m$
[37m                [39;49;00m$slave_editor[37m [39;49;00m?[37m [39;49;00m[33m"[39;49;00m[33menabled[39;49;00m[33m"[39;49;00m[37m [39;49;00m:[37m [39;49;00m[33m"[39;49;00m[33mavailable[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m.[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m);[37m[39;49;00m$
[37m            [39;49;00mprint[37m [39;49;00m$OUT[37m[39;49;00m$
[33m"[39;49;00m[33m\n[39;49;00m[33mEnter h or `h h' for help, or `$doccmd perldebug' for more help.[39;49;00m[33m\n[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
[37m        [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m($term_pid[37m [39;49;00meq[37m [39;49;00m[04m[91m'[39;49;00m[34m-1[39;49;00m[04m[91m'[39;49;00m)[37m[39;49;00m$
[37m    [39;49;00m}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00munless[37m [39;49;00m($runnonstop)[37m[39;49;00m$
}[37m [39;49;00m[04m[91m#[39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mend[37m [39;49;00m[34melse[39;49;00m[37m [39;49;00m[[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m($notty)[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m XXX This looks like a bug to me.[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m Why copy to @ARGS and then futz with @args?[39;49;00m[36m[39;49;00m$
[04m[91m@[39;49;00mARGS[37m [39;49;00m=[37m [39;49;00m[04m[91m@[39;49;00mARGV;[37m[39;49;00m$
[34mfor[39;49;00m[37m [39;49;00m([04m[91m@[39;49;00margs)[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m Make sure backslashes before single quotes are stripped out, and[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m keep args unless they are numeric (XXX why?)[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m s[39;49;00m[36m/[39;49;00m[36m\'[39;49;00m[36m/[39;49;00m[36m\\\'[39;49;00m[36m/[39;49;00m[36mg;                      # removed while not justified understandably[39;49;00m[36m[39;49;00m$
[37m    [39;49;00m[36m#[39;49;00m[36m s[39;49;00m[36m/[39;49;00m[36m(.*)[39;49;00m[36m/[39;49;00m[36m'$1'[39;49;00m[36m/[39;49;00m[36m unless [39;49;00m[36m/[39;49;00m[36m^-?[\d.]+$[39;49;00m[36m/[39;49;00m[36m; # ditto[39;49;00m[36m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m If there was an afterinit() sub defined, call it. It will get[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36m executed in our scope, so it can fiddle with debugger globals.[39;49;00m[36m[39;49;00m$
[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00mdefined[37m [39;49;00m&afterinit[37m [39;49;00m)[37m [39;49;00m{[37m    [39;49;00m[04m[91m#[39;49;00m[37m [39;49;00mMay[37m [39;49;00mbe[37m [39;49;00mdefined[37m [39;49;00min[37m [39;49;00m$rcfile[37m[39;49;00m$
[37m    [39;49;00m&afterinit();[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36m Inform us about "Stack dump during die enabled ..." in dieLevel().[39;49;00m[36m[39;49;00m$
$I_m_init[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;$
