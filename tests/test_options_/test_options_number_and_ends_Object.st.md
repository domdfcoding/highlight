     1	![04m[32mProtoObject[39;49;00m [32msubclass:[39;49;00m [33m#Object[39;49;00m$
     2		[32minstanceVariableNames:[39;49;00m [33m''[39;49;00m$
     3		[32mclassVariableNames:[39;49;00m [33m'DependentsFields'[39;49;00m$
     4		[32mpoolDictionaries:[39;49;00m [33m''[39;49;00m$
     5		[32mcategory:[39;49;00m [33m'Kernel-Objects'[39;49;00m[32m![39;49;00m$
     6	$
     7	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'gk 2/24/2004 08:49'![39;49;00m$
     8	[32mbeep[39;49;00m$
     9		[37m"Deprecated."[39;49;00m$
    10		$
    11		[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use Beeper class>>beep instead.'[39;49;00m.$
    12		[04m[32mBeeper[39;49;00m [32mbeep[39;49;00m[34m! ![39;49;00m$
    13	$
    14	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'gk 2/24/2004 08:50'![39;49;00m$
    15	[32mbeepPrimitive[39;49;00m$
    16		[37m"Deprecated. Beep in the absence of sound support."[39;49;00m$
    17		$
    18		[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use Beeper class>>beep or Beeper class>>beepPrimitive instead.'[39;49;00m.$
    19		[04m[32mBeeper[39;49;00m [32mbeepPrimitive[39;49;00m[34m! ![39;49;00m$
    20	$
    21	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'md 12/12/2003 17:02'![39;49;00m$
    22	[32mbeep:[39;49;00m [31msoundName[39;49;00m$
    23		[37m"Make the given sound, unless the making of sound is disabled in Preferences."[39;49;00m$
    24	$
    25		[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use SampledSound>>playSoundNamed: instead.'[39;49;00m.$
    26		[04m[32mPreferences[39;49;00m [32msoundsEnabled[39;49;00m$
    27			[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mplaySoundNamed:[39;49;00m [31msoundName[39;49;00m]$
    28	[34m! ![39;49;00m$
    29	$
    30	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'sd 11/19/2004 16:57'![39;49;00m$
    31	[32mcontentsGetz:[39;49;00m [31mx[39;49;00m$
    32		[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'there is no method named contents in object and in addition only one sender in a method not called'[39;49;00m. $
    33		[36mself[39;49;00m [32mcontents:[39;49;00m [31mx[39;49;00m[34m! ![39;49;00m$
    34	$
    35	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'sd 11/13/2003 21:10'![39;49;00m$
    36	[32mdeprecatedExplanation:[39;49;00m [31maString[39;49;00m$
    37	     [37m"This method is OBSOLETE.  Use #deprecated: instead."[39;49;00m$
    38		[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use Object>>deprecated: instead of deprecatedExplanation:.'[39;49;00m.$
    39	$
    40		[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
    41			[[04m[32mDeprecation[39;49;00m [32msignal:[39;49;00m ([33m'{1} has been deprecated. {2}'[39;49;00m [32mtranslated[39;49;00m [32mformat:[39;49;00m {[36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m. [31maString[39;49;00m})][34m! ![39;49;00m$
    42	$
    43	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'sd 11/13/2003 21:11'![39;49;00m$
    44	[32mdeprecated:[39;49;00m [31maBlock[39;49;00m [32mexplanation:[39;49;00m [31maString[39;49;00m $
    45		 [37m"This method is OBSOLETE.  Use #deprecated:block: instead."[39;49;00m$
    46		[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use Object>>deprecated:block: instead of deprecated:explanation:.'[39;49;00m.$
    47	$
    48		[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
    49			[[04m[32mDeprecation[39;49;00m$
    50				[32msignal:[39;49;00m ([33m'{1} has been deprecated. {2}'[39;49;00m [32mtranslated[39;49;00m [32mformat:[39;49;00m {[36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m. [31maString[39;49;00m})].$
    51		^ [31maBlock[39;49;00m [32mvalue[39;49;00m.$
    52	[34m! ![39;49;00m$
    53	$
    54	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'md 12/12/2003 16:25'![39;49;00m$
    55	[32mdoIfNotNil:[39;49;00m [31maBlock[39;49;00m$
    56		[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'use ifNotNilDo:'[39;49;00m.$
    57		^ [36mself[39;49;00m [32mifNotNilDo:[39;49;00m [31maBlock[39;49;00m$
    58	[34m! ![39;49;00m$
    59	$
    60	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'md 11/27/2004 12:20'![39;49;00m$
    61	[32mifKindOf:[39;49;00m [31maClass[39;49;00m [32mthenDo:[39;49;00m [31maBlock[39;49;00m$
    62		[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Deprecated. Just use #isKindOf:'[39;49;00m.$
    63		^ ([36mself[39;49;00m [32misKindOf:[39;49;00m [31maClass[39;49;00m) [36mifTrue:[39;49;00m [[31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m][34m! ![39;49;00m$
    64	$
    65	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'gk 2/23/2004 20:51'![39;49;00m$
    66	[32mplaySoundNamed:[39;49;00m [31msoundName[39;49;00m$
    67		[37m"Deprecated.[39;49;00m$
    68	[37m	Play the sound with the given name."[39;49;00m$
    69	$
    70		[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use "SoundService default playSoundNamed: aName" instead.'[39;49;00m.$
    71		[04m[32mSoundService[39;49;00m [32mdefault[39;49;00m [32mplaySoundNamed:[39;49;00m [31msoundName[39;49;00m[34m! ![39;49;00m$
    72	$
    73	$
    74	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:23'![39;49;00m$
    75	[32maidaCanBeLocked[39;49;00m$
    76		[37m"can we get an exclusive lock on that object (not already locked)?"[39;49;00m$
    77		^[36mfalse[39;49;00m[34m! ![39;49;00m$
    78	$
    79	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:23'![39;49;00m$
    80	[32maidaDontCache[39;49;00m$
    81		[37m"don't cache web content in a browser. Appropriate header is added to http response"[39;49;00m$
    82		^[36mfalse[39;49;00m[34m! ![39;49;00m$
    83	$
    84	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:24'![39;49;00m$
    85	[32maidaIsLocked[39;49;00m$
    86		[37m"is object locked exclusively?"[39;49;00m$
    87		^[36mfalse[39;49;00m[34m! ![39;49;00m$
    88	$
    89	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:24'![39;49;00m$
    90	[32maidaLock[39;49;00m$
    91		[37m"get an exclusive lock on that object. Until unlocked, noon else can get that lock. Return false if already locked, true if successfull"[39;49;00m$
    92		^[36mfalse[39;49;00m[34m! ![39;49;00m$
    93	$
    94	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:24'![39;49;00m$
    95	[32maidaUnlock[39;49;00m$
    96		[37m"release an exclusive lock if any"[39;49;00m$
    97		^[36mtrue[39;49;00m[34m! ![39;49;00m$
    98	$
    99	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:24'![39;49;00m$
   100	[32mapp[39;49;00m$
   101		[37m"fastest and most convinient way to find a web app for that object"[39;49;00m$
   102		^[36mself[39;49;00m [32mwebAppFor:[39;49;00m [36mself[39;49;00m [32mfirstSessionFromStack[39;49;00m[34m! ![39;49;00m$
   103	$
   104	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:25'![39;49;00m$
   105	[32mcontentType[39;49;00m$
   106	$
   107		[37m"Janko Mivsek, apr98"[39;49;00m$
   108		[37m"return 'text/html' as content type for web pages"[39;49;00m$
   109	$
   110		^[33m'text/html'[39;49;00m[34m! ![39;49;00m$
   111	$
   112	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:25'![39;49;00m$
   113	[32mdeepSearchOfClass:[39;49;00m [31maClassName[39;49;00m$
   114		[37m"finf all objects of that class down in object hierarchy"[39;49;00m$
   115		|[31m objectDictionary class [39;49;00m|$
   116		[31mobjectDictionary[39;49;00m := [04m[32mIdentityDictionary[39;49;00m [36mnew[39;49;00m.$
   117		[36mself[39;49;00m [32mdeepCopyNotIn:[39;49;00m [31mobjectDictionary[39;49;00m.$
   118		[31mclass[39;49;00m := [31maClassName[39;49;00m [32masSymbol[39;49;00m.$
   119		^[31mobjectDictionary[39;49;00m [32mkeys[39;49;00m [32mselect:[39;49;00m [:[31meach[39;49;00m | [31meach[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32m=[39;49;00m [31mclass[39;49;00m].[34m! ![39;49;00m$
   120	$
   121	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:26'![39;49;00m$
   122	[32mdeepSearchOfObsoleteClasses[39;49;00m$
   123		[37m"find all objects of obsolete classes down in object hierarchy"[39;49;00m$
   124		|[31m objectDictionary [39;49;00m|$
   125		[31mobjectDictionary[39;49;00m := [04m[32mIdentityDictionary[39;49;00m [36mnew[39;49;00m.$
   126		[36mself[39;49;00m [32mdeepCopyNotIn:[39;49;00m [31mobjectDictionary[39;49;00m.$
   127		^[31mobjectDictionary[39;49;00m [32mkeys[39;49;00m [32mselect:[39;49;00m [:[31meach[39;49;00m | [31meach[39;49;00m [32mclass[39;49;00m [32misObsolete[39;49;00m].[34m! ![39;49;00m$
   128	$
   129	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:26'![39;49;00m$
   130	[32mexpiresTimestamp[39;49;00m$
   131		[37m"until when content of this object wont be changed"[39;49;00m$
   132		[37m"used in http response, override if you like to be included"[39;49;00m$
   133		^[36mself[39;49;00m [32mmodifiedTimestamp[39;49;00m  [37m"to reload pages immediately"[39;49;00m[34m! ![39;49;00m$
   134	$
   135	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:26'![39;49;00m$
   136	[32mfirstAppFromStack[39;49;00m$
   137		[37m"try to find a first sender up in calling stack, who is  WebApplication"[39;49;00m$
   138		|[31m context [39;49;00m|$
   139		[31mcontext[39;49;00m := [36mthisContext[39;49;00m.$
   140		[[31mcontext[39;49;00m [32mnotNil[39;49;00m] [36mwhileTrue:[39;49;00m [$
   141			([31mcontext[39;49;00m [32mreceiver[39;49;00m [32misKindOf:[39;49;00m [04m[32mWebApplication[39;49;00m) [36mifTrue:[39;49;00m [^[31mcontext[39;49;00m [32mreceiver[39;49;00m].$
   142			[31mcontext[39;49;00m := [31mcontext[39;49;00m [32msender[39;49;00m].$
   143		^[36mself[39;49;00m [32mfirstSessionFromStack[39;49;00m [32mlastApp[39;49;00m[34m! ![39;49;00m$
   144	$
   145	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/25/2007 21:34'![39;49;00m$
   146	[32mfirstSessionFromStack[39;49;00m$
   147		[37m"try to find a first sender up in calling stack, who is  AIDASite and get session if that call"[39;49;00m$
   148		|[31m context [39;49;00m|$
   149		[31mcontext[39;49;00m := [36mthisContext[39;49;00m.$
   150		[[31mcontext[39;49;00m [32mnotNil[39;49;00m] [36mwhileTrue:[39;49;00m [$
   151			([31mcontext[39;49;00m [32mreceiver[39;49;00m [32misKindOf:[39;49;00m [04m[32mAIDASite[39;49;00m) [36mifTrue:[39;49;00m 	[^([31mcontext[39;49;00m [32mat:[39;49;00m [34m3[39;49;00m) [37m"always?"[39;49;00m].$
   152			[31mcontext[39;49;00m := [31mcontext[39;49;00m [32msender[39;49;00m].$
   153		^[36mnil[39;49;00m[34m! ![39;49;00m$
   154	$
   155	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'mivsek 1/10/2008 18:14'![39;49;00m$
   156	[32mforLanguage:[39;49;00m [31maLanguageCodeSymbol[39;49;00m$
   157		[37m"for multilingual support: returns an apropriate instance of itself for that language. [39;49;00m$
   158	[37m	Langage is defined by ISO 639 2-letter language code, see [39;49;00m$
   159	[37m	http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes"[39;49;00m$
   160		^[36mfalse[39;49;00m[34m! ![39;49;00m$
   161	$
   162	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'mivsek 1/10/2008 18:14'![39;49;00m$
   163	[32misMultilingual[39;49;00m$
   164		[37m"for multilingual support: override this if your domain object responds [39;49;00m$
   165	[37m	to #forLanguage: and returns an apropriate instance of itself for that language"[39;49;00m$
   166		^[36mfalse[39;49;00m[34m! ![39;49;00m$
   167	$
   168	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:27'![39;49;00m$
   169	[32misVersionedObject[39;49;00m$
   170		^[36mfalse[39;49;00m[34m! ![39;49;00m$
   171	$
   172	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:27'![39;49;00m$
   173	[32misWebApplication[39;49;00m$
   174		^[36mfalse[39;49;00m[34m! ![39;49;00m$
   175	$
   176	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:27'![39;49;00m$
   177	[32misWebStyle[39;49;00m$
   178		^[36mfalse[39;49;00m[34m! ![39;49;00m$
   179	$
   180	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:27'![39;49;00m$
   181	[32mmodifiedTimestamp[39;49;00m$
   182		[37m"when this object was last modified"[39;49;00m$
   183		[37m"used in http response, override if you like to be included"[39;49;00m$
   184		^[36mnil[39;49;00m[34m! ![39;49;00m$
   185	$
   186	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:28'![39;49;00m$
   187	[32mpreferedUrl[39;49;00m$
   188		[37m"override with a suggestion for url of this method!! If not already used, [39;49;00m$
   189	[37m	it will be considered by URLResolver during automatic url generation"[39;49;00m$
   190		^[36mnil[39;49;00m[34m! ![39;49;00m$
   191	$
   192	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:28'![39;49;00m$
   193	[32mprintWebAppNotFoundFor:[39;49;00m [31maSession[39;49;00m $
   194		|[31m page [39;49;00m|$
   195		[31mpage[39;49;00m := [04m[32mWebPage[39;49;00m [36mnew[39;49;00m.$
   196		[31mpage[39;49;00m [32maddText:[39;49;00m [33m'Cannot find aWebApplication for object a'[39;49;00m[32m,[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m.$
   197		^[31mpage[39;49;00m[34m! ![39;49;00m$
   198	$
   199	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:28'![39;49;00m$
   200	[32mprintWebPageFor:[39;49;00m [31maSession[39;49;00m $
   201		[37m"find appropriate web application to represent self as web page"[39;49;00m$
   202	$
   203		|[31m webApp [39;49;00m|$
   204		[31mwebApp[39;49;00m := [36mself[39;49;00m [32mwebAppFor:[39;49;00m [31maSession[39;49;00m.$
   205		^[31mwebApp[39;49;00m [32mnotNil[39;49;00m $
   206			[36mifTrue:[39;49;00m [[31mwebApp[39;49;00m [32mprintWebPage[39;49;00m]$
   207			[36mifFalse:[39;49;00m [[36mself[39;49;00m [32mprintWebAppNotFoundFor:[39;49;00m [31maSession[39;49;00m][34m! ![39;49;00m$
   208	$
   209	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:29'![39;49;00m$
   210	[32msendOver:[39;49;00m [31maStream[39;49;00m $
   211		[37m"from Wiki rendering"[39;49;00m$
   212		[36mself[39;49;00m [32mprintOn:[39;49;00m [31maStream[39;49;00m[34m! ![39;49;00m$
   213	$
   214	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:29'![39;49;00m$
   215	[32mwebAppFor:[39;49;00m [31maSession[39;49;00m$
   216		|[31m webApp [39;49;00m|$
   217		[31maSession[39;49;00m [32misNil[39;49;00m [36mifTrue:[39;49;00m [^[36mnil[39;49;00m].$
   218		[31mwebApp[39;49;00m := [31maSession[39;49;00m [32mwebAppFor:[39;49;00m [36mself[39;49;00m.$
   219		[31mwebApp[39;49;00m [32mnotNil[39;49;00m [36mifTrue:[39;49;00m [^[31mwebApp[39;49;00m].$
   220		[31mwebApp[39;49;00m := [04m[32mWebApplication[39;49;00m [32mnewFor:[39;49;00m [36mself[39;49;00m [32mon:[39;49;00m [31maSession[39;49;00m.$
   221		[31mwebApp[39;49;00m [32mnotNil[39;49;00m [36mifTrue:[39;49;00m [[31maSession[39;49;00m [32maddWebApp:[39;49;00m [31mwebApp[39;49;00m [32mfor:[39;49;00m [36mself[39;49;00m].$
   222		^[31mwebApp[39;49;00m[34m! ![39;49;00m$
   223	$
   224	$
   225	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*DynamicBindings'[39;49;00m[34m stamp: 'svp 3/6/2003 16:08'![39;49;00m$
   226	[32mbinding[39;49;00m$
   227		[37m"Answer the DynamicBinding for the receiver (if any)"[39;49;00m$
   228	$
   229		^[04m[32mBindings[39;49;00m [32mbindingFor:[39;49;00m [36mself[39;49;00m [32mifNotBound:[39;49;00m [[36mnil[39;49;00m][34m! ![39;49;00m$
   230	$
   231	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*DynamicBindings'[39;49;00m[34m stamp: 'svp 4/29/2003 00:35'![39;49;00m$
   232	[32mbinding:[39;49;00m [31manObject[39;49;00m$
   233		[37m"Set the dynamic binding for the receiver, if anObject is nil, then [39;49;00m$
   234	[37m	remove the receiver's dynamic binding (if any)"[39;49;00m$
   235	$
   236		^[31manObject[39;49;00m $
   237			[32mifNil:[39;49;00m [[36mself[39;49;00m [32mremoveBinding[39;49;00m]$
   238			[32mifNotNil:[39;49;00m [[04m[32mBindings[39;49;00m [32mbind:[39;49;00m [36mself[39;49;00m [32mto:[39;49;00m [31manObject[39;49;00m][34m! ![39;49;00m$
   239	$
   240	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*DynamicBindings'[39;49;00m[34m stamp: 'svp 3/6/2003 16:09'![39;49;00m$
   241	[32mhasBinding[39;49;00m$
   242		[37m"Answer whether or not the receiver has a dynamic binding"[39;49;00m$
   243	$
   244		^[04m[32mBindings[39;49;00m [32mincludesKey:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
   245	$
   246	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*DynamicBindings'[39;49;00m[34m stamp: 'svp 3/6/2003 16:09'![39;49;00m$
   247	[32mremoveBinding[39;49;00m$
   248		[37m"Remove the dynamic binding associated with the receiver"[39;49;00m$
   249	$
   250		^[04m[32mBindings[39;49;00m [32mremoveKey:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m [][34m! ![39;49;00m$
   251	$
   252	$
   253	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*KomHttpServer'[39;49;00m[34m stamp: 'SVP 8/23/1999 19:17'![39;49;00m$
   254	[32masHtmlDocumentForRequest:[39;49;00m [31maNetworkRequest[39;49;00m$
   255	$
   256		[36mself[39;49;00m [32merror:[39;49;00m $
   257			([33m'The requested object ('[39;49;00m[32m,[39;49;00m $
   258			[36mself[39;49;00m [32masString[39;49;00m[32m,[39;49;00m $
   259			[33m'), could not be converted into HTML for your browser.'[39;49;00m)[34m! ![39;49;00m$
   260	$
   261	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*KomHttpServer'[39;49;00m[34m stamp: 'SVP 8/23/1999 19:23'![39;49;00m$
   262	[32masHttpResponseTo:[39;49;00m [31manHttpRequest[39;49;00m$
   263	$
   264		^([36mself[39;49;00m [32masHtmlDocumentForRequest:[39;49;00m [31manHttpRequest[39;49;00m) $
   265			[32masHttpResponseTo:[39;49;00m [31manHttpRequest[39;49;00m$
   266	[34m! ![39;49;00m$
   267	$
   268	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*KomHttpServer'[39;49;00m[34m stamp: 'svp 5/16/2003 12:47'![39;49;00m$
   269	[32misComancheModule[39;49;00m$
   270	$
   271		^[36mfalse[39;49;00m[34m! ![39;49;00m$
   272	$
   273	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*KomHttpServer'[39;49;00m[34m stamp: 'SVP 8/17/1999 17:51'![39;49;00m$
   274	[32mmimeType[39;49;00m$
   275	$
   276		^[04m[32mMIMEDocument[39;49;00m [32mdefaultContentType[39;49;00m[34m! ![39;49;00m$
   277	$
   278	$
   279	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Morphic-NewCurve-testing'''[39;49;00m[34m stamp: 'wiz 12/31/2005 21:31'![39;49;00m$
   280	[32misNonZero[39;49;00m$
   281	[37m"Overriden in Number. This returns the backstop answer for non-numbers"[39;49;00m$
   282	^[36mfalse[39;49;00m.[34m! ![39;49;00m$
   283	$
   284	$
   285	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/25/2006 18:18'![39;49;00m$
   286	[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   287	[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
   288	[32mto:[39;49;00m [31manObject[39;49;00m$
   289	[32mexclusive:[39;49;00m [31maValueHolder[39;49;00m$
   290	 $
   291		[36mself[39;49;00m$
   292			[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   293			[32mevaluate:[39;49;00m (([04m[32mExclusiveWeakMessageSend[39;49;00m$
   294						[32mreceiver:[39;49;00m [31manObject[39;49;00m$
   295						[32mselector:[39;49;00m [31maMessageSelector[39;49;00m)$
   296							[32mbasicExecuting:[39;49;00m [31maValueHolder[39;49;00m)[34m! ![39;49;00m$
   297	$
   298	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/25/2006 18:17'![39;49;00m$
   299	[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   300	[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
   301	[32mto:[39;49;00m [31manObject[39;49;00m$
   302	[32mwith:[39;49;00m [31manArg[39;49;00m$
   303	[32mexclusive:[39;49;00m [31maValueHolder[39;49;00m$
   304	 $
   305	    [36mself[39;49;00m$
   306	        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   307	        [32mevaluate:[39;49;00m (([04m[32mExclusiveWeakMessageSend[39;49;00m$
   308	 		[32mreceiver:[39;49;00m [31manObject[39;49;00m$
   309			[32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
   310			[32marguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manArg[39;49;00m))$
   311				[32mbasicExecuting:[39;49;00m [31maValueHolder[39;49;00m)[34m! ![39;49;00m$
   312	$
   313	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/25/2006 18:17'![39;49;00m$
   314	[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   315	[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
   316	[32mto:[39;49;00m [31manObject[39;49;00m$
   317	[32mwithArguments:[39;49;00m [31manArgArray[39;49;00m$
   318	[32mexclusive:[39;49;00m [31maValueHolder[39;49;00m$
   319	 $
   320	    [36mself[39;49;00m$
   321	        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   322	        [32mevaluate:[39;49;00m (([04m[32mExclusiveWeakMessageSend[39;49;00m$
   323			[32mreceiver:[39;49;00m [31manObject[39;49;00m$
   324			[32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
   325			[32marguments:[39;49;00m [31manArgArray[39;49;00m)$
   326				[32mbasicExecuting:[39;49;00m [31maValueHolder[39;49;00m)[34m! ![39;49;00m$
   327	$
   328	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/24/2006 11:50'![39;49;00m$
   329	[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   330	[32msendOnce:[39;49;00m [31maMessageSelector[39;49;00m$
   331	[32mto:[39;49;00m [31manObject[39;49;00m$
   332	 $
   333	    [36mself[39;49;00m$
   334	        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   335	        [32mevaluate:[39;49;00m ([04m[32mNonReentrantWeakMessageSend[39;49;00m$
   336	            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
   337	            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m)[34m! ![39;49;00m$
   338	$
   339	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/24/2006 11:49'![39;49;00m$
   340	[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   341	[32msendOnce:[39;49;00m [31maMessageSelector[39;49;00m$
   342	[32mto:[39;49;00m [31manObject[39;49;00m$
   343	[32mwith:[39;49;00m [31manArg[39;49;00m$
   344	 $
   345	    [36mself[39;49;00m$
   346	        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   347	        [32mevaluate:[39;49;00m ([04m[32mNonReentrantWeakMessageSend[39;49;00m$
   348	            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
   349	            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
   350			[32marguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manArg[39;49;00m))[34m! ![39;49;00m$
   351	$
   352	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/24/2006 11:49'![39;49;00m$
   353	[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   354	[32msendOnce:[39;49;00m [31maMessageSelector[39;49;00m$
   355	[32mto:[39;49;00m [31manObject[39;49;00m$
   356	[32mwithArguments:[39;49;00m [31manArgArray[39;49;00m$
   357	 $
   358	    [36mself[39;49;00m$
   359	        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   360	        [32mevaluate:[39;49;00m ([04m[32mNonReentrantWeakMessageSend[39;49;00m$
   361	            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
   362	            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
   363			[32marguments:[39;49;00m [31manArgArray[39;49;00m)[34m! ![39;49;00m$
   364	$
   365	$
   366	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-Widgets'[39;49;00m[34m stamp: 'gvc 1/10/2007 11:41'![39;49;00m$
   367	[32mokToClose[39;49;00m$
   368		[37m"Sent to models when a window closing.[39;49;00m$
   369	[37m	Allows this check to be independent of okToChange."[39;49;00m$
   370		$
   371		^[36mtrue[39;49;00m[34m! ![39;49;00m$
   372	$
   373	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-Widgets'[39;49;00m[34m stamp: 'gvc 4/17/2007 17:41'![39;49;00m$
   374	[32mtaskbarIcon[39;49;00m$
   375		[37m"Answer the icon for the receiver in a task bar[39;49;00m$
   376	[37m	or nil for the default."[39;49;00m$
   377	$
   378		^[36mself[39;49;00m [32mclass[39;49;00m [32mtaskbarIcon[39;49;00m[34m! ![39;49;00m$
   379	$
   380	$
   381	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-Widgets-override'[39;49;00m[34m stamp: 'gvc 9/4/2007 12:32'![39;49;00m$
   382	[32mwindowActiveOnFirstClick[39;49;00m$
   383		[37m"Return true if my window should be active on first click."[39;49;00m$
   384	$
   385		^[36mtrue[39;49;00m[34m! ![39;49;00m$
   386	$
   387	$
   388	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*SeasideAdaptersCompatibility'[39;49;00m[34m stamp: 'pmm 11/25/2007 14:17'![39;49;00m$
   389	[32mtoString[39;49;00m$
   390		^[36mself[39;49;00m[34m! ![39;49;00m$
   391	$
   392	$
   393	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Tools-Explorer'[39;49;00m[34m stamp: 'stephaneducasse 9/17/2005 21:52'![39;49;00m$
   394	[32mexploreAndYourself[39;49;00m$
   395		[37m"i.e. explore; yourself. Thisway i can peek w/o typing all the parentheses"[39;49;00m$
   396		[36mself[39;49;00m [32mexplore[39;49;00m. $
   397	     ^[36mself[39;49;00m[34m! ![39;49;00m$
   398	$
   399	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Tools-Explorer'[39;49;00m[34m stamp: 'stephaneducasse 9/17/2005 21:48'![39;49;00m$
   400	[32mexploreWithLabel:[39;49;00m [31mlabel[39;49;00m$
   401	$
   402		^ [04m[32mObjectExplorer[39;49;00m [36mnew[39;49;00m [32mopenExplorerFor:[39;49;00m [36mself[39;49;00m [32mwithLabel:[39;49;00m$
   403	[31mlabel[39;49;00m[34m! ![39;49;00m$
   404	$
   405	$
   406	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*kernel-extensions-flagging'[39;49;00m[34m stamp: 'mtf 1/26/2008 23:34'![39;49;00m$
   407	[32mdeprecated[39;49;00m$
   408		[37m"Warn that the sending method has been deprecated."[39;49;00m$
   409	$
   410		[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
   411			[[04m[32mDeprecation[39;49;00m [32msignal:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m' has been deprecated.'[39;49;00m][34m! ![39;49;00m$
   412	$
   413	$
   414	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*kernel-extensions-flexibility'[39;49;00m[34m stamp: 'kph 1/27/2008 19:21'![39;49;00m$
   415	[32maskFor:[39;49;00m [31mselector[39;49;00m $
   416	$
   417	    [37m"returns true or false"[39;49;00m$
   418		$
   419		^ ([36mself[39;49;00m [32maskFor:[39;49;00m [31mselector[39;49;00m [32mifAbsent:[39;49;00m [36mnil[39;49;00m) [32m==[39;49;00m [36mtrue[39;49;00m[34m! ![39;49;00m$
   420	$
   421	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*kernel-extensions-flexibility'[39;49;00m[34m stamp: 'kph 10/17/2007 14:01'![39;49;00m$
   422	[32maskFor:[39;49;00m [31mselector[39;49;00m [32mifAbsent:[39;49;00m [31maBlock[39;49;00m$
   423	$
   424	   [37m"enables a default value to be specified in order to be tolerant of potentially missing methods[39;49;00m$
   425	[37m	[39;49;00m$
   426	[37m	e.g.[39;49;00m$
   427	[37m	(myPoint askFor: #originOffset) ifAbsent: [ 0@0 ].[39;49;00m$
   428	[37m	"[39;49;00m$
   429	$
   430		^ ([36mself[39;49;00m [32mclass[39;49;00m [32mcanUnderstand:[39;49;00m [31mselector[39;49;00m) [36mifFalse:[39;49;00m [ [31maBlock[39;49;00m [32mvalue[39;49;00m ] [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m][34m! ![39;49;00m$
   431	$
   432	$
   433	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*kernel-extensions-logging'[39;49;00m[34m stamp: 'mtf 1/26/2008 23:52'![39;49;00m$
   434	[32mlog[39;49;00m$
   435		[37m"This method provides the univeral entry point fo all logging mechanisms"[39;49;00m$
   436		$
   437		[37m"Options:[39;49;00m$
   438	[37m	1. Null for null logging[39;49;00m$
   439	[37m	2. A LogRouter instance wih a FrameworkAdaptor.[39;49;00m$
   440	[37m	3. CurrentLog a process local variable supplying a LogRouter"[39;49;00m$
   441		$
   442		^ ([04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#CurrentLog[39;49;00m [32mifAbsent:[39;49;00m [ [04m[32mNull[39;49;00m [32mdefault[39;49;00m ]) [32mvalue[39;49;00m$
   443			[32msender:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m; [32mbeginEntry[39;49;00m; [32myourself[39;49;00m[34m! ![39;49;00m$
   444	$
   445	$
   446	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-accessing'[39;49;00m[34m stamp: 'lr 3/9/2006 11:31'![39;49;00m$
   447	[32mdescription[39;49;00m$
   448		[37m"Return the description of the reciever. Subclasses might override this message to return instance-based descriptions."[39;49;00m$
   449	$
   450		^ [36mself[39;49;00m [32mclass[39;49;00m [32mdescription[39;49;00m[34m! ![39;49;00m$
   451	$
   452	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-accessing'[39;49;00m[34m stamp: 'lr 3/9/2006 11:31'![39;49;00m$
   453	[32mmementoClass[39;49;00m$
   454		[37m"Return a class to be used to remember or cache the receiver, namely a memento object."[39;49;00m$
   455	$
   456		^ [04m[32mMACheckedMemento[39;49;00m[34m! ![39;49;00m$
   457	$
   458	$
   459	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-model'[39;49;00m[34m stamp: 'lr 3/9/2006 11:31'![39;49;00m$
   460	[32mreadUsing:[39;49;00m [31maDescription[39;49;00m$
   461		[37m"Dispatch the read-access to the receiver using the accessor of aDescription."[39;49;00m$
   462	$
   463		^ [31maDescription[39;49;00m [32maccessor[39;49;00m [32mread:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
   464	$
   465	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-model'[39;49;00m[34m stamp: 'lr 3/9/2006 11:31'![39;49;00m$
   466	[32mwrite:[39;49;00m [31manObject[39;49;00m [32musing:[39;49;00m [31maDescription[39;49;00m$
   467		[37m"Dispatch the write-access to the receiver of anObject using the accessor of aDescription."[39;49;00m$
   468	$
   469		[31maDescription[39;49;00m [32maccessor[39;49;00m [32mwrite:[39;49;00m [31manObject[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
   470	$
   471	$
   472	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-testing'[39;49;00m[34m stamp: 'lr 3/9/2006 11:31'![39;49;00m$
   473	[32misDescription[39;49;00m$
   474		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
   475	$
   476	$
   477	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-morph-converting'[39;49;00m[34m stamp: 'lr 3/9/2006 11:33'![39;49;00m$
   478	[32masMorph[39;49;00m$
   479		^ [36mself[39;49;00m [32mdescription[39;49;00m [32masMorphOn:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
   480	$
   481	$
   482	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-seaside-converting'[39;49;00m[34m stamp: 'lr 3/9/2006 11:33'![39;49;00m$
   483	[32masComponent[39;49;00m$
   484		^ [36mself[39;49;00m [32mdescription[39;49;00m [32masComponentOn:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
   485	$
   486	$
   487	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*monticello'[39;49;00m[34m stamp: 'dvf 8/10/2004 23:25'![39;49;00m$
   488	[32misConflict[39;49;00m$
   489		^[36mfalse[39;49;00m[34m! ![39;49;00m$
   490	$
   491	$
   492	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*null'[39;49;00m[34m stamp: 'kph 9/6/2007 23:31'![39;49;00m$
   493	[32mifNull:[39;49;00m [31maBlock[39;49;00m$
   494	$
   495		^ [36mself[39;49;00m[34m! ![39;49;00m$
   496	$
   497	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*null'[39;49;00m[34m stamp: 'kph 9/6/2007 23:33'![39;49;00m$
   498	[32misNull[39;49;00m$
   499	$
   500		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
   501	$
   502	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*null'[39;49;00m[34m stamp: 'kph 4/12/2007 08:27'![39;49;00m$
   503	[32morNull[39;49;00m$
   504	$
   505		^ [36mself[39;49;00m[34m! ![39;49;00m$
   506	$
   507	$
   508	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*ob-tools-inspector'[39;49;00m[34m stamp: 'lr 6/5/2008 11:07'![39;49;00m$
   509	[32mbasicInspectorNodes[39;49;00m$
   510		<[34minspector:[39;49;00m #'1' priority: 600>$
   511		$
   512		|[31m nodes [39;49;00m|$
   513		[31mnodes[39;49;00m := [04m[32mOrderedCollection[39;49;00m [32mnew:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32m+[39;49;00m [36mself[39;49;00m [32mbasicSize[39;49;00m [32m+[39;49;00m [34m5[39;49;00m.$
   514		[31mnodes[39;49;00m [32madd:[39;49;00m [36mself[39;49;00m [32mselfInspectorNode[39;49;00m.$
   515		[36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mwithIndexDo:[39;49;00m [ :[31mname[39;49;00m :[31mindex[39;49;00m |$
   516			[31mnodes[39;49;00m [32madd:[39;49;00m ([04m[32mOTNamedVariableNode[39;49;00m [32mon:[39;49;00m [36mself[39;49;00m [32mindex:[39;49;00m [31mindex[39;49;00m [32mname:[39;49;00m [31mname[39;49;00m) ].$
   517		[34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32mbasicSize[39;49;00m [32mdo:[39;49;00m [ :[31mindex[39;49;00m |$
   518			[31mnodes[39;49;00m [32madd:[39;49;00m ([04m[32mOTIndexedVariableNode[39;49;00m [32mon:[39;49;00m [36mself[39;49;00m [32mindex:[39;49;00m [31mindex[39;49;00m) ].$
   519		^ [31mnodes[39;49;00m[34m! ![39;49;00m$
   520	$
   521	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*ob-tools-inspector'[39;49;00m[34m stamp: 'lr 6/5/2008 11:07'![39;49;00m$
   522	[32mprotocolInspectorNodes[39;49;00m$
   523		<[34minspector:[39;49;00m #'#' priority: 800>$
   524	$
   525		^ [36mself[39;49;00m [32mclass[39;49;00m [32mallSelectors[39;49;00m [32masArray[39;49;00m [32msort[39;49;00m$
   526			[32mcollect:[39;49;00m [ :[31meach[39;49;00m | [04m[32mOTProtocolInspectorNode[39;49;00m [32mon:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [31meach[39;49;00m ][34m! ![39;49;00m$
   527	$
   528	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*ob-tools-inspector'[39;49;00m[34m stamp: 'lr 6/5/2008 09:58'![39;49;00m$
   529	[32mselfInspectorNode[39;49;00m$
   530		^ [04m[32mOTDerivedInspectorNode[39;49;00m [32mon:[39;49;00m [36mself[39;49;00m [32mlabel:[39;49;00m [33m'self'[39;49;00m [32mblock:[39;49;00m [ :[31mobj[39;49;00m | [31mobj[39;49;00m ][34m! ![39;49;00m$
   531	$
   532	$
   533	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*omnibrowser-converting'[39;49;00m[34m stamp: 'cwp 4/17/2006 12:16'![39;49;00m$
   534	[32masAnnouncement[39;49;00m$
   535		^ [36mself[39;49;00m[34m! ![39;49;00m$
   536	$
   537	$
   538	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*pier-model'[39;49;00m[34m stamp: 'lr 3/9/2006 11:29'![39;49;00m$
   539	[32maccept:[39;49;00m [31maVisitor[39;49;00m$
   540		[36mself[39;49;00m [32msubclassResponsibility[39;49;00m[34m! ![39;49;00m$
   541	$
   542	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*pier-model'[39;49;00m[34m stamp: 'lr 3/9/2006 11:29'![39;49;00m$
   543	[32macceptDecorated:[39;49;00m [31maVisitor[39;49;00m$
   544		[36mself[39;49;00m [32maccept:[39;49;00m [31maVisitor[39;49;00m[34m! ![39;49;00m$
   545	$
   546	$
   547	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*rio-kernel'[39;49;00m[34m stamp: 'kph 3/8/2007 21:25'![39;49;00m$
   548	[32misRio[39;49;00m$
   549	$
   550		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
   551	$
   552	$
   553	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*scriptaculous'[39;49;00m[34m stamp: 'lr 1/4/2007 17:20'![39;49;00m$
   554	[32masFunction[39;49;00m$
   555		^ [36mself[39;49;00m [32masFunction:[39;49;00m [33m#([39;49;00m[33m)[39;49;00m[34m! ![39;49;00m$
   556	$
   557	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*scriptaculous'[39;49;00m[34m stamp: 'lr 1/4/2007 17:21'![39;49;00m$
   558	[32masFunction:[39;49;00m [31maCollection[39;49;00m$
   559		^ [04m[32mSUFunction[39;49;00m [36mnew[39;49;00m [32madd:[39;49;00m [36mself[39;49;00m; [32marguments:[39;49;00m [31maCollection[39;49;00m[34m! ![39;49;00m$
   560	$
   561	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*scriptaculous'[39;49;00m[34m stamp: 'lr 4/11/2006 19:49'![39;49;00m$
   562	[32masJavascript[39;49;00m$
   563		^ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [ :[31mstream[39;49;00m | [36mself[39;49;00m [32mjavascriptOn:[39;49;00m [31mstream[39;49;00m ][34m! ![39;49;00m$
   564	$
   565	$
   566	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*scriptaculous-printing'[39;49;00m[34m stamp: 'lr 4/20/2006 21:10'![39;49;00m$
   567	[32mjavascriptOn:[39;49;00m [31maStream[39;49;00m$
   568		[36mself[39;49;00m [32mprintOn:[39;49;00m [31maStream[39;49;00m[34m! ![39;49;00m$
   569	$
   570	$
   571	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'lr 6/5/2007 21:35'![39;49;00m$
   572	[32mdeprecatedApi[39;49;00m$
   573		[36mself[39;49;00m [32mdeprecatedApi:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mdisplayString[39;49;00m[34m! ![39;49;00m$
   574	$
   575	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'lr 6/5/2007 21:35'![39;49;00m$
   576	[32mdeprecatedApi:[39;49;00m [31maString[39;49;00m$
   577		[04m[32mWADeprecatedApi[39;49;00m [32mraiseSignal:[39;49;00m [31maString[39;49;00m[34m! ![39;49;00m$
   578	$
   579	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'lr 5/9/2007 08:47'![39;49;00m$
   580	[32minspectorFields[39;49;00m$
   581		|[31m members [39;49;00m|$
   582		[31mmembers[39;49;00m := [04m[32mArray[39;49;00m [36mnew[39;49;00m [32mwriteStream[39;49;00m.$
   583		[36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mwithIndexDo:[39;49;00m [ :[31meach[39;49;00m :[31mindex[39;49;00m |$
   584			[31mmembers[39;49;00m [32mnextPut:[39;49;00m [31meach[39;49;00m [32m->[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m) ].$
   585		[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m [36mifTrue:[39;49;00m [$
   586			[34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32msize[39;49;00m [32mdo:[39;49;00m [ :[31mindex[39;49;00m |$
   587				[31mmembers[39;49;00m [32mnextPut:[39;49;00m [31mindex[39;49;00m [32m->[39;49;00m ([36mself[39;49;00m [32mat:[39;49;00m [31mindex[39;49;00m) ] ].$
   588		^ [31mmembers[39;49;00m [32mcontents[39;49;00m[34m! ![39;49;00m$
   589	$
   590	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'avi 3/14/2005 15:19'![39;49;00m$
   591	[32mlabelForSelector:[39;49;00m [31maSymbol[39;49;00m$
   592		^ [31maSymbol[39;49;00m [32masCapitalizedPhrase[39;49;00m[34m! ![39;49;00m$
   593	$
   594	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'pmm 4/7/2007 17:14'![39;49;00m$
   595	[32mrenderOn:[39;49;00m [31maRenderer[39;49;00m$
   596		[37m"Override this method to customize how objects (not components) are rendered when passed as an argument to #render:. The default is the return value of #displayString.[39;49;00m$
   597	[37m	Just remember that you can not use #callback:, #on:of:, or #call:"[39;49;00m$
   598	$
   599		[31maRenderer[39;49;00m [32mtext:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
   600	$
   601	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'lr 3/19/2007 23:13'![39;49;00m$
   602	[32mrestoreFromSnapshot:[39;49;00m [31manObject[39;49;00m$
   603		[36mself[39;49;00m [32mcopyFrom:[39;49;00m [31manObject[39;49;00m[34m! ![39;49;00m$
   604	$
   605	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'avi 9/1/2004 21:20'![39;49;00m$
   606	[32msnapshotCopy[39;49;00m$
   607		^ [36mself[39;49;00m [32mshallowCopy[39;49;00m[34m! ![39;49;00m$
   608	$
   609	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'lr 10/28/2007 14:42'![39;49;00m$
   610	[32mvalidationError:[39;49;00m [31mmessage[39;49;00m$
   611		^[04m[32mWAValidationNotification[39;49;00m [32mraiseSignal:[39;49;00m [31mmessage[39;49;00m[34m! ![39;49;00m$
   612	$
   613	$
   614	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2-encoding'[39;49;00m[34m stamp: 'lr 3/26/2007 20:16'![39;49;00m$
   615	[32mencodeOn:[39;49;00m [31maDocument[39;49;00m$
   616		[31maDocument[39;49;00m [32mprint:[39;49;00m [36mself[39;49;00m [32mdisplayString[39;49;00m[34m! ![39;49;00m$
   617	$
   618	$
   619	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2-squeak'[39;49;00m[34m stamp: 'pmm 5/22/2007 22:10'![39;49;00m$
   620	[32mbeMutable[39;49;00m$
   621		[37m"for VW compatibility, a hack that allows to cache a value in a literal array"[39;49;00m[34m! ![39;49;00m$
   622	$
   623	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2-squeak'[39;49;00m[34m stamp: 'lr 7/12/2005 17:01'![39;49;00m$
   624	[32mdisplayString[39;49;00m$
   625		^ [36mself[39;49;00m [32masString[39;49;00m[34m! ![39;49;00m$
   626	$
   627	$
   628	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*services-base'[39;49;00m[34m stamp: 'rr 3/21/2006 11:54'![39;49;00m$
   629	[32mrequestor[39;49;00m$
   630		[37m"returns the focused window's requestor"[39;49;00m$
   631	$
   632		[37m"SystemWindow focusedWindow ifNotNilDo: [:w | ^ w requestor]."[39;49;00m$
   633	$
   634		[37m"triggers an infinite loop"[39;49;00m$
   635	$
   636		^ [04m[32mRequestor[39;49;00m [32mdefault[39;49;00m[34m! ![39;49;00m$
   637	$
   638	$
   639	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*system-support'[39;49;00m[34m stamp: 'dvf 8/23/2003 12:27'![39;49;00m$
   640	[32msystemNavigation[39;49;00m$
   641	$
   642		^ [04m[32mSystemNavigation[39;49;00m [32mdefault[39;49;00m[34m! ![39;49;00m$
   643	$
   644	$
   645	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*tools-browser'[39;49;00m[34m stamp: 'mu 3/6/2004 15:13'![39;49;00m$
   646	[32mbrowse[39;49;00m$
   647		[36mself[39;49;00m [32msystemNavigation[39;49;00m [32mbrowseClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m[34m! ![39;49;00m$
   648	$
   649	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*tools-browser'[39;49;00m[34m stamp: 'mu 3/11/2004 16:00'![39;49;00m$
   650	[32mbrowseHierarchy[39;49;00m$
   651		[36mself[39;49;00m [32msystemNavigation[39;49;00m [32mbrowseHierarchy:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m[34m! ![39;49;00m$
   652	$
   653	$
   654	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*universes'[39;49;00m[34m stamp: 'ls 11/26/2006 12:33'![39;49;00m$
   655	[32misUPackage[39;49;00m$
   656		^[36mfalse[39;49;00m[34m! ![39;49;00m$
   657	$
   658	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*universes'[39;49;00m[34m stamp: 'ls 11/26/2006 12:33'![39;49;00m$
   659	[32misUPackageCategory[39;49;00m$
   660		^[36mfalse[39;49;00m[34m! ![39;49;00m$
   661	$
   662	$
   663	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'sw 4/30/1998 12:18'![39;49;00m$
   664	[32maddInstanceVarNamed:[39;49;00m [31maName[39;49;00m [32mwithValue:[39;49;00m [31maValue[39;49;00m$
   665		[37m"Add an instance variable named aName and give it value aValue"[39;49;00m$
   666		[36mself[39;49;00m [32mclass[39;49;00m [32maddInstVarName:[39;49;00m [31maName[39;49;00m [32masString[39;49;00m.$
   667		[36mself[39;49;00m [32minstVarAt:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mput:[39;49;00m [31maValue[39;49;00m[34m! ![39;49;00m$
   668	$
   669	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'yo 6/29/2004 11:39'![39;49;00m$
   670	[32mat:[39;49;00m [31mindex[39;49;00m $
   671		[37m"Primitive. Assumes receiver is indexable. Answer the value of an [39;49;00m$
   672	[37m	indexable element in the receiver. Fail if the argument index is not an [39;49;00m$
   673	[37m	Integer or is out of bounds. Essential. See Object documentation [39;49;00m$
   674	[37m	whatIsAPrimitive."[39;49;00m$
   675	$
   676		<[34mprimitive:[39;49;00m 60>$
   677		[31mindex[39;49;00m [32misInteger[39;49;00m [36mifTrue:[39;49;00m$
   678			[[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m$
   679				[36mifTrue:[39;49;00m [[36mself[39;49;00m [32merrorSubscriptBounds:[39;49;00m [31mindex[39;49;00m]$
   680				[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNotIndexable[39;49;00m]].$
   681		[31mindex[39;49;00m [32misNumber[39;49;00m$
   682			[36mifTrue:[39;49;00m [^[36mself[39;49;00m [32mat:[39;49;00m [31mindex[39;49;00m [32masInteger[39;49;00m]$
   683			[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNonIntegerIndex[39;49;00m][34m! ![39;49;00m$
   684	$
   685	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
   686	[32mat:[39;49;00m [31mindex[39;49;00m [32mmodify:[39;49;00m [31maBlock[39;49;00m$
   687		[37m"Replace the element of the collection with itself transformed by the block"[39;49;00m$
   688		^ [36mself[39;49;00m [32mat:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([31maBlock[39;49;00m [32mvalue:[39;49;00m ([36mself[39;49;00m [32mat:[39;49;00m [31mindex[39;49;00m))[34m! ![39;49;00m$
   689	$
   690	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'yo 6/29/2004 13:08'![39;49;00m$
   691	[32mat:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m [31mvalue[39;49;00m $
   692		[37m"Primitive. Assumes receiver is indexable. Store the argument value in [39;49;00m$
   693	[37m	the indexable element of the receiver indicated by index. Fail if the [39;49;00m$
   694	[37m	index is not an Integer or is out of bounds. Or fail if the value is not of [39;49;00m$
   695	[37m	the right type for this kind of collection. Answer the value that was [39;49;00m$
   696	[37m	stored. Essential. See Object documentation whatIsAPrimitive."[39;49;00m$
   697	$
   698		<[34mprimitive:[39;49;00m 61>$
   699		[31mindex[39;49;00m [32misInteger[39;49;00m [36mifTrue:[39;49;00m$
   700			[[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m$
   701				[36mifTrue:[39;49;00m [([31mindex[39;49;00m [32m>=[39;49;00m [34m1[39;49;00m [32mand:[39;49;00m [[31mindex[39;49;00m [32m<=[39;49;00m [36mself[39;49;00m [32msize[39;49;00m])$
   702						[36mifTrue:[39;49;00m [[36mself[39;49;00m [32merrorImproperStore[39;49;00m]$
   703						[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorSubscriptBounds:[39;49;00m [31mindex[39;49;00m]]$
   704				[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNotIndexable[39;49;00m]].$
   705		[31mindex[39;49;00m [32misNumber[39;49;00m$
   706			[36mifTrue:[39;49;00m [^[36mself[39;49;00m [32mat:[39;49;00m [31mindex[39;49;00m [32masInteger[39;49;00m [32mput:[39;49;00m [31mvalue[39;49;00m]$
   707			[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNonIntegerIndex[39;49;00m][34m! ![39;49;00m$
   708	$
   709	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'yo 9/20/2004 10:22'![39;49;00m$
   710	[32mbasicAddInstanceVarNamed:[39;49;00m [31maName[39;49;00m [32mwithValue:[39;49;00m [31maValue[39;49;00m$
   711		[37m"Add an instance variable named aName and give it value aValue"[39;49;00m$
   712		[36mself[39;49;00m [32mclass[39;49;00m [32maddInstVarName:[39;49;00m [31maName[39;49;00m [32masString[39;49;00m.$
   713		[36mself[39;49;00m [32minstVarAt:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mput:[39;49;00m [31maValue[39;49;00m[34m! ![39;49;00m$
   714	$
   715	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
   716	[32mbasicAt:[39;49;00m [31mindex[39;49;00m $
   717		[37m"Primitive. Assumes receiver is indexable. Answer the value of an [39;49;00m$
   718	[37m	indexable element in the receiver. Fail if the argument index is not an [39;49;00m$
   719	[37m	Integer or is out of bounds. Essential. Do not override in a subclass. See [39;49;00m$
   720	[37m	Object documentation whatIsAPrimitive."[39;49;00m$
   721	$
   722		<[34mprimitive:[39;49;00m 60>$
   723		[31mindex[39;49;00m [32misInteger[39;49;00m [36mifTrue:[39;49;00m [[36mself[39;49;00m [32merrorSubscriptBounds:[39;49;00m [31mindex[39;49;00m].$
   724		[31mindex[39;49;00m [32misNumber[39;49;00m$
   725			[36mifTrue:[39;49;00m [^[36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32masInteger[39;49;00m]$
   726			[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNonIntegerIndex[39;49;00m][34m! ![39;49;00m$
   727	$
   728	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
   729	[32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m [31mvalue[39;49;00m $
   730		[37m"Primitive. Assumes receiver is indexable. Store the second argument [39;49;00m$
   731	[37m	value in the indexable element of the receiver indicated by index. Fail [39;49;00m$
   732	[37m	if the index is not an Integer or is out of bounds. Or fail if the value is [39;49;00m$
   733	[37m	not of the right type for this kind of collection. Answer the value that [39;49;00m$
   734	[37m	was stored. Essential. Do not override in a subclass. See Object [39;49;00m$
   735	[37m	documentation whatIsAPrimitive."[39;49;00m$
   736	$
   737		<[34mprimitive:[39;49;00m 61>$
   738		[31mindex[39;49;00m [32misInteger[39;49;00m$
   739			[36mifTrue:[39;49;00m [([31mindex[39;49;00m [32m>=[39;49;00m [34m1[39;49;00m [32mand:[39;49;00m [[31mindex[39;49;00m [32m<=[39;49;00m [36mself[39;49;00m [32msize[39;49;00m])$
   740						[36mifTrue:[39;49;00m [[36mself[39;49;00m [32merrorImproperStore[39;49;00m]$
   741						[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorSubscriptBounds:[39;49;00m [31mindex[39;49;00m]].$
   742		[31mindex[39;49;00m [32misNumber[39;49;00m$
   743			[36mifTrue:[39;49;00m [^[36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32masInteger[39;49;00m [32mput:[39;49;00m [31mvalue[39;49;00m]$
   744			[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNonIntegerIndex[39;49;00m][34m! ![39;49;00m$
   745	$
   746	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
   747	[32mbasicSize[39;49;00m$
   748		[37m"Primitive. Answer the number of indexable variables in the receiver. [39;49;00m$
   749	[37m	This value is the same as the largest legal subscript. Essential. Do not [39;49;00m$
   750	[37m	override in any subclass. See Object documentation whatIsAPrimitive."[39;49;00m$
   751	$
   752		<[34mprimitive:[39;49;00m 62>$
   753		[37m"The number of indexable fields of fixed-length objects is 0"[39;49;00m$
   754		^[34m0[39;49;00m	[34m! ![39;49;00m$
   755	$
   756	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
   757	[32mbindWithTemp:[39;49;00m [31maBlock[39;49;00m$
   758		^ [31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m [32mvalue:[39;49;00m [36mnil[39;49;00m[34m! ![39;49;00m$
   759	$
   760	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'md 10/7/2004 15:43'![39;49;00m$
   761	[32mifNil:[39;49;00m [31mnilBlock[39;49;00m [32mifNotNilDo:[39;49;00m [31maBlock[39;49;00m $
   762		[37m"Evaluate aBlock with the receiver as its argument."[39;49;00m$
   763	$
   764		^ [31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m$
   765	[34m! ![39;49;00m$
   766	$
   767	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'di 11/8/2000 21:04'![39;49;00m$
   768	[32mifNotNilDo:[39;49;00m [31maBlock[39;49;00m$
   769		[37m"Evaluate the given block with the receiver as its argument."[39;49;00m$
   770	$
   771		^ [31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m$
   772	[34m! ![39;49;00m$
   773	$
   774	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'md 10/7/2004 15:43'![39;49;00m$
   775	[32mifNotNilDo:[39;49;00m [31maBlock[39;49;00m [32mifNil:[39;49;00m [31mnilBlock[39;49;00m$
   776		[37m"Evaluate aBlock with the receiver as its argument."[39;49;00m$
   777	$
   778		^ [31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m$
   779	[34m! ![39;49;00m$
   780	$
   781	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'ajh 1/21/2003 12:59'![39;49;00m$
   782	[32min:[39;49;00m [31maBlock[39;49;00m$
   783		[37m"Evaluate the given block with the receiver as its argument."[39;49;00m$
   784	$
   785		^ [31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m$
   786	[34m! ![39;49;00m$
   787	$
   788	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'sw 10/17/2000 11:15'![39;49;00m$
   789	[32mpresenter[39;49;00m$
   790		[37m"Answer the presenter object associated with the receiver.  For morphs, there is in effect a clear containment hierarchy of presenters (accessed via their association with PasteUpMorphs); for arbitrary objects the hook is simply via the current world, at least at present."[39;49;00m$
   791	$
   792		^ [36mself[39;49;00m [32mcurrentWorld[39;49;00m [32mpresenter[39;49;00m[34m! ![39;49;00m$
   793	$
   794	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
   795	[32mreadFromString:[39;49;00m [31maString[39;49;00m$
   796		[37m"Create an object based on the contents of aString."[39;49;00m$
   797	$
   798		^[36mself[39;49;00m [32mreadFrom:[39;49;00m ([04m[32mReadStream[39;49;00m [32mon:[39;49;00m [31maString[39;49;00m)[34m! ![39;49;00m$
   799	$
   800	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'di 3/29/1999 13:10'![39;49;00m$
   801	[32msize[39;49;00m$
   802		[37m"Primitive. Answer the number of indexable variables in the receiver. [39;49;00m$
   803	[37m	This value is the same as the largest legal subscript. Essential. See Object [39;49;00m$
   804	[37m	documentation whatIsAPrimitive."[39;49;00m$
   805	$
   806		<[34mprimitive:[39;49;00m 62>$
   807		[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m [36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNotIndexable[39;49;00m].$
   808		^ [34m0[39;49;00m[34m! ![39;49;00m$
   809	$
   810	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'md 5/16/2006 12:34'![39;49;00m$
   811	[32myourself[39;49;00m$
   812		[37m"Answer self."[39;49;00m$
   813		^[36mself[39;49;00m[34m! ![39;49;00m$
   814	$
   815	$
   816	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'associating'[39;49;00m[34m stamp: 'md 7/22/2005 16:03'![39;49;00m$
   817	[32m->[39;49;00m [31manObject[39;49;00m$
   818		[37m"Answer an Association between self and anObject"[39;49;00m$
   819	$
   820		^[04m[32mAssociation[39;49;00m [32mbasicNew[39;49;00m [32mkey:[39;49;00m [36mself[39;49;00m [32mvalue:[39;49;00m [31manObject[39;49;00m[34m! ![39;49;00m$
   821	$
   822	$
   823	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'binding'[39;49;00m[34m![39;49;00m$
   824	[32mbindingOf:[39;49;00m [31maString[39;49;00m$
   825		^[36mnil[39;49;00m[34m! ![39;49;00m$
   826	$
   827	$
   828	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'breakpoint'[39;49;00m[34m stamp: 'bkv 7/1/2003 12:33'![39;49;00m$
   829	[32mbreak[39;49;00m$
   830		[37m"This is a simple message to use for inserting breakpoints during debugging.[39;49;00m$
   831	[37m	The debugger is opened by sending a signal. This gives a chance to restore[39;49;00m$
   832	[37m	invariants related to multiple processes."[39;49;00m$
   833	$
   834		[04m[32mBreakPoint[39;49;00m [32msignal[39;49;00m.$
   835	$
   836		[37m"nil break."[39;49;00m[34m! ![39;49;00m$
   837	$
   838	$
   839	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'casing'[39;49;00m[34m![39;49;00m$
   840	[32mcaseOf:[39;49;00m [31maBlockAssociationCollection[39;49;00m$
   841		[37m"The elements of aBlockAssociationCollection are associations between blocks.[39;49;00m$
   842	[37m	 Answer the evaluated value of the first association in aBlockAssociationCollection[39;49;00m$
   843	[37m	 whose evaluated key equals the receiver.  If no match is found, report an error."[39;49;00m$
   844	$
   845		^ [36mself[39;49;00m [32mcaseOf:[39;49;00m [31maBlockAssociationCollection[39;49;00m [32motherwise:[39;49;00m [[36mself[39;49;00m [32mcaseError[39;49;00m]$
   846	$
   847	[37m"| z | z _ {[#a]->[1+1]. ['b' asSymbol]->[2+2]. [#c]->[3+3]}. #b caseOf: z"[39;49;00m$
   848	[37m"| z | z _ {[#a]->[1+1]. ['d' asSymbol]->[2+2]. [#c]->[3+3]}. #b caseOf: z"[39;49;00m$
   849	[37m"The following are compiled in-line:"[39;49;00m$
   850	[37m"#b caseOf: {[#a]->[1+1]. ['b' asSymbol]->[2+2]. [#c]->[3+3]}"[39;49;00m$
   851	[37m"#b caseOf: {[#a]->[1+1]. ['d' asSymbol]->[2+2]. [#c]->[3+3]}"[39;49;00m[34m! ![39;49;00m$
   852	$
   853	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'casing'[39;49;00m[34m![39;49;00m$
   854	[32mcaseOf:[39;49;00m [31maBlockAssociationCollection[39;49;00m [32motherwise:[39;49;00m [31maBlock[39;49;00m$
   855		[37m"The elements of aBlockAssociationCollection are associations between blocks.[39;49;00m$
   856	[37m	 Answer the evaluated value of the first association in aBlockAssociationCollection[39;49;00m$
   857	[37m	 whose evaluated key equals the receiver.  If no match is found, answer the result[39;49;00m$
   858	[37m	 of evaluating aBlock."[39;49;00m$
   859	$
   860		[31maBlockAssociationCollection[39;49;00m [32massociationsDo:[39;49;00m$
   861			[:[31massoc[39;49;00m | ([31massoc[39;49;00m [32mkey[39;49;00m [32mvalue[39;49;00m [32m=[39;49;00m [36mself[39;49;00m) [36mifTrue:[39;49;00m [^[31massoc[39;49;00m [32mvalue[39;49;00m [32mvalue[39;49;00m]].$
   862		^ [31maBlock[39;49;00m [32mvalue[39;49;00m$
   863	$
   864	[37m"| z | z _ {[#a]->[1+1]. ['b' asSymbol]->[2+2]. [#c]->[3+3]}. #b caseOf: z otherwise: [0]"[39;49;00m$
   865	[37m"| z | z _ {[#a]->[1+1]. ['d' asSymbol]->[2+2]. [#c]->[3+3]}. #b caseOf: z otherwise: [0]"[39;49;00m$
   866	[37m"The following are compiled in-line:"[39;49;00m$
   867	[37m"#b caseOf: {[#a]->[1+1]. ['b' asSymbol]->[2+2]. [#c]->[3+3]} otherwise: [0]"[39;49;00m$
   868	[37m"#b caseOf: {[#a]->[1+1]. ['d' asSymbol]->[2+2]. [#c]->[3+3]} otherwise: [0]"[39;49;00m[34m! ![39;49;00m$
   869	$
   870	$
   871	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m![39;49;00m$
   872	[32mclass[39;49;00m$
   873		[37m"Primitive. Answer the object which is the receiver's class. Essential. See [39;49;00m$
   874	[37m	Object documentation whatIsAPrimitive."[39;49;00m$
   875	$
   876		<[34mprimitive:[39;49;00m 111>$
   877		[36mself[39;49;00m [32mprimitiveFailed[39;49;00m[34m! ![39;49;00m$
   878	$
   879	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m stamp: 'sw 9/27/2001 15:51'![39;49;00m$
   880	[32minheritsFromAnyIn:[39;49;00m [31maList[39;49;00m$
   881		[37m"Answer whether the receiver inherits from any class represented by any element in the list.  The elements of the list can be classes, class name symbols, or strings representing possible class names.  This allows speculative membership tests to be made even when some of the classes may not be known to the current image, and even when their names are not interned symbols."[39;49;00m$
   882	$
   883		|[31m aClass [39;49;00m|$
   884		[31maList[39;49;00m [32mdo:[39;49;00m$
   885			[:[31melem[39;49;00m | [04m[32mSymbol[39;49;00m [32mhasInterned:[39;49;00m [31melem[39;49;00m [32masString[39;49;00m [36mifTrue:[39;49;00m $
   886				[:[31melemSymbol[39;49;00m | ((([31maClass[39;49;00m _ [04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [31melemSymbol[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m]) [32misKindOf:[39;49;00m [04m[32mClass[39;49;00m)$
   887							[32mand:[39;49;00m [[36mself[39;49;00m [32misKindOf:[39;49;00m [31maClass[39;49;00m])$
   888					[36mifTrue:[39;49;00m$
   889						[^ [36mtrue[39;49;00m]]].$
   890		^ [36mfalse[39;49;00m$
   891	$
   892	$
   893	[37m"[39;49;00m$
   894	[37m{3.  true. 'olive'} do:[39;49;00m$
   895	[37m	[:token |[39;49;00m$
   896	[37m		 {{#Number. #Boolean}. {Number.  Boolean }.  {'Number'. 'Boolean'}} do:[39;49;00m$
   897	[37m			[:list |[39;49;00m$
   898	[37m				Transcript cr; show: token asString, ' list element provided as a ', list first class name, ' - ', (token inheritsFromAnyIn: list) asString]][39;49;00m$
   899	[37m"[39;49;00m[34m! ![39;49;00m$
   900	$
   901	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m![39;49;00m$
   902	[32misKindOf:[39;49;00m [31maClass[39;49;00m $
   903		[37m"Answer whether the class, aClass, is a superclass or class of the receiver."[39;49;00m$
   904	$
   905		[36mself[39;49;00m [32mclass[39;49;00m [32m==[39;49;00m [31maClass[39;49;00m$
   906			[36mifTrue:[39;49;00m [^[36mtrue[39;49;00m]$
   907			[36mifFalse:[39;49;00m [^[36mself[39;49;00m [32mclass[39;49;00m [32minheritsFrom:[39;49;00m [31maClass[39;49;00m][34m! ![39;49;00m$
   908	$
   909	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m stamp: 'sw 2/16/98 02:08'![39;49;00m$
   910	[32misKindOf:[39;49;00m [31maClass[39;49;00m [32morOf:[39;49;00m [31manotherClass[39;49;00m$
   911		[37m"Answer whether either of the classes, aClass or anotherClass,, is a superclass or class of the receiver.  A convenience; could be somewhat optimized"[39;49;00m$
   912		^ ([36mself[39;49;00m [32misKindOf:[39;49;00m [31maClass[39;49;00m) [32mor:[39;49;00m [[36mself[39;49;00m [32misKindOf:[39;49;00m [31manotherClass[39;49;00m][34m! ![39;49;00m$
   913	$
   914	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m![39;49;00m$
   915	[32misMemberOf:[39;49;00m [31maClass[39;49;00m $
   916		[37m"Answer whether the receiver is an instance of the class, aClass."[39;49;00m$
   917	$
   918		^[36mself[39;49;00m [32mclass[39;49;00m [32m==[39;49;00m [31maClass[39;49;00m[34m! ![39;49;00m$
   919	$
   920	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m![39;49;00m$
   921	[32mrespondsTo:[39;49;00m [31maSymbol[39;49;00m $
   922		[37m"Answer whether the method dictionary of the receiver's class contains [39;49;00m$
   923	[37m	aSymbol as a message selector."[39;49;00m$
   924	$
   925		^[36mself[39;49;00m [32mclass[39;49;00m [32mcanUnderstand:[39;49;00m [31maSymbol[39;49;00m[34m! ![39;49;00m$
   926	$
   927	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m stamp: 'tk 10/21/1998 12:38'![39;49;00m$
   928	[32mxxxClass[39;49;00m$
   929		[37m"For subclasses of nil, such as ObjectOut"[39;49;00m$
   930		^ [36mself[39;49;00m [32mclass[39;49;00m[34m! ![39;49;00m$
   931	$
   932	$
   933	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m stamp: 'tk 4/16/1999 18:26'![39;49;00m$
   934	[32mcloseTo:[39;49;00m [31manObject[39;49;00m$
   935		[37m"Answer whether the receiver and the argument represent the same[39;49;00m$
   936	[37m	object. If = is redefined in any subclass, consider also redefining the[39;49;00m$
   937	[37m	message hash."[39;49;00m$
   938	$
   939		|[31m ans [39;49;00m|$
   940		[[31mans[39;49;00m _ [36mself[39;49;00m [32m=[39;49;00m [31manObject[39;49;00m] [32mifError:[39;49;00m [:[31maString[39;49;00m :[31maReceiver[39;49;00m | ^ [36mfalse[39;49;00m].$
   941		^ [31mans[39;49;00m[34m! ![39;49;00m$
   942	$
   943	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m![39;49;00m$
   944	[32mhash[39;49;00m$
   945		[37m"Answer a SmallInteger whose value is related to the receiver's identity.[39;49;00m$
   946	[37m	May be overridden, and should be overridden in any classes that define = "[39;49;00m$
   947	$
   948		^ [36mself[39;49;00m [32midentityHash[39;49;00m[34m! ![39;49;00m$
   949	$
   950	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m stamp: 'pm 9/23/97 09:36'![39;49;00m$
   951	[32mhashMappedBy:[39;49;00m [31mmap[39;49;00m$
   952		[37m"Answer what my hash would be if oops changed according to map."[39;49;00m$
   953	$
   954		^[31mmap[39;49;00m [32mnewHashFor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
   955	$
   956	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m stamp: 'di 9/27/97 20:23'![39;49;00m$
   957	[32midentityHashMappedBy:[39;49;00m [31mmap[39;49;00m$
   958		[37m"Answer what my hash would be if oops changed according to map."[39;49;00m$
   959	$
   960		^[31mmap[39;49;00m [32mnewHashFor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
   961	$
   962	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m stamp: 'sw 8/20/1998 12:34'![39;49;00m$
   963	[32midentityHashPrintString[39;49;00m$
   964		[37m"'fred' identityHashPrintString"[39;49;00m$
   965	$
   966		^ [33m'('[39;49;00m[32m,[39;49;00m [36mself[39;49;00m [32midentityHash[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m')'[39;49;00m[34m! ![39;49;00m$
   967	$
   968	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m stamp: 'ajh 2/2/2002 15:02'![39;49;00m$
   969	[32mliteralEqual:[39;49;00m [31mother[39;49;00m$
   970	$
   971		^ [36mself[39;49;00m [32mclass[39;49;00m [32m==[39;49;00m [31mother[39;49;00m [32mclass[39;49;00m [32mand:[39;49;00m [[36mself[39;49;00m [32m=[39;49;00m [31mother[39;49;00m][34m! ![39;49;00m$
   972	$
   973	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m![39;49;00m$
   974	[32m=[39;49;00m [31manObject[39;49;00m $
   975		[37m"Answer whether the receiver and the argument represent the same [39;49;00m$
   976	[37m	object. If = is redefined in any subclass, consider also redefining the [39;49;00m$
   977	[37m	message hash."[39;49;00m$
   978	$
   979		^[36mself[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m[34m! ![39;49;00m$
   980	$
   981	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m![39;49;00m$
   982	[32m~=[39;49;00m [31manObject[39;49;00m $
   983		[37m"Answer whether the receiver and the argument do not represent the [39;49;00m$
   984	[37m	same object."[39;49;00m$
   985	$
   986		^[36mself[39;49;00m [32m=[39;49;00m [31manObject[39;49;00m [32m==[39;49;00m [36mfalse[39;49;00m[34m! ![39;49;00m$
   987	$
   988	$
   989	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'di 11/9/1998 12:15'![39;49;00m$
   990	[32madaptToFloat:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m$
   991		[37m"If no method has been provided for adapting an object to a Float,[39;49;00m$
   992	[37m	then it may be adequate to simply adapt it to a number."[39;49;00m$
   993		^ [36mself[39;49;00m [32madaptToNumber:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m[34m! ![39;49;00m$
   994	$
   995	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'di 11/9/1998 12:14'![39;49;00m$
   996	[32madaptToFraction:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m$
   997		[37m"If no method has been provided for adapting an object to a Fraction,[39;49;00m$
   998	[37m	then it may be adequate to simply adapt it to a number."[39;49;00m$
   999		^ [36mself[39;49;00m [32madaptToNumber:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m[34m! ![39;49;00m$
  1000	$
  1001	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'di 11/9/1998 12:15'![39;49;00m$
  1002	[32madaptToInteger:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m$
  1003		[37m"If no method has been provided for adapting an object to a Integer,[39;49;00m$
  1004	[37m	then it may be adequate to simply adapt it to a number."[39;49;00m$
  1005		^ [36mself[39;49;00m [32madaptToNumber:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m[34m! ![39;49;00m$
  1006	$
  1007	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'rw 4/27/2002 07:48'![39;49;00m$
  1008	[32masActionSequence[39;49;00m$
  1009	$
  1010		^[04m[32mWeakActionSequence[39;49;00m [32mwith:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  1011	$
  1012	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'rw 7/20/2003 16:03'![39;49;00m$
  1013	[32masActionSequenceTrappingErrors[39;49;00m$
  1014	$
  1015		^[04m[32mWeakActionSequenceTrappingErrors[39;49;00m [32mwith:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  1016	$
  1017	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'svp 5/16/2000 18:14'![39;49;00m$
  1018	[32masDraggableMorph[39;49;00m$
  1019		^([04m[32mStringMorph[39;49;00m [32mcontents:[39;49;00m [36mself[39;49;00m [32mprintString[39;49;00m)$
  1020			[32mcolor:[39;49;00m [04m[32mColor[39;49;00m [32mwhite[39;49;00m;$
  1021			[32myourself[39;49;00m[34m! ![39;49;00m$
  1022	$
  1023	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'sma 5/12/2000 17:39'![39;49;00m$
  1024	[32masOrderedCollection[39;49;00m$
  1025		[37m"Answer an OrderedCollection with the receiver as its only element."[39;49;00m$
  1026	$
  1027		^ [04m[32mOrderedCollection[39;49;00m [32mwith:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  1028	$
  1029	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m![39;49;00m$
  1030	[32masString[39;49;00m$
  1031		[37m"Answer a string that represents the receiver."[39;49;00m$
  1032	$
  1033		^ [36mself[39;49;00m [32mprintString[39;49;00m [34m! ![39;49;00m$
  1034	$
  1035	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'ajh 3/11/2003 10:27'![39;49;00m$
  1036	[32masStringOrText[39;49;00m$
  1037		[37m"Answer a string that represents the receiver."[39;49;00m$
  1038	$
  1039		^ [36mself[39;49;00m [32mprintString[39;49;00m [34m! ![39;49;00m$
  1040	$
  1041	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m![39;49;00m$
  1042	[32mas:[39;49;00m [31maSimilarClass[39;49;00m$
  1043		[37m"Create an object of class aSimilarClass that has similar contents to the receiver."[39;49;00m$
  1044	$
  1045		^ [31maSimilarClass[39;49;00m [32mnewFrom:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  1046	$
  1047	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'RAA 8/2/1999 12:41'![39;49;00m$
  1048	[32mcomplexContents[39;49;00m$
  1049	$
  1050		^[36mself[39;49;00m[34m! ![39;49;00m$
  1051	$
  1052	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'ajh 7/6/2003 20:37'![39;49;00m$
  1053	[32mmustBeBoolean[39;49;00m$
  1054		[37m"Catches attempts to test truth of non-Booleans.  This message is sent from the VM.  The sending context is rewound to just before the jump causing this exception."[39;49;00m$
  1055	$
  1056		^ [36mself[39;49;00m [32mmustBeBooleanIn:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m[34m! ![39;49;00m$
  1057	$
  1058	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'ajh 7/6/2003 20:40'![39;49;00m$
  1059	[32mmustBeBooleanIn:[39;49;00m [31mcontext[39;49;00m$
  1060		[37m"context is the where the non-boolean error occurred. Rewind context to before jump then raise error."[39;49;00m$
  1061	$
  1062		|[31m proceedValue [39;49;00m|$
  1063		[31mcontext[39;49;00m [32mskipBackBeforeJump[39;49;00m.$
  1064		[31mproceedValue[39;49;00m _ [04m[32mNonBooleanReceiver[39;49;00m [36mnew[39;49;00m$
  1065			[32mobject:[39;49;00m [36mself[39;49;00m;$
  1066			[32msignal:[39;49;00m [33m'proceed for truth.'[39;49;00m.$
  1067		^ [31mproceedValue[39;49;00m [32m~~[39;49;00m [36mfalse[39;49;00m[34m! ![39;49;00m$
  1068	$
  1069	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'sw 3/26/2001 12:12'![39;49;00m$
  1070	[32mprintDirectlyToDisplay[39;49;00m$
  1071		[37m"For debugging: write the receiver's printString directly to the display at (0, 100); senders of this are detected by the check-for-slips mechanism."[39;49;00m$
  1072	$
  1073		[36mself[39;49;00m [32masString[39;49;00m [32mdisplayAt:[39;49;00m [34m0[39;49;00m[32m@[39;49;00m[34m100[39;49;00m$
  1074	$
  1075	[37m"StringMorph someInstance printDirectlyToDisplay"[39;49;00m[34m! ![39;49;00m$
  1076	$
  1077	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'RAA 3/31/1999 12:13'![39;49;00m$
  1078	[32mwithoutListWrapper[39;49;00m$
  1079	$
  1080		^[36mself[39;49;00m[34m! ![39;49;00m$
  1081	$
  1082	$
  1083	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m![39;49;00m$
  1084	[32mclone[39;49;00m$
  1085	$
  1086		<[34mprimitive:[39;49;00m 148>$
  1087		[36mself[39;49;00m [32mprimitiveFailed[39;49;00m[34m! ![39;49;00m$
  1088	$
  1089	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'ajh 8/18/2001 21:25'![39;49;00m$
  1090	[32mcopy[39;49;00m$
  1091		[37m"Answer another instance just like the receiver. Subclasses typically override postCopy; they typically do not override shallowCopy."[39;49;00m$
  1092	$
  1093		^[36mself[39;49;00m [32mshallowCopy[39;49;00m [32mpostCopy[39;49;00m[34m! ![39;49;00m$
  1094	$
  1095	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 8/20/1998 16:01'![39;49;00m$
  1096	[32mcopyAddedStateFrom:[39;49;00m [31manotherObject[39;49;00m$
  1097		[37m"Copy over the values of instance variables added by the receiver's class from anotherObject to the receiver.  These will be remapped in mapUniClasses, if needed."[39;49;00m$
  1098	$
  1099		[36mself[39;49;00m [32mclass[39;49;00m [32msuperclass[39;49;00m [32minstSize[39;49;00m [32m+[39;49;00m [34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mdo:[39;49;00m$
  1100			[:[31mindex[39;49;00m | [36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([31manotherObject[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m)][34m! ![39;49;00m$
  1101	$
  1102	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tpr 2/14/2004 21:53'![39;49;00m$
  1103	[32mcopyFrom:[39;49;00m [31manotherObject[39;49;00m$
  1104		[37m"Copy to myself all instance variables I have in common with anotherObject.  This is dangerous because it ignores an object's control over its own inst vars.  "[39;49;00m$
  1105	$
  1106		|[31m mine his [39;49;00m|$
  1107		<[34mprimitive:[39;49;00m 168>$
  1108		[31mmine[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m.$
  1109		[31mhis[39;49;00m _ [31manotherObject[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m.$
  1110		[34m1[39;49;00m [32mto:[39;49;00m ([31mmine[39;49;00m [32msize[39;49;00m [32mmin:[39;49;00m [31mhis[39;49;00m [32msize[39;49;00m) [32mdo:[39;49;00m [:[31mind[39;49;00m |$
  1111			([31mmine[39;49;00m [32mat:[39;49;00m [31mind[39;49;00m) [32m=[39;49;00m ([31mhis[39;49;00m [32mat:[39;49;00m [31mind[39;49;00m) [36mifTrue:[39;49;00m [$
  1112				[36mself[39;49;00m [32minstVarAt:[39;49;00m [31mind[39;49;00m [32mput:[39;49;00m ([31manotherObject[39;49;00m [32minstVarAt:[39;49;00m [31mind[39;49;00m)]].$
  1113		[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m [32m&[39;49;00m [31manotherObject[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m [36mifTrue:[39;49;00m [$
  1114			[34m1[39;49;00m [32mto:[39;49;00m ([36mself[39;49;00m [32mbasicSize[39;49;00m [32mmin:[39;49;00m [31manotherObject[39;49;00m [32mbasicSize[39;49;00m) [32mdo:[39;49;00m [:[31mind[39;49;00m |$
  1115				[36mself[39;49;00m [32mbasicAt:[39;49;00m [31mind[39;49;00m [32mput:[39;49;00m ([31manotherObject[39;49;00m [32mbasicAt:[39;49;00m [31mind[39;49;00m)]].[34m! ![39;49;00m$
  1116	$
  1117	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'ajh 5/23/2002 00:38'![39;49;00m$
  1118	[32mcopySameFrom:[39;49;00m [31motherObject[39;49;00m$
  1119		[37m"Copy to myself all instance variables named the same in otherObject.[39;49;00m$
  1120	[37m	This ignores otherObject's control over its own inst vars."[39;49;00m$
  1121	$
  1122		|[31m myInstVars otherInstVars match [39;49;00m|$
  1123		[31mmyInstVars[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m.$
  1124		[31motherInstVars[39;49;00m _ [31motherObject[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m.$
  1125		[31mmyInstVars[39;49;00m [32mdoWithIndex:[39;49;00m [:[31meach[39;49;00m :[31mindex[39;49;00m |$
  1126			([31mmatch[39;49;00m _ [31motherInstVars[39;49;00m [32mindexOf:[39;49;00m [31meach[39;49;00m) [32m>[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m$
  1127				[[36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([31motherObject[39;49;00m [32minstVarAt:[39;49;00m [31mmatch[39;49;00m)]].$
  1128		[34m1[39;49;00m [32mto:[39;49;00m ([36mself[39;49;00m [32mbasicSize[39;49;00m [32mmin:[39;49;00m [31motherObject[39;49;00m [32mbasicSize[39;49;00m) [32mdo:[39;49;00m [:[31mi[39;49;00m |$
  1129			[36mself[39;49;00m [32mbasicAt:[39;49;00m [31mi[39;49;00m [32mput:[39;49;00m ([31motherObject[39;49;00m [32mbasicAt:[39;49;00m [31mi[39;49;00m)].$
  1130	[34m! ![39;49;00m$
  1131	$
  1132	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 4/20/1999 14:44'![39;49;00m$
  1133	[32mcopyTwoLevel[39;49;00m$
  1134		[37m"one more level than a shallowCopy"[39;49;00m$
  1135	$
  1136		|[31m newObject class index [39;49;00m|$
  1137		[31mclass[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m.$
  1138		[31mnewObject[39;49;00m _ [36mself[39;49;00m [32mclone[39;49;00m.$
  1139		[31mnewObject[39;49;00m [32m==[39;49;00m [36mself[39;49;00m [36mifTrue:[39;49;00m [^ [36mself[39;49;00m].$
  1140		[31mclass[39;49;00m [32misVariable[39;49;00m$
  1141			[36mifTrue:[39;49;00m $
  1142				[[31mindex[39;49;00m _ [36mself[39;49;00m [32mbasicSize[39;49;00m.$
  1143				[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
  1144					[36mwhileTrue:[39;49;00m $
  1145						[[31mnewObject[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m) [32mshallowCopy[39;49;00m.$
  1146						[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]].$
  1147		[31mindex[39;49;00m _ [31mclass[39;49;00m [32minstSize[39;49;00m.$
  1148		[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
  1149			[36mwhileTrue:[39;49;00m $
  1150				[[31mnewObject[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m) [32mshallowCopy[39;49;00m.$
  1151				[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m].$
  1152		^[31mnewObject[39;49;00m[34m! ![39;49;00m$
  1153	$
  1154	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m![39;49;00m$
  1155	[32mdeepCopy[39;49;00m$
  1156		[37m"Answer a copy of the receiver with its own copy of each instance [39;49;00m$
  1157	[37m	variable."[39;49;00m$
  1158	$
  1159		|[31m newObject class index [39;49;00m|$
  1160		[31mclass[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m.$
  1161		([31mclass[39;49;00m [32m==[39;49;00m [04m[32mObject[39;49;00m) [36mifTrue:[39;49;00m [^[36mself[39;49;00m].$
  1162		[31mclass[39;49;00m [32misVariable[39;49;00m$
  1163			[36mifTrue:[39;49;00m $
  1164				[[31mindex[39;49;00m _ [36mself[39;49;00m [32mbasicSize[39;49;00m.$
  1165				[31mnewObject[39;49;00m _ [31mclass[39;49;00m [32mbasicNew:[39;49;00m [31mindex[39;49;00m.$
  1166				[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
  1167					[36mwhileTrue:[39;49;00m $
  1168						[[31mnewObject[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m) [32mdeepCopy[39;49;00m.$
  1169						[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]$
  1170			[36mifFalse:[39;49;00m [[31mnewObject[39;49;00m _ [31mclass[39;49;00m [32mbasicNew[39;49;00m].$
  1171		[31mindex[39;49;00m _ [31mclass[39;49;00m [32minstSize[39;49;00m.$
  1172		[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
  1173			[36mwhileTrue:[39;49;00m $
  1174				[[31mnewObject[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m) [32mdeepCopy[39;49;00m.$
  1175				[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m].$
  1176		^[31mnewObject[39;49;00m[34m! ![39;49;00m$
  1177	$
  1178	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'hg 11/23/1999 13:43'![39;49;00m$
  1179	[32minitialDeepCopierSize[39;49;00m$
  1180		[37m"default value is 4096; other classes may override this, esp. for smaller (=faster) sizes"[39;49;00m$
  1181	$
  1182		^[34m4096[39;49;00m[34m! ![39;49;00m$
  1183	$
  1184	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'ajh 1/27/2003 18:45'![39;49;00m$
  1185	[32mpostCopy[39;49;00m$
  1186		[37m"self is a shallow copy, subclasses should copy fields as necessary to complete the full copy"[39;49;00m$
  1187	$
  1188		^ [36mself[39;49;00m[34m! ![39;49;00m$
  1189	$
  1190	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'jm 11/14/97 11:08'![39;49;00m$
  1191	[32mshallowCopy[39;49;00m$
  1192		[37m"Answer a copy of the receiver which shares the receiver's instance variables."[39;49;00m$
  1193		|[31m class newObject index [39;49;00m|$
  1194		<[34mprimitive:[39;49;00m 148>$
  1195		[31mclass[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m.$
  1196		[31mclass[39;49;00m [32misVariable[39;49;00m$
  1197			[36mifTrue:[39;49;00m $
  1198				[[31mindex[39;49;00m _ [36mself[39;49;00m [32mbasicSize[39;49;00m.$
  1199				[31mnewObject[39;49;00m _ [31mclass[39;49;00m [32mbasicNew:[39;49;00m [31mindex[39;49;00m.$
  1200				[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
  1201					[36mwhileTrue:[39;49;00m $
  1202						[[31mnewObject[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m).$
  1203						[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]$
  1204			[36mifFalse:[39;49;00m [[31mnewObject[39;49;00m _ [31mclass[39;49;00m [32mbasicNew[39;49;00m].$
  1205		[31mindex[39;49;00m _ [31mclass[39;49;00m [32minstSize[39;49;00m.$
  1206		[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
  1207			[36mwhileTrue:[39;49;00m $
  1208				[[31mnewObject[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m).$
  1209				[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m].$
  1210		^ [31mnewObject[39;49;00m[34m! ![39;49;00m$
  1211	$
  1212	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 3/11/2003 13:58'![39;49;00m$
  1213	[32mveryDeepCopy[39;49;00m$
  1214		[37m"Do a complete tree copy using a dictionary.  An object in the tree twice is only copied once.  All references to the object in the copy of the tree will point to the new copy."[39;49;00m$
  1215	$
  1216		|[31m copier new [39;49;00m|$
  1217		[31mcopier[39;49;00m _ [04m[32mDeepCopier[39;49;00m [36mnew[39;49;00m [32minitialize:[39;49;00m [36mself[39;49;00m [32minitialDeepCopierSize[39;49;00m.$
  1218		[31mnew[39;49;00m _ [36mself[39;49;00m [32mveryDeepCopyWith:[39;49;00m [31mcopier[39;49;00m.$
  1219		[31mcopier[39;49;00m [32mmapUniClasses[39;49;00m.$
  1220		[31mcopier[39;49;00m [32mreferences[39;49;00m [32massociationsDo:[39;49;00m [:[31massoc[39;49;00m | $
  1221			[31massoc[39;49;00m [32mvalue[39;49;00m [32mveryDeepFixupWith:[39;49;00m [31mcopier[39;49;00m].$
  1222		[31mcopier[39;49;00m [32mfixDependents[39;49;00m.$
  1223		^ [31mnew[39;49;00m[34m! ![39;49;00m$
  1224	$
  1225	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 3/11/2003 13:58'![39;49;00m$
  1226	[32mveryDeepCopySibling[39;49;00m$
  1227		[37m"Do a complete tree copy using a dictionary.  Substitute a clone of oldPlayer for the root.  Normally, a Player or non systemDefined object would have a new class.  We do not want one this time.  An object in the tree twice, is only copied once.  All references to the object in the copy of the tree will point to the new copy."[39;49;00m$
  1228	$
  1229		|[31m copier new [39;49;00m|$
  1230		[31mcopier[39;49;00m _ [04m[32mDeepCopier[39;49;00m [36mnew[39;49;00m [32minitialize:[39;49;00m [36mself[39;49;00m [32minitialDeepCopierSize[39;49;00m.$
  1231		[31mcopier[39;49;00m [32mnewUniClasses:[39;49;00m [36mfalse[39;49;00m.$
  1232		[31mnew[39;49;00m _ [36mself[39;49;00m [32mveryDeepCopyWith:[39;49;00m [31mcopier[39;49;00m.$
  1233		[31mcopier[39;49;00m [32mmapUniClasses[39;49;00m.$
  1234		[31mcopier[39;49;00m [32mreferences[39;49;00m [32massociationsDo:[39;49;00m [:[31massoc[39;49;00m | $
  1235			[31massoc[39;49;00m [32mvalue[39;49;00m [32mveryDeepFixupWith:[39;49;00m [31mcopier[39;49;00m].$
  1236		[31mcopier[39;49;00m [32mfixDependents[39;49;00m.$
  1237		^ [31mnew[39;49;00m[34m! ![39;49;00m$
  1238	$
  1239	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 5/13/2003 19:39'![39;49;00m$
  1240	[32mveryDeepCopyUsing:[39;49;00m [31mcopier[39;49;00m$
  1241		[37m"Do a complete tree copy using a dictionary.  An object in the tree twice is only copied once.  All references to the object in the copy of the tree will point to the new copy.[39;49;00m$
  1242	[37m	Same as veryDeepCopy except copier (with dictionary) is supplied.[39;49;00m$
  1243	[37m	** do not delete this method, even if it has no callers **"[39;49;00m$
  1244	$
  1245		|[31m new refs newDep newModel [39;49;00m|$
  1246		[31mnew[39;49;00m _ [36mself[39;49;00m [32mveryDeepCopyWith:[39;49;00m [31mcopier[39;49;00m.$
  1247		[31mcopier[39;49;00m [32mmapUniClasses[39;49;00m.$
  1248		[31mcopier[39;49;00m [32mreferences[39;49;00m [32massociationsDo:[39;49;00m [:[31massoc[39;49;00m | $
  1249			[31massoc[39;49;00m [32mvalue[39;49;00m [32mveryDeepFixupWith:[39;49;00m [31mcopier[39;49;00m].$
  1250		[37m"Fix dependents"[39;49;00m$
  1251		[31mrefs[39;49;00m _ [31mcopier[39;49;00m [32mreferences[39;49;00m.$
  1252		[04m[32mDependentsFields[39;49;00m [32massociationsDo:[39;49;00m [:[31mpair[39;49;00m |$
  1253			[31mpair[39;49;00m [32mvalue[39;49;00m [32mdo:[39;49;00m [:[31mdep[39;49;00m | $
  1254				([31mnewDep[39;49;00m _ [31mrefs[39;49;00m [32mat:[39;49;00m [31mdep[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m]) [32mifNotNil:[39;49;00m [$
  1255					[31mnewModel[39;49;00m _ [31mrefs[39;49;00m [32mat:[39;49;00m [31mpair[39;49;00m [32mkey[39;49;00m [32mifAbsent:[39;49;00m [[31mpair[39;49;00m [32mkey[39;49;00m].$
  1256					[31mnewModel[39;49;00m [32maddDependent:[39;49;00m [31mnewDep[39;49;00m]]].$
  1257		^ [31mnew[39;49;00m[34m! ![39;49;00m$
  1258	$
  1259	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 3/11/2003 14:12'![39;49;00m$
  1260	[32mveryDeepCopyWith:[39;49;00m [31mdeepCopier[39;49;00m$
  1261		[37m"Copy me and the entire tree of objects I point to.  An object in the tree twice is copied once, and both references point to him.  deepCopier holds a dictionary of objects we have seen.  Some classes refuse to be copied.  Some classes are picky about which fields get deep copied."[39;49;00m$
  1262		|[31m class index sub subAss new uc sup has mine [39;49;00m|$
  1263		[31mdeepCopier[39;49;00m [32mreferences[39;49;00m [32mat:[39;49;00m [36mself[39;49;00m [32mifPresent:[39;49;00m [:[31mnewer[39;49;00m | ^ [31mnewer[39;49;00m]. 	[37m"already did him"[39;49;00m$
  1264		[31mclass[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m.$
  1265		[31mclass[39;49;00m [32misMeta[39;49;00m [36mifTrue:[39;49;00m [^ [36mself[39;49;00m].		[37m"a class"[39;49;00m$
  1266		[31mnew[39;49;00m _ [36mself[39;49;00m [32mclone[39;49;00m.$
  1267		([31mclass[39;49;00m [32misSystemDefined[39;49;00m [32mnot[39;49;00m [32mand:[39;49;00m [[31mdeepCopier[39;49;00m [32mnewUniClasses[39;49;00m [37m"allowed"[39;49;00m]) [36mifTrue:[39;49;00m [$
  1268			[31muc[39;49;00m _ [31mdeepCopier[39;49;00m [32muniClasses[39;49;00m [32mat:[39;49;00m [31mclass[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m].$
  1269			[31muc[39;49;00m [32mifNil:[39;49;00m [$
  1270				[31mdeepCopier[39;49;00m [32muniClasses[39;49;00m [32mat:[39;49;00m [31mclass[39;49;00m [32mput:[39;49;00m ([31muc[39;49;00m _ [36mself[39;49;00m [32mcopyUniClassWith:[39;49;00m [31mdeepCopier[39;49;00m).$
  1271				[31mdeepCopier[39;49;00m [32mreferences[39;49;00m [32mat:[39;49;00m [31mclass[39;49;00m [32mput:[39;49;00m [31muc[39;49;00m].	[37m"remember"[39;49;00m$
  1272			[31mnew[39;49;00m _ [31muc[39;49;00m [36mnew[39;49;00m.$
  1273			[31mnew[39;49;00m [32mcopyFrom:[39;49;00m [36mself[39;49;00m].	[37m"copy inst vars in case any are weak"[39;49;00m$
  1274		[31mdeepCopier[39;49;00m [32mreferences[39;49;00m [32mat:[39;49;00m [36mself[39;49;00m [32mput:[39;49;00m [31mnew[39;49;00m.	[37m"remember"[39;49;00m$
  1275		([31mclass[39;49;00m [32misVariable[39;49;00m [32mand:[39;49;00m [[31mclass[39;49;00m [32misPointers[39;49;00m]) [36mifTrue:[39;49;00m $
  1276			[[31mindex[39;49;00m _ [36mself[39;49;00m [32mbasicSize[39;49;00m.$
  1277			[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m] [36mwhileTrue:[39;49;00m $
  1278				[[31msub[39;49;00m _ [36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m.$
  1279				([31msubAss[39;49;00m _ [31mdeepCopier[39;49;00m [32mreferences[39;49;00m [32massociationAt:[39;49;00m [31msub[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m])$
  1280					[32mifNil:[39;49;00m [[31mnew[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([31msub[39;49;00m [32mveryDeepCopyWith:[39;49;00m [31mdeepCopier[39;49;00m)]$
  1281					[32mifNotNil:[39;49;00m [[31mnew[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m [31msubAss[39;49;00m [32mvalue[39;49;00m].$
  1282				[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]].$
  1283		[37m"Ask each superclass if it wants to share (weak copy) any inst vars"[39;49;00m$
  1284		[31mnew[39;49;00m [32mveryDeepInner:[39;49;00m [31mdeepCopier[39;49;00m.		[37m"does super a lot"[39;49;00m$
  1285	$
  1286		[37m"other superclasses want all inst vars deep copied"[39;49;00m$
  1287		[31msup[39;49;00m _ [31mclass[39;49;00m.  [31mindex[39;49;00m _ [31mclass[39;49;00m [32minstSize[39;49;00m.$
  1288		[[31mhas[39;49;00m _ [31msup[39;49;00m [32mcompiledMethodAt:[39;49;00m [33m#veryDeepInner:[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m].$
  1289		[31mhas[39;49;00m _ [31mhas[39;49;00m [32mifNil:[39;49;00m [[31mclass[39;49;00m [32misSystemDefined[39;49;00m [32mnot[39;49;00m [37m"is a uniClass"[39;49;00m] [32mifNotNil:[39;49;00m [[36mtrue[39;49;00m].$
  1290		[31mmine[39;49;00m _ [31msup[39;49;00m [32minstVarNames[39;49;00m.$
  1291		[31mhas[39;49;00m [36mifTrue:[39;49;00m [[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [31mmine[39;49;00m [32msize[39;49;00m]	[37m"skip inst vars"[39;49;00m$
  1292			[36mifFalse:[39;49;00m [[34m1[39;49;00m [32mto:[39;49;00m [31mmine[39;49;00m [32msize[39;49;00m [32mdo:[39;49;00m [:[31mxx[39;49;00m |$
  1293					[31msub[39;49;00m _ [36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m.$
  1294					([31msubAss[39;49;00m _ [31mdeepCopier[39;49;00m [32mreferences[39;49;00m [32massociationAt:[39;49;00m [31msub[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m])$
  1295							[37m"use association, not value, so nil is an exceptional value"[39;49;00m$
  1296						[32mifNil:[39;49;00m [[31mnew[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m $
  1297									([31msub[39;49;00m [32mveryDeepCopyWith:[39;49;00m [31mdeepCopier[39;49;00m)]$
  1298						[32mifNotNil:[39;49;00m [[31mnew[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m [31msubAss[39;49;00m [32mvalue[39;49;00m].$
  1299					[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]].$
  1300		([31msup[39;49;00m _ [31msup[39;49;00m [32msuperclass[39;49;00m) [32m==[39;49;00m [36mnil[39;49;00m] [32mwhileFalse[39;49;00m.$
  1301		[31mnew[39;49;00m [32mrehash[39;49;00m.	[37m"force Sets and Dictionaries to rehash"[39;49;00m$
  1302		^ [31mnew[39;49;00m$
  1303	[34m! ![39;49;00m$
  1304	$
  1305	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 1/6/1999 17:39'![39;49;00m$
  1306	[32mveryDeepFixupWith:[39;49;00m [31mdeepCopier[39;49;00m$
  1307		[37m"I have no fields and no superclass.  Catch the super call."[39;49;00m$
  1308	[34m! ![39;49;00m$
  1309	$
  1310	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 9/4/2001 10:30'![39;49;00m$
  1311	[32mveryDeepInner:[39;49;00m [31mdeepCopier[39;49;00m$
  1312		[37m"No special treatment for inst vars of my superclasses.  Override when some need to be weakly copied.  Object>>veryDeepCopyWith: will veryDeepCopy any inst var whose class does not actually define veryDeepInner:"[39;49;00m$
  1313	[34m! ![39;49;00m$
  1314	$
  1315	$
  1316	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'creation'[39;49;00m[34m stamp: 'nk 2/26/2004 13:35'![39;49;00m$
  1317	[32masStringMorph[39;49;00m$
  1318		[37m"Open a StringMorph, as best one can, on the receiver"[39;49;00m$
  1319	$
  1320		^ [36mself[39;49;00m [32masStringOrText[39;49;00m [32masStringMorph[39;49;00m$
  1321	[34m! ![39;49;00m$
  1322	$
  1323	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'creation'[39;49;00m[34m stamp: 'nk 2/26/2004 13:35'![39;49;00m$
  1324	[32masTextMorph[39;49;00m$
  1325		[37m"Open a TextMorph, as best one can, on the receiver"[39;49;00m$
  1326	$
  1327		^ [04m[32mTextMorph[39;49;00m [36mnew[39;49;00m [32mcontentsAsIs:[39;49;00m [36mself[39;49;00m [32masStringOrText[39;49;00m$
  1328	[34m! ![39;49;00m$
  1329	$
  1330	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'creation'[39;49;00m[34m stamp: 'sw 1/29/2002 21:45'![39;49;00m$
  1331	[32mopenAsMorph[39;49;00m$
  1332		[37m"Open a morph, as best one can, on the receiver"[39;49;00m$
  1333	$
  1334		^ [36mself[39;49;00m [32masMorph[39;49;00m [32mopenInHand[39;49;00m$
  1335	$
  1336	[37m"[39;49;00m$
  1337	[37m234 openAsMorph[39;49;00m$
  1338	[37m(ScriptingSystem formAtKey: #TinyMenu) openAsMorph[39;49;00m$
  1339	[37m'fred' openAsMorph[39;49;00m$
  1340	[37m"[39;49;00m[34m! ![39;49;00m$
  1341	$
  1342	$
  1343	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging'[39;49;00m[34m stamp: 'md 11/24/2004 11:45'![39;49;00m$
  1344	[32mhaltIf:[39;49;00m [31mcondition[39;49;00m$
  1345		[37m"This is the typical message to use for inserting breakpoints during [39;49;00m$
  1346	[37m	debugging.  Param can be a block or expression, halt if true.[39;49;00m$
  1347	[37m	If the Block has one arg, the receiver is bound to that.[39;49;00m$
  1348	[37m 	If the condition is a selector, we look up in the callchain. Halt if[39;49;00m$
  1349	[37m      any method's selector equals selector."[39;49;00m$
  1350		|[31m cntxt [39;49;00m|$
  1351	$
  1352		[31mcondition[39;49;00m [32misSymbol[39;49;00m [36mifTrue:[39;49;00m[$
  1353			[37m"only halt if a method with selector symbol is in callchain"[39;49;00m$
  1354			[31mcntxt[39;49;00m := [36mthisContext[39;49;00m.$
  1355			[[31mcntxt[39;49;00m [32msender[39;49;00m [32misNil[39;49;00m] [36mwhileFalse:[39;49;00m [$
  1356				[31mcntxt[39;49;00m := [31mcntxt[39;49;00m [32msender[39;49;00m. $
  1357				([31mcntxt[39;49;00m [32mselector[39;49;00m [32m=[39;49;00m [31mcondition[39;49;00m) [36mifTrue:[39;49;00m [[04m[32mHalt[39;49;00m [32msignal[39;49;00m].$
  1358				].$
  1359			^[36mself[39;49;00m.$
  1360		].$
  1361		([31mcondition[39;49;00m [32misBlock[39;49;00m $
  1362				[36mifTrue:[39;49;00m [[31mcondition[39;49;00m [32mvalueWithPossibleArgument:[39;49;00m [36mself[39;49;00m] $
  1363				[36mifFalse:[39;49;00m [[31mcondition[39;49;00m] $
  1364		) [36mifTrue:[39;49;00m [$
  1365			[04m[32mHalt[39;49;00m [32msignal[39;49;00m$
  1366		].[34m! ![39;49;00m$
  1367	$
  1368	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging'[39;49;00m[34m![39;49;00m$
  1369	[31mneedsWork[39;49;00m[34m! ![39;49;00m$
  1370	$
  1371	$
  1372	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:26'![39;49;00m$
  1373	[32mcheckHaltCountExpired[39;49;00m$
  1374		|[31m counter [39;49;00m|$
  1375		[31mcounter[39;49;00m _ [04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#HaltCount[39;49;00m [32mifAbsent:[39;49;00m [[34m0[39;49;00m].$
  1376		^[31mcounter[39;49;00m [32m=[39;49;00m [34m0[39;49;00m[34m! ![39;49;00m$
  1377	$
  1378	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:04'![39;49;00m$
  1379	[32mclearHaltOnce[39;49;00m$
  1380		[37m"Turn on the halt once flag."[39;49;00m$
  1381		[04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#HaltOnce[39;49;00m [32mput:[39;49;00m [36mfalse[39;49;00m[34m! ![39;49;00m$
  1382	$
  1383	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:30'![39;49;00m$
  1384	[32mdecrementAndCheckHaltCount[39;49;00m$
  1385		[36mself[39;49;00m [32mdecrementHaltCount[39;49;00m.$
  1386		^[36mself[39;49;00m [32mcheckHaltCountExpired[39;49;00m[34m! ![39;49;00m$
  1387	$
  1388	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:28'![39;49;00m$
  1389	[32mdecrementHaltCount[39;49;00m$
  1390		|[31m counter [39;49;00m|$
  1391		[31mcounter[39;49;00m := [04m[32mSmalltalk[39;49;00m$
  1392					[32mat:[39;49;00m [33m#HaltCount[39;49;00m$
  1393					[32mifAbsent:[39;49;00m [[34m0[39;49;00m].$
  1394		[31mcounter[39;49;00m [32m>[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m [$
  1395			[31mcounter[39;49;00m _ [31mcounter[39;49;00m [32m-[39;49;00m [34m1[39;49;00m.$
  1396			[36mself[39;49;00m [32msetHaltCountTo:[39;49;00m [31mcounter[39;49;00m][34m! ![39;49;00m$
  1397	$
  1398	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:42'![39;49;00m$
  1399	[32mdoExpiredHaltCount[39;49;00m$
  1400		[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
  1401		[36mself[39;49;00m [32mremoveHaltCount[39;49;00m.$
  1402		[36mself[39;49;00m [32mhalt[39;49;00m[34m! ![39;49;00m$
  1403	$
  1404	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:44'![39;49;00m$
  1405	[32mdoExpiredHaltCount:[39;49;00m [31maString[39;49;00m$
  1406		[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
  1407		[36mself[39;49;00m [32mremoveHaltCount[39;49;00m.$
  1408		[36mself[39;49;00m [32mhalt:[39;49;00m [31maString[39;49;00m[34m! ![39;49;00m$
  1409	$
  1410	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:45'![39;49;00m$
  1411	[32mdoExpiredInspectCount[39;49;00m$
  1412		[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
  1413		[36mself[39;49;00m [32mremoveHaltCount[39;49;00m.$
  1414		[36mself[39;49;00m [32minspect[39;49;00m[34m! ![39;49;00m$
  1415	$
  1416	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:43'![39;49;00m$
  1417	[32mhaltOnCount:[39;49;00m [31mint[39;49;00m $
  1418		[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
  1419			[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mhasHaltCount[39;49;00m$
  1420					[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdecrementAndCheckHaltCount[39;49;00m$
  1421							[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredHaltCount[39;49;00m]]$
  1422					[36mifFalse:[39;49;00m [[31mint[39;49;00m [32m=[39;49;00m [34m1[39;49;00m$
  1423							[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredHaltCount[39;49;00m]$
  1424							[36mifFalse:[39;49;00m [[36mself[39;49;00m [32msetHaltCountTo:[39;49;00m [31mint[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]][34m! ![39;49;00m$
  1425	$
  1426	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:05'![39;49;00m$
  1427	[32mhaltOnce[39;49;00m$
  1428		[37m"Halt unless we have already done it once."[39;49;00m$
  1429		[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
  1430			[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
  1431				^ [36mself[39;49;00m [32mhalt[39;49;00m][34m! ![39;49;00m$
  1432	$
  1433	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:04'![39;49;00m$
  1434	[32mhaltOnceEnabled[39;49;00m$
  1435		^ [04m[32mSmalltalk[39;49;00m$
  1436			[32mat:[39;49;00m [33m#HaltOnce[39;49;00m$
  1437			[32mifAbsent:[39;49;00m [[36mfalse[39;49;00m][34m! ![39;49;00m$
  1438	$
  1439	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:05'![39;49;00m$
  1440	[32mhaltOnce:[39;49;00m [31maString[39;49;00m $
  1441		[37m"Halt unless we have already done it once."[39;49;00m$
  1442		[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
  1443			[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
  1444				^ [36mself[39;49;00m [32mhalt:[39;49;00m [31maString[39;49;00m][34m! ![39;49;00m$
  1445	$
  1446	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:45'![39;49;00m$
  1447	[32mhalt:[39;49;00m [31maString[39;49;00m [32monCount:[39;49;00m [31mint[39;49;00m $
  1448		[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
  1449			[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mhasHaltCount[39;49;00m$
  1450					[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdecrementAndCheckHaltCount[39;49;00m$
  1451							[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredHaltCount:[39;49;00m [31maString[39;49;00m]]$
  1452					[36mifFalse:[39;49;00m [[31mint[39;49;00m [32m=[39;49;00m [34m1[39;49;00m$
  1453							[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredHaltCount:[39;49;00m [31maString[39;49;00m]$
  1454							[36mifFalse:[39;49;00m [[36mself[39;49;00m [32msetHaltCountTo:[39;49;00m [31mint[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]][34m! ![39;49;00m$
  1455	$
  1456	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:36'![39;49;00m$
  1457	[32mhasHaltCount[39;49;00m$
  1458		^[04m[32mSmalltalk[39;49;00m$
  1459					[32mincludesKey:[39;49;00m [33m#HaltCount[39;49;00m[34m! ![39;49;00m$
  1460	$
  1461	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:46'![39;49;00m$
  1462	[32minspectOnCount:[39;49;00m [31mint[39;49;00m $
  1463		[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
  1464			[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mhasHaltCount[39;49;00m$
  1465					[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdecrementAndCheckHaltCount[39;49;00m$
  1466							[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredInspectCount[39;49;00m]]$
  1467					[36mifFalse:[39;49;00m [[31mint[39;49;00m [32m=[39;49;00m [34m1[39;49;00m$
  1468							[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredInspectCount[39;49;00m]$
  1469							[36mifFalse:[39;49;00m [[36mself[39;49;00m [32msetHaltCountTo:[39;49;00m [31mint[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]][34m! ![39;49;00m$
  1470	$
  1471	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:05'![39;49;00m$
  1472	[32minspectOnce[39;49;00m$
  1473		[37m"Inspect unless we have already done it once."[39;49;00m$
  1474		[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
  1475			[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
  1476				^ [36mself[39;49;00m [32minspect[39;49;00m][34m! ![39;49;00m$
  1477	$
  1478	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 13:20'![39;49;00m$
  1479	[32minspectUntilCount:[39;49;00m [31mint[39;49;00m $
  1480		[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
  1481			[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mhasHaltCount[39;49;00m$
  1482					[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdecrementAndCheckHaltCount[39;49;00m$
  1483							[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredInspectCount[39;49;00m]$
  1484							[36mifFalse:[39;49;00m [[36mself[39;49;00m [32minspect[39;49;00m]]$
  1485					[36mifFalse:[39;49;00m [[31mint[39;49;00m [32m=[39;49;00m [34m1[39;49;00m$
  1486							[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredInspectCount[39;49;00m]$
  1487							[36mifFalse:[39;49;00m [[36mself[39;49;00m [32msetHaltCountTo:[39;49;00m [31mint[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]][34m! ![39;49;00m$
  1488	$
  1489	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:49'![39;49;00m$
  1490	[32mremoveHaltCount[39;49;00m$
  1491		([04m[32mSmalltalk[39;49;00m [32mincludesKey:[39;49;00m [33m#HaltCount[39;49;00m) [36mifTrue:[39;49;00m [$
  1492			[04m[32mSmalltalk[39;49;00m [32mremoveKey:[39;49;00m [33m#HaltCount[39;49;00m][34m! ![39;49;00m$
  1493	$
  1494	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:25'![39;49;00m$
  1495	[32msetHaltCountTo:[39;49;00m [31mint[39;49;00m$
  1496		[04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#HaltCount[39;49;00m [32mput:[39;49;00m [31mint[39;49;00m[34m! ![39;49;00m$
  1497	$
  1498	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:04'![39;49;00m$
  1499	[32msetHaltOnce[39;49;00m$
  1500		[37m"Turn on the halt once flag."[39;49;00m$
  1501		[04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#HaltOnce[39;49;00m [32mput:[39;49;00m [36mtrue[39;49;00m[34m! ![39;49;00m$
  1502	$
  1503	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:04'![39;49;00m$
  1504	[32mtoggleHaltOnce[39;49;00m$
  1505		[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
  1506			[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mclearHaltOnce[39;49;00m]$
  1507			[36mifFalse:[39;49;00m [[36mself[39;49;00m [32msetHaltOnce[39;49;00m][34m! ![39;49;00m$
  1508	$
  1509	$
  1510	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'ar 2/11/2001 01:55'![39;49;00m$
  1511	[32maddDependent:[39;49;00m [31manObject[39;49;00m$
  1512		[37m"Make the given object one of the receiver's dependents."[39;49;00m$
  1513	$
  1514		|[31m dependents [39;49;00m|$
  1515		[31mdependents[39;49;00m _ [36mself[39;49;00m [32mdependents[39;49;00m.$
  1516		([31mdependents[39;49;00m [32mincludes:[39;49;00m [31manObject[39;49;00m) [36mifFalse:[39;49;00m$
  1517			[[36mself[39;49;00m [32mmyDependents:[39;49;00m ([31mdependents[39;49;00m [32mcopyWithDependent:[39;49;00m [31manObject[39;49;00m)].$
  1518		^ [31manObject[39;49;00m[34m! ![39;49;00m$
  1519	$
  1520	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:53'![39;49;00m$
  1521	[32mbreakDependents[39;49;00m$
  1522		[37m"Remove all of the receiver's dependents."[39;49;00m$
  1523	$
  1524		[36mself[39;49;00m [32mmyDependents:[39;49;00m [36mnil[39;49;00m[34m! ![39;49;00m$
  1525	$
  1526	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:26'![39;49;00m$
  1527	[32mcanDiscardEdits[39;49;00m$
  1528		[37m"Answer true if none of the views on this model has unaccepted edits that matter."[39;49;00m$
  1529	$
  1530		[36mself[39;49;00m [32mdependents[39;49;00m$
  1531			[32mdo:[39;49;00m [:[31meach[39;49;00m | [31meach[39;49;00m [32mcanDiscardEdits[39;49;00m [36mifFalse:[39;49;00m [^ [36mfalse[39;49;00m]]$
  1532			[32mwithout:[39;49;00m [36mself[39;49;00m.$
  1533		^ [36mtrue[39;49;00m[34m! ![39;49;00m$
  1534	$
  1535	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:58'![39;49;00m$
  1536	[32mdependents[39;49;00m$
  1537		[37m"Answer a collection of objects that are 'dependent' on the receiver;[39;49;00m$
  1538	[37m	 that is, all objects that should be notified if the receiver changes."[39;49;00m$
  1539	$
  1540		^ [36mself[39;49;00m [32mmyDependents[39;49;00m [32mifNil:[39;49;00m [[33m#([39;49;00m[33m)[39;49;00m][34m! ![39;49;00m$
  1541	$
  1542	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m![39;49;00m$
  1543	[32mevaluate:[39;49;00m [31mactionBlock[39;49;00m [32mwheneverChangeIn:[39;49;00m [31maspectBlock[39;49;00m$
  1544		|[31m viewerThenObject objectThenViewer [39;49;00m|$
  1545		[31mobjectThenViewer[39;49;00m _ [36mself[39;49;00m.$
  1546		[31mviewerThenObject[39;49;00m _ [04m[32mObjectViewer[39;49;00m [32mon:[39;49;00m [31mobjectThenViewer[39;49;00m.$
  1547		[31mobjectThenViewer[39;49;00m [32mbecome:[39;49;00m [31mviewerThenObject[39;49;00m.$
  1548		[37m"--- Then ---"[39;49;00m$
  1549		[31mobjectThenViewer[39;49;00m [32mxxxViewedObject:[39;49;00m [31mviewerThenObject[39;49;00m$
  1550				[32mevaluate:[39;49;00m [31mactionBlock[39;49;00m$
  1551				[32mwheneverChangeIn:[39;49;00m [31maspectBlock[39;49;00m[34m! ![39;49;00m$
  1552	$
  1553	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:59'![39;49;00m$
  1554	[32mhasUnacceptedEdits[39;49;00m$
  1555		[37m"Answer true if any of the views on this object has unaccepted edits."[39;49;00m$
  1556	$
  1557		[36mself[39;49;00m [32mdependents[39;49;00m$
  1558			[32mdo:[39;49;00m [:[31meach[39;49;00m | [31meach[39;49;00m [32mhasUnacceptedEdits[39;49;00m [36mifTrue:[39;49;00m [^ [36mtrue[39;49;00m]]$
  1559			[32mwithout:[39;49;00m [36mself[39;49;00m.$
  1560		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  1561	$
  1562	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:55'![39;49;00m$
  1563	[32mmyDependents[39;49;00m$
  1564		[37m"Private. Answer a list of all the receiver's dependents."[39;49;00m$
  1565	$
  1566		^ [04m[32mDependentsFields[39;49;00m [32mat:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m [][34m! ![39;49;00m$
  1567	$
  1568	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:52'![39;49;00m$
  1569	[32mmyDependents:[39;49;00m [31maCollectionOrNil[39;49;00m$
  1570		[37m"Private. Set (or remove) the receiver's dependents list."[39;49;00m$
  1571	$
  1572		[31maCollectionOrNil[39;49;00m$
  1573			[32mifNil:[39;49;00m [[04m[32mDependentsFields[39;49;00m [32mremoveKey:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m []]$
  1574			[32mifNotNil:[39;49;00m [[04m[32mDependentsFields[39;49;00m [32mat:[39;49;00m [36mself[39;49;00m [32mput:[39;49;00m [31maCollectionOrNil[39;49;00m][34m! ![39;49;00m$
  1575	$
  1576	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'reThink 2/18/2001 17:06'![39;49;00m$
  1577	[32mrelease[39;49;00m$
  1578		[37m"Remove references to objects that may refer to the receiver. This message [39;49;00m$
  1579	[37m	should be overridden by subclasses with any cycles, in which case the [39;49;00m$
  1580	[37m	subclass should also include the expression super release."[39;49;00m$
  1581	$
  1582		[36mself[39;49;00m [32mreleaseActionMap[39;49;00m[34m! ![39;49;00m$
  1583	$
  1584	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 20:23'![39;49;00m$
  1585	[32mremoveDependent:[39;49;00m [31manObject[39;49;00m$
  1586		[37m"Remove the given object as one of the receiver's dependents."[39;49;00m$
  1587	$
  1588		|[31m dependents [39;49;00m|$
  1589		[31mdependents[39;49;00m _ [36mself[39;49;00m [32mdependents[39;49;00m [32mreject:[39;49;00m [:[31meach[39;49;00m | [31meach[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m].$
  1590		[36mself[39;49;00m [32mmyDependents:[39;49;00m ([31mdependents[39;49;00m [32misEmpty[39;49;00m [36mifFalse:[39;49;00m [[31mdependents[39;49;00m]).$
  1591		^ [31manObject[39;49;00m[34m! ![39;49;00m$
  1592	$
  1593	$
  1594	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'bh 9/16/2001 18:10'![39;49;00m$
  1595	[32macceptDroppingMorph:[39;49;00m [31mtransferMorph[39;49;00m [32mevent:[39;49;00m [31mevt[39;49;00m [32minMorph:[39;49;00m [31mdstListMorph[39;49;00m $
  1596		$
  1597		^[36mfalse[39;49;00m.[34m! ![39;49;00m$
  1598	$
  1599	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'mir 5/16/2000 11:35'![39;49;00m$
  1600	[32mdragAnimationFor:[39;49;00m [31mitem[39;49;00m [32mtransferMorph:[39;49;00m [31mtransferMorph[39;49;00m $
  1601		[37m"Default do nothing"[39;49;00m[34m! ![39;49;00m$
  1602	$
  1603	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'panda 4/28/2000 16:20'![39;49;00m$
  1604	[32mdragPassengerFor:[39;49;00m [31mitem[39;49;00m [32minMorph:[39;49;00m [31mdragSource[39;49;00m $
  1605		^[31mitem[39;49;00m[34m! ![39;49;00m$
  1606	$
  1607	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'panda 4/28/2000 16:11'![39;49;00m$
  1608	[32mdragTransferType[39;49;00m$
  1609		^[36mnil[39;49;00m[34m! ![39;49;00m$
  1610	$
  1611	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'panda 4/28/2000 16:05'![39;49;00m$
  1612	[32mdragTransferTypeForMorph:[39;49;00m [31mdragSource[39;49;00m $
  1613		^[36mnil[39;49;00m[34m! ![39;49;00m$
  1614	$
  1615	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'mir 5/8/2000 17:19'![39;49;00m$
  1616	[32mwantsDroppedMorph:[39;49;00m [31maMorph[39;49;00m [32mevent:[39;49;00m [31manEvent[39;49;00m [32minMorph:[39;49;00m [31mdestinationLM[39;49;00m $
  1617		^[36mfalse[39;49;00m[34m! ![39;49;00m$
  1618	$
  1619	$
  1620	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'sma 5/6/2000 19:35'![39;49;00m$
  1621	[32massert:[39;49;00m [31maBlock[39;49;00m$
  1622		[37m"Throw an assertion error if aBlock does not evaluates to true."[39;49;00m$
  1623	$
  1624		[31maBlock[39;49;00m [32mvalue[39;49;00m [36mifFalse:[39;49;00m [[04m[32mAssertionFailure[39;49;00m [32msignal:[39;49;00m [33m'Assertion failed'[39;49;00m][34m! ![39;49;00m$
  1625	$
  1626	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'nk 1/15/2004 10:54'![39;49;00m$
  1627	[32massert:[39;49;00m [31maBlock[39;49;00m [32mdescriptionBlock:[39;49;00m [31mdescriptionBlock[39;49;00m$
  1628		[37m"Throw an assertion error if aBlock does not evaluate to true."[39;49;00m$
  1629	$
  1630		[31maBlock[39;49;00m [32mvalue[39;49;00m [36mifFalse:[39;49;00m [[04m[32mAssertionFailure[39;49;00m [32msignal:[39;49;00m [31mdescriptionBlock[39;49;00m [32mvalue[39;49;00m [32masString[39;49;00m ][34m! ![39;49;00m$
  1631	$
  1632	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'nk 10/25/2003 16:47'![39;49;00m$
  1633	[32massert:[39;49;00m [31maBlock[39;49;00m [32mdescription:[39;49;00m [31maString[39;49;00m$
  1634		[37m"Throw an assertion error if aBlock does not evaluates to true."[39;49;00m$
  1635	$
  1636		[31maBlock[39;49;00m [32mvalue[39;49;00m [36mifFalse:[39;49;00m [[04m[32mAssertionFailure[39;49;00m [32msignal:[39;49;00m [31maString[39;49;00m ][34m! ![39;49;00m$
  1637	$
  1638	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'md 10/13/2004 15:59'![39;49;00m$
  1639	[32mbackwardCompatibilityOnly:[39;49;00m [31manExplanationString[39;49;00m$
  1640		[37m"Warn that the sending method has been deprecated. Methods that are tagt with #backwardCompatibility:[39;49;00m$
  1641	[37m	 are kept for compatibility."[39;49;00m$
  1642	$
  1643		[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
  1644			[[04m[32mDeprecation[39;49;00m [32msignal:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m' has been deprecated (but will be kept for compatibility). '[39;49;00m[32m,[39;49;00m [31manExplanationString[39;49;00m][34m! ![39;49;00m$
  1645	$
  1646	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m![39;49;00m$
  1647	[32mcaseError[39;49;00m$
  1648		[37m"Report an error from an in-line or explicit case statement."[39;49;00m$
  1649	$
  1650		[36mself[39;49;00m [32merror:[39;49;00m [33m'Case not found, and no otherwise clause'[39;49;00m[34m! ![39;49;00m$
  1651	$
  1652	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'rbb 3/1/2005 09:26'![39;49;00m$
  1653	[32mconfirm:[39;49;00m [31mqueryString[39;49;00m$
  1654		[37m"Put up a yes/no menu with caption queryString. Answer true if the [39;49;00m$
  1655	[37m	response is yes, false if no. This is a modal question--the user must [39;49;00m$
  1656	[37m	respond yes or no."[39;49;00m$
  1657	$
  1658		[37m"nil confirm: 'Are you hungry?'"[39;49;00m$
  1659	$
  1660		^ [04m[32mUIManager[39;49;00m [32mdefault[39;49;00m [32mconfirm:[39;49;00m [31mqueryString[39;49;00m[34m! ![39;49;00m$
  1661	$
  1662	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'rbb 3/1/2005 09:27'![39;49;00m$
  1663	[32mconfirm:[39;49;00m [31maString[39;49;00m [32morCancel:[39;49;00m [31mcancelBlock[39;49;00m$
  1664		[37m"Put up a yes/no/cancel menu with caption aString. Answer true if  [39;49;00m$
  1665	[37m	the response is yes, false if no. If cancel is chosen, evaluate  [39;49;00m$
  1666	[37m	cancelBlock. This is a modal question--the user must respond yes or no."[39;49;00m$
  1667	$
  1668		^ [04m[32mUIManager[39;49;00m [32mdefault[39;49;00m [32mconfirm:[39;49;00m [31maString[39;49;00m [32morCancel:[39;49;00m [31mcancelBlock[39;49;00m[34m! ![39;49;00m$
  1669	$
  1670	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'dew 10/6/2003 18:20'![39;49;00m$
  1671	[32mdeprecated:[39;49;00m [31manExplanationString[39;49;00m$
  1672		[37m"Warn that the sending method has been deprecated."[39;49;00m$
  1673	$
  1674		[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
  1675			[[04m[32mDeprecation[39;49;00m [32msignal:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m' has been deprecated. '[39;49;00m[32m,[39;49;00m [31manExplanationString[39;49;00m][34m! ![39;49;00m$
  1676	$
  1677	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'dew 10/7/2003 00:26'![39;49;00m$
  1678	[32mdeprecated:[39;49;00m [31manExplanationString[39;49;00m [32mblock:[39;49;00m [31maBlock[39;49;00m $
  1679		 [37m"Warn that the sender has been deprecated.  Answer the value of aBlock on resumption.  (Note that #deprecated: is usually the preferred method.)"[39;49;00m$
  1680	$
  1681		[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
  1682			[[04m[32mDeprecation[39;49;00m$
  1683				[32msignal:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m' has been deprecated. '[39;49;00m[32m,[39;49;00m [31manExplanationString[39;49;00m].$
  1684		^ [31maBlock[39;49;00m [32mvalue[39;49;00m.$
  1685	[34m! ![39;49;00m$
  1686	$
  1687	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'md 2/22/2006 21:21'![39;49;00m$
  1688	[32mdoesNotUnderstand:[39;49;00m [31maMessage[39;49;00m $
  1689		 [37m"Handle the fact that there was an attempt to send the given message to the receiver but the receiver does not understand this message (typically sent from the machine when a message is sent to the receiver and no method is defined for that selector)."[39;49;00m$
  1690		[37m"Testing: (3 activeProcess)"[39;49;00m$
  1691	$
  1692		[04m[32mMessageNotUnderstood[39;49;00m [36mnew[39;49;00m $
  1693			[32mmessage:[39;49;00m [31maMessage[39;49;00m;$
  1694			[32mreceiver:[39;49;00m [36mself[39;49;00m;$
  1695			[32msignal[39;49;00m.$
  1696		^ [31maMessage[39;49;00m [32msentTo:[39;49;00m [36mself[39;49;00m.$
  1697	[34m! ![39;49;00m$
  1698	$
  1699	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'TRee 11/4/2003 16:47'![39;49;00m$
  1700	[32mdpsTrace:[39;49;00m [31mreportObject[39;49;00m  $
  1701		[04m[32mTranscript[39;49;00m [32mmyDependents[39;49;00m [32misNil[39;49;00m [36mifTrue:[39;49;00m [^[36mself[39;49;00m].$
  1702		[36mself[39;49;00m [32mdpsTrace:[39;49;00m [31mreportObject[39;49;00m [32mlevels:[39;49;00m [34m1[39;49;00m [32mwithContext:[39;49;00m [36mthisContext[39;49;00m$
  1703			$
  1704	[37m" nil dpsTrace: 'sludder'. "[39;49;00m[34m! ![39;49;00m$
  1705	$
  1706	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'TRee 11/4/2003 16:49'![39;49;00m$
  1707	[32mdpsTrace:[39;49;00m [31mreportObject[39;49;00m [32mlevels:[39;49;00m [31manInt[39;49;00m$
  1708		[36mself[39;49;00m [32mdpsTrace:[39;49;00m [31mreportObject[39;49;00m [32mlevels:[39;49;00m [31manInt[39;49;00m [32mwithContext:[39;49;00m [36mthisContext[39;49;00m$
  1709	$
  1710	[37m"(1 to: 3) do: [:int | nil dpsTrace: int levels: 5.]"[39;49;00m[34m! ![39;49;00m$
  1711	$
  1712	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'TRee 11/4/2003 17:02'![39;49;00m$
  1713	[32mdpsTrace:[39;49;00m [31mreportObject[39;49;00m [32mlevels:[39;49;00m [31manInt[39;49;00m [32mwithContext:[39;49;00m [31mcurrentContext[39;49;00m$
  1714		|[31m reportString context displayCount [39;49;00m|$
  1715		[31mreportString[39;49;00m := ([31mreportObject[39;49;00m [32mrespondsTo:[39;49;00m [33m#asString[39;49;00m) $
  1716				[36mifTrue:[39;49;00m [[31mreportObject[39;49;00m [32masString[39;49;00m] [36mifFalse:[39;49;00m [[31mreportObject[39;49;00m [32mprintString[39;49;00m].$
  1717		([04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#Decompiler[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m]) $
  1718		[32mifNil:[39;49;00m $
  1719			[[04m[32mTranscript[39;49;00m [32mcr[39;49;00m; [32mshow:[39;49;00m [31mreportString[39;49;00m]$
  1720		[32mifNotNil:[39;49;00m$
  1721			[[31mcontext[39;49;00m := [31mcurrentContext[39;49;00m.$
  1722			[31mdisplayCount[39;49;00m := [31manInt[39;49;00m [32m>[39;49;00m [34m1[39;49;00m.$
  1723			[34m1[39;49;00m [32mto:[39;49;00m [31manInt[39;49;00m [32mdo:[39;49;00m$
  1724				[:[31mcount[39;49;00m |$
  1725				[04m[32mTranscript[39;49;00m [32mcr[39;49;00m.$
  1726				[31mdisplayCount[39;49;00m$
  1727					[36mifTrue:[39;49;00m [[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m [31mcount[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m': '[39;49;00m].$
  1728				$
  1729				[31mreportString[39;49;00m [32mnotNil[39;49;00m$
  1730				[36mifTrue:[39;49;00m$
  1731					[[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m [31mcontext[39;49;00m [32mhome[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m $
  1732				[32m,[39;49;00m [33m'/'[39;49;00m [32m,[39;49;00m [31mcontext[39;49;00m [32msender[39;49;00m [32mselector[39;49;00m[32m,[39;49;00m  [33m' ('[39;49;00m [32m,[39;49;00m [31mreportString[39;49;00m [32m,[39;49;00m [33m')'[39;49;00m.$
  1733					[31mcontext[39;49;00m := [31mcontext[39;49;00m [32msender[39;49;00m.$
  1734					[31mreportString[39;49;00m := [36mnil[39;49;00m]$
  1735				[36mifFalse:[39;49;00m$
  1736					[([31mcontext[39;49;00m [32mnotNil[39;49;00m [32mand:[39;49;00m [([31mcontext[39;49;00m := [31mcontext[39;49;00m [32msender[39;49;00m) [32mnotNil[39;49;00m])$
  1737					[36mifTrue:[39;49;00m [[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m [31mcontext[39;49;00m [32mreceiver[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32m,[39;49;00m [33m'/'[39;49;00m [32m,[39;49;00m [31mcontext[39;49;00m [32mselector[39;49;00m]]].$
  1738			[37m"Transcript cr"[39;49;00m].[34m! ![39;49;00m$
  1739	$
  1740	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'md 8/2/2005 22:17'![39;49;00m$
  1741	[32merror[39;49;00m$
  1742		[37m"Throw a generic Error exception."[39;49;00m$
  1743	$
  1744		^[36mself[39;49;00m [32merror:[39;49;00m [33m'Error!!'[39;49;00m.[34m! ![39;49;00m$
  1745	$
  1746	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'tfei 4/12/1999 12:55'![39;49;00m$
  1747	[32merror:[39;49;00m [31maString[39;49;00m $
  1748		[37m"Throw a generic Error exception."[39;49;00m$
  1749	$
  1750		^[04m[32mError[39;49;00m [36mnew[39;49;00m [32msignal:[39;49;00m [31maString[39;49;00m[34m! ![39;49;00m$
  1751	$
  1752	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'al 9/16/2005 14:12'![39;49;00m$
  1753	[32mexplicitRequirement[39;49;00m$
  1754		[36mself[39;49;00m [32merror:[39;49;00m [33m'Explicitly required method'[39;49;00m[34m! ![39;49;00m$
  1755	$
  1756	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'al 2/13/2006 22:20'![39;49;00m$
  1757	[32mhalt[39;49;00m$
  1758		[37m"This is the typical message to use for inserting breakpoints during [39;49;00m$
  1759	[37m	debugging. It behaves like halt:, but does not call on halt: in order to [39;49;00m$
  1760	[37m	avoid putting this message on the stack. Halt is especially useful when [39;49;00m$
  1761	[37m	the breakpoint message is an arbitrary one."[39;49;00m$
  1762	$
  1763		[04m[32mHalt[39;49;00m [32msignal[39;49;00m[34m! ![39;49;00m$
  1764	$
  1765	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'tfei 4/12/1999 12:59'![39;49;00m$
  1766	[32mhalt:[39;49;00m [31maString[39;49;00m $
  1767		[37m"This is the typical message to use for inserting breakpoints during [39;49;00m$
  1768	[37m	debugging. It creates and schedules a Notifier with the argument, [39;49;00m$
  1769	[37m	aString, as the label."[39;49;00m$
  1770		$
  1771		[04m[32mHalt[39;49;00m [36mnew[39;49;00m [32msignal:[39;49;00m [31maString[39;49;00m[34m! ![39;49;00m$
  1772	$
  1773	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:24'![39;49;00m$
  1774	[32mhandles:[39;49;00m [31mexception[39;49;00m$
  1775		[37m"This method exists in case a non exception class is the first arg in an on:do: (for instance using a exception class that is not loaded). We prefer this to raising an error during error handling itself. Also, semantically it makes sense that the exception handler is not active if its exception class is not loaded"[39;49;00m$
  1776	$
  1777		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  1778	$
  1779	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'ar 9/27/2005 20:24'![39;49;00m$
  1780	[32mnotifyWithLabel:[39;49;00m [31maString[39;49;00m $
  1781		[37m"Create and schedule a Notifier with aString as the window label as well as the contents of the window, in  order to request confirmation before a process can proceed."[39;49;00m$
  1782	$
  1783		[04m[32mToolSet[39;49;00m$
  1784			[32mdebugContext:[39;49;00m [36mthisContext[39;49;00m$
  1785			[32mlabel:[39;49;00m [31maString[39;49;00m$
  1786			[32mcontents:[39;49;00m [31maString[39;49;00m$
  1787	$
  1788		[37m"nil notifyWithLabel: 'let us see if this works'"[39;49;00m[34m! ![39;49;00m$
  1789	$
  1790	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'hg 10/2/2001 20:49'![39;49;00m$
  1791	[32mnotify:[39;49;00m [31maString[39;49;00m $
  1792		[37m"Create and schedule a Notifier with the argument as the message in [39;49;00m$
  1793	[37m	order to request confirmation before a process can proceed."[39;49;00m$
  1794	$
  1795		[04m[32mWarning[39;49;00m [32msignal:[39;49;00m [31maString[39;49;00m$
  1796	$
  1797		[37m"nil notify: 'confirmation message'"[39;49;00m[34m! ![39;49;00m$
  1798	$
  1799	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m![39;49;00m$
  1800	[32mnotify:[39;49;00m [31maString[39;49;00m [32mat:[39;49;00m [31mlocation[39;49;00m$
  1801		[37m"Create and schedule a Notifier with the argument as the message in [39;49;00m$
  1802	[37m	order to request confirmation before a process can proceed. Subclasses can[39;49;00m$
  1803	[37m	override this and insert an error message at location within aString."[39;49;00m$
  1804	$
  1805		[36mself[39;49;00m [32mnotify:[39;49;00m [31maString[39;49;00m$
  1806	$
  1807		[37m"nil notify: 'confirmation message' at: 12"[39;49;00m[34m! ![39;49;00m$
  1808	$
  1809	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m![39;49;00m$
  1810	[32mprimitiveFailed[39;49;00m$
  1811		[37m"Announce that a primitive has failed and there is no appropriate [39;49;00m$
  1812	[37m	Smalltalk code to run."[39;49;00m$
  1813	$
  1814		[36mself[39;49;00m [32merror:[39;49;00m [33m'a primitive has failed'[39;49;00m[34m! ![39;49;00m$
  1815	$
  1816	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'al 9/16/2005 14:12'![39;49;00m$
  1817	[32mrequirement[39;49;00m$
  1818		[36mself[39;49;00m [32merror:[39;49;00m [33m'Implicitly required method'[39;49;00m[34m! ![39;49;00m$
  1819	$
  1820	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'AFi 2/8/2003 22:52'![39;49;00m$
  1821	[32mshouldBeImplemented[39;49;00m$
  1822		[37m"Announce that this message should be implemented"[39;49;00m$
  1823	$
  1824		[36mself[39;49;00m [32merror:[39;49;00m [33m'This message should be implemented'[39;49;00m[34m! ![39;49;00m$
  1825	$
  1826	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m![39;49;00m$
  1827	[32mshouldNotImplement[39;49;00m$
  1828		[37m"Announce that, although the receiver inherits this message, it should [39;49;00m$
  1829	[37m	not implement it."[39;49;00m$
  1830	$
  1831		[36mself[39;49;00m [32merror:[39;49;00m [33m'This message is not appropriate for this object'[39;49;00m[34m! ![39;49;00m$
  1832	$
  1833	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'md 2/17/2006 12:02'![39;49;00m$
  1834	[32msubclassResponsibility[39;49;00m$
  1835		[37m"This message sets up a framework for the behavior of the class' subclasses.[39;49;00m$
  1836	[37m	Announce that the subclass should have implemented this message."[39;49;00m$
  1837	$
  1838		[36mself[39;49;00m [32merror:[39;49;00m [33m'My subclass should have overridden '[39;49;00m[32m,[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mselector[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
  1839	$
  1840	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'al 12/16/2003 16:16'![39;49;00m$
  1841	[32mtraitConflict[39;49;00m$
  1842		[36mself[39;49;00m [32merror:[39;49;00m [33m'A class or trait does not properly resolve a conflict between multiple traits it uses.'[39;49;00m[34m! ![39;49;00m$
  1843	$
  1844	$
  1845	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'evaluating'[39;49;00m[34m stamp: 'reThink 3/12/2001 18:14'![39;49;00m$
  1846	[32mvalue[39;49;00m$
  1847	$
  1848		^[36mself[39;49;00m[34m! ![39;49;00m$
  1849	$
  1850	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'evaluating'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:23'![39;49;00m$
  1851	[32mvalueWithArguments:[39;49;00m [31maSequenceOfArguments[39;49;00m$
  1852	$
  1853		^[36mself[39;49;00m[34m! ![39;49;00m$
  1854	$
  1855	$
  1856	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events'[39;49;00m[34m stamp: 'nk 8/27/2003 16:23'![39;49;00m$
  1857	[32mactionsWithReceiver:[39;49;00m [31manObject[39;49;00m [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m$
  1858	$
  1859		^([36mself[39;49;00m [32mactionSequenceForEvent:[39;49;00m [31manEventSelector[39;49;00m)$
  1860	                [32mselect:[39;49;00m [:[31manAction[39;49;00m | [31manAction[39;49;00m [32mreceiver[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m ][34m! ![39;49;00m$
  1861	$
  1862	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events'[39;49;00m[34m stamp: 'nk 8/27/2003 17:45'![39;49;00m$
  1863	[32mrenameActionsWithReceiver:[39;49;00m [31manObject[39;49;00m [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m [32mtoEvent:[39;49;00m [31mnewEvent[39;49;00m$
  1864	$
  1865		|[31m oldActions newActions [39;49;00m|$
  1866		[31moldActions[39;49;00m _ [04m[32mSet[39;49;00m [36mnew[39;49;00m.$
  1867		[31mnewActions[39;49;00m _ [04m[32mSet[39;49;00m [36mnew[39;49;00m.$
  1868		([36mself[39;49;00m [32mactionSequenceForEvent:[39;49;00m [31manEventSelector[39;49;00m) [32mdo:[39;49;00m [ :[31maction[39;49;00m |$
  1869			[31maction[39;49;00m [32mreceiver[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m$
  1870				[36mifTrue:[39;49;00m [ [31moldActions[39;49;00m [32madd:[39;49;00m [31manObject[39;49;00m ]$
  1871				[36mifFalse:[39;49;00m [ [31mnewActions[39;49;00m [32madd:[39;49;00m [31manObject[39;49;00m ]].$
  1872		[36mself[39;49;00m [32msetActionSequence:[39;49;00m ([04m[32mActionSequence[39;49;00m [32mwithAll:[39;49;00m [31mnewActions[39;49;00m) [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m.$
  1873		[31moldActions[39;49;00m [32mdo:[39;49;00m [ :[31mact[39;49;00m | [36mself[39;49;00m [32mwhen:[39;49;00m [31mnewEvent[39;49;00m [32mevaluate:[39;49;00m [31mact[39;49;00m ].[34m! ![39;49;00m$
  1874	$
  1875	$
  1876	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'nk 12/20/2002 17:48'![39;49;00m$
  1877	[32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m$
  1878	    [37m"Answer the action to be evaluated when <anEventSelector> has been triggered."[39;49;00m$
  1879	$
  1880		|[31m actions [39;49;00m|$
  1881		[31mactions[39;49;00m := [36mself[39;49;00m [32mactionMap[39;49;00m$
  1882			[32mat:[39;49;00m [31manEventSelector[39;49;00m [32masSymbol[39;49;00m$
  1883			[32mifAbsent:[39;49;00m [[36mnil[39;49;00m].$
  1884		[31mactions[39;49;00m [32mifNil:[39;49;00m [^[36mnil[39;49;00m].$
  1885		^ [31mactions[39;49;00m [32masMinimalRepresentation[39;49;00m[34m! ![39;49;00m$
  1886	$
  1887	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'nk 12/20/2002 17:48'![39;49;00m$
  1888	[32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m$
  1889	[32mifAbsent:[39;49;00m [31manExceptionBlock[39;49;00m$
  1890	    [37m"Answer the action to be evaluated when <anEventSelector> has been triggered."[39;49;00m$
  1891	$
  1892		|[31m actions [39;49;00m|$
  1893		[31mactions[39;49;00m := [36mself[39;49;00m [32mactionMap[39;49;00m$
  1894			[32mat:[39;49;00m [31manEventSelector[39;49;00m [32masSymbol[39;49;00m$
  1895			[32mifAbsent:[39;49;00m [[36mnil[39;49;00m].$
  1896		[31mactions[39;49;00m [32mifNil:[39;49;00m [^[31manExceptionBlock[39;49;00m [32mvalue[39;49;00m].$
  1897		^ [31mactions[39;49;00m [32masMinimalRepresentation[39;49;00m[34m! ![39;49;00m$
  1898	$
  1899	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'reThink 2/18/2001 14:43'![39;49;00m$
  1900	[32mactionMap[39;49;00m$
  1901	$
  1902		^[04m[32mEventManager[39;49;00m [32mactionMapFor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  1903	$
  1904	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'rw 4/27/2002 08:35'![39;49;00m$
  1905	[32mactionSequenceForEvent:[39;49;00m [31manEventSelector[39;49;00m$
  1906	$
  1907	    ^([36mself[39;49;00m [32mactionMap[39;49;00m$
  1908	        [32mat:[39;49;00m [31manEventSelector[39;49;00m [32masSymbol[39;49;00m$
  1909	        [32mifAbsent:[39;49;00m [^[04m[32mWeakActionSequence[39;49;00m [36mnew[39;49;00m])$
  1910	            [32masActionSequence[39;49;00m[34m! ![39;49;00m$
  1911	$
  1912	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'SqR 6/28/2001 13:19'![39;49;00m$
  1913	[32mactionsDo:[39;49;00m [31maBlock[39;49;00m$
  1914	$
  1915		[36mself[39;49;00m [32mactionMap[39;49;00m [32mdo:[39;49;00m [31maBlock[39;49;00m[34m! ![39;49;00m$
  1916	$
  1917	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'rw 2/10/2002 13:05'![39;49;00m$
  1918	[32mcreateActionMap[39;49;00m$
  1919	$
  1920		^[04m[32mIdentityDictionary[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
  1921	$
  1922	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'SqR 2/19/2001 14:04'![39;49;00m$
  1923	[32mhasActionForEvent:[39;49;00m [31manEventSelector[39;49;00m$
  1924	    [37m"Answer true if there is an action associated with anEventSelector"[39;49;00m$
  1925	$
  1926	    ^([36mself[39;49;00m [32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m) [32mnotNil[39;49;00m[34m! ![39;49;00m$
  1927	$
  1928	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:29'![39;49;00m$
  1929	[32msetActionSequence:[39;49;00m [31mactionSequence[39;49;00m$
  1930	[32mforEvent:[39;49;00m [31manEventSelector[39;49;00m$
  1931	$
  1932	    |[31m action [39;49;00m|$
  1933	    [31maction[39;49;00m := [31mactionSequence[39;49;00m [32masMinimalRepresentation[39;49;00m.$
  1934	    [31maction[39;49;00m [32m==[39;49;00m [36mnil[39;49;00m$
  1935	        [36mifTrue:[39;49;00m$
  1936	            [[36mself[39;49;00m [32mremoveActionsForEvent:[39;49;00m [31manEventSelector[39;49;00m]$
  1937	        [36mifFalse:[39;49;00m$
  1938	            [[36mself[39;49;00m [32mupdateableActionMap[39;49;00m$
  1939	                [32mat:[39;49;00m [31manEventSelector[39;49;00m [32masSymbol[39;49;00m$
  1940	                [32mput:[39;49;00m [31maction[39;49;00m][34m! ![39;49;00m$
  1941	$
  1942	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'reThink 2/25/2001 08:50'![39;49;00m$
  1943	[32mupdateableActionMap[39;49;00m$
  1944	$
  1945		^[04m[32mEventManager[39;49;00m [32mupdateableActionMapFor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  1946	$
  1947	$
  1948	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-registering'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:04'![39;49;00m$
  1949	[32mwhen:[39;49;00m [31manEventSelector[39;49;00m [32mevaluate:[39;49;00m [31manAction[39;49;00m $
  1950	$
  1951		|[31m actions [39;49;00m|$
  1952		[31mactions[39;49;00m := [36mself[39;49;00m [32mactionSequenceForEvent:[39;49;00m [31manEventSelector[39;49;00m.$
  1953		([31mactions[39;49;00m [32mincludes:[39;49;00m [31manAction[39;49;00m)$
  1954			[36mifTrue:[39;49;00m [^ [36mself[39;49;00m].$
  1955		[36mself[39;49;00m $
  1956			[32msetActionSequence:[39;49;00m ([31mactions[39;49;00m [32mcopyWith:[39;49;00m [31manAction[39;49;00m)$
  1957			[32mforEvent:[39;49;00m [31manEventSelector[39;49;00m[34m! ![39;49;00m$
  1958	$
  1959	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-registering'[39;49;00m[34m stamp: 'rww 12/30/2002 10:37'![39;49;00m$
  1960	[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
  1961	[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
  1962	[32mto:[39;49;00m [31manObject[39;49;00m$
  1963	 $
  1964	    [36mself[39;49;00m$
  1965	        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
  1966	        [32mevaluate:[39;49;00m ([04m[32mWeakMessageSend[39;49;00m$
  1967	            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
  1968	            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m)[34m! ![39;49;00m$
  1969	$
  1970	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-registering'[39;49;00m[34m stamp: 'rww 12/30/2002 10:37'![39;49;00m$
  1971	[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
  1972	[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
  1973	[32mto:[39;49;00m [31manObject[39;49;00m$
  1974	[32mwithArguments:[39;49;00m [31manArgArray[39;49;00m$
  1975	 $
  1976	    [36mself[39;49;00m$
  1977	        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
  1978	        [32mevaluate:[39;49;00m ([04m[32mWeakMessageSend[39;49;00m$
  1979	            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
  1980	            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
  1981			[32marguments:[39;49;00m [31manArgArray[39;49;00m)[34m! ![39;49;00m$
  1982	$
  1983	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-registering'[39;49;00m[34m stamp: 'rww 12/30/2002 10:37'![39;49;00m$
  1984	[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
  1985	[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
  1986	[32mto:[39;49;00m [31manObject[39;49;00m$
  1987	[32mwith:[39;49;00m [31manArg[39;49;00m$
  1988	 $
  1989	    [36mself[39;49;00m$
  1990	        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
  1991	        [32mevaluate:[39;49;00m ([04m[32mWeakMessageSend[39;49;00m$
  1992	            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
  1993	            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
  1994			[32marguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manArg[39;49;00m))[34m! ![39;49;00m$
  1995	$
  1996	$
  1997	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:33'![39;49;00m$
  1998	[32mreleaseActionMap[39;49;00m$
  1999	$
  2000		[04m[32mEventManager[39;49;00m [32mreleaseActionMapFor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  2001	$
  2002	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:33'![39;49;00m$
  2003	[32mremoveActionsForEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2004	$
  2005	    |[31m map [39;49;00m|$
  2006	    [31mmap[39;49;00m := [36mself[39;49;00m [32mactionMap[39;49;00m.$
  2007	    [31mmap[39;49;00m [32mremoveKey:[39;49;00m [31manEventSelector[39;49;00m [32masSymbol[39;49;00m [32mifAbsent:[39;49;00m [].$
  2008	    [31mmap[39;49;00m [32misEmpty[39;49;00m$
  2009	        [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mreleaseActionMap[39;49;00m][34m! ![39;49;00m$
  2010	$
  2011	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'nk 8/25/2003 21:46'![39;49;00m$
  2012	[32mremoveActionsSatisfying:[39;49;00m [31maBlock[39;49;00m$
  2013	$
  2014		[36mself[39;49;00m [32mactionMap[39;49;00m [32mkeys[39;49;00m [32mdo:[39;49;00m$
  2015			[:[31meachEventSelector[39;49;00m |$
  2016				[36mself[39;49;00m$
  2017	   				[32mremoveActionsSatisfying:[39;49;00m [31maBlock[39;49;00m$
  2018					[32mforEvent:[39;49;00m [31meachEventSelector[39;49;00m$
  2019			][34m! ![39;49;00m$
  2020	$
  2021	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:31'![39;49;00m$
  2022	[32mremoveActionsSatisfying:[39;49;00m [31maOneArgBlock[39;49;00m $
  2023	[32mforEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2024	$
  2025	    [36mself[39;49;00m$
  2026	        [32msetActionSequence:[39;49;00m$
  2027	            (([36mself[39;49;00m [32mactionSequenceForEvent:[39;49;00m [31manEventSelector[39;49;00m)$
  2028	                [32mreject:[39;49;00m [:[31manAction[39;49;00m | [31maOneArgBlock[39;49;00m [32mvalue:[39;49;00m [31manAction[39;49;00m])$
  2029	        [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m[34m! ![39;49;00m$
  2030	$
  2031	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'rw 7/29/2003 17:18'![39;49;00m$
  2032	[32mremoveActionsWithReceiver:[39;49;00m [31manObject[39;49;00m$
  2033	$
  2034		[36mself[39;49;00m [32mactionMap[39;49;00m [32mcopy[39;49;00m [32mkeysDo:[39;49;00m$
  2035			[:[31meachEventSelector[39;49;00m |$
  2036				[36mself[39;49;00m$
  2037	   				[32mremoveActionsSatisfying:[39;49;00m [:[31manAction[39;49;00m | [31manAction[39;49;00m [32mreceiver[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m]$
  2038					[32mforEvent:[39;49;00m [31meachEventSelector[39;49;00m$
  2039			][34m! ![39;49;00m$
  2040	$
  2041	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:36'![39;49;00m$
  2042	[32mremoveActionsWithReceiver:[39;49;00m [31manObject[39;49;00m$
  2043	[32mforEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2044	$
  2045	    [36mself[39;49;00m$
  2046	        [32mremoveActionsSatisfying:[39;49;00m$
  2047	            [:[31manAction[39;49;00m |$
  2048	            [31manAction[39;49;00m [32mreceiver[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m]$
  2049	        [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m[34m! ![39;49;00m$
  2050	$
  2051	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:31'![39;49;00m$
  2052	[32mremoveAction:[39;49;00m [31manAction[39;49;00m$
  2053	[32mforEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2054	$
  2055	    [36mself[39;49;00m$
  2056	        [32mremoveActionsSatisfying:[39;49;00m [:[31maction[39;49;00m | [31maction[39;49;00m [32m=[39;49;00m [31manAction[39;49;00m]$
  2057	        [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m[34m! ![39;49;00m$
  2058	$
  2059	$
  2060	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:22'![39;49;00m$
  2061	[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2062		[37m"Evaluate all actions registered for <anEventSelector>. Return the value of the last registered action."[39;49;00m$
  2063	$
  2064	    ^([36mself[39;49;00m [32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m) [32mvalue[39;49;00m[34m! ![39;49;00m$
  2065	$
  2066	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 17:09'![39;49;00m$
  2067	[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2068	[32mifNotHandled:[39;49;00m [31manExceptionBlock[39;49;00m$
  2069		[37m"Evaluate all actions registered for <anEventSelector>. Return the value of the last registered action."[39;49;00m$
  2070	$
  2071	    ^([36mself[39;49;00m $
  2072			[32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2073			[32mifAbsent:[39;49;00m [^[31manExceptionBlock[39;49;00m [32mvalue[39;49;00m]) [32mvalue[39;49;00m$
  2074	[34m! ![39;49;00m$
  2075	$
  2076	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:21'![39;49;00m$
  2077	[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2078	[32mwithArguments:[39;49;00m [31manArgumentList[39;49;00m$
  2079	$
  2080	    ^([36mself[39;49;00m [32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m)$
  2081	        [32mvalueWithArguments:[39;49;00m [31manArgumentList[39;49;00m[34m! ![39;49;00m$
  2082	$
  2083	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:21'![39;49;00m$
  2084	[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2085	[32mwithArguments:[39;49;00m [31manArgumentList[39;49;00m$
  2086	[32mifNotHandled:[39;49;00m [31manExceptionBlock[39;49;00m$
  2087	$
  2088	    ^([36mself[39;49;00m $
  2089			[32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2090			[32mifAbsent:[39;49;00m [^[31manExceptionBlock[39;49;00m [32mvalue[39;49;00m])$
  2091	        [32mvalueWithArguments:[39;49;00m [31manArgumentList[39;49;00m[34m! ![39;49;00m$
  2092	$
  2093	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 14:59'![39;49;00m$
  2094	[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2095	[32mwith:[39;49;00m [31manObject[39;49;00m$
  2096	$
  2097	    ^[36mself[39;49;00m $
  2098			[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2099			[32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m)[34m! ![39;49;00m$
  2100	$
  2101	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 14:59'![39;49;00m$
  2102	[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2103	[32mwith:[39;49;00m [31manObject[39;49;00m$
  2104	[32mifNotHandled:[39;49;00m [31manExceptionBlock[39;49;00m$
  2105	$
  2106	    ^[36mself[39;49;00m $
  2107			[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2108			[32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m)$
  2109			[32mifNotHandled:[39;49;00m [31manExceptionBlock[39;49;00m[34m! ![39;49;00m$
  2110	$
  2111	$
  2112	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 00:42'![39;49;00m$
  2113	[32mbyteEncode:[39;49;00m[31maStream[39;49;00m$
  2114		[36mself[39;49;00m [32mflattenOnStream:[39;49;00m[31maStream[39;49;00m.$
  2115	[34m! ![39;49;00m$
  2116	$
  2117	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m![39;49;00m$
  2118	[32mdrawOnCanvas:[39;49;00m[31maStream[39;49;00m$
  2119		[36mself[39;49;00m [32mflattenOnStream:[39;49;00m[31maStream[39;49;00m.$
  2120	[34m! ![39;49;00m$
  2121	$
  2122	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 01:31'![39;49;00m$
  2123	[32melementSeparator[39;49;00m$
  2124		^[36mnil[39;49;00m.[34m! ![39;49;00m$
  2125	$
  2126	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m![39;49;00m$
  2127	[32mencodePostscriptOn:[39;49;00m[31maStream[39;49;00m$
  2128		[36mself[39;49;00m [32mbyteEncode:[39;49;00m[31maStream[39;49;00m.$
  2129	[34m! ![39;49;00m$
  2130	$
  2131	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 00:07'![39;49;00m$
  2132	[32mflattenOnStream:[39;49;00m[31maStream[39;49;00m$
  2133		[36mself[39;49;00m [32mwriteOnFilterStream:[39;49;00m[31maStream[39;49;00m.$
  2134	[34m! ![39;49;00m$
  2135	$
  2136	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'mpw 6/22/1930 22:56'![39;49;00m$
  2137	[32mfullDrawPostscriptOn:[39;49;00m[31maStream[39;49;00m$
  2138		^[31maStream[39;49;00m [32mfullDraw:[39;49;00m[36mself[39;49;00m.$
  2139	[34m! ![39;49;00m$
  2140	$
  2141	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 01:51'![39;49;00m$
  2142	[32mprintOnStream:[39;49;00m[31maStream[39;49;00m$
  2143		[36mself[39;49;00m [32mbyteEncode:[39;49;00m[31maStream[39;49;00m.$
  2144	[34m! ![39;49;00m$
  2145	$
  2146	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 00:49'![39;49;00m$
  2147	[32mputOn:[39;49;00m[31maStream[39;49;00m$
  2148		^[31maStream[39;49;00m [32mnextPut:[39;49;00m[36mself[39;49;00m.$
  2149	[34m! ![39;49;00m$
  2150	$
  2151	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 01:53'![39;49;00m$
  2152	[32mstoreOnStream:[39;49;00m[31maStream[39;49;00m$
  2153		[36mself[39;49;00m [32mprintOnStream:[39;49;00m[31maStream[39;49;00m.$
  2154	[34m! ![39;49;00m$
  2155	$
  2156	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 00:06'![39;49;00m$
  2157	[32mwriteOnFilterStream:[39;49;00m[31maStream[39;49;00m$
  2158		[31maStream[39;49;00m [32mwriteObject:[39;49;00m[36mself[39;49;00m.$
  2159	[34m! ![39;49;00m$
  2160	$
  2161	$
  2162	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 3/21/98 16:26'![39;49;00m$
  2163	[32mactAsExecutor[39;49;00m$
  2164		[37m"Prepare the receiver to act as executor for any resources associated with it"[39;49;00m$
  2165		[36mself[39;49;00m [32mbreakDependents[39;49;00m[34m! ![39;49;00m$
  2166	$
  2167	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 3/20/98 22:19'![39;49;00m$
  2168	[32mexecutor[39;49;00m$
  2169		[37m"Return an object which can act as executor for finalization of the receiver"[39;49;00m$
  2170		^[36mself[39;49;00m [32mshallowCopy[39;49;00m [32mactAsExecutor[39;49;00m[34m! ![39;49;00m$
  2171	$
  2172	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 5/19/2003 20:10'![39;49;00m$
  2173	[32mfinalizationRegistry[39;49;00m$
  2174		[37m"Answer the finalization registry associated with the receiver."[39;49;00m$
  2175		^[04m[32mWeakRegistry[39;49;00m [32mdefault[39;49;00m[34m! ![39;49;00m$
  2176	$
  2177	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 3/21/98 16:27'![39;49;00m$
  2178	[32mfinalize[39;49;00m$
  2179		[37m"Finalize the resource associated with the receiver. This message should only be sent during the finalization process. There is NO garantuee that the resource associated with the receiver hasn't been free'd before so take care that you don't run into trouble - this all may happen with interrupt priority."[39;49;00m[34m! ![39;49;00m$
  2180	$
  2181	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 3/21/98 18:38'![39;49;00m$
  2182	[32mretryWithGC:[39;49;00m [31mexecBlock[39;49;00m [32muntil:[39;49;00m [31mtestBlock[39;49;00m$
  2183		[37m"Retry execBlock as long as testBlock returns false. Do an incremental GC after the first try, a full GC after the second try."[39;49;00m$
  2184		|[31m blockValue [39;49;00m|$
  2185		[31mblockValue[39;49;00m := [31mexecBlock[39;49;00m [32mvalue[39;49;00m.$
  2186		([31mtestBlock[39;49;00m [32mvalue:[39;49;00m [31mblockValue[39;49;00m) [36mifTrue:[39;49;00m[^[31mblockValue[39;49;00m].$
  2187		[04m[32mSmalltalk[39;49;00m [32mgarbageCollectMost[39;49;00m.$
  2188		[31mblockValue[39;49;00m := [31mexecBlock[39;49;00m [32mvalue[39;49;00m.$
  2189		([31mtestBlock[39;49;00m [32mvalue:[39;49;00m [31mblockValue[39;49;00m) [36mifTrue:[39;49;00m[^[31mblockValue[39;49;00m].$
  2190		[04m[32mSmalltalk[39;49;00m [32mgarbageCollect[39;49;00m.$
  2191		^[31mexecBlock[39;49;00m [32mvalue[39;49;00m.[34m! ![39;49;00m$
  2192	$
  2193	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 5/19/2003 20:14'![39;49;00m$
  2194	[32mtoFinalizeSend:[39;49;00m [31maSelector[39;49;00m [32mto:[39;49;00m [31maFinalizer[39;49;00m [32mwith:[39;49;00m [31maResourceHandle[39;49;00m$
  2195		[37m"When I am finalized (e.g., garbage collected) close the associated resource handle by sending aSelector to the appropriate finalizer (the guy who knows how to get rid of the resource).[39;49;00m$
  2196	[37m	WARNING: Neither the finalizer nor the resource handle are allowed to reference me. If they do, then I will NEVER be garbage collected. Since this cannot be validated here, it is up to the client to make sure this invariant is not broken."[39;49;00m$
  2197		[36mself[39;49;00m [32m==[39;49;00m [31maFinalizer[39;49;00m [36mifTrue:[39;49;00m[[36mself[39;49;00m [32merror:[39;49;00m [33m'I cannot finalize myself'[39;49;00m].$
  2198		[36mself[39;49;00m [32m==[39;49;00m [31maResourceHandle[39;49;00m [36mifTrue:[39;49;00m[[36mself[39;49;00m [32merror:[39;49;00m [33m'I cannot finalize myself'[39;49;00m].$
  2199		^[36mself[39;49;00m [32mfinalizationRegistry[39;49;00m [32madd:[39;49;00m [36mself[39;49;00m [32mexecutor:[39;49;00m$
  2200			([04m[32mObjectFinalizer[39;49;00m [36mnew[39;49;00m$
  2201				[32mreceiver:[39;49;00m [31maFinalizer[39;49;00m$
  2202				[32mselector:[39;49;00m [31maSelector[39;49;00m$
  2203				[32margument:[39;49;00m [31maResourceHandle[39;49;00m)[34m! ![39;49;00m$
  2204	$
  2205	$
  2206	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'flagging'[39;49;00m[34m stamp: 'sw 8/4/97 16:49'![39;49;00m$
  2207	[32misThisEverCalled[39;49;00m$
  2208		^ [36mself[39;49;00m [32misThisEverCalled:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
  2209	$
  2210	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'flagging'[39;49;00m[34m![39;49;00m$
  2211	[32misThisEverCalled:[39;49;00m [31mmsg[39;49;00m$
  2212		[37m"Send this message, with some useful printable argument, from methods or branches of methods which you believe are never reached.  2/5/96 sw"[39;49;00m$
  2213	$
  2214		[36mself[39;49;00m [32mhalt:[39;49;00m [33m'This is indeed called: '[39;49;00m[32m,[39;49;00m [31mmsg[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
  2215	$
  2216	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'flagging'[39;49;00m[34m stamp: 'jm 3/18/98 17:23'![39;49;00m$
  2217	[32mlogEntry[39;49;00m$
  2218	$
  2219		[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m [33m'Entered '[39;49;00m[32m,[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m; [32mcr[39;49;00m.$
  2220	[34m! ![39;49;00m$
  2221	$
  2222	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'flagging'[39;49;00m[34m stamp: 'jm 3/18/98 17:23'![39;49;00m$
  2223	[32mlogExecution[39;49;00m$
  2224	$
  2225		[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m [33m'Executing '[39;49;00m[32m,[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m; [32mcr[39;49;00m.$
  2226	[34m! ![39;49;00m$
  2227	$
  2228	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'flagging'[39;49;00m[34m stamp: 'jm 3/18/98 17:22'![39;49;00m$
  2229	[32mlogExit[39;49;00m$
  2230	$
  2231		[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m  [33m'Exited '[39;49;00m[32m,[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m; [32mcr[39;49;00m.$
  2232	[34m! ![39;49;00m$
  2233	$
  2234	$
  2235	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'graph model'[39;49;00m[34m stamp: 'dgd 9/18/2004 15:07'![39;49;00m$
  2236	[32maddModelYellowButtonMenuItemsTo:[39;49;00m [31maCustomMenu[39;49;00m [32mforMorph:[39;49;00m [31maMorph[39;49;00m [32mhand:[39;49;00m [31maHandMorph[39;49;00m $
  2237		[37m"The receiver serves as the model for aMorph; a menu is being constructed for the morph, and here the receiver is able to add its own items"[39;49;00m$
  2238		[04m[32mPreferences[39;49;00m [32mcmdGesturesEnabled[39;49;00m [36mifTrue:[39;49;00m [ [37m"build mode"[39;49;00m$
  2239			[31maCustomMenu[39;49;00m [32madd:[39;49;00m [33m'inspect model'[39;49;00m [32mtranslated[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32maction:[39;49;00m [33m#inspect[39;49;00m.$
  2240		].$
  2241	$
  2242		^[31maCustomMenu[39;49;00m$
  2243	[34m! ![39;49;00m$
  2244	$
  2245	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'graph model'[39;49;00m[34m stamp: 'nk 1/23/2004 14:35'![39;49;00m$
  2246	[32mhasModelYellowButtonMenuItems[39;49;00m$
  2247		^[04m[32mPreferences[39;49;00m [32mcmdGesturesEnabled[39;49;00m[34m! ![39;49;00m$
  2248	$
  2249	$
  2250	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'inspecting'[39;49;00m[34m stamp: 'ar 9/27/2005 18:31'![39;49;00m$
  2251	[32mbasicInspect[39;49;00m$
  2252		[37m"Create and schedule an Inspector in which the user can examine the [39;49;00m$
  2253	[37m	receiver's variables. This method should not be overriden."[39;49;00m$
  2254		^[04m[32mToolSet[39;49;00m [32mbasicInspect:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  2255	$
  2256	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'inspecting'[39;49;00m[34m stamp: 'md 1/18/2006 19:09'![39;49;00m$
  2257	[32minspect[39;49;00m$
  2258		[37m"Create and schedule an Inspector in which the user can examine the receiver's variables."[39;49;00m$
  2259		[04m[32mToolSet[39;49;00m [32minspect:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  2260	$
  2261	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'inspecting'[39;49;00m[34m stamp: 'apb 7/14/2004 12:19'![39;49;00m$
  2262	[32minspectorClass[39;49;00m$
  2263		[37m"Answer the class of the inspector to be used on the receiver.  Called by inspect; [39;49;00m$
  2264	[37m	use basicInspect to get a normal (less useful) type of inspector."[39;49;00m$
  2265	$
  2266		^ [04m[32mInspector[39;49;00m[34m! ![39;49;00m$
  2267	$
  2268	$
  2269	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'locales'[39;49;00m[34m stamp: 'tak 8/4/2005 14:55'![39;49;00m$
  2270	[32mlocaleChanged[39;49;00m$
  2271		[36mself[39;49;00m [32mshouldBeImplemented[39;49;00m[34m! ![39;49;00m$
  2272	$
  2273	$
  2274	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 5/7/1998 23:00'![39;49;00m$
  2275	[32mcodeStrippedOut:[39;49;00m [31mmessageString[39;49;00m$
  2276		[37m"When a method is stripped out for external release, it is replaced by a method that calls this"[39;49;00m$
  2277	$
  2278		[36mself[39;49;00m [32mhalt:[39;49;00m [33m'Code stripped out -- '[39;49;00m[32m,[39;49;00m [31mmessageString[39;49;00m[32m,[39;49;00m [33m'-- do not proceed.'[39;49;00m[34m! ![39;49;00m$
  2279	$
  2280	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 1/28/1999 17:31'![39;49;00m$
  2281	[32mcontentsChanged[39;49;00m$
  2282		[36mself[39;49;00m [32mchanged:[39;49;00m [33m#contents[39;49;00m[34m! ![39;49;00m$
  2283	$
  2284	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'ar 3/18/2001 00:03'![39;49;00m$
  2285	[32mcurrentEvent[39;49;00m$
  2286		[37m"Answer the current Morphic event.  This method never returns nil."[39;49;00m$
  2287		^[04m[32mActiveEvent[39;49;00m [32mifNil:[39;49;00m[[36mself[39;49;00m [32mcurrentHand[39;49;00m [32mlastEvent[39;49;00m][34m! ![39;49;00m$
  2288	$
  2289	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'nk 9/1/2004 10:41'![39;49;00m$
  2290	[32mcurrentHand[39;49;00m$
  2291		[37m"Return a usable HandMorph -- the one associated with the object's current environment.  This method will always return a hand, even if it has to conjure one up as a last resort.  If a particular hand is actually handling events at the moment (such as a remote hand or a ghost hand), it will be returned."[39;49;00m$
  2292	$
  2293		^[04m[32mActiveHand[39;49;00m [32mifNil:[39;49;00m [ [36mself[39;49;00m [32mcurrentWorld[39;49;00m [32mprimaryHand[39;49;00m ][34m! ![39;49;00m$
  2294	$
  2295	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 5/17/2001 12:08'![39;49;00m$
  2296	[32mcurrentVocabulary[39;49;00m$
  2297		[37m"Answer the currently-prevailing default vocabulary."[39;49;00m$
  2298	$
  2299		^ [04m[32mSmalltalk[39;49;00m [32misMorphic[39;49;00m [36mifTrue:[39;49;00m$
  2300				[[04m[32mActiveWorld[39;49;00m [32mcurrentVocabulary[39;49;00m]$
  2301			[36mifFalse:[39;49;00m$
  2302				[[04m[32mVocabulary[39;49;00m [32mfullVocabulary[39;49;00m][34m! ![39;49;00m$
  2303	$
  2304	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'ar 3/18/2001 00:08'![39;49;00m$
  2305	[32mcurrentWorld[39;49;00m$
  2306		[37m"Answer a morphic world that is the current UI focus.[39;49;00m$
  2307	[37m		If in an embedded world, it's that world.[39;49;00m$
  2308	[37m		If in a morphic project, it's that project's world.  [39;49;00m$
  2309	[37m		If in an mvc project, it is the topmost morphic-mvc-window's worldMorph. [39;49;00m$
  2310	[37m		If in an mvc project that has no morphic-mvc-windows, then it's just some existing worldmorph instance.[39;49;00m$
  2311	[37m		If in an mvc project in a Squeak that has NO WorldMorph instances, one is created.[39;49;00m$
  2312	[37m[39;49;00m$
  2313	[37m	This method will never return nil, it will always return its best effort at returning a relevant world morph, but if need be -- if there are no worlds anywhere, it will create a new one."[39;49;00m$
  2314	$
  2315		|[31m aView aSubview [39;49;00m|$
  2316		[04m[32mActiveWorld[39;49;00m [32mifNotNil:[39;49;00m[^[04m[32mActiveWorld[39;49;00m].$
  2317		[04m[32mWorld[39;49;00m [32mifNotNil:[39;49;00m[^[04m[32mWorld[39;49;00m].$
  2318		[31maView[39;49;00m _ [04m[32mScheduledControllers[39;49;00m [32mcontrollerSatisfying:[39;49;00m$
  2319			[:[31mctrl[39;49;00m | ([31maSubview[39;49;00m _ [31mctrl[39;49;00m [32mview[39;49;00m [32mfirstSubView[39;49;00m) [32mnotNil[39;49;00m [32mand:[39;49;00m$
  2320				[[31maSubview[39;49;00m [32mmodel[39;49;00m [32misMorph[39;49;00m [32mand:[39;49;00m [[31maSubview[39;49;00m [32mmodel[39;49;00m [32misWorldMorph[39;49;00m]]].$
  2321		^[31maView[39;49;00m$
  2322			[32mifNotNil:[39;49;00m$
  2323				[[31maSubview[39;49;00m [32mmodel[39;49;00m]$
  2324			[32mifNil:[39;49;00m$
  2325				[[04m[32mMVCWiWPasteUpMorph[39;49;00m [32mnewWorldForProject:[39;49;00m [36mnil[39;49;00m].[34m! ![39;49;00m$
  2326	$
  2327	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'jm 5/6/1998 22:35'![39;49;00m$
  2328	[32mflash[39;49;00m$
  2329		[37m"Do nothing."[39;49;00m$
  2330	[34m! ![39;49;00m$
  2331	$
  2332	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 6/16/1998 15:07'![39;49;00m$
  2333	[32minstanceVariableValues[39;49;00m$
  2334		[37m"Answer a collection whose elements are the values of those instance variables of the receiver which were added by the receiver's class"[39;49;00m$
  2335		|[31m c [39;49;00m|$
  2336		[31mc[39;49;00m _ [04m[32mOrderedCollection[39;49;00m [36mnew[39;49;00m.$
  2337		[36mself[39;49;00m [32mclass[39;49;00m [32msuperclass[39;49;00m [32minstSize[39;49;00m [32m+[39;49;00m [34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mdo:[39;49;00m$
  2338			[:[31mi[39;49;00m | [31mc[39;49;00m [32madd:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mi[39;49;00m)].$
  2339		^ [31mc[39;49;00m[34m! ![39;49;00m$
  2340	$
  2341	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 3/20/2001 13:29'![39;49;00m$
  2342	[32misUniversalTiles[39;49;00m$
  2343		[37m"Return true if I (my world) uses universal tiles.  This message can be called in places where the current World is not known, such as when writing out a project.  For more information about the project-writing subtlety addressed by this protocol, kindly contact Ted Kaehler."[39;49;00m$
  2344	$
  2345		^ [04m[32mPreferences[39;49;00m [32muniversalTiles[39;49;00m[34m! ![39;49;00m$
  2346	$
  2347	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 10/24/2000 07:04'![39;49;00m$
  2348	[32mobjectRepresented[39;49;00m$
  2349		[37m"most objects represent themselves; this provides a hook for aliases to grab on to"[39;49;00m$
  2350	$
  2351		^ [36mself[39;49;00m[34m! ![39;49;00m$
  2352	$
  2353	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 5/22/2001 18:31'![39;49;00m$
  2354	[32mrefusesToAcceptCode[39;49;00m$
  2355		[37m"Answer whether the receiver is a code-bearing instrument which at the moment refuses to allow its contents to be submitted"[39;49;00m$
  2356	$
  2357		^ [36mfalse[39;49;00m$
  2358		[34m! ![39;49;00m$
  2359	$
  2360	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'jm 2/24/1999 12:40'![39;49;00m$
  2361	[32mscriptPerformer[39;49;00m$
  2362	$
  2363		^ [36mself[39;49;00m$
  2364	[34m! ![39;49;00m$
  2365	$
  2366	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 3/20/2001 13:40'![39;49;00m$
  2367	[32mslotInfo[39;49;00m$
  2368		[37m"Answer a list of slot-information objects.  Initally only provides useful info for players"[39;49;00m$
  2369	$
  2370		^ [04m[32mDictionary[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
  2371	$
  2372	$
  2373	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:28'![39;49;00m$
  2374	[32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
  2375		[37m"Execute compiledMethod against the receiver with no args"[39;49;00m$
  2376	$
  2377		[37m"<primitive: 189>"[39;49;00m [37m"uncomment once prim 189 is in VM"[39;49;00m$
  2378		^ [36mself[39;49;00m [32mwithArgs:[39;49;00m [33m#([39;49;00m[33m)[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m[34m! ![39;49;00m$
  2379	$
  2380	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'di 3/26/1999 07:52'![39;49;00m$
  2381	[32mperform:[39;49;00m [31maSymbol[39;49;00m $
  2382		[37m"Send the unary selector, aSymbol, to the receiver.[39;49;00m$
  2383	[37m	Fail if the number of arguments expected by the selector is not zero.[39;49;00m$
  2384	[37m	Primitive. Optional. See Object documentation whatIsAPrimitive."[39;49;00m$
  2385	$
  2386		<[34mprimitive:[39;49;00m 83>$
  2387		^ [36mself[39;49;00m [32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mnew:[39;49;00m [34m0[39;49;00m)[34m! ![39;49;00m$
  2388	$
  2389	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'st 11/5/2004 16:19'![39;49;00m$
  2390	[32mperform:[39;49;00m [31mselector[39;49;00m [32morSendTo:[39;49;00m [31motherTarget[39;49;00m$
  2391		[37m"If I wish to intercept and handle selector myself, do it; else send it to otherTarget"[39;49;00m$
  2392		^ ([36mself[39;49;00m [32mrespondsTo:[39;49;00m [31mselector[39;49;00m) [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m] [36mifFalse:[39;49;00m [[31motherTarget[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m][34m! ![39;49;00m$
  2393	$
  2394	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'di 3/26/1999 07:55'![39;49;00m$
  2395	[32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31margArray[39;49;00m $
  2396		[37m"Send the selector, aSymbol, to the receiver with arguments in argArray.[39;49;00m$
  2397	[37m	Fail if the number of arguments expected by the selector [39;49;00m$
  2398	[37m	does not match the size of argArray.[39;49;00m$
  2399	[37m	Primitive. Optional. See Object documentation whatIsAPrimitive."[39;49;00m$
  2400	$
  2401		<[34mprimitive:[39;49;00m 84>$
  2402		^ [36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31margArray[39;49;00m [32minSuperclass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m[34m! ![39;49;00m$
  2403	$
  2404	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'ar 4/25/2005 13:35'![39;49;00m$
  2405	[32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31margArray[39;49;00m [32minSuperclass:[39;49;00m [31mlookupClass[39;49;00m$
  2406		[37m"NOTE:  This is just like perform:withArguments:, except that[39;49;00m$
  2407	[37m	the message lookup process begins, not with the receivers's class,[39;49;00m$
  2408	[37m	but with the supplied superclass instead.  It will fail if lookupClass[39;49;00m$
  2409	[37m	cannot be found among the receiver's superclasses.[39;49;00m$
  2410	[37m	Primitive. Essential. See Object documentation whatIsAPrimitive."[39;49;00m$
  2411	$
  2412		<[34mprimitive:[39;49;00m 100>$
  2413		([31mselector[39;49;00m [32misSymbol[39;49;00m)$
  2414			[36mifFalse:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'selector argument must be a Symbol'[39;49;00m].$
  2415		([31mselector[39;49;00m [32mnumArgs[39;49;00m [32m=[39;49;00m [31margArray[39;49;00m [32msize[39;49;00m)$
  2416			[36mifFalse:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'incorrect number of arguments'[39;49;00m].$
  2417		([36mself[39;49;00m [32mclass[39;49;00m [32m==[39;49;00m [31mlookupClass[39;49;00m [32mor:[39;49;00m [[36mself[39;49;00m [32mclass[39;49;00m [32minheritsFrom:[39;49;00m [31mlookupClass[39;49;00m])$
  2418			[36mifFalse:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'lookupClass is not in my inheritance chain'[39;49;00m].$
  2419		[36mself[39;49;00m [32mprimitiveFailed[39;49;00m[34m! ![39;49;00m$
  2420	$
  2421	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'nk 4/11/2002 14:13'![39;49;00m$
  2422	[32mperform:[39;49;00m [31mselector[39;49;00m [32mwithEnoughArguments:[39;49;00m [31manArray[39;49;00m$
  2423		[37m"Send the selector, aSymbol, to the receiver with arguments in argArray.[39;49;00m$
  2424	[37m	Only use enough arguments for the arity of the selector; supply nils for missing ones."[39;49;00m$
  2425		|[31m numArgs args [39;49;00m|$
  2426		[31mnumArgs[39;49;00m _ [31mselector[39;49;00m [32mnumArgs[39;49;00m.$
  2427		[31manArray[39;49;00m [32msize[39;49;00m [32m==[39;49;00m [31mnumArgs[39;49;00m$
  2428			[36mifTrue:[39;49;00m [ ^[36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31manArray[39;49;00m [32masArray[39;49;00m ].$
  2429	$
  2430		[31margs[39;49;00m _ [04m[32mArray[39;49;00m [32mnew:[39;49;00m [31mnumArgs[39;49;00m.$
  2431		[31margs[39;49;00m [32mreplaceFrom:[39;49;00m [34m1[39;49;00m$
  2432			[32mto:[39;49;00m ([31manArray[39;49;00m [32msize[39;49;00m [32mmin:[39;49;00m [31margs[39;49;00m [32msize[39;49;00m)$
  2433			[32mwith:[39;49;00m [31manArray[39;49;00m$
  2434			[32mstartingAt:[39;49;00m [34m1[39;49;00m.$
  2435	$
  2436		^ [36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31margs[39;49;00m[34m! ![39;49;00m$
  2437	$
  2438	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'di 3/26/1999 07:52'![39;49;00m$
  2439	[32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m $
  2440		[37m"Send the selector, aSymbol, to the receiver with anObject as its argument.[39;49;00m$
  2441	[37m	Fail if the number of arguments expected by the selector is not one.[39;49;00m$
  2442	[37m	Primitive. Optional. See Object documentation whatIsAPrimitive."[39;49;00m$
  2443	$
  2444		<[34mprimitive:[39;49;00m 83>$
  2445		^ [36mself[39;49;00m [32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m)[34m! ![39;49;00m$
  2446	$
  2447	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'di 3/26/1999 07:52'![39;49;00m$
  2448	[32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwith:[39;49;00m [31mfirstObject[39;49;00m [32mwith:[39;49;00m [31msecondObject[39;49;00m $
  2449		[37m"Send the selector, aSymbol, to the receiver with the given arguments.[39;49;00m$
  2450	[37m	Fail if the number of arguments expected by the selector is not two.[39;49;00m$
  2451	[37m	Primitive. Optional. See Object documentation whatIsAPrimitive."[39;49;00m$
  2452	$
  2453		<[34mprimitive:[39;49;00m 83>$
  2454		^ [36mself[39;49;00m [32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31mfirstObject[39;49;00m [32mwith:[39;49;00m [31msecondObject[39;49;00m)[34m! ![39;49;00m$
  2455	$
  2456	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'di 3/26/1999 07:51'![39;49;00m$
  2457	[32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwith:[39;49;00m [31mfirstObject[39;49;00m [32mwith:[39;49;00m [31msecondObject[39;49;00m [32mwith:[39;49;00m [31mthirdObject[39;49;00m $
  2458		[37m"Send the selector, aSymbol, to the receiver with the given arguments.[39;49;00m$
  2459	[37m	Fail if the number of arguments expected by the selector is not three.[39;49;00m$
  2460	[37m	Primitive. Optional. See Object documentation whatIsAPrimitive."[39;49;00m$
  2461	$
  2462		<[34mprimitive:[39;49;00m 83>$
  2463		^ [36mself[39;49;00m [32mperform:[39;49;00m [31maSymbol[39;49;00m$
  2464			[32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31mfirstObject[39;49;00m [32mwith:[39;49;00m [31msecondObject[39;49;00m [32mwith:[39;49;00m [31mthirdObject[39;49;00m)[34m! ![39;49;00m$
  2465	$
  2466	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'NS 1/28/2004 11:19'![39;49;00m$
  2467	[32mwithArgs:[39;49;00m [31margArray[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
  2468		[37m"Execute compiledMethod against the receiver and args in argArray"[39;49;00m$
  2469	$
  2470		|[31m selector [39;49;00m|$
  2471		<[34mprimitive:[39;49;00m 188>$
  2472		[31mselector[39;49;00m _ [04m[32mSymbol[39;49;00m [36mnew[39;49;00m.$
  2473		[36mself[39;49;00m [32mclass[39;49;00m [32maddSelectorSilently:[39;49;00m [31mselector[39;49;00m [32mwithMethod:[39;49;00m [31mcompiledMethod[39;49;00m.$
  2474		^ [[36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31margArray[39;49;00m]$
  2475			[32mensure:[39;49;00m [[36mself[39;49;00m [32mclass[39;49;00m [32mbasicRemoveSelector:[39;49;00m [31mselector[39;49;00m][34m! ![39;49;00m$
  2476	$
  2477	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:28'![39;49;00m$
  2478	[32mwith:[39;49;00m [31marg1[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
  2479		[37m"Execute compiledMethod against the receiver and arg1"[39;49;00m$
  2480	$
  2481		[37m"<primitive: 189>"[39;49;00m [37m"uncomment once prim 189 is in VM"[39;49;00m$
  2482		^ [36mself[39;49;00m [32mwithArgs:[39;49;00m {[31marg1[39;49;00m} [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m[34m! ![39;49;00m$
  2483	$
  2484	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:28'![39;49;00m$
  2485	[32mwith:[39;49;00m [31marg1[39;49;00m [32mwith:[39;49;00m [31marg2[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
  2486		[37m"Execute compiledMethod against the receiver and arg1 & arg2"[39;49;00m$
  2487	$
  2488		[37m"<primitive: 189>"[39;49;00m [37m"uncomment once prim 189 is in VM"[39;49;00m$
  2489		^ [36mself[39;49;00m [32mwithArgs:[39;49;00m {[31marg1[39;49;00m. [31marg2[39;49;00m} [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m[34m! ![39;49;00m$
  2490	$
  2491	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:28'![39;49;00m$
  2492	[32mwith:[39;49;00m [31marg1[39;49;00m [32mwith:[39;49;00m [31marg2[39;49;00m [32mwith:[39;49;00m [31marg3[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
  2493		[37m"Execute compiledMethod against the receiver and arg1, arg2, & arg3"[39;49;00m$
  2494	$
  2495		[37m"<primitive: 189>"[39;49;00m [37m"uncomment once prim 189 is in VM"[39;49;00m$
  2496		^ [36mself[39;49;00m [32mwithArgs:[39;49;00m {[31marg1[39;49;00m. [31marg2[39;49;00m. [31marg3[39;49;00m} [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m[34m! ![39;49;00m$
  2497	$
  2498	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:28'![39;49;00m$
  2499	[32mwith:[39;49;00m [31marg1[39;49;00m [32mwith:[39;49;00m [31marg2[39;49;00m [32mwith:[39;49;00m [31marg3[39;49;00m [32mwith:[39;49;00m [31marg4[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
  2500		[37m"Execute compiledMethod against the receiver and arg1, arg2, arg3, & arg4"[39;49;00m$
  2501	$
  2502		[37m"<primitive: 189>"[39;49;00m [37m"uncomment once prim 189 is in VM"[39;49;00m$
  2503		^ [36mself[39;49;00m [32mwithArgs:[39;49;00m {[31marg1[39;49;00m. [31marg2[39;49;00m. [31marg3[39;49;00m. [31marg4[39;49;00m} [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m[34m! ![39;49;00m$
  2504	$
  2505	$
  2506	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 4/8/1999 12:46'![39;49;00m$
  2507	[32mcomeFullyUpOnReload:[39;49;00m [31msmartRefStream[39;49;00m$
  2508		[37m"Normally this read-in object is exactly what we want to store. 7/26/96 tk"[39;49;00m$
  2509	$
  2510		^ [36mself[39;49;00m[34m! ![39;49;00m$
  2511	$
  2512	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'RAA 12/20/2000 16:51'![39;49;00m$
  2513	[32mconvertToCurrentVersion:[39;49;00m [31mvarDict[39;49;00m [32mrefStream:[39;49;00m [31msmartRefStrm[39;49;00m$
  2514	$
  2515		[37m"subclasses should implement if they wish to convert old instances to modern ones"[39;49;00m[34m! ![39;49;00m$
  2516	$
  2517	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 11/29/2004 15:04'![39;49;00m$
  2518	[32mfixUponLoad:[39;49;00m [31maProject[39;49;00m [32mseg:[39;49;00m [31manImageSegment[39;49;00m$
  2519		[37m"change the object due to conventions that have changed on[39;49;00m$
  2520	[37mthe project level.  (sent to all objects in the incoming project).[39;49;00m$
  2521	[37mSpecific classes should reimplement this."[39;49;00m[34m! ![39;49;00m$
  2522	$
  2523	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'RAA 1/10/2001 14:02'![39;49;00m$
  2524	[32mindexIfCompact[39;49;00m$
  2525	$
  2526		^[34m0[39;49;00m		[37m"helps avoid a #respondsTo: in publishing"[39;49;00m[34m! ![39;49;00m$
  2527	$
  2528	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 2/24/1999 11:08'![39;49;00m$
  2529	[32mobjectForDataStream:[39;49;00m [31mrefStrm[39;49;00m$
  2530	    [37m"Return an object to store on an external data stream."[39;49;00m$
  2531	$
  2532	    ^ [36mself[39;49;00m[34m! ![39;49;00m$
  2533	$
  2534	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 4/8/1999 12:05'![39;49;00m$
  2535	[32mreadDataFrom:[39;49;00m [31maDataStream[39;49;00m [32msize:[39;49;00m [31mvarsOnDisk[39;49;00m$
  2536		[37m"Fill in the fields of self based on the contents of aDataStream.  Return self.[39;49;00m$
  2537	[37m	 Read in the instance-variables written by Object>>storeDataOn:.[39;49;00m$
  2538	[37m	 NOTE: This method must send beginReference: before reading any objects from aDataStream that might reference it.[39;49;00m$
  2539	[37m	 Allow aDataStream to have fewer inst vars.  See SmartRefStream."[39;49;00m$
  2540		|[31m cntInstVars cntIndexedVars [39;49;00m|$
  2541	$
  2542		[31mcntInstVars[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m.$
  2543		[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m$
  2544			[36mifTrue:[39;49;00m [[31mcntIndexedVars[39;49;00m _ [31mvarsOnDisk[39;49;00m [32m-[39;49;00m [31mcntInstVars[39;49;00m.$
  2545					[31mcntIndexedVars[39;49;00m [32m<[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m [$
  2546						[36mself[39;49;00m [32merror:[39;49;00m [33m'Class has changed too much.  Define a convertxxx method'[39;49;00m]]$
  2547			[36mifFalse:[39;49;00m [[31mcntIndexedVars[39;49;00m _ [34m0[39;49;00m.$
  2548					[31mcntInstVars[39;49;00m _ [31mvarsOnDisk[39;49;00m]. 	[37m"OK if fewer than now"[39;49;00m$
  2549	$
  2550		[31maDataStream[39;49;00m [32mbeginReference:[39;49;00m [36mself[39;49;00m.$
  2551		[34m1[39;49;00m [32mto:[39;49;00m [31mcntInstVars[39;49;00m [32mdo:[39;49;00m$
  2552			[:[31mi[39;49;00m | [36mself[39;49;00m [32minstVarAt:[39;49;00m [31mi[39;49;00m [32mput:[39;49;00m [31maDataStream[39;49;00m [32mnext[39;49;00m].$
  2553		[34m1[39;49;00m [32mto:[39;49;00m [31mcntIndexedVars[39;49;00m [32mdo:[39;49;00m$
  2554			[:[31mi[39;49;00m | [36mself[39;49;00m [32mbasicAt:[39;49;00m [31mi[39;49;00m [32mput:[39;49;00m [31maDataStream[39;49;00m [32mnext[39;49;00m].$
  2555		[37m"Total number read MUST be equal to varsOnDisk!!"[39;49;00m$
  2556		^ [36mself[39;49;00m	[37m"If we ever return something other than self, fix calls [39;49;00m$
  2557	[37m			on (super readDataFrom: aDataStream size: anInteger)"[39;49;00m[34m! ![39;49;00m$
  2558	$
  2559	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'CdG 10/17/2005 20:32'![39;49;00m$
  2560	[32msaveOnFile[39;49;00m$
  2561		[37m"Ask the user for a filename and save myself on a SmartReferenceStream file.  Writes out the version and class structure.  The file is fileIn-able.  Does not file out the class of the object.  tk 6/26/97 13:48"[39;49;00m$
  2562	$
  2563		|[31m aFileName fileStream [39;49;00m|$
  2564		[31maFileName[39;49;00m := [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32masFileName[39;49;00m.	[37m"do better?"[39;49;00m$
  2565		[31maFileName[39;49;00m := [04m[32mUIManager[39;49;00m [32mdefault[39;49;00m $
  2566					[32mrequest:[39;49;00m [33m'File name?'[39;49;00m [32mtranslated[39;49;00m [32minitialAnswer:[39;49;00m [31maFileName[39;49;00m.$
  2567		[31maFileName[39;49;00m [32msize[39;49;00m [32m==[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m [^ [04m[32mBeeper[39;49;00m [32mbeep[39;49;00m].$
  2568	$
  2569		[31mfileStream[39;49;00m := [04m[32mFileStream[39;49;00m [32mnewFileNamed:[39;49;00m [31maFileName[39;49;00m [32masFileName[39;49;00m.$
  2570		[31mfileStream[39;49;00m [32mfileOutClass:[39;49;00m [36mnil[39;49;00m [32mandObject:[39;49;00m [36mself[39;49;00m.[34m! ![39;49;00m$
  2571	$
  2572	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 8/9/2001 15:40'![39;49;00m$
  2573	[32mstoreDataOn:[39;49;00m [31maDataStream[39;49;00m$
  2574		[37m"Store myself on a DataStream.  Answer self.  This is a low-level DataStream/ReferenceStream method. See also objectToStoreOnDataStream.  NOTE: This method must send 'aDataStream beginInstance:size:' and then (nextPut:/nextPutWeak:) its subobjects.  readDataFrom:size: reads back what we write here."[39;49;00m$
  2575		|[31m cntInstVars cntIndexedVars [39;49;00m|$
  2576	$
  2577		[31mcntInstVars[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m.$
  2578		[31mcntIndexedVars[39;49;00m _ [36mself[39;49;00m [32mbasicSize[39;49;00m.$
  2579		[31maDataStream[39;49;00m$
  2580			[32mbeginInstance:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m$
  2581			[32msize:[39;49;00m [31mcntInstVars[39;49;00m [32m+[39;49;00m [31mcntIndexedVars[39;49;00m.$
  2582		[34m1[39;49;00m [32mto:[39;49;00m [31mcntInstVars[39;49;00m [32mdo:[39;49;00m$
  2583			[:[31mi[39;49;00m | [31maDataStream[39;49;00m [32mnextPut:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mi[39;49;00m)].$
  2584	$
  2585		[37m"Write fields of a variable length object.  When writing to a dummy [39;49;00m$
  2586	[37m		stream, don't bother to write the bytes"[39;49;00m$
  2587		(([31maDataStream[39;49;00m [32mbyteStream[39;49;00m [32mclass[39;49;00m [32m==[39;49;00m [04m[32mDummyStream[39;49;00m) [32mand:[39;49;00m [[36mself[39;49;00m [32mclass[39;49;00m [32misBits[39;49;00m]) [36mifFalse:[39;49;00m [$
  2588			[34m1[39;49;00m [32mto:[39;49;00m [31mcntIndexedVars[39;49;00m [32mdo:[39;49;00m$
  2589				[:[31mi[39;49;00m | [31maDataStream[39;49;00m [32mnextPut:[39;49;00m ([36mself[39;49;00m [32mbasicAt:[39;49;00m [31mi[39;49;00m)]].$
  2590	[34m! ![39;49;00m$
  2591	$
  2592	$
  2593	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'parts bin'[39;49;00m[34m stamp: 'sw 10/24/2001 16:34'![39;49;00m$
  2594	[32mdescriptionForPartsBin[39;49;00m$
  2595		[37m"If the receiver is a member of a class that would like to be represented in a parts bin, answer the name by which it should be known, and a documentation string to be provided, for example, as balloon help.  When the 'nativitySelector' is sent to the 'globalReceiver', it is expected that some kind of Morph will result.  The parameters used in the implementation below are for documentation purposes only!!"[39;49;00m$
  2596	$
  2597		^ [04m[32mDescriptionForPartsBin[39;49;00m$
  2598			[32mformalName:[39;49;00m [33m'PutFormalNameHere'[39;49;00m$
  2599			[32mcategoryList:[39;49;00m [33m#([39;49;00m[33mPutACategoryHere[39;49;00m [33mMaybePutAnotherCategoryHere[39;49;00m[33m)[39;49;00m$
  2600			[32mdocumentation:[39;49;00m [33m'Put the balloon help here'[39;49;00m$
  2601			[32mglobalReceiverSymbol:[39;49;00m [33m#PutAGlobalHere[39;49;00m$
  2602			[32mnativitySelector:[39;49;00m [33m#PutASelectorHere[39;49;00m[34m! ![39;49;00m$
  2603	$
  2604	$
  2605	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'di 6/20/97 08:57'![39;49;00m$
  2606	[32mfullPrintString[39;49;00m$
  2607		[37m"Answer a String whose characters are a description of the receiver."[39;49;00m$
  2608	$
  2609		^ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [:[31ms[39;49;00m | [36mself[39;49;00m [32mprintOn:[39;49;00m [31ms[39;49;00m][34m! ![39;49;00m$
  2610	$
  2611	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m![39;49;00m$
  2612	[32misLiteral[39;49;00m$
  2613		[37m"Answer whether the receiver has a literal text form recognized by the [39;49;00m$
  2614	[37m	compiler."[39;49;00m$
  2615	$
  2616		^[36mfalse[39;49;00m[34m! ![39;49;00m$
  2617	$
  2618	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sma 6/1/2000 09:28'![39;49;00m$
  2619	[32mlongPrintOn:[39;49;00m [31maStream[39;49;00m$
  2620		[37m"Append to the argument, aStream, the names and values of all [39;49;00m$
  2621	[37m	of the receiver's instance variables."[39;49;00m$
  2622	$
  2623		[36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mdoWithIndex:[39;49;00m$
  2624			[:[31mtitle[39;49;00m :[31mindex[39;49;00m |$
  2625			[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [31mtitle[39;49;00m;$
  2626			 [32mnextPut:[39;49;00m [33m$:[39;49;00m;$
  2627			 [32mspace[39;49;00m;$
  2628			 [32mtab[39;49;00m;$
  2629			 [32mprint:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m);$
  2630			 [32mcr[39;49;00m][34m! ![39;49;00m$
  2631	$
  2632	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'tk 10/19/2001 11:18'![39;49;00m$
  2633	[32mlongPrintOn:[39;49;00m [31maStream[39;49;00m [32mlimitedTo:[39;49;00m [31msizeLimit[39;49;00m [32mindent:[39;49;00m [31mindent[39;49;00m$
  2634		[37m"Append to the argument, aStream, the names and values of all of the receiver's instance variables.  Limit is the length limit for each inst var."[39;49;00m$
  2635	$
  2636		[36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mdoWithIndex:[39;49;00m$
  2637			[:[31mtitle[39;49;00m :[31mindex[39;49;00m |$
  2638			[31mindent[39;49;00m [36mtimesRepeat:[39;49;00m [[31maStream[39;49;00m [32mtab[39;49;00m].$
  2639			[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [31mtitle[39;49;00m;$
  2640			 [32mnextPut:[39;49;00m [33m$:[39;49;00m;$
  2641			 [32mspace[39;49;00m;$
  2642			 [32mtab[39;49;00m;$
  2643			 [32mnextPutAll:[39;49;00m $
  2644				(([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m) [32mprintStringLimitedTo:[39;49;00m ([31msizeLimit[39;49;00m [32m-[39;49;00m[34m3[39;49;00m [32m-[39;49;00m[31mtitle[39;49;00m [32msize[39;49;00m [32mmax:[39;49;00m [34m1[39;49;00m));$
  2645			 [32mcr[39;49;00m][34m! ![39;49;00m$
  2646	$
  2647	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'tk 10/16/2001 19:41'![39;49;00m$
  2648	[32mlongPrintString[39;49;00m$
  2649		[37m"Answer a String whose characters are a description of the receiver."[39;49;00m$
  2650		$
  2651		|[31m str [39;49;00m|$
  2652		[31mstr[39;49;00m _ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [:[31maStream[39;49;00m | [36mself[39;49;00m [32mlongPrintOn:[39;49;00m [31maStream[39;49;00m].$
  2653		[37m"Objects without inst vars should return something"[39;49;00m$
  2654		^ [31mstr[39;49;00m [32misEmpty[39;49;00m [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [04m[32mString[39;49;00m [32mcr[39;49;00m] [36mifFalse:[39;49;00m [[31mstr[39;49;00m][34m! ![39;49;00m$
  2655	$
  2656	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'BG 11/7/2004 13:39'![39;49;00m$
  2657	[32mlongPrintStringLimitedTo:[39;49;00m [31maLimitValue[39;49;00m$
  2658		[37m"Answer a String whose characters are a description of the receiver."[39;49;00m$
  2659		$
  2660		|[31m str [39;49;00m|$
  2661		[31mstr[39;49;00m _ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [:[31maStream[39;49;00m | [36mself[39;49;00m [32mlongPrintOn:[39;49;00m [31maStream[39;49;00m [32mlimitedTo:[39;49;00m [31maLimitValue[39;49;00m [32mindent:[39;49;00m [34m0[39;49;00m].$
  2662		[37m"Objects without inst vars should return something"[39;49;00m$
  2663		^ [31mstr[39;49;00m [32misEmpty[39;49;00m [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [04m[32mString[39;49;00m [32mcr[39;49;00m] [36mifFalse:[39;49;00m [[31mstr[39;49;00m][34m! ![39;49;00m$
  2664	$
  2665	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sw 3/7/2001 13:14'![39;49;00m$
  2666	[32mnominallyUnsent:[39;49;00m [31maSelectorSymbol[39;49;00m$
  2667		[37m"From within the body of a method which is not formally sent within the system, but which you intend to have remain in the system (for potential manual invocation, or for documentation, or perhaps because it's sent by commented-out-code that you anticipate uncommenting out someday, send this message, with the selector itself as the argument.[39;49;00m$
  2668	[37m[39;49;00m$
  2669	[37mThis will serve two purposes:[39;49;00m$
  2670	[37m[39;49;00m$
  2671	[37m	(1)  The method will not be returned by searches for unsent selectors (because it, in a manner of speaking, sends itself).[39;49;00m$
  2672	[37m	(2)	You can locate all such methods by browsing senders of #nominallyUnsent:"[39;49;00m$
  2673	$
  2674		[36mfalse[39;49;00m [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mflag:[39;49;00m [33m#nominallyUnsent:[39;49;00m]    [37m"So that this method itself will appear to be sent"[39;49;00m$
  2675	[34m! ![39;49;00m$
  2676	$
  2677	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sma 6/1/2000 09:31'![39;49;00m$
  2678	[32mprintOn:[39;49;00m [31maStream[39;49;00m$
  2679		[37m"Append to the argument, aStream, a sequence of characters that  [39;49;00m$
  2680	[37m	identifies the receiver."[39;49;00m$
  2681	$
  2682		|[31m title [39;49;00m|$
  2683		[31mtitle[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m.$
  2684		[31maStream[39;49;00m$
  2685			[32mnextPutAll:[39;49;00m ([31mtitle[39;49;00m [32mfirst[39;49;00m [32misVowel[39;49;00m [36mifTrue:[39;49;00m [[33m'an '[39;49;00m] [36mifFalse:[39;49;00m [[33m'a '[39;49;00m]);$
  2686			[32mnextPutAll:[39;49;00m [31mtitle[39;49;00m[34m! ![39;49;00m$
  2687	$
  2688	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sma 6/1/2000 09:22'![39;49;00m$
  2689	[32mprintString[39;49;00m$
  2690		[37m"Answer a String whose characters are a description of the receiver. [39;49;00m$
  2691	[37m	If you want to print without a character limit, use fullPrintString."[39;49;00m$
  2692	$
  2693		^ [36mself[39;49;00m [32mprintStringLimitedTo:[39;49;00m [34m50000[39;49;00m[34m! ![39;49;00m$
  2694	$
  2695	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'tk 5/7/1999 16:20'![39;49;00m$
  2696	[32mprintStringLimitedTo:[39;49;00m [31mlimit[39;49;00m$
  2697		[37m"Answer a String whose characters are a description of the receiver.[39;49;00m$
  2698	[37m	If you want to print without a character limit, use fullPrintString."[39;49;00m$
  2699		|[31m limitedString [39;49;00m|$
  2700		[31mlimitedString[39;49;00m _ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [:[31ms[39;49;00m | [36mself[39;49;00m [32mprintOn:[39;49;00m [31ms[39;49;00m] [32mlimitedTo:[39;49;00m [31mlimit[39;49;00m.$
  2701		[31mlimitedString[39;49;00m [32msize[39;49;00m [32m<[39;49;00m [31mlimit[39;49;00m [36mifTrue:[39;49;00m [^ [31mlimitedString[39;49;00m].$
  2702		^ [31mlimitedString[39;49;00m [32m,[39;49;00m [33m'...etc...'[39;49;00m[34m! ![39;49;00m$
  2703	$
  2704	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'MPW 1/1/1901 00:30'![39;49;00m$
  2705	[32mpropertyList[39;49;00m$
  2706		[37m"Answer a String whose characters are a property-list description of the receiver."[39;49;00m$
  2707	$
  2708		^ [04m[32mPropertyListEncoder[39;49;00m [32mprocess:[39;49;00m[36mself[39;49;00m.$
  2709	[34m! ![39;49;00m$
  2710	$
  2711	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sw 10/17/2000 11:16'![39;49;00m$
  2712	[32mreportableSize[39;49;00m$
  2713		[37m"Answer a string that reports the size of the receiver -- useful for showing in a list view, for example"[39;49;00m$
  2714	$
  2715		^ ([36mself[39;49;00m [32mbasicSize[39;49;00m [32m+[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m) [32mprintString[39;49;00m[34m! ![39;49;00m$
  2716	$
  2717	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m![39;49;00m$
  2718	[32mstoreOn:[39;49;00m [31maStream[39;49;00m $
  2719		[37m"Append to the argument aStream a sequence of characters that is an [39;49;00m$
  2720	[37m	expression whose evaluation creates an object similar to the receiver."[39;49;00m$
  2721	$
  2722		[31maStream[39;49;00m [32mnextPut:[39;49;00m [33m$([39;49;00m.$
  2723		[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m$
  2724			[36mifTrue:[39;49;00m [[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [33m'('[39;49;00m[32m,[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m[32m,[39;49;00m [33m' basicNew: '[39;49;00m;$
  2725						[32mstore:[39;49;00m [36mself[39;49;00m [32mbasicSize[39;49;00m;$
  2726						[32mnextPutAll:[39;49;00m [33m') '[39;49;00m]$
  2727			[36mifFalse:[39;49;00m [[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m[32m,[39;49;00m [33m' basicNew'[39;49;00m].$
  2728		[34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mdo:[39;49;00m$
  2729			[:[31mi[39;49;00m |$
  2730			[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [33m' instVarAt: '[39;49;00m;$
  2731				[32mstore:[39;49;00m [31mi[39;49;00m;$
  2732				[32mnextPutAll:[39;49;00m [33m' put: '[39;49;00m;$
  2733				[32mstore:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mi[39;49;00m);$
  2734				[32mnextPut:[39;49;00m [33m$;[39;49;00m].$
  2735		[34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32mbasicSize[39;49;00m [32mdo:[39;49;00m$
  2736			[:[31mi[39;49;00m |$
  2737			[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [33m' basicAt: '[39;49;00m;$
  2738				[32mstore:[39;49;00m [31mi[39;49;00m;$
  2739				[32mnextPutAll:[39;49;00m [33m' put: '[39;49;00m;$
  2740				[32mstore:[39;49;00m ([36mself[39;49;00m [32mbasicAt:[39;49;00m [31mi[39;49;00m);$
  2741				[32mnextPut:[39;49;00m [33m$;[39;49;00m].$
  2742		[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [33m' yourself)'[39;49;00m$
  2743	[34m! ![39;49;00m$
  2744	$
  2745	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'di 6/20/97 09:12'![39;49;00m$
  2746	[32mstoreString[39;49;00m$
  2747		[37m"Answer a String representation of the receiver from which the receiver [39;49;00m$
  2748	[37m	can be reconstructed."[39;49;00m$
  2749	$
  2750		^ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [:[31ms[39;49;00m | [36mself[39;49;00m [32mstoreOn:[39;49;00m [31ms[39;49;00m][34m! ![39;49;00m$
  2751	$
  2752	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sw 5/2/1998 13:55'![39;49;00m$
  2753	[32mstringForReadout[39;49;00m$
  2754		^ [36mself[39;49;00m [32mstringRepresentation[39;49;00m[34m! ![39;49;00m$
  2755	$
  2756	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m![39;49;00m$
  2757	[32mstringRepresentation[39;49;00m$
  2758		[37m"Answer a string that represents the receiver.  For most objects this is simply its printString, but for strings themselves, it's themselves.  6/12/96 sw"[39;49;00m$
  2759	$
  2760		^ [36mself[39;49;00m [32mprintString[39;49;00m [34m! ![39;49;00m$
  2761	$
  2762	$
  2763	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'ar 3/17/2001 20:11'![39;49;00m$
  2764	[32madaptedToWorld:[39;49;00m [31maWorld[39;49;00m$
  2765		[37m"If I refer to a world or a hand, return the corresponding items in the new world."[39;49;00m$
  2766		^[36mself[39;49;00m[34m! ![39;49;00m$
  2767	$
  2768	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'sw 3/10/2000 13:57'![39;49;00m$
  2769	[32mdefaultFloatPrecisionFor:[39;49;00m [31maGetSelector[39;49;00m$
  2770		[37m"Answer a number indicating the default float precision to be used in a numeric readout for which the receiver is the model."[39;49;00m$
  2771	$
  2772		^ [34m1[39;49;00m[34m! ![39;49;00m$
  2773	$
  2774	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 3/9/2001 17:08'![39;49;00m$
  2775	[32mevaluateUnloggedForSelf:[39;49;00m [31maCodeString[39;49;00m$
  2776	$
  2777		^[04m[32mCompiler[39;49;00m [32mevaluate:[39;49;00m$
  2778			[31maCodeString[39;49;00m$
  2779			[32mfor:[39;49;00m [36mself[39;49;00m$
  2780			[32mlogged:[39;49;00m [36mfalse[39;49;00m[34m! ![39;49;00m$
  2781	$
  2782	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'yo 12/25/2003 16:43'![39;49;00m$
  2783	[32mmethodInterfacesForCategory:[39;49;00m [31maCategorySymbol[39;49;00m [32minVocabulary:[39;49;00m [31maVocabulary[39;49;00m [32mlimitClass:[39;49;00m [31maLimitClass[39;49;00m$
  2784		[37m"Return a list of methodInterfaces for the receiver in the given category, given a vocabulary.  aCategorySymbol is the inherent category symbol, not necessarily the wording as expressed in the vocabulary."[39;49;00m$
  2785	$
  2786		|[31m categorySymbol [39;49;00m|$
  2787		[31mcategorySymbol[39;49;00m _ [31maCategorySymbol[39;49;00m [32masSymbol[39;49;00m.$
  2788	$
  2789		([31mcategorySymbol[39;49;00m [32m==[39;49;00m [04m[32mScriptingSystem[39;49;00m [32mnameForInstanceVariablesCategory[39;49;00m) [36mifTrue:[39;49;00m [$
  2790			[37m"user-defined instance variables"[39;49;00m$
  2791			^ [36mself[39;49;00m [32mmethodInterfacesForInstanceVariablesCategoryIn:[39;49;00m [31maVocabulary[39;49;00m].$
  2792		([31mcategorySymbol[39;49;00m [32m==[39;49;00m [04m[32mScriptingSystem[39;49;00m [32mnameForScriptsCategory[39;49;00m) [36mifTrue:[39;49;00m [$
  2793			[37m"user-defined scripts"[39;49;00m$
  2794			^ [36mself[39;49;00m [32mmethodInterfacesForScriptsCategoryIn:[39;49;00m [31maVocabulary[39;49;00m].$
  2795		[37m"all others"[39;49;00m$
  2796		^ [36mself[39;49;00m [32musableMethodInterfacesIn:[39;49;00m ([31maVocabulary[39;49;00m [32mmethodInterfacesInCategory:[39;49;00m [31mcategorySymbol[39;49;00m$
  2797			[32mforInstance:[39;49;00m [36mself[39;49;00m$
  2798			[32mofClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m$
  2799			[32mlimitClass:[39;49;00m [31maLimitClass[39;49;00m)$
  2800	[34m! ![39;49;00m$
  2801	$
  2802	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'sw 8/3/2001 13:54'![39;49;00m$
  2803	[32mmethodInterfacesForInstanceVariablesCategoryIn:[39;49;00m [31maVocabulary[39;49;00m$
  2804		[37m"Return a collection of methodInterfaces for the instance-variables category.  The vocabulary parameter, at present anyway, is not used.  And for non-players, the method is at present vacuous in any case"[39;49;00m$
  2805	$
  2806		^  [04m[32mOrderedCollection[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
  2807	$
  2808	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'sw 8/3/2001 13:53'![39;49;00m$
  2809	[32mmethodInterfacesForScriptsCategoryIn:[39;49;00m [31maVocabulary[39;49;00m$
  2810		[37m"Answer a list of method interfaces for the category #scripts, as seen in a viewer or other tool.  The vocabulary argument is not presently used.  Also, at present, only Players really do anyting interesting here."[39;49;00m$
  2811	$
  2812		^ [04m[32mOrderedCollection[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
  2813	$
  2814	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 2/16/2001 19:37'![39;49;00m$
  2815	[32mselfWrittenAsIll[39;49;00m$
  2816	$
  2817		^[36mself[39;49;00m[34m! ![39;49;00m$
  2818	$
  2819	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 2/16/2001 19:38'![39;49;00m$
  2820	[32mselfWrittenAsIm[39;49;00m$
  2821	$
  2822		^[36mself[39;49;00m[34m! ![39;49;00m$
  2823	$
  2824	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 2/16/2001 19:37'![39;49;00m$
  2825	[32mselfWrittenAsMe[39;49;00m$
  2826	$
  2827		^[36mself[39;49;00m[34m! ![39;49;00m$
  2828	$
  2829	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 2/16/2001 19:37'![39;49;00m$
  2830	[32mselfWrittenAsMy[39;49;00m$
  2831	$
  2832		^[36mself[39;49;00m[34m! ![39;49;00m$
  2833	$
  2834	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 2/16/2001 19:38'![39;49;00m$
  2835	[32mselfWrittenAsThis[39;49;00m$
  2836	$
  2837		^[36mself[39;49;00m[34m! ![39;49;00m$
  2838	$
  2839	$
  2840	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripts-kernel'[39;49;00m[34m stamp: 'nk 10/14/2004 10:55'![39;49;00m$
  2841	[32muniversalTilesForGetterOf:[39;49;00m [31maMethodInterface[39;49;00m$
  2842		[37m"Return universal tiles for a getter on the given method interface."[39;49;00m$
  2843	$
  2844		|[31m ms argTile argArray itsSelector [39;49;00m|$
  2845		[31mitsSelector[39;49;00m _ [31maMethodInterface[39;49;00m [32mselector[39;49;00m.$
  2846		[31margArray[39;49;00m _ [33m#([39;49;00m[33m)[39;49;00m.$
  2847	$
  2848		[37m"Four gratuituous special cases..."[39;49;00m$
  2849	$
  2850		([31mitsSelector[39;49;00m [32m==[39;49;00m [33m#color:sees:[39;49;00m) [36mifTrue:[39;49;00m$
  2851			[[31margTile[39;49;00m _ [04m[32mScriptingSystem[39;49;00m [32mtileForArgType:[39;49;00m [33m#Color[39;49;00m.$
  2852			[31margArray[39;49;00m _ [04m[32mArray[39;49;00m [32mwith:[39;49;00m [31margTile[39;49;00m [32mcolorSwatch[39;49;00m [32mcolor[39;49;00m [32mwith:[39;49;00m [31margTile[39;49;00m [32mcolorSwatch[39;49;00m [32mcolor[39;49;00m [32mcopy[39;49;00m].$
  2853	$
  2854		[31mitsSelector[39;49;00m [32m==[39;49;00m [33m#seesColor:[39;49;00m [36mifTrue:[39;49;00m$
  2855			[[31margTile[39;49;00m _ [04m[32mScriptingSystem[39;49;00m [32mtileForArgType:[39;49;00m [33m#Color[39;49;00m.$
  2856			[31margArray[39;49;00m _  [04m[32mArray[39;49;00m [32mwith:[39;49;00m [31margTile[39;49;00m [32mcolorSwatch[39;49;00m [32mcolor[39;49;00m].$
  2857	$
  2858		([33m#([39;49;00m[33mtouchesA:[39;49;00m [33moverlaps:[39;49;00m [33moverlapsAny:[39;49;00m[33m)[39;49;00m [32mincludes:[39;49;00m [31mitsSelector[39;49;00m) [36mifTrue:[39;49;00m$
  2859			[[31margTile[39;49;00m _ [04m[32mScriptingSystem[39;49;00m [32mtileForArgType:[39;49;00m [33m#Player[39;49;00m.$
  2860			[31margArray[39;49;00m _ [04m[32mArray[39;49;00m [32mwith:[39;49;00m [31margTile[39;49;00m [32mactualObject[39;49;00m].$
  2861	$
  2862		[31mms[39;49;00m _ [04m[32mMessageSend[39;49;00m [32mreceiver:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [31mitsSelector[39;49;00m [32marguments:[39;49;00m [31margArray[39;49;00m.$
  2863		^ [31mms[39;49;00m [32masTilesIn:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mglobalNames:[39;49;00m ([36mself[39;49;00m [32mclass[39;49;00m [32mofficialClass[39;49;00m [32m~~[39;49;00m [04m[32mCardPlayer[39;49;00m)$
  2864				[37m"For CardPlayers, use 'self'.  For others, name it, and use its name."[39;49;00m[34m! ![39;49;00m$
  2865	$
  2866	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripts-kernel'[39;49;00m[34m stamp: 'tk 9/28/2001 13:30'![39;49;00m$
  2867	[32muniversalTilesForInterface:[39;49;00m [31maMethodInterface[39;49;00m$
  2868		[37m"Return universal tiles for the given method interface.  Record who self is."[39;49;00m$
  2869	$
  2870		|[31m ms argTile itsSelector aType argList [39;49;00m|$
  2871		[31mitsSelector[39;49;00m _ [31maMethodInterface[39;49;00m [32mselector[39;49;00m.$
  2872		[31margList[39;49;00m _ [04m[32mOrderedCollection[39;49;00m [36mnew[39;49;00m.$
  2873		[31maMethodInterface[39;49;00m [32margumentVariables[39;49;00m [32mdoWithIndex:[39;49;00m$
  2874			[:[31manArgumentVariable[39;49;00m :[31manIndex[39;49;00m | $
  2875				[31margTile[39;49;00m _ [04m[32mScriptingSystem[39;49;00m [32mtileForArgType:[39;49;00m ([31maType[39;49;00m _ [31maMethodInterface[39;49;00m [32mtypeForArgumentNumber:[39;49;00m [31manIndex[39;49;00m).$
  2876				[31margList[39;49;00m [32madd:[39;49;00m ([31maType[39;49;00m [32m==[39;49;00m [33m#Player[39;49;00m $
  2877					[36mifTrue:[39;49;00m [[31margTile[39;49;00m [32mactualObject[39;49;00m]$
  2878					[36mifFalse:[39;49;00m [[31margTile[39;49;00m [32mliteral[39;49;00m]).	[37m"default value for each type"[39;49;00m].$
  2879	$
  2880		[31mms[39;49;00m _ [04m[32mMessageSend[39;49;00m [32mreceiver:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [31mitsSelector[39;49;00m [32marguments:[39;49;00m [31margList[39;49;00m [32masArray[39;49;00m.$
  2881		^ [31mms[39;49;00m [32masTilesIn:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mglobalNames:[39;49;00m ([36mself[39;49;00m [32mclass[39;49;00m [32mofficialClass[39;49;00m [32m~~[39;49;00m [04m[32mCardPlayer[39;49;00m)$
  2882				[37m"For CardPlayers, use 'self'.  For others, name it, and use its name."[39;49;00m[34m! ![39;49;00m$
  2883	$
  2884	$
  2885	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'self evaluating'[39;49;00m[34m stamp: 'sd 7/31/2005 21:47'![39;49;00m$
  2886	[32misSelfEvaluating[39;49;00m$
  2887		^ [36mself[39;49;00m [32misLiteral[39;49;00m[34m! ![39;49;00m$
  2888	$
  2889	$
  2890	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m![39;49;00m$
  2891	[32masOop[39;49;00m$
  2892		[37m"Primitive. Answer a SmallInteger whose value is half of the receiver's [39;49;00m$
  2893	[37m	object pointer (interpreting object pointers as 16-bit signed quantities). [39;49;00m$
  2894	[37m	Fail if the receiver is a SmallInteger. Essential. See Object documentation [39;49;00m$
  2895	[37m	whatIsAPrimitive."[39;49;00m$
  2896	$
  2897		<[34mprimitive:[39;49;00m 75>$
  2898		[36mself[39;49;00m [32mprimitiveFailed[39;49;00m[34m! ![39;49;00m$
  2899	$
  2900	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'di 1/9/1999 15:19'![39;49;00m$
  2901	[32mbecomeForward:[39;49;00m [31motherObject[39;49;00m $
  2902		[37m"Primitive. All variables in the entire system that used to point[39;49;00m$
  2903	[37m	to the receiver now point to the argument.[39;49;00m$
  2904	[37m	Fails if either argument is a SmallInteger."[39;49;00m$
  2905	$
  2906		([04m[32mArray[39;49;00m [32mwith:[39;49;00m [36mself[39;49;00m)$
  2907			[32melementsForwardIdentityTo:[39;49;00m$
  2908				([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31motherObject[39;49;00m)[34m! ![39;49;00m$
  2909	$
  2910	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'zz 3/3/2004 23:53'![39;49;00m$
  2911	[32mbecomeForward:[39;49;00m [31motherObject[39;49;00m [32mcopyHash:[39;49;00m [31mcopyHash[39;49;00m$
  2912		[37m"Primitive. All variables in the entire system that used to point to the receiver now point to the argument.[39;49;00m$
  2913	[37m	If copyHash is true, the argument's identity hash bits will be set to those of the receiver.[39;49;00m$
  2914	[37m	Fails if either argument is a SmallInteger."[39;49;00m$
  2915	$
  2916		([04m[32mArray[39;49;00m [32mwith:[39;49;00m [36mself[39;49;00m)$
  2917			[32melementsForwardIdentityTo:[39;49;00m$
  2918				([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31motherObject[39;49;00m)$
  2919					[32mcopyHash:[39;49;00m [31mcopyHash[39;49;00m[34m! ![39;49;00m$
  2920	$
  2921	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'sw 10/16/2000 10:59'![39;49;00m$
  2922	[32mclassName[39;49;00m$
  2923		[37m"Answer a string characterizing the receiver's class, for use in list views for example"[39;49;00m$
  2924	$
  2925		^ [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32masString[39;49;00m[34m! ![39;49;00m$
  2926	$
  2927	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'sw 10/16/2000 11:04'![39;49;00m$
  2928	[32mcreationStamp[39;49;00m$
  2929		[37m"Answer a string which reports the creation particulars of the receiver.  Intended perhaps for list views, but this is presently a feature not easily accessible"[39;49;00m$
  2930	$
  2931		^ [33m'<no creation stamp>'[39;49;00m[34m! ![39;49;00m$
  2932	$
  2933	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m![39;49;00m$
  2934	[32minstVarAt:[39;49;00m [31mindex[39;49;00m $
  2935		[37m"Primitive. Answer a fixed variable in an object. The numbering of the [39;49;00m$
  2936	[37m	variables corresponds to the named instance variables. Fail if the index [39;49;00m$
  2937	[37m	is not an Integer or is not the index of a fixed variable. Essential. See [39;49;00m$
  2938	[37m	Object documentation whatIsAPrimitive."[39;49;00m$
  2939	$
  2940		<[34mprimitive:[39;49;00m 73>$
  2941		[37m"Access beyond fixed variables."[39;49;00m$
  2942		^[36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32m-[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m		[34m! ![39;49;00m$
  2943	$
  2944	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m![39;49;00m$
  2945	[32minstVarAt:[39;49;00m [31manInteger[39;49;00m [32mput:[39;49;00m [31manObject[39;49;00m $
  2946		[37m"Primitive. Store a value into a fixed variable in the receiver. The [39;49;00m$
  2947	[37m	numbering of the variables corresponds to the named instance variables. [39;49;00m$
  2948	[37m	Fail if the index is not an Integer or is not the index of a fixed variable. [39;49;00m$
  2949	[37m	Answer the value stored as the result. Using this message violates the [39;49;00m$
  2950	[37m	principle that each object has sovereign control over the storing of [39;49;00m$
  2951	[37m	values into its instance variables. Essential. See Object documentation [39;49;00m$
  2952	[37m	whatIsAPrimitive."[39;49;00m$
  2953	$
  2954		<[34mprimitive:[39;49;00m 74>$
  2955		[37m"Access beyond fixed fields"[39;49;00m$
  2956		^[36mself[39;49;00m [32mbasicAt:[39;49;00m [31manInteger[39;49;00m [32m-[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mput:[39;49;00m [31manObject[39;49;00m[34m! ![39;49;00m$
  2957	$
  2958	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'sw 10/16/2000 11:09'![39;49;00m$
  2959	[32minstVarNamed:[39;49;00m [31maString[39;49;00m$
  2960		[37m"Return the value of the instance variable in me with that name.  Slow and unclean, but very useful. "[39;49;00m$
  2961	$
  2962		^ [36mself[39;49;00m [32minstVarAt:[39;49;00m ([36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mindexOf:[39;49;00m [31maString[39;49;00m [32masString[39;49;00m)$
  2963	$
  2964	$
  2965	[34m! ![39;49;00m$
  2966	$
  2967	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'sw 10/16/2000 11:10'![39;49;00m$
  2968	[32minstVarNamed:[39;49;00m [31maString[39;49;00m [32mput:[39;49;00m [31maValue[39;49;00m$
  2969		[37m"Store into the value of the instance variable in me of that name.  Slow and unclean, but very useful. "[39;49;00m$
  2970	$
  2971		^ [36mself[39;49;00m [32minstVarAt:[39;49;00m ([36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mindexOf:[39;49;00m [31maString[39;49;00m [32masString[39;49;00m) [32mput:[39;49;00m [31maValue[39;49;00m$
  2972	[34m! ![39;49;00m$
  2973	$
  2974	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'sw 10/17/2000 11:12'![39;49;00m$
  2975	[32moopString[39;49;00m$
  2976		[37m"Answer a string that represents the oop of the receiver"[39;49;00m$
  2977	$
  2978		^ [36mself[39;49;00m [32masOop[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
  2979	$
  2980	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'ar 3/2/2001 01:34'![39;49;00m$
  2981	[32mprimitiveChangeClassTo:[39;49;00m [31manObject[39;49;00m$
  2982		[37m"Primitive. Change the class of the receiver into the class of the argument given that the format of the receiver matches the format of the argument's class. Fail if receiver or argument are SmallIntegers, or the receiver is an instance of a compact class and the argument isn't, or when the argument's class is compact and the receiver isn't, or when the format of the receiver is different from the format of the argument's class, or when the arguments class is fixed and the receiver's size differs from the size that an instance of the argument's class should have.[39;49;00m$
  2983	[37m	Note: The primitive will fail in most cases that you think might work. This is mostly because of a) the difference between compact and non-compact classes, and b) because of differences in the format. As an example, '(Array new: 3) primitiveChangeClassTo: Morph basicNew' would fail for three of the reasons mentioned above. Array is compact, Morph is not (failure #1). Array is variable and Morph is fixed (different format - failure #2). Morph is a fixed-field-only object and the array is too short (failure #3).[39;49;00m$
  2984	[37m	The facility is really provided for certain, very specific applications (mostly related to classes changing shape) and not for casual use."[39;49;00m$
  2985	$
  2986		<[34mprimitive:[39;49;00m 115>$
  2987		[36mself[39;49;00m [32mprimitiveFailed[39;49;00m[34m! ![39;49;00m$
  2988	$
  2989	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'di 3/27/1999 12:21'![39;49;00m$
  2990	[32mrootStubInImageSegment:[39;49;00m [31mimageSegment[39;49;00m$
  2991	$
  2992		^ [04m[32mImageSegmentRootStub[39;49;00m [36mnew[39;49;00m$
  2993			[32mxxSuperclass:[39;49;00m [36mnil[39;49;00m$
  2994			[32mformat:[39;49;00m [36mnil[39;49;00m$
  2995			[32msegment:[39;49;00m [31mimageSegment[39;49;00m[34m! ![39;49;00m$
  2996	$
  2997	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m![39;49;00m$
  2998	[32msomeObject[39;49;00m$
  2999		[37m"Primitive. Answer the first object in the enumeration of all[39;49;00m$
  3000	[37m	 objects."[39;49;00m$
  3001	$
  3002		<[34mprimitive:[39;49;00m 138>$
  3003		[36mself[39;49;00m [32mprimitiveFailed[39;49;00m.[34m! ![39;49;00m$
  3004	$
  3005	$
  3006	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 9/26/2001 11:58'![39;49;00m$
  3007	[32mbasicType[39;49;00m$
  3008		[37m"Answer a symbol representing the inherent type of the receiver"[39;49;00m$
  3009	$
  3010		^ [33m#Object[39;49;00m[34m! ![39;49;00m$
  3011	$
  3012	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 5/3/2001 16:19'![39;49;00m$
  3013	[32mbeViewed[39;49;00m$
  3014		[37m"Open up a viewer on the receiver.  The Presenter is invited to decide just how to present this viewer"[39;49;00m$
  3015	$
  3016		[36mself[39;49;00m [32muniqueNameForReference[39;49;00m.  [37m"So the viewer will have something nice to refer to"[39;49;00m$
  3017		[36mself[39;49;00m [32mpresenter[39;49;00m [32mviewObject:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  3018	$
  3019	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/16/2000 11:01'![39;49;00m$
  3020	[32mcostumes[39;49;00m$
  3021		[37m"Answer a list of costumes associated with the receiver.  The appearance of this method in class Object serves only as a backstop, probably only transitionally"[39;49;00m$
  3022	$
  3023		^ [36mnil[39;49;00m[34m! ![39;49;00m$
  3024	$
  3025	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 1/12/98 18:09'![39;49;00m$
  3026	[31mhaltIfNil[39;49;00m[34m! ![39;49;00m$
  3027	$
  3028	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 1/20/2006 17:09'![39;49;00m$
  3029	[32mhasLiteralSuchThat:[39;49;00m [31mtestBlock[39;49;00m$
  3030		[37m"This is the end of the imbedded structure path so return false."[39;49;00m$
  3031	$
  3032		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3033	$
  3034	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 1/20/2006 17:10'![39;49;00m$
  3035	[32mhasLiteralThorough:[39;49;00m [31mliteral[39;49;00m$
  3036		[37m"Answer true if literal is identical to any literal in this array, even if imbedded in further structures.  This is the end of the imbedded structure path so return false."[39;49;00m$
  3037	$
  3038		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3039	$
  3040	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 1/30/2001 22:24'![39;49;00m$
  3041	[32mhaveFullProtocolBrowsed[39;49;00m$
  3042		[37m"Open up a Lexicon on the receiver"[39;49;00m$
  3043	$
  3044		^ [36mself[39;49;00m [32mhaveFullProtocolBrowsedShowingSelector:[39;49;00m [36mnil[39;49;00m$
  3045	$
  3046		[37m"(2@3) haveFullProtocolBrowsed"[39;49;00m$
  3047	[34m! ![39;49;00m$
  3048	$
  3049	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 9/27/2005 21:04'![39;49;00m$
  3050	[32mhaveFullProtocolBrowsedShowingSelector:[39;49;00m [31maSelector[39;49;00m$
  3051		[37m"Open up a Lexicon on the receiver, having it open up showing aSelector, which may be nil"[39;49;00m$
  3052	$
  3053		|[31m aBrowser [39;49;00m|$
  3054		[31maBrowser[39;49;00m := ([04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#InstanceBrowser[39;49;00m [32mifAbsent:[39;49;00m[^[36mnil[39;49;00m]) [36mnew[39;49;00m [32museVocabulary:[39;49;00m [04m[32mVocabulary[39;49;00m [32mfullVocabulary[39;49;00m.$
  3055		[31maBrowser[39;49;00m [32mopenOnObject:[39;49;00m [36mself[39;49;00m [32minWorld:[39;49;00m [04m[32mActiveWorld[39;49;00m [32mshowingSelector:[39;49;00m [31maSelector[39;49;00m$
  3056	$
  3057		[37m"(2@3) haveFullProtocolBrowsed"[39;49;00m[34m! ![39;49;00m$
  3058	$
  3059	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 7/30/2005 21:21'![39;49;00m$
  3060	[32misArray[39;49;00m$
  3061		^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3062	$
  3063	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 7/9/1999 18:18'![39;49;00m$
  3064	[32misBehavior[39;49;00m$
  3065		[37m"Return true if the receiver is a behavior.[39;49;00m$
  3066	[37m	Note: Do not override in any class except behavior."[39;49;00m$
  3067		^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3068	$
  3069	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ajh 1/21/2003 13:15'![39;49;00m$
  3070	[32misBlock[39;49;00m$
  3071	$
  3072		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3073	$
  3074	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 11/21/2003 12:14'![39;49;00m$
  3075	[32misBlockClosure[39;49;00m$
  3076	$
  3077		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3078	$
  3079	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'yo 8/28/2002 13:41'![39;49;00m$
  3080	[32misCharacter[39;49;00m$
  3081	$
  3082		^ [36mfalse[39;49;00m.$
  3083	[34m! ![39;49;00m$
  3084	$
  3085	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 8/17/1999 19:43'![39;49;00m$
  3086	[32misCollection[39;49;00m$
  3087		[37m"Return true if the receiver is some sort of Collection and responds to basic collection messages such as #size and #do:"[39;49;00m$
  3088		^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3089	$
  3090	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
  3091	[32misColor[39;49;00m$
  3092		[37m"Answer true if receiver is a Color. False by default."[39;49;00m$
  3093	$
  3094		^ [36mfalse[39;49;00m$
  3095	[34m! ![39;49;00m$
  3096	$
  3097	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'nk 4/17/2004 19:43'![39;49;00m$
  3098	[32misColorForm[39;49;00m$
  3099		^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3100	$
  3101	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 11/21/2003 12:14'![39;49;00m$
  3102	[32misCompiledMethod[39;49;00m$
  3103	$
  3104		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3105	$
  3106	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'mk 10/27/2003 17:33'![39;49;00m$
  3107	[32misComplex[39;49;00m$
  3108		[37m"Answer true if receiver is a Complex number. False by default."[39;49;00m$
  3109	$
  3110		^ [36mfalse[39;49;00m$
  3111	[34m! ![39;49;00m$
  3112	$
  3113	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 8/11/2005 16:45'![39;49;00m$
  3114	[32misDictionary[39;49;00m$
  3115		^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3116	$
  3117	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'di 11/9/1998 09:38'![39;49;00m$
  3118	[32misFloat[39;49;00m$
  3119		[37m"Overridden to return true in Float, natch"[39;49;00m$
  3120		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3121	$
  3122	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 10/30/2000 23:22'![39;49;00m$
  3123	[32misForm[39;49;00m$
  3124		^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3125	$
  3126	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'len 1/13/98 21:18'![39;49;00m$
  3127	[32misFraction[39;49;00m$
  3128		[37m"Answer true if the receiver is a Fraction."[39;49;00m$
  3129	$
  3130		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3131	$
  3132	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'rhi 8/14/2003 08:51'![39;49;00m$
  3133	[32misHeap[39;49;00m$
  3134	$
  3135		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3136	$
  3137	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
  3138	[32misInteger[39;49;00m$
  3139		[37m"Overridden to return true in Integer."[39;49;00m$
  3140	$
  3141		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3142	$
  3143	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'rhi 8/12/2003 09:52'![39;49;00m$
  3144	[32misInterval[39;49;00m$
  3145	$
  3146		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3147	$
  3148	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'nk 4/25/2002 08:04'![39;49;00m$
  3149	[32misMessageSend[39;49;00m$
  3150		^[36mfalse[39;49;00m$
  3151	[34m! ![39;49;00m$
  3152	$
  3153	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 2/19/2006 11:24'![39;49;00m$
  3154	[32misMethodProperties[39;49;00m$
  3155		^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3156	$
  3157	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
  3158	[32misMorph[39;49;00m$
  3159	$
  3160		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3161	$
  3162	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 9/13/2000 15:37'![39;49;00m$
  3163	[32misMorphicEvent[39;49;00m$
  3164		^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3165	$
  3166	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'gm 2/22/2003 12:56'![39;49;00m$
  3167	[32misMorphicModel[39;49;00m$
  3168		[37m"Return true if the receiver is a morphic model"[39;49;00m$
  3169		^[36mfalse[39;49;00m$
  3170	[34m! ![39;49;00m$
  3171	$
  3172	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
  3173	[32misNumber[39;49;00m$
  3174		[37m"Overridden to return true in Number, natch"[39;49;00m$
  3175		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3176	$
  3177	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'di 11/6/1998 08:04'![39;49;00m$
  3178	[32misPoint[39;49;00m$
  3179		[37m"Overridden to return true in Point."[39;49;00m$
  3180	$
  3181		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3182	$
  3183	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ikp 9/26/97 14:45'![39;49;00m$
  3184	[32misPseudoContext[39;49;00m$
  3185		^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3186	$
  3187	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 10/2/2005 21:52'![39;49;00m$
  3188	[32misRectangle[39;49;00m$
  3189		^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3190	$
  3191	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'nk 6/14/2004 16:49'![39;49;00m$
  3192	[32misSketchMorph[39;49;00m$
  3193		^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3194	$
  3195	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 12/23/1999 15:43'![39;49;00m$
  3196	[32misStream[39;49;00m$
  3197		[37m"Return true if the receiver responds to the stream protocol"[39;49;00m$
  3198		^[36mfalse[39;49;00m$
  3199	[34m! ![39;49;00m$
  3200	$
  3201	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sma 6/15/2000 15:48'![39;49;00m$
  3202	[32misString[39;49;00m$
  3203		[37m"Overridden to return true in String, natch"[39;49;00m$
  3204		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3205	$
  3206	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 4/30/2003 15:30'![39;49;00m$
  3207	[32misSymbol[39;49;00m$
  3208		^ [36mfalse[39;49;00m [34m! ![39;49;00m$
  3209	$
  3210	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'jam 3/9/2003 15:10'![39;49;00m$
  3211	[32misSystemWindow[39;49;00m$
  3212	[37m"answer whatever the receiver is a SystemWindow"[39;49;00m$
  3213		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3214	$
  3215	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
  3216	[32misText[39;49;00m$
  3217		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3218	$
  3219	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'pmm 7/6/2006 20:46'![39;49;00m$
  3220	[32misTrait[39;49;00m$
  3221		[37m"Return true if the receiver is a trait.[39;49;00m$
  3222	[37m	Note: Do not override in any class except TraitBehavior."[39;49;00m$
  3223		^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3224	$
  3225	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'tk 10/21/97 12:45'![39;49;00m$
  3226	[32misTransparent[39;49;00m$
  3227		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3228	$
  3229	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 8/14/2001 23:19'![39;49;00m$
  3230	[32misVariableBinding[39;49;00m$
  3231		[37m"Return true if I represent a literal variable binding"[39;49;00m$
  3232		^[36mfalse[39;49;00m$
  3233		[34m! ![39;49;00m$
  3234	$
  3235	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ls 7/14/1998 21:45'![39;49;00m$
  3236	[32misWebBrowser[39;49;00m$
  3237		[37m"whether this object is a web browser.  See class: Scamper"[39;49;00m$
  3238		^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3239	$
  3240	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/27/2000 06:58'![39;49;00m$
  3241	[32mknownName[39;49;00m$
  3242		[37m"If a formal name has been handed out for this object, answer it, else nil"[39;49;00m$
  3243		$
  3244		^ [04m[32mPreferences[39;49;00m [32mcapitalizedReferences[39;49;00m$
  3245			[36mifTrue:[39;49;00m$
  3246				[[04m[32mReferences[39;49;00m [32mkeyAtValue:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m]]$
  3247			[36mifFalse:[39;49;00m$
  3248				[[36mnil[39;49;00m][34m! ![39;49;00m$
  3249	$
  3250	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 9/27/96'![39;49;00m$
  3251	[32mname[39;49;00m$
  3252		[37m"Answer a name for the receiver.  This is used generically in the title of certain inspectors, such as the referred-to inspector, and specificially by various subsystems.  By default, we let the object just print itself out..  "[39;49;00m$
  3253	$
  3254		^ [36mself[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
  3255	$
  3256	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 11/19/2001 13:28'![39;49;00m$
  3257	[32mnameForViewer[39;49;00m$
  3258		[37m"Answer a name to be shown in a Viewer that is viewing the receiver"[39;49;00m$
  3259	$
  3260		|[31m aName [39;49;00m|$
  3261		([31maName[39;49;00m _ [36mself[39;49;00m [32muniqueNameForReferenceOrNil[39;49;00m) [32mifNotNil:[39;49;00m [^ [31maName[39;49;00m].$
  3262		([31maName[39;49;00m _ [36mself[39;49;00m [32mknownName[39;49;00m) [32mifNotNil:[39;49;00m [^ [31maName[39;49;00m].$
  3263	$
  3264		^ [([36mself[39;49;00m [32masString[39;49;00m [32mcopyWithout:[39;49;00m [04m[32mCharacter[39;49;00m [32mcr[39;49;00m) [32mtruncateTo:[39;49;00m  [34m27[39;49;00m] [32mifError:[39;49;00m$
  3265			[:[31mmsg[39;49;00m :[31mrcvr[39;49;00m | ^ [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32mprintString[39;49;00m][34m! ![39;49;00m$
  3266	$
  3267	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
  3268	[32mnotNil[39;49;00m$
  3269		[37m"Coerces nil to false and everything else to true."[39;49;00m$
  3270	$
  3271		^[36mtrue[39;49;00m[34m! ![39;49;00m$
  3272	$
  3273	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'tk 9/6/2001 19:15'![39;49;00m$
  3274	[32mopenInstanceBrowserWithTiles[39;49;00m$
  3275		[37m"Open up an instance browser on me with tiles as the code type, and with the search level as desired."[39;49;00m$
  3276	$
  3277		|[31m aBrowser [39;49;00m|$
  3278		[31maBrowser[39;49;00m _ [04m[32mInstanceBrowser[39;49;00m [36mnew[39;49;00m.$
  3279		[31maBrowser[39;49;00m [32museVocabulary:[39;49;00m [04m[32mVocabulary[39;49;00m [32mfullVocabulary[39;49;00m.$
  3280		[31maBrowser[39;49;00m [32mlimitClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m.$
  3281		[31maBrowser[39;49;00m [32mcontentsSymbol:[39;49;00m [33m#tiles[39;49;00m.		[37m"preset it to make extra buttons (tile menus)"[39;49;00m$
  3282		[31maBrowser[39;49;00m [32mopenOnObject:[39;49;00m [36mself[39;49;00m [32minWorld:[39;49;00m [04m[32mActiveWorld[39;49;00m [32mshowingSelector:[39;49;00m [36mnil[39;49;00m.$
  3283		[31maBrowser[39;49;00m [32mcontentsSymbol:[39;49;00m [33m#source[39;49;00m.$
  3284		[31maBrowser[39;49;00m [32mtoggleShowingTiles[39;49;00m.$
  3285	$
  3286		[37m"[39;49;00m$
  3287	[37m(2@3) openInstanceBrowserWithTiles.[39;49;00m$
  3288	[37mWatchMorph new openInstanceBrowserWithTiles[39;49;00m$
  3289	[37m"[39;49;00m[34m! ![39;49;00m$
  3290	$
  3291	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'tk 7/28/2005 04:50'![39;49;00m$
  3292	[32mrenameInternal:[39;49;00m [31mnewName[39;49;00m $
  3293		[37m"Change the internal name (because of a conflict) but leave the external name unchanged.  Change Player class name, but do not change the names that appear in tiles.  Any object that might be pointed to in the References dictionary might get this message sent to it upon reload"[39;49;00m$
  3294	$
  3295		^ [36mnil[39;49;00m	[37m"caller will renameTo:.  new name may be different"[39;49;00m[34m! ![39;49;00m$
  3296	$
  3297	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 2/27/2002 14:55'![39;49;00m$
  3298	[32mrenameTo:[39;49;00m [31mnewName[39;49;00m$
  3299		[37m"If the receiver has an inherent idea about its own name, it should take action here.  Any object that might be pointed to in the References dictionary might get this message sent to it upon reload"[39;49;00m[34m! ![39;49;00m$
  3300	$
  3301	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 1/18/2001 13:43'![39;49;00m$
  3302	[32mshowDiffs[39;49;00m$
  3303		[37m"Answer whether the receiver, serving as the model of a text-bearing entity, is 'showing differences' -- if it is, the editor may wish to show special feedback"[39;49;00m$
  3304	$
  3305		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3306	$
  3307	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/20/1999 14:52'![39;49;00m$
  3308	[32mstepAt:[39;49;00m [31mmillisecondClockValue[39;49;00m [32min:[39;49;00m [31maWindow[39;49;00m$
  3309	$
  3310		^ [36mself[39;49;00m [32mstepIn:[39;49;00m [31maWindow[39;49;00m[34m! ![39;49;00m$
  3311	$
  3312	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/19/1999 08:16'![39;49;00m$
  3313	[32mstepIn:[39;49;00m [31maWindow[39;49;00m$
  3314	$
  3315		^ [36mself[39;49;00m [32mstep[39;49;00m[34m! ![39;49;00m$
  3316	$
  3317	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/19/1999 08:21'![39;49;00m$
  3318	[32mstepTime[39;49;00m$
  3319		$
  3320		^ [34m1000[39;49;00m [37m"milliseconds -- default backstop for objects serving as models of system windows"[39;49;00m[34m! ![39;49;00m$
  3321	$
  3322	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/19/1999 08:22'![39;49;00m$
  3323	[32mstepTimeIn:[39;49;00m [31maSystemWindow[39;49;00m$
  3324		$
  3325		^ [34m1000[39;49;00m [37m"milliseconds -- default backstop for objects serving as models of system windows"[39;49;00m[34m! ![39;49;00m$
  3326	$
  3327	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 5/3/2001 18:22'![39;49;00m$
  3328	[32mvocabularyDemanded[39;49;00m$
  3329		[37m"Answer a vocabulary that the receiver insists be used when it is looked at in a Viewer.  This allows specific classes to insist on specific custom vocabularies"[39;49;00m$
  3330	$
  3331		^ [36mnil[39;49;00m[34m! ![39;49;00m$
  3332	$
  3333	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 11/13/2001 07:26'![39;49;00m$
  3334	[32mwantsDiffFeedback[39;49;00m$
  3335		[37m"Answer whether the receiver, serving as the model of a text-bearing entity, would like for 'diffs' green pane-border feedback to be shown"[39;49;00m$
  3336	$
  3337		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3338	$
  3339	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'di 1/8/1999 15:04'![39;49;00m$
  3340	[32mwantsSteps[39;49;00m$
  3341		[37m"Overridden by morphic classes whose instances want to be stepped,[39;49;00m$
  3342	[37m	or by model classes who want their morphic views to be stepped."[39;49;00m$
  3343	$
  3344		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3345	$
  3346	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/19/1999 08:26'![39;49;00m$
  3347	[32mwantsStepsIn:[39;49;00m [31maSystemWindow[39;49;00m$
  3348		$
  3349		^ [36mself[39;49;00m [32mwantsSteps[39;49;00m[34m! ![39;49;00m$
  3350	$
  3351	$
  3352	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'thumbnail'[39;49;00m[34m stamp: 'dgd 9/25/2004 23:17'![39;49;00m$
  3353	[32miconOrThumbnailOfSize:[39;49;00m [31maNumberOrPoint[39;49;00m $
  3354		[37m"Answer an appropiate form to represent the receiver"[39;49;00m$
  3355		^ [36mnil[39;49;00m[34m! ![39;49;00m$
  3356	$
  3357	$
  3358	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'translation support'[39;49;00m[34m![39;49;00m$
  3359	[32minline:[39;49;00m [31minlineFlag[39;49;00m$
  3360		[37m"For translation only; noop when running in Smalltalk."[39;49;00m[34m! ![39;49;00m$
  3361	$
  3362	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'translation support'[39;49;00m[34m![39;49;00m$
  3363	[32mvar:[39;49;00m [31mvarSymbol[39;49;00m [32mdeclareC:[39;49;00m [31mdeclString[39;49;00m$
  3364		[37m"For translation only; noop when running in Smalltalk."[39;49;00m[34m! ![39;49;00m$
  3365	$
  3366	$
  3367	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/11/2000 20:32'![39;49;00m$
  3368	[32mcapturedState[39;49;00m$
  3369		[37m"May be overridden in subclasses."[39;49;00m$
  3370	$
  3371		^ [36mself[39;49;00m [32mshallowCopy[39;49;00m$
  3372	[34m! ![39;49;00m$
  3373	$
  3374	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/11/2000 20:29'![39;49;00m$
  3375	[32mcommandHistory[39;49;00m$
  3376		[37m"Return the command history for the receiver"[39;49;00m$
  3377		|[31m w [39;49;00m|$
  3378		([31mw[39;49;00m _ [36mself[39;49;00m [32mcurrentWorld[39;49;00m) [32mifNotNil:[39;49;00m [^ [31mw[39;49;00m [32mcommandHistory[39;49;00m].$
  3379		^ [04m[32mCommandHistory[39;49;00m [36mnew[39;49;00m. [37m"won't really record anything but prevent breaking things"[39;49;00m[34m! ![39;49;00m$
  3380	$
  3381	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 12/12/2000 15:01'![39;49;00m$
  3382	[32mpurgeAllCommands[39;49;00m$
  3383		[37m"Purge all commands for this object"[39;49;00m$
  3384		[04m[32mPreferences[39;49;00m [32museUndo[39;49;00m [36mifFalse:[39;49;00m [^ [36mself[39;49;00m]. [37m"get out quickly"[39;49;00m$
  3385		[36mself[39;49;00m [32mcommandHistory[39;49;00m [32mpurgeAllCommandsSuchThat:[39;49;00m [:[31mcmd[39;49;00m | [31mcmd[39;49;00m [32mundoTarget[39;49;00m [32m==[39;49;00m [36mself[39;49;00m].$
  3386	[34m! ![39;49;00m$
  3387	$
  3388	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/12/2000 08:15'![39;49;00m$
  3389	[32mredoFromCapturedState:[39;49;00m [31mst[39;49;00m $
  3390		[37m"May be overridden in subclasses.  See also capturedState"[39;49;00m$
  3391	$
  3392		[36mself[39;49;00m [32mundoFromCapturedState:[39;49;00m [31mst[39;49;00m  [37m"Simple cases are symmetric"[39;49;00m$
  3393	[34m! ![39;49;00m$
  3394	$
  3395	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'sw 11/16/2000 14:42'![39;49;00m$
  3396	[32mrefineRedoTarget:[39;49;00m [31mtarget[39;49;00m [32mselector:[39;49;00m [31maSymbol[39;49;00m [32marguments:[39;49;00m [31marguments[39;49;00m [32min:[39;49;00m [31mrefineBlock[39;49;00m $
  3397		[37m"Any object can override this method to refine its redo specification"[39;49;00m$
  3398	$
  3399		^ [31mrefineBlock[39;49;00m$
  3400			[32mvalue:[39;49;00m [31mtarget[39;49;00m$
  3401			[32mvalue:[39;49;00m [31maSymbol[39;49;00m$
  3402			[32mvalue:[39;49;00m [31marguments[39;49;00m[34m! ![39;49;00m$
  3403	$
  3404	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'sw 11/16/2000 14:42'![39;49;00m$
  3405	[32mrefineUndoTarget:[39;49;00m [31mtarget[39;49;00m [32mselector:[39;49;00m [31maSymbol[39;49;00m [32marguments:[39;49;00m [31marguments[39;49;00m [32min:[39;49;00m [31mrefineBlock[39;49;00m $
  3406		[37m"Any object can override this method to refine its undo specification"[39;49;00m$
  3407	$
  3408		^ [31mrefineBlock[39;49;00m$
  3409			[32mvalue:[39;49;00m [31mtarget[39;49;00m$
  3410			[32mvalue:[39;49;00m [31maSymbol[39;49;00m$
  3411			[32mvalue:[39;49;00m [31marguments[39;49;00m[34m! ![39;49;00m$
  3412	$
  3413	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/11/2000 20:30'![39;49;00m$
  3414	[32mrememberCommand:[39;49;00m [31maCommand[39;49;00m$
  3415		[37m"Remember the given command for undo"[39;49;00m$
  3416		[04m[32mPreferences[39;49;00m [32museUndo[39;49;00m [36mifFalse:[39;49;00m [^ [36mself[39;49;00m]. [37m"get out quickly"[39;49;00m$
  3417		^ [36mself[39;49;00m [32mcommandHistory[39;49;00m [32mrememberCommand:[39;49;00m [31maCommand[39;49;00m[34m! ![39;49;00m$
  3418	$
  3419	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/11/2000 20:30'![39;49;00m$
  3420	[32mrememberUndoableAction:[39;49;00m [31mactionBlock[39;49;00m [32mnamed:[39;49;00m [31mcaption[39;49;00m$
  3421		|[31m cmd result [39;49;00m|$
  3422		[31mcmd[39;49;00m _ [04m[32mCommand[39;49;00m [36mnew[39;49;00m [32mcmdWording:[39;49;00m [31mcaption[39;49;00m.$
  3423		[31mcmd[39;49;00m [32mundoTarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#undoFromCapturedState:[39;49;00m [32margument:[39;49;00m [36mself[39;49;00m [32mcapturedState[39;49;00m.$
  3424		[31mresult[39;49;00m _ [31mactionBlock[39;49;00m [32mvalue[39;49;00m.$
  3425		[31mcmd[39;49;00m [32mredoTarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#redoFromCapturedState:[39;49;00m [32margument:[39;49;00m [36mself[39;49;00m [32mcapturedState[39;49;00m.$
  3426		[36mself[39;49;00m [32mrememberCommand:[39;49;00m [31mcmd[39;49;00m.$
  3427		^ [31mresult[39;49;00m[34m! ![39;49;00m$
  3428	$
  3429	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/11/2000 20:32'![39;49;00m$
  3430	[32mundoFromCapturedState:[39;49;00m [31mst[39;49;00m $
  3431		[37m"May be overridden in subclasses.  See also capturedState"[39;49;00m$
  3432	$
  3433		[36mself[39;49;00m [32mcopyFrom:[39;49;00m [31mst[39;49;00m$
  3434	[34m! ![39;49;00m$
  3435	$
  3436	$
  3437	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m![39;49;00m$
  3438	[32mchanged[39;49;00m$
  3439		[37m"Receiver changed in a general way; inform all the dependents by [39;49;00m$
  3440	[37m	sending each dependent an update: message."[39;49;00m$
  3441	$
  3442		[36mself[39;49;00m [32mchanged:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  3443	$
  3444	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m![39;49;00m$
  3445	[32mchanged:[39;49;00m [31maParameter[39;49;00m $
  3446		[37m"Receiver changed. The change is denoted by the argument aParameter. [39;49;00m$
  3447	[37m	Usually the argument is a Symbol that is part of the dependent's change [39;49;00m$
  3448	[37m	protocol. Inform all of the dependents."[39;49;00m$
  3449	$
  3450		[36mself[39;49;00m [32mdependents[39;49;00m [32mdo:[39;49;00m [:[31maDependent[39;49;00m | [31maDependent[39;49;00m [32mupdate:[39;49;00m [31maParameter[39;49;00m][34m! ![39;49;00m$
  3451	$
  3452	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'nk 2/17/2004 11:12'![39;49;00m$
  3453	[32mchanged:[39;49;00m [31manAspect[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m$
  3454		[37m"Receiver changed. The change is denoted by the argument anAspect. [39;49;00m$
  3455	[37m	Usually the argument is a Symbol that is part of the dependent's change [39;49;00m$
  3456	[37m	protocol. Inform all of the dependents. Also pass anObject for additional information."[39;49;00m$
  3457	$
  3458		[36mself[39;49;00m [32mdependents[39;49;00m [32mdo:[39;49;00m [:[31maDependent[39;49;00m | [31maDependent[39;49;00m [32mupdate:[39;49;00m [31manAspect[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m][34m! ![39;49;00m$
  3459	$
  3460	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'sw 10/12/1999 18:15'![39;49;00m$
  3461	[32mhandledListVerification[39;49;00m$
  3462		[37m"When a self-updating PluggableListMorph lazily checks to see the state of affairs, it first gives its model an opportunity to handle the list verification itself (this is appropriate for some models, such as VersionsBrowser); if a list's model has indeed handled things itself, it returns true here"[39;49;00m$
  3463	$
  3464		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3465	$
  3466	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'sw 10/31/1999 00:15'![39;49;00m$
  3467	[32mnoteSelectionIndex:[39;49;00m [31manInteger[39;49;00m [32mfor:[39;49;00m [31maSymbol[39;49;00m$
  3468		[37m"backstop"[39;49;00m[34m! ![39;49;00m$
  3469	$
  3470	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m![39;49;00m$
  3471	[32mokToChange[39;49;00m$
  3472		[37m"Allows a controller to ask this of any model"[39;49;00m$
  3473		^ [36mtrue[39;49;00m[34m! ![39;49;00m$
  3474	$
  3475	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'sw 10/19/1999 14:39'![39;49;00m$
  3476	[32mupdateListsAndCodeIn:[39;49;00m [31maWindow[39;49;00m$
  3477		[36mself[39;49;00m [32mcanDiscardEdits[39;49;00m [36mifFalse:[39;49;00m [^ [36mself[39;49;00m].$
  3478		[31maWindow[39;49;00m [32mupdatablePanes[39;49;00m [32mdo:[39;49;00m [:[31maPane[39;49;00m | [31maPane[39;49;00m [32mverifyContents[39;49;00m][34m! ![39;49;00m$
  3479	$
  3480	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'sma 2/29/2000 20:05'![39;49;00m$
  3481	[32mupdate:[39;49;00m [31maParameter[39;49;00m $
  3482		[37m"Receive a change notice from an object of whom the receiver is a [39;49;00m$
  3483	[37m	dependent. The default behavior is to do nothing; a subclass might want [39;49;00m$
  3484	[37m	to change itself in some way."[39;49;00m$
  3485	$
  3486		^ [36mself[39;49;00m[34m! ![39;49;00m$
  3487	$
  3488	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'nk 2/17/2004 11:13'![39;49;00m$
  3489	[32mupdate:[39;49;00m [31manAspect[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m$
  3490		[37m"Receive a change notice from an object of whom the receiver is a [39;49;00m$
  3491	[37m	dependent. The default behavior is to call update:,[39;49;00m$
  3492	[37m	which by default does nothing; a subclass might want [39;49;00m$
  3493	[37m	to change itself in some way."[39;49;00m$
  3494	$
  3495		^ [36mself[39;49;00m [32mupdate:[39;49;00m [31manAspect[39;49;00m[34m! ![39;49;00m$
  3496	$
  3497	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'jm 8/20/1998 18:26'![39;49;00m$
  3498	[32mwindowIsClosing[39;49;00m$
  3499		[37m"This message is used to inform a models that its window is closing. Most models do nothing, but some, such as the Debugger, must do some cleanup. Note that this mechanism must be used with care by models that support multiple views, since one view may be closed while others left open."[39;49;00m$
  3500	[34m! ![39;49;00m$
  3501	$
  3502	$
  3503	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 10/4/1999 08:13'![39;49;00m$
  3504	[32maddModelItemsToWindowMenu:[39;49;00m [31maMenu[39;49;00m$
  3505		[37m"aMenu is being constructed to be presented to the user in response to the user's pressing on the menu widget in the title bar of a morphic window.  Here, the model is given the opportunity to add any model-specific items to the menu, whose default target is the SystemWindow itself."[39;49;00m[34m! ![39;49;00m$
  3506	$
  3507	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 10/5/1998 14:39'![39;49;00m$
  3508	[32maddModelMenuItemsTo:[39;49;00m [31maCustomMenu[39;49;00m [32mforMorph:[39;49;00m [31maMorph[39;49;00m [32mhand:[39;49;00m [31maHandMorph[39;49;00m $
  3509		[37m"The receiver serves as the model for aMorph; a menu is being constructed for the morph, and here the receiver is able to add its own items"[39;49;00m$
  3510	[34m! ![39;49;00m$
  3511	$
  3512	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sma 11/12/2000 11:43'![39;49;00m$
  3513	[32masExplorerString[39;49;00m$
  3514		^ [36mself[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
  3515	$
  3516	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 7/13/1999 15:53'![39;49;00m$
  3517	[32mdefaultBackgroundColor[39;49;00m$
  3518		[37m"Answer the color to be used as the base window color for a window whose model is an object of the receiver's class"[39;49;00m$
  3519		$
  3520		^ [04m[32mPreferences[39;49;00m [32mwindowColorFor:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m[34m! ![39;49;00m$
  3521	$
  3522	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m![39;49;00m$
  3523	[32mdefaultLabelForInspector[39;49;00m$
  3524		[37m"Answer the default label to be used for an Inspector window on the receiver."[39;49;00m$
  3525	$
  3526		^ [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m[34m! ![39;49;00m$
  3527	$
  3528	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'RAA 7/10/2000 08:11'![39;49;00m$
  3529	[32meToyStreamedRepresentationNotifying:[39;49;00m [31maWidget[39;49;00m$
  3530	$
  3531		|[31m outData [39;49;00m|$
  3532		[ [31moutData[39;49;00m _ [04m[32mSmartRefStream[39;49;00m [32mstreamedRepresentationOf:[39;49;00m [36mself[39;49;00m ] $
  3533			[32mon:[39;49;00m [04m[32mProgressInitiationException[39;49;00m$
  3534			[32mdo:[39;49;00m [ :[31mex[39;49;00m | $
  3535				[31mex[39;49;00m [32msendNotificationsTo:[39;49;00m [ :[31mmin[39;49;00m :[31mmax[39;49;00m :[31mcurr[39;49;00m |$
  3536					[31maWidget[39;49;00m [32mifNotNil:[39;49;00m [[31maWidget[39;49;00m [32mflashIndicator:[39;49;00m [33m#working[39;49;00m].$
  3537				].$
  3538			].$
  3539		^[31moutData[39;49;00m$
  3540	[34m! ![39;49;00m$
  3541	$
  3542	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'ar 9/27/2005 20:29'![39;49;00m$
  3543	[32mexplore[39;49;00m$
  3544		^[04m[32mToolSet[39;49;00m [32mexplore:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  3545	$
  3546	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 8/15/97 17:25'![39;49;00m$
  3547	[32mfullScreenSize[39;49;00m$
  3548		[37m"Answer the size to which a window displaying the receiver should be set"[39;49;00m$
  3549		|[31m adj [39;49;00m|$
  3550		[31madj[39;49;00m _ ([34m3[39;49;00m [32m*[39;49;00m [04m[32mPreferences[39;49;00m [32mscrollBarWidth[39;49;00m) [32m@[39;49;00m [34m0[39;49;00m.$
  3551		^ [04m[32mRectangle[39;49;00m [32morigin:[39;49;00m [31madj[39;49;00m [32mextent:[39;49;00m ([04m[32mDisplayScreen[39;49;00m [32mactualScreenSize[39;49;00m [32m-[39;49;00m [31madj[39;49;00m)[34m! ![39;49;00m$
  3552	$
  3553	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'RAA 6/21/1999 11:27'![39;49;00m$
  3554	[32mhasContentsInExplorer[39;49;00m$
  3555	$
  3556		^[36mself[39;49;00m [32mbasicSize[39;49;00m [32m>[39;49;00m [34m0[39;49;00m [32mor:[39;49;00m [[36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32misEmpty[39;49;00m [32mnot[39;49;00m]$
  3557	[34m! ![39;49;00m$
  3558	$
  3559	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'rbb 3/1/2005 09:28'![39;49;00m$
  3560	[32minform:[39;49;00m [31maString[39;49;00m$
  3561		[37m"Display a message for the user to read and then dismiss. 6/9/96 sw"[39;49;00m$
  3562	$
  3563		[31maString[39;49;00m [32misEmptyOrNil[39;49;00m [36mifFalse:[39;49;00m [[04m[32mUIManager[39;49;00m [32mdefault[39;49;00m [32minform:[39;49;00m [31maString[39;49;00m][34m! ![39;49;00m$
  3564	$
  3565	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m![39;49;00m$
  3566	[32minitialExtent[39;49;00m$
  3567		[37m"Answer the desired extent for the receiver when a view on it is first opened on the screen. [39;49;00m$
  3568	[37m	5/22/96 sw: in the absence of any override, obtain from RealEstateAgent"[39;49;00m$
  3569	$
  3570		^ [04m[32mRealEstateAgent[39;49;00m [32mstandardWindowExtent[39;49;00m[34m! ![39;49;00m$
  3571	$
  3572	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'ar 9/27/2005 20:30'![39;49;00m$
  3573	[32minspectWithLabel:[39;49;00m [31maLabel[39;49;00m$
  3574		[37m"Create and schedule an Inspector in which the user can examine the receiver's variables."[39;49;00m$
  3575		^[04m[32mToolSet[39;49;00m [32minspect:[39;49;00m [36mself[39;49;00m [32mlabel:[39;49;00m [31maLabel[39;49;00m[34m! ![39;49;00m$
  3576	$
  3577	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 6/12/2001 11:09'![39;49;00m$
  3578	[32mlaunchPartVia:[39;49;00m [31maSelector[39;49;00m$
  3579		[37m"Obtain a morph by sending aSelector to self, and attach it to the morphic hand.  This provides a general protocol for parts bins"[39;49;00m$
  3580	$
  3581		|[31m aMorph [39;49;00m|$
  3582		[31maMorph[39;49;00m _ [36mself[39;49;00m [32mperform:[39;49;00m [31maSelector[39;49;00m.$
  3583		[31maMorph[39;49;00m [32msetProperty:[39;49;00m [33m#beFullyVisibleAfterDrop[39;49;00m [32mtoValue:[39;49;00m [36mtrue[39;49;00m.$
  3584		[31maMorph[39;49;00m [32mopenInHand[39;49;00m[34m! ![39;49;00m$
  3585	$
  3586	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 6/17/2004 01:47'![39;49;00m$
  3587	[32mlaunchPartVia:[39;49;00m [31maSelector[39;49;00m [32mlabel:[39;49;00m [31maString[39;49;00m$
  3588		[37m"Obtain a morph by sending aSelector to self, and attach it to the morphic hand.  This provides a general protocol for parts bins"[39;49;00m$
  3589	$
  3590		|[31m aMorph [39;49;00m|$
  3591		[31maMorph[39;49;00m _ [36mself[39;49;00m [32mperform:[39;49;00m [31maSelector[39;49;00m.$
  3592		[31maMorph[39;49;00m [32msetNameTo:[39;49;00m ([04m[32mActiveWorld[39;49;00m [32munusedMorphNameLike:[39;49;00m [31maString[39;49;00m).$
  3593		[31maMorph[39;49;00m [32msetProperty:[39;49;00m [33m#beFullyVisibleAfterDrop[39;49;00m [32mtoValue:[39;49;00m [36mtrue[39;49;00m.$
  3594		[31maMorph[39;49;00m [32mopenInHand[39;49;00m[34m! ![39;49;00m$
  3595	$
  3596	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 10/16/2000 11:11'![39;49;00m$
  3597	[32mlaunchTileToRefer[39;49;00m$
  3598		[37m"Create a tile to reference the receiver, and attach it to the hand"[39;49;00m$
  3599	$
  3600		[36mself[39;49;00m [32mcurrentHand[39;49;00m [32mattachMorph:[39;49;00m [36mself[39;49;00m [32mtileToRefer[39;49;00m[34m! ![39;49;00m$
  3601	$
  3602	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'di 5/11/1999 22:26'![39;49;00m$
  3603	[32mmodelSleep[39;49;00m$
  3604		[37m"A window with me as model is being exited or collapsed or closed.[39;49;00m$
  3605	[37m	Default response is no-op"[39;49;00m [34m! ![39;49;00m$
  3606	$
  3607	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'di 5/11/1999 22:01'![39;49;00m$
  3608	[32mmodelWakeUp[39;49;00m$
  3609		[37m"A window with me as model is being entered or expanded.  Default response is no-op"[39;49;00m [34m! ![39;49;00m$
  3610	$
  3611	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 10/16/1999 22:45'![39;49;00m$
  3612	[32mmodelWakeUpIn:[39;49;00m [31maWindow[39;49;00m$
  3613		[37m"A window with me as model is being entered or expanded.  Default response is no-op"[39;49;00m $
  3614		[36mself[39;49;00m [32mmodelWakeUp[39;49;00m[34m! ![39;49;00m$
  3615	$
  3616	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 3/8/1999 15:27'![39;49;00m$
  3617	[32mmouseUpBalk:[39;49;00m [31mevt[39;49;00m$
  3618		[37m"A button I own got a mouseDown, but the user moved out before letting up.  Certain kinds of objects (so-called 'radio buttons', for example, and other structures that must always have some selection, e.g. PaintBoxMorph) wish to take special action in this case; this default does nothing."[39;49;00m$
  3619	[34m! ![39;49;00m$
  3620	$
  3621	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 8/22/97 13:14'![39;49;00m$
  3622	[32mnewTileMorphRepresentative[39;49;00m$
  3623		^ [04m[32mTileMorph[39;49;00m [36mnew[39;49;00m [32msetLiteral:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  3624	$
  3625	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'jcg 11/1/2001 13:13'![39;49;00m$
  3626	[32mnotYetImplemented[39;49;00m$
  3627		[36mself[39;49;00m [32minform:[39;49;00m [33m'Not yet implemented ('[39;49;00m[32m,[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m')'[39;49;00m[34m! ![39;49;00m$
  3628	$
  3629	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'di 6/10/1998 15:06'![39;49;00m$
  3630	[32mwindowReqNewLabel:[39;49;00m [31mlabelString[39;49;00m$
  3631		[37m"My window's title has been edited.[39;49;00m$
  3632	[37m	Return true if this is OK, and override for further behavior."[39;49;00m$
  3633	$
  3634		^ [36mtrue[39;49;00m[34m! ![39;49;00m$
  3635	$
  3636	$
  3637	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 10/16/2000 10:35'![39;49;00m$
  3638	[32massureUniClass[39;49;00m$
  3639		[37m"If the receiver is not yet an instance of a uniclass, create a uniclass for it and make the receiver become an instance of that class."[39;49;00m$
  3640	$
  3641		|[31m anInstance [39;49;00m|$
  3642		[36mself[39;49;00m [32mbelongsToUniClass[39;49;00m [36mifTrue:[39;49;00m [^ [36mself[39;49;00m].$
  3643		[31manInstance[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32minstanceOfUniqueClass[39;49;00m.$
  3644		[36mself[39;49;00m [32mbecome:[39;49;00m ([36mself[39;49;00m [32mas:[39;49;00m [31manInstance[39;49;00m [32mclass[39;49;00m).$
  3645		^ [31manInstance[39;49;00m[34m! ![39;49;00m$
  3646	$
  3647	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 10/16/2000 10:41'![39;49;00m$
  3648	[32mbelongsToUniClass[39;49;00m$
  3649		[37m"Answer whether the receiver belongs to a uniclass.  For the moment (this is not entirely satisfactory) this is precisely equated with the classname ending in a digit"[39;49;00m$
  3650	$
  3651		^ [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32mendsWithDigit[39;49;00m[34m! ![39;49;00m$
  3652	$
  3653	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 12/11/2000 15:37'![39;49;00m$
  3654	[32mbrowseOwnClassSubProtocol[39;49;00m$
  3655		[37m"Open up a ProtocolBrowser on the subprotocol of the receiver"[39;49;00m$
  3656	$
  3657		[04m[32mProtocolBrowser[39;49;00m [32mopenSubProtocolForClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m$
  3658	[34m! ![39;49;00m$
  3659	$
  3660	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/4/2001 00:51'![39;49;00m$
  3661	[32mcategoriesForViewer:[39;49;00m [31maViewer[39;49;00m$
  3662		[37m"Answer a list of categories to offer in the given viewer"[39;49;00m$
  3663	$
  3664		^ [31maViewer[39;49;00m [32mcurrentVocabulary[39;49;00m [32mcategoryListForInstance:[39;49;00m [36mself[39;49;00m [32mofClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mlimitClass:[39;49;00m [31maViewer[39;49;00m [32mlimitClass[39;49;00m[34m! ![39;49;00m$
  3665	$
  3666	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/3/2001 22:08'![39;49;00m$
  3667	[32mcategoriesForVocabulary:[39;49;00m [31maVocabulary[39;49;00m [32mlimitClass:[39;49;00m [31maLimitClass[39;49;00m$
  3668		[37m"Answer a list of categories of methods for the receiver when using the given vocabulary, given that one considers only methods that are implemented not further away than aLimitClass"[39;49;00m$
  3669	$
  3670		^ [31maVocabulary[39;49;00m [32mcategoryListForInstance:[39;49;00m [36mself[39;49;00m [32mofClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mlimitClass:[39;49;00m [31maLimitClass[39;49;00m[34m! ![39;49;00m$
  3671	$
  3672	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 10/25/2000 07:20'![39;49;00m$
  3673	[32mchooseNewNameForReference[39;49;00m$
  3674		[37m"Offer an opportunity for the receiver, presumed already to be known in the References registry, to be renamed"[39;49;00m$
  3675	$
  3676		|[31m  nameSym current newName [39;49;00m|$
  3677		[31mcurrent[39;49;00m _ [04m[32mReferences[39;49;00m [32mkeyAtValue:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'not found in References'[39;49;00m].$
  3678	$
  3679		[31mnewName[39;49;00m _ [04m[32mFillInTheBlank[39;49;00m [32mrequest:[39;49;00m [33m'Please enter new name'[39;49;00m [32minitialAnswer:[39;49;00m [31mcurrent[39;49;00m.$
  3680		[37m"Want to user some better way of determining the validity of the chosen identifier, and also want to give more precise diagnostic if the string the user types in is not acceptable.  Work to be done here."[39;49;00m$
  3681	$
  3682		[31mnewName[39;49;00m [32misEmpty[39;49;00m [36mifTrue:[39;49;00m [^ [36mnil[39;49;00m].$
  3683		(([04m[32mScanner[39;49;00m [32misLiteralSymbol:[39;49;00m [31mnewName[39;49;00m) [32mand:[39;49;00m [([31mnewName[39;49;00m [32mincludes:[39;49;00m [33m$:[39;49;00m) [32mnot[39;49;00m])$
  3684			[36mifTrue:[39;49;00m$
  3685				[[31mnameSym[39;49;00m _ [31mnewName[39;49;00m [32mcapitalized[39;49;00m [32masSymbol[39;49;00m.$
  3686				((([04m[32mReferences[39;49;00m [32mincludesKey:[39;49;00m  [31mnameSym[39;49;00m) [32mnot[39;49;00m [32mand:[39;49;00m$
  3687					[([04m[32mSmalltalk[39;49;00m [32mincludesKey:[39;49;00m [31mnameSym[39;49;00m) [32mnot[39;49;00m]) [32mand:[39;49;00m$
  3688							[([04m[32mScriptingSystem[39;49;00m [32mallKnownClassVariableNames[39;49;00m [32mincludes:[39;49;00m [31mnameSym[39;49;00m) [32mnot[39;49;00m])$
  3689						[36mifTrue:[39;49;00m$
  3690							[([04m[32mReferences[39;49;00m [32massociationAt:[39;49;00m [31mcurrent[39;49;00m) [32mkey:[39;49;00m [31mnameSym[39;49;00m.$
  3691							[04m[32mReferences[39;49;00m [32mrehash[39;49;00m.$
  3692							^ [31mnameSym[39;49;00m]].$
  3693		[36mself[39;49;00m [32minform:[39;49;00m [33m'Sorry, that name is not available.'[39;49;00m.$
  3694		^ [36mnil[39;49;00m[34m! ![39;49;00m$
  3695	$
  3696	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/3/2001 21:22'![39;49;00m$
  3697	[32mdefaultLimitClassForVocabulary:[39;49;00m [31maVocabulary[39;49;00m$
  3698		[37m"Answer the class to use, by default, as the limit class on a protocol browser or viewer opened up on the receiver, within the purview of the Vocabulary provided"[39;49;00m$
  3699	$
  3700		^ ([31maVocabulary[39;49;00m [32misKindOf:[39;49;00m [04m[32mFullVocabulary[39;49;00m)$
  3701			[36mifTrue:[39;49;00m$
  3702				 [[36mself[39;49;00m [32mclass[39;49;00m [32msuperclass[39;49;00m [32m==[39;49;00m [04m[32mObject[39;49;00m$
  3703					[36mifTrue:[39;49;00m$
  3704						[[36mself[39;49;00m [32mclass[39;49;00m]$
  3705					[36mifFalse:[39;49;00m$
  3706						[[36mself[39;49;00m [32mclass[39;49;00m [32msuperclass[39;49;00m]]$
  3707			[36mifFalse:[39;49;00m$
  3708				[[04m[32mProtoObject[39;49;00m][34m! ![39;49;00m$
  3709	$
  3710	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 2/14/2000 14:24'![39;49;00m$
  3711	[32mdefaultNameStemForInstances[39;49;00m$
  3712		[37m"Answer a basis for names of default instances of the receiver.  The default is to let the class specify, but certain instances will want to override.  (PasteUpMorphs serving as Worlds come to mind"[39;49;00m$
  3713	$
  3714		^ [36mself[39;49;00m [32mclass[39;49;00m [32mdefaultNameStemForInstances[39;49;00m[34m! ![39;49;00m$
  3715	$
  3716	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 5/22/2001 16:53'![39;49;00m$
  3717	[32melementTypeFor:[39;49;00m [31maStringOrSymbol[39;49;00m [32mvocabulary:[39;49;00m [31maVocabulary[39;49;00m$
  3718		[37m"Answer a symbol characterizing what kind of element aStringOrSymbol represents.  Realistically, at present, this always just returns #systemScript; a prototyped but not-incorporated architecture supported use of a leading colon to characterize an inst var of a system class, and for the moment we still see its remnant here."[39;49;00m$
  3719	$
  3720		[36mself[39;49;00m [32mflag:[39;49;00m [33m#deferred[39;49;00m.  [37m"a loose end in the non-player case"[39;49;00m$
  3721		^ [33m#systemScript[39;49;00m[34m! ![39;49;00m$
  3722	$
  3723	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 5/4/2001 07:04'![39;49;00m$
  3724	[32mexternalName[39;49;00m$
  3725		[37m"Answer an external name by which the receiver is known.  Generic implementation here is a transitional backstop. probably"[39;49;00m$
  3726	$
  3727		^ [36mself[39;49;00m [32mnameForViewer[39;49;00m[34m! ![39;49;00m$
  3728	$
  3729	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 5/4/2001 07:06'![39;49;00m$
  3730	[32mgraphicForViewerTab[39;49;00m$
  3731		[37m"When a Viewer is open on the receiver, its tab needs some graphic to show to the user.  Answer a form or a morph to serve that purpose.  A generic image is used for arbitrary objects, but note my reimplementors"[39;49;00m$
  3732		$
  3733		^ [04m[32mScriptingSystem[39;49;00m [32mformAtKey:[39;49;00m [33m'Image'[39;49;00m[34m! ![39;49;00m$
  3734	$
  3735	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 5/4/2001 07:08'![39;49;00m$
  3736	[32mhasUserDefinedSlots[39;49;00m$
  3737		[37m"Answer whether the receiver has any user-defined slots, in the omniuser sense of the term.  This is needed to allow Viewers to look at any object, not just at Players."[39;49;00m$
  3738	$
  3739		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3740	$
  3741	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/22/2002 14:07'![39;49;00m$
  3742	[32minfoFor:[39;49;00m [31manElement[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m$
  3743		[37m"The user made a gesture asking for info/menu relating to me.  Some of the messages dispatched here are not yet available in this image"[39;49;00m$
  3744	$
  3745		|[31m aMenu elementType [39;49;00m|$
  3746		[31melementType[39;49;00m _ [36mself[39;49;00m [32melementTypeFor:[39;49;00m [31manElement[39;49;00m [32mvocabulary:[39;49;00m [31maViewer[39;49;00m [32mcurrentVocabulary[39;49;00m.$
  3747		(([31melementType[39;49;00m [32m=[39;49;00m [33m#systemSlot[39;49;00m) [32m|[39;49;00m ([31melementType[39;49;00m [32m==[39;49;00m [33m#userSlot[39;49;00m))$
  3748			[36mifTrue:[39;49;00m	[^ [36mself[39;49;00m [32mslotInfoButtonHitFor:[39;49;00m [31manElement[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m].$
  3749		[36mself[39;49;00m [32mflag:[39;49;00m [33m#deferred[39;49;00m.  [37m"Use a traditional MenuMorph, and reinstate the pacify thing"[39;49;00m$
  3750		[31maMenu[39;49;00m _ [04m[32mMenuMorph[39;49;00m [36mnew[39;49;00m [32mdefaultTarget:[39;49;00m [31maViewer[39;49;00m.$
  3751		[33m#([39;49;00m	[33m([39;49;00m[33m'implementors'[39;49;00m			[33mbrowseImplementorsOf:[39;49;00m[33m)[39;49;00m$
  3752			[33m([39;49;00m[33m'senders'[39;49;00m				[33mbrowseSendersOf:[39;49;00m[33m)[39;49;00m$
  3753			[33m([39;49;00m[33m'versions'[39;49;00m				[33mbrowseVersionsOf:[39;49;00m[33m)[39;49;00m$
  3754			[33m-[39;49;00m$
  3755			[33m([39;49;00m[33m'browse full'[39;49;00m			[33mbrowseMethodFull:[39;49;00m[33m)[39;49;00m$
  3756			[33m([39;49;00m[33m'inheritance'[39;49;00m			[33mbrowseMethodInheritance:[39;49;00m[33m)[39;49;00m$
  3757			[33m-[39;49;00m$
  3758			[33m([39;49;00m[33m'about this method'[39;49;00m		[33maboutMethod:[39;49;00m[33m)[39;49;00m[33m)[39;49;00m [32mdo:[39;49;00m$
  3759	$
  3760				[:[31mpair[39;49;00m |$
  3761					[31mpair[39;49;00m [32m=[39;49;00m [33m'-'[39;49;00m$
  3762						[36mifTrue:[39;49;00m$
  3763							[[31maMenu[39;49;00m [32maddLine[39;49;00m]$
  3764						[36mifFalse:[39;49;00m$
  3765							[[31maMenu[39;49;00m [32madd:[39;49;00m [31mpair[39;49;00m [32mfirst[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32mselector:[39;49;00m [31mpair[39;49;00m [32msecond[39;49;00m [32margument:[39;49;00m [31manElement[39;49;00m]].$
  3766		[31maMenu[39;49;00m [32maddLine[39;49;00m.$
  3767		[31maMenu[39;49;00m [32mdefaultTarget:[39;49;00m [36mself[39;49;00m.$
  3768		[33m#([39;49;00m	[33m([39;49;00m[33m'destroy script'[39;49;00m		[33mremoveScript:[39;49;00m[33m)[39;49;00m$
  3769			[33m([39;49;00m[33m'rename script'[39;49;00m		[33mrenameScript:[39;49;00m[33m)[39;49;00m$
  3770			[33m([39;49;00m[33m'pacify script'[39;49;00m		[33mpacifyScript:[39;49;00m[33m)[39;49;00m[33m)[39;49;00m [32mdo:[39;49;00m$
  3771				[:[31mpair[39;49;00m |$
  3772					[31maMenu[39;49;00m [32madd:[39;49;00m [31mpair[39;49;00m [32mfirst[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [31mpair[39;49;00m [32msecond[39;49;00m [32margument:[39;49;00m [31manElement[39;49;00m].$
  3773	$
  3774		[31maMenu[39;49;00m [32maddLine[39;49;00m.$
  3775		[31maMenu[39;49;00m  [32madd:[39;49;00m [33m'show categories....'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32mselector:[39;49;00m [33m#showCategoriesFor:[39;49;00m [32margument:[39;49;00m [31manElement[39;49;00m.$
  3776		[31maMenu[39;49;00m [32mitems[39;49;00m [32msize[39;49;00m [32m==[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m  [37m"won't happen at the moment a/c the above"[39;49;00m$
  3777			[[31maMenu[39;49;00m [32madd:[39;49;00m [33m'ok'[39;49;00m [32maction:[39;49;00m [36mnil[39;49;00m].  [37m"in case it was a slot -- weird, transitional"[39;49;00m$
  3778	$
  3779		[31maMenu[39;49;00m [32maddTitle:[39;49;00m [31manElement[39;49;00m [32masString[39;49;00m[32m,[39;49;00m [33m' ('[39;49;00m[32m,[39;49;00m [31melementType[39;49;00m[32m,[39;49;00m [33m')'[39;49;00m.$
  3780	$
  3781		[31maMenu[39;49;00m [32mpopUpInWorld:[39;49;00m [36mself[39;49;00m [32mcurrentWorld[39;49;00m.$
  3782	 [34m! ![39;49;00m$
  3783	$
  3784	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 9/26/2001 11:58'![39;49;00m$
  3785	[32minitialTypeForSlotNamed:[39;49;00m [31maName[39;49;00m$
  3786		[37m"Answer the initial type to be ascribed to the given instance variable"[39;49;00m$
  3787	$
  3788		^ [33m#Object[39;49;00m[34m! ![39;49;00m$
  3789	$
  3790	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'ar 5/26/2001 16:13'![39;49;00m$
  3791	[32misPlayerLike[39;49;00m$
  3792		[37m"Return true if the receiver is a player-like object"[39;49;00m$
  3793		^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3794	$
  3795	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'nk 9/11/2004 16:53'![39;49;00m$
  3796	[32mmethodInterfacesInPresentationOrderFrom:[39;49;00m [31minterfaceList[39;49;00m [32mforCategory:[39;49;00m [31maCategory[39;49;00m $
  3797		[37m"Answer the interface list sorted in desired presentation order, using a [39;49;00m$
  3798	[37m	static master-ordering list, q.v. The category parameter allows an [39;49;00m$
  3799	[37m	escape in case one wants to apply different order strategies in different [39;49;00m$
  3800	[37m	categories, but for now a single master-priority-ordering is used -- see [39;49;00m$
  3801	[37m	the comment in method EToyVocabulary.masterOrderingOfPhraseSymbols"[39;49;00m$
  3802	$
  3803		|[31m masterOrder ordered unordered index [39;49;00m|$
  3804		[31mmasterOrder[39;49;00m := [04m[32mVocabulary[39;49;00m [32meToyVocabulary[39;49;00m [32mmasterOrderingOfPhraseSymbols[39;49;00m.$
  3805		[31mordered[39;49;00m := [04m[32mSortedCollection[39;49;00m [32msortBlock:[39;49;00m [:[31ma[39;49;00m :[31mb[39;49;00m | [31ma[39;49;00m [32mkey[39;49;00m [32m<[39;49;00m [31mb[39;49;00m [32mkey[39;49;00m].$
  3806		[31munordered[39;49;00m := [04m[32mSortedCollection[39;49;00m [32msortBlock:[39;49;00m [:[31ma[39;49;00m :[31mb[39;49;00m | [31ma[39;49;00m [32mwording[39;49;00m [32m<[39;49;00m [31mb[39;49;00m [32mwording[39;49;00m].$
  3807	$
  3808		[31minterfaceList[39;49;00m [32mdo:[39;49;00m [:[31minterface[39;49;00m | $
  3809			[31mindex[39;49;00m := [31mmasterOrder[39;49;00m [32mindexOf:[39;49;00m [31minterface[39;49;00m [32melementSymbol[39;49;00m.$
  3810			[31mindex[39;49;00m [32misZero[39;49;00m$
  3811				[36mifTrue:[39;49;00m [[31munordered[39;49;00m [32madd:[39;49;00m [31minterface[39;49;00m]$
  3812				[36mifFalse:[39;49;00m [[31mordered[39;49;00m [32madd:[39;49;00m [31mindex[39;49;00m [32m->[39;49;00m [31minterface[39;49;00m]].$
  3813	$
  3814		^ [04m[32mArray[39;49;00m$
  3815			[32mstreamContents:[39;49;00m [:[31mstream[39;49;00m | $
  3816				[31mordered[39;49;00m [32mdo:[39;49;00m [:[31massoc[39;49;00m | [31mstream[39;49;00m [32mnextPut:[39;49;00m [31massoc[39;49;00m [32mvalue[39;49;00m].$
  3817				[31mstream[39;49;00m [32mnextPutAll:[39;49;00m [31munordered[39;49;00m][34m! ![39;49;00m$
  3818	$
  3819	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 10/24/2000 11:36'![39;49;00m$
  3820	[32mnewScriptorAround:[39;49;00m [31maPhraseTileMorph[39;49;00m$
  3821		[37m"Sprout a scriptor around aPhraseTileMorph, thus making a new script.  This is where generalized scriptors will be threaded in"[39;49;00m$
  3822	$
  3823		^ [36mnil[39;49;00m[34m! ![39;49;00m$
  3824	$
  3825	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 10/25/2000 17:42'![39;49;00m$
  3826	[32mofferViewerMenuForEvt:[39;49;00m [31manEvent[39;49;00m [32mmorph:[39;49;00m [31maMorph[39;49;00m$
  3827		[37m"Offer the viewer's primary menu to the user.  aMorph is some morph within the viewer itself, the one within which a mousedown triggered the need for this menu, and it is used only to retrieve the Viewer itself"[39;49;00m$
  3828	$
  3829		[36mself[39;49;00m [32mofferViewerMenuFor:[39;49;00m ([31maMorph[39;49;00m [32mownerThatIsA:[39;49;00m [04m[32mStandardViewer[39;49;00m) [32mevent:[39;49;00m [31manEvent[39;49;00m[34m! ![39;49;00m$
  3830	$
  3831	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/11/2002 02:03'![39;49;00m$
  3832	[32mofferViewerMenuFor:[39;49;00m [31maViewer[39;49;00m [32mevent:[39;49;00m [31mevt[39;49;00m$
  3833		[37m"Offer the primary Viewer menu to the user.  Copied up from Player code, but most of the functions suggested here don't work for non-Player objects, many aren't even defined, some relate to exploratory sw work not yet reflected in the current corpus.  We are early in the life cycle of this method..."[39;49;00m$
  3834	$
  3835		|[31m aMenu [39;49;00m|$
  3836		[31maMenu[39;49;00m _ [04m[32mMenuMorph[39;49;00m [36mnew[39;49;00m [32mdefaultTarget:[39;49;00m [36mself[39;49;00m.$
  3837		[31maMenu[39;49;00m [32maddStayUpItem[39;49;00m.$
  3838		[31maMenu[39;49;00m [32mtitle:[39;49;00m [33m'**CAUTION -- UNDER CONSTRUCTION!!**[39;49;00m$
  3839	[33mMany things may not work!![39;49;00m$
  3840	[33m'[39;49;00m[32m,[39;49;00m [36mself[39;49;00m [32mnameForViewer[39;49;00m.$
  3841		([31maViewer[39;49;00m [32maffordsUniclass[39;49;00m [32mand:[39;49;00m [[36mself[39;49;00m [32mbelongsToUniClass[39;49;00m [32mnot[39;49;00m]) [36mifTrue:[39;49;00m$
  3842			[[31maMenu[39;49;00m [32madd:[39;49;00m [33m'give me a Uniclass'[39;49;00m [32maction:[39;49;00m [33m#assureUniClass[39;49;00m.$
  3843			[31maMenu[39;49;00m [32maddLine[39;49;00m].$
  3844		[31maMenu[39;49;00m [32madd:[39;49;00m [33m'choose vocabulary...'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32maction:[39;49;00m [33m#chooseVocabulary[39;49;00m.$
  3845		[31maMenu[39;49;00m [32madd:[39;49;00m [33m'choose limit class...'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32maction:[39;49;00m [33m#chooseLimitClass[39;49;00m.$
  3846		[31maMenu[39;49;00m [32madd:[39;49;00m [33m'add search pane'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32maction:[39;49;00m [33m#addSearchPane[39;49;00m.$
  3847		[31maMenu[39;49;00m [32mballoonTextForLastItem:[39;49;00m [33m'Specify which class should be the most generic one to have its methods shown in this Viewer'[39;49;00m.$
  3848		[31maMenu[39;49;00m [32maddLine[39;49;00m.$
  3849	$
  3850		[36mself[39;49;00m [32mbelongsToUniClass[39;49;00m [36mifTrue:[39;49;00m$
  3851			[[31maMenu[39;49;00m [32madd:[39;49;00m [33m'add a new instance variable'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#addInstanceVariableIn:[39;49;00m [32margument:[39;49;00m [31maViewer[39;49;00m.$
  3852			[31maMenu[39;49;00m [32madd:[39;49;00m [33m'add a new script'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32mselector:[39;49;00m [33m#newPermanentScriptIn:[39;49;00m [32margument:[39;49;00m [31maViewer[39;49;00m.$
  3853			[31maMenu[39;49;00m [32maddLine[39;49;00m.$
  3854			[31maMenu[39;49;00m [32madd:[39;49;00m [33m'make my class be first-class'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#makeFirstClassClassIn:[39;49;00m [32margument:[39;49;00m [31maViewer[39;49;00m.$
  3855			[31maMenu[39;49;00m [32madd:[39;49;00m [33m'move my changes up to my superclass'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32maction:[39;49;00m [33m#promoteChangesToSuperclass[39;49;00m.$
  3856			[31maMenu[39;49;00m [32maddLine[39;49;00m].$
  3857	$
  3858		[31maMenu[39;49;00m [32madd:[39;49;00m [33m'tear off a tile'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#launchTileToRefer[39;49;00m.$
  3859		[31maMenu[39;49;00m [32maddLine[39;49;00m.$
  3860	$
  3861		[31maMenu[39;49;00m [32madd:[39;49;00m [33m'inspect me'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#inspect[39;49;00m.$
  3862		[31maMenu[39;49;00m [32madd:[39;49;00m [33m'inspect my class'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32maction:[39;49;00m [33m#inspect[39;49;00m.$
  3863		[31maMenu[39;49;00m [32maddLine[39;49;00m.$
  3864	$
  3865		[31maMenu[39;49;00m [32madd:[39;49;00m [33m'browse vocabulary'[39;49;00m [32maction:[39;49;00m [33m#haveFullProtocolBrowsed[39;49;00m.$
  3866		[31maMenu[39;49;00m [32madd:[39;49;00m [33m'inspect this Viewer'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32maction:[39;49;00m [33m#inspect[39;49;00m.$
  3867	$
  3868		[31maMenu[39;49;00m [32mpopUpEvent:[39;49;00m [31mevt[39;49;00m [32min:[39;49;00m [31maViewer[39;49;00m [32mcurrentWorld[39;49;00m$
  3869	$
  3870	[37m"[39;49;00m$
  3871	[37m	aMenu add: 'references to me' target: aViewer action: #browseReferencesToObject.[39;49;00m$
  3872	[37m	aMenu add: 'toggle scratch pane' target: aViewer selector: #toggleScratchPane.[39;49;00m$
  3873	[37m	aMenu add: 'make a nascent script for me' target: aViewer selector: #makeNascentScript.[39;49;00m$
  3874	[37m	aMenu add: 'rename me' target: aViewer selector: #chooseNewNameForReference.[39;49;00m$
  3875	[37m	aMenu add: 'browse full' action: #browseOwnClassFull.[39;49;00m$
  3876	[37m	aMenu add: 'browse hierarchy' action: #browseOwnClassHierarchy.[39;49;00m$
  3877	[37m	aMenu add: 'set user level...' target: aViewer action: #setUserLevel.[39;49;00m$
  3878	[37m	aMenu add: 'browse sub-protocol' action: #browseOwnClassSubProtocol.[39;49;00m$
  3879	[37m	aMenu addLine.[39;49;00m$
  3880	[37m[39;49;00m$
  3881	[37m"[39;49;00m[34m! ![39;49;00m$
  3882	$
  3883	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 1/22/2001 15:20'![39;49;00m$
  3884	[32mrenameScript:[39;49;00m [31moldSelector[39;49;00m$
  3885		[37m"prompt the user for a new selector and apply it.  Presently only works for players"[39;49;00m$
  3886	$
  3887		[36mself[39;49;00m [32mnotYetImplemented[39;49;00m[34m! ![39;49;00m$
  3888	$
  3889	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/10/2004 11:53'![39;49;00m$
  3890	[32mtilePhrasesForCategory:[39;49;00m [31maCategorySymbol[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m$
  3891		[37m"Return a collection of phrases for the category."[39;49;00m$
  3892	$
  3893		|[31m interfaces [39;49;00m|$
  3894		[31minterfaces[39;49;00m _ [36mself[39;49;00m [32mmethodInterfacesForCategory:[39;49;00m [31maCategorySymbol[39;49;00m [32minVocabulary:[39;49;00m [31maViewer[39;49;00m [32mcurrentVocabulary[39;49;00m [32mlimitClass:[39;49;00m [31maViewer[39;49;00m [32mlimitClass[39;49;00m.$
  3895		[31minterfaces[39;49;00m _ [36mself[39;49;00m [32mmethodInterfacesInPresentationOrderFrom:[39;49;00m [31minterfaces[39;49;00m [32mforCategory:[39;49;00m [31maCategorySymbol[39;49;00m.$
  3896		^ [36mself[39;49;00m [32mtilePhrasesForMethodInterfaces:[39;49;00m [31minterfaces[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m[34m! ![39;49;00m$
  3897	$
  3898	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/10/2004 11:53'![39;49;00m$
  3899	[32mtilePhrasesForMethodInterfaces:[39;49;00m [31mmethodInterfaceList[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m$
  3900		[37m"Return a collection of ViewerLine objects corresponding to the method-interface list provided.   The resulting list will be in the same order as the incoming list, but may be smaller if the viewer's vocbulary suppresses some of the methods, or if, in classic tiles mode, the selector requires more arguments than can be handled."[39;49;00m$
  3901	$
  3902		|[31m toSuppress interfaces resultType itsSelector [39;49;00m|$
  3903		[31mtoSuppress[39;49;00m _ [31maViewer[39;49;00m [32mcurrentVocabulary[39;49;00m [32mphraseSymbolsToSuppress[39;49;00m.$
  3904		[31minterfaces[39;49;00m _ [31mmethodInterfaceList[39;49;00m [32mreject:[39;49;00m [:[31mint[39;49;00m | [31mtoSuppress[39;49;00m [32mincludes:[39;49;00m [31mint[39;49;00m [32mselector[39;49;00m].$
  3905		[04m[32mPreferences[39;49;00m [32muniversalTiles[39;49;00m [36mifFalse:[39;49;00m  [37m"Classic tiles have their limitations..."[39;49;00m$
  3906			[[31minterfaces[39;49;00m _ [31minterfaces[39;49;00m [32mselect:[39;49;00m$
  3907				[:[31mint[39;49;00m |$
  3908					[31mitsSelector[39;49;00m _ [31mint[39;49;00m [32mselector[39;49;00m.$
  3909					[31mitsSelector[39;49;00m [32mnumArgs[39;49;00m [32m<[39;49;00m [34m2[39;49;00m [32mor:[39;49;00m$
  3910						[37m"The lone two-arg loophole in classic tiles"[39;49;00m$
  3911						[[33m#([39;49;00m[33mcolor:sees:[39;49;00m[33m)[39;49;00m [32mincludes:[39;49;00m [31mitsSelector[39;49;00m]]].$
  3912	$
  3913		^ [31minterfaces[39;49;00m [32mcollect:[39;49;00m$
  3914			[:[31maMethodInterface[39;49;00m |$
  3915				(([31mresultType[39;49;00m _ [31maMethodInterface[39;49;00m [32mresultType[39;49;00m) [32mnotNil[39;49;00m [32mand:[39;49;00m [[31mresultType[39;49;00m [32m~~[39;49;00m [33m#unknown[39;49;00m]) $
  3916					[36mifTrue:[39;49;00m$
  3917						[[31maViewer[39;49;00m [32mphraseForVariableFrom:[39;49;00m [31maMethodInterface[39;49;00m]$
  3918					[36mifFalse:[39;49;00m$
  3919						[[31maViewer[39;49;00m [32mphraseForCommandFrom:[39;49;00m [31maMethodInterface[39;49;00m]][34m! ![39;49;00m$
  3920	$
  3921	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/10/2004 12:23'![39;49;00m$
  3922	[32mtilePhrasesForSelectorList:[39;49;00m [31maList[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m$
  3923		[37m"Particular to the search facility in viewers.  Answer a list, in appropriate order, of ViewerLine objects to put into the viewer."[39;49;00m$
  3924	$
  3925		|[31m interfaces aVocab [39;49;00m|$
  3926		[31maVocab[39;49;00m _ [31maViewer[39;49;00m [32mcurrentVocabulary[39;49;00m.$
  3927		[31minterfaces[39;49;00m _ [36mself[39;49;00m$
  3928			[32mmethodInterfacesInPresentationOrderFrom:[39;49;00m$
  3929				([31maList[39;49;00m [32mcollect:[39;49;00m [:[31maSel[39;49;00m | [31maVocab[39;49;00m [32mmethodInterfaceForSelector:[39;49;00m [31maSel[39;49;00m [32mclass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m])$
  3930			[32mforCategory:[39;49;00m [33m#search[39;49;00m.$
  3931		^ [36mself[39;49;00m [32mtilePhrasesForMethodInterfaces:[39;49;00m [31minterfaces[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m[34m! ![39;49;00m$
  3932	$
  3933	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 5/4/2001 04:51'![39;49;00m$
  3934	[32mtileToRefer[39;49;00m$
  3935		[37m"Answer a reference tile that comprises an alias to me"[39;49;00m$
  3936	$
  3937		^ [04m[32mTileMorph[39;49;00m [36mnew[39;49;00m [32msetToReferTo:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  3938	$
  3939	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sd 3/30/2005 22:04'![39;49;00m$
  3940	[32muniqueInstanceVariableNameLike:[39;49;00m [31maString[39;49;00m [32mexcluding:[39;49;00m [31mtakenNames[39;49;00m$
  3941		[37m"Answer a nice instance-variable name to be added to the receiver which resembles aString, making sure it does not coincide with any element in takenNames"[39;49;00m$
  3942	$
  3943		|[31m okBase uniqueName usedNames [39;49;00m|$
  3944		[31musedNames[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNamesEverywhere[39;49;00m.$
  3945		[31musedNames[39;49;00m [32mremoveAllFoundIn:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstVarNames[39;49;00m.$
  3946		[31musedNames[39;49;00m [32maddAll:[39;49;00m [31mtakenNames[39;49;00m.$
  3947		[31mokBase[39;49;00m _ [04m[32mScanner[39;49;00m [32mwellFormedInstanceVariableNameFrom:[39;49;00m [31maString[39;49;00m.$
  3948	$
  3949		[31muniqueName[39;49;00m _ [04m[32mUtilities[39;49;00m [32mkeyLike:[39;49;00m [31mokBase[39;49;00m [32msatisfying:[39;49;00m $
  3950			[:[31maKey[39;49;00m | ([31musedNames[39;49;00m [32mincludes:[39;49;00m [31maKey[39;49;00m) [32mnot[39;49;00m].$
  3951	$
  3952		^ [31muniqueName[39;49;00m[34m! ![39;49;00m$
  3953	$
  3954	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 11/21/2001 15:16'![39;49;00m$
  3955	[32muniqueNameForReference[39;49;00m$
  3956		[37m"Answer a nice name by which the receiver can be referred to by other objects.  At present this uses a global References dictionary to hold the database of references, but in due course this will need to acquire some locality"[39;49;00m$
  3957	$
  3958		|[31m aName nameSym stem knownClassVars [39;49;00m|$
  3959		([31maName[39;49;00m _ [36mself[39;49;00m [32muniqueNameForReferenceOrNil[39;49;00m) [32mifNotNil:[39;49;00m [^ [31maName[39;49;00m].$
  3960		([31mstem[39;49;00m _ [36mself[39;49;00m [32mknownName[39;49;00m) [32mifNil:[39;49;00m$
  3961			[[31mstem[39;49;00m _ [36mself[39;49;00m [32mdefaultNameStemForInstances[39;49;00m [32masString[39;49;00m].$
  3962		[31mstem[39;49;00m _ [31mstem[39;49;00m [32mselect:[39;49;00m [:[31mch[39;49;00m | [31mch[39;49;00m [32misLetter[39;49;00m [32mor:[39;49;00m [[31mch[39;49;00m [32misDigit[39;49;00m]].$
  3963		[31mstem[39;49;00m [32msize[39;49;00m [32m==[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m [[31mstem[39;49;00m _ [33m'A'[39;49;00m].$
  3964		[31mstem[39;49;00m [32mfirst[39;49;00m [32misLetter[39;49;00m [36mifFalse:[39;49;00m$
  3965			[[31mstem[39;49;00m _ [33m'A'[39;49;00m[32m,[39;49;00m [31mstem[39;49;00m].$
  3966		[31mstem[39;49;00m _ [31mstem[39;49;00m [32mcapitalized[39;49;00m.$
  3967		[31mknownClassVars[39;49;00m _ [04m[32mScriptingSystem[39;49;00m [32mallKnownClassVariableNames[39;49;00m.$
  3968		[31maName[39;49;00m _ [04m[32mUtilities[39;49;00m [32mkeyLike:[39;49;00m  [31mstem[39;49;00m [32msatisfying:[39;49;00m$
  3969			[:[31mjinaLake[39;49;00m |$
  3970				[31mnameSym[39;49;00m _ [31mjinaLake[39;49;00m [32masSymbol[39;49;00m.$
  3971				 (([04m[32mReferences[39;49;00m [32mincludesKey:[39;49;00m  [31mnameSym[39;49;00m) [32mnot[39;49;00m [32mand:[39;49;00m$
  3972					[([04m[32mSmalltalk[39;49;00m [32mincludesKey:[39;49;00m [31mnameSym[39;49;00m) [32mnot[39;49;00m]) [32mand:[39;49;00m$
  3973							[([31mknownClassVars[39;49;00m [32mincludes:[39;49;00m [31mnameSym[39;49;00m) [32mnot[39;49;00m]].$
  3974	$
  3975		[04m[32mReferences[39;49;00m [32mat:[39;49;00m ([31maName[39;49;00m _ [31maName[39;49;00m [32masSymbol[39;49;00m) [32mput:[39;49;00m [36mself[39;49;00m.$
  3976		^ [31maName[39;49;00m[34m! ![39;49;00m$
  3977	$
  3978	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'md 1/17/2006 17:58'![39;49;00m$
  3979	[32muniqueNameForReferenceFrom:[39;49;00m [31mproposedName[39;49;00m$
  3980		[37m"Answer a satisfactory symbol, similar to the proposedName but obeying the rules, to represent the receiver"[39;49;00m$
  3981	$
  3982		|[31m aName nameSym stem okay [39;49;00m|$
  3983		[31mproposedName[39;49;00m [32m=[39;49;00m [36mself[39;49;00m [32muniqueNameForReferenceOrNil[39;49;00m $
  3984			[36mifTrue:[39;49;00m [^ [31mproposedName[39;49;00m].  [37m"No change"[39;49;00m$
  3985	$
  3986		[31mstem[39;49;00m _ [31mproposedName[39;49;00m [32mselect:[39;49;00m [:[31mch[39;49;00m | [31mch[39;49;00m [32misLetter[39;49;00m [32mor:[39;49;00m [[31mch[39;49;00m [32misDigit[39;49;00m]].$
  3987		[31mstem[39;49;00m [32msize[39;49;00m [32m==[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m [[31mstem[39;49;00m _ [33m'A'[39;49;00m].$
  3988		[31mstem[39;49;00m [32mfirst[39;49;00m [32misLetter[39;49;00m [36mifFalse:[39;49;00m$
  3989			[[31mstem[39;49;00m _ [33m'A'[39;49;00m[32m,[39;49;00m [31mstem[39;49;00m].$
  3990		[31mstem[39;49;00m _ [31mstem[39;49;00m [32mcapitalized[39;49;00m.$
  3991		[31maName[39;49;00m _ [04m[32mUtilities[39;49;00m [32mkeyLike:[39;49;00m [31mstem[39;49;00m [32msatisfying:[39;49;00m$
  3992			[:[31mjinaLake[39;49;00m |$
  3993				[31mnameSym[39;49;00m _ [31mjinaLake[39;49;00m [32masSymbol[39;49;00m.$
  3994				[31mokay[39;49;00m _ [36mtrue[39;49;00m.$
  3995				([36mself[39;49;00m [32mclass[39;49;00m [32mbindingOf:[39;49;00m [31mnameSym[39;49;00m) [32mifNotNil:[39;49;00m [[31mokay[39;49;00m _ [36mfalse[39;49;00m [37m"don't use it"[39;49;00m].$
  3996				[31mokay[39;49;00m].$
  3997		^ [31maName[39;49;00m [32masSymbol[39;49;00m[34m! ![39;49;00m$
  3998	$
  3999	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 3/15/2004 23:01'![39;49;00m$
  4000	[32muniqueNameForReferenceOrNil[39;49;00m$
  4001		[37m"If the receiver has a unique name for reference, return it here, else return nil"[39;49;00m$
  4002	$
  4003		^ [04m[32mReferences[39;49;00m [32mkeyAtValue:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m][34m! ![39;49;00m$
  4004	$
  4005	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'ar 5/16/2001 01:40'![39;49;00m$
  4006	[32mupdateThresholdForGraphicInViewerTab[39;49;00m$
  4007		[37m"When a Viewer is open on the receiver, its tab needs some graphic to show to the user. Computing this graphic can take quite some time so we want to make the update frequency depending on how long it takes to compute the thumbnail. The threshold returned by this method defines that the viewer will update at most every 'threshold * timeItTakesToDraw' milliseconds. Thus, if the time for computing the receiver's thumbnail is 200 msecs and the the threshold is 10, the viewer will update at most every two seconds."[39;49;00m$
  4008		^[34m20[39;49;00m [37m"seems to be a pretty good general choice"[39;49;00m[34m! ![39;49;00m$
  4009	$
  4010	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 3/9/2001 13:48'![39;49;00m$
  4011	[32musableMethodInterfacesIn:[39;49;00m [31maListOfMethodInterfaces[39;49;00m$
  4012		[37m"Filter aList, returning a subset list of apt phrases"[39;49;00m$
  4013	$
  4014		^ [31maListOfMethodInterfaces[39;49;00m$
  4015	[34m! ![39;49;00m$
  4016	$
  4017	$
  4018	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'world hacking'[39;49;00m[34m stamp: 'ar 3/17/2001 23:45'![39;49;00m$
  4019	[32mcouldOpenInMorphic[39;49;00m$
  4020	$
  4021	        [37m"is there an obvious morphic world in which to open a new morph?"[39;49;00m$
  4022	$
  4023	        ^[04m[32mWorld[39;49;00m [32mnotNil[39;49;00m [32mor:[39;49;00m [[04m[32mActiveWorld[39;49;00m [32mnotNil[39;49;00m][34m! ![39;49;00m$
  4024	$
  4025	$
  4026	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m![39;49;00m$
  4027	[32merrorImproperStore[39;49;00m$
  4028		[37m"Create an error notification that an improper store was attempted."[39;49;00m$
  4029	$
  4030		[36mself[39;49;00m [32merror:[39;49;00m [33m'Improper store into indexable object'[39;49;00m[34m! ![39;49;00m$
  4031	$
  4032	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m![39;49;00m$
  4033	[32merrorNonIntegerIndex[39;49;00m$
  4034		[37m"Create an error notification that an improper object was used as an index."[39;49;00m$
  4035	$
  4036		[36mself[39;49;00m [32merror:[39;49;00m [33m'only integers should be used as indices'[39;49;00m[34m! ![39;49;00m$
  4037	$
  4038	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m stamp: 'yo 6/29/2004 11:37'![39;49;00m$
  4039	[32merrorNotIndexable[39;49;00m$
  4040		[37m"Create an error notification that the receiver is not indexable."[39;49;00m$
  4041	$
  4042		[36mself[39;49;00m [32merror:[39;49;00m ([33m'Instances of {1} are not indexable'[39;49;00m [32mtranslated[39;49;00m [32mformat:[39;49;00m {[36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m})[34m! ![39;49;00m$
  4043	$
  4044	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m![39;49;00m$
  4045	[32merrorSubscriptBounds:[39;49;00m [31mindex[39;49;00m $
  4046		[37m"Create an error notification that an improper integer was used as an index."[39;49;00m$
  4047	$
  4048		[36mself[39;49;00m [32merror:[39;49;00m [33m'subscript is out of bounds: '[39;49;00m [32m,[39;49;00m [31mindex[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
  4049	$
  4050	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m stamp: 'ar 2/6/2004 14:47'![39;49;00m$
  4051	[32mprimitiveError:[39;49;00m [31maString[39;49;00m $
  4052		[37m"This method is called when the error handling results in a recursion in [39;49;00m$
  4053	[37m	calling on error: or halt or halt:."[39;49;00m$
  4054	$
  4055		|[31m context [39;49;00m|$
  4056		([04m[32mString[39;49;00m$
  4057			[32mstreamContents:[39;49;00m $
  4058				[:[31ms[39;49;00m |$
  4059				[31ms[39;49;00m [32mnextPutAll:[39;49;00m [33m'***System error handling failed***'[39;49;00m.$
  4060				[31ms[39;49;00m [32mcr[39;49;00m; [32mnextPutAll:[39;49;00m [31maString[39;49;00m.$
  4061				[31mcontext[39;49;00m _ [36mthisContext[39;49;00m [32msender[39;49;00m [32msender[39;49;00m.$
  4062				[34m20[39;49;00m [36mtimesRepeat:[39;49;00m [[31mcontext[39;49;00m [32m==[39;49;00m [36mnil[39;49;00m [36mifFalse:[39;49;00m [[31ms[39;49;00m [32mcr[39;49;00m; [32mprint:[39;49;00m ([31mcontext[39;49;00m _ [31mcontext[39;49;00m [32msender[39;49;00m)]].$
  4063				[31ms[39;49;00m [32mcr[39;49;00m; [32mnextPutAll:[39;49;00m [33m'-------------------------------'[39;49;00m.$
  4064				[31ms[39;49;00m [32mcr[39;49;00m; [32mnextPutAll:[39;49;00m [33m'Type CR to enter an emergency evaluator.'[39;49;00m.$
  4065				[31ms[39;49;00m [32mcr[39;49;00m; [32mnextPutAll:[39;49;00m [33m'Type any other character to restart.'[39;49;00m])$
  4066			[32mdisplayAt:[39;49;00m [34m0[39;49;00m [32m@[39;49;00m [34m0[39;49;00m.$
  4067		[[04m[32mSensor[39;49;00m [32mkeyboardPressed[39;49;00m] [32mwhileFalse[39;49;00m.$
  4068		[04m[32mSensor[39;49;00m [32mkeyboard[39;49;00m [32m=[39;49;00m [04m[32mCharacter[39;49;00m [32mcr[39;49;00m [36mifTrue:[39;49;00m [[04m[32mTranscripter[39;49;00m [32memergencyEvaluator[39;49;00m].$
  4069		[04m[32mSmalltalk[39;49;00m [32misMorphic[39;49;00m$
  4070			[36mifTrue:[39;49;00m [[04m[32mWorld[39;49;00m [32minstall[39;49;00m [37m"init hands and redisplay"[39;49;00m]$
  4071			[36mifFalse:[39;49;00m [[04m[32mScheduledControllers[39;49;00m [32msearchForActiveController[39;49;00m][34m! ![39;49;00m$
  4072	$
  4073	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m![39;49;00m$
  4074	[32mspecies[39;49;00m$
  4075		[37m"Answer the preferred class for reconstructing the receiver.  For example, [39;49;00m$
  4076	[37m	collections create new collections whenever enumeration messages such as [39;49;00m$
  4077	[37m	collect: or select: are invoked.  The new kind of collection is determined by [39;49;00m$
  4078	[37m	the species of the original collection.  Species and class are not always the [39;49;00m$
  4079	[37m	same.  For example, the species of Interval is Array."[39;49;00m$
  4080	$
  4081		^[36mself[39;49;00m [32mclass[39;49;00m[34m! ![39;49;00m$
  4082	$
  4083	[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m![39;49;00m$
  4084	[32mstoreAt:[39;49;00m [31moffset[39;49;00m [32minTempFrame:[39;49;00m [31maContext[39;49;00m$
  4085		[37m"This message had to get sent to an expression already on the stack[39;49;00m$
  4086	[37m	as a Block argument being accessed by the debugger.[39;49;00m$
  4087	[37m	Just re-route it to the temp frame."[39;49;00m$
  4088		^ [31maContext[39;49;00m [32mtempAt:[39;49;00m [31moffset[39;49;00m [32mput:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  4089	$
  4090	[34m"-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- "![39;49;00m$
  4091	$
  4092	[04m[32mObject class[39;49;00m[34m[39;49;00m$
  4093	[34m	instanceVariableNames: [39;49;00m[33m''[39;49;00m[34m![39;49;00m$
  4094	$
  4095	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-Widgets'[39;49;00m[34m stamp: 'gvc 4/17/2007 17:40'![39;49;00m$
  4096	[32mtaskbarIcon[39;49;00m$
  4097		[37m"Answer the icon for an instance of the receiver in a task bar[39;49;00m$
  4098	[37m	or nil for the default."[39;49;00m$
  4099	$
  4100		^[36mnil[39;49;00m[34m! ![39;49;00m$
  4101	$
  4102	$
  4103	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-accessing'[39;49;00m[34m stamp: 'lr 3/27/2006 15:47'![39;49;00m$
  4104	[32mdescription[39;49;00m$
  4105		^ [04m[32mMADescriptionBuilder[39;49;00m [32mfor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  4106	$
  4107	$
  4108	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'class initialization'[39;49;00m[34m stamp: 'ar 2/11/2001 02:00'![39;49;00m$
  4109	[32mflushDependents[39;49;00m$
  4110		[04m[32mDependentsFields[39;49;00m [32mkeysAndValuesDo:[39;49;00m[:[31mkey[39;49;00m :[31mdep[39;49;00m|$
  4111			[31mkey[39;49;00m [32mifNotNil:[39;49;00m[[31mkey[39;49;00m [32mremoveDependent:[39;49;00m [36mnil[39;49;00m].$
  4112		].$
  4113		[04m[32mDependentsFields[39;49;00m [32mfinalizeValues[39;49;00m.[34m! ![39;49;00m$
  4114	$
  4115	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'class initialization'[39;49;00m[34m stamp: 'rw 2/10/2002 13:09'![39;49;00m$
  4116	[32mflushEvents[39;49;00m$
  4117		[37m"Object flushEvents"[39;49;00m$
  4118	$
  4119		[04m[32mEventManager[39;49;00m [32mflushEvents[39;49;00m. [34m! ![39;49;00m$
  4120	$
  4121	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'class initialization'[39;49;00m[34m stamp: 'rww 10/2/2001 07:35'![39;49;00m$
  4122	[32minitialize[39;49;00m$
  4123		[37m"Object initialize"[39;49;00m$
  4124		[04m[32mDependentsFields[39;49;00m [32mifNil:[39;49;00m[[36mself[39;49;00m [32minitializeDependentsFields[39;49;00m].[34m! ![39;49;00m$
  4125	$
  4126	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'class initialization'[39;49;00m[34m stamp: 'ar 2/11/2001 01:41'![39;49;00m$
  4127	[32minitializeDependentsFields[39;49;00m$
  4128		[37m"Object initialize"[39;49;00m$
  4129		[04m[32mDependentsFields[39;49;00m _ [04m[32mWeakIdentityKeyDictionary[39;49;00m [36mnew[39;49;00m.$
  4130	[34m! ![39;49;00m$
  4131	$
  4132	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'class initialization'[39;49;00m[34m stamp: 'ar 2/11/2001 01:45'![39;49;00m$
  4133	[32mreInitializeDependentsFields[39;49;00m$
  4134		[37m"Object reInitializeDependentsFields"[39;49;00m$
  4135		|[31m oldFields [39;49;00m|$
  4136		[31moldFields[39;49;00m _ [04m[32mDependentsFields[39;49;00m.$
  4137		[04m[32mDependentsFields[39;49;00m _ [04m[32mWeakIdentityKeyDictionary[39;49;00m [36mnew[39;49;00m.$
  4138		[31moldFields[39;49;00m [32mkeysAndValuesDo:[39;49;00m[:[31mobj[39;49;00m :[31mdeps[39;49;00m|$
  4139			[31mdeps[39;49;00m [32mdo:[39;49;00m[:[31md[39;49;00m| [31mobj[39;49;00m [32maddDependent:[39;49;00m [31md[39;49;00m]].$
  4140	[34m! ![39;49;00m$
  4141	$
  4142	$
  4143	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'documentation'[39;49;00m[34m![39;49;00m$
  4144	[32mhowToModifyPrimitives[39;49;00m$
  4145		[37m"You are allowed to write methods which specify primitives, but please use [39;49;00m$
  4146	[37m	caution.  If you make a subclass of a class which contains a primitive method, [39;49;00m$
  4147	[37m	the subclass inherits the primitive.  The message which is implemented [39;49;00m$
  4148	[37m	primitively may be overridden in the subclass (E.g., see at:put: in String's [39;49;00m$
  4149	[37m	subclass Symbol).  The primitive behavior can be invoked using super (see [39;49;00m$
  4150	[37m	Symbol string:). [39;49;00m$
  4151	[37m	 [39;49;00m$
  4152	[37m	A class which attempts to mimic the behavior of another class without being [39;49;00m$
  4153	[37m	its subclass may or may not be able to use the primitives of the original class.  [39;49;00m$
  4154	[37m	In general, if the instance variables read or written by a primitive have the [39;49;00m$
  4155	[37m	same meanings and are in the same fields in both classes, the primitive will [39;49;00m$
  4156	[37m	work.  [39;49;00m$
  4157	[37m[39;49;00m$
  4158	[37m	For certain frequently used 'special selectors', the compiler emits a [39;49;00m$
  4159	[37m	send-special-selector bytecode instead of a send-message bytecode.  [39;49;00m$
  4160	[37m	Special selectors were created because they offer two advantages.  Code [39;49;00m$
  4161	[37m	which sends special selectors compiles into fewer bytes than normal.  For [39;49;00m$
  4162	[37m	some pairs of receiver classes and special selectors, the interpreter jumps [39;49;00m$
  4163	[37m	directly to a primitive routine without looking up the method in the class.  [39;49;00m$
  4164	[37m	This is much faster than a normal message lookup. [39;49;00m$
  4165	[37m	 [39;49;00m$
  4166	[37m	A selector which is a special selector solely in order to save space has a [39;49;00m$
  4167	[37m	normal behavior.  Methods whose selectors are special in order to [39;49;00m$
  4168	[37m	gain speed contain the comment, 'No Lookup'.  When the interpreter [39;49;00m$
  4169	[37m	encounters a send-special-selector bytecode, it checks the class of the [39;49;00m$
  4170	[37m	receiver and the selector.  If the class-selector pair is a no-lookup pair, [39;49;00m$
  4171	[37m	then the interpreter swiftly jumps to the routine which implements the [39;49;00m$
  4172	[37m	corresponding primitive.  (A special selector whose receiver is not of the [39;49;00m$
  4173	[37m	right class to make a no-lookup pair, is looked up normally).  The pairs are [39;49;00m$
  4174	[37m	listed below.  No-lookup methods contain a primitive number specification, [39;49;00m$
  4175	[37m	<primitive: xx>, which is redundant.  Since the method is not normally looked [39;49;00m$
  4176	[37m	up, deleting the primitive number specification cannot prevent this [39;49;00m$
  4177	[37m	primitive from running.  If a no-lookup primitive fails, the method is looked [39;49;00m$
  4178	[37m	up normally, and the expressions in it are executed. [39;49;00m$
  4179	[37m	 [39;49;00m$
  4180	[37m	No Lookup pairs of (class, selector) [39;49;00m$
  4181	[37m	 [39;49;00m$
  4182	[37m	SmallInteger with any of		+ - * /  \\  bitOr: bitShift: bitAnd:  // [39;49;00m$
  4183	[37m	SmallInteger with any of		=  ~=  >  <  >=  <= [39;49;00m$
  4184	[37m	Any class with					== [39;49;00m$
  4185	[37m	Any class with 					@ [39;49;00m$
  4186	[37m	Point with either of				x y [39;49;00m$
  4187	[37m	ContextPart with					blockCopy: [39;49;00m$
  4188	[37m	BlockContext with either of 		value value:[39;49;00m$
  4189	[37m	"[39;49;00m$
  4190	$
  4191		[36mself[39;49;00m [32merror:[39;49;00m [33m'comment only'[39;49;00m[34m! ![39;49;00m$
  4192	$
  4193	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'documentation'[39;49;00m[34m![39;49;00m$
  4194	[32mwhatIsAPrimitive[39;49;00m$
  4195		[37m"Some messages in the system are responded to primitively. A primitive   [39;49;00m$
  4196	[37m	response is performed directly by the interpreter rather than by evaluating   [39;49;00m$
  4197	[37m	expressions in a method. The methods for these messages indicate the   [39;49;00m$
  4198	[37m	presence of a primitive response by including <primitive: xx> before the   [39;49;00m$
  4199	[37m	first expression in the method.   [39;49;00m$
  4200	[37m	  [39;49;00m$
  4201	[37m	Primitives exist for several reasons. Certain basic or 'primitive' [39;49;00m$
  4202	[37m	operations cannot be performed in any other way. Smalltalk without [39;49;00m$
  4203	[37m	primitives can move values from one variable to another, but cannot add two [39;49;00m$
  4204	[37m	SmallIntegers together. Many methods for arithmetic and comparison [39;49;00m$
  4205	[37m	between numbers are primitives. Some primitives allow Smalltalk to [39;49;00m$
  4206	[37m	communicate with I/O devices such as the disk, the display, and the keyboard. [39;49;00m$
  4207	[37m	Some primitives exist only to make the system run faster; each does the same [39;49;00m$
  4208	[37m	thing as a certain Smalltalk method, and its implementation as a primitive is [39;49;00m$
  4209	[37m	optional.  [39;49;00m$
  4210	[37m	  [39;49;00m$
  4211	[37m	When the Smalltalk interpreter begins to execute a method which specifies a [39;49;00m$
  4212	[37m	primitive response, it tries to perform the primitive action and to return a [39;49;00m$
  4213	[37m	result. If the routine in the interpreter for this primitive is successful, [39;49;00m$
  4214	[37m	it will return a value and the expressions in the method will not be evaluated. [39;49;00m$
  4215	[37m	If the primitive routine is not successful, the primitive 'fails', and the [39;49;00m$
  4216	[37m	Smalltalk expressions in the method are executed instead. These [39;49;00m$
  4217	[37m	expressions are evaluated as though the primitive routine had not been [39;49;00m$
  4218	[37m	called.  [39;49;00m$
  4219	[37m	  [39;49;00m$
  4220	[37m	The Smalltalk code that is evaluated when a primitive fails usually [39;49;00m$
  4221	[37m	anticipates why that primitive might fail. If the primitive is optional, the [39;49;00m$
  4222	[37m	expressions in the method do exactly what the primitive would have done (See [39;49;00m$
  4223	[37m	Number @). If the primitive only works on certain classes of arguments, the [39;49;00m$
  4224	[37m	Smalltalk code tries to coerce the argument or appeals to a superclass to find [39;49;00m$
  4225	[37m	a more general way of doing the operation (see SmallInteger +). If the [39;49;00m$
  4226	[37m	primitive is never supposed to fail, the expressions signal an error (see [39;49;00m$
  4227	[37m	SmallInteger asFloat).  [39;49;00m$
  4228	[37m	  [39;49;00m$
  4229	[37m	Each method that specifies a primitive has a comment in it. If the primitive is [39;49;00m$
  4230	[37m	optional, the comment will say 'Optional'. An optional primitive that is not [39;49;00m$
  4231	[37m	implemented always fails, and the Smalltalk expressions do the work [39;49;00m$
  4232	[37m	instead.  [39;49;00m$
  4233	[37m	 [39;49;00m$
  4234	[37m	If a primitive is not optional, the comment will say, 'Essential'. Some [39;49;00m$
  4235	[37m	methods will have the comment, 'No Lookup'. See Object [39;49;00m$
  4236	[37m	howToModifyPrimitives for an explanation of special selectors which are [39;49;00m$
  4237	[37m	not looked up.  [39;49;00m$
  4238	[37m	  [39;49;00m$
  4239	[37m	For the primitives for +, -, *, and bitShift: in SmallInteger, and truncated [39;49;00m$
  4240	[37m	in Float, the primitive constructs and returns a 16-bit [39;49;00m$
  4241	[37m	LargePositiveInteger when the result warrants it. Returning 16-bit [39;49;00m$
  4242	[37m	LargePositiveIntegers from these primitives instead of failing is [39;49;00m$
  4243	[37m	optional in the same sense that the LargePositiveInteger arithmetic [39;49;00m$
  4244	[37m	primitives are optional. The comments in the SmallInteger primitives say, [39;49;00m$
  4245	[37m	'Fails if result is not a SmallInteger', even though the implementor has the [39;49;00m$
  4246	[37m	option to construct a LargePositiveInteger. For further information on [39;49;00m$
  4247	[37m	primitives, see the 'Primitive Methods' part of the chapter on the formal [39;49;00m$
  4248	[37m	specification of the interpreter in the Smalltalk book."[39;49;00m$
  4249	$
  4250		[36mself[39;49;00m [32merror:[39;49;00m [33m'comment only'[39;49;00m[34m! ![39;49;00m$
  4251	$
  4252	$
  4253	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'file list services'[39;49;00m[34m stamp: 'nk 6/12/2004 11:41'![39;49;00m$
  4254	[32mfileReaderServicesForDirectory:[39;49;00m [31maFileDirectory[39;49;00m$
  4255		[37m"Backstop"[39;49;00m$
  4256		^[33m#([39;49;00m[33m)[39;49;00m[34m! ![39;49;00m$
  4257	$
  4258	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'file list services'[39;49;00m[34m stamp: 'nk 6/12/2004 11:30'![39;49;00m$
  4259	[32mfileReaderServicesForFile:[39;49;00m [31mfullName[39;49;00m [32msuffix:[39;49;00m [31msuffix[39;49;00m$
  4260		[37m"Backstop"[39;49;00m$
  4261		^[33m#([39;49;00m[33m)[39;49;00m[34m! ![39;49;00m$
  4262	$
  4263	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'file list services'[39;49;00m[34m stamp: 'md 2/15/2006 17:20'![39;49;00m$
  4264	[32mservices[39;49;00m$
  4265		[37m"Backstop"[39;49;00m$
  4266		^[33m#([39;49;00m[33m)[39;49;00m[34m! ![39;49;00m$
  4267	$
  4268	$
  4269	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 1/23/2003 09:45'![39;49;00m$
  4270	[32mcategoryForUniclasses[39;49;00m$
  4271		[37m"Answer the default system category into which to place unique-class instances"[39;49;00m$
  4272	$
  4273		^ [33m'UserObjects'[39;49;00m[34m! ![39;49;00m$
  4274	$
  4275	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 7/28/97 15:56'![39;49;00m$
  4276	[32mchooseUniqueClassName[39;49;00m$
  4277		|[31m i className [39;49;00m|$
  4278		[31mi[39;49;00m _ [34m1[39;49;00m.$
  4279		[[31mclassName[39;49;00m _ ([36mself[39;49;00m [32mname[39;49;00m [32m,[39;49;00m [31mi[39;49;00m [32mprintString[39;49;00m) [32masSymbol[39;49;00m.$
  4280		 [04m[32mSmalltalk[39;49;00m [32mincludesKey:[39;49;00m [31mclassName[39;49;00m]$
  4281			[36mwhileTrue:[39;49;00m [[31mi[39;49;00m _ [31mi[39;49;00m [32m+[39;49;00m [34m1[39;49;00m].$
  4282		^ [31mclassName[39;49;00m[34m! ![39;49;00m$
  4283	$
  4284	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'tk 8/22/1998 08:22'![39;49;00m$
  4285	[32minitialInstance[39;49;00m$
  4286		[37m"Answer the first instance of the receiver, generate an error if there is one already"[39;49;00m$
  4287		[37m"self instanceCount > 0 ifTrue: [self error: 'instance(s) already exist.']."[39;49;00m$
  4288			[37m"Debugging test that is very slow"[39;49;00m$
  4289		^ [36mself[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
  4290	$
  4291	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 5/5/2000 09:30'![39;49;00m$
  4292	[32minitializedInstance[39;49;00m$
  4293		^ [36mself[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
  4294	$
  4295	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 10/16/2000 10:58'![39;49;00m$
  4296	[32minstanceOfUniqueClass[39;49;00m$
  4297		[37m"Answer an instance of a unique subclass of the receiver"[39;49;00m$
  4298	$
  4299		^ [36mself[39;49;00m [32minstanceOfUniqueClassWithInstVarString:[39;49;00m [33m''[39;49;00m [32mandClassInstVarString:[39;49;00m [33m''[39;49;00m[34m! ![39;49;00m$
  4300	$
  4301	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'tk 8/22/1998 08:27'![39;49;00m$
  4302	[32minstanceOfUniqueClassWithInstVarString:[39;49;00m [31minstVarString[39;49;00m [32mandClassInstVarString:[39;49;00m [31mclassInstVarString[39;49;00m$
  4303		[37m"Create a unique class for the receiver, and answer an instance of it"[39;49;00m$
  4304	$
  4305		^ ([36mself[39;49;00m [32mnewUniqueClassInstVars:[39;49;00m [31minstVarString[39;49;00m $
  4306			[32mclassInstVars:[39;49;00m [31mclassInstVarString[39;49;00m) [32minitialInstance[39;49;00m[34m! ![39;49;00m$
  4307	$
  4308	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 10/23/1999 22:51'![39;49;00m$
  4309	[32misUniClass[39;49;00m$
  4310		^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  4311	$
  4312	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'ajh 5/23/2002 00:35'![39;49;00m$
  4313	[32mnewFrom:[39;49;00m [31maSimilarObject[39;49;00m$
  4314		[37m"Create an object that has similar contents to aSimilarObject.[39;49;00m$
  4315	[37m	If the classes have any instance varaibles with the same names, copy them across.[39;49;00m$
  4316	[37m	If this is bad for a class, override this method."[39;49;00m$
  4317	$
  4318		^ ([36mself[39;49;00m [32misVariable[39;49;00m$
  4319			[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mbasicNew:[39;49;00m [31maSimilarObject[39;49;00m [32mbasicSize[39;49;00m]$
  4320			[36mifFalse:[39;49;00m [[36mself[39;49;00m [32mbasicNew[39;49;00m]$
  4321		  ) [32mcopySameFrom:[39;49;00m [31maSimilarObject[39;49;00m[34m! ![39;49;00m$
  4322	$
  4323	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'tk 6/29/1998 12:11'![39;49;00m$
  4324	[32mnewUniqueClassInstVars:[39;49;00m [31minstVarString[39;49;00m [32mclassInstVars:[39;49;00m [31mclassInstVarString[39;49;00m$
  4325		[37m"Create a unique class for the receiver"[39;49;00m$
  4326	$
  4327		|[31m aName aClass [39;49;00m|$
  4328		[36mself[39;49;00m [32misSystemDefined[39;49;00m [36mifFalse:[39;49;00m$
  4329			[^ [31msuperclass[39;49;00m [32mnewUniqueClassInstVars:[39;49;00m [31minstVarString[39;49;00m [32mclassInstVars:[39;49;00m [31mclassInstVarString[39;49;00m].$
  4330		[31maName[39;49;00m _ [36mself[39;49;00m [32mchooseUniqueClassName[39;49;00m.$
  4331		[31maClass[39;49;00m _ [36mself[39;49;00m [32msubclass:[39;49;00m [31maName[39;49;00m [32minstanceVariableNames:[39;49;00m [31minstVarString[39;49;00m $
  4332			[32mclassVariableNames:[39;49;00m [33m''[39;49;00m [32mpoolDictionaries:[39;49;00m [33m''[39;49;00m [32mcategory:[39;49;00m [36mself[39;49;00m [32mcategoryForUniclasses[39;49;00m.$
  4333		[31mclassInstVarString[39;49;00m [32msize[39;49;00m [32m>[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m$
  4334			[[31maClass[39;49;00m [32mclass[39;49;00m [32minstanceVariableNames:[39;49;00m [31mclassInstVarString[39;49;00m].$
  4335		^ [31maClass[39;49;00m[34m! ![39;49;00m$
  4336	$
  4337	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 7/28/97 15:56'![39;49;00m$
  4338	[32mnewUserInstance[39;49;00m$
  4339		[37m"Answer an instance of an appropriate class to serve as a user object in the containment hierarchy"[39;49;00m$
  4340	$
  4341		^ [36mself[39;49;00m [32minstanceOfUniqueClass[39;49;00m[34m! ![39;49;00m$
  4342	$
  4343	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'nk 8/30/2004 07:57'![39;49;00m$
  4344	[32mreadCarefullyFrom:[39;49;00m [31mtextStringOrStream[39;49;00m$
  4345		[37m"Create an object based on the contents of textStringOrStream.  Return an error instead of putting up a SyntaxError window."[39;49;00m$
  4346	$
  4347		|[31m object [39;49;00m|$
  4348		([04m[32mCompiler[39;49;00m [32mcouldEvaluate:[39;49;00m [31mtextStringOrStream[39;49;00m)$
  4349			[36mifFalse:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'expected String, Stream, or Text'[39;49;00m].$
  4350		[31mobject[39;49;00m _ [04m[32mCompiler[39;49;00m [32mevaluate:[39;49;00m [31mtextStringOrStream[39;49;00m [32mfor:[39;49;00m [36mnil[39;49;00m $
  4351					[32mnotifying:[39;49;00m [33m#error:[39;49;00m [37m"signal we want errors"[39;49;00m [32mlogged:[39;49;00m [36mfalse[39;49;00m.$
  4352		([31mobject[39;49;00m [32misKindOf:[39;49;00m [36mself[39;49;00m) [36mifFalse:[39;49;00m [[36mself[39;49;00m [32merror:[39;49;00m [36mself[39;49;00m [32mname[39;49;00m[32m,[39;49;00m [33m' expected'[39;49;00m].$
  4353		^[31mobject[39;49;00m[34m! ![39;49;00m$
  4354	$
  4355	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'nk 8/30/2004 07:57'![39;49;00m$
  4356	[32mreadFrom:[39;49;00m [31mtextStringOrStream[39;49;00m$
  4357		[37m"Create an object based on the contents of textStringOrStream."[39;49;00m$
  4358	$
  4359		|[31m object [39;49;00m|$
  4360		([04m[32mCompiler[39;49;00m [32mcouldEvaluate:[39;49;00m [31mtextStringOrStream[39;49;00m)$
  4361			[36mifFalse:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'expected String, Stream, or Text'[39;49;00m].$
  4362		[31mobject[39;49;00m _ [04m[32mCompiler[39;49;00m [32mevaluate:[39;49;00m [31mtextStringOrStream[39;49;00m.$
  4363		([31mobject[39;49;00m [32misKindOf:[39;49;00m [36mself[39;49;00m) [36mifFalse:[39;49;00m [[36mself[39;49;00m [32merror:[39;49;00m [36mself[39;49;00m [32mname[39;49;00m[32m,[39;49;00m [33m' expected'[39;49;00m].$
  4364		^[31mobject[39;49;00m[34m! ![39;49;00m$
  4365	$
  4366	$
  4367	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 1/8/97'![39;49;00m$
  4368	[32mcreateFrom:[39;49;00m [31maSmartRefStream[39;49;00m [32msize:[39;49;00m [31mvarsOnDisk[39;49;00m [32mversion:[39;49;00m [31minstVarList[39;49;00m$
  4369		[37m"Create an instance of me so objects on the disk can be read in.  Tricky part is computing the size if variable.  Inst vars will be filled in later.  "[39;49;00m$
  4370	$
  4371		^ [36mself[39;49;00m [32misVariable[39;49;00m$
  4372			[36mifFalse:[39;49;00m [[36mself[39;49;00m [32mbasicNew[39;49;00m]$
  4373			[36mifTrue:[39;49;00m [[37m"instVarList is names of old class's inst vars plus a version number"[39;49;00m $
  4374					[36mself[39;49;00m [32mbasicNew:[39;49;00m ([31mvarsOnDisk[39;49;00m [32m-[39;49;00m ([31minstVarList[39;49;00m [32msize[39;49;00m [32m-[39;49;00m [34m1[39;49;00m))]$
  4375	[34m! ![39;49;00m$
  4376	$
  4377	$
  4378	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'window color'[39;49;00m[34m stamp: 'nk 6/10/2004 08:10'![39;49;00m$
  4379	[32mwindowColorSpecification[39;49;00m$
  4380		[37m"Answer a WindowColorSpec object that declares my preference.[39;49;00m$
  4381	[37m	This is a backstop for classes that don't otherwise define a preference."[39;49;00m$
  4382	$
  4383		^ [04m[32mWindowColorSpec[39;49;00m [32mclassSymbol:[39;49;00m [36mself[39;49;00m [32mname[39;49;00m$
  4384			[32mwording:[39;49;00m [33m'Default'[39;49;00m [32mbrightColor:[39;49;00m [33m#white[39;49;00m$
  4385			[32mpastelColor:[39;49;00m [33m#white[39;49;00m$
  4386			[32mhelpMessage:[39;49;00m [33m'Other windows without color preferences.'[39;49;00m[34m! ![39;49;00m$
  4387	$
  4388	$
  4389	[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m stamp: 'mir 8/22/2001 15:20'![39;49;00m$
  4390	[32mreleaseExternalSettings[39;49;00m$
  4391		[37m"Do nothing as a default"[39;49;00m[34m! ![39;49;00m$
  4392	$
  4393	$
  4394	[04m[32mObject[39;49;00m [32minitialize[39;49;00m[32m![39;49;00m$
