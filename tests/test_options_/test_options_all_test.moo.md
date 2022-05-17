     1^Iyou_lose_msg = [33m"Either that person does not exist, or has a different password."[39;49;00m;$
     2^I[34mif[39;49;00m (!([31mcaller[39;49;00m [34min[39;49;00m {#0, [31mthis[39;49;00m}))$
     3^I  [34mreturn[39;49;00m [36mE_PERM[39;49;00m;$
     4^I  [33m"...caller isn't :do_login_command..."[39;49;00m;$
     5^I[34melseif[39;49;00m ([31margs[39;49;00m && ([31margs[39;49;00m[[34m1[39;49;00m] == [33m"test"[39;49;00m))$
     6^I  [34mreturn[39;49;00m [31mthis[39;49;00m:[32mtest[39;49;00m(@[32mlistdelete[39;49;00m([31margs[39;49;00m, [34m1[39;49;00m));$
     7^I[34melseif[39;49;00m (!([36mlength[39;49;00m([31margs[39;49;00m) [34min[39;49;00m {[34m1[39;49;00m, [34m2[39;49;00m}))$
     8^I  [32mnotify[39;49;00m([31mplayer[39;49;00m, [32mtostr[39;49;00m([33m"Usage:  "[39;49;00m, verb, [33m" <existing-player-name> <password>"[39;49;00m));$
     9^I[34melseif[39;49;00m (![32mvalid[39;49;00m(candidate = [31mthis[39;49;00m:[32m_match_player[39;49;00m(name = [32mstrsub[39;49;00m([31margs[39;49;00m[[34m1[39;49;00m], [33m" "[39;49;00m, [33m"_"[39;49;00m))))$
    10^I  [34mif[39;49;00m (name == [33m"guest"[39;49;00m)$
    11^I    [33m"must be no guests"[39;49;00m;$
    12^I    [31mthis[39;49;00m:[32mnotify_lines[39;49;00m([31mthis[39;49;00m:[32mregistration_text[39;49;00m([33m"guest"[39;49;00m));$
    13^I  [34melse[39;49;00m$
    14^I    [32mnotify[39;49;00m([31mplayer[39;49;00m, you_lose_msg);$
    15^I  [34mendif[39;49;00m$
    16^I  [33m"...unknown player..."[39;49;00m;$
    17^I[34melseif[39;49;00m ([32mis_clear_property[39;49;00m(candidate, [33m"password"[39;49;00m) || (([32mtypeof[39;49;00m(candidate.password) == STR) && (([36mlength[39;49;00m(candidate.password) < [34m2[39;49;00m) || ([32mcrypt[39;49;00m({@[31margs[39;49;00m, [33m""[39;49;00m}[[34m2[39;49;00m], candidate.password) != candidate.password))))$
    18^I  [32mnotify[39;49;00m([31mplayer[39;49;00m, you_lose_msg);$
    19^I  [33m"...bad password..."[39;49;00m;$
    20^I  [32mserver_log[39;49;00m([32mtostr[39;49;00m([33m"FAILED CONNECT: "[39;49;00m, [31margs[39;49;00m[[34m1[39;49;00m], [33m" ("[39;49;00m, candidate, [33m") on "[39;49;00m, [32mconnection_name[39;49;00m([31mplayer[39;49;00m), ($string_utils:[32mconnection_hostname[39;49;00m([32mconnection_name[39;49;00m([31mplayer[39;49;00m)) [34min[39;49;00m candidate.all_connect_places) ? [33m""[39;49;00m | [33m"******"[39;49;00m));$
    21^I[34melseif[39;49;00m (((candidate.name == [33m"guest"[39;49;00m) && [31mthis[39;49;00m.sitematch_guests) && [32mvalid[39;49;00m(foreigner = $country_db:[32mget_guest[39;49;00m()))$
    22^I  [32mnotify[39;49;00m([31mplayer[39;49;00m, [32mtostr[39;49;00m([33m"Okay,...  Logging you in as `"[39;49;00m, foreigner:[32mname[39;49;00m(), [33m"'"[39;49;00m));$
    23^I  [31mthis[39;49;00m:[32mrecord_connection[39;49;00m(foreigner);$
    24^I  [34mreturn[39;49;00m foreigner;$
    25^I[34melseif[39;49;00m (([32mparent[39;49;00m(candidate) == $guest) && (![32mvalid[39;49;00m(candidate = candidate:[32mdefer[39;49;00m())))$
    26^I  [34mif[39;49;00m (candidate == #-3)$
    27^I    [32mnotify[39;49;00m([31mplayer[39;49;00m, [33m"Sorry, guest characters are not allowed from your site right now."[39;49;00m);$
    28^I  [34melseif[39;49;00m (candidate == #-2)$
    29^I    [31mthis[39;49;00m:[32mnotify_lines[39;49;00m([31mthis[39;49;00m:[32mregistration_text[39;49;00m([33m"blacklisted"[39;49;00m, [33m"Sorry, guest characters are not allowed from your site."[39;49;00m));$
    30^I  [34melseif[39;49;00m (candidate == #-4)$
    31^I    [31mthis[39;49;00m:[32mnotify_lines[39;49;00m([31mthis[39;49;00m:[32mregistration_text[39;49;00m([33m"guest"[39;49;00m));$
    32^I  [34melse[39;49;00m$
    33^I    [32mnotify[39;49;00m([31mplayer[39;49;00m, [33m"Sorry, all of our guest characters are in use right now."[39;49;00m);$
    34^I  [34mendif[39;49;00m$
    35^I[34melse[39;49;00m$
    36^I  [34mif[39;49;00m ((!(name [34min[39;49;00m candidate.aliases)) && (name != [32mtostr[39;49;00m(candidate)))$
    37^I    [32mnotify[39;49;00m([31mplayer[39;49;00m, [32mtostr[39;49;00m([33m"Okay,... "[39;49;00m, name, [33m" is in use.  Logging you in as `"[39;49;00m, candidate:[32mname[39;49;00m(), [33m"'"[39;49;00m));$
    38^I  [34mendif[39;49;00m$
    39^I  [34mif[39;49;00m ([31mthis[39;49;00m:[32mis_newted[39;49;00m(candidate))$
    40^I    [32mnotify[39;49;00m([31mplayer[39;49;00m, [33m""[39;49;00m);$
    41^I    [32mnotify[39;49;00m([31mplayer[39;49;00m, [31mthis[39;49;00m:[32mnewt_message_for[39;49;00m(candidate));$
    42^I    [32mnotify[39;49;00m([31mplayer[39;49;00m, [33m""[39;49;00m);$
    43^I  [34melse[39;49;00m$
    44^I    [31mthis[39;49;00m:[32mrecord_connection[39;49;00m(candidate);$
    45^I    [34mif[39;49;00m (verb[[34m1[39;49;00m] == [33m"s"[39;49;00m)$
    46^I      candidate.use_do_command = [34m0[39;49;00m;$
    47^I    [34mendif[39;49;00m$
    48^I    [34mreturn[39;49;00m candidate;$
    49^I  [34mendif[39;49;00m$
    50^I[34mendif[39;49;00m$
    51^I[34mreturn[39;49;00m [34m0[39;49;00m;$
