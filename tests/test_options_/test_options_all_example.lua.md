     1^I[37m--[[[39;49;00m$
     2^I[37m^IAuctioneer Advanced[39;49;00m$
     3^I[37m^IVersion: <%version%> (<%codename%>)[39;49;00m$
     4^I[37m^IRevision: $Id: CoreMain.lua 2233 2007-09-25 03:57:33Z norganna $[39;49;00m$
     5^I[37m^IURL: http://auctioneeraddon.com/[39;49;00m$
     6^I[37m[39;49;00m$
     7^I[37m^IThis is an addon for World of Warcraft that adds statistical history to the auction data that is collected[39;49;00m$
     8^I[37m^Iwhen the auction is scanned, so that you can easily determine what price[39;49;00m$
     9^I[37m^Iyou will be able to sell an item for at auction or at a vendor whenever you[39;49;00m$
    10^I[37m^Imouse-over an item in the game[39;49;00m$
    11^I[37m[39;49;00m$
    12^I[37m^ILicense:[39;49;00m$
    13^I[37m^I^IThis program is free software; you can redistribute it and/or[39;49;00m$
    14^I[37m^I^Imodify it under the terms of the GNU General Public License[39;49;00m$
    15^I[37m^I^Ias published by the Free Software Foundation; either version 2[39;49;00m$
    16^I[37m^I^Iof the License, or (at your option) any later version.[39;49;00m$
    17^I[37m[39;49;00m$
    18^I[37m^I^IThis program is distributed in the hope that it will be useful,[39;49;00m$
    19^I[37m^I^Ibut WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m$
    20^I[37m^I^IMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the[39;49;00m$
    21^I[37m^I^IGNU General Public License for more details.[39;49;00m$
    22^I[37m[39;49;00m$
    23^I[37m^I^IYou should have received a copy of the GNU General Public License[39;49;00m$
    24^I[37m^I^Ialong with this program(see GPL.txt); if not, write to the Free Software[39;49;00m$
    25^I[37m^I^IFoundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.[39;49;00m$
    26^I[37m[39;49;00m$
    27^I[37m^INote:[39;49;00m$
    28^I[37m^I^IThis AddOn's source code is specifically designed to work with[39;49;00m$
    29^I[37m^I^IWorld of Warcraft's interpreted AddOn system.[39;49;00m$
    30^I[37m^I^IYou have an implicit licence to use this AddOn with these facilities[39;49;00m$
    31^I[37m^I^Isince that is its designated purpose as per:[39;49;00m$
    32^I[37m^I^Ihttp://www.fsf.org/licensing/licenses/gpl-faq.html#InterpreterIncompat[39;49;00m$
    33^I[37m]][39;49;00m$
    34^I$
    35^I$
    36^I[37m--[[[39;49;00m$
    37^I[37m^ISee CoreAPI.lua for a description of the modules API[39;49;00m$
    38^I[37m]][39;49;00m$
    39^I$
    40^I[34mif[39;49;00m ([35mnot[39;49;00m AucAdvanced) [34mthen[39;49;00m AucAdvanced = {} [34mend[39;49;00m$
    41^I[34mif[39;49;00m ([35mnot[39;49;00m AucAdvancedData) [34mthen[39;49;00m AucAdvancedData = {} [34mend[39;49;00m$
    42^I[34mif[39;49;00m ([35mnot[39;49;00m AucAdvancedLocal) [34mthen[39;49;00m AucAdvancedLocal = {} [34mend[39;49;00m$
    43^I[34mif[39;49;00m ([35mnot[39;49;00m AucAdvancedConfig) [34mthen[39;49;00m AucAdvancedConfig = {} [34mend[39;49;00m$
    44^I$
    45^IAucAdvanced.Version=[33m"[39;49;00m[33m<%version%>[39;49;00m[33m"[39;49;00m;$
    46^I[34mif[39;49;00m (AucAdvanced.Version == [33m"[39;49;00m[33m<[39;49;00m[33m"[39;49;00m..[33m"[39;49;00m[33m%version%>[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m$
    47^I^IAucAdvanced.Version = [33m"[39;49;00m[33m5.0.DEV[39;49;00m[33m"[39;49;00m;$
    48^I[34mend[39;49;00m$
    49^I$
    50^I[34mlocal[39;49;00m private = {}$
    51^I$
    52^I[37m-- For our modular stats system, each stats engine should add their[39;49;00m$
    53^I[37m-- subclass to AucAdvanced.Modules.<type>.<name> and store their data into their own[39;49;00m$
    54^I[37m-- data table in AucAdvancedData.Stats.<type><name>[39;49;00m$
    55^I[34mif[39;49;00m ([35mnot[39;49;00m AucAdvanced.Modules) [34mthen[39;49;00m AucAdvanced.Modules = {Stat={},Util={},Filter={}} [34mend[39;49;00m$
    56^I[34mif[39;49;00m ([35mnot[39;49;00m AucAdvancedData.Stats) [34mthen[39;49;00m AucAdvancedData.Stats = {} [34mend[39;49;00m$
    57^I[34mif[39;49;00m ([35mnot[39;49;00m AucAdvancedLocal.Stats) [34mthen[39;49;00m AucAdvancedLocal.Stats = {} [34mend[39;49;00m$
    58^I$
    59^I[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mTooltipHook[39;49;00m(vars, ret, frame, name, hyperlink, quality, quantity, cost, additional)$
    60^I^I[34mif[39;49;00m EnhTooltip.LinkType(hyperlink) ~= [33m"[39;49;00m[33mitem[39;49;00m[33m"[39;49;00m [34mthen[39;49;00m$
    61^I^I^I[34mreturn[39;49;00m [37m-- Auctioneer hooks into item tooltips only[39;49;00m$
    62^I^I[34mend[39;49;00m$
    63^I$
    64^I^I[37m-- Check to see if we need to force load scandata[39;49;00m$
    65^I^I[34mlocal[39;49;00m getter = AucAdvanced.Settings.GetSetting$
    66^I^I[34mif[39;49;00m (getter([33m"[39;49;00m[33mscandata.tooltip.display[39;49;00m[33m"[39;49;00m) [35mand[39;49;00m getter([33m"[39;49;00m[33mscandata.force[39;49;00m[33m"[39;49;00m)) [34mthen[39;49;00m$
    67^I^I^IAucAdvanced.Scan.GetImage()$
    68^I^I[34mend[39;49;00m$
    69^I$
    70^I^I[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m$
    71^I^I^I[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m$
    72^I^I^I^I[34mif[39;49;00m (engineLib.Processor) [34mthen[39;49;00m engineLib.Processor([33m"[39;49;00m[33mtooltip[39;49;00m[33m"[39;49;00m, frame, name, hyperlink, quality, quantity, cost, additional) [34mend[39;49;00m$
    73^I^I^I[34mend[39;49;00m$
    74^I^I[34mend[39;49;00m$
    75^I[34mend[39;49;00m$
    76^I$
    77^I[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mHookAH[39;49;00m()$
    78^I^Ihooksecurefunc([33m"[39;49;00m[33mAuctionFrameBrowse_Update[39;49;00m[33m"[39;49;00m, AucAdvanced.API.ListUpdate)$
    79^I^I[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m$
    80^I^I^I[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m$
    81^I^I^I^I[34mif[39;49;00m (engineLib.Processor) [34mthen[39;49;00m$
    82^I^I^I^I^IengineLib.Processor([33m"[39;49;00m[33mauctionui[39;49;00m[33m"[39;49;00m)$
    83^I^I^I^I[34mend[39;49;00m$
    84^I^I^I[34mend[39;49;00m$
    85^I^I[34mend[39;49;00m$
    86^I[34mend[39;49;00m$
    87^I$
    88^I[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mOnLoad[39;49;00m(addon)$
    89^I^Iaddon = addon:lower()$
    90^I$
    91^I^I[37m-- Check if the actual addon itself is loading[39;49;00m$
    92^I^I[34mif[39;49;00m (addon == [33m"[39;49;00m[33mauc-advanced[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m$
    93^I^I^IStubby.RegisterAddOnHook([33m"[39;49;00m[33mBlizzard_AuctionUi[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mAuc-Advanced[39;49;00m[33m"[39;49;00m, private.HookAH)$
    94^I^I^IStubby.RegisterFunctionHook([33m"[39;49;00m[33mEnhTooltip.AddTooltip[39;49;00m[33m"[39;49;00m, [34m600[39;49;00m, private.TooltipHook)$
    95^I^I^I[34mfor[39;49;00m pos, module [34min[39;49;00m [36mipairs[39;49;00m(AucAdvanced.EmbeddedModules) [34mdo[39;49;00m$
    96^I^I^I^I[37m-- These embedded modules have also just been loaded[39;49;00m$
    97^I^I^I^Iprivate.OnLoad(module)$
    98^I^I^I[34mend[39;49;00m$
    99^I^I[34mend[39;49;00m$
   100^I$
   101^I^I[37m-- Notify the actual module if it exists[39;49;00m$
   102^I^I[34mlocal[39;49;00m auc, sys, eng = strsplit([33m"[39;49;00m[33m-[39;49;00m[33m"[39;49;00m, addon)$
   103^I^I[34mif[39;49;00m (auc == [33m"[39;49;00m[33mauc[39;49;00m[33m"[39;49;00m [35mand[39;49;00m sys [35mand[39;49;00m eng) [34mthen[39;49;00m$
   104^I^I^I[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m$
   105^I^I^I^I[34mif[39;49;00m (sys == system:lower()) [34mthen[39;49;00m$
   106^I^I^I^I^I[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m$
   107^I^I^I^I^I^I[34mif[39;49;00m (eng == engine:lower() [35mand[39;49;00m engineLib.OnLoad) [34mthen[39;49;00m$
   108^I^I^I^I^I^I^IengineLib.OnLoad(addon)$
   109^I^I^I^I^I^I[34mend[39;49;00m$
   110^I^I^I^I^I[34mend[39;49;00m$
   111^I^I^I^I[34mend[39;49;00m$
   112^I^I^I[34mend[39;49;00m$
   113^I^I[34mend[39;49;00m$
   114^I$
   115^I^I[37m-- Check all modules' load triggers and pass event to processors[39;49;00m$
   116^I^I[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m$
   117^I^I^I[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m$
   118^I^I^I^I[34mif[39;49;00m (engineLib.LoadTriggers [35mand[39;49;00m engineLib.LoadTriggers[addon]) [34mthen[39;49;00m$
   119^I^I^I^I^I[34mif[39;49;00m (engineLib.OnLoad) [34mthen[39;49;00m$
   120^I^I^I^I^I^IengineLib.OnLoad(addon)$
   121^I^I^I^I^I[34mend[39;49;00m$
   122^I^I^I^I[34mend[39;49;00m$
   123^I^I^I^I[34mif[39;49;00m (engineLib.Processor [35mand[39;49;00m auc == [33m"[39;49;00m[33mauc[39;49;00m[33m"[39;49;00m [35mand[39;49;00m sys [35mand[39;49;00m eng) [34mthen[39;49;00m$
   124^I^I^I^I^IengineLib.Processor([33m"[39;49;00m[33mload[39;49;00m[33m"[39;49;00m, addon)$
   125^I^I^I^I[34mend[39;49;00m$
   126^I^I^I[34mend[39;49;00m$
   127^I^I[34mend[39;49;00m$
   128^I[34mend[39;49;00m$
   129^I$
   130^I[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mOnUnload[39;49;00m()$
   131^I^I[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m$
   132^I^I^I[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m$
   133^I^I^I^I[34mif[39;49;00m (engineLib.OnUnload) [34mthen[39;49;00m$
   134^I^I^I^I^IengineLib.OnUnload()$
   135^I^I^I^I[34mend[39;49;00m$
   136^I^I^I[34mend[39;49;00m$
   137^I^I[34mend[39;49;00m$
   138^I[34mend[39;49;00m$
   139^I$
   140^Iprivate.Schedule = {}$
   141^I[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mOnEvent[39;49;00m(...)$
   142^I^I[34mlocal[39;49;00m event, arg = [36mselect[39;49;00m([34m2[39;49;00m, ...)$
   143^I^I[34mif[39;49;00m (event == [33m"[39;49;00m[33mADDON_LOADED[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m$
   144^I^I^I[34mlocal[39;49;00m addon = [36mstring.lower[39;49;00m(arg)$
   145^I^I^I[34mif[39;49;00m (addon:sub([34m1[39;49;00m,[34m4[39;49;00m) == [33m"[39;49;00m[33mauc-[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m$
   146^I^I^I^Iprivate.OnLoad(addon)$
   147^I^I^I[34mend[39;49;00m$
   148^I^I[34melseif[39;49;00m (event == [33m"[39;49;00m[33mAUCTION_HOUSE_SHOW[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m$
   149^I^I^I[37m-- Do Nothing for now[39;49;00m$
   150^I^I[34melseif[39;49;00m (event == [33m"[39;49;00m[33mAUCTION_HOUSE_CLOSED[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m$
   151^I^I^IAucAdvanced.Scan.Interrupt()$
   152^I^I[34melseif[39;49;00m (event == [33m"[39;49;00m[33mPLAYER_LOGOUT[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m$
   153^I^I^IAucAdvanced.Scan.Commit([34mtrue[39;49;00m)$
   154^I^I^Iprivate.OnUnload()$
   155^I^I[34melseif[39;49;00m event == [33m"[39;49;00m[33mUNIT_INVENTORY_CHANGED[39;49;00m[33m"[39;49;00m$
   156^I^I[35mor[39;49;00m event == [33m"[39;49;00m[33mITEM_LOCK_CHANGED[39;49;00m[33m"[39;49;00m$
   157^I^I[35mor[39;49;00m event == [33m"[39;49;00m[33mCURSOR_UPDATE[39;49;00m[33m"[39;49;00m$
   158^I^I[35mor[39;49;00m event == [33m"[39;49;00m[33mBAG_UPDATE[39;49;00m[33m"[39;49;00m$
   159^I^I[34mthen[39;49;00m$
   160^I^I^Iprivate.Schedule[[33m"[39;49;00m[33minventory[39;49;00m[33m"[39;49;00m] = GetTime() + [34m0.15[39;49;00m$
   161^I^I[34mend[39;49;00m$
   162^I[34mend[39;49;00m$
   163^I$
   164^I[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mOnUpdate[39;49;00m(...)$
   165^I^I[34mif[39;49;00m event == [33m"[39;49;00m[33minventory[39;49;00m[33m"[39;49;00m [34mthen[39;49;00m$
   166^I^I^IAucAdvanced.Post.AlertBagsChanged()$
   167^I^I[34mend[39;49;00m$
   168^I$
   169^I^I[34mlocal[39;49;00m now = GetTime()$
   170^I^I[34mfor[39;49;00m event, time [34min[39;49;00m [36mpairs[39;49;00m(private.Schedule) [34mdo[39;49;00m$
   171^I^I^I[34mif[39;49;00m time > now [34mthen[39;49;00m$
   172^I^I^I^I[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m$
   173^I^I^I^I^I[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m$
   174^I^I^I^I^I^I[34mif[39;49;00m engineLib.Processor [34mthen[39;49;00m$
   175^I^I^I^I^I^I^IengineLib.Processor(event, time)$
   176^I^I^I^I^I^I[34mend[39;49;00m$
   177^I^I^I^I^I[34mend[39;49;00m$
   178^I^I^I^I[34mend[39;49;00m$
   179^I^I^I[34mend[39;49;00m$
   180^I^I^Iprivate.Schedule[event] = [34mnil[39;49;00m$
   181^I^I[34mend[39;49;00m$
   182^I[34mend[39;49;00m$
   183^I$
   184^Iprivate.Frame = CreateFrame([33m"[39;49;00m[33mFrame[39;49;00m[33m"[39;49;00m)$
   185^Iprivate.Frame:RegisterEvent([33m"[39;49;00m[33mADDON_LOADED[39;49;00m[33m"[39;49;00m)$
   186^Iprivate.Frame:RegisterEvent([33m"[39;49;00m[33mAUCTION_HOUSE_SHOW[39;49;00m[33m"[39;49;00m)$
   187^Iprivate.Frame:RegisterEvent([33m"[39;49;00m[33mAUCTION_HOUSE_CLOSED[39;49;00m[33m"[39;49;00m)$
   188^Iprivate.Frame:RegisterEvent([33m"[39;49;00m[33mUNIT_INVENTORY_CHANGED[39;49;00m[33m"[39;49;00m)$
   189^Iprivate.Frame:RegisterEvent([33m"[39;49;00m[33mITEM_LOCK_CHANGED[39;49;00m[33m"[39;49;00m)$
   190^Iprivate.Frame:RegisterEvent([33m"[39;49;00m[33mCURSOR_UPDATE[39;49;00m[33m"[39;49;00m)$
   191^Iprivate.Frame:RegisterEvent([33m"[39;49;00m[33mBAG_UPDATE[39;49;00m[33m"[39;49;00m)$
   192^Iprivate.Frame:RegisterEvent([33m"[39;49;00m[33mPLAYER_LOGOUT[39;49;00m[33m"[39;49;00m)$
   193^Iprivate.Frame:SetScript([33m"[39;49;00m[33mOnEvent[39;49;00m[33m"[39;49;00m, private.OnEvent)$
   194^Iprivate.Frame:SetScript([33m"[39;49;00m[33mOnUpdate[39;49;00m[33m"[39;49;00m, private.OnUpdate)$
   195^I$
   196^I[37m-- Auctioneer's debug functions[39;49;00m$
   197^IAucAdvanced.Debug = {}$
   198^I[34mlocal[39;49;00m addonName = [33m"[39;49;00m[33mAuctioneer[39;49;00m[33m"[39;49;00m [37m-- the addon's name as it will be displayed in[39;49;00m$
   199^I                               [37m-- the debug messages[39;49;00m$
   200^I[37m-------------------------------------------------------------------------------[39;49;00m$
   201^I[37m-- Prints the specified message to nLog.[39;49;00m$
   202^I[37m--[39;49;00m$
   203^I[37m-- syntax:[39;49;00m$
   204^I[37m--    errorCode, message = debugPrint([message][, category][, title][, errorCode][, level])[39;49;00m$
   205^I[37m--[39;49;00m$
   206^I[37m-- parameters:[39;49;00m$
   207^I[37m--    message   - (string) the error message[39;49;00m$
   208^I[37m--                nil, no error message specified[39;49;00m$
   209^I[37m--    category  - (string) the category of the debug message[39;49;00m$
   210^I[37m--                nil, no category specified[39;49;00m$
   211^I[37m--    title     - (string) the title for the debug message[39;49;00m$
   212^I[37m--                nil, no title specified[39;49;00m$
   213^I[37m--    errorCode - (number) the error code[39;49;00m$
   214^I[37m--                nil, no error code specified[39;49;00m$
   215^I[37m--    level     - (string) nLog message level[39;49;00m$
   216^I[37m--                         Any nLog.levels string is valid.[39;49;00m$
   217^I[37m--                nil, no level specified[39;49;00m$
   218^I[37m--[39;49;00m$
   219^I[37m-- returns:[39;49;00m$
   220^I[37m--    errorCode - (number) errorCode, if one is specified[39;49;00m$
   221^I[37m--                nil, otherwise[39;49;00m$
   222^I[37m--    message   - (string) message, if one is specified[39;49;00m$
   223^I[37m--                nil, otherwise[39;49;00m$
   224^I[37m-------------------------------------------------------------------------------[39;49;00m$
   225^I[34mfunction[39;49;00m [04m[32mAucAdvanced[39;49;00m.[04m[32mDebug[39;49;00m.[32mDebugPrint[39;49;00m(message, category, title, errorCode, level)$
   226^I^I[34mreturn[39;49;00m DebugLib.DebugPrint(addonName, message, category, title, errorCode, level)$
   227^I[34mend[39;49;00m$
   228^I$
   229^I[37m-------------------------------------------------------------------------------[39;49;00m$
   230^I[37m-- Used to make sure that conditions are met within functions.[39;49;00m$
   231^I[37m-- If test is false, the error message will be written to nLog and the user's[39;49;00m$
   232^I[37m-- default chat channel.[39;49;00m$
   233^I[37m--[39;49;00m$
   234^I[37m-- syntax:[39;49;00m$
   235^I[37m--    assertion = assert(test, message)[39;49;00m$
   236^I[37m--[39;49;00m$
   237^I[37m-- parameters:[39;49;00m$
   238^I[37m--    test    - (any)     false/nil, if the assertion failed[39;49;00m$
   239^I[37m--                        anything else, otherwise[39;49;00m$
   240^I[37m--    message - (string)  the message which will be output to the user[39;49;00m$
   241^I[37m--[39;49;00m$
   242^I[37m-- returns:[39;49;00m$
   243^I[37m--    assertion - (boolean) true, if the test passed[39;49;00m$
   244^I[37m--                          false, otherwise[39;49;00m$
   245^I[37m-------------------------------------------------------------------------------[39;49;00m$
   246^I[34mfunction[39;49;00m [04m[32mAucAdvanced[39;49;00m.[04m[32mDebug[39;49;00m.[32mAssert[39;49;00m(test, message)$
   247^I^I[34mreturn[39;49;00m DebugLib.Assert(addonName, test, message)$
   248^I[34mend[39;49;00m$
   249^I$
   250^I[37m--[==[[39;49;00m$
   251^I[37mHere follow further tests of Lua syntax.[39;49;00m$
   252^I[37m]]==][39;49;00m$
   253^I[37m---[[[39;49;00m$
   254^I[34mlocal[39;49;00m t = {$
   255^I        [ [33m[[[39;49;00m$
   256^I[33mx[39;49;00m$
   257^I[33m]==] \]][39;49;00m]=[34m1[39;49;00m|[34m2[39;49;00m; a={b={c={}}},$
   258^I        [34m1[39;49;00m, [34m1.[39;49;00m, [34m1.2[39;49;00m, [34m.2[39;49;00m, [34m1e3[39;49;00m, [34m1.e3[39;49;00m, [34m1.2e3[39;49;00m, [34m.2e3[39;49;00m, [34m1.2e+3[39;49;00m, [34m1.2E-3[39;49;00m;$
   259^I        [34m0xA[39;49;00m, [34m0Xa[39;49;00m, [34m0xA.[39;49;00m, [34m0x.F[39;49;00m, [34m0xA.F[39;49;00m, [34m0xA.Fp1[39;49;00m, [34m0xA.FP+1[39;49;00m, [34m0Xa.fp-1[39;49;00m;$
   260^I}$
   261^I$
   262^I[34mfunction[39;49;00m [04m[32mt[39;49;00m.[32mf[39;49;00m()$
   263^I        [34mgoto[39;49;00m eof$
   264^I        [36mos.exit[39;49;00m()$
   265^I        :: eof ::$
   266^I[34mend[39;49;00m$
   267^I$
   268^I[34mfunction[39;49;00m [04m[32mt[39;49;00m . [04m[32ma[39;49;00m [37m--[==[x]==][39;49;00m .[04m[32mb[39;49;00m [37m--[==[y]==][39;49;00m [37m--[39;49;00m$
   269^I[37m-- () end[39;49;00m$
   270^I           . [04m[32mc[39;49;00m : [32md[39;49;00m (file)$
   271^I        [34mreturn[39;49;00m [33m'[39;49;00m[33m.[39;49;00m[33m\a[39;49;00m[33m.[39;49;00m[33m\b[39;49;00m[33m.[39;49;00m[33m\f[39;49;00m[33m.[39;49;00m[33m\n[39;49;00m[33m.[39;49;00m[33m\r[39;49;00m[33m.[39;49;00m[33m\t[39;49;00m[33m.[39;49;00m[33m\v[39;49;00m[33m.[39;49;00m[33m\\[39;49;00m[33m.[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m[33m\'[39;49;00m[33m.[39;49;00m[33m\[39;49;00m$
   272^I[33m.[39;49;00m[33m\z    [39;49;00m$
   273^I[33m  ^I [39;49;00m[33m.[39;49;00m[33m\0[39;49;00m[33m.[39;49;00m[33m\00[39;49;00m[33m.[39;49;00m[33m\000[39;49;00m[33m.[39;49;00m[33m\000[39;49;00m[33m0.[39;49;00m[33m\xFa[39;49;00m[33m.[39;49;00m[33m\u{1}[39;49;00m[33m.[39;49;00m[33m\u{1234}[39;49;00m[33m'[39;49;00m$
   274^I[34mend[39;49;00m$
