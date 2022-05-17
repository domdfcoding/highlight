[37m--[39;49;00m[37m[39;49;00m
[37m-- Example of a fragment of an openEHR Archetype, written in the Object Data Instance Notation (ODIN)[39;49;00m[37m[39;49;00m
[37m-- Definition available here: https://github.com/openEHR/odin[39;49;00m[37m[39;49;00m
[37m-- Author: Thomas Beale[39;49;00m[37m[39;49;00m
[37m--[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[04m[32moriginal_author[39;49;00m[37m [39;49;00m=[37m [39;49;00m<[37m[39;49;00m
[37m        [39;49;00m[[33m"[39;49;00m[33mname[39;49;00m[33m"[39;49;00m][37m [39;49;00m=[37m [39;49;00m<[33m"[39;49;00m[33mDr J Joyce[39;49;00m[33m"[39;49;00m>[37m[39;49;00m
[37m        [39;49;00m[[33m"[39;49;00m[33morganisation[39;49;00m[33m"[39;49;00m][37m [39;49;00m=[37m [39;49;00m<[33m"[39;49;00m[33mNT Health Service[39;49;00m[33m"[39;49;00m>[37m[39;49;00m
[37m        [39;49;00m[[33m"[39;49;00m[33mdate[39;49;00m[33m"[39;49;00m][37m [39;49;00m=[37m [39;49;00m<2003-08-03>[37m[39;49;00m
[37m    [39;49;00m>[37m[39;49;00m
[37m    [39;49;00m[04m[32mterm_bindings[39;49;00m[37m [39;49;00m=[37m [39;49;00m<[37m[39;49;00m
[37m        [39;49;00m[[33m"[39;49;00m[33mumls[39;49;00m[33m"[39;49;00m][37m [39;49;00m=[37m [39;49;00m<[37m[39;49;00m
[37m            [39;49;00m[[33m"[39;49;00m[33mid1[39;49;00m[33m"[39;49;00m][37m [39;49;00m=[37m [39;49;00m<http://umls.nlm.edu/id/C124305>[37m [39;49;00m[37m-- apgar result[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[[33m"[39;49;00m[33mid2[39;49;00m[33m"[39;49;00m][37m [39;49;00m=[37m [39;49;00m<http://umls.nlm.edu/id/0000000>[37m [39;49;00m[37m-- 1-minute event [39;49;00m[37m[39;49;00m
[37m        [39;49;00m>[37m[39;49;00m
[37m    [39;49;00m>[37m[39;49;00m
[37m    [39;49;00m[04m[32mlifecycle_state[39;49;00m[37m [39;49;00m=[37m  [39;49;00m<[33m"[39;49;00m[33minitial[39;49;00m[33m"[39;49;00m>[37m[39;49;00m
[37m    [39;49;00m[04m[32mresource_package_uri[39;49;00m[37m [39;49;00m=[37m  [39;49;00m<[33m"[39;49;00m[33mhttp://www.aihw.org.au/data_sets/diabetic_archetypes.html[39;49;00m[33m"[39;49;00m>[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[04m[32mdetails[39;49;00m[37m [39;49;00m=[37m [39;49;00m<[37m[39;49;00m
[37m        [39;49;00m[[33m"[39;49;00m[33men[39;49;00m[33m"[39;49;00m][37m [39;49;00m=[37m [39;49;00m<[37m[39;49;00m
[37m            [39;49;00m[04m[32mlanguage[39;49;00m[37m [39;49;00m=[37m [39;49;00m<[[90miso_639-1[39;49;00m::[90men[39;49;00m]>[37m[39;49;00m
[37m            [39;49;00m[04m[32mpurpose[39;49;00m[37m [39;49;00m=[37m  [39;49;00m<[33m"[39;49;00m[33marchetype for diabetic patient review[39;49;00m[33m"[39;49;00m>[37m[39;49;00m
[37m            [39;49;00m[04m[32muse[39;49;00m[37m [39;49;00m=[37m [39;49;00m<[33m"[39;49;00m[33mused for all hospital or clinic-based diabetic reviews, [39;49;00m
[33m                including first time. Optional sections are removed according to the particular review[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m            [39;49;00m>[37m[39;49;00m
[37m            [39;49;00m[04m[32mmisuse[39;49;00m[37m [39;49;00m=[37m [39;49;00m<[33m"[39;49;00m[33mnot appropriate for pre-diagnosis use[39;49;00m[33m"[39;49;00m>[37m[39;49;00m
[37m            [39;49;00m[04m[32moriginal_resource_uri[39;49;00m[37m [39;49;00m=[37m [39;49;00m<[33m"[39;49;00m[33mhttp://www.healthdata.org.au/data_sets/diabetic_review_data_set_1.html[39;49;00m[33m"[39;49;00m>[37m[39;49;00m
[37m        [39;49;00m>[37m[39;49;00m
[37m        [39;49;00m[[33m"[39;49;00m[33mde[39;49;00m[33m"[39;49;00m][37m [39;49;00m=[37m [39;49;00m<[37m[39;49;00m
[37m            [39;49;00m[04m[32mlanguage[39;49;00m[37m [39;49;00m=[37m [39;49;00m<[[90miso_639-1[39;49;00m::[90mde[39;49;00m]>[37m[39;49;00m
[37m            [39;49;00m[04m[32mpurpose[39;49;00m[37m [39;49;00m=[37m  [39;49;00m<[33m"[39;49;00m[33mArchetyp für die Untersuchung von Patienten mit Diabetes[39;49;00m[33m"[39;49;00m>[37m[39;49;00m
[37m            [39;49;00m[04m[32muse[39;49;00m[37m [39;49;00m=[37m [39;49;00m<[33m"[39;49;00m[33mwird benutzt für alle Diabetes-Untersuchungen im[39;49;00m
[33m                    Krankenhaus, inklusive der ersten Vorstellung. Optionale[39;49;00m
[33m                    Abschnitte werden in Abhängigkeit von der speziellen[39;49;00m
[33m                    Vorstellung entfernt.[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m            [39;49;00m>[37m[39;49;00m
[37m            [39;49;00m[04m[32mmisuse[39;49;00m[37m [39;49;00m=[37m [39;49;00m<[33m"[39;49;00m[33mnicht geeignet für Benutzung vor Diagnosestellung[39;49;00m[33m"[39;49;00m>[37m[39;49;00m
[37m            [39;49;00m[04m[32moriginal_resource_uri[39;49;00m[37m [39;49;00m=[37m [39;49;00m<[33m"[39;49;00m[33mhttp://www.healthdata.org.au/data_sets/diabetic_review_data_set_1.html[39;49;00m[33m"[39;49;00m>[37m[39;49;00m
[37m        [39;49;00m>[37m[39;49;00m
[37m    [39;49;00m>[37m[39;49;00m
[37m^I[39;49;00m
