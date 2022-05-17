     1	[94mFrom:[39;49;00m[37m [39;49;00mSome[37m [39;49;00mOne[37m [39;49;00m<someone@example.com>[37m[39;49;00m$
     2	[94mMIME-Version:[39;49;00m[37m [39;49;00m1.0[37m[39;49;00m$
     3	[94mContent-Type:[39;49;00m[37m [39;49;00mmultipart[33m/[39;49;00mmixed;[37m[39;49;00m$
     4	[37m        [39;49;00m[36mboundary[39;49;00m=[33m"+Testboundary text"[39;49;00m[37m[39;49;00m$
     5	[37m[39;49;00m$
     6	This is a multipart message in MIME format.$
     7	$
     8	[33m--+Testboundary text[39;49;00m$
     9	[94mContent-Type:[39;49;00m[37m [39;49;00mmultipart[33m/[39;49;00malternative;[37m[39;49;00m$
    10	[37m        [39;49;00m[36mboundary[39;49;00m=[33m"hello, boundary"[39;49;00m[37m[39;49;00m$
    11	[37m[39;49;00m$
    12	[33m--hello, boundary[39;49;00m$
    13	[94mContent-Type:[39;49;00m[37m [39;49;00mtext[33m/[39;49;00mplain[37m[39;49;00m$
    14	[37m[39;49;00m$
    15	this is the body text$
    16	$
    17	[33m--hello, boundary[39;49;00m$
    18	[94mContent-Type:[39;49;00m[37m [39;49;00mtext[33m/[39;49;00mhtml;[37m[39;49;00m$
    19	[37m       [39;49;00m[36mcharset[39;49;00m=[33m"utf-8"[39;49;00m[37m[39;49;00m$
    20	[94mContent-Transfer-Encoding:[39;49;00m[37m [39;49;00m[31mquoted-printable[39;49;00m[37m[39;49;00m$
    21	[37m[39;49;00m$
    22	<[94mfont[39;49;00m [36mcolor[39;49;00m=[33m3D"#FF0000"[39;49;00m>This is the body text</[94mfont[39;49;00m>$
    23	$
    24	[33m--hello, boundary--[39;49;00m$
    25	[33m--+Testboundary text[39;49;00m$
    26	[94mContent-Type:[39;49;00m[37m [39;49;00mtext[33m/[39;49;00mplain;$
    27	[94mContent-Disposition:[39;49;00m[37m [39;49;00mattachment;[37m[39;49;00m$
    28	[37m [39;49;00m[37m       [39;49;00mfilename="[32mtest.txt[39;49;00m"[37m[39;49;00m$
    29	[94mContent-Transfer-Encoding:[39;49;00m[37m [39;49;00m[31mbase64[39;49;00m[37m[39;49;00m$
    30	[37m[39;49;00m$
    31	dGhpcyBpcyB0aGUgYXR0YWNobWVudCB0ZXh0$
    32	$
    33	[33m--+Testboundary text--[39;49;00m$
    34	Some additional content here.$
