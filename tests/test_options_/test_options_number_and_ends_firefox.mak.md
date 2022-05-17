     1	[37m#[39;49;00m$
     2	[37m# ***** BEGIN LICENSE BLOCK *****[39;49;00m$
     3	[37m# Version: MPL 1.1/GPL 2.0/LGPL 2.1[39;49;00m$
     4	[37m#[39;49;00m$
     5	[37m# The contents of this file are subject to the Mozilla Public License Version[39;49;00m$
     6	[37m# 1.1 (the "License"); you may not use this file except in compliance with[39;49;00m$
     7	[37m# the License. You may obtain a copy of the License at[39;49;00m$
     8	[37m# http://www.mozilla.org/MPL/[39;49;00m$
     9	[37m#[39;49;00m$
    10	[37m# Software distributed under the License is distributed on an "AS IS" basis,[39;49;00m$
    11	[37m# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License[39;49;00m$
    12	[37m# for the specific language governing rights and limitations under the[39;49;00m$
    13	[37m# License.[39;49;00m$
    14	[37m#[39;49;00m$
    15	[37m# The Original Code is mozilla.org code.[39;49;00m$
    16	[37m#[39;49;00m$
    17	[37m# The Initial Developer of the Original Code is[39;49;00m$
    18	[37m# Netscape Communications Corporation.[39;49;00m$
    19	[37m# Portions created by the Initial Developer are Copyright (C) 1998[39;49;00m$
    20	[37m# the Initial Developer. All Rights Reserved.[39;49;00m$
    21	[37m#[39;49;00m$
    22	[37m# Contributor(s):[39;49;00m$
    23	[37m#[39;49;00m$
    24	[37m# Alternatively, the contents of this file may be used under the terms of[39;49;00m$
    25	[37m# either the GNU General Public License Version 2 or later (the "GPL"), or[39;49;00m$
    26	[37m# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),[39;49;00m$
    27	[37m# in which case the provisions of the GPL or the LGPL are applicable instead[39;49;00m$
    28	[37m# of those above. If you wish to allow use of your version of this file only[39;49;00m$
    29	[37m# under the terms of either the GPL or the LGPL, and not to allow others to[39;49;00m$
    30	[37m# use your version of this file under the terms of the MPL, indicate your[39;49;00m$
    31	[37m# decision by deleting the provisions above and replace them with the notice[39;49;00m$
    32	[37m# and other provisions required by the GPL or the LGPL. If you do not delete[39;49;00m$
    33	[37m# the provisions above, a recipient may use your version of this file under[39;49;00m$
    34	[37m# the terms of any one of the MPL, the GPL or the LGPL.[39;49;00m$
    35	[37m#[39;49;00m$
    36	[37m# ***** END LICENSE BLOCK *****[39;49;00m$
    37	$
    38	[31mDEPTH[39;49;00m		= .$
    39	[31mtopsrcdir[39;49;00m	= @top_srcdir@$
    40	[31msrcdir[39;49;00m		= @srcdir@$
    41	[31mVPATH[39;49;00m		= @srcdir@$
    42	$
    43	[36minclude $(DEPTH)/config/autoconf.mk[39;49;00m$
    44	$
    45	[36minclude $(topsrcdir)/build/unix/modules.mk[39;49;00m$
    46	$
    47	[36mifeq ($(BUILD_MODULES),all)[39;49;00m$
    48	[37m#[39;49;00m$
    49	[37m# And now for something completely different...[39;49;00m$
    50	[37m# Divide the default build into tiers. [39;49;00m$
    51	[37m# Tiers must be defined on module boundaries [39;49;00m$
    52	[37m#[39;49;00m$
    53	[31mSUPPRESS_DEFAULT_RULES[39;49;00m = [34m1[39;49;00m$
    54	$
    55	[32mdefault alldep all[39;49;00m:: [34m$([39;49;00m[31mSUBMAKEFILES[39;49;00m[34m)[39;49;00m$
    56		[34m$([39;49;00mRM[34m)[39;49;00m -rf [34m$([39;49;00mDIST[34m)[39;49;00m/sdk$
    57		[34m$([39;49;00mRM[34m)[39;49;00m -rf [34m$([39;49;00mDIST[34m)[39;49;00m/include$
    58		[34m$([39;49;00mMAKE[34m)[39;49;00m -C config [36mexport[39;49;00m$
    59		[34m$([39;49;00mMAKE[34m)[39;49;00m nspr$
    60		[34m$([39;49;00mMAKE[34m)[39;49;00m ldap$
    61		[34m$([39;49;00mMAKE[34m)[39;49;00m tier_0$
    62		[34m$([39;49;00mMAKE[34m)[39;49;00m tier_1$
    63		[34m$([39;49;00mMAKE[34m)[39;49;00m tier_2$
    64		[34m$([39;49;00mMAKE[34m)[39;49;00m tier_9$
    65		[34m$([39;49;00mMAKE[34m)[39;49;00m tier_50$
    66		[34m$([39;49;00mMAKE[34m)[39;49;00m tier_99$
    67	$
    68	[37m# Make sure that the existing rulesets work[39;49;00m$
    69	[31mDIRS[39;49;00m = [33m\[39;49;00m$
    70		[34m$([39;49;00mtier_0_dirs[34m)[39;49;00m [33m\[39;49;00m$
    71		[34m$([39;49;00mtier_1_dirs[34m)[39;49;00m [33m\[39;49;00m$
    72		[34m$([39;49;00mtier_2_dirs[34m)[39;49;00m [33m\[39;49;00m$
    73		[34m$([39;49;00mtier_9_dirs[34m)[39;49;00m [33m\[39;49;00m$
    74		[34m$([39;49;00mtier_50_dirs[34m)[39;49;00m [33m\[39;49;00m$
    75		[34m$([39;49;00mNULL[34m)[39;49;00m$
    76	$
    77	[36mifdef GC_LEAK_DETECTOR[39;49;00m$
    78	[31mDIRS[39;49;00m += gc/boehm$
    79	[36mendif[39;49;00m$
    80	$
    81	[31mDIRS[39;49;00m	+= [34m$([39;49;00mtier_99_dirs[34m)[39;49;00m$
    82	$
    83	[37m#[39;49;00m$
    84	[37m# tier 0 - base build config dirs[39;49;00m$
    85	[37m# [39;49;00m$
    86	[31mtier_0_dirs[39;49;00m = [33m\[39;49;00m$
    87		config [33m\[39;49;00m$
    88		build [33m\[39;49;00m$
    89		[34m$([39;49;00mNULL[34m)[39;49;00m$
    90	$
    91	[37m#[39;49;00m$
    92	[37m# tier 1 -  3rd party individual libraries[39;49;00m$
    93	[37m#[39;49;00m$
    94	[31mtier_1_dirs[39;49;00m	+= dbm$
    95	$
    96	[36mifndef MOZ_NATIVE_JPEG[39;49;00m$
    97	[31mtier_1_dirs[39;49;00m	+= jpeg$
    98	[36mendif[39;49;00m$
    99	$
   100	[36mifndef MOZ_NATIVE_ZLIB[39;49;00m$
   101	[31mtier_1_dirs[39;49;00m	+= modules/zlib$
   102	[36mendif[39;49;00m$
   103	$
   104	[37m# Installer needs standalone libjar, hence standalone zlib[39;49;00m$
   105	[36mifdef MOZ_INSTALLER[39;49;00m$
   106	[31mtier_1_dirs[39;49;00m	+= modules/zlib/standalone$
   107	[36mendif[39;49;00m$
   108	$
   109	[36mifdef MOZ_UPDATER[39;49;00m$
   110	[31mtier_1_dirs[39;49;00m += modules/libbz2$
   111	[31mtier_1_dirs[39;49;00m += modules/libmar$
   112	[36mendif[39;49;00m$
   113	$
   114	[36mifdef MOZ_SVG_RENDERER_LIBART[39;49;00m$
   115	[31mtier_1_dirs[39;49;00m	+= other-licenses/libart_lgpl$
   116	[36mendif[39;49;00m$
   117	$
   118	[37m#[39;49;00m$
   119	[37m# tier 2 - base libraries[39;49;00m$
   120	[37m# [39;49;00m$
   121	[31mtier_2_dirs[39;49;00m	= [33m\[39;49;00m$
   122			js [33m\[39;49;00m$
   123			xpcom [33m\[39;49;00m$
   124			[34m$([39;49;00mNULL[34m)[39;49;00m$
   125	$
   126	[36mifndef MOZ_NO_XPCOM_OBSOLETE[39;49;00m$
   127	[31mtier_2_dirs[39;49;00m += modules/libreg xpcom/obsolete$
   128	[36mendif[39;49;00m$
   129	$
   130	[36mifdef NS_TRACE_MALLOC[39;49;00m$
   131	[31mtier_2_dirs[39;49;00m	+= tools/trace-malloc/lib$
   132	[36mendif[39;49;00m$
   133	$
   134	[37m#[39;49;00m$
   135	[37m# tier 9 - core components (necko,gecko)[39;49;00m$
   136	[37m#[39;49;00m$
   137	$
   138	[31mtier_9_dirs[39;49;00m += [33m\[39;49;00m$
   139			js/src/xpconnect [33m\[39;49;00m$
   140			intl [33m\[39;49;00m$
   141			db [33m\[39;49;00m$
   142			[34m$([39;49;00mNULL[34m)[39;49;00m$
   143	$
   144	[36mifdef MOZ_STORAGE[39;49;00m$
   145	[31mtier_9_dirs[39;49;00m += storage$
   146	[36mendif[39;49;00m$
   147	$
   148	[36mifdef MOZ_ENABLE_XLIB[39;49;00m$
   149	[31mtier_9_dirs[39;49;00m	+= gfx/src/xlibrgb widget/src/xlibxtbin$
   150	[36mendif[39;49;00m$
   151	$
   152	[36mifdef MOZ_ENABLE_GTK[39;49;00m$
   153	[31mtier_9_dirs[39;49;00m	+= widget/src/gtksuperwin widget/src/gtkxtbin$
   154	[36mendif[39;49;00m$
   155	$
   156	[36mifdef MOZ_ENABLE_GTK2[39;49;00m$
   157	[31mtier_9_dirs[39;49;00m     += widget/src/gtkxtbin$
   158	[36mendif[39;49;00m$
   159	$
   160	[36mifdef MOZ_IPCD[39;49;00m$
   161	[31mtier_9_dirs[39;49;00m += ipc/ipcd$
   162	[36mendif[39;49;00m$
   163	$
   164	[36mifdef MOZ_JSDEBUGGER[39;49;00m$
   165	[31mtier_9_dirs[39;49;00m += js/jsd$
   166	[36mendif[39;49;00m$
   167	$
   168	[31mtier_9_dirs[39;49;00m	+= [33m\[39;49;00m$
   169			modules/libutil [33m\[39;49;00m$
   170			netwerk [33m\[39;49;00m$
   171			modules/libjar [33m\[39;49;00m$
   172			uriloader [33m\[39;49;00m$
   173			modules/libpref [33m\[39;49;00m$
   174			modules/libimg [33m\[39;49;00m$
   175			caps [33m\[39;49;00m$
   176			rdf [33m\[39;49;00m$
   177			parser/expat [33m\[39;49;00m$
   178			parser/xml [33m\[39;49;00m$
   179			parser/htmlparser [33m\[39;49;00m$
   180			gfx [33m\[39;49;00m$
   181			modules/libpr0n [33m\[39;49;00m$
   182			sun-java [33m\[39;49;00m$
   183			modules/plugin [33m\[39;49;00m$
   184			dom [33m\[39;49;00m$
   185			view [33m\[39;49;00m$
   186			widget [33m\[39;49;00m$
   187			content [33m\[39;49;00m$
   188			layout [33m\[39;49;00m$
   189			xpfe/components/shistory [33m\[39;49;00m$
   190			docshell [33m\[39;49;00m$
   191			webshell [33m\[39;49;00m$
   192			embedding [33m\[39;49;00m$
   193			editor [33m\[39;49;00m$
   194			xpfe/appshell [33m\[39;49;00m$
   195			[34m$([39;49;00mNULL[34m)[39;49;00m$
   196	$
   197	[36mifdef MOZ_OJI[39;49;00m$
   198	[31mtier_9_dirs[39;49;00m	+= [33m\[39;49;00m$
   199			js/src/liveconnect [33m\[39;49;00m$
   200			modules/oji [33m\[39;49;00m$
   201			[34m$([39;49;00mNULL[34m)[39;49;00m$
   202	[36mendif[39;49;00m$
   203	$
   204	[36mifdef ACCESSIBILITY[39;49;00m$
   205	[31mtier_9_dirs[39;49;00m    += accessible$
   206	[36mendif[39;49;00m$
   207	$
   208	[37m# [39;49;00m$
   209	[37m# tier 50 - xpfe & toolkit[39;49;00m$
   210	[37m#[39;49;00m$
   211	$
   212	[36mifdef MOZ_XUL[39;49;00m$
   213	[36mifdef MOZ_XUL_APP[39;49;00m$
   214	[31mtier_50_dirs[39;49;00m += chrome$
   215	[36melse[39;49;00m$
   216	[31mtier_50_dirs[39;49;00m += rdf/chrome$
   217	[36mendif[39;49;00m$
   218	[36melse[39;49;00m$
   219	[31mtier_50_dirs[39;49;00m += embedding/minimo/chromelite$
   220	[36mendif[39;49;00m$
   221	$
   222	[31mtier_50_dirs[39;49;00m += profile$
   223	$
   224	[37m# This must preceed xpfe[39;49;00m$
   225	[36mifdef MOZ_JPROF[39;49;00m$
   226	[31mtier_50_dirs[39;49;00m        += tools/jprof$
   227	[36mendif[39;49;00m$
   228	$
   229	[36mifneq (,$(filter mac cocoa,$(MOZ_WIDGET_TOOLKIT)))[39;49;00m$
   230	[31mtier_50_dirs[39;49;00m	+= xpfe/bootstrap/appleevents$
   231	[36mendif[39;49;00m$
   232	$
   233	[31mtier_50_dirs[39;49;00m	+= [33m\[39;49;00m$
   234		xpfe [33m\[39;49;00m$
   235		toolkit/components [33m\[39;49;00m$
   236		[34m$([39;49;00mNULL[34m)[39;49;00m$
   237	$
   238	[36mifndef MOZ_XUL_APP[39;49;00m$
   239	[31mtier_50_dirs[39;49;00m += themes$
   240	[36mendif[39;49;00m$
   241	$
   242	[36mifdef MOZ_ENABLE_XREMOTE[39;49;00m$
   243	[31mtier_50_dirs[39;49;00m += widget/src/xremoteclient$
   244	[36mendif[39;49;00m$
   245	$
   246	[36mifdef MOZ_XUL_APP[39;49;00m$
   247	[31mtier_50_dirs[39;49;00m	+= toolkit$
   248	[36mendif[39;49;00m$
   249	$
   250	[36mifdef MOZ_PHOENIX[39;49;00m$
   251	[37m#XXXBlake this shell path is a temp hack; toolkit shouldn't depend on browser[39;49;00m$
   252	[31mtier_50_dirs[39;49;00m    += browser/components/shell/public$
   253	[36mendif[39;49;00m$
   254	$
   255	[36mifdef MOZ_XPINSTALL[39;49;00m$
   256	[31mtier_50_dirs[39;49;00m     +=  xpinstall$
   257	[36mendif[39;49;00m$
   258	$
   259	[37m# JavaXPCOM JNI code is compiled into libXUL[39;49;00m$
   260	[36mifdef MOZ_JAVAXPCOM[39;49;00m$
   261	[31mtier_50_dirs[39;49;00m	+= extensions/java/xpcom/src$
   262	[36mendif[39;49;00m$
   263	$
   264	[36mifdef MOZ_ENABLE_LIBXUL[39;49;00m$
   265	[31mtier_50_dirs[39;49;00m += [33m\[39;49;00m$
   266			toolkit/library [33m\[39;49;00m$
   267			xpcom/stub [33m\[39;49;00m$
   268			[34m$([39;49;00mNULL[34m)[39;49;00m$
   269	[36mendif[39;49;00m$
   270	$
   271	[36mifdef NS_TRACE_MALLOC[39;49;00m$
   272	[31mtier_50_dirs[39;49;00m += tools/trace-malloc$
   273	[36mendif[39;49;00m$
   274	$
   275	[36mifdef MOZ_PSM[39;49;00m$
   276	[31mtier_50_dirs[39;49;00m	+= security/manager$
   277	[36melse[39;49;00m$
   278	[31mtier_50_dirs[39;49;00m	+= security/manager/boot/public security/manager/ssl/public$
   279	[36mendif[39;49;00m$
   280	$
   281	[36mifdef MOZ_LDAP_XPCOM[39;49;00m$
   282	[31mtier_50_dirs[39;49;00m	+= directory/xpcom$
   283	[36mendif[39;49;00m$
   284	$
   285	[36mifndef MINIMO[39;49;00m$
   286	[36mifdef MOZ_XUL_APP[39;49;00m$
   287	[36mifdef MOZ_ENABLE_GTK2[39;49;00m$
   288	[31mtier_50_dirs[39;49;00m    += toolkit/components/gnome$
   289	[36mendif[39;49;00m$
   290	[36mendif[39;49;00m$
   291	[36mendif[39;49;00m$
   292	$
   293	[36mifdef MOZ_LEAKY[39;49;00m$
   294	[31mtier_50_dirs[39;49;00m        += tools/leaky$
   295	[36mendif[39;49;00m$
   296	$
   297	[36mifdef MOZ_MAPINFO[39;49;00m$
   298	[31mtier_50_dirs[39;49;00m	+= tools/codesighs$
   299	[36mendif[39;49;00m$
   300	$
   301	[37m#[39;49;00m$
   302	[37m# tier 99 - application features[39;49;00m$
   303	[37m#[39;49;00m$
   304	$
   305	[36mifdef MOZ_MAIL_NEWS[39;49;00m$
   306	[31mtier_99_dirs[39;49;00m	+= mailnews$
   307	[36mendif[39;49;00m$
   308	$
   309	[36mifdef MOZ_CALENDAR[39;49;00m$
   310	[31mtier_99_dirs[39;49;00m	+= calendar$
   311	[36mendif[39;49;00m$
   312	$
   313	[36mifdef MOZ_EXTENSIONS[39;49;00m$
   314	[31mtier_99_dirs[39;49;00m	+= extensions$
   315	[36mendif[39;49;00m$
   316	$
   317	[36mifdef MOZ_JAVAXPCOM[39;49;00m$
   318	[31mtier_99_dirs[39;49;00m	+= extensions/java$
   319	[36mendif[39;49;00m$
   320	$
   321	[37m# axcontrol[39;49;00m$
   322	[36mifeq ($(OS_ARCH),WINNT)[39;49;00m$
   323	[36mifndef MOZ_NO_ACTIVEX_SUPPORT[39;49;00m$
   324	[31mtier_99_dirs[39;49;00m += [33m\[39;49;00m$
   325			embedding/browser/activex/src/control [33m\[39;49;00m$
   326			embedding/browser/activex/src/control_kicker [33m\[39;49;00m$
   327			[34m$([39;49;00mNULL[34m)[39;49;00m$
   328	[36mendif[39;49;00m$
   329	[36mendif[39;49;00m$
   330	$
   331	[37m# Java Embedding Plugin[39;49;00m$
   332	[36mifneq (,$(filter mac cocoa,$(MOZ_WIDGET_TOOLKIT)))[39;49;00m$
   333	[31mtier_99_dirs[39;49;00m += plugin/oji/JEP$
   334	[36mendif[39;49;00m$
   335	$
   336	[36mifneq (,$(filter browser suite,$(MOZ_BUILD_APP)))[39;49;00m$
   337	[31mtier_99_dirs[39;49;00m += xpfe/components/search$
   338	[36mendif[39;49;00m$
   339	$
   340	[36mifdef MOZ_BRANDING_DIRECTORY[39;49;00m$
   341	[31mtier_99_dirs[39;49;00m += [34m$([39;49;00mMOZ_BRANDING_DIRECTORY[34m)[39;49;00m$
   342	[36mendif[39;49;00m$
   343	$
   344	[36mifdef MOZ_PHOENIX[39;49;00m$
   345	[31mtier_99_dirs[39;49;00m	+= browser xpfe/bootstrap/init.d$
   346	[36mendif[39;49;00m$
   347	$
   348	[36mifdef MOZ_XULRUNNER[39;49;00m$
   349	[31mtier_99_dirs[39;49;00m	+= xulrunner$
   350	[36mendif[39;49;00m$
   351	$
   352	[36mifdef MOZ_COMPOSER[39;49;00m$
   353	[31mtier_99_dirs[39;49;00m	+= editor/ui$
   354	[36mendif[39;49;00m$
   355	$
   356	[36mifdef MOZ_THUNDERBIRD[39;49;00m$
   357	[31mtier_99_dirs[39;49;00m	+= mail xpfe/bootstrap/init.d$
   358	[36mendif[39;49;00m$
   359	$
   360	[36mifdef MOZ_STANDALONE_COMPOSER[39;49;00m$
   361	[31mtier_99_dirs[39;49;00m	+= composer$
   362	[36mendif[39;49;00m$
   363	$
   364	[36mifdef MOZ_SUNBIRD[39;49;00m$
   365	[31mtier_99_dirs[39;49;00m	+= calendar/sunbird$
   366	[36mendif[39;49;00m$
   367	$
   368	[36mifdef MOZ_SUITE[39;49;00m$
   369	[31mtier_99_dirs[39;49;00m	+= suite$
   370	[36mendif[39;49;00m$
   371	$
   372	[36mifdef MINIMO[39;49;00m$
   373	[31mtier_99_dirs[39;49;00m	+= minimo$
   374	[36mendif[39;49;00m$
   375	$
   376	[36mifdef MOZ_XUL_APP[39;49;00m$
   377	[36mifdef MOZ_INSTALLER[39;49;00m$
   378	[31mtier_99_dirs[39;49;00m     +=  toolkit/mozapps/installer$
   379	[36mendif[39;49;00m$
   380	[36melse[39;49;00m$
   381	[36mifneq (,$(MOZ_XPFE_COMPONENTS)$(MOZ_XUL))[39;49;00m$
   382	[36mifndef MINIMO[39;49;00m$
   383	[31mtier_99_dirs[39;49;00m	+= xpfe/bootstrap$
   384	[36mendif[39;49;00m$
   385	[36mendif[39;49;00m$
   386	[36mendif[39;49;00m$
   387	$
   388	[36mifneq (,$(MOZ_ENABLE_GTK)$(MOZ_ENABLE_GTK2))[39;49;00m$
   389	[31mtier_99_dirs[39;49;00m	+= embedding/browser/gtk$
   390	[36mendif[39;49;00m$
   391	$
   392	[37m# viewer[39;49;00m$
   393	[36mifneq (,$(ENABLE_TESTS))[39;49;00m$
   394	[36mifndef MOZ_ENABLE_LIBXUL[39;49;00m$
   395	[31mtier_99_dirs[39;49;00m += webshell/tests$
   396	[36mendif[39;49;00m$
   397	[36mendif[39;49;00m$
   398	$
   399	[37m# winembed, mfcembed[39;49;00m$
   400	[36mifeq ($(OS_ARCH),WINNT)[39;49;00m$
   401	[36mifneq (,$(ENABLE_TESTS)$(MOZILLA_OFFICIAL))[39;49;00m$
   402	[31mtier_99_dirs[39;49;00m += embedding/tests$
   403	[36mendif[39;49;00m$
   404	[36mendif[39;49;00m$
   405	$
   406	[37m# os2embed[39;49;00m$
   407	[36mifeq ($(OS_ARCH),OS2)[39;49;00m$
   408	[36mifneq (,$(ENABLE_TESTS)$(MOZILLA_OFFICIAL))[39;49;00m$
   409	[31mtier_99_dirs[39;49;00m += embedding/tests$
   410	[36mendif[39;49;00m$
   411	[36mendif[39;49;00m$
   412	$
   413	[36mifeq ($(MOZ_BUILD_APP),macbrowser)[39;49;00m$
   414	[31mtier_99_dirs[39;49;00m += [33m\[39;49;00m$
   415		embedding/config [33m\[39;49;00m$
   416		camino [33m\[39;49;00m$
   417		[34m$([39;49;00mNULL[34m)[39;49;00m$
   418	[36mendif[39;49;00m$
   419	$
   420	[37m# test harnesses [39;49;00m$
   421	[36mifdef ENABLE_TESTS[39;49;00m$
   422	[31mtier_99_dirs[39;49;00m += tools/test-harness$
   423	[36mendif[39;49;00m$
   424	$
   425	[36melse[39;49;00m$
   426	$
   427	[37m# Standalone build[39;49;00m$
   428	$
   429	[31mDIRS[39;49;00m		= [34m$([39;49;00mBUILD_MODULE_DIRS[34m)[39;49;00m$
   430	$
   431	[37m# Hack to generate xpidl Makefile[39;49;00m$
   432	[36mifneq ($(BUILD_MODULES),all)[39;49;00m$
   433	[36mifneq (,$(findstring xpcom, $(BUILD_MODULE_DIRS)))[39;49;00m$
   434	[31mDIRS[39;49;00m		:= xpcom/typelib [34m$([39;49;00mDIRS[34m)[39;49;00m$
   435	[31mSUBMAKEFILES[39;49;00m	:= xpcom/typelib/Makefile$
   436	[36mendif[39;49;00m$
   437	[36mendif[39;49;00m$
   438	$
   439	[32mdefault[39;49;00m:: [34m$([39;49;00m[31mSUBMAKEFILES[39;49;00m[34m)[39;49;00m$
   440		[34m$([39;49;00mMAKE[34m)[39;49;00m [36mexport[39;49;00m$
   441		[34m$([39;49;00mMAKE[34m)[39;49;00m libs$
   442	$
   443	[36mendif # BUILD_MODULES == all[39;49;00m$
   444	$
   445	[31mSTATIC_MAKEFILES[39;49;00m := nsprpub directory/c-sdk security/nss$
   446	$
   447	[31mGARBAGE_DIRS[39;49;00m += dist$
   448	[31mDIST_GARBAGE[39;49;00m = config.cache config.log config.status config-defs.h [33m\[39;49;00m$
   449	   dependencies.beos config/autoconf.mk config/myrules.mk config/myconfig.mk [33m\[39;49;00m$
   450	   unallmakefiles mozilla-config.h [33m\[39;49;00m$
   451	   [34m$([39;49;00mtopsrcdir[34m)[39;49;00m/.mozconfig.mk [34m$([39;49;00mtopsrcdir[34m)[39;49;00m/.mozconfig.out $
   452	$
   453	[37m# Build pseudo-external modules first when export is explicitly called[39;49;00m$
   454	[32mexport[39;49;00m::$
   455		[34m$([39;49;00mRM[34m)[39;49;00m -rf [34m$([39;49;00mDIST[34m)[39;49;00m/sdk$
   456		[34m$([39;49;00mMAKE[34m)[39;49;00m -C config [36mexport[39;49;00m$
   457		[34m$([39;49;00mMAKE[34m)[39;49;00m nspr$
   458		[34m$([39;49;00mMAKE[34m)[39;49;00m ldap$
   459	[36mifneq ($(BUILD_MODULES),all)[39;49;00m$
   460	[36mifneq (,$(findstring xpcom, $(BUILD_MODULE_DIRS)))[39;49;00m$
   461		[34m$([39;49;00mMAKE[34m)[39;49;00m -C xpcom/typelib$
   462		[34m$([39;49;00mMAKE[34m)[39;49;00m export-idl$
   463	[36mendif[39;49;00m$
   464	[36mendif[39;49;00m$
   465	$
   466	[32minstall[39;49;00m::$
   467	[36mifndef MOZ_NATIVE_NSPR[39;49;00m$
   468		[34m$([39;49;00mMAKE[34m)[39;49;00m -C nsprpub real_install [31mDESTDIR[39;49;00m=[34m$([39;49;00mDESTDIR[34m)[39;49;00m [31mlibdir[39;49;00m=[34m$([39;49;00mmozappdir[34m)[39;49;00m [31mincludedir[39;49;00m=[34m$([39;49;00mincludedir[34m)[39;49;00m/nspr$
   469		[34m$([39;49;00mRM[34m)[39;49;00m -f [34m$([39;49;00maddprefix [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mmozappdir[34m)[39;49;00m/[34m$([39;49;00mLIB_PREFIX[34m)[39;49;00m, [34m$([39;49;00maddsuffix .[34m$([39;49;00mLIB_SUFFIX[34m)[39;49;00m, nspr4 plds4 plc4[34m)[39;49;00m[34m)[39;49;00m$
   470		[34m$([39;49;00mRM[34m)[39;49;00m -f [34m$([39;49;00maddprefix [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mbindir[34m)[39;49;00m/,nspr-config compile-et.pl prerr.properties[34m)[39;49;00m$
   471	[36mendif[39;49;00m$
   472	[36mifdef MOZ_LDAP_XPCOM[39;49;00m$
   473		[34m$([39;49;00mMAKE[34m)[39;49;00m -C directory/c-sdk real_install [31mDESTDIR[39;49;00m=[34m$([39;49;00mDESTDIR[34m)[39;49;00m [31mlibdir[39;49;00m=[34m$([39;49;00mmozappdir[34m)[39;49;00m [31mincludedir[39;49;00m=[34m$([39;49;00mincludedir[34m)[39;49;00m/ldap$
   474	[36mendif[39;49;00m$
   475	$
   476	[36minclude $(topsrcdir)/config/rules.mk[39;49;00m$
   477	$
   478	[37m# Clean up after pseudo-external modules[39;49;00m$
   479	[32mclean clobber realclean clobber_all distclean[39;49;00m::$
   480	[36mifndef MOZ_NATIVE_NSPR[39;49;00m$
   481		[34m$([39;49;00mMAKE[34m)[39;49;00m -C nsprpub [31m$@[39;49;00m$
   482	[36mendif[39;49;00m$
   483	[36mifdef MOZ_LDAP_XPCOM[39;49;00m$
   484		[34m$([39;49;00mMAKE[34m)[39;49;00m -C directory/c-sdk [31m$@[39;49;00m$
   485	[36mendif[39;49;00m$
   486	$
   487	[37m# Map mozilla targets to standard automake target[39;49;00m$
   488	[36mifdef MOZ_ENABLE_LIBXUL[39;49;00m$
   489	[32mtier_50[39;49;00m: [34m$([39;49;00m[31maddsuffix[39;49;00m /[31mMakefile[39;49;00m, [34m$[39;49;00m[34m([39;49;00m[31mfilter-out[39;49;00m [34m$[39;49;00m[34m([39;49;00m[31mSTATIC_MAKEFILES[39;49;00m[34m)[39;49;00m, [34m$[39;49;00m[34m([39;49;00m[34m$[39;49;00m@[31m_dirs[39;49;00m[34m)[39;49;00m[34m)[39;49;00m[34m)[39;49;00m$
   490		@echo [33m"[39;49;00m[33mtier_50: [39;49;00m[34m$([39;49;00mtier_50_dirs[34m)[39;49;00m[33m"[39;49;00m$
   491		@[34m$([39;49;00mEXIT_ON_ERROR[34m)[39;49;00m [33m\[39;49;00m$
   492		[34mfor[39;49;00m d [34min[39;49;00m [34m$([39;49;00mtier_50_dirs[34m)[39;49;00m; [34mdo[39;49;00m [33m\[39;49;00m$
   493		    [34m$([39;49;00mUPDATE_TITLE[34m)[39;49;00m [33m\[39;49;00m$
   494	[36m	    if test ! -f $$d/Makefile; then \[39;49;00m$
   495	[36m	      $(PERL) $(AUTOCONF_TOOLS)/make-makefile -t $(topsrcdir) -d $(DEPTH) $(CYGWIN_TOPSRCDIR) $$d/Makefile; \[39;49;00m$
   496	[36m	    fi; \[39;49;00m$
   497	[36m	    $(MAKE) -C $$d export; \[39;49;00m$
   498	[36m	done ; \[39;49;00m$
   499	[36m	for d in $(tier_50_dirs); do \[39;49;00m$
   500	[36m	    $(UPDATE_TITLE) \[39;49;00m$
   501	[36m	    $(MAKE) -C $$d libs; \[39;49;00m$
   502	[36m	done[39;49;00m$
   503		@echo [33m"Building tools from tier 2/9/50"[39;49;00m$
   504		@[34m$([39;49;00mEXIT_ON_ERROR[34m)[39;49;00m [33m\[39;49;00m$
   505		[34mfor[39;49;00m d [34min[39;49;00m [34m$([39;49;00mtier_2_dirs[34m)[39;49;00m [34m$([39;49;00mtier_9_dirs[34m)[39;49;00m [34m$([39;49;00mtier_50_dirs[34m)[39;49;00m; [34mdo[39;49;00m [33m\[39;49;00m$
   506		    [34m$([39;49;00mUPDATE_TITLE[34m)[39;49;00m [33m\[39;49;00m$
   507		    [34m$([39;49;00mMAKE[34m)[39;49;00m -C [31m$$[39;49;00md tools; [33m\[39;49;00m$
   508		[34mdone[39;49;00m;$
   509	[36mendif[39;49;00m$
   510	$
   511	[32mtier_%[39;49;00m:$
   512		@echo [33m"[39;49;00m[31m$@[39;49;00m[33m: [39;49;00m[34m$([39;49;00m[31m$@[39;49;00m_dirs[34m)[39;49;00m[33m"[39;49;00m$
   513		@[34m$([39;49;00mEXIT_ON_ERROR[34m)[39;49;00m [33m\[39;49;00m$
   514		  [34mfor[39;49;00m d [34min[39;49;00m [34m$([39;49;00m[31m$@[39;49;00m_dirs[34m)[39;49;00m; [34mdo[39;49;00m [33m\[39;49;00m$
   515		    [34m$([39;49;00mUPDATE_TITLE[34m)[39;49;00m [33m\[39;49;00m$
   516	[36m	    if test ! -f $$d/Makefile; then \[39;49;00m$
   517	[36m	      $(PERL) $(AUTOCONF_TOOLS)/make-makefile -t $(topsrcdir) -d $(DEPTH) $(CYGWIN_TOPSRCDIR) $$d/Makefile; \[39;49;00m$
   518	[36m	    fi; \[39;49;00m$
   519	[36m	    $(MAKE) -C $$d export; \[39;49;00m$
   520	[36m	  done ; \[39;49;00m$
   521	[36m	  for d in $($@_dirs); do $(UPDATE_TITLE) \[39;49;00m$
   522	[36m	    $(MAKE) -C $$d libs; \[39;49;00m$
   523	[36m	  done[39;49;00m$
   524	$
   525	[37m#[39;49;00m$
   526	[37m# Individual modules[39;49;00m$
   527	[37m#[39;49;00m$
   528	[32mboehm[39;49;00m:$
   529	[36mifdef GC_LEAK_DETECTOR[39;49;00m$
   530		[34m$([39;49;00mMAKE[34m)[39;49;00m -C gc/boehm$
   531	[36mendif[39;49;00m$
   532	$
   533	[32mnspr[39;49;00m: boehm$
   534	[36mifndef MOZ_NATIVE_NSPR[39;49;00m$
   535		[34m$([39;49;00mMAKE[34m)[39;49;00m -C nsprpub$
   536	[36mendif[39;49;00m$
   537	$
   538	[32mldap[39;49;00m:$
   539	[36mifdef MOZ_LDAP_XPCOM[39;49;00m$
   540		[34m$([39;49;00mMAKE[34m)[39;49;00m -C directory/c-sdk$
   541	[36mendif[39;49;00m$
   542	$
   543	[32mdistclean[39;49;00m::$
   544		cat unallmakefiles | [34m$([39;49;00mXARGS[34m)[39;49;00m rm -f$
   545		rm -f unallmakefiles [34m$([39;49;00mDIST_GARBAGE[34m)[39;49;00m$
   546	$
   547	[36mifeq ($(OS_ARCH),WINNT)[39;49;00m$
   548	[32mrebase[39;49;00m:$
   549	[36mifdef MOZILLA_OFFICIAL[39;49;00m$
   550		[36mecho[39;49;00m rebasing [34m$([39;49;00mDIST[34m)[39;49;00m$
   551		/bin/find [34m$([39;49;00mDIST[34m)[39;49;00m -name [33m"*.dll"[39;49;00m > rebase.lst$
   552		rebase -b [34m60000000[39;49;00m -R . -G rebase.lst$
   553		rm rebase.lst$
   554	[36mendif[39;49;00m$
   555	$
   556	[32msplitsymbols[39;49;00m:$
   557	[36mifdef MOZILLA_OFFICIAL[39;49;00m$
   558	[36mifdef MOZ_DEBUG_SYMBOLS[39;49;00m$
   559		[36mecho[39;49;00m finding pdb files$
   560		mkdir -p [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m$
   561		-cp [33m`[39;49;00m/bin/find . -path [33m"./dist"[39;49;00m -prune -o -name [33m"*.dll"[39;49;00m | sed [33m"[39;49;00m[33ms/\.dll[39;49;00m[31m$$[39;49;00m[33m/\.pdb/[39;49;00m[33m"[39;49;00m | xargs[33m`[39;49;00m [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m$
   562		-cp [33m`[39;49;00m/bin/find . -path [33m"./dist"[39;49;00m -prune -o -name [33m"*.exe"[39;49;00m | sed [33m"[39;49;00m[33ms/\.exe[39;49;00m[31m$$[39;49;00m[33m/\.pdb/[39;49;00m[33m"[39;49;00m | xargs[33m`[39;49;00m [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m$
   563		-cp [33m`[39;49;00m/bin/find . -path [33m"./dist"[39;49;00m -prune -o -name [33m"*.EXE"[39;49;00m | sed [33m"[39;49;00m[33ms/\.EXE[39;49;00m[31m$$[39;49;00m[33m/\.pdb/[39;49;00m[33m"[39;49;00m | xargs[33m`[39;49;00m [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m$
   564	[36mendif # MOZ_DEBUG_SYMBOLS[39;49;00m$
   565	[36mifdef MOZ_PROFILE[39;49;00m$
   566		[36mecho[39;49;00m splitting symbols out of binaries$
   567		/bin/find [34m$([39;49;00mDIST[34m)[39;49;00m -name [33m"*.dll"[39;49;00m -exec splitsym {} [33m\;[39;49;00m$
   568		/bin/find [34m$([39;49;00mDIST[34m)[39;49;00m -name [33m"*.exe"[39;49;00m -exec splitsym {} [33m\;[39;49;00m$
   569		/bin/find [34m$([39;49;00mDIST[34m)[39;49;00m -name [33m"*.EXE"[39;49;00m -exec splitsym {} [33m\;[39;49;00m$
   570		mkdir -p [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m$
   571		/bin/find [34m$([39;49;00mDIST[34m)[39;49;00m -name [33m"*.dbg"[39;49;00m -exec mv {} [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m [33m\;[39;49;00m$
   572	[36mendif # MOZ_PROFILE[39;49;00m$
   573	[36mendif # MOZILLA_OFFICIAL[39;49;00m$
   574	$
   575	[32msignnss[39;49;00m:$
   576	[36mifdef MOZILLA_OFFICIAL[39;49;00m$
   577		[36mecho[39;49;00m signing NSS libs$
   578		[36mcd[39;49;00m [34m$([39;49;00mDIST[34m)[39;49;00m/bin; ./shlibsign.exe -v -i softokn3.dll$
   579		[36mcd[39;49;00m [34m$([39;49;00mDIST[34m)[39;49;00m/bin; ./shlibsign.exe -v -i freebl3.dll$
   580	[36mendif # MOZILLA_OFFICIAL[39;49;00m$
   581	$
   582	[31mBUILDID[39;49;00m = [34m$([39;49;00mshell cat [34m$([39;49;00mDEPTH[34m)[39;49;00m/config/build_number[34m)[39;49;00m$
   583	[32mdeliver[39;49;00m: splitsymbols rebase signnss$
   584	$
   585	[36mendif # WINNT[39;49;00m$
