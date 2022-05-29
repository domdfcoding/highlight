Using lexer <pygments.lexers.JavaLexer with {'ensurenl': False, 'tabsize': 0}>
[37m/*[39;49;00m
[37m * Created on 13-Mar-2004[39;49;00m
[37m * Created by James Yeh[39;49;00m
[37m * Copyright (C) 2004, 2005, 2006 Aelitis, All Rights Reserved.[39;49;00m
[37m *[39;49;00m
[37m * This program is free software; you can redistribute it and/or[39;49;00m
[37m * modify it under the terms of the GNU General Public License[39;49;00m
[37m * as published by the Free Software Foundation; either version 2[39;49;00m
[37m * of the License, or (at your option) any later version.[39;49;00m
[37m * This program is distributed in the hope that it will be useful,[39;49;00m
[37m * but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m
[37m * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the[39;49;00m
[37m * GNU General Public License for more details.[39;49;00m
[37m * You should have received a copy of the GNU General Public License[39;49;00m
[37m * along with this program; if not, write to the Free Software[39;49;00m
[37m * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.[39;49;00m
[37m * [39;49;00m
[37m * AELITIS, SAS au capital de 46,603.30 euros[39;49;00m
[37m * 8 Allee Lenotre, La Grille Royale, 78600 Le Mesnil le Roi, France.[39;49;00m
[37m *[39;49;00m
[37m */[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[34mpackage[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.platform.macosx[39;49;00m;[37m[39;49;00m
[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.core3.logging.*[39;49;00m;[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.core3.util.AEMonitor[39;49;00m;[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.core3.util.Debug[39;49;00m;[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.core3.util.SystemProperties[39;49;00m;[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.platform.PlatformManager[39;49;00m;[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.platform.PlatformManagerCapabilities[39;49;00m;[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.platform.PlatformManagerListener[39;49;00m;[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.platform.macosx.access.jnilib.OSXAccess[39;49;00m;[37m[39;49;00m
[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.plugins.platform.PlatformManagerException[39;49;00m;[37m[39;49;00m
[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.io.BufferedReader[39;49;00m;[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.io.File[39;49;00m;[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.io.IOException[39;49;00m;[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.io.InputStreamReader[39;49;00m;[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.text.MessageFormat[39;49;00m;[37m[39;49;00m
[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.util.HashSet[39;49;00m;[37m[39;49;00m
[37m[39;49;00m
[37m[39;49;00m
[37m/**[39;49;00m
[37m * Performs platform-specific operations with Mac OS X[39;49;00m
[37m *[39;49;00m
[37m * @author James Yeh[39;49;00m
[37m * @version 1.0 Initial Version[39;49;00m
[37m * @see PlatformManager[39;49;00m
[37m */[39;49;00m[37m[39;49;00m
[34mpublic[39;49;00m[37m [39;49;00m[34mclass[39;49;00m [04m[32mPlatformManagerImpl[39;49;00m[37m [39;49;00m[34mimplements[39;49;00m[37m [39;49;00mPlatformManager[37m[39;49;00m
{[37m[39;49;00m
[37m    [39;49;00m[34mprivate[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[34mfinal[39;49;00m[37m [39;49;00mLogIDs[37m [39;49;00mLOGID[37m [39;49;00m=[37m [39;49;00mLogIDs.[36mCORE[39;49;00m;[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mPlatformManagerImpl[37m [39;49;00msingleton;[37m[39;49;00m
[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mAEMonitor[37m [39;49;00mclass_mon[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mAEMonitor([33m"[39;49;00m[33mPlatformManager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mprivate[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[34mfinal[39;49;00m[37m [39;49;00mString[37m [39;49;00mUSERDATA_PATH[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mFile(System.[36mgetProperty[39;49;00m([33m"[39;49;00m[33muser.home[39;49;00m[33m"[39;49;00m)[37m [39;49;00m+[37m [39;49;00m[33m"[39;49;00m[33m/Library/Application Support/[39;49;00m[33m"[39;49;00m).[36mgetPath[39;49;00m();[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m//T: PlatformManagerCapabilities[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mprivate[39;49;00m[37m [39;49;00m[34mfinal[39;49;00m[37m [39;49;00mHashSet[37m [39;49;00mcapabilitySet[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mHashSet();[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * Gets the platform manager singleton, which was already initialized[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mPlatformManagerImpl[37m [39;49;00m[32mgetSingleton[39;49;00m()[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00msingleton;[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * Tries to enable cocoa-java access and instantiates the singleton[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mstatic[39;49;00m[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00minitializeSingleton();[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * Instantiates the singleton[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mprivate[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32minitializeSingleton[39;49;00m()[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mclass_mon.[36menter[39;49;00m();[37m[39;49;00m
[37m            [39;49;00msingleton[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerImpl();[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(Throwable[37m [39;49;00me)[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m        	[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00m[33m"[39;49;00m[33mFailed to initialize platform manager[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m					[39;49;00m+[37m [39;49;00m[33m"[39;49;00m[33m for Mac OS X[39;49;00m[33m"[39;49;00m,[37m [39;49;00me));[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m        [39;49;00m[34mfinally[39;49;00m[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mclass_mon.[36mexit[39;49;00m();[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * Creates a new PlatformManager and initializes its capabilities[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[32mPlatformManagerImpl[39;49;00m()[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mRecoverableFileDelete[39;49;00m);[37m[39;49;00m
[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mShowFileInBrowser[39;49;00m);[37m[39;49;00m
[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mShowPathInCommandLine[39;49;00m);[37m[39;49;00m
[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mCreateCommandLineProcess[39;49;00m);[37m[39;49;00m
[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mGetUserDataDirectory[39;49;00m);[37m[39;49;00m
[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mUseNativeScripting[39;49;00m);[37m[39;49;00m
[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mPlaySystemAlert[39;49;00m);[37m[39;49;00m
[37m        [39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(OSXAccess.[36misLoaded[39;49;00m())[37m [39;49;00m{[37m[39;49;00m
[37m	        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mGetVersion[39;49;00m);[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * {@inheritDoc}[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mgetPlatformType[39;49;00m()[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mPT_MACOSX;[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * {@inheritDoc}[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mgetVersion[39;49;00m()[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m    	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!OSXAccess.[36misLoaded[39;49;00m())[37m [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m    	[39;49;00m}[37m[39;49;00m
[37m    	[39;49;00m[37m[39;49;00m
[37m    	[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mOSXAccess.[36mgetVersion[39;49;00m();[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * {@inheritDoc}[39;49;00m
[37m     * @see org.gudy.azureus2.core3.util.SystemProperties#getUserPath()[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mgetUserDataDirectory[39;49;00m()[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mUSERDATA_PATH;[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m	[39;49;00m[34mpublic[39;49;00m[37m [39;49;00mFile[37m[39;49;00m
[37m	[39;49;00m[32mgetLocation[39;49;00m([37m[39;49;00m
[37m		[39;49;00m[36mlong[39;49;00m[37m	[39;49;00mlocation_id[37m [39;49;00m)[37m[39;49;00m
[37m	[39;49;00m[37m[39;49;00m
[37m		[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
[37m	[39;49;00m{[37m[39;49;00m
[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00mlocation_id[37m [39;49;00m==[37m [39;49;00mLOC_USER_DATA[37m [39;49;00m){[37m[39;49;00m
[37m			[39;49;00m[37m[39;49;00m
[37m			[39;49;00m[34mreturn[39;49;00m([37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mFile([37m [39;49;00mUSERDATA_PATH[37m [39;49;00m));[37m[39;49;00m
[37m		[39;49;00m}[37m[39;49;00m
[37m		[39;49;00m[37m[39;49;00m
[37m		[39;49;00m[34mreturn[39;49;00m([37m [39;49;00m[34mnull[39;49;00m[37m [39;49;00m);[37m[39;49;00m
[37m	[39;49;00m}[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * Not implemented; returns True[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m [39;49;00m[32misApplicationRegistered[39;49;00m()[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mtrue[39;49;00m;[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m[39;49;00m
[37m	[39;49;00m[34mpublic[39;49;00m[37m [39;49;00mString[37m[39;49;00m
[37m	[39;49;00m[32mgetApplicationCommandLine[39;49;00m()[37m[39;49;00m
[37m		[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
[37m	[39;49;00m{[37m[39;49;00m
[37m		[39;49;00m[34mtry[39;49;00m{[37m	    [39;49;00m[37m[39;49;00m
[37m			[39;49;00mString[37m	[39;49;00mbundle_path[37m [39;49;00m=[37m [39;49;00mSystem.[36mgetProperty[39;49;00m([33m"[39;49;00m[33muser.dir[39;49;00m[33m"[39;49;00m)[37m [39;49;00m+SystemProperties.[36mSEP[39;49;00m+[37m [39;49;00mSystemProperties.[36mgetApplicationName[39;49;00m()[37m [39;49;00m+[37m [39;49;00m[33m"[39;49;00m[33m.app[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
[37m[39;49;00m
[37m			[39;49;00mFile[37m [39;49;00mosx_app_bundle[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mFile([37m [39;49;00mbundle_path[37m [39;49;00m).[36mgetAbsoluteFile[39;49;00m();[37m[39;49;00m
[37m			[39;49;00m[37m[39;49;00m
[37m			[39;49;00m[34mif[39;49;00m([37m [39;49;00m!osx_app_bundle.[36mexists[39;49;00m()[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m
[37m				[39;49;00mString[37m [39;49;00mmsg[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mOSX app bundle not found: [[39;49;00m[33m"[39;49;00m[37m [39;49;00m+osx_app_bundle.[36mtoString[39;49;00m()+[37m [39;49;00m[33m"[39;49;00m[33m][39;49;00m[33m"[39;49;00m;[37m[39;49;00m
[37m				[39;49;00mSystem.[36mout[39;49;00m.[36mprintln[39;49;00m([37m [39;49;00mmsg[37m [39;49;00m);[37m[39;49;00m
[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Logger.[36misEnabled[39;49;00m())[37m[39;49;00m
[37m					[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00mmsg));[37m		[39;49;00m[37m[39;49;00m
[37m				[39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([37m [39;49;00mmsg[37m [39;49;00m);[37m[39;49;00m
[37m			[39;49;00m}[37m[39;49;00m
[37m			[39;49;00m[37m[39;49;00m
[37m			[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mopen -a [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m [39;49;00m+osx_app_bundle.[36mtoString[39;49;00m()+[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
[37m			[39;49;00m[37m//return osx_app_bundle.toString() +"/Contents/MacOS/JavaApplicationStub";[39;49;00m[37m[39;49;00m
[37m			[39;49;00m[37m[39;49;00m
[37m		[39;49;00m}[37m[39;49;00m
[37m		[39;49;00m[34mcatch[39;49;00m([37m [39;49;00mThrowable[37m [39;49;00mt[37m [39;49;00m){[37m	[39;49;00m[37m[39;49;00m
[37m			[39;49;00mt.[36mprintStackTrace[39;49;00m();[37m[39;49;00m
[37m			[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mnull[39;49;00m;[37m[39;49;00m
[37m		[39;49;00m}[37m[39;49;00m
[37m	[39;49;00m}[37m[39;49;00m
[37m	[39;49;00m[37m[39;49;00m
[37m	[39;49;00m[37m[39;49;00m
[37m	[39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m[39;49;00m
[37m	[39;49;00m[32misAdditionalFileTypeRegistered[39;49;00m([37m[39;49;00m
[37m		[39;49;00mString[37m		[39;49;00mname,[37m				[39;49;00m[37m// e.g. "BitTorrent"[39;49;00m[37m[39;49;00m
[37m		[39;49;00mString[37m		[39;49;00mtype[37m [39;49;00m)[37m				[39;49;00m[37m// e.g. ".torrent"[39;49;00m[37m[39;49;00m
[37m	[39;49;00m[37m[39;49;00m
[37m		[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
[37m	[39;49;00m{[37m[39;49;00m
[37m	    [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m	[39;49;00m}[37m[39;49;00m
[37m	[39;49;00m[37m[39;49;00m
[37m	[39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m
[37m	[39;49;00m[32munregisterAdditionalFileType[39;49;00m([37m[39;49;00m
[37m		[39;49;00mString[37m		[39;49;00mname,[37m				[39;49;00m[37m// e.g. "BitTorrent"[39;49;00m[37m[39;49;00m
[37m		[39;49;00mString[37m		[39;49;00mtype[37m [39;49;00m)[37m				[39;49;00m[37m// e.g. ".torrent"[39;49;00m[37m[39;49;00m
[37m		[39;49;00m[37m[39;49;00m
[37m		[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
[37m	[39;49;00m{[37m[39;49;00m
[37m		[39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m	[39;49;00m}[37m[39;49;00m
[37m	[39;49;00m[37m[39;49;00m
[37m	[39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m
[37m	[39;49;00m[32mregisterAdditionalFileType[39;49;00m([37m[39;49;00m
[37m		[39;49;00mString[37m		[39;49;00mname,[37m				[39;49;00m[37m// e.g. "BitTorrent"[39;49;00m[37m[39;49;00m
[37m		[39;49;00mString[37m		[39;49;00mdescription,[37m		[39;49;00m[37m// e.g. "BitTorrent File"[39;49;00m[37m[39;49;00m
[37m		[39;49;00mString[37m		[39;49;00mtype,[37m				[39;49;00m[37m// e.g. ".torrent"[39;49;00m[37m[39;49;00m
[37m		[39;49;00mString[37m		[39;49;00mcontent_type[37m [39;49;00m)[37m		[39;49;00m[37m// e.g. "application/x-bittorrent"[39;49;00m[37m[39;49;00m
[37m	[39;49;00m[37m[39;49;00m
[37m		[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
[37m	[39;49;00m{[37m[39;49;00m
[37m	   [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m	[39;49;00m}[37m[39;49;00m
[37m	[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * Not implemented; does nothing[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mregisterApplication[39;49;00m()[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[37m// handled by LaunchServices and/0r user interaction[39;49;00m[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * {@inheritDoc}[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mcreateProcess[39;49;00m(String[37m [39;49;00mcmd,[37m [39;49;00m[36mboolean[39;49;00m[37m [39;49;00minheritsHandles)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mperformRuntimeExec(cmd.[36msplit[39;49;00m([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m));[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(Throwable[37m [39;49;00me)[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mFailed to create process[39;49;00m[33m"[39;49;00m,[37m [39;49;00me);[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * {@inheritDoc}[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mperformRecoverableFileDelete[39;49;00m(String[37m [39;49;00mpath)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00mFile[37m [39;49;00mfile[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mFile(path);[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m(!file.[36mexists[39;49;00m())[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m	        	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Logger.[36misEnabled[39;49;00m())[37m[39;49;00m
[37m							[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00mLogEvent.[36mLT_WARNING[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33mCannot find [39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m									[39;49;00m+[37m [39;49;00mfile.[36mgetName[39;49;00m()));[37m[39;49;00m
[37m            [39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[36mboolean[39;49;00m[37m [39;49;00museOSA[37m [39;49;00m=[37m [39;49;00m!NativeInvocationBridge.[36msharedInstance[39;49;00m().[36misEnabled[39;49;00m()[37m [39;49;00m||[37m [39;49;00m!NativeInvocationBridge.[36msharedInstance[39;49;00m().[36mperformRecoverableFileDelete[39;49;00m(file);[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m(useOSA)[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
[37m            [39;49;00m{[37m[39;49;00m
[37m                [39;49;00mStringBuffer[37m [39;49;00msb[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mStringBuffer();[37m[39;49;00m
[37m                [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33mtell application [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m                [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33mFinder[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m                [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m to move (posix file [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m                [39;49;00msb.[36mappend[39;49;00m(path);[37m[39;49;00m
[37m                [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m as alias) to the trash[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m                [39;49;00mperformOSAScript(sb);[37m[39;49;00m
[37m            [39;49;00m}[37m[39;49;00m
[37m            [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(Throwable[37m [39;49;00me)[37m[39;49;00m
[37m            [39;49;00m{[37m[39;49;00m
[37m                [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mFailed to move file[39;49;00m[33m"[39;49;00m,[37m [39;49;00me);[37m[39;49;00m
[37m            [39;49;00m}[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * {@inheritDoc}[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m [39;49;00m[32mhasCapability[39;49;00m(PlatformManagerCapabilities[37m [39;49;00mcapability)[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mcapabilitySet.[36mcontains[39;49;00m(capability);[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * {@inheritDoc}[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mdispose[39;49;00m()[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00mNativeInvocationBridge.[36msharedInstance[39;49;00m().[36mdispose[39;49;00m();[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * {@inheritDoc}[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetTCPTOSEnabled[39;49;00m([36mboolean[39;49;00m[37m [39;49;00menabled)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m	[39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[32mcopyFilePermissions[39;49;00m([37m[39;49;00m
[37m		[39;49;00mString[37m	[39;49;00mfrom_file_name,[37m[39;49;00m
[37m		[39;49;00mString[37m	[39;49;00mto_file_name[37m [39;49;00m)[37m[39;49;00m
[37m	[39;49;00m[37m[39;49;00m
[37m		[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
[37m	[39;49;00m{[37m[39;49;00m
[37m	    [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m		[39;49;00m[37m[39;49;00m
[37m	[39;49;00m}[37m[39;49;00m
[37m	[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * {@inheritDoc}[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mshowFile[39;49;00m(String[37m [39;49;00mpath)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00mFile[37m [39;49;00mfile[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mFile(path);[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m(!file.[36mexists[39;49;00m())[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m        	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Logger.[36misEnabled[39;49;00m())[37m[39;49;00m
[37m        		[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00mLogEvent.[36mLT_WARNING[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33mCannot find [39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m        				[39;49;00m+[37m [39;49;00mfile.[36mgetName[39;49;00m()));[37m[39;49;00m
[37m            [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mFile not found[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mshowInFinder(file);[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m// Public utility methods not shared across the interface[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * Plays the system alert (the jingle is specified by the user in System Preferences)[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mplaySystemAlert[39;49;00m()[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mperformRuntimeExec([34mnew[39;49;00m[37m [39;49;00mString[]{[33m"[39;49;00m[33mbeep[39;49;00m[33m"[39;49;00m});[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m        	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Logger.[36misEnabled[39;49;00m())[37m[39;49;00m
[37m        		[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00mLogEvent.[36mLT_WARNING[39;49;00m,[37m[39;49;00m
[37m						[39;49;00m[33m"[39;49;00m[33mCannot play system alert[39;49;00m[33m"[39;49;00m));[37m[39;49;00m
[37m        	[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m,[37m [39;49;00me));[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * <p>Shows the given file or directory in Finder</p>[39;49;00m
[37m     * @param path Absolute path to the file or directory[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mshowInFinder[39;49;00m(File[37m [39;49;00mpath)[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[36mboolean[39;49;00m[37m [39;49;00museOSA[37m [39;49;00m=[37m [39;49;00m!NativeInvocationBridge.[36msharedInstance[39;49;00m().[36misEnabled[39;49;00m()[37m [39;49;00m||[37m [39;49;00m!NativeInvocationBridge.[36msharedInstance[39;49;00m().[36mshowInFinder[39;49;00m(path);[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m(useOSA)[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mStringBuffer[37m [39;49;00msb[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mStringBuffer();[37m[39;49;00m
[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33mtell application [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m            [39;49;00msb.[36mappend[39;49;00m(getFileBrowserName());[37m[39;49;00m
[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m to reveal (posix file [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m            [39;49;00msb.[36mappend[39;49;00m(path);[37m[39;49;00m
[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m as alias)[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m            [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
[37m            [39;49;00m{[37m[39;49;00m
[37m                [39;49;00mperformOSAScript(sb);[37m[39;49;00m
[37m            [39;49;00m}[37m[39;49;00m
[37m            [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m
[37m            [39;49;00m{[37m[39;49;00m
[37m                [39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogAlert(LogAlert.[36mUNREPEATABLE[39;49;00m,[37m [39;49;00mLogAlert.[36mAT_ERROR[39;49;00m,[37m [39;49;00me[37m[39;49;00m
[37m						[39;49;00m.[36mgetMessage[39;49;00m()));[37m[39;49;00m
[37m            [39;49;00m}[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * <p>Shows the given file or directory in Terminal by executing cd /absolute/path/to</p>[39;49;00m
[37m     * @param path Absolute path to the file or directory[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mshowInTerminal[39;49;00m(String[37m [39;49;00mpath)[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00mshowInTerminal([34mnew[39;49;00m[37m [39;49;00mFile(path));[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * <p>Shows the given file or directory in Terminal by executing cd /absolute/path/to</p>[39;49;00m
[37m     * @param path Absolute path to the file or directory[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mshowInTerminal[39;49;00m(File[37m [39;49;00mpath)[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(path.[36misFile[39;49;00m())[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mpath[37m [39;49;00m=[37m [39;49;00mpath.[36mgetParentFile[39;49;00m();[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(path[37m [39;49;00m!=[37m [39;49;00m[34mnull[39;49;00m[37m [39;49;00m&&[37m [39;49;00mpath.[36misDirectory[39;49;00m())[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mStringBuffer[37m [39;49;00msb[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mStringBuffer();[37m[39;49;00m
[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33mtell application [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33mTerminal[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m to do script [39;49;00m[33m\"[39;49;00m[33mcd [39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m            [39;49;00msb.[36mappend[39;49;00m(path.[36mgetAbsolutePath[39;49;00m().[36mreplaceAll[39;49;00m([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m [39;49;00m[33m"[39;49;00m));[37m[39;49;00m
[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m            [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
[37m            [39;49;00m{[37m[39;49;00m
[37m                [39;49;00mperformOSAScript(sb);[37m[39;49;00m
[37m            [39;49;00m}[37m[39;49;00m
[37m            [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m
[37m            [39;49;00m{[37m[39;49;00m
[37m                [39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogAlert(LogAlert.[36mUNREPEATABLE[39;49;00m,[37m [39;49;00mLogAlert.[36mAT_ERROR[39;49;00m,[37m [39;49;00me[37m[39;49;00m
[37m						[39;49;00m.[36mgetMessage[39;49;00m()));[37m[39;49;00m
[37m            [39;49;00m}[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m        	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Logger.[36misEnabled[39;49;00m())[37m[39;49;00m
[37m        		[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00mLogEvent.[36mLT_WARNING[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33mCannot find [39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m        				[39;49;00m+[37m [39;49;00mpath.[36mgetName[39;49;00m()));[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m// Internal utility methods[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * Compiles a new AppleScript instance and runs it[39;49;00m
[37m     * @param cmd AppleScript command to execute; do not surround command with extra quotation marks[39;49;00m
[37m     * @return Output of the script[39;49;00m
[37m     * @throws IOException If the script failed to execute[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mperformOSAScript[39;49;00m(CharSequence[37m [39;49;00mcmd)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mIOException[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mperformOSAScript([34mnew[39;49;00m[37m [39;49;00mCharSequence[]{cmd});[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * Compiles a new AppleScript instance and runs it[39;49;00m
[37m     * @param cmds AppleScript Sequence of commands to execute; do not surround command with extra quotation marks[39;49;00m
[37m     * @return Output of the script[39;49;00m
[37m     * @throws IOException If the script failed to execute[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mperformOSAScript[39;49;00m(CharSequence[][37m [39;49;00mcmds)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mIOException[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[36mlong[39;49;00m[37m [39;49;00mstart[37m [39;49;00m=[37m [39;49;00mSystem.[36mcurrentTimeMillis[39;49;00m();[37m[39;49;00m
[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mExecuting OSAScript: [39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m        [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mi[37m [39;49;00m<[37m [39;49;00mcmds.[36mlength[39;49;00m;[37m [39;49;00mi++)[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33m\[39;49;00m[33mt[39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mcmds[i]);[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mString[][37m [39;49;00mcmdargs[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mString[[34m2[39;49;00m[37m [39;49;00m*[37m [39;49;00mcmds.[36mlength[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m];[37m[39;49;00m
[37m        [39;49;00mcmdargs[[34m0[39;49;00m][37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mosascript[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mi[37m [39;49;00m<[37m [39;49;00mcmds.[36mlength[39;49;00m;[37m [39;49;00mi++)[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mcmdargs[i[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m][37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m-e[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
[37m            [39;49;00mcmdargs[i[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m2[39;49;00m][37m [39;49;00m=[37m [39;49;00mString.[36mvalueOf[39;49;00m(cmds[i]);[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mProcess[37m [39;49;00mosaProcess[37m [39;49;00m=[37m [39;49;00mperformRuntimeExec(cmdargs);[37m[39;49;00m
[37m        [39;49;00mBufferedReader[37m [39;49;00mreader[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBufferedReader([34mnew[39;49;00m[37m [39;49;00mInputStreamReader(osaProcess.[36mgetInputStream[39;49;00m()));[37m[39;49;00m
[37m        [39;49;00mString[37m [39;49;00mline[37m [39;49;00m=[37m [39;49;00mreader.[36mreadLine[39;49;00m();[37m[39;49;00m
[37m        [39;49;00mreader.[36mclose[39;49;00m();[37m[39;49;00m
[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSAScript Output: [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mline);[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mreader[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBufferedReader([34mnew[39;49;00m[37m [39;49;00mInputStreamReader(osaProcess.[36mgetErrorStream[39;49;00m()));[37m[39;49;00m
[37m        [39;49;00mString[37m [39;49;00merrorMsg[37m [39;49;00m=[37m [39;49;00mreader.[36mreadLine[39;49;00m();[37m[39;49;00m
[37m        [39;49;00mreader.[36mclose[39;49;00m();[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSAScript Error (if any): [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00merrorMsg);[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m(MessageFormat.[36mformat[39;49;00m([33m"[39;49;00m[33mOSAScript execution ended ({0}ms)[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mObject[]{String.[36mvalueOf[39;49;00m(System.[36mcurrentTimeMillis[39;49;00m()[37m [39;49;00m-[37m [39;49;00mstart)}));[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(errorMsg[37m [39;49;00m!=[37m [39;49;00m[34mnull[39;49;00m)[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mIOException(errorMsg);[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mline;[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * Compiles a new AppleScript instance and runs it[39;49;00m
[37m     * @param script AppleScript file (.scpt) to execute[39;49;00m
[37m     * @return Output of the script[39;49;00m
[37m     * @throws IOException If the script failed to execute[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mperformOSAScript[39;49;00m(File[37m [39;49;00mscript)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mIOException[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[36mlong[39;49;00m[37m [39;49;00mstart[37m [39;49;00m=[37m [39;49;00mSystem.[36mcurrentTimeMillis[39;49;00m();[37m[39;49;00m
[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mExecuting OSAScript from file: [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mscript.[36mgetPath[39;49;00m());[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mProcess[37m [39;49;00mosaProcess[37m [39;49;00m=[37m [39;49;00mperformRuntimeExec([34mnew[39;49;00m[37m [39;49;00mString[]{[33m"[39;49;00m[33mosascript[39;49;00m[33m"[39;49;00m,[37m [39;49;00mscript.[36mgetPath[39;49;00m()});[37m[39;49;00m
[37m        [39;49;00mBufferedReader[37m [39;49;00mreader[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBufferedReader([34mnew[39;49;00m[37m [39;49;00mInputStreamReader(osaProcess.[36mgetInputStream[39;49;00m()));[37m[39;49;00m
[37m        [39;49;00mString[37m [39;49;00mline[37m [39;49;00m=[37m [39;49;00mreader.[36mreadLine[39;49;00m();[37m[39;49;00m
[37m        [39;49;00mreader.[36mclose[39;49;00m();[37m[39;49;00m
[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSAScript Output: [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mline);[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mreader[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBufferedReader([34mnew[39;49;00m[37m [39;49;00mInputStreamReader(osaProcess.[36mgetErrorStream[39;49;00m()));[37m[39;49;00m
[37m        [39;49;00mString[37m [39;49;00merrorMsg[37m [39;49;00m=[37m [39;49;00mreader.[36mreadLine[39;49;00m();[37m[39;49;00m
[37m        [39;49;00mreader.[36mclose[39;49;00m();[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSAScript Error (if any): [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00merrorMsg);[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m(MessageFormat.[36mformat[39;49;00m([33m"[39;49;00m[33mOSAScript execution ended ({0}ms)[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mObject[]{String.[36mvalueOf[39;49;00m(System.[36mcurrentTimeMillis[39;49;00m()[37m [39;49;00m-[37m [39;49;00mstart)}));[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(errorMsg[37m [39;49;00m!=[37m [39;49;00m[34mnull[39;49;00m)[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mIOException(errorMsg);[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mline;[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * Compiles a new AppleScript instance to the specified location[39;49;00m
[37m     * @param cmd         Command to compile; do not surround command with extra quotation marks[39;49;00m
[37m     * @param destination Destination location of the AppleScript file[39;49;00m
[37m     * @return True if compiled successfully[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m [39;49;00m[32mcompileOSAScript[39;49;00m(CharSequence[37m [39;49;00mcmd,[37m [39;49;00mFile[37m [39;49;00mdestination)[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mcompileOSAScript([34mnew[39;49;00m[37m [39;49;00mCharSequence[]{cmd},[37m [39;49;00mdestination);[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * Compiles a new AppleScript instance to the specified location[39;49;00m
[37m     * @param cmds Sequence of commands to compile; do not surround command with extra quotation marks[39;49;00m
[37m     * @param destination Destination location of the AppleScript file[39;49;00m
[37m     * @return True if compiled successfully[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m [39;49;00m[32mcompileOSAScript[39;49;00m(CharSequence[][37m [39;49;00mcmds,[37m [39;49;00mFile[37m [39;49;00mdestination)[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[36mlong[39;49;00m[37m [39;49;00mstart[37m [39;49;00m=[37m [39;49;00mSystem.[36mcurrentTimeMillis[39;49;00m();[37m[39;49;00m
[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mCompiling OSAScript: [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mdestination.[36mgetPath[39;49;00m());[37m[39;49;00m
[37m        [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mi[37m [39;49;00m<[37m [39;49;00mcmds.[36mlength[39;49;00m;[37m [39;49;00mi++)[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33m\[39;49;00m[33mt[39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mcmds[i]);[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mString[][37m [39;49;00mcmdargs[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mString[[34m2[39;49;00m[37m [39;49;00m*[37m [39;49;00mcmds.[36mlength[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m3[39;49;00m];[37m[39;49;00m
[37m        [39;49;00mcmdargs[[34m0[39;49;00m][37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mosacompile[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mi[37m [39;49;00m<[37m [39;49;00mcmds.[36mlength[39;49;00m;[37m [39;49;00mi++)[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mcmdargs[i[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m][37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m-e[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
[37m            [39;49;00mcmdargs[i[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m2[39;49;00m][37m [39;49;00m=[37m [39;49;00mString.[36mvalueOf[39;49;00m(cmds[i]);[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mcmdargs[cmdargs.[36mlength[39;49;00m[37m [39;49;00m-[37m [39;49;00m[34m2[39;49;00m][37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m-o[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
[37m        [39;49;00mcmdargs[cmdargs.[36mlength[39;49;00m[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m][37m [39;49;00m=[37m [39;49;00mdestination.[36mgetPath[39;49;00m();[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mString[37m [39;49;00merrorMsg;[37m[39;49;00m
[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mProcess[37m [39;49;00mosaProcess[37m [39;49;00m=[37m [39;49;00mperformRuntimeExec(cmdargs);[37m[39;49;00m
[37m[39;49;00m
[37m            [39;49;00mBufferedReader[37m [39;49;00mreader[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBufferedReader([34mnew[39;49;00m[37m [39;49;00mInputStreamReader(osaProcess.[36mgetErrorStream[39;49;00m()));[37m[39;49;00m
[37m            [39;49;00merrorMsg[37m [39;49;00m=[37m [39;49;00mreader.[36mreadLine[39;49;00m();[37m[39;49;00m
[37m            [39;49;00mreader.[36mclose[39;49;00m();[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSACompile Execution Failed: [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00me.[36mgetMessage[39;49;00m());[37m[39;49;00m
[37m            [39;49;00mDebug.[36mprintStackTrace[39;49;00m(e);[37m[39;49;00m
[37m            [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mfalse[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSACompile Error (if any): [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00merrorMsg);[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m(MessageFormat.[36mformat[39;49;00m([33m"[39;49;00m[33mOSACompile execution ended ({0}ms)[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mObject[]{String.[36mvalueOf[39;49;00m(System.[36mcurrentTimeMillis[39;49;00m()[37m [39;49;00m-[37m [39;49;00mstart)}));[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m(errorMsg[37m [39;49;00m==[37m [39;49;00m[34mnull[39;49;00m);[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * @see Runtime#exec(String[])[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mProcess[37m [39;49;00m[32mperformRuntimeExec[39;49;00m(String[][37m [39;49;00mcmdargs)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mIOException[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mRuntime.[36mgetRuntime[39;49;00m().[36mexec[39;49;00m(cmdargs);[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogAlert(LogAlert.[36mUNREPEATABLE[39;49;00m,[37m [39;49;00me.[36mgetMessage[39;49;00m(),[37m [39;49;00me));[37m[39;49;00m
[37m            [39;49;00m[34mthrow[39;49;00m[37m [39;49;00me;[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m/**[39;49;00m
[37m     * <p>Gets the preferred file browser name</p>[39;49;00m
[37m     * <p>Currently supported browsers are Path Finder and Finder. If Path Finder is currently running[39;49;00m
[37m     * (not just installed), then "Path Finder is returned; else, "Finder" is returned.</p>[39;49;00m
[37m     * @return "Path Finder" if it is currently running; else "Finder"[39;49;00m
[37m     */[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mprivate[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mgetFileBrowserName[39;49;00m()[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00m[37m// slowwwwwwww[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33mtrue[39;49;00m[33m"[39;49;00m.[36mequalsIgnoreCase[39;49;00m(performOSAScript([33m"[39;49;00m[33mtell application [39;49;00m[33m\"[39;49;00m[33mSystem Events[39;49;00m[33m\"[39;49;00m[33m to exists process [39;49;00m[33m\"[39;49;00m[33mPath Finder[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
[37m            [39;49;00m{[37m[39;49;00m
[37m                [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mPath Finder is running[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
[37m[39;49;00m
[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPath Finder[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
[37m            [39;49;00m}[37m[39;49;00m
[37m            [39;49;00m[34melse[39;49;00m[37m[39;49;00m
[37m            [39;49;00m{[37m[39;49;00m
[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mFinder[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
[37m            [39;49;00m}[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m
[37m        [39;49;00m{[37m[39;49;00m
[37m            [39;49;00mDebug.[36mprintStackTrace[39;49;00m(e);[37m[39;49;00m
[37m            [39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00me.[36mgetMessage[39;49;00m(),[37m [39;49;00me));[37m[39;49;00m
[37m[39;49;00m
[37m            [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mFinder[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
[37m        [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m[37m[39;49;00m
[37m	[39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m[39;49;00m
[37m	[39;49;00m[32mtestNativeAvailability[39;49;00m([37m[39;49;00m
[37m		[39;49;00mString[37m	[39;49;00mname[37m [39;49;00m)[37m[39;49;00m
[37m	[39;49;00m[37m[39;49;00m
[37m		[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
[37m	[39;49;00m{[37m[39;49;00m
[37m	    [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m		[39;49;00m[37m[39;49;00m
[37m	[39;49;00m}[37m[39;49;00m
[37m    [39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[32maddListener[39;49;00m([37m[39;49;00m
[37m    	[39;49;00mPlatformManagerListener[37m		[39;49;00mlistener[37m [39;49;00m)[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
[37m    [39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[32mremoveListener[39;49;00m([37m[39;49;00m
[37m    	[39;49;00mPlatformManagerListener[37m		[39;49;00mlistener[37m [39;49;00m)[37m[39;49;00m
[37m    [39;49;00m{[37m[39;49;00m
[37m    [39;49;00m}[37m[39;49;00m
}
