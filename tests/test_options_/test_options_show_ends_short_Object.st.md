![04m[32mProtoObject[39;49;00m [32msubclass:[39;49;00m [33m#Object[39;49;00m$
	[32minstanceVariableNames:[39;49;00m [33m''[39;49;00m$
	[32mclassVariableNames:[39;49;00m [33m'DependentsFields'[39;49;00m$
	[32mpoolDictionaries:[39;49;00m [33m''[39;49;00m$
	[32mcategory:[39;49;00m [33m'Kernel-Objects'[39;49;00m[32m![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'gk 2/24/2004 08:49'![39;49;00m$
[32mbeep[39;49;00m$
	[37m"Deprecated."[39;49;00m$
	$
	[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use Beeper class>>beep instead.'[39;49;00m.$
	[04m[32mBeeper[39;49;00m [32mbeep[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'gk 2/24/2004 08:50'![39;49;00m$
[32mbeepPrimitive[39;49;00m$
	[37m"Deprecated. Beep in the absence of sound support."[39;49;00m$
	$
	[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use Beeper class>>beep or Beeper class>>beepPrimitive instead.'[39;49;00m.$
	[04m[32mBeeper[39;49;00m [32mbeepPrimitive[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'md 12/12/2003 17:02'![39;49;00m$
[32mbeep:[39;49;00m [31msoundName[39;49;00m$
	[37m"Make the given sound, unless the making of sound is disabled in Preferences."[39;49;00m$
$
	[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use SampledSound>>playSoundNamed: instead.'[39;49;00m.$
	[04m[32mPreferences[39;49;00m [32msoundsEnabled[39;49;00m$
		[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mplaySoundNamed:[39;49;00m [31msoundName[39;49;00m]$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'sd 11/19/2004 16:57'![39;49;00m$
[32mcontentsGetz:[39;49;00m [31mx[39;49;00m$
	[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'there is no method named contents in object and in addition only one sender in a method not called'[39;49;00m. $
	[36mself[39;49;00m [32mcontents:[39;49;00m [31mx[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'sd 11/13/2003 21:10'![39;49;00m$
[32mdeprecatedExplanation:[39;49;00m [31maString[39;49;00m$
     [37m"This method is OBSOLETE.  Use #deprecated: instead."[39;49;00m$
	[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use Object>>deprecated: instead of deprecatedExplanation:.'[39;49;00m.$
$
	[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
		[[04m[32mDeprecation[39;49;00m [32msignal:[39;49;00m ([33m'{1} has been deprecated. {2}'[39;49;00m [32mtranslated[39;49;00m [32mformat:[39;49;00m {[36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m. [31maString[39;49;00m})][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'sd 11/13/2003 21:11'![39;49;00m$
[32mdeprecated:[39;49;00m [31maBlock[39;49;00m [32mexplanation:[39;49;00m [31maString[39;49;00m $
	 [37m"This method is OBSOLETE.  Use #deprecated:block: instead."[39;49;00m$
	[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use Object>>deprecated:block: instead of deprecated:explanation:.'[39;49;00m.$
$
	[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
		[[04m[32mDeprecation[39;49;00m$
			[32msignal:[39;49;00m ([33m'{1} has been deprecated. {2}'[39;49;00m [32mtranslated[39;49;00m [32mformat:[39;49;00m {[36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m. [31maString[39;49;00m})].$
	^ [31maBlock[39;49;00m [32mvalue[39;49;00m.$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'md 12/12/2003 16:25'![39;49;00m$
[32mdoIfNotNil:[39;49;00m [31maBlock[39;49;00m$
	[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'use ifNotNilDo:'[39;49;00m.$
	^ [36mself[39;49;00m [32mifNotNilDo:[39;49;00m [31maBlock[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'md 11/27/2004 12:20'![39;49;00m$
[32mifKindOf:[39;49;00m [31maClass[39;49;00m [32mthenDo:[39;49;00m [31maBlock[39;49;00m$
	[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Deprecated. Just use #isKindOf:'[39;49;00m.$
	^ ([36mself[39;49;00m [32misKindOf:[39;49;00m [31maClass[39;49;00m) [36mifTrue:[39;49;00m [[31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*39Deprecated'[39;49;00m[34m stamp: 'gk 2/23/2004 20:51'![39;49;00m$
[32mplaySoundNamed:[39;49;00m [31msoundName[39;49;00m$
	[37m"Deprecated.[39;49;00m$
[37m	Play the sound with the given name."[39;49;00m$
$
	[36mself[39;49;00m [32mdeprecated:[39;49;00m [33m'Use "SoundService default playSoundNamed: aName" instead.'[39;49;00m.$
	[04m[32mSoundService[39;49;00m [32mdefault[39;49;00m [32mplaySoundNamed:[39;49;00m [31msoundName[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:23'![39;49;00m$
[32maidaCanBeLocked[39;49;00m$
	[37m"can we get an exclusive lock on that object (not already locked)?"[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:23'![39;49;00m$
[32maidaDontCache[39;49;00m$
	[37m"don't cache web content in a browser. Appropriate header is added to http response"[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:24'![39;49;00m$
[32maidaIsLocked[39;49;00m$
	[37m"is object locked exclusively?"[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:24'![39;49;00m$
[32maidaLock[39;49;00m$
	[37m"get an exclusive lock on that object. Until unlocked, noon else can get that lock. Return false if already locked, true if successfull"[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:24'![39;49;00m$
[32maidaUnlock[39;49;00m$
	[37m"release an exclusive lock if any"[39;49;00m$
	^[36mtrue[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:24'![39;49;00m$
[32mapp[39;49;00m$
	[37m"fastest and most convinient way to find a web app for that object"[39;49;00m$
	^[36mself[39;49;00m [32mwebAppFor:[39;49;00m [36mself[39;49;00m [32mfirstSessionFromStack[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:25'![39;49;00m$
[32mcontentType[39;49;00m$
$
	[37m"Janko Mivsek, apr98"[39;49;00m$
	[37m"return 'text/html' as content type for web pages"[39;49;00m$
$
	^[33m'text/html'[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:25'![39;49;00m$
[32mdeepSearchOfClass:[39;49;00m [31maClassName[39;49;00m$
	[37m"finf all objects of that class down in object hierarchy"[39;49;00m$
	|[31m objectDictionary class [39;49;00m|$
	[31mobjectDictionary[39;49;00m := [04m[32mIdentityDictionary[39;49;00m [36mnew[39;49;00m.$
	[36mself[39;49;00m [32mdeepCopyNotIn:[39;49;00m [31mobjectDictionary[39;49;00m.$
	[31mclass[39;49;00m := [31maClassName[39;49;00m [32masSymbol[39;49;00m.$
	^[31mobjectDictionary[39;49;00m [32mkeys[39;49;00m [32mselect:[39;49;00m [:[31meach[39;49;00m | [31meach[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32m=[39;49;00m [31mclass[39;49;00m].[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:26'![39;49;00m$
[32mdeepSearchOfObsoleteClasses[39;49;00m$
	[37m"find all objects of obsolete classes down in object hierarchy"[39;49;00m$
	|[31m objectDictionary [39;49;00m|$
	[31mobjectDictionary[39;49;00m := [04m[32mIdentityDictionary[39;49;00m [36mnew[39;49;00m.$
	[36mself[39;49;00m [32mdeepCopyNotIn:[39;49;00m [31mobjectDictionary[39;49;00m.$
	^[31mobjectDictionary[39;49;00m [32mkeys[39;49;00m [32mselect:[39;49;00m [:[31meach[39;49;00m | [31meach[39;49;00m [32mclass[39;49;00m [32misObsolete[39;49;00m].[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:26'![39;49;00m$
[32mexpiresTimestamp[39;49;00m$
	[37m"until when content of this object wont be changed"[39;49;00m$
	[37m"used in http response, override if you like to be included"[39;49;00m$
	^[36mself[39;49;00m [32mmodifiedTimestamp[39;49;00m  [37m"to reload pages immediately"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:26'![39;49;00m$
[32mfirstAppFromStack[39;49;00m$
	[37m"try to find a first sender up in calling stack, who is  WebApplication"[39;49;00m$
	|[31m context [39;49;00m|$
	[31mcontext[39;49;00m := [36mthisContext[39;49;00m.$
	[[31mcontext[39;49;00m [32mnotNil[39;49;00m] [36mwhileTrue:[39;49;00m [$
		([31mcontext[39;49;00m [32mreceiver[39;49;00m [32misKindOf:[39;49;00m [04m[32mWebApplication[39;49;00m) [36mifTrue:[39;49;00m [^[31mcontext[39;49;00m [32mreceiver[39;49;00m].$
		[31mcontext[39;49;00m := [31mcontext[39;49;00m [32msender[39;49;00m].$
	^[36mself[39;49;00m [32mfirstSessionFromStack[39;49;00m [32mlastApp[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/25/2007 21:34'![39;49;00m$
[32mfirstSessionFromStack[39;49;00m$
	[37m"try to find a first sender up in calling stack, who is  AIDASite and get session if that call"[39;49;00m$
	|[31m context [39;49;00m|$
	[31mcontext[39;49;00m := [36mthisContext[39;49;00m.$
	[[31mcontext[39;49;00m [32mnotNil[39;49;00m] [36mwhileTrue:[39;49;00m [$
		([31mcontext[39;49;00m [32mreceiver[39;49;00m [32misKindOf:[39;49;00m [04m[32mAIDASite[39;49;00m) [36mifTrue:[39;49;00m 	[^([31mcontext[39;49;00m [32mat:[39;49;00m [34m3[39;49;00m) [37m"always?"[39;49;00m].$
		[31mcontext[39;49;00m := [31mcontext[39;49;00m [32msender[39;49;00m].$
	^[36mnil[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'mivsek 1/10/2008 18:14'![39;49;00m$
[32mforLanguage:[39;49;00m [31maLanguageCodeSymbol[39;49;00m$
	[37m"for multilingual support: returns an apropriate instance of itself for that language. [39;49;00m$
[37m	Langage is defined by ISO 639 2-letter language code, see [39;49;00m$
[37m	http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes"[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'mivsek 1/10/2008 18:14'![39;49;00m$
[32misMultilingual[39;49;00m$
	[37m"for multilingual support: override this if your domain object responds [39;49;00m$
[37m	to #forLanguage: and returns an apropriate instance of itself for that language"[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:27'![39;49;00m$
[32misVersionedObject[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:27'![39;49;00m$
[32misWebApplication[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:27'![39;49;00m$
[32misWebStyle[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:27'![39;49;00m$
[32mmodifiedTimestamp[39;49;00m$
	[37m"when this object was last modified"[39;49;00m$
	[37m"used in http response, override if you like to be included"[39;49;00m$
	^[36mnil[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:28'![39;49;00m$
[32mpreferedUrl[39;49;00m$
	[37m"override with a suggestion for url of this method!! If not already used, [39;49;00m$
[37m	it will be considered by URLResolver during automatic url generation"[39;49;00m$
	^[36mnil[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:28'![39;49;00m$
[32mprintWebAppNotFoundFor:[39;49;00m [31maSession[39;49;00m $
	|[31m page [39;49;00m|$
	[31mpage[39;49;00m := [04m[32mWebPage[39;49;00m [36mnew[39;49;00m.$
	[31mpage[39;49;00m [32maddText:[39;49;00m [33m'Cannot find aWebApplication for object a'[39;49;00m[32m,[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m.$
	^[31mpage[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:28'![39;49;00m$
[32mprintWebPageFor:[39;49;00m [31maSession[39;49;00m $
	[37m"find appropriate web application to represent self as web page"[39;49;00m$
$
	|[31m webApp [39;49;00m|$
	[31mwebApp[39;49;00m := [36mself[39;49;00m [32mwebAppFor:[39;49;00m [31maSession[39;49;00m.$
	^[31mwebApp[39;49;00m [32mnotNil[39;49;00m $
		[36mifTrue:[39;49;00m [[31mwebApp[39;49;00m [32mprintWebPage[39;49;00m]$
		[36mifFalse:[39;49;00m [[36mself[39;49;00m [32mprintWebAppNotFoundFor:[39;49;00m [31maSession[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:29'![39;49;00m$
[32msendOver:[39;49;00m [31maStream[39;49;00m $
	[37m"from Wiki rendering"[39;49;00m$
	[36mself[39;49;00m [32mprintOn:[39;49;00m [31maStream[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Aida'[39;49;00m[34m stamp: 'JM 4/22/2007 15:29'![39;49;00m$
[32mwebAppFor:[39;49;00m [31maSession[39;49;00m$
	|[31m webApp [39;49;00m|$
	[31maSession[39;49;00m [32misNil[39;49;00m [36mifTrue:[39;49;00m [^[36mnil[39;49;00m].$
	[31mwebApp[39;49;00m := [31maSession[39;49;00m [32mwebAppFor:[39;49;00m [36mself[39;49;00m.$
	[31mwebApp[39;49;00m [32mnotNil[39;49;00m [36mifTrue:[39;49;00m [^[31mwebApp[39;49;00m].$
	[31mwebApp[39;49;00m := [04m[32mWebApplication[39;49;00m [32mnewFor:[39;49;00m [36mself[39;49;00m [32mon:[39;49;00m [31maSession[39;49;00m.$
	[31mwebApp[39;49;00m [32mnotNil[39;49;00m [36mifTrue:[39;49;00m [[31maSession[39;49;00m [32maddWebApp:[39;49;00m [31mwebApp[39;49;00m [32mfor:[39;49;00m [36mself[39;49;00m].$
	^[31mwebApp[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*DynamicBindings'[39;49;00m[34m stamp: 'svp 3/6/2003 16:08'![39;49;00m$
[32mbinding[39;49;00m$
	[37m"Answer the DynamicBinding for the receiver (if any)"[39;49;00m$
$
	^[04m[32mBindings[39;49;00m [32mbindingFor:[39;49;00m [36mself[39;49;00m [32mifNotBound:[39;49;00m [[36mnil[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*DynamicBindings'[39;49;00m[34m stamp: 'svp 4/29/2003 00:35'![39;49;00m$
[32mbinding:[39;49;00m [31manObject[39;49;00m$
	[37m"Set the dynamic binding for the receiver, if anObject is nil, then [39;49;00m$
[37m	remove the receiver's dynamic binding (if any)"[39;49;00m$
$
	^[31manObject[39;49;00m $
		[32mifNil:[39;49;00m [[36mself[39;49;00m [32mremoveBinding[39;49;00m]$
		[32mifNotNil:[39;49;00m [[04m[32mBindings[39;49;00m [32mbind:[39;49;00m [36mself[39;49;00m [32mto:[39;49;00m [31manObject[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*DynamicBindings'[39;49;00m[34m stamp: 'svp 3/6/2003 16:09'![39;49;00m$
[32mhasBinding[39;49;00m$
	[37m"Answer whether or not the receiver has a dynamic binding"[39;49;00m$
$
	^[04m[32mBindings[39;49;00m [32mincludesKey:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*DynamicBindings'[39;49;00m[34m stamp: 'svp 3/6/2003 16:09'![39;49;00m$
[32mremoveBinding[39;49;00m$
	[37m"Remove the dynamic binding associated with the receiver"[39;49;00m$
$
	^[04m[32mBindings[39;49;00m [32mremoveKey:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m [][34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*KomHttpServer'[39;49;00m[34m stamp: 'SVP 8/23/1999 19:17'![39;49;00m$
[32masHtmlDocumentForRequest:[39;49;00m [31maNetworkRequest[39;49;00m$
$
	[36mself[39;49;00m [32merror:[39;49;00m $
		([33m'The requested object ('[39;49;00m[32m,[39;49;00m $
		[36mself[39;49;00m [32masString[39;49;00m[32m,[39;49;00m $
		[33m'), could not be converted into HTML for your browser.'[39;49;00m)[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*KomHttpServer'[39;49;00m[34m stamp: 'SVP 8/23/1999 19:23'![39;49;00m$
[32masHttpResponseTo:[39;49;00m [31manHttpRequest[39;49;00m$
$
	^([36mself[39;49;00m [32masHtmlDocumentForRequest:[39;49;00m [31manHttpRequest[39;49;00m) $
		[32masHttpResponseTo:[39;49;00m [31manHttpRequest[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*KomHttpServer'[39;49;00m[34m stamp: 'svp 5/16/2003 12:47'![39;49;00m$
[32misComancheModule[39;49;00m$
$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*KomHttpServer'[39;49;00m[34m stamp: 'SVP 8/17/1999 17:51'![39;49;00m$
[32mmimeType[39;49;00m$
$
	^[04m[32mMIMEDocument[39;49;00m [32mdefaultContentType[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Morphic-NewCurve-testing'''[39;49;00m[34m stamp: 'wiz 12/31/2005 21:31'![39;49;00m$
[32misNonZero[39;49;00m$
[37m"Overriden in Number. This returns the backstop answer for non-numbers"[39;49;00m$
^[36mfalse[39;49;00m.[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/25/2006 18:18'![39;49;00m$
[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
[32mto:[39;49;00m [31manObject[39;49;00m$
[32mexclusive:[39;49;00m [31maValueHolder[39;49;00m$
 $
	[36mself[39;49;00m$
		[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
		[32mevaluate:[39;49;00m (([04m[32mExclusiveWeakMessageSend[39;49;00m$
					[32mreceiver:[39;49;00m [31manObject[39;49;00m$
					[32mselector:[39;49;00m [31maMessageSelector[39;49;00m)$
						[32mbasicExecuting:[39;49;00m [31maValueHolder[39;49;00m)[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/25/2006 18:17'![39;49;00m$
[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
[32mto:[39;49;00m [31manObject[39;49;00m$
[32mwith:[39;49;00m [31manArg[39;49;00m$
[32mexclusive:[39;49;00m [31maValueHolder[39;49;00m$
 $
    [36mself[39;49;00m$
        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
        [32mevaluate:[39;49;00m (([04m[32mExclusiveWeakMessageSend[39;49;00m$
 		[32mreceiver:[39;49;00m [31manObject[39;49;00m$
		[32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
		[32marguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manArg[39;49;00m))$
			[32mbasicExecuting:[39;49;00m [31maValueHolder[39;49;00m)[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/25/2006 18:17'![39;49;00m$
[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
[32mto:[39;49;00m [31manObject[39;49;00m$
[32mwithArguments:[39;49;00m [31manArgArray[39;49;00m$
[32mexclusive:[39;49;00m [31maValueHolder[39;49;00m$
 $
    [36mself[39;49;00m$
        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
        [32mevaluate:[39;49;00m (([04m[32mExclusiveWeakMessageSend[39;49;00m$
		[32mreceiver:[39;49;00m [31manObject[39;49;00m$
		[32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
		[32marguments:[39;49;00m [31manArgArray[39;49;00m)$
			[32mbasicExecuting:[39;49;00m [31maValueHolder[39;49;00m)[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/24/2006 11:50'![39;49;00m$
[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
[32msendOnce:[39;49;00m [31maMessageSelector[39;49;00m$
[32mto:[39;49;00m [31manObject[39;49;00m$
 $
    [36mself[39;49;00m$
        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
        [32mevaluate:[39;49;00m ([04m[32mNonReentrantWeakMessageSend[39;49;00m$
            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m)[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/24/2006 11:49'![39;49;00m$
[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
[32msendOnce:[39;49;00m [31maMessageSelector[39;49;00m$
[32mto:[39;49;00m [31manObject[39;49;00m$
[32mwith:[39;49;00m [31manArg[39;49;00m$
 $
    [36mself[39;49;00m$
        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
        [32mevaluate:[39;49;00m ([04m[32mNonReentrantWeakMessageSend[39;49;00m$
            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
		[32marguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manArg[39;49;00m))[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-EventEnhancements'[39;49;00m[34m stamp: 'gvc 10/24/2006 11:49'![39;49;00m$
[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
[32msendOnce:[39;49;00m [31maMessageSelector[39;49;00m$
[32mto:[39;49;00m [31manObject[39;49;00m$
[32mwithArguments:[39;49;00m [31manArgArray[39;49;00m$
 $
    [36mself[39;49;00m$
        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
        [32mevaluate:[39;49;00m ([04m[32mNonReentrantWeakMessageSend[39;49;00m$
            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
		[32marguments:[39;49;00m [31manArgArray[39;49;00m)[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-Widgets'[39;49;00m[34m stamp: 'gvc 1/10/2007 11:41'![39;49;00m$
[32mokToClose[39;49;00m$
	[37m"Sent to models when a window closing.[39;49;00m$
[37m	Allows this check to be independent of okToChange."[39;49;00m$
	$
	^[36mtrue[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-Widgets'[39;49;00m[34m stamp: 'gvc 4/17/2007 17:41'![39;49;00m$
[32mtaskbarIcon[39;49;00m$
	[37m"Answer the icon for the receiver in a task bar[39;49;00m$
[37m	or nil for the default."[39;49;00m$
$
	^[36mself[39;49;00m [32mclass[39;49;00m [32mtaskbarIcon[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-Widgets-override'[39;49;00m[34m stamp: 'gvc 9/4/2007 12:32'![39;49;00m$
[32mwindowActiveOnFirstClick[39;49;00m$
	[37m"Return true if my window should be active on first click."[39;49;00m$
$
	^[36mtrue[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*SeasideAdaptersCompatibility'[39;49;00m[34m stamp: 'pmm 11/25/2007 14:17'![39;49;00m$
[32mtoString[39;49;00m$
	^[36mself[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Tools-Explorer'[39;49;00m[34m stamp: 'stephaneducasse 9/17/2005 21:52'![39;49;00m$
[32mexploreAndYourself[39;49;00m$
	[37m"i.e. explore; yourself. Thisway i can peek w/o typing all the parentheses"[39;49;00m$
	[36mself[39;49;00m [32mexplore[39;49;00m. $
     ^[36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*Tools-Explorer'[39;49;00m[34m stamp: 'stephaneducasse 9/17/2005 21:48'![39;49;00m$
[32mexploreWithLabel:[39;49;00m [31mlabel[39;49;00m$
$
	^ [04m[32mObjectExplorer[39;49;00m [36mnew[39;49;00m [32mopenExplorerFor:[39;49;00m [36mself[39;49;00m [32mwithLabel:[39;49;00m$
[31mlabel[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*kernel-extensions-flagging'[39;49;00m[34m stamp: 'mtf 1/26/2008 23:34'![39;49;00m$
[32mdeprecated[39;49;00m$
	[37m"Warn that the sending method has been deprecated."[39;49;00m$
$
	[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
		[[04m[32mDeprecation[39;49;00m [32msignal:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m' has been deprecated.'[39;49;00m][34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*kernel-extensions-flexibility'[39;49;00m[34m stamp: 'kph 1/27/2008 19:21'![39;49;00m$
[32maskFor:[39;49;00m [31mselector[39;49;00m $
$
    [37m"returns true or false"[39;49;00m$
	$
	^ ([36mself[39;49;00m [32maskFor:[39;49;00m [31mselector[39;49;00m [32mifAbsent:[39;49;00m [36mnil[39;49;00m) [32m==[39;49;00m [36mtrue[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*kernel-extensions-flexibility'[39;49;00m[34m stamp: 'kph 10/17/2007 14:01'![39;49;00m$
[32maskFor:[39;49;00m [31mselector[39;49;00m [32mifAbsent:[39;49;00m [31maBlock[39;49;00m$
$
   [37m"enables a default value to be specified in order to be tolerant of potentially missing methods[39;49;00m$
[37m	[39;49;00m$
[37m	e.g.[39;49;00m$
[37m	(myPoint askFor: #originOffset) ifAbsent: [ 0@0 ].[39;49;00m$
[37m	"[39;49;00m$
$
	^ ([36mself[39;49;00m [32mclass[39;49;00m [32mcanUnderstand:[39;49;00m [31mselector[39;49;00m) [36mifFalse:[39;49;00m [ [31maBlock[39;49;00m [32mvalue[39;49;00m ] [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m][34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*kernel-extensions-logging'[39;49;00m[34m stamp: 'mtf 1/26/2008 23:52'![39;49;00m$
[32mlog[39;49;00m$
	[37m"This method provides the univeral entry point fo all logging mechanisms"[39;49;00m$
	$
	[37m"Options:[39;49;00m$
[37m	1. Null for null logging[39;49;00m$
[37m	2. A LogRouter instance wih a FrameworkAdaptor.[39;49;00m$
[37m	3. CurrentLog a process local variable supplying a LogRouter"[39;49;00m$
	$
	^ ([04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#CurrentLog[39;49;00m [32mifAbsent:[39;49;00m [ [04m[32mNull[39;49;00m [32mdefault[39;49;00m ]) [32mvalue[39;49;00m$
		[32msender:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m; [32mbeginEntry[39;49;00m; [32myourself[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-accessing'[39;49;00m[34m stamp: 'lr 3/9/2006 11:31'![39;49;00m$
[32mdescription[39;49;00m$
	[37m"Return the description of the reciever. Subclasses might override this message to return instance-based descriptions."[39;49;00m$
$
	^ [36mself[39;49;00m [32mclass[39;49;00m [32mdescription[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-accessing'[39;49;00m[34m stamp: 'lr 3/9/2006 11:31'![39;49;00m$
[32mmementoClass[39;49;00m$
	[37m"Return a class to be used to remember or cache the receiver, namely a memento object."[39;49;00m$
$
	^ [04m[32mMACheckedMemento[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-model'[39;49;00m[34m stamp: 'lr 3/9/2006 11:31'![39;49;00m$
[32mreadUsing:[39;49;00m [31maDescription[39;49;00m$
	[37m"Dispatch the read-access to the receiver using the accessor of aDescription."[39;49;00m$
$
	^ [31maDescription[39;49;00m [32maccessor[39;49;00m [32mread:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-model'[39;49;00m[34m stamp: 'lr 3/9/2006 11:31'![39;49;00m$
[32mwrite:[39;49;00m [31manObject[39;49;00m [32musing:[39;49;00m [31maDescription[39;49;00m$
	[37m"Dispatch the write-access to the receiver of anObject using the accessor of aDescription."[39;49;00m$
$
	[31maDescription[39;49;00m [32maccessor[39;49;00m [32mwrite:[39;49;00m [31manObject[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-testing'[39;49;00m[34m stamp: 'lr 3/9/2006 11:31'![39;49;00m$
[32misDescription[39;49;00m$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-morph-converting'[39;49;00m[34m stamp: 'lr 3/9/2006 11:33'![39;49;00m$
[32masMorph[39;49;00m$
	^ [36mself[39;49;00m [32mdescription[39;49;00m [32masMorphOn:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-seaside-converting'[39;49;00m[34m stamp: 'lr 3/9/2006 11:33'![39;49;00m$
[32masComponent[39;49;00m$
	^ [36mself[39;49;00m [32mdescription[39;49;00m [32masComponentOn:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*monticello'[39;49;00m[34m stamp: 'dvf 8/10/2004 23:25'![39;49;00m$
[32misConflict[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*null'[39;49;00m[34m stamp: 'kph 9/6/2007 23:31'![39;49;00m$
[32mifNull:[39;49;00m [31maBlock[39;49;00m$
$
	^ [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*null'[39;49;00m[34m stamp: 'kph 9/6/2007 23:33'![39;49;00m$
[32misNull[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*null'[39;49;00m[34m stamp: 'kph 4/12/2007 08:27'![39;49;00m$
[32morNull[39;49;00m$
$
	^ [36mself[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*ob-tools-inspector'[39;49;00m[34m stamp: 'lr 6/5/2008 11:07'![39;49;00m$
[32mbasicInspectorNodes[39;49;00m$
	<[34minspector:[39;49;00m #'1' priority: 600>$
	$
	|[31m nodes [39;49;00m|$
	[31mnodes[39;49;00m := [04m[32mOrderedCollection[39;49;00m [32mnew:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32m+[39;49;00m [36mself[39;49;00m [32mbasicSize[39;49;00m [32m+[39;49;00m [34m5[39;49;00m.$
	[31mnodes[39;49;00m [32madd:[39;49;00m [36mself[39;49;00m [32mselfInspectorNode[39;49;00m.$
	[36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mwithIndexDo:[39;49;00m [ :[31mname[39;49;00m :[31mindex[39;49;00m |$
		[31mnodes[39;49;00m [32madd:[39;49;00m ([04m[32mOTNamedVariableNode[39;49;00m [32mon:[39;49;00m [36mself[39;49;00m [32mindex:[39;49;00m [31mindex[39;49;00m [32mname:[39;49;00m [31mname[39;49;00m) ].$
	[34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32mbasicSize[39;49;00m [32mdo:[39;49;00m [ :[31mindex[39;49;00m |$
		[31mnodes[39;49;00m [32madd:[39;49;00m ([04m[32mOTIndexedVariableNode[39;49;00m [32mon:[39;49;00m [36mself[39;49;00m [32mindex:[39;49;00m [31mindex[39;49;00m) ].$
	^ [31mnodes[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*ob-tools-inspector'[39;49;00m[34m stamp: 'lr 6/5/2008 11:07'![39;49;00m$
[32mprotocolInspectorNodes[39;49;00m$
	<[34minspector:[39;49;00m #'#' priority: 800>$
$
	^ [36mself[39;49;00m [32mclass[39;49;00m [32mallSelectors[39;49;00m [32masArray[39;49;00m [32msort[39;49;00m$
		[32mcollect:[39;49;00m [ :[31meach[39;49;00m | [04m[32mOTProtocolInspectorNode[39;49;00m [32mon:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [31meach[39;49;00m ][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*ob-tools-inspector'[39;49;00m[34m stamp: 'lr 6/5/2008 09:58'![39;49;00m$
[32mselfInspectorNode[39;49;00m$
	^ [04m[32mOTDerivedInspectorNode[39;49;00m [32mon:[39;49;00m [36mself[39;49;00m [32mlabel:[39;49;00m [33m'self'[39;49;00m [32mblock:[39;49;00m [ :[31mobj[39;49;00m | [31mobj[39;49;00m ][34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*omnibrowser-converting'[39;49;00m[34m stamp: 'cwp 4/17/2006 12:16'![39;49;00m$
[32masAnnouncement[39;49;00m$
	^ [36mself[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*pier-model'[39;49;00m[34m stamp: 'lr 3/9/2006 11:29'![39;49;00m$
[32maccept:[39;49;00m [31maVisitor[39;49;00m$
	[36mself[39;49;00m [32msubclassResponsibility[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*pier-model'[39;49;00m[34m stamp: 'lr 3/9/2006 11:29'![39;49;00m$
[32macceptDecorated:[39;49;00m [31maVisitor[39;49;00m$
	[36mself[39;49;00m [32maccept:[39;49;00m [31maVisitor[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*rio-kernel'[39;49;00m[34m stamp: 'kph 3/8/2007 21:25'![39;49;00m$
[32misRio[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*scriptaculous'[39;49;00m[34m stamp: 'lr 1/4/2007 17:20'![39;49;00m$
[32masFunction[39;49;00m$
	^ [36mself[39;49;00m [32masFunction:[39;49;00m [33m#([39;49;00m[33m)[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*scriptaculous'[39;49;00m[34m stamp: 'lr 1/4/2007 17:21'![39;49;00m$
[32masFunction:[39;49;00m [31maCollection[39;49;00m$
	^ [04m[32mSUFunction[39;49;00m [36mnew[39;49;00m [32madd:[39;49;00m [36mself[39;49;00m; [32marguments:[39;49;00m [31maCollection[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*scriptaculous'[39;49;00m[34m stamp: 'lr 4/11/2006 19:49'![39;49;00m$
[32masJavascript[39;49;00m$
	^ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [ :[31mstream[39;49;00m | [36mself[39;49;00m [32mjavascriptOn:[39;49;00m [31mstream[39;49;00m ][34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*scriptaculous-printing'[39;49;00m[34m stamp: 'lr 4/20/2006 21:10'![39;49;00m$
[32mjavascriptOn:[39;49;00m [31maStream[39;49;00m$
	[36mself[39;49;00m [32mprintOn:[39;49;00m [31maStream[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'lr 6/5/2007 21:35'![39;49;00m$
[32mdeprecatedApi[39;49;00m$
	[36mself[39;49;00m [32mdeprecatedApi:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mdisplayString[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'lr 6/5/2007 21:35'![39;49;00m$
[32mdeprecatedApi:[39;49;00m [31maString[39;49;00m$
	[04m[32mWADeprecatedApi[39;49;00m [32mraiseSignal:[39;49;00m [31maString[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'lr 5/9/2007 08:47'![39;49;00m$
[32minspectorFields[39;49;00m$
	|[31m members [39;49;00m|$
	[31mmembers[39;49;00m := [04m[32mArray[39;49;00m [36mnew[39;49;00m [32mwriteStream[39;49;00m.$
	[36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mwithIndexDo:[39;49;00m [ :[31meach[39;49;00m :[31mindex[39;49;00m |$
		[31mmembers[39;49;00m [32mnextPut:[39;49;00m [31meach[39;49;00m [32m->[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m) ].$
	[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m [36mifTrue:[39;49;00m [$
		[34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32msize[39;49;00m [32mdo:[39;49;00m [ :[31mindex[39;49;00m |$
			[31mmembers[39;49;00m [32mnextPut:[39;49;00m [31mindex[39;49;00m [32m->[39;49;00m ([36mself[39;49;00m [32mat:[39;49;00m [31mindex[39;49;00m) ] ].$
	^ [31mmembers[39;49;00m [32mcontents[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'avi 3/14/2005 15:19'![39;49;00m$
[32mlabelForSelector:[39;49;00m [31maSymbol[39;49;00m$
	^ [31maSymbol[39;49;00m [32masCapitalizedPhrase[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'pmm 4/7/2007 17:14'![39;49;00m$
[32mrenderOn:[39;49;00m [31maRenderer[39;49;00m$
	[37m"Override this method to customize how objects (not components) are rendered when passed as an argument to #render:. The default is the return value of #displayString.[39;49;00m$
[37m	Just remember that you can not use #callback:, #on:of:, or #call:"[39;49;00m$
$
	[31maRenderer[39;49;00m [32mtext:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'lr 3/19/2007 23:13'![39;49;00m$
[32mrestoreFromSnapshot:[39;49;00m [31manObject[39;49;00m$
	[36mself[39;49;00m [32mcopyFrom:[39;49;00m [31manObject[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'avi 9/1/2004 21:20'![39;49;00m$
[32msnapshotCopy[39;49;00m$
	^ [36mself[39;49;00m [32mshallowCopy[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2'[39;49;00m[34m stamp: 'lr 10/28/2007 14:42'![39;49;00m$
[32mvalidationError:[39;49;00m [31mmessage[39;49;00m$
	^[04m[32mWAValidationNotification[39;49;00m [32mraiseSignal:[39;49;00m [31mmessage[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2-encoding'[39;49;00m[34m stamp: 'lr 3/26/2007 20:16'![39;49;00m$
[32mencodeOn:[39;49;00m [31maDocument[39;49;00m$
	[31maDocument[39;49;00m [32mprint:[39;49;00m [36mself[39;49;00m [32mdisplayString[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2-squeak'[39;49;00m[34m stamp: 'pmm 5/22/2007 22:10'![39;49;00m$
[32mbeMutable[39;49;00m$
	[37m"for VW compatibility, a hack that allows to cache a value in a literal array"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*seaside2-squeak'[39;49;00m[34m stamp: 'lr 7/12/2005 17:01'![39;49;00m$
[32mdisplayString[39;49;00m$
	^ [36mself[39;49;00m [32masString[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*services-base'[39;49;00m[34m stamp: 'rr 3/21/2006 11:54'![39;49;00m$
[32mrequestor[39;49;00m$
	[37m"returns the focused window's requestor"[39;49;00m$
$
	[37m"SystemWindow focusedWindow ifNotNilDo: [:w | ^ w requestor]."[39;49;00m$
$
	[37m"triggers an infinite loop"[39;49;00m$
$
	^ [04m[32mRequestor[39;49;00m [32mdefault[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*system-support'[39;49;00m[34m stamp: 'dvf 8/23/2003 12:27'![39;49;00m$
[32msystemNavigation[39;49;00m$
$
	^ [04m[32mSystemNavigation[39;49;00m [32mdefault[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*tools-browser'[39;49;00m[34m stamp: 'mu 3/6/2004 15:13'![39;49;00m$
[32mbrowse[39;49;00m$
	[36mself[39;49;00m [32msystemNavigation[39;49;00m [32mbrowseClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*tools-browser'[39;49;00m[34m stamp: 'mu 3/11/2004 16:00'![39;49;00m$
[32mbrowseHierarchy[39;49;00m$
	[36mself[39;49;00m [32msystemNavigation[39;49;00m [32mbrowseHierarchy:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*universes'[39;49;00m[34m stamp: 'ls 11/26/2006 12:33'![39;49;00m$
[32misUPackage[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'*universes'[39;49;00m[34m stamp: 'ls 11/26/2006 12:33'![39;49;00m$
[32misUPackageCategory[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'sw 4/30/1998 12:18'![39;49;00m$
[32maddInstanceVarNamed:[39;49;00m [31maName[39;49;00m [32mwithValue:[39;49;00m [31maValue[39;49;00m$
	[37m"Add an instance variable named aName and give it value aValue"[39;49;00m$
	[36mself[39;49;00m [32mclass[39;49;00m [32maddInstVarName:[39;49;00m [31maName[39;49;00m [32masString[39;49;00m.$
	[36mself[39;49;00m [32minstVarAt:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mput:[39;49;00m [31maValue[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'yo 6/29/2004 11:39'![39;49;00m$
[32mat:[39;49;00m [31mindex[39;49;00m $
	[37m"Primitive. Assumes receiver is indexable. Answer the value of an [39;49;00m$
[37m	indexable element in the receiver. Fail if the argument index is not an [39;49;00m$
[37m	Integer or is out of bounds. Essential. See Object documentation [39;49;00m$
[37m	whatIsAPrimitive."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 60>$
	[31mindex[39;49;00m [32misInteger[39;49;00m [36mifTrue:[39;49;00m$
		[[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m$
			[36mifTrue:[39;49;00m [[36mself[39;49;00m [32merrorSubscriptBounds:[39;49;00m [31mindex[39;49;00m]$
			[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNotIndexable[39;49;00m]].$
	[31mindex[39;49;00m [32misNumber[39;49;00m$
		[36mifTrue:[39;49;00m [^[36mself[39;49;00m [32mat:[39;49;00m [31mindex[39;49;00m [32masInteger[39;49;00m]$
		[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNonIntegerIndex[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
[32mat:[39;49;00m [31mindex[39;49;00m [32mmodify:[39;49;00m [31maBlock[39;49;00m$
	[37m"Replace the element of the collection with itself transformed by the block"[39;49;00m$
	^ [36mself[39;49;00m [32mat:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([31maBlock[39;49;00m [32mvalue:[39;49;00m ([36mself[39;49;00m [32mat:[39;49;00m [31mindex[39;49;00m))[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'yo 6/29/2004 13:08'![39;49;00m$
[32mat:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m [31mvalue[39;49;00m $
	[37m"Primitive. Assumes receiver is indexable. Store the argument value in [39;49;00m$
[37m	the indexable element of the receiver indicated by index. Fail if the [39;49;00m$
[37m	index is not an Integer or is out of bounds. Or fail if the value is not of [39;49;00m$
[37m	the right type for this kind of collection. Answer the value that was [39;49;00m$
[37m	stored. Essential. See Object documentation whatIsAPrimitive."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 61>$
	[31mindex[39;49;00m [32misInteger[39;49;00m [36mifTrue:[39;49;00m$
		[[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m$
			[36mifTrue:[39;49;00m [([31mindex[39;49;00m [32m>=[39;49;00m [34m1[39;49;00m [32mand:[39;49;00m [[31mindex[39;49;00m [32m<=[39;49;00m [36mself[39;49;00m [32msize[39;49;00m])$
					[36mifTrue:[39;49;00m [[36mself[39;49;00m [32merrorImproperStore[39;49;00m]$
					[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorSubscriptBounds:[39;49;00m [31mindex[39;49;00m]]$
			[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNotIndexable[39;49;00m]].$
	[31mindex[39;49;00m [32misNumber[39;49;00m$
		[36mifTrue:[39;49;00m [^[36mself[39;49;00m [32mat:[39;49;00m [31mindex[39;49;00m [32masInteger[39;49;00m [32mput:[39;49;00m [31mvalue[39;49;00m]$
		[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNonIntegerIndex[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'yo 9/20/2004 10:22'![39;49;00m$
[32mbasicAddInstanceVarNamed:[39;49;00m [31maName[39;49;00m [32mwithValue:[39;49;00m [31maValue[39;49;00m$
	[37m"Add an instance variable named aName and give it value aValue"[39;49;00m$
	[36mself[39;49;00m [32mclass[39;49;00m [32maddInstVarName:[39;49;00m [31maName[39;49;00m [32masString[39;49;00m.$
	[36mself[39;49;00m [32minstVarAt:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mput:[39;49;00m [31maValue[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
[32mbasicAt:[39;49;00m [31mindex[39;49;00m $
	[37m"Primitive. Assumes receiver is indexable. Answer the value of an [39;49;00m$
[37m	indexable element in the receiver. Fail if the argument index is not an [39;49;00m$
[37m	Integer or is out of bounds. Essential. Do not override in a subclass. See [39;49;00m$
[37m	Object documentation whatIsAPrimitive."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 60>$
	[31mindex[39;49;00m [32misInteger[39;49;00m [36mifTrue:[39;49;00m [[36mself[39;49;00m [32merrorSubscriptBounds:[39;49;00m [31mindex[39;49;00m].$
	[31mindex[39;49;00m [32misNumber[39;49;00m$
		[36mifTrue:[39;49;00m [^[36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32masInteger[39;49;00m]$
		[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNonIntegerIndex[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
[32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m [31mvalue[39;49;00m $
	[37m"Primitive. Assumes receiver is indexable. Store the second argument [39;49;00m$
[37m	value in the indexable element of the receiver indicated by index. Fail [39;49;00m$
[37m	if the index is not an Integer or is out of bounds. Or fail if the value is [39;49;00m$
[37m	not of the right type for this kind of collection. Answer the value that [39;49;00m$
[37m	was stored. Essential. Do not override in a subclass. See Object [39;49;00m$
[37m	documentation whatIsAPrimitive."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 61>$
	[31mindex[39;49;00m [32misInteger[39;49;00m$
		[36mifTrue:[39;49;00m [([31mindex[39;49;00m [32m>=[39;49;00m [34m1[39;49;00m [32mand:[39;49;00m [[31mindex[39;49;00m [32m<=[39;49;00m [36mself[39;49;00m [32msize[39;49;00m])$
					[36mifTrue:[39;49;00m [[36mself[39;49;00m [32merrorImproperStore[39;49;00m]$
					[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorSubscriptBounds:[39;49;00m [31mindex[39;49;00m]].$
	[31mindex[39;49;00m [32misNumber[39;49;00m$
		[36mifTrue:[39;49;00m [^[36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32masInteger[39;49;00m [32mput:[39;49;00m [31mvalue[39;49;00m]$
		[36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNonIntegerIndex[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
[32mbasicSize[39;49;00m$
	[37m"Primitive. Answer the number of indexable variables in the receiver. [39;49;00m$
[37m	This value is the same as the largest legal subscript. Essential. Do not [39;49;00m$
[37m	override in any subclass. See Object documentation whatIsAPrimitive."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 62>$
	[37m"The number of indexable fields of fixed-length objects is 0"[39;49;00m$
	^[34m0[39;49;00m	[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
[32mbindWithTemp:[39;49;00m [31maBlock[39;49;00m$
	^ [31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m [32mvalue:[39;49;00m [36mnil[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'md 10/7/2004 15:43'![39;49;00m$
[32mifNil:[39;49;00m [31mnilBlock[39;49;00m [32mifNotNilDo:[39;49;00m [31maBlock[39;49;00m $
	[37m"Evaluate aBlock with the receiver as its argument."[39;49;00m$
$
	^ [31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'di 11/8/2000 21:04'![39;49;00m$
[32mifNotNilDo:[39;49;00m [31maBlock[39;49;00m$
	[37m"Evaluate the given block with the receiver as its argument."[39;49;00m$
$
	^ [31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'md 10/7/2004 15:43'![39;49;00m$
[32mifNotNilDo:[39;49;00m [31maBlock[39;49;00m [32mifNil:[39;49;00m [31mnilBlock[39;49;00m$
	[37m"Evaluate aBlock with the receiver as its argument."[39;49;00m$
$
	^ [31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'ajh 1/21/2003 12:59'![39;49;00m$
[32min:[39;49;00m [31maBlock[39;49;00m$
	[37m"Evaluate the given block with the receiver as its argument."[39;49;00m$
$
	^ [31maBlock[39;49;00m [32mvalue:[39;49;00m [36mself[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'sw 10/17/2000 11:15'![39;49;00m$
[32mpresenter[39;49;00m$
	[37m"Answer the presenter object associated with the receiver.  For morphs, there is in effect a clear containment hierarchy of presenters (accessed via their association with PasteUpMorphs); for arbitrary objects the hook is simply via the current world, at least at present."[39;49;00m$
$
	^ [36mself[39;49;00m [32mcurrentWorld[39;49;00m [32mpresenter[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m![39;49;00m$
[32mreadFromString:[39;49;00m [31maString[39;49;00m$
	[37m"Create an object based on the contents of aString."[39;49;00m$
$
	^[36mself[39;49;00m [32mreadFrom:[39;49;00m ([04m[32mReadStream[39;49;00m [32mon:[39;49;00m [31maString[39;49;00m)[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'di 3/29/1999 13:10'![39;49;00m$
[32msize[39;49;00m$
	[37m"Primitive. Answer the number of indexable variables in the receiver. [39;49;00m$
[37m	This value is the same as the largest legal subscript. Essential. See Object [39;49;00m$
[37m	documentation whatIsAPrimitive."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 62>$
	[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m [36mifFalse:[39;49;00m [[36mself[39;49;00m [32merrorNotIndexable[39;49;00m].$
	^ [34m0[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'accessing'[39;49;00m[34m stamp: 'md 5/16/2006 12:34'![39;49;00m$
[32myourself[39;49;00m$
	[37m"Answer self."[39;49;00m$
	^[36mself[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'associating'[39;49;00m[34m stamp: 'md 7/22/2005 16:03'![39;49;00m$
[32m->[39;49;00m [31manObject[39;49;00m$
	[37m"Answer an Association between self and anObject"[39;49;00m$
$
	^[04m[32mAssociation[39;49;00m [32mbasicNew[39;49;00m [32mkey:[39;49;00m [36mself[39;49;00m [32mvalue:[39;49;00m [31manObject[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'binding'[39;49;00m[34m![39;49;00m$
[32mbindingOf:[39;49;00m [31maString[39;49;00m$
	^[36mnil[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'breakpoint'[39;49;00m[34m stamp: 'bkv 7/1/2003 12:33'![39;49;00m$
[32mbreak[39;49;00m$
	[37m"This is a simple message to use for inserting breakpoints during debugging.[39;49;00m$
[37m	The debugger is opened by sending a signal. This gives a chance to restore[39;49;00m$
[37m	invariants related to multiple processes."[39;49;00m$
$
	[04m[32mBreakPoint[39;49;00m [32msignal[39;49;00m.$
$
	[37m"nil break."[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'casing'[39;49;00m[34m![39;49;00m$
[32mcaseOf:[39;49;00m [31maBlockAssociationCollection[39;49;00m$
	[37m"The elements of aBlockAssociationCollection are associations between blocks.[39;49;00m$
[37m	 Answer the evaluated value of the first association in aBlockAssociationCollection[39;49;00m$
[37m	 whose evaluated key equals the receiver.  If no match is found, report an error."[39;49;00m$
$
	^ [36mself[39;49;00m [32mcaseOf:[39;49;00m [31maBlockAssociationCollection[39;49;00m [32motherwise:[39;49;00m [[36mself[39;49;00m [32mcaseError[39;49;00m]$
$
[37m"| z | z _ {[#a]->[1+1]. ['b' asSymbol]->[2+2]. [#c]->[3+3]}. #b caseOf: z"[39;49;00m$
[37m"| z | z _ {[#a]->[1+1]. ['d' asSymbol]->[2+2]. [#c]->[3+3]}. #b caseOf: z"[39;49;00m$
[37m"The following are compiled in-line:"[39;49;00m$
[37m"#b caseOf: {[#a]->[1+1]. ['b' asSymbol]->[2+2]. [#c]->[3+3]}"[39;49;00m$
[37m"#b caseOf: {[#a]->[1+1]. ['d' asSymbol]->[2+2]. [#c]->[3+3]}"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'casing'[39;49;00m[34m![39;49;00m$
[32mcaseOf:[39;49;00m [31maBlockAssociationCollection[39;49;00m [32motherwise:[39;49;00m [31maBlock[39;49;00m$
	[37m"The elements of aBlockAssociationCollection are associations between blocks.[39;49;00m$
[37m	 Answer the evaluated value of the first association in aBlockAssociationCollection[39;49;00m$
[37m	 whose evaluated key equals the receiver.  If no match is found, answer the result[39;49;00m$
[37m	 of evaluating aBlock."[39;49;00m$
$
	[31maBlockAssociationCollection[39;49;00m [32massociationsDo:[39;49;00m$
		[:[31massoc[39;49;00m | ([31massoc[39;49;00m [32mkey[39;49;00m [32mvalue[39;49;00m [32m=[39;49;00m [36mself[39;49;00m) [36mifTrue:[39;49;00m [^[31massoc[39;49;00m [32mvalue[39;49;00m [32mvalue[39;49;00m]].$
	^ [31maBlock[39;49;00m [32mvalue[39;49;00m$
$
[37m"| z | z _ {[#a]->[1+1]. ['b' asSymbol]->[2+2]. [#c]->[3+3]}. #b caseOf: z otherwise: [0]"[39;49;00m$
[37m"| z | z _ {[#a]->[1+1]. ['d' asSymbol]->[2+2]. [#c]->[3+3]}. #b caseOf: z otherwise: [0]"[39;49;00m$
[37m"The following are compiled in-line:"[39;49;00m$
[37m"#b caseOf: {[#a]->[1+1]. ['b' asSymbol]->[2+2]. [#c]->[3+3]} otherwise: [0]"[39;49;00m$
[37m"#b caseOf: {[#a]->[1+1]. ['d' asSymbol]->[2+2]. [#c]->[3+3]} otherwise: [0]"[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m![39;49;00m$
[32mclass[39;49;00m$
	[37m"Primitive. Answer the object which is the receiver's class. Essential. See [39;49;00m$
[37m	Object documentation whatIsAPrimitive."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 111>$
	[36mself[39;49;00m [32mprimitiveFailed[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m stamp: 'sw 9/27/2001 15:51'![39;49;00m$
[32minheritsFromAnyIn:[39;49;00m [31maList[39;49;00m$
	[37m"Answer whether the receiver inherits from any class represented by any element in the list.  The elements of the list can be classes, class name symbols, or strings representing possible class names.  This allows speculative membership tests to be made even when some of the classes may not be known to the current image, and even when their names are not interned symbols."[39;49;00m$
$
	|[31m aClass [39;49;00m|$
	[31maList[39;49;00m [32mdo:[39;49;00m$
		[:[31melem[39;49;00m | [04m[32mSymbol[39;49;00m [32mhasInterned:[39;49;00m [31melem[39;49;00m [32masString[39;49;00m [36mifTrue:[39;49;00m $
			[:[31melemSymbol[39;49;00m | ((([31maClass[39;49;00m _ [04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [31melemSymbol[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m]) [32misKindOf:[39;49;00m [04m[32mClass[39;49;00m)$
						[32mand:[39;49;00m [[36mself[39;49;00m [32misKindOf:[39;49;00m [31maClass[39;49;00m])$
				[36mifTrue:[39;49;00m$
					[^ [36mtrue[39;49;00m]]].$
	^ [36mfalse[39;49;00m$
$
$
[37m"[39;49;00m$
[37m{3.  true. 'olive'} do:[39;49;00m$
[37m	[:token |[39;49;00m$
[37m		 {{#Number. #Boolean}. {Number.  Boolean }.  {'Number'. 'Boolean'}} do:[39;49;00m$
[37m			[:list |[39;49;00m$
[37m				Transcript cr; show: token asString, ' list element provided as a ', list first class name, ' - ', (token inheritsFromAnyIn: list) asString]][39;49;00m$
[37m"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m![39;49;00m$
[32misKindOf:[39;49;00m [31maClass[39;49;00m $
	[37m"Answer whether the class, aClass, is a superclass or class of the receiver."[39;49;00m$
$
	[36mself[39;49;00m [32mclass[39;49;00m [32m==[39;49;00m [31maClass[39;49;00m$
		[36mifTrue:[39;49;00m [^[36mtrue[39;49;00m]$
		[36mifFalse:[39;49;00m [^[36mself[39;49;00m [32mclass[39;49;00m [32minheritsFrom:[39;49;00m [31maClass[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m stamp: 'sw 2/16/98 02:08'![39;49;00m$
[32misKindOf:[39;49;00m [31maClass[39;49;00m [32morOf:[39;49;00m [31manotherClass[39;49;00m$
	[37m"Answer whether either of the classes, aClass or anotherClass,, is a superclass or class of the receiver.  A convenience; could be somewhat optimized"[39;49;00m$
	^ ([36mself[39;49;00m [32misKindOf:[39;49;00m [31maClass[39;49;00m) [32mor:[39;49;00m [[36mself[39;49;00m [32misKindOf:[39;49;00m [31manotherClass[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m![39;49;00m$
[32misMemberOf:[39;49;00m [31maClass[39;49;00m $
	[37m"Answer whether the receiver is an instance of the class, aClass."[39;49;00m$
$
	^[36mself[39;49;00m [32mclass[39;49;00m [32m==[39;49;00m [31maClass[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m![39;49;00m$
[32mrespondsTo:[39;49;00m [31maSymbol[39;49;00m $
	[37m"Answer whether the method dictionary of the receiver's class contains [39;49;00m$
[37m	aSymbol as a message selector."[39;49;00m$
$
	^[36mself[39;49;00m [32mclass[39;49;00m [32mcanUnderstand:[39;49;00m [31maSymbol[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'class membership'[39;49;00m[34m stamp: 'tk 10/21/1998 12:38'![39;49;00m$
[32mxxxClass[39;49;00m$
	[37m"For subclasses of nil, such as ObjectOut"[39;49;00m$
	^ [36mself[39;49;00m [32mclass[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m stamp: 'tk 4/16/1999 18:26'![39;49;00m$
[32mcloseTo:[39;49;00m [31manObject[39;49;00m$
	[37m"Answer whether the receiver and the argument represent the same[39;49;00m$
[37m	object. If = is redefined in any subclass, consider also redefining the[39;49;00m$
[37m	message hash."[39;49;00m$
$
	|[31m ans [39;49;00m|$
	[[31mans[39;49;00m _ [36mself[39;49;00m [32m=[39;49;00m [31manObject[39;49;00m] [32mifError:[39;49;00m [:[31maString[39;49;00m :[31maReceiver[39;49;00m | ^ [36mfalse[39;49;00m].$
	^ [31mans[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m![39;49;00m$
[32mhash[39;49;00m$
	[37m"Answer a SmallInteger whose value is related to the receiver's identity.[39;49;00m$
[37m	May be overridden, and should be overridden in any classes that define = "[39;49;00m$
$
	^ [36mself[39;49;00m [32midentityHash[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m stamp: 'pm 9/23/97 09:36'![39;49;00m$
[32mhashMappedBy:[39;49;00m [31mmap[39;49;00m$
	[37m"Answer what my hash would be if oops changed according to map."[39;49;00m$
$
	^[31mmap[39;49;00m [32mnewHashFor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m stamp: 'di 9/27/97 20:23'![39;49;00m$
[32midentityHashMappedBy:[39;49;00m [31mmap[39;49;00m$
	[37m"Answer what my hash would be if oops changed according to map."[39;49;00m$
$
	^[31mmap[39;49;00m [32mnewHashFor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m stamp: 'sw 8/20/1998 12:34'![39;49;00m$
[32midentityHashPrintString[39;49;00m$
	[37m"'fred' identityHashPrintString"[39;49;00m$
$
	^ [33m'('[39;49;00m[32m,[39;49;00m [36mself[39;49;00m [32midentityHash[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m')'[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m stamp: 'ajh 2/2/2002 15:02'![39;49;00m$
[32mliteralEqual:[39;49;00m [31mother[39;49;00m$
$
	^ [36mself[39;49;00m [32mclass[39;49;00m [32m==[39;49;00m [31mother[39;49;00m [32mclass[39;49;00m [32mand:[39;49;00m [[36mself[39;49;00m [32m=[39;49;00m [31mother[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m![39;49;00m$
[32m=[39;49;00m [31manObject[39;49;00m $
	[37m"Answer whether the receiver and the argument represent the same [39;49;00m$
[37m	object. If = is redefined in any subclass, consider also redefining the [39;49;00m$
[37m	message hash."[39;49;00m$
$
	^[36mself[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'comparing'[39;49;00m[34m![39;49;00m$
[32m~=[39;49;00m [31manObject[39;49;00m $
	[37m"Answer whether the receiver and the argument do not represent the [39;49;00m$
[37m	same object."[39;49;00m$
$
	^[36mself[39;49;00m [32m=[39;49;00m [31manObject[39;49;00m [32m==[39;49;00m [36mfalse[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'di 11/9/1998 12:15'![39;49;00m$
[32madaptToFloat:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m$
	[37m"If no method has been provided for adapting an object to a Float,[39;49;00m$
[37m	then it may be adequate to simply adapt it to a number."[39;49;00m$
	^ [36mself[39;49;00m [32madaptToNumber:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'di 11/9/1998 12:14'![39;49;00m$
[32madaptToFraction:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m$
	[37m"If no method has been provided for adapting an object to a Fraction,[39;49;00m$
[37m	then it may be adequate to simply adapt it to a number."[39;49;00m$
	^ [36mself[39;49;00m [32madaptToNumber:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'di 11/9/1998 12:15'![39;49;00m$
[32madaptToInteger:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m$
	[37m"If no method has been provided for adapting an object to a Integer,[39;49;00m$
[37m	then it may be adequate to simply adapt it to a number."[39;49;00m$
	^ [36mself[39;49;00m [32madaptToNumber:[39;49;00m [31mrcvr[39;49;00m [32mandSend:[39;49;00m [31mselector[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'rw 4/27/2002 07:48'![39;49;00m$
[32masActionSequence[39;49;00m$
$
	^[04m[32mWeakActionSequence[39;49;00m [32mwith:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'rw 7/20/2003 16:03'![39;49;00m$
[32masActionSequenceTrappingErrors[39;49;00m$
$
	^[04m[32mWeakActionSequenceTrappingErrors[39;49;00m [32mwith:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'svp 5/16/2000 18:14'![39;49;00m$
[32masDraggableMorph[39;49;00m$
	^([04m[32mStringMorph[39;49;00m [32mcontents:[39;49;00m [36mself[39;49;00m [32mprintString[39;49;00m)$
		[32mcolor:[39;49;00m [04m[32mColor[39;49;00m [32mwhite[39;49;00m;$
		[32myourself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'sma 5/12/2000 17:39'![39;49;00m$
[32masOrderedCollection[39;49;00m$
	[37m"Answer an OrderedCollection with the receiver as its only element."[39;49;00m$
$
	^ [04m[32mOrderedCollection[39;49;00m [32mwith:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m![39;49;00m$
[32masString[39;49;00m$
	[37m"Answer a string that represents the receiver."[39;49;00m$
$
	^ [36mself[39;49;00m [32mprintString[39;49;00m [34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'ajh 3/11/2003 10:27'![39;49;00m$
[32masStringOrText[39;49;00m$
	[37m"Answer a string that represents the receiver."[39;49;00m$
$
	^ [36mself[39;49;00m [32mprintString[39;49;00m [34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m![39;49;00m$
[32mas:[39;49;00m [31maSimilarClass[39;49;00m$
	[37m"Create an object of class aSimilarClass that has similar contents to the receiver."[39;49;00m$
$
	^ [31maSimilarClass[39;49;00m [32mnewFrom:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'RAA 8/2/1999 12:41'![39;49;00m$
[32mcomplexContents[39;49;00m$
$
	^[36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'ajh 7/6/2003 20:37'![39;49;00m$
[32mmustBeBoolean[39;49;00m$
	[37m"Catches attempts to test truth of non-Booleans.  This message is sent from the VM.  The sending context is rewound to just before the jump causing this exception."[39;49;00m$
$
	^ [36mself[39;49;00m [32mmustBeBooleanIn:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'ajh 7/6/2003 20:40'![39;49;00m$
[32mmustBeBooleanIn:[39;49;00m [31mcontext[39;49;00m$
	[37m"context is the where the non-boolean error occurred. Rewind context to before jump then raise error."[39;49;00m$
$
	|[31m proceedValue [39;49;00m|$
	[31mcontext[39;49;00m [32mskipBackBeforeJump[39;49;00m.$
	[31mproceedValue[39;49;00m _ [04m[32mNonBooleanReceiver[39;49;00m [36mnew[39;49;00m$
		[32mobject:[39;49;00m [36mself[39;49;00m;$
		[32msignal:[39;49;00m [33m'proceed for truth.'[39;49;00m.$
	^ [31mproceedValue[39;49;00m [32m~~[39;49;00m [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'sw 3/26/2001 12:12'![39;49;00m$
[32mprintDirectlyToDisplay[39;49;00m$
	[37m"For debugging: write the receiver's printString directly to the display at (0, 100); senders of this are detected by the check-for-slips mechanism."[39;49;00m$
$
	[36mself[39;49;00m [32masString[39;49;00m [32mdisplayAt:[39;49;00m [34m0[39;49;00m[32m@[39;49;00m[34m100[39;49;00m$
$
[37m"StringMorph someInstance printDirectlyToDisplay"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'converting'[39;49;00m[34m stamp: 'RAA 3/31/1999 12:13'![39;49;00m$
[32mwithoutListWrapper[39;49;00m$
$
	^[36mself[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m![39;49;00m$
[32mclone[39;49;00m$
$
	<[34mprimitive:[39;49;00m 148>$
	[36mself[39;49;00m [32mprimitiveFailed[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'ajh 8/18/2001 21:25'![39;49;00m$
[32mcopy[39;49;00m$
	[37m"Answer another instance just like the receiver. Subclasses typically override postCopy; they typically do not override shallowCopy."[39;49;00m$
$
	^[36mself[39;49;00m [32mshallowCopy[39;49;00m [32mpostCopy[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 8/20/1998 16:01'![39;49;00m$
[32mcopyAddedStateFrom:[39;49;00m [31manotherObject[39;49;00m$
	[37m"Copy over the values of instance variables added by the receiver's class from anotherObject to the receiver.  These will be remapped in mapUniClasses, if needed."[39;49;00m$
$
	[36mself[39;49;00m [32mclass[39;49;00m [32msuperclass[39;49;00m [32minstSize[39;49;00m [32m+[39;49;00m [34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mdo:[39;49;00m$
		[:[31mindex[39;49;00m | [36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([31manotherObject[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m)][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tpr 2/14/2004 21:53'![39;49;00m$
[32mcopyFrom:[39;49;00m [31manotherObject[39;49;00m$
	[37m"Copy to myself all instance variables I have in common with anotherObject.  This is dangerous because it ignores an object's control over its own inst vars.  "[39;49;00m$
$
	|[31m mine his [39;49;00m|$
	<[34mprimitive:[39;49;00m 168>$
	[31mmine[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m.$
	[31mhis[39;49;00m _ [31manotherObject[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m.$
	[34m1[39;49;00m [32mto:[39;49;00m ([31mmine[39;49;00m [32msize[39;49;00m [32mmin:[39;49;00m [31mhis[39;49;00m [32msize[39;49;00m) [32mdo:[39;49;00m [:[31mind[39;49;00m |$
		([31mmine[39;49;00m [32mat:[39;49;00m [31mind[39;49;00m) [32m=[39;49;00m ([31mhis[39;49;00m [32mat:[39;49;00m [31mind[39;49;00m) [36mifTrue:[39;49;00m [$
			[36mself[39;49;00m [32minstVarAt:[39;49;00m [31mind[39;49;00m [32mput:[39;49;00m ([31manotherObject[39;49;00m [32minstVarAt:[39;49;00m [31mind[39;49;00m)]].$
	[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m [32m&[39;49;00m [31manotherObject[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m [36mifTrue:[39;49;00m [$
		[34m1[39;49;00m [32mto:[39;49;00m ([36mself[39;49;00m [32mbasicSize[39;49;00m [32mmin:[39;49;00m [31manotherObject[39;49;00m [32mbasicSize[39;49;00m) [32mdo:[39;49;00m [:[31mind[39;49;00m |$
			[36mself[39;49;00m [32mbasicAt:[39;49;00m [31mind[39;49;00m [32mput:[39;49;00m ([31manotherObject[39;49;00m [32mbasicAt:[39;49;00m [31mind[39;49;00m)]].[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'ajh 5/23/2002 00:38'![39;49;00m$
[32mcopySameFrom:[39;49;00m [31motherObject[39;49;00m$
	[37m"Copy to myself all instance variables named the same in otherObject.[39;49;00m$
[37m	This ignores otherObject's control over its own inst vars."[39;49;00m$
$
	|[31m myInstVars otherInstVars match [39;49;00m|$
	[31mmyInstVars[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m.$
	[31motherInstVars[39;49;00m _ [31motherObject[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m.$
	[31mmyInstVars[39;49;00m [32mdoWithIndex:[39;49;00m [:[31meach[39;49;00m :[31mindex[39;49;00m |$
		([31mmatch[39;49;00m _ [31motherInstVars[39;49;00m [32mindexOf:[39;49;00m [31meach[39;49;00m) [32m>[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m$
			[[36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([31motherObject[39;49;00m [32minstVarAt:[39;49;00m [31mmatch[39;49;00m)]].$
	[34m1[39;49;00m [32mto:[39;49;00m ([36mself[39;49;00m [32mbasicSize[39;49;00m [32mmin:[39;49;00m [31motherObject[39;49;00m [32mbasicSize[39;49;00m) [32mdo:[39;49;00m [:[31mi[39;49;00m |$
		[36mself[39;49;00m [32mbasicAt:[39;49;00m [31mi[39;49;00m [32mput:[39;49;00m ([31motherObject[39;49;00m [32mbasicAt:[39;49;00m [31mi[39;49;00m)].$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 4/20/1999 14:44'![39;49;00m$
[32mcopyTwoLevel[39;49;00m$
	[37m"one more level than a shallowCopy"[39;49;00m$
$
	|[31m newObject class index [39;49;00m|$
	[31mclass[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m.$
	[31mnewObject[39;49;00m _ [36mself[39;49;00m [32mclone[39;49;00m.$
	[31mnewObject[39;49;00m [32m==[39;49;00m [36mself[39;49;00m [36mifTrue:[39;49;00m [^ [36mself[39;49;00m].$
	[31mclass[39;49;00m [32misVariable[39;49;00m$
		[36mifTrue:[39;49;00m $
			[[31mindex[39;49;00m _ [36mself[39;49;00m [32mbasicSize[39;49;00m.$
			[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
				[36mwhileTrue:[39;49;00m $
					[[31mnewObject[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m) [32mshallowCopy[39;49;00m.$
					[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]].$
	[31mindex[39;49;00m _ [31mclass[39;49;00m [32minstSize[39;49;00m.$
	[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
		[36mwhileTrue:[39;49;00m $
			[[31mnewObject[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m) [32mshallowCopy[39;49;00m.$
			[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m].$
	^[31mnewObject[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m![39;49;00m$
[32mdeepCopy[39;49;00m$
	[37m"Answer a copy of the receiver with its own copy of each instance [39;49;00m$
[37m	variable."[39;49;00m$
$
	|[31m newObject class index [39;49;00m|$
	[31mclass[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m.$
	([31mclass[39;49;00m [32m==[39;49;00m [04m[32mObject[39;49;00m) [36mifTrue:[39;49;00m [^[36mself[39;49;00m].$
	[31mclass[39;49;00m [32misVariable[39;49;00m$
		[36mifTrue:[39;49;00m $
			[[31mindex[39;49;00m _ [36mself[39;49;00m [32mbasicSize[39;49;00m.$
			[31mnewObject[39;49;00m _ [31mclass[39;49;00m [32mbasicNew:[39;49;00m [31mindex[39;49;00m.$
			[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
				[36mwhileTrue:[39;49;00m $
					[[31mnewObject[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m) [32mdeepCopy[39;49;00m.$
					[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]$
		[36mifFalse:[39;49;00m [[31mnewObject[39;49;00m _ [31mclass[39;49;00m [32mbasicNew[39;49;00m].$
	[31mindex[39;49;00m _ [31mclass[39;49;00m [32minstSize[39;49;00m.$
	[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
		[36mwhileTrue:[39;49;00m $
			[[31mnewObject[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m) [32mdeepCopy[39;49;00m.$
			[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m].$
	^[31mnewObject[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'hg 11/23/1999 13:43'![39;49;00m$
[32minitialDeepCopierSize[39;49;00m$
	[37m"default value is 4096; other classes may override this, esp. for smaller (=faster) sizes"[39;49;00m$
$
	^[34m4096[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'ajh 1/27/2003 18:45'![39;49;00m$
[32mpostCopy[39;49;00m$
	[37m"self is a shallow copy, subclasses should copy fields as necessary to complete the full copy"[39;49;00m$
$
	^ [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'jm 11/14/97 11:08'![39;49;00m$
[32mshallowCopy[39;49;00m$
	[37m"Answer a copy of the receiver which shares the receiver's instance variables."[39;49;00m$
	|[31m class newObject index [39;49;00m|$
	<[34mprimitive:[39;49;00m 148>$
	[31mclass[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m.$
	[31mclass[39;49;00m [32misVariable[39;49;00m$
		[36mifTrue:[39;49;00m $
			[[31mindex[39;49;00m _ [36mself[39;49;00m [32mbasicSize[39;49;00m.$
			[31mnewObject[39;49;00m _ [31mclass[39;49;00m [32mbasicNew:[39;49;00m [31mindex[39;49;00m.$
			[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
				[36mwhileTrue:[39;49;00m $
					[[31mnewObject[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m).$
					[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]$
		[36mifFalse:[39;49;00m [[31mnewObject[39;49;00m _ [31mclass[39;49;00m [32mbasicNew[39;49;00m].$
	[31mindex[39;49;00m _ [31mclass[39;49;00m [32minstSize[39;49;00m.$
	[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m]$
		[36mwhileTrue:[39;49;00m $
			[[31mnewObject[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m).$
			[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m].$
	^ [31mnewObject[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 3/11/2003 13:58'![39;49;00m$
[32mveryDeepCopy[39;49;00m$
	[37m"Do a complete tree copy using a dictionary.  An object in the tree twice is only copied once.  All references to the object in the copy of the tree will point to the new copy."[39;49;00m$
$
	|[31m copier new [39;49;00m|$
	[31mcopier[39;49;00m _ [04m[32mDeepCopier[39;49;00m [36mnew[39;49;00m [32minitialize:[39;49;00m [36mself[39;49;00m [32minitialDeepCopierSize[39;49;00m.$
	[31mnew[39;49;00m _ [36mself[39;49;00m [32mveryDeepCopyWith:[39;49;00m [31mcopier[39;49;00m.$
	[31mcopier[39;49;00m [32mmapUniClasses[39;49;00m.$
	[31mcopier[39;49;00m [32mreferences[39;49;00m [32massociationsDo:[39;49;00m [:[31massoc[39;49;00m | $
		[31massoc[39;49;00m [32mvalue[39;49;00m [32mveryDeepFixupWith:[39;49;00m [31mcopier[39;49;00m].$
	[31mcopier[39;49;00m [32mfixDependents[39;49;00m.$
	^ [31mnew[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 3/11/2003 13:58'![39;49;00m$
[32mveryDeepCopySibling[39;49;00m$
	[37m"Do a complete tree copy using a dictionary.  Substitute a clone of oldPlayer for the root.  Normally, a Player or non systemDefined object would have a new class.  We do not want one this time.  An object in the tree twice, is only copied once.  All references to the object in the copy of the tree will point to the new copy."[39;49;00m$
$
	|[31m copier new [39;49;00m|$
	[31mcopier[39;49;00m _ [04m[32mDeepCopier[39;49;00m [36mnew[39;49;00m [32minitialize:[39;49;00m [36mself[39;49;00m [32minitialDeepCopierSize[39;49;00m.$
	[31mcopier[39;49;00m [32mnewUniClasses:[39;49;00m [36mfalse[39;49;00m.$
	[31mnew[39;49;00m _ [36mself[39;49;00m [32mveryDeepCopyWith:[39;49;00m [31mcopier[39;49;00m.$
	[31mcopier[39;49;00m [32mmapUniClasses[39;49;00m.$
	[31mcopier[39;49;00m [32mreferences[39;49;00m [32massociationsDo:[39;49;00m [:[31massoc[39;49;00m | $
		[31massoc[39;49;00m [32mvalue[39;49;00m [32mveryDeepFixupWith:[39;49;00m [31mcopier[39;49;00m].$
	[31mcopier[39;49;00m [32mfixDependents[39;49;00m.$
	^ [31mnew[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 5/13/2003 19:39'![39;49;00m$
[32mveryDeepCopyUsing:[39;49;00m [31mcopier[39;49;00m$
	[37m"Do a complete tree copy using a dictionary.  An object in the tree twice is only copied once.  All references to the object in the copy of the tree will point to the new copy.[39;49;00m$
[37m	Same as veryDeepCopy except copier (with dictionary) is supplied.[39;49;00m$
[37m	** do not delete this method, even if it has no callers **"[39;49;00m$
$
	|[31m new refs newDep newModel [39;49;00m|$
	[31mnew[39;49;00m _ [36mself[39;49;00m [32mveryDeepCopyWith:[39;49;00m [31mcopier[39;49;00m.$
	[31mcopier[39;49;00m [32mmapUniClasses[39;49;00m.$
	[31mcopier[39;49;00m [32mreferences[39;49;00m [32massociationsDo:[39;49;00m [:[31massoc[39;49;00m | $
		[31massoc[39;49;00m [32mvalue[39;49;00m [32mveryDeepFixupWith:[39;49;00m [31mcopier[39;49;00m].$
	[37m"Fix dependents"[39;49;00m$
	[31mrefs[39;49;00m _ [31mcopier[39;49;00m [32mreferences[39;49;00m.$
	[04m[32mDependentsFields[39;49;00m [32massociationsDo:[39;49;00m [:[31mpair[39;49;00m |$
		[31mpair[39;49;00m [32mvalue[39;49;00m [32mdo:[39;49;00m [:[31mdep[39;49;00m | $
			([31mnewDep[39;49;00m _ [31mrefs[39;49;00m [32mat:[39;49;00m [31mdep[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m]) [32mifNotNil:[39;49;00m [$
				[31mnewModel[39;49;00m _ [31mrefs[39;49;00m [32mat:[39;49;00m [31mpair[39;49;00m [32mkey[39;49;00m [32mifAbsent:[39;49;00m [[31mpair[39;49;00m [32mkey[39;49;00m].$
				[31mnewModel[39;49;00m [32maddDependent:[39;49;00m [31mnewDep[39;49;00m]]].$
	^ [31mnew[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 3/11/2003 14:12'![39;49;00m$
[32mveryDeepCopyWith:[39;49;00m [31mdeepCopier[39;49;00m$
	[37m"Copy me and the entire tree of objects I point to.  An object in the tree twice is copied once, and both references point to him.  deepCopier holds a dictionary of objects we have seen.  Some classes refuse to be copied.  Some classes are picky about which fields get deep copied."[39;49;00m$
	|[31m class index sub subAss new uc sup has mine [39;49;00m|$
	[31mdeepCopier[39;49;00m [32mreferences[39;49;00m [32mat:[39;49;00m [36mself[39;49;00m [32mifPresent:[39;49;00m [:[31mnewer[39;49;00m | ^ [31mnewer[39;49;00m]. 	[37m"already did him"[39;49;00m$
	[31mclass[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m.$
	[31mclass[39;49;00m [32misMeta[39;49;00m [36mifTrue:[39;49;00m [^ [36mself[39;49;00m].		[37m"a class"[39;49;00m$
	[31mnew[39;49;00m _ [36mself[39;49;00m [32mclone[39;49;00m.$
	([31mclass[39;49;00m [32misSystemDefined[39;49;00m [32mnot[39;49;00m [32mand:[39;49;00m [[31mdeepCopier[39;49;00m [32mnewUniClasses[39;49;00m [37m"allowed"[39;49;00m]) [36mifTrue:[39;49;00m [$
		[31muc[39;49;00m _ [31mdeepCopier[39;49;00m [32muniClasses[39;49;00m [32mat:[39;49;00m [31mclass[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m].$
		[31muc[39;49;00m [32mifNil:[39;49;00m [$
			[31mdeepCopier[39;49;00m [32muniClasses[39;49;00m [32mat:[39;49;00m [31mclass[39;49;00m [32mput:[39;49;00m ([31muc[39;49;00m _ [36mself[39;49;00m [32mcopyUniClassWith:[39;49;00m [31mdeepCopier[39;49;00m).$
			[31mdeepCopier[39;49;00m [32mreferences[39;49;00m [32mat:[39;49;00m [31mclass[39;49;00m [32mput:[39;49;00m [31muc[39;49;00m].	[37m"remember"[39;49;00m$
		[31mnew[39;49;00m _ [31muc[39;49;00m [36mnew[39;49;00m.$
		[31mnew[39;49;00m [32mcopyFrom:[39;49;00m [36mself[39;49;00m].	[37m"copy inst vars in case any are weak"[39;49;00m$
	[31mdeepCopier[39;49;00m [32mreferences[39;49;00m [32mat:[39;49;00m [36mself[39;49;00m [32mput:[39;49;00m [31mnew[39;49;00m.	[37m"remember"[39;49;00m$
	([31mclass[39;49;00m [32misVariable[39;49;00m [32mand:[39;49;00m [[31mclass[39;49;00m [32misPointers[39;49;00m]) [36mifTrue:[39;49;00m $
		[[31mindex[39;49;00m _ [36mself[39;49;00m [32mbasicSize[39;49;00m.$
		[[31mindex[39;49;00m [32m>[39;49;00m [34m0[39;49;00m] [36mwhileTrue:[39;49;00m $
			[[31msub[39;49;00m _ [36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m.$
			([31msubAss[39;49;00m _ [31mdeepCopier[39;49;00m [32mreferences[39;49;00m [32massociationAt:[39;49;00m [31msub[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m])$
				[32mifNil:[39;49;00m [[31mnew[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m ([31msub[39;49;00m [32mveryDeepCopyWith:[39;49;00m [31mdeepCopier[39;49;00m)]$
				[32mifNotNil:[39;49;00m [[31mnew[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m [31msubAss[39;49;00m [32mvalue[39;49;00m].$
			[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]].$
	[37m"Ask each superclass if it wants to share (weak copy) any inst vars"[39;49;00m$
	[31mnew[39;49;00m [32mveryDeepInner:[39;49;00m [31mdeepCopier[39;49;00m.		[37m"does super a lot"[39;49;00m$
$
	[37m"other superclasses want all inst vars deep copied"[39;49;00m$
	[31msup[39;49;00m _ [31mclass[39;49;00m.  [31mindex[39;49;00m _ [31mclass[39;49;00m [32minstSize[39;49;00m.$
	[[31mhas[39;49;00m _ [31msup[39;49;00m [32mcompiledMethodAt:[39;49;00m [33m#veryDeepInner:[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m].$
	[31mhas[39;49;00m _ [31mhas[39;49;00m [32mifNil:[39;49;00m [[31mclass[39;49;00m [32misSystemDefined[39;49;00m [32mnot[39;49;00m [37m"is a uniClass"[39;49;00m] [32mifNotNil:[39;49;00m [[36mtrue[39;49;00m].$
	[31mmine[39;49;00m _ [31msup[39;49;00m [32minstVarNames[39;49;00m.$
	[31mhas[39;49;00m [36mifTrue:[39;49;00m [[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [31mmine[39;49;00m [32msize[39;49;00m]	[37m"skip inst vars"[39;49;00m$
		[36mifFalse:[39;49;00m [[34m1[39;49;00m [32mto:[39;49;00m [31mmine[39;49;00m [32msize[39;49;00m [32mdo:[39;49;00m [:[31mxx[39;49;00m |$
				[31msub[39;49;00m _ [36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m.$
				([31msubAss[39;49;00m _ [31mdeepCopier[39;49;00m [32mreferences[39;49;00m [32massociationAt:[39;49;00m [31msub[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m])$
						[37m"use association, not value, so nil is an exceptional value"[39;49;00m$
					[32mifNil:[39;49;00m [[31mnew[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m $
								([31msub[39;49;00m [32mveryDeepCopyWith:[39;49;00m [31mdeepCopier[39;49;00m)]$
					[32mifNotNil:[39;49;00m [[31mnew[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m [32mput:[39;49;00m [31msubAss[39;49;00m [32mvalue[39;49;00m].$
				[31mindex[39;49;00m _ [31mindex[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]].$
	([31msup[39;49;00m _ [31msup[39;49;00m [32msuperclass[39;49;00m) [32m==[39;49;00m [36mnil[39;49;00m] [32mwhileFalse[39;49;00m.$
	[31mnew[39;49;00m [32mrehash[39;49;00m.	[37m"force Sets and Dictionaries to rehash"[39;49;00m$
	^ [31mnew[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 1/6/1999 17:39'![39;49;00m$
[32mveryDeepFixupWith:[39;49;00m [31mdeepCopier[39;49;00m$
	[37m"I have no fields and no superclass.  Catch the super call."[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'copying'[39;49;00m[34m stamp: 'tk 9/4/2001 10:30'![39;49;00m$
[32mveryDeepInner:[39;49;00m [31mdeepCopier[39;49;00m$
	[37m"No special treatment for inst vars of my superclasses.  Override when some need to be weakly copied.  Object>>veryDeepCopyWith: will veryDeepCopy any inst var whose class does not actually define veryDeepInner:"[39;49;00m$
[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'creation'[39;49;00m[34m stamp: 'nk 2/26/2004 13:35'![39;49;00m$
[32masStringMorph[39;49;00m$
	[37m"Open a StringMorph, as best one can, on the receiver"[39;49;00m$
$
	^ [36mself[39;49;00m [32masStringOrText[39;49;00m [32masStringMorph[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'creation'[39;49;00m[34m stamp: 'nk 2/26/2004 13:35'![39;49;00m$
[32masTextMorph[39;49;00m$
	[37m"Open a TextMorph, as best one can, on the receiver"[39;49;00m$
$
	^ [04m[32mTextMorph[39;49;00m [36mnew[39;49;00m [32mcontentsAsIs:[39;49;00m [36mself[39;49;00m [32masStringOrText[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'creation'[39;49;00m[34m stamp: 'sw 1/29/2002 21:45'![39;49;00m$
[32mopenAsMorph[39;49;00m$
	[37m"Open a morph, as best one can, on the receiver"[39;49;00m$
$
	^ [36mself[39;49;00m [32masMorph[39;49;00m [32mopenInHand[39;49;00m$
$
[37m"[39;49;00m$
[37m234 openAsMorph[39;49;00m$
[37m(ScriptingSystem formAtKey: #TinyMenu) openAsMorph[39;49;00m$
[37m'fred' openAsMorph[39;49;00m$
[37m"[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging'[39;49;00m[34m stamp: 'md 11/24/2004 11:45'![39;49;00m$
[32mhaltIf:[39;49;00m [31mcondition[39;49;00m$
	[37m"This is the typical message to use for inserting breakpoints during [39;49;00m$
[37m	debugging.  Param can be a block or expression, halt if true.[39;49;00m$
[37m	If the Block has one arg, the receiver is bound to that.[39;49;00m$
[37m 	If the condition is a selector, we look up in the callchain. Halt if[39;49;00m$
[37m      any method's selector equals selector."[39;49;00m$
	|[31m cntxt [39;49;00m|$
$
	[31mcondition[39;49;00m [32misSymbol[39;49;00m [36mifTrue:[39;49;00m[$
		[37m"only halt if a method with selector symbol is in callchain"[39;49;00m$
		[31mcntxt[39;49;00m := [36mthisContext[39;49;00m.$
		[[31mcntxt[39;49;00m [32msender[39;49;00m [32misNil[39;49;00m] [36mwhileFalse:[39;49;00m [$
			[31mcntxt[39;49;00m := [31mcntxt[39;49;00m [32msender[39;49;00m. $
			([31mcntxt[39;49;00m [32mselector[39;49;00m [32m=[39;49;00m [31mcondition[39;49;00m) [36mifTrue:[39;49;00m [[04m[32mHalt[39;49;00m [32msignal[39;49;00m].$
			].$
		^[36mself[39;49;00m.$
	].$
	([31mcondition[39;49;00m [32misBlock[39;49;00m $
			[36mifTrue:[39;49;00m [[31mcondition[39;49;00m [32mvalueWithPossibleArgument:[39;49;00m [36mself[39;49;00m] $
			[36mifFalse:[39;49;00m [[31mcondition[39;49;00m] $
	) [36mifTrue:[39;49;00m [$
		[04m[32mHalt[39;49;00m [32msignal[39;49;00m$
	].[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging'[39;49;00m[34m![39;49;00m$
[31mneedsWork[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:26'![39;49;00m$
[32mcheckHaltCountExpired[39;49;00m$
	|[31m counter [39;49;00m|$
	[31mcounter[39;49;00m _ [04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#HaltCount[39;49;00m [32mifAbsent:[39;49;00m [[34m0[39;49;00m].$
	^[31mcounter[39;49;00m [32m=[39;49;00m [34m0[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:04'![39;49;00m$
[32mclearHaltOnce[39;49;00m$
	[37m"Turn on the halt once flag."[39;49;00m$
	[04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#HaltOnce[39;49;00m [32mput:[39;49;00m [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:30'![39;49;00m$
[32mdecrementAndCheckHaltCount[39;49;00m$
	[36mself[39;49;00m [32mdecrementHaltCount[39;49;00m.$
	^[36mself[39;49;00m [32mcheckHaltCountExpired[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:28'![39;49;00m$
[32mdecrementHaltCount[39;49;00m$
	|[31m counter [39;49;00m|$
	[31mcounter[39;49;00m := [04m[32mSmalltalk[39;49;00m$
				[32mat:[39;49;00m [33m#HaltCount[39;49;00m$
				[32mifAbsent:[39;49;00m [[34m0[39;49;00m].$
	[31mcounter[39;49;00m [32m>[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m [$
		[31mcounter[39;49;00m _ [31mcounter[39;49;00m [32m-[39;49;00m [34m1[39;49;00m.$
		[36mself[39;49;00m [32msetHaltCountTo:[39;49;00m [31mcounter[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:42'![39;49;00m$
[32mdoExpiredHaltCount[39;49;00m$
	[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
	[36mself[39;49;00m [32mremoveHaltCount[39;49;00m.$
	[36mself[39;49;00m [32mhalt[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:44'![39;49;00m$
[32mdoExpiredHaltCount:[39;49;00m [31maString[39;49;00m$
	[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
	[36mself[39;49;00m [32mremoveHaltCount[39;49;00m.$
	[36mself[39;49;00m [32mhalt:[39;49;00m [31maString[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:45'![39;49;00m$
[32mdoExpiredInspectCount[39;49;00m$
	[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
	[36mself[39;49;00m [32mremoveHaltCount[39;49;00m.$
	[36mself[39;49;00m [32minspect[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:43'![39;49;00m$
[32mhaltOnCount:[39;49;00m [31mint[39;49;00m $
	[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
		[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mhasHaltCount[39;49;00m$
				[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdecrementAndCheckHaltCount[39;49;00m$
						[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredHaltCount[39;49;00m]]$
				[36mifFalse:[39;49;00m [[31mint[39;49;00m [32m=[39;49;00m [34m1[39;49;00m$
						[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredHaltCount[39;49;00m]$
						[36mifFalse:[39;49;00m [[36mself[39;49;00m [32msetHaltCountTo:[39;49;00m [31mint[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:05'![39;49;00m$
[32mhaltOnce[39;49;00m$
	[37m"Halt unless we have already done it once."[39;49;00m$
	[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
		[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
			^ [36mself[39;49;00m [32mhalt[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:04'![39;49;00m$
[32mhaltOnceEnabled[39;49;00m$
	^ [04m[32mSmalltalk[39;49;00m$
		[32mat:[39;49;00m [33m#HaltOnce[39;49;00m$
		[32mifAbsent:[39;49;00m [[36mfalse[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:05'![39;49;00m$
[32mhaltOnce:[39;49;00m [31maString[39;49;00m $
	[37m"Halt unless we have already done it once."[39;49;00m$
	[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
		[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
			^ [36mself[39;49;00m [32mhalt:[39;49;00m [31maString[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:45'![39;49;00m$
[32mhalt:[39;49;00m [31maString[39;49;00m [32monCount:[39;49;00m [31mint[39;49;00m $
	[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
		[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mhasHaltCount[39;49;00m$
				[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdecrementAndCheckHaltCount[39;49;00m$
						[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredHaltCount:[39;49;00m [31maString[39;49;00m]]$
				[36mifFalse:[39;49;00m [[31mint[39;49;00m [32m=[39;49;00m [34m1[39;49;00m$
						[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredHaltCount:[39;49;00m [31maString[39;49;00m]$
						[36mifFalse:[39;49;00m [[36mself[39;49;00m [32msetHaltCountTo:[39;49;00m [31mint[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:36'![39;49;00m$
[32mhasHaltCount[39;49;00m$
	^[04m[32mSmalltalk[39;49;00m$
				[32mincludesKey:[39;49;00m [33m#HaltCount[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:46'![39;49;00m$
[32minspectOnCount:[39;49;00m [31mint[39;49;00m $
	[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
		[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mhasHaltCount[39;49;00m$
				[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdecrementAndCheckHaltCount[39;49;00m$
						[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredInspectCount[39;49;00m]]$
				[36mifFalse:[39;49;00m [[31mint[39;49;00m [32m=[39;49;00m [34m1[39;49;00m$
						[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredInspectCount[39;49;00m]$
						[36mifFalse:[39;49;00m [[36mself[39;49;00m [32msetHaltCountTo:[39;49;00m [31mint[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:05'![39;49;00m$
[32minspectOnce[39;49;00m$
	[37m"Inspect unless we have already done it once."[39;49;00m$
	[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
		[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mclearHaltOnce[39;49;00m.$
			^ [36mself[39;49;00m [32minspect[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 13:20'![39;49;00m$
[32minspectUntilCount:[39;49;00m [31mint[39;49;00m $
	[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
		[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mhasHaltCount[39;49;00m$
				[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdecrementAndCheckHaltCount[39;49;00m$
						[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredInspectCount[39;49;00m]$
						[36mifFalse:[39;49;00m [[36mself[39;49;00m [32minspect[39;49;00m]]$
				[36mifFalse:[39;49;00m [[31mint[39;49;00m [32m=[39;49;00m [34m1[39;49;00m$
						[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mdoExpiredInspectCount[39;49;00m]$
						[36mifFalse:[39;49;00m [[36mself[39;49;00m [32msetHaltCountTo:[39;49;00m [31mint[39;49;00m [32m-[39;49;00m [34m1[39;49;00m]]][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:49'![39;49;00m$
[32mremoveHaltCount[39;49;00m$
	([04m[32mSmalltalk[39;49;00m [32mincludesKey:[39;49;00m [33m#HaltCount[39;49;00m) [36mifTrue:[39;49;00m [$
		[04m[32mSmalltalk[39;49;00m [32mremoveKey:[39;49;00m [33m#HaltCount[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 6/2/2004 08:25'![39;49;00m$
[32msetHaltCountTo:[39;49;00m [31mint[39;49;00m$
	[04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#HaltCount[39;49;00m [32mput:[39;49;00m [31mint[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:04'![39;49;00m$
[32msetHaltOnce[39;49;00m$
	[37m"Turn on the halt once flag."[39;49;00m$
	[04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#HaltOnce[39;49;00m [32mput:[39;49;00m [36mtrue[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'debugging-haltOnce'[39;49;00m[34m stamp: 'sbw 5/19/2004 19:04'![39;49;00m$
[32mtoggleHaltOnce[39;49;00m$
	[36mself[39;49;00m [32mhaltOnceEnabled[39;49;00m$
		[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mclearHaltOnce[39;49;00m]$
		[36mifFalse:[39;49;00m [[36mself[39;49;00m [32msetHaltOnce[39;49;00m][34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'ar 2/11/2001 01:55'![39;49;00m$
[32maddDependent:[39;49;00m [31manObject[39;49;00m$
	[37m"Make the given object one of the receiver's dependents."[39;49;00m$
$
	|[31m dependents [39;49;00m|$
	[31mdependents[39;49;00m _ [36mself[39;49;00m [32mdependents[39;49;00m.$
	([31mdependents[39;49;00m [32mincludes:[39;49;00m [31manObject[39;49;00m) [36mifFalse:[39;49;00m$
		[[36mself[39;49;00m [32mmyDependents:[39;49;00m ([31mdependents[39;49;00m [32mcopyWithDependent:[39;49;00m [31manObject[39;49;00m)].$
	^ [31manObject[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:53'![39;49;00m$
[32mbreakDependents[39;49;00m$
	[37m"Remove all of the receiver's dependents."[39;49;00m$
$
	[36mself[39;49;00m [32mmyDependents:[39;49;00m [36mnil[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:26'![39;49;00m$
[32mcanDiscardEdits[39;49;00m$
	[37m"Answer true if none of the views on this model has unaccepted edits that matter."[39;49;00m$
$
	[36mself[39;49;00m [32mdependents[39;49;00m$
		[32mdo:[39;49;00m [:[31meach[39;49;00m | [31meach[39;49;00m [32mcanDiscardEdits[39;49;00m [36mifFalse:[39;49;00m [^ [36mfalse[39;49;00m]]$
		[32mwithout:[39;49;00m [36mself[39;49;00m.$
	^ [36mtrue[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:58'![39;49;00m$
[32mdependents[39;49;00m$
	[37m"Answer a collection of objects that are 'dependent' on the receiver;[39;49;00m$
[37m	 that is, all objects that should be notified if the receiver changes."[39;49;00m$
$
	^ [36mself[39;49;00m [32mmyDependents[39;49;00m [32mifNil:[39;49;00m [[33m#([39;49;00m[33m)[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m![39;49;00m$
[32mevaluate:[39;49;00m [31mactionBlock[39;49;00m [32mwheneverChangeIn:[39;49;00m [31maspectBlock[39;49;00m$
	|[31m viewerThenObject objectThenViewer [39;49;00m|$
	[31mobjectThenViewer[39;49;00m _ [36mself[39;49;00m.$
	[31mviewerThenObject[39;49;00m _ [04m[32mObjectViewer[39;49;00m [32mon:[39;49;00m [31mobjectThenViewer[39;49;00m.$
	[31mobjectThenViewer[39;49;00m [32mbecome:[39;49;00m [31mviewerThenObject[39;49;00m.$
	[37m"--- Then ---"[39;49;00m$
	[31mobjectThenViewer[39;49;00m [32mxxxViewedObject:[39;49;00m [31mviewerThenObject[39;49;00m$
			[32mevaluate:[39;49;00m [31mactionBlock[39;49;00m$
			[32mwheneverChangeIn:[39;49;00m [31maspectBlock[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:59'![39;49;00m$
[32mhasUnacceptedEdits[39;49;00m$
	[37m"Answer true if any of the views on this object has unaccepted edits."[39;49;00m$
$
	[36mself[39;49;00m [32mdependents[39;49;00m$
		[32mdo:[39;49;00m [:[31meach[39;49;00m | [31meach[39;49;00m [32mhasUnacceptedEdits[39;49;00m [36mifTrue:[39;49;00m [^ [36mtrue[39;49;00m]]$
		[32mwithout:[39;49;00m [36mself[39;49;00m.$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:55'![39;49;00m$
[32mmyDependents[39;49;00m$
	[37m"Private. Answer a list of all the receiver's dependents."[39;49;00m$
$
	^ [04m[32mDependentsFields[39;49;00m [32mat:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m [][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 19:52'![39;49;00m$
[32mmyDependents:[39;49;00m [31maCollectionOrNil[39;49;00m$
	[37m"Private. Set (or remove) the receiver's dependents list."[39;49;00m$
$
	[31maCollectionOrNil[39;49;00m$
		[32mifNil:[39;49;00m [[04m[32mDependentsFields[39;49;00m [32mremoveKey:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m []]$
		[32mifNotNil:[39;49;00m [[04m[32mDependentsFields[39;49;00m [32mat:[39;49;00m [36mself[39;49;00m [32mput:[39;49;00m [31maCollectionOrNil[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'reThink 2/18/2001 17:06'![39;49;00m$
[32mrelease[39;49;00m$
	[37m"Remove references to objects that may refer to the receiver. This message [39;49;00m$
[37m	should be overridden by subclasses with any cycles, in which case the [39;49;00m$
[37m	subclass should also include the expression super release."[39;49;00m$
$
	[36mself[39;49;00m [32mreleaseActionMap[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'dependents access'[39;49;00m[34m stamp: 'sma 2/29/2000 20:23'![39;49;00m$
[32mremoveDependent:[39;49;00m [31manObject[39;49;00m$
	[37m"Remove the given object as one of the receiver's dependents."[39;49;00m$
$
	|[31m dependents [39;49;00m|$
	[31mdependents[39;49;00m _ [36mself[39;49;00m [32mdependents[39;49;00m [32mreject:[39;49;00m [:[31meach[39;49;00m | [31meach[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m].$
	[36mself[39;49;00m [32mmyDependents:[39;49;00m ([31mdependents[39;49;00m [32misEmpty[39;49;00m [36mifFalse:[39;49;00m [[31mdependents[39;49;00m]).$
	^ [31manObject[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'bh 9/16/2001 18:10'![39;49;00m$
[32macceptDroppingMorph:[39;49;00m [31mtransferMorph[39;49;00m [32mevent:[39;49;00m [31mevt[39;49;00m [32minMorph:[39;49;00m [31mdstListMorph[39;49;00m $
	$
	^[36mfalse[39;49;00m.[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'mir 5/16/2000 11:35'![39;49;00m$
[32mdragAnimationFor:[39;49;00m [31mitem[39;49;00m [32mtransferMorph:[39;49;00m [31mtransferMorph[39;49;00m $
	[37m"Default do nothing"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'panda 4/28/2000 16:20'![39;49;00m$
[32mdragPassengerFor:[39;49;00m [31mitem[39;49;00m [32minMorph:[39;49;00m [31mdragSource[39;49;00m $
	^[31mitem[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'panda 4/28/2000 16:11'![39;49;00m$
[32mdragTransferType[39;49;00m$
	^[36mnil[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'panda 4/28/2000 16:05'![39;49;00m$
[32mdragTransferTypeForMorph:[39;49;00m [31mdragSource[39;49;00m $
	^[36mnil[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'drag and drop'[39;49;00m[34m stamp: 'mir 5/8/2000 17:19'![39;49;00m$
[32mwantsDroppedMorph:[39;49;00m [31maMorph[39;49;00m [32mevent:[39;49;00m [31manEvent[39;49;00m [32minMorph:[39;49;00m [31mdestinationLM[39;49;00m $
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'sma 5/6/2000 19:35'![39;49;00m$
[32massert:[39;49;00m [31maBlock[39;49;00m$
	[37m"Throw an assertion error if aBlock does not evaluates to true."[39;49;00m$
$
	[31maBlock[39;49;00m [32mvalue[39;49;00m [36mifFalse:[39;49;00m [[04m[32mAssertionFailure[39;49;00m [32msignal:[39;49;00m [33m'Assertion failed'[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'nk 1/15/2004 10:54'![39;49;00m$
[32massert:[39;49;00m [31maBlock[39;49;00m [32mdescriptionBlock:[39;49;00m [31mdescriptionBlock[39;49;00m$
	[37m"Throw an assertion error if aBlock does not evaluate to true."[39;49;00m$
$
	[31maBlock[39;49;00m [32mvalue[39;49;00m [36mifFalse:[39;49;00m [[04m[32mAssertionFailure[39;49;00m [32msignal:[39;49;00m [31mdescriptionBlock[39;49;00m [32mvalue[39;49;00m [32masString[39;49;00m ][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'nk 10/25/2003 16:47'![39;49;00m$
[32massert:[39;49;00m [31maBlock[39;49;00m [32mdescription:[39;49;00m [31maString[39;49;00m$
	[37m"Throw an assertion error if aBlock does not evaluates to true."[39;49;00m$
$
	[31maBlock[39;49;00m [32mvalue[39;49;00m [36mifFalse:[39;49;00m [[04m[32mAssertionFailure[39;49;00m [32msignal:[39;49;00m [31maString[39;49;00m ][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'md 10/13/2004 15:59'![39;49;00m$
[32mbackwardCompatibilityOnly:[39;49;00m [31manExplanationString[39;49;00m$
	[37m"Warn that the sending method has been deprecated. Methods that are tagt with #backwardCompatibility:[39;49;00m$
[37m	 are kept for compatibility."[39;49;00m$
$
	[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
		[[04m[32mDeprecation[39;49;00m [32msignal:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m' has been deprecated (but will be kept for compatibility). '[39;49;00m[32m,[39;49;00m [31manExplanationString[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m![39;49;00m$
[32mcaseError[39;49;00m$
	[37m"Report an error from an in-line or explicit case statement."[39;49;00m$
$
	[36mself[39;49;00m [32merror:[39;49;00m [33m'Case not found, and no otherwise clause'[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'rbb 3/1/2005 09:26'![39;49;00m$
[32mconfirm:[39;49;00m [31mqueryString[39;49;00m$
	[37m"Put up a yes/no menu with caption queryString. Answer true if the [39;49;00m$
[37m	response is yes, false if no. This is a modal question--the user must [39;49;00m$
[37m	respond yes or no."[39;49;00m$
$
	[37m"nil confirm: 'Are you hungry?'"[39;49;00m$
$
	^ [04m[32mUIManager[39;49;00m [32mdefault[39;49;00m [32mconfirm:[39;49;00m [31mqueryString[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'rbb 3/1/2005 09:27'![39;49;00m$
[32mconfirm:[39;49;00m [31maString[39;49;00m [32morCancel:[39;49;00m [31mcancelBlock[39;49;00m$
	[37m"Put up a yes/no/cancel menu with caption aString. Answer true if  [39;49;00m$
[37m	the response is yes, false if no. If cancel is chosen, evaluate  [39;49;00m$
[37m	cancelBlock. This is a modal question--the user must respond yes or no."[39;49;00m$
$
	^ [04m[32mUIManager[39;49;00m [32mdefault[39;49;00m [32mconfirm:[39;49;00m [31maString[39;49;00m [32morCancel:[39;49;00m [31mcancelBlock[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'dew 10/6/2003 18:20'![39;49;00m$
[32mdeprecated:[39;49;00m [31manExplanationString[39;49;00m$
	[37m"Warn that the sending method has been deprecated."[39;49;00m$
$
	[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
		[[04m[32mDeprecation[39;49;00m [32msignal:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m' has been deprecated. '[39;49;00m[32m,[39;49;00m [31manExplanationString[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'dew 10/7/2003 00:26'![39;49;00m$
[32mdeprecated:[39;49;00m [31manExplanationString[39;49;00m [32mblock:[39;49;00m [31maBlock[39;49;00m $
	 [37m"Warn that the sender has been deprecated.  Answer the value of aBlock on resumption.  (Note that #deprecated: is usually the preferred method.)"[39;49;00m$
$
	[04m[32mPreferences[39;49;00m [32mshowDeprecationWarnings[39;49;00m [36mifTrue:[39;49;00m$
		[[04m[32mDeprecation[39;49;00m$
			[32msignal:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m' has been deprecated. '[39;49;00m[32m,[39;49;00m [31manExplanationString[39;49;00m].$
	^ [31maBlock[39;49;00m [32mvalue[39;49;00m.$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'md 2/22/2006 21:21'![39;49;00m$
[32mdoesNotUnderstand:[39;49;00m [31maMessage[39;49;00m $
	 [37m"Handle the fact that there was an attempt to send the given message to the receiver but the receiver does not understand this message (typically sent from the machine when a message is sent to the receiver and no method is defined for that selector)."[39;49;00m$
	[37m"Testing: (3 activeProcess)"[39;49;00m$
$
	[04m[32mMessageNotUnderstood[39;49;00m [36mnew[39;49;00m $
		[32mmessage:[39;49;00m [31maMessage[39;49;00m;$
		[32mreceiver:[39;49;00m [36mself[39;49;00m;$
		[32msignal[39;49;00m.$
	^ [31maMessage[39;49;00m [32msentTo:[39;49;00m [36mself[39;49;00m.$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'TRee 11/4/2003 16:47'![39;49;00m$
[32mdpsTrace:[39;49;00m [31mreportObject[39;49;00m  $
	[04m[32mTranscript[39;49;00m [32mmyDependents[39;49;00m [32misNil[39;49;00m [36mifTrue:[39;49;00m [^[36mself[39;49;00m].$
	[36mself[39;49;00m [32mdpsTrace:[39;49;00m [31mreportObject[39;49;00m [32mlevels:[39;49;00m [34m1[39;49;00m [32mwithContext:[39;49;00m [36mthisContext[39;49;00m$
		$
[37m" nil dpsTrace: 'sludder'. "[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'TRee 11/4/2003 16:49'![39;49;00m$
[32mdpsTrace:[39;49;00m [31mreportObject[39;49;00m [32mlevels:[39;49;00m [31manInt[39;49;00m$
	[36mself[39;49;00m [32mdpsTrace:[39;49;00m [31mreportObject[39;49;00m [32mlevels:[39;49;00m [31manInt[39;49;00m [32mwithContext:[39;49;00m [36mthisContext[39;49;00m$
$
[37m"(1 to: 3) do: [:int | nil dpsTrace: int levels: 5.]"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'TRee 11/4/2003 17:02'![39;49;00m$
[32mdpsTrace:[39;49;00m [31mreportObject[39;49;00m [32mlevels:[39;49;00m [31manInt[39;49;00m [32mwithContext:[39;49;00m [31mcurrentContext[39;49;00m$
	|[31m reportString context displayCount [39;49;00m|$
	[31mreportString[39;49;00m := ([31mreportObject[39;49;00m [32mrespondsTo:[39;49;00m [33m#asString[39;49;00m) $
			[36mifTrue:[39;49;00m [[31mreportObject[39;49;00m [32masString[39;49;00m] [36mifFalse:[39;49;00m [[31mreportObject[39;49;00m [32mprintString[39;49;00m].$
	([04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#Decompiler[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m]) $
	[32mifNil:[39;49;00m $
		[[04m[32mTranscript[39;49;00m [32mcr[39;49;00m; [32mshow:[39;49;00m [31mreportString[39;49;00m]$
	[32mifNotNil:[39;49;00m$
		[[31mcontext[39;49;00m := [31mcurrentContext[39;49;00m.$
		[31mdisplayCount[39;49;00m := [31manInt[39;49;00m [32m>[39;49;00m [34m1[39;49;00m.$
		[34m1[39;49;00m [32mto:[39;49;00m [31manInt[39;49;00m [32mdo:[39;49;00m$
			[:[31mcount[39;49;00m |$
			[04m[32mTranscript[39;49;00m [32mcr[39;49;00m.$
			[31mdisplayCount[39;49;00m$
				[36mifTrue:[39;49;00m [[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m [31mcount[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m': '[39;49;00m].$
			$
			[31mreportString[39;49;00m [32mnotNil[39;49;00m$
			[36mifTrue:[39;49;00m$
				[[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m [31mcontext[39;49;00m [32mhome[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m $
			[32m,[39;49;00m [33m'/'[39;49;00m [32m,[39;49;00m [31mcontext[39;49;00m [32msender[39;49;00m [32mselector[39;49;00m[32m,[39;49;00m  [33m' ('[39;49;00m [32m,[39;49;00m [31mreportString[39;49;00m [32m,[39;49;00m [33m')'[39;49;00m.$
				[31mcontext[39;49;00m := [31mcontext[39;49;00m [32msender[39;49;00m.$
				[31mreportString[39;49;00m := [36mnil[39;49;00m]$
			[36mifFalse:[39;49;00m$
				[([31mcontext[39;49;00m [32mnotNil[39;49;00m [32mand:[39;49;00m [([31mcontext[39;49;00m := [31mcontext[39;49;00m [32msender[39;49;00m) [32mnotNil[39;49;00m])$
				[36mifTrue:[39;49;00m [[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m [31mcontext[39;49;00m [32mreceiver[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32m,[39;49;00m [33m'/'[39;49;00m [32m,[39;49;00m [31mcontext[39;49;00m [32mselector[39;49;00m]]].$
		[37m"Transcript cr"[39;49;00m].[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'md 8/2/2005 22:17'![39;49;00m$
[32merror[39;49;00m$
	[37m"Throw a generic Error exception."[39;49;00m$
$
	^[36mself[39;49;00m [32merror:[39;49;00m [33m'Error!!'[39;49;00m.[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'tfei 4/12/1999 12:55'![39;49;00m$
[32merror:[39;49;00m [31maString[39;49;00m $
	[37m"Throw a generic Error exception."[39;49;00m$
$
	^[04m[32mError[39;49;00m [36mnew[39;49;00m [32msignal:[39;49;00m [31maString[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'al 9/16/2005 14:12'![39;49;00m$
[32mexplicitRequirement[39;49;00m$
	[36mself[39;49;00m [32merror:[39;49;00m [33m'Explicitly required method'[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'al 2/13/2006 22:20'![39;49;00m$
[32mhalt[39;49;00m$
	[37m"This is the typical message to use for inserting breakpoints during [39;49;00m$
[37m	debugging. It behaves like halt:, but does not call on halt: in order to [39;49;00m$
[37m	avoid putting this message on the stack. Halt is especially useful when [39;49;00m$
[37m	the breakpoint message is an arbitrary one."[39;49;00m$
$
	[04m[32mHalt[39;49;00m [32msignal[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'tfei 4/12/1999 12:59'![39;49;00m$
[32mhalt:[39;49;00m [31maString[39;49;00m $
	[37m"This is the typical message to use for inserting breakpoints during [39;49;00m$
[37m	debugging. It creates and schedules a Notifier with the argument, [39;49;00m$
[37m	aString, as the label."[39;49;00m$
	$
	[04m[32mHalt[39;49;00m [36mnew[39;49;00m [32msignal:[39;49;00m [31maString[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:24'![39;49;00m$
[32mhandles:[39;49;00m [31mexception[39;49;00m$
	[37m"This method exists in case a non exception class is the first arg in an on:do: (for instance using a exception class that is not loaded). We prefer this to raising an error during error handling itself. Also, semantically it makes sense that the exception handler is not active if its exception class is not loaded"[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'ar 9/27/2005 20:24'![39;49;00m$
[32mnotifyWithLabel:[39;49;00m [31maString[39;49;00m $
	[37m"Create and schedule a Notifier with aString as the window label as well as the contents of the window, in  order to request confirmation before a process can proceed."[39;49;00m$
$
	[04m[32mToolSet[39;49;00m$
		[32mdebugContext:[39;49;00m [36mthisContext[39;49;00m$
		[32mlabel:[39;49;00m [31maString[39;49;00m$
		[32mcontents:[39;49;00m [31maString[39;49;00m$
$
	[37m"nil notifyWithLabel: 'let us see if this works'"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'hg 10/2/2001 20:49'![39;49;00m$
[32mnotify:[39;49;00m [31maString[39;49;00m $
	[37m"Create and schedule a Notifier with the argument as the message in [39;49;00m$
[37m	order to request confirmation before a process can proceed."[39;49;00m$
$
	[04m[32mWarning[39;49;00m [32msignal:[39;49;00m [31maString[39;49;00m$
$
	[37m"nil notify: 'confirmation message'"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m![39;49;00m$
[32mnotify:[39;49;00m [31maString[39;49;00m [32mat:[39;49;00m [31mlocation[39;49;00m$
	[37m"Create and schedule a Notifier with the argument as the message in [39;49;00m$
[37m	order to request confirmation before a process can proceed. Subclasses can[39;49;00m$
[37m	override this and insert an error message at location within aString."[39;49;00m$
$
	[36mself[39;49;00m [32mnotify:[39;49;00m [31maString[39;49;00m$
$
	[37m"nil notify: 'confirmation message' at: 12"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m![39;49;00m$
[32mprimitiveFailed[39;49;00m$
	[37m"Announce that a primitive has failed and there is no appropriate [39;49;00m$
[37m	Smalltalk code to run."[39;49;00m$
$
	[36mself[39;49;00m [32merror:[39;49;00m [33m'a primitive has failed'[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'al 9/16/2005 14:12'![39;49;00m$
[32mrequirement[39;49;00m$
	[36mself[39;49;00m [32merror:[39;49;00m [33m'Implicitly required method'[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'AFi 2/8/2003 22:52'![39;49;00m$
[32mshouldBeImplemented[39;49;00m$
	[37m"Announce that this message should be implemented"[39;49;00m$
$
	[36mself[39;49;00m [32merror:[39;49;00m [33m'This message should be implemented'[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m![39;49;00m$
[32mshouldNotImplement[39;49;00m$
	[37m"Announce that, although the receiver inherits this message, it should [39;49;00m$
[37m	not implement it."[39;49;00m$
$
	[36mself[39;49;00m [32merror:[39;49;00m [33m'This message is not appropriate for this object'[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'md 2/17/2006 12:02'![39;49;00m$
[32msubclassResponsibility[39;49;00m$
	[37m"This message sets up a framework for the behavior of the class' subclasses.[39;49;00m$
[37m	Announce that the subclass should have implemented this message."[39;49;00m$
$
	[36mself[39;49;00m [32merror:[39;49;00m [33m'My subclass should have overridden '[39;49;00m[32m,[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mselector[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'error handling'[39;49;00m[34m stamp: 'al 12/16/2003 16:16'![39;49;00m$
[32mtraitConflict[39;49;00m$
	[36mself[39;49;00m [32merror:[39;49;00m [33m'A class or trait does not properly resolve a conflict between multiple traits it uses.'[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'evaluating'[39;49;00m[34m stamp: 'reThink 3/12/2001 18:14'![39;49;00m$
[32mvalue[39;49;00m$
$
	^[36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'evaluating'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:23'![39;49;00m$
[32mvalueWithArguments:[39;49;00m [31maSequenceOfArguments[39;49;00m$
$
	^[36mself[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events'[39;49;00m[34m stamp: 'nk 8/27/2003 16:23'![39;49;00m$
[32mactionsWithReceiver:[39;49;00m [31manObject[39;49;00m [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m$
$
	^([36mself[39;49;00m [32mactionSequenceForEvent:[39;49;00m [31manEventSelector[39;49;00m)$
                [32mselect:[39;49;00m [:[31manAction[39;49;00m | [31manAction[39;49;00m [32mreceiver[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m ][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events'[39;49;00m[34m stamp: 'nk 8/27/2003 17:45'![39;49;00m$
[32mrenameActionsWithReceiver:[39;49;00m [31manObject[39;49;00m [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m [32mtoEvent:[39;49;00m [31mnewEvent[39;49;00m$
$
	|[31m oldActions newActions [39;49;00m|$
	[31moldActions[39;49;00m _ [04m[32mSet[39;49;00m [36mnew[39;49;00m.$
	[31mnewActions[39;49;00m _ [04m[32mSet[39;49;00m [36mnew[39;49;00m.$
	([36mself[39;49;00m [32mactionSequenceForEvent:[39;49;00m [31manEventSelector[39;49;00m) [32mdo:[39;49;00m [ :[31maction[39;49;00m |$
		[31maction[39;49;00m [32mreceiver[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m$
			[36mifTrue:[39;49;00m [ [31moldActions[39;49;00m [32madd:[39;49;00m [31manObject[39;49;00m ]$
			[36mifFalse:[39;49;00m [ [31mnewActions[39;49;00m [32madd:[39;49;00m [31manObject[39;49;00m ]].$
	[36mself[39;49;00m [32msetActionSequence:[39;49;00m ([04m[32mActionSequence[39;49;00m [32mwithAll:[39;49;00m [31mnewActions[39;49;00m) [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m.$
	[31moldActions[39;49;00m [32mdo:[39;49;00m [ :[31mact[39;49;00m | [36mself[39;49;00m [32mwhen:[39;49;00m [31mnewEvent[39;49;00m [32mevaluate:[39;49;00m [31mact[39;49;00m ].[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'nk 12/20/2002 17:48'![39;49;00m$
[32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m$
    [37m"Answer the action to be evaluated when <anEventSelector> has been triggered."[39;49;00m$
$
	|[31m actions [39;49;00m|$
	[31mactions[39;49;00m := [36mself[39;49;00m [32mactionMap[39;49;00m$
		[32mat:[39;49;00m [31manEventSelector[39;49;00m [32masSymbol[39;49;00m$
		[32mifAbsent:[39;49;00m [[36mnil[39;49;00m].$
	[31mactions[39;49;00m [32mifNil:[39;49;00m [^[36mnil[39;49;00m].$
	^ [31mactions[39;49;00m [32masMinimalRepresentation[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'nk 12/20/2002 17:48'![39;49;00m$
[32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m$
[32mifAbsent:[39;49;00m [31manExceptionBlock[39;49;00m$
    [37m"Answer the action to be evaluated when <anEventSelector> has been triggered."[39;49;00m$
$
	|[31m actions [39;49;00m|$
	[31mactions[39;49;00m := [36mself[39;49;00m [32mactionMap[39;49;00m$
		[32mat:[39;49;00m [31manEventSelector[39;49;00m [32masSymbol[39;49;00m$
		[32mifAbsent:[39;49;00m [[36mnil[39;49;00m].$
	[31mactions[39;49;00m [32mifNil:[39;49;00m [^[31manExceptionBlock[39;49;00m [32mvalue[39;49;00m].$
	^ [31mactions[39;49;00m [32masMinimalRepresentation[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'reThink 2/18/2001 14:43'![39;49;00m$
[32mactionMap[39;49;00m$
$
	^[04m[32mEventManager[39;49;00m [32mactionMapFor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'rw 4/27/2002 08:35'![39;49;00m$
[32mactionSequenceForEvent:[39;49;00m [31manEventSelector[39;49;00m$
$
    ^([36mself[39;49;00m [32mactionMap[39;49;00m$
        [32mat:[39;49;00m [31manEventSelector[39;49;00m [32masSymbol[39;49;00m$
        [32mifAbsent:[39;49;00m [^[04m[32mWeakActionSequence[39;49;00m [36mnew[39;49;00m])$
            [32masActionSequence[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'SqR 6/28/2001 13:19'![39;49;00m$
[32mactionsDo:[39;49;00m [31maBlock[39;49;00m$
$
	[36mself[39;49;00m [32mactionMap[39;49;00m [32mdo:[39;49;00m [31maBlock[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'rw 2/10/2002 13:05'![39;49;00m$
[32mcreateActionMap[39;49;00m$
$
	^[04m[32mIdentityDictionary[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'SqR 2/19/2001 14:04'![39;49;00m$
[32mhasActionForEvent:[39;49;00m [31manEventSelector[39;49;00m$
    [37m"Answer true if there is an action associated with anEventSelector"[39;49;00m$
$
    ^([36mself[39;49;00m [32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m) [32mnotNil[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:29'![39;49;00m$
[32msetActionSequence:[39;49;00m [31mactionSequence[39;49;00m$
[32mforEvent:[39;49;00m [31manEventSelector[39;49;00m$
$
    |[31m action [39;49;00m|$
    [31maction[39;49;00m := [31mactionSequence[39;49;00m [32masMinimalRepresentation[39;49;00m.$
    [31maction[39;49;00m [32m==[39;49;00m [36mnil[39;49;00m$
        [36mifTrue:[39;49;00m$
            [[36mself[39;49;00m [32mremoveActionsForEvent:[39;49;00m [31manEventSelector[39;49;00m]$
        [36mifFalse:[39;49;00m$
            [[36mself[39;49;00m [32mupdateableActionMap[39;49;00m$
                [32mat:[39;49;00m [31manEventSelector[39;49;00m [32masSymbol[39;49;00m$
                [32mput:[39;49;00m [31maction[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-accessing'[39;49;00m[34m stamp: 'reThink 2/25/2001 08:50'![39;49;00m$
[32mupdateableActionMap[39;49;00m$
$
	^[04m[32mEventManager[39;49;00m [32mupdateableActionMapFor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-registering'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:04'![39;49;00m$
[32mwhen:[39;49;00m [31manEventSelector[39;49;00m [32mevaluate:[39;49;00m [31manAction[39;49;00m $
$
	|[31m actions [39;49;00m|$
	[31mactions[39;49;00m := [36mself[39;49;00m [32mactionSequenceForEvent:[39;49;00m [31manEventSelector[39;49;00m.$
	([31mactions[39;49;00m [32mincludes:[39;49;00m [31manAction[39;49;00m)$
		[36mifTrue:[39;49;00m [^ [36mself[39;49;00m].$
	[36mself[39;49;00m $
		[32msetActionSequence:[39;49;00m ([31mactions[39;49;00m [32mcopyWith:[39;49;00m [31manAction[39;49;00m)$
		[32mforEvent:[39;49;00m [31manEventSelector[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-registering'[39;49;00m[34m stamp: 'rww 12/30/2002 10:37'![39;49;00m$
[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
[32mto:[39;49;00m [31manObject[39;49;00m$
 $
    [36mself[39;49;00m$
        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
        [32mevaluate:[39;49;00m ([04m[32mWeakMessageSend[39;49;00m$
            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m)[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-registering'[39;49;00m[34m stamp: 'rww 12/30/2002 10:37'![39;49;00m$
[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
[32mto:[39;49;00m [31manObject[39;49;00m$
[32mwithArguments:[39;49;00m [31manArgArray[39;49;00m$
 $
    [36mself[39;49;00m$
        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
        [32mevaluate:[39;49;00m ([04m[32mWeakMessageSend[39;49;00m$
            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
		[32marguments:[39;49;00m [31manArgArray[39;49;00m)[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-registering'[39;49;00m[34m stamp: 'rww 12/30/2002 10:37'![39;49;00m$
[32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
[32msend:[39;49;00m [31maMessageSelector[39;49;00m$
[32mto:[39;49;00m [31manObject[39;49;00m$
[32mwith:[39;49;00m [31manArg[39;49;00m$
 $
    [36mself[39;49;00m$
        [32mwhen:[39;49;00m [31manEventSelector[39;49;00m$
        [32mevaluate:[39;49;00m ([04m[32mWeakMessageSend[39;49;00m$
            [32mreceiver:[39;49;00m [31manObject[39;49;00m$
            [32mselector:[39;49;00m [31maMessageSelector[39;49;00m$
		[32marguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manArg[39;49;00m))[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:33'![39;49;00m$
[32mreleaseActionMap[39;49;00m$
$
	[04m[32mEventManager[39;49;00m [32mreleaseActionMapFor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:33'![39;49;00m$
[32mremoveActionsForEvent:[39;49;00m [31manEventSelector[39;49;00m$
$
    |[31m map [39;49;00m|$
    [31mmap[39;49;00m := [36mself[39;49;00m [32mactionMap[39;49;00m.$
    [31mmap[39;49;00m [32mremoveKey:[39;49;00m [31manEventSelector[39;49;00m [32masSymbol[39;49;00m [32mifAbsent:[39;49;00m [].$
    [31mmap[39;49;00m [32misEmpty[39;49;00m$
        [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mreleaseActionMap[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'nk 8/25/2003 21:46'![39;49;00m$
[32mremoveActionsSatisfying:[39;49;00m [31maBlock[39;49;00m$
$
	[36mself[39;49;00m [32mactionMap[39;49;00m [32mkeys[39;49;00m [32mdo:[39;49;00m$
		[:[31meachEventSelector[39;49;00m |$
			[36mself[39;49;00m$
   				[32mremoveActionsSatisfying:[39;49;00m [31maBlock[39;49;00m$
				[32mforEvent:[39;49;00m [31meachEventSelector[39;49;00m$
		][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:31'![39;49;00m$
[32mremoveActionsSatisfying:[39;49;00m [31maOneArgBlock[39;49;00m $
[32mforEvent:[39;49;00m [31manEventSelector[39;49;00m$
$
    [36mself[39;49;00m$
        [32msetActionSequence:[39;49;00m$
            (([36mself[39;49;00m [32mactionSequenceForEvent:[39;49;00m [31manEventSelector[39;49;00m)$
                [32mreject:[39;49;00m [:[31manAction[39;49;00m | [31maOneArgBlock[39;49;00m [32mvalue:[39;49;00m [31manAction[39;49;00m])$
        [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'rw 7/29/2003 17:18'![39;49;00m$
[32mremoveActionsWithReceiver:[39;49;00m [31manObject[39;49;00m$
$
	[36mself[39;49;00m [32mactionMap[39;49;00m [32mcopy[39;49;00m [32mkeysDo:[39;49;00m$
		[:[31meachEventSelector[39;49;00m |$
			[36mself[39;49;00m$
   				[32mremoveActionsSatisfying:[39;49;00m [:[31manAction[39;49;00m | [31manAction[39;49;00m [32mreceiver[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m]$
				[32mforEvent:[39;49;00m [31meachEventSelector[39;49;00m$
		][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:36'![39;49;00m$
[32mremoveActionsWithReceiver:[39;49;00m [31manObject[39;49;00m$
[32mforEvent:[39;49;00m [31manEventSelector[39;49;00m$
$
    [36mself[39;49;00m$
        [32mremoveActionsSatisfying:[39;49;00m$
            [:[31manAction[39;49;00m |$
            [31manAction[39;49;00m [32mreceiver[39;49;00m [32m==[39;49;00m [31manObject[39;49;00m]$
        [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-removing'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:31'![39;49;00m$
[32mremoveAction:[39;49;00m [31manAction[39;49;00m$
[32mforEvent:[39;49;00m [31manEventSelector[39;49;00m$
$
    [36mself[39;49;00m$
        [32mremoveActionsSatisfying:[39;49;00m [:[31maction[39;49;00m | [31maction[39;49;00m [32m=[39;49;00m [31manAction[39;49;00m]$
        [32mforEvent:[39;49;00m [31manEventSelector[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:22'![39;49;00m$
[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
	[37m"Evaluate all actions registered for <anEventSelector>. Return the value of the last registered action."[39;49;00m$
$
    ^([36mself[39;49;00m [32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m) [32mvalue[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 17:09'![39;49;00m$
[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
[32mifNotHandled:[39;49;00m [31manExceptionBlock[39;49;00m$
	[37m"Evaluate all actions registered for <anEventSelector>. Return the value of the last registered action."[39;49;00m$
$
    ^([36mself[39;49;00m $
		[32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m$
		[32mifAbsent:[39;49;00m [^[31manExceptionBlock[39;49;00m [32mvalue[39;49;00m]) [32mvalue[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:21'![39;49;00m$
[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
[32mwithArguments:[39;49;00m [31manArgumentList[39;49;00m$
$
    ^([36mself[39;49;00m [32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m)$
        [32mvalueWithArguments:[39;49;00m [31manArgumentList[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 15:21'![39;49;00m$
[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
[32mwithArguments:[39;49;00m [31manArgumentList[39;49;00m$
[32mifNotHandled:[39;49;00m [31manExceptionBlock[39;49;00m$
$
    ^([36mself[39;49;00m $
		[32mactionForEvent:[39;49;00m [31manEventSelector[39;49;00m$
		[32mifAbsent:[39;49;00m [^[31manExceptionBlock[39;49;00m [32mvalue[39;49;00m])$
        [32mvalueWithArguments:[39;49;00m [31manArgumentList[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 14:59'![39;49;00m$
[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
[32mwith:[39;49;00m [31manObject[39;49;00m$
$
    ^[36mself[39;49;00m $
		[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
		[32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m)[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'events-triggering'[39;49;00m[34m stamp: 'reThink 2/18/2001 14:59'![39;49;00m$
[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
[32mwith:[39;49;00m [31manObject[39;49;00m$
[32mifNotHandled:[39;49;00m [31manExceptionBlock[39;49;00m$
$
    ^[36mself[39;49;00m $
		[32mtriggerEvent:[39;49;00m [31manEventSelector[39;49;00m$
		[32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m)$
		[32mifNotHandled:[39;49;00m [31manExceptionBlock[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 00:42'![39;49;00m$
[32mbyteEncode:[39;49;00m[31maStream[39;49;00m$
	[36mself[39;49;00m [32mflattenOnStream:[39;49;00m[31maStream[39;49;00m.$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m![39;49;00m$
[32mdrawOnCanvas:[39;49;00m[31maStream[39;49;00m$
	[36mself[39;49;00m [32mflattenOnStream:[39;49;00m[31maStream[39;49;00m.$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 01:31'![39;49;00m$
[32melementSeparator[39;49;00m$
	^[36mnil[39;49;00m.[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m![39;49;00m$
[32mencodePostscriptOn:[39;49;00m[31maStream[39;49;00m$
	[36mself[39;49;00m [32mbyteEncode:[39;49;00m[31maStream[39;49;00m.$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 00:07'![39;49;00m$
[32mflattenOnStream:[39;49;00m[31maStream[39;49;00m$
	[36mself[39;49;00m [32mwriteOnFilterStream:[39;49;00m[31maStream[39;49;00m.$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'mpw 6/22/1930 22:56'![39;49;00m$
[32mfullDrawPostscriptOn:[39;49;00m[31maStream[39;49;00m$
	^[31maStream[39;49;00m [32mfullDraw:[39;49;00m[36mself[39;49;00m.$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 01:51'![39;49;00m$
[32mprintOnStream:[39;49;00m[31maStream[39;49;00m$
	[36mself[39;49;00m [32mbyteEncode:[39;49;00m[31maStream[39;49;00m.$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 00:49'![39;49;00m$
[32mputOn:[39;49;00m[31maStream[39;49;00m$
	^[31maStream[39;49;00m [32mnextPut:[39;49;00m[36mself[39;49;00m.$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 01:53'![39;49;00m$
[32mstoreOnStream:[39;49;00m[31maStream[39;49;00m$
	[36mself[39;49;00m [32mprintOnStream:[39;49;00m[31maStream[39;49;00m.$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'filter streaming'[39;49;00m[34m stamp: 'MPW 1/1/1901 00:06'![39;49;00m$
[32mwriteOnFilterStream:[39;49;00m[31maStream[39;49;00m$
	[31maStream[39;49;00m [32mwriteObject:[39;49;00m[36mself[39;49;00m.$
[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 3/21/98 16:26'![39;49;00m$
[32mactAsExecutor[39;49;00m$
	[37m"Prepare the receiver to act as executor for any resources associated with it"[39;49;00m$
	[36mself[39;49;00m [32mbreakDependents[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 3/20/98 22:19'![39;49;00m$
[32mexecutor[39;49;00m$
	[37m"Return an object which can act as executor for finalization of the receiver"[39;49;00m$
	^[36mself[39;49;00m [32mshallowCopy[39;49;00m [32mactAsExecutor[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 5/19/2003 20:10'![39;49;00m$
[32mfinalizationRegistry[39;49;00m$
	[37m"Answer the finalization registry associated with the receiver."[39;49;00m$
	^[04m[32mWeakRegistry[39;49;00m [32mdefault[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 3/21/98 16:27'![39;49;00m$
[32mfinalize[39;49;00m$
	[37m"Finalize the resource associated with the receiver. This message should only be sent during the finalization process. There is NO garantuee that the resource associated with the receiver hasn't been free'd before so take care that you don't run into trouble - this all may happen with interrupt priority."[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 3/21/98 18:38'![39;49;00m$
[32mretryWithGC:[39;49;00m [31mexecBlock[39;49;00m [32muntil:[39;49;00m [31mtestBlock[39;49;00m$
	[37m"Retry execBlock as long as testBlock returns false. Do an incremental GC after the first try, a full GC after the second try."[39;49;00m$
	|[31m blockValue [39;49;00m|$
	[31mblockValue[39;49;00m := [31mexecBlock[39;49;00m [32mvalue[39;49;00m.$
	([31mtestBlock[39;49;00m [32mvalue:[39;49;00m [31mblockValue[39;49;00m) [36mifTrue:[39;49;00m[^[31mblockValue[39;49;00m].$
	[04m[32mSmalltalk[39;49;00m [32mgarbageCollectMost[39;49;00m.$
	[31mblockValue[39;49;00m := [31mexecBlock[39;49;00m [32mvalue[39;49;00m.$
	([31mtestBlock[39;49;00m [32mvalue:[39;49;00m [31mblockValue[39;49;00m) [36mifTrue:[39;49;00m[^[31mblockValue[39;49;00m].$
	[04m[32mSmalltalk[39;49;00m [32mgarbageCollect[39;49;00m.$
	^[31mexecBlock[39;49;00m [32mvalue[39;49;00m.[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'finalization'[39;49;00m[34m stamp: 'ar 5/19/2003 20:14'![39;49;00m$
[32mtoFinalizeSend:[39;49;00m [31maSelector[39;49;00m [32mto:[39;49;00m [31maFinalizer[39;49;00m [32mwith:[39;49;00m [31maResourceHandle[39;49;00m$
	[37m"When I am finalized (e.g., garbage collected) close the associated resource handle by sending aSelector to the appropriate finalizer (the guy who knows how to get rid of the resource).[39;49;00m$
[37m	WARNING: Neither the finalizer nor the resource handle are allowed to reference me. If they do, then I will NEVER be garbage collected. Since this cannot be validated here, it is up to the client to make sure this invariant is not broken."[39;49;00m$
	[36mself[39;49;00m [32m==[39;49;00m [31maFinalizer[39;49;00m [36mifTrue:[39;49;00m[[36mself[39;49;00m [32merror:[39;49;00m [33m'I cannot finalize myself'[39;49;00m].$
	[36mself[39;49;00m [32m==[39;49;00m [31maResourceHandle[39;49;00m [36mifTrue:[39;49;00m[[36mself[39;49;00m [32merror:[39;49;00m [33m'I cannot finalize myself'[39;49;00m].$
	^[36mself[39;49;00m [32mfinalizationRegistry[39;49;00m [32madd:[39;49;00m [36mself[39;49;00m [32mexecutor:[39;49;00m$
		([04m[32mObjectFinalizer[39;49;00m [36mnew[39;49;00m$
			[32mreceiver:[39;49;00m [31maFinalizer[39;49;00m$
			[32mselector:[39;49;00m [31maSelector[39;49;00m$
			[32margument:[39;49;00m [31maResourceHandle[39;49;00m)[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'flagging'[39;49;00m[34m stamp: 'sw 8/4/97 16:49'![39;49;00m$
[32misThisEverCalled[39;49;00m$
	^ [36mself[39;49;00m [32misThisEverCalled:[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'flagging'[39;49;00m[34m![39;49;00m$
[32misThisEverCalled:[39;49;00m [31mmsg[39;49;00m$
	[37m"Send this message, with some useful printable argument, from methods or branches of methods which you believe are never reached.  2/5/96 sw"[39;49;00m$
$
	[36mself[39;49;00m [32mhalt:[39;49;00m [33m'This is indeed called: '[39;49;00m[32m,[39;49;00m [31mmsg[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'flagging'[39;49;00m[34m stamp: 'jm 3/18/98 17:23'![39;49;00m$
[32mlogEntry[39;49;00m$
$
	[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m [33m'Entered '[39;49;00m[32m,[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m; [32mcr[39;49;00m.$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'flagging'[39;49;00m[34m stamp: 'jm 3/18/98 17:23'![39;49;00m$
[32mlogExecution[39;49;00m$
$
	[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m [33m'Executing '[39;49;00m[32m,[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m; [32mcr[39;49;00m.$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'flagging'[39;49;00m[34m stamp: 'jm 3/18/98 17:22'![39;49;00m$
[32mlogExit[39;49;00m$
$
	[04m[32mTranscript[39;49;00m [32mshow:[39;49;00m  [33m'Exited '[39;49;00m[32m,[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m; [32mcr[39;49;00m.$
[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'graph model'[39;49;00m[34m stamp: 'dgd 9/18/2004 15:07'![39;49;00m$
[32maddModelYellowButtonMenuItemsTo:[39;49;00m [31maCustomMenu[39;49;00m [32mforMorph:[39;49;00m [31maMorph[39;49;00m [32mhand:[39;49;00m [31maHandMorph[39;49;00m $
	[37m"The receiver serves as the model for aMorph; a menu is being constructed for the morph, and here the receiver is able to add its own items"[39;49;00m$
	[04m[32mPreferences[39;49;00m [32mcmdGesturesEnabled[39;49;00m [36mifTrue:[39;49;00m [ [37m"build mode"[39;49;00m$
		[31maCustomMenu[39;49;00m [32madd:[39;49;00m [33m'inspect model'[39;49;00m [32mtranslated[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32maction:[39;49;00m [33m#inspect[39;49;00m.$
	].$
$
	^[31maCustomMenu[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'graph model'[39;49;00m[34m stamp: 'nk 1/23/2004 14:35'![39;49;00m$
[32mhasModelYellowButtonMenuItems[39;49;00m$
	^[04m[32mPreferences[39;49;00m [32mcmdGesturesEnabled[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'inspecting'[39;49;00m[34m stamp: 'ar 9/27/2005 18:31'![39;49;00m$
[32mbasicInspect[39;49;00m$
	[37m"Create and schedule an Inspector in which the user can examine the [39;49;00m$
[37m	receiver's variables. This method should not be overriden."[39;49;00m$
	^[04m[32mToolSet[39;49;00m [32mbasicInspect:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'inspecting'[39;49;00m[34m stamp: 'md 1/18/2006 19:09'![39;49;00m$
[32minspect[39;49;00m$
	[37m"Create and schedule an Inspector in which the user can examine the receiver's variables."[39;49;00m$
	[04m[32mToolSet[39;49;00m [32minspect:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'inspecting'[39;49;00m[34m stamp: 'apb 7/14/2004 12:19'![39;49;00m$
[32minspectorClass[39;49;00m$
	[37m"Answer the class of the inspector to be used on the receiver.  Called by inspect; [39;49;00m$
[37m	use basicInspect to get a normal (less useful) type of inspector."[39;49;00m$
$
	^ [04m[32mInspector[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'locales'[39;49;00m[34m stamp: 'tak 8/4/2005 14:55'![39;49;00m$
[32mlocaleChanged[39;49;00m$
	[36mself[39;49;00m [32mshouldBeImplemented[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 5/7/1998 23:00'![39;49;00m$
[32mcodeStrippedOut:[39;49;00m [31mmessageString[39;49;00m$
	[37m"When a method is stripped out for external release, it is replaced by a method that calls this"[39;49;00m$
$
	[36mself[39;49;00m [32mhalt:[39;49;00m [33m'Code stripped out -- '[39;49;00m[32m,[39;49;00m [31mmessageString[39;49;00m[32m,[39;49;00m [33m'-- do not proceed.'[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 1/28/1999 17:31'![39;49;00m$
[32mcontentsChanged[39;49;00m$
	[36mself[39;49;00m [32mchanged:[39;49;00m [33m#contents[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'ar 3/18/2001 00:03'![39;49;00m$
[32mcurrentEvent[39;49;00m$
	[37m"Answer the current Morphic event.  This method never returns nil."[39;49;00m$
	^[04m[32mActiveEvent[39;49;00m [32mifNil:[39;49;00m[[36mself[39;49;00m [32mcurrentHand[39;49;00m [32mlastEvent[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'nk 9/1/2004 10:41'![39;49;00m$
[32mcurrentHand[39;49;00m$
	[37m"Return a usable HandMorph -- the one associated with the object's current environment.  This method will always return a hand, even if it has to conjure one up as a last resort.  If a particular hand is actually handling events at the moment (such as a remote hand or a ghost hand), it will be returned."[39;49;00m$
$
	^[04m[32mActiveHand[39;49;00m [32mifNil:[39;49;00m [ [36mself[39;49;00m [32mcurrentWorld[39;49;00m [32mprimaryHand[39;49;00m ][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 5/17/2001 12:08'![39;49;00m$
[32mcurrentVocabulary[39;49;00m$
	[37m"Answer the currently-prevailing default vocabulary."[39;49;00m$
$
	^ [04m[32mSmalltalk[39;49;00m [32misMorphic[39;49;00m [36mifTrue:[39;49;00m$
			[[04m[32mActiveWorld[39;49;00m [32mcurrentVocabulary[39;49;00m]$
		[36mifFalse:[39;49;00m$
			[[04m[32mVocabulary[39;49;00m [32mfullVocabulary[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'ar 3/18/2001 00:08'![39;49;00m$
[32mcurrentWorld[39;49;00m$
	[37m"Answer a morphic world that is the current UI focus.[39;49;00m$
[37m		If in an embedded world, it's that world.[39;49;00m$
[37m		If in a morphic project, it's that project's world.  [39;49;00m$
[37m		If in an mvc project, it is the topmost morphic-mvc-window's worldMorph. [39;49;00m$
[37m		If in an mvc project that has no morphic-mvc-windows, then it's just some existing worldmorph instance.[39;49;00m$
[37m		If in an mvc project in a Squeak that has NO WorldMorph instances, one is created.[39;49;00m$
[37m[39;49;00m$
[37m	This method will never return nil, it will always return its best effort at returning a relevant world morph, but if need be -- if there are no worlds anywhere, it will create a new one."[39;49;00m$
$
	|[31m aView aSubview [39;49;00m|$
	[04m[32mActiveWorld[39;49;00m [32mifNotNil:[39;49;00m[^[04m[32mActiveWorld[39;49;00m].$
	[04m[32mWorld[39;49;00m [32mifNotNil:[39;49;00m[^[04m[32mWorld[39;49;00m].$
	[31maView[39;49;00m _ [04m[32mScheduledControllers[39;49;00m [32mcontrollerSatisfying:[39;49;00m$
		[:[31mctrl[39;49;00m | ([31maSubview[39;49;00m _ [31mctrl[39;49;00m [32mview[39;49;00m [32mfirstSubView[39;49;00m) [32mnotNil[39;49;00m [32mand:[39;49;00m$
			[[31maSubview[39;49;00m [32mmodel[39;49;00m [32misMorph[39;49;00m [32mand:[39;49;00m [[31maSubview[39;49;00m [32mmodel[39;49;00m [32misWorldMorph[39;49;00m]]].$
	^[31maView[39;49;00m$
		[32mifNotNil:[39;49;00m$
			[[31maSubview[39;49;00m [32mmodel[39;49;00m]$
		[32mifNil:[39;49;00m$
			[[04m[32mMVCWiWPasteUpMorph[39;49;00m [32mnewWorldForProject:[39;49;00m [36mnil[39;49;00m].[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'jm 5/6/1998 22:35'![39;49;00m$
[32mflash[39;49;00m$
	[37m"Do nothing."[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 6/16/1998 15:07'![39;49;00m$
[32minstanceVariableValues[39;49;00m$
	[37m"Answer a collection whose elements are the values of those instance variables of the receiver which were added by the receiver's class"[39;49;00m$
	|[31m c [39;49;00m|$
	[31mc[39;49;00m _ [04m[32mOrderedCollection[39;49;00m [36mnew[39;49;00m.$
	[36mself[39;49;00m [32mclass[39;49;00m [32msuperclass[39;49;00m [32minstSize[39;49;00m [32m+[39;49;00m [34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mdo:[39;49;00m$
		[:[31mi[39;49;00m | [31mc[39;49;00m [32madd:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mi[39;49;00m)].$
	^ [31mc[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 3/20/2001 13:29'![39;49;00m$
[32misUniversalTiles[39;49;00m$
	[37m"Return true if I (my world) uses universal tiles.  This message can be called in places where the current World is not known, such as when writing out a project.  For more information about the project-writing subtlety addressed by this protocol, kindly contact Ted Kaehler."[39;49;00m$
$
	^ [04m[32mPreferences[39;49;00m [32muniversalTiles[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 10/24/2000 07:04'![39;49;00m$
[32mobjectRepresented[39;49;00m$
	[37m"most objects represent themselves; this provides a hook for aliases to grab on to"[39;49;00m$
$
	^ [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 5/22/2001 18:31'![39;49;00m$
[32mrefusesToAcceptCode[39;49;00m$
	[37m"Answer whether the receiver is a code-bearing instrument which at the moment refuses to allow its contents to be submitted"[39;49;00m$
$
	^ [36mfalse[39;49;00m$
	[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'jm 2/24/1999 12:40'![39;49;00m$
[32mscriptPerformer[39;49;00m$
$
	^ [36mself[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'macpal'[39;49;00m[34m stamp: 'sw 3/20/2001 13:40'![39;49;00m$
[32mslotInfo[39;49;00m$
	[37m"Answer a list of slot-information objects.  Initally only provides useful info for players"[39;49;00m$
$
	^ [04m[32mDictionary[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:28'![39;49;00m$
[32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
	[37m"Execute compiledMethod against the receiver with no args"[39;49;00m$
$
	[37m"<primitive: 189>"[39;49;00m [37m"uncomment once prim 189 is in VM"[39;49;00m$
	^ [36mself[39;49;00m [32mwithArgs:[39;49;00m [33m#([39;49;00m[33m)[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'di 3/26/1999 07:52'![39;49;00m$
[32mperform:[39;49;00m [31maSymbol[39;49;00m $
	[37m"Send the unary selector, aSymbol, to the receiver.[39;49;00m$
[37m	Fail if the number of arguments expected by the selector is not zero.[39;49;00m$
[37m	Primitive. Optional. See Object documentation whatIsAPrimitive."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 83>$
	^ [36mself[39;49;00m [32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mnew:[39;49;00m [34m0[39;49;00m)[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'st 11/5/2004 16:19'![39;49;00m$
[32mperform:[39;49;00m [31mselector[39;49;00m [32morSendTo:[39;49;00m [31motherTarget[39;49;00m$
	[37m"If I wish to intercept and handle selector myself, do it; else send it to otherTarget"[39;49;00m$
	^ ([36mself[39;49;00m [32mrespondsTo:[39;49;00m [31mselector[39;49;00m) [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m] [36mifFalse:[39;49;00m [[31motherTarget[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'di 3/26/1999 07:55'![39;49;00m$
[32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31margArray[39;49;00m $
	[37m"Send the selector, aSymbol, to the receiver with arguments in argArray.[39;49;00m$
[37m	Fail if the number of arguments expected by the selector [39;49;00m$
[37m	does not match the size of argArray.[39;49;00m$
[37m	Primitive. Optional. See Object documentation whatIsAPrimitive."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 84>$
	^ [36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31margArray[39;49;00m [32minSuperclass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'ar 4/25/2005 13:35'![39;49;00m$
[32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31margArray[39;49;00m [32minSuperclass:[39;49;00m [31mlookupClass[39;49;00m$
	[37m"NOTE:  This is just like perform:withArguments:, except that[39;49;00m$
[37m	the message lookup process begins, not with the receivers's class,[39;49;00m$
[37m	but with the supplied superclass instead.  It will fail if lookupClass[39;49;00m$
[37m	cannot be found among the receiver's superclasses.[39;49;00m$
[37m	Primitive. Essential. See Object documentation whatIsAPrimitive."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 100>$
	([31mselector[39;49;00m [32misSymbol[39;49;00m)$
		[36mifFalse:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'selector argument must be a Symbol'[39;49;00m].$
	([31mselector[39;49;00m [32mnumArgs[39;49;00m [32m=[39;49;00m [31margArray[39;49;00m [32msize[39;49;00m)$
		[36mifFalse:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'incorrect number of arguments'[39;49;00m].$
	([36mself[39;49;00m [32mclass[39;49;00m [32m==[39;49;00m [31mlookupClass[39;49;00m [32mor:[39;49;00m [[36mself[39;49;00m [32mclass[39;49;00m [32minheritsFrom:[39;49;00m [31mlookupClass[39;49;00m])$
		[36mifFalse:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'lookupClass is not in my inheritance chain'[39;49;00m].$
	[36mself[39;49;00m [32mprimitiveFailed[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'nk 4/11/2002 14:13'![39;49;00m$
[32mperform:[39;49;00m [31mselector[39;49;00m [32mwithEnoughArguments:[39;49;00m [31manArray[39;49;00m$
	[37m"Send the selector, aSymbol, to the receiver with arguments in argArray.[39;49;00m$
[37m	Only use enough arguments for the arity of the selector; supply nils for missing ones."[39;49;00m$
	|[31m numArgs args [39;49;00m|$
	[31mnumArgs[39;49;00m _ [31mselector[39;49;00m [32mnumArgs[39;49;00m.$
	[31manArray[39;49;00m [32msize[39;49;00m [32m==[39;49;00m [31mnumArgs[39;49;00m$
		[36mifTrue:[39;49;00m [ ^[36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31manArray[39;49;00m [32masArray[39;49;00m ].$
$
	[31margs[39;49;00m _ [04m[32mArray[39;49;00m [32mnew:[39;49;00m [31mnumArgs[39;49;00m.$
	[31margs[39;49;00m [32mreplaceFrom:[39;49;00m [34m1[39;49;00m$
		[32mto:[39;49;00m ([31manArray[39;49;00m [32msize[39;49;00m [32mmin:[39;49;00m [31margs[39;49;00m [32msize[39;49;00m)$
		[32mwith:[39;49;00m [31manArray[39;49;00m$
		[32mstartingAt:[39;49;00m [34m1[39;49;00m.$
$
	^ [36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31margs[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'di 3/26/1999 07:52'![39;49;00m$
[32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m $
	[37m"Send the selector, aSymbol, to the receiver with anObject as its argument.[39;49;00m$
[37m	Fail if the number of arguments expected by the selector is not one.[39;49;00m$
[37m	Primitive. Optional. See Object documentation whatIsAPrimitive."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 83>$
	^ [36mself[39;49;00m [32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m)[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'di 3/26/1999 07:52'![39;49;00m$
[32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwith:[39;49;00m [31mfirstObject[39;49;00m [32mwith:[39;49;00m [31msecondObject[39;49;00m $
	[37m"Send the selector, aSymbol, to the receiver with the given arguments.[39;49;00m$
[37m	Fail if the number of arguments expected by the selector is not two.[39;49;00m$
[37m	Primitive. Optional. See Object documentation whatIsAPrimitive."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 83>$
	^ [36mself[39;49;00m [32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31mfirstObject[39;49;00m [32mwith:[39;49;00m [31msecondObject[39;49;00m)[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'di 3/26/1999 07:51'![39;49;00m$
[32mperform:[39;49;00m [31maSymbol[39;49;00m [32mwith:[39;49;00m [31mfirstObject[39;49;00m [32mwith:[39;49;00m [31msecondObject[39;49;00m [32mwith:[39;49;00m [31mthirdObject[39;49;00m $
	[37m"Send the selector, aSymbol, to the receiver with the given arguments.[39;49;00m$
[37m	Fail if the number of arguments expected by the selector is not three.[39;49;00m$
[37m	Primitive. Optional. See Object documentation whatIsAPrimitive."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 83>$
	^ [36mself[39;49;00m [32mperform:[39;49;00m [31maSymbol[39;49;00m$
		[32mwithArguments:[39;49;00m ([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31mfirstObject[39;49;00m [32mwith:[39;49;00m [31msecondObject[39;49;00m [32mwith:[39;49;00m [31mthirdObject[39;49;00m)[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'NS 1/28/2004 11:19'![39;49;00m$
[32mwithArgs:[39;49;00m [31margArray[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
	[37m"Execute compiledMethod against the receiver and args in argArray"[39;49;00m$
$
	|[31m selector [39;49;00m|$
	<[34mprimitive:[39;49;00m 188>$
	[31mselector[39;49;00m _ [04m[32mSymbol[39;49;00m [36mnew[39;49;00m.$
	[36mself[39;49;00m [32mclass[39;49;00m [32maddSelectorSilently:[39;49;00m [31mselector[39;49;00m [32mwithMethod:[39;49;00m [31mcompiledMethod[39;49;00m.$
	^ [[36mself[39;49;00m [32mperform:[39;49;00m [31mselector[39;49;00m [32mwithArguments:[39;49;00m [31margArray[39;49;00m]$
		[32mensure:[39;49;00m [[36mself[39;49;00m [32mclass[39;49;00m [32mbasicRemoveSelector:[39;49;00m [31mselector[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:28'![39;49;00m$
[32mwith:[39;49;00m [31marg1[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
	[37m"Execute compiledMethod against the receiver and arg1"[39;49;00m$
$
	[37m"<primitive: 189>"[39;49;00m [37m"uncomment once prim 189 is in VM"[39;49;00m$
	^ [36mself[39;49;00m [32mwithArgs:[39;49;00m {[31marg1[39;49;00m} [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:28'![39;49;00m$
[32mwith:[39;49;00m [31marg1[39;49;00m [32mwith:[39;49;00m [31marg2[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
	[37m"Execute compiledMethod against the receiver and arg1 & arg2"[39;49;00m$
$
	[37m"<primitive: 189>"[39;49;00m [37m"uncomment once prim 189 is in VM"[39;49;00m$
	^ [36mself[39;49;00m [32mwithArgs:[39;49;00m {[31marg1[39;49;00m. [31marg2[39;49;00m} [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:28'![39;49;00m$
[32mwith:[39;49;00m [31marg1[39;49;00m [32mwith:[39;49;00m [31marg2[39;49;00m [32mwith:[39;49;00m [31marg3[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
	[37m"Execute compiledMethod against the receiver and arg1, arg2, & arg3"[39;49;00m$
$
	[37m"<primitive: 189>"[39;49;00m [37m"uncomment once prim 189 is in VM"[39;49;00m$
	^ [36mself[39;49;00m [32mwithArgs:[39;49;00m {[31marg1[39;49;00m. [31marg2[39;49;00m. [31marg3[39;49;00m} [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'message handling'[39;49;00m[34m stamp: 'md 1/20/2006 16:28'![39;49;00m$
[32mwith:[39;49;00m [31marg1[39;49;00m [32mwith:[39;49;00m [31marg2[39;49;00m [32mwith:[39;49;00m [31marg3[39;49;00m [32mwith:[39;49;00m [31marg4[39;49;00m [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m$
	[37m"Execute compiledMethod against the receiver and arg1, arg2, arg3, & arg4"[39;49;00m$
$
	[37m"<primitive: 189>"[39;49;00m [37m"uncomment once prim 189 is in VM"[39;49;00m$
	^ [36mself[39;49;00m [32mwithArgs:[39;49;00m {[31marg1[39;49;00m. [31marg2[39;49;00m. [31marg3[39;49;00m. [31marg4[39;49;00m} [32mexecuteMethod:[39;49;00m [31mcompiledMethod[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 4/8/1999 12:46'![39;49;00m$
[32mcomeFullyUpOnReload:[39;49;00m [31msmartRefStream[39;49;00m$
	[37m"Normally this read-in object is exactly what we want to store. 7/26/96 tk"[39;49;00m$
$
	^ [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'RAA 12/20/2000 16:51'![39;49;00m$
[32mconvertToCurrentVersion:[39;49;00m [31mvarDict[39;49;00m [32mrefStream:[39;49;00m [31msmartRefStrm[39;49;00m$
$
	[37m"subclasses should implement if they wish to convert old instances to modern ones"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 11/29/2004 15:04'![39;49;00m$
[32mfixUponLoad:[39;49;00m [31maProject[39;49;00m [32mseg:[39;49;00m [31manImageSegment[39;49;00m$
	[37m"change the object due to conventions that have changed on[39;49;00m$
[37mthe project level.  (sent to all objects in the incoming project).[39;49;00m$
[37mSpecific classes should reimplement this."[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'RAA 1/10/2001 14:02'![39;49;00m$
[32mindexIfCompact[39;49;00m$
$
	^[34m0[39;49;00m		[37m"helps avoid a #respondsTo: in publishing"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 2/24/1999 11:08'![39;49;00m$
[32mobjectForDataStream:[39;49;00m [31mrefStrm[39;49;00m$
    [37m"Return an object to store on an external data stream."[39;49;00m$
$
    ^ [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 4/8/1999 12:05'![39;49;00m$
[32mreadDataFrom:[39;49;00m [31maDataStream[39;49;00m [32msize:[39;49;00m [31mvarsOnDisk[39;49;00m$
	[37m"Fill in the fields of self based on the contents of aDataStream.  Return self.[39;49;00m$
[37m	 Read in the instance-variables written by Object>>storeDataOn:.[39;49;00m$
[37m	 NOTE: This method must send beginReference: before reading any objects from aDataStream that might reference it.[39;49;00m$
[37m	 Allow aDataStream to have fewer inst vars.  See SmartRefStream."[39;49;00m$
	|[31m cntInstVars cntIndexedVars [39;49;00m|$
$
	[31mcntInstVars[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m.$
	[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m$
		[36mifTrue:[39;49;00m [[31mcntIndexedVars[39;49;00m _ [31mvarsOnDisk[39;49;00m [32m-[39;49;00m [31mcntInstVars[39;49;00m.$
				[31mcntIndexedVars[39;49;00m [32m<[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m [$
					[36mself[39;49;00m [32merror:[39;49;00m [33m'Class has changed too much.  Define a convertxxx method'[39;49;00m]]$
		[36mifFalse:[39;49;00m [[31mcntIndexedVars[39;49;00m _ [34m0[39;49;00m.$
				[31mcntInstVars[39;49;00m _ [31mvarsOnDisk[39;49;00m]. 	[37m"OK if fewer than now"[39;49;00m$
$
	[31maDataStream[39;49;00m [32mbeginReference:[39;49;00m [36mself[39;49;00m.$
	[34m1[39;49;00m [32mto:[39;49;00m [31mcntInstVars[39;49;00m [32mdo:[39;49;00m$
		[:[31mi[39;49;00m | [36mself[39;49;00m [32minstVarAt:[39;49;00m [31mi[39;49;00m [32mput:[39;49;00m [31maDataStream[39;49;00m [32mnext[39;49;00m].$
	[34m1[39;49;00m [32mto:[39;49;00m [31mcntIndexedVars[39;49;00m [32mdo:[39;49;00m$
		[:[31mi[39;49;00m | [36mself[39;49;00m [32mbasicAt:[39;49;00m [31mi[39;49;00m [32mput:[39;49;00m [31maDataStream[39;49;00m [32mnext[39;49;00m].$
	[37m"Total number read MUST be equal to varsOnDisk!!"[39;49;00m$
	^ [36mself[39;49;00m	[37m"If we ever return something other than self, fix calls [39;49;00m$
[37m			on (super readDataFrom: aDataStream size: anInteger)"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'CdG 10/17/2005 20:32'![39;49;00m$
[32msaveOnFile[39;49;00m$
	[37m"Ask the user for a filename and save myself on a SmartReferenceStream file.  Writes out the version and class structure.  The file is fileIn-able.  Does not file out the class of the object.  tk 6/26/97 13:48"[39;49;00m$
$
	|[31m aFileName fileStream [39;49;00m|$
	[31maFileName[39;49;00m := [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32masFileName[39;49;00m.	[37m"do better?"[39;49;00m$
	[31maFileName[39;49;00m := [04m[32mUIManager[39;49;00m [32mdefault[39;49;00m $
				[32mrequest:[39;49;00m [33m'File name?'[39;49;00m [32mtranslated[39;49;00m [32minitialAnswer:[39;49;00m [31maFileName[39;49;00m.$
	[31maFileName[39;49;00m [32msize[39;49;00m [32m==[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m [^ [04m[32mBeeper[39;49;00m [32mbeep[39;49;00m].$
$
	[31mfileStream[39;49;00m := [04m[32mFileStream[39;49;00m [32mnewFileNamed:[39;49;00m [31maFileName[39;49;00m [32masFileName[39;49;00m.$
	[31mfileStream[39;49;00m [32mfileOutClass:[39;49;00m [36mnil[39;49;00m [32mandObject:[39;49;00m [36mself[39;49;00m.[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 8/9/2001 15:40'![39;49;00m$
[32mstoreDataOn:[39;49;00m [31maDataStream[39;49;00m$
	[37m"Store myself on a DataStream.  Answer self.  This is a low-level DataStream/ReferenceStream method. See also objectToStoreOnDataStream.  NOTE: This method must send 'aDataStream beginInstance:size:' and then (nextPut:/nextPutWeak:) its subobjects.  readDataFrom:size: reads back what we write here."[39;49;00m$
	|[31m cntInstVars cntIndexedVars [39;49;00m|$
$
	[31mcntInstVars[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m.$
	[31mcntIndexedVars[39;49;00m _ [36mself[39;49;00m [32mbasicSize[39;49;00m.$
	[31maDataStream[39;49;00m$
		[32mbeginInstance:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m$
		[32msize:[39;49;00m [31mcntInstVars[39;49;00m [32m+[39;49;00m [31mcntIndexedVars[39;49;00m.$
	[34m1[39;49;00m [32mto:[39;49;00m [31mcntInstVars[39;49;00m [32mdo:[39;49;00m$
		[:[31mi[39;49;00m | [31maDataStream[39;49;00m [32mnextPut:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mi[39;49;00m)].$
$
	[37m"Write fields of a variable length object.  When writing to a dummy [39;49;00m$
[37m		stream, don't bother to write the bytes"[39;49;00m$
	(([31maDataStream[39;49;00m [32mbyteStream[39;49;00m [32mclass[39;49;00m [32m==[39;49;00m [04m[32mDummyStream[39;49;00m) [32mand:[39;49;00m [[36mself[39;49;00m [32mclass[39;49;00m [32misBits[39;49;00m]) [36mifFalse:[39;49;00m [$
		[34m1[39;49;00m [32mto:[39;49;00m [31mcntIndexedVars[39;49;00m [32mdo:[39;49;00m$
			[:[31mi[39;49;00m | [31maDataStream[39;49;00m [32mnextPut:[39;49;00m ([36mself[39;49;00m [32mbasicAt:[39;49;00m [31mi[39;49;00m)]].$
[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'parts bin'[39;49;00m[34m stamp: 'sw 10/24/2001 16:34'![39;49;00m$
[32mdescriptionForPartsBin[39;49;00m$
	[37m"If the receiver is a member of a class that would like to be represented in a parts bin, answer the name by which it should be known, and a documentation string to be provided, for example, as balloon help.  When the 'nativitySelector' is sent to the 'globalReceiver', it is expected that some kind of Morph will result.  The parameters used in the implementation below are for documentation purposes only!!"[39;49;00m$
$
	^ [04m[32mDescriptionForPartsBin[39;49;00m$
		[32mformalName:[39;49;00m [33m'PutFormalNameHere'[39;49;00m$
		[32mcategoryList:[39;49;00m [33m#([39;49;00m[33mPutACategoryHere[39;49;00m [33mMaybePutAnotherCategoryHere[39;49;00m[33m)[39;49;00m$
		[32mdocumentation:[39;49;00m [33m'Put the balloon help here'[39;49;00m$
		[32mglobalReceiverSymbol:[39;49;00m [33m#PutAGlobalHere[39;49;00m$
		[32mnativitySelector:[39;49;00m [33m#PutASelectorHere[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'di 6/20/97 08:57'![39;49;00m$
[32mfullPrintString[39;49;00m$
	[37m"Answer a String whose characters are a description of the receiver."[39;49;00m$
$
	^ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [:[31ms[39;49;00m | [36mself[39;49;00m [32mprintOn:[39;49;00m [31ms[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m![39;49;00m$
[32misLiteral[39;49;00m$
	[37m"Answer whether the receiver has a literal text form recognized by the [39;49;00m$
[37m	compiler."[39;49;00m$
$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sma 6/1/2000 09:28'![39;49;00m$
[32mlongPrintOn:[39;49;00m [31maStream[39;49;00m$
	[37m"Append to the argument, aStream, the names and values of all [39;49;00m$
[37m	of the receiver's instance variables."[39;49;00m$
$
	[36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mdoWithIndex:[39;49;00m$
		[:[31mtitle[39;49;00m :[31mindex[39;49;00m |$
		[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [31mtitle[39;49;00m;$
		 [32mnextPut:[39;49;00m [33m$:[39;49;00m;$
		 [32mspace[39;49;00m;$
		 [32mtab[39;49;00m;$
		 [32mprint:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m);$
		 [32mcr[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'tk 10/19/2001 11:18'![39;49;00m$
[32mlongPrintOn:[39;49;00m [31maStream[39;49;00m [32mlimitedTo:[39;49;00m [31msizeLimit[39;49;00m [32mindent:[39;49;00m [31mindent[39;49;00m$
	[37m"Append to the argument, aStream, the names and values of all of the receiver's instance variables.  Limit is the length limit for each inst var."[39;49;00m$
$
	[36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mdoWithIndex:[39;49;00m$
		[:[31mtitle[39;49;00m :[31mindex[39;49;00m |$
		[31mindent[39;49;00m [36mtimesRepeat:[39;49;00m [[31maStream[39;49;00m [32mtab[39;49;00m].$
		[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [31mtitle[39;49;00m;$
		 [32mnextPut:[39;49;00m [33m$:[39;49;00m;$
		 [32mspace[39;49;00m;$
		 [32mtab[39;49;00m;$
		 [32mnextPutAll:[39;49;00m $
			(([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mindex[39;49;00m) [32mprintStringLimitedTo:[39;49;00m ([31msizeLimit[39;49;00m [32m-[39;49;00m[34m3[39;49;00m [32m-[39;49;00m[31mtitle[39;49;00m [32msize[39;49;00m [32mmax:[39;49;00m [34m1[39;49;00m));$
		 [32mcr[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'tk 10/16/2001 19:41'![39;49;00m$
[32mlongPrintString[39;49;00m$
	[37m"Answer a String whose characters are a description of the receiver."[39;49;00m$
	$
	|[31m str [39;49;00m|$
	[31mstr[39;49;00m _ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [:[31maStream[39;49;00m | [36mself[39;49;00m [32mlongPrintOn:[39;49;00m [31maStream[39;49;00m].$
	[37m"Objects without inst vars should return something"[39;49;00m$
	^ [31mstr[39;49;00m [32misEmpty[39;49;00m [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [04m[32mString[39;49;00m [32mcr[39;49;00m] [36mifFalse:[39;49;00m [[31mstr[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'BG 11/7/2004 13:39'![39;49;00m$
[32mlongPrintStringLimitedTo:[39;49;00m [31maLimitValue[39;49;00m$
	[37m"Answer a String whose characters are a description of the receiver."[39;49;00m$
	$
	|[31m str [39;49;00m|$
	[31mstr[39;49;00m _ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [:[31maStream[39;49;00m | [36mself[39;49;00m [32mlongPrintOn:[39;49;00m [31maStream[39;49;00m [32mlimitedTo:[39;49;00m [31maLimitValue[39;49;00m [32mindent:[39;49;00m [34m0[39;49;00m].$
	[37m"Objects without inst vars should return something"[39;49;00m$
	^ [31mstr[39;49;00m [32misEmpty[39;49;00m [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [04m[32mString[39;49;00m [32mcr[39;49;00m] [36mifFalse:[39;49;00m [[31mstr[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sw 3/7/2001 13:14'![39;49;00m$
[32mnominallyUnsent:[39;49;00m [31maSelectorSymbol[39;49;00m$
	[37m"From within the body of a method which is not formally sent within the system, but which you intend to have remain in the system (for potential manual invocation, or for documentation, or perhaps because it's sent by commented-out-code that you anticipate uncommenting out someday, send this message, with the selector itself as the argument.[39;49;00m$
[37m[39;49;00m$
[37mThis will serve two purposes:[39;49;00m$
[37m[39;49;00m$
[37m	(1)  The method will not be returned by searches for unsent selectors (because it, in a manner of speaking, sends itself).[39;49;00m$
[37m	(2)	You can locate all such methods by browsing senders of #nominallyUnsent:"[39;49;00m$
$
	[36mfalse[39;49;00m [36mifTrue:[39;49;00m [[36mself[39;49;00m [32mflag:[39;49;00m [33m#nominallyUnsent:[39;49;00m]    [37m"So that this method itself will appear to be sent"[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sma 6/1/2000 09:31'![39;49;00m$
[32mprintOn:[39;49;00m [31maStream[39;49;00m$
	[37m"Append to the argument, aStream, a sequence of characters that  [39;49;00m$
[37m	identifies the receiver."[39;49;00m$
$
	|[31m title [39;49;00m|$
	[31mtitle[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m.$
	[31maStream[39;49;00m$
		[32mnextPutAll:[39;49;00m ([31mtitle[39;49;00m [32mfirst[39;49;00m [32misVowel[39;49;00m [36mifTrue:[39;49;00m [[33m'an '[39;49;00m] [36mifFalse:[39;49;00m [[33m'a '[39;49;00m]);$
		[32mnextPutAll:[39;49;00m [31mtitle[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sma 6/1/2000 09:22'![39;49;00m$
[32mprintString[39;49;00m$
	[37m"Answer a String whose characters are a description of the receiver. [39;49;00m$
[37m	If you want to print without a character limit, use fullPrintString."[39;49;00m$
$
	^ [36mself[39;49;00m [32mprintStringLimitedTo:[39;49;00m [34m50000[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'tk 5/7/1999 16:20'![39;49;00m$
[32mprintStringLimitedTo:[39;49;00m [31mlimit[39;49;00m$
	[37m"Answer a String whose characters are a description of the receiver.[39;49;00m$
[37m	If you want to print without a character limit, use fullPrintString."[39;49;00m$
	|[31m limitedString [39;49;00m|$
	[31mlimitedString[39;49;00m _ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [:[31ms[39;49;00m | [36mself[39;49;00m [32mprintOn:[39;49;00m [31ms[39;49;00m] [32mlimitedTo:[39;49;00m [31mlimit[39;49;00m.$
	[31mlimitedString[39;49;00m [32msize[39;49;00m [32m<[39;49;00m [31mlimit[39;49;00m [36mifTrue:[39;49;00m [^ [31mlimitedString[39;49;00m].$
	^ [31mlimitedString[39;49;00m [32m,[39;49;00m [33m'...etc...'[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'MPW 1/1/1901 00:30'![39;49;00m$
[32mpropertyList[39;49;00m$
	[37m"Answer a String whose characters are a property-list description of the receiver."[39;49;00m$
$
	^ [04m[32mPropertyListEncoder[39;49;00m [32mprocess:[39;49;00m[36mself[39;49;00m.$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sw 10/17/2000 11:16'![39;49;00m$
[32mreportableSize[39;49;00m$
	[37m"Answer a string that reports the size of the receiver -- useful for showing in a list view, for example"[39;49;00m$
$
	^ ([36mself[39;49;00m [32mbasicSize[39;49;00m [32m+[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m) [32mprintString[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m![39;49;00m$
[32mstoreOn:[39;49;00m [31maStream[39;49;00m $
	[37m"Append to the argument aStream a sequence of characters that is an [39;49;00m$
[37m	expression whose evaluation creates an object similar to the receiver."[39;49;00m$
$
	[31maStream[39;49;00m [32mnextPut:[39;49;00m [33m$([39;49;00m.$
	[36mself[39;49;00m [32mclass[39;49;00m [32misVariable[39;49;00m$
		[36mifTrue:[39;49;00m [[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [33m'('[39;49;00m[32m,[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m[32m,[39;49;00m [33m' basicNew: '[39;49;00m;$
					[32mstore:[39;49;00m [36mself[39;49;00m [32mbasicSize[39;49;00m;$
					[32mnextPutAll:[39;49;00m [33m') '[39;49;00m]$
		[36mifFalse:[39;49;00m [[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m[32m,[39;49;00m [33m' basicNew'[39;49;00m].$
	[34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mdo:[39;49;00m$
		[:[31mi[39;49;00m |$
		[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [33m' instVarAt: '[39;49;00m;$
			[32mstore:[39;49;00m [31mi[39;49;00m;$
			[32mnextPutAll:[39;49;00m [33m' put: '[39;49;00m;$
			[32mstore:[39;49;00m ([36mself[39;49;00m [32minstVarAt:[39;49;00m [31mi[39;49;00m);$
			[32mnextPut:[39;49;00m [33m$;[39;49;00m].$
	[34m1[39;49;00m [32mto:[39;49;00m [36mself[39;49;00m [32mbasicSize[39;49;00m [32mdo:[39;49;00m$
		[:[31mi[39;49;00m |$
		[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [33m' basicAt: '[39;49;00m;$
			[32mstore:[39;49;00m [31mi[39;49;00m;$
			[32mnextPutAll:[39;49;00m [33m' put: '[39;49;00m;$
			[32mstore:[39;49;00m ([36mself[39;49;00m [32mbasicAt:[39;49;00m [31mi[39;49;00m);$
			[32mnextPut:[39;49;00m [33m$;[39;49;00m].$
	[31maStream[39;49;00m [32mnextPutAll:[39;49;00m [33m' yourself)'[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'di 6/20/97 09:12'![39;49;00m$
[32mstoreString[39;49;00m$
	[37m"Answer a String representation of the receiver from which the receiver [39;49;00m$
[37m	can be reconstructed."[39;49;00m$
$
	^ [04m[32mString[39;49;00m [32mstreamContents:[39;49;00m [:[31ms[39;49;00m | [36mself[39;49;00m [32mstoreOn:[39;49;00m [31ms[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m stamp: 'sw 5/2/1998 13:55'![39;49;00m$
[32mstringForReadout[39;49;00m$
	^ [36mself[39;49;00m [32mstringRepresentation[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'printing'[39;49;00m[34m![39;49;00m$
[32mstringRepresentation[39;49;00m$
	[37m"Answer a string that represents the receiver.  For most objects this is simply its printString, but for strings themselves, it's themselves.  6/12/96 sw"[39;49;00m$
$
	^ [36mself[39;49;00m [32mprintString[39;49;00m [34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'ar 3/17/2001 20:11'![39;49;00m$
[32madaptedToWorld:[39;49;00m [31maWorld[39;49;00m$
	[37m"If I refer to a world or a hand, return the corresponding items in the new world."[39;49;00m$
	^[36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'sw 3/10/2000 13:57'![39;49;00m$
[32mdefaultFloatPrecisionFor:[39;49;00m [31maGetSelector[39;49;00m$
	[37m"Answer a number indicating the default float precision to be used in a numeric readout for which the receiver is the model."[39;49;00m$
$
	^ [34m1[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 3/9/2001 17:08'![39;49;00m$
[32mevaluateUnloggedForSelf:[39;49;00m [31maCodeString[39;49;00m$
$
	^[04m[32mCompiler[39;49;00m [32mevaluate:[39;49;00m$
		[31maCodeString[39;49;00m$
		[32mfor:[39;49;00m [36mself[39;49;00m$
		[32mlogged:[39;49;00m [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'yo 12/25/2003 16:43'![39;49;00m$
[32mmethodInterfacesForCategory:[39;49;00m [31maCategorySymbol[39;49;00m [32minVocabulary:[39;49;00m [31maVocabulary[39;49;00m [32mlimitClass:[39;49;00m [31maLimitClass[39;49;00m$
	[37m"Return a list of methodInterfaces for the receiver in the given category, given a vocabulary.  aCategorySymbol is the inherent category symbol, not necessarily the wording as expressed in the vocabulary."[39;49;00m$
$
	|[31m categorySymbol [39;49;00m|$
	[31mcategorySymbol[39;49;00m _ [31maCategorySymbol[39;49;00m [32masSymbol[39;49;00m.$
$
	([31mcategorySymbol[39;49;00m [32m==[39;49;00m [04m[32mScriptingSystem[39;49;00m [32mnameForInstanceVariablesCategory[39;49;00m) [36mifTrue:[39;49;00m [$
		[37m"user-defined instance variables"[39;49;00m$
		^ [36mself[39;49;00m [32mmethodInterfacesForInstanceVariablesCategoryIn:[39;49;00m [31maVocabulary[39;49;00m].$
	([31mcategorySymbol[39;49;00m [32m==[39;49;00m [04m[32mScriptingSystem[39;49;00m [32mnameForScriptsCategory[39;49;00m) [36mifTrue:[39;49;00m [$
		[37m"user-defined scripts"[39;49;00m$
		^ [36mself[39;49;00m [32mmethodInterfacesForScriptsCategoryIn:[39;49;00m [31maVocabulary[39;49;00m].$
	[37m"all others"[39;49;00m$
	^ [36mself[39;49;00m [32musableMethodInterfacesIn:[39;49;00m ([31maVocabulary[39;49;00m [32mmethodInterfacesInCategory:[39;49;00m [31mcategorySymbol[39;49;00m$
		[32mforInstance:[39;49;00m [36mself[39;49;00m$
		[32mofClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m$
		[32mlimitClass:[39;49;00m [31maLimitClass[39;49;00m)$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'sw 8/3/2001 13:54'![39;49;00m$
[32mmethodInterfacesForInstanceVariablesCategoryIn:[39;49;00m [31maVocabulary[39;49;00m$
	[37m"Return a collection of methodInterfaces for the instance-variables category.  The vocabulary parameter, at present anyway, is not used.  And for non-players, the method is at present vacuous in any case"[39;49;00m$
$
	^  [04m[32mOrderedCollection[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'sw 8/3/2001 13:53'![39;49;00m$
[32mmethodInterfacesForScriptsCategoryIn:[39;49;00m [31maVocabulary[39;49;00m$
	[37m"Answer a list of method interfaces for the category #scripts, as seen in a viewer or other tool.  The vocabulary argument is not presently used.  Also, at present, only Players really do anyting interesting here."[39;49;00m$
$
	^ [04m[32mOrderedCollection[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 2/16/2001 19:37'![39;49;00m$
[32mselfWrittenAsIll[39;49;00m$
$
	^[36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 2/16/2001 19:38'![39;49;00m$
[32mselfWrittenAsIm[39;49;00m$
$
	^[36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 2/16/2001 19:37'![39;49;00m$
[32mselfWrittenAsMe[39;49;00m$
$
	^[36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 2/16/2001 19:37'![39;49;00m$
[32mselfWrittenAsMy[39;49;00m$
$
	^[36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripting'[39;49;00m[34m stamp: 'RAA 2/16/2001 19:38'![39;49;00m$
[32mselfWrittenAsThis[39;49;00m$
$
	^[36mself[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripts-kernel'[39;49;00m[34m stamp: 'nk 10/14/2004 10:55'![39;49;00m$
[32muniversalTilesForGetterOf:[39;49;00m [31maMethodInterface[39;49;00m$
	[37m"Return universal tiles for a getter on the given method interface."[39;49;00m$
$
	|[31m ms argTile argArray itsSelector [39;49;00m|$
	[31mitsSelector[39;49;00m _ [31maMethodInterface[39;49;00m [32mselector[39;49;00m.$
	[31margArray[39;49;00m _ [33m#([39;49;00m[33m)[39;49;00m.$
$
	[37m"Four gratuituous special cases..."[39;49;00m$
$
	([31mitsSelector[39;49;00m [32m==[39;49;00m [33m#color:sees:[39;49;00m) [36mifTrue:[39;49;00m$
		[[31margTile[39;49;00m _ [04m[32mScriptingSystem[39;49;00m [32mtileForArgType:[39;49;00m [33m#Color[39;49;00m.$
		[31margArray[39;49;00m _ [04m[32mArray[39;49;00m [32mwith:[39;49;00m [31margTile[39;49;00m [32mcolorSwatch[39;49;00m [32mcolor[39;49;00m [32mwith:[39;49;00m [31margTile[39;49;00m [32mcolorSwatch[39;49;00m [32mcolor[39;49;00m [32mcopy[39;49;00m].$
$
	[31mitsSelector[39;49;00m [32m==[39;49;00m [33m#seesColor:[39;49;00m [36mifTrue:[39;49;00m$
		[[31margTile[39;49;00m _ [04m[32mScriptingSystem[39;49;00m [32mtileForArgType:[39;49;00m [33m#Color[39;49;00m.$
		[31margArray[39;49;00m _  [04m[32mArray[39;49;00m [32mwith:[39;49;00m [31margTile[39;49;00m [32mcolorSwatch[39;49;00m [32mcolor[39;49;00m].$
$
	([33m#([39;49;00m[33mtouchesA:[39;49;00m [33moverlaps:[39;49;00m [33moverlapsAny:[39;49;00m[33m)[39;49;00m [32mincludes:[39;49;00m [31mitsSelector[39;49;00m) [36mifTrue:[39;49;00m$
		[[31margTile[39;49;00m _ [04m[32mScriptingSystem[39;49;00m [32mtileForArgType:[39;49;00m [33m#Player[39;49;00m.$
		[31margArray[39;49;00m _ [04m[32mArray[39;49;00m [32mwith:[39;49;00m [31margTile[39;49;00m [32mactualObject[39;49;00m].$
$
	[31mms[39;49;00m _ [04m[32mMessageSend[39;49;00m [32mreceiver:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [31mitsSelector[39;49;00m [32marguments:[39;49;00m [31margArray[39;49;00m.$
	^ [31mms[39;49;00m [32masTilesIn:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mglobalNames:[39;49;00m ([36mself[39;49;00m [32mclass[39;49;00m [32mofficialClass[39;49;00m [32m~~[39;49;00m [04m[32mCardPlayer[39;49;00m)$
			[37m"For CardPlayers, use 'self'.  For others, name it, and use its name."[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'scripts-kernel'[39;49;00m[34m stamp: 'tk 9/28/2001 13:30'![39;49;00m$
[32muniversalTilesForInterface:[39;49;00m [31maMethodInterface[39;49;00m$
	[37m"Return universal tiles for the given method interface.  Record who self is."[39;49;00m$
$
	|[31m ms argTile itsSelector aType argList [39;49;00m|$
	[31mitsSelector[39;49;00m _ [31maMethodInterface[39;49;00m [32mselector[39;49;00m.$
	[31margList[39;49;00m _ [04m[32mOrderedCollection[39;49;00m [36mnew[39;49;00m.$
	[31maMethodInterface[39;49;00m [32margumentVariables[39;49;00m [32mdoWithIndex:[39;49;00m$
		[:[31manArgumentVariable[39;49;00m :[31manIndex[39;49;00m | $
			[31margTile[39;49;00m _ [04m[32mScriptingSystem[39;49;00m [32mtileForArgType:[39;49;00m ([31maType[39;49;00m _ [31maMethodInterface[39;49;00m [32mtypeForArgumentNumber:[39;49;00m [31manIndex[39;49;00m).$
			[31margList[39;49;00m [32madd:[39;49;00m ([31maType[39;49;00m [32m==[39;49;00m [33m#Player[39;49;00m $
				[36mifTrue:[39;49;00m [[31margTile[39;49;00m [32mactualObject[39;49;00m]$
				[36mifFalse:[39;49;00m [[31margTile[39;49;00m [32mliteral[39;49;00m]).	[37m"default value for each type"[39;49;00m].$
$
	[31mms[39;49;00m _ [04m[32mMessageSend[39;49;00m [32mreceiver:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [31mitsSelector[39;49;00m [32marguments:[39;49;00m [31margList[39;49;00m [32masArray[39;49;00m.$
	^ [31mms[39;49;00m [32masTilesIn:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mglobalNames:[39;49;00m ([36mself[39;49;00m [32mclass[39;49;00m [32mofficialClass[39;49;00m [32m~~[39;49;00m [04m[32mCardPlayer[39;49;00m)$
			[37m"For CardPlayers, use 'self'.  For others, name it, and use its name."[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'self evaluating'[39;49;00m[34m stamp: 'sd 7/31/2005 21:47'![39;49;00m$
[32misSelfEvaluating[39;49;00m$
	^ [36mself[39;49;00m [32misLiteral[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m![39;49;00m$
[32masOop[39;49;00m$
	[37m"Primitive. Answer a SmallInteger whose value is half of the receiver's [39;49;00m$
[37m	object pointer (interpreting object pointers as 16-bit signed quantities). [39;49;00m$
[37m	Fail if the receiver is a SmallInteger. Essential. See Object documentation [39;49;00m$
[37m	whatIsAPrimitive."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 75>$
	[36mself[39;49;00m [32mprimitiveFailed[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'di 1/9/1999 15:19'![39;49;00m$
[32mbecomeForward:[39;49;00m [31motherObject[39;49;00m $
	[37m"Primitive. All variables in the entire system that used to point[39;49;00m$
[37m	to the receiver now point to the argument.[39;49;00m$
[37m	Fails if either argument is a SmallInteger."[39;49;00m$
$
	([04m[32mArray[39;49;00m [32mwith:[39;49;00m [36mself[39;49;00m)$
		[32melementsForwardIdentityTo:[39;49;00m$
			([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31motherObject[39;49;00m)[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'zz 3/3/2004 23:53'![39;49;00m$
[32mbecomeForward:[39;49;00m [31motherObject[39;49;00m [32mcopyHash:[39;49;00m [31mcopyHash[39;49;00m$
	[37m"Primitive. All variables in the entire system that used to point to the receiver now point to the argument.[39;49;00m$
[37m	If copyHash is true, the argument's identity hash bits will be set to those of the receiver.[39;49;00m$
[37m	Fails if either argument is a SmallInteger."[39;49;00m$
$
	([04m[32mArray[39;49;00m [32mwith:[39;49;00m [36mself[39;49;00m)$
		[32melementsForwardIdentityTo:[39;49;00m$
			([04m[32mArray[39;49;00m [32mwith:[39;49;00m [31motherObject[39;49;00m)$
				[32mcopyHash:[39;49;00m [31mcopyHash[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'sw 10/16/2000 10:59'![39;49;00m$
[32mclassName[39;49;00m$
	[37m"Answer a string characterizing the receiver's class, for use in list views for example"[39;49;00m$
$
	^ [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32masString[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'sw 10/16/2000 11:04'![39;49;00m$
[32mcreationStamp[39;49;00m$
	[37m"Answer a string which reports the creation particulars of the receiver.  Intended perhaps for list views, but this is presently a feature not easily accessible"[39;49;00m$
$
	^ [33m'<no creation stamp>'[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m![39;49;00m$
[32minstVarAt:[39;49;00m [31mindex[39;49;00m $
	[37m"Primitive. Answer a fixed variable in an object. The numbering of the [39;49;00m$
[37m	variables corresponds to the named instance variables. Fail if the index [39;49;00m$
[37m	is not an Integer or is not the index of a fixed variable. Essential. See [39;49;00m$
[37m	Object documentation whatIsAPrimitive."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 73>$
	[37m"Access beyond fixed variables."[39;49;00m$
	^[36mself[39;49;00m [32mbasicAt:[39;49;00m [31mindex[39;49;00m [32m-[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m		[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m![39;49;00m$
[32minstVarAt:[39;49;00m [31manInteger[39;49;00m [32mput:[39;49;00m [31manObject[39;49;00m $
	[37m"Primitive. Store a value into a fixed variable in the receiver. The [39;49;00m$
[37m	numbering of the variables corresponds to the named instance variables. [39;49;00m$
[37m	Fail if the index is not an Integer or is not the index of a fixed variable. [39;49;00m$
[37m	Answer the value stored as the result. Using this message violates the [39;49;00m$
[37m	principle that each object has sovereign control over the storing of [39;49;00m$
[37m	values into its instance variables. Essential. See Object documentation [39;49;00m$
[37m	whatIsAPrimitive."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 74>$
	[37m"Access beyond fixed fields"[39;49;00m$
	^[36mself[39;49;00m [32mbasicAt:[39;49;00m [31manInteger[39;49;00m [32m-[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstSize[39;49;00m [32mput:[39;49;00m [31manObject[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'sw 10/16/2000 11:09'![39;49;00m$
[32minstVarNamed:[39;49;00m [31maString[39;49;00m$
	[37m"Return the value of the instance variable in me with that name.  Slow and unclean, but very useful. "[39;49;00m$
$
	^ [36mself[39;49;00m [32minstVarAt:[39;49;00m ([36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mindexOf:[39;49;00m [31maString[39;49;00m [32masString[39;49;00m)$
$
$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'sw 10/16/2000 11:10'![39;49;00m$
[32minstVarNamed:[39;49;00m [31maString[39;49;00m [32mput:[39;49;00m [31maValue[39;49;00m$
	[37m"Store into the value of the instance variable in me of that name.  Slow and unclean, but very useful. "[39;49;00m$
$
	^ [36mself[39;49;00m [32minstVarAt:[39;49;00m ([36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32mindexOf:[39;49;00m [31maString[39;49;00m [32masString[39;49;00m) [32mput:[39;49;00m [31maValue[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'sw 10/17/2000 11:12'![39;49;00m$
[32moopString[39;49;00m$
	[37m"Answer a string that represents the oop of the receiver"[39;49;00m$
$
	^ [36mself[39;49;00m [32masOop[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'ar 3/2/2001 01:34'![39;49;00m$
[32mprimitiveChangeClassTo:[39;49;00m [31manObject[39;49;00m$
	[37m"Primitive. Change the class of the receiver into the class of the argument given that the format of the receiver matches the format of the argument's class. Fail if receiver or argument are SmallIntegers, or the receiver is an instance of a compact class and the argument isn't, or when the argument's class is compact and the receiver isn't, or when the format of the receiver is different from the format of the argument's class, or when the arguments class is fixed and the receiver's size differs from the size that an instance of the argument's class should have.[39;49;00m$
[37m	Note: The primitive will fail in most cases that you think might work. This is mostly because of a) the difference between compact and non-compact classes, and b) because of differences in the format. As an example, '(Array new: 3) primitiveChangeClassTo: Morph basicNew' would fail for three of the reasons mentioned above. Array is compact, Morph is not (failure #1). Array is variable and Morph is fixed (different format - failure #2). Morph is a fixed-field-only object and the array is too short (failure #3).[39;49;00m$
[37m	The facility is really provided for certain, very specific applications (mostly related to classes changing shape) and not for casual use."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 115>$
	[36mself[39;49;00m [32mprimitiveFailed[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m stamp: 'di 3/27/1999 12:21'![39;49;00m$
[32mrootStubInImageSegment:[39;49;00m [31mimageSegment[39;49;00m$
$
	^ [04m[32mImageSegmentRootStub[39;49;00m [36mnew[39;49;00m$
		[32mxxSuperclass:[39;49;00m [36mnil[39;49;00m$
		[32mformat:[39;49;00m [36mnil[39;49;00m$
		[32msegment:[39;49;00m [31mimageSegment[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'system primitives'[39;49;00m[34m![39;49;00m$
[32msomeObject[39;49;00m$
	[37m"Primitive. Answer the first object in the enumeration of all[39;49;00m$
[37m	 objects."[39;49;00m$
$
	<[34mprimitive:[39;49;00m 138>$
	[36mself[39;49;00m [32mprimitiveFailed[39;49;00m.[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 9/26/2001 11:58'![39;49;00m$
[32mbasicType[39;49;00m$
	[37m"Answer a symbol representing the inherent type of the receiver"[39;49;00m$
$
	^ [33m#Object[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 5/3/2001 16:19'![39;49;00m$
[32mbeViewed[39;49;00m$
	[37m"Open up a viewer on the receiver.  The Presenter is invited to decide just how to present this viewer"[39;49;00m$
$
	[36mself[39;49;00m [32muniqueNameForReference[39;49;00m.  [37m"So the viewer will have something nice to refer to"[39;49;00m$
	[36mself[39;49;00m [32mpresenter[39;49;00m [32mviewObject:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/16/2000 11:01'![39;49;00m$
[32mcostumes[39;49;00m$
	[37m"Answer a list of costumes associated with the receiver.  The appearance of this method in class Object serves only as a backstop, probably only transitionally"[39;49;00m$
$
	^ [36mnil[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 1/12/98 18:09'![39;49;00m$
[31mhaltIfNil[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 1/20/2006 17:09'![39;49;00m$
[32mhasLiteralSuchThat:[39;49;00m [31mtestBlock[39;49;00m$
	[37m"This is the end of the imbedded structure path so return false."[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 1/20/2006 17:10'![39;49;00m$
[32mhasLiteralThorough:[39;49;00m [31mliteral[39;49;00m$
	[37m"Answer true if literal is identical to any literal in this array, even if imbedded in further structures.  This is the end of the imbedded structure path so return false."[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 1/30/2001 22:24'![39;49;00m$
[32mhaveFullProtocolBrowsed[39;49;00m$
	[37m"Open up a Lexicon on the receiver"[39;49;00m$
$
	^ [36mself[39;49;00m [32mhaveFullProtocolBrowsedShowingSelector:[39;49;00m [36mnil[39;49;00m$
$
	[37m"(2@3) haveFullProtocolBrowsed"[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 9/27/2005 21:04'![39;49;00m$
[32mhaveFullProtocolBrowsedShowingSelector:[39;49;00m [31maSelector[39;49;00m$
	[37m"Open up a Lexicon on the receiver, having it open up showing aSelector, which may be nil"[39;49;00m$
$
	|[31m aBrowser [39;49;00m|$
	[31maBrowser[39;49;00m := ([04m[32mSmalltalk[39;49;00m [32mat:[39;49;00m [33m#InstanceBrowser[39;49;00m [32mifAbsent:[39;49;00m[^[36mnil[39;49;00m]) [36mnew[39;49;00m [32museVocabulary:[39;49;00m [04m[32mVocabulary[39;49;00m [32mfullVocabulary[39;49;00m.$
	[31maBrowser[39;49;00m [32mopenOnObject:[39;49;00m [36mself[39;49;00m [32minWorld:[39;49;00m [04m[32mActiveWorld[39;49;00m [32mshowingSelector:[39;49;00m [31maSelector[39;49;00m$
$
	[37m"(2@3) haveFullProtocolBrowsed"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 7/30/2005 21:21'![39;49;00m$
[32misArray[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 7/9/1999 18:18'![39;49;00m$
[32misBehavior[39;49;00m$
	[37m"Return true if the receiver is a behavior.[39;49;00m$
[37m	Note: Do not override in any class except behavior."[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ajh 1/21/2003 13:15'![39;49;00m$
[32misBlock[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 11/21/2003 12:14'![39;49;00m$
[32misBlockClosure[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'yo 8/28/2002 13:41'![39;49;00m$
[32misCharacter[39;49;00m$
$
	^ [36mfalse[39;49;00m.$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 8/17/1999 19:43'![39;49;00m$
[32misCollection[39;49;00m$
	[37m"Return true if the receiver is some sort of Collection and responds to basic collection messages such as #size and #do:"[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
[32misColor[39;49;00m$
	[37m"Answer true if receiver is a Color. False by default."[39;49;00m$
$
	^ [36mfalse[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'nk 4/17/2004 19:43'![39;49;00m$
[32misColorForm[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 11/21/2003 12:14'![39;49;00m$
[32misCompiledMethod[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'mk 10/27/2003 17:33'![39;49;00m$
[32misComplex[39;49;00m$
	[37m"Answer true if receiver is a Complex number. False by default."[39;49;00m$
$
	^ [36mfalse[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 8/11/2005 16:45'![39;49;00m$
[32misDictionary[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'di 11/9/1998 09:38'![39;49;00m$
[32misFloat[39;49;00m$
	[37m"Overridden to return true in Float, natch"[39;49;00m$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 10/30/2000 23:22'![39;49;00m$
[32misForm[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'len 1/13/98 21:18'![39;49;00m$
[32misFraction[39;49;00m$
	[37m"Answer true if the receiver is a Fraction."[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'rhi 8/14/2003 08:51'![39;49;00m$
[32misHeap[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
[32misInteger[39;49;00m$
	[37m"Overridden to return true in Integer."[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'rhi 8/12/2003 09:52'![39;49;00m$
[32misInterval[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'nk 4/25/2002 08:04'![39;49;00m$
[32misMessageSend[39;49;00m$
	^[36mfalse[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 2/19/2006 11:24'![39;49;00m$
[32misMethodProperties[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
[32misMorph[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 9/13/2000 15:37'![39;49;00m$
[32misMorphicEvent[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'gm 2/22/2003 12:56'![39;49;00m$
[32misMorphicModel[39;49;00m$
	[37m"Return true if the receiver is a morphic model"[39;49;00m$
	^[36mfalse[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
[32misNumber[39;49;00m$
	[37m"Overridden to return true in Number, natch"[39;49;00m$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'di 11/6/1998 08:04'![39;49;00m$
[32misPoint[39;49;00m$
	[37m"Overridden to return true in Point."[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ikp 9/26/97 14:45'![39;49;00m$
[32misPseudoContext[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 10/2/2005 21:52'![39;49;00m$
[32misRectangle[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'nk 6/14/2004 16:49'![39;49;00m$
[32misSketchMorph[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 12/23/1999 15:43'![39;49;00m$
[32misStream[39;49;00m$
	[37m"Return true if the receiver responds to the stream protocol"[39;49;00m$
	^[36mfalse[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sma 6/15/2000 15:48'![39;49;00m$
[32misString[39;49;00m$
	[37m"Overridden to return true in String, natch"[39;49;00m$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'md 4/30/2003 15:30'![39;49;00m$
[32misSymbol[39;49;00m$
	^ [36mfalse[39;49;00m [34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'jam 3/9/2003 15:10'![39;49;00m$
[32misSystemWindow[39;49;00m$
[37m"answer whatever the receiver is a SystemWindow"[39;49;00m$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
[32misText[39;49;00m$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'pmm 7/6/2006 20:46'![39;49;00m$
[32misTrait[39;49;00m$
	[37m"Return true if the receiver is a trait.[39;49;00m$
[37m	Note: Do not override in any class except TraitBehavior."[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'tk 10/21/97 12:45'![39;49;00m$
[32misTransparent[39;49;00m$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ar 8/14/2001 23:19'![39;49;00m$
[32misVariableBinding[39;49;00m$
	[37m"Return true if I represent a literal variable binding"[39;49;00m$
	^[36mfalse[39;49;00m$
	[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'ls 7/14/1998 21:45'![39;49;00m$
[32misWebBrowser[39;49;00m$
	[37m"whether this object is a web browser.  See class: Scamper"[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/27/2000 06:58'![39;49;00m$
[32mknownName[39;49;00m$
	[37m"If a formal name has been handed out for this object, answer it, else nil"[39;49;00m$
	$
	^ [04m[32mPreferences[39;49;00m [32mcapitalizedReferences[39;49;00m$
		[36mifTrue:[39;49;00m$
			[[04m[32mReferences[39;49;00m [32mkeyAtValue:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m]]$
		[36mifFalse:[39;49;00m$
			[[36mnil[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 9/27/96'![39;49;00m$
[32mname[39;49;00m$
	[37m"Answer a name for the receiver.  This is used generically in the title of certain inspectors, such as the referred-to inspector, and specificially by various subsystems.  By default, we let the object just print itself out..  "[39;49;00m$
$
	^ [36mself[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 11/19/2001 13:28'![39;49;00m$
[32mnameForViewer[39;49;00m$
	[37m"Answer a name to be shown in a Viewer that is viewing the receiver"[39;49;00m$
$
	|[31m aName [39;49;00m|$
	([31maName[39;49;00m _ [36mself[39;49;00m [32muniqueNameForReferenceOrNil[39;49;00m) [32mifNotNil:[39;49;00m [^ [31maName[39;49;00m].$
	([31maName[39;49;00m _ [36mself[39;49;00m [32mknownName[39;49;00m) [32mifNotNil:[39;49;00m [^ [31maName[39;49;00m].$
$
	^ [([36mself[39;49;00m [32masString[39;49;00m [32mcopyWithout:[39;49;00m [04m[32mCharacter[39;49;00m [32mcr[39;49;00m) [32mtruncateTo:[39;49;00m  [34m27[39;49;00m] [32mifError:[39;49;00m$
		[:[31mmsg[39;49;00m :[31mrcvr[39;49;00m | ^ [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32mprintString[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m![39;49;00m$
[32mnotNil[39;49;00m$
	[37m"Coerces nil to false and everything else to true."[39;49;00m$
$
	^[36mtrue[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'tk 9/6/2001 19:15'![39;49;00m$
[32mopenInstanceBrowserWithTiles[39;49;00m$
	[37m"Open up an instance browser on me with tiles as the code type, and with the search level as desired."[39;49;00m$
$
	|[31m aBrowser [39;49;00m|$
	[31maBrowser[39;49;00m _ [04m[32mInstanceBrowser[39;49;00m [36mnew[39;49;00m.$
	[31maBrowser[39;49;00m [32museVocabulary:[39;49;00m [04m[32mVocabulary[39;49;00m [32mfullVocabulary[39;49;00m.$
	[31maBrowser[39;49;00m [32mlimitClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m.$
	[31maBrowser[39;49;00m [32mcontentsSymbol:[39;49;00m [33m#tiles[39;49;00m.		[37m"preset it to make extra buttons (tile menus)"[39;49;00m$
	[31maBrowser[39;49;00m [32mopenOnObject:[39;49;00m [36mself[39;49;00m [32minWorld:[39;49;00m [04m[32mActiveWorld[39;49;00m [32mshowingSelector:[39;49;00m [36mnil[39;49;00m.$
	[31maBrowser[39;49;00m [32mcontentsSymbol:[39;49;00m [33m#source[39;49;00m.$
	[31maBrowser[39;49;00m [32mtoggleShowingTiles[39;49;00m.$
$
	[37m"[39;49;00m$
[37m(2@3) openInstanceBrowserWithTiles.[39;49;00m$
[37mWatchMorph new openInstanceBrowserWithTiles[39;49;00m$
[37m"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'tk 7/28/2005 04:50'![39;49;00m$
[32mrenameInternal:[39;49;00m [31mnewName[39;49;00m $
	[37m"Change the internal name (because of a conflict) but leave the external name unchanged.  Change Player class name, but do not change the names that appear in tiles.  Any object that might be pointed to in the References dictionary might get this message sent to it upon reload"[39;49;00m$
$
	^ [36mnil[39;49;00m	[37m"caller will renameTo:.  new name may be different"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 2/27/2002 14:55'![39;49;00m$
[32mrenameTo:[39;49;00m [31mnewName[39;49;00m$
	[37m"If the receiver has an inherent idea about its own name, it should take action here.  Any object that might be pointed to in the References dictionary might get this message sent to it upon reload"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 1/18/2001 13:43'![39;49;00m$
[32mshowDiffs[39;49;00m$
	[37m"Answer whether the receiver, serving as the model of a text-bearing entity, is 'showing differences' -- if it is, the editor may wish to show special feedback"[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/20/1999 14:52'![39;49;00m$
[32mstepAt:[39;49;00m [31mmillisecondClockValue[39;49;00m [32min:[39;49;00m [31maWindow[39;49;00m$
$
	^ [36mself[39;49;00m [32mstepIn:[39;49;00m [31maWindow[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/19/1999 08:16'![39;49;00m$
[32mstepIn:[39;49;00m [31maWindow[39;49;00m$
$
	^ [36mself[39;49;00m [32mstep[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/19/1999 08:21'![39;49;00m$
[32mstepTime[39;49;00m$
	$
	^ [34m1000[39;49;00m [37m"milliseconds -- default backstop for objects serving as models of system windows"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/19/1999 08:22'![39;49;00m$
[32mstepTimeIn:[39;49;00m [31maSystemWindow[39;49;00m$
	$
	^ [34m1000[39;49;00m [37m"milliseconds -- default backstop for objects serving as models of system windows"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 5/3/2001 18:22'![39;49;00m$
[32mvocabularyDemanded[39;49;00m$
	[37m"Answer a vocabulary that the receiver insists be used when it is looked at in a Viewer.  This allows specific classes to insist on specific custom vocabularies"[39;49;00m$
$
	^ [36mnil[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 11/13/2001 07:26'![39;49;00m$
[32mwantsDiffFeedback[39;49;00m$
	[37m"Answer whether the receiver, serving as the model of a text-bearing entity, would like for 'diffs' green pane-border feedback to be shown"[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'di 1/8/1999 15:04'![39;49;00m$
[32mwantsSteps[39;49;00m$
	[37m"Overridden by morphic classes whose instances want to be stepped,[39;49;00m$
[37m	or by model classes who want their morphic views to be stepped."[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'testing'[39;49;00m[34m stamp: 'sw 10/19/1999 08:26'![39;49;00m$
[32mwantsStepsIn:[39;49;00m [31maSystemWindow[39;49;00m$
	$
	^ [36mself[39;49;00m [32mwantsSteps[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'thumbnail'[39;49;00m[34m stamp: 'dgd 9/25/2004 23:17'![39;49;00m$
[32miconOrThumbnailOfSize:[39;49;00m [31maNumberOrPoint[39;49;00m $
	[37m"Answer an appropiate form to represent the receiver"[39;49;00m$
	^ [36mnil[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'translation support'[39;49;00m[34m![39;49;00m$
[32minline:[39;49;00m [31minlineFlag[39;49;00m$
	[37m"For translation only; noop when running in Smalltalk."[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'translation support'[39;49;00m[34m![39;49;00m$
[32mvar:[39;49;00m [31mvarSymbol[39;49;00m [32mdeclareC:[39;49;00m [31mdeclString[39;49;00m$
	[37m"For translation only; noop when running in Smalltalk."[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/11/2000 20:32'![39;49;00m$
[32mcapturedState[39;49;00m$
	[37m"May be overridden in subclasses."[39;49;00m$
$
	^ [36mself[39;49;00m [32mshallowCopy[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/11/2000 20:29'![39;49;00m$
[32mcommandHistory[39;49;00m$
	[37m"Return the command history for the receiver"[39;49;00m$
	|[31m w [39;49;00m|$
	([31mw[39;49;00m _ [36mself[39;49;00m [32mcurrentWorld[39;49;00m) [32mifNotNil:[39;49;00m [^ [31mw[39;49;00m [32mcommandHistory[39;49;00m].$
	^ [04m[32mCommandHistory[39;49;00m [36mnew[39;49;00m. [37m"won't really record anything but prevent breaking things"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 12/12/2000 15:01'![39;49;00m$
[32mpurgeAllCommands[39;49;00m$
	[37m"Purge all commands for this object"[39;49;00m$
	[04m[32mPreferences[39;49;00m [32museUndo[39;49;00m [36mifFalse:[39;49;00m [^ [36mself[39;49;00m]. [37m"get out quickly"[39;49;00m$
	[36mself[39;49;00m [32mcommandHistory[39;49;00m [32mpurgeAllCommandsSuchThat:[39;49;00m [:[31mcmd[39;49;00m | [31mcmd[39;49;00m [32mundoTarget[39;49;00m [32m==[39;49;00m [36mself[39;49;00m].$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/12/2000 08:15'![39;49;00m$
[32mredoFromCapturedState:[39;49;00m [31mst[39;49;00m $
	[37m"May be overridden in subclasses.  See also capturedState"[39;49;00m$
$
	[36mself[39;49;00m [32mundoFromCapturedState:[39;49;00m [31mst[39;49;00m  [37m"Simple cases are symmetric"[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'sw 11/16/2000 14:42'![39;49;00m$
[32mrefineRedoTarget:[39;49;00m [31mtarget[39;49;00m [32mselector:[39;49;00m [31maSymbol[39;49;00m [32marguments:[39;49;00m [31marguments[39;49;00m [32min:[39;49;00m [31mrefineBlock[39;49;00m $
	[37m"Any object can override this method to refine its redo specification"[39;49;00m$
$
	^ [31mrefineBlock[39;49;00m$
		[32mvalue:[39;49;00m [31mtarget[39;49;00m$
		[32mvalue:[39;49;00m [31maSymbol[39;49;00m$
		[32mvalue:[39;49;00m [31marguments[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'sw 11/16/2000 14:42'![39;49;00m$
[32mrefineUndoTarget:[39;49;00m [31mtarget[39;49;00m [32mselector:[39;49;00m [31maSymbol[39;49;00m [32marguments:[39;49;00m [31marguments[39;49;00m [32min:[39;49;00m [31mrefineBlock[39;49;00m $
	[37m"Any object can override this method to refine its undo specification"[39;49;00m$
$
	^ [31mrefineBlock[39;49;00m$
		[32mvalue:[39;49;00m [31mtarget[39;49;00m$
		[32mvalue:[39;49;00m [31maSymbol[39;49;00m$
		[32mvalue:[39;49;00m [31marguments[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/11/2000 20:30'![39;49;00m$
[32mrememberCommand:[39;49;00m [31maCommand[39;49;00m$
	[37m"Remember the given command for undo"[39;49;00m$
	[04m[32mPreferences[39;49;00m [32museUndo[39;49;00m [36mifFalse:[39;49;00m [^ [36mself[39;49;00m]. [37m"get out quickly"[39;49;00m$
	^ [36mself[39;49;00m [32mcommandHistory[39;49;00m [32mrememberCommand:[39;49;00m [31maCommand[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/11/2000 20:30'![39;49;00m$
[32mrememberUndoableAction:[39;49;00m [31mactionBlock[39;49;00m [32mnamed:[39;49;00m [31mcaption[39;49;00m$
	|[31m cmd result [39;49;00m|$
	[31mcmd[39;49;00m _ [04m[32mCommand[39;49;00m [36mnew[39;49;00m [32mcmdWording:[39;49;00m [31mcaption[39;49;00m.$
	[31mcmd[39;49;00m [32mundoTarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#undoFromCapturedState:[39;49;00m [32margument:[39;49;00m [36mself[39;49;00m [32mcapturedState[39;49;00m.$
	[31mresult[39;49;00m _ [31mactionBlock[39;49;00m [32mvalue[39;49;00m.$
	[31mcmd[39;49;00m [32mredoTarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#redoFromCapturedState:[39;49;00m [32margument:[39;49;00m [36mself[39;49;00m [32mcapturedState[39;49;00m.$
	[36mself[39;49;00m [32mrememberCommand:[39;49;00m [31mcmd[39;49;00m.$
	^ [31mresult[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'undo'[39;49;00m[34m stamp: 'di 9/11/2000 20:32'![39;49;00m$
[32mundoFromCapturedState:[39;49;00m [31mst[39;49;00m $
	[37m"May be overridden in subclasses.  See also capturedState"[39;49;00m$
$
	[36mself[39;49;00m [32mcopyFrom:[39;49;00m [31mst[39;49;00m$
[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m![39;49;00m$
[32mchanged[39;49;00m$
	[37m"Receiver changed in a general way; inform all the dependents by [39;49;00m$
[37m	sending each dependent an update: message."[39;49;00m$
$
	[36mself[39;49;00m [32mchanged:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m![39;49;00m$
[32mchanged:[39;49;00m [31maParameter[39;49;00m $
	[37m"Receiver changed. The change is denoted by the argument aParameter. [39;49;00m$
[37m	Usually the argument is a Symbol that is part of the dependent's change [39;49;00m$
[37m	protocol. Inform all of the dependents."[39;49;00m$
$
	[36mself[39;49;00m [32mdependents[39;49;00m [32mdo:[39;49;00m [:[31maDependent[39;49;00m | [31maDependent[39;49;00m [32mupdate:[39;49;00m [31maParameter[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'nk 2/17/2004 11:12'![39;49;00m$
[32mchanged:[39;49;00m [31manAspect[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m$
	[37m"Receiver changed. The change is denoted by the argument anAspect. [39;49;00m$
[37m	Usually the argument is a Symbol that is part of the dependent's change [39;49;00m$
[37m	protocol. Inform all of the dependents. Also pass anObject for additional information."[39;49;00m$
$
	[36mself[39;49;00m [32mdependents[39;49;00m [32mdo:[39;49;00m [:[31maDependent[39;49;00m | [31maDependent[39;49;00m [32mupdate:[39;49;00m [31manAspect[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'sw 10/12/1999 18:15'![39;49;00m$
[32mhandledListVerification[39;49;00m$
	[37m"When a self-updating PluggableListMorph lazily checks to see the state of affairs, it first gives its model an opportunity to handle the list verification itself (this is appropriate for some models, such as VersionsBrowser); if a list's model has indeed handled things itself, it returns true here"[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'sw 10/31/1999 00:15'![39;49;00m$
[32mnoteSelectionIndex:[39;49;00m [31manInteger[39;49;00m [32mfor:[39;49;00m [31maSymbol[39;49;00m$
	[37m"backstop"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m![39;49;00m$
[32mokToChange[39;49;00m$
	[37m"Allows a controller to ask this of any model"[39;49;00m$
	^ [36mtrue[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'sw 10/19/1999 14:39'![39;49;00m$
[32mupdateListsAndCodeIn:[39;49;00m [31maWindow[39;49;00m$
	[36mself[39;49;00m [32mcanDiscardEdits[39;49;00m [36mifFalse:[39;49;00m [^ [36mself[39;49;00m].$
	[31maWindow[39;49;00m [32mupdatablePanes[39;49;00m [32mdo:[39;49;00m [:[31maPane[39;49;00m | [31maPane[39;49;00m [32mverifyContents[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'sma 2/29/2000 20:05'![39;49;00m$
[32mupdate:[39;49;00m [31maParameter[39;49;00m $
	[37m"Receive a change notice from an object of whom the receiver is a [39;49;00m$
[37m	dependent. The default behavior is to do nothing; a subclass might want [39;49;00m$
[37m	to change itself in some way."[39;49;00m$
$
	^ [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'nk 2/17/2004 11:13'![39;49;00m$
[32mupdate:[39;49;00m [31manAspect[39;49;00m [32mwith:[39;49;00m [31manObject[39;49;00m$
	[37m"Receive a change notice from an object of whom the receiver is a [39;49;00m$
[37m	dependent. The default behavior is to call update:,[39;49;00m$
[37m	which by default does nothing; a subclass might want [39;49;00m$
[37m	to change itself in some way."[39;49;00m$
$
	^ [36mself[39;49;00m [32mupdate:[39;49;00m [31manAspect[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'updating'[39;49;00m[34m stamp: 'jm 8/20/1998 18:26'![39;49;00m$
[32mwindowIsClosing[39;49;00m$
	[37m"This message is used to inform a models that its window is closing. Most models do nothing, but some, such as the Debugger, must do some cleanup. Note that this mechanism must be used with care by models that support multiple views, since one view may be closed while others left open."[39;49;00m$
[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 10/4/1999 08:13'![39;49;00m$
[32maddModelItemsToWindowMenu:[39;49;00m [31maMenu[39;49;00m$
	[37m"aMenu is being constructed to be presented to the user in response to the user's pressing on the menu widget in the title bar of a morphic window.  Here, the model is given the opportunity to add any model-specific items to the menu, whose default target is the SystemWindow itself."[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 10/5/1998 14:39'![39;49;00m$
[32maddModelMenuItemsTo:[39;49;00m [31maCustomMenu[39;49;00m [32mforMorph:[39;49;00m [31maMorph[39;49;00m [32mhand:[39;49;00m [31maHandMorph[39;49;00m $
	[37m"The receiver serves as the model for aMorph; a menu is being constructed for the morph, and here the receiver is able to add its own items"[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sma 11/12/2000 11:43'![39;49;00m$
[32masExplorerString[39;49;00m$
	^ [36mself[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 7/13/1999 15:53'![39;49;00m$
[32mdefaultBackgroundColor[39;49;00m$
	[37m"Answer the color to be used as the base window color for a window whose model is an object of the receiver's class"[39;49;00m$
	$
	^ [04m[32mPreferences[39;49;00m [32mwindowColorFor:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m![39;49;00m$
[32mdefaultLabelForInspector[39;49;00m$
	[37m"Answer the default label to be used for an Inspector window on the receiver."[39;49;00m$
$
	^ [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'RAA 7/10/2000 08:11'![39;49;00m$
[32meToyStreamedRepresentationNotifying:[39;49;00m [31maWidget[39;49;00m$
$
	|[31m outData [39;49;00m|$
	[ [31moutData[39;49;00m _ [04m[32mSmartRefStream[39;49;00m [32mstreamedRepresentationOf:[39;49;00m [36mself[39;49;00m ] $
		[32mon:[39;49;00m [04m[32mProgressInitiationException[39;49;00m$
		[32mdo:[39;49;00m [ :[31mex[39;49;00m | $
			[31mex[39;49;00m [32msendNotificationsTo:[39;49;00m [ :[31mmin[39;49;00m :[31mmax[39;49;00m :[31mcurr[39;49;00m |$
				[31maWidget[39;49;00m [32mifNotNil:[39;49;00m [[31maWidget[39;49;00m [32mflashIndicator:[39;49;00m [33m#working[39;49;00m].$
			].$
		].$
	^[31moutData[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'ar 9/27/2005 20:29'![39;49;00m$
[32mexplore[39;49;00m$
	^[04m[32mToolSet[39;49;00m [32mexplore:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 8/15/97 17:25'![39;49;00m$
[32mfullScreenSize[39;49;00m$
	[37m"Answer the size to which a window displaying the receiver should be set"[39;49;00m$
	|[31m adj [39;49;00m|$
	[31madj[39;49;00m _ ([34m3[39;49;00m [32m*[39;49;00m [04m[32mPreferences[39;49;00m [32mscrollBarWidth[39;49;00m) [32m@[39;49;00m [34m0[39;49;00m.$
	^ [04m[32mRectangle[39;49;00m [32morigin:[39;49;00m [31madj[39;49;00m [32mextent:[39;49;00m ([04m[32mDisplayScreen[39;49;00m [32mactualScreenSize[39;49;00m [32m-[39;49;00m [31madj[39;49;00m)[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'RAA 6/21/1999 11:27'![39;49;00m$
[32mhasContentsInExplorer[39;49;00m$
$
	^[36mself[39;49;00m [32mbasicSize[39;49;00m [32m>[39;49;00m [34m0[39;49;00m [32mor:[39;49;00m [[36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNames[39;49;00m [32misEmpty[39;49;00m [32mnot[39;49;00m]$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'rbb 3/1/2005 09:28'![39;49;00m$
[32minform:[39;49;00m [31maString[39;49;00m$
	[37m"Display a message for the user to read and then dismiss. 6/9/96 sw"[39;49;00m$
$
	[31maString[39;49;00m [32misEmptyOrNil[39;49;00m [36mifFalse:[39;49;00m [[04m[32mUIManager[39;49;00m [32mdefault[39;49;00m [32minform:[39;49;00m [31maString[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m![39;49;00m$
[32minitialExtent[39;49;00m$
	[37m"Answer the desired extent for the receiver when a view on it is first opened on the screen. [39;49;00m$
[37m	5/22/96 sw: in the absence of any override, obtain from RealEstateAgent"[39;49;00m$
$
	^ [04m[32mRealEstateAgent[39;49;00m [32mstandardWindowExtent[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'ar 9/27/2005 20:30'![39;49;00m$
[32minspectWithLabel:[39;49;00m [31maLabel[39;49;00m$
	[37m"Create and schedule an Inspector in which the user can examine the receiver's variables."[39;49;00m$
	^[04m[32mToolSet[39;49;00m [32minspect:[39;49;00m [36mself[39;49;00m [32mlabel:[39;49;00m [31maLabel[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 6/12/2001 11:09'![39;49;00m$
[32mlaunchPartVia:[39;49;00m [31maSelector[39;49;00m$
	[37m"Obtain a morph by sending aSelector to self, and attach it to the morphic hand.  This provides a general protocol for parts bins"[39;49;00m$
$
	|[31m aMorph [39;49;00m|$
	[31maMorph[39;49;00m _ [36mself[39;49;00m [32mperform:[39;49;00m [31maSelector[39;49;00m.$
	[31maMorph[39;49;00m [32msetProperty:[39;49;00m [33m#beFullyVisibleAfterDrop[39;49;00m [32mtoValue:[39;49;00m [36mtrue[39;49;00m.$
	[31maMorph[39;49;00m [32mopenInHand[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 6/17/2004 01:47'![39;49;00m$
[32mlaunchPartVia:[39;49;00m [31maSelector[39;49;00m [32mlabel:[39;49;00m [31maString[39;49;00m$
	[37m"Obtain a morph by sending aSelector to self, and attach it to the morphic hand.  This provides a general protocol for parts bins"[39;49;00m$
$
	|[31m aMorph [39;49;00m|$
	[31maMorph[39;49;00m _ [36mself[39;49;00m [32mperform:[39;49;00m [31maSelector[39;49;00m.$
	[31maMorph[39;49;00m [32msetNameTo:[39;49;00m ([04m[32mActiveWorld[39;49;00m [32munusedMorphNameLike:[39;49;00m [31maString[39;49;00m).$
	[31maMorph[39;49;00m [32msetProperty:[39;49;00m [33m#beFullyVisibleAfterDrop[39;49;00m [32mtoValue:[39;49;00m [36mtrue[39;49;00m.$
	[31maMorph[39;49;00m [32mopenInHand[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 10/16/2000 11:11'![39;49;00m$
[32mlaunchTileToRefer[39;49;00m$
	[37m"Create a tile to reference the receiver, and attach it to the hand"[39;49;00m$
$
	[36mself[39;49;00m [32mcurrentHand[39;49;00m [32mattachMorph:[39;49;00m [36mself[39;49;00m [32mtileToRefer[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'di 5/11/1999 22:26'![39;49;00m$
[32mmodelSleep[39;49;00m$
	[37m"A window with me as model is being exited or collapsed or closed.[39;49;00m$
[37m	Default response is no-op"[39;49;00m [34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'di 5/11/1999 22:01'![39;49;00m$
[32mmodelWakeUp[39;49;00m$
	[37m"A window with me as model is being entered or expanded.  Default response is no-op"[39;49;00m [34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 10/16/1999 22:45'![39;49;00m$
[32mmodelWakeUpIn:[39;49;00m [31maWindow[39;49;00m$
	[37m"A window with me as model is being entered or expanded.  Default response is no-op"[39;49;00m $
	[36mself[39;49;00m [32mmodelWakeUp[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 3/8/1999 15:27'![39;49;00m$
[32mmouseUpBalk:[39;49;00m [31mevt[39;49;00m$
	[37m"A button I own got a mouseDown, but the user moved out before letting up.  Certain kinds of objects (so-called 'radio buttons', for example, and other structures that must always have some selection, e.g. PaintBoxMorph) wish to take special action in this case; this default does nothing."[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'sw 8/22/97 13:14'![39;49;00m$
[32mnewTileMorphRepresentative[39;49;00m$
	^ [04m[32mTileMorph[39;49;00m [36mnew[39;49;00m [32msetLiteral:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'jcg 11/1/2001 13:13'![39;49;00m$
[32mnotYetImplemented[39;49;00m$
	[36mself[39;49;00m [32minform:[39;49;00m [33m'Not yet implemented ('[39;49;00m[32m,[39;49;00m [36mthisContext[39;49;00m [32msender[39;49;00m [32mprintString[39;49;00m[32m,[39;49;00m [33m')'[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'user interface'[39;49;00m[34m stamp: 'di 6/10/1998 15:06'![39;49;00m$
[32mwindowReqNewLabel:[39;49;00m [31mlabelString[39;49;00m$
	[37m"My window's title has been edited.[39;49;00m$
[37m	Return true if this is OK, and override for further behavior."[39;49;00m$
$
	^ [36mtrue[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 10/16/2000 10:35'![39;49;00m$
[32massureUniClass[39;49;00m$
	[37m"If the receiver is not yet an instance of a uniclass, create a uniclass for it and make the receiver become an instance of that class."[39;49;00m$
$
	|[31m anInstance [39;49;00m|$
	[36mself[39;49;00m [32mbelongsToUniClass[39;49;00m [36mifTrue:[39;49;00m [^ [36mself[39;49;00m].$
	[31manInstance[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32minstanceOfUniqueClass[39;49;00m.$
	[36mself[39;49;00m [32mbecome:[39;49;00m ([36mself[39;49;00m [32mas:[39;49;00m [31manInstance[39;49;00m [32mclass[39;49;00m).$
	^ [31manInstance[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 10/16/2000 10:41'![39;49;00m$
[32mbelongsToUniClass[39;49;00m$
	[37m"Answer whether the receiver belongs to a uniclass.  For the moment (this is not entirely satisfactory) this is precisely equated with the classname ending in a digit"[39;49;00m$
$
	^ [36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m [32mendsWithDigit[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 12/11/2000 15:37'![39;49;00m$
[32mbrowseOwnClassSubProtocol[39;49;00m$
	[37m"Open up a ProtocolBrowser on the subprotocol of the receiver"[39;49;00m$
$
	[04m[32mProtocolBrowser[39;49;00m [32mopenSubProtocolForClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/4/2001 00:51'![39;49;00m$
[32mcategoriesForViewer:[39;49;00m [31maViewer[39;49;00m$
	[37m"Answer a list of categories to offer in the given viewer"[39;49;00m$
$
	^ [31maViewer[39;49;00m [32mcurrentVocabulary[39;49;00m [32mcategoryListForInstance:[39;49;00m [36mself[39;49;00m [32mofClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mlimitClass:[39;49;00m [31maViewer[39;49;00m [32mlimitClass[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/3/2001 22:08'![39;49;00m$
[32mcategoriesForVocabulary:[39;49;00m [31maVocabulary[39;49;00m [32mlimitClass:[39;49;00m [31maLimitClass[39;49;00m$
	[37m"Answer a list of categories of methods for the receiver when using the given vocabulary, given that one considers only methods that are implemented not further away than aLimitClass"[39;49;00m$
$
	^ [31maVocabulary[39;49;00m [32mcategoryListForInstance:[39;49;00m [36mself[39;49;00m [32mofClass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32mlimitClass:[39;49;00m [31maLimitClass[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 10/25/2000 07:20'![39;49;00m$
[32mchooseNewNameForReference[39;49;00m$
	[37m"Offer an opportunity for the receiver, presumed already to be known in the References registry, to be renamed"[39;49;00m$
$
	|[31m  nameSym current newName [39;49;00m|$
	[31mcurrent[39;49;00m _ [04m[32mReferences[39;49;00m [32mkeyAtValue:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'not found in References'[39;49;00m].$
$
	[31mnewName[39;49;00m _ [04m[32mFillInTheBlank[39;49;00m [32mrequest:[39;49;00m [33m'Please enter new name'[39;49;00m [32minitialAnswer:[39;49;00m [31mcurrent[39;49;00m.$
	[37m"Want to user some better way of determining the validity of the chosen identifier, and also want to give more precise diagnostic if the string the user types in is not acceptable.  Work to be done here."[39;49;00m$
$
	[31mnewName[39;49;00m [32misEmpty[39;49;00m [36mifTrue:[39;49;00m [^ [36mnil[39;49;00m].$
	(([04m[32mScanner[39;49;00m [32misLiteralSymbol:[39;49;00m [31mnewName[39;49;00m) [32mand:[39;49;00m [([31mnewName[39;49;00m [32mincludes:[39;49;00m [33m$:[39;49;00m) [32mnot[39;49;00m])$
		[36mifTrue:[39;49;00m$
			[[31mnameSym[39;49;00m _ [31mnewName[39;49;00m [32mcapitalized[39;49;00m [32masSymbol[39;49;00m.$
			((([04m[32mReferences[39;49;00m [32mincludesKey:[39;49;00m  [31mnameSym[39;49;00m) [32mnot[39;49;00m [32mand:[39;49;00m$
				[([04m[32mSmalltalk[39;49;00m [32mincludesKey:[39;49;00m [31mnameSym[39;49;00m) [32mnot[39;49;00m]) [32mand:[39;49;00m$
						[([04m[32mScriptingSystem[39;49;00m [32mallKnownClassVariableNames[39;49;00m [32mincludes:[39;49;00m [31mnameSym[39;49;00m) [32mnot[39;49;00m])$
					[36mifTrue:[39;49;00m$
						[([04m[32mReferences[39;49;00m [32massociationAt:[39;49;00m [31mcurrent[39;49;00m) [32mkey:[39;49;00m [31mnameSym[39;49;00m.$
						[04m[32mReferences[39;49;00m [32mrehash[39;49;00m.$
						^ [31mnameSym[39;49;00m]].$
	[36mself[39;49;00m [32minform:[39;49;00m [33m'Sorry, that name is not available.'[39;49;00m.$
	^ [36mnil[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/3/2001 21:22'![39;49;00m$
[32mdefaultLimitClassForVocabulary:[39;49;00m [31maVocabulary[39;49;00m$
	[37m"Answer the class to use, by default, as the limit class on a protocol browser or viewer opened up on the receiver, within the purview of the Vocabulary provided"[39;49;00m$
$
	^ ([31maVocabulary[39;49;00m [32misKindOf:[39;49;00m [04m[32mFullVocabulary[39;49;00m)$
		[36mifTrue:[39;49;00m$
			 [[36mself[39;49;00m [32mclass[39;49;00m [32msuperclass[39;49;00m [32m==[39;49;00m [04m[32mObject[39;49;00m$
				[36mifTrue:[39;49;00m$
					[[36mself[39;49;00m [32mclass[39;49;00m]$
				[36mifFalse:[39;49;00m$
					[[36mself[39;49;00m [32mclass[39;49;00m [32msuperclass[39;49;00m]]$
		[36mifFalse:[39;49;00m$
			[[04m[32mProtoObject[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 2/14/2000 14:24'![39;49;00m$
[32mdefaultNameStemForInstances[39;49;00m$
	[37m"Answer a basis for names of default instances of the receiver.  The default is to let the class specify, but certain instances will want to override.  (PasteUpMorphs serving as Worlds come to mind"[39;49;00m$
$
	^ [36mself[39;49;00m [32mclass[39;49;00m [32mdefaultNameStemForInstances[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 5/22/2001 16:53'![39;49;00m$
[32melementTypeFor:[39;49;00m [31maStringOrSymbol[39;49;00m [32mvocabulary:[39;49;00m [31maVocabulary[39;49;00m$
	[37m"Answer a symbol characterizing what kind of element aStringOrSymbol represents.  Realistically, at present, this always just returns #systemScript; a prototyped but not-incorporated architecture supported use of a leading colon to characterize an inst var of a system class, and for the moment we still see its remnant here."[39;49;00m$
$
	[36mself[39;49;00m [32mflag:[39;49;00m [33m#deferred[39;49;00m.  [37m"a loose end in the non-player case"[39;49;00m$
	^ [33m#systemScript[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 5/4/2001 07:04'![39;49;00m$
[32mexternalName[39;49;00m$
	[37m"Answer an external name by which the receiver is known.  Generic implementation here is a transitional backstop. probably"[39;49;00m$
$
	^ [36mself[39;49;00m [32mnameForViewer[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 5/4/2001 07:06'![39;49;00m$
[32mgraphicForViewerTab[39;49;00m$
	[37m"When a Viewer is open on the receiver, its tab needs some graphic to show to the user.  Answer a form or a morph to serve that purpose.  A generic image is used for arbitrary objects, but note my reimplementors"[39;49;00m$
	$
	^ [04m[32mScriptingSystem[39;49;00m [32mformAtKey:[39;49;00m [33m'Image'[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 5/4/2001 07:08'![39;49;00m$
[32mhasUserDefinedSlots[39;49;00m$
	[37m"Answer whether the receiver has any user-defined slots, in the omniuser sense of the term.  This is needed to allow Viewers to look at any object, not just at Players."[39;49;00m$
$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/22/2002 14:07'![39;49;00m$
[32minfoFor:[39;49;00m [31manElement[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m$
	[37m"The user made a gesture asking for info/menu relating to me.  Some of the messages dispatched here are not yet available in this image"[39;49;00m$
$
	|[31m aMenu elementType [39;49;00m|$
	[31melementType[39;49;00m _ [36mself[39;49;00m [32melementTypeFor:[39;49;00m [31manElement[39;49;00m [32mvocabulary:[39;49;00m [31maViewer[39;49;00m [32mcurrentVocabulary[39;49;00m.$
	(([31melementType[39;49;00m [32m=[39;49;00m [33m#systemSlot[39;49;00m) [32m|[39;49;00m ([31melementType[39;49;00m [32m==[39;49;00m [33m#userSlot[39;49;00m))$
		[36mifTrue:[39;49;00m	[^ [36mself[39;49;00m [32mslotInfoButtonHitFor:[39;49;00m [31manElement[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m].$
	[36mself[39;49;00m [32mflag:[39;49;00m [33m#deferred[39;49;00m.  [37m"Use a traditional MenuMorph, and reinstate the pacify thing"[39;49;00m$
	[31maMenu[39;49;00m _ [04m[32mMenuMorph[39;49;00m [36mnew[39;49;00m [32mdefaultTarget:[39;49;00m [31maViewer[39;49;00m.$
	[33m#([39;49;00m	[33m([39;49;00m[33m'implementors'[39;49;00m			[33mbrowseImplementorsOf:[39;49;00m[33m)[39;49;00m$
		[33m([39;49;00m[33m'senders'[39;49;00m				[33mbrowseSendersOf:[39;49;00m[33m)[39;49;00m$
		[33m([39;49;00m[33m'versions'[39;49;00m				[33mbrowseVersionsOf:[39;49;00m[33m)[39;49;00m$
		[33m-[39;49;00m$
		[33m([39;49;00m[33m'browse full'[39;49;00m			[33mbrowseMethodFull:[39;49;00m[33m)[39;49;00m$
		[33m([39;49;00m[33m'inheritance'[39;49;00m			[33mbrowseMethodInheritance:[39;49;00m[33m)[39;49;00m$
		[33m-[39;49;00m$
		[33m([39;49;00m[33m'about this method'[39;49;00m		[33maboutMethod:[39;49;00m[33m)[39;49;00m[33m)[39;49;00m [32mdo:[39;49;00m$
$
			[:[31mpair[39;49;00m |$
				[31mpair[39;49;00m [32m=[39;49;00m [33m'-'[39;49;00m$
					[36mifTrue:[39;49;00m$
						[[31maMenu[39;49;00m [32maddLine[39;49;00m]$
					[36mifFalse:[39;49;00m$
						[[31maMenu[39;49;00m [32madd:[39;49;00m [31mpair[39;49;00m [32mfirst[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32mselector:[39;49;00m [31mpair[39;49;00m [32msecond[39;49;00m [32margument:[39;49;00m [31manElement[39;49;00m]].$
	[31maMenu[39;49;00m [32maddLine[39;49;00m.$
	[31maMenu[39;49;00m [32mdefaultTarget:[39;49;00m [36mself[39;49;00m.$
	[33m#([39;49;00m	[33m([39;49;00m[33m'destroy script'[39;49;00m		[33mremoveScript:[39;49;00m[33m)[39;49;00m$
		[33m([39;49;00m[33m'rename script'[39;49;00m		[33mrenameScript:[39;49;00m[33m)[39;49;00m$
		[33m([39;49;00m[33m'pacify script'[39;49;00m		[33mpacifyScript:[39;49;00m[33m)[39;49;00m[33m)[39;49;00m [32mdo:[39;49;00m$
			[:[31mpair[39;49;00m |$
				[31maMenu[39;49;00m [32madd:[39;49;00m [31mpair[39;49;00m [32mfirst[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [31mpair[39;49;00m [32msecond[39;49;00m [32margument:[39;49;00m [31manElement[39;49;00m].$
$
	[31maMenu[39;49;00m [32maddLine[39;49;00m.$
	[31maMenu[39;49;00m  [32madd:[39;49;00m [33m'show categories....'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32mselector:[39;49;00m [33m#showCategoriesFor:[39;49;00m [32margument:[39;49;00m [31manElement[39;49;00m.$
	[31maMenu[39;49;00m [32mitems[39;49;00m [32msize[39;49;00m [32m==[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m  [37m"won't happen at the moment a/c the above"[39;49;00m$
		[[31maMenu[39;49;00m [32madd:[39;49;00m [33m'ok'[39;49;00m [32maction:[39;49;00m [36mnil[39;49;00m].  [37m"in case it was a slot -- weird, transitional"[39;49;00m$
$
	[31maMenu[39;49;00m [32maddTitle:[39;49;00m [31manElement[39;49;00m [32masString[39;49;00m[32m,[39;49;00m [33m' ('[39;49;00m[32m,[39;49;00m [31melementType[39;49;00m[32m,[39;49;00m [33m')'[39;49;00m.$
$
	[31maMenu[39;49;00m [32mpopUpInWorld:[39;49;00m [36mself[39;49;00m [32mcurrentWorld[39;49;00m.$
 [34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 9/26/2001 11:58'![39;49;00m$
[32minitialTypeForSlotNamed:[39;49;00m [31maName[39;49;00m$
	[37m"Answer the initial type to be ascribed to the given instance variable"[39;49;00m$
$
	^ [33m#Object[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'ar 5/26/2001 16:13'![39;49;00m$
[32misPlayerLike[39;49;00m$
	[37m"Return true if the receiver is a player-like object"[39;49;00m$
	^[36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'nk 9/11/2004 16:53'![39;49;00m$
[32mmethodInterfacesInPresentationOrderFrom:[39;49;00m [31minterfaceList[39;49;00m [32mforCategory:[39;49;00m [31maCategory[39;49;00m $
	[37m"Answer the interface list sorted in desired presentation order, using a [39;49;00m$
[37m	static master-ordering list, q.v. The category parameter allows an [39;49;00m$
[37m	escape in case one wants to apply different order strategies in different [39;49;00m$
[37m	categories, but for now a single master-priority-ordering is used -- see [39;49;00m$
[37m	the comment in method EToyVocabulary.masterOrderingOfPhraseSymbols"[39;49;00m$
$
	|[31m masterOrder ordered unordered index [39;49;00m|$
	[31mmasterOrder[39;49;00m := [04m[32mVocabulary[39;49;00m [32meToyVocabulary[39;49;00m [32mmasterOrderingOfPhraseSymbols[39;49;00m.$
	[31mordered[39;49;00m := [04m[32mSortedCollection[39;49;00m [32msortBlock:[39;49;00m [:[31ma[39;49;00m :[31mb[39;49;00m | [31ma[39;49;00m [32mkey[39;49;00m [32m<[39;49;00m [31mb[39;49;00m [32mkey[39;49;00m].$
	[31munordered[39;49;00m := [04m[32mSortedCollection[39;49;00m [32msortBlock:[39;49;00m [:[31ma[39;49;00m :[31mb[39;49;00m | [31ma[39;49;00m [32mwording[39;49;00m [32m<[39;49;00m [31mb[39;49;00m [32mwording[39;49;00m].$
$
	[31minterfaceList[39;49;00m [32mdo:[39;49;00m [:[31minterface[39;49;00m | $
		[31mindex[39;49;00m := [31mmasterOrder[39;49;00m [32mindexOf:[39;49;00m [31minterface[39;49;00m [32melementSymbol[39;49;00m.$
		[31mindex[39;49;00m [32misZero[39;49;00m$
			[36mifTrue:[39;49;00m [[31munordered[39;49;00m [32madd:[39;49;00m [31minterface[39;49;00m]$
			[36mifFalse:[39;49;00m [[31mordered[39;49;00m [32madd:[39;49;00m [31mindex[39;49;00m [32m->[39;49;00m [31minterface[39;49;00m]].$
$
	^ [04m[32mArray[39;49;00m$
		[32mstreamContents:[39;49;00m [:[31mstream[39;49;00m | $
			[31mordered[39;49;00m [32mdo:[39;49;00m [:[31massoc[39;49;00m | [31mstream[39;49;00m [32mnextPut:[39;49;00m [31massoc[39;49;00m [32mvalue[39;49;00m].$
			[31mstream[39;49;00m [32mnextPutAll:[39;49;00m [31munordered[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 10/24/2000 11:36'![39;49;00m$
[32mnewScriptorAround:[39;49;00m [31maPhraseTileMorph[39;49;00m$
	[37m"Sprout a scriptor around aPhraseTileMorph, thus making a new script.  This is where generalized scriptors will be threaded in"[39;49;00m$
$
	^ [36mnil[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 10/25/2000 17:42'![39;49;00m$
[32mofferViewerMenuForEvt:[39;49;00m [31manEvent[39;49;00m [32mmorph:[39;49;00m [31maMorph[39;49;00m$
	[37m"Offer the viewer's primary menu to the user.  aMorph is some morph within the viewer itself, the one within which a mousedown triggered the need for this menu, and it is used only to retrieve the Viewer itself"[39;49;00m$
$
	[36mself[39;49;00m [32mofferViewerMenuFor:[39;49;00m ([31maMorph[39;49;00m [32mownerThatIsA:[39;49;00m [04m[32mStandardViewer[39;49;00m) [32mevent:[39;49;00m [31manEvent[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/11/2002 02:03'![39;49;00m$
[32mofferViewerMenuFor:[39;49;00m [31maViewer[39;49;00m [32mevent:[39;49;00m [31mevt[39;49;00m$
	[37m"Offer the primary Viewer menu to the user.  Copied up from Player code, but most of the functions suggested here don't work for non-Player objects, many aren't even defined, some relate to exploratory sw work not yet reflected in the current corpus.  We are early in the life cycle of this method..."[39;49;00m$
$
	|[31m aMenu [39;49;00m|$
	[31maMenu[39;49;00m _ [04m[32mMenuMorph[39;49;00m [36mnew[39;49;00m [32mdefaultTarget:[39;49;00m [36mself[39;49;00m.$
	[31maMenu[39;49;00m [32maddStayUpItem[39;49;00m.$
	[31maMenu[39;49;00m [32mtitle:[39;49;00m [33m'**CAUTION -- UNDER CONSTRUCTION!!**[39;49;00m$
[33mMany things may not work!![39;49;00m$
[33m'[39;49;00m[32m,[39;49;00m [36mself[39;49;00m [32mnameForViewer[39;49;00m.$
	([31maViewer[39;49;00m [32maffordsUniclass[39;49;00m [32mand:[39;49;00m [[36mself[39;49;00m [32mbelongsToUniClass[39;49;00m [32mnot[39;49;00m]) [36mifTrue:[39;49;00m$
		[[31maMenu[39;49;00m [32madd:[39;49;00m [33m'give me a Uniclass'[39;49;00m [32maction:[39;49;00m [33m#assureUniClass[39;49;00m.$
		[31maMenu[39;49;00m [32maddLine[39;49;00m].$
	[31maMenu[39;49;00m [32madd:[39;49;00m [33m'choose vocabulary...'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32maction:[39;49;00m [33m#chooseVocabulary[39;49;00m.$
	[31maMenu[39;49;00m [32madd:[39;49;00m [33m'choose limit class...'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32maction:[39;49;00m [33m#chooseLimitClass[39;49;00m.$
	[31maMenu[39;49;00m [32madd:[39;49;00m [33m'add search pane'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32maction:[39;49;00m [33m#addSearchPane[39;49;00m.$
	[31maMenu[39;49;00m [32mballoonTextForLastItem:[39;49;00m [33m'Specify which class should be the most generic one to have its methods shown in this Viewer'[39;49;00m.$
	[31maMenu[39;49;00m [32maddLine[39;49;00m.$
$
	[36mself[39;49;00m [32mbelongsToUniClass[39;49;00m [36mifTrue:[39;49;00m$
		[[31maMenu[39;49;00m [32madd:[39;49;00m [33m'add a new instance variable'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#addInstanceVariableIn:[39;49;00m [32margument:[39;49;00m [31maViewer[39;49;00m.$
		[31maMenu[39;49;00m [32madd:[39;49;00m [33m'add a new script'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32mselector:[39;49;00m [33m#newPermanentScriptIn:[39;49;00m [32margument:[39;49;00m [31maViewer[39;49;00m.$
		[31maMenu[39;49;00m [32maddLine[39;49;00m.$
		[31maMenu[39;49;00m [32madd:[39;49;00m [33m'make my class be first-class'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#makeFirstClassClassIn:[39;49;00m [32margument:[39;49;00m [31maViewer[39;49;00m.$
		[31maMenu[39;49;00m [32madd:[39;49;00m [33m'move my changes up to my superclass'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32maction:[39;49;00m [33m#promoteChangesToSuperclass[39;49;00m.$
		[31maMenu[39;49;00m [32maddLine[39;49;00m].$
$
	[31maMenu[39;49;00m [32madd:[39;49;00m [33m'tear off a tile'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#launchTileToRefer[39;49;00m.$
	[31maMenu[39;49;00m [32maddLine[39;49;00m.$
$
	[31maMenu[39;49;00m [32madd:[39;49;00m [33m'inspect me'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mselector:[39;49;00m [33m#inspect[39;49;00m.$
	[31maMenu[39;49;00m [32madd:[39;49;00m [33m'inspect my class'[39;49;00m [32mtarget:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32maction:[39;49;00m [33m#inspect[39;49;00m.$
	[31maMenu[39;49;00m [32maddLine[39;49;00m.$
$
	[31maMenu[39;49;00m [32madd:[39;49;00m [33m'browse vocabulary'[39;49;00m [32maction:[39;49;00m [33m#haveFullProtocolBrowsed[39;49;00m.$
	[31maMenu[39;49;00m [32madd:[39;49;00m [33m'inspect this Viewer'[39;49;00m [32mtarget:[39;49;00m [31maViewer[39;49;00m [32maction:[39;49;00m [33m#inspect[39;49;00m.$
$
	[31maMenu[39;49;00m [32mpopUpEvent:[39;49;00m [31mevt[39;49;00m [32min:[39;49;00m [31maViewer[39;49;00m [32mcurrentWorld[39;49;00m$
$
[37m"[39;49;00m$
[37m	aMenu add: 'references to me' target: aViewer action: #browseReferencesToObject.[39;49;00m$
[37m	aMenu add: 'toggle scratch pane' target: aViewer selector: #toggleScratchPane.[39;49;00m$
[37m	aMenu add: 'make a nascent script for me' target: aViewer selector: #makeNascentScript.[39;49;00m$
[37m	aMenu add: 'rename me' target: aViewer selector: #chooseNewNameForReference.[39;49;00m$
[37m	aMenu add: 'browse full' action: #browseOwnClassFull.[39;49;00m$
[37m	aMenu add: 'browse hierarchy' action: #browseOwnClassHierarchy.[39;49;00m$
[37m	aMenu add: 'set user level...' target: aViewer action: #setUserLevel.[39;49;00m$
[37m	aMenu add: 'browse sub-protocol' action: #browseOwnClassSubProtocol.[39;49;00m$
[37m	aMenu addLine.[39;49;00m$
[37m[39;49;00m$
[37m"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 1/22/2001 15:20'![39;49;00m$
[32mrenameScript:[39;49;00m [31moldSelector[39;49;00m$
	[37m"prompt the user for a new selector and apply it.  Presently only works for players"[39;49;00m$
$
	[36mself[39;49;00m [32mnotYetImplemented[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/10/2004 11:53'![39;49;00m$
[32mtilePhrasesForCategory:[39;49;00m [31maCategorySymbol[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m$
	[37m"Return a collection of phrases for the category."[39;49;00m$
$
	|[31m interfaces [39;49;00m|$
	[31minterfaces[39;49;00m _ [36mself[39;49;00m [32mmethodInterfacesForCategory:[39;49;00m [31maCategorySymbol[39;49;00m [32minVocabulary:[39;49;00m [31maViewer[39;49;00m [32mcurrentVocabulary[39;49;00m [32mlimitClass:[39;49;00m [31maViewer[39;49;00m [32mlimitClass[39;49;00m.$
	[31minterfaces[39;49;00m _ [36mself[39;49;00m [32mmethodInterfacesInPresentationOrderFrom:[39;49;00m [31minterfaces[39;49;00m [32mforCategory:[39;49;00m [31maCategorySymbol[39;49;00m.$
	^ [36mself[39;49;00m [32mtilePhrasesForMethodInterfaces:[39;49;00m [31minterfaces[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/10/2004 11:53'![39;49;00m$
[32mtilePhrasesForMethodInterfaces:[39;49;00m [31mmethodInterfaceList[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m$
	[37m"Return a collection of ViewerLine objects corresponding to the method-interface list provided.   The resulting list will be in the same order as the incoming list, but may be smaller if the viewer's vocbulary suppresses some of the methods, or if, in classic tiles mode, the selector requires more arguments than can be handled."[39;49;00m$
$
	|[31m toSuppress interfaces resultType itsSelector [39;49;00m|$
	[31mtoSuppress[39;49;00m _ [31maViewer[39;49;00m [32mcurrentVocabulary[39;49;00m [32mphraseSymbolsToSuppress[39;49;00m.$
	[31minterfaces[39;49;00m _ [31mmethodInterfaceList[39;49;00m [32mreject:[39;49;00m [:[31mint[39;49;00m | [31mtoSuppress[39;49;00m [32mincludes:[39;49;00m [31mint[39;49;00m [32mselector[39;49;00m].$
	[04m[32mPreferences[39;49;00m [32muniversalTiles[39;49;00m [36mifFalse:[39;49;00m  [37m"Classic tiles have their limitations..."[39;49;00m$
		[[31minterfaces[39;49;00m _ [31minterfaces[39;49;00m [32mselect:[39;49;00m$
			[:[31mint[39;49;00m |$
				[31mitsSelector[39;49;00m _ [31mint[39;49;00m [32mselector[39;49;00m.$
				[31mitsSelector[39;49;00m [32mnumArgs[39;49;00m [32m<[39;49;00m [34m2[39;49;00m [32mor:[39;49;00m$
					[37m"The lone two-arg loophole in classic tiles"[39;49;00m$
					[[33m#([39;49;00m[33mcolor:sees:[39;49;00m[33m)[39;49;00m [32mincludes:[39;49;00m [31mitsSelector[39;49;00m]]].$
$
	^ [31minterfaces[39;49;00m [32mcollect:[39;49;00m$
		[:[31maMethodInterface[39;49;00m |$
			(([31mresultType[39;49;00m _ [31maMethodInterface[39;49;00m [32mresultType[39;49;00m) [32mnotNil[39;49;00m [32mand:[39;49;00m [[31mresultType[39;49;00m [32m~~[39;49;00m [33m#unknown[39;49;00m]) $
				[36mifTrue:[39;49;00m$
					[[31maViewer[39;49;00m [32mphraseForVariableFrom:[39;49;00m [31maMethodInterface[39;49;00m]$
				[36mifFalse:[39;49;00m$
					[[31maViewer[39;49;00m [32mphraseForCommandFrom:[39;49;00m [31maMethodInterface[39;49;00m]][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 8/10/2004 12:23'![39;49;00m$
[32mtilePhrasesForSelectorList:[39;49;00m [31maList[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m$
	[37m"Particular to the search facility in viewers.  Answer a list, in appropriate order, of ViewerLine objects to put into the viewer."[39;49;00m$
$
	|[31m interfaces aVocab [39;49;00m|$
	[31maVocab[39;49;00m _ [31maViewer[39;49;00m [32mcurrentVocabulary[39;49;00m.$
	[31minterfaces[39;49;00m _ [36mself[39;49;00m$
		[32mmethodInterfacesInPresentationOrderFrom:[39;49;00m$
			([31maList[39;49;00m [32mcollect:[39;49;00m [:[31maSel[39;49;00m | [31maVocab[39;49;00m [32mmethodInterfaceForSelector:[39;49;00m [31maSel[39;49;00m [32mclass:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m])$
		[32mforCategory:[39;49;00m [33m#search[39;49;00m.$
	^ [36mself[39;49;00m [32mtilePhrasesForMethodInterfaces:[39;49;00m [31minterfaces[39;49;00m [32minViewer:[39;49;00m [31maViewer[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 5/4/2001 04:51'![39;49;00m$
[32mtileToRefer[39;49;00m$
	[37m"Answer a reference tile that comprises an alias to me"[39;49;00m$
$
	^ [04m[32mTileMorph[39;49;00m [36mnew[39;49;00m [32msetToReferTo:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sd 3/30/2005 22:04'![39;49;00m$
[32muniqueInstanceVariableNameLike:[39;49;00m [31maString[39;49;00m [32mexcluding:[39;49;00m [31mtakenNames[39;49;00m$
	[37m"Answer a nice instance-variable name to be added to the receiver which resembles aString, making sure it does not coincide with any element in takenNames"[39;49;00m$
$
	|[31m okBase uniqueName usedNames [39;49;00m|$
	[31musedNames[39;49;00m _ [36mself[39;49;00m [32mclass[39;49;00m [32mallInstVarNamesEverywhere[39;49;00m.$
	[31musedNames[39;49;00m [32mremoveAllFoundIn:[39;49;00m [36mself[39;49;00m [32mclass[39;49;00m [32minstVarNames[39;49;00m.$
	[31musedNames[39;49;00m [32maddAll:[39;49;00m [31mtakenNames[39;49;00m.$
	[31mokBase[39;49;00m _ [04m[32mScanner[39;49;00m [32mwellFormedInstanceVariableNameFrom:[39;49;00m [31maString[39;49;00m.$
$
	[31muniqueName[39;49;00m _ [04m[32mUtilities[39;49;00m [32mkeyLike:[39;49;00m [31mokBase[39;49;00m [32msatisfying:[39;49;00m $
		[:[31maKey[39;49;00m | ([31musedNames[39;49;00m [32mincludes:[39;49;00m [31maKey[39;49;00m) [32mnot[39;49;00m].$
$
	^ [31muniqueName[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 11/21/2001 15:16'![39;49;00m$
[32muniqueNameForReference[39;49;00m$
	[37m"Answer a nice name by which the receiver can be referred to by other objects.  At present this uses a global References dictionary to hold the database of references, but in due course this will need to acquire some locality"[39;49;00m$
$
	|[31m aName nameSym stem knownClassVars [39;49;00m|$
	([31maName[39;49;00m _ [36mself[39;49;00m [32muniqueNameForReferenceOrNil[39;49;00m) [32mifNotNil:[39;49;00m [^ [31maName[39;49;00m].$
	([31mstem[39;49;00m _ [36mself[39;49;00m [32mknownName[39;49;00m) [32mifNil:[39;49;00m$
		[[31mstem[39;49;00m _ [36mself[39;49;00m [32mdefaultNameStemForInstances[39;49;00m [32masString[39;49;00m].$
	[31mstem[39;49;00m _ [31mstem[39;49;00m [32mselect:[39;49;00m [:[31mch[39;49;00m | [31mch[39;49;00m [32misLetter[39;49;00m [32mor:[39;49;00m [[31mch[39;49;00m [32misDigit[39;49;00m]].$
	[31mstem[39;49;00m [32msize[39;49;00m [32m==[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m [[31mstem[39;49;00m _ [33m'A'[39;49;00m].$
	[31mstem[39;49;00m [32mfirst[39;49;00m [32misLetter[39;49;00m [36mifFalse:[39;49;00m$
		[[31mstem[39;49;00m _ [33m'A'[39;49;00m[32m,[39;49;00m [31mstem[39;49;00m].$
	[31mstem[39;49;00m _ [31mstem[39;49;00m [32mcapitalized[39;49;00m.$
	[31mknownClassVars[39;49;00m _ [04m[32mScriptingSystem[39;49;00m [32mallKnownClassVariableNames[39;49;00m.$
	[31maName[39;49;00m _ [04m[32mUtilities[39;49;00m [32mkeyLike:[39;49;00m  [31mstem[39;49;00m [32msatisfying:[39;49;00m$
		[:[31mjinaLake[39;49;00m |$
			[31mnameSym[39;49;00m _ [31mjinaLake[39;49;00m [32masSymbol[39;49;00m.$
			 (([04m[32mReferences[39;49;00m [32mincludesKey:[39;49;00m  [31mnameSym[39;49;00m) [32mnot[39;49;00m [32mand:[39;49;00m$
				[([04m[32mSmalltalk[39;49;00m [32mincludesKey:[39;49;00m [31mnameSym[39;49;00m) [32mnot[39;49;00m]) [32mand:[39;49;00m$
						[([31mknownClassVars[39;49;00m [32mincludes:[39;49;00m [31mnameSym[39;49;00m) [32mnot[39;49;00m]].$
$
	[04m[32mReferences[39;49;00m [32mat:[39;49;00m ([31maName[39;49;00m _ [31maName[39;49;00m [32masSymbol[39;49;00m) [32mput:[39;49;00m [36mself[39;49;00m.$
	^ [31maName[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'md 1/17/2006 17:58'![39;49;00m$
[32muniqueNameForReferenceFrom:[39;49;00m [31mproposedName[39;49;00m$
	[37m"Answer a satisfactory symbol, similar to the proposedName but obeying the rules, to represent the receiver"[39;49;00m$
$
	|[31m aName nameSym stem okay [39;49;00m|$
	[31mproposedName[39;49;00m [32m=[39;49;00m [36mself[39;49;00m [32muniqueNameForReferenceOrNil[39;49;00m $
		[36mifTrue:[39;49;00m [^ [31mproposedName[39;49;00m].  [37m"No change"[39;49;00m$
$
	[31mstem[39;49;00m _ [31mproposedName[39;49;00m [32mselect:[39;49;00m [:[31mch[39;49;00m | [31mch[39;49;00m [32misLetter[39;49;00m [32mor:[39;49;00m [[31mch[39;49;00m [32misDigit[39;49;00m]].$
	[31mstem[39;49;00m [32msize[39;49;00m [32m==[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m [[31mstem[39;49;00m _ [33m'A'[39;49;00m].$
	[31mstem[39;49;00m [32mfirst[39;49;00m [32misLetter[39;49;00m [36mifFalse:[39;49;00m$
		[[31mstem[39;49;00m _ [33m'A'[39;49;00m[32m,[39;49;00m [31mstem[39;49;00m].$
	[31mstem[39;49;00m _ [31mstem[39;49;00m [32mcapitalized[39;49;00m.$
	[31maName[39;49;00m _ [04m[32mUtilities[39;49;00m [32mkeyLike:[39;49;00m [31mstem[39;49;00m [32msatisfying:[39;49;00m$
		[:[31mjinaLake[39;49;00m |$
			[31mnameSym[39;49;00m _ [31mjinaLake[39;49;00m [32masSymbol[39;49;00m.$
			[31mokay[39;49;00m _ [36mtrue[39;49;00m.$
			([36mself[39;49;00m [32mclass[39;49;00m [32mbindingOf:[39;49;00m [31mnameSym[39;49;00m) [32mifNotNil:[39;49;00m [[31mokay[39;49;00m _ [36mfalse[39;49;00m [37m"don't use it"[39;49;00m].$
			[31mokay[39;49;00m].$
	^ [31maName[39;49;00m [32masSymbol[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 3/15/2004 23:01'![39;49;00m$
[32muniqueNameForReferenceOrNil[39;49;00m$
	[37m"If the receiver has a unique name for reference, return it here, else return nil"[39;49;00m$
$
	^ [04m[32mReferences[39;49;00m [32mkeyAtValue:[39;49;00m [36mself[39;49;00m [32mifAbsent:[39;49;00m [[36mnil[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'ar 5/16/2001 01:40'![39;49;00m$
[32mupdateThresholdForGraphicInViewerTab[39;49;00m$
	[37m"When a Viewer is open on the receiver, its tab needs some graphic to show to the user. Computing this graphic can take quite some time so we want to make the update frequency depending on how long it takes to compute the thumbnail. The threshold returned by this method defines that the viewer will update at most every 'threshold * timeItTakesToDraw' milliseconds. Thus, if the time for computing the receiver's thumbnail is 200 msecs and the the threshold is 10, the viewer will update at most every two seconds."[39;49;00m$
	^[34m20[39;49;00m [37m"seems to be a pretty good general choice"[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'viewer'[39;49;00m[34m stamp: 'sw 3/9/2001 13:48'![39;49;00m$
[32musableMethodInterfacesIn:[39;49;00m [31maListOfMethodInterfaces[39;49;00m$
	[37m"Filter aList, returning a subset list of apt phrases"[39;49;00m$
$
	^ [31maListOfMethodInterfaces[39;49;00m$
[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'world hacking'[39;49;00m[34m stamp: 'ar 3/17/2001 23:45'![39;49;00m$
[32mcouldOpenInMorphic[39;49;00m$
$
        [37m"is there an obvious morphic world in which to open a new morph?"[39;49;00m$
$
        ^[04m[32mWorld[39;49;00m [32mnotNil[39;49;00m [32mor:[39;49;00m [[04m[32mActiveWorld[39;49;00m [32mnotNil[39;49;00m][34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m![39;49;00m$
[32merrorImproperStore[39;49;00m$
	[37m"Create an error notification that an improper store was attempted."[39;49;00m$
$
	[36mself[39;49;00m [32merror:[39;49;00m [33m'Improper store into indexable object'[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m![39;49;00m$
[32merrorNonIntegerIndex[39;49;00m$
	[37m"Create an error notification that an improper object was used as an index."[39;49;00m$
$
	[36mself[39;49;00m [32merror:[39;49;00m [33m'only integers should be used as indices'[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m stamp: 'yo 6/29/2004 11:37'![39;49;00m$
[32merrorNotIndexable[39;49;00m$
	[37m"Create an error notification that the receiver is not indexable."[39;49;00m$
$
	[36mself[39;49;00m [32merror:[39;49;00m ([33m'Instances of {1} are not indexable'[39;49;00m [32mtranslated[39;49;00m [32mformat:[39;49;00m {[36mself[39;49;00m [32mclass[39;49;00m [32mname[39;49;00m})[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m![39;49;00m$
[32merrorSubscriptBounds:[39;49;00m [31mindex[39;49;00m $
	[37m"Create an error notification that an improper integer was used as an index."[39;49;00m$
$
	[36mself[39;49;00m [32merror:[39;49;00m [33m'subscript is out of bounds: '[39;49;00m [32m,[39;49;00m [31mindex[39;49;00m [32mprintString[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m stamp: 'ar 2/6/2004 14:47'![39;49;00m$
[32mprimitiveError:[39;49;00m [31maString[39;49;00m $
	[37m"This method is called when the error handling results in a recursion in [39;49;00m$
[37m	calling on error: or halt or halt:."[39;49;00m$
$
	|[31m context [39;49;00m|$
	([04m[32mString[39;49;00m$
		[32mstreamContents:[39;49;00m $
			[:[31ms[39;49;00m |$
			[31ms[39;49;00m [32mnextPutAll:[39;49;00m [33m'***System error handling failed***'[39;49;00m.$
			[31ms[39;49;00m [32mcr[39;49;00m; [32mnextPutAll:[39;49;00m [31maString[39;49;00m.$
			[31mcontext[39;49;00m _ [36mthisContext[39;49;00m [32msender[39;49;00m [32msender[39;49;00m.$
			[34m20[39;49;00m [36mtimesRepeat:[39;49;00m [[31mcontext[39;49;00m [32m==[39;49;00m [36mnil[39;49;00m [36mifFalse:[39;49;00m [[31ms[39;49;00m [32mcr[39;49;00m; [32mprint:[39;49;00m ([31mcontext[39;49;00m _ [31mcontext[39;49;00m [32msender[39;49;00m)]].$
			[31ms[39;49;00m [32mcr[39;49;00m; [32mnextPutAll:[39;49;00m [33m'-------------------------------'[39;49;00m.$
			[31ms[39;49;00m [32mcr[39;49;00m; [32mnextPutAll:[39;49;00m [33m'Type CR to enter an emergency evaluator.'[39;49;00m.$
			[31ms[39;49;00m [32mcr[39;49;00m; [32mnextPutAll:[39;49;00m [33m'Type any other character to restart.'[39;49;00m])$
		[32mdisplayAt:[39;49;00m [34m0[39;49;00m [32m@[39;49;00m [34m0[39;49;00m.$
	[[04m[32mSensor[39;49;00m [32mkeyboardPressed[39;49;00m] [32mwhileFalse[39;49;00m.$
	[04m[32mSensor[39;49;00m [32mkeyboard[39;49;00m [32m=[39;49;00m [04m[32mCharacter[39;49;00m [32mcr[39;49;00m [36mifTrue:[39;49;00m [[04m[32mTranscripter[39;49;00m [32memergencyEvaluator[39;49;00m].$
	[04m[32mSmalltalk[39;49;00m [32misMorphic[39;49;00m$
		[36mifTrue:[39;49;00m [[04m[32mWorld[39;49;00m [32minstall[39;49;00m [37m"init hands and redisplay"[39;49;00m]$
		[36mifFalse:[39;49;00m [[04m[32mScheduledControllers[39;49;00m [32msearchForActiveController[39;49;00m][34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m![39;49;00m$
[32mspecies[39;49;00m$
	[37m"Answer the preferred class for reconstructing the receiver.  For example, [39;49;00m$
[37m	collections create new collections whenever enumeration messages such as [39;49;00m$
[37m	collect: or select: are invoked.  The new kind of collection is determined by [39;49;00m$
[37m	the species of the original collection.  Species and class are not always the [39;49;00m$
[37m	same.  For example, the species of Interval is Array."[39;49;00m$
$
	^[36mself[39;49;00m [32mclass[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m![39;49;00m$
[32mstoreAt:[39;49;00m [31moffset[39;49;00m [32minTempFrame:[39;49;00m [31maContext[39;49;00m$
	[37m"This message had to get sent to an expression already on the stack[39;49;00m$
[37m	as a Block argument being accessed by the debugger.[39;49;00m$
[37m	Just re-route it to the temp frame."[39;49;00m$
	^ [31maContext[39;49;00m [32mtempAt:[39;49;00m [31moffset[39;49;00m [32mput:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
[34m"-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- "![39;49;00m$
$
[04m[32mObject class[39;49;00m[34m[39;49;00m$
[34m	instanceVariableNames: [39;49;00m[33m''[39;49;00m[34m![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'*Pinesoft-Widgets'[39;49;00m[34m stamp: 'gvc 4/17/2007 17:40'![39;49;00m$
[32mtaskbarIcon[39;49;00m$
	[37m"Answer the icon for an instance of the receiver in a task bar[39;49;00m$
[37m	or nil for the default."[39;49;00m$
$
	^[36mnil[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'*magritte-model-accessing'[39;49;00m[34m stamp: 'lr 3/27/2006 15:47'![39;49;00m$
[32mdescription[39;49;00m$
	^ [04m[32mMADescriptionBuilder[39;49;00m [32mfor:[39;49;00m [36mself[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'class initialization'[39;49;00m[34m stamp: 'ar 2/11/2001 02:00'![39;49;00m$
[32mflushDependents[39;49;00m$
	[04m[32mDependentsFields[39;49;00m [32mkeysAndValuesDo:[39;49;00m[:[31mkey[39;49;00m :[31mdep[39;49;00m|$
		[31mkey[39;49;00m [32mifNotNil:[39;49;00m[[31mkey[39;49;00m [32mremoveDependent:[39;49;00m [36mnil[39;49;00m].$
	].$
	[04m[32mDependentsFields[39;49;00m [32mfinalizeValues[39;49;00m.[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'class initialization'[39;49;00m[34m stamp: 'rw 2/10/2002 13:09'![39;49;00m$
[32mflushEvents[39;49;00m$
	[37m"Object flushEvents"[39;49;00m$
$
	[04m[32mEventManager[39;49;00m [32mflushEvents[39;49;00m. [34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'class initialization'[39;49;00m[34m stamp: 'rww 10/2/2001 07:35'![39;49;00m$
[32minitialize[39;49;00m$
	[37m"Object initialize"[39;49;00m$
	[04m[32mDependentsFields[39;49;00m [32mifNil:[39;49;00m[[36mself[39;49;00m [32minitializeDependentsFields[39;49;00m].[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'class initialization'[39;49;00m[34m stamp: 'ar 2/11/2001 01:41'![39;49;00m$
[32minitializeDependentsFields[39;49;00m$
	[37m"Object initialize"[39;49;00m$
	[04m[32mDependentsFields[39;49;00m _ [04m[32mWeakIdentityKeyDictionary[39;49;00m [36mnew[39;49;00m.$
[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'class initialization'[39;49;00m[34m stamp: 'ar 2/11/2001 01:45'![39;49;00m$
[32mreInitializeDependentsFields[39;49;00m$
	[37m"Object reInitializeDependentsFields"[39;49;00m$
	|[31m oldFields [39;49;00m|$
	[31moldFields[39;49;00m _ [04m[32mDependentsFields[39;49;00m.$
	[04m[32mDependentsFields[39;49;00m _ [04m[32mWeakIdentityKeyDictionary[39;49;00m [36mnew[39;49;00m.$
	[31moldFields[39;49;00m [32mkeysAndValuesDo:[39;49;00m[:[31mobj[39;49;00m :[31mdeps[39;49;00m|$
		[31mdeps[39;49;00m [32mdo:[39;49;00m[:[31md[39;49;00m| [31mobj[39;49;00m [32maddDependent:[39;49;00m [31md[39;49;00m]].$
[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'documentation'[39;49;00m[34m![39;49;00m$
[32mhowToModifyPrimitives[39;49;00m$
	[37m"You are allowed to write methods which specify primitives, but please use [39;49;00m$
[37m	caution.  If you make a subclass of a class which contains a primitive method, [39;49;00m$
[37m	the subclass inherits the primitive.  The message which is implemented [39;49;00m$
[37m	primitively may be overridden in the subclass (E.g., see at:put: in String's [39;49;00m$
[37m	subclass Symbol).  The primitive behavior can be invoked using super (see [39;49;00m$
[37m	Symbol string:). [39;49;00m$
[37m	 [39;49;00m$
[37m	A class which attempts to mimic the behavior of another class without being [39;49;00m$
[37m	its subclass may or may not be able to use the primitives of the original class.  [39;49;00m$
[37m	In general, if the instance variables read or written by a primitive have the [39;49;00m$
[37m	same meanings and are in the same fields in both classes, the primitive will [39;49;00m$
[37m	work.  [39;49;00m$
[37m[39;49;00m$
[37m	For certain frequently used 'special selectors', the compiler emits a [39;49;00m$
[37m	send-special-selector bytecode instead of a send-message bytecode.  [39;49;00m$
[37m	Special selectors were created because they offer two advantages.  Code [39;49;00m$
[37m	which sends special selectors compiles into fewer bytes than normal.  For [39;49;00m$
[37m	some pairs of receiver classes and special selectors, the interpreter jumps [39;49;00m$
[37m	directly to a primitive routine without looking up the method in the class.  [39;49;00m$
[37m	This is much faster than a normal message lookup. [39;49;00m$
[37m	 [39;49;00m$
[37m	A selector which is a special selector solely in order to save space has a [39;49;00m$
[37m	normal behavior.  Methods whose selectors are special in order to [39;49;00m$
[37m	gain speed contain the comment, 'No Lookup'.  When the interpreter [39;49;00m$
[37m	encounters a send-special-selector bytecode, it checks the class of the [39;49;00m$
[37m	receiver and the selector.  If the class-selector pair is a no-lookup pair, [39;49;00m$
[37m	then the interpreter swiftly jumps to the routine which implements the [39;49;00m$
[37m	corresponding primitive.  (A special selector whose receiver is not of the [39;49;00m$
[37m	right class to make a no-lookup pair, is looked up normally).  The pairs are [39;49;00m$
[37m	listed below.  No-lookup methods contain a primitive number specification, [39;49;00m$
[37m	<primitive: xx>, which is redundant.  Since the method is not normally looked [39;49;00m$
[37m	up, deleting the primitive number specification cannot prevent this [39;49;00m$
[37m	primitive from running.  If a no-lookup primitive fails, the method is looked [39;49;00m$
[37m	up normally, and the expressions in it are executed. [39;49;00m$
[37m	 [39;49;00m$
[37m	No Lookup pairs of (class, selector) [39;49;00m$
[37m	 [39;49;00m$
[37m	SmallInteger with any of		+ - * /  \\  bitOr: bitShift: bitAnd:  // [39;49;00m$
[37m	SmallInteger with any of		=  ~=  >  <  >=  <= [39;49;00m$
[37m	Any class with					== [39;49;00m$
[37m	Any class with 					@ [39;49;00m$
[37m	Point with either of				x y [39;49;00m$
[37m	ContextPart with					blockCopy: [39;49;00m$
[37m	BlockContext with either of 		value value:[39;49;00m$
[37m	"[39;49;00m$
$
	[36mself[39;49;00m [32merror:[39;49;00m [33m'comment only'[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'documentation'[39;49;00m[34m![39;49;00m$
[32mwhatIsAPrimitive[39;49;00m$
	[37m"Some messages in the system are responded to primitively. A primitive   [39;49;00m$
[37m	response is performed directly by the interpreter rather than by evaluating   [39;49;00m$
[37m	expressions in a method. The methods for these messages indicate the   [39;49;00m$
[37m	presence of a primitive response by including <primitive: xx> before the   [39;49;00m$
[37m	first expression in the method.   [39;49;00m$
[37m	  [39;49;00m$
[37m	Primitives exist for several reasons. Certain basic or 'primitive' [39;49;00m$
[37m	operations cannot be performed in any other way. Smalltalk without [39;49;00m$
[37m	primitives can move values from one variable to another, but cannot add two [39;49;00m$
[37m	SmallIntegers together. Many methods for arithmetic and comparison [39;49;00m$
[37m	between numbers are primitives. Some primitives allow Smalltalk to [39;49;00m$
[37m	communicate with I/O devices such as the disk, the display, and the keyboard. [39;49;00m$
[37m	Some primitives exist only to make the system run faster; each does the same [39;49;00m$
[37m	thing as a certain Smalltalk method, and its implementation as a primitive is [39;49;00m$
[37m	optional.  [39;49;00m$
[37m	  [39;49;00m$
[37m	When the Smalltalk interpreter begins to execute a method which specifies a [39;49;00m$
[37m	primitive response, it tries to perform the primitive action and to return a [39;49;00m$
[37m	result. If the routine in the interpreter for this primitive is successful, [39;49;00m$
[37m	it will return a value and the expressions in the method will not be evaluated. [39;49;00m$
[37m	If the primitive routine is not successful, the primitive 'fails', and the [39;49;00m$
[37m	Smalltalk expressions in the method are executed instead. These [39;49;00m$
[37m	expressions are evaluated as though the primitive routine had not been [39;49;00m$
[37m	called.  [39;49;00m$
[37m	  [39;49;00m$
[37m	The Smalltalk code that is evaluated when a primitive fails usually [39;49;00m$
[37m	anticipates why that primitive might fail. If the primitive is optional, the [39;49;00m$
[37m	expressions in the method do exactly what the primitive would have done (See [39;49;00m$
[37m	Number @). If the primitive only works on certain classes of arguments, the [39;49;00m$
[37m	Smalltalk code tries to coerce the argument or appeals to a superclass to find [39;49;00m$
[37m	a more general way of doing the operation (see SmallInteger +). If the [39;49;00m$
[37m	primitive is never supposed to fail, the expressions signal an error (see [39;49;00m$
[37m	SmallInteger asFloat).  [39;49;00m$
[37m	  [39;49;00m$
[37m	Each method that specifies a primitive has a comment in it. If the primitive is [39;49;00m$
[37m	optional, the comment will say 'Optional'. An optional primitive that is not [39;49;00m$
[37m	implemented always fails, and the Smalltalk expressions do the work [39;49;00m$
[37m	instead.  [39;49;00m$
[37m	 [39;49;00m$
[37m	If a primitive is not optional, the comment will say, 'Essential'. Some [39;49;00m$
[37m	methods will have the comment, 'No Lookup'. See Object [39;49;00m$
[37m	howToModifyPrimitives for an explanation of special selectors which are [39;49;00m$
[37m	not looked up.  [39;49;00m$
[37m	  [39;49;00m$
[37m	For the primitives for +, -, *, and bitShift: in SmallInteger, and truncated [39;49;00m$
[37m	in Float, the primitive constructs and returns a 16-bit [39;49;00m$
[37m	LargePositiveInteger when the result warrants it. Returning 16-bit [39;49;00m$
[37m	LargePositiveIntegers from these primitives instead of failing is [39;49;00m$
[37m	optional in the same sense that the LargePositiveInteger arithmetic [39;49;00m$
[37m	primitives are optional. The comments in the SmallInteger primitives say, [39;49;00m$
[37m	'Fails if result is not a SmallInteger', even though the implementor has the [39;49;00m$
[37m	option to construct a LargePositiveInteger. For further information on [39;49;00m$
[37m	primitives, see the 'Primitive Methods' part of the chapter on the formal [39;49;00m$
[37m	specification of the interpreter in the Smalltalk book."[39;49;00m$
$
	[36mself[39;49;00m [32merror:[39;49;00m [33m'comment only'[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'file list services'[39;49;00m[34m stamp: 'nk 6/12/2004 11:41'![39;49;00m$
[32mfileReaderServicesForDirectory:[39;49;00m [31maFileDirectory[39;49;00m$
	[37m"Backstop"[39;49;00m$
	^[33m#([39;49;00m[33m)[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'file list services'[39;49;00m[34m stamp: 'nk 6/12/2004 11:30'![39;49;00m$
[32mfileReaderServicesForFile:[39;49;00m [31mfullName[39;49;00m [32msuffix:[39;49;00m [31msuffix[39;49;00m$
	[37m"Backstop"[39;49;00m$
	^[33m#([39;49;00m[33m)[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'file list services'[39;49;00m[34m stamp: 'md 2/15/2006 17:20'![39;49;00m$
[32mservices[39;49;00m$
	[37m"Backstop"[39;49;00m$
	^[33m#([39;49;00m[33m)[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 1/23/2003 09:45'![39;49;00m$
[32mcategoryForUniclasses[39;49;00m$
	[37m"Answer the default system category into which to place unique-class instances"[39;49;00m$
$
	^ [33m'UserObjects'[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 7/28/97 15:56'![39;49;00m$
[32mchooseUniqueClassName[39;49;00m$
	|[31m i className [39;49;00m|$
	[31mi[39;49;00m _ [34m1[39;49;00m.$
	[[31mclassName[39;49;00m _ ([36mself[39;49;00m [32mname[39;49;00m [32m,[39;49;00m [31mi[39;49;00m [32mprintString[39;49;00m) [32masSymbol[39;49;00m.$
	 [04m[32mSmalltalk[39;49;00m [32mincludesKey:[39;49;00m [31mclassName[39;49;00m]$
		[36mwhileTrue:[39;49;00m [[31mi[39;49;00m _ [31mi[39;49;00m [32m+[39;49;00m [34m1[39;49;00m].$
	^ [31mclassName[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'tk 8/22/1998 08:22'![39;49;00m$
[32minitialInstance[39;49;00m$
	[37m"Answer the first instance of the receiver, generate an error if there is one already"[39;49;00m$
	[37m"self instanceCount > 0 ifTrue: [self error: 'instance(s) already exist.']."[39;49;00m$
		[37m"Debugging test that is very slow"[39;49;00m$
	^ [36mself[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 5/5/2000 09:30'![39;49;00m$
[32minitializedInstance[39;49;00m$
	^ [36mself[39;49;00m [36mnew[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 10/16/2000 10:58'![39;49;00m$
[32minstanceOfUniqueClass[39;49;00m$
	[37m"Answer an instance of a unique subclass of the receiver"[39;49;00m$
$
	^ [36mself[39;49;00m [32minstanceOfUniqueClassWithInstVarString:[39;49;00m [33m''[39;49;00m [32mandClassInstVarString:[39;49;00m [33m''[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'tk 8/22/1998 08:27'![39;49;00m$
[32minstanceOfUniqueClassWithInstVarString:[39;49;00m [31minstVarString[39;49;00m [32mandClassInstVarString:[39;49;00m [31mclassInstVarString[39;49;00m$
	[37m"Create a unique class for the receiver, and answer an instance of it"[39;49;00m$
$
	^ ([36mself[39;49;00m [32mnewUniqueClassInstVars:[39;49;00m [31minstVarString[39;49;00m $
		[32mclassInstVars:[39;49;00m [31mclassInstVarString[39;49;00m) [32minitialInstance[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 10/23/1999 22:51'![39;49;00m$
[32misUniClass[39;49;00m$
	^ [36mfalse[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'ajh 5/23/2002 00:35'![39;49;00m$
[32mnewFrom:[39;49;00m [31maSimilarObject[39;49;00m$
	[37m"Create an object that has similar contents to aSimilarObject.[39;49;00m$
[37m	If the classes have any instance varaibles with the same names, copy them across.[39;49;00m$
[37m	If this is bad for a class, override this method."[39;49;00m$
$
	^ ([36mself[39;49;00m [32misVariable[39;49;00m$
		[36mifTrue:[39;49;00m [[36mself[39;49;00m [32mbasicNew:[39;49;00m [31maSimilarObject[39;49;00m [32mbasicSize[39;49;00m]$
		[36mifFalse:[39;49;00m [[36mself[39;49;00m [32mbasicNew[39;49;00m]$
	  ) [32mcopySameFrom:[39;49;00m [31maSimilarObject[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'tk 6/29/1998 12:11'![39;49;00m$
[32mnewUniqueClassInstVars:[39;49;00m [31minstVarString[39;49;00m [32mclassInstVars:[39;49;00m [31mclassInstVarString[39;49;00m$
	[37m"Create a unique class for the receiver"[39;49;00m$
$
	|[31m aName aClass [39;49;00m|$
	[36mself[39;49;00m [32misSystemDefined[39;49;00m [36mifFalse:[39;49;00m$
		[^ [31msuperclass[39;49;00m [32mnewUniqueClassInstVars:[39;49;00m [31minstVarString[39;49;00m [32mclassInstVars:[39;49;00m [31mclassInstVarString[39;49;00m].$
	[31maName[39;49;00m _ [36mself[39;49;00m [32mchooseUniqueClassName[39;49;00m.$
	[31maClass[39;49;00m _ [36mself[39;49;00m [32msubclass:[39;49;00m [31maName[39;49;00m [32minstanceVariableNames:[39;49;00m [31minstVarString[39;49;00m $
		[32mclassVariableNames:[39;49;00m [33m''[39;49;00m [32mpoolDictionaries:[39;49;00m [33m''[39;49;00m [32mcategory:[39;49;00m [36mself[39;49;00m [32mcategoryForUniclasses[39;49;00m.$
	[31mclassInstVarString[39;49;00m [32msize[39;49;00m [32m>[39;49;00m [34m0[39;49;00m [36mifTrue:[39;49;00m$
		[[31maClass[39;49;00m [32mclass[39;49;00m [32minstanceVariableNames:[39;49;00m [31mclassInstVarString[39;49;00m].$
	^ [31maClass[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'sw 7/28/97 15:56'![39;49;00m$
[32mnewUserInstance[39;49;00m$
	[37m"Answer an instance of an appropriate class to serve as a user object in the containment hierarchy"[39;49;00m$
$
	^ [36mself[39;49;00m [32minstanceOfUniqueClass[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'nk 8/30/2004 07:57'![39;49;00m$
[32mreadCarefullyFrom:[39;49;00m [31mtextStringOrStream[39;49;00m$
	[37m"Create an object based on the contents of textStringOrStream.  Return an error instead of putting up a SyntaxError window."[39;49;00m$
$
	|[31m object [39;49;00m|$
	([04m[32mCompiler[39;49;00m [32mcouldEvaluate:[39;49;00m [31mtextStringOrStream[39;49;00m)$
		[36mifFalse:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'expected String, Stream, or Text'[39;49;00m].$
	[31mobject[39;49;00m _ [04m[32mCompiler[39;49;00m [32mevaluate:[39;49;00m [31mtextStringOrStream[39;49;00m [32mfor:[39;49;00m [36mnil[39;49;00m $
				[32mnotifying:[39;49;00m [33m#error:[39;49;00m [37m"signal we want errors"[39;49;00m [32mlogged:[39;49;00m [36mfalse[39;49;00m.$
	([31mobject[39;49;00m [32misKindOf:[39;49;00m [36mself[39;49;00m) [36mifFalse:[39;49;00m [[36mself[39;49;00m [32merror:[39;49;00m [36mself[39;49;00m [32mname[39;49;00m[32m,[39;49;00m [33m' expected'[39;49;00m].$
	^[31mobject[39;49;00m[34m! ![39;49;00m$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'instance creation'[39;49;00m[34m stamp: 'nk 8/30/2004 07:57'![39;49;00m$
[32mreadFrom:[39;49;00m [31mtextStringOrStream[39;49;00m$
	[37m"Create an object based on the contents of textStringOrStream."[39;49;00m$
$
	|[31m object [39;49;00m|$
	([04m[32mCompiler[39;49;00m [32mcouldEvaluate:[39;49;00m [31mtextStringOrStream[39;49;00m)$
		[36mifFalse:[39;49;00m [^ [36mself[39;49;00m [32merror:[39;49;00m [33m'expected String, Stream, or Text'[39;49;00m].$
	[31mobject[39;49;00m _ [04m[32mCompiler[39;49;00m [32mevaluate:[39;49;00m [31mtextStringOrStream[39;49;00m.$
	([31mobject[39;49;00m [32misKindOf:[39;49;00m [36mself[39;49;00m) [36mifFalse:[39;49;00m [[36mself[39;49;00m [32merror:[39;49;00m [36mself[39;49;00m [32mname[39;49;00m[32m,[39;49;00m [33m' expected'[39;49;00m].$
	^[31mobject[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'objects from disk'[39;49;00m[34m stamp: 'tk 1/8/97'![39;49;00m$
[32mcreateFrom:[39;49;00m [31maSmartRefStream[39;49;00m [32msize:[39;49;00m [31mvarsOnDisk[39;49;00m [32mversion:[39;49;00m [31minstVarList[39;49;00m$
	[37m"Create an instance of me so objects on the disk can be read in.  Tricky part is computing the size if variable.  Inst vars will be filled in later.  "[39;49;00m$
$
	^ [36mself[39;49;00m [32misVariable[39;49;00m$
		[36mifFalse:[39;49;00m [[36mself[39;49;00m [32mbasicNew[39;49;00m]$
		[36mifTrue:[39;49;00m [[37m"instVarList is names of old class's inst vars plus a version number"[39;49;00m $
				[36mself[39;49;00m [32mbasicNew:[39;49;00m ([31mvarsOnDisk[39;49;00m [32m-[39;49;00m ([31minstVarList[39;49;00m [32msize[39;49;00m [32m-[39;49;00m [34m1[39;49;00m))]$
[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'window color'[39;49;00m[34m stamp: 'nk 6/10/2004 08:10'![39;49;00m$
[32mwindowColorSpecification[39;49;00m$
	[37m"Answer a WindowColorSpec object that declares my preference.[39;49;00m$
[37m	This is a backstop for classes that don't otherwise define a preference."[39;49;00m$
$
	^ [04m[32mWindowColorSpec[39;49;00m [32mclassSymbol:[39;49;00m [36mself[39;49;00m [32mname[39;49;00m$
		[32mwording:[39;49;00m [33m'Default'[39;49;00m [32mbrightColor:[39;49;00m [33m#white[39;49;00m$
		[32mpastelColor:[39;49;00m [33m#white[39;49;00m$
		[32mhelpMessage:[39;49;00m [33m'Other windows without color preferences.'[39;49;00m[34m! ![39;49;00m$
$
$
[34m![39;49;00m[04m[32mObject class[39;49;00m[34m methodsFor: [39;49;00m[33m'private'[39;49;00m[34m stamp: 'mir 8/22/2001 15:20'![39;49;00m$
[32mreleaseExternalSettings[39;49;00m$
	[37m"Do nothing as a default"[39;49;00m[34m! ![39;49;00m$
$
$
[04m[32mObject[39;49;00m [32minitialize[39;49;00m[32m![39;49;00m$
