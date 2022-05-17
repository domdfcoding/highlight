     1^I[37m/*[39;49;00m$
     2^I[37m * Created on 13-Mar-2004[39;49;00m$
     3^I[37m * Created by James Yeh[39;49;00m$
     4^I[37m * Copyright (C) 2004, 2005, 2006 Aelitis, All Rights Reserved.[39;49;00m$
     5^I[37m *[39;49;00m$
     6^I[37m * This program is free software; you can redistribute it and/or[39;49;00m$
     7^I[37m * modify it under the terms of the GNU General Public License[39;49;00m$
     8^I[37m * as published by the Free Software Foundation; either version 2[39;49;00m$
     9^I[37m * of the License, or (at your option) any later version.[39;49;00m$
    10^I[37m * This program is distributed in the hope that it will be useful,[39;49;00m$
    11^I[37m * but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m$
    12^I[37m * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the[39;49;00m$
    13^I[37m * GNU General Public License for more details.[39;49;00m$
    14^I[37m * You should have received a copy of the GNU General Public License[39;49;00m$
    15^I[37m * along with this program; if not, write to the Free Software[39;49;00m$
    16^I[37m * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.[39;49;00m$
    17^I[37m * [39;49;00m$
    18^I[37m * AELITIS, SAS au capital de 46,603.30 euros[39;49;00m$
    19^I[37m * 8 Allee Lenotre, La Grille Royale, 78600 Le Mesnil le Roi, France.[39;49;00m$
    20^I[37m *[39;49;00m$
    21^I[37m */[39;49;00m[37m[39;49;00m$
    22^I[37m[39;49;00m$
    23^I[34mpackage[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.platform.macosx[39;49;00m;[37m[39;49;00m$
    24^I[37m[39;49;00m$
    25^I[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.core3.logging.*[39;49;00m;[37m[39;49;00m$
    26^I[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.core3.util.AEMonitor[39;49;00m;[37m[39;49;00m$
    27^I[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.core3.util.Debug[39;49;00m;[37m[39;49;00m$
    28^I[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.core3.util.SystemProperties[39;49;00m;[37m[39;49;00m$
    29^I[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.platform.PlatformManager[39;49;00m;[37m[39;49;00m$
    30^I[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.platform.PlatformManagerCapabilities[39;49;00m;[37m[39;49;00m$
    31^I[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.platform.PlatformManagerListener[39;49;00m;[37m[39;49;00m$
    32^I[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.platform.macosx.access.jnilib.OSXAccess[39;49;00m;[37m[39;49;00m$
    33^I[37m[39;49;00m$
    34^I[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.plugins.platform.PlatformManagerException[39;49;00m;[37m[39;49;00m$
    35^I[37m[39;49;00m$
    36^I[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.io.BufferedReader[39;49;00m;[37m[39;49;00m$
    37^I[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.io.File[39;49;00m;[37m[39;49;00m$
    38^I[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.io.IOException[39;49;00m;[37m[39;49;00m$
    39^I[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.io.InputStreamReader[39;49;00m;[37m[39;49;00m$
    40^I[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.text.MessageFormat[39;49;00m;[37m[39;49;00m$
    41^I[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.util.HashSet[39;49;00m;[37m[39;49;00m$
    42^I[37m[39;49;00m$
    43^I[37m[39;49;00m$
    44^I[37m/**[39;49;00m$
    45^I[37m * Performs platform-specific operations with Mac OS X[39;49;00m$
    46^I[37m *[39;49;00m$
    47^I[37m * @author James Yeh[39;49;00m$
    48^I[37m * @version 1.0 Initial Version[39;49;00m$
    49^I[37m * @see PlatformManager[39;49;00m$
    50^I[37m */[39;49;00m[37m[39;49;00m$
    51^I[34mpublic[39;49;00m[37m [39;49;00m[34mclass[39;49;00m [04m[32mPlatformManagerImpl[39;49;00m[37m [39;49;00m[34mimplements[39;49;00m[37m [39;49;00mPlatformManager[37m[39;49;00m$
    52^I{[37m[39;49;00m$
    53^I[37m    [39;49;00m[34mprivate[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[34mfinal[39;49;00m[37m [39;49;00mLogIDs[37m [39;49;00mLOGID[37m [39;49;00m=[37m [39;49;00mLogIDs.[36mCORE[39;49;00m;[37m[39;49;00m$
    54^I[37m[39;49;00m$
    55^I[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mPlatformManagerImpl[37m [39;49;00msingleton;[37m[39;49;00m$
    56^I[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mAEMonitor[37m [39;49;00mclass_mon[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mAEMonitor([33m"[39;49;00m[33mPlatformManager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
    57^I[37m[39;49;00m$
    58^I[37m    [39;49;00m[34mprivate[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[34mfinal[39;49;00m[37m [39;49;00mString[37m [39;49;00mUSERDATA_PATH[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mFile(System.[36mgetProperty[39;49;00m([33m"[39;49;00m[33muser.home[39;49;00m[33m"[39;49;00m)[37m [39;49;00m+[37m [39;49;00m[33m"[39;49;00m[33m/Library/Application Support/[39;49;00m[33m"[39;49;00m).[36mgetPath[39;49;00m();[37m[39;49;00m$
    59^I[37m[39;49;00m$
    60^I[37m    [39;49;00m[37m//T: PlatformManagerCapabilities[39;49;00m[37m[39;49;00m$
    61^I[37m    [39;49;00m[34mprivate[39;49;00m[37m [39;49;00m[34mfinal[39;49;00m[37m [39;49;00mHashSet[37m [39;49;00mcapabilitySet[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mHashSet();[37m[39;49;00m$
    62^I[37m[39;49;00m$
    63^I[37m    [39;49;00m[37m/**[39;49;00m$
    64^I[37m     * Gets the platform manager singleton, which was already initialized[39;49;00m$
    65^I[37m     */[39;49;00m[37m[39;49;00m$
    66^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mPlatformManagerImpl[37m [39;49;00m[32mgetSingleton[39;49;00m()[37m[39;49;00m$
    67^I[37m    [39;49;00m{[37m[39;49;00m$
    68^I[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00msingleton;[37m[39;49;00m$
    69^I[37m    [39;49;00m}[37m[39;49;00m$
    70^I[37m[39;49;00m$
    71^I[37m    [39;49;00m[37m/**[39;49;00m$
    72^I[37m     * Tries to enable cocoa-java access and instantiates the singleton[39;49;00m$
    73^I[37m     */[39;49;00m[37m[39;49;00m$
    74^I[37m    [39;49;00m[34mstatic[39;49;00m[37m[39;49;00m$
    75^I[37m    [39;49;00m{[37m[39;49;00m$
    76^I[37m        [39;49;00minitializeSingleton();[37m[39;49;00m$
    77^I[37m    [39;49;00m}[37m[39;49;00m$
    78^I[37m[39;49;00m$
    79^I[37m    [39;49;00m[37m/**[39;49;00m$
    80^I[37m     * Instantiates the singleton[39;49;00m$
    81^I[37m     */[39;49;00m[37m[39;49;00m$
    82^I[37m    [39;49;00m[34mprivate[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32minitializeSingleton[39;49;00m()[37m[39;49;00m$
    83^I[37m    [39;49;00m{[37m[39;49;00m$
    84^I[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m$
    85^I[37m        [39;49;00m{[37m[39;49;00m$
    86^I[37m            [39;49;00mclass_mon.[36menter[39;49;00m();[37m[39;49;00m$
    87^I[37m            [39;49;00msingleton[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerImpl();[37m[39;49;00m$
    88^I[37m        [39;49;00m}[37m[39;49;00m$
    89^I[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(Throwable[37m [39;49;00me)[37m[39;49;00m$
    90^I[37m        [39;49;00m{[37m[39;49;00m$
    91^I[37m        ^I[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00m[33m"[39;49;00m[33mFailed to initialize platform manager[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
    92^I[37m^I^I^I^I^I[39;49;00m+[37m [39;49;00m[33m"[39;49;00m[33m for Mac OS X[39;49;00m[33m"[39;49;00m,[37m [39;49;00me));[37m[39;49;00m$
    93^I[37m        [39;49;00m}[37m[39;49;00m$
    94^I[37m        [39;49;00m[34mfinally[39;49;00m[37m[39;49;00m$
    95^I[37m        [39;49;00m{[37m[39;49;00m$
    96^I[37m            [39;49;00mclass_mon.[36mexit[39;49;00m();[37m[39;49;00m$
    97^I[37m        [39;49;00m}[37m[39;49;00m$
    98^I[37m    [39;49;00m}[37m[39;49;00m$
    99^I[37m[39;49;00m$
   100^I[37m    [39;49;00m[37m/**[39;49;00m$
   101^I[37m     * Creates a new PlatformManager and initializes its capabilities[39;49;00m$
   102^I[37m     */[39;49;00m[37m[39;49;00m$
   103^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[32mPlatformManagerImpl[39;49;00m()[37m[39;49;00m$
   104^I[37m    [39;49;00m{[37m[39;49;00m$
   105^I[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mRecoverableFileDelete[39;49;00m);[37m[39;49;00m$
   106^I[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mShowFileInBrowser[39;49;00m);[37m[39;49;00m$
   107^I[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mShowPathInCommandLine[39;49;00m);[37m[39;49;00m$
   108^I[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mCreateCommandLineProcess[39;49;00m);[37m[39;49;00m$
   109^I[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mGetUserDataDirectory[39;49;00m);[37m[39;49;00m$
   110^I[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mUseNativeScripting[39;49;00m);[37m[39;49;00m$
   111^I[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mPlaySystemAlert[39;49;00m);[37m[39;49;00m$
   112^I[37m        [39;49;00m[37m[39;49;00m$
   113^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(OSXAccess.[36misLoaded[39;49;00m())[37m [39;49;00m{[37m[39;49;00m$
   114^I[37m^I        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mGetVersion[39;49;00m);[37m[39;49;00m$
   115^I[37m        [39;49;00m}[37m[39;49;00m$
   116^I[37m    [39;49;00m}[37m[39;49;00m$
   117^I[37m[39;49;00m$
   118^I[37m    [39;49;00m[37m/**[39;49;00m$
   119^I[37m     * {@inheritDoc}[39;49;00m$
   120^I[37m     */[39;49;00m[37m[39;49;00m$
   121^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mgetPlatformType[39;49;00m()[37m[39;49;00m$
   122^I[37m    [39;49;00m{[37m[39;49;00m$
   123^I[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mPT_MACOSX;[37m[39;49;00m$
   124^I[37m    [39;49;00m}[37m[39;49;00m$
   125^I[37m[39;49;00m$
   126^I[37m    [39;49;00m[37m/**[39;49;00m$
   127^I[37m     * {@inheritDoc}[39;49;00m$
   128^I[37m     */[39;49;00m[37m[39;49;00m$
   129^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mgetVersion[39;49;00m()[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m$
   130^I[37m    [39;49;00m{[37m[39;49;00m$
   131^I[37m    ^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!OSXAccess.[36misLoaded[39;49;00m())[37m [39;49;00m{[37m[39;49;00m$
   132^I[37m        [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   133^I[37m    ^I[39;49;00m}[37m[39;49;00m$
   134^I[37m    ^I[39;49;00m[37m[39;49;00m$
   135^I[37m    ^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mOSXAccess.[36mgetVersion[39;49;00m();[37m[39;49;00m$
   136^I[37m    [39;49;00m}[37m[39;49;00m$
   137^I[37m[39;49;00m$
   138^I[37m    [39;49;00m[37m/**[39;49;00m$
   139^I[37m     * {@inheritDoc}[39;49;00m$
   140^I[37m     * @see org.gudy.azureus2.core3.util.SystemProperties#getUserPath()[39;49;00m$
   141^I[37m     */[39;49;00m[37m[39;49;00m$
   142^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mgetUserDataDirectory[39;49;00m()[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m$
   143^I[37m    [39;49;00m{[37m[39;49;00m$
   144^I[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mUSERDATA_PATH;[37m[39;49;00m$
   145^I[37m    [39;49;00m}[37m[39;49;00m$
   146^I[37m[39;49;00m$
   147^I[37m^I[39;49;00m[34mpublic[39;49;00m[37m [39;49;00mFile[37m[39;49;00m$
   148^I[37m^I[39;49;00m[32mgetLocation[39;49;00m([37m[39;49;00m$
   149^I[37m^I^I[39;49;00m[36mlong[39;49;00m[37m^I[39;49;00mlocation_id[37m [39;49;00m)[37m[39;49;00m$
   150^I[37m^I[39;49;00m[37m[39;49;00m$
   151^I[37m^I^I[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m$
   152^I[37m^I[39;49;00m{[37m[39;49;00m$
   153^I[37m^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00mlocation_id[37m [39;49;00m==[37m [39;49;00mLOC_USER_DATA[37m [39;49;00m){[37m[39;49;00m$
   154^I[37m^I^I^I[39;49;00m[37m[39;49;00m$
   155^I[37m^I^I^I[39;49;00m[34mreturn[39;49;00m([37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mFile([37m [39;49;00mUSERDATA_PATH[37m [39;49;00m));[37m[39;49;00m$
   156^I[37m^I^I[39;49;00m}[37m[39;49;00m$
   157^I[37m^I^I[39;49;00m[37m[39;49;00m$
   158^I[37m^I^I[39;49;00m[34mreturn[39;49;00m([37m [39;49;00m[34mnull[39;49;00m[37m [39;49;00m);[37m[39;49;00m$
   159^I[37m^I[39;49;00m}[37m[39;49;00m$
   160^I[37m    [39;49;00m[37m/**[39;49;00m$
   161^I[37m     * Not implemented; returns True[39;49;00m$
   162^I[37m     */[39;49;00m[37m[39;49;00m$
   163^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m [39;49;00m[32misApplicationRegistered[39;49;00m()[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m$
   164^I[37m    [39;49;00m{[37m[39;49;00m$
   165^I[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mtrue[39;49;00m;[37m[39;49;00m$
   166^I[37m    [39;49;00m}[37m[39;49;00m$
   167^I[37m[39;49;00m$
   168^I[37m    [39;49;00m[37m[39;49;00m$
   169^I[37m^I[39;49;00m[34mpublic[39;49;00m[37m [39;49;00mString[37m[39;49;00m$
   170^I[37m^I[39;49;00m[32mgetApplicationCommandLine[39;49;00m()[37m[39;49;00m$
   171^I[37m^I^I[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m$
   172^I[37m^I[39;49;00m{[37m[39;49;00m$
   173^I[37m^I^I[39;49;00m[34mtry[39;49;00m{[37m^I    [39;49;00m[37m[39;49;00m$
   174^I[37m^I^I^I[39;49;00mString[37m^I[39;49;00mbundle_path[37m [39;49;00m=[37m [39;49;00mSystem.[36mgetProperty[39;49;00m([33m"[39;49;00m[33muser.dir[39;49;00m[33m"[39;49;00m)[37m [39;49;00m+SystemProperties.[36mSEP[39;49;00m+[37m [39;49;00mSystemProperties.[36mgetApplicationName[39;49;00m()[37m [39;49;00m+[37m [39;49;00m[33m"[39;49;00m[33m.app[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   175^I[37m[39;49;00m$
   176^I[37m^I^I^I[39;49;00mFile[37m [39;49;00mosx_app_bundle[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mFile([37m [39;49;00mbundle_path[37m [39;49;00m).[36mgetAbsoluteFile[39;49;00m();[37m[39;49;00m$
   177^I[37m^I^I^I[39;49;00m[37m[39;49;00m$
   178^I[37m^I^I^I[39;49;00m[34mif[39;49;00m([37m [39;49;00m!osx_app_bundle.[36mexists[39;49;00m()[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m$
   179^I[37m^I^I^I^I[39;49;00mString[37m [39;49;00mmsg[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mOSX app bundle not found: [[39;49;00m[33m"[39;49;00m[37m [39;49;00m+osx_app_bundle.[36mtoString[39;49;00m()+[37m [39;49;00m[33m"[39;49;00m[33m][39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   180^I[37m^I^I^I^I[39;49;00mSystem.[36mout[39;49;00m.[36mprintln[39;49;00m([37m [39;49;00mmsg[37m [39;49;00m);[37m[39;49;00m$
   181^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Logger.[36misEnabled[39;49;00m())[37m[39;49;00m$
   182^I[37m^I^I^I^I^I[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00mmsg));[37m^I^I[39;49;00m[37m[39;49;00m$
   183^I[37m^I^I^I^I[39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([37m [39;49;00mmsg[37m [39;49;00m);[37m[39;49;00m$
   184^I[37m^I^I^I[39;49;00m}[37m[39;49;00m$
   185^I[37m^I^I^I[39;49;00m[37m[39;49;00m$
   186^I[37m^I^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mopen -a [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m [39;49;00m+osx_app_bundle.[36mtoString[39;49;00m()+[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   187^I[37m^I^I^I[39;49;00m[37m//return osx_app_bundle.toString() +"/Contents/MacOS/JavaApplicationStub";[39;49;00m[37m[39;49;00m$
   188^I[37m^I^I^I[39;49;00m[37m[39;49;00m$
   189^I[37m^I^I[39;49;00m}[37m[39;49;00m$
   190^I[37m^I^I[39;49;00m[34mcatch[39;49;00m([37m [39;49;00mThrowable[37m [39;49;00mt[37m [39;49;00m){[37m^I[39;49;00m[37m[39;49;00m$
   191^I[37m^I^I^I[39;49;00mt.[36mprintStackTrace[39;49;00m();[37m[39;49;00m$
   192^I[37m^I^I^I[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mnull[39;49;00m;[37m[39;49;00m$
   193^I[37m^I^I[39;49;00m}[37m[39;49;00m$
   194^I[37m^I[39;49;00m}[37m[39;49;00m$
   195^I[37m^I[39;49;00m[37m[39;49;00m$
   196^I[37m^I[39;49;00m[37m[39;49;00m$
   197^I[37m^I[39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m[39;49;00m$
   198^I[37m^I[39;49;00m[32misAdditionalFileTypeRegistered[39;49;00m([37m[39;49;00m$
   199^I[37m^I^I[39;49;00mString[37m^I^I[39;49;00mname,[37m^I^I^I^I[39;49;00m[37m// e.g. "BitTorrent"[39;49;00m[37m[39;49;00m$
   200^I[37m^I^I[39;49;00mString[37m^I^I[39;49;00mtype[37m [39;49;00m)[37m^I^I^I^I[39;49;00m[37m// e.g. ".torrent"[39;49;00m[37m[39;49;00m$
   201^I[37m^I[39;49;00m[37m[39;49;00m$
   202^I[37m^I^I[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m$
   203^I[37m^I[39;49;00m{[37m[39;49;00m$
   204^I[37m^I    [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   205^I[37m^I[39;49;00m}[37m[39;49;00m$
   206^I[37m^I[39;49;00m[37m[39;49;00m$
   207^I[37m^I[39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m$
   208^I[37m^I[39;49;00m[32munregisterAdditionalFileType[39;49;00m([37m[39;49;00m$
   209^I[37m^I^I[39;49;00mString[37m^I^I[39;49;00mname,[37m^I^I^I^I[39;49;00m[37m// e.g. "BitTorrent"[39;49;00m[37m[39;49;00m$
   210^I[37m^I^I[39;49;00mString[37m^I^I[39;49;00mtype[37m [39;49;00m)[37m^I^I^I^I[39;49;00m[37m// e.g. ".torrent"[39;49;00m[37m[39;49;00m$
   211^I[37m^I^I[39;49;00m[37m[39;49;00m$
   212^I[37m^I^I[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m$
   213^I[37m^I[39;49;00m{[37m[39;49;00m$
   214^I[37m^I^I[39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   215^I[37m^I[39;49;00m}[37m[39;49;00m$
   216^I[37m^I[39;49;00m[37m[39;49;00m$
   217^I[37m^I[39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m$
   218^I[37m^I[39;49;00m[32mregisterAdditionalFileType[39;49;00m([37m[39;49;00m$
   219^I[37m^I^I[39;49;00mString[37m^I^I[39;49;00mname,[37m^I^I^I^I[39;49;00m[37m// e.g. "BitTorrent"[39;49;00m[37m[39;49;00m$
   220^I[37m^I^I[39;49;00mString[37m^I^I[39;49;00mdescription,[37m^I^I[39;49;00m[37m// e.g. "BitTorrent File"[39;49;00m[37m[39;49;00m$
   221^I[37m^I^I[39;49;00mString[37m^I^I[39;49;00mtype,[37m^I^I^I^I[39;49;00m[37m// e.g. ".torrent"[39;49;00m[37m[39;49;00m$
   222^I[37m^I^I[39;49;00mString[37m^I^I[39;49;00mcontent_type[37m [39;49;00m)[37m^I^I[39;49;00m[37m// e.g. "application/x-bittorrent"[39;49;00m[37m[39;49;00m$
   223^I[37m^I[39;49;00m[37m[39;49;00m$
   224^I[37m^I^I[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m$
   225^I[37m^I[39;49;00m{[37m[39;49;00m$
   226^I[37m^I   [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   227^I[37m^I[39;49;00m}[37m[39;49;00m$
   228^I[37m^I[39;49;00m[37m[39;49;00m$
   229^I[37m    [39;49;00m[37m/**[39;49;00m$
   230^I[37m     * Not implemented; does nothing[39;49;00m$
   231^I[37m     */[39;49;00m[37m[39;49;00m$
   232^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mregisterApplication[39;49;00m()[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m$
   233^I[37m    [39;49;00m{[37m[39;49;00m$
   234^I[37m        [39;49;00m[37m// handled by LaunchServices and/0r user interaction[39;49;00m[37m[39;49;00m$
   235^I[37m    [39;49;00m}[37m[39;49;00m$
   236^I[37m[39;49;00m$
   237^I[37m    [39;49;00m[37m/**[39;49;00m$
   238^I[37m     * {@inheritDoc}[39;49;00m$
   239^I[37m     */[39;49;00m[37m[39;49;00m$
   240^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mcreateProcess[39;49;00m(String[37m [39;49;00mcmd,[37m [39;49;00m[36mboolean[39;49;00m[37m [39;49;00minheritsHandles)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m$
   241^I[37m    [39;49;00m{[37m[39;49;00m$
   242^I[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m$
   243^I[37m        [39;49;00m{[37m[39;49;00m$
   244^I[37m            [39;49;00mperformRuntimeExec(cmd.[36msplit[39;49;00m([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m));[37m[39;49;00m$
   245^I[37m        [39;49;00m}[37m[39;49;00m$
   246^I[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(Throwable[37m [39;49;00me)[37m[39;49;00m$
   247^I[37m        [39;49;00m{[37m[39;49;00m$
   248^I[37m            [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mFailed to create process[39;49;00m[33m"[39;49;00m,[37m [39;49;00me);[37m[39;49;00m$
   249^I[37m        [39;49;00m}[37m[39;49;00m$
   250^I[37m    [39;49;00m}[37m[39;49;00m$
   251^I[37m[39;49;00m$
   252^I[37m    [39;49;00m[37m/**[39;49;00m$
   253^I[37m     * {@inheritDoc}[39;49;00m$
   254^I[37m     */[39;49;00m[37m[39;49;00m$
   255^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mperformRecoverableFileDelete[39;49;00m(String[37m [39;49;00mpath)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m$
   256^I[37m    [39;49;00m{[37m[39;49;00m$
   257^I[37m        [39;49;00mFile[37m [39;49;00mfile[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mFile(path);[37m[39;49;00m$
   258^I[37m        [39;49;00m[34mif[39;49;00m(!file.[36mexists[39;49;00m())[37m[39;49;00m$
   259^I[37m        [39;49;00m{[37m[39;49;00m$
   260^I[37m^I        ^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Logger.[36misEnabled[39;49;00m())[37m[39;49;00m$
   261^I[37m^I^I^I^I^I^I^I[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00mLogEvent.[36mLT_WARNING[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33mCannot find [39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   262^I[37m^I^I^I^I^I^I^I^I^I[39;49;00m+[37m [39;49;00mfile.[36mgetName[39;49;00m()));[37m[39;49;00m$
   263^I[37m            [39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
   264^I[37m        [39;49;00m}[37m[39;49;00m$
   265^I[37m[39;49;00m$
   266^I[37m        [39;49;00m[36mboolean[39;49;00m[37m [39;49;00museOSA[37m [39;49;00m=[37m [39;49;00m!NativeInvocationBridge.[36msharedInstance[39;49;00m().[36misEnabled[39;49;00m()[37m [39;49;00m||[37m [39;49;00m!NativeInvocationBridge.[36msharedInstance[39;49;00m().[36mperformRecoverableFileDelete[39;49;00m(file);[37m[39;49;00m$
   267^I[37m[39;49;00m$
   268^I[37m        [39;49;00m[34mif[39;49;00m(useOSA)[37m[39;49;00m$
   269^I[37m        [39;49;00m{[37m[39;49;00m$
   270^I[37m            [39;49;00m[34mtry[39;49;00m[37m[39;49;00m$
   271^I[37m            [39;49;00m{[37m[39;49;00m$
   272^I[37m                [39;49;00mStringBuffer[37m [39;49;00msb[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mStringBuffer();[37m[39;49;00m$
   273^I[37m                [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33mtell application [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   274^I[37m                [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33mFinder[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   275^I[37m                [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m to move (posix file [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   276^I[37m                [39;49;00msb.[36mappend[39;49;00m(path);[37m[39;49;00m$
   277^I[37m                [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m as alias) to the trash[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   278^I[37m[39;49;00m$
   279^I[37m                [39;49;00mperformOSAScript(sb);[37m[39;49;00m$
   280^I[37m            [39;49;00m}[37m[39;49;00m$
   281^I[37m            [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(Throwable[37m [39;49;00me)[37m[39;49;00m$
   282^I[37m            [39;49;00m{[37m[39;49;00m$
   283^I[37m                [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mFailed to move file[39;49;00m[33m"[39;49;00m,[37m [39;49;00me);[37m[39;49;00m$
   284^I[37m            [39;49;00m}[37m[39;49;00m$
   285^I[37m        [39;49;00m}[37m[39;49;00m$
   286^I[37m    [39;49;00m}[37m[39;49;00m$
   287^I[37m[39;49;00m$
   288^I[37m    [39;49;00m[37m/**[39;49;00m$
   289^I[37m     * {@inheritDoc}[39;49;00m$
   290^I[37m     */[39;49;00m[37m[39;49;00m$
   291^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m [39;49;00m[32mhasCapability[39;49;00m(PlatformManagerCapabilities[37m [39;49;00mcapability)[37m[39;49;00m$
   292^I[37m    [39;49;00m{[37m[39;49;00m$
   293^I[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mcapabilitySet.[36mcontains[39;49;00m(capability);[37m[39;49;00m$
   294^I[37m    [39;49;00m}[37m[39;49;00m$
   295^I[37m[39;49;00m$
   296^I[37m    [39;49;00m[37m/**[39;49;00m$
   297^I[37m     * {@inheritDoc}[39;49;00m$
   298^I[37m     */[39;49;00m[37m[39;49;00m$
   299^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mdispose[39;49;00m()[37m[39;49;00m$
   300^I[37m    [39;49;00m{[37m[39;49;00m$
   301^I[37m        [39;49;00mNativeInvocationBridge.[36msharedInstance[39;49;00m().[36mdispose[39;49;00m();[37m[39;49;00m$
   302^I[37m    [39;49;00m}[37m[39;49;00m$
   303^I[37m[39;49;00m$
   304^I[37m    [39;49;00m[37m/**[39;49;00m$
   305^I[37m     * {@inheritDoc}[39;49;00m$
   306^I[37m     */[39;49;00m[37m[39;49;00m$
   307^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetTCPTOSEnabled[39;49;00m([36mboolean[39;49;00m[37m [39;49;00menabled)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m$
   308^I[37m    [39;49;00m{[37m[39;49;00m$
   309^I[37m        [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   310^I[37m    [39;49;00m}[37m[39;49;00m$
   311^I[37m[39;49;00m$
   312^I[37m^I[39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m$
   313^I[37m    [39;49;00m[32mcopyFilePermissions[39;49;00m([37m[39;49;00m$
   314^I[37m^I^I[39;49;00mString[37m^I[39;49;00mfrom_file_name,[37m[39;49;00m$
   315^I[37m^I^I[39;49;00mString[37m^I[39;49;00mto_file_name[37m [39;49;00m)[37m[39;49;00m$
   316^I[37m^I[39;49;00m[37m[39;49;00m$
   317^I[37m^I^I[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m$
   318^I[37m^I[39;49;00m{[37m[39;49;00m$
   319^I[37m^I    [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m^I^I[39;49;00m[37m[39;49;00m$
   320^I[37m^I[39;49;00m}[37m[39;49;00m$
   321^I[37m^I[39;49;00m[37m[39;49;00m$
   322^I[37m    [39;49;00m[37m/**[39;49;00m$
   323^I[37m     * {@inheritDoc}[39;49;00m$
   324^I[37m     */[39;49;00m[37m[39;49;00m$
   325^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mshowFile[39;49;00m(String[37m [39;49;00mpath)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m$
   326^I[37m    [39;49;00m{[37m[39;49;00m$
   327^I[37m        [39;49;00mFile[37m [39;49;00mfile[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mFile(path);[37m[39;49;00m$
   328^I[37m        [39;49;00m[34mif[39;49;00m(!file.[36mexists[39;49;00m())[37m[39;49;00m$
   329^I[37m        [39;49;00m{[37m[39;49;00m$
   330^I[37m        ^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Logger.[36misEnabled[39;49;00m())[37m[39;49;00m$
   331^I[37m        ^I^I[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00mLogEvent.[36mLT_WARNING[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33mCannot find [39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   332^I[37m        ^I^I^I^I[39;49;00m+[37m [39;49;00mfile.[36mgetName[39;49;00m()));[37m[39;49;00m$
   333^I[37m            [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mFile not found[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   334^I[37m        [39;49;00m}[37m[39;49;00m$
   335^I[37m[39;49;00m$
   336^I[37m        [39;49;00mshowInFinder(file);[37m[39;49;00m$
   337^I[37m    [39;49;00m}[37m[39;49;00m$
   338^I[37m[39;49;00m$
   339^I[37m    [39;49;00m[37m// Public utility methods not shared across the interface[39;49;00m[37m[39;49;00m$
   340^I[37m[39;49;00m$
   341^I[37m    [39;49;00m[37m/**[39;49;00m$
   342^I[37m     * Plays the system alert (the jingle is specified by the user in System Preferences)[39;49;00m$
   343^I[37m     */[39;49;00m[37m[39;49;00m$
   344^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mplaySystemAlert[39;49;00m()[37m[39;49;00m$
   345^I[37m    [39;49;00m{[37m[39;49;00m$
   346^I[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m$
   347^I[37m        [39;49;00m{[37m[39;49;00m$
   348^I[37m            [39;49;00mperformRuntimeExec([34mnew[39;49;00m[37m [39;49;00mString[]{[33m"[39;49;00m[33mbeep[39;49;00m[33m"[39;49;00m});[37m[39;49;00m$
   349^I[37m        [39;49;00m}[37m[39;49;00m$
   350^I[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m$
   351^I[37m        [39;49;00m{[37m[39;49;00m$
   352^I[37m        ^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Logger.[36misEnabled[39;49;00m())[37m[39;49;00m$
   353^I[37m        ^I^I[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00mLogEvent.[36mLT_WARNING[39;49;00m,[37m[39;49;00m$
   354^I[37m^I^I^I^I^I^I[39;49;00m[33m"[39;49;00m[33mCannot play system alert[39;49;00m[33m"[39;49;00m));[37m[39;49;00m$
   355^I[37m        ^I[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m,[37m [39;49;00me));[37m[39;49;00m$
   356^I[37m        [39;49;00m}[37m[39;49;00m$
   357^I[37m    [39;49;00m}[37m[39;49;00m$
   358^I[37m[39;49;00m$
   359^I[37m    [39;49;00m[37m/**[39;49;00m$
   360^I[37m     * <p>Shows the given file or directory in Finder</p>[39;49;00m$
   361^I[37m     * @param path Absolute path to the file or directory[39;49;00m$
   362^I[37m     */[39;49;00m[37m[39;49;00m$
   363^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mshowInFinder[39;49;00m(File[37m [39;49;00mpath)[37m[39;49;00m$
   364^I[37m    [39;49;00m{[37m[39;49;00m$
   365^I[37m        [39;49;00m[36mboolean[39;49;00m[37m [39;49;00museOSA[37m [39;49;00m=[37m [39;49;00m!NativeInvocationBridge.[36msharedInstance[39;49;00m().[36misEnabled[39;49;00m()[37m [39;49;00m||[37m [39;49;00m!NativeInvocationBridge.[36msharedInstance[39;49;00m().[36mshowInFinder[39;49;00m(path);[37m[39;49;00m$
   366^I[37m[39;49;00m$
   367^I[37m        [39;49;00m[34mif[39;49;00m(useOSA)[37m[39;49;00m$
   368^I[37m        [39;49;00m{[37m[39;49;00m$
   369^I[37m            [39;49;00mStringBuffer[37m [39;49;00msb[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mStringBuffer();[37m[39;49;00m$
   370^I[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33mtell application [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   371^I[37m            [39;49;00msb.[36mappend[39;49;00m(getFileBrowserName());[37m[39;49;00m$
   372^I[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m to reveal (posix file [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   373^I[37m            [39;49;00msb.[36mappend[39;49;00m(path);[37m[39;49;00m$
   374^I[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m as alias)[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   375^I[37m[39;49;00m$
   376^I[37m            [39;49;00m[34mtry[39;49;00m[37m[39;49;00m$
   377^I[37m            [39;49;00m{[37m[39;49;00m$
   378^I[37m                [39;49;00mperformOSAScript(sb);[37m[39;49;00m$
   379^I[37m            [39;49;00m}[37m[39;49;00m$
   380^I[37m            [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m$
   381^I[37m            [39;49;00m{[37m[39;49;00m$
   382^I[37m                [39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogAlert(LogAlert.[36mUNREPEATABLE[39;49;00m,[37m [39;49;00mLogAlert.[36mAT_ERROR[39;49;00m,[37m [39;49;00me[37m[39;49;00m$
   383^I[37m^I^I^I^I^I^I[39;49;00m.[36mgetMessage[39;49;00m()));[37m[39;49;00m$
   384^I[37m            [39;49;00m}[37m[39;49;00m$
   385^I[37m        [39;49;00m}[37m[39;49;00m$
   386^I[37m    [39;49;00m}[37m[39;49;00m$
   387^I[37m[39;49;00m$
   388^I[37m    [39;49;00m[37m/**[39;49;00m$
   389^I[37m     * <p>Shows the given file or directory in Terminal by executing cd /absolute/path/to</p>[39;49;00m$
   390^I[37m     * @param path Absolute path to the file or directory[39;49;00m$
   391^I[37m     */[39;49;00m[37m[39;49;00m$
   392^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mshowInTerminal[39;49;00m(String[37m [39;49;00mpath)[37m[39;49;00m$
   393^I[37m    [39;49;00m{[37m[39;49;00m$
   394^I[37m        [39;49;00mshowInTerminal([34mnew[39;49;00m[37m [39;49;00mFile(path));[37m[39;49;00m$
   395^I[37m    [39;49;00m}[37m[39;49;00m$
   396^I[37m[39;49;00m$
   397^I[37m    [39;49;00m[37m/**[39;49;00m$
   398^I[37m     * <p>Shows the given file or directory in Terminal by executing cd /absolute/path/to</p>[39;49;00m$
   399^I[37m     * @param path Absolute path to the file or directory[39;49;00m$
   400^I[37m     */[39;49;00m[37m[39;49;00m$
   401^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mshowInTerminal[39;49;00m(File[37m [39;49;00mpath)[37m[39;49;00m$
   402^I[37m    [39;49;00m{[37m[39;49;00m$
   403^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(path.[36misFile[39;49;00m())[37m[39;49;00m$
   404^I[37m        [39;49;00m{[37m[39;49;00m$
   405^I[37m            [39;49;00mpath[37m [39;49;00m=[37m [39;49;00mpath.[36mgetParentFile[39;49;00m();[37m[39;49;00m$
   406^I[37m        [39;49;00m}[37m[39;49;00m$
   407^I[37m[39;49;00m$
   408^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(path[37m [39;49;00m!=[37m [39;49;00m[34mnull[39;49;00m[37m [39;49;00m&&[37m [39;49;00mpath.[36misDirectory[39;49;00m())[37m[39;49;00m$
   409^I[37m        [39;49;00m{[37m[39;49;00m$
   410^I[37m            [39;49;00mStringBuffer[37m [39;49;00msb[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mStringBuffer();[37m[39;49;00m$
   411^I[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33mtell application [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   412^I[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33mTerminal[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   413^I[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m to do script [39;49;00m[33m\"[39;49;00m[33mcd [39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   414^I[37m            [39;49;00msb.[36mappend[39;49;00m(path.[36mgetAbsolutePath[39;49;00m().[36mreplaceAll[39;49;00m([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m [39;49;00m[33m"[39;49;00m));[37m[39;49;00m$
   415^I[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   416^I[37m[39;49;00m$
   417^I[37m            [39;49;00m[34mtry[39;49;00m[37m[39;49;00m$
   418^I[37m            [39;49;00m{[37m[39;49;00m$
   419^I[37m                [39;49;00mperformOSAScript(sb);[37m[39;49;00m$
   420^I[37m            [39;49;00m}[37m[39;49;00m$
   421^I[37m            [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m$
   422^I[37m            [39;49;00m{[37m[39;49;00m$
   423^I[37m                [39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogAlert(LogAlert.[36mUNREPEATABLE[39;49;00m,[37m [39;49;00mLogAlert.[36mAT_ERROR[39;49;00m,[37m [39;49;00me[37m[39;49;00m$
   424^I[37m^I^I^I^I^I^I[39;49;00m.[36mgetMessage[39;49;00m()));[37m[39;49;00m$
   425^I[37m            [39;49;00m}[37m[39;49;00m$
   426^I[37m        [39;49;00m}[37m[39;49;00m$
   427^I[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
   428^I[37m        [39;49;00m{[37m[39;49;00m$
   429^I[37m        ^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Logger.[36misEnabled[39;49;00m())[37m[39;49;00m$
   430^I[37m        ^I^I[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00mLogEvent.[36mLT_WARNING[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33mCannot find [39;49;00m[33m"[39;49;00m[37m[39;49;00m$
   431^I[37m        ^I^I^I^I[39;49;00m+[37m [39;49;00mpath.[36mgetName[39;49;00m()));[37m[39;49;00m$
   432^I[37m        [39;49;00m}[37m[39;49;00m$
   433^I[37m    [39;49;00m}[37m[39;49;00m$
   434^I[37m[39;49;00m$
   435^I[37m    [39;49;00m[37m// Internal utility methods[39;49;00m[37m[39;49;00m$
   436^I[37m[39;49;00m$
   437^I[37m    [39;49;00m[37m/**[39;49;00m$
   438^I[37m     * Compiles a new AppleScript instance and runs it[39;49;00m$
   439^I[37m     * @param cmd AppleScript command to execute; do not surround command with extra quotation marks[39;49;00m$
   440^I[37m     * @return Output of the script[39;49;00m$
   441^I[37m     * @throws IOException If the script failed to execute[39;49;00m$
   442^I[37m     */[39;49;00m[37m[39;49;00m$
   443^I[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mperformOSAScript[39;49;00m(CharSequence[37m [39;49;00mcmd)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mIOException[37m[39;49;00m$
   444^I[37m    [39;49;00m{[37m[39;49;00m$
   445^I[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mperformOSAScript([34mnew[39;49;00m[37m [39;49;00mCharSequence[]{cmd});[37m[39;49;00m$
   446^I[37m    [39;49;00m}[37m[39;49;00m$
   447^I[37m[39;49;00m$
   448^I[37m    [39;49;00m[37m/**[39;49;00m$
   449^I[37m     * Compiles a new AppleScript instance and runs it[39;49;00m$
   450^I[37m     * @param cmds AppleScript Sequence of commands to execute; do not surround command with extra quotation marks[39;49;00m$
   451^I[37m     * @return Output of the script[39;49;00m$
   452^I[37m     * @throws IOException If the script failed to execute[39;49;00m$
   453^I[37m     */[39;49;00m[37m[39;49;00m$
   454^I[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mperformOSAScript[39;49;00m(CharSequence[][37m [39;49;00mcmds)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mIOException[37m[39;49;00m$
   455^I[37m    [39;49;00m{[37m[39;49;00m$
   456^I[37m        [39;49;00m[36mlong[39;49;00m[37m [39;49;00mstart[37m [39;49;00m=[37m [39;49;00mSystem.[36mcurrentTimeMillis[39;49;00m();[37m[39;49;00m$
   457^I[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mExecuting OSAScript: [39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   458^I[37m        [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mi[37m [39;49;00m<[37m [39;49;00mcmds.[36mlength[39;49;00m;[37m [39;49;00mi++)[37m[39;49;00m$
   459^I[37m        [39;49;00m{[37m[39;49;00m$
   460^I[37m            [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33m\[39;49;00m[33mt[39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mcmds[i]);[37m[39;49;00m$
   461^I[37m        [39;49;00m}[37m[39;49;00m$
   462^I[37m[39;49;00m$
   463^I[37m        [39;49;00mString[][37m [39;49;00mcmdargs[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mString[[34m2[39;49;00m[37m [39;49;00m*[37m [39;49;00mcmds.[36mlength[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m];[37m[39;49;00m$
   464^I[37m        [39;49;00mcmdargs[[34m0[39;49;00m][37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mosascript[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   465^I[37m        [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mi[37m [39;49;00m<[37m [39;49;00mcmds.[36mlength[39;49;00m;[37m [39;49;00mi++)[37m[39;49;00m$
   466^I[37m        [39;49;00m{[37m[39;49;00m$
   467^I[37m            [39;49;00mcmdargs[i[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m][37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m-e[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   468^I[37m            [39;49;00mcmdargs[i[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m2[39;49;00m][37m [39;49;00m=[37m [39;49;00mString.[36mvalueOf[39;49;00m(cmds[i]);[37m[39;49;00m$
   469^I[37m        [39;49;00m}[37m[39;49;00m$
   470^I[37m[39;49;00m$
   471^I[37m        [39;49;00mProcess[37m [39;49;00mosaProcess[37m [39;49;00m=[37m [39;49;00mperformRuntimeExec(cmdargs);[37m[39;49;00m$
   472^I[37m        [39;49;00mBufferedReader[37m [39;49;00mreader[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBufferedReader([34mnew[39;49;00m[37m [39;49;00mInputStreamReader(osaProcess.[36mgetInputStream[39;49;00m()));[37m[39;49;00m$
   473^I[37m        [39;49;00mString[37m [39;49;00mline[37m [39;49;00m=[37m [39;49;00mreader.[36mreadLine[39;49;00m();[37m[39;49;00m$
   474^I[37m        [39;49;00mreader.[36mclose[39;49;00m();[37m[39;49;00m$
   475^I[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSAScript Output: [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mline);[37m[39;49;00m$
   476^I[37m[39;49;00m$
   477^I[37m        [39;49;00mreader[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBufferedReader([34mnew[39;49;00m[37m [39;49;00mInputStreamReader(osaProcess.[36mgetErrorStream[39;49;00m()));[37m[39;49;00m$
   478^I[37m        [39;49;00mString[37m [39;49;00merrorMsg[37m [39;49;00m=[37m [39;49;00mreader.[36mreadLine[39;49;00m();[37m[39;49;00m$
   479^I[37m        [39;49;00mreader.[36mclose[39;49;00m();[37m[39;49;00m$
   480^I[37m[39;49;00m$
   481^I[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSAScript Error (if any): [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00merrorMsg);[37m[39;49;00m$
   482^I[37m[39;49;00m$
   483^I[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m(MessageFormat.[36mformat[39;49;00m([33m"[39;49;00m[33mOSAScript execution ended ({0}ms)[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mObject[]{String.[36mvalueOf[39;49;00m(System.[36mcurrentTimeMillis[39;49;00m()[37m [39;49;00m-[37m [39;49;00mstart)}));[37m[39;49;00m$
   484^I[37m[39;49;00m$
   485^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(errorMsg[37m [39;49;00m!=[37m [39;49;00m[34mnull[39;49;00m)[37m[39;49;00m$
   486^I[37m        [39;49;00m{[37m[39;49;00m$
   487^I[37m            [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mIOException(errorMsg);[37m[39;49;00m$
   488^I[37m        [39;49;00m}[37m[39;49;00m$
   489^I[37m[39;49;00m$
   490^I[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mline;[37m[39;49;00m$
   491^I[37m    [39;49;00m}[37m[39;49;00m$
   492^I[37m[39;49;00m$
   493^I[37m    [39;49;00m[37m/**[39;49;00m$
   494^I[37m     * Compiles a new AppleScript instance and runs it[39;49;00m$
   495^I[37m     * @param script AppleScript file (.scpt) to execute[39;49;00m$
   496^I[37m     * @return Output of the script[39;49;00m$
   497^I[37m     * @throws IOException If the script failed to execute[39;49;00m$
   498^I[37m     */[39;49;00m[37m[39;49;00m$
   499^I[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mperformOSAScript[39;49;00m(File[37m [39;49;00mscript)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mIOException[37m[39;49;00m$
   500^I[37m    [39;49;00m{[37m[39;49;00m$
   501^I[37m        [39;49;00m[36mlong[39;49;00m[37m [39;49;00mstart[37m [39;49;00m=[37m [39;49;00mSystem.[36mcurrentTimeMillis[39;49;00m();[37m[39;49;00m$
   502^I[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mExecuting OSAScript from file: [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mscript.[36mgetPath[39;49;00m());[37m[39;49;00m$
   503^I[37m[39;49;00m$
   504^I[37m        [39;49;00mProcess[37m [39;49;00mosaProcess[37m [39;49;00m=[37m [39;49;00mperformRuntimeExec([34mnew[39;49;00m[37m [39;49;00mString[]{[33m"[39;49;00m[33mosascript[39;49;00m[33m"[39;49;00m,[37m [39;49;00mscript.[36mgetPath[39;49;00m()});[37m[39;49;00m$
   505^I[37m        [39;49;00mBufferedReader[37m [39;49;00mreader[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBufferedReader([34mnew[39;49;00m[37m [39;49;00mInputStreamReader(osaProcess.[36mgetInputStream[39;49;00m()));[37m[39;49;00m$
   506^I[37m        [39;49;00mString[37m [39;49;00mline[37m [39;49;00m=[37m [39;49;00mreader.[36mreadLine[39;49;00m();[37m[39;49;00m$
   507^I[37m        [39;49;00mreader.[36mclose[39;49;00m();[37m[39;49;00m$
   508^I[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSAScript Output: [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mline);[37m[39;49;00m$
   509^I[37m[39;49;00m$
   510^I[37m        [39;49;00mreader[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBufferedReader([34mnew[39;49;00m[37m [39;49;00mInputStreamReader(osaProcess.[36mgetErrorStream[39;49;00m()));[37m[39;49;00m$
   511^I[37m        [39;49;00mString[37m [39;49;00merrorMsg[37m [39;49;00m=[37m [39;49;00mreader.[36mreadLine[39;49;00m();[37m[39;49;00m$
   512^I[37m        [39;49;00mreader.[36mclose[39;49;00m();[37m[39;49;00m$
   513^I[37m[39;49;00m$
   514^I[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSAScript Error (if any): [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00merrorMsg);[37m[39;49;00m$
   515^I[37m[39;49;00m$
   516^I[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m(MessageFormat.[36mformat[39;49;00m([33m"[39;49;00m[33mOSAScript execution ended ({0}ms)[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mObject[]{String.[36mvalueOf[39;49;00m(System.[36mcurrentTimeMillis[39;49;00m()[37m [39;49;00m-[37m [39;49;00mstart)}));[37m[39;49;00m$
   517^I[37m[39;49;00m$
   518^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(errorMsg[37m [39;49;00m!=[37m [39;49;00m[34mnull[39;49;00m)[37m[39;49;00m$
   519^I[37m        [39;49;00m{[37m[39;49;00m$
   520^I[37m            [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mIOException(errorMsg);[37m[39;49;00m$
   521^I[37m        [39;49;00m}[37m[39;49;00m$
   522^I[37m[39;49;00m$
   523^I[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mline;[37m[39;49;00m$
   524^I[37m    [39;49;00m}[37m[39;49;00m$
   525^I[37m[39;49;00m$
   526^I[37m    [39;49;00m[37m/**[39;49;00m$
   527^I[37m     * Compiles a new AppleScript instance to the specified location[39;49;00m$
   528^I[37m     * @param cmd         Command to compile; do not surround command with extra quotation marks[39;49;00m$
   529^I[37m     * @param destination Destination location of the AppleScript file[39;49;00m$
   530^I[37m     * @return True if compiled successfully[39;49;00m$
   531^I[37m     */[39;49;00m[37m[39;49;00m$
   532^I[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m [39;49;00m[32mcompileOSAScript[39;49;00m(CharSequence[37m [39;49;00mcmd,[37m [39;49;00mFile[37m [39;49;00mdestination)[37m[39;49;00m$
   533^I[37m    [39;49;00m{[37m[39;49;00m$
   534^I[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mcompileOSAScript([34mnew[39;49;00m[37m [39;49;00mCharSequence[]{cmd},[37m [39;49;00mdestination);[37m[39;49;00m$
   535^I[37m    [39;49;00m}[37m[39;49;00m$
   536^I[37m[39;49;00m$
   537^I[37m    [39;49;00m[37m/**[39;49;00m$
   538^I[37m     * Compiles a new AppleScript instance to the specified location[39;49;00m$
   539^I[37m     * @param cmds Sequence of commands to compile; do not surround command with extra quotation marks[39;49;00m$
   540^I[37m     * @param destination Destination location of the AppleScript file[39;49;00m$
   541^I[37m     * @return True if compiled successfully[39;49;00m$
   542^I[37m     */[39;49;00m[37m[39;49;00m$
   543^I[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m [39;49;00m[32mcompileOSAScript[39;49;00m(CharSequence[][37m [39;49;00mcmds,[37m [39;49;00mFile[37m [39;49;00mdestination)[37m[39;49;00m$
   544^I[37m    [39;49;00m{[37m[39;49;00m$
   545^I[37m        [39;49;00m[36mlong[39;49;00m[37m [39;49;00mstart[37m [39;49;00m=[37m [39;49;00mSystem.[36mcurrentTimeMillis[39;49;00m();[37m[39;49;00m$
   546^I[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mCompiling OSAScript: [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mdestination.[36mgetPath[39;49;00m());[37m[39;49;00m$
   547^I[37m        [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mi[37m [39;49;00m<[37m [39;49;00mcmds.[36mlength[39;49;00m;[37m [39;49;00mi++)[37m[39;49;00m$
   548^I[37m        [39;49;00m{[37m[39;49;00m$
   549^I[37m            [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33m\[39;49;00m[33mt[39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mcmds[i]);[37m[39;49;00m$
   550^I[37m        [39;49;00m}[37m[39;49;00m$
   551^I[37m[39;49;00m$
   552^I[37m        [39;49;00mString[][37m [39;49;00mcmdargs[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mString[[34m2[39;49;00m[37m [39;49;00m*[37m [39;49;00mcmds.[36mlength[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m3[39;49;00m];[37m[39;49;00m$
   553^I[37m        [39;49;00mcmdargs[[34m0[39;49;00m][37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mosacompile[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   554^I[37m        [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mi[37m [39;49;00m<[37m [39;49;00mcmds.[36mlength[39;49;00m;[37m [39;49;00mi++)[37m[39;49;00m$
   555^I[37m        [39;49;00m{[37m[39;49;00m$
   556^I[37m            [39;49;00mcmdargs[i[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m][37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m-e[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   557^I[37m            [39;49;00mcmdargs[i[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m2[39;49;00m][37m [39;49;00m=[37m [39;49;00mString.[36mvalueOf[39;49;00m(cmds[i]);[37m[39;49;00m$
   558^I[37m        [39;49;00m}[37m[39;49;00m$
   559^I[37m[39;49;00m$
   560^I[37m        [39;49;00mcmdargs[cmdargs.[36mlength[39;49;00m[37m [39;49;00m-[37m [39;49;00m[34m2[39;49;00m][37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m-o[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   561^I[37m        [39;49;00mcmdargs[cmdargs.[36mlength[39;49;00m[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m][37m [39;49;00m=[37m [39;49;00mdestination.[36mgetPath[39;49;00m();[37m[39;49;00m$
   562^I[37m[39;49;00m$
   563^I[37m        [39;49;00mString[37m [39;49;00merrorMsg;[37m[39;49;00m$
   564^I[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m$
   565^I[37m        [39;49;00m{[37m[39;49;00m$
   566^I[37m            [39;49;00mProcess[37m [39;49;00mosaProcess[37m [39;49;00m=[37m [39;49;00mperformRuntimeExec(cmdargs);[37m[39;49;00m$
   567^I[37m[39;49;00m$
   568^I[37m            [39;49;00mBufferedReader[37m [39;49;00mreader[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBufferedReader([34mnew[39;49;00m[37m [39;49;00mInputStreamReader(osaProcess.[36mgetErrorStream[39;49;00m()));[37m[39;49;00m$
   569^I[37m            [39;49;00merrorMsg[37m [39;49;00m=[37m [39;49;00mreader.[36mreadLine[39;49;00m();[37m[39;49;00m$
   570^I[37m            [39;49;00mreader.[36mclose[39;49;00m();[37m[39;49;00m$
   571^I[37m        [39;49;00m}[37m[39;49;00m$
   572^I[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m$
   573^I[37m        [39;49;00m{[37m[39;49;00m$
   574^I[37m            [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSACompile Execution Failed: [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00me.[36mgetMessage[39;49;00m());[37m[39;49;00m$
   575^I[37m            [39;49;00mDebug.[36mprintStackTrace[39;49;00m(e);[37m[39;49;00m$
   576^I[37m            [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mfalse[39;49;00m;[37m[39;49;00m$
   577^I[37m        [39;49;00m}[37m[39;49;00m$
   578^I[37m[39;49;00m$
   579^I[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSACompile Error (if any): [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00merrorMsg);[37m[39;49;00m$
   580^I[37m[39;49;00m$
   581^I[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m(MessageFormat.[36mformat[39;49;00m([33m"[39;49;00m[33mOSACompile execution ended ({0}ms)[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mObject[]{String.[36mvalueOf[39;49;00m(System.[36mcurrentTimeMillis[39;49;00m()[37m [39;49;00m-[37m [39;49;00mstart)}));[37m[39;49;00m$
   582^I[37m[39;49;00m$
   583^I[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m(errorMsg[37m [39;49;00m==[37m [39;49;00m[34mnull[39;49;00m);[37m[39;49;00m$
   584^I[37m    [39;49;00m}[37m[39;49;00m$
   585^I[37m[39;49;00m$
   586^I[37m    [39;49;00m[37m/**[39;49;00m$
   587^I[37m     * @see Runtime#exec(String[])[39;49;00m$
   588^I[37m     */[39;49;00m[37m[39;49;00m$
   589^I[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mProcess[37m [39;49;00m[32mperformRuntimeExec[39;49;00m(String[][37m [39;49;00mcmdargs)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mIOException[37m[39;49;00m$
   590^I[37m    [39;49;00m{[37m[39;49;00m$
   591^I[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m$
   592^I[37m        [39;49;00m{[37m[39;49;00m$
   593^I[37m            [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mRuntime.[36mgetRuntime[39;49;00m().[36mexec[39;49;00m(cmdargs);[37m[39;49;00m$
   594^I[37m        [39;49;00m}[37m[39;49;00m$
   595^I[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m$
   596^I[37m        [39;49;00m{[37m[39;49;00m$
   597^I[37m            [39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogAlert(LogAlert.[36mUNREPEATABLE[39;49;00m,[37m [39;49;00me.[36mgetMessage[39;49;00m(),[37m [39;49;00me));[37m[39;49;00m$
   598^I[37m            [39;49;00m[34mthrow[39;49;00m[37m [39;49;00me;[37m[39;49;00m$
   599^I[37m        [39;49;00m}[37m[39;49;00m$
   600^I[37m    [39;49;00m}[37m[39;49;00m$
   601^I[37m[39;49;00m$
   602^I[37m    [39;49;00m[37m/**[39;49;00m$
   603^I[37m     * <p>Gets the preferred file browser name</p>[39;49;00m$
   604^I[37m     * <p>Currently supported browsers are Path Finder and Finder. If Path Finder is currently running[39;49;00m$
   605^I[37m     * (not just installed), then "Path Finder is returned; else, "Finder" is returned.</p>[39;49;00m$
   606^I[37m     * @return "Path Finder" if it is currently running; else "Finder"[39;49;00m$
   607^I[37m     */[39;49;00m[37m[39;49;00m$
   608^I[37m    [39;49;00m[34mprivate[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mgetFileBrowserName[39;49;00m()[37m[39;49;00m$
   609^I[37m    [39;49;00m{[37m[39;49;00m$
   610^I[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m$
   611^I[37m        [39;49;00m{[37m[39;49;00m$
   612^I[37m            [39;49;00m[37m// slowwwwwwww[39;49;00m[37m[39;49;00m$
   613^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33mtrue[39;49;00m[33m"[39;49;00m.[36mequalsIgnoreCase[39;49;00m(performOSAScript([33m"[39;49;00m[33mtell application [39;49;00m[33m\"[39;49;00m[33mSystem Events[39;49;00m[33m\"[39;49;00m[33m to exists process [39;49;00m[33m\"[39;49;00m[33mPath Finder[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m$
   614^I[37m            [39;49;00m{[37m[39;49;00m$
   615^I[37m                [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mPath Finder is running[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   616^I[37m[39;49;00m$
   617^I[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPath Finder[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   618^I[37m            [39;49;00m}[37m[39;49;00m$
   619^I[37m            [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
   620^I[37m            [39;49;00m{[37m[39;49;00m$
   621^I[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mFinder[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   622^I[37m            [39;49;00m}[37m[39;49;00m$
   623^I[37m        [39;49;00m}[37m[39;49;00m$
   624^I[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m$
   625^I[37m        [39;49;00m{[37m[39;49;00m$
   626^I[37m            [39;49;00mDebug.[36mprintStackTrace[39;49;00m(e);[37m[39;49;00m$
   627^I[37m            [39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00me.[36mgetMessage[39;49;00m(),[37m [39;49;00me));[37m[39;49;00m$
   628^I[37m[39;49;00m$
   629^I[37m            [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mFinder[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   630^I[37m        [39;49;00m}[37m[39;49;00m$
   631^I[37m    [39;49;00m}[37m[39;49;00m$
   632^I[37m    [39;49;00m[37m[39;49;00m$
   633^I[37m^I[39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m[39;49;00m$
   634^I[37m^I[39;49;00m[32mtestNativeAvailability[39;49;00m([37m[39;49;00m$
   635^I[37m^I^I[39;49;00mString[37m^I[39;49;00mname[37m [39;49;00m)[37m[39;49;00m$
   636^I[37m^I[39;49;00m[37m[39;49;00m$
   637^I[37m^I^I[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m$
   638^I[37m^I[39;49;00m{[37m[39;49;00m$
   639^I[37m^I    [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m^I^I[39;49;00m[37m[39;49;00m$
   640^I[37m^I[39;49;00m}[37m[39;49;00m$
   641^I[37m    [39;49;00m[37m[39;49;00m$
   642^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m$
   643^I[37m    [39;49;00m[32maddListener[39;49;00m([37m[39;49;00m$
   644^I[37m    ^I[39;49;00mPlatformManagerListener[37m^I^I[39;49;00mlistener[37m [39;49;00m)[37m[39;49;00m$
   645^I[37m    [39;49;00m{[37m[39;49;00m$
   646^I[37m    [39;49;00m}[37m[39;49;00m$
   647^I[37m    [39;49;00m[37m[39;49;00m$
   648^I[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m$
   649^I[37m    [39;49;00m[32mremoveListener[39;49;00m([37m[39;49;00m$
   650^I[37m    ^I[39;49;00mPlatformManagerListener[37m^I^I[39;49;00mlistener[37m [39;49;00m)[37m[39;49;00m$
   651^I[37m    [39;49;00m{[37m[39;49;00m$
   652^I[37m    [39;49;00m}[37m[39;49;00m$
   653^I}$
