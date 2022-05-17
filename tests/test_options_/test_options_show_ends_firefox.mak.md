[37m#[39;49;00m$
[37m# ***** BEGIN LICENSE BLOCK *****[39;49;00m$
[37m# Version: MPL 1.1/GPL 2.0/LGPL 2.1[39;49;00m$
[37m#[39;49;00m$
[37m# The contents of this file are subject to the Mozilla Public License Version[39;49;00m$
[37m# 1.1 (the "License"); you may not use this file except in compliance with[39;49;00m$
[37m# the License. You may obtain a copy of the License at[39;49;00m$
[37m# http://www.mozilla.org/MPL/[39;49;00m$
[37m#[39;49;00m$
[37m# Software distributed under the License is distributed on an "AS IS" basis,[39;49;00m$
[37m# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License[39;49;00m$
[37m# for the specific language governing rights and limitations under the[39;49;00m$
[37m# License.[39;49;00m$
[37m#[39;49;00m$
[37m# The Original Code is mozilla.org code.[39;49;00m$
[37m#[39;49;00m$
[37m# The Initial Developer of the Original Code is[39;49;00m$
[37m# Netscape Communications Corporation.[39;49;00m$
[37m# Portions created by the Initial Developer are Copyright (C) 1998[39;49;00m$
[37m# the Initial Developer. All Rights Reserved.[39;49;00m$
[37m#[39;49;00m$
[37m# Contributor(s):[39;49;00m$
[37m#[39;49;00m$
[37m# Alternatively, the contents of this file may be used under the terms of[39;49;00m$
[37m# either the GNU General Public License Version 2 or later (the "GPL"), or[39;49;00m$
[37m# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),[39;49;00m$
[37m# in which case the provisions of the GPL or the LGPL are applicable instead[39;49;00m$
[37m# of those above. If you wish to allow use of your version of this file only[39;49;00m$
[37m# under the terms of either the GPL or the LGPL, and not to allow others to[39;49;00m$
[37m# use your version of this file under the terms of the MPL, indicate your[39;49;00m$
[37m# decision by deleting the provisions above and replace them with the notice[39;49;00m$
[37m# and other provisions required by the GPL or the LGPL. If you do not delete[39;49;00m$
[37m# the provisions above, a recipient may use your version of this file under[39;49;00m$
[37m# the terms of any one of the MPL, the GPL or the LGPL.[39;49;00m$
[37m#[39;49;00m$
[37m# ***** END LICENSE BLOCK *****[39;49;00m$
$
[31mDEPTH[39;49;00m		= .$
[31mtopsrcdir[39;49;00m	= @top_srcdir@$
[31msrcdir[39;49;00m		= @srcdir@$
[31mVPATH[39;49;00m		= @srcdir@$
$
[36minclude $(DEPTH)/config/autoconf.mk[39;49;00m$
$
[36minclude $(topsrcdir)/build/unix/modules.mk[39;49;00m$
$
[36mifeq ($(BUILD_MODULES),all)[39;49;00m$
[37m#[39;49;00m$
[37m# And now for something completely different...[39;49;00m$
[37m# Divide the default build into tiers. [39;49;00m$
[37m# Tiers must be defined on module boundaries [39;49;00m$
[37m#[39;49;00m$
[31mSUPPRESS_DEFAULT_RULES[39;49;00m = [34m1[39;49;00m$
$
[32mdefault alldep all[39;49;00m:: [34m$([39;49;00m[31mSUBMAKEFILES[39;49;00m[34m)[39;49;00m$
	[34m$([39;49;00mRM[34m)[39;49;00m -rf [34m$([39;49;00mDIST[34m)[39;49;00m/sdk$
	[34m$([39;49;00mRM[34m)[39;49;00m -rf [34m$([39;49;00mDIST[34m)[39;49;00m/include$
	[34m$([39;49;00mMAKE[34m)[39;49;00m -C config [36mexport[39;49;00m$
	[34m$([39;49;00mMAKE[34m)[39;49;00m nspr$
	[34m$([39;49;00mMAKE[34m)[39;49;00m ldap$
	[34m$([39;49;00mMAKE[34m)[39;49;00m tier_0$
	[34m$([39;49;00mMAKE[34m)[39;49;00m tier_1$
	[34m$([39;49;00mMAKE[34m)[39;49;00m tier_2$
	[34m$([39;49;00mMAKE[34m)[39;49;00m tier_9$
	[34m$([39;49;00mMAKE[34m)[39;49;00m tier_50$
	[34m$([39;49;00mMAKE[34m)[39;49;00m tier_99$
$
[37m# Make sure that the existing rulesets work[39;49;00m$
[31mDIRS[39;49;00m = [33m\[39;49;00m$
	[34m$([39;49;00mtier_0_dirs[34m)[39;49;00m [33m\[39;49;00m$
	[34m$([39;49;00mtier_1_dirs[34m)[39;49;00m [33m\[39;49;00m$
	[34m$([39;49;00mtier_2_dirs[34m)[39;49;00m [33m\[39;49;00m$
	[34m$([39;49;00mtier_9_dirs[34m)[39;49;00m [33m\[39;49;00m$
	[34m$([39;49;00mtier_50_dirs[34m)[39;49;00m [33m\[39;49;00m$
	[34m$([39;49;00mNULL[34m)[39;49;00m$
$
[36mifdef GC_LEAK_DETECTOR[39;49;00m$
[31mDIRS[39;49;00m += gc/boehm$
[36mendif[39;49;00m$
$
[31mDIRS[39;49;00m	+= [34m$([39;49;00mtier_99_dirs[34m)[39;49;00m$
$
[37m#[39;49;00m$
[37m# tier 0 - base build config dirs[39;49;00m$
[37m# [39;49;00m$
[31mtier_0_dirs[39;49;00m = [33m\[39;49;00m$
	config [33m\[39;49;00m$
	build [33m\[39;49;00m$
	[34m$([39;49;00mNULL[34m)[39;49;00m$
$
[37m#[39;49;00m$
[37m# tier 1 -  3rd party individual libraries[39;49;00m$
[37m#[39;49;00m$
[31mtier_1_dirs[39;49;00m	+= dbm$
$
[36mifndef MOZ_NATIVE_JPEG[39;49;00m$
[31mtier_1_dirs[39;49;00m	+= jpeg$
[36mendif[39;49;00m$
$
[36mifndef MOZ_NATIVE_ZLIB[39;49;00m$
[31mtier_1_dirs[39;49;00m	+= modules/zlib$
[36mendif[39;49;00m$
$
[37m# Installer needs standalone libjar, hence standalone zlib[39;49;00m$
[36mifdef MOZ_INSTALLER[39;49;00m$
[31mtier_1_dirs[39;49;00m	+= modules/zlib/standalone$
[36mendif[39;49;00m$
$
[36mifdef MOZ_UPDATER[39;49;00m$
[31mtier_1_dirs[39;49;00m += modules/libbz2$
[31mtier_1_dirs[39;49;00m += modules/libmar$
[36mendif[39;49;00m$
$
[36mifdef MOZ_SVG_RENDERER_LIBART[39;49;00m$
[31mtier_1_dirs[39;49;00m	+= other-licenses/libart_lgpl$
[36mendif[39;49;00m$
$
[37m#[39;49;00m$
[37m# tier 2 - base libraries[39;49;00m$
[37m# [39;49;00m$
[31mtier_2_dirs[39;49;00m	= [33m\[39;49;00m$
		js [33m\[39;49;00m$
		xpcom [33m\[39;49;00m$
		[34m$([39;49;00mNULL[34m)[39;49;00m$
$
[36mifndef MOZ_NO_XPCOM_OBSOLETE[39;49;00m$
[31mtier_2_dirs[39;49;00m += modules/libreg xpcom/obsolete$
[36mendif[39;49;00m$
$
[36mifdef NS_TRACE_MALLOC[39;49;00m$
[31mtier_2_dirs[39;49;00m	+= tools/trace-malloc/lib$
[36mendif[39;49;00m$
$
[37m#[39;49;00m$
[37m# tier 9 - core components (necko,gecko)[39;49;00m$
[37m#[39;49;00m$
$
[31mtier_9_dirs[39;49;00m += [33m\[39;49;00m$
		js/src/xpconnect [33m\[39;49;00m$
		intl [33m\[39;49;00m$
		db [33m\[39;49;00m$
		[34m$([39;49;00mNULL[34m)[39;49;00m$
$
[36mifdef MOZ_STORAGE[39;49;00m$
[31mtier_9_dirs[39;49;00m += storage$
[36mendif[39;49;00m$
$
[36mifdef MOZ_ENABLE_XLIB[39;49;00m$
[31mtier_9_dirs[39;49;00m	+= gfx/src/xlibrgb widget/src/xlibxtbin$
[36mendif[39;49;00m$
$
[36mifdef MOZ_ENABLE_GTK[39;49;00m$
[31mtier_9_dirs[39;49;00m	+= widget/src/gtksuperwin widget/src/gtkxtbin$
[36mendif[39;49;00m$
$
[36mifdef MOZ_ENABLE_GTK2[39;49;00m$
[31mtier_9_dirs[39;49;00m     += widget/src/gtkxtbin$
[36mendif[39;49;00m$
$
[36mifdef MOZ_IPCD[39;49;00m$
[31mtier_9_dirs[39;49;00m += ipc/ipcd$
[36mendif[39;49;00m$
$
[36mifdef MOZ_JSDEBUGGER[39;49;00m$
[31mtier_9_dirs[39;49;00m += js/jsd$
[36mendif[39;49;00m$
$
[31mtier_9_dirs[39;49;00m	+= [33m\[39;49;00m$
		modules/libutil [33m\[39;49;00m$
		netwerk [33m\[39;49;00m$
		modules/libjar [33m\[39;49;00m$
		uriloader [33m\[39;49;00m$
		modules/libpref [33m\[39;49;00m$
		modules/libimg [33m\[39;49;00m$
		caps [33m\[39;49;00m$
		rdf [33m\[39;49;00m$
		parser/expat [33m\[39;49;00m$
		parser/xml [33m\[39;49;00m$
		parser/htmlparser [33m\[39;49;00m$
		gfx [33m\[39;49;00m$
		modules/libpr0n [33m\[39;49;00m$
		sun-java [33m\[39;49;00m$
		modules/plugin [33m\[39;49;00m$
		dom [33m\[39;49;00m$
		view [33m\[39;49;00m$
		widget [33m\[39;49;00m$
		content [33m\[39;49;00m$
		layout [33m\[39;49;00m$
		xpfe/components/shistory [33m\[39;49;00m$
		docshell [33m\[39;49;00m$
		webshell [33m\[39;49;00m$
		embedding [33m\[39;49;00m$
		editor [33m\[39;49;00m$
		xpfe/appshell [33m\[39;49;00m$
		[34m$([39;49;00mNULL[34m)[39;49;00m$
$
[36mifdef MOZ_OJI[39;49;00m$
[31mtier_9_dirs[39;49;00m	+= [33m\[39;49;00m$
		js/src/liveconnect [33m\[39;49;00m$
		modules/oji [33m\[39;49;00m$
		[34m$([39;49;00mNULL[34m)[39;49;00m$
[36mendif[39;49;00m$
$
[36mifdef ACCESSIBILITY[39;49;00m$
[31mtier_9_dirs[39;49;00m    += accessible$
[36mendif[39;49;00m$
$
[37m# [39;49;00m$
[37m# tier 50 - xpfe & toolkit[39;49;00m$
[37m#[39;49;00m$
$
[36mifdef MOZ_XUL[39;49;00m$
[36mifdef MOZ_XUL_APP[39;49;00m$
[31mtier_50_dirs[39;49;00m += chrome$
[36melse[39;49;00m$
[31mtier_50_dirs[39;49;00m += rdf/chrome$
[36mendif[39;49;00m$
[36melse[39;49;00m$
[31mtier_50_dirs[39;49;00m += embedding/minimo/chromelite$
[36mendif[39;49;00m$
$
[31mtier_50_dirs[39;49;00m += profile$
$
[37m# This must preceed xpfe[39;49;00m$
[36mifdef MOZ_JPROF[39;49;00m$
[31mtier_50_dirs[39;49;00m        += tools/jprof$
[36mendif[39;49;00m$
$
[36mifneq (,$(filter mac cocoa,$(MOZ_WIDGET_TOOLKIT)))[39;49;00m$
[31mtier_50_dirs[39;49;00m	+= xpfe/bootstrap/appleevents$
[36mendif[39;49;00m$
$
[31mtier_50_dirs[39;49;00m	+= [33m\[39;49;00m$
	xpfe [33m\[39;49;00m$
	toolkit/components [33m\[39;49;00m$
	[34m$([39;49;00mNULL[34m)[39;49;00m$
$
[36mifndef MOZ_XUL_APP[39;49;00m$
[31mtier_50_dirs[39;49;00m += themes$
[36mendif[39;49;00m$
$
[36mifdef MOZ_ENABLE_XREMOTE[39;49;00m$
[31mtier_50_dirs[39;49;00m += widget/src/xremoteclient$
[36mendif[39;49;00m$
$
[36mifdef MOZ_XUL_APP[39;49;00m$
[31mtier_50_dirs[39;49;00m	+= toolkit$
[36mendif[39;49;00m$
$
[36mifdef MOZ_PHOENIX[39;49;00m$
[37m#XXXBlake this shell path is a temp hack; toolkit shouldn't depend on browser[39;49;00m$
[31mtier_50_dirs[39;49;00m    += browser/components/shell/public$
[36mendif[39;49;00m$
$
[36mifdef MOZ_XPINSTALL[39;49;00m$
[31mtier_50_dirs[39;49;00m     +=  xpinstall$
[36mendif[39;49;00m$
$
[37m# JavaXPCOM JNI code is compiled into libXUL[39;49;00m$
[36mifdef MOZ_JAVAXPCOM[39;49;00m$
[31mtier_50_dirs[39;49;00m	+= extensions/java/xpcom/src$
[36mendif[39;49;00m$
$
[36mifdef MOZ_ENABLE_LIBXUL[39;49;00m$
[31mtier_50_dirs[39;49;00m += [33m\[39;49;00m$
		toolkit/library [33m\[39;49;00m$
		xpcom/stub [33m\[39;49;00m$
		[34m$([39;49;00mNULL[34m)[39;49;00m$
[36mendif[39;49;00m$
$
[36mifdef NS_TRACE_MALLOC[39;49;00m$
[31mtier_50_dirs[39;49;00m += tools/trace-malloc$
[36mendif[39;49;00m$
$
[36mifdef MOZ_PSM[39;49;00m$
[31mtier_50_dirs[39;49;00m	+= security/manager$
[36melse[39;49;00m$
[31mtier_50_dirs[39;49;00m	+= security/manager/boot/public security/manager/ssl/public$
[36mendif[39;49;00m$
$
[36mifdef MOZ_LDAP_XPCOM[39;49;00m$
[31mtier_50_dirs[39;49;00m	+= directory/xpcom$
[36mendif[39;49;00m$
$
[36mifndef MINIMO[39;49;00m$
[36mifdef MOZ_XUL_APP[39;49;00m$
[36mifdef MOZ_ENABLE_GTK2[39;49;00m$
[31mtier_50_dirs[39;49;00m    += toolkit/components/gnome$
[36mendif[39;49;00m$
[36mendif[39;49;00m$
[36mendif[39;49;00m$
$
[36mifdef MOZ_LEAKY[39;49;00m$
[31mtier_50_dirs[39;49;00m        += tools/leaky$
[36mendif[39;49;00m$
$
[36mifdef MOZ_MAPINFO[39;49;00m$
[31mtier_50_dirs[39;49;00m	+= tools/codesighs$
[36mendif[39;49;00m$
$
[37m#[39;49;00m$
[37m# tier 99 - application features[39;49;00m$
[37m#[39;49;00m$
$
[36mifdef MOZ_MAIL_NEWS[39;49;00m$
[31mtier_99_dirs[39;49;00m	+= mailnews$
[36mendif[39;49;00m$
$
[36mifdef MOZ_CALENDAR[39;49;00m$
[31mtier_99_dirs[39;49;00m	+= calendar$
[36mendif[39;49;00m$
$
[36mifdef MOZ_EXTENSIONS[39;49;00m$
[31mtier_99_dirs[39;49;00m	+= extensions$
[36mendif[39;49;00m$
$
[36mifdef MOZ_JAVAXPCOM[39;49;00m$
[31mtier_99_dirs[39;49;00m	+= extensions/java$
[36mendif[39;49;00m$
$
[37m# axcontrol[39;49;00m$
[36mifeq ($(OS_ARCH),WINNT)[39;49;00m$
[36mifndef MOZ_NO_ACTIVEX_SUPPORT[39;49;00m$
[31mtier_99_dirs[39;49;00m += [33m\[39;49;00m$
		embedding/browser/activex/src/control [33m\[39;49;00m$
		embedding/browser/activex/src/control_kicker [33m\[39;49;00m$
		[34m$([39;49;00mNULL[34m)[39;49;00m$
[36mendif[39;49;00m$
[36mendif[39;49;00m$
$
[37m# Java Embedding Plugin[39;49;00m$
[36mifneq (,$(filter mac cocoa,$(MOZ_WIDGET_TOOLKIT)))[39;49;00m$
[31mtier_99_dirs[39;49;00m += plugin/oji/JEP$
[36mendif[39;49;00m$
$
[36mifneq (,$(filter browser suite,$(MOZ_BUILD_APP)))[39;49;00m$
[31mtier_99_dirs[39;49;00m += xpfe/components/search$
[36mendif[39;49;00m$
$
[36mifdef MOZ_BRANDING_DIRECTORY[39;49;00m$
[31mtier_99_dirs[39;49;00m += [34m$([39;49;00mMOZ_BRANDING_DIRECTORY[34m)[39;49;00m$
[36mendif[39;49;00m$
$
[36mifdef MOZ_PHOENIX[39;49;00m$
[31mtier_99_dirs[39;49;00m	+= browser xpfe/bootstrap/init.d$
[36mendif[39;49;00m$
$
[36mifdef MOZ_XULRUNNER[39;49;00m$
[31mtier_99_dirs[39;49;00m	+= xulrunner$
[36mendif[39;49;00m$
$
[36mifdef MOZ_COMPOSER[39;49;00m$
[31mtier_99_dirs[39;49;00m	+= editor/ui$
[36mendif[39;49;00m$
$
[36mifdef MOZ_THUNDERBIRD[39;49;00m$
[31mtier_99_dirs[39;49;00m	+= mail xpfe/bootstrap/init.d$
[36mendif[39;49;00m$
$
[36mifdef MOZ_STANDALONE_COMPOSER[39;49;00m$
[31mtier_99_dirs[39;49;00m	+= composer$
[36mendif[39;49;00m$
$
[36mifdef MOZ_SUNBIRD[39;49;00m$
[31mtier_99_dirs[39;49;00m	+= calendar/sunbird$
[36mendif[39;49;00m$
$
[36mifdef MOZ_SUITE[39;49;00m$
[31mtier_99_dirs[39;49;00m	+= suite$
[36mendif[39;49;00m$
$
[36mifdef MINIMO[39;49;00m$
[31mtier_99_dirs[39;49;00m	+= minimo$
[36mendif[39;49;00m$
$
[36mifdef MOZ_XUL_APP[39;49;00m$
[36mifdef MOZ_INSTALLER[39;49;00m$
[31mtier_99_dirs[39;49;00m     +=  toolkit/mozapps/installer$
[36mendif[39;49;00m$
[36melse[39;49;00m$
[36mifneq (,$(MOZ_XPFE_COMPONENTS)$(MOZ_XUL))[39;49;00m$
[36mifndef MINIMO[39;49;00m$
[31mtier_99_dirs[39;49;00m	+= xpfe/bootstrap$
[36mendif[39;49;00m$
[36mendif[39;49;00m$
[36mendif[39;49;00m$
$
[36mifneq (,$(MOZ_ENABLE_GTK)$(MOZ_ENABLE_GTK2))[39;49;00m$
[31mtier_99_dirs[39;49;00m	+= embedding/browser/gtk$
[36mendif[39;49;00m$
$
[37m# viewer[39;49;00m$
[36mifneq (,$(ENABLE_TESTS))[39;49;00m$
[36mifndef MOZ_ENABLE_LIBXUL[39;49;00m$
[31mtier_99_dirs[39;49;00m += webshell/tests$
[36mendif[39;49;00m$
[36mendif[39;49;00m$
$
[37m# winembed, mfcembed[39;49;00m$
[36mifeq ($(OS_ARCH),WINNT)[39;49;00m$
[36mifneq (,$(ENABLE_TESTS)$(MOZILLA_OFFICIAL))[39;49;00m$
[31mtier_99_dirs[39;49;00m += embedding/tests$
[36mendif[39;49;00m$
[36mendif[39;49;00m$
$
[37m# os2embed[39;49;00m$
[36mifeq ($(OS_ARCH),OS2)[39;49;00m$
[36mifneq (,$(ENABLE_TESTS)$(MOZILLA_OFFICIAL))[39;49;00m$
[31mtier_99_dirs[39;49;00m += embedding/tests$
[36mendif[39;49;00m$
[36mendif[39;49;00m$
$
[36mifeq ($(MOZ_BUILD_APP),macbrowser)[39;49;00m$
[31mtier_99_dirs[39;49;00m += [33m\[39;49;00m$
	embedding/config [33m\[39;49;00m$
	camino [33m\[39;49;00m$
	[34m$([39;49;00mNULL[34m)[39;49;00m$
[36mendif[39;49;00m$
$
[37m# test harnesses [39;49;00m$
[36mifdef ENABLE_TESTS[39;49;00m$
[31mtier_99_dirs[39;49;00m += tools/test-harness$
[36mendif[39;49;00m$
$
[36melse[39;49;00m$
$
[37m# Standalone build[39;49;00m$
$
[31mDIRS[39;49;00m		= [34m$([39;49;00mBUILD_MODULE_DIRS[34m)[39;49;00m$
$
[37m# Hack to generate xpidl Makefile[39;49;00m$
[36mifneq ($(BUILD_MODULES),all)[39;49;00m$
[36mifneq (,$(findstring xpcom, $(BUILD_MODULE_DIRS)))[39;49;00m$
[31mDIRS[39;49;00m		:= xpcom/typelib [34m$([39;49;00mDIRS[34m)[39;49;00m$
[31mSUBMAKEFILES[39;49;00m	:= xpcom/typelib/Makefile$
[36mendif[39;49;00m$
[36mendif[39;49;00m$
$
[32mdefault[39;49;00m:: [34m$([39;49;00m[31mSUBMAKEFILES[39;49;00m[34m)[39;49;00m$
	[34m$([39;49;00mMAKE[34m)[39;49;00m [36mexport[39;49;00m$
	[34m$([39;49;00mMAKE[34m)[39;49;00m libs$
$
[36mendif # BUILD_MODULES == all[39;49;00m$
$
[31mSTATIC_MAKEFILES[39;49;00m := nsprpub directory/c-sdk security/nss$
$
[31mGARBAGE_DIRS[39;49;00m += dist$
[31mDIST_GARBAGE[39;49;00m = config.cache config.log config.status config-defs.h [33m\[39;49;00m$
   dependencies.beos config/autoconf.mk config/myrules.mk config/myconfig.mk [33m\[39;49;00m$
   unallmakefiles mozilla-config.h [33m\[39;49;00m$
   [34m$([39;49;00mtopsrcdir[34m)[39;49;00m/.mozconfig.mk [34m$([39;49;00mtopsrcdir[34m)[39;49;00m/.mozconfig.out $
$
[37m# Build pseudo-external modules first when export is explicitly called[39;49;00m$
[32mexport[39;49;00m::$
	[34m$([39;49;00mRM[34m)[39;49;00m -rf [34m$([39;49;00mDIST[34m)[39;49;00m/sdk$
	[34m$([39;49;00mMAKE[34m)[39;49;00m -C config [36mexport[39;49;00m$
	[34m$([39;49;00mMAKE[34m)[39;49;00m nspr$
	[34m$([39;49;00mMAKE[34m)[39;49;00m ldap$
[36mifneq ($(BUILD_MODULES),all)[39;49;00m$
[36mifneq (,$(findstring xpcom, $(BUILD_MODULE_DIRS)))[39;49;00m$
	[34m$([39;49;00mMAKE[34m)[39;49;00m -C xpcom/typelib$
	[34m$([39;49;00mMAKE[34m)[39;49;00m export-idl$
[36mendif[39;49;00m$
[36mendif[39;49;00m$
$
[32minstall[39;49;00m::$
[36mifndef MOZ_NATIVE_NSPR[39;49;00m$
	[34m$([39;49;00mMAKE[34m)[39;49;00m -C nsprpub real_install [31mDESTDIR[39;49;00m=[34m$([39;49;00mDESTDIR[34m)[39;49;00m [31mlibdir[39;49;00m=[34m$([39;49;00mmozappdir[34m)[39;49;00m [31mincludedir[39;49;00m=[34m$([39;49;00mincludedir[34m)[39;49;00m/nspr$
	[34m$([39;49;00mRM[34m)[39;49;00m -f [34m$([39;49;00maddprefix [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mmozappdir[34m)[39;49;00m/[34m$([39;49;00mLIB_PREFIX[34m)[39;49;00m, [34m$([39;49;00maddsuffix .[34m$([39;49;00mLIB_SUFFIX[34m)[39;49;00m, nspr4 plds4 plc4[34m)[39;49;00m[34m)[39;49;00m$
	[34m$([39;49;00mRM[34m)[39;49;00m -f [34m$([39;49;00maddprefix [34m$([39;49;00mDESTDIR[34m)[39;49;00m[34m$([39;49;00mbindir[34m)[39;49;00m/,nspr-config compile-et.pl prerr.properties[34m)[39;49;00m$
[36mendif[39;49;00m$
[36mifdef MOZ_LDAP_XPCOM[39;49;00m$
	[34m$([39;49;00mMAKE[34m)[39;49;00m -C directory/c-sdk real_install [31mDESTDIR[39;49;00m=[34m$([39;49;00mDESTDIR[34m)[39;49;00m [31mlibdir[39;49;00m=[34m$([39;49;00mmozappdir[34m)[39;49;00m [31mincludedir[39;49;00m=[34m$([39;49;00mincludedir[34m)[39;49;00m/ldap$
[36mendif[39;49;00m$
$
[36minclude $(topsrcdir)/config/rules.mk[39;49;00m$
$
[37m# Clean up after pseudo-external modules[39;49;00m$
[32mclean clobber realclean clobber_all distclean[39;49;00m::$
[36mifndef MOZ_NATIVE_NSPR[39;49;00m$
	[34m$([39;49;00mMAKE[34m)[39;49;00m -C nsprpub [31m$@[39;49;00m$
[36mendif[39;49;00m$
[36mifdef MOZ_LDAP_XPCOM[39;49;00m$
	[34m$([39;49;00mMAKE[34m)[39;49;00m -C directory/c-sdk [31m$@[39;49;00m$
[36mendif[39;49;00m$
$
[37m# Map mozilla targets to standard automake target[39;49;00m$
[36mifdef MOZ_ENABLE_LIBXUL[39;49;00m$
[32mtier_50[39;49;00m: [34m$([39;49;00m[31maddsuffix[39;49;00m /[31mMakefile[39;49;00m, [34m$[39;49;00m[34m([39;49;00m[31mfilter-out[39;49;00m [34m$[39;49;00m[34m([39;49;00m[31mSTATIC_MAKEFILES[39;49;00m[34m)[39;49;00m, [34m$[39;49;00m[34m([39;49;00m[34m$[39;49;00m@[31m_dirs[39;49;00m[34m)[39;49;00m[34m)[39;49;00m[34m)[39;49;00m$
	@echo [33m"[39;49;00m[33mtier_50: [39;49;00m[34m$([39;49;00mtier_50_dirs[34m)[39;49;00m[33m"[39;49;00m$
	@[34m$([39;49;00mEXIT_ON_ERROR[34m)[39;49;00m [33m\[39;49;00m$
	[34mfor[39;49;00m d [34min[39;49;00m [34m$([39;49;00mtier_50_dirs[34m)[39;49;00m; [34mdo[39;49;00m [33m\[39;49;00m$
	    [34m$([39;49;00mUPDATE_TITLE[34m)[39;49;00m [33m\[39;49;00m$
[36m	    if test ! -f $$d/Makefile; then \[39;49;00m$
[36m	      $(PERL) $(AUTOCONF_TOOLS)/make-makefile -t $(topsrcdir) -d $(DEPTH) $(CYGWIN_TOPSRCDIR) $$d/Makefile; \[39;49;00m$
[36m	    fi; \[39;49;00m$
[36m	    $(MAKE) -C $$d export; \[39;49;00m$
[36m	done ; \[39;49;00m$
[36m	for d in $(tier_50_dirs); do \[39;49;00m$
[36m	    $(UPDATE_TITLE) \[39;49;00m$
[36m	    $(MAKE) -C $$d libs; \[39;49;00m$
[36m	done[39;49;00m$
	@echo [33m"Building tools from tier 2/9/50"[39;49;00m$
	@[34m$([39;49;00mEXIT_ON_ERROR[34m)[39;49;00m [33m\[39;49;00m$
	[34mfor[39;49;00m d [34min[39;49;00m [34m$([39;49;00mtier_2_dirs[34m)[39;49;00m [34m$([39;49;00mtier_9_dirs[34m)[39;49;00m [34m$([39;49;00mtier_50_dirs[34m)[39;49;00m; [34mdo[39;49;00m [33m\[39;49;00m$
	    [34m$([39;49;00mUPDATE_TITLE[34m)[39;49;00m [33m\[39;49;00m$
	    [34m$([39;49;00mMAKE[34m)[39;49;00m -C [31m$$[39;49;00md tools; [33m\[39;49;00m$
	[34mdone[39;49;00m;$
[36mendif[39;49;00m$
$
[32mtier_%[39;49;00m:$
	@echo [33m"[39;49;00m[31m$@[39;49;00m[33m: [39;49;00m[34m$([39;49;00m[31m$@[39;49;00m_dirs[34m)[39;49;00m[33m"[39;49;00m$
	@[34m$([39;49;00mEXIT_ON_ERROR[34m)[39;49;00m [33m\[39;49;00m$
	  [34mfor[39;49;00m d [34min[39;49;00m [34m$([39;49;00m[31m$@[39;49;00m_dirs[34m)[39;49;00m; [34mdo[39;49;00m [33m\[39;49;00m$
	    [34m$([39;49;00mUPDATE_TITLE[34m)[39;49;00m [33m\[39;49;00m$
[36m	    if test ! -f $$d/Makefile; then \[39;49;00m$
[36m	      $(PERL) $(AUTOCONF_TOOLS)/make-makefile -t $(topsrcdir) -d $(DEPTH) $(CYGWIN_TOPSRCDIR) $$d/Makefile; \[39;49;00m$
[36m	    fi; \[39;49;00m$
[36m	    $(MAKE) -C $$d export; \[39;49;00m$
[36m	  done ; \[39;49;00m$
[36m	  for d in $($@_dirs); do $(UPDATE_TITLE) \[39;49;00m$
[36m	    $(MAKE) -C $$d libs; \[39;49;00m$
[36m	  done[39;49;00m$
$
[37m#[39;49;00m$
[37m# Individual modules[39;49;00m$
[37m#[39;49;00m$
[32mboehm[39;49;00m:$
[36mifdef GC_LEAK_DETECTOR[39;49;00m$
	[34m$([39;49;00mMAKE[34m)[39;49;00m -C gc/boehm$
[36mendif[39;49;00m$
$
[32mnspr[39;49;00m: boehm$
[36mifndef MOZ_NATIVE_NSPR[39;49;00m$
	[34m$([39;49;00mMAKE[34m)[39;49;00m -C nsprpub$
[36mendif[39;49;00m$
$
[32mldap[39;49;00m:$
[36mifdef MOZ_LDAP_XPCOM[39;49;00m$
	[34m$([39;49;00mMAKE[34m)[39;49;00m -C directory/c-sdk$
[36mendif[39;49;00m$
$
[32mdistclean[39;49;00m::$
	cat unallmakefiles | [34m$([39;49;00mXARGS[34m)[39;49;00m rm -f$
	rm -f unallmakefiles [34m$([39;49;00mDIST_GARBAGE[34m)[39;49;00m$
$
[36mifeq ($(OS_ARCH),WINNT)[39;49;00m$
[32mrebase[39;49;00m:$
[36mifdef MOZILLA_OFFICIAL[39;49;00m$
	[36mecho[39;49;00m rebasing [34m$([39;49;00mDIST[34m)[39;49;00m$
	/bin/find [34m$([39;49;00mDIST[34m)[39;49;00m -name [33m"*.dll"[39;49;00m > rebase.lst$
	rebase -b [34m60000000[39;49;00m -R . -G rebase.lst$
	rm rebase.lst$
[36mendif[39;49;00m$
$
[32msplitsymbols[39;49;00m:$
[36mifdef MOZILLA_OFFICIAL[39;49;00m$
[36mifdef MOZ_DEBUG_SYMBOLS[39;49;00m$
	[36mecho[39;49;00m finding pdb files$
	mkdir -p [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m$
	-cp [33m`[39;49;00m/bin/find . -path [33m"./dist"[39;49;00m -prune -o -name [33m"*.dll"[39;49;00m | sed [33m"[39;49;00m[33ms/\.dll[39;49;00m[31m$$[39;49;00m[33m/\.pdb/[39;49;00m[33m"[39;49;00m | xargs[33m`[39;49;00m [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m$
	-cp [33m`[39;49;00m/bin/find . -path [33m"./dist"[39;49;00m -prune -o -name [33m"*.exe"[39;49;00m | sed [33m"[39;49;00m[33ms/\.exe[39;49;00m[31m$$[39;49;00m[33m/\.pdb/[39;49;00m[33m"[39;49;00m | xargs[33m`[39;49;00m [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m$
	-cp [33m`[39;49;00m/bin/find . -path [33m"./dist"[39;49;00m -prune -o -name [33m"*.EXE"[39;49;00m | sed [33m"[39;49;00m[33ms/\.EXE[39;49;00m[31m$$[39;49;00m[33m/\.pdb/[39;49;00m[33m"[39;49;00m | xargs[33m`[39;49;00m [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m$
[36mendif # MOZ_DEBUG_SYMBOLS[39;49;00m$
[36mifdef MOZ_PROFILE[39;49;00m$
	[36mecho[39;49;00m splitting symbols out of binaries$
	/bin/find [34m$([39;49;00mDIST[34m)[39;49;00m -name [33m"*.dll"[39;49;00m -exec splitsym {} [33m\;[39;49;00m$
	/bin/find [34m$([39;49;00mDIST[34m)[39;49;00m -name [33m"*.exe"[39;49;00m -exec splitsym {} [33m\;[39;49;00m$
	/bin/find [34m$([39;49;00mDIST[34m)[39;49;00m -name [33m"*.EXE"[39;49;00m -exec splitsym {} [33m\;[39;49;00m$
	mkdir -p [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m$
	/bin/find [34m$([39;49;00mDIST[34m)[39;49;00m -name [33m"*.dbg"[39;49;00m -exec mv {} [34m$([39;49;00mDIST[34m)[39;49;00m/[34m$([39;49;00mBUILDID[34m)[39;49;00m [33m\;[39;49;00m$
[36mendif # MOZ_PROFILE[39;49;00m$
[36mendif # MOZILLA_OFFICIAL[39;49;00m$
$
[32msignnss[39;49;00m:$
[36mifdef MOZILLA_OFFICIAL[39;49;00m$
	[36mecho[39;49;00m signing NSS libs$
	[36mcd[39;49;00m [34m$([39;49;00mDIST[34m)[39;49;00m/bin; ./shlibsign.exe -v -i softokn3.dll$
	[36mcd[39;49;00m [34m$([39;49;00mDIST[34m)[39;49;00m/bin; ./shlibsign.exe -v -i freebl3.dll$
[36mendif # MOZILLA_OFFICIAL[39;49;00m$
$
[31mBUILDID[39;49;00m = [34m$([39;49;00mshell cat [34m$([39;49;00mDEPTH[34m)[39;49;00m/config/build_number[34m)[39;49;00m$
[32mdeliver[39;49;00m: splitsymbols rebase signnss$
$
[36mendif # WINNT[39;49;00m$
