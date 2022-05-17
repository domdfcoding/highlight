     1^I![04m[32mProtoObject[39;49;00m [32msubclass:[39;49;00m [33m#Object[39;49;00m$
     2^I^I[32minstanceVariableNames:[39;49;00m [33m''[39;49;00m$
     3^I^I[32mclassVariableNames:[39;49;00m [33m'DependentsFields'[39;49;00m$
     4^I^I[32mpoolDictionaries:[39;49;00m [33m''[39;49;00m$
     5^I^I[32mcategory:[39;49;00m [33m'Kernel-Objects'[39;49;00m[32m![39;49;00m$
     6^I$
     7^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'gk 2/24/2004 08:49'![39;49;00m$
     8^I[32mbeep[39;49;00m$
     9^I^I[37m"Deprecated."[39;49;00m$
    10^I^I$
    11^I^I[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use Beeper class>>beep instead.'[39;49;00m.$
    12^I^I[04m[32mBeeper[39;49;00m [32mbeep[39;49;00m[34m! ![39;49;00m$
    13^I$
    14^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'gk 2/24/2004 08:50'![39;49;00m$
    15^I[32mbeepPrimitive[39;49;00m$
    16^I^I[37m"Deprecated. Beep in the absence of sound support."[39;49;00m$
    17^I^I$
    18^I^I[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use Beeper class>>beep or Beeper class>>beepPrimitive instead.'[39;49;00m.$
    19^I^I[04m[32mBeeper[39;49;00m [32mbeepPrimitive[39;49;00m[34m! ![39;49;00m$
    20^I$
    21^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'md 12/12/2003 17:02'![39;49;00m$
    22^I[32mbeep:[39;49;00m [31msoundName[39;49;00m$
    23^I^I[37m"Make the given sound, unless the making of sound is disabled in Preferences."[39;49;00m$
    24^I$
    25^I^I[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use SampledSound>>playSoundNamed: instead.'[39;49;00m.$
    26^I^I[04m[32mPreferences[39;49;00m [32msoundsEnabled[39;49;00m$
    27^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mplaySoundNamed:[39;49;00m [31msoundName[39;49;00m]$
    28^I[34m! ![39;49;00m$
    29^I$
    30^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'sd 11/19/2004 16:57'![39;49;00m$
    31^I[32mcontentsGetz:[39;49;00m [31mx[39;49;00m$
    32^I^I[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'there is no method named contents in object and in addition only one sender in a method not called'[39;49;00m. $
    33^I^I[36mself[39;49;00m [32mcontents:[39;49;00m [31mx[39;49;00m[34m! ![39;49;00m$
    34^I$
    35^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'sd 11/13/2003 21:10'![39;49;00m$
    36^I[32mdeprecatedExplanation:[39;49;00m [31maString[39;49;00m$
    37^I     [37m"This method is OBSOLETE.  Use #deprecated: instead."[39;49;00m$
    38^I^I[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use Object>>deprecated: instead of deprecatedExplanation:.'[39;49;00m.$
    39^I$
    40^I^I[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
    41^I^I^I[[04m[32mDeprecation[39;49;00m [32msignal:[39;49;00m ([33m'{1} has been deprecated. {2}'[39;49;00m [32mtranslated[39;49;00m [32mformat:[39;49;00m {[36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m. [31maString[39;49;00m})][34m! ![39;49;00m$
    42^I$
    43^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'sd 11/13/2003 21:11'![39;49;00m$
    44^I[32mdeprecated:[39;49;00m [31maBlock[39;49;00m [32mexplanation:[39;49;00m [31maString[39;49;00m $
    45^I^I [37m"This method is OBSOLETE.  Use #deprecated:block: instead."[39;49;00m$
    46^I^I[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use Object>>deprecated:block: instead of deprecated:explanation:.'[39;49;00m.$
    47^I$
    48^I^I[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
    49^I^I^I[[04m[32mDeprecation[39;49;00m$
    50^I^I^I^I[32msignal:[39;49;00m ([33m'{1} has been deprecated. {2}'[39;49;00m [32mtranslated[39;49;00m [32mformat:[39;49;00m {[36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m. [31maString[39;49;00m})].$
    51^I^I^ [31maBlock[39;49;00m [32mvalue[39;49;00m.$
    52^I[34m! ![39;49;00m$
    53^I$
    54^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'md 12/12/2003 16:25'![39;49;00m$
    55^I[32mdoIfNotNil:[39;49;00m [31maBlock[39;49;00m$
    56^I^I[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'use ifNotNilDo:'[39;49;00m.$
    57^I^I^ [36mself[39;49;00m [32mifNotNilDo:[39;49;00m [31maBlock[39;49;00m$
    58^I[34m! ![39;49;00m$
    59^I$
    60^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'md 11/27/2004 12:20'![39;49;00m$
    61^I[32mifKindOf:[39;49;00m [31maClass[39;49;00m [32mthenDo:[39;49;00m [31maBlock[39;49;00m$
    62^I^I[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Deprecated. Just use #isKindOf:'[39;49;00m.$
    63^I^I^ ([36mself[39;49;00m [32misKindOf:[39;49;00m [31maClass[39;49;00m) [36mifTrue:[39;49;00m [[31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m][34m! ![39;49;00m$
    64^I$
    65^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'gk 2/23/2004 20:51'![39;49;00m$
    66^I[32mplaySoundNamed:[39;49;00m [31msoundName[39;49;00m$
    67^I^I[37m"Deprecated.[39;49;00m$
    68^I[37m^IPlay the sound with the given name."[39;49;00m$
    69^I$
    70^I^I[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use "SoundService default playSoundNamed: aName" instead.'[39;49;00m.$
    71^I^I[04m[32mSoundService[39;49;00m [32mdefault[39;49;00m [32mplaySoundNamed:[39;49;00m [31msoundName[39;49;00m[34m! ![39;49;00m$
    72^I$
    73^I$
    74^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:23'![39;49;00m$
    75^I[32maidaCanBeLocked[39;49;00m$
    76^I^I[37m"can we get an exclusive lock on that object (not already locked)?"[39;49;00m$
    77^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
    78^I$
    79^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:23'![39;49;00m$
    80^I[32maidaDontCache[39;49;00m$
    81^I^I[37m"don't cache web content in a browser. Appropriate header is added to http response"[39;49;00m$
    82^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
    83^I$
    84^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:24'![39;49;00m$
    85^I[32maidaIsLocked[39;49;00m$
    86^I^I[37m"is object locked exclusively?"[39;49;00m$
    87^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
    88^I$
    89^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:24'![39;49;00m$
    90^I[32maidaLock[39;49;00m$
    91^I^I[37m"get an exclusive lock on that object. Until unlocked, noon else can get that lock. Return false if already locked, true if successfull"[39;49;00m$
    92^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
    93^I$
    94^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:24'![39;49;00m$
    95^I[32maidaUnlock[39;49;00m$
    96^I^I[37m"release an exclusive lock if any"[39;49;00m$
    97^I^I^[36mtrue[39;49;00m[34m! ![39;49;00m$
    98^I$
    99^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:24'![39;49;00m$
   100^I[32mapp[39;49;00m$
   101^I^I[37m"fastest and most convinient way to find a web app for that object"[39;49;00m$
   102^I^I^[36mself[39;49;00m [32mwebAppFor:[39;49;00m [36mself[39;49;00m [32mfirstSessionFromStack[39;49;00m[34m! ![39;49;00m$
   103^I$
   104^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:25'![39;49;00m$
   105^I[32mcontentType[39;49;00m$
   106^I$
   107^I^I[37m"Janko Mivsek, apr98"[39;49;00m$
   108^I^I[37m"return 'text/html' as content type for web pages"[39;49;00m$
   109^I$
   110^I^I^[33m'text/html'[39;49;00m[34m! ![39;49;00m$
   111^I$
   112^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:25'![39;49;00m$
   113^I[32mdeepSearchOfClass:[39;49;00m [31maClassName[39;49;00m$
   114^I^I[37m"finf all objects of that class down in object hierarchy"[39;49;00m$
   115^I^I|[31m objectDictionary class [39;49;00m|$
   116^I^I[31mobjectDictionary[39;49;00m := [04m[32mIdentityDictionary[39;49;00m [36mnew[39;49;00m.$
   117^I^I[36mself[39;49;00m [32mdeepCopyNotIn:[39;49;00m [31mobjectDictionary[39;49;00m.$
   118^I^I[31mclass[39;49;00m := [31maClassName[39;49;00m [32masSymbol[39;49;00m.$
   119^I^I^[31mobjectDictionary[39;49;00m [32mkeys[39;49;00m [32mselect:[39;49;00m [:[31meach[39;49;00m | [31meach[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32m=[39;49;00m [31mclass[39;49;00m].[34m! ![39;49;00m$
   120^I$
   121^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:26'![39;49;00m$
   122^I[32mdeepSearchOfObsoleteClasses[39;49;00m$
   123^I^I[37m"find all objects of obsolete classes down in object hierarchy"[39;49;00m$
   124^I^I|[31m objectDictionary [39;49;00m|$
   125^I^I[31mobjectDictionary[39;49;00m := [04m[32mIdentityDictionary[39;49;00m [36mnew[39;49;00m.$
   126^I^I[36mself[39;49;00m [32mdeepCopyNotIn:[39;49;00m [31mobjectDictionary[39;49;00m.$
   127^I^I^[31mobjectDictionary[39;49;00m [32mkeys[39;49;00m [32mselect:[39;49;00m [:[31meach[39;49;00m | [31meach[39;49;00m [32mclass[39;49;00m [32misObsolete[39;49;00m].[34m! ![39;49;00m$
   128^I$
   129^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:26'![39;49;00m$
   130^I[32mexpiresTimestamp[39;49;00m$
   131^I^I[37m"until when content of this object wont be changed"[39;49;00m$
   132^I^I[37m"used in http response, override if you like to be included"[39;49;00m$
   133^I^I^[36mself[39;49;00m [32mmodifiedTimestamp[39;49;00m  [37m"to reload pages immediately"[39;49;00m[34m! ![39;49;00m$
   134^I$
   135^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:26'![39;49;00m$
   136^I[32mfirstAppFromStack[39;49;00m$
   137^I^I[37m"try to find a first sender up in calling stack, who is  WebApplication"[39;49;00m$
   138^I^I|[31m context [39;49;00m|$
   139^I^I[31mcontext[39;49;00m := [36mthisContext[39;49;00m.$
   140^I^I[[31mcontext[39;49;00m [32mnotNil[39;49;00m] [36mwhileTrue:[39;49;00m [$
   141^I^I^I([31mcontext[39;49;00m [32mreceiver[39;49;00m [32misKindOf:[39;49;00m [04m[32mWebApplication[39;49;00m) [36mifTrue:[39;49;00m [^[31mcontext[39;49;00m [32mreceiver[39;49;00m].$
   142^I^I^I[31mcontext[39;49;00m := [31mcontext[39;49;00m [32msender[39;49;00m].$
   143^I^I^[36mself[39;49;00m [32mfirstSessionFromStack[39;49;00m [32mlastApp[39;49;00m[34m! ![39;49;00m$
   144^I$
   145^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/25/2007 21:34'![39;49;00m$
   146^I[32mfirstSessionFromStack[39;49;00m$
   147^I^I[37m"try to find a first sender up in calling stack, who is  AIDASite and get session if that call"[39;49;00m$
   148^I^I|[31m context [39;49;00m|$
   149^I^I[31mcontext[39;49;00m := [36mthisContext[39;49;00m.$
   150^I^I[[31mcontext[39;49;00m [32mnotNil[39;49;00m] [36mwhileTrue:[39;49;00m [$
   151^I^I^I([31mcontext[39;49;00m [32mreceiver[39;49;00m [32misKindOf:[39;49;00m [04m[32mAIDASite[39;49;00m) [36mifTrue:[39;49;00m ^I[^([31mcontext[39;49;00m [32mat:[39;49;00m [34m3[39;49;00m) [37m"always?"[39;49;00m].$
   152^I^I^I[31mcontext[39;49;00m := [31mcontext[39;49;00m [32msender[39;49;00m].$
   153^I^I^[36mnil[39;49;00m[34m! ![39;49;00m$
   154^I$
   155^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'mivsek 1/10/2008 18:14'![39;49;00m$
   156^I[32mforLanguage:[39;49;00m [31maLanguageCodeSymbol[39;49;00m$
   157^I^I[37m"for multilingual support: returns an apropriate instance of itself for that language. [39;49;00m$
   158^I[37m^ILangage is defined by ISO 639 2-letter language code, see [39;49;00m$
   159^I[37m^Ihttp://en.wikipedia.org/wiki/List_of_ISO_639-1_codes"[39;49;00m$
   160^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
   161^I$
   162^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'mivsek 1/10/2008 18:14'![39;49;00m$
   163^I[32misMultilingual[39;49;00m$
   164^I^I[37m"for multilingual support: override this if your domain object responds [39;49;00m$
   165^I[37m^Ito #forLanguage: and returns an apropriate instance of itself for that language"[39;49;00m$
   166^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
   167^I$
   168^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:27'![39;49;00m$
   169^I[32misVersionedObject[39;49;00m$
   170^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
   171^I$
   172^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:27'![39;49;00m$
   173^I[32misWebApplication[39;49;00m$
   174^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
   175^I$
   176^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:27'![39;49;00m$
   177^I[32misWebStyle[39;49;00m$
   178^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
   179^I$
   180^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:27'![39;49;00m$
   181^I[32mmodifiedTimestamp[39;49;00m$
   182^I^I[37m"when this object was last modified"[39;49;00m$
   183^I^I[37m"used in http response, override if you like to be included"[39;49;00m$
   184^I^I^[36mnil[39;49;00m[34m! ![39;49;00m$
   185^I$
   186^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:28'![39;49;00m$
   187^I[32mpreferedUrl[39;49;00m$
   188^I^I[37m"override with a suggestion for url of this method!! If not already used, [39;49;00m$
   189^I[37m^Iit will be considered by URLResolver during automatic url generation"[39;49;00m$
   190^I^I^[36mnil[39;49;00m[34m! ![39;49;00m$
   191^I$
   192^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:28'![39;49;00m$
   193^I[32mprintWebAppNotFoundFor:[39;49;00m [31maSession[39;49;00m $
   194^I^I|[31m page [39;49;00m|$
   195^I^I[31mpage[39;49;00m := [04m[32mWebPage[39;49;00m [36mnew[39;49;00m.$
   196^I^I[31mpage[39;49;00m [32maddText:[39;49;00m [33m'Cannot find aWebApplication for object a'[39;49;00m[32m,[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m.$
   197^I^I^[31mpage[39;49;00m[34m! ![39;49;00m$
   198^I$
   199^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:28'![39;49;00m$
   200^I[32mprintWebPageFor:[39;49;00m [31maSession[39;49;00m $
   201^I^I[37m"find appropriate web application to represent self as web page"[39;49;00m$
   202^I$
   203^I^I|[31m webApp [39;49;00m|$
   204^I^I[31mwebApp[39;49;00m := [36mself[39;49;00m [32mwebAppFor:[39;49;00m [31maSession[39;49;00m.$
   205^I^I^[31mwebApp[39;49;00m [32mnotNil[39;49;00m $
   206^I^I^I[36mifTrue:[39;49;00m [[31mwebApp[39;49;00m [32mprintWebPage[39;49;00m]$
   207^I^I^I[36mifFalse:[39;49;00m [[36mself[39;49;00m [32mprintWebAppNotFoundFor:[39;49;00m [31maSession[39;49;00m][34m! ![39;49;00m$
   208^I$
   209^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:29'![39;49;00m$
   210^I[32msendOver:[39;49;00m [31maStream[39;49;00m $
   211^I^I[37m"from Wiki rendering"[39;49;00m$
   212^I^I[36mself[39;49;00m [32mprintOn:[39;49;00m [31maStream[39;49;00m[34m! ![39;49;00m$
   213^I$
   214^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:29'![39;49;00m$
   215^I[32mwebAppFor:[39;49;00m [31maSession[39;49;00m$
   216^I^I|[31m webApp [39;49;00m|$
   217^I^I[31maSession[39;49;00m [32misNil[39;49;00m [36mifTrue:[39;49;00m [^[36mnil[39;49;00m].$
   218^I^I[31mwebApp[39;49;00m := [31maSession[39;49;00m [32mwebAppFor:[39;49;00m [36mself[39;49;00m.$
   219^I^I[31mwebApp[39;49;00m [32mnotNil[39;49;00m [36mifTrue:[39;49;00m [^[31mwebApp[39;49;00m].$
   220^I^I[31mwebApp[39;49;00m := [04m[32mWebApplication[39;49;00m [32mnewFor:[39;49;00m [36mself[39;49;00m [32mon:[39;49;00m [31maSession[39;49;00m.$
   221^I^I[31mwebApp[39;49;00m [32mnotNil[39;49;00m [36mifTrue:[39;49;00m [[31maSession[39;49;00m [32maddWebApp:[39;49;00m [31mwebApp[39;49;00m [32mfor:[39;49;00m [36mself[39;49;00m].$
   222^I^I^[31mwebApp[39;49;00m[34m! ![39;49;00m$
   223^I$
   224^I$
   225^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*DynamicBindings'[39;49;00m[34m stamp: 'svp 3/6/2003 16:08'![39;49;00m$
   226^I[32mbinding[39;49;00m$
   227^I^I[37m"Answer the DynamicBinding for the receiver (if any)"[39;49;00m$
   228^I$
   229^I^I^[04m[32mBindings[39;49;00m [32mbindingFor:[39;49;00m [36mself[39;49;00m [32mifNotBound:[39;49;00m [[36mnil[39;49;00m][34m! ![39;49;00m$
   230^I$
   231^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*DynamicBindings'[39;49;00m[34m stamp: 'svp 4/29/2003 00:35'![39;49;00m$
   232^I[32mbinding:[39;49;00m [31manObject[39;49;00m$
   233^I^I[37m"Set the dynamic binding for the receiver, if anObject is nil, then [39;49;00m$
   234^I[37m^Iremove the receiver's dynamic binding (if any)"[39;49;00m$
   235^I$
   236^I^I^[31manObject[39;49;00m $
   237^I^I^I[32mifNil:[39;49;00m [[36mself[39;49;00m [32mremoveBinding[39;49;00m]$
   238^I^I^I[32mifNotNil:[39;49;00m [[04m[32mBindings[39;49;00m [32mbind:[39;49;00m [36mself[39;49;00m [32mto:[39;49;00m [31manObject[39;49;00m][34m! ![39;49;00m$
   239^I$
   240^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*DynamicBindings'[39;49;00m[34m stamp: 'svp 3/6/2003 16:09'![39;49;00m$
   241^I[32mhasBinding[39;49;00m$
   242^I^I[37m"Answer whether or not the receiver has a dynamic binding"[39;49;00m$
   243^I$
   244^I^I^[04m[32mBindings[39;49;00m [32mincludesKey:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
   245^I$
   246^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*DynamicBindings'[39;49;00m[34m stamp: 'svp 3/6/2003 16:09'![39;49;00m$
   247^I[32mremoveBinding[39;49;00m$
   248^I^I[37m"Remove the dynamic binding associated with the receiver"[39;49;00m$
   249^I$
   250^I^I^[04m[32mBindings[39;49;00m [32mremoveKey:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m [][34m! ![39;49;00m$
   251^I$
   252^I$
   253^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*KomHttpServer'[39;49;00m[34m stamp: 'SVP 8/23/1999 19:17'![39;49;00m$
   254^I[32masHtmlDocumentForRequest:[39;49;00m [31maNetworkRequest[39;49;00m$
   255^I$
   256^I^I[36mself[39;49;00m [32merror:[39;49;00m $
   257^I^I^I([33m'The requested object ('[39;49;00m[32m,[39;49;00m $
   258^I^I^I[36mself[39;49;00m [32masString[39;49;00m[32m,[39;49;00m $
   259^I^I^I[33m'), could not be converted into HTML for your browser.'[39;49;00m)[34m! ![39;49;00m$
   260^I$
   261^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*KomHttpServer'[39;49;00m[34m stamp: 'SVP 8/23/1999 19:23'![39;49;00m$
   262^I[32masHttpResponseTo:[39;49;00m [31manHttpRequest[39;49;00m$
   263^I$
   264^I^I^([36mself[39;49;00m [32masHtmlDocumentForRequest:[39;49;00m [31manHttpRequest[39;49;00m) $
   265^I^I^I[32masHttpResponseTo:[39;49;00m [31manHttpRequest[39;49;00m$
   266^I[34m! ![39;49;00m$
   267^I$
   268^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*KomHttpServer'[39;49;00m[34m stamp: 'svp 5/16/2003 12:47'![39;49;00m$
   269^I[32misComancheModule[39;49;00m$
   270^I$
   271^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
   272^I$
   273^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*KomHttpServer'[39;49;00m[34m stamp: 'SVP 8/17/1999 17:51'![39;49;00m$
   274^I[32mmimeType[39;49;00m$
   275^I$
   276^I^I^[04m[32mMIMEDocument[39;49;00m [32mdefaultContentType[39;49;00m[34m! ![39;49;00m$
   277^I$
   278^I$
   279^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Morphic-NewCurve-testing'''[39;49;00m[34m stamp: 'wiz 12/31/2005 21:31'![39;49;00m$
   280^I[32misNonZero[39;49;00m$
   281^I[37m"Overriden in Number. This returns the backstop answer for non-numbers"[39;49;00m$
   282^I^[36mfalse[39;49;00m.[34m! ![39;49;00m$
   283^I$
   284^I$
   285^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/25/2006 18:18'![39;49;00m$
   286^I[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   287^I[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
   288^I[32mto:[39;49;00m [31manObject[39;49;00m$
   289^I[32mexclusive:[39;49;00m [31maValueHolder[39;49;00m$
   290^I $
   291^I^I[36mself[39;49;00m$
   292^I^I^I[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   293^I^I^I[32mevaluate:[39;49;00m (([04m[32mExclusiveWeakMessageSend[39;49;00m$
   294^I^I^I^I^I^I[32mreceiver:[39;49;00m [31manObject[39;49;00m$
   295^I^I^I^I^I^I[32mselector:[39;49;00m [31maMessageSelector[39;49;00m)$
   296^I^I^I^I^I^I^I[32mbasicExecuting:[39;49;00m [31maValueHolder[39;49;00m)[34m! ![39;49;00m$
   297^I$
   298^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/25/2006 18:17'![39;49;00m$
   299^I[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   300^I[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
   301^I[32mto:[39;49;00m [31manObject[39;49;00m$
   302^I[32mwith:[39;49;00m [31manArg[39;49;00m$
   303^I[32mexclusive:[39;49;00m [31maValueHolder[39;49;00m$
   304^I $
   305^I    [36mself[39;49;00m$
   306^I        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   307^I        [32mevaluate:[39;49;00m (([04m[32mExclusiveWeakMessageSend[39;49;00m$
   308^I ^I^I[32mreceiver:[39;49;00m [31manObject[39;49;00m$
   309^I^I^I[32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
   310^I^I^I[32marguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manArg[39;49;00m))$
   311^I^I^I^I[32mbasicExecuting:[39;49;00m [31maValueHolder[39;49;00m)[34m! ![39;49;00m$
   312^I$
   313^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/25/2006 18:17'![39;49;00m$
   314^I[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   315^I[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
   316^I[32mto:[39;49;00m [31manObject[39;49;00m$
   317^I[32mwithArguments:[39;49;00m [31manArgArray[39;49;00m$
   318^I[32mexclusive:[39;49;00m [31maValueHolder[39;49;00m$
   319^I $
   320^I    [36mself[39;49;00m$
   321^I        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   322^I        [32mevaluate:[39;49;00m (([04m[32mExclusiveWeakMessageSend[39;49;00m$
   323^I^I^I[32mreceiver:[39;49;00m [31manObject[39;49;00m$
   324^I^I^I[32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
   325^I^I^I[32marguments:[39;49;00m [31manArgArray[39;49;00m)$
   326^I^I^I^I[32mbasicExecuting:[39;49;00m [31maValueHolder[39;49;00m)[34m! ![39;49;00m$
   327^I$
   328^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/24/2006 11:50'![39;49;00m$
   329^I[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   330^I[32msendOnce:[39;49;00m [31maMessageSelector[39;49;00m$
   331^I[32mto:[39;49;00m [31manObject[39;49;00m$
   332^I $
   333^I    [36mself[39;49;00m$
   334^I        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   335^I        [32mevaluate:[39;49;00m ([04m[32mNonReentrantWeakMessageSend[39;49;00m$
   336^I            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
   337^I            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m)[34m! ![39;49;00m$
   338^I$
   339^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/24/2006 11:49'![39;49;00m$
   340^I[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   341^I[32msendOnce:[39;49;00m [31maMessageSelector[39;49;00m$
   342^I[32mto:[39;49;00m [31manObject[39;49;00m$
   343^I[32mwith:[39;49;00m [31manArg[39;49;00m$
   344^I $
   345^I    [36mself[39;49;00m$
   346^I        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   347^I        [32mevaluate:[39;49;00m ([04m[32mNonReentrantWeakMessageSend[39;49;00m$
   348^I            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
   349^I            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
   350^I^I^I[32marguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manArg[39;49;00m))[34m! ![39;49;00m$
   351^I$
   352^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/24/2006 11:49'![39;49;00m$
   353^I[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   354^I[32msendOnce:[39;49;00m [31maMessageSelector[39;49;00m$
   355^I[32mto:[39;49;00m [31manObject[39;49;00m$
   356^I[32mwithArguments:[39;49;00m [31manArgArray[39;49;00m$
   357^I $
   358^I    [36mself[39;49;00m$
   359^I        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
   360^I        [32mevaluate:[39;49;00m ([04m[32mNonReentrantWeakMessageSend[39;49;00m$
   361^I            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
   362^I            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
   363^I^I^I[32marguments:[39;49;00m [31manArgArray[39;49;00m)[34m! ![39;49;00m$
   364^I$
   365^I$
   366^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-Widgets'[39;49;00m[34m stamp: 'gvc 1/10/2007 11:41'![39;49;00m$
   367^I[32mokToClose[39;49;00m$
   368^I^I[37m"Sent to models when a window closing.[39;49;00m$
   369^I[37m^IAllows this check to be independent of okToChange."[39;49;00m$
   370^I^I$
   371^I^I^[36mtrue[39;49;00m[34m! ![39;49;00m$
   372^I$
   373^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-Widgets'[39;49;00m[34m stamp: 'gvc 4/17/2007 17:41'![39;49;00m$
   374^I[32mtaskbarIcon[39;49;00m$
   375^I^I[37m"Answer the icon for the receiver in a task bar[39;49;00m$
   376^I[37m^Ior nil for the default."[39;49;00m$
   377^I$
   378^I^I^[36mself[39;49;00m [32mclass[39;49;00m [32mtaskbarIcon[39;49;00m[34m! ![39;49;00m$
   379^I$
   380^I$
   381^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-Widgets-override'[39;49;00m[34m stamp: 'gvc 9/4/2007 12:32'![39;49;00m$
   382^I[32mwindowActiveOnFirstClick[39;49;00m$
   383^I^I[37m"Return true if my window should be active on first click."[39;49;00m$
   384^I$
   385^I^I^[36mtrue[39;49;00m[34m! ![39;49;00m$
   386^I$
   387^I$
   388^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*SeasideAdaptersCompatibility'[39;49;00m[34m stamp: 'pmm 11/25/2007 14:17'![39;49;00m$
   389^I[32mtoString[39;49;00m$
   390^I^I^[36mself[39;49;00m[34m! ![39;49;00m$
   391^I$
   392^I$
   393^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Tools-Explorer'[39;49;00m[34m stamp: 'stephaneducasse 9/17/2005 21:52'![39;49;00m$
   394^I[32mexploreAndYourself[39;49;00m$
   395^I^I[37m"i.e. explore; yourself. Thisway i can peek w/o typing all the parentheses"[39;49;00m$
   396^I^I[36mself[39;49;00m [32mexplore[39;49;00m. $
   397^I     ^[36mself[39;49;00m[34m! ![39;49;00m$
   398^I$
   399^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Tools-Explorer'[39;49;00m[34m stamp: 'stephaneducasse 9/17/2005 21:48'![39;49;00m$
   400^I[32mexploreWithLabel:[39;49;00m [31mlabel[39;49;00m$
   401^I$
   402^I^I^ [04m[32mObjectExplorer[39;49;00m [36mnew[39;49;00m [32mopenExplorerFor:[39;49;00m [36mself[39;49;00m [32mwithLabel:[39;49;00m$
   403^I[31mlabel[39;49;00m[34m! ![39;49;00m$
   404^I$
   405^I$
   406^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*kernel-extensions-flagging'[39;49;00m[34m stamp: 'mtf 1/26/2008 23:34'![39;49;00m$
   407^I[32mdeprecated[39;49;00m$
   408^I^I[37m"Warn that the sending method has been deprecated."[39;49;00m$
   409^I$
   410^I^I[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
   411^I^I^I[[04m[32mDeprecation[39;49;00m [32msignal:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m' has been deprecated.'[39;49;00m][34m! ![39;49;00m$
   412^I$
   413^I$
   414^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*kernel-extensions-flexibility'[39;49;00m[34m stamp: 'kph 1/27/2008 19:21'![39;49;00m$
   415^I[32maskFor:[39;49;00m [31mselector[39;49;00m $
   416^I$
   417^I    [37m"returns true or false"[39;49;00m$
   418^I^I$
   419^I^I^ ([36mself[39;49;00m [32maskFor:[39;49;00m [31mselector[39;49;00m [32mifAbsent:[39;49;00m [36mnil[39;49;00m) [32m==[39;49;00m [36mtrue[39;49;00m[34m! ![39;49;00m$
   420^I$
   421^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*kernel-extensions-flexibility'[39;49;00m[34m stamp: 'kph 10/17/2007 14:01'![39;49;00m$
   422^I[32maskFor:[39;49;00m [31mselector[39;49;00m [32mifAbsent:[39;49;00m [31maBlock[39;49;00m$
   423^I$
   424^I   [37m"enables a default value to be specified in order to be tolerant of potentially missing methods[39;49;00m$
   425^I[37m^I[39;49;00m$
   426^I[37m^Ie.g.[39;49;00m$
   427^I[37m^I(myPoint askFor: #originOffset) ifAbsent: [ 0@0 ].[39;49;00m$
   428^I[37m^I"[39;49;00m$
   429^I$
   430^I^I^ ([36mself[39;49;00m [32mclass[39;49;00m [32mcanUnderstand:[39;49;00m [31mselector[39;49;00m) [36mifFalse:[39;49;00m [ [31maBlock[39;49;00m [32mvalue[39;49;00m ] [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m][34m! ![39;49;00m$
   431^I$
   432^I$
   433^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*kernel-extensions-logging'[39;49;00m[34m stamp: 'mtf 1/26/2008 23:52'![39;49;00m$
   434^I[32mlog[39;49;00m$
   435^I^I[37m"This method provides the univeral entry point fo all logging mechanisms"[39;49;00m$
   436^I^I$
   437^I^I[37m"Options:[39;49;00m$
   438^I[37m^I1. Null for null logging[39;49;00m$
   439^I[37m^I2. A LogRouter instance wih a FrameworkAdaptor.[39;49;00m$
   440^I[37m^I3. CurrentLog a process local variable supplying a LogRouter"[39;49;00m$
   441^I^I$
   442^I^I^ ([04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#CurrentLog[39;49;00m [32mifAbsent:[39;49;00m [ [04m[32mNull[39;49;00m [32mdefault[39;49;00m ]) [32mvalue[39;49;00m$
   443^I^I^I[32msender:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m; [32mbeginEntry[39;49;00m; [32myourself[39;49;00m[34m! ![39;49;00m$
   444^I$
   445^I$
   446^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-accessing'[39;49;00m[34m stamp: 'lr 3/9/2006 11:31'![39;49;00m$
   447^I[32mdescription[39;49;00m$
   448^I^I[37m"Return the description of the reciever. Subclasses might override this message to return instance-based descriptions."[39;49;00m$
   449^I$
   450^I^I^ [36mself[39;49;00m [32mclass[39;49;00m [32mdescription[39;49;00m[34m! ![39;49;00m$
   451^I$
   452^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-accessing'[39;49;00m[34m stamp: 'lr 3/9/2006 11:31'![39;49;00m$
   453^I[32mmementoClass[39;49;00m$
   454^I^I[37m"Return a class to be used to remember or cache the receiver, namely a memento object."[39;49;00m$
   455^I$
   456^I^I^ [04m[32mMACheckedMemento[39;49;00m[34m! ![39;49;00m$
   457^I$
   458^I$
   459^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-model'[39;49;00m[34m stamp: 'lr 3/9/2006 11:31'![39;49;00m$
   460^I[32mreadUsing:[39;49;00m [31maDescription[39;49;00m$
   461^I^I[37m"Dispatch the read-access to the receiver using the accessor of aDescription."[39;49;00m$
   462^I$
   463^I^I^ [31maDescription[39;49;00m [32maccessor[39;49;00m [32mread:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
   464^I$
   465^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-model'[39;49;00m[34m stamp: 'lr 3/9/2006 11:31'![39;49;00m$
   466^I[32mwrite:[39;49;00m [31manObject[39;49;00m [32musing:[39;49;00m [31maDescription[39;49;00m$
   467^I^I[37m"Dispatch the write-access to the receiver of anObject using the accessor of aDescription."[39;49;00m$
   468^I$
   469^I^I[31maDescription[39;49;00m [32maccessor[39;49;00m [32mwrite:[39;49;00m [31manObject[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
   470^I$
   471^I$
   472^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-testing'[39;49;00m[34m stamp: 'lr 3/9/2006 11:31'![39;49;00m$
   473^I[32misDescription[39;49;00m$
   474^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
   475^I$
   476^I$
   477^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-morph-converting'[39;49;00m[34m stamp: 'lr 3/9/2006 11:33'![39;49;00m$
   478^I[32masMorph[39;49;00m$
   479^I^I^ [36mself[39;49;00m [32mdescription[39;49;00m [32masMorphOn:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
   480^I$
   481^I$
   482^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-seaside-converting'[39;49;00m[34m stamp: 'lr 3/9/2006 11:33'![39;49;00m$
   483^I[32masComponent[39;49;00m$
   484^I^I^ [36mself[39;49;00m [32mdescription[39;49;00m [32masComponentOn:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
   485^I$
   486^I$
   487^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*monticello'[39;49;00m[34m stamp: 'dvf 8/10/2004 23:25'![39;49;00m$
   488^I[32misConflict[39;49;00m$
   489^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
   490^I$
   491^I$
   492^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*null'[39;49;00m[34m stamp: 'kph 9/6/2007 23:31'![39;49;00m$
   493^I[32mifNull:[39;49;00m [31maBlock[39;49;00m$
   494^I$
   495^I^I^ [36mself[39;49;00m[34m! ![39;49;00m$
   496^I$
   497^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*null'[39;49;00m[34m stamp: 'kph 9/6/2007 23:33'![39;49;00m$
   498^I[32misNull[39;49;00m$
   499^I$
   500^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
   501^I$
   502^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*null'[39;49;00m[34m stamp: 'kph 4/12/2007 08:27'![39;49;00m$
   503^I[32morNull[39;49;00m$
   504^I$
   505^I^I^ [36mself[39;49;00m[34m! ![39;49;00m$
   506^I$
   507^I$
   508^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*ob-tools-inspector'[39;49;00m[34m stamp: 'lr 6/5/2008 11:07'![39;49;00m$
   509^I[32mbasicInspectorNodes[39;49;00m$
   510^I^I<[34minspector:[39;49;00m #'1' priority: 600>$
   511^I^I$
   512^I^I|[31m nodes [39;49;00m|$
   513^I^I[31mnodes[39;49;00m := [04m[32mOrderedCollection[39;49;00m [32mnew:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32m+[39;49;00m [36mself[39;49;00m [32mbasicSize[39;49;00m [32m+[39;49;00m [34m5[39;49;00m.$
   514^I^I[31mnodes[39;49;00m [32madd:[39;49;00m [36mself[39;49;00m [32mselfInspectorNode[39;49;00m.$
   515^I^I[36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mwithIndexDo:[39;49;00m [ :[31mname[39;49;00m :[31mindex[39;49;00m |$
   516^I^I^I[31mnodes[39;49;00m [32madd:[39;49;00m ([04m[32mOTNamedVariableNode[39;49;00m [32mon:[39;49;00m [36mself[39;49;00m [32mindex:[39;49;00m [31mindex[39;49;00m [32mname:[39;49;00m [31mname[39;49;00m) ].$
   517^I^I[34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32mbasicSize[39;49;00m [32mdo:[39;49;00m [ :[31mindex[39;49;00m |$
   518^I^I^I[31mnodes[39;49;00m [32madd:[39;49;00m ([04m[32mOTIndexedVariableNode[39;49;00m [32mon:[39;49;00m [36mself[39;49;00m [32mindex:[39;49;00m [31mindex[39;49;00m) ].$
   519^I^I^ [31mnodes[39;49;00m[34m! ![39;49;00m$
   520^I$
   521^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*ob-tools-inspector'[39;49;00m[34m stamp: 'lr 6/5/2008 11:07'![39;49;00m$
   522^I[32mprotocolInspectorNodes[39;49;00m$
   523^I^I<[34minspector:[39;49;00m #'#' priority: 800>$
   524^I$
   525^I^I^ [36mself[39;49;00m [32mclass[39;49;00m [32mallSelectors[39;49;00m [32masArray[39;49;00m [32msort[39;49;00m$
   526^I^I^I[32mcollect:[39;49;00m [ :[31meach[39;49;00m | [04m[32mOTProtocolInspectorNode[39;49;00m [32mon:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [31meach[39;49;00m ][34m! ![39;49;00m$
   527^I$
   528^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*ob-tools-inspector'[39;49;00m[34m stamp: 'lr 6/5/2008 09:58'![39;49;00m$
   529^I[32mselfInspectorNode[39;49;00m$
   530^I^I^ [04m[32mOTDerivedInspectorNode[39;49;00m [32mon:[39;49;00m [36mself[39;49;00m [32mlabel:[39;49;00m [33m'self'[39;49;00m [32mblock:[39;49;00m [ :[31mobj[39;49;00m | [31mobj[39;49;00m ][34m! ![39;49;00m$
   531^I$
   532^I$
   533^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*omnibrowser-converting'[39;49;00m[34m stamp: 'cwp 4/17/2006 12:16'![39;49;00m$
   534^I[32masAnnouncement[39;49;00m$
   535^I^I^ [36mself[39;49;00m[34m! ![39;49;00m$
   536^I$
   537^I$
   538^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*pier-model'[39;49;00m[34m stamp: 'lr 3/9/2006 11:29'![39;49;00m$
   539^I[32maccept:[39;49;00m [31maVisitor[39;49;00m$
   540^I^I[36mself[39;49;00m [32msubclassResponsibility[39;49;00m[34m! ![39;49;00m$
   541^I$
   542^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*pier-model'[39;49;00m[34m stamp: 'lr 3/9/2006 11:29'![39;49;00m$
   543^I[32macceptDecorated:[39;49;00m [31maVisitor[39;49;00m$
   544^I^I[36mself[39;49;00m [32maccept:[39;49;00m [31maVisitor[39;49;00m[34m! ![39;49;00m$
   545^I$
   546^I$
   547^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*rio-kernel'[39;49;00m[34m stamp: 'kph 3/8/2007 21:25'![39;49;00m$
   548^I[32misRio[39;49;00m$
   549^I$
   550^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
   551^I$
   552^I$
   553^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*scriptaculous'[39;49;00m[34m stamp: 'lr 1/4/2007 17:20'![39;49;00m$
   554^I[32masFunction[39;49;00m$
   555^I^I^ [36mself[39;49;00m [32masFunction:[39;49;00m [33m#([39;49;00m[33m)[39;49;00m[34m! ![39;49;00m$
   556^I$
   557^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*scriptaculous'[39;49;00m[34m stamp: 'lr 1/4/2007 17:21'![39;49;00m$
   558^I[32masFunction:[39;49;00m [31maCollection[39;49;00m$
   559^I^I^ [04m[32mSUFunction[39;49;00m [36mnew[39;49;00m [32madd:[39;49;00m [36mself[39;49;00m; [32marguments:[39;49;00m [31maCollection[39;49;00m[34m! ![39;49;00m$
   560^I$
   561^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*scriptaculous'[39;49;00m[34m stamp: 'lr 4/11/2006 19:49'![39;49;00m$
   562^I[32masJavascript[39;49;00m$
   563^I^I^ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [ :[31mstream[39;49;00m | [36mself[39;49;00m [32mjavascriptOn:[39;49;00m [31mstream[39;49;00m ][34m! ![39;49;00m$
   564^I$
   565^I$
   566^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*scriptaculous-printing'[39;49;00m[34m stamp: 'lr 4/20/2006 21:10'![39;49;00m$
   567^I[32mjavascriptOn:[39;49;00m [31maStream[39;49;00m$
   568^I^I[36mself[39;49;00m [32mprintOn:[39;49;00m [31maStream[39;49;00m[34m! ![39;49;00m$
   569^I$
   570^I$
   571^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'lr 6/5/2007 21:35'![39;49;00m$
   572^I[32mdeprecatedApi[39;49;00m$
   573^I^I[36mself[39;49;00m [32mdeprecatedApi:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mdisplayString[39;49;00m[34m! ![39;49;00m$
   574^I$
   575^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'lr 6/5/2007 21:35'![39;49;00m$
   576^I[32mdeprecatedApi:[39;49;00m [31maString[39;49;00m$
   577^I^I[04m[32mWADeprecatedApi[39;49;00m [32mraiseSignal:[39;49;00m [31maString[39;49;00m[34m! ![39;49;00m$
   578^I$
   579^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'lr 5/9/2007 08:47'![39;49;00m$
   580^I[32minspectorFields[39;49;00m$
   581^I^I|[31m members [39;49;00m|$
   582^I^I[31mmembers[39;49;00m := [04m[32mArray[39;49;00m [36mnew[39;49;00m [32mwriteStream[39;49;00m.$
   583^I^I[36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mwithIndexDo:[39;49;00m [ :[31meach[39;49;00m :[31mindex[39;49;00m |$
   584^I^I^I[31mmembers[39;49;00m [32mnextPut:[39;49;00m [31meach[39;49;00m [32m->[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m) ].$
   585^I^I[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m [36mifTrue:[39;49;00m [$
   586^I^I^I[34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32msize[39;49;00m [32mdo:[39;49;00m [ :[31mindex[39;49;00m |$
   587^I^I^I^I[31mmembers[39;49;00m [32mnextPut:[39;49;00m [31mindex[39;49;00m [32m->[39;49;00m ([36mself[39;49;00m [32mat:[39;49;00m [31mindex[39;49;00m) ] ].$
   588^I^I^ [31mmembers[39;49;00m [32mcontents[39;49;00m[34m! ![39;49;00m$
   589^I$
   590^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'avi 3/14/2005 15:19'![39;49;00m$
   591^I[32mlabelForSelector:[39;49;00m [31maSymbol[39;49;00m$
   592^I^I^ [31maSymbol[39;49;00m [32masCapitalizedPhrase[39;49;00m[34m! ![39;49;00m$
   593^I$
   594^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'pmm 4/7/2007 17:14'![39;49;00m$
   595^I[32mrenderOn:[39;49;00m [31maRenderer[39;49;00m$
   596^I^I[37m"Override this method to customize how objects (not components) are rendered when passed as an argument to #render:. The default is the return value of #displayString.[39;49;00m$
   597^I[37m^IJust remember that you can not use #callback:, #on:of:, or #call:"[39;49;00m$
   598^I$
   599^I^I[31maRenderer[39;49;00m [32mtext:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
   600^I$
   601^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'lr 3/19/2007 23:13'![39;49;00m$
   602^I[32mrestoreFromSnapshot:[39;49;00m [31manObject[39;49;00m$
   603^I^I[36mself[39;49;00m [32mcopyFrom:[39;49;00m [31manObject[39;49;00m[34m! ![39;49;00m$
   604^I$
   605^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'avi 9/1/2004 21:20'![39;49;00m$
   606^I[32msnapshotCopy[39;49;00m$
   607^I^I^ [36mself[39;49;00m [32mshallowCopy[39;49;00m[34m! ![39;49;00m$
   608^I$
   609^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'lr 10/28/2007 14:42'![39;49;00m$
   610^I[32mvalidationError:[39;49;00m [31mmessage[39;49;00m$
   611^I^I^[04m[32mWAValidationNotification[39;49;00m [32mraiseSignal:[39;49;00m [31mmessage[39;49;00m[34m! ![39;49;00m$
   612^I$
   613^I$
   614^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2-encoding'[39;49;00m[34m stamp: 'lr 3/26/2007 20:16'![39;49;00m$
   615^I[32mencodeOn:[39;49;00m [31maDocument[39;49;00m$
   616^I^I[31maDocument[39;49;00m [32mprint:[39;49;00m [36mself[39;49;00m [32mdisplayString[39;49;00m[34m! ![39;49;00m$
   617^I$
   618^I$
   619^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2-squeak'[39;49;00m[34m stamp: 'pmm 5/22/2007 22:10'![39;49;00m$
   620^I[32mbeMutable[39;49;00m$
   621^I^I[37m"for VW compatibility, a hack that allows to cache a value in a literal array"[39;49;00m[34m! ![39;49;00m$
   622^I$
   623^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2-squeak'[39;49;00m[34m stamp: 'lr 7/12/2005 17:01'![39;49;00m$
   624^I[32mdisplayString[39;49;00m$
   625^I^I^ [36mself[39;49;00m [32masString[39;49;00m[34m! ![39;49;00m$
   626^I$
   627^I$
   628^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*services-base'[39;49;00m[34m stamp: 'rr 3/21/2006 11:54'![39;49;00m$
   629^I[32mrequestor[39;49;00m$
   630^I^I[37m"returns the focused window's requestor"[39;49;00m$
   631^I$
   632^I^I[37m"SystemWindow focusedWindow ifNotNilDo: [:w | ^ w requestor]."[39;49;00m$
   633^I$
   634^I^I[37m"triggers an infinite loop"[39;49;00m$
   635^I$
   636^I^I^ [04m[32mRequestor[39;49;00m [32mdefault[39;49;00m[34m! ![39;49;00m$
   637^I$
   638^I$
   639^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*system-support'[39;49;00m[34m stamp: 'dvf 8/23/2003 12:27'![39;49;00m$
   640^I[32msystemNavigation[39;49;00m$
   641^I$
   642^I^I^ [04m[32mSystemNavigation[39;49;00m [32mdefault[39;49;00m[34m! ![39;49;00m$
   643^I$
   644^I$
   645^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*tools-browser'[39;49;00m[34m stamp: 'mu 3/6/2004 15:13'![39;49;00m$
   646^I[32mbrowse[39;49;00m$
   647^I^I[36mself[39;49;00m [32msystemNavigation[39;49;00m [32mbrowseClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m[34m! ![39;49;00m$
   648^I$
   649^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*tools-browser'[39;49;00m[34m stamp: 'mu 3/11/2004 16:00'![39;49;00m$
   650^I[32mbrowseHierarchy[39;49;00m$
   651^I^I[36mself[39;49;00m [32msystemNavigation[39;49;00m [32mbrowseHierarchy:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m[34m! ![39;49;00m$
   652^I$
   653^I$
   654^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*universes'[39;49;00m[34m stamp: 'ls 11/26/2006 12:33'![39;49;00m$
   655^I[32misUPackage[39;49;00m$
   656^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
   657^I$
   658^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*universes'[39;49;00m[34m stamp: 'ls 11/26/2006 12:33'![39;49;00m$
   659^I[32misUPackageCategory[39;49;00m$
   660^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
   661^I$
   662^I$
   663^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'sw 4/30/1998 12:18'![39;49;00m$
   664^I[32maddInstanceVarNamed:[39;49;00m [31maName[39;49;00m [32mwithValue:[39;49;00m [31maValue[39;49;00m$
   665^I^I[37m"Add an instance variable named aName and give it value aValue"[39;49;00m$
   666^I^I[36mself[39;49;00m [32mclass[39;49;00m [32maddInstVarName:[39;49;00m [31maName[39;49;00m [32masString[39;49;00m.$
   667^I^I[36mself[39;49;00m [32minstVarAt:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mput:[39;49;00m [31maValue[39;49;00m[34m! ![39;49;00m$
   668^I$
   669^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'yo 6/29/2004 11:39'![39;49;00m$
   670^I[32mat:[39;49;00m [31mindex[39;49;00m $
   671^I^I[37m"Primitive. Assumes receiver is indexable. Answer the value of an [39;49;00m$
   672^I[37m^Iindexable element in the receiver. Fail if the argument index is not an [39;49;00m$
   673^I[37m^IInteger or is out of bounds. Essential. See Object documentation [39;49;00m$
   674^I[37m^IwhatIsAPrimitive."[39;49;00m$
   675^I$
   676^I^I<[34mprimitive:[39;49;00m 60>$
   677^I^I[31mindex[39;49;00m [32misInteger[39;49;00m [36mifTrue:[39;49;00m$
   678^I^I^I[[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m$
   679^I^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32merrorSubscriptBounds:[39;49;00m [31mindex[39;49;00m]$
   680^I^I^I^I[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNotIndexable[39;49;00m]].$
   681^I^I[31mindex[39;49;00m [32misNumber[39;49;00m$
   682^I^I^I[36mifTrue:[39;49;00m [^[36mself[39;49;00m [32mat:[39;49;00m [31mindex[39;49;00m [32masInteger[39;49;00m]$
   683^I^I^I[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNonIntegerIndex[39;49;00m][34m! ![39;49;00m$
   684^I$
   685^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
   686^I[32mat:[39;49;00m [31mindex[39;49;00m [32mmodify:[39;49;00m [31maBlock[39;49;00m$
   687^I^I[37m"Replace the element of the collection with itself transformed by the block"[39;49;00m$
   688^I^I^ [36mself[39;49;00m [32mat:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([31maBlock[39;49;00m [32mvalue:[39;49;00m ([36mself[39;49;00m [32mat:[39;49;00m [31mindex[39;49;00m))[34m! ![39;49;00m$
   689^I$
   690^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'yo 6/29/2004 13:08'![39;49;00m$
   691^I[32mat:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m [31mvalue[39;49;00m $
   692^I^I[37m"Primitive. Assumes receiver is indexable. Store the argument value in [39;49;00m$
   693^I[37m^Ithe indexable element of the receiver indicated by index. Fail if the [39;49;00m$
   694^I[37m^Iindex is not an Integer or is out of bounds. Or fail if the value is not of [39;49;00m$
   695^I[37m^Ithe right type for this kind of collection. Answer the value that was [39;49;00m$
   696^I[37m^Istored. Essential. See Object documentation whatIsAPrimitive."[39;49;00m$
   697^I$
   698^I^I<[34mprimitive:[39;49;00m 61>$
   699^I^I[31mindex[39;49;00m [32misInteger[39;49;00m [36mifTrue:[39;49;00m$
   700^I^I^I[[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m$
   701^I^I^I^I[36mifTrue:[39;49;00m [([31mindex[39;49;00m [32m>=[39;49;00m [34m1[39;49;00m [32mand:[39;49;00m [[31mindex[39;49;00m [32m<=[39;49;00m [36mself[39;49;00m [32msize[39;49;00m])$
   702^I^I^I^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32merrorImproperStore[39;49;00m]$
   703^I^I^I^I^I^I[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorSubscriptBounds:[39;49;00m [31mindex[39;49;00m]]$
   704^I^I^I^I[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNotIndexable[39;49;00m]].$
   705^I^I[31mindex[39;49;00m [32misNumber[39;49;00m$
   706^I^I^I[36mifTrue:[39;49;00m [^[36mself[39;49;00m [32mat:[39;49;00m [31mindex[39;49;00m [32masInteger[39;49;00m [32mput:[39;49;00m [31mvalue[39;49;00m]$
   707^I^I^I[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNonIntegerIndex[39;49;00m][34m! ![39;49;00m$
   708^I$
   709^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'yo 9/20/2004 10:22'![39;49;00m$
   710^I[32mbasicAddInstanceVarNamed:[39;49;00m [31maName[39;49;00m [32mwithValue:[39;49;00m [31maValue[39;49;00m$
   711^I^I[37m"Add an instance variable named aName and give it value aValue"[39;49;00m$
   712^I^I[36mself[39;49;00m [32mclass[39;49;00m [32maddInstVarName:[39;49;00m [31maName[39;49;00m [32masString[39;49;00m.$
   713^I^I[36mself[39;49;00m [32minstVarAt:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mput:[39;49;00m [31maValue[39;49;00m[34m! ![39;49;00m$
   714^I$
   715^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
   716^I[32mbasicAt:[39;49;00m [31mindex[39;49;00m $
   717^I^I[37m"Primitive. Assumes receiver is indexable. Answer the value of an [39;49;00m$
   718^I[37m^Iindexable element in the receiver. Fail if the argument index is not an [39;49;00m$
   719^I[37m^IInteger or is out of bounds. Essential. Do not override in a subclass. See [39;49;00m$
   720^I[37m^IObject documentation whatIsAPrimitive."[39;49;00m$
   721^I$
   722^I^I<[34mprimitive:[39;49;00m 60>$
   723^I^I[31mindex[39;49;00m [32misInteger[39;49;00m [36mifTrue:[39;49;00m [[36mself[39;49;00m [32merrorSubscriptBounds:[39;49;00m [31mindex[39;49;00m].$
   724^I^I[31mindex[39;49;00m [32misNumber[39;49;00m$
   725^I^I^I[36mifTrue:[39;49;00m [^[36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32masInteger[39;49;00m]$
   726^I^I^I[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNonIntegerIndex[39;49;00m][34m! ![39;49;00m$
   727^I$
   728^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
   729^I[32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m [31mvalue[39;49;00m $
   730^I^I[37m"Primitive. Assumes receiver is indexable. Store the second argument [39;49;00m$
   731^I[37m^Ivalue in the indexable element of the receiver indicated by index. Fail [39;49;00m$
   732^I[37m^Iif the index is not an Integer or is out of bounds. Or fail if the value is [39;49;00m$
   733^I[37m^Inot of the right type for this kind of collection. Answer the value that [39;49;00m$
   734^I[37m^Iwas stored. Essential. Do not override in a subclass. See Object [39;49;00m$
   735^I[37m^Idocumentation whatIsAPrimitive."[39;49;00m$
   736^I$
   737^I^I<[34mprimitive:[39;49;00m 61>$
   738^I^I[31mindex[39;49;00m [32misInteger[39;49;00m$
   739^I^I^I[36mifTrue:[39;49;00m [([31mindex[39;49;00m [32m>=[39;49;00m [34m1[39;49;00m [32mand:[39;49;00m [[31mindex[39;49;00m [32m<=[39;49;00m [36mself[39;49;00m [32msize[39;49;00m])$
   740^I^I^I^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32merrorImproperStore[39;49;00m]$
   741^I^I^I^I^I^I[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorSubscriptBounds:[39;49;00m [31mindex[39;49;00m]].$
   742^I^I[31mindex[39;49;00m [32misNumber[39;49;00m$
   743^I^I^I[36mifTrue:[39;49;00m [^[36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32masInteger[39;49;00m [32mput:[39;49;00m [31mvalue[39;49;00m]$
   744^I^I^I[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNonIntegerIndex[39;49;00m][34m! ![39;49;00m$
   745^I$
   746^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
   747^I[32mbasicSize[39;49;00m$
   748^I^I[37m"Primitive. Answer the number of indexable variables in the receiver. [39;49;00m$
   749^I[37m^IThis value is the same as the largest legal subscript. Essential. Do not [39;49;00m$
   750^I[37m^Ioverride in any subclass. See Object documentation whatIsAPrimitive."[39;49;00m$
   751^I$
   752^I^I<[34mprimitive:[39;49;00m 62>$
   753^I^I[37m"The number of indexable fields of fixed-length objects is 0"[39;49;00m$
   754^I^I^[34m0[39;49;00m^I[34m! ![39;49;00m$
   755^I$
   756^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
   757^I[32mbindWithTemp:[39;49;00m [31maBlock[39;49;00m$
   758^I^I^ [31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m [32mvalue:[39;49;00m [36mnil[39;49;00m[34m! ![39;49;00m$
   759^I$
   760^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'md 10/7/2004 15:43'![39;49;00m$
   761^I[32mifNil:[39;49;00m [31mnilBlock[39;49;00m [32mifNotNilDo:[39;49;00m [31maBlock[39;49;00m $
   762^I^I[37m"Evaluate aBlock with the receiver as its argument."[39;49;00m$
   763^I$
   764^I^I^ [31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m$
   765^I[34m! ![39;49;00m$
   766^I$
   767^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'di 11/8/2000 21:04'![39;49;00m$
   768^I[32mifNotNilDo:[39;49;00m [31maBlock[39;49;00m$
   769^I^I[37m"Evaluate the given block with the receiver as its argument."[39;49;00m$
   770^I$
   771^I^I^ [31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m$
   772^I[34m! ![39;49;00m$
   773^I$
   774^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'md 10/7/2004 15:43'![39;49;00m$
   775^I[32mifNotNilDo:[39;49;00m [31maBlock[39;49;00m [32mifNil:[39;49;00m [31mnilBlock[39;49;00m$
   776^I^I[37m"Evaluate aBlock with the receiver as its argument."[39;49;00m$
   777^I$
   778^I^I^ [31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m$
   779^I[34m! ![39;49;00m$
   780^I$
   781^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'ajh 1/21/2003 12:59'![39;49;00m$
   782^I[32min:[39;49;00m [31maBlock[39;49;00m$
   783^I^I[37m"Evaluate the given block with the receiver as its argument."[39;49;00m$
   784^I$
   785^I^I^ [31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m$
   786^I[34m! ![39;49;00m$
   787^I$
   788^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'sw 10/17/2000 11:15'![39;49;00m$
   789^I[32mpresenter[39;49;00m$
   790^I^I[37m"Answer the presenter object associated with the receiver.  For morphs, there is in effect a clear containment hierarchy of presenters (accessed via their association with PasteUpMorphs); for arbitrary objects the hook is simply via the current world, at least at present."[39;49;00m$
   791^I$
   792^I^I^ [36mself[39;49;00m [32mcurrentWorld[39;49;00m [32mpresenter[39;49;00m[34m! ![39;49;00m$
   793^I$
   794^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
   795^I[32mreadFromString:[39;49;00m [31maString[39;49;00m$
   796^I^I[37m"Create an object based on the contents of aString."[39;49;00m$
   797^I$
   798^I^I^[36mself[39;49;00m [32mreadFrom:[39;49;00m ([04m[32mReadStream[39;49;00m [32mon:[39;49;00m [31maString[39;49;00m)[34m! ![39;49;00m$
   799^I$
   800^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'di 3/29/1999 13:10'![39;49;00m$
   801^I[32msize[39;49;00m$
   802^I^I[37m"Primitive. Answer the number of indexable variables in the receiver. [39;49;00m$
   803^I[37m^IThis value is the same as the largest legal subscript. Essential. See Object [39;49;00m$
   804^I[37m^Idocumentation whatIsAPrimitive."[39;49;00m$
   805^I$
   806^I^I<[34mprimitive:[39;49;00m 62>$
   807^I^I[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m [36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNotIndexable[39;49;00m].$
   808^I^I^ [34m0[39;49;00m[34m! ![39;49;00m$
   809^I$
   810^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'md 5/16/2006 12:34'![39;49;00m$
   811^I[32myourself[39;49;00m$
   812^I^I[37m"Answer self."[39;49;00m$
   813^I^I^[36mself[39;49;00m[34m! ![39;49;00m$
   814^I$
   815^I$
   816^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'associating'[39;49;00m[34m stamp: 'md 7/22/2005 16:03'![39;49;00m$
   817^I[32m->[39;49;00m [31manObject[39;49;00m$
   818^I^I[37m"Answer an Association between self and anObject"[39;49;00m$
   819^I$
   820^I^I^[04m[32mAssociation[39;49;00m [32mbasicNew[39;49;00m [32mkey:[39;49;00m [36mself[39;49;00m [32mvalue:[39;49;00m [31manObject[39;49;00m[34m! ![39;49;00m$
   821^I$
   822^I$
   823^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'binding'[39;49;00m[34m![39;49;00m$
   824^I[32mbindingOf:[39;49;00m [31maString[39;49;00m$
   825^I^I^[36mnil[39;49;00m[34m! ![39;49;00m$
   826^I$
   827^I$
   828^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'breakpoint'[39;49;00m[34m stamp: 'bkv 7/1/2003 12:33'![39;49;00m$
   829^I[32mbreak[39;49;00m$
   830^I^I[37m"This is a simple message to use for inserting breakpoints during debugging.[39;49;00m$
   831^I[37m^IThe debugger is opened by sending a signal. This gives a chance to restore[39;49;00m$
   832^I[37m^Iinvariants related to multiple processes."[39;49;00m$
   833^I$
   834^I^I[04m[32mBreakPoint[39;49;00m [32msignal[39;49;00m.$
   835^I$
   836^I^I[37m"nil break."[39;49;00m[34m! ![39;49;00m$
   837^I$
   838^I$
   839^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'casing'[39;49;00m[34m![39;49;00m$
   840^I[32mcaseOf:[39;49;00m [31maBlockAssociationCollection[39;49;00m$
   841^I^I[37m"The elements of aBlockAssociationCollection are associations between blocks.[39;49;00m$
   842^I[37m^I Answer the evaluated value of the first association in aBlockAssociationCollection[39;49;00m$
   843^I[37m^I whose evaluated key equals the receiver.  If no match is found, report an error."[39;49;00m$
   844^I$
   845^I^I^ [36mself[39;49;00m [32mcaseOf:[39;49;00m [31maBlockAssociationCollection[39;49;00m [32motherwise:[39;49;00m [[36mself[39;49;00m [32mcaseError[39;49;00m]$
   846^I$
   847^I[37m"| z | z _ {[#a]->[1+1]. ['b' asSymbol]->[2+2]. [#c]->[3+3]}. #b caseOf: z"[39;49;00m$
   848^I[37m"| z | z _ {[#a]->[1+1]. ['d' asSymbol]->[2+2]. [#c]->[3+3]}. #b caseOf: z"[39;49;00m$
   849^I[37m"The following are compiled in-line:"[39;49;00m$
   850^I[37m"#b caseOf: {[#a]->[1+1]. ['b' asSymbol]->[2+2]. [#c]->[3+3]}"[39;49;00m$
   851^I[37m"#b caseOf: {[#a]->[1+1]. ['d' asSymbol]->[2+2]. [#c]->[3+3]}"[39;49;00m[34m! ![39;49;00m$
   852^I$
   853^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'casing'[39;49;00m[34m![39;49;00m$
   854^I[32mcaseOf:[39;49;00m [31maBlockAssociationCollection[39;49;00m [32motherwise:[39;49;00m [31maBlock[39;49;00m$
   855^I^I[37m"The elements of aBlockAssociationCollection are associations between blocks.[39;49;00m$
   856^I[37m^I Answer the evaluated value of the first association in aBlockAssociationCollection[39;49;00m$
   857^I[37m^I whose evaluated key equals the receiver.  If no match is found, answer the result[39;49;00m$
   858^I[37m^I of evaluating aBlock."[39;49;00m$
   859^I$
   860^I^I[31maBlockAssociationCollection[39;49;00m [32massociationsDo:[39;49;00m$
   861^I^I^I[:[31massoc[39;49;00m | ([31massoc[39;49;00m [32mkey[39;49;00m [32mvalue[39;49;00m [32m=[39;49;00m [36mself[39;49;00m) [36mifTrue:[39;49;00m [^[31massoc[39;49;00m [32mvalue[39;49;00m [32mvalue[39;49;00m]].$
   862^I^I^ [31maBlock[39;49;00m [32mvalue[39;49;00m$
   863^I$
   864^I[37m"| z | z _ {[#a]->[1+1]. ['b' asSymbol]->[2+2]. [#c]->[3+3]}. #b caseOf: z otherwise: [0]"[39;49;00m$
   865^I[37m"| z | z _ {[#a]->[1+1]. ['d' asSymbol]->[2+2]. [#c]->[3+3]}. #b caseOf: z otherwise: [0]"[39;49;00m$
   866^I[37m"The following are compiled in-line:"[39;49;00m$
   867^I[37m"#b caseOf: {[#a]->[1+1]. ['b' asSymbol]->[2+2]. [#c]->[3+3]} otherwise: [0]"[39;49;00m$
   868^I[37m"#b caseOf: {[#a]->[1+1]. ['d' asSymbol]->[2+2]. [#c]->[3+3]} otherwise: [0]"[39;49;00m[34m! ![39;49;00m$
   869^I$
   870^I$
   871^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m![39;49;00m$
   872^I[32mclass[39;49;00m$
   873^I^I[37m"Primitive. Answer the object which is the receiver's class. Essential. See [39;49;00m$
   874^I[37m^IObject documentation whatIsAPrimitive."[39;49;00m$
   875^I$
   876^I^I<[34mprimitive:[39;49;00m 111>$
   877^I^I[36mself[39;49;00m [32mprimitiveFailed[39;49;00m[34m! ![39;49;00m$
   878^I$
   879^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m stamp: 'sw 9/27/2001 15:51'![39;49;00m$
   880^I[32minheritsFromAnyIn:[39;49;00m [31maList[39;49;00m$
   881^I^I[37m"Answer whether the receiver inherits from any class represented by any element in the list.  The elements of the list can be classes, class name symbols, or strings representing possible class names.  This allows speculative membership tests to be made even when some of the classes may not be known to the current image, and even when their names are not interned symbols."[39;49;00m$
   882^I$
   883^I^I|[31m aClass [39;49;00m|$
   884^I^I[31maList[39;49;00m [32mdo:[39;49;00m$
   885^I^I^I[:[31melem[39;49;00m | [04m[32mSymbol[39;49;00m [32mhasInterned:[39;49;00m [31melem[39;49;00m [32masString[39;49;00m [36mifTrue:[39;49;00m $
   886^I^I^I^I[:[31melemSymbol[39;49;00m | ((([31maClass[39;49;00m _ [04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [31melemSymbol[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m]) [32misKindOf:[39;49;00m [04m[32mClass[39;49;00m)$
   887^I^I^I^I^I^I^I[32mand:[39;49;00m [[36mself[39;49;00m [32misKindOf:[39;49;00m [31maClass[39;49;00m])$
   888^I^I^I^I^I[36mifTrue:[39;49;00m$
   889^I^I^I^I^I^I[^ [36mtrue[39;49;00m]]].$
   890^I^I^ [36mfalse[39;49;00m$
   891^I$
   892^I$
   893^I[37m"[39;49;00m$
   894^I[37m{3.  true. 'olive'} do:[39;49;00m$
   895^I[37m^I[:token |[39;49;00m$
   896^I[37m^I^I {{#Number. #Boolean}. {Number.  Boolean }.  {'Number'. 'Boolean'}} do:[39;49;00m$
   897^I[37m^I^I^I[:list |[39;49;00m$
   898^I[37m^I^I^I^ITranscript cr; show: token asString, ' list element provided as a ', list first class name, ' - ', (token inheritsFromAnyIn: list) asString]][39;49;00m$
   899^I[37m"[39;49;00m[34m! ![39;49;00m$
   900^I$
   901^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m![39;49;00m$
   902^I[32misKindOf:[39;49;00m [31maClass[39;49;00m $
   903^I^I[37m"Answer whether the class, aClass, is a superclass or class of the receiver."[39;49;00m$
   904^I$
   905^I^I[36mself[39;49;00m [32mclass[39;49;00m [32m==[39;49;00m [31maClass[39;49;00m$
   906^I^I^I[36mifTrue:[39;49;00m [^[36mtrue[39;49;00m]$
   907^I^I^I[36mifFalse:[39;49;00m [^[36mself[39;49;00m [32mclass[39;49;00m [32minheritsFrom:[39;49;00m [31maClass[39;49;00m][34m! ![39;49;00m$
   908^I$
   909^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m stamp: 'sw 2/16/98 02:08'![39;49;00m$
   910^I[32misKindOf:[39;49;00m [31maClass[39;49;00m [32morOf:[39;49;00m [31manotherClass[39;49;00m$
   911^I^I[37m"Answer whether either of the classes, aClass or anotherClass,, is a superclass or class of the receiver.  A convenience; could be somewhat optimized"[39;49;00m$
   912^I^I^ ([36mself[39;49;00m [32misKindOf:[39;49;00m [31maClass[39;49;00m) [32mor:[39;49;00m [[36mself[39;49;00m [32misKindOf:[39;49;00m [31manotherClass[39;49;00m][34m! ![39;49;00m$
   913^I$
   914^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m![39;49;00m$
   915^I[32misMemberOf:[39;49;00m [31maClass[39;49;00m $
   916^I^I[37m"Answer whether the receiver is an instance of the class, aClass."[39;49;00m$
   917^I$
   918^I^I^[36mself[39;49;00m [32mclass[39;49;00m [32m==[39;49;00m [31maClass[39;49;00m[34m! ![39;49;00m$
   919^I$
   920^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m![39;49;00m$
   921^I[32mrespondsTo:[39;49;00m [31maSymbol[39;49;00m $
   922^I^I[37m"Answer whether the method dictionary of the receiver's class contains [39;49;00m$
   923^I[37m^IaSymbol as a message selector."[39;49;00m$
   924^I$
   925^I^I^[36mself[39;49;00m [32mclass[39;49;00m [32mcanUnderstand:[39;49;00m [31maSymbol[39;49;00m[34m! ![39;49;00m$
   926^I$
   927^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m stamp: 'tk 10/21/1998 12:38'![39;49;00m$
   928^I[32mxxxClass[39;49;00m$
   929^I^I[37m"For subclasses of nil, such as ObjectOut"[39;49;00m$
   930^I^I^ [36mself[39;49;00m [32mclass[39;49;00m[34m! ![39;49;00m$
   931^I$
   932^I$
   933^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m stamp: 'tk 4/16/1999 18:26'![39;49;00m$
   934^I[32mcloseTo:[39;49;00m [31manObject[39;49;00m$
   935^I^I[37m"Answer whether the receiver and the argument represent the same[39;49;00m$
   936^I[37m^Iobject. If = is redefined in any subclass, consider also redefining the[39;49;00m$
   937^I[37m^Imessage hash."[39;49;00m$
   938^I$
   939^I^I|[31m ans [39;49;00m|$
   940^I^I[[31mans[39;49;00m _ [36mself[39;49;00m [32m=[39;49;00m [31manObject[39;49;00m] [32mifError:[39;49;00m [:[31maString[39;49;00m :[31maReceiver[39;49;00m | ^ [36mfalse[39;49;00m].$
   941^I^I^ [31mans[39;49;00m[34m! ![39;49;00m$
   942^I$
   943^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m![39;49;00m$
   944^I[32mhash[39;49;00m$
   945^I^I[37m"Answer a SmallInteger whose value is related to the receiver's identity.[39;49;00m$
   946^I[37m^IMay be overridden, and should be overridden in any classes that define = "[39;49;00m$
   947^I$
   948^I^I^ [36mself[39;49;00m [32midentityHash[39;49;00m[34m! ![39;49;00m$
   949^I$
   950^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m stamp: 'pm 9/23/97 09:36'![39;49;00m$
   951^I[32mhashMappedBy:[39;49;00m [31mmap[39;49;00m$
   952^I^I[37m"Answer what my hash would be if oops changed according to map."[39;49;00m$
   953^I$
   954^I^I^[31mmap[39;49;00m [32mnewHashFor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
   955^I$
   956^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m stamp: 'di 9/27/97 20:23'![39;49;00m$
   957^I[32midentityHashMappedBy:[39;49;00m [31mmap[39;49;00m$
   958^I^I[37m"Answer what my hash would be if oops changed according to map."[39;49;00m$
   959^I$
   960^I^I^[31mmap[39;49;00m [32mnewHashFor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
   961^I$
   962^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m stamp: 'sw 8/20/1998 12:34'![39;49;00m$
   963^I[32midentityHashPrintString[39;49;00m$
   964^I^I[37m"'fred' identityHashPrintString"[39;49;00m$
   965^I$
   966^I^I^ [33m'('[39;49;00m[32m,[39;49;00m [36mself[39;49;00m [32midentityHash[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m')'[39;49;00m[34m! ![39;49;00m$
   967^I$
   968^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m stamp: 'ajh 2/2/2002 15:02'![39;49;00m$
   969^I[32mliteralEqual:[39;49;00m [31mother[39;49;00m$
   970^I$
   971^I^I^ [36mself[39;49;00m [32mclass[39;49;00m [32m==[39;49;00m [31mother[39;49;00m [32mclass[39;49;00m [32mand:[39;49;00m [[36mself[39;49;00m [32m=[39;49;00m [31mother[39;49;00m][34m! ![39;49;00m$
   972^I$
   973^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m![39;49;00m$
   974^I[32m=[39;49;00m [31manObject[39;49;00m $
   975^I^I[37m"Answer whether the receiver and the argument represent the same [39;49;00m$
   976^I[37m^Iobject. If = is redefined in any subclass, consider also redefining the [39;49;00m$
   977^I[37m^Imessage hash."[39;49;00m$
   978^I$
   979^I^I^[36mself[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m[34m! ![39;49;00m$
   980^I$
   981^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m![39;49;00m$
   982^I[32m~=[39;49;00m [31manObject[39;49;00m $
   983^I^I[37m"Answer whether the receiver and the argument do not represent the [39;49;00m$
   984^I[37m^Isame object."[39;49;00m$
   985^I$
   986^I^I^[36mself[39;49;00m [32m=[39;49;00m [31manObject[39;49;00m [32m==[39;49;00m [36mfalse[39;49;00m[34m! ![39;49;00m$
   987^I$
   988^I$
   989^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'di 11/9/1998 12:15'![39;49;00m$
   990^I[32madaptToFloat:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m$
   991^I^I[37m"If no method has been provided for adapting an object to a Float,[39;49;00m$
   992^I[37m^Ithen it may be adequate to simply adapt it to a number."[39;49;00m$
   993^I^I^ [36mself[39;49;00m [32madaptToNumber:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m[34m! ![39;49;00m$
   994^I$
   995^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'di 11/9/1998 12:14'![39;49;00m$
   996^I[32madaptToFraction:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m$
   997^I^I[37m"If no method has been provided for adapting an object to a Fraction,[39;49;00m$
   998^I[37m^Ithen it may be adequate to simply adapt it to a number."[39;49;00m$
   999^I^I^ [36mself[39;49;00m [32madaptToNumber:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m[34m! ![39;49;00m$
  1000^I$
  1001^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'di 11/9/1998 12:15'![39;49;00m$
  1002^I[32madaptToInteger:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m$
  1003^I^I[37m"If no method has been provided for adapting an object to a Integer,[39;49;00m$
  1004^I[37m^Ithen it may be adequate to simply adapt it to a number."[39;49;00m$
  1005^I^I^ [36mself[39;49;00m [32madaptToNumber:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m[34m! ![39;49;00m$
  1006^I$
  1007^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'rw 4/27/2002 07:48'![39;49;00m$
  1008^I[32masActionSequence[39;49;00m$
  1009^I$
  1010^I^I^[04m[32mWeakActionSequence[39;49;00m [32mwith:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  1011^I$
  1012^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'rw 7/20/2003 16:03'![39;49;00m$
  1013^I[32masActionSequenceTrappingErrors[39;49;00m$
  1014^I$
  1015^I^I^[04m[32mWeakActionSequenceTrappingErrors[39;49;00m [32mwith:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  1016^I$
  1017^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'svp 5/16/2000 18:14'![39;49;00m$
  1018^I[32masDraggableMorph[39;49;00m$
  1019^I^I^([04m[32mStringMorph[39;49;00m [32mcontents:[39;49;00m [36mself[39;49;00m [32mprintString[39;49;00m)$
  1020^I^I^I[32mcolor:[39;49;00m [04m[32mColor[39;49;00m [32mwhite[39;49;00m;$
  1021^I^I^I[32myourself[39;49;00m[34m! ![39;49;00m$
  1022^I$
  1023^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'sma 5/12/2000 17:39'![39;49;00m$
  1024^I[32masOrderedCollection[39;49;00m$
  1025^I^I[37m"Answer an OrderedCollection with the receiver as its only element."[39;49;00m$
  1026^I$
  1027^I^I^ [04m[32mOrderedCollection[39;49;00m [32mwith:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  1028^I$
  1029^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m![39;49;00m$
  1030^I[32masString[39;49;00m$
  1031^I^I[37m"Answer a string that represents the receiver."[39;49;00m$
  1032^I$
  1033^I^I^ [36mself[39;49;00m [32mprintString[39;49;00m [34m! ![39;49;00m$
  1034^I$
  1035^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'ajh 3/11/2003 10:27'![39;49;00m$
  1036^I[32masStringOrText[39;49;00m$
  1037^I^I[37m"Answer a string that represents the receiver."[39;49;00m$
  1038^I$
  1039^I^I^ [36mself[39;49;00m [32mprintString[39;49;00m [34m! ![39;49;00m$
  1040^I$
  1041^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m![39;49;00m$
  1042^I[32mas:[39;49;00m [31maSimilarClass[39;49;00m$
  1043^I^I[37m"Create an object of class aSimilarClass that has similar contents to the receiver."[39;49;00m$
  1044^I$
  1045^I^I^ [31maSimilarClass[39;49;00m [32mnewFrom:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  1046^I$
  1047^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'RAA 8/2/1999 12:41'![39;49;00m$
  1048^I[32mcomplexContents[39;49;00m$
  1049^I$
  1050^I^I^[36mself[39;49;00m[34m! ![39;49;00m$
  1051^I$
  1052^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'ajh 7/6/2003 20:37'![39;49;00m$
  1053^I[32mmustBeBoolean[39;49;00m$
  1054^I^I[37m"Catches attempts to test truth of non-Booleans.  This message is sent from the VM.  The sending context is rewound to just before the jump causing this exception."[39;49;00m$
  1055^I$
  1056^I^I^ [36mself[39;49;00m [32mmustBeBooleanIn:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m[34m! ![39;49;00m$
  1057^I$
  1058^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'ajh 7/6/2003 20:40'![39;49;00m$
  1059^I[32mmustBeBooleanIn:[39;49;00m [31mcontext[39;49;00m$
  1060^I^I[37m"context is the where the non-boolean error occurred. Rewind context to before jump then raise error."[39;49;00m$
  1061^I$
  1062^I^I|[31m proceedValue [39;49;00m|$
  1063^I^I[31mcontext[39;49;00m [32mskipBackBeforeJump[39;49;00m.$
  1064^I^I[31mproceedValue[39;49;00m _ [04m[32mNonBooleanReceiver[39;49;00m [36mnew[39;49;00m$
  1065^I^I^I[32mobject:[39;49;00m [36mself[39;49;00m;$
  1066^I^I^I[32msignal:[39;49;00m [33m'proceed for truth.'[39;49;00m.$
  1067^I^I^ [31mproceedValue[39;49;00m [32m~~[39;49;00m [36mfalse[39;49;00m[34m! ![39;49;00m$
  1068^I$
  1069^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'sw 3/26/2001 12:12'![39;49;00m$
  1070^I[32mprintDirectlyToDisplay[39;49;00m$
  1071^I^I[37m"For debugging: write the receiver's printString directly to the display at (0, 100); senders of this are detected by the check-for-slips mechanism."[39;49;00m$
  1072^I$
  1073^I^I[36mself[39;49;00m [32masString[39;49;00m [32mdisplayAt:[39;49;00m [34m0[39;49;00m[32m@[39;49;00m[34m100[39;49;00m$
  1074^I$
  1075^I[37m"StringMorph someInstance printDirectlyToDisplay"[39;49;00m[34m! ![39;49;00m$
  1076^I$
  1077^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'RAA 3/31/1999 12:13'![39;49;00m$
  1078^I[32mwithoutListWrapper[39;49;00m$
  1079^I$
  1080^I^I^[36mself[39;49;00m[34m! ![39;49;00m$
  1081^I$
  1082^I$
  1083^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m![39;49;00m$
  1084^I[32mclone[39;49;00m$
  1085^I$
  1086^I^I<[34mprimitive:[39;49;00m 148>$
  1087^I^I[36mself[39;49;00m [32mprimitiveFailed[39;49;00m[34m! ![39;49;00m$
  1088^I$
  1089^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'ajh 8/18/2001 21:25'![39;49;00m$
  1090^I[32mcopy[39;49;00m$
  1091^I^I[37m"Answer another instance just like the receiver. Subclasses typically override postCopy; they typically do not override shallowCopy."[39;49;00m$
  1092^I$
  1093^I^I^[36mself[39;49;00m [32mshallowCopy[39;49;00m [32mpostCopy[39;49;00m[34m! ![39;49;00m$
  1094^I$
  1095^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 8/20/1998 16:01'![39;49;00m$
  1096^I[32mcopyAddedStateFrom:[39;49;00m [31manotherObject[39;49;00m$
  1097^I^I[37m"Copy over the values of instance variables added by the receiver's class from anotherObject to the receiver.  These will be remapped in mapUniClasses, if needed."[39;49;00m$
  1098^I$
  1099^I^I[36mself[39;49;00m [32mclass[39;49;00m [32msuperclass[39;49;00m [32minstSize[39;49;00m [32m+[39;49;00m [34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mdo:[39;49;00m$
  1100^I^I^I[:[31mindex[39;49;00m | [36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([31manotherObject[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m)][34m! ![39;49;00m$
  1101^I$
  1102^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tpr 2/14/2004 21:53'![39;49;00m$
  1103^I[32mcopyFrom:[39;49;00m [31manotherObject[39;49;00m$
  1104^I^I[37m"Copy to myself all instance variables I have in common with anotherObject.  This is dangerous because it ignores an object's control over its own inst vars.  "[39;49;00m$
  1105^I$
  1106^I^I|[31m mine his [39;49;00m|$
  1107^I^I<[34mprimitive:[39;49;00m 168>$
  1108^I^I[31mmine[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m.$
  1109^I^I[31mhis[39;49;00m _ [31manotherObject[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m.$
  1110^I^I[34m1[39;49;00m [32mto:[39;49;00m ([31mmine[39;49;00m [32msize[39;49;00m [32mmin:[39;49;00m [31mhis[39;49;00m [32msize[39;49;00m) [32mdo:[39;49;00m [:[31mind[39;49;00m |$
  1111^I^I^I([31mmine[39;49;00m [32mat:[39;49;00m [31mind[39;49;00m) [32m=[39;49;00m ([31mhis[39;49;00m [32mat:[39;49;00m [31mind[39;49;00m) [36mifTrue:[39;49;00m [$
  1112^I^I^I^I[36mself[39;49;00m [32minstVarAt:[39;49;00m [31mind[39;49;00m [32mput:[39;49;00m ([31manotherObject[39;49;00m [32minstVarAt:[39;49;00m [31mind[39;49;00m)]].$
  1113^I^I[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m [32m&[39;49;00m [31manotherObject[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m [36mifTrue:[39;49;00m [$
  1114^I^I^I[34m1[39;49;00m [32mto:[39;49;00m ([36mself[39;49;00m [32mbasicSize[39;49;00m [32mmin:[39;49;00m [31manotherObject[39;49;00m [32mbasicSize[39;49;00m) [32mdo:[39;49;00m [:[31mind[39;49;00m |$
  1115^I^I^I^I[36mself[39;49;00m [32mbasicAt:[39;49;00m [31mind[39;49;00m [32mput:[39;49;00m ([31manotherObject[39;49;00m [32mbasicAt:[39;49;00m [31mind[39;49;00m)]].[34m! ![39;49;00m$
  1116^I$
  1117^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'ajh 5/23/2002 00:38'![39;49;00m$
  1118^I[32mcopySameFrom:[39;49;00m [31motherObject[39;49;00m$
  1119^I^I[37m"Copy to myself all instance variables named the same in otherObject.[39;49;00m$
  1120^I[37m^IThis ignores otherObject's control over its own inst vars."[39;49;00m$
  1121^I$
  1122^I^I|[31m myInstVars otherInstVars match [39;49;00m|$
  1123^I^I[31mmyInstVars[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m.$
  1124^I^I[31motherInstVars[39;49;00m _ [31motherObject[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m.$
  1125^I^I[31mmyInstVars[39;49;00m [32mdoWithIndex:[39;49;00m [:[31meach[39;49;00m :[31mindex[39;49;00m |$
  1126^I^I^I([31mmatch[39;49;00m _ [31motherInstVars[39;49;00m [32mindexOf:[39;49;00m [31meach[39;49;00m) [32m>[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m$
  1127^I^I^I^I[[36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([31motherObject[39;49;00m [32minstVarAt:[39;49;00m [31mmatch[39;49;00m)]].$
  1128^I^I[34m1[39;49;00m [32mto:[39;49;00m ([36mself[39;49;00m [32mbasicSize[39;49;00m [32mmin:[39;49;00m [31motherObject[39;49;00m [32mbasicSize[39;49;00m) [32mdo:[39;49;00m [:[31mi[39;49;00m |$
  1129^I^I^I[36mself[39;49;00m [32mbasicAt:[39;49;00m [31mi[39;49;00m [32mput:[39;49;00m ([31motherObject[39;49;00m [32mbasicAt:[39;49;00m [31mi[39;49;00m)].$
  1130^I[34m! ![39;49;00m$
  1131^I$
  1132^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 4/20/1999 14:44'![39;49;00m$
  1133^I[32mcopyTwoLevel[39;49;00m$
  1134^I^I[37m"one more level than a shallowCopy"[39;49;00m$
  1135^I$
  1136^I^I|[31m newObject class index [39;49;00m|$
  1137^I^I[31mclass[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m.$
  1138^I^I[31mnewObject[39;49;00m _ [36mself[39;49;00m [32mclone[39;49;00m.$
  1139^I^I[31mnewObject[39;49;00m [32m==[39;49;00m [36mself[39;49;00m [36mifTrue:[39;49;00m [^ [36mself[39;49;00m].$
  1140^I^I[31mclass[39;49;00m [32misVariable[39;49;00m$
  1141^I^I^I[36mifTrue:[39;49;00m $
  1142^I^I^I^I[[31mindex[39;49;00m _ [36mself[39;49;00m [32mbasicSize[39;49;00m.$
  1143^I^I^I^I[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
  1144^I^I^I^I^I[36mwhileTrue:[39;49;00m $
  1145^I^I^I^I^I^I[[31mnewObject[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m) [32mshallowCopy[39;49;00m.$
  1146^I^I^I^I^I^I[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]].$
  1147^I^I[31mindex[39;49;00m _ [31mclass[39;49;00m [32minstSize[39;49;00m.$
  1148^I^I[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
  1149^I^I^I[36mwhileTrue:[39;49;00m $
  1150^I^I^I^I[[31mnewObject[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m) [32mshallowCopy[39;49;00m.$
  1151^I^I^I^I[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m].$
  1152^I^I^[31mnewObject[39;49;00m[34m! ![39;49;00m$
  1153^I$
  1154^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m![39;49;00m$
  1155^I[32mdeepCopy[39;49;00m$
  1156^I^I[37m"Answer a copy of the receiver with its own copy of each instance [39;49;00m$
  1157^I[37m^Ivariable."[39;49;00m$
  1158^I$
  1159^I^I|[31m newObject class index [39;49;00m|$
  1160^I^I[31mclass[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m.$
  1161^I^I([31mclass[39;49;00m [32m==[39;49;00m [04m[32mObject[39;49;00m) [36mifTrue:[39;49;00m [^[36mself[39;49;00m].$
  1162^I^I[31mclass[39;49;00m [32misVariable[39;49;00m$
  1163^I^I^I[36mifTrue:[39;49;00m $
  1164^I^I^I^I[[31mindex[39;49;00m _ [36mself[39;49;00m [32mbasicSize[39;49;00m.$
  1165^I^I^I^I[31mnewObject[39;49;00m _ [31mclass[39;49;00m [32mbasicNew:[39;49;00m [31mindex[39;49;00m.$
  1166^I^I^I^I[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
  1167^I^I^I^I^I[36mwhileTrue:[39;49;00m $
  1168^I^I^I^I^I^I[[31mnewObject[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m) [32mdeepCopy[39;49;00m.$
  1169^I^I^I^I^I^I[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]$
  1170^I^I^I[36mifFalse:[39;49;00m [[31mnewObject[39;49;00m _ [31mclass[39;49;00m [32mbasicNew[39;49;00m].$
  1171^I^I[31mindex[39;49;00m _ [31mclass[39;49;00m [32minstSize[39;49;00m.$
  1172^I^I[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
  1173^I^I^I[36mwhileTrue:[39;49;00m $
  1174^I^I^I^I[[31mnewObject[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m) [32mdeepCopy[39;49;00m.$
  1175^I^I^I^I[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m].$
  1176^I^I^[31mnewObject[39;49;00m[34m! ![39;49;00m$
  1177^I$
  1178^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'hg 11/23/1999 13:43'![39;49;00m$
  1179^I[32minitialDeepCopierSize[39;49;00m$
  1180^I^I[37m"default value is 4096; other classes may override this, esp. for smaller (=faster) sizes"[39;49;00m$
  1181^I$
  1182^I^I^[34m4096[39;49;00m[34m! ![39;49;00m$
  1183^I$
  1184^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'ajh 1/27/2003 18:45'![39;49;00m$
  1185^I[32mpostCopy[39;49;00m$
  1186^I^I[37m"self is a shallow copy, subclasses should copy fields as necessary to complete the full copy"[39;49;00m$
  1187^I$
  1188^I^I^ [36mself[39;49;00m[34m! ![39;49;00m$
  1189^I$
  1190^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'jm 11/14/97 11:08'![39;49;00m$
  1191^I[32mshallowCopy[39;49;00m$
  1192^I^I[37m"Answer a copy of the receiver which shares the receiver's instance variables."[39;49;00m$
  1193^I^I|[31m class newObject index [39;49;00m|$
  1194^I^I<[34mprimitive:[39;49;00m 148>$
  1195^I^I[31mclass[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m.$
  1196^I^I[31mclass[39;49;00m [32misVariable[39;49;00m$
  1197^I^I^I[36mifTrue:[39;49;00m $
  1198^I^I^I^I[[31mindex[39;49;00m _ [36mself[39;49;00m [32mbasicSize[39;49;00m.$
  1199^I^I^I^I[31mnewObject[39;49;00m _ [31mclass[39;49;00m [32mbasicNew:[39;49;00m [31mindex[39;49;00m.$
  1200^I^I^I^I[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
  1201^I^I^I^I^I[36mwhileTrue:[39;49;00m $
  1202^I^I^I^I^I^I[[31mnewObject[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m).$
  1203^I^I^I^I^I^I[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]$
  1204^I^I^I[36mifFalse:[39;49;00m [[31mnewObject[39;49;00m _ [31mclass[39;49;00m [32mbasicNew[39;49;00m].$
  1205^I^I[31mindex[39;49;00m _ [31mclass[39;49;00m [32minstSize[39;49;00m.$
  1206^I^I[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
  1207^I^I^I[36mwhileTrue:[39;49;00m $
  1208^I^I^I^I[[31mnewObject[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m).$
  1209^I^I^I^I[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m].$
  1210^I^I^ [31mnewObject[39;49;00m[34m! ![39;49;00m$
  1211^I$
  1212^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 3/11/2003 13:58'![39;49;00m$
  1213^I[32mveryDeepCopy[39;49;00m$
  1214^I^I[37m"Do a complete tree copy using a dictionary.  An object in the tree twice is only copied once.  All references to the object in the copy of the tree will point to the new copy."[39;49;00m$
  1215^I$
  1216^I^I|[31m copier new [39;49;00m|$
  1217^I^I[31mcopier[39;49;00m _ [04m[32mDeepCopier[39;49;00m [36mnew[39;49;00m [32minitialize:[39;49;00m [36mself[39;49;00m [32minitialDeepCopierSize[39;49;00m.$
  1218^I^I[31mnew[39;49;00m _ [36mself[39;49;00m [32mveryDeepCopyWith:[39;49;00m [31mcopier[39;49;00m.$
  1219^I^I[31mcopier[39;49;00m [32mmapUniClasses[39;49;00m.$
  1220^I^I[31mcopier[39;49;00m [32mreferences[39;49;00m [32massociationsDo:[39;49;00m [:[31massoc[39;49;00m | $
  1221^I^I^I[31massoc[39;49;00m [32mvalue[39;49;00m [32mveryDeepFixupWith:[39;49;00m [31mcopier[39;49;00m].$
  1222^I^I[31mcopier[39;49;00m [32mfixDependents[39;49;00m.$
  1223^I^I^ [31mnew[39;49;00m[34m! ![39;49;00m$
  1224^I$
  1225^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 3/11/2003 13:58'![39;49;00m$
  1226^I[32mveryDeepCopySibling[39;49;00m$
  1227^I^I[37m"Do a complete tree copy using a dictionary.  Substitute a clone of oldPlayer for the root.  Normally, a Player or non systemDefined object would have a new class.  We do not want one this time.  An object in the tree twice, is only copied once.  All references to the object in the copy of the tree will point to the new copy."[39;49;00m$
  1228^I$
  1229^I^I|[31m copier new [39;49;00m|$
  1230^I^I[31mcopier[39;49;00m _ [04m[32mDeepCopier[39;49;00m [36mnew[39;49;00m [32minitialize:[39;49;00m [36mself[39;49;00m [32minitialDeepCopierSize[39;49;00m.$
  1231^I^I[31mcopier[39;49;00m [32mnewUniClasses:[39;49;00m [36mfalse[39;49;00m.$
  1232^I^I[31mnew[39;49;00m _ [36mself[39;49;00m [32mveryDeepCopyWith:[39;49;00m [31mcopier[39;49;00m.$
  1233^I^I[31mcopier[39;49;00m [32mmapUniClasses[39;49;00m.$
  1234^I^I[31mcopier[39;49;00m [32mreferences[39;49;00m [32massociationsDo:[39;49;00m [:[31massoc[39;49;00m | $
  1235^I^I^I[31massoc[39;49;00m [32mvalue[39;49;00m [32mveryDeepFixupWith:[39;49;00m [31mcopier[39;49;00m].$
  1236^I^I[31mcopier[39;49;00m [32mfixDependents[39;49;00m.$
  1237^I^I^ [31mnew[39;49;00m[34m! ![39;49;00m$
  1238^I$
  1239^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 5/13/2003 19:39'![39;49;00m$
  1240^I[32mveryDeepCopyUsing:[39;49;00m [31mcopier[39;49;00m$
  1241^I^I[37m"Do a complete tree copy using a dictionary.  An object in the tree twice is only copied once.  All references to the object in the copy of the tree will point to the new copy.[39;49;00m$
  1242^I[37m^ISame as veryDeepCopy except copier (with dictionary) is supplied.[39;49;00m$
  1243^I[37m^I** do not delete this method, even if it has no callers **"[39;49;00m$
  1244^I$
  1245^I^I|[31m new refs newDep newModel [39;49;00m|$
  1246^I^I[31mnew[39;49;00m _ [36mself[39;49;00m [32mveryDeepCopyWith:[39;49;00m [31mcopier[39;49;00m.$
  1247^I^I[31mcopier[39;49;00m [32mmapUniClasses[39;49;00m.$
  1248^I^I[31mcopier[39;49;00m [32mreferences[39;49;00m [32massociationsDo:[39;49;00m [:[31massoc[39;49;00m | $
  1249^I^I^I[31massoc[39;49;00m [32mvalue[39;49;00m [32mveryDeepFixupWith:[39;49;00m [31mcopier[39;49;00m].$
  1250^I^I[37m"Fix dependents"[39;49;00m$
  1251^I^I[31mrefs[39;49;00m _ [31mcopier[39;49;00m [32mreferences[39;49;00m.$
  1252^I^I[04m[32mDependentsFields[39;49;00m [32massociationsDo:[39;49;00m [:[31mpair[39;49;00m |$
  1253^I^I^I[31mpair[39;49;00m [32mvalue[39;49;00m [32mdo:[39;49;00m [:[31mdep[39;49;00m | $
  1254^I^I^I^I([31mnewDep[39;49;00m _ [31mrefs[39;49;00m [32mat:[39;49;00m [31mdep[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m]) [32mifNotNil:[39;49;00m [$
  1255^I^I^I^I^I[31mnewModel[39;49;00m _ [31mrefs[39;49;00m [32mat:[39;49;00m [31mpair[39;49;00m [32mkey[39;49;00m [32mifAbsent:[39;49;00m [[31mpair[39;49;00m [32mkey[39;49;00m].$
  1256^I^I^I^I^I[31mnewModel[39;49;00m [32maddDependent:[39;49;00m [31mnewDep[39;49;00m]]].$
  1257^I^I^ [31mnew[39;49;00m[34m! ![39;49;00m$
  1258^I$
  1259^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 3/11/2003 14:12'![39;49;00m$
  1260^I[32mveryDeepCopyWith:[39;49;00m [31mdeepCopier[39;49;00m$
  1261^I^I[37m"Copy me and the entire tree of objects I point to.  An object in the tree twice is copied once, and both references point to him.  deepCopier holds a dictionary of objects we have seen.  Some classes refuse to be copied.  Some classes are picky about which fields get deep copied."[39;49;00m$
  1262^I^I|[31m class index sub subAss new uc sup has mine [39;49;00m|$
  1263^I^I[31mdeepCopier[39;49;00m [32mreferences[39;49;00m [32mat:[39;49;00m [36mself[39;49;00m [32mifPresent:[39;49;00m [:[31mnewer[39;49;00m | ^ [31mnewer[39;49;00m]. ^I[37m"already did him"[39;49;00m$
  1264^I^I[31mclass[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m.$
  1265^I^I[31mclass[39;49;00m [32misMeta[39;49;00m [36mifTrue:[39;49;00m [^ [36mself[39;49;00m].^I^I[37m"a class"[39;49;00m$
  1266^I^I[31mnew[39;49;00m _ [36mself[39;49;00m [32mclone[39;49;00m.$
  1267^I^I([31mclass[39;49;00m [32misSystemDefined[39;49;00m [32mnot[39;49;00m [32mand:[39;49;00m [[31mdeepCopier[39;49;00m [32mnewUniClasses[39;49;00m [37m"allowed"[39;49;00m]) [36mifTrue:[39;49;00m [$
  1268^I^I^I[31muc[39;49;00m _ [31mdeepCopier[39;49;00m [32muniClasses[39;49;00m [32mat:[39;49;00m [31mclass[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m].$
  1269^I^I^I[31muc[39;49;00m [32mifNil:[39;49;00m [$
  1270^I^I^I^I[31mdeepCopier[39;49;00m [32muniClasses[39;49;00m [32mat:[39;49;00m [31mclass[39;49;00m [32mput:[39;49;00m ([31muc[39;49;00m _ [36mself[39;49;00m [32mcopyUniClassWith:[39;49;00m [31mdeepCopier[39;49;00m).$
  1271^I^I^I^I[31mdeepCopier[39;49;00m [32mreferences[39;49;00m [32mat:[39;49;00m [31mclass[39;49;00m [32mput:[39;49;00m [31muc[39;49;00m].^I[37m"remember"[39;49;00m$
  1272^I^I^I[31mnew[39;49;00m _ [31muc[39;49;00m [36mnew[39;49;00m.$
  1273^I^I^I[31mnew[39;49;00m [32mcopyFrom:[39;49;00m [36mself[39;49;00m].^I[37m"copy inst vars in case any are weak"[39;49;00m$
  1274^I^I[31mdeepCopier[39;49;00m [32mreferences[39;49;00m [32mat:[39;49;00m [36mself[39;49;00m [32mput:[39;49;00m [31mnew[39;49;00m.^I[37m"remember"[39;49;00m$
  1275^I^I([31mclass[39;49;00m [32misVariable[39;49;00m [32mand:[39;49;00m [[31mclass[39;49;00m [32misPointers[39;49;00m]) [36mifTrue:[39;49;00m $
  1276^I^I^I[[31mindex[39;49;00m _ [36mself[39;49;00m [32mbasicSize[39;49;00m.$
  1277^I^I^I[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m] [36mwhileTrue:[39;49;00m $
  1278^I^I^I^I[[31msub[39;49;00m _ [36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m.$
  1279^I^I^I^I([31msubAss[39;49;00m _ [31mdeepCopier[39;49;00m [32mreferences[39;49;00m [32massociationAt:[39;49;00m [31msub[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m])$
  1280^I^I^I^I^I[32mifNil:[39;49;00m [[31mnew[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([31msub[39;49;00m [32mveryDeepCopyWith:[39;49;00m [31mdeepCopier[39;49;00m)]$
  1281^I^I^I^I^I[32mifNotNil:[39;49;00m [[31mnew[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m [31msubAss[39;49;00m [32mvalue[39;49;00m].$
  1282^I^I^I^I[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]].$
  1283^I^I[37m"Ask each superclass if it wants to share (weak copy) any inst vars"[39;49;00m$
  1284^I^I[31mnew[39;49;00m [32mveryDeepInner:[39;49;00m [31mdeepCopier[39;49;00m.^I^I[37m"does super a lot"[39;49;00m$
  1285^I$
  1286^I^I[37m"other superclasses want all inst vars deep copied"[39;49;00m$
  1287^I^I[31msup[39;49;00m _ [31mclass[39;49;00m.  [31mindex[39;49;00m _ [31mclass[39;49;00m [32minstSize[39;49;00m.$
  1288^I^I[[31mhas[39;49;00m _ [31msup[39;49;00m [32mcompiledMethodAt:[39;49;00m [33m#veryDeepInner:[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m].$
  1289^I^I[31mhas[39;49;00m _ [31mhas[39;49;00m [32mifNil:[39;49;00m [[31mclass[39;49;00m [32misSystemDefined[39;49;00m [32mnot[39;49;00m [37m"is a uniClass"[39;49;00m] [32mifNotNil:[39;49;00m [[36mtrue[39;49;00m].$
  1290^I^I[31mmine[39;49;00m _ [31msup[39;49;00m [32minstVarNames[39;49;00m.$
  1291^I^I[31mhas[39;49;00m [36mifTrue:[39;49;00m [[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [31mmine[39;49;00m [32msize[39;49;00m]^I[37m"skip inst vars"[39;49;00m$
  1292^I^I^I[36mifFalse:[39;49;00m [[34m1[39;49;00m [32mto:[39;49;00m [31mmine[39;49;00m [32msize[39;49;00m [32mdo:[39;49;00m [:[31mxx[39;49;00m |$
  1293^I^I^I^I^I[31msub[39;49;00m _ [36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m.$
  1294^I^I^I^I^I([31msubAss[39;49;00m _ [31mdeepCopier[39;49;00m [32mreferences[39;49;00m [32massociationAt:[39;49;00m [31msub[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m])$
  1295^I^I^I^I^I^I^I[37m"use association, not value, so nil is an exceptional value"[39;49;00m$
  1296^I^I^I^I^I^I[32mifNil:[39;49;00m [[31mnew[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m $
  1297^I^I^I^I^I^I^I^I^I([31msub[39;49;00m [32mveryDeepCopyWith:[39;49;00m [31mdeepCopier[39;49;00m)]$
  1298^I^I^I^I^I^I[32mifNotNil:[39;49;00m [[31mnew[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m [31msubAss[39;49;00m [32mvalue[39;49;00m].$
  1299^I^I^I^I^I[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]].$
  1300^I^I([31msup[39;49;00m _ [31msup[39;49;00m [32msuperclass[39;49;00m) [32m==[39;49;00m [36mnil[39;49;00m] [32mwhileFalse[39;49;00m.$
  1301^I^I[31mnew[39;49;00m [32mrehash[39;49;00m.^I[37m"force Sets and Dictionaries to rehash"[39;49;00m$
  1302^I^I^ [31mnew[39;49;00m$
  1303^I[34m! ![39;49;00m$
  1304^I$
  1305^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 1/6/1999 17:39'![39;49;00m$
  1306^I[32mveryDeepFixupWith:[39;49;00m [31mdeepCopier[39;49;00m$
  1307^I^I[37m"I have no fields and no superclass.  Catch the super call."[39;49;00m$
  1308^I[34m! ![39;49;00m$
  1309^I$
  1310^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 9/4/2001 10:30'![39;49;00m$
  1311^I[32mveryDeepInner:[39;49;00m [31mdeepCopier[39;49;00m$
  1312^I^I[37m"No special treatment for inst vars of my superclasses.  Override when some need to be weakly copied.  Object>>veryDeepCopyWith: will veryDeepCopy any inst var whose class does not actually define veryDeepInner:"[39;49;00m$
  1313^I[34m! ![39;49;00m$
  1314^I$
  1315^I$
  1316^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'creation'[39;49;00m[34m stamp: 'nk 2/26/2004 13:35'![39;49;00m$
  1317^I[32masStringMorph[39;49;00m$
  1318^I^I[37m"Open a StringMorph, as best one can, on the receiver"[39;49;00m$
  1319^I$
  1320^I^I^ [36mself[39;49;00m [32masStringOrText[39;49;00m [32masStringMorph[39;49;00m$
  1321^I[34m! ![39;49;00m$
  1322^I$
  1323^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'creation'[39;49;00m[34m stamp: 'nk 2/26/2004 13:35'![39;49;00m$
  1324^I[32masTextMorph[39;49;00m$
  1325^I^I[37m"Open a TextMorph, as best one can, on the receiver"[39;49;00m$
  1326^I$
  1327^I^I^ [04m[32mTextMorph[39;49;00m [36mnew[39;49;00m [32mcontentsAsIs:[39;49;00m [36mself[39;49;00m [32masStringOrText[39;49;00m$
  1328^I[34m! ![39;49;00m$
  1329^I$
  1330^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'creation'[39;49;00m[34m stamp: 'sw 1/29/2002 21:45'![39;49;00m$
  1331^I[32mopenAsMorph[39;49;00m$
  1332^I^I[37m"Open a morph, as best one can, on the receiver"[39;49;00m$
  1333^I$
  1334^I^I^ [36mself[39;49;00m [32masMorph[39;49;00m [32mopenInHand[39;49;00m$
  1335^I$
  1336^I[37m"[39;49;00m$
  1337^I[37m234 openAsMorph[39;49;00m$
  1338^I[37m(ScriptingSystem formAtKey: #TinyMenu) openAsMorph[39;49;00m$
  1339^I[37m'fred' openAsMorph[39;49;00m$
  1340^I[37m"[39;49;00m[34m! ![39;49;00m$
  1341^I$
  1342^I$
  1343^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging'[39;49;00m[34m stamp: 'md 11/24/2004 11:45'![39;49;00m$
  1344^I[32mhaltIf:[39;49;00m [31mcondition[39;49;00m$
  1345^I^I[37m"This is the typical message to use for inserting breakpoints during [39;49;00m$
  1346^I[37m^Idebugging.  Param can be a block or expression, halt if true.[39;49;00m$
  1347^I[37m^IIf the Block has one arg, the receiver is bound to that.[39;49;00m$
  1348^I[37m ^IIf the condition is a selector, we look up in the callchain. Halt if[39;49;00m$
  1349^I[37m      any method's selector equals selector."[39;49;00m$
  1350^I^I|[31m cntxt [39;49;00m|$
  1351^I$
  1352^I^I[31mcondition[39;49;00m [32misSymbol[39;49;00m [36mifTrue:[39;49;00m[$
  1353^I^I^I[37m"only halt if a method with selector symbol is in callchain"[39;49;00m$
  1354^I^I^I[31mcntxt[39;49;00m := [36mthisContext[39;49;00m.$
  1355^I^I^I[[31mcntxt[39;49;00m [32msender[39;49;00m [32misNil[39;49;00m] [36mwhileFalse:[39;49;00m [$
  1356^I^I^I^I[31mcntxt[39;49;00m := [31mcntxt[39;49;00m [32msender[39;49;00m. $
  1357^I^I^I^I([31mcntxt[39;49;00m [32mselector[39;49;00m [32m=[39;49;00m [31mcondition[39;49;00m) [36mifTrue:[39;49;00m [[04m[32mHalt[39;49;00m [32msignal[39;49;00m].$
  1358^I^I^I^I].$
  1359^I^I^I^[36mself[39;49;00m.$
  1360^I^I].$
  1361^I^I([31mcondition[39;49;00m [32misBlock[39;49;00m $
  1362^I^I^I^I[36mifTrue:[39;49;00m [[31mcondition[39;49;00m [32mvalueWithPossibleArgument:[39;49;00m [36mself[39;49;00m] $
  1363^I^I^I^I[36mifFalse:[39;49;00m [[31mcondition[39;49;00m] $
  1364^I^I) [36mifTrue:[39;49;00m [$
  1365^I^I^I[04m[32mHalt[39;49;00m [32msignal[39;49;00m$
  1366^I^I].[34m! ![39;49;00m$
  1367^I$
  1368^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging'[39;49;00m[34m![39;49;00m$
  1369^I[31mneedsWork[39;49;00m[34m! ![39;49;00m$
  1370^I$
  1371^I$
  1372^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:26'![39;49;00m$
  1373^I[32mcheckHaltCountExpired[39;49;00m$
  1374^I^I|[31m counter [39;49;00m|$
  1375^I^I[31mcounter[39;49;00m _ [04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#HaltCount[39;49;00m [32mifAbsent:[39;49;00m [[34m0[39;49;00m].$
  1376^I^I^[31mcounter[39;49;00m [32m=[39;49;00m [34m0[39;49;00m[34m! ![39;49;00m$
  1377^I$
  1378^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:04'![39;49;00m$
  1379^I[32mclearHaltOnce[39;49;00m$
  1380^I^I[37m"Turn on the halt once flag."[39;49;00m$
  1381^I^I[04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#HaltOnce[39;49;00m [32mput:[39;49;00m [36mfalse[39;49;00m[34m! ![39;49;00m$
  1382^I$
  1383^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:30'![39;49;00m$
  1384^I[32mdecrementAndCheckHaltCount[39;49;00m$
  1385^I^I[36mself[39;49;00m [32mdecrementHaltCount[39;49;00m.$
  1386^I^I^[36mself[39;49;00m [32mcheckHaltCountExpired[39;49;00m[34m! ![39;49;00m$
  1387^I$
  1388^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:28'![39;49;00m$
  1389^I[32mdecrementHaltCount[39;49;00m$
  1390^I^I|[31m counter [39;49;00m|$
  1391^I^I[31mcounter[39;49;00m := [04m[32mSmalltalk[39;49;00m$
  1392^I^I^I^I^I[32mat:[39;49;00m [33m#HaltCount[39;49;00m$
  1393^I^I^I^I^I[32mifAbsent:[39;49;00m [[34m0[39;49;00m].$
  1394^I^I[31mcounter[39;49;00m [32m>[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m [$
  1395^I^I^I[31mcounter[39;49;00m _ [31mcounter[39;49;00m [32m-[39;49;00m [34m1[39;49;00m.$
  1396^I^I^I[36mself[39;49;00m [32msetHaltCountTo:[39;49;00m [31mcounter[39;49;00m][34m! ![39;49;00m$
  1397^I$
  1398^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:42'![39;49;00m$
  1399^I[32mdoExpiredHaltCount[39;49;00m$
  1400^I^I[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
  1401^I^I[36mself[39;49;00m [32mremoveHaltCount[39;49;00m.$
  1402^I^I[36mself[39;49;00m [32mhalt[39;49;00m[34m! ![39;49;00m$
  1403^I$
  1404^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:44'![39;49;00m$
  1405^I[32mdoExpiredHaltCount:[39;49;00m [31maString[39;49;00m$
  1406^I^I[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
  1407^I^I[36mself[39;49;00m [32mremoveHaltCount[39;49;00m.$
  1408^I^I[36mself[39;49;00m [32mhalt:[39;49;00m [31maString[39;49;00m[34m! ![39;49;00m$
  1409^I$
  1410^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:45'![39;49;00m$
  1411^I[32mdoExpiredInspectCount[39;49;00m$
  1412^I^I[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
  1413^I^I[36mself[39;49;00m [32mremoveHaltCount[39;49;00m.$
  1414^I^I[36mself[39;49;00m [32minspect[39;49;00m[34m! ![39;49;00m$
  1415^I$
  1416^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:43'![39;49;00m$
  1417^I[32mhaltOnCount:[39;49;00m [31mint[39;49;00m $
  1418^I^I[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
  1419^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mhasHaltCount[39;49;00m$
  1420^I^I^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdecrementAndCheckHaltCount[39;49;00m$
  1421^I^I^I^I^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredHaltCount[39;49;00m]]$
  1422^I^I^I^I^I[36mifFalse:[39;49;00m [[31mint[39;49;00m [32m=[39;49;00m [34m1[39;49;00m$
  1423^I^I^I^I^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredHaltCount[39;49;00m]$
  1424^I^I^I^I^I^I^I[36mifFalse:[39;49;00m [[36mself[39;49;00m [32msetHaltCountTo:[39;49;00m [31mint[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]][34m! ![39;49;00m$
  1425^I$
  1426^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:05'![39;49;00m$
  1427^I[32mhaltOnce[39;49;00m$
  1428^I^I[37m"Halt unless we have already done it once."[39;49;00m$
  1429^I^I[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
  1430^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
  1431^I^I^I^I^ [36mself[39;49;00m [32mhalt[39;49;00m][34m! ![39;49;00m$
  1432^I$
  1433^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:04'![39;49;00m$
  1434^I[32mhaltOnceEnabled[39;49;00m$
  1435^I^I^ [04m[32mSmalltalk[39;49;00m$
  1436^I^I^I[32mat:[39;49;00m [33m#HaltOnce[39;49;00m$
  1437^I^I^I[32mifAbsent:[39;49;00m [[36mfalse[39;49;00m][34m! ![39;49;00m$
  1438^I$
  1439^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:05'![39;49;00m$
  1440^I[32mhaltOnce:[39;49;00m [31maString[39;49;00m $
  1441^I^I[37m"Halt unless we have already done it once."[39;49;00m$
  1442^I^I[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
  1443^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
  1444^I^I^I^I^ [36mself[39;49;00m [32mhalt:[39;49;00m [31maString[39;49;00m][34m! ![39;49;00m$
  1445^I$
  1446^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:45'![39;49;00m$
  1447^I[32mhalt:[39;49;00m [31maString[39;49;00m [32monCount:[39;49;00m [31mint[39;49;00m $
  1448^I^I[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
  1449^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mhasHaltCount[39;49;00m$
  1450^I^I^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdecrementAndCheckHaltCount[39;49;00m$
  1451^I^I^I^I^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredHaltCount:[39;49;00m [31maString[39;49;00m]]$
  1452^I^I^I^I^I[36mifFalse:[39;49;00m [[31mint[39;49;00m [32m=[39;49;00m [34m1[39;49;00m$
  1453^I^I^I^I^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredHaltCount:[39;49;00m [31maString[39;49;00m]$
  1454^I^I^I^I^I^I^I[36mifFalse:[39;49;00m [[36mself[39;49;00m [32msetHaltCountTo:[39;49;00m [31mint[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]][34m! ![39;49;00m$
  1455^I$
  1456^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:36'![39;49;00m$
  1457^I[32mhasHaltCount[39;49;00m$
  1458^I^I^[04m[32mSmalltalk[39;49;00m$
  1459^I^I^I^I^I[32mincludesKey:[39;49;00m [33m#HaltCount[39;49;00m[34m! ![39;49;00m$
  1460^I$
  1461^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:46'![39;49;00m$
  1462^I[32minspectOnCount:[39;49;00m [31mint[39;49;00m $
  1463^I^I[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
  1464^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mhasHaltCount[39;49;00m$
  1465^I^I^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdecrementAndCheckHaltCount[39;49;00m$
  1466^I^I^I^I^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredInspectCount[39;49;00m]]$
  1467^I^I^I^I^I[36mifFalse:[39;49;00m [[31mint[39;49;00m [32m=[39;49;00m [34m1[39;49;00m$
  1468^I^I^I^I^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredInspectCount[39;49;00m]$
  1469^I^I^I^I^I^I^I[36mifFalse:[39;49;00m [[36mself[39;49;00m [32msetHaltCountTo:[39;49;00m [31mint[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]][34m! ![39;49;00m$
  1470^I$
  1471^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:05'![39;49;00m$
  1472^I[32minspectOnce[39;49;00m$
  1473^I^I[37m"Inspect unless we have already done it once."[39;49;00m$
  1474^I^I[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
  1475^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
  1476^I^I^I^I^ [36mself[39;49;00m [32minspect[39;49;00m][34m! ![39;49;00m$
  1477^I$
  1478^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 13:20'![39;49;00m$
  1479^I[32minspectUntilCount:[39;49;00m [31mint[39;49;00m $
  1480^I^I[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
  1481^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mhasHaltCount[39;49;00m$
  1482^I^I^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdecrementAndCheckHaltCount[39;49;00m$
  1483^I^I^I^I^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredInspectCount[39;49;00m]$
  1484^I^I^I^I^I^I^I[36mifFalse:[39;49;00m [[36mself[39;49;00m [32minspect[39;49;00m]]$
  1485^I^I^I^I^I[36mifFalse:[39;49;00m [[31mint[39;49;00m [32m=[39;49;00m [34m1[39;49;00m$
  1486^I^I^I^I^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredInspectCount[39;49;00m]$
  1487^I^I^I^I^I^I^I[36mifFalse:[39;49;00m [[36mself[39;49;00m [32msetHaltCountTo:[39;49;00m [31mint[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]][34m! ![39;49;00m$
  1488^I$
  1489^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:49'![39;49;00m$
  1490^I[32mremoveHaltCount[39;49;00m$
  1491^I^I([04m[32mSmalltalk[39;49;00m [32mincludesKey:[39;49;00m [33m#HaltCount[39;49;00m) [36mifTrue:[39;49;00m [$
  1492^I^I^I[04m[32mSmalltalk[39;49;00m [32mremoveKey:[39;49;00m [33m#HaltCount[39;49;00m][34m! ![39;49;00m$
  1493^I$
  1494^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:25'![39;49;00m$
  1495^I[32msetHaltCountTo:[39;49;00m [31mint[39;49;00m$
  1496^I^I[04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#HaltCount[39;49;00m [32mput:[39;49;00m [31mint[39;49;00m[34m! ![39;49;00m$
  1497^I$
  1498^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:04'![39;49;00m$
  1499^I[32msetHaltOnce[39;49;00m$
  1500^I^I[37m"Turn on the halt once flag."[39;49;00m$
  1501^I^I[04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#HaltOnce[39;49;00m [32mput:[39;49;00m [36mtrue[39;49;00m[34m! ![39;49;00m$
  1502^I$
  1503^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:04'![39;49;00m$
  1504^I[32mtoggleHaltOnce[39;49;00m$
  1505^I^I[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
  1506^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mclearHaltOnce[39;49;00m]$
  1507^I^I^I[36mifFalse:[39;49;00m [[36mself[39;49;00m [32msetHaltOnce[39;49;00m][34m! ![39;49;00m$
  1508^I$
  1509^I$
  1510^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'ar 2/11/2001 01:55'![39;49;00m$
  1511^I[32maddDependent:[39;49;00m [31manObject[39;49;00m$
  1512^I^I[37m"Make the given object one of the receiver's dependents."[39;49;00m$
  1513^I$
  1514^I^I|[31m dependents [39;49;00m|$
  1515^I^I[31mdependents[39;49;00m _ [36mself[39;49;00m [32mdependents[39;49;00m.$
  1516^I^I([31mdependents[39;49;00m [32mincludes:[39;49;00m [31manObject[39;49;00m) [36mifFalse:[39;49;00m$
  1517^I^I^I[[36mself[39;49;00m [32mmyDependents:[39;49;00m ([31mdependents[39;49;00m [32mcopyWithDependent:[39;49;00m [31manObject[39;49;00m)].$
  1518^I^I^ [31manObject[39;49;00m[34m! ![39;49;00m$
  1519^I$
  1520^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:53'![39;49;00m$
  1521^I[32mbreakDependents[39;49;00m$
  1522^I^I[37m"Remove all of the receiver's dependents."[39;49;00m$
  1523^I$
  1524^I^I[36mself[39;49;00m [32mmyDependents:[39;49;00m [36mnil[39;49;00m[34m! ![39;49;00m$
  1525^I$
  1526^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:26'![39;49;00m$
  1527^I[32mcanDiscardEdits[39;49;00m$
  1528^I^I[37m"Answer true if none of the views on this model has unaccepted edits that matter."[39;49;00m$
  1529^I$
  1530^I^I[36mself[39;49;00m [32mdependents[39;49;00m$
  1531^I^I^I[32mdo:[39;49;00m [:[31meach[39;49;00m | [31meach[39;49;00m [32mcanDiscardEdits[39;49;00m [36mifFalse:[39;49;00m [^ [36mfalse[39;49;00m]]$
  1532^I^I^I[32mwithout:[39;49;00m [36mself[39;49;00m.$
  1533^I^I^ [36mtrue[39;49;00m[34m! ![39;49;00m$
  1534^I$
  1535^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:58'![39;49;00m$
  1536^I[32mdependents[39;49;00m$
  1537^I^I[37m"Answer a collection of objects that are 'dependent' on the receiver;[39;49;00m$
  1538^I[37m^I that is, all objects that should be notified if the receiver changes."[39;49;00m$
  1539^I$
  1540^I^I^ [36mself[39;49;00m [32mmyDependents[39;49;00m [32mifNil:[39;49;00m [[33m#([39;49;00m[33m)[39;49;00m][34m! ![39;49;00m$
  1541^I$
  1542^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m![39;49;00m$
  1543^I[32mevaluate:[39;49;00m [31mactionBlock[39;49;00m [32mwheneverChangeIn:[39;49;00m [31maspectBlock[39;49;00m$
  1544^I^I|[31m viewerThenObject objectThenViewer [39;49;00m|$
  1545^I^I[31mobjectThenViewer[39;49;00m _ [36mself[39;49;00m.$
  1546^I^I[31mviewerThenObject[39;49;00m _ [04m[32mObjectViewer[39;49;00m [32mon:[39;49;00m [31mobjectThenViewer[39;49;00m.$
  1547^I^I[31mobjectThenViewer[39;49;00m [32mbecome:[39;49;00m [31mviewerThenObject[39;49;00m.$
  1548^I^I[37m"--- Then ---"[39;49;00m$
  1549^I^I[31mobjectThenViewer[39;49;00m [32mxxxViewedObject:[39;49;00m [31mviewerThenObject[39;49;00m$
  1550^I^I^I^I[32mevaluate:[39;49;00m [31mactionBlock[39;49;00m$
  1551^I^I^I^I[32mwheneverChangeIn:[39;49;00m [31maspectBlock[39;49;00m[34m! ![39;49;00m$
  1552^I$
  1553^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:59'![39;49;00m$
  1554^I[32mhasUnacceptedEdits[39;49;00m$
  1555^I^I[37m"Answer true if any of the views on this object has unaccepted edits."[39;49;00m$
  1556^I$
  1557^I^I[36mself[39;49;00m [32mdependents[39;49;00m$
  1558^I^I^I[32mdo:[39;49;00m [:[31meach[39;49;00m | [31meach[39;49;00m [32mhasUnacceptedEdits[39;49;00m [36mifTrue:[39;49;00m [^ [36mtrue[39;49;00m]]$
  1559^I^I^I[32mwithout:[39;49;00m [36mself[39;49;00m.$
  1560^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  1561^I$
  1562^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:55'![39;49;00m$
  1563^I[32mmyDependents[39;49;00m$
  1564^I^I[37m"Private. Answer a list of all the receiver's dependents."[39;49;00m$
  1565^I$
  1566^I^I^ [04m[32mDependentsFields[39;49;00m [32mat:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m [][34m! ![39;49;00m$
  1567^I$
  1568^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:52'![39;49;00m$
  1569^I[32mmyDependents:[39;49;00m [31maCollectionOrNil[39;49;00m$
  1570^I^I[37m"Private. Set (or remove) the receiver's dependents list."[39;49;00m$
  1571^I$
  1572^I^I[31maCollectionOrNil[39;49;00m$
  1573^I^I^I[32mifNil:[39;49;00m [[04m[32mDependentsFields[39;49;00m [32mremoveKey:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m []]$
  1574^I^I^I[32mifNotNil:[39;49;00m [[04m[32mDependentsFields[39;49;00m [32mat:[39;49;00m [36mself[39;49;00m [32mput:[39;49;00m [31maCollectionOrNil[39;49;00m][34m! ![39;49;00m$
  1575^I$
  1576^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'reThink 2/18/2001 17:06'![39;49;00m$
  1577^I[32mrelease[39;49;00m$
  1578^I^I[37m"Remove references to objects that may refer to the receiver. This message [39;49;00m$
  1579^I[37m^Ishould be overridden by subclasses with any cycles, in which case the [39;49;00m$
  1580^I[37m^Isubclass should also include the expression super release."[39;49;00m$
  1581^I$
  1582^I^I[36mself[39;49;00m [32mreleaseActionMap[39;49;00m[34m! ![39;49;00m$
  1583^I$
  1584^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 20:23'![39;49;00m$
  1585^I[32mremoveDependent:[39;49;00m [31manObject[39;49;00m$
  1586^I^I[37m"Remove the given object as one of the receiver's dependents."[39;49;00m$
  1587^I$
  1588^I^I|[31m dependents [39;49;00m|$
  1589^I^I[31mdependents[39;49;00m _ [36mself[39;49;00m [32mdependents[39;49;00m [32mreject:[39;49;00m [:[31meach[39;49;00m | [31meach[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m].$
  1590^I^I[36mself[39;49;00m [32mmyDependents:[39;49;00m ([31mdependents[39;49;00m [32misEmpty[39;49;00m [36mifFalse:[39;49;00m [[31mdependents[39;49;00m]).$
  1591^I^I^ [31manObject[39;49;00m[34m! ![39;49;00m$
  1592^I$
  1593^I$
  1594^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'bh 9/16/2001 18:10'![39;49;00m$
  1595^I[32macceptDroppingMorph:[39;49;00m [31mtransferMorph[39;49;00m [32mevent:[39;49;00m [31mevt[39;49;00m [32minMorph:[39;49;00m [31mdstListMorph[39;49;00m $
  1596^I^I$
  1597^I^I^[36mfalse[39;49;00m.[34m! ![39;49;00m$
  1598^I$
  1599^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'mir 5/16/2000 11:35'![39;49;00m$
  1600^I[32mdragAnimationFor:[39;49;00m [31mitem[39;49;00m [32mtransferMorph:[39;49;00m [31mtransferMorph[39;49;00m $
  1601^I^I[37m"Default do nothing"[39;49;00m[34m! ![39;49;00m$
  1602^I$
  1603^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'panda 4/28/2000 16:20'![39;49;00m$
  1604^I[32mdragPassengerFor:[39;49;00m [31mitem[39;49;00m [32minMorph:[39;49;00m [31mdragSource[39;49;00m $
  1605^I^I^[31mitem[39;49;00m[34m! ![39;49;00m$
  1606^I$
  1607^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'panda 4/28/2000 16:11'![39;49;00m$
  1608^I[32mdragTransferType[39;49;00m$
  1609^I^I^[36mnil[39;49;00m[34m! ![39;49;00m$
  1610^I$
  1611^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'panda 4/28/2000 16:05'![39;49;00m$
  1612^I[32mdragTransferTypeForMorph:[39;49;00m [31mdragSource[39;49;00m $
  1613^I^I^[36mnil[39;49;00m[34m! ![39;49;00m$
  1614^I$
  1615^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'mir 5/8/2000 17:19'![39;49;00m$
  1616^I[32mwantsDroppedMorph:[39;49;00m [31maMorph[39;49;00m [32mevent:[39;49;00m [31manEvent[39;49;00m [32minMorph:[39;49;00m [31mdestinationLM[39;49;00m $
  1617^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
  1618^I$
  1619^I$
  1620^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'sma 5/6/2000 19:35'![39;49;00m$
  1621^I[32massert:[39;49;00m [31maBlock[39;49;00m$
  1622^I^I[37m"Throw an assertion error if aBlock does not evaluates to true."[39;49;00m$
  1623^I$
  1624^I^I[31maBlock[39;49;00m [32mvalue[39;49;00m [36mifFalse:[39;49;00m [[04m[32mAssertionFailure[39;49;00m [32msignal:[39;49;00m [33m'Assertion failed'[39;49;00m][34m! ![39;49;00m$
  1625^I$
  1626^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'nk 1/15/2004 10:54'![39;49;00m$
  1627^I[32massert:[39;49;00m [31maBlock[39;49;00m [32mdescriptionBlock:[39;49;00m [31mdescriptionBlock[39;49;00m$
  1628^I^I[37m"Throw an assertion error if aBlock does not evaluate to true."[39;49;00m$
  1629^I$
  1630^I^I[31maBlock[39;49;00m [32mvalue[39;49;00m [36mifFalse:[39;49;00m [[04m[32mAssertionFailure[39;49;00m [32msignal:[39;49;00m [31mdescriptionBlock[39;49;00m [32mvalue[39;49;00m [32masString[39;49;00m ][34m! ![39;49;00m$
  1631^I$
  1632^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'nk 10/25/2003 16:47'![39;49;00m$
  1633^I[32massert:[39;49;00m [31maBlock[39;49;00m [32mdescription:[39;49;00m [31maString[39;49;00m$
  1634^I^I[37m"Throw an assertion error if aBlock does not evaluates to true."[39;49;00m$
  1635^I$
  1636^I^I[31maBlock[39;49;00m [32mvalue[39;49;00m [36mifFalse:[39;49;00m [[04m[32mAssertionFailure[39;49;00m [32msignal:[39;49;00m [31maString[39;49;00m ][34m! ![39;49;00m$
  1637^I$
  1638^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'md 10/13/2004 15:59'![39;49;00m$
  1639^I[32mbackwardCompatibilityOnly:[39;49;00m [31manExplanationString[39;49;00m$
  1640^I^I[37m"Warn that the sending method has been deprecated. Methods that are tagt with #backwardCompatibility:[39;49;00m$
  1641^I[37m^I are kept for compatibility."[39;49;00m$
  1642^I$
  1643^I^I[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
  1644^I^I^I[[04m[32mDeprecation[39;49;00m [32msignal:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m' has been deprecated (but will be kept for compatibility). '[39;49;00m[32m,[39;49;00m [31manExplanationString[39;49;00m][34m! ![39;49;00m$
  1645^I$
  1646^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m![39;49;00m$
  1647^I[32mcaseError[39;49;00m$
  1648^I^I[37m"Report an error from an in-line or explicit case statement."[39;49;00m$
  1649^I$
  1650^I^I[36mself[39;49;00m [32merror:[39;49;00m [33m'Case not found, and no otherwise clause'[39;49;00m[34m! ![39;49;00m$
  1651^I$
  1652^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'rbb 3/1/2005 09:26'![39;49;00m$
  1653^I[32mconfirm:[39;49;00m [31mqueryString[39;49;00m$
  1654^I^I[37m"Put up a yes/no menu with caption queryString. Answer true if the [39;49;00m$
  1655^I[37m^Iresponse is yes, false if no. This is a modal question--the user must [39;49;00m$
  1656^I[37m^Irespond yes or no."[39;49;00m$
  1657^I$
  1658^I^I[37m"nil confirm: 'Are you hungry?'"[39;49;00m$
  1659^I$
  1660^I^I^ [04m[32mUIManager[39;49;00m [32mdefault[39;49;00m [32mconfirm:[39;49;00m [31mqueryString[39;49;00m[34m! ![39;49;00m$
  1661^I$
  1662^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'rbb 3/1/2005 09:27'![39;49;00m$
  1663^I[32mconfirm:[39;49;00m [31maString[39;49;00m [32morCancel:[39;49;00m [31mcancelBlock[39;49;00m$
  1664^I^I[37m"Put up a yes/no/cancel menu with caption aString. Answer true if  [39;49;00m$
  1665^I[37m^Ithe response is yes, false if no. If cancel is chosen, evaluate  [39;49;00m$
  1666^I[37m^IcancelBlock. This is a modal question--the user must respond yes or no."[39;49;00m$
  1667^I$
  1668^I^I^ [04m[32mUIManager[39;49;00m [32mdefault[39;49;00m [32mconfirm:[39;49;00m [31maString[39;49;00m [32morCancel:[39;49;00m [31mcancelBlock[39;49;00m[34m! ![39;49;00m$
  1669^I$
  1670^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'dew 10/6/2003 18:20'![39;49;00m$
  1671^I[32mdeprecated:[39;49;00m [31manExplanationString[39;49;00m$
  1672^I^I[37m"Warn that the sending method has been deprecated."[39;49;00m$
  1673^I$
  1674^I^I[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
  1675^I^I^I[[04m[32mDeprecation[39;49;00m [32msignal:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m' has been deprecated. '[39;49;00m[32m,[39;49;00m [31manExplanationString[39;49;00m][34m! ![39;49;00m$
  1676^I$
  1677^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'dew 10/7/2003 00:26'![39;49;00m$
  1678^I[32mdeprecated:[39;49;00m [31manExplanationString[39;49;00m [32mblock:[39;49;00m [31maBlock[39;49;00m $
  1679^I^I [37m"Warn that the sender has been deprecated.  Answer the value of aBlock on resumption.  (Note that #deprecated: is usually the preferred method.)"[39;49;00m$
  1680^I$
  1681^I^I[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
  1682^I^I^I[[04m[32mDeprecation[39;49;00m$
  1683^I^I^I^I[32msignal:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m' has been deprecated. '[39;49;00m[32m,[39;49;00m [31manExplanationString[39;49;00m].$
  1684^I^I^ [31maBlock[39;49;00m [32mvalue[39;49;00m.$
  1685^I[34m! ![39;49;00m$
  1686^I$
  1687^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'md 2/22/2006 21:21'![39;49;00m$
  1688^I[32mdoesNotUnderstand:[39;49;00m [31maMessage[39;49;00m $
  1689^I^I [37m"Handle the fact that there was an attempt to send the given message to the receiver but the receiver does not understand this message (typically sent from the machine when a message is sent to the receiver and no method is defined for that selector)."[39;49;00m$
  1690^I^I[37m"Testing: (3 activeProcess)"[39;49;00m$
  1691^I$
  1692^I^I[04m[32mMessageNotUnderstood[39;49;00m [36mnew[39;49;00m $
  1693^I^I^I[32mmessage:[39;49;00m [31maMessage[39;49;00m;$
  1694^I^I^I[32mreceiver:[39;49;00m [36mself[39;49;00m;$
  1695^I^I^I[32msignal[39;49;00m.$
  1696^I^I^ [31maMessage[39;49;00m [32msentTo:[39;49;00m [36mself[39;49;00m.$
  1697^I[34m! ![39;49;00m$
  1698^I$
  1699^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'TRee 11/4/2003 16:47'![39;49;00m$
  1700^I[32mdpsTrace:[39;49;00m [31mreportObject[39;49;00m  $
  1701^I^I[04m[32mTranscript[39;49;00m [32mmyDependents[39;49;00m [32misNil[39;49;00m [36mifTrue:[39;49;00m [^[36mself[39;49;00m].$
  1702^I^I[36mself[39;49;00m [32mdpsTrace:[39;49;00m [31mreportObject[39;49;00m [32mlevels:[39;49;00m [34m1[39;49;00m [32mwithContext:[39;49;00m [36mthisContext[39;49;00m$
  1703^I^I^I$
  1704^I[37m" nil dpsTrace: 'sludder'. "[39;49;00m[34m! ![39;49;00m$
  1705^I$
  1706^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'TRee 11/4/2003 16:49'![39;49;00m$
  1707^I[32mdpsTrace:[39;49;00m [31mreportObject[39;49;00m [32mlevels:[39;49;00m [31manInt[39;49;00m$
  1708^I^I[36mself[39;49;00m [32mdpsTrace:[39;49;00m [31mreportObject[39;49;00m [32mlevels:[39;49;00m [31manInt[39;49;00m [32mwithContext:[39;49;00m [36mthisContext[39;49;00m$
  1709^I$
  1710^I[37m"(1 to: 3) do: [:int | nil dpsTrace: int levels: 5.]"[39;49;00m[34m! ![39;49;00m$
  1711^I$
  1712^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'TRee 11/4/2003 17:02'![39;49;00m$
  1713^I[32mdpsTrace:[39;49;00m [31mreportObject[39;49;00m [32mlevels:[39;49;00m [31manInt[39;49;00m [32mwithContext:[39;49;00m [31mcurrentContext[39;49;00m$
  1714^I^I|[31m reportString context displayCount [39;49;00m|$
  1715^I^I[31mreportString[39;49;00m := ([31mreportObject[39;49;00m [32mrespondsTo:[39;49;00m [33m#asString[39;49;00m) $
  1716^I^I^I^I[36mifTrue:[39;49;00m [[31mreportObject[39;49;00m [32masString[39;49;00m] [36mifFalse:[39;49;00m [[31mreportObject[39;49;00m [32mprintString[39;49;00m].$
  1717^I^I([04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#Decompiler[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m]) $
  1718^I^I[32mifNil:[39;49;00m $
  1719^I^I^I[[04m[32mTranscript[39;49;00m [32mcr[39;49;00m; [32mshow:[39;49;00m [31mreportString[39;49;00m]$
  1720^I^I[32mifNotNil:[39;49;00m$
  1721^I^I^I[[31mcontext[39;49;00m := [31mcurrentContext[39;49;00m.$
  1722^I^I^I[31mdisplayCount[39;49;00m := [31manInt[39;49;00m [32m>[39;49;00m [34m1[39;49;00m.$
  1723^I^I^I[34m1[39;49;00m [32mto:[39;49;00m [31manInt[39;49;00m [32mdo:[39;49;00m$
  1724^I^I^I^I[:[31mcount[39;49;00m |$
  1725^I^I^I^I[04m[32mTranscript[39;49;00m [32mcr[39;49;00m.$
  1726^I^I^I^I[31mdisplayCount[39;49;00m$
  1727^I^I^I^I^I[36mifTrue:[39;49;00m [[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m [31mcount[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m': '[39;49;00m].$
  1728^I^I^I^I$
  1729^I^I^I^I[31mreportString[39;49;00m [32mnotNil[39;49;00m$
  1730^I^I^I^I[36mifTrue:[39;49;00m$
  1731^I^I^I^I^I[[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m [31mcontext[39;49;00m [32mhome[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m $
  1732^I^I^I^I[32m,[39;49;00m [33m'/'[39;49;00m [32m,[39;49;00m [31mcontext[39;49;00m [32msender[39;49;00m [32mselector[39;49;00m[32m,[39;49;00m  [33m' ('[39;49;00m [32m,[39;49;00m [31mreportString[39;49;00m [32m,[39;49;00m [33m')'[39;49;00m.$
  1733^I^I^I^I^I[31mcontext[39;49;00m := [31mcontext[39;49;00m [32msender[39;49;00m.$
  1734^I^I^I^I^I[31mreportString[39;49;00m := [36mnil[39;49;00m]$
  1735^I^I^I^I[36mifFalse:[39;49;00m$
  1736^I^I^I^I^I[([31mcontext[39;49;00m [32mnotNil[39;49;00m [32mand:[39;49;00m [([31mcontext[39;49;00m := [31mcontext[39;49;00m [32msender[39;49;00m) [32mnotNil[39;49;00m])$
  1737^I^I^I^I^I[36mifTrue:[39;49;00m [[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m [31mcontext[39;49;00m [32mreceiver[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32m,[39;49;00m [33m'/'[39;49;00m [32m,[39;49;00m [31mcontext[39;49;00m [32mselector[39;49;00m]]].$
  1738^I^I^I[37m"Transcript cr"[39;49;00m].[34m! ![39;49;00m$
  1739^I$
  1740^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'md 8/2/2005 22:17'![39;49;00m$
  1741^I[32merror[39;49;00m$
  1742^I^I[37m"Throw a generic Error exception."[39;49;00m$
  1743^I$
  1744^I^I^[36mself[39;49;00m [32merror:[39;49;00m [33m'Error!!'[39;49;00m.[34m! ![39;49;00m$
  1745^I$
  1746^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'tfei 4/12/1999 12:55'![39;49;00m$
  1747^I[32merror:[39;49;00m [31maString[39;49;00m $
  1748^I^I[37m"Throw a generic Error exception."[39;49;00m$
  1749^I$
  1750^I^I^[04m[32mError[39;49;00m [36mnew[39;49;00m [32msignal:[39;49;00m [31maString[39;49;00m[34m! ![39;49;00m$
  1751^I$
  1752^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'al 9/16/2005 14:12'![39;49;00m$
  1753^I[32mexplicitRequirement[39;49;00m$
  1754^I^I[36mself[39;49;00m [32merror:[39;49;00m [33m'Explicitly required method'[39;49;00m[34m! ![39;49;00m$
  1755^I$
  1756^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'al 2/13/2006 22:20'![39;49;00m$
  1757^I[32mhalt[39;49;00m$
  1758^I^I[37m"This is the typical message to use for inserting breakpoints during [39;49;00m$
  1759^I[37m^Idebugging. It behaves like halt:, but does not call on halt: in order to [39;49;00m$
  1760^I[37m^Iavoid putting this message on the stack. Halt is especially useful when [39;49;00m$
  1761^I[37m^Ithe breakpoint message is an arbitrary one."[39;49;00m$
  1762^I$
  1763^I^I[04m[32mHalt[39;49;00m [32msignal[39;49;00m[34m! ![39;49;00m$
  1764^I$
  1765^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'tfei 4/12/1999 12:59'![39;49;00m$
  1766^I[32mhalt:[39;49;00m [31maString[39;49;00m $
  1767^I^I[37m"This is the typical message to use for inserting breakpoints during [39;49;00m$
  1768^I[37m^Idebugging. It creates and schedules a Notifier with the argument, [39;49;00m$
  1769^I[37m^IaString, as the label."[39;49;00m$
  1770^I^I$
  1771^I^I[04m[32mHalt[39;49;00m [36mnew[39;49;00m [32msignal:[39;49;00m [31maString[39;49;00m[34m! ![39;49;00m$
  1772^I$
  1773^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:24'![39;49;00m$
  1774^I[32mhandles:[39;49;00m [31mexception[39;49;00m$
  1775^I^I[37m"This method exists in case a non exception class is the first arg in an on:do: (for instance using a exception class that is not loaded). We prefer this to raising an error during error handling itself. Also, semantically it makes sense that the exception handler is not active if its exception class is not loaded"[39;49;00m$
  1776^I$
  1777^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  1778^I$
  1779^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'ar 9/27/2005 20:24'![39;49;00m$
  1780^I[32mnotifyWithLabel:[39;49;00m [31maString[39;49;00m $
  1781^I^I[37m"Create and schedule a Notifier with aString as the window label as well as the contents of the window, in  order to request confirmation before a process can proceed."[39;49;00m$
  1782^I$
  1783^I^I[04m[32mToolSet[39;49;00m$
  1784^I^I^I[32mdebugContext:[39;49;00m [36mthisContext[39;49;00m$
  1785^I^I^I[32mlabel:[39;49;00m [31maString[39;49;00m$
  1786^I^I^I[32mcontents:[39;49;00m [31maString[39;49;00m$
  1787^I$
  1788^I^I[37m"nil notifyWithLabel: 'let us see if this works'"[39;49;00m[34m! ![39;49;00m$
  1789^I$
  1790^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'hg 10/2/2001 20:49'![39;49;00m$
  1791^I[32mnotify:[39;49;00m [31maString[39;49;00m $
  1792^I^I[37m"Create and schedule a Notifier with the argument as the message in [39;49;00m$
  1793^I[37m^Iorder to request confirmation before a process can proceed."[39;49;00m$
  1794^I$
  1795^I^I[04m[32mWarning[39;49;00m [32msignal:[39;49;00m [31maString[39;49;00m$
  1796^I$
  1797^I^I[37m"nil notify: 'confirmation message'"[39;49;00m[34m! ![39;49;00m$
  1798^I$
  1799^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m![39;49;00m$
  1800^I[32mnotify:[39;49;00m [31maString[39;49;00m [32mat:[39;49;00m [31mlocation[39;49;00m$
  1801^I^I[37m"Create and schedule a Notifier with the argument as the message in [39;49;00m$
  1802^I[37m^Iorder to request confirmation before a process can proceed. Subclasses can[39;49;00m$
  1803^I[37m^Ioverride this and insert an error message at location within aString."[39;49;00m$
  1804^I$
  1805^I^I[36mself[39;49;00m [32mnotify:[39;49;00m [31maString[39;49;00m$
  1806^I$
  1807^I^I[37m"nil notify: 'confirmation message' at: 12"[39;49;00m[34m! ![39;49;00m$
  1808^I$
  1809^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m![39;49;00m$
  1810^I[32mprimitiveFailed[39;49;00m$
  1811^I^I[37m"Announce that a primitive has failed and there is no appropriate [39;49;00m$
  1812^I[37m^ISmalltalk code to run."[39;49;00m$
  1813^I$
  1814^I^I[36mself[39;49;00m [32merror:[39;49;00m [33m'a primitive has failed'[39;49;00m[34m! ![39;49;00m$
  1815^I$
  1816^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'al 9/16/2005 14:12'![39;49;00m$
  1817^I[32mrequirement[39;49;00m$
  1818^I^I[36mself[39;49;00m [32merror:[39;49;00m [33m'Implicitly required method'[39;49;00m[34m! ![39;49;00m$
  1819^I$
  1820^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'AFi 2/8/2003 22:52'![39;49;00m$
  1821^I[32mshouldBeImplemented[39;49;00m$
  1822^I^I[37m"Announce that this message should be implemented"[39;49;00m$
  1823^I$
  1824^I^I[36mself[39;49;00m [32merror:[39;49;00m [33m'This message should be implemented'[39;49;00m[34m! ![39;49;00m$
  1825^I$
  1826^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m![39;49;00m$
  1827^I[32mshouldNotImplement[39;49;00m$
  1828^I^I[37m"Announce that, although the receiver inherits this message, it should [39;49;00m$
  1829^I[37m^Inot implement it."[39;49;00m$
  1830^I$
  1831^I^I[36mself[39;49;00m [32merror:[39;49;00m [33m'This message is not appropriate for this object'[39;49;00m[34m! ![39;49;00m$
  1832^I$
  1833^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'md 2/17/2006 12:02'![39;49;00m$
  1834^I[32msubclassResponsibility[39;49;00m$
  1835^I^I[37m"This message sets up a framework for the behavior of the class' subclasses.[39;49;00m$
  1836^I[37m^IAnnounce that the subclass should have implemented this message."[39;49;00m$
  1837^I$
  1838^I^I[36mself[39;49;00m [32merror:[39;49;00m [33m'My subclass should have overridden '[39;49;00m[32m,[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mselector[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
  1839^I$
  1840^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'al 12/16/2003 16:16'![39;49;00m$
  1841^I[32mtraitConflict[39;49;00m$
  1842^I^I[36mself[39;49;00m [32merror:[39;49;00m [33m'A class or trait does not properly resolve a conflict between multiple traits it uses.'[39;49;00m[34m! ![39;49;00m$
  1843^I$
  1844^I$
  1845^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'evaluating'[39;49;00m[34m stamp: 'reThink 3/12/2001 18:14'![39;49;00m$
  1846^I[32mvalue[39;49;00m$
  1847^I$
  1848^I^I^[36mself[39;49;00m[34m! ![39;49;00m$
  1849^I$
  1850^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'evaluating'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:23'![39;49;00m$
  1851^I[32mvalueWithArguments:[39;49;00m [31maSequenceOfArguments[39;49;00m$
  1852^I$
  1853^I^I^[36mself[39;49;00m[34m! ![39;49;00m$
  1854^I$
  1855^I$
  1856^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events'[39;49;00m[34m stamp: 'nk 8/27/2003 16:23'![39;49;00m$
  1857^I[32mactionsWithReceiver:[39;49;00m [31manObject[39;49;00m [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m$
  1858^I$
  1859^I^I^([36mself[39;49;00m [32mactionSequenceForEvent:[39;49;00m [31manEventSelector[39;49;00m)$
  1860^I                [32mselect:[39;49;00m [:[31manAction[39;49;00m | [31manAction[39;49;00m [32mreceiver[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m ][34m! ![39;49;00m$
  1861^I$
  1862^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events'[39;49;00m[34m stamp: 'nk 8/27/2003 17:45'![39;49;00m$
  1863^I[32mrenameActionsWithReceiver:[39;49;00m [31manObject[39;49;00m [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m [32mtoEvent:[39;49;00m [31mnewEvent[39;49;00m$
  1864^I$
  1865^I^I|[31m oldActions newActions [39;49;00m|$
  1866^I^I[31moldActions[39;49;00m _ [04m[32mSet[39;49;00m [36mnew[39;49;00m.$
  1867^I^I[31mnewActions[39;49;00m _ [04m[32mSet[39;49;00m [36mnew[39;49;00m.$
  1868^I^I([36mself[39;49;00m [32mactionSequenceForEvent:[39;49;00m [31manEventSelector[39;49;00m) [32mdo:[39;49;00m [ :[31maction[39;49;00m |$
  1869^I^I^I[31maction[39;49;00m [32mreceiver[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m$
  1870^I^I^I^I[36mifTrue:[39;49;00m [ [31moldActions[39;49;00m [32madd:[39;49;00m [31manObject[39;49;00m ]$
  1871^I^I^I^I[36mifFalse:[39;49;00m [ [31mnewActions[39;49;00m [32madd:[39;49;00m [31manObject[39;49;00m ]].$
  1872^I^I[36mself[39;49;00m [32msetActionSequence:[39;49;00m ([04m[32mActionSequence[39;49;00m [32mwithAll:[39;49;00m [31mnewActions[39;49;00m) [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m.$
  1873^I^I[31moldActions[39;49;00m [32mdo:[39;49;00m [ :[31mact[39;49;00m | [36mself[39;49;00m [32mwhen:[39;49;00m [31mnewEvent[39;49;00m [32mevaluate:[39;49;00m [31mact[39;49;00m ].[34m! ![39;49;00m$
  1874^I$
  1875^I$
  1876^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'nk 12/20/2002 17:48'![39;49;00m$
  1877^I[32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m$
  1878^I    [37m"Answer the action to be evaluated when <anEventSelector> has been triggered."[39;49;00m$
  1879^I$
  1880^I^I|[31m actions [39;49;00m|$
  1881^I^I[31mactions[39;49;00m := [36mself[39;49;00m [32mactionMap[39;49;00m$
  1882^I^I^I[32mat:[39;49;00m [31manEventSelector[39;49;00m [32masSymbol[39;49;00m$
  1883^I^I^I[32mifAbsent:[39;49;00m [[36mnil[39;49;00m].$
  1884^I^I[31mactions[39;49;00m [32mifNil:[39;49;00m [^[36mnil[39;49;00m].$
  1885^I^I^ [31mactions[39;49;00m [32masMinimalRepresentation[39;49;00m[34m! ![39;49;00m$
  1886^I$
  1887^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'nk 12/20/2002 17:48'![39;49;00m$
  1888^I[32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m$
  1889^I[32mifAbsent:[39;49;00m [31manExceptionBlock[39;49;00m$
  1890^I    [37m"Answer the action to be evaluated when <anEventSelector> has been triggered."[39;49;00m$
  1891^I$
  1892^I^I|[31m actions [39;49;00m|$
  1893^I^I[31mactions[39;49;00m := [36mself[39;49;00m [32mactionMap[39;49;00m$
  1894^I^I^I[32mat:[39;49;00m [31manEventSelector[39;49;00m [32masSymbol[39;49;00m$
  1895^I^I^I[32mifAbsent:[39;49;00m [[36mnil[39;49;00m].$
  1896^I^I[31mactions[39;49;00m [32mifNil:[39;49;00m [^[31manExceptionBlock[39;49;00m [32mvalue[39;49;00m].$
  1897^I^I^ [31mactions[39;49;00m [32masMinimalRepresentation[39;49;00m[34m! ![39;49;00m$
  1898^I$
  1899^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'reThink 2/18/2001 14:43'![39;49;00m$
  1900^I[32mactionMap[39;49;00m$
  1901^I$
  1902^I^I^[04m[32mEventManager[39;49;00m [32mactionMapFor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  1903^I$
  1904^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'rw 4/27/2002 08:35'![39;49;00m$
  1905^I[32mactionSequenceForEvent:[39;49;00m [31manEventSelector[39;49;00m$
  1906^I$
  1907^I    ^([36mself[39;49;00m [32mactionMap[39;49;00m$
  1908^I        [32mat:[39;49;00m [31manEventSelector[39;49;00m [32masSymbol[39;49;00m$
  1909^I        [32mifAbsent:[39;49;00m [^[04m[32mWeakActionSequence[39;49;00m [36mnew[39;49;00m])$
  1910^I            [32masActionSequence[39;49;00m[34m! ![39;49;00m$
  1911^I$
  1912^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'SqR 6/28/2001 13:19'![39;49;00m$
  1913^I[32mactionsDo:[39;49;00m [31maBlock[39;49;00m$
  1914^I$
  1915^I^I[36mself[39;49;00m [32mactionMap[39;49;00m [32mdo:[39;49;00m [31maBlock[39;49;00m[34m! ![39;49;00m$
  1916^I$
  1917^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'rw 2/10/2002 13:05'![39;49;00m$
  1918^I[32mcreateActionMap[39;49;00m$
  1919^I$
  1920^I^I^[04m[32mIdentityDictionary[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
  1921^I$
  1922^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'SqR 2/19/2001 14:04'![39;49;00m$
  1923^I[32mhasActionForEvent:[39;49;00m [31manEventSelector[39;49;00m$
  1924^I    [37m"Answer true if there is an action associated with anEventSelector"[39;49;00m$
  1925^I$
  1926^I    ^([36mself[39;49;00m [32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m) [32mnotNil[39;49;00m[34m! ![39;49;00m$
  1927^I$
  1928^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:29'![39;49;00m$
  1929^I[32msetActionSequence:[39;49;00m [31mactionSequence[39;49;00m$
  1930^I[32mforEvent:[39;49;00m [31manEventSelector[39;49;00m$
  1931^I$
  1932^I    |[31m action [39;49;00m|$
  1933^I    [31maction[39;49;00m := [31mactionSequence[39;49;00m [32masMinimalRepresentation[39;49;00m.$
  1934^I    [31maction[39;49;00m [32m==[39;49;00m [36mnil[39;49;00m$
  1935^I        [36mifTrue:[39;49;00m$
  1936^I            [[36mself[39;49;00m [32mremoveActionsForEvent:[39;49;00m [31manEventSelector[39;49;00m]$
  1937^I        [36mifFalse:[39;49;00m$
  1938^I            [[36mself[39;49;00m [32mupdateableActionMap[39;49;00m$
  1939^I                [32mat:[39;49;00m [31manEventSelector[39;49;00m [32masSymbol[39;49;00m$
  1940^I                [32mput:[39;49;00m [31maction[39;49;00m][34m! ![39;49;00m$
  1941^I$
  1942^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'reThink 2/25/2001 08:50'![39;49;00m$
  1943^I[32mupdateableActionMap[39;49;00m$
  1944^I$
  1945^I^I^[04m[32mEventManager[39;49;00m [32mupdateableActionMapFor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  1946^I$
  1947^I$
  1948^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-registering'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:04'![39;49;00m$
  1949^I[32mwhen:[39;49;00m [31manEventSelector[39;49;00m [32mevaluate:[39;49;00m [31manAction[39;49;00m $
  1950^I$
  1951^I^I|[31m actions [39;49;00m|$
  1952^I^I[31mactions[39;49;00m := [36mself[39;49;00m [32mactionSequenceForEvent:[39;49;00m [31manEventSelector[39;49;00m.$
  1953^I^I([31mactions[39;49;00m [32mincludes:[39;49;00m [31manAction[39;49;00m)$
  1954^I^I^I[36mifTrue:[39;49;00m [^ [36mself[39;49;00m].$
  1955^I^I[36mself[39;49;00m $
  1956^I^I^I[32msetActionSequence:[39;49;00m ([31mactions[39;49;00m [32mcopyWith:[39;49;00m [31manAction[39;49;00m)$
  1957^I^I^I[32mforEvent:[39;49;00m [31manEventSelector[39;49;00m[34m! ![39;49;00m$
  1958^I$
  1959^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-registering'[39;49;00m[34m stamp: 'rww 12/30/2002 10:37'![39;49;00m$
  1960^I[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
  1961^I[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
  1962^I[32mto:[39;49;00m [31manObject[39;49;00m$
  1963^I $
  1964^I    [36mself[39;49;00m$
  1965^I        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
  1966^I        [32mevaluate:[39;49;00m ([04m[32mWeakMessageSend[39;49;00m$
  1967^I            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
  1968^I            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m)[34m! ![39;49;00m$
  1969^I$
  1970^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-registering'[39;49;00m[34m stamp: 'rww 12/30/2002 10:37'![39;49;00m$
  1971^I[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
  1972^I[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
  1973^I[32mto:[39;49;00m [31manObject[39;49;00m$
  1974^I[32mwithArguments:[39;49;00m [31manArgArray[39;49;00m$
  1975^I $
  1976^I    [36mself[39;49;00m$
  1977^I        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
  1978^I        [32mevaluate:[39;49;00m ([04m[32mWeakMessageSend[39;49;00m$
  1979^I            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
  1980^I            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
  1981^I^I^I[32marguments:[39;49;00m [31manArgArray[39;49;00m)[34m! ![39;49;00m$
  1982^I$
  1983^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-registering'[39;49;00m[34m stamp: 'rww 12/30/2002 10:37'![39;49;00m$
  1984^I[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
  1985^I[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
  1986^I[32mto:[39;49;00m [31manObject[39;49;00m$
  1987^I[32mwith:[39;49;00m [31manArg[39;49;00m$
  1988^I $
  1989^I    [36mself[39;49;00m$
  1990^I        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
  1991^I        [32mevaluate:[39;49;00m ([04m[32mWeakMessageSend[39;49;00m$
  1992^I            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
  1993^I            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
  1994^I^I^I[32marguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manArg[39;49;00m))[34m! ![39;49;00m$
  1995^I$
  1996^I$
  1997^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:33'![39;49;00m$
  1998^I[32mreleaseActionMap[39;49;00m$
  1999^I$
  2000^I^I[04m[32mEventManager[39;49;00m [32mreleaseActionMapFor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  2001^I$
  2002^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:33'![39;49;00m$
  2003^I[32mremoveActionsForEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2004^I$
  2005^I    |[31m map [39;49;00m|$
  2006^I    [31mmap[39;49;00m := [36mself[39;49;00m [32mactionMap[39;49;00m.$
  2007^I    [31mmap[39;49;00m [32mremoveKey:[39;49;00m [31manEventSelector[39;49;00m [32masSymbol[39;49;00m [32mifAbsent:[39;49;00m [].$
  2008^I    [31mmap[39;49;00m [32misEmpty[39;49;00m$
  2009^I        [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mreleaseActionMap[39;49;00m][34m! ![39;49;00m$
  2010^I$
  2011^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'nk 8/25/2003 21:46'![39;49;00m$
  2012^I[32mremoveActionsSatisfying:[39;49;00m [31maBlock[39;49;00m$
  2013^I$
  2014^I^I[36mself[39;49;00m [32mactionMap[39;49;00m [32mkeys[39;49;00m [32mdo:[39;49;00m$
  2015^I^I^I[:[31meachEventSelector[39;49;00m |$
  2016^I^I^I^I[36mself[39;49;00m$
  2017^I   ^I^I^I^I[32mremoveActionsSatisfying:[39;49;00m [31maBlock[39;49;00m$
  2018^I^I^I^I^I[32mforEvent:[39;49;00m [31meachEventSelector[39;49;00m$
  2019^I^I^I][34m! ![39;49;00m$
  2020^I$
  2021^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:31'![39;49;00m$
  2022^I[32mremoveActionsSatisfying:[39;49;00m [31maOneArgBlock[39;49;00m $
  2023^I[32mforEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2024^I$
  2025^I    [36mself[39;49;00m$
  2026^I        [32msetActionSequence:[39;49;00m$
  2027^I            (([36mself[39;49;00m [32mactionSequenceForEvent:[39;49;00m [31manEventSelector[39;49;00m)$
  2028^I                [32mreject:[39;49;00m [:[31manAction[39;49;00m | [31maOneArgBlock[39;49;00m [32mvalue:[39;49;00m [31manAction[39;49;00m])$
  2029^I        [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m[34m! ![39;49;00m$
  2030^I$
  2031^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'rw 7/29/2003 17:18'![39;49;00m$
  2032^I[32mremoveActionsWithReceiver:[39;49;00m [31manObject[39;49;00m$
  2033^I$
  2034^I^I[36mself[39;49;00m [32mactionMap[39;49;00m [32mcopy[39;49;00m [32mkeysDo:[39;49;00m$
  2035^I^I^I[:[31meachEventSelector[39;49;00m |$
  2036^I^I^I^I[36mself[39;49;00m$
  2037^I   ^I^I^I^I[32mremoveActionsSatisfying:[39;49;00m [:[31manAction[39;49;00m | [31manAction[39;49;00m [32mreceiver[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m]$
  2038^I^I^I^I^I[32mforEvent:[39;49;00m [31meachEventSelector[39;49;00m$
  2039^I^I^I][34m! ![39;49;00m$
  2040^I$
  2041^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:36'![39;49;00m$
  2042^I[32mremoveActionsWithReceiver:[39;49;00m [31manObject[39;49;00m$
  2043^I[32mforEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2044^I$
  2045^I    [36mself[39;49;00m$
  2046^I        [32mremoveActionsSatisfying:[39;49;00m$
  2047^I            [:[31manAction[39;49;00m |$
  2048^I            [31manAction[39;49;00m [32mreceiver[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m]$
  2049^I        [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m[34m! ![39;49;00m$
  2050^I$
  2051^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:31'![39;49;00m$
  2052^I[32mremoveAction:[39;49;00m [31manAction[39;49;00m$
  2053^I[32mforEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2054^I$
  2055^I    [36mself[39;49;00m$
  2056^I        [32mremoveActionsSatisfying:[39;49;00m [:[31maction[39;49;00m | [31maction[39;49;00m [32m=[39;49;00m [31manAction[39;49;00m]$
  2057^I        [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m[34m! ![39;49;00m$
  2058^I$
  2059^I$
  2060^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:22'![39;49;00m$
  2061^I[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2062^I^I[37m"Evaluate all actions registered for <anEventSelector>. Return the value of the last registered action."[39;49;00m$
  2063^I$
  2064^I    ^([36mself[39;49;00m [32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m) [32mvalue[39;49;00m[34m! ![39;49;00m$
  2065^I$
  2066^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 17:09'![39;49;00m$
  2067^I[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2068^I[32mifNotHandled:[39;49;00m [31manExceptionBlock[39;49;00m$
  2069^I^I[37m"Evaluate all actions registered for <anEventSelector>. Return the value of the last registered action."[39;49;00m$
  2070^I$
  2071^I    ^([36mself[39;49;00m $
  2072^I^I^I[32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2073^I^I^I[32mifAbsent:[39;49;00m [^[31manExceptionBlock[39;49;00m [32mvalue[39;49;00m]) [32mvalue[39;49;00m$
  2074^I[34m! ![39;49;00m$
  2075^I$
  2076^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:21'![39;49;00m$
  2077^I[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2078^I[32mwithArguments:[39;49;00m [31manArgumentList[39;49;00m$
  2079^I$
  2080^I    ^([36mself[39;49;00m [32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m)$
  2081^I        [32mvalueWithArguments:[39;49;00m [31manArgumentList[39;49;00m[34m! ![39;49;00m$
  2082^I$
  2083^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:21'![39;49;00m$
  2084^I[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2085^I[32mwithArguments:[39;49;00m [31manArgumentList[39;49;00m$
  2086^I[32mifNotHandled:[39;49;00m [31manExceptionBlock[39;49;00m$
  2087^I$
  2088^I    ^([36mself[39;49;00m $
  2089^I^I^I[32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2090^I^I^I[32mifAbsent:[39;49;00m [^[31manExceptionBlock[39;49;00m [32mvalue[39;49;00m])$
  2091^I        [32mvalueWithArguments:[39;49;00m [31manArgumentList[39;49;00m[34m! ![39;49;00m$
  2092^I$
  2093^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 14:59'![39;49;00m$
  2094^I[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2095^I[32mwith:[39;49;00m [31manObject[39;49;00m$
  2096^I$
  2097^I    ^[36mself[39;49;00m $
  2098^I^I^I[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2099^I^I^I[32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m)[34m! ![39;49;00m$
  2100^I$
  2101^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 14:59'![39;49;00m$
  2102^I[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2103^I[32mwith:[39;49;00m [31manObject[39;49;00m$
  2104^I[32mifNotHandled:[39;49;00m [31manExceptionBlock[39;49;00m$
  2105^I$
  2106^I    ^[36mself[39;49;00m $
  2107^I^I^I[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
  2108^I^I^I[32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m)$
  2109^I^I^I[32mifNotHandled:[39;49;00m [31manExceptionBlock[39;49;00m[34m! ![39;49;00m$
  2110^I$
  2111^I$
  2112^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 00:42'![39;49;00m$
  2113^I[32mbyteEncode:[39;49;00m[31maStream[39;49;00m$
  2114^I^I[36mself[39;49;00m [32mflattenOnStream:[39;49;00m[31maStream[39;49;00m.$
  2115^I[34m! ![39;49;00m$
  2116^I$
  2117^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m![39;49;00m$
  2118^I[32mdrawOnCanvas:[39;49;00m[31maStream[39;49;00m$
  2119^I^I[36mself[39;49;00m [32mflattenOnStream:[39;49;00m[31maStream[39;49;00m.$
  2120^I[34m! ![39;49;00m$
  2121^I$
  2122^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 01:31'![39;49;00m$
  2123^I[32melementSeparator[39;49;00m$
  2124^I^I^[36mnil[39;49;00m.[34m! ![39;49;00m$
  2125^I$
  2126^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m![39;49;00m$
  2127^I[32mencodePostscriptOn:[39;49;00m[31maStream[39;49;00m$
  2128^I^I[36mself[39;49;00m [32mbyteEncode:[39;49;00m[31maStream[39;49;00m.$
  2129^I[34m! ![39;49;00m$
  2130^I$
  2131^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 00:07'![39;49;00m$
  2132^I[32mflattenOnStream:[39;49;00m[31maStream[39;49;00m$
  2133^I^I[36mself[39;49;00m [32mwriteOnFilterStream:[39;49;00m[31maStream[39;49;00m.$
  2134^I[34m! ![39;49;00m$
  2135^I$
  2136^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'mpw 6/22/1930 22:56'![39;49;00m$
  2137^I[32mfullDrawPostscriptOn:[39;49;00m[31maStream[39;49;00m$
  2138^I^I^[31maStream[39;49;00m [32mfullDraw:[39;49;00m[36mself[39;49;00m.$
  2139^I[34m! ![39;49;00m$
  2140^I$
  2141^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 01:51'![39;49;00m$
  2142^I[32mprintOnStream:[39;49;00m[31maStream[39;49;00m$
  2143^I^I[36mself[39;49;00m [32mbyteEncode:[39;49;00m[31maStream[39;49;00m.$
  2144^I[34m! ![39;49;00m$
  2145^I$
  2146^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 00:49'![39;49;00m$
  2147^I[32mputOn:[39;49;00m[31maStream[39;49;00m$
  2148^I^I^[31maStream[39;49;00m [32mnextPut:[39;49;00m[36mself[39;49;00m.$
  2149^I[34m! ![39;49;00m$
  2150^I$
  2151^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 01:53'![39;49;00m$
  2152^I[32mstoreOnStream:[39;49;00m[31maStream[39;49;00m$
  2153^I^I[36mself[39;49;00m [32mprintOnStream:[39;49;00m[31maStream[39;49;00m.$
  2154^I[34m! ![39;49;00m$
  2155^I$
  2156^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 00:06'![39;49;00m$
  2157^I[32mwriteOnFilterStream:[39;49;00m[31maStream[39;49;00m$
  2158^I^I[31maStream[39;49;00m [32mwriteObject:[39;49;00m[36mself[39;49;00m.$
  2159^I[34m! ![39;49;00m$
  2160^I$
  2161^I$
  2162^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 3/21/98 16:26'![39;49;00m$
  2163^I[32mactAsExecutor[39;49;00m$
  2164^I^I[37m"Prepare the receiver to act as executor for any resources associated with it"[39;49;00m$
  2165^I^I[36mself[39;49;00m [32mbreakDependents[39;49;00m[34m! ![39;49;00m$
  2166^I$
  2167^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 3/20/98 22:19'![39;49;00m$
  2168^I[32mexecutor[39;49;00m$
  2169^I^I[37m"Return an object which can act as executor for finalization of the receiver"[39;49;00m$
  2170^I^I^[36mself[39;49;00m [32mshallowCopy[39;49;00m [32mactAsExecutor[39;49;00m[34m! ![39;49;00m$
  2171^I$
  2172^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 5/19/2003 20:10'![39;49;00m$
  2173^I[32mfinalizationRegistry[39;49;00m$
  2174^I^I[37m"Answer the finalization registry associated with the receiver."[39;49;00m$
  2175^I^I^[04m[32mWeakRegistry[39;49;00m [32mdefault[39;49;00m[34m! ![39;49;00m$
  2176^I$
  2177^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 3/21/98 16:27'![39;49;00m$
  2178^I[32mfinalize[39;49;00m$
  2179^I^I[37m"Finalize the resource associated with the receiver. This message should only be sent during the finalization process. There is NO garantuee that the resource associated with the receiver hasn't been free'd before so take care that you don't run into trouble - this all may happen with interrupt priority."[39;49;00m[34m! ![39;49;00m$
  2180^I$
  2181^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 3/21/98 18:38'![39;49;00m$
  2182^I[32mretryWithGC:[39;49;00m [31mexecBlock[39;49;00m [32muntil:[39;49;00m [31mtestBlock[39;49;00m$
  2183^I^I[37m"Retry execBlock as long as testBlock returns false. Do an incremental GC after the first try, a full GC after the second try."[39;49;00m$
  2184^I^I|[31m blockValue [39;49;00m|$
  2185^I^I[31mblockValue[39;49;00m := [31mexecBlock[39;49;00m [32mvalue[39;49;00m.$
  2186^I^I([31mtestBlock[39;49;00m [32mvalue:[39;49;00m [31mblockValue[39;49;00m) [36mifTrue:[39;49;00m[^[31mblockValue[39;49;00m].$
  2187^I^I[04m[32mSmalltalk[39;49;00m [32mgarbageCollectMost[39;49;00m.$
  2188^I^I[31mblockValue[39;49;00m := [31mexecBlock[39;49;00m [32mvalue[39;49;00m.$
  2189^I^I([31mtestBlock[39;49;00m [32mvalue:[39;49;00m [31mblockValue[39;49;00m) [36mifTrue:[39;49;00m[^[31mblockValue[39;49;00m].$
  2190^I^I[04m[32mSmalltalk[39;49;00m [32mgarbageCollect[39;49;00m.$
  2191^I^I^[31mexecBlock[39;49;00m [32mvalue[39;49;00m.[34m! ![39;49;00m$
  2192^I$
  2193^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 5/19/2003 20:14'![39;49;00m$
  2194^I[32mtoFinalizeSend:[39;49;00m [31maSelector[39;49;00m [32mto:[39;49;00m [31maFinalizer[39;49;00m [32mwith:[39;49;00m [31maResourceHandle[39;49;00m$
  2195^I^I[37m"When I am finalized (e.g., garbage collected) close the associated resource handle by sending aSelector to the appropriate finalizer (the guy who knows how to get rid of the resource).[39;49;00m$
  2196^I[37m^IWARNING: Neither the finalizer nor the resource handle are allowed to reference me. If they do, then I will NEVER be garbage collected. Since this cannot be validated here, it is up to the client to make sure this invariant is not broken."[39;49;00m$
  2197^I^I[36mself[39;49;00m [32m==[39;49;00m [31maFinalizer[39;49;00m [36mifTrue:[39;49;00m[[36mself[39;49;00m [32merror:[39;49;00m [33m'I cannot finalize myself'[39;49;00m].$
  2198^I^I[36mself[39;49;00m [32m==[39;49;00m [31maResourceHandle[39;49;00m [36mifTrue:[39;49;00m[[36mself[39;49;00m [32merror:[39;49;00m [33m'I cannot finalize myself'[39;49;00m].$
  2199^I^I^[36mself[39;49;00m [32mfinalizationRegistry[39;49;00m [32madd:[39;49;00m [36mself[39;49;00m [32mexecutor:[39;49;00m$
  2200^I^I^I([04m[32mObjectFinalizer[39;49;00m [36mnew[39;49;00m$
  2201^I^I^I^I[32mreceiver:[39;49;00m [31maFinalizer[39;49;00m$
  2202^I^I^I^I[32mselector:[39;49;00m [31maSelector[39;49;00m$
  2203^I^I^I^I[32margument:[39;49;00m [31maResourceHandle[39;49;00m)[34m! ![39;49;00m$
  2204^I$
  2205^I$
  2206^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'flagging'[39;49;00m[34m stamp: 'sw 8/4/97 16:49'![39;49;00m$
  2207^I[32misThisEverCalled[39;49;00m$
  2208^I^I^ [36mself[39;49;00m [32misThisEverCalled:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
  2209^I$
  2210^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'flagging'[39;49;00m[34m![39;49;00m$
  2211^I[32misThisEverCalled:[39;49;00m [31mmsg[39;49;00m$
  2212^I^I[37m"Send this message, with some useful printable argument, from methods or branches of methods which you believe are never reached.  2/5/96 sw"[39;49;00m$
  2213^I$
  2214^I^I[36mself[39;49;00m [32mhalt:[39;49;00m [33m'This is indeed called: '[39;49;00m[32m,[39;49;00m [31mmsg[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
  2215^I$
  2216^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'flagging'[39;49;00m[34m stamp: 'jm 3/18/98 17:23'![39;49;00m$
  2217^I[32mlogEntry[39;49;00m$
  2218^I$
  2219^I^I[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m [33m'Entered '[39;49;00m[32m,[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m; [32mcr[39;49;00m.$
  2220^I[34m! ![39;49;00m$
  2221^I$
  2222^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'flagging'[39;49;00m[34m stamp: 'jm 3/18/98 17:23'![39;49;00m$
  2223^I[32mlogExecution[39;49;00m$
  2224^I$
  2225^I^I[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m [33m'Executing '[39;49;00m[32m,[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m; [32mcr[39;49;00m.$
  2226^I[34m! ![39;49;00m$
  2227^I$
  2228^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'flagging'[39;49;00m[34m stamp: 'jm 3/18/98 17:22'![39;49;00m$
  2229^I[32mlogExit[39;49;00m$
  2230^I$
  2231^I^I[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m  [33m'Exited '[39;49;00m[32m,[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m; [32mcr[39;49;00m.$
  2232^I[34m! ![39;49;00m$
  2233^I$
  2234^I$
  2235^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'graph model'[39;49;00m[34m stamp: 'dgd 9/18/2004 15:07'![39;49;00m$
  2236^I[32maddModelYellowButtonMenuItemsTo:[39;49;00m [31maCustomMenu[39;49;00m [32mforMorph:[39;49;00m [31maMorph[39;49;00m [32mhand:[39;49;00m [31maHandMorph[39;49;00m $
  2237^I^I[37m"The receiver serves as the model for aMorph; a menu is being constructed for the morph, and here the receiver is able to add its own items"[39;49;00m$
  2238^I^I[04m[32mPreferences[39;49;00m [32mcmdGesturesEnabled[39;49;00m [36mifTrue:[39;49;00m [ [37m"build mode"[39;49;00m$
  2239^I^I^I[31maCustomMenu[39;49;00m [32madd:[39;49;00m [33m'inspect model'[39;49;00m [32mtranslated[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32maction:[39;49;00m [33m#inspect[39;49;00m.$
  2240^I^I].$
  2241^I$
  2242^I^I^[31maCustomMenu[39;49;00m$
  2243^I[34m! ![39;49;00m$
  2244^I$
  2245^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'graph model'[39;49;00m[34m stamp: 'nk 1/23/2004 14:35'![39;49;00m$
  2246^I[32mhasModelYellowButtonMenuItems[39;49;00m$
  2247^I^I^[04m[32mPreferences[39;49;00m [32mcmdGesturesEnabled[39;49;00m[34m! ![39;49;00m$
  2248^I$
  2249^I$
  2250^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'inspecting'[39;49;00m[34m stamp: 'ar 9/27/2005 18:31'![39;49;00m$
  2251^I[32mbasicInspect[39;49;00m$
  2252^I^I[37m"Create and schedule an Inspector in which the user can examine the [39;49;00m$
  2253^I[37m^Ireceiver's variables. This method should not be overriden."[39;49;00m$
  2254^I^I^[04m[32mToolSet[39;49;00m [32mbasicInspect:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  2255^I$
  2256^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'inspecting'[39;49;00m[34m stamp: 'md 1/18/2006 19:09'![39;49;00m$
  2257^I[32minspect[39;49;00m$
  2258^I^I[37m"Create and schedule an Inspector in which the user can examine the receiver's variables."[39;49;00m$
  2259^I^I[04m[32mToolSet[39;49;00m [32minspect:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  2260^I$
  2261^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'inspecting'[39;49;00m[34m stamp: 'apb 7/14/2004 12:19'![39;49;00m$
  2262^I[32minspectorClass[39;49;00m$
  2263^I^I[37m"Answer the class of the inspector to be used on the receiver.  Called by inspect; [39;49;00m$
  2264^I[37m^Iuse basicInspect to get a normal (less useful) type of inspector."[39;49;00m$
  2265^I$
  2266^I^I^ [04m[32mInspector[39;49;00m[34m! ![39;49;00m$
  2267^I$
  2268^I$
  2269^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'locales'[39;49;00m[34m stamp: 'tak 8/4/2005 14:55'![39;49;00m$
  2270^I[32mlocaleChanged[39;49;00m$
  2271^I^I[36mself[39;49;00m [32mshouldBeImplemented[39;49;00m[34m! ![39;49;00m$
  2272^I$
  2273^I$
  2274^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 5/7/1998 23:00'![39;49;00m$
  2275^I[32mcodeStrippedOut:[39;49;00m [31mmessageString[39;49;00m$
  2276^I^I[37m"When a method is stripped out for external release, it is replaced by a method that calls this"[39;49;00m$
  2277^I$
  2278^I^I[36mself[39;49;00m [32mhalt:[39;49;00m [33m'Code stripped out -- '[39;49;00m[32m,[39;49;00m [31mmessageString[39;49;00m[32m,[39;49;00m [33m'-- do not proceed.'[39;49;00m[34m! ![39;49;00m$
  2279^I$
  2280^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 1/28/1999 17:31'![39;49;00m$
  2281^I[32mcontentsChanged[39;49;00m$
  2282^I^I[36mself[39;49;00m [32mchanged:[39;49;00m [33m#contents[39;49;00m[34m! ![39;49;00m$
  2283^I$
  2284^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'ar 3/18/2001 00:03'![39;49;00m$
  2285^I[32mcurrentEvent[39;49;00m$
  2286^I^I[37m"Answer the current Morphic event.  This method never returns nil."[39;49;00m$
  2287^I^I^[04m[32mActiveEvent[39;49;00m [32mifNil:[39;49;00m[[36mself[39;49;00m [32mcurrentHand[39;49;00m [32mlastEvent[39;49;00m][34m! ![39;49;00m$
  2288^I$
  2289^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'nk 9/1/2004 10:41'![39;49;00m$
  2290^I[32mcurrentHand[39;49;00m$
  2291^I^I[37m"Return a usable HandMorph -- the one associated with the object's current environment.  This method will always return a hand, even if it has to conjure one up as a last resort.  If a particular hand is actually handling events at the moment (such as a remote hand or a ghost hand), it will be returned."[39;49;00m$
  2292^I$
  2293^I^I^[04m[32mActiveHand[39;49;00m [32mifNil:[39;49;00m [ [36mself[39;49;00m [32mcurrentWorld[39;49;00m [32mprimaryHand[39;49;00m ][34m! ![39;49;00m$
  2294^I$
  2295^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 5/17/2001 12:08'![39;49;00m$
  2296^I[32mcurrentVocabulary[39;49;00m$
  2297^I^I[37m"Answer the currently-prevailing default vocabulary."[39;49;00m$
  2298^I$
  2299^I^I^ [04m[32mSmalltalk[39;49;00m [32misMorphic[39;49;00m [36mifTrue:[39;49;00m$
  2300^I^I^I^I[[04m[32mActiveWorld[39;49;00m [32mcurrentVocabulary[39;49;00m]$
  2301^I^I^I[36mifFalse:[39;49;00m$
  2302^I^I^I^I[[04m[32mVocabulary[39;49;00m [32mfullVocabulary[39;49;00m][34m! ![39;49;00m$
  2303^I$
  2304^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'ar 3/18/2001 00:08'![39;49;00m$
  2305^I[32mcurrentWorld[39;49;00m$
  2306^I^I[37m"Answer a morphic world that is the current UI focus.[39;49;00m$
  2307^I[37m^I^IIf in an embedded world, it's that world.[39;49;00m$
  2308^I[37m^I^IIf in a morphic project, it's that project's world.  [39;49;00m$
  2309^I[37m^I^IIf in an mvc project, it is the topmost morphic-mvc-window's worldMorph. [39;49;00m$
  2310^I[37m^I^IIf in an mvc project that has no morphic-mvc-windows, then it's just some existing worldmorph instance.[39;49;00m$
  2311^I[37m^I^IIf in an mvc project in a Squeak that has NO WorldMorph instances, one is created.[39;49;00m$
  2312^I[37m[39;49;00m$
  2313^I[37m^IThis method will never return nil, it will always return its best effort at returning a relevant world morph, but if need be -- if there are no worlds anywhere, it will create a new one."[39;49;00m$
  2314^I$
  2315^I^I|[31m aView aSubview [39;49;00m|$
  2316^I^I[04m[32mActiveWorld[39;49;00m [32mifNotNil:[39;49;00m[^[04m[32mActiveWorld[39;49;00m].$
  2317^I^I[04m[32mWorld[39;49;00m [32mifNotNil:[39;49;00m[^[04m[32mWorld[39;49;00m].$
  2318^I^I[31maView[39;49;00m _ [04m[32mScheduledControllers[39;49;00m [32mcontrollerSatisfying:[39;49;00m$
  2319^I^I^I[:[31mctrl[39;49;00m | ([31maSubview[39;49;00m _ [31mctrl[39;49;00m [32mview[39;49;00m [32mfirstSubView[39;49;00m) [32mnotNil[39;49;00m [32mand:[39;49;00m$
  2320^I^I^I^I[[31maSubview[39;49;00m [32mmodel[39;49;00m [32misMorph[39;49;00m [32mand:[39;49;00m [[31maSubview[39;49;00m [32mmodel[39;49;00m [32misWorldMorph[39;49;00m]]].$
  2321^I^I^[31maView[39;49;00m$
  2322^I^I^I[32mifNotNil:[39;49;00m$
  2323^I^I^I^I[[31maSubview[39;49;00m [32mmodel[39;49;00m]$
  2324^I^I^I[32mifNil:[39;49;00m$
  2325^I^I^I^I[[04m[32mMVCWiWPasteUpMorph[39;49;00m [32mnewWorldForProject:[39;49;00m [36mnil[39;49;00m].[34m! ![39;49;00m$
  2326^I$
  2327^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'jm 5/6/1998 22:35'![39;49;00m$
  2328^I[32mflash[39;49;00m$
  2329^I^I[37m"Do nothing."[39;49;00m$
  2330^I[34m! ![39;49;00m$
  2331^I$
  2332^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 6/16/1998 15:07'![39;49;00m$
  2333^I[32minstanceVariableValues[39;49;00m$
  2334^I^I[37m"Answer a collection whose elements are the values of those instance variables of the receiver which were added by the receiver's class"[39;49;00m$
  2335^I^I|[31m c [39;49;00m|$
  2336^I^I[31mc[39;49;00m _ [04m[32mOrderedCollection[39;49;00m [36mnew[39;49;00m.$
  2337^I^I[36mself[39;49;00m [32mclass[39;49;00m [32msuperclass[39;49;00m [32minstSize[39;49;00m [32m+[39;49;00m [34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mdo:[39;49;00m$
  2338^I^I^I[:[31mi[39;49;00m | [31mc[39;49;00m [32madd:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mi[39;49;00m)].$
  2339^I^I^ [31mc[39;49;00m[34m! ![39;49;00m$
  2340^I$
  2341^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 3/20/2001 13:29'![39;49;00m$
  2342^I[32misUniversalTiles[39;49;00m$
  2343^I^I[37m"Return true if I (my world) uses universal tiles.  This message can be called in places where the current World is not known, such as when writing out a project.  For more information about the project-writing subtlety addressed by this protocol, kindly contact Ted Kaehler."[39;49;00m$
  2344^I$
  2345^I^I^ [04m[32mPreferences[39;49;00m [32muniversalTiles[39;49;00m[34m! ![39;49;00m$
  2346^I$
  2347^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 10/24/2000 07:04'![39;49;00m$
  2348^I[32mobjectRepresented[39;49;00m$
  2349^I^I[37m"most objects represent themselves; this provides a hook for aliases to grab on to"[39;49;00m$
  2350^I$
  2351^I^I^ [36mself[39;49;00m[34m! ![39;49;00m$
  2352^I$
  2353^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 5/22/2001 18:31'![39;49;00m$
  2354^I[32mrefusesToAcceptCode[39;49;00m$
  2355^I^I[37m"Answer whether the receiver is a code-bearing instrument which at the moment refuses to allow its contents to be submitted"[39;49;00m$
  2356^I$
  2357^I^I^ [36mfalse[39;49;00m$
  2358^I^I[34m! ![39;49;00m$
  2359^I$
  2360^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'jm 2/24/1999 12:40'![39;49;00m$
  2361^I[32mscriptPerformer[39;49;00m$
  2362^I$
  2363^I^I^ [36mself[39;49;00m$
  2364^I[34m! ![39;49;00m$
  2365^I$
  2366^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 3/20/2001 13:40'![39;49;00m$
  2367^I[32mslotInfo[39;49;00m$
  2368^I^I[37m"Answer a list of slot-information objects.  Initally only provides useful info for players"[39;49;00m$
  2369^I$
  2370^I^I^ [04m[32mDictionary[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
  2371^I$
  2372^I$
  2373^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:28'![39;49;00m$
  2374^I[32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
  2375^I^I[37m"Execute compiledMethod against the receiver with no args"[39;49;00m$
  2376^I$
  2377^I^I[37m"<primitive: 189>"[39;49;00m [37m"uncomment once prim 189 is in VM"[39;49;00m$
  2378^I^I^ [36mself[39;49;00m [32mwithArgs:[39;49;00m [33m#([39;49;00m[33m)[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m[34m! ![39;49;00m$
  2379^I$
  2380^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'di 3/26/1999 07:52'![39;49;00m$
  2381^I[32mperform:[39;49;00m [31maSymbol[39;49;00m $
  2382^I^I[37m"Send the unary selector, aSymbol, to the receiver.[39;49;00m$
  2383^I[37m^IFail if the number of arguments expected by the selector is not zero.[39;49;00m$
  2384^I[37m^IPrimitive. Optional. See Object documentation whatIsAPrimitive."[39;49;00m$
  2385^I$
  2386^I^I<[34mprimitive:[39;49;00m 83>$
  2387^I^I^ [36mself[39;49;00m [32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mnew:[39;49;00m [34m0[39;49;00m)[34m! ![39;49;00m$
  2388^I$
  2389^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'st 11/5/2004 16:19'![39;49;00m$
  2390^I[32mperform:[39;49;00m [31mselector[39;49;00m [32morSendTo:[39;49;00m [31motherTarget[39;49;00m$
  2391^I^I[37m"If I wish to intercept and handle selector myself, do it; else send it to otherTarget"[39;49;00m$
  2392^I^I^ ([36mself[39;49;00m [32mrespondsTo:[39;49;00m [31mselector[39;49;00m) [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m] [36mifFalse:[39;49;00m [[31motherTarget[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m][34m! ![39;49;00m$
  2393^I$
  2394^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'di 3/26/1999 07:55'![39;49;00m$
  2395^I[32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31margArray[39;49;00m $
  2396^I^I[37m"Send the selector, aSymbol, to the receiver with arguments in argArray.[39;49;00m$
  2397^I[37m^IFail if the number of arguments expected by the selector [39;49;00m$
  2398^I[37m^Idoes not match the size of argArray.[39;49;00m$
  2399^I[37m^IPrimitive. Optional. See Object documentation whatIsAPrimitive."[39;49;00m$
  2400^I$
  2401^I^I<[34mprimitive:[39;49;00m 84>$
  2402^I^I^ [36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31margArray[39;49;00m [32minSuperclass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m[34m! ![39;49;00m$
  2403^I$
  2404^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'ar 4/25/2005 13:35'![39;49;00m$
  2405^I[32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31margArray[39;49;00m [32minSuperclass:[39;49;00m [31mlookupClass[39;49;00m$
  2406^I^I[37m"NOTE:  This is just like perform:withArguments:, except that[39;49;00m$
  2407^I[37m^Ithe message lookup process begins, not with the receivers's class,[39;49;00m$
  2408^I[37m^Ibut with the supplied superclass instead.  It will fail if lookupClass[39;49;00m$
  2409^I[37m^Icannot be found among the receiver's superclasses.[39;49;00m$
  2410^I[37m^IPrimitive. Essential. See Object documentation whatIsAPrimitive."[39;49;00m$
  2411^I$
  2412^I^I<[34mprimitive:[39;49;00m 100>$
  2413^I^I([31mselector[39;49;00m [32misSymbol[39;49;00m)$
  2414^I^I^I[36mifFalse:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'selector argument must be a Symbol'[39;49;00m].$
  2415^I^I([31mselector[39;49;00m [32mnumArgs[39;49;00m [32m=[39;49;00m [31margArray[39;49;00m [32msize[39;49;00m)$
  2416^I^I^I[36mifFalse:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'incorrect number of arguments'[39;49;00m].$
  2417^I^I([36mself[39;49;00m [32mclass[39;49;00m [32m==[39;49;00m [31mlookupClass[39;49;00m [32mor:[39;49;00m [[36mself[39;49;00m [32mclass[39;49;00m [32minheritsFrom:[39;49;00m [31mlookupClass[39;49;00m])$
  2418^I^I^I[36mifFalse:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'lookupClass is not in my inheritance chain'[39;49;00m].$
  2419^I^I[36mself[39;49;00m [32mprimitiveFailed[39;49;00m[34m! ![39;49;00m$
  2420^I$
  2421^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'nk 4/11/2002 14:13'![39;49;00m$
  2422^I[32mperform:[39;49;00m [31mselector[39;49;00m [32mwithEnoughArguments:[39;49;00m [31manArray[39;49;00m$
  2423^I^I[37m"Send the selector, aSymbol, to the receiver with arguments in argArray.[39;49;00m$
  2424^I[37m^IOnly use enough arguments for the arity of the selector; supply nils for missing ones."[39;49;00m$
  2425^I^I|[31m numArgs args [39;49;00m|$
  2426^I^I[31mnumArgs[39;49;00m _ [31mselector[39;49;00m [32mnumArgs[39;49;00m.$
  2427^I^I[31manArray[39;49;00m [32msize[39;49;00m [32m==[39;49;00m [31mnumArgs[39;49;00m$
  2428^I^I^I[36mifTrue:[39;49;00m [ ^[36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31manArray[39;49;00m [32masArray[39;49;00m ].$
  2429^I$
  2430^I^I[31margs[39;49;00m _ [04m[32mArray[39;49;00m [32mnew:[39;49;00m [31mnumArgs[39;49;00m.$
  2431^I^I[31margs[39;49;00m [32mreplaceFrom:[39;49;00m [34m1[39;49;00m$
  2432^I^I^I[32mto:[39;49;00m ([31manArray[39;49;00m [32msize[39;49;00m [32mmin:[39;49;00m [31margs[39;49;00m [32msize[39;49;00m)$
  2433^I^I^I[32mwith:[39;49;00m [31manArray[39;49;00m$
  2434^I^I^I[32mstartingAt:[39;49;00m [34m1[39;49;00m.$
  2435^I$
  2436^I^I^ [36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31margs[39;49;00m[34m! ![39;49;00m$
  2437^I$
  2438^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'di 3/26/1999 07:52'![39;49;00m$
  2439^I[32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m $
  2440^I^I[37m"Send the selector, aSymbol, to the receiver with anObject as its argument.[39;49;00m$
  2441^I[37m^IFail if the number of arguments expected by the selector is not one.[39;49;00m$
  2442^I[37m^IPrimitive. Optional. See Object documentation whatIsAPrimitive."[39;49;00m$
  2443^I$
  2444^I^I<[34mprimitive:[39;49;00m 83>$
  2445^I^I^ [36mself[39;49;00m [32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m)[34m! ![39;49;00m$
  2446^I$
  2447^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'di 3/26/1999 07:52'![39;49;00m$
  2448^I[32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwith:[39;49;00m [31mfirstObject[39;49;00m [32mwith:[39;49;00m [31msecondObject[39;49;00m $
  2449^I^I[37m"Send the selector, aSymbol, to the receiver with the given arguments.[39;49;00m$
  2450^I[37m^IFail if the number of arguments expected by the selector is not two.[39;49;00m$
  2451^I[37m^IPrimitive. Optional. See Object documentation whatIsAPrimitive."[39;49;00m$
  2452^I$
  2453^I^I<[34mprimitive:[39;49;00m 83>$
  2454^I^I^ [36mself[39;49;00m [32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31mfirstObject[39;49;00m [32mwith:[39;49;00m [31msecondObject[39;49;00m)[34m! ![39;49;00m$
  2455^I$
  2456^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'di 3/26/1999 07:51'![39;49;00m$
  2457^I[32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwith:[39;49;00m [31mfirstObject[39;49;00m [32mwith:[39;49;00m [31msecondObject[39;49;00m [32mwith:[39;49;00m [31mthirdObject[39;49;00m $
  2458^I^I[37m"Send the selector, aSymbol, to the receiver with the given arguments.[39;49;00m$
  2459^I[37m^IFail if the number of arguments expected by the selector is not three.[39;49;00m$
  2460^I[37m^IPrimitive. Optional. See Object documentation whatIsAPrimitive."[39;49;00m$
  2461^I$
  2462^I^I<[34mprimitive:[39;49;00m 83>$
  2463^I^I^ [36mself[39;49;00m [32mperform:[39;49;00m [31maSymbol[39;49;00m$
  2464^I^I^I[32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31mfirstObject[39;49;00m [32mwith:[39;49;00m [31msecondObject[39;49;00m [32mwith:[39;49;00m [31mthirdObject[39;49;00m)[34m! ![39;49;00m$
  2465^I$
  2466^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'NS 1/28/2004 11:19'![39;49;00m$
  2467^I[32mwithArgs:[39;49;00m [31margArray[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
  2468^I^I[37m"Execute compiledMethod against the receiver and args in argArray"[39;49;00m$
  2469^I$
  2470^I^I|[31m selector [39;49;00m|$
  2471^I^I<[34mprimitive:[39;49;00m 188>$
  2472^I^I[31mselector[39;49;00m _ [04m[32mSymbol[39;49;00m [36mnew[39;49;00m.$
  2473^I^I[36mself[39;49;00m [32mclass[39;49;00m [32maddSelectorSilently:[39;49;00m [31mselector[39;49;00m [32mwithMethod:[39;49;00m [31mcompiledMethod[39;49;00m.$
  2474^I^I^ [[36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31margArray[39;49;00m]$
  2475^I^I^I[32mensure:[39;49;00m [[36mself[39;49;00m [32mclass[39;49;00m [32mbasicRemoveSelector:[39;49;00m [31mselector[39;49;00m][34m! ![39;49;00m$
  2476^I$
  2477^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:28'![39;49;00m$
  2478^I[32mwith:[39;49;00m [31marg1[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
  2479^I^I[37m"Execute compiledMethod against the receiver and arg1"[39;49;00m$
  2480^I$
  2481^I^I[37m"<primitive: 189>"[39;49;00m [37m"uncomment once prim 189 is in VM"[39;49;00m$
  2482^I^I^ [36mself[39;49;00m [32mwithArgs:[39;49;00m {[31marg1[39;49;00m} [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m[34m! ![39;49;00m$
  2483^I$
  2484^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:28'![39;49;00m$
  2485^I[32mwith:[39;49;00m [31marg1[39;49;00m [32mwith:[39;49;00m [31marg2[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
  2486^I^I[37m"Execute compiledMethod against the receiver and arg1 & arg2"[39;49;00m$
  2487^I$
  2488^I^I[37m"<primitive: 189>"[39;49;00m [37m"uncomment once prim 189 is in VM"[39;49;00m$
  2489^I^I^ [36mself[39;49;00m [32mwithArgs:[39;49;00m {[31marg1[39;49;00m. [31marg2[39;49;00m} [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m[34m! ![39;49;00m$
  2490^I$
  2491^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:28'![39;49;00m$
  2492^I[32mwith:[39;49;00m [31marg1[39;49;00m [32mwith:[39;49;00m [31marg2[39;49;00m [32mwith:[39;49;00m [31marg3[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
  2493^I^I[37m"Execute compiledMethod against the receiver and arg1, arg2, & arg3"[39;49;00m$
  2494^I$
  2495^I^I[37m"<primitive: 189>"[39;49;00m [37m"uncomment once prim 189 is in VM"[39;49;00m$
  2496^I^I^ [36mself[39;49;00m [32mwithArgs:[39;49;00m {[31marg1[39;49;00m. [31marg2[39;49;00m. [31marg3[39;49;00m} [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m[34m! ![39;49;00m$
  2497^I$
  2498^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:28'![39;49;00m$
  2499^I[32mwith:[39;49;00m [31marg1[39;49;00m [32mwith:[39;49;00m [31marg2[39;49;00m [32mwith:[39;49;00m [31marg3[39;49;00m [32mwith:[39;49;00m [31marg4[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
  2500^I^I[37m"Execute compiledMethod against the receiver and arg1, arg2, arg3, & arg4"[39;49;00m$
  2501^I$
  2502^I^I[37m"<primitive: 189>"[39;49;00m [37m"uncomment once prim 189 is in VM"[39;49;00m$
  2503^I^I^ [36mself[39;49;00m [32mwithArgs:[39;49;00m {[31marg1[39;49;00m. [31marg2[39;49;00m. [31marg3[39;49;00m. [31marg4[39;49;00m} [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m[34m! ![39;49;00m$
  2504^I$
  2505^I$
  2506^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 4/8/1999 12:46'![39;49;00m$
  2507^I[32mcomeFullyUpOnReload:[39;49;00m [31msmartRefStream[39;49;00m$
  2508^I^I[37m"Normally this read-in object is exactly what we want to store. 7/26/96 tk"[39;49;00m$
  2509^I$
  2510^I^I^ [36mself[39;49;00m[34m! ![39;49;00m$
  2511^I$
  2512^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'RAA 12/20/2000 16:51'![39;49;00m$
  2513^I[32mconvertToCurrentVersion:[39;49;00m [31mvarDict[39;49;00m [32mrefStream:[39;49;00m [31msmartRefStrm[39;49;00m$
  2514^I$
  2515^I^I[37m"subclasses should implement if they wish to convert old instances to modern ones"[39;49;00m[34m! ![39;49;00m$
  2516^I$
  2517^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 11/29/2004 15:04'![39;49;00m$
  2518^I[32mfixUponLoad:[39;49;00m [31maProject[39;49;00m [32mseg:[39;49;00m [31manImageSegment[39;49;00m$
  2519^I^I[37m"change the object due to conventions that have changed on[39;49;00m$
  2520^I[37mthe project level.  (sent to all objects in the incoming project).[39;49;00m$
  2521^I[37mSpecific classes should reimplement this."[39;49;00m[34m! ![39;49;00m$
  2522^I$
  2523^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'RAA 1/10/2001 14:02'![39;49;00m$
  2524^I[32mindexIfCompact[39;49;00m$
  2525^I$
  2526^I^I^[34m0[39;49;00m^I^I[37m"helps avoid a #respondsTo: in publishing"[39;49;00m[34m! ![39;49;00m$
  2527^I$
  2528^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 2/24/1999 11:08'![39;49;00m$
  2529^I[32mobjectForDataStream:[39;49;00m [31mrefStrm[39;49;00m$
  2530^I    [37m"Return an object to store on an external data stream."[39;49;00m$
  2531^I$
  2532^I    ^ [36mself[39;49;00m[34m! ![39;49;00m$
  2533^I$
  2534^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 4/8/1999 12:05'![39;49;00m$
  2535^I[32mreadDataFrom:[39;49;00m [31maDataStream[39;49;00m [32msize:[39;49;00m [31mvarsOnDisk[39;49;00m$
  2536^I^I[37m"Fill in the fields of self based on the contents of aDataStream.  Return self.[39;49;00m$
  2537^I[37m^I Read in the instance-variables written by Object>>storeDataOn:.[39;49;00m$
  2538^I[37m^I NOTE: This method must send beginReference: before reading any objects from aDataStream that might reference it.[39;49;00m$
  2539^I[37m^I Allow aDataStream to have fewer inst vars.  See SmartRefStream."[39;49;00m$
  2540^I^I|[31m cntInstVars cntIndexedVars [39;49;00m|$
  2541^I$
  2542^I^I[31mcntInstVars[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m.$
  2543^I^I[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m$
  2544^I^I^I[36mifTrue:[39;49;00m [[31mcntIndexedVars[39;49;00m _ [31mvarsOnDisk[39;49;00m [32m-[39;49;00m [31mcntInstVars[39;49;00m.$
  2545^I^I^I^I^I[31mcntIndexedVars[39;49;00m [32m<[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m [$
  2546^I^I^I^I^I^I[36mself[39;49;00m [32merror:[39;49;00m [33m'Class has changed too much.  Define a convertxxx method'[39;49;00m]]$
  2547^I^I^I[36mifFalse:[39;49;00m [[31mcntIndexedVars[39;49;00m _ [34m0[39;49;00m.$
  2548^I^I^I^I^I[31mcntInstVars[39;49;00m _ [31mvarsOnDisk[39;49;00m]. ^I[37m"OK if fewer than now"[39;49;00m$
  2549^I$
  2550^I^I[31maDataStream[39;49;00m [32mbeginReference:[39;49;00m [36mself[39;49;00m.$
  2551^I^I[34m1[39;49;00m [32mto:[39;49;00m [31mcntInstVars[39;49;00m [32mdo:[39;49;00m$
  2552^I^I^I[:[31mi[39;49;00m | [36mself[39;49;00m [32minstVarAt:[39;49;00m [31mi[39;49;00m [32mput:[39;49;00m [31maDataStream[39;49;00m [32mnext[39;49;00m].$
  2553^I^I[34m1[39;49;00m [32mto:[39;49;00m [31mcntIndexedVars[39;49;00m [32mdo:[39;49;00m$
  2554^I^I^I[:[31mi[39;49;00m | [36mself[39;49;00m [32mbasicAt:[39;49;00m [31mi[39;49;00m [32mput:[39;49;00m [31maDataStream[39;49;00m [32mnext[39;49;00m].$
  2555^I^I[37m"Total number read MUST be equal to varsOnDisk!!"[39;49;00m$
  2556^I^I^ [36mself[39;49;00m^I[37m"If we ever return something other than self, fix calls [39;49;00m$
  2557^I[37m^I^I^Ion (super readDataFrom: aDataStream size: anInteger)"[39;49;00m[34m! ![39;49;00m$
  2558^I$
  2559^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'CdG 10/17/2005 20:32'![39;49;00m$
  2560^I[32msaveOnFile[39;49;00m$
  2561^I^I[37m"Ask the user for a filename and save myself on a SmartReferenceStream file.  Writes out the version and class structure.  The file is fileIn-able.  Does not file out the class of the object.  tk 6/26/97 13:48"[39;49;00m$
  2562^I$
  2563^I^I|[31m aFileName fileStream [39;49;00m|$
  2564^I^I[31maFileName[39;49;00m := [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32masFileName[39;49;00m.^I[37m"do better?"[39;49;00m$
  2565^I^I[31maFileName[39;49;00m := [04m[32mUIManager[39;49;00m [32mdefault[39;49;00m $
  2566^I^I^I^I^I[32mrequest:[39;49;00m [33m'File name?'[39;49;00m [32mtranslated[39;49;00m [32minitialAnswer:[39;49;00m [31maFileName[39;49;00m.$
  2567^I^I[31maFileName[39;49;00m [32msize[39;49;00m [32m==[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m [^ [04m[32mBeeper[39;49;00m [32mbeep[39;49;00m].$
  2568^I$
  2569^I^I[31mfileStream[39;49;00m := [04m[32mFileStream[39;49;00m [32mnewFileNamed:[39;49;00m [31maFileName[39;49;00m [32masFileName[39;49;00m.$
  2570^I^I[31mfileStream[39;49;00m [32mfileOutClass:[39;49;00m [36mnil[39;49;00m [32mandObject:[39;49;00m [36mself[39;49;00m.[34m! ![39;49;00m$
  2571^I$
  2572^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 8/9/2001 15:40'![39;49;00m$
  2573^I[32mstoreDataOn:[39;49;00m [31maDataStream[39;49;00m$
  2574^I^I[37m"Store myself on a DataStream.  Answer self.  This is a low-level DataStream/ReferenceStream method. See also objectToStoreOnDataStream.  NOTE: This method must send 'aDataStream beginInstance:size:' and then (nextPut:/nextPutWeak:) its subobjects.  readDataFrom:size: reads back what we write here."[39;49;00m$
  2575^I^I|[31m cntInstVars cntIndexedVars [39;49;00m|$
  2576^I$
  2577^I^I[31mcntInstVars[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m.$
  2578^I^I[31mcntIndexedVars[39;49;00m _ [36mself[39;49;00m [32mbasicSize[39;49;00m.$
  2579^I^I[31maDataStream[39;49;00m$
  2580^I^I^I[32mbeginInstance:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m$
  2581^I^I^I[32msize:[39;49;00m [31mcntInstVars[39;49;00m [32m+[39;49;00m [31mcntIndexedVars[39;49;00m.$
  2582^I^I[34m1[39;49;00m [32mto:[39;49;00m [31mcntInstVars[39;49;00m [32mdo:[39;49;00m$
  2583^I^I^I[:[31mi[39;49;00m | [31maDataStream[39;49;00m [32mnextPut:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mi[39;49;00m)].$
  2584^I$
  2585^I^I[37m"Write fields of a variable length object.  When writing to a dummy [39;49;00m$
  2586^I[37m^I^Istream, don't bother to write the bytes"[39;49;00m$
  2587^I^I(([31maDataStream[39;49;00m [32mbyteStream[39;49;00m [32mclass[39;49;00m [32m==[39;49;00m [04m[32mDummyStream[39;49;00m) [32mand:[39;49;00m [[36mself[39;49;00m [32mclass[39;49;00m [32misBits[39;49;00m]) [36mifFalse:[39;49;00m [$
  2588^I^I^I[34m1[39;49;00m [32mto:[39;49;00m [31mcntIndexedVars[39;49;00m [32mdo:[39;49;00m$
  2589^I^I^I^I[:[31mi[39;49;00m | [31maDataStream[39;49;00m [32mnextPut:[39;49;00m ([36mself[39;49;00m [32mbasicAt:[39;49;00m [31mi[39;49;00m)]].$
  2590^I[34m! ![39;49;00m$
  2591^I$
  2592^I$
  2593^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'parts bin'[39;49;00m[34m stamp: 'sw 10/24/2001 16:34'![39;49;00m$
  2594^I[32mdescriptionForPartsBin[39;49;00m$
  2595^I^I[37m"If the receiver is a member of a class that would like to be represented in a parts bin, answer the name by which it should be known, and a documentation string to be provided, for example, as balloon help.  When the 'nativitySelector' is sent to the 'globalReceiver', it is expected that some kind of Morph will result.  The parameters used in the implementation below are for documentation purposes only!!"[39;49;00m$
  2596^I$
  2597^I^I^ [04m[32mDescriptionForPartsBin[39;49;00m$
  2598^I^I^I[32mformalName:[39;49;00m [33m'PutFormalNameHere'[39;49;00m$
  2599^I^I^I[32mcategoryList:[39;49;00m [33m#([39;49;00m[33mPutACategoryHere[39;49;00m [33mMaybePutAnotherCategoryHere[39;49;00m[33m)[39;49;00m$
  2600^I^I^I[32mdocumentation:[39;49;00m [33m'Put the balloon help here'[39;49;00m$
  2601^I^I^I[32mglobalReceiverSymbol:[39;49;00m [33m#PutAGlobalHere[39;49;00m$
  2602^I^I^I[32mnativitySelector:[39;49;00m [33m#PutASelectorHere[39;49;00m[34m! ![39;49;00m$
  2603^I$
  2604^I$
  2605^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'di 6/20/97 08:57'![39;49;00m$
  2606^I[32mfullPrintString[39;49;00m$
  2607^I^I[37m"Answer a String whose characters are a description of the receiver."[39;49;00m$
  2608^I$
  2609^I^I^ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [:[31ms[39;49;00m | [36mself[39;49;00m [32mprintOn:[39;49;00m [31ms[39;49;00m][34m! ![39;49;00m$
  2610^I$
  2611^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m![39;49;00m$
  2612^I[32misLiteral[39;49;00m$
  2613^I^I[37m"Answer whether the receiver has a literal text form recognized by the [39;49;00m$
  2614^I[37m^Icompiler."[39;49;00m$
  2615^I$
  2616^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
  2617^I$
  2618^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sma 6/1/2000 09:28'![39;49;00m$
  2619^I[32mlongPrintOn:[39;49;00m [31maStream[39;49;00m$
  2620^I^I[37m"Append to the argument, aStream, the names and values of all [39;49;00m$
  2621^I[37m^Iof the receiver's instance variables."[39;49;00m$
  2622^I$
  2623^I^I[36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mdoWithIndex:[39;49;00m$
  2624^I^I^I[:[31mtitle[39;49;00m :[31mindex[39;49;00m |$
  2625^I^I^I[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [31mtitle[39;49;00m;$
  2626^I^I^I [32mnextPut:[39;49;00m [33m$:[39;49;00m;$
  2627^I^I^I [32mspace[39;49;00m;$
  2628^I^I^I [32mtab[39;49;00m;$
  2629^I^I^I [32mprint:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m);$
  2630^I^I^I [32mcr[39;49;00m][34m! ![39;49;00m$
  2631^I$
  2632^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'tk 10/19/2001 11:18'![39;49;00m$
  2633^I[32mlongPrintOn:[39;49;00m [31maStream[39;49;00m [32mlimitedTo:[39;49;00m [31msizeLimit[39;49;00m [32mindent:[39;49;00m [31mindent[39;49;00m$
  2634^I^I[37m"Append to the argument, aStream, the names and values of all of the receiver's instance variables.  Limit is the length limit for each inst var."[39;49;00m$
  2635^I$
  2636^I^I[36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mdoWithIndex:[39;49;00m$
  2637^I^I^I[:[31mtitle[39;49;00m :[31mindex[39;49;00m |$
  2638^I^I^I[31mindent[39;49;00m [36mtimesRepeat:[39;49;00m [[31maStream[39;49;00m [32mtab[39;49;00m].$
  2639^I^I^I[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [31mtitle[39;49;00m;$
  2640^I^I^I [32mnextPut:[39;49;00m [33m$:[39;49;00m;$
  2641^I^I^I [32mspace[39;49;00m;$
  2642^I^I^I [32mtab[39;49;00m;$
  2643^I^I^I [32mnextPutAll:[39;49;00m $
  2644^I^I^I^I(([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m) [32mprintStringLimitedTo:[39;49;00m ([31msizeLimit[39;49;00m [32m-[39;49;00m[34m3[39;49;00m [32m-[39;49;00m[31mtitle[39;49;00m [32msize[39;49;00m [32mmax:[39;49;00m [34m1[39;49;00m));$
  2645^I^I^I [32mcr[39;49;00m][34m! ![39;49;00m$
  2646^I$
  2647^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'tk 10/16/2001 19:41'![39;49;00m$
  2648^I[32mlongPrintString[39;49;00m$
  2649^I^I[37m"Answer a String whose characters are a description of the receiver."[39;49;00m$
  2650^I^I$
  2651^I^I|[31m str [39;49;00m|$
  2652^I^I[31mstr[39;49;00m _ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [:[31maStream[39;49;00m | [36mself[39;49;00m [32mlongPrintOn:[39;49;00m [31maStream[39;49;00m].$
  2653^I^I[37m"Objects without inst vars should return something"[39;49;00m$
  2654^I^I^ [31mstr[39;49;00m [32misEmpty[39;49;00m [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [04m[32mString[39;49;00m [32mcr[39;49;00m] [36mifFalse:[39;49;00m [[31mstr[39;49;00m][34m! ![39;49;00m$
  2655^I$
  2656^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'BG 11/7/2004 13:39'![39;49;00m$
  2657^I[32mlongPrintStringLimitedTo:[39;49;00m [31maLimitValue[39;49;00m$
  2658^I^I[37m"Answer a String whose characters are a description of the receiver."[39;49;00m$
  2659^I^I$
  2660^I^I|[31m str [39;49;00m|$
  2661^I^I[31mstr[39;49;00m _ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [:[31maStream[39;49;00m | [36mself[39;49;00m [32mlongPrintOn:[39;49;00m [31maStream[39;49;00m [32mlimitedTo:[39;49;00m [31maLimitValue[39;49;00m [32mindent:[39;49;00m [34m0[39;49;00m].$
  2662^I^I[37m"Objects without inst vars should return something"[39;49;00m$
  2663^I^I^ [31mstr[39;49;00m [32misEmpty[39;49;00m [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [04m[32mString[39;49;00m [32mcr[39;49;00m] [36mifFalse:[39;49;00m [[31mstr[39;49;00m][34m! ![39;49;00m$
  2664^I$
  2665^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sw 3/7/2001 13:14'![39;49;00m$
  2666^I[32mnominallyUnsent:[39;49;00m [31maSelectorSymbol[39;49;00m$
  2667^I^I[37m"From within the body of a method which is not formally sent within the system, but which you intend to have remain in the system (for potential manual invocation, or for documentation, or perhaps because it's sent by commented-out-code that you anticipate uncommenting out someday, send this message, with the selector itself as the argument.[39;49;00m$
  2668^I[37m[39;49;00m$
  2669^I[37mThis will serve two purposes:[39;49;00m$
  2670^I[37m[39;49;00m$
  2671^I[37m^I(1)  The method will not be returned by searches for unsent selectors (because it, in a manner of speaking, sends itself).[39;49;00m$
  2672^I[37m^I(2)^IYou can locate all such methods by browsing senders of #nominallyUnsent:"[39;49;00m$
  2673^I$
  2674^I^I[36mfalse[39;49;00m [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mflag:[39;49;00m [33m#nominallyUnsent:[39;49;00m]    [37m"So that this method itself will appear to be sent"[39;49;00m$
  2675^I[34m! ![39;49;00m$
  2676^I$
  2677^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sma 6/1/2000 09:31'![39;49;00m$
  2678^I[32mprintOn:[39;49;00m [31maStream[39;49;00m$
  2679^I^I[37m"Append to the argument, aStream, a sequence of characters that  [39;49;00m$
  2680^I[37m^Iidentifies the receiver."[39;49;00m$
  2681^I$
  2682^I^I|[31m title [39;49;00m|$
  2683^I^I[31mtitle[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m.$
  2684^I^I[31maStream[39;49;00m$
  2685^I^I^I[32mnextPutAll:[39;49;00m ([31mtitle[39;49;00m [32mfirst[39;49;00m [32misVowel[39;49;00m [36mifTrue:[39;49;00m [[33m'an '[39;49;00m] [36mifFalse:[39;49;00m [[33m'a '[39;49;00m]);$
  2686^I^I^I[32mnextPutAll:[39;49;00m [31mtitle[39;49;00m[34m! ![39;49;00m$
  2687^I$
  2688^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sma 6/1/2000 09:22'![39;49;00m$
  2689^I[32mprintString[39;49;00m$
  2690^I^I[37m"Answer a String whose characters are a description of the receiver. [39;49;00m$
  2691^I[37m^IIf you want to print without a character limit, use fullPrintString."[39;49;00m$
  2692^I$
  2693^I^I^ [36mself[39;49;00m [32mprintStringLimitedTo:[39;49;00m [34m50000[39;49;00m[34m! ![39;49;00m$
  2694^I$
  2695^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'tk 5/7/1999 16:20'![39;49;00m$
  2696^I[32mprintStringLimitedTo:[39;49;00m [31mlimit[39;49;00m$
  2697^I^I[37m"Answer a String whose characters are a description of the receiver.[39;49;00m$
  2698^I[37m^IIf you want to print without a character limit, use fullPrintString."[39;49;00m$
  2699^I^I|[31m limitedString [39;49;00m|$
  2700^I^I[31mlimitedString[39;49;00m _ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [:[31ms[39;49;00m | [36mself[39;49;00m [32mprintOn:[39;49;00m [31ms[39;49;00m] [32mlimitedTo:[39;49;00m [31mlimit[39;49;00m.$
  2701^I^I[31mlimitedString[39;49;00m [32msize[39;49;00m [32m<[39;49;00m [31mlimit[39;49;00m [36mifTrue:[39;49;00m [^ [31mlimitedString[39;49;00m].$
  2702^I^I^ [31mlimitedString[39;49;00m [32m,[39;49;00m [33m'...etc...'[39;49;00m[34m! ![39;49;00m$
  2703^I$
  2704^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'MPW 1/1/1901 00:30'![39;49;00m$
  2705^I[32mpropertyList[39;49;00m$
  2706^I^I[37m"Answer a String whose characters are a property-list description of the receiver."[39;49;00m$
  2707^I$
  2708^I^I^ [04m[32mPropertyListEncoder[39;49;00m [32mprocess:[39;49;00m[36mself[39;49;00m.$
  2709^I[34m! ![39;49;00m$
  2710^I$
  2711^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sw 10/17/2000 11:16'![39;49;00m$
  2712^I[32mreportableSize[39;49;00m$
  2713^I^I[37m"Answer a string that reports the size of the receiver -- useful for showing in a list view, for example"[39;49;00m$
  2714^I$
  2715^I^I^ ([36mself[39;49;00m [32mbasicSize[39;49;00m [32m+[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m) [32mprintString[39;49;00m[34m! ![39;49;00m$
  2716^I$
  2717^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m![39;49;00m$
  2718^I[32mstoreOn:[39;49;00m [31maStream[39;49;00m $
  2719^I^I[37m"Append to the argument aStream a sequence of characters that is an [39;49;00m$
  2720^I[37m^Iexpression whose evaluation creates an object similar to the receiver."[39;49;00m$
  2721^I$
  2722^I^I[31maStream[39;49;00m [32mnextPut:[39;49;00m [33m$([39;49;00m.$
  2723^I^I[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m$
  2724^I^I^I[36mifTrue:[39;49;00m [[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [33m'('[39;49;00m[32m,[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m[32m,[39;49;00m [33m' basicNew: '[39;49;00m;$
  2725^I^I^I^I^I^I[32mstore:[39;49;00m [36mself[39;49;00m [32mbasicSize[39;49;00m;$
  2726^I^I^I^I^I^I[32mnextPutAll:[39;49;00m [33m') '[39;49;00m]$
  2727^I^I^I[36mifFalse:[39;49;00m [[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m[32m,[39;49;00m [33m' basicNew'[39;49;00m].$
  2728^I^I[34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mdo:[39;49;00m$
  2729^I^I^I[:[31mi[39;49;00m |$
  2730^I^I^I[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [33m' instVarAt: '[39;49;00m;$
  2731^I^I^I^I[32mstore:[39;49;00m [31mi[39;49;00m;$
  2732^I^I^I^I[32mnextPutAll:[39;49;00m [33m' put: '[39;49;00m;$
  2733^I^I^I^I[32mstore:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mi[39;49;00m);$
  2734^I^I^I^I[32mnextPut:[39;49;00m [33m$;[39;49;00m].$
  2735^I^I[34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32mbasicSize[39;49;00m [32mdo:[39;49;00m$
  2736^I^I^I[:[31mi[39;49;00m |$
  2737^I^I^I[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [33m' basicAt: '[39;49;00m;$
  2738^I^I^I^I[32mstore:[39;49;00m [31mi[39;49;00m;$
  2739^I^I^I^I[32mnextPutAll:[39;49;00m [33m' put: '[39;49;00m;$
  2740^I^I^I^I[32mstore:[39;49;00m ([36mself[39;49;00m [32mbasicAt:[39;49;00m [31mi[39;49;00m);$
  2741^I^I^I^I[32mnextPut:[39;49;00m [33m$;[39;49;00m].$
  2742^I^I[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [33m' yourself)'[39;49;00m$
  2743^I[34m! ![39;49;00m$
  2744^I$
  2745^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'di 6/20/97 09:12'![39;49;00m$
  2746^I[32mstoreString[39;49;00m$
  2747^I^I[37m"Answer a String representation of the receiver from which the receiver [39;49;00m$
  2748^I[37m^Ican be reconstructed."[39;49;00m$
  2749^I$
  2750^I^I^ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [:[31ms[39;49;00m | [36mself[39;49;00m [32mstoreOn:[39;49;00m [31ms[39;49;00m][34m! ![39;49;00m$
  2751^I$
  2752^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sw 5/2/1998 13:55'![39;49;00m$
  2753^I[32mstringForReadout[39;49;00m$
  2754^I^I^ [36mself[39;49;00m [32mstringRepresentation[39;49;00m[34m! ![39;49;00m$
  2755^I$
  2756^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m![39;49;00m$
  2757^I[32mstringRepresentation[39;49;00m$
  2758^I^I[37m"Answer a string that represents the receiver.  For most objects this is simply its printString, but for strings themselves, it's themselves.  6/12/96 sw"[39;49;00m$
  2759^I$
  2760^I^I^ [36mself[39;49;00m [32mprintString[39;49;00m [34m! ![39;49;00m$
  2761^I$
  2762^I$
  2763^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'ar 3/17/2001 20:11'![39;49;00m$
  2764^I[32madaptedToWorld:[39;49;00m [31maWorld[39;49;00m$
  2765^I^I[37m"If I refer to a world or a hand, return the corresponding items in the new world."[39;49;00m$
  2766^I^I^[36mself[39;49;00m[34m! ![39;49;00m$
  2767^I$
  2768^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'sw 3/10/2000 13:57'![39;49;00m$
  2769^I[32mdefaultFloatPrecisionFor:[39;49;00m [31maGetSelector[39;49;00m$
  2770^I^I[37m"Answer a number indicating the default float precision to be used in a numeric readout for which the receiver is the model."[39;49;00m$
  2771^I$
  2772^I^I^ [34m1[39;49;00m[34m! ![39;49;00m$
  2773^I$
  2774^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 3/9/2001 17:08'![39;49;00m$
  2775^I[32mevaluateUnloggedForSelf:[39;49;00m [31maCodeString[39;49;00m$
  2776^I$
  2777^I^I^[04m[32mCompiler[39;49;00m [32mevaluate:[39;49;00m$
  2778^I^I^I[31maCodeString[39;49;00m$
  2779^I^I^I[32mfor:[39;49;00m [36mself[39;49;00m$
  2780^I^I^I[32mlogged:[39;49;00m [36mfalse[39;49;00m[34m! ![39;49;00m$
  2781^I$
  2782^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'yo 12/25/2003 16:43'![39;49;00m$
  2783^I[32mmethodInterfacesForCategory:[39;49;00m [31maCategorySymbol[39;49;00m [32minVocabulary:[39;49;00m [31maVocabulary[39;49;00m [32mlimitClass:[39;49;00m [31maLimitClass[39;49;00m$
  2784^I^I[37m"Return a list of methodInterfaces for the receiver in the given category, given a vocabulary.  aCategorySymbol is the inherent category symbol, not necessarily the wording as expressed in the vocabulary."[39;49;00m$
  2785^I$
  2786^I^I|[31m categorySymbol [39;49;00m|$
  2787^I^I[31mcategorySymbol[39;49;00m _ [31maCategorySymbol[39;49;00m [32masSymbol[39;49;00m.$
  2788^I$
  2789^I^I([31mcategorySymbol[39;49;00m [32m==[39;49;00m [04m[32mScriptingSystem[39;49;00m [32mnameForInstanceVariablesCategory[39;49;00m) [36mifTrue:[39;49;00m [$
  2790^I^I^I[37m"user-defined instance variables"[39;49;00m$
  2791^I^I^I^ [36mself[39;49;00m [32mmethodInterfacesForInstanceVariablesCategoryIn:[39;49;00m [31maVocabulary[39;49;00m].$
  2792^I^I([31mcategorySymbol[39;49;00m [32m==[39;49;00m [04m[32mScriptingSystem[39;49;00m [32mnameForScriptsCategory[39;49;00m) [36mifTrue:[39;49;00m [$
  2793^I^I^I[37m"user-defined scripts"[39;49;00m$
  2794^I^I^I^ [36mself[39;49;00m [32mmethodInterfacesForScriptsCategoryIn:[39;49;00m [31maVocabulary[39;49;00m].$
  2795^I^I[37m"all others"[39;49;00m$
  2796^I^I^ [36mself[39;49;00m [32musableMethodInterfacesIn:[39;49;00m ([31maVocabulary[39;49;00m [32mmethodInterfacesInCategory:[39;49;00m [31mcategorySymbol[39;49;00m$
  2797^I^I^I[32mforInstance:[39;49;00m [36mself[39;49;00m$
  2798^I^I^I[32mofClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m$
  2799^I^I^I[32mlimitClass:[39;49;00m [31maLimitClass[39;49;00m)$
  2800^I[34m! ![39;49;00m$
  2801^I$
  2802^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'sw 8/3/2001 13:54'![39;49;00m$
  2803^I[32mmethodInterfacesForInstanceVariablesCategoryIn:[39;49;00m [31maVocabulary[39;49;00m$
  2804^I^I[37m"Return a collection of methodInterfaces for the instance-variables category.  The vocabulary parameter, at present anyway, is not used.  And for non-players, the method is at present vacuous in any case"[39;49;00m$
  2805^I$
  2806^I^I^  [04m[32mOrderedCollection[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
  2807^I$
  2808^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'sw 8/3/2001 13:53'![39;49;00m$
  2809^I[32mmethodInterfacesForScriptsCategoryIn:[39;49;00m [31maVocabulary[39;49;00m$
  2810^I^I[37m"Answer a list of method interfaces for the category #scripts, as seen in a viewer or other tool.  The vocabulary argument is not presently used.  Also, at present, only Players really do anyting interesting here."[39;49;00m$
  2811^I$
  2812^I^I^ [04m[32mOrderedCollection[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
  2813^I$
  2814^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 2/16/2001 19:37'![39;49;00m$
  2815^I[32mselfWrittenAsIll[39;49;00m$
  2816^I$
  2817^I^I^[36mself[39;49;00m[34m! ![39;49;00m$
  2818^I$
  2819^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 2/16/2001 19:38'![39;49;00m$
  2820^I[32mselfWrittenAsIm[39;49;00m$
  2821^I$
  2822^I^I^[36mself[39;49;00m[34m! ![39;49;00m$
  2823^I$
  2824^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 2/16/2001 19:37'![39;49;00m$
  2825^I[32mselfWrittenAsMe[39;49;00m$
  2826^I$
  2827^I^I^[36mself[39;49;00m[34m! ![39;49;00m$
  2828^I$
  2829^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 2/16/2001 19:37'![39;49;00m$
  2830^I[32mselfWrittenAsMy[39;49;00m$
  2831^I$
  2832^I^I^[36mself[39;49;00m[34m! ![39;49;00m$
  2833^I$
  2834^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 2/16/2001 19:38'![39;49;00m$
  2835^I[32mselfWrittenAsThis[39;49;00m$
  2836^I$
  2837^I^I^[36mself[39;49;00m[34m! ![39;49;00m$
  2838^I$
  2839^I$
  2840^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripts-kernel'[39;49;00m[34m stamp: 'nk 10/14/2004 10:55'![39;49;00m$
  2841^I[32muniversalTilesForGetterOf:[39;49;00m [31maMethodInterface[39;49;00m$
  2842^I^I[37m"Return universal tiles for a getter on the given method interface."[39;49;00m$
  2843^I$
  2844^I^I|[31m ms argTile argArray itsSelector [39;49;00m|$
  2845^I^I[31mitsSelector[39;49;00m _ [31maMethodInterface[39;49;00m [32mselector[39;49;00m.$
  2846^I^I[31margArray[39;49;00m _ [33m#([39;49;00m[33m)[39;49;00m.$
  2847^I$
  2848^I^I[37m"Four gratuituous special cases..."[39;49;00m$
  2849^I$
  2850^I^I([31mitsSelector[39;49;00m [32m==[39;49;00m [33m#color:sees:[39;49;00m) [36mifTrue:[39;49;00m$
  2851^I^I^I[[31margTile[39;49;00m _ [04m[32mScriptingSystem[39;49;00m [32mtileForArgType:[39;49;00m [33m#Color[39;49;00m.$
  2852^I^I^I[31margArray[39;49;00m _ [04m[32mArray[39;49;00m [32mwith:[39;49;00m [31margTile[39;49;00m [32mcolorSwatch[39;49;00m [32mcolor[39;49;00m [32mwith:[39;49;00m [31margTile[39;49;00m [32mcolorSwatch[39;49;00m [32mcolor[39;49;00m [32mcopy[39;49;00m].$
  2853^I$
  2854^I^I[31mitsSelector[39;49;00m [32m==[39;49;00m [33m#seesColor:[39;49;00m [36mifTrue:[39;49;00m$
  2855^I^I^I[[31margTile[39;49;00m _ [04m[32mScriptingSystem[39;49;00m [32mtileForArgType:[39;49;00m [33m#Color[39;49;00m.$
  2856^I^I^I[31margArray[39;49;00m _  [04m[32mArray[39;49;00m [32mwith:[39;49;00m [31margTile[39;49;00m [32mcolorSwatch[39;49;00m [32mcolor[39;49;00m].$
  2857^I$
  2858^I^I([33m#([39;49;00m[33mtouchesA:[39;49;00m [33moverlaps:[39;49;00m [33moverlapsAny:[39;49;00m[33m)[39;49;00m [32mincludes:[39;49;00m [31mitsSelector[39;49;00m) [36mifTrue:[39;49;00m$
  2859^I^I^I[[31margTile[39;49;00m _ [04m[32mScriptingSystem[39;49;00m [32mtileForArgType:[39;49;00m [33m#Player[39;49;00m.$
  2860^I^I^I[31margArray[39;49;00m _ [04m[32mArray[39;49;00m [32mwith:[39;49;00m [31margTile[39;49;00m [32mactualObject[39;49;00m].$
  2861^I$
  2862^I^I[31mms[39;49;00m _ [04m[32mMessageSend[39;49;00m [32mreceiver:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [31mitsSelector[39;49;00m [32marguments:[39;49;00m [31margArray[39;49;00m.$
  2863^I^I^ [31mms[39;49;00m [32masTilesIn:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mglobalNames:[39;49;00m ([36mself[39;49;00m [32mclass[39;49;00m [32mofficialClass[39;49;00m [32m~~[39;49;00m [04m[32mCardPlayer[39;49;00m)$
  2864^I^I^I^I[37m"For CardPlayers, use 'self'.  For others, name it, and use its name."[39;49;00m[34m! ![39;49;00m$
  2865^I$
  2866^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripts-kernel'[39;49;00m[34m stamp: 'tk 9/28/2001 13:30'![39;49;00m$
  2867^I[32muniversalTilesForInterface:[39;49;00m [31maMethodInterface[39;49;00m$
  2868^I^I[37m"Return universal tiles for the given method interface.  Record who self is."[39;49;00m$
  2869^I$
  2870^I^I|[31m ms argTile itsSelector aType argList [39;49;00m|$
  2871^I^I[31mitsSelector[39;49;00m _ [31maMethodInterface[39;49;00m [32mselector[39;49;00m.$
  2872^I^I[31margList[39;49;00m _ [04m[32mOrderedCollection[39;49;00m [36mnew[39;49;00m.$
  2873^I^I[31maMethodInterface[39;49;00m [32margumentVariables[39;49;00m [32mdoWithIndex:[39;49;00m$
  2874^I^I^I[:[31manArgumentVariable[39;49;00m :[31manIndex[39;49;00m | $
  2875^I^I^I^I[31margTile[39;49;00m _ [04m[32mScriptingSystem[39;49;00m [32mtileForArgType:[39;49;00m ([31maType[39;49;00m _ [31maMethodInterface[39;49;00m [32mtypeForArgumentNumber:[39;49;00m [31manIndex[39;49;00m).$
  2876^I^I^I^I[31margList[39;49;00m [32madd:[39;49;00m ([31maType[39;49;00m [32m==[39;49;00m [33m#Player[39;49;00m $
  2877^I^I^I^I^I[36mifTrue:[39;49;00m [[31margTile[39;49;00m [32mactualObject[39;49;00m]$
  2878^I^I^I^I^I[36mifFalse:[39;49;00m [[31margTile[39;49;00m [32mliteral[39;49;00m]).^I[37m"default value for each type"[39;49;00m].$
  2879^I$
  2880^I^I[31mms[39;49;00m _ [04m[32mMessageSend[39;49;00m [32mreceiver:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [31mitsSelector[39;49;00m [32marguments:[39;49;00m [31margList[39;49;00m [32masArray[39;49;00m.$
  2881^I^I^ [31mms[39;49;00m [32masTilesIn:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mglobalNames:[39;49;00m ([36mself[39;49;00m [32mclass[39;49;00m [32mofficialClass[39;49;00m [32m~~[39;49;00m [04m[32mCardPlayer[39;49;00m)$
  2882^I^I^I^I[37m"For CardPlayers, use 'self'.  For others, name it, and use its name."[39;49;00m[34m! ![39;49;00m$
  2883^I$
  2884^I$
  2885^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'self evaluating'[39;49;00m[34m stamp: 'sd 7/31/2005 21:47'![39;49;00m$
  2886^I[32misSelfEvaluating[39;49;00m$
  2887^I^I^ [36mself[39;49;00m [32misLiteral[39;49;00m[34m! ![39;49;00m$
  2888^I$
  2889^I$
  2890^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m![39;49;00m$
  2891^I[32masOop[39;49;00m$
  2892^I^I[37m"Primitive. Answer a SmallInteger whose value is half of the receiver's [39;49;00m$
  2893^I[37m^Iobject pointer (interpreting object pointers as 16-bit signed quantities). [39;49;00m$
  2894^I[37m^IFail if the receiver is a SmallInteger. Essential. See Object documentation [39;49;00m$
  2895^I[37m^IwhatIsAPrimitive."[39;49;00m$
  2896^I$
  2897^I^I<[34mprimitive:[39;49;00m 75>$
  2898^I^I[36mself[39;49;00m [32mprimitiveFailed[39;49;00m[34m! ![39;49;00m$
  2899^I$
  2900^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'di 1/9/1999 15:19'![39;49;00m$
  2901^I[32mbecomeForward:[39;49;00m [31motherObject[39;49;00m $
  2902^I^I[37m"Primitive. All variables in the entire system that used to point[39;49;00m$
  2903^I[37m^Ito the receiver now point to the argument.[39;49;00m$
  2904^I[37m^IFails if either argument is a SmallInteger."[39;49;00m$
  2905^I$
  2906^I^I([04m[32mArray[39;49;00m [32mwith:[39;49;00m [36mself[39;49;00m)$
  2907^I^I^I[32melementsForwardIdentityTo:[39;49;00m$
  2908^I^I^I^I([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31motherObject[39;49;00m)[34m! ![39;49;00m$
  2909^I$
  2910^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'zz 3/3/2004 23:53'![39;49;00m$
  2911^I[32mbecomeForward:[39;49;00m [31motherObject[39;49;00m [32mcopyHash:[39;49;00m [31mcopyHash[39;49;00m$
  2912^I^I[37m"Primitive. All variables in the entire system that used to point to the receiver now point to the argument.[39;49;00m$
  2913^I[37m^IIf copyHash is true, the argument's identity hash bits will be set to those of the receiver.[39;49;00m$
  2914^I[37m^IFails if either argument is a SmallInteger."[39;49;00m$
  2915^I$
  2916^I^I([04m[32mArray[39;49;00m [32mwith:[39;49;00m [36mself[39;49;00m)$
  2917^I^I^I[32melementsForwardIdentityTo:[39;49;00m$
  2918^I^I^I^I([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31motherObject[39;49;00m)$
  2919^I^I^I^I^I[32mcopyHash:[39;49;00m [31mcopyHash[39;49;00m[34m! ![39;49;00m$
  2920^I$
  2921^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'sw 10/16/2000 10:59'![39;49;00m$
  2922^I[32mclassName[39;49;00m$
  2923^I^I[37m"Answer a string characterizing the receiver's class, for use in list views for example"[39;49;00m$
  2924^I$
  2925^I^I^ [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32masString[39;49;00m[34m! ![39;49;00m$
  2926^I$
  2927^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'sw 10/16/2000 11:04'![39;49;00m$
  2928^I[32mcreationStamp[39;49;00m$
  2929^I^I[37m"Answer a string which reports the creation particulars of the receiver.  Intended perhaps for list views, but this is presently a feature not easily accessible"[39;49;00m$
  2930^I$
  2931^I^I^ [33m'<no creation stamp>'[39;49;00m[34m! ![39;49;00m$
  2932^I$
  2933^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m![39;49;00m$
  2934^I[32minstVarAt:[39;49;00m [31mindex[39;49;00m $
  2935^I^I[37m"Primitive. Answer a fixed variable in an object. The numbering of the [39;49;00m$
  2936^I[37m^Ivariables corresponds to the named instance variables. Fail if the index [39;49;00m$
  2937^I[37m^Iis not an Integer or is not the index of a fixed variable. Essential. See [39;49;00m$
  2938^I[37m^IObject documentation whatIsAPrimitive."[39;49;00m$
  2939^I$
  2940^I^I<[34mprimitive:[39;49;00m 73>$
  2941^I^I[37m"Access beyond fixed variables."[39;49;00m$
  2942^I^I^[36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32m-[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m^I^I[34m! ![39;49;00m$
  2943^I$
  2944^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m![39;49;00m$
  2945^I[32minstVarAt:[39;49;00m [31manInteger[39;49;00m [32mput:[39;49;00m [31manObject[39;49;00m $
  2946^I^I[37m"Primitive. Store a value into a fixed variable in the receiver. The [39;49;00m$
  2947^I[37m^Inumbering of the variables corresponds to the named instance variables. [39;49;00m$
  2948^I[37m^IFail if the index is not an Integer or is not the index of a fixed variable. [39;49;00m$
  2949^I[37m^IAnswer the value stored as the result. Using this message violates the [39;49;00m$
  2950^I[37m^Iprinciple that each object has sovereign control over the storing of [39;49;00m$
  2951^I[37m^Ivalues into its instance variables. Essential. See Object documentation [39;49;00m$
  2952^I[37m^IwhatIsAPrimitive."[39;49;00m$
  2953^I$
  2954^I^I<[34mprimitive:[39;49;00m 74>$
  2955^I^I[37m"Access beyond fixed fields"[39;49;00m$
  2956^I^I^[36mself[39;49;00m [32mbasicAt:[39;49;00m [31manInteger[39;49;00m [32m-[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mput:[39;49;00m [31manObject[39;49;00m[34m! ![39;49;00m$
  2957^I$
  2958^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'sw 10/16/2000 11:09'![39;49;00m$
  2959^I[32minstVarNamed:[39;49;00m [31maString[39;49;00m$
  2960^I^I[37m"Return the value of the instance variable in me with that name.  Slow and unclean, but very useful. "[39;49;00m$
  2961^I$
  2962^I^I^ [36mself[39;49;00m [32minstVarAt:[39;49;00m ([36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mindexOf:[39;49;00m [31maString[39;49;00m [32masString[39;49;00m)$
  2963^I$
  2964^I$
  2965^I[34m! ![39;49;00m$
  2966^I$
  2967^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'sw 10/16/2000 11:10'![39;49;00m$
  2968^I[32minstVarNamed:[39;49;00m [31maString[39;49;00m [32mput:[39;49;00m [31maValue[39;49;00m$
  2969^I^I[37m"Store into the value of the instance variable in me of that name.  Slow and unclean, but very useful. "[39;49;00m$
  2970^I$
  2971^I^I^ [36mself[39;49;00m [32minstVarAt:[39;49;00m ([36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mindexOf:[39;49;00m [31maString[39;49;00m [32masString[39;49;00m) [32mput:[39;49;00m [31maValue[39;49;00m$
  2972^I[34m! ![39;49;00m$
  2973^I$
  2974^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'sw 10/17/2000 11:12'![39;49;00m$
  2975^I[32moopString[39;49;00m$
  2976^I^I[37m"Answer a string that represents the oop of the receiver"[39;49;00m$
  2977^I$
  2978^I^I^ [36mself[39;49;00m [32masOop[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
  2979^I$
  2980^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'ar 3/2/2001 01:34'![39;49;00m$
  2981^I[32mprimitiveChangeClassTo:[39;49;00m [31manObject[39;49;00m$
  2982^I^I[37m"Primitive. Change the class of the receiver into the class of the argument given that the format of the receiver matches the format of the argument's class. Fail if receiver or argument are SmallIntegers, or the receiver is an instance of a compact class and the argument isn't, or when the argument's class is compact and the receiver isn't, or when the format of the receiver is different from the format of the argument's class, or when the arguments class is fixed and the receiver's size differs from the size that an instance of the argument's class should have.[39;49;00m$
  2983^I[37m^INote: The primitive will fail in most cases that you think might work. This is mostly because of a) the difference between compact and non-compact classes, and b) because of differences in the format. As an example, '(Array new: 3) primitiveChangeClassTo: Morph basicNew' would fail for three of the reasons mentioned above. Array is compact, Morph is not (failure #1). Array is variable and Morph is fixed (different format - failure #2). Morph is a fixed-field-only object and the array is too short (failure #3).[39;49;00m$
  2984^I[37m^IThe facility is really provided for certain, very specific applications (mostly related to classes changing shape) and not for casual use."[39;49;00m$
  2985^I$
  2986^I^I<[34mprimitive:[39;49;00m 115>$
  2987^I^I[36mself[39;49;00m [32mprimitiveFailed[39;49;00m[34m! ![39;49;00m$
  2988^I$
  2989^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'di 3/27/1999 12:21'![39;49;00m$
  2990^I[32mrootStubInImageSegment:[39;49;00m [31mimageSegment[39;49;00m$
  2991^I$
  2992^I^I^ [04m[32mImageSegmentRootStub[39;49;00m [36mnew[39;49;00m$
  2993^I^I^I[32mxxSuperclass:[39;49;00m [36mnil[39;49;00m$
  2994^I^I^I[32mformat:[39;49;00m [36mnil[39;49;00m$
  2995^I^I^I[32msegment:[39;49;00m [31mimageSegment[39;49;00m[34m! ![39;49;00m$
  2996^I$
  2997^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m![39;49;00m$
  2998^I[32msomeObject[39;49;00m$
  2999^I^I[37m"Primitive. Answer the first object in the enumeration of all[39;49;00m$
  3000^I[37m^I objects."[39;49;00m$
  3001^I$
  3002^I^I<[34mprimitive:[39;49;00m 138>$
  3003^I^I[36mself[39;49;00m [32mprimitiveFailed[39;49;00m.[34m! ![39;49;00m$
  3004^I$
  3005^I$
  3006^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 9/26/2001 11:58'![39;49;00m$
  3007^I[32mbasicType[39;49;00m$
  3008^I^I[37m"Answer a symbol representing the inherent type of the receiver"[39;49;00m$
  3009^I$
  3010^I^I^ [33m#Object[39;49;00m[34m! ![39;49;00m$
  3011^I$
  3012^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 5/3/2001 16:19'![39;49;00m$
  3013^I[32mbeViewed[39;49;00m$
  3014^I^I[37m"Open up a viewer on the receiver.  The Presenter is invited to decide just how to present this viewer"[39;49;00m$
  3015^I$
  3016^I^I[36mself[39;49;00m [32muniqueNameForReference[39;49;00m.  [37m"So the viewer will have something nice to refer to"[39;49;00m$
  3017^I^I[36mself[39;49;00m [32mpresenter[39;49;00m [32mviewObject:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  3018^I$
  3019^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/16/2000 11:01'![39;49;00m$
  3020^I[32mcostumes[39;49;00m$
  3021^I^I[37m"Answer a list of costumes associated with the receiver.  The appearance of this method in class Object serves only as a backstop, probably only transitionally"[39;49;00m$
  3022^I$
  3023^I^I^ [36mnil[39;49;00m[34m! ![39;49;00m$
  3024^I$
  3025^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 1/12/98 18:09'![39;49;00m$
  3026^I[31mhaltIfNil[39;49;00m[34m! ![39;49;00m$
  3027^I$
  3028^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 1/20/2006 17:09'![39;49;00m$
  3029^I[32mhasLiteralSuchThat:[39;49;00m [31mtestBlock[39;49;00m$
  3030^I^I[37m"This is the end of the imbedded structure path so return false."[39;49;00m$
  3031^I$
  3032^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3033^I$
  3034^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 1/20/2006 17:10'![39;49;00m$
  3035^I[32mhasLiteralThorough:[39;49;00m [31mliteral[39;49;00m$
  3036^I^I[37m"Answer true if literal is identical to any literal in this array, even if imbedded in further structures.  This is the end of the imbedded structure path so return false."[39;49;00m$
  3037^I$
  3038^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3039^I$
  3040^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 1/30/2001 22:24'![39;49;00m$
  3041^I[32mhaveFullProtocolBrowsed[39;49;00m$
  3042^I^I[37m"Open up a Lexicon on the receiver"[39;49;00m$
  3043^I$
  3044^I^I^ [36mself[39;49;00m [32mhaveFullProtocolBrowsedShowingSelector:[39;49;00m [36mnil[39;49;00m$
  3045^I$
  3046^I^I[37m"(2@3) haveFullProtocolBrowsed"[39;49;00m$
  3047^I[34m! ![39;49;00m$
  3048^I$
  3049^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 9/27/2005 21:04'![39;49;00m$
  3050^I[32mhaveFullProtocolBrowsedShowingSelector:[39;49;00m [31maSelector[39;49;00m$
  3051^I^I[37m"Open up a Lexicon on the receiver, having it open up showing aSelector, which may be nil"[39;49;00m$
  3052^I$
  3053^I^I|[31m aBrowser [39;49;00m|$
  3054^I^I[31maBrowser[39;49;00m := ([04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#InstanceBrowser[39;49;00m [32mifAbsent:[39;49;00m[^[36mnil[39;49;00m]) [36mnew[39;49;00m [32museVocabulary:[39;49;00m [04m[32mVocabulary[39;49;00m [32mfullVocabulary[39;49;00m.$
  3055^I^I[31maBrowser[39;49;00m [32mopenOnObject:[39;49;00m [36mself[39;49;00m [32minWorld:[39;49;00m [04m[32mActiveWorld[39;49;00m [32mshowingSelector:[39;49;00m [31maSelector[39;49;00m$
  3056^I$
  3057^I^I[37m"(2@3) haveFullProtocolBrowsed"[39;49;00m[34m! ![39;49;00m$
  3058^I$
  3059^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 7/30/2005 21:21'![39;49;00m$
  3060^I[32misArray[39;49;00m$
  3061^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3062^I$
  3063^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 7/9/1999 18:18'![39;49;00m$
  3064^I[32misBehavior[39;49;00m$
  3065^I^I[37m"Return true if the receiver is a behavior.[39;49;00m$
  3066^I[37m^INote: Do not override in any class except behavior."[39;49;00m$
  3067^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3068^I$
  3069^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ajh 1/21/2003 13:15'![39;49;00m$
  3070^I[32misBlock[39;49;00m$
  3071^I$
  3072^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3073^I$
  3074^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 11/21/2003 12:14'![39;49;00m$
  3075^I[32misBlockClosure[39;49;00m$
  3076^I$
  3077^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3078^I$
  3079^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'yo 8/28/2002 13:41'![39;49;00m$
  3080^I[32misCharacter[39;49;00m$
  3081^I$
  3082^I^I^ [36mfalse[39;49;00m.$
  3083^I[34m! ![39;49;00m$
  3084^I$
  3085^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 8/17/1999 19:43'![39;49;00m$
  3086^I[32misCollection[39;49;00m$
  3087^I^I[37m"Return true if the receiver is some sort of Collection and responds to basic collection messages such as #size and #do:"[39;49;00m$
  3088^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3089^I$
  3090^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
  3091^I[32misColor[39;49;00m$
  3092^I^I[37m"Answer true if receiver is a Color. False by default."[39;49;00m$
  3093^I$
  3094^I^I^ [36mfalse[39;49;00m$
  3095^I[34m! ![39;49;00m$
  3096^I$
  3097^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'nk 4/17/2004 19:43'![39;49;00m$
  3098^I[32misColorForm[39;49;00m$
  3099^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3100^I$
  3101^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 11/21/2003 12:14'![39;49;00m$
  3102^I[32misCompiledMethod[39;49;00m$
  3103^I$
  3104^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3105^I$
  3106^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'mk 10/27/2003 17:33'![39;49;00m$
  3107^I[32misComplex[39;49;00m$
  3108^I^I[37m"Answer true if receiver is a Complex number. False by default."[39;49;00m$
  3109^I$
  3110^I^I^ [36mfalse[39;49;00m$
  3111^I[34m! ![39;49;00m$
  3112^I$
  3113^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 8/11/2005 16:45'![39;49;00m$
  3114^I[32misDictionary[39;49;00m$
  3115^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3116^I$
  3117^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'di 11/9/1998 09:38'![39;49;00m$
  3118^I[32misFloat[39;49;00m$
  3119^I^I[37m"Overridden to return true in Float, natch"[39;49;00m$
  3120^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3121^I$
  3122^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 10/30/2000 23:22'![39;49;00m$
  3123^I[32misForm[39;49;00m$
  3124^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3125^I$
  3126^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'len 1/13/98 21:18'![39;49;00m$
  3127^I[32misFraction[39;49;00m$
  3128^I^I[37m"Answer true if the receiver is a Fraction."[39;49;00m$
  3129^I$
  3130^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3131^I$
  3132^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'rhi 8/14/2003 08:51'![39;49;00m$
  3133^I[32misHeap[39;49;00m$
  3134^I$
  3135^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3136^I$
  3137^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
  3138^I[32misInteger[39;49;00m$
  3139^I^I[37m"Overridden to return true in Integer."[39;49;00m$
  3140^I$
  3141^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3142^I$
  3143^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'rhi 8/12/2003 09:52'![39;49;00m$
  3144^I[32misInterval[39;49;00m$
  3145^I$
  3146^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3147^I$
  3148^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'nk 4/25/2002 08:04'![39;49;00m$
  3149^I[32misMessageSend[39;49;00m$
  3150^I^I^[36mfalse[39;49;00m$
  3151^I[34m! ![39;49;00m$
  3152^I$
  3153^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 2/19/2006 11:24'![39;49;00m$
  3154^I[32misMethodProperties[39;49;00m$
  3155^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3156^I$
  3157^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
  3158^I[32misMorph[39;49;00m$
  3159^I$
  3160^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3161^I$
  3162^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 9/13/2000 15:37'![39;49;00m$
  3163^I[32misMorphicEvent[39;49;00m$
  3164^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3165^I$
  3166^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'gm 2/22/2003 12:56'![39;49;00m$
  3167^I[32misMorphicModel[39;49;00m$
  3168^I^I[37m"Return true if the receiver is a morphic model"[39;49;00m$
  3169^I^I^[36mfalse[39;49;00m$
  3170^I[34m! ![39;49;00m$
  3171^I$
  3172^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
  3173^I[32misNumber[39;49;00m$
  3174^I^I[37m"Overridden to return true in Number, natch"[39;49;00m$
  3175^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3176^I$
  3177^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'di 11/6/1998 08:04'![39;49;00m$
  3178^I[32misPoint[39;49;00m$
  3179^I^I[37m"Overridden to return true in Point."[39;49;00m$
  3180^I$
  3181^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3182^I$
  3183^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ikp 9/26/97 14:45'![39;49;00m$
  3184^I[32misPseudoContext[39;49;00m$
  3185^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3186^I$
  3187^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 10/2/2005 21:52'![39;49;00m$
  3188^I[32misRectangle[39;49;00m$
  3189^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3190^I$
  3191^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'nk 6/14/2004 16:49'![39;49;00m$
  3192^I[32misSketchMorph[39;49;00m$
  3193^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3194^I$
  3195^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 12/23/1999 15:43'![39;49;00m$
  3196^I[32misStream[39;49;00m$
  3197^I^I[37m"Return true if the receiver responds to the stream protocol"[39;49;00m$
  3198^I^I^[36mfalse[39;49;00m$
  3199^I[34m! ![39;49;00m$
  3200^I$
  3201^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sma 6/15/2000 15:48'![39;49;00m$
  3202^I[32misString[39;49;00m$
  3203^I^I[37m"Overridden to return true in String, natch"[39;49;00m$
  3204^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3205^I$
  3206^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 4/30/2003 15:30'![39;49;00m$
  3207^I[32misSymbol[39;49;00m$
  3208^I^I^ [36mfalse[39;49;00m [34m! ![39;49;00m$
  3209^I$
  3210^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'jam 3/9/2003 15:10'![39;49;00m$
  3211^I[32misSystemWindow[39;49;00m$
  3212^I[37m"answer whatever the receiver is a SystemWindow"[39;49;00m$
  3213^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3214^I$
  3215^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
  3216^I[32misText[39;49;00m$
  3217^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3218^I$
  3219^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'pmm 7/6/2006 20:46'![39;49;00m$
  3220^I[32misTrait[39;49;00m$
  3221^I^I[37m"Return true if the receiver is a trait.[39;49;00m$
  3222^I[37m^INote: Do not override in any class except TraitBehavior."[39;49;00m$
  3223^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3224^I$
  3225^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'tk 10/21/97 12:45'![39;49;00m$
  3226^I[32misTransparent[39;49;00m$
  3227^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3228^I$
  3229^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 8/14/2001 23:19'![39;49;00m$
  3230^I[32misVariableBinding[39;49;00m$
  3231^I^I[37m"Return true if I represent a literal variable binding"[39;49;00m$
  3232^I^I^[36mfalse[39;49;00m$
  3233^I^I[34m! ![39;49;00m$
  3234^I$
  3235^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ls 7/14/1998 21:45'![39;49;00m$
  3236^I[32misWebBrowser[39;49;00m$
  3237^I^I[37m"whether this object is a web browser.  See class: Scamper"[39;49;00m$
  3238^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3239^I$
  3240^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/27/2000 06:58'![39;49;00m$
  3241^I[32mknownName[39;49;00m$
  3242^I^I[37m"If a formal name has been handed out for this object, answer it, else nil"[39;49;00m$
  3243^I^I$
  3244^I^I^ [04m[32mPreferences[39;49;00m [32mcapitalizedReferences[39;49;00m$
  3245^I^I^I[36mifTrue:[39;49;00m$
  3246^I^I^I^I[[04m[32mReferences[39;49;00m [32mkeyAtValue:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m]]$
  3247^I^I^I[36mifFalse:[39;49;00m$
  3248^I^I^I^I[[36mnil[39;49;00m][34m! ![39;49;00m$
  3249^I$
  3250^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 9/27/96'![39;49;00m$
  3251^I[32mname[39;49;00m$
  3252^I^I[37m"Answer a name for the receiver.  This is used generically in the title of certain inspectors, such as the referred-to inspector, and specificially by various subsystems.  By default, we let the object just print itself out..  "[39;49;00m$
  3253^I$
  3254^I^I^ [36mself[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
  3255^I$
  3256^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 11/19/2001 13:28'![39;49;00m$
  3257^I[32mnameForViewer[39;49;00m$
  3258^I^I[37m"Answer a name to be shown in a Viewer that is viewing the receiver"[39;49;00m$
  3259^I$
  3260^I^I|[31m aName [39;49;00m|$
  3261^I^I([31maName[39;49;00m _ [36mself[39;49;00m [32muniqueNameForReferenceOrNil[39;49;00m) [32mifNotNil:[39;49;00m [^ [31maName[39;49;00m].$
  3262^I^I([31maName[39;49;00m _ [36mself[39;49;00m [32mknownName[39;49;00m) [32mifNotNil:[39;49;00m [^ [31maName[39;49;00m].$
  3263^I$
  3264^I^I^ [([36mself[39;49;00m [32masString[39;49;00m [32mcopyWithout:[39;49;00m [04m[32mCharacter[39;49;00m [32mcr[39;49;00m) [32mtruncateTo:[39;49;00m  [34m27[39;49;00m] [32mifError:[39;49;00m$
  3265^I^I^I[:[31mmsg[39;49;00m :[31mrcvr[39;49;00m | ^ [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32mprintString[39;49;00m][34m! ![39;49;00m$
  3266^I$
  3267^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
  3268^I[32mnotNil[39;49;00m$
  3269^I^I[37m"Coerces nil to false and everything else to true."[39;49;00m$
  3270^I$
  3271^I^I^[36mtrue[39;49;00m[34m! ![39;49;00m$
  3272^I$
  3273^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'tk 9/6/2001 19:15'![39;49;00m$
  3274^I[32mopenInstanceBrowserWithTiles[39;49;00m$
  3275^I^I[37m"Open up an instance browser on me with tiles as the code type, and with the search level as desired."[39;49;00m$
  3276^I$
  3277^I^I|[31m aBrowser [39;49;00m|$
  3278^I^I[31maBrowser[39;49;00m _ [04m[32mInstanceBrowser[39;49;00m [36mnew[39;49;00m.$
  3279^I^I[31maBrowser[39;49;00m [32museVocabulary:[39;49;00m [04m[32mVocabulary[39;49;00m [32mfullVocabulary[39;49;00m.$
  3280^I^I[31maBrowser[39;49;00m [32mlimitClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m.$
  3281^I^I[31maBrowser[39;49;00m [32mcontentsSymbol:[39;49;00m [33m#tiles[39;49;00m.^I^I[37m"preset it to make extra buttons (tile menus)"[39;49;00m$
  3282^I^I[31maBrowser[39;49;00m [32mopenOnObject:[39;49;00m [36mself[39;49;00m [32minWorld:[39;49;00m [04m[32mActiveWorld[39;49;00m [32mshowingSelector:[39;49;00m [36mnil[39;49;00m.$
  3283^I^I[31maBrowser[39;49;00m [32mcontentsSymbol:[39;49;00m [33m#source[39;49;00m.$
  3284^I^I[31maBrowser[39;49;00m [32mtoggleShowingTiles[39;49;00m.$
  3285^I$
  3286^I^I[37m"[39;49;00m$
  3287^I[37m(2@3) openInstanceBrowserWithTiles.[39;49;00m$
  3288^I[37mWatchMorph new openInstanceBrowserWithTiles[39;49;00m$
  3289^I[37m"[39;49;00m[34m! ![39;49;00m$
  3290^I$
  3291^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'tk 7/28/2005 04:50'![39;49;00m$
  3292^I[32mrenameInternal:[39;49;00m [31mnewName[39;49;00m $
  3293^I^I[37m"Change the internal name (because of a conflict) but leave the external name unchanged.  Change Player class name, but do not change the names that appear in tiles.  Any object that might be pointed to in the References dictionary might get this message sent to it upon reload"[39;49;00m$
  3294^I$
  3295^I^I^ [36mnil[39;49;00m^I[37m"caller will renameTo:.  new name may be different"[39;49;00m[34m! ![39;49;00m$
  3296^I$
  3297^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 2/27/2002 14:55'![39;49;00m$
  3298^I[32mrenameTo:[39;49;00m [31mnewName[39;49;00m$
  3299^I^I[37m"If the receiver has an inherent idea about its own name, it should take action here.  Any object that might be pointed to in the References dictionary might get this message sent to it upon reload"[39;49;00m[34m! ![39;49;00m$
  3300^I$
  3301^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 1/18/2001 13:43'![39;49;00m$
  3302^I[32mshowDiffs[39;49;00m$
  3303^I^I[37m"Answer whether the receiver, serving as the model of a text-bearing entity, is 'showing differences' -- if it is, the editor may wish to show special feedback"[39;49;00m$
  3304^I$
  3305^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3306^I$
  3307^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/20/1999 14:52'![39;49;00m$
  3308^I[32mstepAt:[39;49;00m [31mmillisecondClockValue[39;49;00m [32min:[39;49;00m [31maWindow[39;49;00m$
  3309^I$
  3310^I^I^ [36mself[39;49;00m [32mstepIn:[39;49;00m [31maWindow[39;49;00m[34m! ![39;49;00m$
  3311^I$
  3312^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/19/1999 08:16'![39;49;00m$
  3313^I[32mstepIn:[39;49;00m [31maWindow[39;49;00m$
  3314^I$
  3315^I^I^ [36mself[39;49;00m [32mstep[39;49;00m[34m! ![39;49;00m$
  3316^I$
  3317^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/19/1999 08:21'![39;49;00m$
  3318^I[32mstepTime[39;49;00m$
  3319^I^I$
  3320^I^I^ [34m1000[39;49;00m [37m"milliseconds -- default backstop for objects serving as models of system windows"[39;49;00m[34m! ![39;49;00m$
  3321^I$
  3322^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/19/1999 08:22'![39;49;00m$
  3323^I[32mstepTimeIn:[39;49;00m [31maSystemWindow[39;49;00m$
  3324^I^I$
  3325^I^I^ [34m1000[39;49;00m [37m"milliseconds -- default backstop for objects serving as models of system windows"[39;49;00m[34m! ![39;49;00m$
  3326^I$
  3327^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 5/3/2001 18:22'![39;49;00m$
  3328^I[32mvocabularyDemanded[39;49;00m$
  3329^I^I[37m"Answer a vocabulary that the receiver insists be used when it is looked at in a Viewer.  This allows specific classes to insist on specific custom vocabularies"[39;49;00m$
  3330^I$
  3331^I^I^ [36mnil[39;49;00m[34m! ![39;49;00m$
  3332^I$
  3333^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 11/13/2001 07:26'![39;49;00m$
  3334^I[32mwantsDiffFeedback[39;49;00m$
  3335^I^I[37m"Answer whether the receiver, serving as the model of a text-bearing entity, would like for 'diffs' green pane-border feedback to be shown"[39;49;00m$
  3336^I$
  3337^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3338^I$
  3339^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'di 1/8/1999 15:04'![39;49;00m$
  3340^I[32mwantsSteps[39;49;00m$
  3341^I^I[37m"Overridden by morphic classes whose instances want to be stepped,[39;49;00m$
  3342^I[37m^Ior by model classes who want their morphic views to be stepped."[39;49;00m$
  3343^I$
  3344^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3345^I$
  3346^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/19/1999 08:26'![39;49;00m$
  3347^I[32mwantsStepsIn:[39;49;00m [31maSystemWindow[39;49;00m$
  3348^I^I$
  3349^I^I^ [36mself[39;49;00m [32mwantsSteps[39;49;00m[34m! ![39;49;00m$
  3350^I$
  3351^I$
  3352^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'thumbnail'[39;49;00m[34m stamp: 'dgd 9/25/2004 23:17'![39;49;00m$
  3353^I[32miconOrThumbnailOfSize:[39;49;00m [31maNumberOrPoint[39;49;00m $
  3354^I^I[37m"Answer an appropiate form to represent the receiver"[39;49;00m$
  3355^I^I^ [36mnil[39;49;00m[34m! ![39;49;00m$
  3356^I$
  3357^I$
  3358^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'translation support'[39;49;00m[34m![39;49;00m$
  3359^I[32minline:[39;49;00m [31minlineFlag[39;49;00m$
  3360^I^I[37m"For translation only; noop when running in Smalltalk."[39;49;00m[34m! ![39;49;00m$
  3361^I$
  3362^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'translation support'[39;49;00m[34m![39;49;00m$
  3363^I[32mvar:[39;49;00m [31mvarSymbol[39;49;00m [32mdeclareC:[39;49;00m [31mdeclString[39;49;00m$
  3364^I^I[37m"For translation only; noop when running in Smalltalk."[39;49;00m[34m! ![39;49;00m$
  3365^I$
  3366^I$
  3367^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/11/2000 20:32'![39;49;00m$
  3368^I[32mcapturedState[39;49;00m$
  3369^I^I[37m"May be overridden in subclasses."[39;49;00m$
  3370^I$
  3371^I^I^ [36mself[39;49;00m [32mshallowCopy[39;49;00m$
  3372^I[34m! ![39;49;00m$
  3373^I$
  3374^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/11/2000 20:29'![39;49;00m$
  3375^I[32mcommandHistory[39;49;00m$
  3376^I^I[37m"Return the command history for the receiver"[39;49;00m$
  3377^I^I|[31m w [39;49;00m|$
  3378^I^I([31mw[39;49;00m _ [36mself[39;49;00m [32mcurrentWorld[39;49;00m) [32mifNotNil:[39;49;00m [^ [31mw[39;49;00m [32mcommandHistory[39;49;00m].$
  3379^I^I^ [04m[32mCommandHistory[39;49;00m [36mnew[39;49;00m. [37m"won't really record anything but prevent breaking things"[39;49;00m[34m! ![39;49;00m$
  3380^I$
  3381^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 12/12/2000 15:01'![39;49;00m$
  3382^I[32mpurgeAllCommands[39;49;00m$
  3383^I^I[37m"Purge all commands for this object"[39;49;00m$
  3384^I^I[04m[32mPreferences[39;49;00m [32museUndo[39;49;00m [36mifFalse:[39;49;00m [^ [36mself[39;49;00m]. [37m"get out quickly"[39;49;00m$
  3385^I^I[36mself[39;49;00m [32mcommandHistory[39;49;00m [32mpurgeAllCommandsSuchThat:[39;49;00m [:[31mcmd[39;49;00m | [31mcmd[39;49;00m [32mundoTarget[39;49;00m [32m==[39;49;00m [36mself[39;49;00m].$
  3386^I[34m! ![39;49;00m$
  3387^I$
  3388^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/12/2000 08:15'![39;49;00m$
  3389^I[32mredoFromCapturedState:[39;49;00m [31mst[39;49;00m $
  3390^I^I[37m"May be overridden in subclasses.  See also capturedState"[39;49;00m$
  3391^I$
  3392^I^I[36mself[39;49;00m [32mundoFromCapturedState:[39;49;00m [31mst[39;49;00m  [37m"Simple cases are symmetric"[39;49;00m$
  3393^I[34m! ![39;49;00m$
  3394^I$
  3395^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'sw 11/16/2000 14:42'![39;49;00m$
  3396^I[32mrefineRedoTarget:[39;49;00m [31mtarget[39;49;00m [32mselector:[39;49;00m [31maSymbol[39;49;00m [32marguments:[39;49;00m [31marguments[39;49;00m [32min:[39;49;00m [31mrefineBlock[39;49;00m $
  3397^I^I[37m"Any object can override this method to refine its redo specification"[39;49;00m$
  3398^I$
  3399^I^I^ [31mrefineBlock[39;49;00m$
  3400^I^I^I[32mvalue:[39;49;00m [31mtarget[39;49;00m$
  3401^I^I^I[32mvalue:[39;49;00m [31maSymbol[39;49;00m$
  3402^I^I^I[32mvalue:[39;49;00m [31marguments[39;49;00m[34m! ![39;49;00m$
  3403^I$
  3404^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'sw 11/16/2000 14:42'![39;49;00m$
  3405^I[32mrefineUndoTarget:[39;49;00m [31mtarget[39;49;00m [32mselector:[39;49;00m [31maSymbol[39;49;00m [32marguments:[39;49;00m [31marguments[39;49;00m [32min:[39;49;00m [31mrefineBlock[39;49;00m $
  3406^I^I[37m"Any object can override this method to refine its undo specification"[39;49;00m$
  3407^I$
  3408^I^I^ [31mrefineBlock[39;49;00m$
  3409^I^I^I[32mvalue:[39;49;00m [31mtarget[39;49;00m$
  3410^I^I^I[32mvalue:[39;49;00m [31maSymbol[39;49;00m$
  3411^I^I^I[32mvalue:[39;49;00m [31marguments[39;49;00m[34m! ![39;49;00m$
  3412^I$
  3413^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/11/2000 20:30'![39;49;00m$
  3414^I[32mrememberCommand:[39;49;00m [31maCommand[39;49;00m$
  3415^I^I[37m"Remember the given command for undo"[39;49;00m$
  3416^I^I[04m[32mPreferences[39;49;00m [32museUndo[39;49;00m [36mifFalse:[39;49;00m [^ [36mself[39;49;00m]. [37m"get out quickly"[39;49;00m$
  3417^I^I^ [36mself[39;49;00m [32mcommandHistory[39;49;00m [32mrememberCommand:[39;49;00m [31maCommand[39;49;00m[34m! ![39;49;00m$
  3418^I$
  3419^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/11/2000 20:30'![39;49;00m$
  3420^I[32mrememberUndoableAction:[39;49;00m [31mactionBlock[39;49;00m [32mnamed:[39;49;00m [31mcaption[39;49;00m$
  3421^I^I|[31m cmd result [39;49;00m|$
  3422^I^I[31mcmd[39;49;00m _ [04m[32mCommand[39;49;00m [36mnew[39;49;00m [32mcmdWording:[39;49;00m [31mcaption[39;49;00m.$
  3423^I^I[31mcmd[39;49;00m [32mundoTarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#undoFromCapturedState:[39;49;00m [32margument:[39;49;00m [36mself[39;49;00m [32mcapturedState[39;49;00m.$
  3424^I^I[31mresult[39;49;00m _ [31mactionBlock[39;49;00m [32mvalue[39;49;00m.$
  3425^I^I[31mcmd[39;49;00m [32mredoTarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#redoFromCapturedState:[39;49;00m [32margument:[39;49;00m [36mself[39;49;00m [32mcapturedState[39;49;00m.$
  3426^I^I[36mself[39;49;00m [32mrememberCommand:[39;49;00m [31mcmd[39;49;00m.$
  3427^I^I^ [31mresult[39;49;00m[34m! ![39;49;00m$
  3428^I$
  3429^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/11/2000 20:32'![39;49;00m$
  3430^I[32mundoFromCapturedState:[39;49;00m [31mst[39;49;00m $
  3431^I^I[37m"May be overridden in subclasses.  See also capturedState"[39;49;00m$
  3432^I$
  3433^I^I[36mself[39;49;00m [32mcopyFrom:[39;49;00m [31mst[39;49;00m$
  3434^I[34m! ![39;49;00m$
  3435^I$
  3436^I$
  3437^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m![39;49;00m$
  3438^I[32mchanged[39;49;00m$
  3439^I^I[37m"Receiver changed in a general way; inform all the dependents by [39;49;00m$
  3440^I[37m^Isending each dependent an update: message."[39;49;00m$
  3441^I$
  3442^I^I[36mself[39;49;00m [32mchanged:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  3443^I$
  3444^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m![39;49;00m$
  3445^I[32mchanged:[39;49;00m [31maParameter[39;49;00m $
  3446^I^I[37m"Receiver changed. The change is denoted by the argument aParameter. [39;49;00m$
  3447^I[37m^IUsually the argument is a Symbol that is part of the dependent's change [39;49;00m$
  3448^I[37m^Iprotocol. Inform all of the dependents."[39;49;00m$
  3449^I$
  3450^I^I[36mself[39;49;00m [32mdependents[39;49;00m [32mdo:[39;49;00m [:[31maDependent[39;49;00m | [31maDependent[39;49;00m [32mupdate:[39;49;00m [31maParameter[39;49;00m][34m! ![39;49;00m$
  3451^I$
  3452^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'nk 2/17/2004 11:12'![39;49;00m$
  3453^I[32mchanged:[39;49;00m [31manAspect[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m$
  3454^I^I[37m"Receiver changed. The change is denoted by the argument anAspect. [39;49;00m$
  3455^I[37m^IUsually the argument is a Symbol that is part of the dependent's change [39;49;00m$
  3456^I[37m^Iprotocol. Inform all of the dependents. Also pass anObject for additional information."[39;49;00m$
  3457^I$
  3458^I^I[36mself[39;49;00m [32mdependents[39;49;00m [32mdo:[39;49;00m [:[31maDependent[39;49;00m | [31maDependent[39;49;00m [32mupdate:[39;49;00m [31manAspect[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m][34m! ![39;49;00m$
  3459^I$
  3460^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'sw 10/12/1999 18:15'![39;49;00m$
  3461^I[32mhandledListVerification[39;49;00m$
  3462^I^I[37m"When a self-updating PluggableListMorph lazily checks to see the state of affairs, it first gives its model an opportunity to handle the list verification itself (this is appropriate for some models, such as VersionsBrowser); if a list's model has indeed handled things itself, it returns true here"[39;49;00m$
  3463^I$
  3464^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3465^I$
  3466^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'sw 10/31/1999 00:15'![39;49;00m$
  3467^I[32mnoteSelectionIndex:[39;49;00m [31manInteger[39;49;00m [32mfor:[39;49;00m [31maSymbol[39;49;00m$
  3468^I^I[37m"backstop"[39;49;00m[34m! ![39;49;00m$
  3469^I$
  3470^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m![39;49;00m$
  3471^I[32mokToChange[39;49;00m$
  3472^I^I[37m"Allows a controller to ask this of any model"[39;49;00m$
  3473^I^I^ [36mtrue[39;49;00m[34m! ![39;49;00m$
  3474^I$
  3475^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'sw 10/19/1999 14:39'![39;49;00m$
  3476^I[32mupdateListsAndCodeIn:[39;49;00m [31maWindow[39;49;00m$
  3477^I^I[36mself[39;49;00m [32mcanDiscardEdits[39;49;00m [36mifFalse:[39;49;00m [^ [36mself[39;49;00m].$
  3478^I^I[31maWindow[39;49;00m [32mupdatablePanes[39;49;00m [32mdo:[39;49;00m [:[31maPane[39;49;00m | [31maPane[39;49;00m [32mverifyContents[39;49;00m][34m! ![39;49;00m$
  3479^I$
  3480^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'sma 2/29/2000 20:05'![39;49;00m$
  3481^I[32mupdate:[39;49;00m [31maParameter[39;49;00m $
  3482^I^I[37m"Receive a change notice from an object of whom the receiver is a [39;49;00m$
  3483^I[37m^Idependent. The default behavior is to do nothing; a subclass might want [39;49;00m$
  3484^I[37m^Ito change itself in some way."[39;49;00m$
  3485^I$
  3486^I^I^ [36mself[39;49;00m[34m! ![39;49;00m$
  3487^I$
  3488^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'nk 2/17/2004 11:13'![39;49;00m$
  3489^I[32mupdate:[39;49;00m [31manAspect[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m$
  3490^I^I[37m"Receive a change notice from an object of whom the receiver is a [39;49;00m$
  3491^I[37m^Idependent. The default behavior is to call update:,[39;49;00m$
  3492^I[37m^Iwhich by default does nothing; a subclass might want [39;49;00m$
  3493^I[37m^Ito change itself in some way."[39;49;00m$
  3494^I$
  3495^I^I^ [36mself[39;49;00m [32mupdate:[39;49;00m [31manAspect[39;49;00m[34m! ![39;49;00m$
  3496^I$
  3497^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'jm 8/20/1998 18:26'![39;49;00m$
  3498^I[32mwindowIsClosing[39;49;00m$
  3499^I^I[37m"This message is used to inform a models that its window is closing. Most models do nothing, but some, such as the Debugger, must do some cleanup. Note that this mechanism must be used with care by models that support multiple views, since one view may be closed while others left open."[39;49;00m$
  3500^I[34m! ![39;49;00m$
  3501^I$
  3502^I$
  3503^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 10/4/1999 08:13'![39;49;00m$
  3504^I[32maddModelItemsToWindowMenu:[39;49;00m [31maMenu[39;49;00m$
  3505^I^I[37m"aMenu is being constructed to be presented to the user in response to the user's pressing on the menu widget in the title bar of a morphic window.  Here, the model is given the opportunity to add any model-specific items to the menu, whose default target is the SystemWindow itself."[39;49;00m[34m! ![39;49;00m$
  3506^I$
  3507^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 10/5/1998 14:39'![39;49;00m$
  3508^I[32maddModelMenuItemsTo:[39;49;00m [31maCustomMenu[39;49;00m [32mforMorph:[39;49;00m [31maMorph[39;49;00m [32mhand:[39;49;00m [31maHandMorph[39;49;00m $
  3509^I^I[37m"The receiver serves as the model for aMorph; a menu is being constructed for the morph, and here the receiver is able to add its own items"[39;49;00m$
  3510^I[34m! ![39;49;00m$
  3511^I$
  3512^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sma 11/12/2000 11:43'![39;49;00m$
  3513^I[32masExplorerString[39;49;00m$
  3514^I^I^ [36mself[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
  3515^I$
  3516^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 7/13/1999 15:53'![39;49;00m$
  3517^I[32mdefaultBackgroundColor[39;49;00m$
  3518^I^I[37m"Answer the color to be used as the base window color for a window whose model is an object of the receiver's class"[39;49;00m$
  3519^I^I$
  3520^I^I^ [04m[32mPreferences[39;49;00m [32mwindowColorFor:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m[34m! ![39;49;00m$
  3521^I$
  3522^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m![39;49;00m$
  3523^I[32mdefaultLabelForInspector[39;49;00m$
  3524^I^I[37m"Answer the default label to be used for an Inspector window on the receiver."[39;49;00m$
  3525^I$
  3526^I^I^ [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m[34m! ![39;49;00m$
  3527^I$
  3528^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'RAA 7/10/2000 08:11'![39;49;00m$
  3529^I[32meToyStreamedRepresentationNotifying:[39;49;00m [31maWidget[39;49;00m$
  3530^I$
  3531^I^I|[31m outData [39;49;00m|$
  3532^I^I[ [31moutData[39;49;00m _ [04m[32mSmartRefStream[39;49;00m [32mstreamedRepresentationOf:[39;49;00m [36mself[39;49;00m ] $
  3533^I^I^I[32mon:[39;49;00m [04m[32mProgressInitiationException[39;49;00m$
  3534^I^I^I[32mdo:[39;49;00m [ :[31mex[39;49;00m | $
  3535^I^I^I^I[31mex[39;49;00m [32msendNotificationsTo:[39;49;00m [ :[31mmin[39;49;00m :[31mmax[39;49;00m :[31mcurr[39;49;00m |$
  3536^I^I^I^I^I[31maWidget[39;49;00m [32mifNotNil:[39;49;00m [[31maWidget[39;49;00m [32mflashIndicator:[39;49;00m [33m#working[39;49;00m].$
  3537^I^I^I^I].$
  3538^I^I^I].$
  3539^I^I^[31moutData[39;49;00m$
  3540^I[34m! ![39;49;00m$
  3541^I$
  3542^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'ar 9/27/2005 20:29'![39;49;00m$
  3543^I[32mexplore[39;49;00m$
  3544^I^I^[04m[32mToolSet[39;49;00m [32mexplore:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  3545^I$
  3546^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 8/15/97 17:25'![39;49;00m$
  3547^I[32mfullScreenSize[39;49;00m$
  3548^I^I[37m"Answer the size to which a window displaying the receiver should be set"[39;49;00m$
  3549^I^I|[31m adj [39;49;00m|$
  3550^I^I[31madj[39;49;00m _ ([34m3[39;49;00m [32m*[39;49;00m [04m[32mPreferences[39;49;00m [32mscrollBarWidth[39;49;00m) [32m@[39;49;00m [34m0[39;49;00m.$
  3551^I^I^ [04m[32mRectangle[39;49;00m [32morigin:[39;49;00m [31madj[39;49;00m [32mextent:[39;49;00m ([04m[32mDisplayScreen[39;49;00m [32mactualScreenSize[39;49;00m [32m-[39;49;00m [31madj[39;49;00m)[34m! ![39;49;00m$
  3552^I$
  3553^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'RAA 6/21/1999 11:27'![39;49;00m$
  3554^I[32mhasContentsInExplorer[39;49;00m$
  3555^I$
  3556^I^I^[36mself[39;49;00m [32mbasicSize[39;49;00m [32m>[39;49;00m [34m0[39;49;00m [32mor:[39;49;00m [[36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32misEmpty[39;49;00m [32mnot[39;49;00m]$
  3557^I[34m! ![39;49;00m$
  3558^I$
  3559^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'rbb 3/1/2005 09:28'![39;49;00m$
  3560^I[32minform:[39;49;00m [31maString[39;49;00m$
  3561^I^I[37m"Display a message for the user to read and then dismiss. 6/9/96 sw"[39;49;00m$
  3562^I$
  3563^I^I[31maString[39;49;00m [32misEmptyOrNil[39;49;00m [36mifFalse:[39;49;00m [[04m[32mUIManager[39;49;00m [32mdefault[39;49;00m [32minform:[39;49;00m [31maString[39;49;00m][34m! ![39;49;00m$
  3564^I$
  3565^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m![39;49;00m$
  3566^I[32minitialExtent[39;49;00m$
  3567^I^I[37m"Answer the desired extent for the receiver when a view on it is first opened on the screen. [39;49;00m$
  3568^I[37m^I5/22/96 sw: in the absence of any override, obtain from RealEstateAgent"[39;49;00m$
  3569^I$
  3570^I^I^ [04m[32mRealEstateAgent[39;49;00m [32mstandardWindowExtent[39;49;00m[34m! ![39;49;00m$
  3571^I$
  3572^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'ar 9/27/2005 20:30'![39;49;00m$
  3573^I[32minspectWithLabel:[39;49;00m [31maLabel[39;49;00m$
  3574^I^I[37m"Create and schedule an Inspector in which the user can examine the receiver's variables."[39;49;00m$
  3575^I^I^[04m[32mToolSet[39;49;00m [32minspect:[39;49;00m [36mself[39;49;00m [32mlabel:[39;49;00m [31maLabel[39;49;00m[34m! ![39;49;00m$
  3576^I$
  3577^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 6/12/2001 11:09'![39;49;00m$
  3578^I[32mlaunchPartVia:[39;49;00m [31maSelector[39;49;00m$
  3579^I^I[37m"Obtain a morph by sending aSelector to self, and attach it to the morphic hand.  This provides a general protocol for parts bins"[39;49;00m$
  3580^I$
  3581^I^I|[31m aMorph [39;49;00m|$
  3582^I^I[31maMorph[39;49;00m _ [36mself[39;49;00m [32mperform:[39;49;00m [31maSelector[39;49;00m.$
  3583^I^I[31maMorph[39;49;00m [32msetProperty:[39;49;00m [33m#beFullyVisibleAfterDrop[39;49;00m [32mtoValue:[39;49;00m [36mtrue[39;49;00m.$
  3584^I^I[31maMorph[39;49;00m [32mopenInHand[39;49;00m[34m! ![39;49;00m$
  3585^I$
  3586^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 6/17/2004 01:47'![39;49;00m$
  3587^I[32mlaunchPartVia:[39;49;00m [31maSelector[39;49;00m [32mlabel:[39;49;00m [31maString[39;49;00m$
  3588^I^I[37m"Obtain a morph by sending aSelector to self, and attach it to the morphic hand.  This provides a general protocol for parts bins"[39;49;00m$
  3589^I$
  3590^I^I|[31m aMorph [39;49;00m|$
  3591^I^I[31maMorph[39;49;00m _ [36mself[39;49;00m [32mperform:[39;49;00m [31maSelector[39;49;00m.$
  3592^I^I[31maMorph[39;49;00m [32msetNameTo:[39;49;00m ([04m[32mActiveWorld[39;49;00m [32munusedMorphNameLike:[39;49;00m [31maString[39;49;00m).$
  3593^I^I[31maMorph[39;49;00m [32msetProperty:[39;49;00m [33m#beFullyVisibleAfterDrop[39;49;00m [32mtoValue:[39;49;00m [36mtrue[39;49;00m.$
  3594^I^I[31maMorph[39;49;00m [32mopenInHand[39;49;00m[34m! ![39;49;00m$
  3595^I$
  3596^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 10/16/2000 11:11'![39;49;00m$
  3597^I[32mlaunchTileToRefer[39;49;00m$
  3598^I^I[37m"Create a tile to reference the receiver, and attach it to the hand"[39;49;00m$
  3599^I$
  3600^I^I[36mself[39;49;00m [32mcurrentHand[39;49;00m [32mattachMorph:[39;49;00m [36mself[39;49;00m [32mtileToRefer[39;49;00m[34m! ![39;49;00m$
  3601^I$
  3602^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'di 5/11/1999 22:26'![39;49;00m$
  3603^I[32mmodelSleep[39;49;00m$
  3604^I^I[37m"A window with me as model is being exited or collapsed or closed.[39;49;00m$
  3605^I[37m^IDefault response is no-op"[39;49;00m [34m! ![39;49;00m$
  3606^I$
  3607^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'di 5/11/1999 22:01'![39;49;00m$
  3608^I[32mmodelWakeUp[39;49;00m$
  3609^I^I[37m"A window with me as model is being entered or expanded.  Default response is no-op"[39;49;00m [34m! ![39;49;00m$
  3610^I$
  3611^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 10/16/1999 22:45'![39;49;00m$
  3612^I[32mmodelWakeUpIn:[39;49;00m [31maWindow[39;49;00m$
  3613^I^I[37m"A window with me as model is being entered or expanded.  Default response is no-op"[39;49;00m $
  3614^I^I[36mself[39;49;00m [32mmodelWakeUp[39;49;00m[34m! ![39;49;00m$
  3615^I$
  3616^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 3/8/1999 15:27'![39;49;00m$
  3617^I[32mmouseUpBalk:[39;49;00m [31mevt[39;49;00m$
  3618^I^I[37m"A button I own got a mouseDown, but the user moved out before letting up.  Certain kinds of objects (so-called 'radio buttons', for example, and other structures that must always have some selection, e.g. PaintBoxMorph) wish to take special action in this case; this default does nothing."[39;49;00m$
  3619^I[34m! ![39;49;00m$
  3620^I$
  3621^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 8/22/97 13:14'![39;49;00m$
  3622^I[32mnewTileMorphRepresentative[39;49;00m$
  3623^I^I^ [04m[32mTileMorph[39;49;00m [36mnew[39;49;00m [32msetLiteral:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  3624^I$
  3625^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'jcg 11/1/2001 13:13'![39;49;00m$
  3626^I[32mnotYetImplemented[39;49;00m$
  3627^I^I[36mself[39;49;00m [32minform:[39;49;00m [33m'Not yet implemented ('[39;49;00m[32m,[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m')'[39;49;00m[34m! ![39;49;00m$
  3628^I$
  3629^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'di 6/10/1998 15:06'![39;49;00m$
  3630^I[32mwindowReqNewLabel:[39;49;00m [31mlabelString[39;49;00m$
  3631^I^I[37m"My window's title has been edited.[39;49;00m$
  3632^I[37m^IReturn true if this is OK, and override for further behavior."[39;49;00m$
  3633^I$
  3634^I^I^ [36mtrue[39;49;00m[34m! ![39;49;00m$
  3635^I$
  3636^I$
  3637^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 10/16/2000 10:35'![39;49;00m$
  3638^I[32massureUniClass[39;49;00m$
  3639^I^I[37m"If the receiver is not yet an instance of a uniclass, create a uniclass for it and make the receiver become an instance of that class."[39;49;00m$
  3640^I$
  3641^I^I|[31m anInstance [39;49;00m|$
  3642^I^I[36mself[39;49;00m [32mbelongsToUniClass[39;49;00m [36mifTrue:[39;49;00m [^ [36mself[39;49;00m].$
  3643^I^I[31manInstance[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32minstanceOfUniqueClass[39;49;00m.$
  3644^I^I[36mself[39;49;00m [32mbecome:[39;49;00m ([36mself[39;49;00m [32mas:[39;49;00m [31manInstance[39;49;00m [32mclass[39;49;00m).$
  3645^I^I^ [31manInstance[39;49;00m[34m! ![39;49;00m$
  3646^I$
  3647^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 10/16/2000 10:41'![39;49;00m$
  3648^I[32mbelongsToUniClass[39;49;00m$
  3649^I^I[37m"Answer whether the receiver belongs to a uniclass.  For the moment (this is not entirely satisfactory) this is precisely equated with the classname ending in a digit"[39;49;00m$
  3650^I$
  3651^I^I^ [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32mendsWithDigit[39;49;00m[34m! ![39;49;00m$
  3652^I$
  3653^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 12/11/2000 15:37'![39;49;00m$
  3654^I[32mbrowseOwnClassSubProtocol[39;49;00m$
  3655^I^I[37m"Open up a ProtocolBrowser on the subprotocol of the receiver"[39;49;00m$
  3656^I$
  3657^I^I[04m[32mProtocolBrowser[39;49;00m [32mopenSubProtocolForClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m$
  3658^I[34m! ![39;49;00m$
  3659^I$
  3660^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/4/2001 00:51'![39;49;00m$
  3661^I[32mcategoriesForViewer:[39;49;00m [31maViewer[39;49;00m$
  3662^I^I[37m"Answer a list of categories to offer in the given viewer"[39;49;00m$
  3663^I$
  3664^I^I^ [31maViewer[39;49;00m [32mcurrentVocabulary[39;49;00m [32mcategoryListForInstance:[39;49;00m [36mself[39;49;00m [32mofClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mlimitClass:[39;49;00m [31maViewer[39;49;00m [32mlimitClass[39;49;00m[34m! ![39;49;00m$
  3665^I$
  3666^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/3/2001 22:08'![39;49;00m$
  3667^I[32mcategoriesForVocabulary:[39;49;00m [31maVocabulary[39;49;00m [32mlimitClass:[39;49;00m [31maLimitClass[39;49;00m$
  3668^I^I[37m"Answer a list of categories of methods for the receiver when using the given vocabulary, given that one considers only methods that are implemented not further away than aLimitClass"[39;49;00m$
  3669^I$
  3670^I^I^ [31maVocabulary[39;49;00m [32mcategoryListForInstance:[39;49;00m [36mself[39;49;00m [32mofClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mlimitClass:[39;49;00m [31maLimitClass[39;49;00m[34m! ![39;49;00m$
  3671^I$
  3672^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 10/25/2000 07:20'![39;49;00m$
  3673^I[32mchooseNewNameForReference[39;49;00m$
  3674^I^I[37m"Offer an opportunity for the receiver, presumed already to be known in the References registry, to be renamed"[39;49;00m$
  3675^I$
  3676^I^I|[31m  nameSym current newName [39;49;00m|$
  3677^I^I[31mcurrent[39;49;00m _ [04m[32mReferences[39;49;00m [32mkeyAtValue:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'not found in References'[39;49;00m].$
  3678^I$
  3679^I^I[31mnewName[39;49;00m _ [04m[32mFillInTheBlank[39;49;00m [32mrequest:[39;49;00m [33m'Please enter new name'[39;49;00m [32minitialAnswer:[39;49;00m [31mcurrent[39;49;00m.$
  3680^I^I[37m"Want to user some better way of determining the validity of the chosen identifier, and also want to give more precise diagnostic if the string the user types in is not acceptable.  Work to be done here."[39;49;00m$
  3681^I$
  3682^I^I[31mnewName[39;49;00m [32misEmpty[39;49;00m [36mifTrue:[39;49;00m [^ [36mnil[39;49;00m].$
  3683^I^I(([04m[32mScanner[39;49;00m [32misLiteralSymbol:[39;49;00m [31mnewName[39;49;00m) [32mand:[39;49;00m [([31mnewName[39;49;00m [32mincludes:[39;49;00m [33m$:[39;49;00m) [32mnot[39;49;00m])$
  3684^I^I^I[36mifTrue:[39;49;00m$
  3685^I^I^I^I[[31mnameSym[39;49;00m _ [31mnewName[39;49;00m [32mcapitalized[39;49;00m [32masSymbol[39;49;00m.$
  3686^I^I^I^I((([04m[32mReferences[39;49;00m [32mincludesKey:[39;49;00m  [31mnameSym[39;49;00m) [32mnot[39;49;00m [32mand:[39;49;00m$
  3687^I^I^I^I^I[([04m[32mSmalltalk[39;49;00m [32mincludesKey:[39;49;00m [31mnameSym[39;49;00m) [32mnot[39;49;00m]) [32mand:[39;49;00m$
  3688^I^I^I^I^I^I^I[([04m[32mScriptingSystem[39;49;00m [32mallKnownClassVariableNames[39;49;00m [32mincludes:[39;49;00m [31mnameSym[39;49;00m) [32mnot[39;49;00m])$
  3689^I^I^I^I^I^I[36mifTrue:[39;49;00m$
  3690^I^I^I^I^I^I^I[([04m[32mReferences[39;49;00m [32massociationAt:[39;49;00m [31mcurrent[39;49;00m) [32mkey:[39;49;00m [31mnameSym[39;49;00m.$
  3691^I^I^I^I^I^I^I[04m[32mReferences[39;49;00m [32mrehash[39;49;00m.$
  3692^I^I^I^I^I^I^I^ [31mnameSym[39;49;00m]].$
  3693^I^I[36mself[39;49;00m [32minform:[39;49;00m [33m'Sorry, that name is not available.'[39;49;00m.$
  3694^I^I^ [36mnil[39;49;00m[34m! ![39;49;00m$
  3695^I$
  3696^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/3/2001 21:22'![39;49;00m$
  3697^I[32mdefaultLimitClassForVocabulary:[39;49;00m [31maVocabulary[39;49;00m$
  3698^I^I[37m"Answer the class to use, by default, as the limit class on a protocol browser or viewer opened up on the receiver, within the purview of the Vocabulary provided"[39;49;00m$
  3699^I$
  3700^I^I^ ([31maVocabulary[39;49;00m [32misKindOf:[39;49;00m [04m[32mFullVocabulary[39;49;00m)$
  3701^I^I^I[36mifTrue:[39;49;00m$
  3702^I^I^I^I [[36mself[39;49;00m [32mclass[39;49;00m [32msuperclass[39;49;00m [32m==[39;49;00m [04m[32mObject[39;49;00m$
  3703^I^I^I^I^I[36mifTrue:[39;49;00m$
  3704^I^I^I^I^I^I[[36mself[39;49;00m [32mclass[39;49;00m]$
  3705^I^I^I^I^I[36mifFalse:[39;49;00m$
  3706^I^I^I^I^I^I[[36mself[39;49;00m [32mclass[39;49;00m [32msuperclass[39;49;00m]]$
  3707^I^I^I[36mifFalse:[39;49;00m$
  3708^I^I^I^I[[04m[32mProtoObject[39;49;00m][34m! ![39;49;00m$
  3709^I$
  3710^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 2/14/2000 14:24'![39;49;00m$
  3711^I[32mdefaultNameStemForInstances[39;49;00m$
  3712^I^I[37m"Answer a basis for names of default instances of the receiver.  The default is to let the class specify, but certain instances will want to override.  (PasteUpMorphs serving as Worlds come to mind"[39;49;00m$
  3713^I$
  3714^I^I^ [36mself[39;49;00m [32mclass[39;49;00m [32mdefaultNameStemForInstances[39;49;00m[34m! ![39;49;00m$
  3715^I$
  3716^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 5/22/2001 16:53'![39;49;00m$
  3717^I[32melementTypeFor:[39;49;00m [31maStringOrSymbol[39;49;00m [32mvocabulary:[39;49;00m [31maVocabulary[39;49;00m$
  3718^I^I[37m"Answer a symbol characterizing what kind of element aStringOrSymbol represents.  Realistically, at present, this always just returns #systemScript; a prototyped but not-incorporated architecture supported use of a leading colon to characterize an inst var of a system class, and for the moment we still see its remnant here."[39;49;00m$
  3719^I$
  3720^I^I[36mself[39;49;00m [32mflag:[39;49;00m [33m#deferred[39;49;00m.  [37m"a loose end in the non-player case"[39;49;00m$
  3721^I^I^ [33m#systemScript[39;49;00m[34m! ![39;49;00m$
  3722^I$
  3723^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 5/4/2001 07:04'![39;49;00m$
  3724^I[32mexternalName[39;49;00m$
  3725^I^I[37m"Answer an external name by which the receiver is known.  Generic implementation here is a transitional backstop. probably"[39;49;00m$
  3726^I$
  3727^I^I^ [36mself[39;49;00m [32mnameForViewer[39;49;00m[34m! ![39;49;00m$
  3728^I$
  3729^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 5/4/2001 07:06'![39;49;00m$
  3730^I[32mgraphicForViewerTab[39;49;00m$
  3731^I^I[37m"When a Viewer is open on the receiver, its tab needs some graphic to show to the user.  Answer a form or a morph to serve that purpose.  A generic image is used for arbitrary objects, but note my reimplementors"[39;49;00m$
  3732^I^I$
  3733^I^I^ [04m[32mScriptingSystem[39;49;00m [32mformAtKey:[39;49;00m [33m'Image'[39;49;00m[34m! ![39;49;00m$
  3734^I$
  3735^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 5/4/2001 07:08'![39;49;00m$
  3736^I[32mhasUserDefinedSlots[39;49;00m$
  3737^I^I[37m"Answer whether the receiver has any user-defined slots, in the omniuser sense of the term.  This is needed to allow Viewers to look at any object, not just at Players."[39;49;00m$
  3738^I$
  3739^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  3740^I$
  3741^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/22/2002 14:07'![39;49;00m$
  3742^I[32minfoFor:[39;49;00m [31manElement[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m$
  3743^I^I[37m"The user made a gesture asking for info/menu relating to me.  Some of the messages dispatched here are not yet available in this image"[39;49;00m$
  3744^I$
  3745^I^I|[31m aMenu elementType [39;49;00m|$
  3746^I^I[31melementType[39;49;00m _ [36mself[39;49;00m [32melementTypeFor:[39;49;00m [31manElement[39;49;00m [32mvocabulary:[39;49;00m [31maViewer[39;49;00m [32mcurrentVocabulary[39;49;00m.$
  3747^I^I(([31melementType[39;49;00m [32m=[39;49;00m [33m#systemSlot[39;49;00m) [32m|[39;49;00m ([31melementType[39;49;00m [32m==[39;49;00m [33m#userSlot[39;49;00m))$
  3748^I^I^I[36mifTrue:[39;49;00m^I[^ [36mself[39;49;00m [32mslotInfoButtonHitFor:[39;49;00m [31manElement[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m].$
  3749^I^I[36mself[39;49;00m [32mflag:[39;49;00m [33m#deferred[39;49;00m.  [37m"Use a traditional MenuMorph, and reinstate the pacify thing"[39;49;00m$
  3750^I^I[31maMenu[39;49;00m _ [04m[32mMenuMorph[39;49;00m [36mnew[39;49;00m [32mdefaultTarget:[39;49;00m [31maViewer[39;49;00m.$
  3751^I^I[33m#([39;49;00m^I[33m([39;49;00m[33m'implementors'[39;49;00m^I^I^I[33mbrowseImplementorsOf:[39;49;00m[33m)[39;49;00m$
  3752^I^I^I[33m([39;49;00m[33m'senders'[39;49;00m^I^I^I^I[33mbrowseSendersOf:[39;49;00m[33m)[39;49;00m$
  3753^I^I^I[33m([39;49;00m[33m'versions'[39;49;00m^I^I^I^I[33mbrowseVersionsOf:[39;49;00m[33m)[39;49;00m$
  3754^I^I^I[33m-[39;49;00m$
  3755^I^I^I[33m([39;49;00m[33m'browse full'[39;49;00m^I^I^I[33mbrowseMethodFull:[39;49;00m[33m)[39;49;00m$
  3756^I^I^I[33m([39;49;00m[33m'inheritance'[39;49;00m^I^I^I[33mbrowseMethodInheritance:[39;49;00m[33m)[39;49;00m$
  3757^I^I^I[33m-[39;49;00m$
  3758^I^I^I[33m([39;49;00m[33m'about this method'[39;49;00m^I^I[33maboutMethod:[39;49;00m[33m)[39;49;00m[33m)[39;49;00m [32mdo:[39;49;00m$
  3759^I$
  3760^I^I^I^I[:[31mpair[39;49;00m |$
  3761^I^I^I^I^I[31mpair[39;49;00m [32m=[39;49;00m [33m'-'[39;49;00m$
  3762^I^I^I^I^I^I[36mifTrue:[39;49;00m$
  3763^I^I^I^I^I^I^I[[31maMenu[39;49;00m [32maddLine[39;49;00m]$
  3764^I^I^I^I^I^I[36mifFalse:[39;49;00m$
  3765^I^I^I^I^I^I^I[[31maMenu[39;49;00m [32madd:[39;49;00m [31mpair[39;49;00m [32mfirst[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32mselector:[39;49;00m [31mpair[39;49;00m [32msecond[39;49;00m [32margument:[39;49;00m [31manElement[39;49;00m]].$
  3766^I^I[31maMenu[39;49;00m [32maddLine[39;49;00m.$
  3767^I^I[31maMenu[39;49;00m [32mdefaultTarget:[39;49;00m [36mself[39;49;00m.$
  3768^I^I[33m#([39;49;00m^I[33m([39;49;00m[33m'destroy script'[39;49;00m^I^I[33mremoveScript:[39;49;00m[33m)[39;49;00m$
  3769^I^I^I[33m([39;49;00m[33m'rename script'[39;49;00m^I^I[33mrenameScript:[39;49;00m[33m)[39;49;00m$
  3770^I^I^I[33m([39;49;00m[33m'pacify script'[39;49;00m^I^I[33mpacifyScript:[39;49;00m[33m)[39;49;00m[33m)[39;49;00m [32mdo:[39;49;00m$
  3771^I^I^I^I[:[31mpair[39;49;00m |$
  3772^I^I^I^I^I[31maMenu[39;49;00m [32madd:[39;49;00m [31mpair[39;49;00m [32mfirst[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [31mpair[39;49;00m [32msecond[39;49;00m [32margument:[39;49;00m [31manElement[39;49;00m].$
  3773^I$
  3774^I^I[31maMenu[39;49;00m [32maddLine[39;49;00m.$
  3775^I^I[31maMenu[39;49;00m  [32madd:[39;49;00m [33m'show categories....'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32mselector:[39;49;00m [33m#showCategoriesFor:[39;49;00m [32margument:[39;49;00m [31manElement[39;49;00m.$
  3776^I^I[31maMenu[39;49;00m [32mitems[39;49;00m [32msize[39;49;00m [32m==[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m  [37m"won't happen at the moment a/c the above"[39;49;00m$
  3777^I^I^I[[31maMenu[39;49;00m [32madd:[39;49;00m [33m'ok'[39;49;00m [32maction:[39;49;00m [36mnil[39;49;00m].  [37m"in case it was a slot -- weird, transitional"[39;49;00m$
  3778^I$
  3779^I^I[31maMenu[39;49;00m [32maddTitle:[39;49;00m [31manElement[39;49;00m [32masString[39;49;00m[32m,[39;49;00m [33m' ('[39;49;00m[32m,[39;49;00m [31melementType[39;49;00m[32m,[39;49;00m [33m')'[39;49;00m.$
  3780^I$
  3781^I^I[31maMenu[39;49;00m [32mpopUpInWorld:[39;49;00m [36mself[39;49;00m [32mcurrentWorld[39;49;00m.$
  3782^I [34m! ![39;49;00m$
  3783^I$
  3784^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 9/26/2001 11:58'![39;49;00m$
  3785^I[32minitialTypeForSlotNamed:[39;49;00m [31maName[39;49;00m$
  3786^I^I[37m"Answer the initial type to be ascribed to the given instance variable"[39;49;00m$
  3787^I$
  3788^I^I^ [33m#Object[39;49;00m[34m! ![39;49;00m$
  3789^I$
  3790^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'ar 5/26/2001 16:13'![39;49;00m$
  3791^I[32misPlayerLike[39;49;00m$
  3792^I^I[37m"Return true if the receiver is a player-like object"[39;49;00m$
  3793^I^I^[36mfalse[39;49;00m[34m! ![39;49;00m$
  3794^I$
  3795^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'nk 9/11/2004 16:53'![39;49;00m$
  3796^I[32mmethodInterfacesInPresentationOrderFrom:[39;49;00m [31minterfaceList[39;49;00m [32mforCategory:[39;49;00m [31maCategory[39;49;00m $
  3797^I^I[37m"Answer the interface list sorted in desired presentation order, using a [39;49;00m$
  3798^I[37m^Istatic master-ordering list, q.v. The category parameter allows an [39;49;00m$
  3799^I[37m^Iescape in case one wants to apply different order strategies in different [39;49;00m$
  3800^I[37m^Icategories, but for now a single master-priority-ordering is used -- see [39;49;00m$
  3801^I[37m^Ithe comment in method EToyVocabulary.masterOrderingOfPhraseSymbols"[39;49;00m$
  3802^I$
  3803^I^I|[31m masterOrder ordered unordered index [39;49;00m|$
  3804^I^I[31mmasterOrder[39;49;00m := [04m[32mVocabulary[39;49;00m [32meToyVocabulary[39;49;00m [32mmasterOrderingOfPhraseSymbols[39;49;00m.$
  3805^I^I[31mordered[39;49;00m := [04m[32mSortedCollection[39;49;00m [32msortBlock:[39;49;00m [:[31ma[39;49;00m :[31mb[39;49;00m | [31ma[39;49;00m [32mkey[39;49;00m [32m<[39;49;00m [31mb[39;49;00m [32mkey[39;49;00m].$
  3806^I^I[31munordered[39;49;00m := [04m[32mSortedCollection[39;49;00m [32msortBlock:[39;49;00m [:[31ma[39;49;00m :[31mb[39;49;00m | [31ma[39;49;00m [32mwording[39;49;00m [32m<[39;49;00m [31mb[39;49;00m [32mwording[39;49;00m].$
  3807^I$
  3808^I^I[31minterfaceList[39;49;00m [32mdo:[39;49;00m [:[31minterface[39;49;00m | $
  3809^I^I^I[31mindex[39;49;00m := [31mmasterOrder[39;49;00m [32mindexOf:[39;49;00m [31minterface[39;49;00m [32melementSymbol[39;49;00m.$
  3810^I^I^I[31mindex[39;49;00m [32misZero[39;49;00m$
  3811^I^I^I^I[36mifTrue:[39;49;00m [[31munordered[39;49;00m [32madd:[39;49;00m [31minterface[39;49;00m]$
  3812^I^I^I^I[36mifFalse:[39;49;00m [[31mordered[39;49;00m [32madd:[39;49;00m [31mindex[39;49;00m [32m->[39;49;00m [31minterface[39;49;00m]].$
  3813^I$
  3814^I^I^ [04m[32mArray[39;49;00m$
  3815^I^I^I[32mstreamContents:[39;49;00m [:[31mstream[39;49;00m | $
  3816^I^I^I^I[31mordered[39;49;00m [32mdo:[39;49;00m [:[31massoc[39;49;00m | [31mstream[39;49;00m [32mnextPut:[39;49;00m [31massoc[39;49;00m [32mvalue[39;49;00m].$
  3817^I^I^I^I[31mstream[39;49;00m [32mnextPutAll:[39;49;00m [31munordered[39;49;00m][34m! ![39;49;00m$
  3818^I$
  3819^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 10/24/2000 11:36'![39;49;00m$
  3820^I[32mnewScriptorAround:[39;49;00m [31maPhraseTileMorph[39;49;00m$
  3821^I^I[37m"Sprout a scriptor around aPhraseTileMorph, thus making a new script.  This is where generalized scriptors will be threaded in"[39;49;00m$
  3822^I$
  3823^I^I^ [36mnil[39;49;00m[34m! ![39;49;00m$
  3824^I$
  3825^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 10/25/2000 17:42'![39;49;00m$
  3826^I[32mofferViewerMenuForEvt:[39;49;00m [31manEvent[39;49;00m [32mmorph:[39;49;00m [31maMorph[39;49;00m$
  3827^I^I[37m"Offer the viewer's primary menu to the user.  aMorph is some morph within the viewer itself, the one within which a mousedown triggered the need for this menu, and it is used only to retrieve the Viewer itself"[39;49;00m$
  3828^I$
  3829^I^I[36mself[39;49;00m [32mofferViewerMenuFor:[39;49;00m ([31maMorph[39;49;00m [32mownerThatIsA:[39;49;00m [04m[32mStandardViewer[39;49;00m) [32mevent:[39;49;00m [31manEvent[39;49;00m[34m! ![39;49;00m$
  3830^I$
  3831^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/11/2002 02:03'![39;49;00m$
  3832^I[32mofferViewerMenuFor:[39;49;00m [31maViewer[39;49;00m [32mevent:[39;49;00m [31mevt[39;49;00m$
  3833^I^I[37m"Offer the primary Viewer menu to the user.  Copied up from Player code, but most of the functions suggested here don't work for non-Player objects, many aren't even defined, some relate to exploratory sw work not yet reflected in the current corpus.  We are early in the life cycle of this method..."[39;49;00m$
  3834^I$
  3835^I^I|[31m aMenu [39;49;00m|$
  3836^I^I[31maMenu[39;49;00m _ [04m[32mMenuMorph[39;49;00m [36mnew[39;49;00m [32mdefaultTarget:[39;49;00m [36mself[39;49;00m.$
  3837^I^I[31maMenu[39;49;00m [32maddStayUpItem[39;49;00m.$
  3838^I^I[31maMenu[39;49;00m [32mtitle:[39;49;00m [33m'**CAUTION -- UNDER CONSTRUCTION!!**[39;49;00m$
  3839^I[33mMany things may not work!![39;49;00m$
  3840^I[33m'[39;49;00m[32m,[39;49;00m [36mself[39;49;00m [32mnameForViewer[39;49;00m.$
  3841^I^I([31maViewer[39;49;00m [32maffordsUniclass[39;49;00m [32mand:[39;49;00m [[36mself[39;49;00m [32mbelongsToUniClass[39;49;00m [32mnot[39;49;00m]) [36mifTrue:[39;49;00m$
  3842^I^I^I[[31maMenu[39;49;00m [32madd:[39;49;00m [33m'give me a Uniclass'[39;49;00m [32maction:[39;49;00m [33m#assureUniClass[39;49;00m.$
  3843^I^I^I[31maMenu[39;49;00m [32maddLine[39;49;00m].$
  3844^I^I[31maMenu[39;49;00m [32madd:[39;49;00m [33m'choose vocabulary...'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32maction:[39;49;00m [33m#chooseVocabulary[39;49;00m.$
  3845^I^I[31maMenu[39;49;00m [32madd:[39;49;00m [33m'choose limit class...'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32maction:[39;49;00m [33m#chooseLimitClass[39;49;00m.$
  3846^I^I[31maMenu[39;49;00m [32madd:[39;49;00m [33m'add search pane'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32maction:[39;49;00m [33m#addSearchPane[39;49;00m.$
  3847^I^I[31maMenu[39;49;00m [32mballoonTextForLastItem:[39;49;00m [33m'Specify which class should be the most generic one to have its methods shown in this Viewer'[39;49;00m.$
  3848^I^I[31maMenu[39;49;00m [32maddLine[39;49;00m.$
  3849^I$
  3850^I^I[36mself[39;49;00m [32mbelongsToUniClass[39;49;00m [36mifTrue:[39;49;00m$
  3851^I^I^I[[31maMenu[39;49;00m [32madd:[39;49;00m [33m'add a new instance variable'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#addInstanceVariableIn:[39;49;00m [32margument:[39;49;00m [31maViewer[39;49;00m.$
  3852^I^I^I[31maMenu[39;49;00m [32madd:[39;49;00m [33m'add a new script'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32mselector:[39;49;00m [33m#newPermanentScriptIn:[39;49;00m [32margument:[39;49;00m [31maViewer[39;49;00m.$
  3853^I^I^I[31maMenu[39;49;00m [32maddLine[39;49;00m.$
  3854^I^I^I[31maMenu[39;49;00m [32madd:[39;49;00m [33m'make my class be first-class'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#makeFirstClassClassIn:[39;49;00m [32margument:[39;49;00m [31maViewer[39;49;00m.$
  3855^I^I^I[31maMenu[39;49;00m [32madd:[39;49;00m [33m'move my changes up to my superclass'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32maction:[39;49;00m [33m#promoteChangesToSuperclass[39;49;00m.$
  3856^I^I^I[31maMenu[39;49;00m [32maddLine[39;49;00m].$
  3857^I$
  3858^I^I[31maMenu[39;49;00m [32madd:[39;49;00m [33m'tear off a tile'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#launchTileToRefer[39;49;00m.$
  3859^I^I[31maMenu[39;49;00m [32maddLine[39;49;00m.$
  3860^I$
  3861^I^I[31maMenu[39;49;00m [32madd:[39;49;00m [33m'inspect me'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#inspect[39;49;00m.$
  3862^I^I[31maMenu[39;49;00m [32madd:[39;49;00m [33m'inspect my class'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32maction:[39;49;00m [33m#inspect[39;49;00m.$
  3863^I^I[31maMenu[39;49;00m [32maddLine[39;49;00m.$
  3864^I$
  3865^I^I[31maMenu[39;49;00m [32madd:[39;49;00m [33m'browse vocabulary'[39;49;00m [32maction:[39;49;00m [33m#haveFullProtocolBrowsed[39;49;00m.$
  3866^I^I[31maMenu[39;49;00m [32madd:[39;49;00m [33m'inspect this Viewer'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32maction:[39;49;00m [33m#inspect[39;49;00m.$
  3867^I$
  3868^I^I[31maMenu[39;49;00m [32mpopUpEvent:[39;49;00m [31mevt[39;49;00m [32min:[39;49;00m [31maViewer[39;49;00m [32mcurrentWorld[39;49;00m$
  3869^I$
  3870^I[37m"[39;49;00m$
  3871^I[37m^IaMenu add: 'references to me' target: aViewer action: #browseReferencesToObject.[39;49;00m$
  3872^I[37m^IaMenu add: 'toggle scratch pane' target: aViewer selector: #toggleScratchPane.[39;49;00m$
  3873^I[37m^IaMenu add: 'make a nascent script for me' target: aViewer selector: #makeNascentScript.[39;49;00m$
  3874^I[37m^IaMenu add: 'rename me' target: aViewer selector: #chooseNewNameForReference.[39;49;00m$
  3875^I[37m^IaMenu add: 'browse full' action: #browseOwnClassFull.[39;49;00m$
  3876^I[37m^IaMenu add: 'browse hierarchy' action: #browseOwnClassHierarchy.[39;49;00m$
  3877^I[37m^IaMenu add: 'set user level...' target: aViewer action: #setUserLevel.[39;49;00m$
  3878^I[37m^IaMenu add: 'browse sub-protocol' action: #browseOwnClassSubProtocol.[39;49;00m$
  3879^I[37m^IaMenu addLine.[39;49;00m$
  3880^I[37m[39;49;00m$
  3881^I[37m"[39;49;00m[34m! ![39;49;00m$
  3882^I$
  3883^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 1/22/2001 15:20'![39;49;00m$
  3884^I[32mrenameScript:[39;49;00m [31moldSelector[39;49;00m$
  3885^I^I[37m"prompt the user for a new selector and apply it.  Presently only works for players"[39;49;00m$
  3886^I$
  3887^I^I[36mself[39;49;00m [32mnotYetImplemented[39;49;00m[34m! ![39;49;00m$
  3888^I$
  3889^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/10/2004 11:53'![39;49;00m$
  3890^I[32mtilePhrasesForCategory:[39;49;00m [31maCategorySymbol[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m$
  3891^I^I[37m"Return a collection of phrases for the category."[39;49;00m$
  3892^I$
  3893^I^I|[31m interfaces [39;49;00m|$
  3894^I^I[31minterfaces[39;49;00m _ [36mself[39;49;00m [32mmethodInterfacesForCategory:[39;49;00m [31maCategorySymbol[39;49;00m [32minVocabulary:[39;49;00m [31maViewer[39;49;00m [32mcurrentVocabulary[39;49;00m [32mlimitClass:[39;49;00m [31maViewer[39;49;00m [32mlimitClass[39;49;00m.$
  3895^I^I[31minterfaces[39;49;00m _ [36mself[39;49;00m [32mmethodInterfacesInPresentationOrderFrom:[39;49;00m [31minterfaces[39;49;00m [32mforCategory:[39;49;00m [31maCategorySymbol[39;49;00m.$
  3896^I^I^ [36mself[39;49;00m [32mtilePhrasesForMethodInterfaces:[39;49;00m [31minterfaces[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m[34m! ![39;49;00m$
  3897^I$
  3898^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/10/2004 11:53'![39;49;00m$
  3899^I[32mtilePhrasesForMethodInterfaces:[39;49;00m [31mmethodInterfaceList[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m$
  3900^I^I[37m"Return a collection of ViewerLine objects corresponding to the method-interface list provided.   The resulting list will be in the same order as the incoming list, but may be smaller if the viewer's vocbulary suppresses some of the methods, or if, in classic tiles mode, the selector requires more arguments than can be handled."[39;49;00m$
  3901^I$
  3902^I^I|[31m toSuppress interfaces resultType itsSelector [39;49;00m|$
  3903^I^I[31mtoSuppress[39;49;00m _ [31maViewer[39;49;00m [32mcurrentVocabulary[39;49;00m [32mphraseSymbolsToSuppress[39;49;00m.$
  3904^I^I[31minterfaces[39;49;00m _ [31mmethodInterfaceList[39;49;00m [32mreject:[39;49;00m [:[31mint[39;49;00m | [31mtoSuppress[39;49;00m [32mincludes:[39;49;00m [31mint[39;49;00m [32mselector[39;49;00m].$
  3905^I^I[04m[32mPreferences[39;49;00m [32muniversalTiles[39;49;00m [36mifFalse:[39;49;00m  [37m"Classic tiles have their limitations..."[39;49;00m$
  3906^I^I^I[[31minterfaces[39;49;00m _ [31minterfaces[39;49;00m [32mselect:[39;49;00m$
  3907^I^I^I^I[:[31mint[39;49;00m |$
  3908^I^I^I^I^I[31mitsSelector[39;49;00m _ [31mint[39;49;00m [32mselector[39;49;00m.$
  3909^I^I^I^I^I[31mitsSelector[39;49;00m [32mnumArgs[39;49;00m [32m<[39;49;00m [34m2[39;49;00m [32mor:[39;49;00m$
  3910^I^I^I^I^I^I[37m"The lone two-arg loophole in classic tiles"[39;49;00m$
  3911^I^I^I^I^I^I[[33m#([39;49;00m[33mcolor:sees:[39;49;00m[33m)[39;49;00m [32mincludes:[39;49;00m [31mitsSelector[39;49;00m]]].$
  3912^I$
  3913^I^I^ [31minterfaces[39;49;00m [32mcollect:[39;49;00m$
  3914^I^I^I[:[31maMethodInterface[39;49;00m |$
  3915^I^I^I^I(([31mresultType[39;49;00m _ [31maMethodInterface[39;49;00m [32mresultType[39;49;00m) [32mnotNil[39;49;00m [32mand:[39;49;00m [[31mresultType[39;49;00m [32m~~[39;49;00m [33m#unknown[39;49;00m]) $
  3916^I^I^I^I^I[36mifTrue:[39;49;00m$
  3917^I^I^I^I^I^I[[31maViewer[39;49;00m [32mphraseForVariableFrom:[39;49;00m [31maMethodInterface[39;49;00m]$
  3918^I^I^I^I^I[36mifFalse:[39;49;00m$
  3919^I^I^I^I^I^I[[31maViewer[39;49;00m [32mphraseForCommandFrom:[39;49;00m [31maMethodInterface[39;49;00m]][34m! ![39;49;00m$
  3920^I$
  3921^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/10/2004 12:23'![39;49;00m$
  3922^I[32mtilePhrasesForSelectorList:[39;49;00m [31maList[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m$
  3923^I^I[37m"Particular to the search facility in viewers.  Answer a list, in appropriate order, of ViewerLine objects to put into the viewer."[39;49;00m$
  3924^I$
  3925^I^I|[31m interfaces aVocab [39;49;00m|$
  3926^I^I[31maVocab[39;49;00m _ [31maViewer[39;49;00m [32mcurrentVocabulary[39;49;00m.$
  3927^I^I[31minterfaces[39;49;00m _ [36mself[39;49;00m$
  3928^I^I^I[32mmethodInterfacesInPresentationOrderFrom:[39;49;00m$
  3929^I^I^I^I([31maList[39;49;00m [32mcollect:[39;49;00m [:[31maSel[39;49;00m | [31maVocab[39;49;00m [32mmethodInterfaceForSelector:[39;49;00m [31maSel[39;49;00m [32mclass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m])$
  3930^I^I^I[32mforCategory:[39;49;00m [33m#search[39;49;00m.$
  3931^I^I^ [36mself[39;49;00m [32mtilePhrasesForMethodInterfaces:[39;49;00m [31minterfaces[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m[34m! ![39;49;00m$
  3932^I$
  3933^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 5/4/2001 04:51'![39;49;00m$
  3934^I[32mtileToRefer[39;49;00m$
  3935^I^I[37m"Answer a reference tile that comprises an alias to me"[39;49;00m$
  3936^I$
  3937^I^I^ [04m[32mTileMorph[39;49;00m [36mnew[39;49;00m [32msetToReferTo:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  3938^I$
  3939^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sd 3/30/2005 22:04'![39;49;00m$
  3940^I[32muniqueInstanceVariableNameLike:[39;49;00m [31maString[39;49;00m [32mexcluding:[39;49;00m [31mtakenNames[39;49;00m$
  3941^I^I[37m"Answer a nice instance-variable name to be added to the receiver which resembles aString, making sure it does not coincide with any element in takenNames"[39;49;00m$
  3942^I$
  3943^I^I|[31m okBase uniqueName usedNames [39;49;00m|$
  3944^I^I[31musedNames[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNamesEverywhere[39;49;00m.$
  3945^I^I[31musedNames[39;49;00m [32mremoveAllFoundIn:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstVarNames[39;49;00m.$
  3946^I^I[31musedNames[39;49;00m [32maddAll:[39;49;00m [31mtakenNames[39;49;00m.$
  3947^I^I[31mokBase[39;49;00m _ [04m[32mScanner[39;49;00m [32mwellFormedInstanceVariableNameFrom:[39;49;00m [31maString[39;49;00m.$
  3948^I$
  3949^I^I[31muniqueName[39;49;00m _ [04m[32mUtilities[39;49;00m [32mkeyLike:[39;49;00m [31mokBase[39;49;00m [32msatisfying:[39;49;00m $
  3950^I^I^I[:[31maKey[39;49;00m | ([31musedNames[39;49;00m [32mincludes:[39;49;00m [31maKey[39;49;00m) [32mnot[39;49;00m].$
  3951^I$
  3952^I^I^ [31muniqueName[39;49;00m[34m! ![39;49;00m$
  3953^I$
  3954^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 11/21/2001 15:16'![39;49;00m$
  3955^I[32muniqueNameForReference[39;49;00m$
  3956^I^I[37m"Answer a nice name by which the receiver can be referred to by other objects.  At present this uses a global References dictionary to hold the database of references, but in due course this will need to acquire some locality"[39;49;00m$
  3957^I$
  3958^I^I|[31m aName nameSym stem knownClassVars [39;49;00m|$
  3959^I^I([31maName[39;49;00m _ [36mself[39;49;00m [32muniqueNameForReferenceOrNil[39;49;00m) [32mifNotNil:[39;49;00m [^ [31maName[39;49;00m].$
  3960^I^I([31mstem[39;49;00m _ [36mself[39;49;00m [32mknownName[39;49;00m) [32mifNil:[39;49;00m$
  3961^I^I^I[[31mstem[39;49;00m _ [36mself[39;49;00m [32mdefaultNameStemForInstances[39;49;00m [32masString[39;49;00m].$
  3962^I^I[31mstem[39;49;00m _ [31mstem[39;49;00m [32mselect:[39;49;00m [:[31mch[39;49;00m | [31mch[39;49;00m [32misLetter[39;49;00m [32mor:[39;49;00m [[31mch[39;49;00m [32misDigit[39;49;00m]].$
  3963^I^I[31mstem[39;49;00m [32msize[39;49;00m [32m==[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m [[31mstem[39;49;00m _ [33m'A'[39;49;00m].$
  3964^I^I[31mstem[39;49;00m [32mfirst[39;49;00m [32misLetter[39;49;00m [36mifFalse:[39;49;00m$
  3965^I^I^I[[31mstem[39;49;00m _ [33m'A'[39;49;00m[32m,[39;49;00m [31mstem[39;49;00m].$
  3966^I^I[31mstem[39;49;00m _ [31mstem[39;49;00m [32mcapitalized[39;49;00m.$
  3967^I^I[31mknownClassVars[39;49;00m _ [04m[32mScriptingSystem[39;49;00m [32mallKnownClassVariableNames[39;49;00m.$
  3968^I^I[31maName[39;49;00m _ [04m[32mUtilities[39;49;00m [32mkeyLike:[39;49;00m  [31mstem[39;49;00m [32msatisfying:[39;49;00m$
  3969^I^I^I[:[31mjinaLake[39;49;00m |$
  3970^I^I^I^I[31mnameSym[39;49;00m _ [31mjinaLake[39;49;00m [32masSymbol[39;49;00m.$
  3971^I^I^I^I (([04m[32mReferences[39;49;00m [32mincludesKey:[39;49;00m  [31mnameSym[39;49;00m) [32mnot[39;49;00m [32mand:[39;49;00m$
  3972^I^I^I^I^I[([04m[32mSmalltalk[39;49;00m [32mincludesKey:[39;49;00m [31mnameSym[39;49;00m) [32mnot[39;49;00m]) [32mand:[39;49;00m$
  3973^I^I^I^I^I^I^I[([31mknownClassVars[39;49;00m [32mincludes:[39;49;00m [31mnameSym[39;49;00m) [32mnot[39;49;00m]].$
  3974^I$
  3975^I^I[04m[32mReferences[39;49;00m [32mat:[39;49;00m ([31maName[39;49;00m _ [31maName[39;49;00m [32masSymbol[39;49;00m) [32mput:[39;49;00m [36mself[39;49;00m.$
  3976^I^I^ [31maName[39;49;00m[34m! ![39;49;00m$
  3977^I$
  3978^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'md 1/17/2006 17:58'![39;49;00m$
  3979^I[32muniqueNameForReferenceFrom:[39;49;00m [31mproposedName[39;49;00m$
  3980^I^I[37m"Answer a satisfactory symbol, similar to the proposedName but obeying the rules, to represent the receiver"[39;49;00m$
  3981^I$
  3982^I^I|[31m aName nameSym stem okay [39;49;00m|$
  3983^I^I[31mproposedName[39;49;00m [32m=[39;49;00m [36mself[39;49;00m [32muniqueNameForReferenceOrNil[39;49;00m $
  3984^I^I^I[36mifTrue:[39;49;00m [^ [31mproposedName[39;49;00m].  [37m"No change"[39;49;00m$
  3985^I$
  3986^I^I[31mstem[39;49;00m _ [31mproposedName[39;49;00m [32mselect:[39;49;00m [:[31mch[39;49;00m | [31mch[39;49;00m [32misLetter[39;49;00m [32mor:[39;49;00m [[31mch[39;49;00m [32misDigit[39;49;00m]].$
  3987^I^I[31mstem[39;49;00m [32msize[39;49;00m [32m==[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m [[31mstem[39;49;00m _ [33m'A'[39;49;00m].$
  3988^I^I[31mstem[39;49;00m [32mfirst[39;49;00m [32misLetter[39;49;00m [36mifFalse:[39;49;00m$
  3989^I^I^I[[31mstem[39;49;00m _ [33m'A'[39;49;00m[32m,[39;49;00m [31mstem[39;49;00m].$
  3990^I^I[31mstem[39;49;00m _ [31mstem[39;49;00m [32mcapitalized[39;49;00m.$
  3991^I^I[31maName[39;49;00m _ [04m[32mUtilities[39;49;00m [32mkeyLike:[39;49;00m [31mstem[39;49;00m [32msatisfying:[39;49;00m$
  3992^I^I^I[:[31mjinaLake[39;49;00m |$
  3993^I^I^I^I[31mnameSym[39;49;00m _ [31mjinaLake[39;49;00m [32masSymbol[39;49;00m.$
  3994^I^I^I^I[31mokay[39;49;00m _ [36mtrue[39;49;00m.$
  3995^I^I^I^I([36mself[39;49;00m [32mclass[39;49;00m [32mbindingOf:[39;49;00m [31mnameSym[39;49;00m) [32mifNotNil:[39;49;00m [[31mokay[39;49;00m _ [36mfalse[39;49;00m [37m"don't use it"[39;49;00m].$
  3996^I^I^I^I[31mokay[39;49;00m].$
  3997^I^I^ [31maName[39;49;00m [32masSymbol[39;49;00m[34m! ![39;49;00m$
  3998^I$
  3999^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 3/15/2004 23:01'![39;49;00m$
  4000^I[32muniqueNameForReferenceOrNil[39;49;00m$
  4001^I^I[37m"If the receiver has a unique name for reference, return it here, else return nil"[39;49;00m$
  4002^I$
  4003^I^I^ [04m[32mReferences[39;49;00m [32mkeyAtValue:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m][34m! ![39;49;00m$
  4004^I$
  4005^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'ar 5/16/2001 01:40'![39;49;00m$
  4006^I[32mupdateThresholdForGraphicInViewerTab[39;49;00m$
  4007^I^I[37m"When a Viewer is open on the receiver, its tab needs some graphic to show to the user. Computing this graphic can take quite some time so we want to make the update frequency depending on how long it takes to compute the thumbnail. The threshold returned by this method defines that the viewer will update at most every 'threshold * timeItTakesToDraw' milliseconds. Thus, if the time for computing the receiver's thumbnail is 200 msecs and the the threshold is 10, the viewer will update at most every two seconds."[39;49;00m$
  4008^I^I^[34m20[39;49;00m [37m"seems to be a pretty good general choice"[39;49;00m[34m! ![39;49;00m$
  4009^I$
  4010^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 3/9/2001 13:48'![39;49;00m$
  4011^I[32musableMethodInterfacesIn:[39;49;00m [31maListOfMethodInterfaces[39;49;00m$
  4012^I^I[37m"Filter aList, returning a subset list of apt phrases"[39;49;00m$
  4013^I$
  4014^I^I^ [31maListOfMethodInterfaces[39;49;00m$
  4015^I[34m! ![39;49;00m$
  4016^I$
  4017^I$
  4018^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'world hacking'[39;49;00m[34m stamp: 'ar 3/17/2001 23:45'![39;49;00m$
  4019^I[32mcouldOpenInMorphic[39;49;00m$
  4020^I$
  4021^I        [37m"is there an obvious morphic world in which to open a new morph?"[39;49;00m$
  4022^I$
  4023^I        ^[04m[32mWorld[39;49;00m [32mnotNil[39;49;00m [32mor:[39;49;00m [[04m[32mActiveWorld[39;49;00m [32mnotNil[39;49;00m][34m! ![39;49;00m$
  4024^I$
  4025^I$
  4026^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m![39;49;00m$
  4027^I[32merrorImproperStore[39;49;00m$
  4028^I^I[37m"Create an error notification that an improper store was attempted."[39;49;00m$
  4029^I$
  4030^I^I[36mself[39;49;00m [32merror:[39;49;00m [33m'Improper store into indexable object'[39;49;00m[34m! ![39;49;00m$
  4031^I$
  4032^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m![39;49;00m$
  4033^I[32merrorNonIntegerIndex[39;49;00m$
  4034^I^I[37m"Create an error notification that an improper object was used as an index."[39;49;00m$
  4035^I$
  4036^I^I[36mself[39;49;00m [32merror:[39;49;00m [33m'only integers should be used as indices'[39;49;00m[34m! ![39;49;00m$
  4037^I$
  4038^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m stamp: 'yo 6/29/2004 11:37'![39;49;00m$
  4039^I[32merrorNotIndexable[39;49;00m$
  4040^I^I[37m"Create an error notification that the receiver is not indexable."[39;49;00m$
  4041^I$
  4042^I^I[36mself[39;49;00m [32merror:[39;49;00m ([33m'Instances of {1} are not indexable'[39;49;00m [32mtranslated[39;49;00m [32mformat:[39;49;00m {[36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m})[34m! ![39;49;00m$
  4043^I$
  4044^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m![39;49;00m$
  4045^I[32merrorSubscriptBounds:[39;49;00m [31mindex[39;49;00m $
  4046^I^I[37m"Create an error notification that an improper integer was used as an index."[39;49;00m$
  4047^I$
  4048^I^I[36mself[39;49;00m [32merror:[39;49;00m [33m'subscript is out of bounds: '[39;49;00m [32m,[39;49;00m [31mindex[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
  4049^I$
  4050^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m stamp: 'ar 2/6/2004 14:47'![39;49;00m$
  4051^I[32mprimitiveError:[39;49;00m [31maString[39;49;00m $
  4052^I^I[37m"This method is called when the error handling results in a recursion in [39;49;00m$
  4053^I[37m^Icalling on error: or halt or halt:."[39;49;00m$
  4054^I$
  4055^I^I|[31m context [39;49;00m|$
  4056^I^I([04m[32mString[39;49;00m$
  4057^I^I^I[32mstreamContents:[39;49;00m $
  4058^I^I^I^I[:[31ms[39;49;00m |$
  4059^I^I^I^I[31ms[39;49;00m [32mnextPutAll:[39;49;00m [33m'***System error handling failed***'[39;49;00m.$
  4060^I^I^I^I[31ms[39;49;00m [32mcr[39;49;00m; [32mnextPutAll:[39;49;00m [31maString[39;49;00m.$
  4061^I^I^I^I[31mcontext[39;49;00m _ [36mthisContext[39;49;00m [32msender[39;49;00m [32msender[39;49;00m.$
  4062^I^I^I^I[34m20[39;49;00m [36mtimesRepeat:[39;49;00m [[31mcontext[39;49;00m [32m==[39;49;00m [36mnil[39;49;00m [36mifFalse:[39;49;00m [[31ms[39;49;00m [32mcr[39;49;00m; [32mprint:[39;49;00m ([31mcontext[39;49;00m _ [31mcontext[39;49;00m [32msender[39;49;00m)]].$
  4063^I^I^I^I[31ms[39;49;00m [32mcr[39;49;00m; [32mnextPutAll:[39;49;00m [33m'-------------------------------'[39;49;00m.$
  4064^I^I^I^I[31ms[39;49;00m [32mcr[39;49;00m; [32mnextPutAll:[39;49;00m [33m'Type CR to enter an emergency evaluator.'[39;49;00m.$
  4065^I^I^I^I[31ms[39;49;00m [32mcr[39;49;00m; [32mnextPutAll:[39;49;00m [33m'Type any other character to restart.'[39;49;00m])$
  4066^I^I^I[32mdisplayAt:[39;49;00m [34m0[39;49;00m [32m@[39;49;00m [34m0[39;49;00m.$
  4067^I^I[[04m[32mSensor[39;49;00m [32mkeyboardPressed[39;49;00m] [32mwhileFalse[39;49;00m.$
  4068^I^I[04m[32mSensor[39;49;00m [32mkeyboard[39;49;00m [32m=[39;49;00m [04m[32mCharacter[39;49;00m [32mcr[39;49;00m [36mifTrue:[39;49;00m [[04m[32mTranscripter[39;49;00m [32memergencyEvaluator[39;49;00m].$
  4069^I^I[04m[32mSmalltalk[39;49;00m [32misMorphic[39;49;00m$
  4070^I^I^I[36mifTrue:[39;49;00m [[04m[32mWorld[39;49;00m [32minstall[39;49;00m [37m"init hands and redisplay"[39;49;00m]$
  4071^I^I^I[36mifFalse:[39;49;00m [[04m[32mScheduledControllers[39;49;00m [32msearchForActiveController[39;49;00m][34m! ![39;49;00m$
  4072^I$
  4073^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m![39;49;00m$
  4074^I[32mspecies[39;49;00m$
  4075^I^I[37m"Answer the preferred class for reconstructing the receiver.  For example, [39;49;00m$
  4076^I[37m^Icollections create new collections whenever enumeration messages such as [39;49;00m$
  4077^I[37m^Icollect: or select: are invoked.  The new kind of collection is determined by [39;49;00m$
  4078^I[37m^Ithe species of the original collection.  Species and class are not always the [39;49;00m$
  4079^I[37m^Isame.  For example, the species of Interval is Array."[39;49;00m$
  4080^I$
  4081^I^I^[36mself[39;49;00m [32mclass[39;49;00m[34m! ![39;49;00m$
  4082^I$
  4083^I[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m![39;49;00m$
  4084^I[32mstoreAt:[39;49;00m [31moffset[39;49;00m [32minTempFrame:[39;49;00m [31maContext[39;49;00m$
  4085^I^I[37m"This message had to get sent to an expression already on the stack[39;49;00m$
  4086^I[37m^Ias a Block argument being accessed by the debugger.[39;49;00m$
  4087^I[37m^IJust re-route it to the temp frame."[39;49;00m$
  4088^I^I^ [31maContext[39;49;00m [32mtempAt:[39;49;00m [31moffset[39;49;00m [32mput:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  4089^I$
  4090^I[34m"-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- "![39;49;00m$
  4091^I$
  4092^I[04m[32mObject class[39;49;00m[34m[39;49;00m$
  4093^I[34m^IinstanceVariableNames: [39;49;00m[33m''[39;49;00m[34m![39;49;00m$
  4094^I$
  4095^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-Widgets'[39;49;00m[34m stamp: 'gvc 4/17/2007 17:40'![39;49;00m$
  4096^I[32mtaskbarIcon[39;49;00m$
  4097^I^I[37m"Answer the icon for an instance of the receiver in a task bar[39;49;00m$
  4098^I[37m^Ior nil for the default."[39;49;00m$
  4099^I$
  4100^I^I^[36mnil[39;49;00m[34m! ![39;49;00m$
  4101^I$
  4102^I$
  4103^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-accessing'[39;49;00m[34m stamp: 'lr 3/27/2006 15:47'![39;49;00m$
  4104^I[32mdescription[39;49;00m$
  4105^I^I^ [04m[32mMADescriptionBuilder[39;49;00m [32mfor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
  4106^I$
  4107^I$
  4108^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'class initialization'[39;49;00m[34m stamp: 'ar 2/11/2001 02:00'![39;49;00m$
  4109^I[32mflushDependents[39;49;00m$
  4110^I^I[04m[32mDependentsFields[39;49;00m [32mkeysAndValuesDo:[39;49;00m[:[31mkey[39;49;00m :[31mdep[39;49;00m|$
  4111^I^I^I[31mkey[39;49;00m [32mifNotNil:[39;49;00m[[31mkey[39;49;00m [32mremoveDependent:[39;49;00m [36mnil[39;49;00m].$
  4112^I^I].$
  4113^I^I[04m[32mDependentsFields[39;49;00m [32mfinalizeValues[39;49;00m.[34m! ![39;49;00m$
  4114^I$
  4115^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'class initialization'[39;49;00m[34m stamp: 'rw 2/10/2002 13:09'![39;49;00m$
  4116^I[32mflushEvents[39;49;00m$
  4117^I^I[37m"Object flushEvents"[39;49;00m$
  4118^I$
  4119^I^I[04m[32mEventManager[39;49;00m [32mflushEvents[39;49;00m. [34m! ![39;49;00m$
  4120^I$
  4121^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'class initialization'[39;49;00m[34m stamp: 'rww 10/2/2001 07:35'![39;49;00m$
  4122^I[32minitialize[39;49;00m$
  4123^I^I[37m"Object initialize"[39;49;00m$
  4124^I^I[04m[32mDependentsFields[39;49;00m [32mifNil:[39;49;00m[[36mself[39;49;00m [32minitializeDependentsFields[39;49;00m].[34m! ![39;49;00m$
  4125^I$
  4126^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'class initialization'[39;49;00m[34m stamp: 'ar 2/11/2001 01:41'![39;49;00m$
  4127^I[32minitializeDependentsFields[39;49;00m$
  4128^I^I[37m"Object initialize"[39;49;00m$
  4129^I^I[04m[32mDependentsFields[39;49;00m _ [04m[32mWeakIdentityKeyDictionary[39;49;00m [36mnew[39;49;00m.$
  4130^I[34m! ![39;49;00m$
  4131^I$
  4132^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'class initialization'[39;49;00m[34m stamp: 'ar 2/11/2001 01:45'![39;49;00m$
  4133^I[32mreInitializeDependentsFields[39;49;00m$
  4134^I^I[37m"Object reInitializeDependentsFields"[39;49;00m$
  4135^I^I|[31m oldFields [39;49;00m|$
  4136^I^I[31moldFields[39;49;00m _ [04m[32mDependentsFields[39;49;00m.$
  4137^I^I[04m[32mDependentsFields[39;49;00m _ [04m[32mWeakIdentityKeyDictionary[39;49;00m [36mnew[39;49;00m.$
  4138^I^I[31moldFields[39;49;00m [32mkeysAndValuesDo:[39;49;00m[:[31mobj[39;49;00m :[31mdeps[39;49;00m|$
  4139^I^I^I[31mdeps[39;49;00m [32mdo:[39;49;00m[:[31md[39;49;00m| [31mobj[39;49;00m [32maddDependent:[39;49;00m [31md[39;49;00m]].$
  4140^I[34m! ![39;49;00m$
  4141^I$
  4142^I$
  4143^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'documentation'[39;49;00m[34m![39;49;00m$
  4144^I[32mhowToModifyPrimitives[39;49;00m$
  4145^I^I[37m"You are allowed to write methods which specify primitives, but please use [39;49;00m$
  4146^I[37m^Icaution.  If you make a subclass of a class which contains a primitive method, [39;49;00m$
  4147^I[37m^Ithe subclass inherits the primitive.  The message which is implemented [39;49;00m$
  4148^I[37m^Iprimitively may be overridden in the subclass (E.g., see at:put: in String's [39;49;00m$
  4149^I[37m^Isubclass Symbol).  The primitive behavior can be invoked using super (see [39;49;00m$
  4150^I[37m^ISymbol string:). [39;49;00m$
  4151^I[37m^I [39;49;00m$
  4152^I[37m^IA class which attempts to mimic the behavior of another class without being [39;49;00m$
  4153^I[37m^Iits subclass may or may not be able to use the primitives of the original class.  [39;49;00m$
  4154^I[37m^IIn general, if the instance variables read or written by a primitive have the [39;49;00m$
  4155^I[37m^Isame meanings and are in the same fields in both classes, the primitive will [39;49;00m$
  4156^I[37m^Iwork.  [39;49;00m$
  4157^I[37m[39;49;00m$
  4158^I[37m^IFor certain frequently used 'special selectors', the compiler emits a [39;49;00m$
  4159^I[37m^Isend-special-selector bytecode instead of a send-message bytecode.  [39;49;00m$
  4160^I[37m^ISpecial selectors were created because they offer two advantages.  Code [39;49;00m$
  4161^I[37m^Iwhich sends special selectors compiles into fewer bytes than normal.  For [39;49;00m$
  4162^I[37m^Isome pairs of receiver classes and special selectors, the interpreter jumps [39;49;00m$
  4163^I[37m^Idirectly to a primitive routine without looking up the method in the class.  [39;49;00m$
  4164^I[37m^IThis is much faster than a normal message lookup. [39;49;00m$
  4165^I[37m^I [39;49;00m$
  4166^I[37m^IA selector which is a special selector solely in order to save space has a [39;49;00m$
  4167^I[37m^Inormal behavior.  Methods whose selectors are special in order to [39;49;00m$
  4168^I[37m^Igain speed contain the comment, 'No Lookup'.  When the interpreter [39;49;00m$
  4169^I[37m^Iencounters a send-special-selector bytecode, it checks the class of the [39;49;00m$
  4170^I[37m^Ireceiver and the selector.  If the class-selector pair is a no-lookup pair, [39;49;00m$
  4171^I[37m^Ithen the interpreter swiftly jumps to the routine which implements the [39;49;00m$
  4172^I[37m^Icorresponding primitive.  (A special selector whose receiver is not of the [39;49;00m$
  4173^I[37m^Iright class to make a no-lookup pair, is looked up normally).  The pairs are [39;49;00m$
  4174^I[37m^Ilisted below.  No-lookup methods contain a primitive number specification, [39;49;00m$
  4175^I[37m^I<primitive: xx>, which is redundant.  Since the method is not normally looked [39;49;00m$
  4176^I[37m^Iup, deleting the primitive number specification cannot prevent this [39;49;00m$
  4177^I[37m^Iprimitive from running.  If a no-lookup primitive fails, the method is looked [39;49;00m$
  4178^I[37m^Iup normally, and the expressions in it are executed. [39;49;00m$
  4179^I[37m^I [39;49;00m$
  4180^I[37m^INo Lookup pairs of (class, selector) [39;49;00m$
  4181^I[37m^I [39;49;00m$
  4182^I[37m^ISmallInteger with any of^I^I+ - * /  \\  bitOr: bitShift: bitAnd:  // [39;49;00m$
  4183^I[37m^ISmallInteger with any of^I^I=  ~=  >  <  >=  <= [39;49;00m$
  4184^I[37m^IAny class with^I^I^I^I^I== [39;49;00m$
  4185^I[37m^IAny class with ^I^I^I^I^I@ [39;49;00m$
  4186^I[37m^IPoint with either of^I^I^I^Ix y [39;49;00m$
  4187^I[37m^IContextPart with^I^I^I^I^IblockCopy: [39;49;00m$
  4188^I[37m^IBlockContext with either of ^I^Ivalue value:[39;49;00m$
  4189^I[37m^I"[39;49;00m$
  4190^I$
  4191^I^I[36mself[39;49;00m [32merror:[39;49;00m [33m'comment only'[39;49;00m[34m! ![39;49;00m$
  4192^I$
  4193^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'documentation'[39;49;00m[34m![39;49;00m$
  4194^I[32mwhatIsAPrimitive[39;49;00m$
  4195^I^I[37m"Some messages in the system are responded to primitively. A primitive   [39;49;00m$
  4196^I[37m^Iresponse is performed directly by the interpreter rather than by evaluating   [39;49;00m$
  4197^I[37m^Iexpressions in a method. The methods for these messages indicate the   [39;49;00m$
  4198^I[37m^Ipresence of a primitive response by including <primitive: xx> before the   [39;49;00m$
  4199^I[37m^Ifirst expression in the method.   [39;49;00m$
  4200^I[37m^I  [39;49;00m$
  4201^I[37m^IPrimitives exist for several reasons. Certain basic or 'primitive' [39;49;00m$
  4202^I[37m^Ioperations cannot be performed in any other way. Smalltalk without [39;49;00m$
  4203^I[37m^Iprimitives can move values from one variable to another, but cannot add two [39;49;00m$
  4204^I[37m^ISmallIntegers together. Many methods for arithmetic and comparison [39;49;00m$
  4205^I[37m^Ibetween numbers are primitives. Some primitives allow Smalltalk to [39;49;00m$
  4206^I[37m^Icommunicate with I/O devices such as the disk, the display, and the keyboard. [39;49;00m$
  4207^I[37m^ISome primitives exist only to make the system run faster; each does the same [39;49;00m$
  4208^I[37m^Ithing as a certain Smalltalk method, and its implementation as a primitive is [39;49;00m$
  4209^I[37m^Ioptional.  [39;49;00m$
  4210^I[37m^I  [39;49;00m$
  4211^I[37m^IWhen the Smalltalk interpreter begins to execute a method which specifies a [39;49;00m$
  4212^I[37m^Iprimitive response, it tries to perform the primitive action and to return a [39;49;00m$
  4213^I[37m^Iresult. If the routine in the interpreter for this primitive is successful, [39;49;00m$
  4214^I[37m^Iit will return a value and the expressions in the method will not be evaluated. [39;49;00m$
  4215^I[37m^IIf the primitive routine is not successful, the primitive 'fails', and the [39;49;00m$
  4216^I[37m^ISmalltalk expressions in the method are executed instead. These [39;49;00m$
  4217^I[37m^Iexpressions are evaluated as though the primitive routine had not been [39;49;00m$
  4218^I[37m^Icalled.  [39;49;00m$
  4219^I[37m^I  [39;49;00m$
  4220^I[37m^IThe Smalltalk code that is evaluated when a primitive fails usually [39;49;00m$
  4221^I[37m^Ianticipates why that primitive might fail. If the primitive is optional, the [39;49;00m$
  4222^I[37m^Iexpressions in the method do exactly what the primitive would have done (See [39;49;00m$
  4223^I[37m^INumber @). If the primitive only works on certain classes of arguments, the [39;49;00m$
  4224^I[37m^ISmalltalk code tries to coerce the argument or appeals to a superclass to find [39;49;00m$
  4225^I[37m^Ia more general way of doing the operation (see SmallInteger +). If the [39;49;00m$
  4226^I[37m^Iprimitive is never supposed to fail, the expressions signal an error (see [39;49;00m$
  4227^I[37m^ISmallInteger asFloat).  [39;49;00m$
  4228^I[37m^I  [39;49;00m$
  4229^I[37m^IEach method that specifies a primitive has a comment in it. If the primitive is [39;49;00m$
  4230^I[37m^Ioptional, the comment will say 'Optional'. An optional primitive that is not [39;49;00m$
  4231^I[37m^Iimplemented always fails, and the Smalltalk expressions do the work [39;49;00m$
  4232^I[37m^Iinstead.  [39;49;00m$
  4233^I[37m^I [39;49;00m$
  4234^I[37m^IIf a primitive is not optional, the comment will say, 'Essential'. Some [39;49;00m$
  4235^I[37m^Imethods will have the comment, 'No Lookup'. See Object [39;49;00m$
  4236^I[37m^IhowToModifyPrimitives for an explanation of special selectors which are [39;49;00m$
  4237^I[37m^Inot looked up.  [39;49;00m$
  4238^I[37m^I  [39;49;00m$
  4239^I[37m^IFor the primitives for +, -, *, and bitShift: in SmallInteger, and truncated [39;49;00m$
  4240^I[37m^Iin Float, the primitive constructs and returns a 16-bit [39;49;00m$
  4241^I[37m^ILargePositiveInteger when the result warrants it. Returning 16-bit [39;49;00m$
  4242^I[37m^ILargePositiveIntegers from these primitives instead of failing is [39;49;00m$
  4243^I[37m^Ioptional in the same sense that the LargePositiveInteger arithmetic [39;49;00m$
  4244^I[37m^Iprimitives are optional. The comments in the SmallInteger primitives say, [39;49;00m$
  4245^I[37m^I'Fails if result is not a SmallInteger', even though the implementor has the [39;49;00m$
  4246^I[37m^Ioption to construct a LargePositiveInteger. For further information on [39;49;00m$
  4247^I[37m^Iprimitives, see the 'Primitive Methods' part of the chapter on the formal [39;49;00m$
  4248^I[37m^Ispecification of the interpreter in the Smalltalk book."[39;49;00m$
  4249^I$
  4250^I^I[36mself[39;49;00m [32merror:[39;49;00m [33m'comment only'[39;49;00m[34m! ![39;49;00m$
  4251^I$
  4252^I$
  4253^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'file list services'[39;49;00m[34m stamp: 'nk 6/12/2004 11:41'![39;49;00m$
  4254^I[32mfileReaderServicesForDirectory:[39;49;00m [31maFileDirectory[39;49;00m$
  4255^I^I[37m"Backstop"[39;49;00m$
  4256^I^I^[33m#([39;49;00m[33m)[39;49;00m[34m! ![39;49;00m$
  4257^I$
  4258^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'file list services'[39;49;00m[34m stamp: 'nk 6/12/2004 11:30'![39;49;00m$
  4259^I[32mfileReaderServicesForFile:[39;49;00m [31mfullName[39;49;00m [32msuffix:[39;49;00m [31msuffix[39;49;00m$
  4260^I^I[37m"Backstop"[39;49;00m$
  4261^I^I^[33m#([39;49;00m[33m)[39;49;00m[34m! ![39;49;00m$
  4262^I$
  4263^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'file list services'[39;49;00m[34m stamp: 'md 2/15/2006 17:20'![39;49;00m$
  4264^I[32mservices[39;49;00m$
  4265^I^I[37m"Backstop"[39;49;00m$
  4266^I^I^[33m#([39;49;00m[33m)[39;49;00m[34m! ![39;49;00m$
  4267^I$
  4268^I$
  4269^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 1/23/2003 09:45'![39;49;00m$
  4270^I[32mcategoryForUniclasses[39;49;00m$
  4271^I^I[37m"Answer the default system category into which to place unique-class instances"[39;49;00m$
  4272^I$
  4273^I^I^ [33m'UserObjects'[39;49;00m[34m! ![39;49;00m$
  4274^I$
  4275^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 7/28/97 15:56'![39;49;00m$
  4276^I[32mchooseUniqueClassName[39;49;00m$
  4277^I^I|[31m i className [39;49;00m|$
  4278^I^I[31mi[39;49;00m _ [34m1[39;49;00m.$
  4279^I^I[[31mclassName[39;49;00m _ ([36mself[39;49;00m [32mname[39;49;00m [32m,[39;49;00m [31mi[39;49;00m [32mprintString[39;49;00m) [32masSymbol[39;49;00m.$
  4280^I^I [04m[32mSmalltalk[39;49;00m [32mincludesKey:[39;49;00m [31mclassName[39;49;00m]$
  4281^I^I^I[36mwhileTrue:[39;49;00m [[31mi[39;49;00m _ [31mi[39;49;00m [32m+[39;49;00m [34m1[39;49;00m].$
  4282^I^I^ [31mclassName[39;49;00m[34m! ![39;49;00m$
  4283^I$
  4284^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'tk 8/22/1998 08:22'![39;49;00m$
  4285^I[32minitialInstance[39;49;00m$
  4286^I^I[37m"Answer the first instance of the receiver, generate an error if there is one already"[39;49;00m$
  4287^I^I[37m"self instanceCount > 0 ifTrue: [self error: 'instance(s) already exist.']."[39;49;00m$
  4288^I^I^I[37m"Debugging test that is very slow"[39;49;00m$
  4289^I^I^ [36mself[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
  4290^I$
  4291^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 5/5/2000 09:30'![39;49;00m$
  4292^I[32minitializedInstance[39;49;00m$
  4293^I^I^ [36mself[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
  4294^I$
  4295^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 10/16/2000 10:58'![39;49;00m$
  4296^I[32minstanceOfUniqueClass[39;49;00m$
  4297^I^I[37m"Answer an instance of a unique subclass of the receiver"[39;49;00m$
  4298^I$
  4299^I^I^ [36mself[39;49;00m [32minstanceOfUniqueClassWithInstVarString:[39;49;00m [33m''[39;49;00m [32mandClassInstVarString:[39;49;00m [33m''[39;49;00m[34m! ![39;49;00m$
  4300^I$
  4301^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'tk 8/22/1998 08:27'![39;49;00m$
  4302^I[32minstanceOfUniqueClassWithInstVarString:[39;49;00m [31minstVarString[39;49;00m [32mandClassInstVarString:[39;49;00m [31mclassInstVarString[39;49;00m$
  4303^I^I[37m"Create a unique class for the receiver, and answer an instance of it"[39;49;00m$
  4304^I$
  4305^I^I^ ([36mself[39;49;00m [32mnewUniqueClassInstVars:[39;49;00m [31minstVarString[39;49;00m $
  4306^I^I^I[32mclassInstVars:[39;49;00m [31mclassInstVarString[39;49;00m) [32minitialInstance[39;49;00m[34m! ![39;49;00m$
  4307^I$
  4308^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 10/23/1999 22:51'![39;49;00m$
  4309^I[32misUniClass[39;49;00m$
  4310^I^I^ [36mfalse[39;49;00m[34m! ![39;49;00m$
  4311^I$
  4312^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'ajh 5/23/2002 00:35'![39;49;00m$
  4313^I[32mnewFrom:[39;49;00m [31maSimilarObject[39;49;00m$
  4314^I^I[37m"Create an object that has similar contents to aSimilarObject.[39;49;00m$
  4315^I[37m^IIf the classes have any instance varaibles with the same names, copy them across.[39;49;00m$
  4316^I[37m^IIf this is bad for a class, override this method."[39;49;00m$
  4317^I$
  4318^I^I^ ([36mself[39;49;00m [32misVariable[39;49;00m$
  4319^I^I^I[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mbasicNew:[39;49;00m [31maSimilarObject[39;49;00m [32mbasicSize[39;49;00m]$
  4320^I^I^I[36mifFalse:[39;49;00m [[36mself[39;49;00m [32mbasicNew[39;49;00m]$
  4321^I^I  ) [32mcopySameFrom:[39;49;00m [31maSimilarObject[39;49;00m[34m! ![39;49;00m$
  4322^I$
  4323^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'tk 6/29/1998 12:11'![39;49;00m$
  4324^I[32mnewUniqueClassInstVars:[39;49;00m [31minstVarString[39;49;00m [32mclassInstVars:[39;49;00m [31mclassInstVarString[39;49;00m$
  4325^I^I[37m"Create a unique class for the receiver"[39;49;00m$
  4326^I$
  4327^I^I|[31m aName aClass [39;49;00m|$
  4328^I^I[36mself[39;49;00m [32misSystemDefined[39;49;00m [36mifFalse:[39;49;00m$
  4329^I^I^I[^ [31msuperclass[39;49;00m [32mnewUniqueClassInstVars:[39;49;00m [31minstVarString[39;49;00m [32mclassInstVars:[39;49;00m [31mclassInstVarString[39;49;00m].$
  4330^I^I[31maName[39;49;00m _ [36mself[39;49;00m [32mchooseUniqueClassName[39;49;00m.$
  4331^I^I[31maClass[39;49;00m _ [36mself[39;49;00m [32msubclass:[39;49;00m [31maName[39;49;00m [32minstanceVariableNames:[39;49;00m [31minstVarString[39;49;00m $
  4332^I^I^I[32mclassVariableNames:[39;49;00m [33m''[39;49;00m [32mpoolDictionaries:[39;49;00m [33m''[39;49;00m [32mcategory:[39;49;00m [36mself[39;49;00m [32mcategoryForUniclasses[39;49;00m.$
  4333^I^I[31mclassInstVarString[39;49;00m [32msize[39;49;00m [32m>[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m$
  4334^I^I^I[[31maClass[39;49;00m [32mclass[39;49;00m [32minstanceVariableNames:[39;49;00m [31mclassInstVarString[39;49;00m].$
  4335^I^I^ [31maClass[39;49;00m[34m! ![39;49;00m$
  4336^I$
  4337^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 7/28/97 15:56'![39;49;00m$
  4338^I[32mnewUserInstance[39;49;00m$
  4339^I^I[37m"Answer an instance of an appropriate class to serve as a user object in the containment hierarchy"[39;49;00m$
  4340^I$
  4341^I^I^ [36mself[39;49;00m [32minstanceOfUniqueClass[39;49;00m[34m! ![39;49;00m$
  4342^I$
  4343^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'nk 8/30/2004 07:57'![39;49;00m$
  4344^I[32mreadCarefullyFrom:[39;49;00m [31mtextStringOrStream[39;49;00m$
  4345^I^I[37m"Create an object based on the contents of textStringOrStream.  Return an error instead of putting up a SyntaxError window."[39;49;00m$
  4346^I$
  4347^I^I|[31m object [39;49;00m|$
  4348^I^I([04m[32mCompiler[39;49;00m [32mcouldEvaluate:[39;49;00m [31mtextStringOrStream[39;49;00m)$
  4349^I^I^I[36mifFalse:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'expected String, Stream, or Text'[39;49;00m].$
  4350^I^I[31mobject[39;49;00m _ [04m[32mCompiler[39;49;00m [32mevaluate:[39;49;00m [31mtextStringOrStream[39;49;00m [32mfor:[39;49;00m [36mnil[39;49;00m $
  4351^I^I^I^I^I[32mnotifying:[39;49;00m [33m#error:[39;49;00m [37m"signal we want errors"[39;49;00m [32mlogged:[39;49;00m [36mfalse[39;49;00m.$
  4352^I^I([31mobject[39;49;00m [32misKindOf:[39;49;00m [36mself[39;49;00m) [36mifFalse:[39;49;00m [[36mself[39;49;00m [32merror:[39;49;00m [36mself[39;49;00m [32mname[39;49;00m[32m,[39;49;00m [33m' expected'[39;49;00m].$
  4353^I^I^[31mobject[39;49;00m[34m! ![39;49;00m$
  4354^I$
  4355^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'nk 8/30/2004 07:57'![39;49;00m$
  4356^I[32mreadFrom:[39;49;00m [31mtextStringOrStream[39;49;00m$
  4357^I^I[37m"Create an object based on the contents of textStringOrStream."[39;49;00m$
  4358^I$
  4359^I^I|[31m object [39;49;00m|$
  4360^I^I([04m[32mCompiler[39;49;00m [32mcouldEvaluate:[39;49;00m [31mtextStringOrStream[39;49;00m)$
  4361^I^I^I[36mifFalse:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'expected String, Stream, or Text'[39;49;00m].$
  4362^I^I[31mobject[39;49;00m _ [04m[32mCompiler[39;49;00m [32mevaluate:[39;49;00m [31mtextStringOrStream[39;49;00m.$
  4363^I^I([31mobject[39;49;00m [32misKindOf:[39;49;00m [36mself[39;49;00m) [36mifFalse:[39;49;00m [[36mself[39;49;00m [32merror:[39;49;00m [36mself[39;49;00m [32mname[39;49;00m[32m,[39;49;00m [33m' expected'[39;49;00m].$
  4364^I^I^[31mobject[39;49;00m[34m! ![39;49;00m$
  4365^I$
  4366^I$
  4367^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 1/8/97'![39;49;00m$
  4368^I[32mcreateFrom:[39;49;00m [31maSmartRefStream[39;49;00m [32msize:[39;49;00m [31mvarsOnDisk[39;49;00m [32mversion:[39;49;00m [31minstVarList[39;49;00m$
  4369^I^I[37m"Create an instance of me so objects on the disk can be read in.  Tricky part is computing the size if variable.  Inst vars will be filled in later.  "[39;49;00m$
  4370^I$
  4371^I^I^ [36mself[39;49;00m [32misVariable[39;49;00m$
  4372^I^I^I[36mifFalse:[39;49;00m [[36mself[39;49;00m [32mbasicNew[39;49;00m]$
  4373^I^I^I[36mifTrue:[39;49;00m [[37m"instVarList is names of old class's inst vars plus a version number"[39;49;00m $
  4374^I^I^I^I^I[36mself[39;49;00m [32mbasicNew:[39;49;00m ([31mvarsOnDisk[39;49;00m [32m-[39;49;00m ([31minstVarList[39;49;00m [32msize[39;49;00m [32m-[39;49;00m [34m1[39;49;00m))]$
  4375^I[34m! ![39;49;00m$
  4376^I$
  4377^I$
  4378^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'window color'[39;49;00m[34m stamp: 'nk 6/10/2004 08:10'![39;49;00m$
  4379^I[32mwindowColorSpecification[39;49;00m$
  4380^I^I[37m"Answer a WindowColorSpec object that declares my preference.[39;49;00m$
  4381^I[37m^IThis is a backstop for classes that don't otherwise define a preference."[39;49;00m$
  4382^I$
  4383^I^I^ [04m[32mWindowColorSpec[39;49;00m [32mclassSymbol:[39;49;00m [36mself[39;49;00m [32mname[39;49;00m$
  4384^I^I^I[32mwording:[39;49;00m [33m'Default'[39;49;00m [32mbrightColor:[39;49;00m [33m#white[39;49;00m$
  4385^I^I^I[32mpastelColor:[39;49;00m [33m#white[39;49;00m$
  4386^I^I^I[32mhelpMessage:[39;49;00m [33m'Other windows without color preferences.'[39;49;00m[34m! ![39;49;00m$
  4387^I$
  4388^I$
  4389^I[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m stamp: 'mir 8/22/2001 15:20'![39;49;00m$
  4390^I[32mreleaseExternalSettings[39;49;00m$
  4391^I^I[37m"Do nothing as a default"[39;49;00m[34m! ![39;49;00m$
  4392^I$
  4393^I$
  4394^I[04m[32mObject[39;49;00m [32minitialize[39;49;00m[32m![39;49;00m$
