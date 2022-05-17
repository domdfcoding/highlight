[37m--[[[39;49;00m
[37m^IAuctioneer Advanced[39;49;00m
[37m^IVersion: <%version%> (<%codename%>)[39;49;00m
[37m^IRevision: $Id: CoreMain.lua 2233 2007-09-25 03:57:33Z norganna $[39;49;00m
[37m^IURL: http://auctioneeraddon.com/[39;49;00m
[37m[39;49;00m
[37m^IThis is an addon for World of Warcraft that adds statistical history to the auction data that is collected[39;49;00m
[37m^Iwhen the auction is scanned, so that you can easily determine what price[39;49;00m
[37m^Iyou will be able to sell an item for at auction or at a vendor whenever you[39;49;00m
[37m^Imouse-over an item in the game[39;49;00m
[37m[39;49;00m
[37m^ILicense:[39;49;00m
[37m^I^IThis program is free software; you can redistribute it and/or[39;49;00m
[37m^I^Imodify it under the terms of the GNU General Public License[39;49;00m
[37m^I^Ias published by the Free Software Foundation; either version 2[39;49;00m
[37m^I^Iof the License, or (at your option) any later version.[39;49;00m
[37m[39;49;00m
[37m^I^IThis program is distributed in the hope that it will be useful,[39;49;00m
[37m^I^Ibut WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m
[37m^I^IMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the[39;49;00m
[37m^I^IGNU General Public License for more details.[39;49;00m
[37m[39;49;00m
[37m^I^IYou should have received a copy of the GNU General Public License[39;49;00m
[37m^I^Ialong with this program(see GPL.txt); if not, write to the Free Software[39;49;00m
[37m^I^IFoundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.[39;49;00m
[37m[39;49;00m
[37m^INote:[39;49;00m
[37m^I^IThis AddOn's source code is specifically designed to work with[39;49;00m
[37m^I^IWorld of Warcraft's interpreted AddOn system.[39;49;00m
[37m^I^IYou have an implicit licence to use this AddOn with these facilities[39;49;00m
[37m^I^Isince that is its designated purpose as per:[39;49;00m
[37m^I^Ihttp://www.fsf.org/licensing/licenses/gpl-faq.html#InterpreterIncompat[39;49;00m
[37m]][39;49;00m


[37m--[[[39;49;00m
[37m^ISee CoreAPI.lua for a description of the modules API[39;49;00m
[37m]][39;49;00m

[34mif[39;49;00m ([35mnot[39;49;00m AucAdvanced) [34mthen[39;49;00m AucAdvanced = {} [34mend[39;49;00m
[34mif[39;49;00m ([35mnot[39;49;00m AucAdvancedData) [34mthen[39;49;00m AucAdvancedData = {} [34mend[39;49;00m
[34mif[39;49;00m ([35mnot[39;49;00m AucAdvancedLocal) [34mthen[39;49;00m AucAdvancedLocal = {} [34mend[39;49;00m
[34mif[39;49;00m ([35mnot[39;49;00m AucAdvancedConfig) [34mthen[39;49;00m AucAdvancedConfig = {} [34mend[39;49;00m

AucAdvanced.Version=[33m"[39;49;00m[33m<%version%>[39;49;00m[33m"[39;49;00m;
[34mif[39;49;00m (AucAdvanced.Version == [33m"[39;49;00m[33m<[39;49;00m[33m"[39;49;00m..[33m"[39;49;00m[33m%version%>[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m
^IAucAdvanced.Version = [33m"[39;49;00m[33m5.0.DEV[39;49;00m[33m"[39;49;00m;
[34mend[39;49;00m

[34mlocal[39;49;00m private = {}

[37m-- For our modular stats system, each stats engine should add their[39;49;00m
[37m-- subclass to AucAdvanced.Modules.<type>.<name> and store their data into their own[39;49;00m
[37m-- data table in AucAdvancedData.Stats.<type><name>[39;49;00m
[34mif[39;49;00m ([35mnot[39;49;00m AucAdvanced.Modules) [34mthen[39;49;00m AucAdvanced.Modules = {Stat={},Util={},Filter={}} [34mend[39;49;00m
[34mif[39;49;00m ([35mnot[39;49;00m AucAdvancedData.Stats) [34mthen[39;49;00m AucAdvancedData.Stats = {} [34mend[39;49;00m
[34mif[39;49;00m ([35mnot[39;49;00m AucAdvancedLocal.Stats) [34mthen[39;49;00m AucAdvancedLocal.Stats = {} [34mend[39;49;00m

[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mTooltipHook[39;49;00m(vars, ret, frame, name, hyperlink, quality, quantity, cost, additional)
^I[34mif[39;49;00m EnhTooltip.LinkType(hyperlink) ~= [33m"[39;49;00m[33mitem[39;49;00m[33m"[39;49;00m [34mthen[39;49;00m
^I^I[34mreturn[39;49;00m [37m-- Auctioneer hooks into item tooltips only[39;49;00m
^I[34mend[39;49;00m

^I[37m-- Check to see if we need to force load scandata[39;49;00m
^I[34mlocal[39;49;00m getter = AucAdvanced.Settings.GetSetting
^I[34mif[39;49;00m (getter([33m"[39;49;00m[33mscandata.tooltip.display[39;49;00m[33m"[39;49;00m) [35mand[39;49;00m getter([33m"[39;49;00m[33mscandata.force[39;49;00m[33m"[39;49;00m)) [34mthen[39;49;00m
^I^IAucAdvanced.Scan.GetImage()
^I[34mend[39;49;00m

^I[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m
^I^I[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m
^I^I^I[34mif[39;49;00m (engineLib.Processor) [34mthen[39;49;00m engineLib.Processor([33m"[39;49;00m[33mtooltip[39;49;00m[33m"[39;49;00m, frame, name, hyperlink, quality, quantity, cost, additional) [34mend[39;49;00m
^I^I[34mend[39;49;00m
^I[34mend[39;49;00m
[34mend[39;49;00m

[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mHookAH[39;49;00m()
^Ihooksecurefunc([33m"[39;49;00m[33mAuctionFrameBrowse_Update[39;49;00m[33m"[39;49;00m, AucAdvanced.API.ListUpdate)
^I[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m
^I^I[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m
^I^I^I[34mif[39;49;00m (engineLib.Processor) [34mthen[39;49;00m
^I^I^I^IengineLib.Processor([33m"[39;49;00m[33mauctionui[39;49;00m[33m"[39;49;00m)
^I^I^I[34mend[39;49;00m
^I^I[34mend[39;49;00m
^I[34mend[39;49;00m
[34mend[39;49;00m

[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mOnLoad[39;49;00m(addon)
^Iaddon = addon:lower()

^I[37m-- Check if the actual addon itself is loading[39;49;00m
^I[34mif[39;49;00m (addon == [33m"[39;49;00m[33mauc-advanced[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m
^I^IStubby.RegisterAddOnHook([33m"[39;49;00m[33mBlizzard_AuctionUi[39;49;00m[33m"[39;49;00m, [33m"[39;49;00m[33mAuc-Advanced[39;49;00m[33m"[39;49;00m, private.HookAH)
^I^IStubby.RegisterFunctionHook([33m"[39;49;00m[33mEnhTooltip.AddTooltip[39;49;00m[33m"[39;49;00m, [34m600[39;49;00m, private.TooltipHook)
^I^I[34mfor[39;49;00m pos, module [34min[39;49;00m [36mipairs[39;49;00m(AucAdvanced.EmbeddedModules) [34mdo[39;49;00m
^I^I^I[37m-- These embedded modules have also just been loaded[39;49;00m
^I^I^Iprivate.OnLoad(module)
^I^I[34mend[39;49;00m
^I[34mend[39;49;00m

^I[37m-- Notify the actual module if it exists[39;49;00m
^I[34mlocal[39;49;00m auc, sys, eng = strsplit([33m"[39;49;00m[33m-[39;49;00m[33m"[39;49;00m, addon)
^I[34mif[39;49;00m (auc == [33m"[39;49;00m[33mauc[39;49;00m[33m"[39;49;00m [35mand[39;49;00m sys [35mand[39;49;00m eng) [34mthen[39;49;00m
^I^I[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m
^I^I^I[34mif[39;49;00m (sys == system:lower()) [34mthen[39;49;00m
^I^I^I^I[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m
^I^I^I^I^I[34mif[39;49;00m (eng == engine:lower() [35mand[39;49;00m engineLib.OnLoad) [34mthen[39;49;00m
^I^I^I^I^I^IengineLib.OnLoad(addon)
^I^I^I^I^I[34mend[39;49;00m
^I^I^I^I[34mend[39;49;00m
^I^I^I[34mend[39;49;00m
^I^I[34mend[39;49;00m
^I[34mend[39;49;00m

^I[37m-- Check all modules' load triggers and pass event to processors[39;49;00m
^I[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m
^I^I[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m
^I^I^I[34mif[39;49;00m (engineLib.LoadTriggers [35mand[39;49;00m engineLib.LoadTriggers[addon]) [34mthen[39;49;00m
^I^I^I^I[34mif[39;49;00m (engineLib.OnLoad) [34mthen[39;49;00m
^I^I^I^I^IengineLib.OnLoad(addon)
^I^I^I^I[34mend[39;49;00m
^I^I^I[34mend[39;49;00m
^I^I^I[34mif[39;49;00m (engineLib.Processor [35mand[39;49;00m auc == [33m"[39;49;00m[33mauc[39;49;00m[33m"[39;49;00m [35mand[39;49;00m sys [35mand[39;49;00m eng) [34mthen[39;49;00m
^I^I^I^IengineLib.Processor([33m"[39;49;00m[33mload[39;49;00m[33m"[39;49;00m, addon)
^I^I^I[34mend[39;49;00m
^I^I[34mend[39;49;00m
^I[34mend[39;49;00m
[34mend[39;49;00m

[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mOnUnload[39;49;00m()
^I[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m
^I^I[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m
^I^I^I[34mif[39;49;00m (engineLib.OnUnload) [34mthen[39;49;00m
^I^I^I^IengineLib.OnUnload()
^I^I^I[34mend[39;49;00m
^I^I[34mend[39;49;00m
^I[34mend[39;49;00m
[34mend[39;49;00m

private.Schedule = {}
[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mOnEvent[39;49;00m(...)
^I[34mlocal[39;49;00m event, arg = [36mselect[39;49;00m([34m2[39;49;00m, ...)
^I[34mif[39;49;00m (event == [33m"[39;49;00m[33mADDON_LOADED[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m
^I^I[34mlocal[39;49;00m addon = [36mstring.lower[39;49;00m(arg)
^I^I[34mif[39;49;00m (addon:sub([34m1[39;49;00m,[34m4[39;49;00m) == [33m"[39;49;00m[33mauc-[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m
^I^I^Iprivate.OnLoad(addon)
^I^I[34mend[39;49;00m
^I[34melseif[39;49;00m (event == [33m"[39;49;00m[33mAUCTION_HOUSE_SHOW[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m
^I^I[37m-- Do Nothing for now[39;49;00m
^I[34melseif[39;49;00m (event == [33m"[39;49;00m[33mAUCTION_HOUSE_CLOSED[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m
^I^IAucAdvanced.Scan.Interrupt()
^I[34melseif[39;49;00m (event == [33m"[39;49;00m[33mPLAYER_LOGOUT[39;49;00m[33m"[39;49;00m) [34mthen[39;49;00m
^I^IAucAdvanced.Scan.Commit([34mtrue[39;49;00m)
^I^Iprivate.OnUnload()
^I[34melseif[39;49;00m event == [33m"[39;49;00m[33mUNIT_INVENTORY_CHANGED[39;49;00m[33m"[39;49;00m
^I[35mor[39;49;00m event == [33m"[39;49;00m[33mITEM_LOCK_CHANGED[39;49;00m[33m"[39;49;00m
^I[35mor[39;49;00m event == [33m"[39;49;00m[33mCURSOR_UPDATE[39;49;00m[33m"[39;49;00m
^I[35mor[39;49;00m event == [33m"[39;49;00m[33mBAG_UPDATE[39;49;00m[33m"[39;49;00m
^I[34mthen[39;49;00m
^I^Iprivate.Schedule[[33m"[39;49;00m[33minventory[39;49;00m[33m"[39;49;00m] = GetTime() + [34m0.15[39;49;00m
^I[34mend[39;49;00m
[34mend[39;49;00m

[34mfunction[39;49;00m [04m[32mprivate[39;49;00m.[32mOnUpdate[39;49;00m(...)
^I[34mif[39;49;00m event == [33m"[39;49;00m[33minventory[39;49;00m[33m"[39;49;00m [34mthen[39;49;00m
^I^IAucAdvanced.Post.AlertBagsChanged()
^I[34mend[39;49;00m

^I[34mlocal[39;49;00m now = GetTime()
^I[34mfor[39;49;00m event, time [34min[39;49;00m [36mpairs[39;49;00m(private.Schedule) [34mdo[39;49;00m
^I^I[34mif[39;49;00m time > now [34mthen[39;49;00m
^I^I^I[34mfor[39;49;00m system, systemMods [34min[39;49;00m [36mpairs[39;49;00m(AucAdvanced.Modules) [34mdo[39;49;00m
^I^I^I^I[34mfor[39;49;00m engine, engineLib [34min[39;49;00m [36mpairs[39;49;00m(systemMods) [34mdo[39;49;00m
^I^I^I^I^I[34mif[39;49;00m engineLib.Processor [34mthen[39;49;00m
^I^I^I^I^I^IengineLib.Processor(event, time)
^I^I^I^I^I[34mend[39;49;00m
^I^I^I^I[34mend[39;49;00m
^I^I^I[34mend[39;49;00m
^I^I[34mend[39;49;00m
^I^Iprivate.Schedule[event] = [34mnil[39;49;00m
^I[34mend[39;49;00m
[34mend[39;49;00m

private.Frame = CreateFrame([33m"[39;49;00m[33mFrame[39;49;00m[33m"[39;49;00m)
private.Frame:RegisterEvent([33m"[39;49;00m[33mADDON_LOADED[39;49;00m[33m"[39;49;00m)
private.Frame:RegisterEvent([33m"[39;49;00m[33mAUCTION_HOUSE_SHOW[39;49;00m[33m"[39;49;00m)
private.Frame:RegisterEvent([33m"[39;49;00m[33mAUCTION_HOUSE_CLOSED[39;49;00m[33m"[39;49;00m)
private.Frame:RegisterEvent([33m"[39;49;00m[33mUNIT_INVENTORY_CHANGED[39;49;00m[33m"[39;49;00m)
private.Frame:RegisterEvent([33m"[39;49;00m[33mITEM_LOCK_CHANGED[39;49;00m[33m"[39;49;00m)
private.Frame:RegisterEvent([33m"[39;49;00m[33mCURSOR_UPDATE[39;49;00m[33m"[39;49;00m)
private.Frame:RegisterEvent([33m"[39;49;00m[33mBAG_UPDATE[39;49;00m[33m"[39;49;00m)
private.Frame:RegisterEvent([33m"[39;49;00m[33mPLAYER_LOGOUT[39;49;00m[33m"[39;49;00m)
private.Frame:SetScript([33m"[39;49;00m[33mOnEvent[39;49;00m[33m"[39;49;00m, private.OnEvent)
private.Frame:SetScript([33m"[39;49;00m[33mOnUpdate[39;49;00m[33m"[39;49;00m, private.OnUpdate)

[37m-- Auctioneer's debug functions[39;49;00m
AucAdvanced.Debug = {}
[34mlocal[39;49;00m addonName = [33m"[39;49;00m[33mAuctioneer[39;49;00m[33m"[39;49;00m [37m-- the addon's name as it will be displayed in[39;49;00m
                               [37m-- the debug messages[39;49;00m
[37m-------------------------------------------------------------------------------[39;49;00m
[37m-- Prints the specified message to nLog.[39;49;00m
[37m--[39;49;00m
[37m-- syntax:[39;49;00m
[37m--    errorCode, message = debugPrint([message][, category][, title][, errorCode][, level])[39;49;00m
[37m--[39;49;00m
[37m-- parameters:[39;49;00m
[37m--    message   - (string) the error message[39;49;00m
[37m--                nil, no error message specified[39;49;00m
[37m--    category  - (string) the category of the debug message[39;49;00m
[37m--                nil, no category specified[39;49;00m
[37m--    title     - (string) the title for the debug message[39;49;00m
[37m--                nil, no title specified[39;49;00m
[37m--    errorCode - (number) the error code[39;49;00m
[37m--                nil, no error code specified[39;49;00m
[37m--    level     - (string) nLog message level[39;49;00m
[37m--                         Any nLog.levels string is valid.[39;49;00m
[37m--                nil, no level specified[39;49;00m
[37m--[39;49;00m
[37m-- returns:[39;49;00m
[37m--    errorCode - (number) errorCode, if one is specified[39;49;00m
[37m--                nil, otherwise[39;49;00m
[37m--    message   - (string) message, if one is specified[39;49;00m
[37m--                nil, otherwise[39;49;00m
[37m-------------------------------------------------------------------------------[39;49;00m
[34mfunction[39;49;00m [04m[32mAucAdvanced[39;49;00m.[04m[32mDebug[39;49;00m.[32mDebugPrint[39;49;00m(message, category, title, errorCode, level)
^I[34mreturn[39;49;00m DebugLib.DebugPrint(addonName, message, category, title, errorCode, level)
[34mend[39;49;00m

[37m-------------------------------------------------------------------------------[39;49;00m
[37m-- Used to make sure that conditions are met within functions.[39;49;00m
[37m-- If test is false, the error message will be written to nLog and the user's[39;49;00m
[37m-- default chat channel.[39;49;00m
[37m--[39;49;00m
[37m-- syntax:[39;49;00m
[37m--    assertion = assert(test, message)[39;49;00m
[37m--[39;49;00m
[37m-- parameters:[39;49;00m
[37m--    test    - (any)     false/nil, if the assertion failed[39;49;00m
[37m--                        anything else, otherwise[39;49;00m
[37m--    message - (string)  the message which will be output to the user[39;49;00m
[37m--[39;49;00m
[37m-- returns:[39;49;00m
[37m--    assertion - (boolean) true, if the test passed[39;49;00m
[37m--                          false, otherwise[39;49;00m
[37m-------------------------------------------------------------------------------[39;49;00m
[34mfunction[39;49;00m [04m[32mAucAdvanced[39;49;00m.[04m[32mDebug[39;49;00m.[32mAssert[39;49;00m(test, message)
^I[34mreturn[39;49;00m DebugLib.Assert(addonName, test, message)
[34mend[39;49;00m

[37m--[==[[39;49;00m
[37mHere follow further tests of Lua syntax.[39;49;00m
[37m]]==][39;49;00m
[37m---[[[39;49;00m
[34mlocal[39;49;00m t = {
        [ [33m[[[39;49;00m
[33mx[39;49;00m
[33m]==] \]][39;49;00m]=[34m1[39;49;00m|[34m2[39;49;00m; a={b={c={}}},
        [34m1[39;49;00m, [34m1.[39;49;00m, [34m1.2[39;49;00m, [34m.2[39;49;00m, [34m1e3[39;49;00m, [34m1.e3[39;49;00m, [34m1.2e3[39;49;00m, [34m.2e3[39;49;00m, [34m1.2e+3[39;49;00m, [34m1.2E-3[39;49;00m;
        [34m0xA[39;49;00m, [34m0Xa[39;49;00m, [34m0xA.[39;49;00m, [34m0x.F[39;49;00m, [34m0xA.F[39;49;00m, [34m0xA.Fp1[39;49;00m, [34m0xA.FP+1[39;49;00m, [34m0Xa.fp-1[39;49;00m;
}

[34mfunction[39;49;00m [04m[32mt[39;49;00m.[32mf[39;49;00m()
        [34mgoto[39;49;00m eof
        [36mos.exit[39;49;00m()
        :: eof ::
[34mend[39;49;00m

[34mfunction[39;49;00m [04m[32mt[39;49;00m . [04m[32ma[39;49;00m [37m--[==[x]==][39;49;00m .[04m[32mb[39;49;00m [37m--[==[y]==][39;49;00m [37m--[39;49;00m
[37m-- () end[39;49;00m
           . [04m[32mc[39;49;00m : [32md[39;49;00m (file)
        [34mreturn[39;49;00m [33m'[39;49;00m[33m.[39;49;00m[33m\a[39;49;00m[33m.[39;49;00m[33m\b[39;49;00m[33m.[39;49;00m[33m\f[39;49;00m[33m.[39;49;00m[33m\n[39;49;00m[33m.[39;49;00m[33m\r[39;49;00m[33m.[39;49;00m[33m\t[39;49;00m[33m.[39;49;00m[33m\v[39;49;00m[33m.[39;49;00m[33m\\[39;49;00m[33m.[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m[33m\'[39;49;00m[33m.[39;49;00m[33m\[39;49;00m
[33m.[39;49;00m[33m\z    [39;49;00m
[33m  ^I [39;49;00m[33m.[39;49;00m[33m\0[39;49;00m[33m.[39;49;00m[33m\00[39;49;00m[33m.[39;49;00m[33m\000[39;49;00m[33m.[39;49;00m[33m\000[39;49;00m[33m0.[39;49;00m[33m\xFa[39;49;00m[33m.[39;49;00m[33m\u{1}[39;49;00m[33m.[39;49;00m[33m\u{1234}[39;49;00m[33m'[39;49;00m
[34mend[39;49;00m
