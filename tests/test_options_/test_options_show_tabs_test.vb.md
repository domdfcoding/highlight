[37m' Copyright (c) 2008 Silken Web - Free BSD License[39;49;00m[37m[39;49;00m
[37m' All rights reserved.[39;49;00m[37m[39;49;00m
[37m'[39;49;00m[37m[39;49;00m
[37m' Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:[39;49;00m[37m[39;49;00m
[37m' * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer[39;49;00m[37m[39;49;00m
[37m' * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.[39;49;00m[37m[39;49;00m
[37m' * Neither the name of Silken Web nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.[39;49;00m[37m[39;49;00m
[37m'[39;49;00m[37m[39;49;00m
[37m' THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,[39;49;00m[37m[39;49;00m
[37m' THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS[39;49;00m[37m[39;49;00m
[37m' BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE[39;49;00m[37m[39;49;00m
[37m' GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT[39;49;00m[37m[39;49;00m
[37m' LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH[39;49;00m[37m[39;49;00m
[37m' DAMAGE.[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[34mImports[39;49;00m[37m [39;49;00m[04m[36mSystem[39;49;00m[04m[36m.[39;49;00m[04m[36mNet[39;49;00m[04m[36m.[39;49;00m[04m[36mMail[39;49;00m[37m[39;49;00m
[34mImports[39;49;00m[37m [39;49;00m[04m[36mSilkenWeb[39;49;00m[04m[36m.[39;49;00m[04m[36mEntities[39;49;00m[37m[39;49;00m
[34mImports[39;49;00m[37m [39;49;00m[04m[36mSystem[39;49;00m[04m[36m.[39;49;00m[04m[36mText[39;49;00m[04m[36m.[39;49;00m[04m[36mRegularExpressions[39;49;00m[37m[39;49;00m
[34mImports[39;49;00m[37m [39;49;00m[04m[36mSystem[39;49;00m[04m[36m.[39;49;00m[04m[36mReflection[39;49;00m[37m[39;49;00m
[34mImports[39;49;00m[37m [39;49;00m[04m[36mSilkenWeb[39;49;00m[04m[36m.[39;49;00m[04m[36mValidation[39;49;00m[37m[39;49;00m
[34mImports[39;49;00m[37m [39;49;00m[04m[36mSystem[39;49;00m[04m[36m.[39;49;00m[04m[36mGlobalization[39;49;00m[37m[39;49;00m
[34mImports[39;49;00m[37m [39;49;00m[04m[36mSilkenWeb[39;49;00m[04m[36m.[39;49;00m[04m[36mReflection[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[34mNamespace[39;49;00m[37m [39;49;00m[04m[36mSilkenWeb[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[37m''' Represents an Email and what you can do with it.[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[37m''' <remarks>[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[37m''' Keith Jackson[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[37m''' 11/04/2008[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[37m'''[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[37m''' This class is intended to be inherrited for providing all manner of system generated emails, each represented by it's own class.[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[37m''' </remarks>[39;49;00m[37m[39;49;00m
[37m    [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mMustInherit[39;49;00m[37m [39;49;00m[34mClass[39;49;00m[37m [39;49;00m[04m[32mEmailBase[39;49;00m[37m [39;49;00m:[37m [39;49;00m[34mImplements[39;49;00m[37m [39;49;00mIValidatable,[37m [39;49;00mIDisposable[37m[39;49;00m
[37m[39;49;00m
[36m#Region " Constants "[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mConst[39;49;00m[37m [39;49;00mLenientRegexPattern[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mConst[39;49;00m[37m [39;49;00mStrictRegexPattern[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m^(([^<>()[\]\\.,;:\s@\[39;49;00m[33m""[39;49;00m[33m]+(\.[^<>()[\]\\.,;:\s@\[39;49;00m[33m""[39;49;00m[33m]+)*)|(\[39;49;00m[33m""[39;49;00m[33m.+\[39;49;00m[33m""[39;49;00m[33m))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mConst[39;49;00m[37m [39;49;00mInvalidEmailAddressError[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mThe Email address provided was invalid[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mConst[39;49;00m[37m [39;49;00mInvalidEmailAddressErrorWithAddress[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mThe Email address, {0}, provided was invalid[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mConst[39;49;00m[37m [39;49;00mNullEmailAddressError[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33mThe Email address was not provided[39;49;00m[33m"[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[36m#End Region[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[36m#Region " Fields "[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00mdisposedValue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m_message[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mMailMessage[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailMessage()[37m[39;49;00m
[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m_mailClient[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mSmtpClient[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m_useStrictValidation[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[36m#End Region[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[36m#Region " Construction "[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' Instantiates a new Email of the derived type.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="sender">The email address of the sender of the message.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="recipients">The email addresses of the recipients of the message.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="subject">The subject of the message.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="body">The body of the message.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mNew[39;49;00m([34mByVal[39;49;00m[37m [39;49;00msender[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00msubject[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mbody[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00m[34mParamArray[39;49;00m[37m [39;49;00mrecipients[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m())[37m[39;49;00m
[37m            [39;49;00m_message.From[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(sender)[37m[39;49;00m
[37m            [39;49;00m[34mFor[39;49;00m[37m [39;49;00mi[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mInteger[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mTo[39;49;00m[37m [39;49;00mrecipients.Length[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m
[37m                [39;49;00m_message.To.Add(recipients(i))[37m[39;49;00m
[37m            [39;49;00m[34mNext[39;49;00m[37m[39;49;00m
[37m            [39;49;00m_message.Subject[37m [39;49;00m=[37m [39;49;00msubject[37m[39;49;00m
[37m            [39;49;00m_message.Body[37m [39;49;00m=[37m [39;49;00mbody[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[36m#End Region[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[36m#Region " Properties "[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' Gets the Attachments for the message.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mReadOnly[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mAttachments[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mAttachmentCollection[37m[39;49;00m
[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.Attachments[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' The email addresses of the BCC recipients of the message.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mBccRecipients[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m()[37m[39;49;00m
[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.Bcc.ToAddressStringArray()[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m())[37m[39;49;00m
[37m                [39;49;00m_message.Bcc.Clear()[37m[39;49;00m
[37m                [39;49;00m_message.Bcc.Add(value.ToDelimitedString())[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' The body of the message.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mBody[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.Body[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m
[37m                [39;49;00m_message.Body[37m [39;49;00m=[37m [39;49;00mvalue[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' The email addresses of the CC recipients of the message.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mCCRecipients[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m()[37m[39;49;00m
[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.CC.ToAddressStringArray()[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m())[37m[39;49;00m
[37m                [39;49;00m_message.CC.Clear()[37m[39;49;00m
[37m                [39;49;00m_message.CC.Add(value.ToDelimitedString())[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' Gets or Sets a flag to indicate if the body of the message is HTML.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mIsBodyHtml[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.IsBodyHtml[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m)[37m[39;49;00m
[37m                [39;49;00m_message.IsBodyHtml[37m [39;49;00m=[37m [39;49;00mvalue[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' Gets the Mail message wrapped by the EmailBase class.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mReadOnly[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mMessage[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mMailMessage[37m[39;49;00m
[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' Gets or Sets the Priority of the message.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mPriority[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mMailPriority[37m[39;49;00m
[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.Priority[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mMailPriority)[37m[39;49;00m
[37m                [39;49;00m_message.Priority[37m [39;49;00m=[37m [39;49;00mvalue[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' The email addresses of the recipients of the message.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mRecipients[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m()[37m[39;49;00m
[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.To.ToAddressStringArray()[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m())[37m[39;49;00m
[37m                [39;49;00m_message.To.Clear()[37m[39;49;00m
[37m                [39;49;00m_message.To.Add(value.ToDelimitedString())[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' The reply email address of the sender of the message.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mReplyTo[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00m_message.ReplyTo[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m
[37m                    [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m[36mString[39;49;00m.Empty[37m[39;49;00m
[37m                [39;49;00m[34mElse[39;49;00m[37m[39;49;00m
[37m                    [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.ReplyTo.Address[37m[39;49;00m
[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m
[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00m_message.ReplyTo[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m
[37m                    [39;49;00m_message.ReplyTo[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(value)[37m[39;49;00m
[37m                [39;49;00m[34mElse[39;49;00m[37m[39;49;00m
[37m                    [39;49;00m_message.ReplyTo[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(value,[37m [39;49;00m_message.ReplyTo.DisplayName)[37m[39;49;00m
[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' The reply display name of the sender of the message.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mReplyToDisplayName[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00m_message.ReplyTo[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m
[37m                    [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m[36mString[39;49;00m.Empty[37m[39;49;00m
[37m                [39;49;00m[34mElse[39;49;00m[37m[39;49;00m
[37m                    [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.ReplyTo.DisplayName[37m[39;49;00m
[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m
[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00m_message.ReplyTo[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m
[37m                    [39;49;00m_message.ReplyTo[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(_message.From.Address,[37m [39;49;00mvalue)[37m[39;49;00m
[37m                [39;49;00m[34mElse[39;49;00m[37m[39;49;00m
[37m                    [39;49;00m_message.ReplyTo[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(_message.ReplyTo.Address,[37m [39;49;00mvalue)[37m[39;49;00m
[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' The email address of the sender of the message.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mSender[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.From.Address[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m
[37m                [39;49;00m_message.From[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(value,[37m [39;49;00m_message.From.DisplayName)[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' The display name of the sender of the message.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mSenderDisplayName[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.From.DisplayName[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m
[37m                [39;49;00m_message.From[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mMailAddress(_message.From.Address,[37m [39;49;00mvalue)[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' The subject of the message.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mSubject[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_message.Subject[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m
[37m                [39;49;00m_message.Subject[37m [39;49;00m=[37m [39;49;00mvalue[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[36m#End Region[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[36m#Region " Methods "[39;49;00m
[37m[39;49;00m
[36m#Region " Send Methods "[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' Sends this email[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="mailServer">The SMTP server to use to send the email.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mSend[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mmailServer[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m
[37m            [39;49;00m_mailClient[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mSmtpClient(mailServer)[37m[39;49;00m
[37m            [39;49;00m_mailClient.Send(_message)[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' Sends this email asynchronously.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="mailServer">The SMTP server to use to send the email.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="userToken">A user defined token passed to the recieving method on completion of the asynchronous task.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mSendAsync[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mmailServer[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00muserToken[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mObject[39;49;00m)[37m[39;49;00m
[37m            [39;49;00m_mailClient[37m [39;49;00m=[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mSmtpClient(mailServer)[37m[39;49;00m
[37m            [39;49;00m_mailClient.SendAsync(_message,[37m [39;49;00muserToken)[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' Cancels an attempt to send this email asynchronously.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mSendAsyncCancel[39;49;00m()[37m[39;49;00m
[37m            [39;49;00m_mailClient.SendAsyncCancel()[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[36m#End Region[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[36m#End Region[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[36m#Region " IValidatable Implementation "[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' gets and Sets a flag to indicate whether to use strict validation.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m [39;49;00m[32mUseStrictValidation[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mReturn[39;49;00m[37m [39;49;00m_useStrictValidation[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mGet[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mSet[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mvalue[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m)[37m[39;49;00m
[37m                [39;49;00m_useStrictValidation[37m [39;49;00m=[37m [39;49;00mvalue[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSet[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mProperty[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' Validates this email.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <returns>A ValidationResponse, containing a flag to indicate if validation was passed and a collection of Property Names and validation errors.</returns>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mFunction[39;49;00m[37m [39;49;00m[32mValidate[39;49;00m()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mValidationResponse[37m [39;49;00m[34mImplements[39;49;00m[37m [39;49;00mIValidatable.Validate[37m[39;49;00m
[37m[39;49;00m
[37m            [39;49;00m[34mDim[39;49;00m[37m [39;49;00mretVal[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[34mNew[39;49;00m[37m [39;49;00mValidationResponse()[37m[39;49;00m
[37m            [39;49;00m[34mDim[39;49;00m[37m [39;49;00mmailRegEx[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34mIf[39;49;00m(_useStrictValidation,[37m [39;49;00mStrictRegexPattern,[37m [39;49;00mLenientRegexPattern)[37m[39;49;00m
[37m[39;49;00m
[37m            [39;49;00mValidateAddress([33m"[39;49;00m[33mSender[39;49;00m[33m"[39;49;00m,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx,[37m [39;49;00m[34mTrue[39;49;00m)[37m[39;49;00m
[37m            [39;49;00mValidateAddresses([33m"[39;49;00m[33mRecipients[39;49;00m[33m"[39;49;00m,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx,[37m [39;49;00m[34mTrue[39;49;00m)[37m[39;49;00m
[37m            [39;49;00mValidateAddresses([33m"[39;49;00m[33mCcRecipients[39;49;00m[33m"[39;49;00m,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx)[37m[39;49;00m
[37m            [39;49;00mValidateAddresses([33m"[39;49;00m[33mBccRecipients[39;49;00m[33m"[39;49;00m,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx)[37m[39;49;00m
[37m            [39;49;00mValidateAddress([33m"[39;49;00m[33mReplyTo[39;49;00m[33m"[39;49;00m,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx)[37m[39;49;00m
[37m[39;49;00m
[37m            [39;49;00m[34mReturn[39;49;00m[37m [39;49;00mretVal[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mFunction[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' Validates a single Email Address property.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="propertyName">The name of the property to validate.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="retVal">The validation response object.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="mailRegEx">The regular expression pattern to use for validation.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m[34mOverloads[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mValidateAddress[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mpropertyName[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByRef[39;49;00m[37m [39;49;00mretVal[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mValidationResponse,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mmailRegEx[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m
[37m            [39;49;00mValidateAddress(propertyName,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx,[37m [39;49;00m[34mFalse[39;49;00m)[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' Validates a single Email Address property.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="propertyName">The name of the property to validate.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="retVal">The validation response object.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="mailRegEx">The regular expression pattern to use for validation.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="required">Indicates if the address is required; False if not specified.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m[34mOverloads[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mValidateAddress[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mpropertyName[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByRef[39;49;00m[37m [39;49;00mretVal[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mValidationResponse,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mmailRegEx[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mrequired[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m)[37m[39;49;00m
[37m[39;49;00m
[37m            [39;49;00m[34mDim[39;49;00m[37m [39;49;00memailAddress[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00mReflectionHelper.Properties.GetProperty([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m)([34mMe[39;49;00m,[37m [39;49;00mpropertyName)[37m[39;49;00m
[37m[39;49;00m
[37m            [39;49;00m[34mIf[39;49;00m[37m [39;49;00memailAddress[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[35mOrElse[39;49;00m[37m [39;49;00memailAddress.Length[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00mrequired[37m [39;49;00m[34mThen[39;49;00m[37m [39;49;00mretVal.Add([34mNew[39;49;00m[37m [39;49;00mKeyValuePair([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[36mString[39;49;00m)(propertyName,[37m [39;49;00mNullEmailAddressError))[37m[39;49;00m
[37m            [39;49;00m[34mElse[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00m([34mNot[39;49;00m[37m [39;49;00mRegex.IsMatch(emailAddress,[37m [39;49;00mmailRegEx))[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m
[37m                    [39;49;00mretVal.Add([34mNew[39;49;00m[37m [39;49;00mKeyValuePair([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[36mString[39;49;00m)(propertyName,[37m [39;49;00mInvalidEmailAddressError))[37m[39;49;00m
[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' Validates a string array of Email Address property.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="propertyName">The name of the property to validate.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="retVal">The validation response object.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="mailRegEx">The regular expression pattern to use for validation.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m[34mOverloads[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mValidateAddresses[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mpropertyName[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByRef[39;49;00m[37m [39;49;00mretVal[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mValidationResponse,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mmailRegEx[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m)[37m[39;49;00m
[37m            [39;49;00mValidateAddresses(propertyName,[37m [39;49;00mretVal,[37m [39;49;00mmailRegEx,[37m [39;49;00m[34mFalse[39;49;00m)[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[37m''' <summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' Validates a string array of Email Address property.[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' </summary>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="propertyName">The name of the property to validate.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="retVal">The validation response object.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="mailRegEx">The regular expression pattern to use for validation.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[37m''' <param name="required">Indicates if the address is required; False if not specified.</param>[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mPrivate[39;49;00m[37m [39;49;00m[34mOverloads[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mValidateAddresses[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mpropertyName[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByRef[39;49;00m[37m [39;49;00mretVal[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00mValidationResponse,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mmailRegEx[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[34mByVal[39;49;00m[37m [39;49;00mrequired[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m)[37m[39;49;00m
[37m[39;49;00m
[37m            [39;49;00m[34mDim[39;49;00m[37m [39;49;00memailAddresses()[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mString[39;49;00m[37m [39;49;00m=[37m [39;49;00mReflectionHelper.Properties.GetProperty([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m())([34mMe[39;49;00m,[37m [39;49;00mpropertyName)[37m[39;49;00m
[37m[39;49;00m
[37m            [39;49;00m[34mIf[39;49;00m[37m [39;49;00memailAddresses[37m [39;49;00m[35mIs[39;49;00m[37m [39;49;00m[34mNothing[39;49;00m[37m [39;49;00m[35mOrElse[39;49;00m[37m [39;49;00memailAddresses.Length[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00mrequired[37m [39;49;00m[34mThen[39;49;00m[37m [39;49;00mretVal.Add([34mNew[39;49;00m[37m [39;49;00mKeyValuePair([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[36mString[39;49;00m)(propertyName,[37m [39;49;00m[36mString[39;49;00m.Format(CultureInfo.CurrentCulture,[37m [39;49;00mNullEmailAddressError)))[37m[39;49;00m
[37m            [39;49;00m[34mElse[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mFor[39;49;00m[37m [39;49;00mi[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mInteger[39;49;00m[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m[34mTo[39;49;00m[37m [39;49;00memailAddresses.Length[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m
[37m                    [39;49;00m[34mIf[39;49;00m[37m [39;49;00m([34mNot[39;49;00m[37m [39;49;00mRegex.IsMatch(emailAddresses(i),[37m [39;49;00mmailRegEx))[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m
[37m                        [39;49;00mretVal.Add([34mNew[39;49;00m[37m [39;49;00mKeyValuePair([34mOf[39;49;00m[37m [39;49;00m[36mString[39;49;00m,[37m [39;49;00m[36mString[39;49;00m)(propertyName,[37m [39;49;00m[36mString[39;49;00m.Format(CultureInfo.CurrentCulture,[37m [39;49;00mInvalidEmailAddressErrorWithAddress,[37m [39;49;00memailAddresses(i))))[37m[39;49;00m
[37m                    [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mNext[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[36m#End Region[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[36m#Region " IDisposable Implementation "[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mProtected[39;49;00m[37m [39;49;00m[34mOverridable[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mDispose[39;49;00m([34mByVal[39;49;00m[37m [39;49;00mdisposing[37m [39;49;00m[35mAs[39;49;00m[37m [39;49;00m[36mBoolean[39;49;00m)[37m[39;49;00m
[37m            [39;49;00m[34mIf[39;49;00m[37m [39;49;00m[34mNot[39;49;00m[37m [39;49;00m[34mMe[39;49;00m.disposedValue[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m
[37m                [39;49;00m[34mIf[39;49;00m[37m [39;49;00mdisposing[37m [39;49;00m[34mThen[39;49;00m[37m[39;49;00m
[37m                    [39;49;00m_message.Dispose()[37m[39;49;00m
[37m                [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m
[37m                [39;49;00m_mailClient[37m [39;49;00m=[37m [39;49;00m[34mNothing[39;49;00m[37m[39;49;00m
[37m                [39;49;00m_message[37m [39;49;00m=[37m [39;49;00m[34mNothing[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mIf[39;49;00m[37m[39;49;00m
[37m            [39;49;00m[34mMe[39;49;00m.disposedValue[37m [39;49;00m=[37m [39;49;00m[34mTrue[39;49;00m[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m        [39;49;00m[34mPublic[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m [39;49;00m[32mDispose[39;49;00m()[37m [39;49;00m[34mImplements[39;49;00m[37m [39;49;00mIDisposable.Dispose[37m[39;49;00m
[37m            [39;49;00m[37m' Do not change this code.  Put cleanup code in Dispose(ByVal disposing As Boolean) above.[39;49;00m[37m[39;49;00m
[37m            [39;49;00mDispose([34mTrue[39;49;00m)[37m[39;49;00m
[37m            [39;49;00mGC.SuppressFinalize([34mMe[39;49;00m)[37m[39;49;00m
[37m        [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mSub[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[36m#End Region[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[37m    [39;49;00m[34mEnd[39;49;00m[37m [39;49;00m[34mClass[39;49;00m[37m[39;49;00m
[37m[39;49;00m
[34mEnd[39;49;00m[37m [39;49;00m[34mNamespace[39;49;00m
