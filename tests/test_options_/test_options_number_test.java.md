     1	[37m/*[39;49;00m
     2	[37m * Created on 13-Mar-2004[39;49;00m
     3	[37m * Created by James Yeh[39;49;00m
     4	[37m * Copyright (C) 2004, 2005, 2006 Aelitis, All Rights Reserved.[39;49;00m
     5	[37m *[39;49;00m
     6	[37m * This program is free software; you can redistribute it and/or[39;49;00m
     7	[37m * modify it under the terms of the GNU General Public License[39;49;00m
     8	[37m * as published by the Free Software Foundation; either version 2[39;49;00m
     9	[37m * of the License, or (at your option) any later version.[39;49;00m
    10	[37m * This program is distributed in the hope that it will be useful,[39;49;00m
    11	[37m * but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m
    12	[37m * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the[39;49;00m
    13	[37m * GNU General Public License for more details.[39;49;00m
    14	[37m * You should have received a copy of the GNU General Public License[39;49;00m
    15	[37m * along with this program; if not, write to the Free Software[39;49;00m
    16	[37m * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.[39;49;00m
    17	[37m * [39;49;00m
    18	[37m * AELITIS, SAS au capital de 46,603.30 euros[39;49;00m
    19	[37m * 8 Allee Lenotre, La Grille Royale, 78600 Le Mesnil le Roi, France.[39;49;00m
    20	[37m *[39;49;00m
    21	[37m */[39;49;00m[37m[39;49;00m
    22	[37m[39;49;00m
    23	[34mpackage[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.platform.macosx[39;49;00m;[37m[39;49;00m
    24	[37m[39;49;00m
    25	[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.core3.logging.*[39;49;00m;[37m[39;49;00m
    26	[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.core3.util.AEMonitor[39;49;00m;[37m[39;49;00m
    27	[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.core3.util.Debug[39;49;00m;[37m[39;49;00m
    28	[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.core3.util.SystemProperties[39;49;00m;[37m[39;49;00m
    29	[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.platform.PlatformManager[39;49;00m;[37m[39;49;00m
    30	[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.platform.PlatformManagerCapabilities[39;49;00m;[37m[39;49;00m
    31	[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.platform.PlatformManagerListener[39;49;00m;[37m[39;49;00m
    32	[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.platform.macosx.access.jnilib.OSXAccess[39;49;00m;[37m[39;49;00m
    33	[37m[39;49;00m
    34	[34mimport[39;49;00m[37m [39;49;00m[04m[36morg.gudy.azureus2.plugins.platform.PlatformManagerException[39;49;00m;[37m[39;49;00m
    35	[37m[39;49;00m
    36	[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.io.BufferedReader[39;49;00m;[37m[39;49;00m
    37	[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.io.File[39;49;00m;[37m[39;49;00m
    38	[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.io.IOException[39;49;00m;[37m[39;49;00m
    39	[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.io.InputStreamReader[39;49;00m;[37m[39;49;00m
    40	[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.text.MessageFormat[39;49;00m;[37m[39;49;00m
    41	[34mimport[39;49;00m[37m [39;49;00m[04m[36mjava.util.HashSet[39;49;00m;[37m[39;49;00m
    42	[37m[39;49;00m
    43	[37m[39;49;00m
    44	[37m/**[39;49;00m
    45	[37m * Performs platform-specific operations with Mac OS X[39;49;00m
    46	[37m *[39;49;00m
    47	[37m * @author James Yeh[39;49;00m
    48	[37m * @version 1.0 Initial Version[39;49;00m
    49	[37m * @see PlatformManager[39;49;00m
    50	[37m */[39;49;00m[37m[39;49;00m
    51	[34mpublic[39;49;00m[37m [39;49;00m[34mclass[39;49;00m [04m[32mPlatformManagerImpl[39;49;00m[37m [39;49;00m[34mimplements[39;49;00m[37m [39;49;00mPlatformManager[37m[39;49;00m
    52	{[37m[39;49;00m
    53	[37m    [39;49;00m[34mprivate[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[34mfinal[39;49;00m[37m [39;49;00mLogIDs[37m [39;49;00mLOGID[37m [39;49;00m=[37m [39;49;00mLogIDs.[36mCORE[39;49;00m;[37m[39;49;00m
    54	[37m[39;49;00m
    55	[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mPlatformManagerImpl[37m [39;49;00msingleton;[37m[39;49;00m
    56	[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mAEMonitor[37m [39;49;00mclass_mon[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mAEMonitor([33m"[39;49;00m[33mPlatformManager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
    57	[37m[39;49;00m
    58	[37m    [39;49;00m[34mprivate[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[34mfinal[39;49;00m[37m [39;49;00mString[37m [39;49;00mUSERDATA_PATH[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mFile(System.[36mgetProperty[39;49;00m([33m"[39;49;00m[33muser.home[39;49;00m[33m"[39;49;00m)[37m [39;49;00m+[37m [39;49;00m[33m"[39;49;00m[33m/Library/Application Support/[39;49;00m[33m"[39;49;00m).[36mgetPath[39;49;00m();[37m[39;49;00m
    59	[37m[39;49;00m
    60	[37m    [39;49;00m[37m//T: PlatformManagerCapabilities[39;49;00m[37m[39;49;00m
    61	[37m    [39;49;00m[34mprivate[39;49;00m[37m [39;49;00m[34mfinal[39;49;00m[37m [39;49;00mHashSet[37m [39;49;00mcapabilitySet[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mHashSet();[37m[39;49;00m
    62	[37m[39;49;00m
    63	[37m    [39;49;00m[37m/**[39;49;00m
    64	[37m     * Gets the platform manager singleton, which was already initialized[39;49;00m
    65	[37m     */[39;49;00m[37m[39;49;00m
    66	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mPlatformManagerImpl[37m [39;49;00m[32mgetSingleton[39;49;00m()[37m[39;49;00m
    67	[37m    [39;49;00m{[37m[39;49;00m
    68	[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00msingleton;[37m[39;49;00m
    69	[37m    [39;49;00m}[37m[39;49;00m
    70	[37m[39;49;00m
    71	[37m    [39;49;00m[37m/**[39;49;00m
    72	[37m     * Tries to enable cocoa-java access and instantiates the singleton[39;49;00m
    73	[37m     */[39;49;00m[37m[39;49;00m
    74	[37m    [39;49;00m[34mstatic[39;49;00m[37m[39;49;00m
    75	[37m    [39;49;00m{[37m[39;49;00m
    76	[37m        [39;49;00minitializeSingleton();[37m[39;49;00m
    77	[37m    [39;49;00m}[37m[39;49;00m
    78	[37m[39;49;00m
    79	[37m    [39;49;00m[37m/**[39;49;00m
    80	[37m     * Instantiates the singleton[39;49;00m
    81	[37m     */[39;49;00m[37m[39;49;00m
    82	[37m    [39;49;00m[34mprivate[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32minitializeSingleton[39;49;00m()[37m[39;49;00m
    83	[37m    [39;49;00m{[37m[39;49;00m
    84	[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
    85	[37m        [39;49;00m{[37m[39;49;00m
    86	[37m            [39;49;00mclass_mon.[36menter[39;49;00m();[37m[39;49;00m
    87	[37m            [39;49;00msingleton[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerImpl();[37m[39;49;00m
    88	[37m        [39;49;00m}[37m[39;49;00m
    89	[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(Throwable[37m [39;49;00me)[37m[39;49;00m
    90	[37m        [39;49;00m{[37m[39;49;00m
    91	[37m        	[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00m[33m"[39;49;00m[33mFailed to initialize platform manager[39;49;00m[33m"[39;49;00m[37m[39;49;00m
    92	[37m					[39;49;00m+[37m [39;49;00m[33m"[39;49;00m[33m for Mac OS X[39;49;00m[33m"[39;49;00m,[37m [39;49;00me));[37m[39;49;00m
    93	[37m        [39;49;00m}[37m[39;49;00m
    94	[37m        [39;49;00m[34mfinally[39;49;00m[37m[39;49;00m
    95	[37m        [39;49;00m{[37m[39;49;00m
    96	[37m            [39;49;00mclass_mon.[36mexit[39;49;00m();[37m[39;49;00m
    97	[37m        [39;49;00m}[37m[39;49;00m
    98	[37m    [39;49;00m}[37m[39;49;00m
    99	[37m[39;49;00m
   100	[37m    [39;49;00m[37m/**[39;49;00m
   101	[37m     * Creates a new PlatformManager and initializes its capabilities[39;49;00m
   102	[37m     */[39;49;00m[37m[39;49;00m
   103	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[32mPlatformManagerImpl[39;49;00m()[37m[39;49;00m
   104	[37m    [39;49;00m{[37m[39;49;00m
   105	[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mRecoverableFileDelete[39;49;00m);[37m[39;49;00m
   106	[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mShowFileInBrowser[39;49;00m);[37m[39;49;00m
   107	[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mShowPathInCommandLine[39;49;00m);[37m[39;49;00m
   108	[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mCreateCommandLineProcess[39;49;00m);[37m[39;49;00m
   109	[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mGetUserDataDirectory[39;49;00m);[37m[39;49;00m
   110	[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mUseNativeScripting[39;49;00m);[37m[39;49;00m
   111	[37m        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mPlaySystemAlert[39;49;00m);[37m[39;49;00m
   112	[37m        [39;49;00m[37m[39;49;00m
   113	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(OSXAccess.[36misLoaded[39;49;00m())[37m [39;49;00m{[37m[39;49;00m
   114	[37m	        [39;49;00mcapabilitySet.[36madd[39;49;00m(PlatformManagerCapabilities.[36mGetVersion[39;49;00m);[37m[39;49;00m
   115	[37m        [39;49;00m}[37m[39;49;00m
   116	[37m    [39;49;00m}[37m[39;49;00m
   117	[37m[39;49;00m
   118	[37m    [39;49;00m[37m/**[39;49;00m
   119	[37m     * {@inheritDoc}[39;49;00m
   120	[37m     */[39;49;00m[37m[39;49;00m
   121	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mgetPlatformType[39;49;00m()[37m[39;49;00m
   122	[37m    [39;49;00m{[37m[39;49;00m
   123	[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mPT_MACOSX;[37m[39;49;00m
   124	[37m    [39;49;00m}[37m[39;49;00m
   125	[37m[39;49;00m
   126	[37m    [39;49;00m[37m/**[39;49;00m
   127	[37m     * {@inheritDoc}[39;49;00m
   128	[37m     */[39;49;00m[37m[39;49;00m
   129	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mgetVersion[39;49;00m()[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
   130	[37m    [39;49;00m{[37m[39;49;00m
   131	[37m    	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!OSXAccess.[36misLoaded[39;49;00m())[37m [39;49;00m{[37m[39;49;00m
   132	[37m        [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   133	[37m    	[39;49;00m}[37m[39;49;00m
   134	[37m    	[39;49;00m[37m[39;49;00m
   135	[37m    	[39;49;00m[34mreturn[39;49;00m[37m [39;49;00mOSXAccess.[36mgetVersion[39;49;00m();[37m[39;49;00m
   136	[37m    [39;49;00m}[37m[39;49;00m
   137	[37m[39;49;00m
   138	[37m    [39;49;00m[37m/**[39;49;00m
   139	[37m     * {@inheritDoc}[39;49;00m
   140	[37m     * @see org.gudy.azureus2.core3.util.SystemProperties#getUserPath()[39;49;00m
   141	[37m     */[39;49;00m[37m[39;49;00m
   142	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mgetUserDataDirectory[39;49;00m()[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
   143	[37m    [39;49;00m{[37m[39;49;00m
   144	[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mUSERDATA_PATH;[37m[39;49;00m
   145	[37m    [39;49;00m}[37m[39;49;00m
   146	[37m[39;49;00m
   147	[37m	[39;49;00m[34mpublic[39;49;00m[37m [39;49;00mFile[37m[39;49;00m
   148	[37m	[39;49;00m[32mgetLocation[39;49;00m([37m[39;49;00m
   149	[37m		[39;49;00m[36mlong[39;49;00m[37m	[39;49;00mlocation_id[37m [39;49;00m)[37m[39;49;00m
   150	[37m	[39;49;00m[37m[39;49;00m
   151	[37m		[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
   152	[37m	[39;49;00m{[37m[39;49;00m
   153	[37m		[39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00mlocation_id[37m [39;49;00m==[37m [39;49;00mLOC_USER_DATA[37m [39;49;00m){[37m[39;49;00m
   154	[37m			[39;49;00m[37m[39;49;00m
   155	[37m			[39;49;00m[34mreturn[39;49;00m([37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mFile([37m [39;49;00mUSERDATA_PATH[37m [39;49;00m));[37m[39;49;00m
   156	[37m		[39;49;00m}[37m[39;49;00m
   157	[37m		[39;49;00m[37m[39;49;00m
   158	[37m		[39;49;00m[34mreturn[39;49;00m([37m [39;49;00m[34mnull[39;49;00m[37m [39;49;00m);[37m[39;49;00m
   159	[37m	[39;49;00m}[37m[39;49;00m
   160	[37m    [39;49;00m[37m/**[39;49;00m
   161	[37m     * Not implemented; returns True[39;49;00m
   162	[37m     */[39;49;00m[37m[39;49;00m
   163	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m [39;49;00m[32misApplicationRegistered[39;49;00m()[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
   164	[37m    [39;49;00m{[37m[39;49;00m
   165	[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mtrue[39;49;00m;[37m[39;49;00m
   166	[37m    [39;49;00m}[37m[39;49;00m
   167	[37m[39;49;00m
   168	[37m    [39;49;00m[37m[39;49;00m
   169	[37m	[39;49;00m[34mpublic[39;49;00m[37m [39;49;00mString[37m[39;49;00m
   170	[37m	[39;49;00m[32mgetApplicationCommandLine[39;49;00m()[37m[39;49;00m
   171	[37m		[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
   172	[37m	[39;49;00m{[37m[39;49;00m
   173	[37m		[39;49;00m[34mtry[39;49;00m{[37m	    [39;49;00m[37m[39;49;00m
   174	[37m			[39;49;00mString[37m	[39;49;00mbundle_path[37m [39;49;00m=[37m [39;49;00mSystem.[36mgetProperty[39;49;00m([33m"[39;49;00m[33muser.dir[39;49;00m[33m"[39;49;00m)[37m [39;49;00m+SystemProperties.[36mSEP[39;49;00m+[37m [39;49;00mSystemProperties.[36mgetApplicationName[39;49;00m()[37m [39;49;00m+[37m [39;49;00m[33m"[39;49;00m[33m.app[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
   175	[37m[39;49;00m
   176	[37m			[39;49;00mFile[37m [39;49;00mosx_app_bundle[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mFile([37m [39;49;00mbundle_path[37m [39;49;00m).[36mgetAbsoluteFile[39;49;00m();[37m[39;49;00m
   177	[37m			[39;49;00m[37m[39;49;00m
   178	[37m			[39;49;00m[34mif[39;49;00m([37m [39;49;00m!osx_app_bundle.[36mexists[39;49;00m()[37m [39;49;00m)[37m [39;49;00m{[37m[39;49;00m
   179	[37m				[39;49;00mString[37m [39;49;00mmsg[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mOSX app bundle not found: [[39;49;00m[33m"[39;49;00m[37m [39;49;00m+osx_app_bundle.[36mtoString[39;49;00m()+[37m [39;49;00m[33m"[39;49;00m[33m][39;49;00m[33m"[39;49;00m;[37m[39;49;00m
   180	[37m				[39;49;00mSystem.[36mout[39;49;00m.[36mprintln[39;49;00m([37m [39;49;00mmsg[37m [39;49;00m);[37m[39;49;00m
   181	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Logger.[36misEnabled[39;49;00m())[37m[39;49;00m
   182	[37m					[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00mmsg));[37m		[39;49;00m[37m[39;49;00m
   183	[37m				[39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([37m [39;49;00mmsg[37m [39;49;00m);[37m[39;49;00m
   184	[37m			[39;49;00m}[37m[39;49;00m
   185	[37m			[39;49;00m[37m[39;49;00m
   186	[37m			[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mopen -a [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m[37m [39;49;00m+osx_app_bundle.[36mtoString[39;49;00m()+[37m [39;49;00m[33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
   187	[37m			[39;49;00m[37m//return osx_app_bundle.toString() +"/Contents/MacOS/JavaApplicationStub";[39;49;00m[37m[39;49;00m
   188	[37m			[39;49;00m[37m[39;49;00m
   189	[37m		[39;49;00m}[37m[39;49;00m
   190	[37m		[39;49;00m[34mcatch[39;49;00m([37m [39;49;00mThrowable[37m [39;49;00mt[37m [39;49;00m){[37m	[39;49;00m[37m[39;49;00m
   191	[37m			[39;49;00mt.[36mprintStackTrace[39;49;00m();[37m[39;49;00m
   192	[37m			[39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mnull[39;49;00m;[37m[39;49;00m
   193	[37m		[39;49;00m}[37m[39;49;00m
   194	[37m	[39;49;00m}[37m[39;49;00m
   195	[37m	[39;49;00m[37m[39;49;00m
   196	[37m	[39;49;00m[37m[39;49;00m
   197	[37m	[39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m[39;49;00m
   198	[37m	[39;49;00m[32misAdditionalFileTypeRegistered[39;49;00m([37m[39;49;00m
   199	[37m		[39;49;00mString[37m		[39;49;00mname,[37m				[39;49;00m[37m// e.g. "BitTorrent"[39;49;00m[37m[39;49;00m
   200	[37m		[39;49;00mString[37m		[39;49;00mtype[37m [39;49;00m)[37m				[39;49;00m[37m// e.g. ".torrent"[39;49;00m[37m[39;49;00m
   201	[37m	[39;49;00m[37m[39;49;00m
   202	[37m		[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
   203	[37m	[39;49;00m{[37m[39;49;00m
   204	[37m	    [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   205	[37m	[39;49;00m}[37m[39;49;00m
   206	[37m	[39;49;00m[37m[39;49;00m
   207	[37m	[39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m
   208	[37m	[39;49;00m[32munregisterAdditionalFileType[39;49;00m([37m[39;49;00m
   209	[37m		[39;49;00mString[37m		[39;49;00mname,[37m				[39;49;00m[37m// e.g. "BitTorrent"[39;49;00m[37m[39;49;00m
   210	[37m		[39;49;00mString[37m		[39;49;00mtype[37m [39;49;00m)[37m				[39;49;00m[37m// e.g. ".torrent"[39;49;00m[37m[39;49;00m
   211	[37m		[39;49;00m[37m[39;49;00m
   212	[37m		[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
   213	[37m	[39;49;00m{[37m[39;49;00m
   214	[37m		[39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   215	[37m	[39;49;00m}[37m[39;49;00m
   216	[37m	[39;49;00m[37m[39;49;00m
   217	[37m	[39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m
   218	[37m	[39;49;00m[32mregisterAdditionalFileType[39;49;00m([37m[39;49;00m
   219	[37m		[39;49;00mString[37m		[39;49;00mname,[37m				[39;49;00m[37m// e.g. "BitTorrent"[39;49;00m[37m[39;49;00m
   220	[37m		[39;49;00mString[37m		[39;49;00mdescription,[37m		[39;49;00m[37m// e.g. "BitTorrent File"[39;49;00m[37m[39;49;00m
   221	[37m		[39;49;00mString[37m		[39;49;00mtype,[37m				[39;49;00m[37m// e.g. ".torrent"[39;49;00m[37m[39;49;00m
   222	[37m		[39;49;00mString[37m		[39;49;00mcontent_type[37m [39;49;00m)[37m		[39;49;00m[37m// e.g. "application/x-bittorrent"[39;49;00m[37m[39;49;00m
   223	[37m	[39;49;00m[37m[39;49;00m
   224	[37m		[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
   225	[37m	[39;49;00m{[37m[39;49;00m
   226	[37m	   [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   227	[37m	[39;49;00m}[37m[39;49;00m
   228	[37m	[39;49;00m[37m[39;49;00m
   229	[37m    [39;49;00m[37m/**[39;49;00m
   230	[37m     * Not implemented; does nothing[39;49;00m
   231	[37m     */[39;49;00m[37m[39;49;00m
   232	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mregisterApplication[39;49;00m()[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
   233	[37m    [39;49;00m{[37m[39;49;00m
   234	[37m        [39;49;00m[37m// handled by LaunchServices and/0r user interaction[39;49;00m[37m[39;49;00m
   235	[37m    [39;49;00m}[37m[39;49;00m
   236	[37m[39;49;00m
   237	[37m    [39;49;00m[37m/**[39;49;00m
   238	[37m     * {@inheritDoc}[39;49;00m
   239	[37m     */[39;49;00m[37m[39;49;00m
   240	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mcreateProcess[39;49;00m(String[37m [39;49;00mcmd,[37m [39;49;00m[36mboolean[39;49;00m[37m [39;49;00minheritsHandles)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
   241	[37m    [39;49;00m{[37m[39;49;00m
   242	[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
   243	[37m        [39;49;00m{[37m[39;49;00m
   244	[37m            [39;49;00mperformRuntimeExec(cmd.[36msplit[39;49;00m([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m));[37m[39;49;00m
   245	[37m        [39;49;00m}[37m[39;49;00m
   246	[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(Throwable[37m [39;49;00me)[37m[39;49;00m
   247	[37m        [39;49;00m{[37m[39;49;00m
   248	[37m            [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mFailed to create process[39;49;00m[33m"[39;49;00m,[37m [39;49;00me);[37m[39;49;00m
   249	[37m        [39;49;00m}[37m[39;49;00m
   250	[37m    [39;49;00m}[37m[39;49;00m
   251	[37m[39;49;00m
   252	[37m    [39;49;00m[37m/**[39;49;00m
   253	[37m     * {@inheritDoc}[39;49;00m
   254	[37m     */[39;49;00m[37m[39;49;00m
   255	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mperformRecoverableFileDelete[39;49;00m(String[37m [39;49;00mpath)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
   256	[37m    [39;49;00m{[37m[39;49;00m
   257	[37m        [39;49;00mFile[37m [39;49;00mfile[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mFile(path);[37m[39;49;00m
   258	[37m        [39;49;00m[34mif[39;49;00m(!file.[36mexists[39;49;00m())[37m[39;49;00m
   259	[37m        [39;49;00m{[37m[39;49;00m
   260	[37m	        	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Logger.[36misEnabled[39;49;00m())[37m[39;49;00m
   261	[37m							[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00mLogEvent.[36mLT_WARNING[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33mCannot find [39;49;00m[33m"[39;49;00m[37m[39;49;00m
   262	[37m									[39;49;00m+[37m [39;49;00mfile.[36mgetName[39;49;00m()));[37m[39;49;00m
   263	[37m            [39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m
   264	[37m        [39;49;00m}[37m[39;49;00m
   265	[37m[39;49;00m
   266	[37m        [39;49;00m[36mboolean[39;49;00m[37m [39;49;00museOSA[37m [39;49;00m=[37m [39;49;00m!NativeInvocationBridge.[36msharedInstance[39;49;00m().[36misEnabled[39;49;00m()[37m [39;49;00m||[37m [39;49;00m!NativeInvocationBridge.[36msharedInstance[39;49;00m().[36mperformRecoverableFileDelete[39;49;00m(file);[37m[39;49;00m
   267	[37m[39;49;00m
   268	[37m        [39;49;00m[34mif[39;49;00m(useOSA)[37m[39;49;00m
   269	[37m        [39;49;00m{[37m[39;49;00m
   270	[37m            [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
   271	[37m            [39;49;00m{[37m[39;49;00m
   272	[37m                [39;49;00mStringBuffer[37m [39;49;00msb[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mStringBuffer();[37m[39;49;00m
   273	[37m                [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33mtell application [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   274	[37m                [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33mFinder[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   275	[37m                [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m to move (posix file [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   276	[37m                [39;49;00msb.[36mappend[39;49;00m(path);[37m[39;49;00m
   277	[37m                [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m as alias) to the trash[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   278	[37m[39;49;00m
   279	[37m                [39;49;00mperformOSAScript(sb);[37m[39;49;00m
   280	[37m            [39;49;00m}[37m[39;49;00m
   281	[37m            [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(Throwable[37m [39;49;00me)[37m[39;49;00m
   282	[37m            [39;49;00m{[37m[39;49;00m
   283	[37m                [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mFailed to move file[39;49;00m[33m"[39;49;00m,[37m [39;49;00me);[37m[39;49;00m
   284	[37m            [39;49;00m}[37m[39;49;00m
   285	[37m        [39;49;00m}[37m[39;49;00m
   286	[37m    [39;49;00m}[37m[39;49;00m
   287	[37m[39;49;00m
   288	[37m    [39;49;00m[37m/**[39;49;00m
   289	[37m     * {@inheritDoc}[39;49;00m
   290	[37m     */[39;49;00m[37m[39;49;00m
   291	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m [39;49;00m[32mhasCapability[39;49;00m(PlatformManagerCapabilities[37m [39;49;00mcapability)[37m[39;49;00m
   292	[37m    [39;49;00m{[37m[39;49;00m
   293	[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mcapabilitySet.[36mcontains[39;49;00m(capability);[37m[39;49;00m
   294	[37m    [39;49;00m}[37m[39;49;00m
   295	[37m[39;49;00m
   296	[37m    [39;49;00m[37m/**[39;49;00m
   297	[37m     * {@inheritDoc}[39;49;00m
   298	[37m     */[39;49;00m[37m[39;49;00m
   299	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mdispose[39;49;00m()[37m[39;49;00m
   300	[37m    [39;49;00m{[37m[39;49;00m
   301	[37m        [39;49;00mNativeInvocationBridge.[36msharedInstance[39;49;00m().[36mdispose[39;49;00m();[37m[39;49;00m
   302	[37m    [39;49;00m}[37m[39;49;00m
   303	[37m[39;49;00m
   304	[37m    [39;49;00m[37m/**[39;49;00m
   305	[37m     * {@inheritDoc}[39;49;00m
   306	[37m     */[39;49;00m[37m[39;49;00m
   307	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetTCPTOSEnabled[39;49;00m([36mboolean[39;49;00m[37m [39;49;00menabled)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
   308	[37m    [39;49;00m{[37m[39;49;00m
   309	[37m        [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   310	[37m    [39;49;00m}[37m[39;49;00m
   311	[37m[39;49;00m
   312	[37m	[39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m
   313	[37m    [39;49;00m[32mcopyFilePermissions[39;49;00m([37m[39;49;00m
   314	[37m		[39;49;00mString[37m	[39;49;00mfrom_file_name,[37m[39;49;00m
   315	[37m		[39;49;00mString[37m	[39;49;00mto_file_name[37m [39;49;00m)[37m[39;49;00m
   316	[37m	[39;49;00m[37m[39;49;00m
   317	[37m		[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
   318	[37m	[39;49;00m{[37m[39;49;00m
   319	[37m	    [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m		[39;49;00m[37m[39;49;00m
   320	[37m	[39;49;00m}[37m[39;49;00m
   321	[37m	[39;49;00m[37m[39;49;00m
   322	[37m    [39;49;00m[37m/**[39;49;00m
   323	[37m     * {@inheritDoc}[39;49;00m
   324	[37m     */[39;49;00m[37m[39;49;00m
   325	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mshowFile[39;49;00m(String[37m [39;49;00mpath)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
   326	[37m    [39;49;00m{[37m[39;49;00m
   327	[37m        [39;49;00mFile[37m [39;49;00mfile[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mFile(path);[37m[39;49;00m
   328	[37m        [39;49;00m[34mif[39;49;00m(!file.[36mexists[39;49;00m())[37m[39;49;00m
   329	[37m        [39;49;00m{[37m[39;49;00m
   330	[37m        	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Logger.[36misEnabled[39;49;00m())[37m[39;49;00m
   331	[37m        		[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00mLogEvent.[36mLT_WARNING[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33mCannot find [39;49;00m[33m"[39;49;00m[37m[39;49;00m
   332	[37m        				[39;49;00m+[37m [39;49;00mfile.[36mgetName[39;49;00m()));[37m[39;49;00m
   333	[37m            [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mFile not found[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   334	[37m        [39;49;00m}[37m[39;49;00m
   335	[37m[39;49;00m
   336	[37m        [39;49;00mshowInFinder(file);[37m[39;49;00m
   337	[37m    [39;49;00m}[37m[39;49;00m
   338	[37m[39;49;00m
   339	[37m    [39;49;00m[37m// Public utility methods not shared across the interface[39;49;00m[37m[39;49;00m
   340	[37m[39;49;00m
   341	[37m    [39;49;00m[37m/**[39;49;00m
   342	[37m     * Plays the system alert (the jingle is specified by the user in System Preferences)[39;49;00m
   343	[37m     */[39;49;00m[37m[39;49;00m
   344	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mplaySystemAlert[39;49;00m()[37m[39;49;00m
   345	[37m    [39;49;00m{[37m[39;49;00m
   346	[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
   347	[37m        [39;49;00m{[37m[39;49;00m
   348	[37m            [39;49;00mperformRuntimeExec([34mnew[39;49;00m[37m [39;49;00mString[]{[33m"[39;49;00m[33mbeep[39;49;00m[33m"[39;49;00m});[37m[39;49;00m
   349	[37m        [39;49;00m}[37m[39;49;00m
   350	[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m
   351	[37m        [39;49;00m{[37m[39;49;00m
   352	[37m        	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Logger.[36misEnabled[39;49;00m())[37m[39;49;00m
   353	[37m        		[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00mLogEvent.[36mLT_WARNING[39;49;00m,[37m[39;49;00m
   354	[37m						[39;49;00m[33m"[39;49;00m[33mCannot play system alert[39;49;00m[33m"[39;49;00m));[37m[39;49;00m
   355	[37m        	[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m,[37m [39;49;00me));[37m[39;49;00m
   356	[37m        [39;49;00m}[37m[39;49;00m
   357	[37m    [39;49;00m}[37m[39;49;00m
   358	[37m[39;49;00m
   359	[37m    [39;49;00m[37m/**[39;49;00m
   360	[37m     * <p>Shows the given file or directory in Finder</p>[39;49;00m
   361	[37m     * @param path Absolute path to the file or directory[39;49;00m
   362	[37m     */[39;49;00m[37m[39;49;00m
   363	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mshowInFinder[39;49;00m(File[37m [39;49;00mpath)[37m[39;49;00m
   364	[37m    [39;49;00m{[37m[39;49;00m
   365	[37m        [39;49;00m[36mboolean[39;49;00m[37m [39;49;00museOSA[37m [39;49;00m=[37m [39;49;00m!NativeInvocationBridge.[36msharedInstance[39;49;00m().[36misEnabled[39;49;00m()[37m [39;49;00m||[37m [39;49;00m!NativeInvocationBridge.[36msharedInstance[39;49;00m().[36mshowInFinder[39;49;00m(path);[37m[39;49;00m
   366	[37m[39;49;00m
   367	[37m        [39;49;00m[34mif[39;49;00m(useOSA)[37m[39;49;00m
   368	[37m        [39;49;00m{[37m[39;49;00m
   369	[37m            [39;49;00mStringBuffer[37m [39;49;00msb[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mStringBuffer();[37m[39;49;00m
   370	[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33mtell application [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   371	[37m            [39;49;00msb.[36mappend[39;49;00m(getFileBrowserName());[37m[39;49;00m
   372	[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m to reveal (posix file [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   373	[37m            [39;49;00msb.[36mappend[39;49;00m(path);[37m[39;49;00m
   374	[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m as alias)[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   375	[37m[39;49;00m
   376	[37m            [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
   377	[37m            [39;49;00m{[37m[39;49;00m
   378	[37m                [39;49;00mperformOSAScript(sb);[37m[39;49;00m
   379	[37m            [39;49;00m}[37m[39;49;00m
   380	[37m            [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m
   381	[37m            [39;49;00m{[37m[39;49;00m
   382	[37m                [39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogAlert(LogAlert.[36mUNREPEATABLE[39;49;00m,[37m [39;49;00mLogAlert.[36mAT_ERROR[39;49;00m,[37m [39;49;00me[37m[39;49;00m
   383	[37m						[39;49;00m.[36mgetMessage[39;49;00m()));[37m[39;49;00m
   384	[37m            [39;49;00m}[37m[39;49;00m
   385	[37m        [39;49;00m}[37m[39;49;00m
   386	[37m    [39;49;00m}[37m[39;49;00m
   387	[37m[39;49;00m
   388	[37m    [39;49;00m[37m/**[39;49;00m
   389	[37m     * <p>Shows the given file or directory in Terminal by executing cd /absolute/path/to</p>[39;49;00m
   390	[37m     * @param path Absolute path to the file or directory[39;49;00m
   391	[37m     */[39;49;00m[37m[39;49;00m
   392	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mshowInTerminal[39;49;00m(String[37m [39;49;00mpath)[37m[39;49;00m
   393	[37m    [39;49;00m{[37m[39;49;00m
   394	[37m        [39;49;00mshowInTerminal([34mnew[39;49;00m[37m [39;49;00mFile(path));[37m[39;49;00m
   395	[37m    [39;49;00m}[37m[39;49;00m
   396	[37m[39;49;00m
   397	[37m    [39;49;00m[37m/**[39;49;00m
   398	[37m     * <p>Shows the given file or directory in Terminal by executing cd /absolute/path/to</p>[39;49;00m
   399	[37m     * @param path Absolute path to the file or directory[39;49;00m
   400	[37m     */[39;49;00m[37m[39;49;00m
   401	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mshowInTerminal[39;49;00m(File[37m [39;49;00mpath)[37m[39;49;00m
   402	[37m    [39;49;00m{[37m[39;49;00m
   403	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(path.[36misFile[39;49;00m())[37m[39;49;00m
   404	[37m        [39;49;00m{[37m[39;49;00m
   405	[37m            [39;49;00mpath[37m [39;49;00m=[37m [39;49;00mpath.[36mgetParentFile[39;49;00m();[37m[39;49;00m
   406	[37m        [39;49;00m}[37m[39;49;00m
   407	[37m[39;49;00m
   408	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(path[37m [39;49;00m!=[37m [39;49;00m[34mnull[39;49;00m[37m [39;49;00m&&[37m [39;49;00mpath.[36misDirectory[39;49;00m())[37m[39;49;00m
   409	[37m        [39;49;00m{[37m[39;49;00m
   410	[37m            [39;49;00mStringBuffer[37m [39;49;00msb[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mStringBuffer();[37m[39;49;00m
   411	[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33mtell application [39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   412	[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33mTerminal[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   413	[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m to do script [39;49;00m[33m\"[39;49;00m[33mcd [39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   414	[37m            [39;49;00msb.[36mappend[39;49;00m(path.[36mgetAbsolutePath[39;49;00m().[36mreplaceAll[39;49;00m([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m\\[39;49;00m[33m [39;49;00m[33m"[39;49;00m));[37m[39;49;00m
   415	[37m            [39;49;00msb.[36mappend[39;49;00m([33m"[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   416	[37m[39;49;00m
   417	[37m            [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
   418	[37m            [39;49;00m{[37m[39;49;00m
   419	[37m                [39;49;00mperformOSAScript(sb);[37m[39;49;00m
   420	[37m            [39;49;00m}[37m[39;49;00m
   421	[37m            [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m
   422	[37m            [39;49;00m{[37m[39;49;00m
   423	[37m                [39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogAlert(LogAlert.[36mUNREPEATABLE[39;49;00m,[37m [39;49;00mLogAlert.[36mAT_ERROR[39;49;00m,[37m [39;49;00me[37m[39;49;00m
   424	[37m						[39;49;00m.[36mgetMessage[39;49;00m()));[37m[39;49;00m
   425	[37m            [39;49;00m}[37m[39;49;00m
   426	[37m        [39;49;00m}[37m[39;49;00m
   427	[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m
   428	[37m        [39;49;00m{[37m[39;49;00m
   429	[37m        	[39;49;00m[34mif[39;49;00m[37m [39;49;00m(Logger.[36misEnabled[39;49;00m())[37m[39;49;00m
   430	[37m        		[39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00mLogEvent.[36mLT_WARNING[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33mCannot find [39;49;00m[33m"[39;49;00m[37m[39;49;00m
   431	[37m        				[39;49;00m+[37m [39;49;00mpath.[36mgetName[39;49;00m()));[37m[39;49;00m
   432	[37m        [39;49;00m}[37m[39;49;00m
   433	[37m    [39;49;00m}[37m[39;49;00m
   434	[37m[39;49;00m
   435	[37m    [39;49;00m[37m// Internal utility methods[39;49;00m[37m[39;49;00m
   436	[37m[39;49;00m
   437	[37m    [39;49;00m[37m/**[39;49;00m
   438	[37m     * Compiles a new AppleScript instance and runs it[39;49;00m
   439	[37m     * @param cmd AppleScript command to execute; do not surround command with extra quotation marks[39;49;00m
   440	[37m     * @return Output of the script[39;49;00m
   441	[37m     * @throws IOException If the script failed to execute[39;49;00m
   442	[37m     */[39;49;00m[37m[39;49;00m
   443	[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mperformOSAScript[39;49;00m(CharSequence[37m [39;49;00mcmd)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mIOException[37m[39;49;00m
   444	[37m    [39;49;00m{[37m[39;49;00m
   445	[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mperformOSAScript([34mnew[39;49;00m[37m [39;49;00mCharSequence[]{cmd});[37m[39;49;00m
   446	[37m    [39;49;00m}[37m[39;49;00m
   447	[37m[39;49;00m
   448	[37m    [39;49;00m[37m/**[39;49;00m
   449	[37m     * Compiles a new AppleScript instance and runs it[39;49;00m
   450	[37m     * @param cmds AppleScript Sequence of commands to execute; do not surround command with extra quotation marks[39;49;00m
   451	[37m     * @return Output of the script[39;49;00m
   452	[37m     * @throws IOException If the script failed to execute[39;49;00m
   453	[37m     */[39;49;00m[37m[39;49;00m
   454	[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mperformOSAScript[39;49;00m(CharSequence[][37m [39;49;00mcmds)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mIOException[37m[39;49;00m
   455	[37m    [39;49;00m{[37m[39;49;00m
   456	[37m        [39;49;00m[36mlong[39;49;00m[37m [39;49;00mstart[37m [39;49;00m=[37m [39;49;00mSystem.[36mcurrentTimeMillis[39;49;00m();[37m[39;49;00m
   457	[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mExecuting OSAScript: [39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   458	[37m        [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mi[37m [39;49;00m<[37m [39;49;00mcmds.[36mlength[39;49;00m;[37m [39;49;00mi++)[37m[39;49;00m
   459	[37m        [39;49;00m{[37m[39;49;00m
   460	[37m            [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33m\[39;49;00m[33mt[39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mcmds[i]);[37m[39;49;00m
   461	[37m        [39;49;00m}[37m[39;49;00m
   462	[37m[39;49;00m
   463	[37m        [39;49;00mString[][37m [39;49;00mcmdargs[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mString[[34m2[39;49;00m[37m [39;49;00m*[37m [39;49;00mcmds.[36mlength[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m];[37m[39;49;00m
   464	[37m        [39;49;00mcmdargs[[34m0[39;49;00m][37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mosascript[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
   465	[37m        [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mi[37m [39;49;00m<[37m [39;49;00mcmds.[36mlength[39;49;00m;[37m [39;49;00mi++)[37m[39;49;00m
   466	[37m        [39;49;00m{[37m[39;49;00m
   467	[37m            [39;49;00mcmdargs[i[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m][37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m-e[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
   468	[37m            [39;49;00mcmdargs[i[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m2[39;49;00m][37m [39;49;00m=[37m [39;49;00mString.[36mvalueOf[39;49;00m(cmds[i]);[37m[39;49;00m
   469	[37m        [39;49;00m}[37m[39;49;00m
   470	[37m[39;49;00m
   471	[37m        [39;49;00mProcess[37m [39;49;00mosaProcess[37m [39;49;00m=[37m [39;49;00mperformRuntimeExec(cmdargs);[37m[39;49;00m
   472	[37m        [39;49;00mBufferedReader[37m [39;49;00mreader[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBufferedReader([34mnew[39;49;00m[37m [39;49;00mInputStreamReader(osaProcess.[36mgetInputStream[39;49;00m()));[37m[39;49;00m
   473	[37m        [39;49;00mString[37m [39;49;00mline[37m [39;49;00m=[37m [39;49;00mreader.[36mreadLine[39;49;00m();[37m[39;49;00m
   474	[37m        [39;49;00mreader.[36mclose[39;49;00m();[37m[39;49;00m
   475	[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSAScript Output: [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mline);[37m[39;49;00m
   476	[37m[39;49;00m
   477	[37m        [39;49;00mreader[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBufferedReader([34mnew[39;49;00m[37m [39;49;00mInputStreamReader(osaProcess.[36mgetErrorStream[39;49;00m()));[37m[39;49;00m
   478	[37m        [39;49;00mString[37m [39;49;00merrorMsg[37m [39;49;00m=[37m [39;49;00mreader.[36mreadLine[39;49;00m();[37m[39;49;00m
   479	[37m        [39;49;00mreader.[36mclose[39;49;00m();[37m[39;49;00m
   480	[37m[39;49;00m
   481	[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSAScript Error (if any): [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00merrorMsg);[37m[39;49;00m
   482	[37m[39;49;00m
   483	[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m(MessageFormat.[36mformat[39;49;00m([33m"[39;49;00m[33mOSAScript execution ended ({0}ms)[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mObject[]{String.[36mvalueOf[39;49;00m(System.[36mcurrentTimeMillis[39;49;00m()[37m [39;49;00m-[37m [39;49;00mstart)}));[37m[39;49;00m
   484	[37m[39;49;00m
   485	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(errorMsg[37m [39;49;00m!=[37m [39;49;00m[34mnull[39;49;00m)[37m[39;49;00m
   486	[37m        [39;49;00m{[37m[39;49;00m
   487	[37m            [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mIOException(errorMsg);[37m[39;49;00m
   488	[37m        [39;49;00m}[37m[39;49;00m
   489	[37m[39;49;00m
   490	[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mline;[37m[39;49;00m
   491	[37m    [39;49;00m}[37m[39;49;00m
   492	[37m[39;49;00m
   493	[37m    [39;49;00m[37m/**[39;49;00m
   494	[37m     * Compiles a new AppleScript instance and runs it[39;49;00m
   495	[37m     * @param script AppleScript file (.scpt) to execute[39;49;00m
   496	[37m     * @return Output of the script[39;49;00m
   497	[37m     * @throws IOException If the script failed to execute[39;49;00m
   498	[37m     */[39;49;00m[37m[39;49;00m
   499	[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mperformOSAScript[39;49;00m(File[37m [39;49;00mscript)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mIOException[37m[39;49;00m
   500	[37m    [39;49;00m{[37m[39;49;00m
   501	[37m        [39;49;00m[36mlong[39;49;00m[37m [39;49;00mstart[37m [39;49;00m=[37m [39;49;00mSystem.[36mcurrentTimeMillis[39;49;00m();[37m[39;49;00m
   502	[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mExecuting OSAScript from file: [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mscript.[36mgetPath[39;49;00m());[37m[39;49;00m
   503	[37m[39;49;00m
   504	[37m        [39;49;00mProcess[37m [39;49;00mosaProcess[37m [39;49;00m=[37m [39;49;00mperformRuntimeExec([34mnew[39;49;00m[37m [39;49;00mString[]{[33m"[39;49;00m[33mosascript[39;49;00m[33m"[39;49;00m,[37m [39;49;00mscript.[36mgetPath[39;49;00m()});[37m[39;49;00m
   505	[37m        [39;49;00mBufferedReader[37m [39;49;00mreader[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBufferedReader([34mnew[39;49;00m[37m [39;49;00mInputStreamReader(osaProcess.[36mgetInputStream[39;49;00m()));[37m[39;49;00m
   506	[37m        [39;49;00mString[37m [39;49;00mline[37m [39;49;00m=[37m [39;49;00mreader.[36mreadLine[39;49;00m();[37m[39;49;00m
   507	[37m        [39;49;00mreader.[36mclose[39;49;00m();[37m[39;49;00m
   508	[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSAScript Output: [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mline);[37m[39;49;00m
   509	[37m[39;49;00m
   510	[37m        [39;49;00mreader[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBufferedReader([34mnew[39;49;00m[37m [39;49;00mInputStreamReader(osaProcess.[36mgetErrorStream[39;49;00m()));[37m[39;49;00m
   511	[37m        [39;49;00mString[37m [39;49;00merrorMsg[37m [39;49;00m=[37m [39;49;00mreader.[36mreadLine[39;49;00m();[37m[39;49;00m
   512	[37m        [39;49;00mreader.[36mclose[39;49;00m();[37m[39;49;00m
   513	[37m[39;49;00m
   514	[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSAScript Error (if any): [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00merrorMsg);[37m[39;49;00m
   515	[37m[39;49;00m
   516	[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m(MessageFormat.[36mformat[39;49;00m([33m"[39;49;00m[33mOSAScript execution ended ({0}ms)[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mObject[]{String.[36mvalueOf[39;49;00m(System.[36mcurrentTimeMillis[39;49;00m()[37m [39;49;00m-[37m [39;49;00mstart)}));[37m[39;49;00m
   517	[37m[39;49;00m
   518	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(errorMsg[37m [39;49;00m!=[37m [39;49;00m[34mnull[39;49;00m)[37m[39;49;00m
   519	[37m        [39;49;00m{[37m[39;49;00m
   520	[37m            [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mIOException(errorMsg);[37m[39;49;00m
   521	[37m        [39;49;00m}[37m[39;49;00m
   522	[37m[39;49;00m
   523	[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mline;[37m[39;49;00m
   524	[37m    [39;49;00m}[37m[39;49;00m
   525	[37m[39;49;00m
   526	[37m    [39;49;00m[37m/**[39;49;00m
   527	[37m     * Compiles a new AppleScript instance to the specified location[39;49;00m
   528	[37m     * @param cmd         Command to compile; do not surround command with extra quotation marks[39;49;00m
   529	[37m     * @param destination Destination location of the AppleScript file[39;49;00m
   530	[37m     * @return True if compiled successfully[39;49;00m
   531	[37m     */[39;49;00m[37m[39;49;00m
   532	[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m [39;49;00m[32mcompileOSAScript[39;49;00m(CharSequence[37m [39;49;00mcmd,[37m [39;49;00mFile[37m [39;49;00mdestination)[37m[39;49;00m
   533	[37m    [39;49;00m{[37m[39;49;00m
   534	[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mcompileOSAScript([34mnew[39;49;00m[37m [39;49;00mCharSequence[]{cmd},[37m [39;49;00mdestination);[37m[39;49;00m
   535	[37m    [39;49;00m}[37m[39;49;00m
   536	[37m[39;49;00m
   537	[37m    [39;49;00m[37m/**[39;49;00m
   538	[37m     * Compiles a new AppleScript instance to the specified location[39;49;00m
   539	[37m     * @param cmds Sequence of commands to compile; do not surround command with extra quotation marks[39;49;00m
   540	[37m     * @param destination Destination location of the AppleScript file[39;49;00m
   541	[37m     * @return True if compiled successfully[39;49;00m
   542	[37m     */[39;49;00m[37m[39;49;00m
   543	[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m [39;49;00m[32mcompileOSAScript[39;49;00m(CharSequence[][37m [39;49;00mcmds,[37m [39;49;00mFile[37m [39;49;00mdestination)[37m[39;49;00m
   544	[37m    [39;49;00m{[37m[39;49;00m
   545	[37m        [39;49;00m[36mlong[39;49;00m[37m [39;49;00mstart[37m [39;49;00m=[37m [39;49;00mSystem.[36mcurrentTimeMillis[39;49;00m();[37m[39;49;00m
   546	[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mCompiling OSAScript: [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mdestination.[36mgetPath[39;49;00m());[37m[39;49;00m
   547	[37m        [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mi[37m [39;49;00m<[37m [39;49;00mcmds.[36mlength[39;49;00m;[37m [39;49;00mi++)[37m[39;49;00m
   548	[37m        [39;49;00m{[37m[39;49;00m
   549	[37m            [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33m\[39;49;00m[33mt[39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00mcmds[i]);[37m[39;49;00m
   550	[37m        [39;49;00m}[37m[39;49;00m
   551	[37m[39;49;00m
   552	[37m        [39;49;00mString[][37m [39;49;00mcmdargs[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mString[[34m2[39;49;00m[37m [39;49;00m*[37m [39;49;00mcmds.[36mlength[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m3[39;49;00m];[37m[39;49;00m
   553	[37m        [39;49;00mcmdargs[[34m0[39;49;00m][37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mosacompile[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
   554	[37m        [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mi[37m [39;49;00m<[37m [39;49;00mcmds.[36mlength[39;49;00m;[37m [39;49;00mi++)[37m[39;49;00m
   555	[37m        [39;49;00m{[37m[39;49;00m
   556	[37m            [39;49;00mcmdargs[i[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m][37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m-e[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
   557	[37m            [39;49;00mcmdargs[i[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m[37m [39;49;00m+[37m [39;49;00m[34m2[39;49;00m][37m [39;49;00m=[37m [39;49;00mString.[36mvalueOf[39;49;00m(cmds[i]);[37m[39;49;00m
   558	[37m        [39;49;00m}[37m[39;49;00m
   559	[37m[39;49;00m
   560	[37m        [39;49;00mcmdargs[cmdargs.[36mlength[39;49;00m[37m [39;49;00m-[37m [39;49;00m[34m2[39;49;00m][37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m-o[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
   561	[37m        [39;49;00mcmdargs[cmdargs.[36mlength[39;49;00m[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m][37m [39;49;00m=[37m [39;49;00mdestination.[36mgetPath[39;49;00m();[37m[39;49;00m
   562	[37m[39;49;00m
   563	[37m        [39;49;00mString[37m [39;49;00merrorMsg;[37m[39;49;00m
   564	[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
   565	[37m        [39;49;00m{[37m[39;49;00m
   566	[37m            [39;49;00mProcess[37m [39;49;00mosaProcess[37m [39;49;00m=[37m [39;49;00mperformRuntimeExec(cmdargs);[37m[39;49;00m
   567	[37m[39;49;00m
   568	[37m            [39;49;00mBufferedReader[37m [39;49;00mreader[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mBufferedReader([34mnew[39;49;00m[37m [39;49;00mInputStreamReader(osaProcess.[36mgetErrorStream[39;49;00m()));[37m[39;49;00m
   569	[37m            [39;49;00merrorMsg[37m [39;49;00m=[37m [39;49;00mreader.[36mreadLine[39;49;00m();[37m[39;49;00m
   570	[37m            [39;49;00mreader.[36mclose[39;49;00m();[37m[39;49;00m
   571	[37m        [39;49;00m}[37m[39;49;00m
   572	[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m
   573	[37m        [39;49;00m{[37m[39;49;00m
   574	[37m            [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSACompile Execution Failed: [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00me.[36mgetMessage[39;49;00m());[37m[39;49;00m
   575	[37m            [39;49;00mDebug.[36mprintStackTrace[39;49;00m(e);[37m[39;49;00m
   576	[37m            [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34mfalse[39;49;00m;[37m[39;49;00m
   577	[37m        [39;49;00m}[37m[39;49;00m
   578	[37m[39;49;00m
   579	[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mOSACompile Error (if any): [39;49;00m[33m"[39;49;00m[37m [39;49;00m+[37m [39;49;00merrorMsg);[37m[39;49;00m
   580	[37m[39;49;00m
   581	[37m        [39;49;00mDebug.[36moutNoStack[39;49;00m(MessageFormat.[36mformat[39;49;00m([33m"[39;49;00m[33mOSACompile execution ended ({0}ms)[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mObject[]{String.[36mvalueOf[39;49;00m(System.[36mcurrentTimeMillis[39;49;00m()[37m [39;49;00m-[37m [39;49;00mstart)}));[37m[39;49;00m
   582	[37m[39;49;00m
   583	[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m(errorMsg[37m [39;49;00m==[37m [39;49;00m[34mnull[39;49;00m);[37m[39;49;00m
   584	[37m    [39;49;00m}[37m[39;49;00m
   585	[37m[39;49;00m
   586	[37m    [39;49;00m[37m/**[39;49;00m
   587	[37m     * @see Runtime#exec(String[])[39;49;00m
   588	[37m     */[39;49;00m[37m[39;49;00m
   589	[37m    [39;49;00m[34mprotected[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mProcess[37m [39;49;00m[32mperformRuntimeExec[39;49;00m(String[][37m [39;49;00mcmdargs)[37m [39;49;00m[34mthrows[39;49;00m[37m [39;49;00mIOException[37m[39;49;00m
   590	[37m    [39;49;00m{[37m[39;49;00m
   591	[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
   592	[37m        [39;49;00m{[37m[39;49;00m
   593	[37m            [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mRuntime.[36mgetRuntime[39;49;00m().[36mexec[39;49;00m(cmdargs);[37m[39;49;00m
   594	[37m        [39;49;00m}[37m[39;49;00m
   595	[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m
   596	[37m        [39;49;00m{[37m[39;49;00m
   597	[37m            [39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogAlert(LogAlert.[36mUNREPEATABLE[39;49;00m,[37m [39;49;00me.[36mgetMessage[39;49;00m(),[37m [39;49;00me));[37m[39;49;00m
   598	[37m            [39;49;00m[34mthrow[39;49;00m[37m [39;49;00me;[37m[39;49;00m
   599	[37m        [39;49;00m}[37m[39;49;00m
   600	[37m    [39;49;00m}[37m[39;49;00m
   601	[37m[39;49;00m
   602	[37m    [39;49;00m[37m/**[39;49;00m
   603	[37m     * <p>Gets the preferred file browser name</p>[39;49;00m
   604	[37m     * <p>Currently supported browsers are Path Finder and Finder. If Path Finder is currently running[39;49;00m
   605	[37m     * (not just installed), then "Path Finder is returned; else, "Finder" is returned.</p>[39;49;00m
   606	[37m     * @return "Path Finder" if it is currently running; else "Finder"[39;49;00m
   607	[37m     */[39;49;00m[37m[39;49;00m
   608	[37m    [39;49;00m[34mprivate[39;49;00m[37m [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mString[37m [39;49;00m[32mgetFileBrowserName[39;49;00m()[37m[39;49;00m
   609	[37m    [39;49;00m{[37m[39;49;00m
   610	[37m        [39;49;00m[34mtry[39;49;00m[37m[39;49;00m
   611	[37m        [39;49;00m{[37m[39;49;00m
   612	[37m            [39;49;00m[37m// slowwwwwwww[39;49;00m[37m[39;49;00m
   613	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m([33m"[39;49;00m[33mtrue[39;49;00m[33m"[39;49;00m.[36mequalsIgnoreCase[39;49;00m(performOSAScript([33m"[39;49;00m[33mtell application [39;49;00m[33m\"[39;49;00m[33mSystem Events[39;49;00m[33m\"[39;49;00m[33m to exists process [39;49;00m[33m\"[39;49;00m[33mPath Finder[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m)))[37m[39;49;00m
   614	[37m            [39;49;00m{[37m[39;49;00m
   615	[37m                [39;49;00mDebug.[36moutNoStack[39;49;00m([33m"[39;49;00m[33mPath Finder is running[39;49;00m[33m"[39;49;00m);[37m[39;49;00m
   616	[37m[39;49;00m
   617	[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mPath Finder[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
   618	[37m            [39;49;00m}[37m[39;49;00m
   619	[37m            [39;49;00m[34melse[39;49;00m[37m[39;49;00m
   620	[37m            [39;49;00m{[37m[39;49;00m
   621	[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mFinder[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
   622	[37m            [39;49;00m}[37m[39;49;00m
   623	[37m        [39;49;00m}[37m[39;49;00m
   624	[37m        [39;49;00m[34mcatch[39;49;00m[37m [39;49;00m(IOException[37m [39;49;00me)[37m[39;49;00m
   625	[37m        [39;49;00m{[37m[39;49;00m
   626	[37m            [39;49;00mDebug.[36mprintStackTrace[39;49;00m(e);[37m[39;49;00m
   627	[37m            [39;49;00mLogger.[36mlog[39;49;00m([34mnew[39;49;00m[37m [39;49;00mLogEvent(LOGID,[37m [39;49;00me.[36mgetMessage[39;49;00m(),[37m [39;49;00me));[37m[39;49;00m
   628	[37m[39;49;00m
   629	[37m            [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33mFinder[39;49;00m[33m"[39;49;00m;[37m[39;49;00m
   630	[37m        [39;49;00m}[37m[39;49;00m
   631	[37m    [39;49;00m}[37m[39;49;00m
   632	[37m    [39;49;00m[37m[39;49;00m
   633	[37m	[39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mboolean[39;49;00m[37m[39;49;00m
   634	[37m	[39;49;00m[32mtestNativeAvailability[39;49;00m([37m[39;49;00m
   635	[37m		[39;49;00mString[37m	[39;49;00mname[37m [39;49;00m)[37m[39;49;00m
   636	[37m	[39;49;00m[37m[39;49;00m
   637	[37m		[39;49;00m[34mthrows[39;49;00m[37m [39;49;00mPlatformManagerException[37m[39;49;00m
   638	[37m	[39;49;00m{[37m[39;49;00m
   639	[37m	    [39;49;00m[34mthrow[39;49;00m[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mPlatformManagerException([33m"[39;49;00m[33mUnsupported capability called on platform manager[39;49;00m[33m"[39;49;00m);[37m		[39;49;00m[37m[39;49;00m
   640	[37m	[39;49;00m}[37m[39;49;00m
   641	[37m    [39;49;00m[37m[39;49;00m
   642	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m
   643	[37m    [39;49;00m[32maddListener[39;49;00m([37m[39;49;00m
   644	[37m    	[39;49;00mPlatformManagerListener[37m		[39;49;00mlistener[37m [39;49;00m)[37m[39;49;00m
   645	[37m    [39;49;00m{[37m[39;49;00m
   646	[37m    [39;49;00m}[37m[39;49;00m
   647	[37m    [39;49;00m[37m[39;49;00m
   648	[37m    [39;49;00m[34mpublic[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m[39;49;00m
   649	[37m    [39;49;00m[32mremoveListener[39;49;00m([37m[39;49;00m
   650	[37m    	[39;49;00mPlatformManagerListener[37m		[39;49;00mlistener[37m [39;49;00m)[37m[39;49;00m
   651	[37m    [39;49;00m{[37m[39;49;00m
   652	[37m    [39;49;00m}[37m[39;49;00m
   653	}
