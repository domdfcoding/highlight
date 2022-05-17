     1	 [37m/****************************************************************************[39;49;00m
     2	[37m **[39;49;00m
     3	[37m ** Copyright (C) 2011 Nokia Corporation and/or its subsidiary(-ies).[39;49;00m
     4	[37m ** All rights reserved.[39;49;00m
     5	[37m ** Contact: Nokia Corporation (qt-info@nokia.com)[39;49;00m
     6	[37m **[39;49;00m
     7	[37m ** This file is part of the QtDeclarative module of the Qt Toolkit.[39;49;00m
     8	[37m **[39;49;00m
     9	[37m ** $QT_BEGIN_LICENSE:LGPL$[39;49;00m
    10	[37m ** GNU Lesser General Public License Usage[39;49;00m
    11	[37m ** This file may be used under the terms of the GNU Lesser General Public[39;49;00m
    12	[37m ** License version 2.1 as published by the Free Software Foundation and[39;49;00m
    13	[37m ** appearing in the file LICENSE.LGPL included in the packaging of this[39;49;00m
    14	[37m ** file. Please review the following information to ensure the GNU Lesser[39;49;00m
    15	[37m ** General Public License version 2.1 requirements will be met:[39;49;00m
    16	[37m ** http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.[39;49;00m
    17	[37m **[39;49;00m
    18	[37m ** In addition, as a special exception, Nokia gives you certain additional[39;49;00m
    19	[37m ** rights. These rights are described in the Nokia Qt LGPL Exception[39;49;00m
    20	[37m ** version 1.1, included in the file LGPL_EXCEPTION.txt in this package.[39;49;00m
    21	[37m **[39;49;00m
    22	[37m ** GNU General Public License Usage[39;49;00m
    23	[37m ** Alternatively, this file may be used under the terms of the GNU General[39;49;00m
    24	[37m ** Public License version 3.0 as published by the Free Software Foundation[39;49;00m
    25	[37m ** and appearing in the file LICENSE.GPL included in the packaging of this[39;49;00m
    26	[37m ** file. Please review the following information to ensure the GNU General[39;49;00m
    27	[37m ** Public License version 3.0 requirements will be met:[39;49;00m
    28	[37m ** http://www.gnu.org/copyleft/gpl.html.[39;49;00m
    29	[37m **[39;49;00m
    30	[37m ** Other Usage[39;49;00m
    31	[37m ** Alternatively, this file may be used in accordance with the terms and[39;49;00m
    32	[37m ** conditions contained in a signed written agreement between you and Nokia.[39;49;00m
    33	[37m **[39;49;00m
    34	[37m **[39;49;00m
    35	[37m **[39;49;00m
    36	[37m **[39;49;00m
    37	[37m **[39;49;00m
    38	[37m ** $QT_END_LICENSE$[39;49;00m
    39	[37m **[39;49;00m
    40	[37m ****************************************************************************/[39;49;00m
    41
    42	 [34mimport[39;49;00m QtQuick [34m1.0[39;49;00m
    43	 [34mimport[39;49;00m [33m"MinehuntCore"[39;49;00m [34m1.0[39;49;00m
    44
    45	 Item {
    46	     [34mid: field[39;49;00m
    47	     property [34mint[39;49;00m [34mclickx:[39;49;00m [34m0[39;49;00m
    48	     property [34mint[39;49;00m [34mclicky:[39;49;00m [34m0[39;49;00m
    49
    50	     [34mwidth:[39;49;00m [34m450[39;49;00m; [34mheight:[39;49;00m [34m450[39;49;00m
    51
    52	     Image { [34msource:[39;49;00m [33m"MinehuntCore/pics/background.png"[39;49;00m; [34manchors.fill:[39;49;00m parent; [34mfillMode:[39;49;00m Image.Tile }
    53
    54	     Grid {
    55	         [34manchors.horizontalCenter:[39;49;00m parent.horizontalCenter
    56	         [34mcolumns:[39;49;00m [34m9[39;49;00m; [34mspacing:[39;49;00m [34m1[39;49;00m
    57
    58	         Repeater {
    59	             [34mid: repeater[39;49;00m
    60	             [34mmodel:[39;49;00m tiles
    61	             [34mdelegate:[39;49;00m Tile {}
    62	         }
    63	     }
    64
    65	     Row {
    66	         [34mid: gamedata[39;49;00m
    67	         [34mx:[39;49;00m [34m20[39;49;00m; [34mspacing:[39;49;00m [34m20[39;49;00m
    68	         [34manchors.bottom:[39;49;00m field.bottom; [34manchors.bottomMargin:[39;49;00m [34m15[39;49;00m
    69
    70	         Image {
    71	             [34msource:[39;49;00m [33m"MinehuntCore/pics/quit.png"[39;49;00m
    72	             [34mscale:[39;49;00m quitMouse.pressed ? [34m0.8[39;49;00m : [34m1.0[39;49;00m
    73	             [34msmooth:[39;49;00m quitMouse.pressed
    74	             [34my:[39;49;00m [34m10[39;49;00m
    75	             MouseArea {
    76	                 [34mid: quitMouse[39;49;00m
    77	                 [34manchors.fill:[39;49;00m parent
    78	                 [34manchors.margins:[39;49;00m -[34m20[39;49;00m
    79	                 [34monClicked:[39;49;00m Qt.quit()
    80	             }
    81	         }
    82	         Column {
    83	             [34mspacing:[39;49;00m [34m2[39;49;00m
    84	             Image { [34msource:[39;49;00m [33m"MinehuntCore/pics/bomb-color.png"[39;49;00m }
    85	             Text { [34manchors.horizontalCenter:[39;49;00m parent.horizontalCenter; [34mcolor:[39;49;00m [33m"white"[39;49;00m; [34mtext:[39;49;00m numMines }
    86	         }
    87
    88	         Column {
    89	             [34mspacing:[39;49;00m [34m2[39;49;00m
    90	             Image { [34msource:[39;49;00m [33m"MinehuntCore/pics/flag-color.png"[39;49;00m }
    91	             Text { [34manchors.horizontalCenter:[39;49;00m parent.horizontalCenter; [34mcolor:[39;49;00m [33m"white"[39;49;00m; [34mtext:[39;49;00m numFlags }
    92	         }
    93	     }
    94
    95	     Image {
    96	         [34manchors.bottom:[39;49;00m field.bottom; [34manchors.bottomMargin:[39;49;00m [34m15[39;49;00m
    97	         [34manchors.right:[39;49;00m field.right; [34manchors.rightMargin:[39;49;00m [34m20[39;49;00m
    98	         [34msource:[39;49;00m isPlaying ? [33m'MinehuntCore/pics/face-smile.png'[39;49;00m :
    99	         hasWon ? [33m'MinehuntCore/pics/face-smile-big.png'[39;49;00m: [33m'MinehuntCore/pics/face-sad.png'[39;49;00m
   100
   101	         MouseArea { [34manchors.fill:[39;49;00m parent; [34monPressed:[39;49;00m reset() }
   102	     }
   103	     Text {
   104	         [34manchors.centerIn:[39;49;00m parent; [34mwidth:[39;49;00m parent.width - [34m20[39;49;00m
   105	         [34mhorizontalAlignment:[39;49;00m Text.AlignHCenter
   106	         [34mwrapMode:[39;49;00m Text.WordWrap
   107	         [34mtext:[39;49;00m [33m"Minehunt demo has to be compiled to run.\n\nPlease see README."[39;49;00m
   108	         [34mcolor:[39;49;00m [33m"white"[39;49;00m; [34mfont.bold:[39;49;00m [34mtrue[39;49;00m; [34mfont.pixelSize:[39;49;00m [34m14[39;49;00m
   109	         [34mvisible:[39;49;00m tiles == [34mundefined[39;49;00m
   110	     }
   111
   112	 }
