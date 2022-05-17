     1	[37m--[[[39;49;00m$
     2	[37m	Auctioneer Advanced[39;49;00m$
     3	[37m	Version: <%version%> (<%codename%>)[39;49;00m$
     4	[37m	Revision: $Id: CoreMain.lua 2233 2007-09-25 03:57:33Z norganna $[39;49;00m$
     5	[37m	URL: http://auctioneeraddon.com/[39;49;00m$
     6	[37m[39;49;00m$
     7	[37m	This is an addon for World of Warcraft that adds statistical history to the auction data that is collected[39;49;00m$
     8	[37m	when the auction is scanned, so that you can easily determine what price[39;49;00m$
     9	[37m	you will be able to sell an item for at auction or at a vendor whenever you[39;49;00m$
    10	[37m	mouse-over an item in the game[39;49;00m$
    11	[37m[39;49;00m$
    12	[37m	License:[39;49;00m$
    13	[37m		This program is free software; you can redistribute it and/or[39;49;00m$
    14	[37m		modify it under the terms of the GNU General Public License[39;49;00m$
    15	[37m		as published by the Free Software Foundation; either version 2[39;49;00m$
    16	[37m		of the License, or (at your option) any later version.[39;49;00m$
    17	[37m[39;49;00m$
    18	[37m		This program is distributed in the hope that it will be useful,[39;49;00m$
    19	[37m		but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m$
    20	[37m		MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the[39;49;00m$
    21	[37m		GNU General Public License for more details.[39;49;00m$
    22	[37m[39;49;00m$
    23	[37m		You should have received a copy of the GNU General Public License[39;49;00m$
    24	[37m		along with this program(see GPL.txt); if not, write to the Free Software[39;49;00m$
    25	[37m		Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.[39;49;00m$
    26	[37m[39;49;00m$
    27	[37m	Note:[39;49;00m$
    28	[37m		This AddOn's source code is specifically designed to work with[39;49;00m$
    29	[37m		World of Warcraft's interpreted AddOn system.[39;49;00m$
    30	[37m		You have an implicit licence to use this AddOn with these facilities[39;49;00m$
    31	[37m		since that is its designated purpose as per:[39;49;00m$
    32	[37m		http://www.fsf.org/licensing/licenses/gpl-faq.html#InterpreterIncompat[39;49;00m$
    33	[37m]][39;49;00m$
    34	$
    35	$
    36	[37m--[[[39;49;00m$
    37	[37m	See CoreAPI.lua for a description of the modules API[39;49;00m$
    38	[37m]][39;49;00m$
    39	$
    40	[34mif[39;49;00m ([35mnot[39;49;00m AucAdvanced) [34mthen[39;49;00m AucAdvanced = {} [34mend[39;49;00m$
    41	[34mif[39;49;00m ([35mnot[39;49;00m AucAdvancedData) [34mthen[39;49;00m AucAdvancedData = {} [34mend[39;49;00m$
    42	[34mif[39;49;00m ([35mnot[39;49;00m AucAdvancedLocal) [34mthen[39;49;00m AucAdvancedLocal = {} [34mend[39;49;00m$
    43	[34mif[39;49;00m ([35mnot[39;49;00m AucAdvancedConfig) [34mthen[39;49;00m AucAdvancedConfig = {} [34mend[39;49;00m$
    44	$
    45	AucAdvanced.Version=[33m"[39;49;00m[33m<%version%>[39;49;00m[33m"[39;49;00m;$
    46	[34mif[39;49;00m (AucAdvanced.Version == [33m"[39;49;00m[33m<[39;49;00m[33m"[39;49;00m..[33m"[39;49;00m[33m%version%>[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m$
    47		AucAdvanced.Version = [33m"[39;49;00m[33m5.0.DEV[39;49;00m[33m"[39;49;00m;$
    48	[34mend[39;49;00m$
    49	$
    50	[34mlocal[39;49;00m private = {}$
    51	$
    52	[37m-- For our modular stats system, each stats engine should add their[39;49;00m$
    53	[37m-- subclass to AucAdvanced.Modules.<type>.<name> and store their data into their own[39;49;00m$
    54	[37m-- data table in AucAdvancedData.Stats.<type><name>[39;49;00m$
    55	[34mif[39;49;00m ([35mnot[39;49;00m AucAdvanced.Modules) [34mthen[39;49;00m AucAdvanced.Modules = {Stat={},Util={},Filter={}} [34mend[39;49;00m$
    56	[34mif[39;49;00m ([35mnot[39;49;00m AucAdvancedData.Stats) [34mthen[39;49;00m AucAdvancedData.Stats = {} [34mend[39;49;00m$
    57	[34mif[39;49;00m ([35mnot[39;49;00m AucAdvancedLocal.Stats) [34mthen[39;49;00m AucAdvancedLocal.Stats = {} [34mend[39;49;00m$
    58	$
    59	[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mTooltipHook[39;49;00m(vars, ret, frame, name, hyperlink, quality, quantity, cost, additional)$
    60		[34mif[39;49;00m EnhTooltip.LinkType(hyperlink) ~= [33m"[39;49;00m[33mitem[39;49;00m[33m"[39;49;00m [34mthen[39;49;00m$
    61			[34mreturn[39;49;00m [37m-- Auctioneer hooks into item tooltips only[39;49;00m$
    62		[34mend[39;49;00m$
    63	$
    64		[37m-- Check to see if we need to force load scandata[39;49;00m$
    65		[34mlocal[39;49;00m getter = AucAdvanced.Settings.GetSetting$
    66		[34mif[39;49;00m (getter([33m"[39;49;00m[33mscandata.tooltip.display[39;49;00m[33m"[39;49;00m) [35mand[39;49;00m getter([33m"[39;49;00m[33mscandata.force[39;49;00m[33m"[39;49;00m)) [34mthen[39;49;00m$
    67			AucAdvanced.Scan.GetImage()$
    68		[34mend[39;49;00m$
    69	$
    70		[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m$
    71			[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m$
    72				[34mif[39;49;00m (engineLib.Processor) [34mthen[39;49;00m engineLib.Processor([33m"[39;49;00m[33mtooltip[39;49;00m[33m"[39;49;00m, frame, name, hyperlink, quality, quantity, cost, additional) [34mend[39;49;00m$
    73			[34mend[39;49;00m$
    74		[34mend[39;49;00m$
    75	[34mend[39;49;00m$
    76	$
    77	[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mHookAH[39;49;00m()$
    78		hooksecurefunc([33m"[39;49;00m[33mAuctionFrameBrowse_Update[39;49;00m[33m"[39;49;00m, AucAdvanced.API.ListUpdate)$
    79		[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m$
    80			[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m$
    81				[34mif[39;49;00m (engineLib.Processor) [34mthen[39;49;00m$
    82					engineLib.Processor([33m"[39;49;00m[33mauctionui[39;49;00m[33m"[39;49;00m)$
    83				[34mend[39;49;00m$
    84			[34mend[39;49;00m$
    85		[34mend[39;49;00m$
    86	[34mend[39;49;00m$
    87	$
    88	[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mOnLoad[39;49;00m(addon)$
    89		addon = addon:lower()$
    90	$
    91		[37m-- Check if the actual addon itself is loading[39;49;00m$
    92		[34mif[39;49;00m (addon == [33m"[39;49;00m[33mauc-advanced[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m$
    93			Stubby.RegisterAddOnHook([33m"[39;49;00m[33mBlizzard_AuctionUi[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mAuc-Advanced[39;49;00m[33m"[39;49;00m, private.HookAH)$
    94			Stubby.RegisterFunctionHook([33m"[39;49;00m[33mEnhTooltip.AddTooltip[39;49;00m[33m"[39;49;00m, [34m600[39;49;00m, private.TooltipHook)$
    95			[34mfor[39;49;00m pos, module [34min[39;49;00m [36mipairs[39;49;00m(AucAdvanced.EmbeddedModules) [34mdo[39;49;00m$
    96				[37m-- These embedded modules have also just been loaded[39;49;00m$
    97				private.OnLoad(module)$
    98			[34mend[39;49;00m$
    99		[34mend[39;49;00m$
   100	$
   101		[37m-- Notify the actual module if it exists[39;49;00m$
   102		[34mlocal[39;49;00m auc, sys, eng = strsplit([33m"[39;49;00m[33m-[39;49;00m[33m"[39;49;00m, addon)$
   103		[34mif[39;49;00m (auc == [33m"[39;49;00m[33mauc[39;49;00m[33m"[39;49;00m [35mand[39;49;00m sys [35mand[39;49;00m eng) [34mthen[39;49;00m$
   104			[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m$
   105				[34mif[39;49;00m (sys == system:lower()) [34mthen[39;49;00m$
   106					[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m$
   107						[34mif[39;49;00m (eng == engine:lower() [35mand[39;49;00m engineLib.OnLoad) [34mthen[39;49;00m$
   108							engineLib.OnLoad(addon)$
   109						[34mend[39;49;00m$
   110					[34mend[39;49;00m$
   111				[34mend[39;49;00m$
   112			[34mend[39;49;00m$
   113		[34mend[39;49;00m$
   114	$
   115		[37m-- Check all modules' load triggers and pass event to processors[39;49;00m$
   116		[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m$
   117			[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m$
   118				[34mif[39;49;00m (engineLib.LoadTriggers [35mand[39;49;00m engineLib.LoadTriggers[addon]) [34mthen[39;49;00m$
   119					[34mif[39;49;00m (engineLib.OnLoad) [34mthen[39;49;00m$
   120						engineLib.OnLoad(addon)$
   121					[34mend[39;49;00m$
   122				[34mend[39;49;00m$
   123				[34mif[39;49;00m (engineLib.Processor [35mand[39;49;00m auc == [33m"[39;49;00m[33mauc[39;49;00m[33m"[39;49;00m [35mand[39;49;00m sys [35mand[39;49;00m eng) [34mthen[39;49;00m$
   124					engineLib.Processor([33m"[39;49;00m[33mload[39;49;00m[33m"[39;49;00m, addon)$
   125				[34mend[39;49;00m$
   126			[34mend[39;49;00m$
   127		[34mend[39;49;00m$
   128	[34mend[39;49;00m$
   129	$
   130	[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mOnUnload[39;49;00m()$
   131		[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m$
   132			[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m$
   133				[34mif[39;49;00m (engineLib.OnUnload) [34mthen[39;49;00m$
   134					engineLib.OnUnload()$
   135				[34mend[39;49;00m$
   136			[34mend[39;49;00m$
   137		[34mend[39;49;00m$
   138	[34mend[39;49;00m$
   139	$
   140	private.Schedule = {}$
   141	[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mOnEvent[39;49;00m(...)$
   142		[34mlocal[39;49;00m event, arg = [36mselect[39;49;00m([34m2[39;49;00m, ...)$
   143		[34mif[39;49;00m (event == [33m"[39;49;00m[33mADDON_LOADED[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m$
   144			[34mlocal[39;49;00m addon = [36mstring.lower[39;49;00m(arg)$
   145			[34mif[39;49;00m (addon:sub([34m1[39;49;00m,[34m4[39;49;00m) == [33m"[39;49;00m[33mauc-[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m$
   146				private.OnLoad(addon)$
   147			[34mend[39;49;00m$
   148		[34melseif[39;49;00m (event == [33m"[39;49;00m[33mAUCTION_HOUSE_SHOW[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m$
   149			[37m-- Do Nothing for now[39;49;00m$
   150		[34melseif[39;49;00m (event == [33m"[39;49;00m[33mAUCTION_HOUSE_CLOSED[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m$
   151			AucAdvanced.Scan.Interrupt()$
   152		[34melseif[39;49;00m (event == [33m"[39;49;00m[33mPLAYER_LOGOUT[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m$
   153			AucAdvanced.Scan.Commit([34mtrue[39;49;00m)$
   154			private.OnUnload()$
   155		[34melseif[39;49;00m event == [33m"[39;49;00m[33mUNIT_INVENTORY_CHANGED[39;49;00m[33m"[39;49;00m$
   156		[35mor[39;49;00m event == [33m"[39;49;00m[33mITEM_LOCK_CHANGED[39;49;00m[33m"[39;49;00m$
   157		[35mor[39;49;00m event == [33m"[39;49;00m[33mCURSOR_UPDATE[39;49;00m[33m"[39;49;00m$
   158		[35mor[39;49;00m event == [33m"[39;49;00m[33mBAG_UPDATE[39;49;00m[33m"[39;49;00m$
   159		[34mthen[39;49;00m$
   160			private.Schedule[[33m"[39;49;00m[33minventory[39;49;00m[33m"[39;49;00m] = GetTime() + [34m0.15[39;49;00m$
   161		[34mend[39;49;00m$
   162	[34mend[39;49;00m$
   163	$
   164	[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mOnUpdate[39;49;00m(...)$
   165		[34mif[39;49;00m event == [33m"[39;49;00m[33minventory[39;49;00m[33m"[39;49;00m [34mthen[39;49;00m$
   166			AucAdvanced.Post.AlertBagsChanged()$
   167		[34mend[39;49;00m$
   168	$
   169		[34mlocal[39;49;00m now = GetTime()$
   170		[34mfor[39;49;00m event, time [34min[39;49;00m [36mpairs[39;49;00m(private.Schedule) [34mdo[39;49;00m$
   171			[34mif[39;49;00m time > now [34mthen[39;49;00m$
   172				[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m$
   173					[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m$
   174						[34mif[39;49;00m engineLib.Processor [34mthen[39;49;00m$
   175							engineLib.Processor(event, time)$
   176						[34mend[39;49;00m$
   177					[34mend[39;49;00m$
   178				[34mend[39;49;00m$
   179			[34mend[39;49;00m$
   180			private.Schedule[event] = [34mnil[39;49;00m$
   181		[34mend[39;49;00m$
   182	[34mend[39;49;00m$
   183	$
   184	private.Frame = CreateFrame([33m"[39;49;00m[33mFrame[39;49;00m[33m"[39;49;00m)$
   185	private.Frame:RegisterEvent([33m"[39;49;00m[33mADDON_LOADED[39;49;00m[33m"[39;49;00m)$
   186	private.Frame:RegisterEvent([33m"[39;49;00m[33mAUCTION_HOUSE_SHOW[39;49;00m[33m"[39;49;00m)$
   187	private.Frame:RegisterEvent([33m"[39;49;00m[33mAUCTION_HOUSE_CLOSED[39;49;00m[33m"[39;49;00m)$
   188	private.Frame:RegisterEvent([33m"[39;49;00m[33mUNIT_INVENTORY_CHANGED[39;49;00m[33m"[39;49;00m)$
   189	private.Frame:RegisterEvent([33m"[39;49;00m[33mITEM_LOCK_CHANGED[39;49;00m[33m"[39;49;00m)$
   190	private.Frame:RegisterEvent([33m"[39;49;00m[33mCURSOR_UPDATE[39;49;00m[33m"[39;49;00m)$
   191	private.Frame:RegisterEvent([33m"[39;49;00m[33mBAG_UPDATE[39;49;00m[33m"[39;49;00m)$
   192	private.Frame:RegisterEvent([33m"[39;49;00m[33mPLAYER_LOGOUT[39;49;00m[33m"[39;49;00m)$
   193	private.Frame:SetScript([33m"[39;49;00m[33mOnEvent[39;49;00m[33m"[39;49;00m, private.OnEvent)$
   194	private.Frame:SetScript([33m"[39;49;00m[33mOnUpdate[39;49;00m[33m"[39;49;00m, private.OnUpdate)$
   195	$
   196	[37m-- Auctioneer's debug functions[39;49;00m$
   197	AucAdvanced.Debug = {}$
   198	[34mlocal[39;49;00m addonName = [33m"[39;49;00m[33mAuctioneer[39;49;00m[33m"[39;49;00m [37m-- the addon's name as it will be displayed in[39;49;00m$
   199	                               [37m-- the debug messages[39;49;00m$
   200	[37m-------------------------------------------------------------------------------[39;49;00m$
   201	[37m-- Prints the specified message to nLog.[39;49;00m$
   202	[37m--[39;49;00m$
   203	[37m-- syntax:[39;49;00m$
   204	[37m--    errorCode, message = debugPrint([message][, category][, title][, errorCode][, level])[39;49;00m$
   205	[37m--[39;49;00m$
   206	[37m-- parameters:[39;49;00m$
   207	[37m--    message   - (string) the error message[39;49;00m$
   208	[37m--                nil, no error message specified[39;49;00m$
   209	[37m--    category  - (string) the category of the debug message[39;49;00m$
   210	[37m--                nil, no category specified[39;49;00m$
   211	[37m--    title     - (string) the title for the debug message[39;49;00m$
   212	[37m--                nil, no title specified[39;49;00m$
   213	[37m--    errorCode - (number) the error code[39;49;00m$
   214	[37m--                nil, no error code specified[39;49;00m$
   215	[37m--    level     - (string) nLog message level[39;49;00m$
   216	[37m--                         Any nLog.levels string is valid.[39;49;00m$
   217	[37m--                nil, no level specified[39;49;00m$
   218	[37m--[39;49;00m$
   219	[37m-- returns:[39;49;00m$
   220	[37m--    errorCode - (number) errorCode, if one is specified[39;49;00m$
   221	[37m--                nil, otherwise[39;49;00m$
   222	[37m--    message   - (string) message, if one is specified[39;49;00m$
   223	[37m--                nil, otherwise[39;49;00m$
   224	[37m-------------------------------------------------------------------------------[39;49;00m$
   225	[34mfunction[39;49;00m [04m[32mAucAdvanced[39;49;00m.[04m[32mDebug[39;49;00m.[32mDebugPrint[39;49;00m(message, category, title, errorCode, level)$
   226		[34mreturn[39;49;00m DebugLib.DebugPrint(addonName, message, category, title, errorCode, level)$
   227	[34mend[39;49;00m$
   228	$
   229	[37m-------------------------------------------------------------------------------[39;49;00m$
   230	[37m-- Used to make sure that conditions are met within functions.[39;49;00m$
   231	[37m-- If test is false, the error message will be written to nLog and the user's[39;49;00m$
   232	[37m-- default chat channel.[39;49;00m$
   233	[37m--[39;49;00m$
   234	[37m-- syntax:[39;49;00m$
   235	[37m--    assertion = assert(test, message)[39;49;00m$
   236	[37m--[39;49;00m$
   237	[37m-- parameters:[39;49;00m$
   238	[37m--    test    - (any)     false/nil, if the assertion failed[39;49;00m$
   239	[37m--                        anything else, otherwise[39;49;00m$
   240	[37m--    message - (string)  the message which will be output to the user[39;49;00m$
   241	[37m--[39;49;00m$
   242	[37m-- returns:[39;49;00m$
   243	[37m--    assertion - (boolean) true, if the test passed[39;49;00m$
   244	[37m--                          false, otherwise[39;49;00m$
   245	[37m-------------------------------------------------------------------------------[39;49;00m$
   246	[34mfunction[39;49;00m [04m[32mAucAdvanced[39;49;00m.[04m[32mDebug[39;49;00m.[32mAssert[39;49;00m(test, message)$
   247		[34mreturn[39;49;00m DebugLib.Assert(addonName, test, message)$
   248	[34mend[39;49;00m$
   249	$
   250	[37m--[==[[39;49;00m$
   251	[37mHere follow further tests of Lua syntax.[39;49;00m$
   252	[37m]]==][39;49;00m$
   253	[37m---[[[39;49;00m$
   254	[34mlocal[39;49;00m t = {$
   255	        [ [33m[[[39;49;00m$
   256	[33mx[39;49;00m$
   257	[33m]==] \]][39;49;00m]=[34m1[39;49;00m|[34m2[39;49;00m; a={b={c={}}},$
   258	        [34m1[39;49;00m, [34m1.[39;49;00m, [34m1.2[39;49;00m, [34m.2[39;49;00m, [34m1e3[39;49;00m, [34m1.e3[39;49;00m, [34m1.2e3[39;49;00m, [34m.2e3[39;49;00m, [34m1.2e+3[39;49;00m, [34m1.2E-3[39;49;00m;$
   259	        [34m0xA[39;49;00m, [34m0Xa[39;49;00m, [34m0xA.[39;49;00m, [34m0x.F[39;49;00m, [34m0xA.F[39;49;00m, [34m0xA.Fp1[39;49;00m, [34m0xA.FP+1[39;49;00m, [34m0Xa.fp-1[39;49;00m;$
   260	}$
   261	$
   262	[34mfunction[39;49;00m [04m[32mt[39;49;00m.[32mf[39;49;00m()$
   263	        [34mgoto[39;49;00m eof$
   264	        [36mos.exit[39;49;00m()$
   265	        :: eof ::$
   266	[34mend[39;49;00m$
   267	$
   268	[34mfunction[39;49;00m [04m[32mt[39;49;00m . [04m[32ma[39;49;00m [37m--[==[x]==][39;49;00m .[04m[32mb[39;49;00m [37m--[==[y]==][39;49;00m [37m--[39;49;00m$
   269	[37m-- () end[39;49;00m$
   270	           . [04m[32mc[39;49;00m : [32md[39;49;00m (file)$
   271	        [34mreturn[39;49;00m [33m'[39;49;00m[33m.[39;49;00m[33m\a[39;49;00m[33m.[39;49;00m[33m\b[39;49;00m[33m.[39;49;00m[33m\f[39;49;00m[33m.[39;49;00m[33m\n[39;49;00m[33m.[39;49;00m[33m\r[39;49;00m[33m.[39;49;00m[33m\t[39;49;00m[33m.[39;49;00m[33m\v[39;49;00m[33m.[39;49;00m[33m\\[39;49;00m[33m.[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m[33m\'[39;49;00m[33m.[39;49;00m[33m\[39;49;00m$
   272	[33m.[39;49;00m[33m\z    [39;49;00m$
   273	[33m  	 [39;49;00m[33m.[39;49;00m[33m\0[39;49;00m[33m.[39;49;00m[33m\00[39;49;00m[33m.[39;49;00m[33m\000[39;49;00m[33m.[39;49;00m[33m\000[39;49;00m[33m0.[39;49;00m[33m\xFa[39;49;00m[33m.[39;49;00m[33m\u{1}[39;49;00m[33m.[39;49;00m[33m\u{1234}[39;49;00m[33m'[39;49;00m$
   274	[34mend[39;49;00m$
