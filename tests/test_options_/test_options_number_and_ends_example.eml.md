     1	[94mMime-Version:[39;49;00m[37m [39;49;00m1.0[37m [39;49;00m(Apple[37m [39;49;00mMessage[37m [39;49;00mframework[37m [39;49;00mv730)[37m[39;49;00m$
     2	[94mContent-Type:[39;49;00m[37m [39;49;00mmultipart[33m/[39;49;00mmixed;[37m [39;49;00m[36mboundary[39;49;00m=[33mApple-Mail-13-196941151[39;49;00m[37m[39;49;00m$
     3	[94mMessage-Id:[39;49;00m[37m [39;49;00m<9169D984-4E0B-45EF-82D4-8F5E53AD7012@example.com>[37m[39;49;00m$
     4	[94mFrom:[39;49;00m[37m [39;49;00mfoo@example.com[37m[39;49;00m$
     5	[94mSubject:[39;49;00m[37m [39;49;00mtesting[37m[39;49;00m$
     6	[94mDate:[39;49;00m[37m [39;49;00m[90mMon, 6 Jun 2005 22:21:22 +0200[39;49;00m[37m[39;49;00m$
     7	[94mTo:[39;49;00m[37m [39;49;00mblah@example.com[37m[39;49;00m$
     8	[37m[39;49;00m$
     9	$
    10	[33m--Apple-Mail-13-196941151[39;49;00m$
    11	[94mContent-Transfer-Encoding:[39;49;00m[37m [39;49;00m[31mquoted-printable[39;49;00m[37m[39;49;00m$
    12	[94mContent-Type:[39;49;00m[37m [39;49;00mtext[33m/[39;49;00mplain;[37m[39;49;00m$
    13	[37m	[39;49;00m[36mcharset[39;49;00m=[33mISO-8859-1[39;49;00m;[37m[39;49;00m$
    14	[37m	[39;49;00m[36mdelsp[39;49;00m=[33myes[39;49;00m;[37m[39;49;00m$
    15	[37m	[39;49;00m[36mformat[39;49;00m=[33mflowed[39;49;00m[37m[39;49;00m$
    16	[37m[39;49;00m$
    17	This is the first part.$
    18	$
    19	[33m--Apple-Mail-13-196941151[39;49;00m$
    20	Content-Type: message/rfc822;$
    21	  name="ForwardedMessage.eml";$
    22	$
    23	Return-Path: <xxxx@xxxx.com>$
    24	X-Original-To: xxxx@xxxx.com$
    25	Delivered-To: xxxx@xxxx.com$
    26	Received: from localhost (localhost [127.0.0.1])$
    27		by xxx.xxxxx.com (Postfix) with ESMTP id 50FD3A96F$
    28		for <xxxx@xxxx.com>; Tue, 10 May 2005 17:26:50 +0000 (GMT)$
    29	Received: from xxx.xxxxx.com ([127.0.0.1])$
    30	 by localhost (xxx.xxxxx.com [127.0.0.1]) (amavisd-new, port 10024)$
    31	 with LMTP id 70060-03 for <xxxx@xxxx.com>;$
    32	 Tue, 10 May 2005 17:26:49 +0000 (GMT)$
    33	Received: from xxx.xxxxx.com (xxx.xxxxx.com [69.36.39.150])$
    34		by xxx.xxxxx.com (Postfix) with ESMTP id 8B957A94B$
    35		for <xxxx@xxxx.com>; Tue, 10 May 2005 17:26:48 +0000 (GMT)$
    36	Received: from xxx.xxxxx.com (xxx.xxxxx.com [64.233.184.203])$
    37		by xxx.xxxxx.com (Postfix) with ESMTP id 9972514824C$
    38		for <xxxx@xxxx.com>; Tue, 10 May 2005 12:26:40 -0500 (CDT)$
    39	Received: by xxx.xxxxx.com with SMTP id 68so1694448wri$
    40	        for <xxxx@xxxx.com>; Tue, 10 May 2005 10:26:40 -0700 (PDT)$
    41	DomainKey-Signature: a=rsa-sha1; q=dns; c=nofws;$
    42	        s=beta; d=xxxxx.com;$
    43	        h=received:message-id:date:from:reply-to:to:subject:mime-version:content-type;$
    44	        b=g8ZO5ttS6GPEMAz9WxrRk9+9IXBUfQIYsZLL6T88+ECbsXqGIgfGtzJJFn6o9CE3/HMrrIGkN5AisxVFTGXWxWci5YA/7PTVWwPOhJff5BRYQDVNgRKqMl/SMttNrrRElsGJjnD1UyQ/5kQmcBxq2PuZI5Zc47u6CILcuoBcM+A=$
    45	Received: by 10.54.96.19 with SMTP id t19mr621017wrb;$
    46	        Tue, 10 May 2005 10:26:39 -0700 (PDT)$
    47	Received: by 10.54.110.5 with HTTP; Tue, 10 May 2005 10:26:39 -0700 (PDT)$
    48	Message-ID: <xxxx@xxxx.com>$
    49	Date: Tue, 10 May 2005 11:26:39 -0600$
    50	From: Test Tester <xxxx@xxxx.com>$
    51	Reply-To: Test Tester <xxxx@xxxx.com>$
    52	To: xxxx@xxxx.com, xxxx@xxxx.com$
    53	Subject: Another PDF$
    54	Mime-Version: 1.0$
    55	Content-Type: multipart/mixed;$
    56		boundary="----=_Part_2192_32400445.1115745999735"$
    57	X-Virus-Scanned: amavisd-new at textdrive.com$
    58	$
    59	------=_Part_2192_32400445.1115745999735$
    60	Content-Type: text/plain; charset=ISO-8859-1$
    61	Content-Transfer-Encoding: quoted-printable$
    62	Content-Disposition: inline$
    63	$
    64	Just attaching another PDF, here, to see what the message looks like,$
    65	and to see if I can figure out what is going wrong here.$
    66	$
    67	------=_Part_2192_32400445.1115745999735$
    68	Content-Type: application/pdf; name="broken.pdf"$
    69	Content-Transfer-Encoding: base64$
    70	Content-Disposition: attachment; filename="broken.pdf"$
    71	$
    72	JVBERi0xLjQNCiXk9tzfDQoxIDAgb2JqDQo8PCAvTGVuZ3RoIDIgMCBSDQogICAvRmlsdGVyIC9G$
    73	bGF0ZURlY29kZQ0KPj4NCnN0cmVhbQ0KeJy9Wt2KJbkNvm/od6jrhZxYln9hWEh2p+8HBvICySaE$
    74	ycLuTV4/1ifJ9qnq09NpSBimu76yLUuy/qzqcPz7+em3Ixx/CDc6CsXxs3b5+fvfjr/8cPz6/BRu$
    75	rbfAx/n3739/fuJylJ5u5fjX81OuDr4deK4Bz3z/aDP+8fz0yw8g0Ofq7ktr1Mn+u28rvhy/jVeD$
    76	QSa+9YNKHP/pxjvDNfVAx/m3MFz54FhvTbaseaxiDoN2LeMVMw+yA7RbHSCDzxZuaYB2E1Yay7QU$
    77	x89vz0+tyFDKMlAHK5yqLmnjF+c4RjEiQIUeKwblXMe+AsZjN1J5yGQL5DHpDHksurM81rF6PKab$
    78	gK6zAarIDzIiUY23rJsN9iorAE816aIu6lsgAdQFsuhhkHOUFgVjp2GjMqSewITXNQ27jrMeamkg$
    79	1rPI3iLWG2CIaSBB+V1245YVRICGbbpYKHc2USFDl6M09acQVQYhlwIrkBNLISvXhGlF1wi5FHCw$
    80	wxZkoGNJlVeJCEsqKA+3YAV5AMb6KkeaqEJQmFKKQU8T1pRi2ihE1Y4CDrqoYFFXYjJJOatsyzuI$
    81	8SIlykuxKTMibWK8H1PgEvqYgs4GmQSrEjJAalgGirIhik+p4ZQN9E3ETFPAHE1b8pp1l/0Rc1gl$
    82	fQs0ABWvyoZZzU8VnPXwVVcO9BEsyjEJaO6eBoZRyKGlrKoYoOygA8BGIzgwN3RQ15ouigG5idZQ$
    83	fx2U4Db2CqiLO0WHAZoylGiCAqhniNQjFjQPSkmjwfNTgQ6M1Ih+eWo36wFmjIxDJZiGUBiWsAyR$
    84	xX3EekGOizkGI96Ol9zVZTAivikURhRsHh2E3JhWMpSTZCnnonrLhMCodgrNcgo4uyJUJc6qnVss$
    85	nrGd1Ptr0YwisCOYyIbUwVjV4xBUNLbguSO2YHujonAMJkMdSI7bIw91Akq2AUlMUWGFTMAOamjU$
    86	OvZQCxIkY2pCpMFo/IwLdVLHs6nddwTRrgoVbvLU9eB0G4EMndV0TNoxHbt3JBWwK6hhv3iHfDtF$
    87	yokB302IpEBTnWICde4uYc/1khDbSIkQopO6lcqamGBu1OSE3N5IPSsZX00CkSHRiiyx6HQIShsS$
    88	HSVNswdVsaOUSAWq9aYhDtGDaoG5a3lBGkYt/lFlBFt1UqrYnzVtUpUQnLiZeouKgf1KhRBViRRk$
    89	ExepJCzTwEmFDalIRbLEGtw0gfpESOpIAF/NnpPzcVCG86s0g2DuSyd41uhNGbEgaSrWEXORErbw$
    90	------=_Part_2192_32400445.1115745999735--$
    91	$
    92	--Apple-Mail-13-196941151--$
