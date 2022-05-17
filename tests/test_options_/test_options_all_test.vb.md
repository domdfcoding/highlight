     1^I[37m' Copyright (c) 2008 Silken Web - Free BSD License[39;49;00m[37m[39;49;00m$
     2^I[37m' All rights reserved.[39;49;00m[37m[39;49;00m$
     3^I[37m'[39;49;00m[37m[39;49;00m$
     4^I[37m' Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:[39;49;00m[37m[39;49;00m$
     5^I[37m' * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer[39;49;00m[37m[39;49;00m$
     6^I[37m' * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.[39;49;00m[37m[39;49;00m$
     7^I[37m' * Neither the name of Silken Web nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.[39;49;00m[37m[39;49;00m$
     8^I[37m'[39;49;00m[37m[39;49;00m$
     9^I[37m' THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,[39;49;00m[37m[39;49;00m$
    10^I[37m' THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS[39;49;00m[37m[39;49;00m$
    11^I[37m' BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE[39;49;00m[37m[39;49;00m$
    12^I[37m' GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT[39;49;00m[37m[39;49;00m$
    13^I[37m' LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH[39;49;00m[37m[39;49;00m$
    14^I[37m' DAMAGE.[39;49;00m[37m[39;49;00m$
    15^I[37m[39;49;00m$
    16^I[34mImports[39;49;00m[37m [39;49;00m[04m[36mSystem[39;49;00m[04m[36m.[39;49;00m[04m[36mNet[39;49;00m[04m[36m.[39;49;00m[04m[36mMail[39;49;00m[37m[39;49;00m$
    17^I[34mImports[39;49;00m[37m [39;49;00m[04m[36mSilkenWeb[39;49;00m[04m[36m.[39;49;00m[04m[36mEntities[39;49;00m[37m[39;49;00m$
    18^I[34mImports[39;49;00m[37m [39;49;00m[04m[36mSystem[39;49;00m[04m[36m.[39;49;00m[04m[36mText[39;49;00m[04m[36m.[39;49;00m[04m[36mRegularExpressions[39;49;00m[37m[39;49;00m$
    19^I[34mImports[39;49;00m[37m [39;49;00m[04m[36mSystem[39;49;00m[04m[36m.[39;49;00m[04m[36mReflection[39;49;00m[37m[39;49;00m$
    20^I[34mImports[39;49;00m[37m [39;49;00m[04m[36mSilkenWeb[39;49;00m[04m[36m.[39;49;00m[04m[36mValidation[39;49;00m[37m[39;49;00m$
    21^I[34mImports[39;49;00m[37m [39;49;00m[04m[36mSystem[39;49;00m[04m[36m.[39;49;00m[04m[36mGlobalization[39;49;00m[37m[39;49;00m$
    22^I[34mImports[39;49;00m[37m [39;49;00m[04m[36mSilkenWeb[39;49;00m[04m[36m.[39;49;00m[04m[36mReflection[39;49;00m[37m[39;49;00m$
    23^I[37m[39;49;00m$
    24^I[34mNamespace[39;49;00m[37m [39;49;00m[04m[36mSilkenWeb[39;49;00m[37m[39;49;00m$
    25^I[37m[39;49;00m$
    26^I[37m    [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
    27^I[37m    [39;49;00m[37m''' Represents an Email and what you can do with it.[39;49;00m[37m[39;49;00m$
    28^I[37m    [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
    29^I[37m    [39;49;00m[37m''' <remarks>[39;49;00m[37m[39;49;00m$
    30^I[37m    [39;49;00m[37m''' Keith Jackson[39;49;00m[37m[39;49;00m$
    31^I[37m    [39;49;00m[37m''' 11/04/2008[39;49;00m[37m[39;49;00m$
    32^I[37m    [39;49;00m[37m'''[39;49;00m[37m[39;49;00m$
    33^I[37m    [39;49;00m[37m''' This class is intended to be inherrited for providing all manner of system generated emails, each represented by it's own class.[39;49;00m[37m[39;49;00m$
    34^I[37m    [39;49;00m[37m''' </remarks>[39;49;00m[37m[39;49;00m$
    35^I[37m    [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mMustInherit[39;49;00m[37m [39;49;00m[34mClass[39;49;00m[37m [39;49;00m[04m[32mEmailBase[39;49;00m[37m [39;49;00m:[37m [39;49;00m[34mImplements[39;49;00m[37m [39;49;00mIValidatable,[37m [39;49;00mIDisposable[37m[39;49;00m$
    36^I[37m[39;49;00m$
    37^I[36m#Region " Constants "[39;49;00m$
    38^I[37m[39;49;00m$
    39^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mConst[39;49;00m[37m [39;49;00mLenientRegexPattern[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
    40^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mConst[39;49;00m[37m [39;49;00mStrictRegexPattern[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m^(([^<>()[\]\\.,;:\s@\[39;49;00m[33m""[39;49;00m[33m]+(\.[^<>()[\]\\.,;:\s@\[39;49;00m[33m""[39;49;00m[33m]+)*)|(\[39;49;00m[33m""[39;49;00m[33m.+\[39;49;00m[33m""[39;49;00m[33m))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
    41^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mConst[39;49;00m[37m [39;49;00mInvalidEmailAddressError[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mThe Email address provided was invalid[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
    42^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mConst[39;49;00m[37m [39;49;00mInvalidEmailAddressErrorWithAddress[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mThe Email address, {0}, provided was invalid[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
    43^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mConst[39;49;00m[37m [39;49;00mNullEmailAddressError[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mThe Email address was not provided[39;49;00m[33m"[39;49;00m[37m[39;49;00m$
    44^I[37m[39;49;00m$
    45^I[36m#End Region[39;49;00m[37m[39;49;00m$
    46^I[37m[39;49;00m$
    47^I[36m#Region " Fields "[39;49;00m$
    48^I[37m[39;49;00m$
    49^I[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00mdisposedValue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m[37m[39;49;00m$
    50^I[37m[39;49;00m$
    51^I[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m_message[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mMailMessage[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailMessage()[37m[39;49;00m$
    52^I[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m_mailClient[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mSmtpClient[37m[39;49;00m$
    53^I[37m[39;49;00m$
    54^I[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m_useStrictValidation[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m[37m[39;49;00m$
    55^I[37m[39;49;00m$
    56^I[36m#End Region[39;49;00m[37m[39;49;00m$
    57^I[37m[39;49;00m$
    58^I[36m#Region " Construction "[39;49;00m$
    59^I[37m[39;49;00m$
    60^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
    61^I[37m        [39;49;00m[37m''' Instantiates a new Email of the derived type.[39;49;00m[37m[39;49;00m$
    62^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
    63^I[37m        [39;49;00m[37m''' <param name="sender">The email address of the sender of the message.</param>[39;49;00m[37m[39;49;00m$
    64^I[37m        [39;49;00m[37m''' <param name="recipients">The email addresses of the recipients of the message.</param>[39;49;00m[37m[39;49;00m$
    65^I[37m        [39;49;00m[37m''' <param name="subject">The subject of the message.</param>[39;49;00m[37m[39;49;00m$
    66^I[37m        [39;49;00m[37m''' <param name="body">The body of the message.</param>[39;49;00m[37m[39;49;00m$
    67^I[37m        [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mNew[39;49;00m([34mByVal[39;49;00m[37m [39;49;00msender[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00msubject[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mbody[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00m[34mParamArray[39;49;00m[37m [39;49;00mrecipients[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m())[37m[39;49;00m$
    68^I[37m            [39;49;00m_message.From[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(sender)[37m[39;49;00m$
    69^I[37m            [39;49;00m[34mFor[39;49;00m[37m [39;49;00mi[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mInteger[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mTo[39;49;00m[37m [39;49;00mrecipients.Length[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
    70^I[37m                [39;49;00m_message.To.Add(recipients(i))[37m[39;49;00m$
    71^I[37m            [39;49;00m[34mNext[39;49;00m[37m[39;49;00m$
    72^I[37m            [39;49;00m_message.Subject[37m [39;49;00m=[37m [39;49;00msubject[37m[39;49;00m$
    73^I[37m            [39;49;00m_message.Body[37m [39;49;00m=[37m [39;49;00mbody[37m[39;49;00m$
    74^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
    75^I[37m[39;49;00m$
    76^I[36m#End Region[39;49;00m[37m[39;49;00m$
    77^I[37m[39;49;00m$
    78^I[36m#Region " Properties "[39;49;00m$
    79^I[37m[39;49;00m$
    80^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
    81^I[37m        [39;49;00m[37m''' Gets the Attachments for the message.[39;49;00m[37m[39;49;00m$
    82^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
    83^I[37m        [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mReadOnly[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mAttachments[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mAttachmentCollection[37m[39;49;00m$
    84^I[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
    85^I[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.Attachments[37m[39;49;00m$
    86^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
    87^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
    88^I[37m[39;49;00m$
    89^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
    90^I[37m        [39;49;00m[37m''' The email addresses of the BCC recipients of the message.[39;49;00m[37m[39;49;00m$
    91^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
    92^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mBccRecipients[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m()[37m[39;49;00m$
    93^I[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
    94^I[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.Bcc.ToAddressStringArray()[37m[39;49;00m$
    95^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
    96^I[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m())[37m[39;49;00m$
    97^I[37m                [39;49;00m_message.Bcc.Clear()[37m[39;49;00m$
    98^I[37m                [39;49;00m_message.Bcc.Add(value.ToDelimitedString())[37m[39;49;00m$
    99^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   100^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   101^I[37m[39;49;00m$
   102^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   103^I[37m        [39;49;00m[37m''' The body of the message.[39;49;00m[37m[39;49;00m$
   104^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   105^I[37m        [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mBody[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m$
   106^I[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   107^I[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.Body[37m[39;49;00m$
   108^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   109^I[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   110^I[37m                [39;49;00m_message.Body[37m [39;49;00m=[37m [39;49;00mvalue[37m[39;49;00m$
   111^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   112^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   113^I[37m[39;49;00m$
   114^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   115^I[37m        [39;49;00m[37m''' The email addresses of the CC recipients of the message.[39;49;00m[37m[39;49;00m$
   116^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   117^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mCCRecipients[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m()[37m[39;49;00m$
   118^I[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   119^I[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.CC.ToAddressStringArray()[37m[39;49;00m$
   120^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   121^I[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m())[37m[39;49;00m$
   122^I[37m                [39;49;00m_message.CC.Clear()[37m[39;49;00m$
   123^I[37m                [39;49;00m_message.CC.Add(value.ToDelimitedString())[37m[39;49;00m$
   124^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   125^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   126^I[37m[39;49;00m$
   127^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   128^I[37m        [39;49;00m[37m''' Gets or Sets a flag to indicate if the body of the message is HTML.[39;49;00m[37m[39;49;00m$
   129^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   130^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mIsBodyHtml[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m[37m[39;49;00m$
   131^I[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   132^I[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.IsBodyHtml[37m[39;49;00m$
   133^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   134^I[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m)[37m[39;49;00m$
   135^I[37m                [39;49;00m_message.IsBodyHtml[37m [39;49;00m=[37m [39;49;00mvalue[37m[39;49;00m$
   136^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   137^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   138^I[37m[39;49;00m$
   139^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   140^I[37m        [39;49;00m[37m''' Gets the Mail message wrapped by the EmailBase class.[39;49;00m[37m[39;49;00m$
   141^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   142^I[37m        [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mReadOnly[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mMessage[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mMailMessage[37m[39;49;00m$
   143^I[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   144^I[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message[37m[39;49;00m$
   145^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   146^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   147^I[37m[39;49;00m$
   148^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   149^I[37m        [39;49;00m[37m''' Gets or Sets the Priority of the message.[39;49;00m[37m[39;49;00m$
   150^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   151^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mPriority[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mMailPriority[37m[39;49;00m$
   152^I[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   153^I[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.Priority[37m[39;49;00m$
   154^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   155^I[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mMailPriority)[37m[39;49;00m$
   156^I[37m                [39;49;00m_message.Priority[37m [39;49;00m=[37m [39;49;00mvalue[37m[39;49;00m$
   157^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   158^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   159^I[37m[39;49;00m$
   160^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   161^I[37m        [39;49;00m[37m''' The email addresses of the recipients of the message.[39;49;00m[37m[39;49;00m$
   162^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   163^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mRecipients[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m()[37m[39;49;00m$
   164^I[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   165^I[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.To.ToAddressStringArray()[37m[39;49;00m$
   166^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   167^I[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m())[37m[39;49;00m$
   168^I[37m                [39;49;00m_message.To.Clear()[37m[39;49;00m$
   169^I[37m                [39;49;00m_message.To.Add(value.ToDelimitedString())[37m[39;49;00m$
   170^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   171^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   172^I[37m[39;49;00m$
   173^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   174^I[37m        [39;49;00m[37m''' The reply email address of the sender of the message.[39;49;00m[37m[39;49;00m$
   175^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   176^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mReplyTo[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m$
   177^I[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   178^I[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00m_message.ReplyTo[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   179^I[37m                    [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m[36mString[39;49;00m.Empty[37m[39;49;00m$
   180^I[37m                [39;49;00m[34mElse[39;49;00m[37m[39;49;00m$
   181^I[37m                    [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.ReplyTo.Address[37m[39;49;00m$
   182^I[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   183^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   184^I[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   185^I[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00m_message.ReplyTo[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   186^I[37m                    [39;49;00m_message.ReplyTo[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(value)[37m[39;49;00m$
   187^I[37m                [39;49;00m[34mElse[39;49;00m[37m[39;49;00m$
   188^I[37m                    [39;49;00m_message.ReplyTo[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(value,[37m [39;49;00m_message.ReplyTo.DisplayName)[37m[39;49;00m$
   189^I[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   190^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   191^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   192^I[37m[39;49;00m$
   193^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   194^I[37m        [39;49;00m[37m''' The reply display name of the sender of the message.[39;49;00m[37m[39;49;00m$
   195^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   196^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mReplyToDisplayName[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m$
   197^I[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   198^I[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00m_message.ReplyTo[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   199^I[37m                    [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m[36mString[39;49;00m.Empty[37m[39;49;00m$
   200^I[37m                [39;49;00m[34mElse[39;49;00m[37m[39;49;00m$
   201^I[37m                    [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.ReplyTo.DisplayName[37m[39;49;00m$
   202^I[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   203^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   204^I[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   205^I[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00m_message.ReplyTo[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   206^I[37m                    [39;49;00m_message.ReplyTo[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(_message.From.Address,[37m [39;49;00mvalue)[37m[39;49;00m$
   207^I[37m                [39;49;00m[34mElse[39;49;00m[37m[39;49;00m$
   208^I[37m                    [39;49;00m_message.ReplyTo[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(_message.ReplyTo.Address,[37m [39;49;00mvalue)[37m[39;49;00m$
   209^I[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   210^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   211^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   212^I[37m[39;49;00m$
   213^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   214^I[37m        [39;49;00m[37m''' The email address of the sender of the message.[39;49;00m[37m[39;49;00m$
   215^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   216^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mSender[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m$
   217^I[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   218^I[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.From.Address[37m[39;49;00m$
   219^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   220^I[37m            [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   221^I[37m                [39;49;00m_message.From[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(value,[37m [39;49;00m_message.From.DisplayName)[37m[39;49;00m$
   222^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   223^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   224^I[37m[39;49;00m$
   225^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   226^I[37m        [39;49;00m[37m''' The display name of the sender of the message.[39;49;00m[37m[39;49;00m$
   227^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   228^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mSenderDisplayName[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m$
   229^I[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   230^I[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.From.DisplayName[37m[39;49;00m$
   231^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   232^I[37m            [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   233^I[37m                [39;49;00m_message.From[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(_message.From.Address,[37m [39;49;00mvalue)[37m[39;49;00m$
   234^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   235^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   236^I[37m[39;49;00m$
   237^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   238^I[37m        [39;49;00m[37m''' The subject of the message.[39;49;00m[37m[39;49;00m$
   239^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   240^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mSubject[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m$
   241^I[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   242^I[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.Subject[37m[39;49;00m$
   243^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   244^I[37m            [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   245^I[37m                [39;49;00m_message.Subject[37m [39;49;00m=[37m [39;49;00mvalue[37m[39;49;00m$
   246^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   247^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   248^I[37m[39;49;00m$
   249^I[36m#End Region[39;49;00m[37m[39;49;00m$
   250^I[37m[39;49;00m$
   251^I[36m#Region " Methods "[39;49;00m$
   252^I[37m[39;49;00m$
   253^I[36m#Region " Send Methods "[39;49;00m$
   254^I[37m[39;49;00m$
   255^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   256^I[37m        [39;49;00m[37m''' Sends this email[39;49;00m[37m[39;49;00m$
   257^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   258^I[37m        [39;49;00m[37m''' <param name="mailServer">The SMTP server to use to send the email.</param>[39;49;00m[37m[39;49;00m$
   259^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mSend[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mmailServer[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   260^I[37m            [39;49;00m_mailClient[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mSmtpClient(mailServer)[37m[39;49;00m$
   261^I[37m            [39;49;00m_mailClient.Send(_message)[37m[39;49;00m$
   262^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   263^I[37m[39;49;00m$
   264^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   265^I[37m        [39;49;00m[37m''' Sends this email asynchronously.[39;49;00m[37m[39;49;00m$
   266^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   267^I[37m        [39;49;00m[37m''' <param name="mailServer">The SMTP server to use to send the email.</param>[39;49;00m[37m[39;49;00m$
   268^I[37m        [39;49;00m[37m''' <param name="userToken">A user defined token passed to the recieving method on completion of the asynchronous task.</param>[39;49;00m[37m[39;49;00m$
   269^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mSendAsync[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mmailServer[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00muserToken[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mObject[39;49;00m)[37m[39;49;00m$
   270^I[37m            [39;49;00m_mailClient[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mSmtpClient(mailServer)[37m[39;49;00m$
   271^I[37m            [39;49;00m_mailClient.SendAsync(_message,[37m [39;49;00muserToken)[37m[39;49;00m$
   272^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   273^I[37m[39;49;00m$
   274^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   275^I[37m        [39;49;00m[37m''' Cancels an attempt to send this email asynchronously.[39;49;00m[37m[39;49;00m$
   276^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   277^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mSendAsyncCancel[39;49;00m()[37m[39;49;00m$
   278^I[37m            [39;49;00m_mailClient.SendAsyncCancel()[37m[39;49;00m$
   279^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   280^I[37m[39;49;00m$
   281^I[36m#End Region[39;49;00m[37m[39;49;00m$
   282^I[37m[39;49;00m$
   283^I[36m#End Region[39;49;00m[37m[39;49;00m$
   284^I[37m[39;49;00m$
   285^I[36m#Region " IValidatable Implementation "[39;49;00m$
   286^I[37m[39;49;00m$
   287^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   288^I[37m        [39;49;00m[37m''' gets and Sets a flag to indicate whether to use strict validation.[39;49;00m[37m[39;49;00m$
   289^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   290^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mUseStrictValidation[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m[37m[39;49;00m$
   291^I[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   292^I[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_useStrictValidation[37m[39;49;00m$
   293^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m$
   294^I[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m)[37m[39;49;00m$
   295^I[37m                [39;49;00m_useStrictValidation[37m [39;49;00m=[37m [39;49;00mvalue[37m[39;49;00m$
   296^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m$
   297^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m$
   298^I[37m[39;49;00m$
   299^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   300^I[37m        [39;49;00m[37m''' Validates this email.[39;49;00m[37m[39;49;00m$
   301^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   302^I[37m        [39;49;00m[37m''' <returns>A ValidationResponse, containing a flag to indicate if validation was passed and a collection of Property Names and validation errors.</returns>[39;49;00m[37m[39;49;00m$
   303^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mFunction[39;49;00m[37m [39;49;00m[32mValidate[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mValidationResponse[37m [39;49;00m[34mImplements[39;49;00m[37m [39;49;00mIValidatable.Validate[37m[39;49;00m$
   304^I[37m[39;49;00m$
   305^I[37m            [39;49;00m[34mDim[39;49;00m[37m [39;49;00mretVal[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mValidationResponse()[37m[39;49;00m$
   306^I[37m            [39;49;00m[34mDim[39;49;00m[37m [39;49;00mmailRegEx[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34mIf[39;49;00m(_useStrictValidation,[37m [39;49;00mStrictRegexPattern,[37m [39;49;00mLenientRegexPattern)[37m[39;49;00m$
   307^I[37m[39;49;00m$
   308^I[37m            [39;49;00mValidateAddress([33m"[39;49;00m[33mSender[39;49;00m[33m"[39;49;00m,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx,[37m [39;49;00m[34mTrue[39;49;00m)[37m[39;49;00m$
   309^I[37m            [39;49;00mValidateAddresses([33m"[39;49;00m[33mRecipients[39;49;00m[33m"[39;49;00m,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx,[37m [39;49;00m[34mTrue[39;49;00m)[37m[39;49;00m$
   310^I[37m            [39;49;00mValidateAddresses([33m"[39;49;00m[33mCcRecipients[39;49;00m[33m"[39;49;00m,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx)[37m[39;49;00m$
   311^I[37m            [39;49;00mValidateAddresses([33m"[39;49;00m[33mBccRecipients[39;49;00m[33m"[39;49;00m,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx)[37m[39;49;00m$
   312^I[37m            [39;49;00mValidateAddress([33m"[39;49;00m[33mReplyTo[39;49;00m[33m"[39;49;00m,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx)[37m[39;49;00m$
   313^I[37m[39;49;00m$
   314^I[37m            [39;49;00m[34mReturn[39;49;00m[37m [39;49;00mretVal[37m[39;49;00m$
   315^I[37m[39;49;00m$
   316^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mFunction[39;49;00m[37m[39;49;00m$
   317^I[37m[39;49;00m$
   318^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   319^I[37m        [39;49;00m[37m''' Validates a single Email Address property.[39;49;00m[37m[39;49;00m$
   320^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   321^I[37m        [39;49;00m[37m''' <param name="propertyName">The name of the property to validate.</param>[39;49;00m[37m[39;49;00m$
   322^I[37m        [39;49;00m[37m''' <param name="retVal">The validation response object.</param>[39;49;00m[37m[39;49;00m$
   323^I[37m        [39;49;00m[37m''' <param name="mailRegEx">The regular expression pattern to use for validation.</param>[39;49;00m[37m[39;49;00m$
   324^I[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m[34mOverloads[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mValidateAddress[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mpropertyName[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByRef[39;49;00m[37m [39;49;00mretVal[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mValidationResponse,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mmailRegEx[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   325^I[37m            [39;49;00mValidateAddress(propertyName,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx,[37m [39;49;00m[34mFalse[39;49;00m)[37m[39;49;00m$
   326^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   327^I[37m[39;49;00m$
   328^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   329^I[37m        [39;49;00m[37m''' Validates a single Email Address property.[39;49;00m[37m[39;49;00m$
   330^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   331^I[37m        [39;49;00m[37m''' <param name="propertyName">The name of the property to validate.</param>[39;49;00m[37m[39;49;00m$
   332^I[37m        [39;49;00m[37m''' <param name="retVal">The validation response object.</param>[39;49;00m[37m[39;49;00m$
   333^I[37m        [39;49;00m[37m''' <param name="mailRegEx">The regular expression pattern to use for validation.</param>[39;49;00m[37m[39;49;00m$
   334^I[37m        [39;49;00m[37m''' <param name="required">Indicates if the address is required; False if not specified.</param>[39;49;00m[37m[39;49;00m$
   335^I[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m[34mOverloads[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mValidateAddress[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mpropertyName[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByRef[39;49;00m[37m [39;49;00mretVal[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mValidationResponse,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mmailRegEx[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mrequired[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m)[37m[39;49;00m$
   336^I[37m[39;49;00m$
   337^I[37m            [39;49;00m[34mDim[39;49;00m[37m [39;49;00memailAddress[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00mReflectionHelper.Properties.GetProperty([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m)([34mMe[39;49;00m,[37m [39;49;00mpropertyName)[37m[39;49;00m$
   338^I[37m[39;49;00m$
   339^I[37m            [39;49;00m[34mIf[39;49;00m[37m [39;49;00memailAddress[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[35mOrElse[39;49;00m[37m [39;49;00memailAddress.Length[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   340^I[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00mrequired[37m [39;49;00m[34mThen[39;49;00m[37m [39;49;00mretVal.Add([34mNew[39;49;00m[37m [39;49;00mKeyValuePair([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[36mString[39;49;00m)(propertyName,[37m [39;49;00mNullEmailAddressError))[37m[39;49;00m$
   341^I[37m            [39;49;00m[34mElse[39;49;00m[37m[39;49;00m$
   342^I[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00m([34mNot[39;49;00m[37m [39;49;00mRegex.IsMatch(emailAddress,[37m [39;49;00mmailRegEx))[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   343^I[37m                    [39;49;00mretVal.Add([34mNew[39;49;00m[37m [39;49;00mKeyValuePair([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[36mString[39;49;00m)(propertyName,[37m [39;49;00mInvalidEmailAddressError))[37m[39;49;00m$
   344^I[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   345^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   346^I[37m[39;49;00m$
   347^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   348^I[37m[39;49;00m$
   349^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   350^I[37m        [39;49;00m[37m''' Validates a string array of Email Address property.[39;49;00m[37m[39;49;00m$
   351^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   352^I[37m        [39;49;00m[37m''' <param name="propertyName">The name of the property to validate.</param>[39;49;00m[37m[39;49;00m$
   353^I[37m        [39;49;00m[37m''' <param name="retVal">The validation response object.</param>[39;49;00m[37m[39;49;00m$
   354^I[37m        [39;49;00m[37m''' <param name="mailRegEx">The regular expression pattern to use for validation.</param>[39;49;00m[37m[39;49;00m$
   355^I[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m[34mOverloads[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mValidateAddresses[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mpropertyName[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByRef[39;49;00m[37m [39;49;00mretVal[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mValidationResponse,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mmailRegEx[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m$
   356^I[37m            [39;49;00mValidateAddresses(propertyName,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx,[37m [39;49;00m[34mFalse[39;49;00m)[37m[39;49;00m$
   357^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   358^I[37m[39;49;00m$
   359^I[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m$
   360^I[37m        [39;49;00m[37m''' Validates a string array of Email Address property.[39;49;00m[37m[39;49;00m$
   361^I[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m$
   362^I[37m        [39;49;00m[37m''' <param name="propertyName">The name of the property to validate.</param>[39;49;00m[37m[39;49;00m$
   363^I[37m        [39;49;00m[37m''' <param name="retVal">The validation response object.</param>[39;49;00m[37m[39;49;00m$
   364^I[37m        [39;49;00m[37m''' <param name="mailRegEx">The regular expression pattern to use for validation.</param>[39;49;00m[37m[39;49;00m$
   365^I[37m        [39;49;00m[37m''' <param name="required">Indicates if the address is required; False if not specified.</param>[39;49;00m[37m[39;49;00m$
   366^I[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m[34mOverloads[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mValidateAddresses[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mpropertyName[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByRef[39;49;00m[37m [39;49;00mretVal[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mValidationResponse,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mmailRegEx[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mrequired[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m)[37m[39;49;00m$
   367^I[37m[39;49;00m$
   368^I[37m            [39;49;00m[34mDim[39;49;00m[37m [39;49;00memailAddresses()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00mReflectionHelper.Properties.GetProperty([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m())([34mMe[39;49;00m,[37m [39;49;00mpropertyName)[37m[39;49;00m$
   369^I[37m[39;49;00m$
   370^I[37m            [39;49;00m[34mIf[39;49;00m[37m [39;49;00memailAddresses[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[35mOrElse[39;49;00m[37m [39;49;00memailAddresses.Length[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   371^I[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00mrequired[37m [39;49;00m[34mThen[39;49;00m[37m [39;49;00mretVal.Add([34mNew[39;49;00m[37m [39;49;00mKeyValuePair([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[36mString[39;49;00m)(propertyName,[37m [39;49;00m[36mString[39;49;00m.Format(CultureInfo.CurrentCulture,[37m [39;49;00mNullEmailAddressError)))[37m[39;49;00m$
   372^I[37m            [39;49;00m[34mElse[39;49;00m[37m[39;49;00m$
   373^I[37m                [39;49;00m[34mFor[39;49;00m[37m [39;49;00mi[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mInteger[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mTo[39;49;00m[37m [39;49;00memailAddresses.Length[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
   374^I[37m                    [39;49;00m[34mIf[39;49;00m[37m [39;49;00m([34mNot[39;49;00m[37m [39;49;00mRegex.IsMatch(emailAddresses(i),[37m [39;49;00mmailRegEx))[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   375^I[37m                        [39;49;00mretVal.Add([34mNew[39;49;00m[37m [39;49;00mKeyValuePair([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[36mString[39;49;00m)(propertyName,[37m [39;49;00m[36mString[39;49;00m.Format(CultureInfo.CurrentCulture,[37m [39;49;00mInvalidEmailAddressErrorWithAddress,[37m [39;49;00memailAddresses(i))))[37m[39;49;00m$
   376^I[37m                    [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   377^I[37m                [39;49;00m[34mNext[39;49;00m[37m[39;49;00m$
   378^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   379^I[37m[39;49;00m$
   380^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   381^I[37m[39;49;00m$
   382^I[36m#End Region[39;49;00m[37m[39;49;00m$
   383^I[37m[39;49;00m$
   384^I[36m#Region " IDisposable Implementation "[39;49;00m$
   385^I[37m[39;49;00m$
   386^I[37m        [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mDispose[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mdisposing[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m)[37m[39;49;00m$
   387^I[37m            [39;49;00m[34mIf[39;49;00m[37m [39;49;00m[34mNot[39;49;00m[37m [39;49;00m[34mMe[39;49;00m.disposedValue[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   388^I[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00mdisposing[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m$
   389^I[37m                    [39;49;00m_message.Dispose()[37m[39;49;00m$
   390^I[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   391^I[37m                [39;49;00m_mailClient[37m [39;49;00m=[37m [39;49;00m[34mNothing[39;49;00m[37m[39;49;00m$
   392^I[37m                [39;49;00m_message[37m [39;49;00m=[37m [39;49;00m[34mNothing[39;49;00m[37m[39;49;00m$
   393^I[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m$
   394^I[37m            [39;49;00m[34mMe[39;49;00m.disposedValue[37m [39;49;00m=[37m [39;49;00m[34mTrue[39;49;00m[37m[39;49;00m$
   395^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   396^I[37m[39;49;00m$
   397^I[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mDispose[39;49;00m()[37m [39;49;00m[34mImplements[39;49;00m[37m [39;49;00mIDisposable.Dispose[37m[39;49;00m$
   398^I[37m            [39;49;00m[37m' Do not change this code.  Put cleanup code in Dispose(ByVal disposing As Boolean) above.[39;49;00m[37m[39;49;00m$
   399^I[37m            [39;49;00mDispose([34mTrue[39;49;00m)[37m[39;49;00m$
   400^I[37m            [39;49;00mGC.SuppressFinalize([34mMe[39;49;00m)[37m[39;49;00m$
   401^I[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m$
   402^I[37m[39;49;00m$
   403^I[36m#End Region[39;49;00m[37m[39;49;00m$
   404^I[37m[39;49;00m$
   405^I[37m    [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mClass[39;49;00m[37m[39;49;00m$
   406^I[37m[39;49;00m$
   407^I[34mEnd[39;49;00m[37m [39;49;00m[34mNamespace[39;49;00m$
