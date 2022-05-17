     1	[37m' Copyright (c) 2008 Silken Web - Free BSD License[39;49;00m[37m[39;49;00m$
     2	[37m' All rights reserved.[39;49;00m[37m[39;49;00m$
     3	[37m'[39;49;00m[37m[39;49;00m$
     4	[37m' Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:[39;49;00m[37m[39;49;00m$
     5	[37m' * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer[39;49;00m[37m[39;49;00m$
     6	[37m' * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.[39;49;00m[37m[39;49;00m$
     7	[37m' * Neither the name of Silken Web nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.[39;49;00m[37m[39;49;00m$
     8	[37m'[39;49;00m[37m[39;49;00m$
     9	[37m' THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,[39;49;00m[37m[39;49;00m$
    10	[37m' THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS[39;49;00m[37m[39;49;00m$
    11	[37m' BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE[39;49;00m[37m[39;49;00m$
    12	[37m' GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT[39;49;00m[37m[39;49;00m$
    13	[37m' LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH[39;49;00m[37m[39;49;00m$
    14	[37m' DAMAGE.[39;49;00m[37m[39;49;00m$
    15	[37m[39;49;00m$
    16	[34mImports[39;49;00m[37m [39;49;00m[04m[36mSystem[39;49;00m[04m[36m.[39;49;00m[04m[36mNet[39;49;00m[04m[36m.[39;49;00m[04m[36mMail[39;49;00m[37m[39;49;00m$
    17	[34mImports[39;49;00m[37m [39;49;00m[04m[36mSilkenWeb[39;49;00m[04m[36m.[39;49;00m[04m[36mEntities[39;49;00m[37m[39;49;00m$
    18	[34mImports[39;49;00m[37m [39;49;00m[04m[36mSystem[39;49;00m[04m[36m.[39;49;00m[04m[36mText[39;49;00m[04m[36m.[39;49;00m[04m[36mRegularExpressions[39;49;00m[37m[39;49;00m$
    19	[34mImports[39;49;00m[37m [39;49;00m[04m[36mSystem[39;49;00m[04m[36m.[39;49;00m[04m[36mReflection[39;49;00m[37m[39;49;00m$
    20	[34mImports[39;49;00m[37m [39;49;00m[04m[36mSilkenWeb[39;49;00m[04m[36m.[39;49;00m[04m[36mValidation[39;49;00m[37m[39;49;00m$
    21	[34mImports[39;49;00m[37m [39;49;00m[04m[36mSystem[39;49;00m[04m[36m.[39;49;00m[04m[36mGlobalization[39;49;00m[37m[39;49;00m$
    22	[34mImports[39;49;00m[37m [39;49;00m[04m[36mSilkenWeb[39;49;00m[04m[36m.[39;49;00m[04m[36mReflection[39;49;00m[37m[39;49;00m$
    23	[37m[39;49;00m$
    24	[34mNamespace[39;49;00m[37m [39;49;00m[04m[36mSilkenWeb[39;49;00m[37m[39;49;00m$
    25	[37m[39;49;00m$
    26	[37m    [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
    27	[37m    [39;49;00m[37m''' Represents an Email and what you can do with it.[39;49;00m[37m[39;49;00m$
    28	[37m    [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
    29	[37m    [39;49;00m[37m''' <remarks>[39;49;00m[37m[39;49;00m$
    30	[37m    [39;49;00m[37m''' Keith Jackson[39;49;00m[37m[39;49;00m$
    31	[37m    [39;49;00m[37m''' 11/04/2008[39;49;00m[37m[39;49;00m$
    32	[37m    [39;49;00m[37m'''[39;49;00m[37m[39;49;00m$
    33	[37m    [39;49;00m[37m''' This class is intended to be inherrited for providing all manner of system generated emails, each represented by it's own class.[39;49;00m[37m[39;49;00m$
    34	[37m    [39;49;00m[37m''' </remarks>[39;49;00m[37m[39;49;00m$
    35	[37m    [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mMustInherit[39;49;00m[37m [39;49;00m[34mClass[39;49;00m[37m [39;49;00m[04m[32mEmailBase[39;49;00m[37m [39;49;00m:[37m [39;49;00m[34mImplements[39;49;00m[37m [39;49;00mIValidatable,[37m [39;49;00mIDisposable[37m[39;49;00m$
    36	[37m[39;49;00m$
    37	[36m#Region " Constants "[39;49;00m$
    38	[37m[39;49;00m$
    39	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mConst[39;49;00m[37m [39;49;00mLenientRegexPattern[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
    40	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mConst[39;49;00m[37m [39;49;00mStrictRegexPattern[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m^(([^<>()[\]\\.,;:\s@\[39;49;00m[33m""[39;49;00m[33m]+(\.[^<>()[\]\\.,;:\s@\[39;49;00m[33m""[39;49;00m[33m]+)*)|(\[39;49;00m[33m""[39;49;00m[33m.+\[39;49;00m[33m""[39;49;00m[33m))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
    41	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mConst[39;49;00m[37m [39;49;00mInvalidEmailAddressError[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mThe Email address provided was invalid[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
    42	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mConst[39;49;00m[37m [39;49;00mInvalidEmailAddressErrorWithAddress[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mThe Email address, {0}, provided was invalid[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
    43	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mConst[39;49;00m[37m [39;49;00mNullEmailAddressError[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mThe Email address was not provided[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
    44	[37m[39;49;00m$
    45	[36m#End Region[39;49;00m[37m[39;49;00m$
    46	[37m[39;49;00m$
    47	[36m#Region " Fields "[39;49;00m$
    48	[37m[39;49;00m$
    49	[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00mdisposedValue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m[37m[39;49;00m$
    50	[37m[39;49;00m$
    51	[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m_message[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mMailMessage[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailMessage()[37m[39;49;00m$
    52	[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m_mailClient[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mSmtpClient[37m[39;49;00m$
    53	[37m[39;49;00m$
    54	[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m_useStrictValidation[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m[37m[39;49;00m$
    55	[37m[39;49;00m$
    56	[36m#End Region[39;49;00m[37m[39;49;00m$
    57	[37m[39;49;00m$
    58	[36m#Region " Construction "[39;49;00m$
    59	[37m[39;49;00m$
    60	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
    61	[37m        [39;49;00m[37m''' Instantiates a new Email of the derived type.[39;49;00m[37m[39;49;00m$
    62	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
    63	[37m        [39;49;00m[37m''' <param name="sender">The email address of the sender of the message.</param>[39;49;00m[37m[39;49;00m$
    64	[37m        [39;49;00m[37m''' <param name="recipients">The email addresses of the recipients of the message.</param>[39;49;00m[37m[39;49;00m$
    65	[37m        [39;49;00m[37m''' <param name="subject">The subject of the message.</param>[39;49;00m[37m[39;49;00m$
    66	[37m        [39;49;00m[37m''' <param name="body">The body of the message.</param>[39;49;00m[37m[39;49;00m$
    67	[37m        [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mNew[39;49;00m([34mByVal[39;49;00m[37m [39;49;00msender[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00msubject[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mbody[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00m[34mParamArray[39;49;00m[37m [39;49;00mrecipients[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m())[37m[39;49;00m$
    68	[37m            [39;49;00m_message.From[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(sender)[37m[39;49;00m$
    69	[37m            [39;49;00m[34mFor[39;49;00m[37m [39;49;00mi[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mInteger[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mTo[39;49;00m[37m [39;49;00mrecipients.Length[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
    70	[37m                [39;49;00m_message.To.Add(recipients(i))[37m[39;49;00m$
    71	[37m            [39;49;00m[34mNext[39;49;00m[37m[39;49;00m$
    72	[37m            [39;49;00m_message.Subject[37m [39;49;00m=[37m [39;49;00msubject[37m[39;49;00m$
    73	[37m            [39;49;00m_message.Body[37m [39;49;00m=[37m [39;49;00mbody[37m[39;49;00m$
    74	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
    75	[37m[39;49;00m$
    76	[36m#End Region[39;49;00m[37m[39;49;00m$
    77	[37m[39;49;00m$
    78	[36m#Region " Properties "[39;49;00m$
    79	[37m[39;49;00m$
    80	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
    81	[37m        [39;49;00m[37m''' Gets the Attachments for the message.[39;49;00m[37m[39;49;00m$
    82	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
    83	[37m        [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mReadOnly[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mAttachments[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mAttachmentCollection[37m[39;49;00m$
    84	[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
    85	[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.Attachments[37m[39;49;00m$
    86	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
    87	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
    88	[37m[39;49;00m$
    89	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
    90	[37m        [39;49;00m[37m''' The email addresses of the BCC recipients of the message.[39;49;00m[37m[39;49;00m$
    91	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
    92	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mBccRecipients[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m()[37m[39;49;00m$
    93	[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
    94	[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.Bcc.ToAddressStringArray()[37m[39;49;00m$
    95	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
    96	[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m())[37m[39;49;00m$
    97	[37m                [39;49;00m_message.Bcc.Clear()[37m[39;49;00m$
    98	[37m                [39;49;00m_message.Bcc.Add(value.ToDelimitedString())[37m[39;49;00m$
    99	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   100	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   101	[37m[39;49;00m$
   102	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   103	[37m        [39;49;00m[37m''' The body of the message.[39;49;00m[37m[39;49;00m$
   104	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   105	[37m        [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mBody[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m$
   106	[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   107	[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.Body[37m[39;49;00m$
   108	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   109	[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   110	[37m                [39;49;00m_message.Body[37m [39;49;00m=[37m [39;49;00mvalue[37m[39;49;00m$
   111	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   112	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   113	[37m[39;49;00m$
   114	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   115	[37m        [39;49;00m[37m''' The email addresses of the CC recipients of the message.[39;49;00m[37m[39;49;00m$
   116	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   117	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mCCRecipients[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m()[37m[39;49;00m$
   118	[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   119	[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.CC.ToAddressStringArray()[37m[39;49;00m$
   120	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   121	[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m())[37m[39;49;00m$
   122	[37m                [39;49;00m_message.CC.Clear()[37m[39;49;00m$
   123	[37m                [39;49;00m_message.CC.Add(value.ToDelimitedString())[37m[39;49;00m$
   124	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   125	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   126	[37m[39;49;00m$
   127	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   128	[37m        [39;49;00m[37m''' Gets or Sets a flag to indicate if the body of the message is HTML.[39;49;00m[37m[39;49;00m$
   129	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   130	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mIsBodyHtml[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m[37m[39;49;00m$
   131	[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   132	[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.IsBodyHtml[37m[39;49;00m$
   133	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   134	[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m)[37m[39;49;00m$
   135	[37m                [39;49;00m_message.IsBodyHtml[37m [39;49;00m=[37m [39;49;00mvalue[37m[39;49;00m$
   136	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   137	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   138	[37m[39;49;00m$
   139	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   140	[37m        [39;49;00m[37m''' Gets the Mail message wrapped by the EmailBase class.[39;49;00m[37m[39;49;00m$
   141	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   142	[37m        [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mReadOnly[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mMessage[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mMailMessage[37m[39;49;00m$
   143	[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   144	[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message[37m[39;49;00m$
   145	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   146	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   147	[37m[39;49;00m$
   148	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   149	[37m        [39;49;00m[37m''' Gets or Sets the Priority of the message.[39;49;00m[37m[39;49;00m$
   150	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   151	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mPriority[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mMailPriority[37m[39;49;00m$
   152	[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   153	[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.Priority[37m[39;49;00m$
   154	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   155	[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mMailPriority)[37m[39;49;00m$
   156	[37m                [39;49;00m_message.Priority[37m [39;49;00m=[37m [39;49;00mvalue[37m[39;49;00m$
   157	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   158	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   159	[37m[39;49;00m$
   160	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   161	[37m        [39;49;00m[37m''' The email addresses of the recipients of the message.[39;49;00m[37m[39;49;00m$
   162	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   163	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mRecipients[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m()[37m[39;49;00m$
   164	[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   165	[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.To.ToAddressStringArray()[37m[39;49;00m$
   166	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   167	[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m())[37m[39;49;00m$
   168	[37m                [39;49;00m_message.To.Clear()[37m[39;49;00m$
   169	[37m                [39;49;00m_message.To.Add(value.ToDelimitedString())[37m[39;49;00m$
   170	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   171	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   172	[37m[39;49;00m$
   173	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   174	[37m        [39;49;00m[37m''' The reply email address of the sender of the message.[39;49;00m[37m[39;49;00m$
   175	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   176	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mReplyTo[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m$
   177	[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   178	[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00m_message.ReplyTo[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   179	[37m                    [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m[36mString[39;49;00m.Empty[37m[39;49;00m$
   180	[37m                [39;49;00m[34mElse[39;49;00m[37m[39;49;00m$
   181	[37m                    [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.ReplyTo.Address[37m[39;49;00m$
   182	[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   183	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   184	[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   185	[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00m_message.ReplyTo[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   186	[37m                    [39;49;00m_message.ReplyTo[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(value)[37m[39;49;00m$
   187	[37m                [39;49;00m[34mElse[39;49;00m[37m[39;49;00m$
   188	[37m                    [39;49;00m_message.ReplyTo[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(value,[37m [39;49;00m_message.ReplyTo.DisplayName)[37m[39;49;00m$
   189	[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   190	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   191	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   192	[37m[39;49;00m$
   193	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   194	[37m        [39;49;00m[37m''' The reply display name of the sender of the message.[39;49;00m[37m[39;49;00m$
   195	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   196	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mReplyToDisplayName[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m$
   197	[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   198	[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00m_message.ReplyTo[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   199	[37m                    [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m[36mString[39;49;00m.Empty[37m[39;49;00m$
   200	[37m                [39;49;00m[34mElse[39;49;00m[37m[39;49;00m$
   201	[37m                    [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.ReplyTo.DisplayName[37m[39;49;00m$
   202	[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   203	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   204	[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   205	[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00m_message.ReplyTo[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   206	[37m                    [39;49;00m_message.ReplyTo[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(_message.From.Address,[37m [39;49;00mvalue)[37m[39;49;00m$
   207	[37m                [39;49;00m[34mElse[39;49;00m[37m[39;49;00m$
   208	[37m                    [39;49;00m_message.ReplyTo[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(_message.ReplyTo.Address,[37m [39;49;00mvalue)[37m[39;49;00m$
   209	[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   210	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   211	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   212	[37m[39;49;00m$
   213	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   214	[37m        [39;49;00m[37m''' The email address of the sender of the message.[39;49;00m[37m[39;49;00m$
   215	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   216	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mSender[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m$
   217	[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   218	[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.From.Address[37m[39;49;00m$
   219	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   220	[37m            [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   221	[37m                [39;49;00m_message.From[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(value,[37m [39;49;00m_message.From.DisplayName)[37m[39;49;00m$
   222	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   223	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   224	[37m[39;49;00m$
   225	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   226	[37m        [39;49;00m[37m''' The display name of the sender of the message.[39;49;00m[37m[39;49;00m$
   227	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   228	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mSenderDisplayName[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m$
   229	[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   230	[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.From.DisplayName[37m[39;49;00m$
   231	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   232	[37m            [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   233	[37m                [39;49;00m_message.From[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(_message.From.Address,[37m [39;49;00mvalue)[37m[39;49;00m$
   234	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   235	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   236	[37m[39;49;00m$
   237	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   238	[37m        [39;49;00m[37m''' The subject of the message.[39;49;00m[37m[39;49;00m$
   239	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   240	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mSubject[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m$
   241	[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   242	[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.Subject[37m[39;49;00m$
   243	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   244	[37m            [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   245	[37m                [39;49;00m_message.Subject[37m [39;49;00m=[37m [39;49;00mvalue[37m[39;49;00m$
   246	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   247	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   248	[37m[39;49;00m$
   249	[36m#End Region[39;49;00m[37m[39;49;00m$
   250	[37m[39;49;00m$
   251	[36m#Region " Methods "[39;49;00m$
   252	[37m[39;49;00m$
   253	[36m#Region " Send Methods "[39;49;00m$
   254	[37m[39;49;00m$
   255	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   256	[37m        [39;49;00m[37m''' Sends this email[39;49;00m[37m[39;49;00m$
   257	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   258	[37m        [39;49;00m[37m''' <param name="mailServer">The SMTP server to use to send the email.</param>[39;49;00m[37m[39;49;00m$
   259	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mSend[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mmailServer[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   260	[37m            [39;49;00m_mailClient[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mSmtpClient(mailServer)[37m[39;49;00m$
   261	[37m            [39;49;00m_mailClient.Send(_message)[37m[39;49;00m$
   262	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   263	[37m[39;49;00m$
   264	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   265	[37m        [39;49;00m[37m''' Sends this email asynchronously.[39;49;00m[37m[39;49;00m$
   266	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   267	[37m        [39;49;00m[37m''' <param name="mailServer">The SMTP server to use to send the email.</param>[39;49;00m[37m[39;49;00m$
   268	[37m        [39;49;00m[37m''' <param name="userToken">A user defined token passed to the recieving method on completion of the asynchronous task.</param>[39;49;00m[37m[39;49;00m$
   269	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mSendAsync[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mmailServer[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00muserToken[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mObject[39;49;00m)[37m[39;49;00m$
   270	[37m            [39;49;00m_mailClient[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mSmtpClient(mailServer)[37m[39;49;00m$
   271	[37m            [39;49;00m_mailClient.SendAsync(_message,[37m [39;49;00muserToken)[37m[39;49;00m$
   272	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   273	[37m[39;49;00m$
   274	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   275	[37m        [39;49;00m[37m''' Cancels an attempt to send this email asynchronously.[39;49;00m[37m[39;49;00m$
   276	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   277	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mSendAsyncCancel[39;49;00m()[37m[39;49;00m$
   278	[37m            [39;49;00m_mailClient.SendAsyncCancel()[37m[39;49;00m$
   279	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   280	[37m[39;49;00m$
   281	[36m#End Region[39;49;00m[37m[39;49;00m$
   282	[37m[39;49;00m$
   283	[36m#End Region[39;49;00m[37m[39;49;00m$
   284	[37m[39;49;00m$
   285	[36m#Region " IValidatable Implementation "[39;49;00m$
   286	[37m[39;49;00m$
   287	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   288	[37m        [39;49;00m[37m''' gets and Sets a flag to indicate whether to use strict validation.[39;49;00m[37m[39;49;00m$
   289	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   290	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mUseStrictValidation[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m[37m[39;49;00m$
   291	[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   292	[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_useStrictValidation[37m[39;49;00m$
   293	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   294	[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m)[37m[39;49;00m$
   295	[37m                [39;49;00m_useStrictValidation[37m [39;49;00m=[37m [39;49;00mvalue[37m[39;49;00m$
   296	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   297	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   298	[37m[39;49;00m$
   299	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   300	[37m        [39;49;00m[37m''' Validates this email.[39;49;00m[37m[39;49;00m$
   301	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   302	[37m        [39;49;00m[37m''' <returns>A ValidationResponse, containing a flag to indicate if validation was passed and a collection of Property Names and validation errors.</returns>[39;49;00m[37m[39;49;00m$
   303	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mFunction[39;49;00m[37m [39;49;00m[32mValidate[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mValidationResponse[37m [39;49;00m[34mImplements[39;49;00m[37m [39;49;00mIValidatable.Validate[37m[39;49;00m$
   304	[37m[39;49;00m$
   305	[37m            [39;49;00m[34mDim[39;49;00m[37m [39;49;00mretVal[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mValidationResponse()[37m[39;49;00m$
   306	[37m            [39;49;00m[34mDim[39;49;00m[37m [39;49;00mmailRegEx[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34mIf[39;49;00m(_useStrictValidation,[37m [39;49;00mStrictRegexPattern,[37m [39;49;00mLenientRegexPattern)[37m[39;49;00m$
   307	[37m[39;49;00m$
   308	[37m            [39;49;00mValidateAddress([33m"[39;49;00m[33mSender[39;49;00m[33m"[39;49;00m,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx,[37m [39;49;00m[34mTrue[39;49;00m)[37m[39;49;00m$
   309	[37m            [39;49;00mValidateAddresses([33m"[39;49;00m[33mRecipients[39;49;00m[33m"[39;49;00m,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx,[37m [39;49;00m[34mTrue[39;49;00m)[37m[39;49;00m$
   310	[37m            [39;49;00mValidateAddresses([33m"[39;49;00m[33mCcRecipients[39;49;00m[33m"[39;49;00m,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx)[37m[39;49;00m$
   311	[37m            [39;49;00mValidateAddresses([33m"[39;49;00m[33mBccRecipients[39;49;00m[33m"[39;49;00m,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx)[37m[39;49;00m$
   312	[37m            [39;49;00mValidateAddress([33m"[39;49;00m[33mReplyTo[39;49;00m[33m"[39;49;00m,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx)[37m[39;49;00m$
   313	[37m[39;49;00m$
   314	[37m            [39;49;00m[34mReturn[39;49;00m[37m [39;49;00mretVal[37m[39;49;00m$
   315	[37m[39;49;00m$
   316	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mFunction[39;49;00m[37m[39;49;00m$
   317	[37m[39;49;00m$
   318	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   319	[37m        [39;49;00m[37m''' Validates a single Email Address property.[39;49;00m[37m[39;49;00m$
   320	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   321	[37m        [39;49;00m[37m''' <param name="propertyName">The name of the property to validate.</param>[39;49;00m[37m[39;49;00m$
   322	[37m        [39;49;00m[37m''' <param name="retVal">The validation response object.</param>[39;49;00m[37m[39;49;00m$
   323	[37m        [39;49;00m[37m''' <param name="mailRegEx">The regular expression pattern to use for validation.</param>[39;49;00m[37m[39;49;00m$
   324	[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m[34mOverloads[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mValidateAddress[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mpropertyName[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByRef[39;49;00m[37m [39;49;00mretVal[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mValidationResponse,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mmailRegEx[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   325	[37m            [39;49;00mValidateAddress(propertyName,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx,[37m [39;49;00m[34mFalse[39;49;00m)[37m[39;49;00m$
   326	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   327	[37m[39;49;00m$
   328	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   329	[37m        [39;49;00m[37m''' Validates a single Email Address property.[39;49;00m[37m[39;49;00m$
   330	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   331	[37m        [39;49;00m[37m''' <param name="propertyName">The name of the property to validate.</param>[39;49;00m[37m[39;49;00m$
   332	[37m        [39;49;00m[37m''' <param name="retVal">The validation response object.</param>[39;49;00m[37m[39;49;00m$
   333	[37m        [39;49;00m[37m''' <param name="mailRegEx">The regular expression pattern to use for validation.</param>[39;49;00m[37m[39;49;00m$
   334	[37m        [39;49;00m[37m''' <param name="required">Indicates if the address is required; False if not specified.</param>[39;49;00m[37m[39;49;00m$
   335	[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m[34mOverloads[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mValidateAddress[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mpropertyName[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByRef[39;49;00m[37m [39;49;00mretVal[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mValidationResponse,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mmailRegEx[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mrequired[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m)[37m[39;49;00m$
   336	[37m[39;49;00m$
   337	[37m            [39;49;00m[34mDim[39;49;00m[37m [39;49;00memailAddress[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00mReflectionHelper.Properties.GetProperty([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m)([34mMe[39;49;00m,[37m [39;49;00mpropertyName)[37m[39;49;00m$
   338	[37m[39;49;00m$
   339	[37m            [39;49;00m[34mIf[39;49;00m[37m [39;49;00memailAddress[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[35mOrElse[39;49;00m[37m [39;49;00memailAddress.Length[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   340	[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00mrequired[37m [39;49;00m[34mThen[39;49;00m[37m [39;49;00mretVal.Add([34mNew[39;49;00m[37m [39;49;00mKeyValuePair([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[36mString[39;49;00m)(propertyName,[37m [39;49;00mNullEmailAddressError))[37m[39;49;00m$
   341	[37m            [39;49;00m[34mElse[39;49;00m[37m[39;49;00m$
   342	[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00m([34mNot[39;49;00m[37m [39;49;00mRegex.IsMatch(emailAddress,[37m [39;49;00mmailRegEx))[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   343	[37m                    [39;49;00mretVal.Add([34mNew[39;49;00m[37m [39;49;00mKeyValuePair([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[36mString[39;49;00m)(propertyName,[37m [39;49;00mInvalidEmailAddressError))[37m[39;49;00m$
   344	[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   345	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   346	[37m[39;49;00m$
   347	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   348	[37m[39;49;00m$
   349	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   350	[37m        [39;49;00m[37m''' Validates a string array of Email Address property.[39;49;00m[37m[39;49;00m$
   351	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   352	[37m        [39;49;00m[37m''' <param name="propertyName">The name of the property to validate.</param>[39;49;00m[37m[39;49;00m$
   353	[37m        [39;49;00m[37m''' <param name="retVal">The validation response object.</param>[39;49;00m[37m[39;49;00m$
   354	[37m        [39;49;00m[37m''' <param name="mailRegEx">The regular expression pattern to use for validation.</param>[39;49;00m[37m[39;49;00m$
   355	[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m[34mOverloads[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mValidateAddresses[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mpropertyName[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByRef[39;49;00m[37m [39;49;00mretVal[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mValidationResponse,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mmailRegEx[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   356	[37m            [39;49;00mValidateAddresses(propertyName,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx,[37m [39;49;00m[34mFalse[39;49;00m)[37m[39;49;00m$
   357	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   358	[37m[39;49;00m$
   359	[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   360	[37m        [39;49;00m[37m''' Validates a string array of Email Address property.[39;49;00m[37m[39;49;00m$
   361	[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   362	[37m        [39;49;00m[37m''' <param name="propertyName">The name of the property to validate.</param>[39;49;00m[37m[39;49;00m$
   363	[37m        [39;49;00m[37m''' <param name="retVal">The validation response object.</param>[39;49;00m[37m[39;49;00m$
   364	[37m        [39;49;00m[37m''' <param name="mailRegEx">The regular expression pattern to use for validation.</param>[39;49;00m[37m[39;49;00m$
   365	[37m        [39;49;00m[37m''' <param name="required">Indicates if the address is required; False if not specified.</param>[39;49;00m[37m[39;49;00m$
   366	[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m[34mOverloads[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mValidateAddresses[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mpropertyName[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByRef[39;49;00m[37m [39;49;00mretVal[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mValidationResponse,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mmailRegEx[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mrequired[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m)[37m[39;49;00m$
   367	[37m[39;49;00m$
   368	[37m            [39;49;00m[34mDim[39;49;00m[37m [39;49;00memailAddresses()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00mReflectionHelper.Properties.GetProperty([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m())([34mMe[39;49;00m,[37m [39;49;00mpropertyName)[37m[39;49;00m$
   369	[37m[39;49;00m$
   370	[37m            [39;49;00m[34mIf[39;49;00m[37m [39;49;00memailAddresses[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[35mOrElse[39;49;00m[37m [39;49;00memailAddresses.Length[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   371	[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00mrequired[37m [39;49;00m[34mThen[39;49;00m[37m [39;49;00mretVal.Add([34mNew[39;49;00m[37m [39;49;00mKeyValuePair([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[36mString[39;49;00m)(propertyName,[37m [39;49;00m[36mString[39;49;00m.Format(CultureInfo.CurrentCulture,[37m [39;49;00mNullEmailAddressError)))[37m[39;49;00m$
   372	[37m            [39;49;00m[34mElse[39;49;00m[37m[39;49;00m$
   373	[37m                [39;49;00m[34mFor[39;49;00m[37m [39;49;00mi[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mInteger[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mTo[39;49;00m[37m [39;49;00memailAddresses.Length[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
   374	[37m                    [39;49;00m[34mIf[39;49;00m[37m [39;49;00m([34mNot[39;49;00m[37m [39;49;00mRegex.IsMatch(emailAddresses(i),[37m [39;49;00mmailRegEx))[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   375	[37m                        [39;49;00mretVal.Add([34mNew[39;49;00m[37m [39;49;00mKeyValuePair([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[36mString[39;49;00m)(propertyName,[37m [39;49;00m[36mString[39;49;00m.Format(CultureInfo.CurrentCulture,[37m [39;49;00mInvalidEmailAddressErrorWithAddress,[37m [39;49;00memailAddresses(i))))[37m[39;49;00m$
   376	[37m                    [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   377	[37m                [39;49;00m[34mNext[39;49;00m[37m[39;49;00m$
   378	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   379	[37m[39;49;00m$
   380	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   381	[37m[39;49;00m$
   382	[36m#End Region[39;49;00m[37m[39;49;00m$
   383	[37m[39;49;00m$
   384	[36m#Region " IDisposable Implementation "[39;49;00m$
   385	[37m[39;49;00m$
   386	[37m        [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mDispose[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mdisposing[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m)[37m[39;49;00m$
   387	[37m            [39;49;00m[34mIf[39;49;00m[37m [39;49;00m[34mNot[39;49;00m[37m [39;49;00m[34mMe[39;49;00m.disposedValue[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   388	[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00mdisposing[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   389	[37m                    [39;49;00m_message.Dispose()[37m[39;49;00m$
   390	[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   391	[37m                [39;49;00m_mailClient[37m [39;49;00m=[37m [39;49;00m[34mNothing[39;49;00m[37m[39;49;00m$
   392	[37m                [39;49;00m_message[37m [39;49;00m=[37m [39;49;00m[34mNothing[39;49;00m[37m[39;49;00m$
   393	[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   394	[37m            [39;49;00m[34mMe[39;49;00m.disposedValue[37m [39;49;00m=[37m [39;49;00m[34mTrue[39;49;00m[37m[39;49;00m$
   395	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   396	[37m[39;49;00m$
   397	[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mDispose[39;49;00m()[37m [39;49;00m[34mImplements[39;49;00m[37m [39;49;00mIDisposable.Dispose[37m[39;49;00m$
   398	[37m            [39;49;00m[37m' Do not change this code.  Put cleanup code in Dispose(ByVal disposing As Boolean) above.[39;49;00m[37m[39;49;00m$
   399	[37m            [39;49;00mDispose([34mTrue[39;49;00m)[37m[39;49;00m$
   400	[37m            [39;49;00mGC.SuppressFinalize([34mMe[39;49;00m)[37m[39;49;00m$
   401	[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   402	[37m[39;49;00m$
   403	[36m#End Region[39;49;00m[37m[39;49;00m$
   404	[37m[39;49;00m$
   405	[37m    [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mClass[39;49;00m[37m[39;49;00m$
   406	[37m[39;49;00m$
   407	[34mEnd[39;49;00m[37m [39;49;00m[34mNamespace[39;49;00m$
