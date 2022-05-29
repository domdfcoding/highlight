Using lexer <pygments.lexers.HandlebarsHtmlLexer with {'ensurenl': False, 'tabsize': 0}>
[36m{{[39;49;00m[34m#[39;49;00m[34mview[39;49;00m [31mEmberFirebaseChat[39;49;00m[31m.ChatView[39;49;00m [36mclass[39;49;00m=[33m"chat-container"[39;49;00m[36m}}[39;49;00m
  <[94mdiv[39;49;00m [36mclass[39;49;00m=[33m"chat-messages-container"[39;49;00m>
    <[94mul[39;49;00m [36mclass[39;49;00m=[33m"chat-messages"[39;49;00m>
      [36m{{[39;49;00m[34m#[39;49;00m[34meach[39;49;00m [31mmessage[39;49;00m [31min[39;49;00m [31mcontent[39;49;00m[36m}}[39;49;00m
      <[94mli[39;49;00m>
        [[36m{{[39;49;00m[31mformatTimestamp[39;49;00m [33m"message.timestamp"[39;49;00m [36mfmtString[39;49;00m=[33m"h:mm:ss A"[39;49;00m[36m}}[39;49;00m]
        <[94mstrong[39;49;00m>[36m{{[39;49;00m[31mmessage[39;49;00m[31m.sender[39;49;00m[36m}}[39;49;00m</[94mstrong[39;49;00m>: [36m{{[39;49;00m[31mmessage[39;49;00m[31m.content[39;49;00m[36m}}[39;49;00m
      </[94mli[39;49;00m>
      [36m{{[39;49;00m[34m/[39;49;00m[34meach[39;49;00m[36m}}[39;49;00m
    </[94mul[39;49;00m>
  </[94mdiv[39;49;00m>

  [37m{{! Comment }}[39;49;00m
  [37m{{{[39;49;00m[31munescaped[39;49;00m [31mvalue[39;49;00m[37m}}}[39;49;00m

  [36m{{[39;49;00m[34m#[39;49;00m[34mview[39;49;00m [31mEmberFirebaseChat[39;49;00m[31m.InputView[39;49;00m [36mclass[39;49;00m=[33m"chat-input-container"[39;49;00m[36m}}[39;49;00m
    <[94mform[39;49;00m [36mclass[39;49;00m=[33m"form-inline"[39;49;00m>
      [36m{{[39;49;00m[34m#[39;49;00m[34mif[39;49;00m [33m"auth.authed"[39;49;00m[36m}}[39;49;00m
        [36m{{[39;49;00m[34m#[39;49;00m[34mif[39;49;00m [33m"auth.hasName"[39;49;00m[36m}}[39;49;00m
          <[94minput[39;49;00m [36mtype[39;49;00m=[33m"text"[39;49;00m [36mid[39;49;00m=[33m"message"[39;49;00m [36mplaceholder[39;49;00m=[33m"Message"[39;49;00m>
          <[94mbutton[39;49;00m [36m{{[39;49;00m[31maction[39;49;00m [33m"postMessage"[39;49;00m [36mtarget[39;49;00m=[33m"view"[39;49;00m[36m}}[39;49;00m [36mclass[39;49;00m=[33m"btn"[39;49;00m>Send</[94mbutton[39;49;00m>
        [36m{{[39;49;00m[31melse[39;49;00m[36m}}[39;49;00m
          <[94minput[39;49;00m [36mtype[39;49;00m=[33m"text"[39;49;00m [36mid[39;49;00m=[33m"username"[39;49;00m [36mplaceholder[39;49;00m=[33m"Enter your username..."[39;49;00m>
          <[94mbutton[39;49;00m [36m{{[39;49;00m[31maction[39;49;00m [33m"pickName"[39;49;00m [36mtarget[39;49;00m=[33m"view"[39;49;00m[36m}}[39;49;00m [36mclass[39;49;00m=[33m"btn"[39;49;00m>Send</[94mbutton[39;49;00m>
        [36m{{[39;49;00m[34m/[39;49;00m[34mif[39;49;00m[36m}}[39;49;00m
      [36m{{[39;49;00m[31melse[39;49;00m[36m}}[39;49;00m
        <[94minput[39;49;00m [36mtype[39;49;00m=[33m"text"[39;49;00m [36mplaceholder[39;49;00m=[33m"Log in with Persona to chat!"[39;49;00m [36mdisabled[39;49;00m=[33m"disabled"[39;49;00m>
        <[94mbutton[39;49;00m [36m{{[39;49;00m[31maction[39;49;00m [33m"login"[39;49;00m[36m}}[39;49;00m [36mclass[39;49;00m=[33m"btn"[39;49;00m>Login</[94mbutton[39;49;00m>
      [36m{{[39;49;00m[34m/[39;49;00m[34mif[39;49;00m[36m}}[39;49;00m
    </[94mform[39;49;00m>
  [36m{{[39;49;00m[34m/[39;49;00m[34mview[39;49;00m[36m}}[39;49;00m
[36m{{[39;49;00m[34m/[39;49;00m[34mview[39;49;00m[36m}}[39;49;00m
