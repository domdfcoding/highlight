     1^I [37m/****************************************************************************[39;49;00m$
     2^I[37m **[39;49;00m$
     3^I[37m ** Copyright (C) 2011 Nokia Corporation and/or its subsidiary(-ies).[39;49;00m$
     4^I[37m ** All rights reserved.[39;49;00m$
     5^I[37m ** Contact: Nokia Corporation (qt-info@nokia.com)[39;49;00m$
     6^I[37m **[39;49;00m$
     7^I[37m ** This file is part of the QtDeclarative module of the Qt Toolkit.[39;49;00m$
     8^I[37m **[39;49;00m$
     9^I[37m ** $QT_BEGIN_LICENSE:LGPL$[39;49;00m$
    10^I[37m ** GNU Lesser General Public License Usage[39;49;00m$
    11^I[37m ** This file may be used under the terms of the GNU Lesser General Public[39;49;00m$
    12^I[37m ** License version 2.1 as published by the Free Software Foundation and[39;49;00m$
    13^I[37m ** appearing in the file LICENSE.LGPL included in the packaging of this[39;49;00m$
    14^I[37m ** file. Please review the following information to ensure the GNU Lesser[39;49;00m$
    15^I[37m ** General Public License version 2.1 requirements will be met:[39;49;00m$
    16^I[37m ** http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.[39;49;00m$
    17^I[37m **[39;49;00m$
    18^I[37m ** In addition, as a special exception, Nokia gives you certain additional[39;49;00m$
    19^I[37m ** rights. These rights are described in the Nokia Qt LGPL Exception[39;49;00m$
    20^I[37m ** version 1.1, included in the file LGPL_EXCEPTION.txt in this package.[39;49;00m$
    21^I[37m **[39;49;00m$
    22^I[37m ** GNU General Public License Usage[39;49;00m$
    23^I[37m ** Alternatively, this file may be used under the terms of the GNU General[39;49;00m$
    24^I[37m ** Public License version 3.0 as published by the Free Software Foundation[39;49;00m$
    25^I[37m ** and appearing in the file LICENSE.GPL included in the packaging of this[39;49;00m$
    26^I[37m ** file. Please review the following information to ensure the GNU General[39;49;00m$
    27^I[37m ** Public License version 3.0 requirements will be met:[39;49;00m$
    28^I[37m ** http://www.gnu.org/copyleft/gpl.html.[39;49;00m$
    29^I[37m **[39;49;00m$
    30^I[37m ** Other Usage[39;49;00m$
    31^I[37m ** Alternatively, this file may be used in accordance with the terms and[39;49;00m$
    32^I[37m ** conditions contained in a signed written agreement between you and Nokia.[39;49;00m$
    33^I[37m **[39;49;00m$
    34^I[37m **[39;49;00m$
    35^I[37m **[39;49;00m$
    36^I[37m **[39;49;00m$
    37^I[37m **[39;49;00m$
    38^I[37m ** $QT_END_LICENSE$[39;49;00m$
    39^I[37m **[39;49;00m$
    40^I[37m ****************************************************************************/[39;49;00m$
    41^I$
    42^I [34mimport[39;49;00m QtQuick [34m1.0[39;49;00m$
    43^I [34mimport[39;49;00m [33m"MinehuntCore"[39;49;00m [34m1.0[39;49;00m$
    44^I$
    45^I Item {$
    46^I     [34mid: field[39;49;00m$
    47^I     property [34mint[39;49;00m [34mclickx:[39;49;00m [34m0[39;49;00m$
    48^I     property [34mint[39;49;00m [34mclicky:[39;49;00m [34m0[39;49;00m$
    49^I$
    50^I     [34mwidth:[39;49;00m [34m450[39;49;00m; [34mheight:[39;49;00m [34m450[39;49;00m$
    51^I$
    52^I     Image { [34msource:[39;49;00m [33m"MinehuntCore/pics/background.png"[39;49;00m; [34manchors.fill:[39;49;00m parent; [34mfillMode:[39;49;00m Image.Tile }$
    53^I$
    54^I     Grid {$
    55^I         [34manchors.horizontalCenter:[39;49;00m parent.horizontalCenter$
    56^I         [34mcolumns:[39;49;00m [34m9[39;49;00m; [34mspacing:[39;49;00m [34m1[39;49;00m$
    57^I$
    58^I         Repeater {$
    59^I             [34mid: repeater[39;49;00m$
    60^I             [34mmodel:[39;49;00m tiles$
    61^I             [34mdelegate:[39;49;00m Tile {}$
    62^I         }$
    63^I     }$
    64^I$
    65^I     Row {$
    66^I         [34mid: gamedata[39;49;00m$
    67^I         [34mx:[39;49;00m [34m20[39;49;00m; [34mspacing:[39;49;00m [34m20[39;49;00m$
    68^I         [34manchors.bottom:[39;49;00m field.bottom; [34manchors.bottomMargin:[39;49;00m [34m15[39;49;00m$
    69^I$
    70^I         Image {$
    71^I             [34msource:[39;49;00m [33m"MinehuntCore/pics/quit.png"[39;49;00m$
    72^I             [34mscale:[39;49;00m quitMouse.pressed ? [34m0.8[39;49;00m : [34m1.0[39;49;00m$
    73^I             [34msmooth:[39;49;00m quitMouse.pressed$
    74^I             [34my:[39;49;00m [34m10[39;49;00m$
    75^I             MouseArea {$
    76^I                 [34mid: quitMouse[39;49;00m$
    77^I                 [34manchors.fill:[39;49;00m parent$
    78^I                 [34manchors.margins:[39;49;00m -[34m20[39;49;00m$
    79^I                 [34monClicked:[39;49;00m Qt.quit()$
    80^I             }$
    81^I         }$
    82^I         Column {$
    83^I             [34mspacing:[39;49;00m [34m2[39;49;00m$
    84^I             Image { [34msource:[39;49;00m [33m"MinehuntCore/pics/bomb-color.png"[39;49;00m }$
    85^I             Text { [34manchors.horizontalCenter:[39;49;00m parent.horizontalCenter; [34mcolor:[39;49;00m [33m"white"[39;49;00m; [34mtext:[39;49;00m numMines }$
    86^I         }$
    87^I$
    88^I         Column {$
    89^I             [34mspacing:[39;49;00m [34m2[39;49;00m$
    90^I             Image { [34msource:[39;49;00m [33m"MinehuntCore/pics/flag-color.png"[39;49;00m }$
    91^I             Text { [34manchors.horizontalCenter:[39;49;00m parent.horizontalCenter; [34mcolor:[39;49;00m [33m"white"[39;49;00m; [34mtext:[39;49;00m numFlags }$
    92^I         }$
    93^I     }$
    94^I$
    95^I     Image {$
    96^I         [34manchors.bottom:[39;49;00m field.bottom; [34manchors.bottomMargin:[39;49;00m [34m15[39;49;00m$
    97^I         [34manchors.right:[39;49;00m field.right; [34manchors.rightMargin:[39;49;00m [34m20[39;49;00m$
    98^I         [34msource:[39;49;00m isPlaying ? [33m'MinehuntCore/pics/face-smile.png'[39;49;00m :$
    99^I         hasWon ? [33m'MinehuntCore/pics/face-smile-big.png'[39;49;00m: [33m'MinehuntCore/pics/face-sad.png'[39;49;00m$
   100^I$
   101^I         MouseArea { [34manchors.fill:[39;49;00m parent; [34monPressed:[39;49;00m reset() }$
   102^I     }$
   103^I     Text {$
   104^I         [34manchors.centerIn:[39;49;00m parent; [34mwidth:[39;49;00m parent.width - [34m20[39;49;00m$
   105^I         [34mhorizontalAlignment:[39;49;00m Text.AlignHCenter$
   106^I         [34mwrapMode:[39;49;00m Text.WordWrap$
   107^I         [34mtext:[39;49;00m [33m"Minehunt demo has to be compiled to run.\n\nPlease see README."[39;49;00m$
   108^I         [34mcolor:[39;49;00m [33m"white"[39;49;00m; [34mfont.bold:[39;49;00m [34mtrue[39;49;00m; [34mfont.pixelSize:[39;49;00m [34m14[39;49;00m$
   109^I         [34mvisible:[39;49;00m tiles == [34mundefined[39;49;00m$
   110^I     }$
   111^I$
   112^I }$
