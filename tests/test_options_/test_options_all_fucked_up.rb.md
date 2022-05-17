     1^I[37m# vim:ft=ruby[39;49;00m$
     2^I$
     3^Ievents = [31mHash[39;49;00m.new { |h, k| h[k] = [] }$
     4^I[31mDATA[39;49;00m.read.split([33m/[39;49;00m[33m\[39;49;00m[33mn[39;49;00m[33m\[39;49;00m[33mn[39;49;00m[33m\[39;49;00m[33mn[39;49;00m[33m\[39;49;00m[33ms*[39;49;00m[33m/[39;49;00m).each [34mdo[39;49;00m |event|$
     5^I^I[36mname[39;49;00m = event[[33m/[39;49;00m[33m^.*[39;49;00m[33m/[39;49;00m].sub([33m/[39;49;00m[33mhttp:.*[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m'[39;49;00m)$
     6^I^Ievent[[33m/[39;49;00m[33m\[39;49;00m[33mn.*[39;49;00m[33m/m[39;49;00m].scan([33m/[39;49;00m[33m^([A-Z]{2}[39;49;00m[33m\[39;49;00m[33mS*)[39;49;00m[33m\[39;49;00m[33ms*([39;49;00m[33m\[39;49;00m[33mS*)[39;49;00m[33m\[39;49;00m[33ms*([39;49;00m[33m\[39;49;00m[33mS*)([39;49;00m[33m\[39;49;00m[33ms*[39;49;00m[33m\[39;49;00m[33mS*)[39;49;00m[33m/[39;49;00m) [34mdo[39;49;00m |kind, day, daytime, comment|$
     7^I^I^Ievents[ [day, daytime] ] << [kind, [36mname[39;49;00m + comment]$
     8^I^I[34mend[39;49;00m$
     9^I[34mend[39;49;00m$
    10^I$
    11^Iconflicts = [34m0[39;49;00m$
    12^Ievents.to_a.sort_by [34mdo[39;49;00m |(day, daytime),|$
    13^I^I[[33m%w([39;49;00m[33mMo Di Mi Do Fr[39;49;00m[33m)[39;49;00m.index(day) || [34m0[39;49;00m, daytime]$
    14^I[34mend[39;49;00m.each [34mdo[39;49;00m |(day, daytime), names|$
    15^I^I[34mif[39;49;00m names.size > [34m1[39;49;00m$
    16^I^I^Iconflicts += [34m1[39;49;00m$
    17^I^I^I[36mprint[39;49;00m [33m'[39;49;00m[33m!!! [39;49;00m[33m'[39;49;00m$
    18^I^I[34mend[39;49;00m$
    19^I^I[36mprint[39;49;00m [33m"[39;49;00m[33m#{[39;49;00mday[33m}[39;49;00m[33m [39;49;00m[33m#{[39;49;00mdaytime[33m}[39;49;00m[33m: [39;49;00m[33m"[39;49;00m$
    20^I^Inames.each { |kind, [36mname[39;49;00m| [36mputs[39;49;00m [33m"[39;49;00m[33m  [39;49;00m[33m#{[39;49;00mkind[33m}[39;49;00m[33m  [39;49;00m[33m#{[39;49;00m[36mname[39;49;00m[33m}[39;49;00m[33m"[39;49;00m }$
    21^I^I[36mputs[39;49;00m$
    22^I[34mend[39;49;00m$
    23^I$
    24^I[36mputs[39;49;00m [33m'[39;49;00m[33m%d conflicts[39;49;00m[33m'[39;49;00m % conflicts$
    25^I[36mputs[39;49;00m [33m'[39;49;00m[33m%d SWS[39;49;00m[33m'[39;49;00m % (events.inject([34m0[39;49;00m) { |sum, ((day, daytime),)| sum + (daytime[[33m/[39;49;00m[33m\[39;49;00m[33md+$[39;49;00m[33m/[39;49;00m].to_i - daytime[[33m/[39;49;00m[33m^[39;49;00m[33m\[39;49;00m[33md+[39;49;00m[33m/[39;49;00m].to_i) })$
    26^I$
    27^Istring = [33m% foo [39;49;00m    [37m# strange. huh?[39;49;00m$
    28^I[36mprint[39;49;00m [33m"[39;49;00m[33mEscape here: [39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
    29^I[36mprint[39;49;00m [33m'[39;49;00m[33mDont escape here: [39;49;00m[33m\n[39;49;00m[33m'[39;49;00m$
    30^I$
    31^I[36m__END__[39;49;00m[36m[39;49;00m$
    32^I[36mInformatik und Informationsgesellschaft I: Digitale Medien (32 214)[39;49;00m$
    33^I[36mComputer lassen ihre eigentliche Bestimmung durch Multimedia und Vernetzung erkennen: Es sind digitale Medien, die alle bisherigen Massen- und Kommunikationsmedien simulieren, kopieren oder ersetzen können. Die kurze Geschichte elektronischer Medien vom Telegramm bis zum Fernsehen wird so zur Vorgeschichte des Computers als Medium. Der Prozess der Mediatisierung der Rechnernetze soll in Technik, Theorie und Praxis untersucht werden. Das PR soll die Techniken der ortsverteilten und zeitversetzten Lehre an Hand praktischer Übungen vorführen und untersuchen.[39;49;00m$
    34^I[36mVL ^IDi^I15-17^Iwöch.^IRUD 25, 3.101^IJ. Koubek[39;49;00m$
    35^I[36mVL^IDo^I15-17^Iwöch.^IRUD 25, 3.101[39;49;00m$
    36^I[36mUE/PR^IDo^I17-19^Iwöch.^IRUD 25, 3.101^IJ.-M. Loebel[39;49;00m$
    37^I[36m[39;49;00m$
    38^I[36m[39;49;00m$
    39^I[36mMethoden und Modelle des Systementwurfs (32 223)[39;49;00m$
    40^I[36mGute Methoden zum Entwurf und zur Verifikation von Systemen sind ein Schlüssel für gute Software. Dieses Seminar betrachtet moderne Entwurfsmethoden.[39;49;00m$
    41^I[36m VL^IDi^I09-11^Iwöch.^IRUD 26, 0313^IW. Reisig[39;49;00m$
    42^I[36m VL^IDo^I09-11^Iwöch.^IRUD 26, 0313^I[39;49;00m$
    43^I[36m UE^IDi^I11-13^Iwöch.^IRUD 26, 0313^I[39;49;00m$
    44^I[36m PR^IDi^I13-15^Iwöch.^IRUD 26, 0313^ID. Weinberg[39;49;00m$
    45^I[36m[39;49;00m$
    46^I[36m[39;49;00m$
    47^I[36mKomplexitätstheorie (32 229)[39;49;00m$
    48^I[36mIn dieser Vorlesung untersuchen wir eine Reihe von wichtigen algorithmischen Problemstellungen aus verschiedenen Bereichen der Informatik. Unser besonderes Interesse gilt dabei der Abschätzung der Rechenressourcen, die zu ihrer Lösung aufzubringen sind.  Die Vorlesung bildet eine wichtige Grundlage für weiterführende Veranstaltungen in den Bereichen Algorithmen, Kryptologie, Algorithmisches Lernen und Algorithmisches Beweisen.[39;49;00m$
    49^I[36m VL ^IDi^I09-11^Iwöch.^IRUD 26, 1303^IJ. Köbler[39;49;00m$
    50^I[36m VL^IDo^I09-11^Iwöch.^IRUD 26, 1305^I[39;49;00m$
    51^I[36m UE^IDo^I11-13^Iwöch.^IRUD 26, 1305^I[39;49;00m$
    52^I[36m[39;49;00m$
    53^I[36m[39;49;00m$
    54^I[36mZuverlässige Systeme (32 234)[39;49;00m$
    55^I[36mMit zunehmender Verbreitung der Computertechnologie in immer mehr Bereichen des menschlichen Lebens wird die Zuverlässigkeit solcher Systeme zu einer immer zentraleren Frage.[39;49;00m$
    56^I[36mDer Halbkurs "Zuverlässige Systeme" konzentriert sich auf folgende Schwerpunkte: Zuverlässigkeit, Fehlertoleranz, Responsivität, Messungen, Anwendungen, Systemmodelle und Techniken, Ausfallverhalten, Fehlermodelle, Schedulingtechniken, Software/Hardware - responsives Systemdesign, Analyse und Synthese, Bewertung, Fallstudien in Forschung und Industrie.[39;49;00m$
    57^I[36mDer Halbkurs kann mit dem Halbkurs "Eigenschaften mobiler und eingebetteter Systeme" zu einem Projektkurs kombiniert werden. Ein gemeinsames Projekt begleitet beide Halbkurse.[39;49;00m$
    58^I[36mVL ^IDi^I09-11^Iwöch.^IRUD 26, 1308^IM. Malek[39;49;00m$
    59^I[36mVL^IDo^I09-11^Iwöch.^IRUD 26, 1308[39;49;00m$
    60^I[36mPR^In.V.[39;49;00m$
    61^I[36m[39;49;00m$
    62^I[36m[39;49;00m$
    63^I[36mStochastik für InformatikerInnen (32 239)[39;49;00m$
    64^I[36mGrundlagen der Wahrscheinlichkeitsrechnung, Diskrete und stetige Wahrscheinlichkeitsmodelle in der Informatik, Grenzwertsätze, Simulationsverfahren, Zufallszahlen, Statistische Schätz- und Testverfahren, Markoffsche Ketten, Simulated Annealing, Probabilistische Analyse von Algorithmen.[39;49;00m$
    65^I[36mVL^IMo^I09-11^Iwöch.^IRUD 25, 3.101^IW. Kössler[39;49;00m$
    66^I[36mVL^IMi^I09-11^Iwöch.^IRUD 25, 3.101[39;49;00m$
    67^I[36mUE^IMo^I11-13^Iwöch.^IRUD 25, 3.101[39;49;00m$
    68^I[36m UE^IMi^I11-13^Iwöch.^IRUD 25. 3.101[39;49;00m$
    69^I[36m[39;49;00m$
    70^I[36m[39;49;00m$
    71^I[36mGeschichte der Informatik  Ausgewählte Kapitel (32 243)[39;49;00m$
    72^I[36mVL^IMi^I13-15^Iwöch.^IRUD 25, 3.113^IW. Coy[39;49;00m$
    73^I[36m[39;49;00m$
    74^I[36m[39;49;00m$
    75^I[36mAktuelle Themen der Theoretischen Informatik (32 260)[39;49;00m$
    76^I[36mIn diesem Seminar sollen wichtige aktuelle Veröffentlichungen aus der theoretischen Informatik gemeinsam erarbeitet werden. Genaueres wird erst kurz vor dem Seminar entschieden. Bei Interesse wenden Sie sich bitte möglichst frühzeitig an den Veranstalter.[39;49;00m$
    77^I[36m SE^IFr^I09-11^Iwöch.^IRUD 26, 1307^IM. Grohe [39;49;00m$
