 [37m/****************************************************************************[39;49;00m
[37m **[39;49;00m
[37m ** Copyright (C) 2011 Nokia Corporation and/or its subsidiary(-ies).[39;49;00m
[37m ** All rights reserved.[39;49;00m
[37m ** Contact: Nokia Corporation (qt-info@nokia.com)[39;49;00m
[37m **[39;49;00m
[37m ** This file is part of the QtDeclarative module of the Qt Toolkit.[39;49;00m
[37m **[39;49;00m
[37m ** $QT_BEGIN_LICENSE:LGPL$[39;49;00m
[37m ** GNU Lesser General Public License Usage[39;49;00m
[37m ** This file may be used under the terms of the GNU Lesser General Public[39;49;00m
[37m ** License version 2.1 as published by the Free Software Foundation and[39;49;00m
[37m ** appearing in the file LICENSE.LGPL included in the packaging of this[39;49;00m
[37m ** file. Please review the following information to ensure the GNU Lesser[39;49;00m
[37m ** General Public License version 2.1 requirements will be met:[39;49;00m
[37m ** http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.[39;49;00m
[37m **[39;49;00m
[37m ** In addition, as a special exception, Nokia gives you certain additional[39;49;00m
[37m ** rights. These rights are described in the Nokia Qt LGPL Exception[39;49;00m
[37m ** version 1.1, included in the file LGPL_EXCEPTION.txt in this package.[39;49;00m
[37m **[39;49;00m
[37m ** GNU General Public License Usage[39;49;00m
[37m ** Alternatively, this file may be used under the terms of the GNU General[39;49;00m
[37m ** Public License version 3.0 as published by the Free Software Foundation[39;49;00m
[37m ** and appearing in the file LICENSE.GPL included in the packaging of this[39;49;00m
[37m ** file. Please review the following information to ensure the GNU General[39;49;00m
[37m ** Public License version 3.0 requirements will be met:[39;49;00m
[37m ** http://www.gnu.org/copyleft/gpl.html.[39;49;00m
[37m **[39;49;00m
[37m ** Other Usage[39;49;00m
[37m ** Alternatively, this file may be used in accordance with the terms and[39;49;00m
[37m ** conditions contained in a signed written agreement between you and Nokia.[39;49;00m
[37m **[39;49;00m
[37m **[39;49;00m
[37m **[39;49;00m
[37m **[39;49;00m
[37m **[39;49;00m
[37m ** $QT_END_LICENSE$[39;49;00m
[37m **[39;49;00m
[37m ****************************************************************************/[39;49;00m

 [34mimport[39;49;00m QtQuick [34m1.0[39;49;00m
 [34mimport[39;49;00m [33m"MinehuntCore"[39;49;00m [34m1.0[39;49;00m

 Item {
     [34mid: field[39;49;00m
     property [34mint[39;49;00m [34mclickx:[39;49;00m [34m0[39;49;00m
     property [34mint[39;49;00m [34mclicky:[39;49;00m [34m0[39;49;00m

     [34mwidth:[39;49;00m [34m450[39;49;00m; [34mheight:[39;49;00m [34m450[39;49;00m

     Image { [34msource:[39;49;00m [33m"MinehuntCore/pics/background.png"[39;49;00m; [34manchors.fill:[39;49;00m parent; [34mfillMode:[39;49;00m Image.Tile }

     Grid {
         [34manchors.horizontalCenter:[39;49;00m parent.horizontalCenter
         [34mcolumns:[39;49;00m [34m9[39;49;00m; [34mspacing:[39;49;00m [34m1[39;49;00m

         Repeater {
             [34mid: repeater[39;49;00m
             [34mmodel:[39;49;00m tiles
             [34mdelegate:[39;49;00m Tile {}
         }
     }

     Row {
         [34mid: gamedata[39;49;00m
         [34mx:[39;49;00m [34m20[39;49;00m; [34mspacing:[39;49;00m [34m20[39;49;00m
         [34manchors.bottom:[39;49;00m field.bottom; [34manchors.bottomMargin:[39;49;00m [34m15[39;49;00m

         Image {
             [34msource:[39;49;00m [33m"MinehuntCore/pics/quit.png"[39;49;00m
             [34mscale:[39;49;00m quitMouse.pressed ? [34m0.8[39;49;00m : [34m1.0[39;49;00m
             [34msmooth:[39;49;00m quitMouse.pressed
             [34my:[39;49;00m [34m10[39;49;00m
             MouseArea {
                 [34mid: quitMouse[39;49;00m
                 [34manchors.fill:[39;49;00m parent
                 [34manchors.margins:[39;49;00m -[34m20[39;49;00m
                 [34monClicked:[39;49;00m Qt.quit()
             }
         }
         Column {
             [34mspacing:[39;49;00m [34m2[39;49;00m
             Image { [34msource:[39;49;00m [33m"MinehuntCore/pics/bomb-color.png"[39;49;00m }
             Text { [34manchors.horizontalCenter:[39;49;00m parent.horizontalCenter; [34mcolor:[39;49;00m [33m"white"[39;49;00m; [34mtext:[39;49;00m numMines }
         }

         Column {
             [34mspacing:[39;49;00m [34m2[39;49;00m
             Image { [34msource:[39;49;00m [33m"MinehuntCore/pics/flag-color.png"[39;49;00m }
             Text { [34manchors.horizontalCenter:[39;49;00m parent.horizontalCenter; [34mcolor:[39;49;00m [33m"white"[39;49;00m; [34mtext:[39;49;00m numFlags }
         }
     }

     Image {
         [34manchors.bottom:[39;49;00m field.bottom; [34manchors.bottomMargin:[39;49;00m [34m15[39;49;00m
         [34manchors.right:[39;49;00m field.right; [34manchors.rightMargin:[39;49;00m [34m20[39;49;00m
         [34msource:[39;49;00m isPlaying ? [33m'MinehuntCore/pics/face-smile.png'[39;49;00m :
         hasWon ? [33m'MinehuntCore/pics/face-smile-big.png'[39;49;00m: [33m'MinehuntCore/pics/face-sad.png'[39;49;00m

         MouseArea { [34manchors.fill:[39;49;00m parent; [34monPressed:[39;49;00m reset() }
     }
     Text {
         [34manchors.centerIn:[39;49;00m parent; [34mwidth:[39;49;00m parent.width - [34m20[39;49;00m
         [34mhorizontalAlignment:[39;49;00m Text.AlignHCenter
         [34mwrapMode:[39;49;00m Text.WordWrap
         [34mtext:[39;49;00m [33m"Minehunt demo has to be compiled to run.\n\nPlease see README."[39;49;00m
         [34mcolor:[39;49;00m [33m"white"[39;49;00m; [34mfont.bold:[39;49;00m [34mtrue[39;49;00m; [34mfont.pixelSize:[39;49;00m [34m14[39;49;00m
         [34mvisible:[39;49;00m tiles == [34mundefined[39;49;00m
     }

 }
