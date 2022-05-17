     1^I[37m#[39;49;00m$
     2^I[37m# ***** BEGIN LICENSE BLOCK *****[39;49;00m$
     3^I[37m# Version: MPL 1.1/GPL 2.0/LGPL 2.1[39;49;00m$
     4^I[37m#[39;49;00m$
     5^I[37m# The contents of this file are subject to the Mozilla Public License Version[39;49;00m$
     6^I[37m# 1.1 (the "License"); you may not use this file except in compliance with[39;49;00m$
     7^I[37m# the License. You may obtain a copy of the License at[39;49;00m$
     8^I[37m# http://www.mozilla.org/MPL/[39;49;00m$
     9^I[37m#[39;49;00m$
    10^I[37m# Software distributed under the License is distributed on an "AS IS" basis,[39;49;00m$
    11^I[37m# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License[39;49;00m$
    12^I[37m# for the specific language governing rights and limitations under the[39;49;00m$
    13^I[37m# License.[39;49;00m$
    14^I[37m#[39;49;00m$
    15^I[37m# The Original Code is mozilla.org code.[39;49;00m$
    16^I[37m#[39;49;00m$
    17^I[37m# The Initial Developer of the Original Code is[39;49;00m$
    18^I[37m# Netscape Communications Corporation.[39;49;00m$
    19^I[37m# Portions created by the Initial Developer are Copyright (C) 1998[39;49;00m$
    20^I[37m# the Initial Developer. All Rights Reserved.[39;49;00m$
    21^I[37m#[39;49;00m$
    22^I[37m# Contributor(s):[39;49;00m$
    23^I[37m#[39;49;00m$
    24^I[37m# Alternatively, the contents of this file may be used under the terms of[39;49;00m$
    25^I[37m# either the GNU General Public License Version 2 or later (the "GPL"), or[39;49;00m$
    26^I[37m# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),[39;49;00m$
    27^I[37m# in which case the provisions of the GPL or the LGPL are applicable instead[39;49;00m$
    28^I[37m# of those above. If you wish to allow use of your version of this file only[39;49;00m$
    29^I[37m# under the terms of either the GPL or the LGPL, and not to allow others to[39;49;00m$
    30^I[37m# use your version of this file under the terms of the MPL, indicate your[39;49;00m$
    31^I[37m# decision by deleting the provisions above and replace them with the notice[39;49;00m$
    32^I[37m# and other provisions required by the GPL or the LGPL. If you do not delete[39;49;00m$
    33^I[37m# the provisions above, a recipient may use your version of this file under[39;49;00m$
    34^I[37m# the terms of any one of the MPL, the GPL or the LGPL.[39;49;00m$
    35^I[37m#[39;49;00m$
    36^I[37m# ***** END LICENSE BLOCK *****[39;49;00m$
    37^I$
    38^I[31mDEPTH[39;49;00m^I^I= .$
    39^I[31mtopsrcdir[39;49;00m^I= @top_srcdir@$
    40^I[31msrcdir[39;49;00m^I^I= @srcdir@$
    41^I[31mVPATH[39;49;00m^I^I= @srcdir@$
    42^I$
    43^I[36minclude $(DEPTH)/config/autoconf.mk[39;49;00m$
    44^I$
    45^I[36minclude $(topsrcdir)/build/unix/modules.mk[39;49;00m$
    46^I$
    47^I[36mifeq ($(BUILD_MODULES),all)[39;49;00m$
    48^I[37m#[39;49;00m$
    49^I[37m# And now for something completely different...[39;49;00m$
    50^I[37m# Divide the default build into tiers. [39;49;00m$
    51^I[37m# Tiers must be defined on module boundaries [39;49;00m$
    52^I[37m#[39;49;00m$
    53^I[31mSUPPRESS_DEFAULT_RULES[39;49;00m = [34m1[39;49;00m$
    54^I$
    55^I[32mdefault alldep all[39;49;00m:: [34m$([39;49;00m[31mSUBMAKEFILES[39;49;00m[34m)[39;49;00m$
    56^I^I[34m$([39;49;00mRM[34m)[39;49;00m -rf [34m$([39;49;00mDIST[34m)[39;49;00m/sdk$
    57^I^I[34m$([39;49;00mRM[34m)[39;49;00m -rf [34m$([39;49;00mDIST[34m)[39;49;00m/include$
    58^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m -C config [36mexport[39;49;00m$
    59^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m nspr$
    60^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m ldap$
    61^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m tier_0$
    62^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m tier_1$
    63^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m tier_2$
    64^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m tier_9$
    65^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m tier_50$
    66^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m tier_99$
    67^I$
    68^I[37m# Make sure that the existing rulesets work[39;49;00m$
    69^I[31mDIRS[39;49;00m = [33m\[39;49;00m$
    70^I^I[34m$([39;49;00mtier_0_dirs[34m)[39;49;00m [33m\[39;49;00m$
    71^I^I[34m$([39;49;00mtier_1_dirs[34m)[39;49;00m [33m\[39;49;00m$
    72^I^I[34m$([39;49;00mtier_2_dirs[34m)[39;49;00m [33m\[39;49;00m$
    73^I^I[34m$([39;49;00mtier_9_dirs[34m)[39;49;00m [33m\[39;49;00m$
    74^I^I[34m$([39;49;00mtier_50_dirs[34m)[39;49;00m [33m\[39;49;00m$
    75^I^I[34m$([39;49;00mNULL[34m)[39;49;00m$
    76^I$
    77^I[36mifdef GC_LEAK_DETECTOR[39;49;00m$
    78^I[31mDIRS[39;49;00m += gc/boehm$
    79^I[36mendif[39;49;00m$
    80^I$
    81^I[31mDIRS[39;49;00m^I+= [34m$([39;49;00mtier_99_dirs[34m)[39;49;00m$
    82^I$
    83^I[37m#[39;49;00m$
    84^I[37m# tier 0 - base build config dirs[39;49;00m$
    85^I[37m# [39;49;00m$
    86^I[31mtier_0_dirs[39;49;00m = [33m\[39;49;00m$
    87^I^Iconfig [33m\[39;49;00m$
    88^I^Ibuild [33m\[39;49;00m$
    89^I^I[34m$([39;49;00mNULL[34m)[39;49;00m$
    90^I$
    91^I[37m#[39;49;00m$
    92^I[37m# tier 1 -  3rd party individual libraries[39;49;00m$
    93^I[37m#[39;49;00m$
    94^I[31mtier_1_dirs[39;49;00m^I+= dbm$
    95^I$
    96^I[36mifndef MOZ_NATIVE_JPEG[39;49;00m$
    97^I[31mtier_1_dirs[39;49;00m^I+= jpeg$
    98^I[36mendif[39;49;00m$
    99^I$
   100^I[36mifndef MOZ_NATIVE_ZLIB[39;49;00m$
   101^I[31mtier_1_dirs[39;49;00m^I+= modules/zlib$
   102^I[36mendif[39;49;00m$
   103^I$
   104^I[37m# Installer needs standalone libjar, hence standalone zlib[39;49;00m$
   105^I[36mifdef MOZ_INSTALLER[39;49;00m$
   106^I[31mtier_1_dirs[39;49;00m^I+= modules/zlib/standalone$
   107^I[36mendif[39;49;00m$
   108^I$
   109^I[36mifdef MOZ_UPDATER[39;49;00m$
   110^I[31mtier_1_dirs[39;49;00m += modules/libbz2$
   111^I[31mtier_1_dirs[39;49;00m += modules/libmar$
   112^I[36mendif[39;49;00m$
   113^I$
   114^I[36mifdef MOZ_SVG_RENDERER_LIBART[39;49;00m$
   115^I[31mtier_1_dirs[39;49;00m^I+= other-licenses/libart_lgpl$
   116^I[36mendif[39;49;00m$
   117^I$
   118^I[37m#[39;49;00m$
   119^I[37m# tier 2 - base libraries[39;49;00m$
   120^I[37m# [39;49;00m$
   121^I[31mtier_2_dirs[39;49;00m^I= [33m\[39;49;00m$
   122^I^I^Ijs [33m\[39;49;00m$
   123^I^I^Ixpcom [33m\[39;49;00m$
   124^I^I^I[34m$([39;49;00mNULL[34m)[39;49;00m$
   125^I$
   126^I[36mifndef MOZ_NO_XPCOM_OBSOLETE[39;49;00m$
   127^I[31mtier_2_dirs[39;49;00m += modules/libreg xpcom/obsolete$
   128^I[36mendif[39;49;00m$
   129^I$
   130^I[36mifdef NS_TRACE_MALLOC[39;49;00m$
   131^I[31mtier_2_dirs[39;49;00m^I+= tools/trace-malloc/lib$
   132^I[36mendif[39;49;00m$
   133^I$
   134^I[37m#[39;49;00m$
   135^I[37m# tier 9 - core components (necko,gecko)[39;49;00m$
   136^I[37m#[39;49;00m$
   137^I$
   138^I[31mtier_9_dirs[39;49;00m += [33m\[39;49;00m$
   139^I^I^Ijs/src/xpconnect [33m\[39;49;00m$
   140^I^I^Iintl [33m\[39;49;00m$
   141^I^I^Idb [33m\[39;49;00m$
   142^I^I^I[34m$([39;49;00mNULL[34m)[39;49;00m$
   143^I$
   144^I[36mifdef MOZ_STORAGE[39;49;00m$
   145^I[31mtier_9_dirs[39;49;00m += storage$
   146^I[36mendif[39;49;00m$
   147^I$
   148^I[36mifdef MOZ_ENABLE_XLIB[39;49;00m$
   149^I[31mtier_9_dirs[39;49;00m^I+= gfx/src/xlibrgb widget/src/xlibxtbin$
   150^I[36mendif[39;49;00m$
   151^I$
   152^I[36mifdef MOZ_ENABLE_GTK[39;49;00m$
   153^I[31mtier_9_dirs[39;49;00m^I+= widget/src/gtksuperwin widget/src/gtkxtbin$
   154^I[36mendif[39;49;00m$
   155^I$
   156^I[36mifdef MOZ_ENABLE_GTK2[39;49;00m$
   157^I[31mtier_9_dirs[39;49;00m     += widget/src/gtkxtbin$
   158^I[36mendif[39;49;00m$
   159^I$
   160^I[36mifdef MOZ_IPCD[39;49;00m$
   161^I[31mtier_9_dirs[39;49;00m += ipc/ipcd$
   162^I[36mendif[39;49;00m$
   163^I$
   164^I[36mifdef MOZ_JSDEBUGGER[39;49;00m$
   165^I[31mtier_9_dirs[39;49;00m += js/jsd$
   166^I[36mendif[39;49;00m$
   167^I$
   168^I[31mtier_9_dirs[39;49;00m^I+= [33m\[39;49;00m$
   169^I^I^Imodules/libutil [33m\[39;49;00m$
   170^I^I^Inetwerk [33m\[39;49;00m$
   171^I^I^Imodules/libjar [33m\[39;49;00m$
   172^I^I^Iuriloader [33m\[39;49;00m$
   173^I^I^Imodules/libpref [33m\[39;49;00m$
   174^I^I^Imodules/libimg [33m\[39;49;00m$
   175^I^I^Icaps [33m\[39;49;00m$
   176^I^I^Irdf [33m\[39;49;00m$
   177^I^I^Iparser/expat [33m\[39;49;00m$
   178^I^I^Iparser/xml [33m\[39;49;00m$
   179^I^I^Iparser/htmlparser [33m\[39;49;00m$
   180^I^I^Igfx [33m\[39;49;00m$
   181^I^I^Imodules/libpr0n [33m\[39;49;00m$
   182^I^I^Isun-java [33m\[39;49;00m$
   183^I^I^Imodules/plugin [33m\[39;49;00m$
   184^I^I^Idom [33m\[39;49;00m$
   185^I^I^Iview [33m\[39;49;00m$
   186^I^I^Iwidget [33m\[39;49;00m$
   187^I^I^Icontent [33m\[39;49;00m$
   188^I^I^Ilayout [33m\[39;49;00m$
   189^I^I^Ixpfe/components/shistory [33m\[39;49;00m$
   190^I^I^Idocshell [33m\[39;49;00m$
   191^I^I^Iwebshell [33m\[39;49;00m$
   192^I^I^Iembedding [33m\[39;49;00m$
   193^I^I^Ieditor [33m\[39;49;00m$
   194^I^I^Ixpfe/appshell [33m\[39;49;00m$
   195^I^I^I[34m$([39;49;00mNULL[34m)[39;49;00m$
   196^I$
   197^I[36mifdef MOZ_OJI[39;49;00m$
   198^I[31mtier_9_dirs[39;49;00m^I+= [33m\[39;49;00m$
   199^I^I^Ijs/src/liveconnect [33m\[39;49;00m$
   200^I^I^Imodules/oji [33m\[39;49;00m$
   201^I^I^I[34m$([39;49;00mNULL[34m)[39;49;00m$
   202^I[36mendif[39;49;00m$
   203^I$
   204^I[36mifdef ACCESSIBILITY[39;49;00m$
   205^I[31mtier_9_dirs[39;49;00m    += accessible$
   206^I[36mendif[39;49;00m$
   207^I$
   208^I[37m# [39;49;00m$
   209^I[37m# tier 50 - xpfe & toolkit[39;49;00m$
   210^I[37m#[39;49;00m$
   211^I$
   212^I[36mifdef MOZ_XUL[39;49;00m$
   213^I[36mifdef MOZ_XUL_APP[39;49;00m$
   214^I[31mtier_50_dirs[39;49;00m += chrome$
   215^I[36melse[39;49;00m$
   216^I[31mtier_50_dirs[39;49;00m += rdf/chrome$
   217^I[36mendif[39;49;00m$
   218^I[36melse[39;49;00m$
   219^I[31mtier_50_dirs[39;49;00m += embedding/minimo/chromelite$
   220^I[36mendif[39;49;00m$
   221^I$
   222^I[31mtier_50_dirs[39;49;00m += profile$
   223^I$
   224^I[37m# This must preceed xpfe[39;49;00m$
   225^I[36mifdef MOZ_JPROF[39;49;00m$
   226^I[31mtier_50_dirs[39;49;00m        += tools/jprof$
   227^I[36mendif[39;49;00m$
   228^I$
   229^I[36mifneq (,$(filter mac cocoa,$(MOZ_WIDGET_TOOLKIT)))[39;49;00m$
   230^I[31mtier_50_dirs[39;49;00m^I+= xpfe/bootstrap/appleevents$
   231^I[36mendif[39;49;00m$
   232^I$
   233^I[31mtier_50_dirs[39;49;00m^I+= [33m\[39;49;00m$
   234^I^Ixpfe [33m\[39;49;00m$
   235^I^Itoolkit/components [33m\[39;49;00m$
   236^I^I[34m$([39;49;00mNULL[34m)[39;49;00m$
   237^I$
   238^I[36mifndef MOZ_XUL_APP[39;49;00m$
   239^I[31mtier_50_dirs[39;49;00m += themes$
   240^I[36mendif[39;49;00m$
   241^I$
   242^I[36mifdef MOZ_ENABLE_XREMOTE[39;49;00m$
   243^I[31mtier_50_dirs[39;49;00m += widget/src/xremoteclient$
   244^I[36mendif[39;49;00m$
   245^I$
   246^I[36mifdef MOZ_XUL_APP[39;49;00m$
   247^I[31mtier_50_dirs[39;49;00m^I+= toolkit$
   248^I[36mendif[39;49;00m$
   249^I$
   250^I[36mifdef MOZ_PHOENIX[39;49;00m$
   251^I[37m#XXXBlake this shell path is a temp hack; toolkit shouldn't depend on browser[39;49;00m$
   252^I[31mtier_50_dirs[39;49;00m    += browser/components/shell/public$
   253^I[36mendif[39;49;00m$
   254^I$
   255^I[36mifdef MOZ_XPINSTALL[39;49;00m$
   256^I[31mtier_50_dirs[39;49;00m     +=  xpinstall$
   257^I[36mendif[39;49;00m$
   258^I$
   259^I[37m# JavaXPCOM JNI code is compiled into libXUL[39;49;00m$
   260^I[36mifdef MOZ_JAVAXPCOM[39;49;00m$
   261^I[31mtier_50_dirs[39;49;00m^I+= extensions/java/xpcom/src$
   262^I[36mendif[39;49;00m$
   263^I$
   264^I[36mifdef MOZ_ENABLE_LIBXUL[39;49;00m$
   265^I[31mtier_50_dirs[39;49;00m += [33m\[39;49;00m$
   266^I^I^Itoolkit/library [33m\[39;49;00m$
   267^I^I^Ixpcom/stub [33m\[39;49;00m$
   268^I^I^I[34m$([39;49;00mNULL[34m)[39;49;00m$
   269^I[36mendif[39;49;00m$
   270^I$
   271^I[36mifdef NS_TRACE_MALLOC[39;49;00m$
   272^I[31mtier_50_dirs[39;49;00m += tools/trace-malloc$
   273^I[36mendif[39;49;00m$
   274^I$
   275^I[36mifdef MOZ_PSM[39;49;00m$
   276^I[31mtier_50_dirs[39;49;00m^I+= security/manager$
   277^I[36melse[39;49;00m$
   278^I[31mtier_50_dirs[39;49;00m^I+= security/manager/boot/public security/manager/ssl/public$
   279^I[36mendif[39;49;00m$
   280^I$
   281^I[36mifdef MOZ_LDAP_XPCOM[39;49;00m$
   282^I[31mtier_50_dirs[39;49;00m^I+= directory/xpcom$
   283^I[36mendif[39;49;00m$
   284^I$
   285^I[36mifndef MINIMO[39;49;00m$
   286^I[36mifdef MOZ_XUL_APP[39;49;00m$
   287^I[36mifdef MOZ_ENABLE_GTK2[39;49;00m$
   288^I[31mtier_50_dirs[39;49;00m    += toolkit/components/gnome$
   289^I[36mendif[39;49;00m$
   290^I[36mendif[39;49;00m$
   291^I[36mendif[39;49;00m$
   292^I$
   293^I[36mifdef MOZ_LEAKY[39;49;00m$
   294^I[31mtier_50_dirs[39;49;00m        += tools/leaky$
   295^I[36mendif[39;49;00m$
   296^I$
   297^I[36mifdef MOZ_MAPINFO[39;49;00m$
   298^I[31mtier_50_dirs[39;49;00m^I+= tools/codesighs$
   299^I[36mendif[39;49;00m$
   300^I$
   301^I[37m#[39;49;00m$
   302^I[37m# tier 99 - application features[39;49;00m$
   303^I[37m#[39;49;00m$
   304^I$
   305^I[36mifdef MOZ_MAIL_NEWS[39;49;00m$
   306^I[31mtier_99_dirs[39;49;00m^I+= mailnews$
   307^I[36mendif[39;49;00m$
   308^I$
   309^I[36mifdef MOZ_CALENDAR[39;49;00m$
   310^I[31mtier_99_dirs[39;49;00m^I+= calendar$
   311^I[36mendif[39;49;00m$
   312^I$
   313^I[36mifdef MOZ_EXTENSIONS[39;49;00m$
   314^I[31mtier_99_dirs[39;49;00m^I+= extensions$
   315^I[36mendif[39;49;00m$
   316^I$
   317^I[36mifdef MOZ_JAVAXPCOM[39;49;00m$
   318^I[31mtier_99_dirs[39;49;00m^I+= extensions/java$
   319^I[36mendif[39;49;00m$
   320^I$
   321^I[37m# axcontrol[39;49;00m$
   322^I[36mifeq ($(OS_ARCH),WINNT)[39;49;00m$
   323^I[36mifndef MOZ_NO_ACTIVEX_SUPPORT[39;49;00m$
   324^I[31mtier_99_dirs[39;49;00m += [33m\[39;49;00m$
   325^I^I^Iembedding/browser/activex/src/control [33m\[39;49;00m$
   326^I^I^Iembedding/browser/activex/src/control_kicker [33m\[39;49;00m$
   327^I^I^I[34m$([39;49;00mNULL[34m)[39;49;00m$
   328^I[36mendif[39;49;00m$
   329^I[36mendif[39;49;00m$
   330^I$
   331^I[37m# Java Embedding Plugin[39;49;00m$
   332^I[36mifneq (,$(filter mac cocoa,$(MOZ_WIDGET_TOOLKIT)))[39;49;00m$
   333^I[31mtier_99_dirs[39;49;00m += plugin/oji/JEP$
   334^I[36mendif[39;49;00m$
   335^I$
   336^I[36mifneq (,$(filter browser suite,$(MOZ_BUILD_APP)))[39;49;00m$
   337^I[31mtier_99_dirs[39;49;00m += xpfe/components/search$
   338^I[36mendif[39;49;00m$
   339^I$
   340^I[36mifdef MOZ_BRANDING_DIRECTORY[39;49;00m$
   341^I[31mtier_99_dirs[39;49;00m += [34m$([39;49;00mMOZ_BRANDING_DIRECTORY[34m)[39;49;00m$
   342^I[36mendif[39;49;00m$
   343^I$
   344^I[36mifdef MOZ_PHOENIX[39;49;00m$
   345^I[31mtier_99_dirs[39;49;00m^I+= browser xpfe/bootstrap/init.d$
   346^I[36mendif[39;49;00m$
   347^I$
   348^I[36mifdef MOZ_XULRUNNER[39;49;00m$
   349^I[31mtier_99_dirs[39;49;00m^I+= xulrunner$
   350^I[36mendif[39;49;00m$
   351^I$
   352^I[36mifdef MOZ_COMPOSER[39;49;00m$
   353^I[31mtier_99_dirs[39;49;00m^I+= editor/ui$
   354^I[36mendif[39;49;00m$
   355^I$
   356^I[36mifdef MOZ_THUNDERBIRD[39;49;00m$
   357^I[31mtier_99_dirs[39;49;00m^I+= mail xpfe/bootstrap/init.d$
   358^I[36mendif[39;49;00m$
   359^I$
   360^I[36mifdef MOZ_STANDALONE_COMPOSER[39;49;00m$
   361^I[31mtier_99_dirs[39;49;00m^I+= composer$
   362^I[36mendif[39;49;00m$
   363^I$
   364^I[36mifdef MOZ_SUNBIRD[39;49;00m$
   365^I[31mtier_99_dirs[39;49;00m^I+= calendar/sunbird$
   366^I[36mendif[39;49;00m$
   367^I$
   368^I[36mifdef MOZ_SUITE[39;49;00m$
   369^I[31mtier_99_dirs[39;49;00m^I+= suite$
   370^I[36mendif[39;49;00m$
   371^I$
   372^I[36mifdef MINIMO[39;49;00m$
   373^I[31mtier_99_dirs[39;49;00m^I+= minimo$
   374^I[36mendif[39;49;00m$
   375^I$
   376^I[36mifdef MOZ_XUL_APP[39;49;00m$
   377^I[36mifdef MOZ_INSTALLER[39;49;00m$
   378^I[31mtier_99_dirs[39;49;00m     +=  toolkit/mozapps/installer$
   379^I[36mendif[39;49;00m$
   380^I[36melse[39;49;00m$
   381^I[36mifneq (,$(MOZ_XPFE_COMPONENTS)$(MOZ_XUL))[39;49;00m$
   382^I[36mifndef MINIMO[39;49;00m$
   383^I[31mtier_99_dirs[39;49;00m^I+= xpfe/bootstrap$
   384^I[36mendif[39;49;00m$
   385^I[36mendif[39;49;00m$
   386^I[36mendif[39;49;00m$
   387^I$
   388^I[36mifneq (,$(MOZ_ENABLE_GTK)$(MOZ_ENABLE_GTK2))[39;49;00m$
   389^I[31mtier_99_dirs[39;49;00m^I+= embedding/browser/gtk$
   390^I[36mendif[39;49;00m$
   391^I$
   392^I[37m# viewer[39;49;00m$
   393^I[36mifneq (,$(ENABLE_TESTS))[39;49;00m$
   394^I[36mifndef MOZ_ENABLE_LIBXUL[39;49;00m$
   395^I[31mtier_99_dirs[39;49;00m += webshell/tests$
   396^I[36mendif[39;49;00m$
   397^I[36mendif[39;49;00m$
   398^I$
   399^I[37m# winembed, mfcembed[39;49;00m$
   400^I[36mifeq ($(OS_ARCH),WINNT)[39;49;00m$
   401^I[36mifneq (,$(ENABLE_TESTS)$(MOZILLA_OFFICIAL))[39;49;00m$
   402^I[31mtier_99_dirs[39;49;00m += embedding/tests$
   403^I[36mendif[39;49;00m$
   404^I[36mendif[39;49;00m$
   405^I$
   406^I[37m# os2embed[39;49;00m$
   407^I[36mifeq ($(OS_ARCH),OS2)[39;49;00m$
   408^I[36mifneq (,$(ENABLE_TESTS)$(MOZILLA_OFFICIAL))[39;49;00m$
   409^I[31mtier_99_dirs[39;49;00m += embedding/tests$
   410^I[36mendif[39;49;00m$
   411^I[36mendif[39;49;00m$
   412^I$
   413^I[36mifeq ($(MOZ_BUILD_APP),macbrowser)[39;49;00m$
   414^I[31mtier_99_dirs[39;49;00m += [33m\[39;49;00m$
   415^I^Iembedding/config [33m\[39;49;00m$
   416^I^Icamino [33m\[39;49;00m$
   417^I^I[34m$([39;49;00mNULL[34m)[39;49;00m$
   418^I[36mendif[39;49;00m$
   419^I$
   420^I[37m# test harnesses [39;49;00m$
   421^I[36mifdef ENABLE_TESTS[39;49;00m$
   422^I[31mtier_99_dirs[39;49;00m += tools/test-harness$
   423^I[36mendif[39;49;00m$
   424^I$
   425^I[36melse[39;49;00m$
   426^I$
   427^I[37m# Standalone build[39;49;00m$
   428^I$
   429^I[31mDIRS[39;49;00m^I^I= [34m$([39;49;00mBUILD_MODULE_DIRS[34m)[39;49;00m$
   430^I$
   431^I[37m# Hack to generate xpidl Makefile[39;49;00m$
   432^I[36mifneq ($(BUILD_MODULES),all)[39;49;00m$
   433^I[36mifneq (,$(findstring xpcom, $(BUILD_MODULE_DIRS)))[39;49;00m$
   434^I[31mDIRS[39;49;00m^I^I:= xpcom/typelib [34m$([39;49;00mDIRS[34m)[39;49;00m$
   435^I[31mSUBMAKEFILES[39;49;00m^I:= xpcom/typelib/Makefile$
   436^I[36mendif[39;49;00m$
   437^I[36mendif[39;49;00m$
   438^I$
   439^I[32mdefault[39;49;00m:: [34m$([39;49;00m[31mSUBMAKEFILES[39;49;00m[34m)[39;49;00m$
   440^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m [36mexport[39;49;00m$
   441^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m libs$
   442^I$
   443^I[36mendif # BUILD_MODULES == all[39;49;00m$
   444^I$
   445^I[31mSTATIC_MAKEFILES[39;49;00m := nsprpub directory/c-sdk security/nss$
   446^I$
   447^I[31mGARBAGE_DIRS[39;49;00m += dist$
   448^I[31mDIST_GARBAGE[39;49;00m = config.cache config.log config.status config-defs.h [33m\[39;49;00m$
   449^I   dependencies.beos config/autoconf.mk config/myrules.mk config/myconfig.mk [33m\[39;49;00m$
   450^I   unallmakefiles mozilla-config.h [33m\[39;49;00m$
   451^I   [34m$([39;49;00mtopsrcdir[34m)[39;49;00m/.mozconfig.mk [34m$([39;49;00mtopsrcdir[34m)[39;49;00m/.mozconfig.out $
   452^I$
   453^I[37m# Build pseudo-external modules first when export is explicitly called[39;49;00m$
   454^I[32mexport[39;49;00m::$
   455^I^I[34m$([39;49;00mRM[34m)[39;49;00m -rf [34m$([39;49;00mDIST[34m)[39;49;00m/sdk$
   456^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m -C config [36mexport[39;49;00m$
   457^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m nspr$
   458^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m ldap$
   459^I[36mifneq ($(BUILD_MODULES),all)[39;49;00m$
   460^I[36mifneq (,$(findstring xpcom, $(BUILD_MODULE_DIRS)))[39;49;00m$
   461^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m -C xpcom/typelib$
   462^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m export-idl$
   463^I[36mendif[39;49;00m$
   464^I[36mendif[39;49;00m$
   465^I$
   466^I[32minstall[39;49;00m::$
   467^I[36mifndef MOZ_NATIVE_NSPR[39;49;00m$
   468^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m -C nsprpub real_install [31mDESTDIR[39;49;00m=[34m$([39;49;00mDESTDIR[34m)[39;49;00m [31mlibdir[39;49;00m=[34m$([39;49;00mmozappdir[34m)[39;49;00m [31mincludedir[39;49;00m=[34m$([39;49;00mincludedir[34m)[39;49;00m/nspr$
   469^I^I[34m$([39;49;00mRM[34m)[39;49;00m -f [34m$([39;49;00maddprefix [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mmozappdir[34m)[39;49;00m/[34m$([39;49;00mLIB_PREFIX[34m)[39;49;00m, [34m$([39;49;00maddsuffix .[34m$([39;49;00mLIB_SUFFIX[34m)[39;49;00m, nspr4 plds4 plc4[34m)[39;49;00m[34m)[39;49;00m$
   470^I^I[34m$([39;49;00mRM[34m)[39;49;00m -f [34m$([39;49;00maddprefix [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mbindir[34m)[39;49;00m/,nspr-config compile-et.pl prerr.properties[34m)[39;49;00m$
   471^I[36mendif[39;49;00m$
   472^I[36mifdef MOZ_LDAP_XPCOM[39;49;00m$
   473^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m -C directory/c-sdk real_install [31mDESTDIR[39;49;00m=[34m$([39;49;00mDESTDIR[34m)[39;49;00m [31mlibdir[39;49;00m=[34m$([39;49;00mmozappdir[34m)[39;49;00m [31mincludedir[39;49;00m=[34m$([39;49;00mincludedir[34m)[39;49;00m/ldap$
   474^I[36mendif[39;49;00m$
   475^I$
   476^I[36minclude $(topsrcdir)/config/rules.mk[39;49;00m$
   477^I$
   478^I[37m# Clean up after pseudo-external modules[39;49;00m$
   479^I[32mclean clobber realclean clobber_all distclean[39;49;00m::$
   480^I[36mifndef MOZ_NATIVE_NSPR[39;49;00m$
   481^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m -C nsprpub [31m$@[39;49;00m$
   482^I[36mendif[39;49;00m$
   483^I[36mifdef MOZ_LDAP_XPCOM[39;49;00m$
   484^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m -C directory/c-sdk [31m$@[39;49;00m$
   485^I[36mendif[39;49;00m$
   486^I$
   487^I[37m# Map mozilla targets to standard automake target[39;49;00m$
   488^I[36mifdef MOZ_ENABLE_LIBXUL[39;49;00m$
   489^I[32mtier_50[39;49;00m: [34m$([39;49;00m[31maddsuffix[39;49;00m /[31mMakefile[39;49;00m, [34m$[39;49;00m[34m([39;49;00m[31mfilter-out[39;49;00m [34m$[39;49;00m[34m([39;49;00m[31mSTATIC_MAKEFILES[39;49;00m[34m)[39;49;00m, [34m$[39;49;00m[34m([39;49;00m[34m$[39;49;00m@[31m_dirs[39;49;00m[34m)[39;49;00m[34m)[39;49;00m[34m)[39;49;00m$
   490^I^I@echo [33m"[39;49;00m[33mtier_50: [39;49;00m[34m$([39;49;00mtier_50_dirs[34m)[39;49;00m[33m"[39;49;00m$
   491^I^I@[34m$([39;49;00mEXIT_ON_ERROR[34m)[39;49;00m [33m\[39;49;00m$
   492^I^I[34mfor[39;49;00m d [34min[39;49;00m [34m$([39;49;00mtier_50_dirs[34m)[39;49;00m; [34mdo[39;49;00m [33m\[39;49;00m$
   493^I^I    [34m$([39;49;00mUPDATE_TITLE[34m)[39;49;00m [33m\[39;49;00m$
   494^I[36m^I    if test ! -f $$d/Makefile; then \[39;49;00m$
   495^I[36m^I      $(PERL) $(AUTOCONF_TOOLS)/make-makefile -t $(topsrcdir) -d $(DEPTH) $(CYGWIN_TOPSRCDIR) $$d/Makefile; \[39;49;00m$
   496^I[36m^I    fi; \[39;49;00m$
   497^I[36m^I    $(MAKE) -C $$d export; \[39;49;00m$
   498^I[36m^Idone ; \[39;49;00m$
   499^I[36m^Ifor d in $(tier_50_dirs); do \[39;49;00m$
   500^I[36m^I    $(UPDATE_TITLE) \[39;49;00m$
   501^I[36m^I    $(MAKE) -C $$d libs; \[39;49;00m$
   502^I[36m^Idone[39;49;00m$
   503^I^I@echo [33m"Building tools from tier 2/9/50"[39;49;00m$
   504^I^I@[34m$([39;49;00mEXIT_ON_ERROR[34m)[39;49;00m [33m\[39;49;00m$
   505^I^I[34mfor[39;49;00m d [34min[39;49;00m [34m$([39;49;00mtier_2_dirs[34m)[39;49;00m [34m$([39;49;00mtier_9_dirs[34m)[39;49;00m [34m$([39;49;00mtier_50_dirs[34m)[39;49;00m; [34mdo[39;49;00m [33m\[39;49;00m$
   506^I^I    [34m$([39;49;00mUPDATE_TITLE[34m)[39;49;00m [33m\[39;49;00m$
   507^I^I    [34m$([39;49;00mMAKE[34m)[39;49;00m -C [31m$$[39;49;00md tools; [33m\[39;49;00m$
   508^I^I[34mdone[39;49;00m;$
   509^I[36mendif[39;49;00m$
   510^I$
   511^I[32mtier_%[39;49;00m:$
   512^I^I@echo [33m"[39;49;00m[31m$@[39;49;00m[33m: [39;49;00m[34m$([39;49;00m[31m$@[39;49;00m_dirs[34m)[39;49;00m[33m"[39;49;00m$
   513^I^I@[34m$([39;49;00mEXIT_ON_ERROR[34m)[39;49;00m [33m\[39;49;00m$
   514^I^I  [34mfor[39;49;00m d [34min[39;49;00m [34m$([39;49;00m[31m$@[39;49;00m_dirs[34m)[39;49;00m; [34mdo[39;49;00m [33m\[39;49;00m$
   515^I^I    [34m$([39;49;00mUPDATE_TITLE[34m)[39;49;00m [33m\[39;49;00m$
   516^I[36m^I    if test ! -f $$d/Makefile; then \[39;49;00m$
   517^I[36m^I      $(PERL) $(AUTOCONF_TOOLS)/make-makefile -t $(topsrcdir) -d $(DEPTH) $(CYGWIN_TOPSRCDIR) $$d/Makefile; \[39;49;00m$
   518^I[36m^I    fi; \[39;49;00m$
   519^I[36m^I    $(MAKE) -C $$d export; \[39;49;00m$
   520^I[36m^I  done ; \[39;49;00m$
   521^I[36m^I  for d in $($@_dirs); do $(UPDATE_TITLE) \[39;49;00m$
   522^I[36m^I    $(MAKE) -C $$d libs; \[39;49;00m$
   523^I[36m^I  done[39;49;00m$
   524^I$
   525^I[37m#[39;49;00m$
   526^I[37m# Individual modules[39;49;00m$
   527^I[37m#[39;49;00m$
   528^I[32mboehm[39;49;00m:$
   529^I[36mifdef GC_LEAK_DETECTOR[39;49;00m$
   530^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m -C gc/boehm$
   531^I[36mendif[39;49;00m$
   532^I$
   533^I[32mnspr[39;49;00m: boehm$
   534^I[36mifndef MOZ_NATIVE_NSPR[39;49;00m$
   535^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m -C nsprpub$
   536^I[36mendif[39;49;00m$
   537^I$
   538^I[32mldap[39;49;00m:$
   539^I[36mifdef MOZ_LDAP_XPCOM[39;49;00m$
   540^I^I[34m$([39;49;00mMAKE[34m)[39;49;00m -C directory/c-sdk$
   541^I[36mendif[39;49;00m$
   542^I$
   543^I[32mdistclean[39;49;00m::$
   544^I^Icat unallmakefiles | [34m$([39;49;00mXARGS[34m)[39;49;00m rm -f$
   545^I^Irm -f unallmakefiles [34m$([39;49;00mDIST_GARBAGE[34m)[39;49;00m$
   546^I$
   547^I[36mifeq ($(OS_ARCH),WINNT)[39;49;00m$
   548^I[32mrebase[39;49;00m:$
   549^I[36mifdef MOZILLA_OFFICIAL[39;49;00m$
   550^I^I[36mecho[39;49;00m rebasing [34m$([39;49;00mDIST[34m)[39;49;00m$
   551^I^I/bin/find [34m$([39;49;00mDIST[34m)[39;49;00m -name [33m"*.dll"[39;49;00m > rebase.lst$
   552^I^Irebase -b [34m60000000[39;49;00m -R . -G rebase.lst$
   553^I^Irm rebase.lst$
   554^I[36mendif[39;49;00m$
   555^I$
   556^I[32msplitsymbols[39;49;00m:$
   557^I[36mifdef MOZILLA_OFFICIAL[39;49;00m$
   558^I[36mifdef MOZ_DEBUG_SYMBOLS[39;49;00m$
   559^I^I[36mecho[39;49;00m finding pdb files$
   560^I^Imkdir -p [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m$
   561^I^I-cp [33m`[39;49;00m/bin/find . -path [33m"./dist"[39;49;00m -prune -o -name [33m"*.dll"[39;49;00m | sed [33m"[39;49;00m[33ms/\.dll[39;49;00m[31m$$[39;49;00m[33m/\.pdb/[39;49;00m[33m"[39;49;00m | xargs[33m`[39;49;00m [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m$
   562^I^I-cp [33m`[39;49;00m/bin/find . -path [33m"./dist"[39;49;00m -prune -o -name [33m"*.exe"[39;49;00m | sed [33m"[39;49;00m[33ms/\.exe[39;49;00m[31m$$[39;49;00m[33m/\.pdb/[39;49;00m[33m"[39;49;00m | xargs[33m`[39;49;00m [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m$
   563^I^I-cp [33m`[39;49;00m/bin/find . -path [33m"./dist"[39;49;00m -prune -o -name [33m"*.EXE"[39;49;00m | sed [33m"[39;49;00m[33ms/\.EXE[39;49;00m[31m$$[39;49;00m[33m/\.pdb/[39;49;00m[33m"[39;49;00m | xargs[33m`[39;49;00m [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m$
   564^I[36mendif # MOZ_DEBUG_SYMBOLS[39;49;00m$
   565^I[36mifdef MOZ_PROFILE[39;49;00m$
   566^I^I[36mecho[39;49;00m splitting symbols out of binaries$
   567^I^I/bin/find [34m$([39;49;00mDIST[34m)[39;49;00m -name [33m"*.dll"[39;49;00m -exec splitsym {} [33m\;[39;49;00m$
   568^I^I/bin/find [34m$([39;49;00mDIST[34m)[39;49;00m -name [33m"*.exe"[39;49;00m -exec splitsym {} [33m\;[39;49;00m$
   569^I^I/bin/find [34m$([39;49;00mDIST[34m)[39;49;00m -name [33m"*.EXE"[39;49;00m -exec splitsym {} [33m\;[39;49;00m$
   570^I^Imkdir -p [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m$
   571^I^I/bin/find [34m$([39;49;00mDIST[34m)[39;49;00m -name [33m"*.dbg"[39;49;00m -exec mv {} [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m [33m\;[39;49;00m$
   572^I[36mendif # MOZ_PROFILE[39;49;00m$
   573^I[36mendif # MOZILLA_OFFICIAL[39;49;00m$
   574^I$
   575^I[32msignnss[39;49;00m:$
   576^I[36mifdef MOZILLA_OFFICIAL[39;49;00m$
   577^I^I[36mecho[39;49;00m signing NSS libs$
   578^I^I[36mcd[39;49;00m [34m$([39;49;00mDIST[34m)[39;49;00m/bin; ./shlibsign.exe -v -i softokn3.dll$
   579^I^I[36mcd[39;49;00m [34m$([39;49;00mDIST[34m)[39;49;00m/bin; ./shlibsign.exe -v -i freebl3.dll$
   580^I[36mendif # MOZILLA_OFFICIAL[39;49;00m$
   581^I$
   582^I[31mBUILDID[39;49;00m = [34m$([39;49;00mshell cat [34m$([39;49;00mDEPTH[34m)[39;49;00m/config/build_number[34m)[39;49;00m$
   583^I[32mdeliver[39;49;00m: splitsymbols rebase signnss$
   584^I$
   585^I[36mendif # WINNT[39;49;00m$
