[94mFrom:[39;49;00m[37m [39;49;00mSome[37m [39;49;00mOne[37m [39;49;00m<someone@example.com>[37m[39;49;00m
[94mMIME-Version:[39;49;00m[37m [39;49;00m1.0[37m[39;49;00m
[94mContent-Type:[39;49;00m[37m [39;49;00mmultipart[33m/[39;49;00mmixed;[37m[39;49;00m
[37m        [39;49;00m[36mboundary[39;49;00m=[33m"+Testboundary text"[39;49;00m[37m[39;49;00m
[37m[39;49;00m
This is a multipart message in MIME format.

[33m--+Testboundary text[39;49;00m
[94mContent-Type:[39;49;00m[37m [39;49;00mmultipart[33m/[39;49;00malternative;[37m[39;49;00m
[37m        [39;49;00m[36mboundary[39;49;00m=[33m"hello, boundary"[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[33m--hello, boundary[39;49;00m
[94mContent-Type:[39;49;00m[37m [39;49;00mtext[33m/[39;49;00mplain[37m[39;49;00m
[37m[39;49;00m
this is the body text

[33m--hello, boundary[39;49;00m
[94mContent-Type:[39;49;00m[37m [39;49;00mtext[33m/[39;49;00mhtml;[37m[39;49;00m
[37m       [39;49;00m[36mcharset[39;49;00m=[33m"utf-8"[39;49;00m[37m[39;49;00m
[94mContent-Transfer-Encoding:[39;49;00m[37m [39;49;00m[31mquoted-printable[39;49;00m[37m[39;49;00m
[37m[39;49;00m
<[94mfont[39;49;00m [36mcolor[39;49;00m=[33m3D"#FF0000"[39;49;00m>This is the body text</[94mfont[39;49;00m>

[33m--hello, boundary--[39;49;00m
[33m--+Testboundary text[39;49;00m
[94mContent-Type:[39;49;00m[37m [39;49;00mtext[33m/[39;49;00mplain;
[94mContent-Disposition:[39;49;00m[37m [39;49;00mattachment;[37m[39;49;00m
[37m [39;49;00m[37m       [39;49;00mfilename="[32mtest.txt[39;49;00m"[37m[39;49;00m
[94mContent-Transfer-Encoding:[39;49;00m[37m [39;49;00m[31mbase64[39;49;00m[37m[39;49;00m
[37m[39;49;00m
dGhpcyBpcyB0aGUgYXR0YWNobWVudCB0ZXh0

[33m--+Testboundary text--[39;49;00m
Some additional content here.
