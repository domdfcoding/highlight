     1^I[37m/***************************************************************************[39;49;00m$
     2^I[37m                    ansigenerator.cpp  -  description[39;49;00m$
     3^I[37m                             -------------------[39;49;00m$
     4^I[37m    begin                : Jul 5 2004[39;49;00m$
     5^I[37m    copyright            : (C) 2004 by André Simon[39;49;00m$
     6^I[37m    email                : andre.simon1@gmx.de[39;49;00m$
     7^I[37m ***************************************************************************/[39;49;00m[37m[39;49;00m$
     8^I[37m[39;49;00m$
     9^I[37m/***************************************************************************[39;49;00m$
    10^I[37m *                                                                         *[39;49;00m$
    11^I[37m *   This program is free software; you can redistribute it and/or modify  *[39;49;00m$
    12^I[37m *   it under the terms of the GNU General Public License as published by  *[39;49;00m$
    13^I[37m *   the Free Software Foundation; either version 2 of the License, or     *[39;49;00m$
    14^I[37m *   (at your option) any later version.                                   *[39;49;00m$
    15^I[37m *                                                                         *[39;49;00m$
    16^I[37m ***************************************************************************/[39;49;00m[37m[39;49;00m$
    17^I[37m[39;49;00m$
    18^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"ansigenerator.h"[39;49;00m[36m[39;49;00m$
    19^I[37m[39;49;00m$
    20^I[34musing[39;49;00m[37m [39;49;00m[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mstd[39;49;00m;[37m[39;49;00m$
    21^I[37m[39;49;00m$
    22^I[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mhighlight[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
    23^I[37m[39;49;00m$
    24^I[37m[39;49;00m$
    25^Istring[37m  [39;49;00m[32mAnsiGenerator::getOpenTag[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring&font,[37m[39;49;00m$
    26^I[37m                                  [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring&fgCol,[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring&bgCol)[37m [39;49;00m{[37m[39;49;00m$
    27^I[37m    [39;49;00mostringstream[37m [39;49;00ms;[37m[39;49;00m$
    28^I[37m    [39;49;00ms[37m  [39;49;00m<<[37m [39;49;00m[33m"[39;49;00m[33m\033[39;49;00m[33m[[39;49;00m[33m"[39;49;00m<<font;[37m[39;49;00m$
    29^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!fgCol.empty())[37m[39;49;00m$
    30^I[37m        [39;49;00ms<<[33m"[39;49;00m[33m;[39;49;00m[33m"[39;49;00m<<fgCol;[37m[39;49;00m$
    31^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!bgCol.empty())[37m[39;49;00m$
    32^I[37m        [39;49;00ms<<[33m"[39;49;00m[33m;[39;49;00m[33m"[39;49;00m<<bgCol;[37m[39;49;00m$
    33^I[37m    [39;49;00ms[37m [39;49;00m<<[37m [39;49;00m[33m"[39;49;00m[33mm[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
    34^I[37m    [39;49;00m[34mreturn[39;49;00m[37m  [39;49;00ms.str();[37m[39;49;00m$
    35^I}[37m[39;49;00m$
    36^I[37m[39;49;00m$
    37^I[37m[39;49;00m$
    38^IAnsiGenerator::AnsiGenerator([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&colourTheme)[37m[39;49;00m$
    39^I[37m        [39;49;00m:[37m [39;49;00mCodeGenerator(colourTheme)[37m [39;49;00m{[37m[39;49;00m$
    40^I[37m    [39;49;00mstyleTagOpen.push_back([33m"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
    41^I[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m31[39;49;00m[33m"[39;49;00m));[37m [39;49;00m[37m//str[39;49;00m$
    42^I[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m34[39;49;00m[33m"[39;49;00m));[37m//number[39;49;00m$
    43^I[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m34[39;49;00m[33m"[39;49;00m));[37m//sl comment[39;49;00m$
    44^I[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m34[39;49;00m[33m"[39;49;00m));[37m//ml comment[39;49;00m$
    45^I[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m35[39;49;00m[33m"[39;49;00m));[37m//escapeChar[39;49;00m$
    46^I[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m35[39;49;00m[33m"[39;49;00m));[37m//directive[39;49;00m$
    47^I[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m01[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m31[39;49;00m[33m"[39;49;00m));[37m//directive string[39;49;00m$
    48^I[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m30[39;49;00m[33m"[39;49;00m));[37m//linenum[39;49;00m$
    49^I[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m01[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m));[37m//symbol[39;49;00m$
    50^I[37m[39;49;00m$
    51^I[37m    [39;49;00mstyleTagClose.push_back([33m"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
    52^I[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi=[34m1[39;49;00m;i<NUMBER_BUILTIN_STYLES;[37m [39;49;00mi++)[37m [39;49;00m{[37m[39;49;00m$
    53^I[37m        [39;49;00mstyleTagClose.push_back([33m"[39;49;00m[33m\033[39;49;00m[33m[m[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
    54^I[37m    [39;49;00m}[37m[39;49;00m$
    55^I[37m    [39;49;00mnewLineTag[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
    56^I[37m    [39;49;00mspacer[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
    57^I}[37m[39;49;00m$
    58^I[37m[39;49;00m$
    59^IAnsiGenerator::AnsiGenerator()[37m [39;49;00m{}[37m[39;49;00m$
    60^IAnsiGenerator::~AnsiGenerator()[37m [39;49;00m{}[37m[39;49;00m$
    61^I[37m[39;49;00m$
    62^Istring[37m [39;49;00mAnsiGenerator::getHeader([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&[37m [39;49;00mtitle)[37m [39;49;00m{[37m[39;49;00m$
    63^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mstring();[37m[39;49;00m$
    64^I}[37m[39;49;00m$
    65^I[37m[39;49;00m$
    66^I[36mvoid[39;49;00m[37m [39;49;00mAnsiGenerator::printBody()[37m [39;49;00m{[37m[39;49;00m$
    67^I[37m    [39;49;00mprocessRootState();[37m[39;49;00m$
    68^I}[37m[39;49;00m$
    69^I[37m[39;49;00m$
    70^Istring[37m [39;49;00mAnsiGenerator::getFooter()[37m [39;49;00m{[37m[39;49;00m$
    71^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mstring();[37m[39;49;00m$
    72^I}[37m[39;49;00m$
    73^I[37m[39;49;00m$
    74^Istring[37m [39;49;00mAnsiGenerator::maskCharacter([36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00mc)[37m [39;49;00m{[37m[39;49;00m$
    75^I[37m    [39;49;00mstring[37m [39;49;00mm;[37m[39;49;00m$
    76^I[37m    [39;49;00mm+=c;[37m[39;49;00m$
    77^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mm;[37m[39;49;00m$
    78^I}[37m[39;49;00m$
    79^I[37m[39;49;00m$
    80^Istring[37m [39;49;00mAnsiGenerator::getMatchingOpenTag([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mstyleID)[37m [39;49;00m{[37m[39;49;00m$
    81^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m(styleID)?getOpenTag([33m"[39;49;00m[33m01[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m32[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m):getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m33[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
    82^I}[37m[39;49;00m$
    83^I[37m[39;49;00m$
    84^Istring[37m [39;49;00mAnsiGenerator::getMatchingCloseTag([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mstyleID)[37m [39;49;00m{[37m[39;49;00m$
    85^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\033[39;49;00m[33m[m[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
    86^I}[37m[39;49;00m$
    87^I[37m[39;49;00m$
    88^I}[37m[39;49;00m$
    89^I[37m/***************************************************************************[39;49;00m$
    90^I[37m                         ansicode.h  -  description[39;49;00m$
    91^I[37m                             -------------------[39;49;00m$
    92^I[37m    begin                : Jul 5 2004[39;49;00m$
    93^I[37m    copyright            : (C) 2004 by Andre Simon[39;49;00m$
    94^I[37m    email                : andre.simon1@gmx.de[39;49;00m$
    95^I[37m ***************************************************************************/[39;49;00m[37m[39;49;00m$
    96^I[37m[39;49;00m$
    97^I[37m/***************************************************************************[39;49;00m$
    98^I[37m *                                                                         *[39;49;00m$
    99^I[37m *   This program is free software; you can redistribute it and/or modify  *[39;49;00m$
   100^I[37m *   it under the terms of the GNU General Public License as published by  *[39;49;00m$
   101^I[37m *   the Free Software Foundation; either version 2 of the License, or     *[39;49;00m$
   102^I[37m *   (at your option) any later version.                                   *[39;49;00m$
   103^I[37m *                                                                         *[39;49;00m$
   104^I[37m ***************************************************************************/[39;49;00m[37m[39;49;00m$
   105^I[37m[39;49;00m$
   106^I[36m#[39;49;00m[36mifndef ANSIGENERATOR_H[39;49;00m[36m[39;49;00m$
   107^I[36m#[39;49;00m[36mdefine ANSIGENERATOR_H[39;49;00m[36m[39;49;00m$
   108^I[37m[39;49;00m$
   109^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<iostream>[39;49;00m[36m[39;49;00m$
   110^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<fstream>[39;49;00m[36m[39;49;00m$
   111^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<string>[39;49;00m[36m[39;49;00m$
   112^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<sstream>[39;49;00m[36m[39;49;00m$
   113^I[37m[39;49;00m$
   114^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"codegenerator.h"[39;49;00m[36m[39;49;00m$
   115^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"charcodes.h"[39;49;00m[36m[39;49;00m$
   116^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"version.h"[39;49;00m[36m[39;49;00m$
   117^I[37m[39;49;00m$
   118^I[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mhighlight[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
   119^I[37m[39;49;00m$
   120^I[37m/**[39;49;00m$
   121^I[37m   \brief This class generates ANSI escape sequences.[39;49;00m$
   122^I[37m[39;49;00m$
   123^I[37m   It contains information about the resulting document structure (document[39;49;00m$
   124^I[37m   header and footer), the colour system, white space handling and text[39;49;00m$
   125^I[37m   formatting attributes.[39;49;00m$
   126^I[37m[39;49;00m$
   127^I[37m* @author Andre Simon[39;49;00m$
   128^I[37m*/[39;49;00m[37m[39;49;00m$
   129^I[37m[39;49;00m$
   130^I[34mclass[39;49;00m[37m [39;49;00m[04m[32mAnsiGenerator[39;49;00m[37m [39;49;00m:[37m [39;49;00m[34mpublic[39;49;00m[37m [39;49;00mhighlight::CodeGenerator[37m[39;49;00m$
   131^I[37m  [39;49;00m{[37m[39;49;00m$
   132^I[37m  [39;49;00m[34mpublic[39;49;00m:[37m[39;49;00m$
   133^I[37m[39;49;00m$
   134^I[37m   [39;49;00m[37m/** Constructor[39;49;00m$
   135^I[37m     \param colourTheme Name of Colour theme to use[39;49;00m$
   136^I[37m    */[39;49;00m[37m[39;49;00m$
   137^I[37m    [39;49;00mAnsiGenerator([37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&colourTheme);[37m[39;49;00m$
   138^I[37m    [39;49;00mAnsiGenerator();[37m[39;49;00m$
   139^I[37m    [39;49;00m~AnsiGenerator();[37m[39;49;00m$
   140^I[37m[39;49;00m$
   141^I[37m   [39;49;00m[37m/** prints document header[39;49;00m$
   142^I[37m       \param  title Title of the document[39;49;00m$
   143^I[37m    */[39;49;00m[37m[39;49;00m$
   144^I[37m    [39;49;00mstring[37m [39;49;00m[32mgetHeader[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&[37m [39;49;00mtitle);[37m[39;49;00m$
   145^I[37m[39;49;00m$
   146^I[37m    [39;49;00m[37m/** Prints document footer*/[39;49;00m[37m[39;49;00m$
   147^I[37m    [39;49;00mstring[37m [39;49;00m[32mgetFooter[39;49;00m();[37m[39;49;00m$
   148^I[37m[39;49;00m$
   149^I[37m    [39;49;00m[37m/** Prints document body*/[39;49;00m[37m[39;49;00m$
   150^I[37m    [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mprintBody[39;49;00m();[37m[39;49;00m$
   151^I[37m[39;49;00m$
   152^I[37m  [39;49;00m[34mprivate[39;49;00m:[37m[39;49;00m$
   153^I[37m[39;49;00m$
   154^I[37m    [39;49;00m[37m/** \return escaped character*/[39;49;00m[37m[39;49;00m$
   155^I[37m    [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00mstring[37m [39;49;00mmaskCharacter([36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m);[37m[39;49;00m$
   156^I[37m[39;49;00m$
   157^I[37m[39;49;00m$
   158^I[37m    [39;49;00m[37m/** gibt ANSI-"Tags" zurueck (Farbindex+bold+kursiv)*/[39;49;00m[37m[39;49;00m$
   159^I[37m    [39;49;00mstring[37m [39;49;00m[32mgetOpenTag[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring&font,[37m[39;49;00m$
   160^I[37m                      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring&fgCol,[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring&bgCol=[33m"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   161^I[37m[39;49;00m$
   162^I[37m[39;49;00m$
   163^I[37m[39;49;00m$
   164^I[37m    [39;49;00mstring[37m [39;49;00m[32mgetMatchingOpenTag[39;49;00m([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mstyleID);[37m[39;49;00m$
   165^I[37m    [39;49;00mstring[37m [39;49;00m[32mgetMatchingCloseTag[39;49;00m([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mstyleID);[37m[39;49;00m$
   166^I[37m  [39;49;00m};[37m[39;49;00m$
   167^I[37m[39;49;00m$
   168^I}[37m[39;49;00m$
   169^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   170^I[37m/*[39;49;00m$
   171^I[37m * Copyright (c) 1998,1999,2000,2001,2002 Tal Davidson. All rights reserved.[39;49;00m$
   172^I[37m *[39;49;00m$
   173^I[37m * ASBeautifier.cpp[39;49;00m$
   174^I[37m * by Tal Davidson (davidsont@bigfoot.com)[39;49;00m$
   175^I[37m * This file is a part of "Artistic Style" - an indentater and reformatter[39;49;00m$
   176^I[37m * of C, C, C# and Java source files.[39;49;00m$
   177^I[37m *[39;49;00m$
   178^I[37m * The "Artistic Style" project, including all files needed to compile it,[39;49;00m$
   179^I[37m * is free software; you can redistribute it and/or use it and/or modify it[39;49;00m$
   180^I[37m * under the terms of the GNU General Public License as published [39;49;00m$
   181^I[37m * by the Free Software Foundation; either version 2 of the License, [39;49;00m$
   182^I[37m * or (at your option) any later version.[39;49;00m$
   183^I[37m *[39;49;00m$
   184^I[37m * This program is distributed in the hope that it will be useful,[39;49;00m$
   185^I[37m * but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m$
   186^I[37m * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.[39;49;00m$
   187^I[37m *[39;49;00m$
   188^I[37m * You should have received a copy of the GNU General Public[39;49;00m$
   189^I[37m * License along with this program.[39;49;00m$
   190^I[37m *[39;49;00m$
   191^I[37m * Patches:[39;49;00m$
   192^I[37m * 18 March 1999 - Brian Rampel -[39;49;00m$
   193^I[37m *       Fixed inverse insertion of spaces vs. tabs when in -t mode.[39;49;00m$
   194^I[37m * 08 may 2004 [39;49;00m$
   195^I[37m *       applied ASBeautifier.cpp.BITFIELD.patch.bz2[39;49;00m$
   196^I[37m */[39;49;00m[37m[39;49;00m$
   197^I[37m[39;49;00m$
   198^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"compiler_defines.h"[39;49;00m[36m[39;49;00m$
   199^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"ASBeautifier.h"[39;49;00m[36m[39;49;00m$
   200^I[37m[39;49;00m$
   201^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<vector>[39;49;00m[36m[39;49;00m$
   202^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<string>[39;49;00m[36m[39;49;00m$
   203^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<cctype>[39;49;00m[36m[39;49;00m$
   204^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<algorithm>[39;49;00m[36m[39;49;00m$
   205^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<iostream>[39;49;00m[36m[39;49;00m$
   206^I[37m[39;49;00m$
   207^I[37m[39;49;00m$
   208^I[36m#[39;49;00m[36mdefine INIT_CONTAINER(container, value)     {if ( (container) != NULL ) delete (container); (container) = (value); }[39;49;00m[36m[39;49;00m$
   209^I[36m#[39;49;00m[36mdefine DELETE_CONTAINER(container)          {if ( (container) != NULL ) delete (container) ; }[39;49;00m[36m[39;49;00m$
   210^I[37m[39;49;00m$
   211^I[36m#[39;49;00m[36mifdef USES_NAMESPACE[39;49;00m[36m[39;49;00m$
   212^I[34musing[39;49;00m[37m [39;49;00m[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mstd[39;49;00m;[37m[39;49;00m$
   213^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   214^I[37m[39;49;00m$
   215^I[37m[39;49;00m$
   216^I[37m[39;49;00m$
   217^I[37m[39;49;00m$
   218^I[36m#[39;49;00m[36mifdef USES_NAMESPACE[39;49;00m[36m[39;49;00m$
   219^I[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mastyle[39;49;00m[37m[39;49;00m$
   220^I[37m  [39;49;00m{[37m[39;49;00m$
   221^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   222^I[37m[39;49;00m$
   223^I[37m  [39;49;00m[36mbool[39;49;00m[37m [39;49;00mASBeautifier::calledInitStatic[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   224^I[37m[39;49;00m$
   225^I[37m  [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mASBeautifier::headers;[37m[39;49;00m$
   226^I[37m  [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mASBeautifier::nonParenHeaders;[37m[39;49;00m$
   227^I[37m  [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mASBeautifier::preBlockStatements;[37m[39;49;00m$
   228^I[37m  [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mASBeautifier::assignmentOperators;[37m[39;49;00m$
   229^I[37m  [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mASBeautifier::nonAssignmentOperators;[37m[39;49;00m$
   230^I[37m[39;49;00m$
   231^I[37m  [39;49;00m[37m/*[39;49;00m$
   232^I[37m   * initialize the static vars[39;49;00m$
   233^I[37m   */[39;49;00m[37m[39;49;00m$
   234^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mASBeautifier::initStatic[39;49;00m()[37m[39;49;00m$
   235^I[37m  [39;49;00m{[37m[39;49;00m$
   236^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(calledInitStatic)[37m[39;49;00m$
   237^I[37m      [39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
   238^I[37m[39;49;00m$
   239^I[37m    [39;49;00mcalledInitStatic[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
   240^I[37m[39;49;00m$
   241^I[37m    [39;49;00mheaders.push_back(&AS_IF);[37m[39;49;00m$
   242^I[37m    [39;49;00mheaders.push_back(&AS_ELSE);[37m[39;49;00m$
   243^I[37m    [39;49;00mheaders.push_back(&AS_FOR);[37m[39;49;00m$
   244^I[37m    [39;49;00mheaders.push_back(&AS_WHILE);[37m[39;49;00m$
   245^I[37m    [39;49;00mheaders.push_back(&AS_DO);[37m[39;49;00m$
   246^I[37m    [39;49;00mheaders.push_back(&AS_TRY);[37m[39;49;00m$
   247^I[37m    [39;49;00mheaders.push_back(&AS_CATCH);[37m[39;49;00m$
   248^I[37m    [39;49;00mheaders.push_back(&AS_FINALLY);[37m[39;49;00m$
   249^I[37m    [39;49;00mheaders.push_back(&AS_SYNCHRONIZED);[37m[39;49;00m$
   250^I[37m    [39;49;00mheaders.push_back(&AS_SWITCH);[37m[39;49;00m$
   251^I[37m    [39;49;00mheaders.push_back(&AS_CASE);[37m[39;49;00m$
   252^I[37m    [39;49;00mheaders.push_back(&AS_DEFAULT);[37m[39;49;00m$
   253^I[37m    [39;49;00mheaders.push_back(&AS_FOREACH);[37m[39;49;00m$
   254^I[37m    [39;49;00mheaders.push_back(&AS_LOCK);[37m[39;49;00m$
   255^I[37m    [39;49;00mheaders.push_back(&AS_UNSAFE);[37m[39;49;00m$
   256^I[37m    [39;49;00mheaders.push_back(&AS_FIXED);[37m[39;49;00m$
   257^I[37m    [39;49;00mheaders.push_back(&AS_GET);[37m[39;49;00m$
   258^I[37m    [39;49;00mheaders.push_back(&AS_SET);[37m[39;49;00m$
   259^I[37m    [39;49;00mheaders.push_back(&AS_ADD);[37m[39;49;00m$
   260^I[37m    [39;49;00mheaders.push_back(&AS_REMOVE);[37m[39;49;00m$
   261^I[37m    [39;49;00m[37m//headers.push_back(&AS_PUBLIC);[39;49;00m$
   262^I[37m    [39;49;00m[37m//headers.push_back(&AS_PRIVATE);[39;49;00m$
   263^I[37m    [39;49;00m[37m//headers.push_back(&AS_PROTECTED);[39;49;00m$
   264^I[37m[39;49;00m$
   265^I[37m    [39;49;00m[37m//headers.push_back(&AS_OPERATOR);[39;49;00m$
   266^I[37m    [39;49;00mheaders.push_back(&AS_TEMPLATE);[37m[39;49;00m$
   267^I[37m    [39;49;00mheaders.push_back(&AS_CONST);[37m[39;49;00m$
   268^I[37m    [39;49;00m[37m/**/[39;49;00m[37m[39;49;00m$
   269^I[37m    [39;49;00mheaders.push_back(&AS_STATIC);[37m[39;49;00m$
   270^I[37m    [39;49;00mheaders.push_back(&AS_EXTERN);[37m[39;49;00m$
   271^I[37m[39;49;00m$
   272^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_ELSE);[37m[39;49;00m$
   273^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_DO);[37m[39;49;00m$
   274^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_TRY);[37m[39;49;00m$
   275^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_FINALLY);[37m[39;49;00m$
   276^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_STATIC);[37m[39;49;00m$
   277^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_CONST);[37m[39;49;00m$
   278^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_EXTERN);[37m[39;49;00m$
   279^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_CASE);[37m[39;49;00m$
   280^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_DEFAULT);[37m[39;49;00m$
   281^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_UNSAFE);[37m[39;49;00m$
   282^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_GET);[37m[39;49;00m$
   283^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_SET);[37m[39;49;00m$
   284^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_ADD);[37m[39;49;00m$
   285^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_REMOVE);[37m[39;49;00m$
   286^I[37m[39;49;00m$
   287^I[37m[39;49;00m$
   288^I[37m[39;49;00m$
   289^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_PUBLIC);[37m[39;49;00m$
   290^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_PRIVATE);[37m[39;49;00m$
   291^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_PROTECTED);[37m[39;49;00m$
   292^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_TEMPLATE);[37m[39;49;00m$
   293^I[37m    [39;49;00mnonParenHeaders.push_back(&AS_CONST);[37m[39;49;00m$
   294^I[37m    [39;49;00m[37m///    nonParenHeaders.push_back(&AS_ASM);[39;49;00m$
   295^I[37m[39;49;00m$
   296^I[37m    [39;49;00mpreBlockStatements.push_back(&AS_CLASS);[37m[39;49;00m$
   297^I[37m    [39;49;00mpreBlockStatements.push_back(&AS_STRUCT);[37m[39;49;00m$
   298^I[37m    [39;49;00mpreBlockStatements.push_back(&AS_UNION);[37m[39;49;00m$
   299^I[37m    [39;49;00mpreBlockStatements.push_back(&AS_INTERFACE);[37m[39;49;00m$
   300^I[37m    [39;49;00mpreBlockStatements.push_back(&AS_NAMESPACE);[37m[39;49;00m$
   301^I[37m    [39;49;00mpreBlockStatements.push_back(&AS_THROWS);[37m[39;49;00m$
   302^I[37m    [39;49;00mpreBlockStatements.push_back(&AS_EXTERN);[37m[39;49;00m$
   303^I[37m[39;49;00m$
   304^I[37m    [39;49;00massignmentOperators.push_back(&AS_ASSIGN);[37m[39;49;00m$
   305^I[37m    [39;49;00massignmentOperators.push_back(&AS_PLUS_ASSIGN);[37m[39;49;00m$
   306^I[37m    [39;49;00massignmentOperators.push_back(&AS_MINUS_ASSIGN);[37m[39;49;00m$
   307^I[37m    [39;49;00massignmentOperators.push_back(&AS_MULT_ASSIGN);[37m[39;49;00m$
   308^I[37m    [39;49;00massignmentOperators.push_back(&AS_DIV_ASSIGN);[37m[39;49;00m$
   309^I[37m    [39;49;00massignmentOperators.push_back(&AS_MOD_ASSIGN);[37m[39;49;00m$
   310^I[37m    [39;49;00massignmentOperators.push_back(&AS_OR_ASSIGN);[37m[39;49;00m$
   311^I[37m    [39;49;00massignmentOperators.push_back(&AS_AND_ASSIGN);[37m[39;49;00m$
   312^I[37m    [39;49;00massignmentOperators.push_back(&AS_XOR_ASSIGN);[37m[39;49;00m$
   313^I[37m    [39;49;00massignmentOperators.push_back(&AS_GR_GR_GR_ASSIGN);[37m[39;49;00m$
   314^I[37m    [39;49;00massignmentOperators.push_back(&AS_GR_GR_ASSIGN);[37m[39;49;00m$
   315^I[37m    [39;49;00massignmentOperators.push_back(&AS_LS_LS_LS_ASSIGN);[37m[39;49;00m$
   316^I[37m    [39;49;00massignmentOperators.push_back(&AS_LS_LS_ASSIGN);[37m[39;49;00m$
   317^I[37m[39;49;00m$
   318^I[37m    [39;49;00massignmentOperators.push_back(&AS_RETURN);[37m[39;49;00m$
   319^I[37m[39;49;00m$
   320^I[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_EQUAL);[37m[39;49;00m$
   321^I[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_PLUS_PLUS);[37m[39;49;00m$
   322^I[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_MINUS_MINUS);[37m[39;49;00m$
   323^I[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_NOT_EQUAL);[37m[39;49;00m$
   324^I[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_GR_EQUAL);[37m[39;49;00m$
   325^I[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_GR_GR_GR);[37m[39;49;00m$
   326^I[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_GR_GR);[37m[39;49;00m$
   327^I[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_LS_EQUAL);[37m[39;49;00m$
   328^I[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_LS_LS_LS);[37m[39;49;00m$
   329^I[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_LS_LS);[37m[39;49;00m$
   330^I[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_ARROW);[37m[39;49;00m$
   331^I[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_AND);[37m[39;49;00m$
   332^I[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_OR);[37m[39;49;00m$
   333^I[37m  [39;49;00m}[37m[39;49;00m$
   334^I[37m[39;49;00m$
   335^I[37m  [39;49;00m[37m/**[39;49;00m$
   336^I[37m   * ASBeautifier's constructor[39;49;00m$
   337^I[37m   */[39;49;00m[37m[39;49;00m$
   338^I[37m  [39;49;00mASBeautifier::ASBeautifier()[37m[39;49;00m$
   339^I[37m  [39;49;00m{[37m[39;49;00m$
   340^I[37m    [39;49;00minitStatic();[37m[39;49;00m$
   341^I[37m[39;49;00m$
   342^I[37m    [39;49;00mwaitingBeautifierStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   343^I[37m    [39;49;00mactiveBeautifierStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   344^I[37m    [39;49;00mwaitingBeautifierStackLengthStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   345^I[37m    [39;49;00mactiveBeautifierStackLengthStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   346^I[37m[39;49;00m$
   347^I[37m    [39;49;00mheaderStack[37m  [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   348^I[37m    [39;49;00mtempStacks[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   349^I[37m    [39;49;00mblockParenDepthStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   350^I[37m    [39;49;00mblockStatementStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   351^I[37m    [39;49;00mparenStatementStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   352^I[37m    [39;49;00mbracketBlockStateStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   353^I[37m    [39;49;00minStatementIndentStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   354^I[37m    [39;49;00minStatementIndentStackSizeStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   355^I[37m    [39;49;00mparenIndentStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   356^I[37m    [39;49;00msourceIterator[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   357^I[37m[39;49;00m$
   358^I[37m    [39;49;00misMinimalConditinalIndentSet[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   359^I[37m    [39;49;00mshouldForceTabIndentation[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   360^I[37m[39;49;00m$
   361^I[37m    [39;49;00msetSpaceIndentation([34m4[39;49;00m);[37m[39;49;00m$
   362^I[37m    [39;49;00msetMaxInStatementIndentLength([34m40[39;49;00m);[37m[39;49;00m$
   363^I[37m    [39;49;00msetClassIndent([36mfalse[39;49;00m);[37m[39;49;00m$
   364^I[37m    [39;49;00msetSwitchIndent([36mfalse[39;49;00m);[37m[39;49;00m$
   365^I[37m    [39;49;00msetCaseIndent([36mfalse[39;49;00m);[37m[39;49;00m$
   366^I[37m    [39;49;00msetBlockIndent([36mfalse[39;49;00m);[37m[39;49;00m$
   367^I[37m    [39;49;00msetBracketIndent([36mfalse[39;49;00m);[37m[39;49;00m$
   368^I[37m    [39;49;00msetNamespaceIndent([36mfalse[39;49;00m);[37m[39;49;00m$
   369^I[37m    [39;49;00msetLabelIndent([36mfalse[39;49;00m);[37m[39;49;00m$
   370^I[37m    [39;49;00msetEmptyLineFill([36mfalse[39;49;00m);[37m[39;49;00m$
   371^I[37m    [39;49;00msetCStyle();[37m[39;49;00m$
   372^I[37m    [39;49;00msetPreprocessorIndent([36mfalse[39;49;00m);[37m[39;49;00m$
   373^I[37m  [39;49;00m}[37m[39;49;00m$
   374^I[37m[39;49;00m$
   375^I[37m  [39;49;00mASBeautifier::ASBeautifier([34mconst[39;49;00m[37m [39;49;00mASBeautifier[37m [39;49;00m&other)[37m[39;49;00m$
   376^I[37m  [39;49;00m{[37m[39;49;00m$
   377^I[37m    [39;49;00mwaitingBeautifierStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   378^I[37m    [39;49;00mactiveBeautifierStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   379^I[37m    [39;49;00mwaitingBeautifierStackLengthStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   380^I[37m    [39;49;00mactiveBeautifierStackLengthStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   381^I[37m[39;49;00m$
   382^I[37m    [39;49;00mheaderStack[37m  [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>;[37m[39;49;00m$
   383^I[37m    [39;49;00m*headerStack[37m [39;49;00m=[37m [39;49;00m*other.headerStack;[37m[39;49;00m$
   384^I[37m[39;49;00m$
   385^I[37m    [39;49;00mtempStacks[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>*[37m [39;49;00m>;[37m[39;49;00m$
   386^I[37m    [39;49;00mvector<[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>*[37m [39;49;00m>::iterator[37m [39;49;00miter;[37m[39;49;00m$
   387^I[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(iter[37m [39;49;00m=[37m [39;49;00mother.tempStacks->begin();[37m[39;49;00m$
   388^I[37m         [39;49;00miter[37m [39;49;00m!=[37m [39;49;00mother.tempStacks->end();[37m[39;49;00m$
   389^I[37m         [39;49;00m++iter)[37m[39;49;00m$
   390^I[37m      [39;49;00m{[37m[39;49;00m$
   391^I[37m        [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m*newVec[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>;[37m[39;49;00m$
   392^I[37m        [39;49;00m*newVec[37m [39;49;00m=[37m [39;49;00m**iter;[37m[39;49;00m$
   393^I[37m        [39;49;00mtempStacks->push_back(newVec);[37m[39;49;00m$
   394^I[37m      [39;49;00m}[37m[39;49;00m$
   395^I[37m    [39;49;00mblockParenDepthStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>;[37m[39;49;00m$
   396^I[37m    [39;49;00m*blockParenDepthStack[37m [39;49;00m=[37m [39;49;00m*other.blockParenDepthStack;[37m[39;49;00m$
   397^I[37m[39;49;00m$
   398^I[37m    [39;49;00mblockStatementStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>;[37m[39;49;00m$
   399^I[37m    [39;49;00m*blockStatementStack[37m [39;49;00m=[37m [39;49;00m*other.blockStatementStack;[37m[39;49;00m$
   400^I[37m[39;49;00m$
   401^I[37m    [39;49;00mparenStatementStack[37m [39;49;00m=[37m  [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>;[37m[39;49;00m$
   402^I[37m    [39;49;00m*parenStatementStack[37m [39;49;00m=[37m [39;49;00m*other.parenStatementStack;[37m[39;49;00m$
   403^I[37m[39;49;00m$
   404^I[37m    [39;49;00mbracketBlockStateStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>;[37m[39;49;00m$
   405^I[37m    [39;49;00m*bracketBlockStateStack[37m [39;49;00m=[37m [39;49;00m*other.bracketBlockStateStack;[37m[39;49;00m$
   406^I[37m[39;49;00m$
   407^I[37m    [39;49;00minStatementIndentStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>;[37m[39;49;00m$
   408^I[37m    [39;49;00m*inStatementIndentStack[37m [39;49;00m=[37m [39;49;00m*other.inStatementIndentStack;[37m[39;49;00m$
   409^I[37m[39;49;00m$
   410^I[37m    [39;49;00minStatementIndentStackSizeStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>;[37m[39;49;00m$
   411^I[37m    [39;49;00m*inStatementIndentStackSizeStack[37m [39;49;00m=[37m [39;49;00m*other.inStatementIndentStackSizeStack;[37m[39;49;00m$
   412^I[37m[39;49;00m$
   413^I[37m    [39;49;00mparenIndentStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>;[37m[39;49;00m$
   414^I[37m    [39;49;00m*parenIndentStack[37m [39;49;00m=[37m [39;49;00m*other.parenIndentStack;[37m[39;49;00m$
   415^I[37m[39;49;00m$
   416^I[37m    [39;49;00msourceIterator[37m [39;49;00m=[37m [39;49;00mother.sourceIterator;[37m[39;49;00m$
   417^I[37m[39;49;00m$
   418^I[37m    [39;49;00mindentString[37m [39;49;00m=[37m [39;49;00mother.indentString;[37m[39;49;00m$
   419^I[37m    [39;49;00mcurrentHeader[37m [39;49;00m=[37m [39;49;00mother.currentHeader;[37m[39;49;00m$
   420^I[37m    [39;49;00mpreviousLastLineHeader[37m [39;49;00m=[37m [39;49;00mother.previousLastLineHeader;[37m[39;49;00m$
   421^I[37m    [39;49;00mimmediatelyPreviousAssignmentOp[37m [39;49;00m=[37m [39;49;00mother.immediatelyPreviousAssignmentOp;[37m[39;49;00m$
   422^I[37m    [39;49;00misInQuote[37m [39;49;00m=[37m [39;49;00mother.isInQuote;[37m[39;49;00m$
   423^I[37m    [39;49;00misInComment[37m [39;49;00m=[37m [39;49;00mother.isInComment;[37m[39;49;00m$
   424^I[37m    [39;49;00misInCase[37m [39;49;00m=[37m [39;49;00mother.isInCase;[37m[39;49;00m$
   425^I[37m    [39;49;00misInQuestion[37m [39;49;00m=[37m [39;49;00mother.isInQuestion;[37m[39;49;00m$
   426^I[37m    [39;49;00misInStatement[37m [39;49;00m=other.[37m [39;49;00misInStatement;[37m[39;49;00m$
   427^I[37m    [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00mother.isInHeader;[37m[39;49;00m$
   428^I[37m    [39;49;00misCStyle[37m [39;49;00m=[37m [39;49;00mother.isCStyle;[37m[39;49;00m$
   429^I[37m    [39;49;00misInOperator[37m [39;49;00m=[37m [39;49;00mother.isInOperator;[37m[39;49;00m$
   430^I[37m    [39;49;00misInTemplate[37m [39;49;00m=[37m [39;49;00mother.isInTemplate;[37m[39;49;00m$
   431^I[37m    [39;49;00misInConst[37m [39;49;00m=[37m [39;49;00mother.isInConst;[37m[39;49;00m$
   432^I[37m    [39;49;00mclassIndent[37m [39;49;00m=[37m [39;49;00mother.classIndent;[37m[39;49;00m$
   433^I[37m    [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00mother.isInClassHeader;[37m[39;49;00m$
   434^I[37m    [39;49;00misInClassHeaderTab[37m [39;49;00m=[37m [39;49;00mother.isInClassHeaderTab;[37m[39;49;00m$
   435^I[37m    [39;49;00mswitchIndent[37m [39;49;00m=[37m [39;49;00mother.switchIndent;[37m[39;49;00m$
   436^I[37m    [39;49;00mcaseIndent[37m [39;49;00m=[37m [39;49;00mother.caseIndent;[37m[39;49;00m$
   437^I[37m    [39;49;00mnamespaceIndent[37m [39;49;00m=[37m [39;49;00mother.namespaceIndent;[37m[39;49;00m$
   438^I[37m    [39;49;00mbracketIndent[37m [39;49;00m=[37m [39;49;00mother.bracketIndent;[37m[39;49;00m$
   439^I[37m    [39;49;00mblockIndent[37m [39;49;00m=[37m [39;49;00mother.blockIndent;[37m[39;49;00m$
   440^I[37m    [39;49;00mlabelIndent[37m [39;49;00m=[37m [39;49;00mother.labelIndent;[37m[39;49;00m$
   441^I[37m    [39;49;00mpreprocessorIndent[37m [39;49;00m=[37m [39;49;00mother.preprocessorIndent;[37m[39;49;00m$
   442^I[37m    [39;49;00mparenDepth[37m [39;49;00m=[37m [39;49;00mother.parenDepth;[37m[39;49;00m$
   443^I[37m    [39;49;00mindentLength[37m [39;49;00m=[37m [39;49;00mother.indentLength;[37m[39;49;00m$
   444^I[37m    [39;49;00mblockTabCount[37m [39;49;00m=[37m [39;49;00mother.blockTabCount;[37m[39;49;00m$
   445^I[37m    [39;49;00mleadingWhiteSpaces[37m [39;49;00m=[37m [39;49;00mother.leadingWhiteSpaces;[37m[39;49;00m$
   446^I[37m    [39;49;00mmaxInStatementIndent[37m [39;49;00m=[37m [39;49;00mother.maxInStatementIndent;[37m[39;49;00m$
   447^I[37m    [39;49;00mtemplateDepth[37m [39;49;00m=[37m [39;49;00mother.templateDepth;[37m[39;49;00m$
   448^I[37m    [39;49;00mquoteChar[37m [39;49;00m=[37m [39;49;00mother.quoteChar;[37m[39;49;00m$
   449^I[37m    [39;49;00mprevNonSpaceCh[37m [39;49;00m=[37m [39;49;00mother.prevNonSpaceCh;[37m[39;49;00m$
   450^I[37m    [39;49;00mcurrentNonSpaceCh[37m [39;49;00m=[37m [39;49;00mother.currentNonSpaceCh;[37m[39;49;00m$
   451^I[37m    [39;49;00mcurrentNonLegalCh[37m [39;49;00m=[37m [39;49;00mother.currentNonLegalCh;[37m[39;49;00m$
   452^I[37m    [39;49;00mprevNonLegalCh[37m [39;49;00m=[37m [39;49;00mother.prevNonLegalCh;[37m[39;49;00m$
   453^I[37m    [39;49;00misInConditional[37m [39;49;00m=[37m [39;49;00mother.isInConditional;[37m[39;49;00m$
   454^I[37m    [39;49;00mminConditionalIndent[37m [39;49;00m=[37m [39;49;00mother.minConditionalIndent;[37m[39;49;00m$
   455^I[37m    [39;49;00mprevFinalLineSpaceTabCount[37m [39;49;00m=[37m [39;49;00mother.prevFinalLineSpaceTabCount;[37m[39;49;00m$
   456^I[37m    [39;49;00mprevFinalLineTabCount[37m [39;49;00m=[37m [39;49;00mother.prevFinalLineTabCount;[37m[39;49;00m$
   457^I[37m    [39;49;00memptyLineFill[37m [39;49;00m=[37m [39;49;00mother.emptyLineFill;[37m[39;49;00m$
   458^I[37m    [39;49;00mprobationHeader[37m [39;49;00m=[37m [39;49;00mother.probationHeader;[37m[39;49;00m$
   459^I[37m    [39;49;00misInDefine[37m [39;49;00m=[37m [39;49;00mother.isInDefine;[37m[39;49;00m$
   460^I[37m    [39;49;00misInDefineDefinition[37m [39;49;00m=[37m [39;49;00mother.isInDefineDefinition;[37m[39;49;00m$
   461^I[37m    [39;49;00mbackslashEndsPrevLine[37m [39;49;00m=[37m [39;49;00mother.backslashEndsPrevLine;[37m[39;49;00m$
   462^I[37m    [39;49;00mdefineTabCount[37m [39;49;00m=[37m [39;49;00mother.defineTabCount;[37m[39;49;00m$
   463^I[37m  [39;49;00m}[37m[39;49;00m$
   464^I[37m[39;49;00m$
   465^I[37m  [39;49;00m[37m/**[39;49;00m$
   466^I[37m   * ASBeautifier's destructor[39;49;00m$
   467^I[37m   */[39;49;00m[37m[39;49;00m$
   468^I[37m  [39;49;00mASBeautifier::~ASBeautifier()[37m[39;49;00m$
   469^I[37m  [39;49;00m{[37m[39;49;00m$
   470^I[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mheaderStack[37m [39;49;00m);[37m[39;49;00m$
   471^I[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mtempStacks[37m [39;49;00m);[37m[39;49;00m$
   472^I[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mblockParenDepthStack[37m [39;49;00m);[37m[39;49;00m$
   473^I[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mblockStatementStack[37m [39;49;00m);[37m[39;49;00m$
   474^I[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mparenStatementStack[37m [39;49;00m);[37m[39;49;00m$
   475^I[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mbracketBlockStateStack[37m [39;49;00m);[37m[39;49;00m$
   476^I[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00minStatementIndentStack[37m [39;49;00m);[37m[39;49;00m$
   477^I[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00minStatementIndentStackSizeStack[37m [39;49;00m);[37m[39;49;00m$
   478^I[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mparenIndentStack[37m [39;49;00m);[37m[39;49;00m$
   479^I[37m[39;49;00m$
   480^I[37m    [39;49;00m[37m// DELETE_CONTAINER( sourceIterator );[39;49;00m$
   481^I[37m  [39;49;00m}[37m[39;49;00m$
   482^I[37m[39;49;00m$
   483^I[37m  [39;49;00m[37m/**[39;49;00m$
   484^I[37m   * initialize the ASBeautifier.[39;49;00m$
   485^I[37m   *[39;49;00m$
   486^I[37m   * init() should be called every time a ABeautifier object is to start[39;49;00m$
   487^I[37m   * beautifying a NEW source file.[39;49;00m$
   488^I[37m   * init() recieves a pointer to a DYNAMICALLY CREATED ASSourceIterator object[39;49;00m$
   489^I[37m   * that will be used to iterate through the source code. This object will be[39;49;00m$
   490^I[37m   * deleted during the ASBeautifier's destruction, and thus should not be[39;49;00m$
   491^I[37m   * deleted elsewhere.[39;49;00m$
   492^I[37m   *[39;49;00m$
   493^I[37m   * @param iter     a pointer to the DYNAMICALLY CREATED ASSourceIterator object.[39;49;00m$
   494^I[37m   */[39;49;00m[37m[39;49;00m$
   495^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::init(ASSourceIterator[37m [39;49;00m*iter)[37m[39;49;00m$
   496^I[37m[39;49;00m$
   497^I[37m  [39;49;00m{[37m[39;49;00m$
   498^I[37m    [39;49;00msourceIterator[37m [39;49;00m=[37m [39;49;00miter;[37m[39;49;00m$
   499^I[37m    [39;49;00minit();[37m[39;49;00m$
   500^I[37m  [39;49;00m}[37m[39;49;00m$
   501^I[37m[39;49;00m$
   502^I[37m  [39;49;00m[37m/**[39;49;00m$
   503^I[37m   * initialize the ASBeautifier.[39;49;00m$
   504^I[37m   */[39;49;00m[37m[39;49;00m$
   505^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::init()[37m[39;49;00m$
   506^I[37m  [39;49;00m{[37m[39;49;00m$
   507^I[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mwaitingBeautifierStack,[37m  [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<ASBeautifier*>[37m [39;49;00m);[37m[39;49;00m$
   508^I[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mactiveBeautifierStack,[37m  [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<ASBeautifier*>[37m [39;49;00m);[37m[39;49;00m$
   509^I[37m[39;49;00m$
   510^I[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mwaitingBeautifierStackLengthStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   511^I[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mactiveBeautifierStackLengthStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   512^I[37m[39;49;00m$
   513^I[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mheaderStack,[37m  [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m);[37m[39;49;00m$
   514^I[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mtempStacks,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>*[37m [39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   515^I[37m    [39;49;00mtempStacks->push_back([34mnew[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>);[37m[39;49;00m$
   516^I[37m[39;49;00m$
   517^I[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mblockParenDepthStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   518^I[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mblockStatementStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   519^I[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mparenStatementStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   520^I[37m[39;49;00m$
   521^I[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mbracketBlockStateStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   522^I[37m    [39;49;00mbracketBlockStateStack->push_back([36mtrue[39;49;00m);[37m[39;49;00m$
   523^I[37m[39;49;00m$
   524^I[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00minStatementIndentStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   525^I[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00minStatementIndentStackSizeStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   526^I[37m    [39;49;00minStatementIndentStackSizeStack->push_back([34m0[39;49;00m);[37m[39;49;00m$
   527^I[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mparenIndentStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   528^I[37m[39;49;00m$
   529^I[37m    [39;49;00mimmediatelyPreviousAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   530^I[37m    [39;49;00mpreviousLastLineHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   531^I[37m[39;49;00m$
   532^I[37m    [39;49;00misInQuote[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   533^I[37m    [39;49;00misInComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   534^I[37m    [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   535^I[37m    [39;49;00misInCase[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   536^I[37m    [39;49;00misInQuestion[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   537^I[37m    [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   538^I[37m    [39;49;00misInClassHeaderTab[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   539^I[37m    [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   540^I[37m    [39;49;00misInOperator[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   541^I[37m    [39;49;00misInTemplate[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   542^I[37m    [39;49;00misInConst[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   543^I[37m    [39;49;00misInConditional[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   544^I[37m    [39;49;00mtemplateDepth[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   545^I[37m    [39;49;00mparenDepth=[34m0[39;49;00m;[37m[39;49;00m$
   546^I[37m    [39;49;00mblockTabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   547^I[37m    [39;49;00mleadingWhiteSpaces[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   548^I[37m    [39;49;00mprevNonSpaceCh[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
   549^I[37m    [39;49;00mcurrentNonSpaceCh[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
   550^I[37m    [39;49;00mprevNonLegalCh[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
   551^I[37m    [39;49;00mcurrentNonLegalCh[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
   552^I[37m    [39;49;00mprevFinalLineSpaceTabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   553^I[37m    [39;49;00mprevFinalLineTabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   554^I[37m    [39;49;00mprobationHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   555^I[37m    [39;49;00mbackslashEndsPrevLine[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   556^I[37m    [39;49;00misInDefine[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   557^I[37m    [39;49;00misInDefineDefinition[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   558^I[37m    [39;49;00mdefineTabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   559^I[37m  [39;49;00m}[37m[39;49;00m$
   560^I[37m[39;49;00m$
   561^I[37m  [39;49;00m[37m/**[39;49;00m$
   562^I[37m   * set indentation style to ANSI C/C++.  [39;49;00m$
   563^I[37m   */[39;49;00m[37m[39;49;00m$
   564^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setCStyle()[37m[39;49;00m$
   565^I[37m  [39;49;00m{[37m[39;49;00m$
   566^I[37m    [39;49;00misCStyle[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
   567^I[37m  [39;49;00m}[37m[39;49;00m$
   568^I[37m[39;49;00m$
   569^I[37m  [39;49;00m[37m/**[39;49;00m$
   570^I[37m   * set indentation style to Java / K&R.  [39;49;00m$
   571^I[37m   */[39;49;00m[37m[39;49;00m$
   572^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setJavaStyle()[37m[39;49;00m$
   573^I[37m  [39;49;00m{[37m[39;49;00m$
   574^I[37m    [39;49;00misCStyle[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   575^I[37m  [39;49;00m}[37m[39;49;00m$
   576^I[37m[39;49;00m$
   577^I[37m  [39;49;00m[37m/**[39;49;00m$
   578^I[37m   * indent using one tab per indentation[39;49;00m$
   579^I[37m   */[39;49;00m[37m[39;49;00m$
   580^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setTabIndentation([36mint[39;49;00m[37m [39;49;00mlength,[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mforceTabs)[37m[39;49;00m$
   581^I[37m  [39;49;00m{[37m[39;49;00m$
   582^I[37m    [39;49;00mindentString[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m\t[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   583^I[37m    [39;49;00mindentLength[37m [39;49;00m=[37m [39;49;00mlength;[37m[39;49;00m$
   584^I[37m    [39;49;00mshouldForceTabIndentation[37m [39;49;00m=[37m [39;49;00mforceTabs;[37m[39;49;00m$
   585^I[37m[39;49;00m$
   586^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isMinimalConditinalIndentSet)[37m[39;49;00m$
   587^I[37m      [39;49;00mminConditionalIndent[37m [39;49;00m=[37m [39;49;00mindentLength[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m$
   588^I[37m  [39;49;00m}[37m[39;49;00m$
   589^I[37m[39;49;00m$
   590^I[37m  [39;49;00m[37m/**[39;49;00m$
   591^I[37m   [39;49;00m$
   592^I[37m   * indent using a number of spaces per indentation.[39;49;00m$
   593^I[37m   *[39;49;00m$
   594^I[37m   * @param   length     number of spaces per indent.[39;49;00m$
   595^I[37m   */[39;49;00m[37m[39;49;00m$
   596^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setSpaceIndentation([36mint[39;49;00m[37m [39;49;00mlength)[37m[39;49;00m$
   597^I[37m  [39;49;00m{[37m[39;49;00m$
   598^I[37m    [39;49;00mindentString=string(length,[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
   599^I[37m    [39;49;00mindentLength[37m [39;49;00m=[37m [39;49;00mlength;[37m[39;49;00m$
   600^I[37m[39;49;00m$
   601^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isMinimalConditinalIndentSet)[37m[39;49;00m$
   602^I[37m      [39;49;00mminConditionalIndent[37m [39;49;00m=[37m [39;49;00mindentLength[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m$
   603^I[37m  [39;49;00m}[37m[39;49;00m$
   604^I[37m[39;49;00m$
   605^I[37m  [39;49;00m[37m/**[39;49;00m$
   606^I[37m   * set the maximum indentation between two lines in a multi-line statement.[39;49;00m$
   607^I[37m   *[39;49;00m$
   608^I[37m   * @param   max     maximum indentation length.[39;49;00m$
   609^I[37m   */[39;49;00m[37m[39;49;00m$
   610^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setMaxInStatementIndentLength([36mint[39;49;00m[37m [39;49;00mmax)[37m[39;49;00m$
   611^I[37m  [39;49;00m{[37m[39;49;00m$
   612^I[37m    [39;49;00mmaxInStatementIndent[37m [39;49;00m=[37m [39;49;00mmax;[37m[39;49;00m$
   613^I[37m  [39;49;00m}[37m[39;49;00m$
   614^I[37m[39;49;00m$
   615^I[37m  [39;49;00m[37m/**[39;49;00m$
   616^I[37m   * set the minimum indentation between two lines in a multi-line condition.[39;49;00m$
   617^I[37m   *[39;49;00m$
   618^I[37m   * @param   min     minimal indentation length.[39;49;00m$
   619^I[37m   */[39;49;00m[37m[39;49;00m$
   620^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setMinConditionalIndentLength([36mint[39;49;00m[37m [39;49;00mmin)[37m[39;49;00m$
   621^I[37m  [39;49;00m{[37m[39;49;00m$
   622^I[37m    [39;49;00mminConditionalIndent[37m [39;49;00m=[37m [39;49;00mmin;[37m[39;49;00m$
   623^I[37m    [39;49;00misMinimalConditinalIndentSet[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
   624^I[37m  [39;49;00m}[37m[39;49;00m$
   625^I[37m[39;49;00m$
   626^I[37m  [39;49;00m[37m/**[39;49;00m$
   627^I[37m   * set the state of the bracket indentation option. If true, brackets will [39;49;00m$
   628^I[37m   * be indented one additional indent.[39;49;00m$
   629^I[37m   *[39;49;00m$
   630^I[37m   * @param   state             state of option.[39;49;00m$
   631^I[37m   */[39;49;00m[37m[39;49;00m$
   632^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setBracketIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   633^I[37m  [39;49;00m{[37m[39;49;00m$
   634^I[37m    [39;49;00mbracketIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   635^I[37m  [39;49;00m}[37m[39;49;00m$
   636^I[37m[39;49;00m$
   637^I[37m  [39;49;00m[37m/**[39;49;00m$
   638^I[37m   * set the state of the block indentation option. If true, entire blocks [39;49;00m$
   639^I[37m   * will be indented one additional indent, similar to the GNU indent style.[39;49;00m$
   640^I[37m   *[39;49;00m$
   641^I[37m   * @param   state             state of option.[39;49;00m$
   642^I[37m   */[39;49;00m[37m[39;49;00m$
   643^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setBlockIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   644^I[37m  [39;49;00m{[37m[39;49;00m$
   645^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(state)[37m[39;49;00m$
   646^I[37m      [39;49;00msetBracketIndent([36mfalse[39;49;00m);[37m [39;49;00m[37m// so that we don't have both bracket and block indent[39;49;00m$
   647^I[37m    [39;49;00mblockIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   648^I[37m  [39;49;00m}[37m[39;49;00m$
   649^I[37m[39;49;00m$
   650^I[37m  [39;49;00m[37m/**[39;49;00m$
   651^I[37m   * set the state of the class indentation option. If true, C++ class[39;49;00m$
   652^I[37m   * definitions will be indented one additional indent.[39;49;00m$
   653^I[37m   *[39;49;00m$
   654^I[37m   * @param   state             state of option.[39;49;00m$
   655^I[37m   */[39;49;00m[37m[39;49;00m$
   656^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setClassIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   657^I[37m  [39;49;00m{[37m[39;49;00m$
   658^I[37m    [39;49;00mclassIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   659^I[37m  [39;49;00m}[37m[39;49;00m$
   660^I[37m[39;49;00m$
   661^I[37m  [39;49;00m[37m/**[39;49;00m$
   662^I[37m   * set the state of the switch indentation option. If true, blocks of 'switch' [39;49;00m$
   663^I[37m   * statements will be indented one additional indent.[39;49;00m$
   664^I[37m   *[39;49;00m$
   665^I[37m   * @param   state             state of option.[39;49;00m$
   666^I[37m   */[39;49;00m[37m[39;49;00m$
   667^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setSwitchIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   668^I[37m  [39;49;00m{[37m[39;49;00m$
   669^I[37m    [39;49;00mswitchIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   670^I[37m  [39;49;00m}[37m[39;49;00m$
   671^I[37m[39;49;00m$
   672^I[37m  [39;49;00m[37m/**[39;49;00m$
   673^I[37m   * set the state of the case indentation option. If true, lines of 'case' [39;49;00m$
   674^I[37m   * statements will be indented one additional indent.[39;49;00m$
   675^I[37m   *[39;49;00m$
   676^I[37m   * @param   state             state of option.[39;49;00m$
   677^I[37m   */[39;49;00m[37m[39;49;00m$
   678^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setCaseIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   679^I[37m  [39;49;00m{[37m[39;49;00m$
   680^I[37m    [39;49;00mcaseIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   681^I[37m  [39;49;00m}[37m[39;49;00m$
   682^I[37m  [39;49;00m[37m/**[39;49;00m$
   683^I[37m   * set the state of the namespace indentation option. [39;49;00m$
   684^I[37m   * If true, blocks of 'namespace' statements will be indented one [39;49;00m$
   685^I[37m   * additional indent. Otherwise, NO indentation will be added.[39;49;00m$
   686^I[37m   *[39;49;00m$
   687^I[37m   * @param   state             state of option.[39;49;00m$
   688^I[37m   */[39;49;00m[37m[39;49;00m$
   689^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setNamespaceIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   690^I[37m  [39;49;00m{[37m[39;49;00m$
   691^I[37m    [39;49;00mnamespaceIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   692^I[37m  [39;49;00m}[37m[39;49;00m$
   693^I[37m[39;49;00m$
   694^I[37m  [39;49;00m[37m/**[39;49;00m$
   695^I[37m   * set the state of the label indentation option. [39;49;00m$
   696^I[37m   * If true, labels will be indented one indent LESS than the[39;49;00m$
   697^I[37m   * current indentation level.[39;49;00m$
   698^I[37m   * If false, labels will be flushed to the left with NO[39;49;00m$
   699^I[37m   * indent at all.[39;49;00m$
   700^I[37m   *[39;49;00m$
   701^I[37m   * @param   state             state of option.[39;49;00m$
   702^I[37m   */[39;49;00m[37m[39;49;00m$
   703^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setLabelIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   704^I[37m  [39;49;00m{[37m[39;49;00m$
   705^I[37m    [39;49;00mlabelIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   706^I[37m  [39;49;00m}[37m[39;49;00m$
   707^I[37m[39;49;00m$
   708^I[37m  [39;49;00m[37m/**[39;49;00m$
   709^I[37m   * set the state of the preprocessor indentation option. [39;49;00m$
   710^I[37m   * If true, multiline #define statements will be indented.[39;49;00m$
   711^I[37m   *[39;49;00m$
   712^I[37m   * @param   state             state of option.[39;49;00m$
   713^I[37m   */[39;49;00m[37m[39;49;00m$
   714^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setPreprocessorIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   715^I[37m  [39;49;00m{[37m[39;49;00m$
   716^I[37m    [39;49;00mpreprocessorIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   717^I[37m  [39;49;00m}[37m[39;49;00m$
   718^I[37m[39;49;00m$
   719^I[37m  [39;49;00m[37m/**[39;49;00m$
   720^I[37m   * set the state of the empty line fill option. [39;49;00m$
   721^I[37m   * If true, empty lines will be filled with the whitespace.[39;49;00m$
   722^I[37m   * of their previous lines.[39;49;00m$
   723^I[37m   * If false, these lines will remain empty.[39;49;00m$
   724^I[37m   *[39;49;00m$
   725^I[37m   * @param   state             state of option.[39;49;00m$
   726^I[37m   */[39;49;00m[37m[39;49;00m$
   727^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setEmptyLineFill([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   728^I[37m  [39;49;00m{[37m[39;49;00m$
   729^I[37m    [39;49;00memptyLineFill[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   730^I[37m  [39;49;00m}[37m[39;49;00m$
   731^I[37m[39;49;00m$
   732^I[37m  [39;49;00m[37m/**[39;49;00m$
   733^I[37m   * check if there are any indented lines ready to be read by nextLine()[39;49;00m$
   734^I[37m   *[39;49;00m$
   735^I[37m   * @return    are there any indented lines ready?[39;49;00m$
   736^I[37m   */[39;49;00m[37m[39;49;00m$
   737^I[37m  [39;49;00m[36mbool[39;49;00m[37m [39;49;00mASBeautifier::hasMoreLines()[37m [39;49;00m[34mconst[39;49;00m[37m[39;49;00m$
   738^I[37m    [39;49;00m{[37m[39;49;00m$
   739^I[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00msourceIterator->hasMoreLines();[37m[39;49;00m$
   740^I[37m    [39;49;00m}[37m[39;49;00m$
   741^I[37m[39;49;00m$
   742^I[37m  [39;49;00m[37m/**[39;49;00m$
   743^I[37m   * get the next indented line.[39;49;00m$
   744^I[37m   *[39;49;00m$
   745^I[37m   * @return    indented line.[39;49;00m$
   746^I[37m   */[39;49;00m[37m[39;49;00m$
   747^I[37m  [39;49;00mstring[37m [39;49;00mASBeautifier::nextLine()[37m[39;49;00m$
   748^I[37m  [39;49;00m{[37m[39;49;00m$
   749^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mbeautify(sourceIterator->nextLine());[37m[39;49;00m$
   750^I[37m  [39;49;00m}[37m[39;49;00m$
   751^I[37m[39;49;00m$
   752^I[37m  [39;49;00m[37m/**[39;49;00m$
   753^I[37m   * beautify a line of source code.[39;49;00m$
   754^I[37m   * every line of source code in a source code file should be sent[39;49;00m$
   755^I[37m   * one after the other to the beautify method.[39;49;00m$
   756^I[37m   *[39;49;00m$
   757^I[37m   * @return      the indented line.[39;49;00m$
   758^I[37m   * @param originalLine       the original unindented line.[39;49;00m$
   759^I[37m   */[39;49;00m[37m[39;49;00m$
   760^I[37m  [39;49;00mstring[37m [39;49;00mASBeautifier::beautify([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&originalLine)[37m[39;49;00m$
   761^I[37m  [39;49;00m{[37m[39;49;00m$
   762^I[37m    [39;49;00mstring[37m [39;49;00mline;[37m[39;49;00m$
   763^I[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInLineComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   764^I[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00mlineStartsInComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   765^I[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInClass[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   766^I[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInSwitch[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   767^I[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00misImmediatelyAfterConst[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   768^I[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00misSpecialChar[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   769^I[37m[39;49;00m$
   770^I[37m    [39;49;00m[36mchar[39;49;00m[37m [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
   771^I[37m    [39;49;00m[36mchar[39;49;00m[37m [39;49;00mprevCh;[37m[39;49;00m$
   772^I[37m    [39;49;00mstring[37m [39;49;00moutBuffer;[37m [39;49;00m[37m// the newly idented line is bufferd here[39;49;00m$
   773^I[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mtabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   774^I[37m    [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*lastLineHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   775^I[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00mclosingBracketReached[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   776^I[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mspaceTabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   777^I[37m    [39;49;00m[36mchar[39;49;00m[37m [39;49;00mtempCh;[37m[39;49;00m$
   778^I[37m    [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mheaderStackSize[37m [39;49;00m=[37m [39;49;00mheaderStack->size();[37m[39;49;00m$
   779^I[37m    [39;49;00m[37m//bool isLineInStatement = isInStatement;[39;49;00m$
   780^I[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00mshouldIndentBrackettedLine[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
   781^I[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mlineOpeningBlocksNum[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   782^I[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mlineClosingBlocksNum[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   783^I[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00mpreviousLineProbation[37m [39;49;00m=[37m [39;49;00m(probationHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
   784^I[37m    [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi;[37m[39;49;00m$
   785^I[37m[39;49;00m$
   786^I[37m    [39;49;00mcurrentHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   787^I[37m[39;49;00m$
   788^I[37m    [39;49;00mlineStartsInComment[37m [39;49;00m=[37m [39;49;00misInComment;[37m[39;49;00m$
   789^I[37m[39;49;00m$
   790^I[37m    [39;49;00m[37m// handle and remove white spaces around the line:[39;49;00m$
   791^I[37m    [39;49;00m[37m// If not in comment, first find out size of white space before line,[39;49;00m$
   792^I[37m    [39;49;00m[37m// so that possible comments starting in the line continue in[39;49;00m$
   793^I[37m    [39;49;00m[37m// relation to the preliminary white-space.[39;49;00m$
   794^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInComment)[37m[39;49;00m$
   795^I[37m      [39;49;00m{[37m[39;49;00m$
   796^I[37m        [39;49;00mleadingWhiteSpaces[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   797^I[37m        [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(leadingWhiteSpaces<originalLine.length()[37m [39;49;00m&&[37m [39;49;00moriginalLine[leadingWhiteSpaces][37m [39;49;00m<=[37m [39;49;00m[34m0x20[39;49;00m)[37m[39;49;00m$
   798^I[37m          [39;49;00mleadingWhiteSpaces++;[37m[39;49;00m$
   799^I[37m[39;49;00m$
   800^I[37m        [39;49;00mline[37m [39;49;00m=[37m [39;49;00mtrim(originalLine);[37m[39;49;00m$
   801^I[37m      [39;49;00m}[37m[39;49;00m$
   802^I[37m    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
   803^I[37m      [39;49;00m{[37m[39;49;00m$
   804^I[37m        [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mtrimSize;[37m[39;49;00m$
   805^I[37m        [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(trimSize=[34m0[39;49;00m;[37m[39;49;00m$
   806^I[37m             [39;49;00mtrimSize[37m [39;49;00m<[37m [39;49;00moriginalLine.length()[37m [39;49;00m&&[37m [39;49;00mtrimSize<leadingWhiteSpaces[37m [39;49;00m&&[37m [39;49;00moriginalLine[trimSize][37m [39;49;00m<=[37m [39;49;00m[34m0x20[39;49;00m[37m [39;49;00m;[37m[39;49;00m$
   807^I[37m             [39;49;00mtrimSize++)[37m[39;49;00m$
   808^I[37m          [39;49;00m;[37m[39;49;00m$
   809^I[37m        [39;49;00mline[37m [39;49;00m=[37m [39;49;00moriginalLine.substr(trimSize);[37m[39;49;00m$
   810^I[37m      [39;49;00m}[37m[39;49;00m$
   811^I[37m[39;49;00m$
   812^I[37m[39;49;00m$
   813^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.length()[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   814^I[37m      [39;49;00m{[37m[39;49;00m$
   815^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(emptyLineFill)[37m[39;49;00m$
   816^I[37m          [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mpreLineWS(prevFinalLineSpaceTabCount,[37m [39;49;00mprevFinalLineTabCount);[37m[39;49;00m$
   817^I[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
   818^I[37m          [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mline;[37m[39;49;00m$
   819^I[37m      [39;49;00m}[37m[39;49;00m$
   820^I[37m[39;49;00m$
   821^I[37m    [39;49;00m[37m// handle preprocessor commands[39;49;00m$
   822^I[37m[39;49;00m$
   823^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00m!isInComment[37m [39;49;00m&&[37m [39;49;00m(line[[34m0[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m#[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mbackslashEndsPrevLine))[37m[39;49;00m$
   824^I[37m      [39;49;00m{[37m[39;49;00m$
   825^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line[[34m0[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m#[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
   826^I[37m          [39;49;00m{[37m[39;49;00m$
   827^I[37m            [39;49;00mstring[37m [39;49;00mpreproc[37m [39;49;00m=[37m [39;49;00mtrim(string(line.c_str()[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m));[37m[39;49;00m$
   828^I[37m[39;49;00m$
   829^I[37m[39;49;00m$
   830^I[37m            [39;49;00m[37m// When finding a multi-lined #define statement, the original beautifier[39;49;00m$
   831^I[37m            [39;49;00m[37m// 1. sets its isInDefineDefinition flag[39;49;00m$
   832^I[37m            [39;49;00m[37m// 2. clones a new beautifier that will be used for the actual indentation[39;49;00m$
   833^I[37m            [39;49;00m[37m//    of the #define. This clone is put into the activeBeautifierStack in order[39;49;00m$
   834^I[37m            [39;49;00m[37m//    to be called for the actual indentation.[39;49;00m$
   835^I[37m            [39;49;00m[37m// The original beautifier will have isInDefineDefinition = true, isInDefine = false[39;49;00m$
   836^I[37m            [39;49;00m[37m// The cloned beautifier will have   isInDefineDefinition = true, isInDefine = true[39;49;00m$
   837^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preprocessorIndent[37m [39;49;00m&&[37m [39;49;00mpreproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m6[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33mdefine[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m  [39;49;00mline[line.length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
   838^I[37m              [39;49;00m{[37m[39;49;00m$
   839^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInDefineDefinition)[37m[39;49;00m$
   840^I[37m                  [39;49;00m{[37m[39;49;00m$
   841^I[37m                    [39;49;00mASBeautifier[37m [39;49;00m*defineBeautifier;[37m[39;49;00m$
   842^I[37m[39;49;00m$
   843^I[37m                    [39;49;00m[37m// this is the original beautifier[39;49;00m$
   844^I[37m                    [39;49;00misInDefineDefinition[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
   845^I[37m[39;49;00m$
   846^I[37m                    [39;49;00m[37m// push a new beautifier into the active stack[39;49;00m$
   847^I[37m                    [39;49;00m[37m// this breautifier will be used for the indentation of this define[39;49;00m$
   848^I[37m                    [39;49;00mdefineBeautifier[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mASBeautifier(*[34mthis[39;49;00m);[37m[39;49;00m$
   849^I[37m                    [39;49;00m[37m//defineBeautifier->init();[39;49;00m$
   850^I[37m                    [39;49;00m[37m//defineBeautifier->isInDefineDefinition = true;[39;49;00m$
   851^I[37m                    [39;49;00m[37m//defineBeautifier->beautify("");[39;49;00m$
   852^I[37m                    [39;49;00mactiveBeautifierStack->push_back(defineBeautifier);[37m[39;49;00m$
   853^I[37m                  [39;49;00m}[37m[39;49;00m$
   854^I[37m                [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
   855^I[37m                  [39;49;00m{[37m[39;49;00m$
   856^I[37m                    [39;49;00m[37m// the is the cloned beautifier that is in charge of indenting the #define.[39;49;00m$
   857^I[37m                    [39;49;00misInDefine[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
   858^I[37m                  [39;49;00m}[37m[39;49;00m$
   859^I[37m              [39;49;00m}[37m[39;49;00m$
   860^I[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33mif[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   861^I[37m              [39;49;00m{[37m[39;49;00m$
   862^I[37m                [39;49;00m[37m// push a new beautifier into the stack[39;49;00m$
   863^I[37m                [39;49;00mwaitingBeautifierStackLengthStack->push_back(waitingBeautifierStack->size());[37m[39;49;00m$
   864^I[37m                [39;49;00mactiveBeautifierStackLengthStack->push_back(activeBeautifierStack->size());[37m[39;49;00m$
   865^I[37m                [39;49;00mwaitingBeautifierStack->push_back([34mnew[39;49;00m[37m [39;49;00mASBeautifier(*[34mthis[39;49;00m));[37m[39;49;00m$
   866^I[37m              [39;49;00m}[37m[39;49;00m$
   867^I[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m4[39;49;00m[37m/*2*/[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33melse[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   868^I[37m              [39;49;00m{[37m[39;49;00m$
   869^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!waitingBeautifierStack->empty())[37m[39;49;00m$
   870^I[37m                  [39;49;00m{[37m[39;49;00m$
   871^I[37m                    [39;49;00m[37m// MOVE current waiting beautifier to active stack.[39;49;00m$
   872^I[37m                    [39;49;00mactiveBeautifierStack->push_back(waitingBeautifierStack->back());[37m[39;49;00m$
   873^I[37m                    [39;49;00mwaitingBeautifierStack->pop_back();[37m[39;49;00m$
   874^I[37m                  [39;49;00m}[37m[39;49;00m$
   875^I[37m              [39;49;00m}[37m[39;49;00m$
   876^I[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m4[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33melif[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   877^I[37m              [39;49;00m{[37m[39;49;00m$
   878^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!waitingBeautifierStack->empty())[37m[39;49;00m$
   879^I[37m                  [39;49;00m{[37m[39;49;00m$
   880^I[37m                    [39;49;00m[37m// append a COPY current waiting beautifier to active stack, WITHOUT deleting the original.[39;49;00m$
   881^I[37m                    [39;49;00mactiveBeautifierStack->push_back([37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mASBeautifier([37m [39;49;00m*(waitingBeautifierStack->back())[37m [39;49;00m)[37m [39;49;00m);[37m[39;49;00m$
   882^I[37m                  [39;49;00m}[37m[39;49;00m$
   883^I[37m              [39;49;00m}[37m[39;49;00m$
   884^I[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m5[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33mendif[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   885^I[37m              [39;49;00m{[37m[39;49;00m$
   886^I[37m                [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mstackLength;[37m[39;49;00m$
   887^I[37m                [39;49;00mASBeautifier[37m [39;49;00m*beautifier;[37m[39;49;00m$
   888^I[37m[39;49;00m$
   889^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!waitingBeautifierStackLengthStack->empty())[37m[39;49;00m$
   890^I[37m                  [39;49;00m{[37m[39;49;00m$
   891^I[37m                    [39;49;00mstackLength[37m [39;49;00m=[37m [39;49;00mwaitingBeautifierStackLengthStack->back();[37m[39;49;00m$
   892^I[37m                    [39;49;00mwaitingBeautifierStackLengthStack->pop_back();[37m[39;49;00m$
   893^I[37m                    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(waitingBeautifierStack->size()[37m [39;49;00m>[37m [39;49;00mstackLength)[37m[39;49;00m$
   894^I[37m                      [39;49;00m{[37m[39;49;00m$
   895^I[37m                        [39;49;00mbeautifier[37m [39;49;00m=[37m [39;49;00mwaitingBeautifierStack->back();[37m[39;49;00m$
   896^I[37m                        [39;49;00mwaitingBeautifierStack->pop_back();[37m[39;49;00m$
   897^I[37m                        [39;49;00m[34mdelete[39;49;00m[37m [39;49;00mbeautifier;[37m[39;49;00m$
   898^I[37m                      [39;49;00m}[37m[39;49;00m$
   899^I[37m                  [39;49;00m}[37m[39;49;00m$
   900^I[37m[39;49;00m$
   901^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!activeBeautifierStackLengthStack->empty())[37m[39;49;00m$
   902^I[37m                  [39;49;00m{[37m[39;49;00m$
   903^I[37m                    [39;49;00mstackLength[37m [39;49;00m=[37m [39;49;00mactiveBeautifierStackLengthStack->back();[37m[39;49;00m$
   904^I[37m                    [39;49;00mactiveBeautifierStackLengthStack->pop_back();[37m[39;49;00m$
   905^I[37m                    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(activeBeautifierStack->size()[37m [39;49;00m>[37m [39;49;00mstackLength)[37m[39;49;00m$
   906^I[37m                      [39;49;00m{[37m[39;49;00m$
   907^I[37m                        [39;49;00mbeautifier[37m [39;49;00m=[37m [39;49;00mactiveBeautifierStack->back();[37m[39;49;00m$
   908^I[37m                        [39;49;00mactiveBeautifierStack->pop_back();[37m[39;49;00m$
   909^I[37m                        [39;49;00m[34mdelete[39;49;00m[37m [39;49;00mbeautifier;[37m[39;49;00m$
   910^I[37m                      [39;49;00m}[37m[39;49;00m$
   911^I[37m                  [39;49;00m}[37m[39;49;00m$
   912^I[37m[39;49;00m$
   913^I[37m[39;49;00m$
   914^I[37m              [39;49;00m}[37m[39;49;00m$
   915^I[37m          [39;49;00m}[37m[39;49;00m$
   916^I[37m[39;49;00m$
   917^I[37m        [39;49;00m[37m// check if the last char is a backslash[39;49;00m$
   918^I[37m        [39;49;00m[34mif[39;49;00m(line.length()[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   919^I[37m          [39;49;00mbackslashEndsPrevLine[37m [39;49;00m=[37m [39;49;00m(line[line.length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
   920^I[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
   921^I[37m          [39;49;00mbackslashEndsPrevLine[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   922^I[37m[39;49;00m$
   923^I[37m        [39;49;00m[37m// check if this line ends a multi-line #define[39;49;00m$
   924^I[37m        [39;49;00m[37m// if so, use the #define's cloned beautifier for the line's indentation[39;49;00m$
   925^I[37m        [39;49;00m[37m// and then remove it from the active beautifier stack and delete it.[39;49;00m$
   926^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!backslashEndsPrevLine[37m [39;49;00m&&[37m [39;49;00misInDefineDefinition[37m [39;49;00m&&[37m [39;49;00m!isInDefine)[37m[39;49;00m$
   927^I[37m          [39;49;00m{[37m[39;49;00m$
   928^I[37m            [39;49;00mstring[37m [39;49;00mbeautifiedLine;[37m[39;49;00m$
   929^I[37m            [39;49;00mASBeautifier[37m [39;49;00m*defineBeautifier;[37m[39;49;00m$
   930^I[37m[39;49;00m$
   931^I[37m            [39;49;00misInDefineDefinition[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   932^I[37m            [39;49;00mdefineBeautifier[37m [39;49;00m=[37m [39;49;00mactiveBeautifierStack->back();[37m[39;49;00m$
   933^I[37m            [39;49;00mactiveBeautifierStack->pop_back();[37m[39;49;00m$
   934^I[37m[39;49;00m$
   935^I[37m            [39;49;00mbeautifiedLine[37m [39;49;00m=[37m [39;49;00mdefineBeautifier->beautify(line);[37m[39;49;00m$
   936^I[37m            [39;49;00m[34mdelete[39;49;00m[37m [39;49;00mdefineBeautifier;[37m[39;49;00m$
   937^I[37m            [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mbeautifiedLine;[37m[39;49;00m$
   938^I[37m          [39;49;00m}[37m[39;49;00m$
   939^I[37m[39;49;00m$
   940^I[37m        [39;49;00m[37m// unless this is a multi-line #define, return this precompiler line as is.[39;49;00m$
   941^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInDefine[37m [39;49;00m&&[37m [39;49;00m!isInDefineDefinition)[37m[39;49;00m$
   942^I[37m          [39;49;00m[34mreturn[39;49;00m[37m [39;49;00moriginalLine;[37m[39;49;00m$
   943^I[37m      [39;49;00m}[37m[39;49;00m$
   944^I[37m[39;49;00m$
   945^I[37m    [39;49;00m[37m// if there exists any worker beautifier in the activeBeautifierStack,[39;49;00m$
   946^I[37m    [39;49;00m[37m// then use it instead of me to indent the current line.[39;49;00m$
   947^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInDefine[37m [39;49;00m&&[37m [39;49;00mactiveBeautifierStack[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00m!activeBeautifierStack->empty())[37m[39;49;00m$
   948^I[37m      [39;49;00m{[37m[39;49;00m$
   949^I[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mactiveBeautifierStack->back()->beautify(line);[37m[39;49;00m$
   950^I[37m      [39;49;00m}[37m[39;49;00m$
   951^I[37m[39;49;00m$
   952^I[37m    [39;49;00m[37m// calculate preliminary indentation based on data from past lines[39;49;00m$
   953^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStack->empty())[37m[39;49;00m$
   954^I[37m      [39;49;00mspaceTabCount[37m [39;49;00m=[37m [39;49;00minStatementIndentStack->back();[37m[39;49;00m$
   955^I[37m[39;49;00m$
   956^I[37m[39;49;00m$
   957^I[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(i=[34m0[39;49;00m;[37m [39;49;00mi<headerStackSize;[37m [39;49;00mi++)[37m[39;49;00m$
   958^I[37m      [39;49;00m{[37m[39;49;00m$
   959^I[37m        [39;49;00misInClass[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   960^I[37m[39;49;00m$
   961^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(blockIndent[37m [39;49;00m||[37m [39;49;00m(!(i>[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(*headerStack)[i[34m-1[39;49;00m][37m [39;49;00m!=[37m [39;49;00m&AS_OPEN_BRACKET[37m[39;49;00m$
   962^I[37m                              [39;49;00m&&[37m [39;49;00m(*headerStack)[i][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET)))[37m[39;49;00m$
   963^I[37m          [39;49;00m++tabCount;[37m[39;49;00m$
   964^I[37m[39;49;00m$
   965^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00m!namespaceIndent[37m [39;49;00m&&[37m [39;49;00mi[37m [39;49;00m>=[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
   966^I[37m            [39;49;00m&&[37m [39;49;00m(*headerStack)[i[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_NAMESPACE[37m[39;49;00m$
   967^I[37m            [39;49;00m&&[37m [39;49;00m(*headerStack)[i][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET)[37m[39;49;00m$
   968^I[37m          [39;49;00m--tabCount;[37m[39;49;00m$
   969^I[37m[39;49;00m$
   970^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00mi[37m [39;49;00m>=[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
   971^I[37m            [39;49;00m&&[37m [39;49;00m(*headerStack)[i[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_CLASS[37m[39;49;00m$
   972^I[37m            [39;49;00m&&[37m [39;49;00m(*headerStack)[i][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET[37m [39;49;00m)[37m[39;49;00m$
   973^I[37m          [39;49;00m{[37m[39;49;00m$
   974^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(classIndent)[37m[39;49;00m$
   975^I[37m              [39;49;00m++tabCount;[37m[39;49;00m$
   976^I[37m            [39;49;00misInClass[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
   977^I[37m          [39;49;00m}[37m[39;49;00m$
   978^I[37m[39;49;00m$
   979^I[37m        [39;49;00m[37m// is the switchIndent option is on, indent switch statements an additional indent.[39;49;00m$
   980^I[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(switchIndent[37m [39;49;00m&&[37m [39;49;00mi[37m [39;49;00m>[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m&&[37m[39;49;00m$
   981^I[37m                 [39;49;00m(*headerStack)[i[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_SWITCH[37m [39;49;00m&&[37m[39;49;00m$
   982^I[37m                 [39;49;00m(*headerStack)[i][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET[37m[39;49;00m$
   983^I[37m                [39;49;00m)[37m[39;49;00m$
   984^I[37m          [39;49;00m{[37m[39;49;00m$
   985^I[37m            [39;49;00m++tabCount;[37m[39;49;00m$
   986^I[37m            [39;49;00misInSwitch[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
   987^I[37m          [39;49;00m}[37m[39;49;00m$
   988^I[37m[39;49;00m$
   989^I[37m      [39;49;00m}[37m[39;49;00m$
   990^I[37m[39;49;00m$
   991^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!lineStartsInComment[37m[39;49;00m$
   992^I[37m        [39;49;00m&&[37m [39;49;00misCStyle[37m[39;49;00m$
   993^I[37m        [39;49;00m&&[37m [39;49;00misInClass[37m[39;49;00m$
   994^I[37m        [39;49;00m&&[37m [39;49;00mclassIndent[37m[39;49;00m$
   995^I[37m        [39;49;00m&&[37m [39;49;00mheaderStackSize[37m [39;49;00m>=[37m [39;49;00m[34m2[39;49;00m[37m[39;49;00m$
   996^I[37m        [39;49;00m&&(*headerStack)[headerStackSize[34m-2[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_CLASS[37m[39;49;00m$
   997^I[37m        [39;49;00m&&[37m [39;49;00m(*headerStack)[headerStackSize[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET[37m[39;49;00m$
   998^I[37m        [39;49;00m&&[37m [39;49;00mline[[34m0[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
   999^I[37m      [39;49;00m--tabCount;[37m[39;49;00m$
  1000^I[37m[39;49;00m$
  1001^I[37m    [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!lineStartsInComment[37m[39;49;00m$
  1002^I[37m             [39;49;00m&&[37m [39;49;00misInSwitch[37m[39;49;00m$
  1003^I[37m             [39;49;00m&&[37m [39;49;00mswitchIndent[37m[39;49;00m$
  1004^I[37m             [39;49;00m&&[37m [39;49;00mheaderStackSize[37m [39;49;00m>=[37m [39;49;00m[34m2[39;49;00m[37m[39;49;00m$
  1005^I[37m             [39;49;00m&&[37m [39;49;00m(*headerStack)[headerStackSize[34m-2[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_SWITCH[37m[39;49;00m$
  1006^I[37m             [39;49;00m&&[37m [39;49;00m(*headerStack)[headerStackSize[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET[37m[39;49;00m$
  1007^I[37m             [39;49;00m&&[37m [39;49;00mline[[34m0[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1008^I[37m      [39;49;00m--tabCount;[37m[39;49;00m$
  1009^I[37m[39;49;00m$
  1010^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInClassHeader)[37m[39;49;00m$
  1011^I[37m      [39;49;00m{[37m[39;49;00m$
  1012^I[37m        [39;49;00misInClassHeaderTab[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1013^I[37m        [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m$
  1014^I[37m      [39;49;00m}[37m[39;49;00m$
  1015^I[37m[39;49;00m$
  1016^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInConditional)[37m[39;49;00m$
  1017^I[37m      [39;49;00m{[37m[39;49;00m$
  1018^I[37m        [39;49;00m--tabCount;[37m[39;49;00m$
  1019^I[37m      [39;49;00m}[37m[39;49;00m$
  1020^I[37m[39;49;00m$
  1021^I[37m[39;49;00m$
  1022^I[37m    [39;49;00m[37m// parse characters in the current line.[39;49;00m$
  1023^I[37m[39;49;00m$
  1024^I[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(i=[34m0[39;49;00m;[37m [39;49;00mi<line.length();[37m [39;49;00mi++)[37m[39;49;00m$
  1025^I[37m      [39;49;00m{[37m[39;49;00m$
  1026^I[37m        [39;49;00mtempCh[37m [39;49;00m=[37m [39;49;00mline[i];[37m[39;49;00m$
  1027^I[37m[39;49;00m$
  1028^I[37m        [39;49;00mprevCh[37m [39;49;00m=[37m [39;49;00mch;[37m[39;49;00m$
  1029^I[37m        [39;49;00mch[37m [39;49;00m=[37m [39;49;00mtempCh;[37m[39;49;00m$
  1030^I[37m[39;49;00m$
  1031^I[37m        [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00mch);[37m[39;49;00m$
  1032^I[37m[39;49;00m$
  1033^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isWhiteSpace(ch))[37m[39;49;00m$
  1034^I[37m          [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1035^I[37m[39;49;00m$
  1036^I[37m[39;49;00m$
  1037^I[37m        [39;49;00m[37m// handle special characters (i.e. backslash+character such as \n, \t, ...)[39;49;00m$
  1038^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isSpecialChar)[37m[39;49;00m$
  1039^I[37m          [39;49;00m{[37m[39;49;00m$
  1040^I[37m            [39;49;00misSpecialChar[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1041^I[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1042^I[37m          [39;49;00m}[37m[39;49;00m$
  1043^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00mline.COMPARE(i,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1044^I[37m          [39;49;00m{[37m[39;49;00m$
  1045^I[37m            [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
  1046^I[37m            [39;49;00mi++;[37m[39;49;00m$
  1047^I[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1048^I[37m          [39;49;00m}[37m[39;49;00m$
  1049^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00mch==[33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1050^I[37m          [39;49;00m{[37m[39;49;00m$
  1051^I[37m            [39;49;00misSpecialChar[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1052^I[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1053^I[37m          [39;49;00m}[37m[39;49;00m$
  1054^I[37m[39;49;00m$
  1055^I[37m        [39;49;00m[37m// handle quotes (such as 'x' and "Hello Dolly")[39;49;00m$
  1056^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00m(ch==[33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch==[33m'[39;49;00m[33m\'[39;49;00m[33m'[39;49;00m))[37m[39;49;00m$
  1057^I[37m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInQuote)[37m[39;49;00m$
  1058^I[37m            [39;49;00m{[37m[39;49;00m$
  1059^I[37m              [39;49;00mquoteChar[37m [39;49;00m=[37m [39;49;00mch;[37m[39;49;00m$
  1060^I[37m              [39;49;00misInQuote[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1061^I[37m            [39;49;00m}[37m[39;49;00m$
  1062^I[37m          [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(quoteChar[37m [39;49;00m==[37m [39;49;00mch)[37m[39;49;00m$
  1063^I[37m            [39;49;00m{[37m[39;49;00m$
  1064^I[37m              [39;49;00misInQuote[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1065^I[37m              [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1066^I[37m              [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1067^I[37m            [39;49;00m}[37m[39;49;00m$
  1068^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInQuote)[37m[39;49;00m$
  1069^I[37m          [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1070^I[37m[39;49;00m$
  1071^I[37m        [39;49;00m[37m// handle comments[39;49;00m$
  1072^I[37m[39;49;00m$
  1073^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m!(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00mline.COMPARE(i,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_OPEN_LINE_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
  1074^I[37m          [39;49;00m{[37m[39;49;00m$
  1075^I[37m            [39;49;00misInLineComment[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1076^I[37m            [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
  1077^I[37m            [39;49;00mi++;[37m[39;49;00m$
  1078^I[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1079^I[37m          [39;49;00m}[37m[39;49;00m$
  1080^I[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m!(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00mline.COMPARE(i,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_OPEN_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
  1081^I[37m          [39;49;00m{[37m[39;49;00m$
  1082^I[37m            [39;49;00misInComment[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1083^I[37m            [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
  1084^I[37m            [39;49;00mi++;[37m[39;49;00m$
  1085^I[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1086^I[37m          [39;49;00m}[37m[39;49;00m$
  1087^I[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00mline.COMPARE(i,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_CLOSE_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
  1088^I[37m          [39;49;00m{[37m[39;49;00m$
  1089^I[37m            [39;49;00misInComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1090^I[37m            [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
  1091^I[37m            [39;49;00mi++;[37m[39;49;00m$
  1092^I[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1093^I[37m          [39;49;00m}[37m[39;49;00m$
  1094^I[37m[39;49;00m$
  1095^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInComment||isInLineComment)[37m[39;49;00m$
  1096^I[37m          [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1097^I[37m[39;49;00m$
  1098^I[37m        [39;49;00m[37m// if we have reached this far then we are NOT in a comment or string of special character...[39;49;00m$
  1099^I[37m[39;49;00m$
  1100^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(probationHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1101^I[37m          [39;49;00m{[37m[39;49;00m$
  1102^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m((probationHeader[37m [39;49;00m==[37m [39;49;00m&AS_STATIC[37m [39;49;00m||[37m [39;49;00mprobationHeader[37m [39;49;00m==[37m [39;49;00m&AS_CONST)[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1103^I[37m                 [39;49;00m||[37m [39;49;00m(probationHeader[37m [39;49;00m==[37m [39;49;00m&AS_SYNCHRONIZED[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m))[37m[39;49;00m$
  1104^I[37m              [39;49;00m{[37m[39;49;00m$
  1105^I[37m                [39;49;00m[37m// insert the probation header as a new header[39;49;00m$
  1106^I[37m                [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1107^I[37m                [39;49;00mheaderStack->push_back(probationHeader);[37m[39;49;00m$
  1108^I[37m[39;49;00m$
  1109^I[37m                [39;49;00m[37m// handle the specific probation header[39;49;00m$
  1110^I[37m                [39;49;00misInConditional[37m [39;49;00m=[37m [39;49;00m(probationHeader[37m [39;49;00m==[37m [39;49;00m&AS_SYNCHRONIZED);[37m[39;49;00m$
  1111^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(probationHeader[37m [39;49;00m==[37m [39;49;00m&AS_CONST)[37m[39;49;00m$
  1112^I[37m                  [39;49;00misImmediatelyAfterConst[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1113^I[37m                [39;49;00m[37m//  isInConst = true;[39;49;00m$
  1114^I[37m                [39;49;00m[37m/* TODO:[39;49;00m$
  1115^I[37m                 * There is actually no more need for the global isInConst variable.[39;49;00m$
  1116^I[37m                               * The only reason for checking const is to see if there is a const[39;49;00m$
  1117^I[37m                 * immediately before an open-bracket.[39;49;00m$
  1118^I[37m                 * Since CONST is now put into probation and is checked during itspost-char,[39;49;00m$
  1119^I[37m                 * isImmediatelyAfterConst can be set by its own...[39;49;00m$
  1120^I[37m                 */[39;49;00m[37m[39;49;00m$
  1121^I[37m[39;49;00m$
  1122^I[37m                [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1123^I[37m                [39;49;00m[37m// if the probation comes from the previous line, then indent by 1 tab count.[39;49;00m$
  1124^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(previousLineProbation[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1125^I[37m                  [39;49;00mtabCount++;[37m[39;49;00m$
  1126^I[37m                [39;49;00mpreviousLineProbation[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1127^I[37m              [39;49;00m}[37m[39;49;00m$
  1128^I[37m[39;49;00m$
  1129^I[37m            [39;49;00m[37m// dismiss the probation header[39;49;00m$
  1130^I[37m            [39;49;00mprobationHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1131^I[37m          [39;49;00m}[37m[39;49;00m$
  1132^I[37m[39;49;00m$
  1133^I[37m        [39;49;00mprevNonSpaceCh[37m [39;49;00m=[37m [39;49;00mcurrentNonSpaceCh;[37m[39;49;00m$
  1134^I[37m        [39;49;00mcurrentNonSpaceCh[37m [39;49;00m=[37m [39;49;00mch;[37m[39;49;00m$
  1135^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isLegalNameChar(ch)[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m!=[37m [39;49;00m[33m'[39;49;00m[33m,[39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m!=[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
  1136^I[37m          [39;49;00m{[37m[39;49;00m$
  1137^I[37m            [39;49;00mprevNonLegalCh[37m [39;49;00m=[37m [39;49;00mcurrentNonLegalCh;[37m[39;49;00m$
  1138^I[37m            [39;49;00mcurrentNonLegalCh[37m [39;49;00m=[37m [39;49;00mch;[37m[39;49;00m$
  1139^I[37m          [39;49;00m}[37m[39;49;00m$
  1140^I[37m[39;49;00m$
  1141^I[37m        [39;49;00m[37m//if (isInConst)[39;49;00m$
  1142^I[37m        [39;49;00m[37m//{[39;49;00m$
  1143^I[37m        [39;49;00m[37m//    isInConst = false;[39;49;00m$
  1144^I[37m        [39;49;00m[37m//    isImmediatelyAfterConst = true;[39;49;00m$
  1145^I[37m        [39;49;00m[37m//}[39;49;00m$
  1146^I[37m[39;49;00m$
  1147^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInHeader)[37m[39;49;00m$
  1148^I[37m          [39;49;00m{[37m[39;49;00m$
  1149^I[37m            [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1150^I[37m            [39;49;00mcurrentHeader[37m [39;49;00m=[37m [39;49;00mheaderStack->back();[37m[39;49;00m$
  1151^I[37m          [39;49;00m}[37m[39;49;00m$
  1152^I[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1153^I[37m          [39;49;00mcurrentHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1154^I[37m[39;49;00m$
  1155^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00misInTemplate[37m[39;49;00m$
  1156^I[37m            [39;49;00m&&[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m<[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m>[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1157^I[37m            [39;49;00m&&[37m  [39;49;00mfindHeader(line,[37m [39;49;00mi,[37m [39;49;00mnonAssignmentOperators)[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[37m//;[39;49;00m$
  1158^I[37m          [39;49;00m{[37m[39;49;00m$
  1159^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m<[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1160^I[37m              [39;49;00m{[37m[39;49;00m$
  1161^I[37m                [39;49;00m++templateDepth;[37m[39;49;00m$
  1162^I[37m              [39;49;00m}[37m[39;49;00m$
  1163^I[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m>[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1164^I[37m              [39;49;00m{[37m[39;49;00m$
  1165^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(--templateDepth[37m [39;49;00m<=[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1166^I[37m                  [39;49;00m{[37m[39;49;00m$
  1167^I[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInTemplate)[37m[39;49;00m$
  1168^I[37m                      [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
  1169^I[37m                    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1170^I[37m                      [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33mt[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
  1171^I[37m                    [39;49;00misInTemplate[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1172^I[37m                    [39;49;00mtemplateDepth[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  1173^I[37m                  [39;49;00m}[37m[39;49;00m$
  1174^I[37m[39;49;00m$
  1175^I[37m              [39;49;00m}[37m[39;49;00m$
  1176^I[37m          [39;49;00m}[37m[39;49;00m$
  1177^I[37m[39;49;00m$
  1178^I[37m        [39;49;00m[37m// handle parenthesies[39;49;00m$
  1179^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m[[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m][39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1180^I[37m          [39;49;00m{[37m[39;49;00m$
  1181^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m[[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1182^I[37m              [39;49;00m{[37m[39;49;00m$
  1183^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(parenDepth[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1184^I[37m                  [39;49;00m{[37m[39;49;00m$
  1185^I[37m                    [39;49;00mparenStatementStack->push_back(isInStatement);[37m[39;49;00m$
  1186^I[37m                    [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1187^I[37m                  [39;49;00m}[37m[39;49;00m$
  1188^I[37m                [39;49;00mparenDepth++;[37m[39;49;00m$
  1189^I[37m[39;49;00m$
  1190^I[37m                [39;49;00minStatementIndentStackSizeStack->push_back(inStatementIndentStack->size());[37m[39;49;00m$
  1191^I[37m[39;49;00m$
  1192^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(currentHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1193^I[37m                  [39;49;00mregisterInStatementIndent(line,[37m [39;49;00mi,[37m [39;49;00mspaceTabCount,[37m [39;49;00mminConditionalIndent[37m/*indentLength*2*/[39;49;00m,[37m [39;49;00m[36mtrue[39;49;00m);[37m[39;49;00m$
  1194^I[37m                [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1195^I[37m                  [39;49;00mregisterInStatementIndent(line,[37m [39;49;00mi,[37m [39;49;00mspaceTabCount,[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00m[36mtrue[39;49;00m);[37m[39;49;00m$
  1196^I[37m              [39;49;00m}[37m[39;49;00m$
  1197^I[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m][39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1198^I[37m              [39;49;00m{[37m[39;49;00m$
  1199^I[37m                [39;49;00mparenDepth--;[37m[39;49;00m$
  1200^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(parenDepth[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1201^I[37m                  [39;49;00m{[37m[39;49;00m$
  1202^I[37m                    [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00mparenStatementStack->back();[37m[39;49;00m$
  1203^I[37m                    [39;49;00mparenStatementStack->pop_back();[37m[39;49;00m$
  1204^I[37m                    [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
  1205^I[37m[39;49;00m$
  1206^I[37m                    [39;49;00misInConditional[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1207^I[37m                  [39;49;00m}[37m[39;49;00m$
  1208^I[37m[39;49;00m$
  1209^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStackSizeStack->empty())[37m[39;49;00m$
  1210^I[37m                  [39;49;00m{[37m[39;49;00m$
  1211^I[37m                    [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mpreviousIndentStackSize[37m [39;49;00m=[37m [39;49;00minStatementIndentStackSizeStack->back();[37m[39;49;00m$
  1212^I[37m                    [39;49;00minStatementIndentStackSizeStack->pop_back();[37m[39;49;00m$
  1213^I[37m                    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(previousIndentStackSize[37m [39;49;00m<[37m [39;49;00minStatementIndentStack->size())[37m[39;49;00m$
  1214^I[37m                      [39;49;00minStatementIndentStack->pop_back();[37m[39;49;00m$
  1215^I[37m[39;49;00m$
  1216^I[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!parenIndentStack->empty())[37m[39;49;00m$
  1217^I[37m                      [39;49;00m{[37m[39;49;00m$
  1218^I[37m                        [39;49;00m[36mint[39;49;00m[37m [39;49;00mpoppedIndent[37m [39;49;00m=[37m [39;49;00mparenIndentStack->back();[37m[39;49;00m$
  1219^I[37m                        [39;49;00mparenIndentStack->pop_back();[37m[39;49;00m$
  1220^I[37m[39;49;00m$
  1221^I[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1222^I[37m                          [39;49;00mspaceTabCount[37m [39;49;00m=[37m [39;49;00mpoppedIndent;[37m[39;49;00m$
  1223^I[37m                      [39;49;00m}[37m[39;49;00m$
  1224^I[37m                  [39;49;00m}[37m[39;49;00m$
  1225^I[37m              [39;49;00m}[37m[39;49;00m$
  1226^I[37m[39;49;00m$
  1227^I[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1228^I[37m          [39;49;00m}[37m[39;49;00m$
  1229^I[37m[39;49;00m$
  1230^I[37m[39;49;00m$
  1231^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1232^I[37m          [39;49;00m{[37m[39;49;00m$
  1233^I[37m            [39;49;00m[36mbool[39;49;00m[37m [39;49;00misBlockOpener[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1234^I[37m[39;49;00m$
  1235^I[37m            [39;49;00m[37m// first, check if '{' is a block-opener or an static-array opener[39;49;00m$
  1236^I[37m            [39;49;00misBlockOpener[37m [39;49;00m=[37m [39;49;00m([37m [39;49;00m(prevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00mbracketBlockStateStack->back())[37m[39;49;00m$
  1237^I[37m                              [39;49;00m||[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
  1238^I[37m                              [39;49;00m||[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
  1239^I[37m                              [39;49;00m||[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
  1240^I[37m                              [39;49;00m||[37m [39;49;00misInClassHeader[37m[39;49;00m$
  1241^I[37m                              [39;49;00m||[37m [39;49;00misBlockOpener[37m[39;49;00m$
  1242^I[37m                              [39;49;00m||[37m [39;49;00misImmediatelyAfterConst[37m[39;49;00m$
  1243^I[37m                              [39;49;00m||[37m [39;49;00m(isInDefine[37m [39;49;00m&&[37m[39;49;00m$
  1244^I[37m                                  [39;49;00m(prevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[37m[39;49;00m$
  1245^I[37m                                   [39;49;00m||[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m_[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
  1246^I[37m                                   [39;49;00m||[37m [39;49;00misalnum(prevNonSpaceCh)))[37m [39;49;00m);[37m[39;49;00m$
  1247^I[37m[39;49;00m$
  1248^I[37m            [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1249^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isBlockOpener[37m [39;49;00m&&[37m [39;49;00mcurrentHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1250^I[37m              [39;49;00m{[37m[39;49;00m$
  1251^I[37m                [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mn=[34m0[39;49;00m;[37m [39;49;00mn[37m [39;49;00m<[37m [39;49;00mnonParenHeaders.size();[37m [39;49;00mn++)[37m[39;49;00m$
  1252^I[37m                  [39;49;00m[34mif[39;49;00m[37m [39;49;00m(currentHeader[37m [39;49;00m==[37m [39;49;00mnonParenHeaders[n])[37m[39;49;00m$
  1253^I[37m                    [39;49;00m{[37m[39;49;00m$
  1254^I[37m                      [39;49;00misBlockOpener[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1255^I[37m                      [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1256^I[37m                    [39;49;00m}[37m[39;49;00m$
  1257^I[37m              [39;49;00m}[37m[39;49;00m$
  1258^I[37m            [39;49;00mbracketBlockStateStack->push_back(isBlockOpener);[37m[39;49;00m$
  1259^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isBlockOpener)[37m[39;49;00m$
  1260^I[37m              [39;49;00m{[37m[39;49;00m$
  1261^I[37m                [39;49;00minStatementIndentStackSizeStack->push_back(inStatementIndentStack->size());[37m[39;49;00m$
  1262^I[37m                [39;49;00mregisterInStatementIndent(line,[37m [39;49;00mi,[37m [39;49;00mspaceTabCount,[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00m[36mtrue[39;49;00m);[37m[39;49;00m$
  1263^I[37m                [39;49;00mparenDepth++;[37m[39;49;00m$
  1264^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1265^I[37m                  [39;49;00mshouldIndentBrackettedLine[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1266^I[37m[39;49;00m$
  1267^I[37m                [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1268^I[37m              [39;49;00m}[37m[39;49;00m$
  1269^I[37m[39;49;00m$
  1270^I[37m            [39;49;00m[37m// this bracket is a block opener...[39;49;00m$
  1271^I[37m[39;49;00m$
  1272^I[37m            [39;49;00m++lineOpeningBlocksNum;[37m[39;49;00m$
  1273^I[37m[39;49;00m$
  1274^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInClassHeader)[37m[39;49;00m$
  1275^I[37m              [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1276^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInClassHeaderTab)[37m[39;49;00m$
  1277^I[37m              [39;49;00m{[37m[39;49;00m$
  1278^I[37m                [39;49;00misInClassHeaderTab[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1279^I[37m                [39;49;00mtabCount[37m [39;49;00m-=[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m$
  1280^I[37m              [39;49;00m}[37m[39;49;00m$
  1281^I[37m[39;49;00m$
  1282^I[37m            [39;49;00mblockParenDepthStack->push_back(parenDepth);[37m[39;49;00m$
  1283^I[37m            [39;49;00mblockStatementStack->push_back(isInStatement);[37m[39;49;00m$
  1284^I[37m[39;49;00m$
  1285^I[37m            [39;49;00minStatementIndentStackSizeStack->push_back(inStatementIndentStack->size());[37m[39;49;00m$
  1286^I[37m[39;49;00m$
  1287^I[37m            [39;49;00mblockTabCount[37m [39;49;00m+=[37m [39;49;00misInStatement?[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m:[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  1288^I[37m            [39;49;00mparenDepth[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  1289^I[37m            [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1290^I[37m[39;49;00m$
  1291^I[37m            [39;49;00mtempStacks->push_back([34mnew[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>);[37m[39;49;00m$
  1292^I[37m            [39;49;00mheaderStack->push_back(&AS_OPEN_BRACKET);[37m[39;49;00m$
  1293^I[37m            [39;49;00mlastLineHeader[37m [39;49;00m=[37m [39;49;00m&AS_OPEN_BRACKET;[37m [39;49;00m[37m// <------[39;49;00m$
  1294^I[37m[39;49;00m$
  1295^I[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1296^I[37m          [39;49;00m}[37m[39;49;00m$
  1297^I[37m[39;49;00m$
  1298^I[37m        [39;49;00m[37m//check if a header has been reached[39;49;00m$
  1299^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(prevCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1300^I[37m          [39;49;00m{[37m[39;49;00m$
  1301^I[37m            [39;49;00m[36mbool[39;49;00m[37m [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1302^I[37m            [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*newHeader[37m [39;49;00m=[37m [39;49;00mfindHeader(line,[37m [39;49;00mi,[37m [39;49;00mheaders);[37m[39;49;00m$
  1303^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1304^I[37m              [39;49;00m{[37m[39;49;00m$
  1305^I[37m                [39;49;00m[37m// if we reached here, then this is a header...[39;49;00m$
  1306^I[37m                [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1307^I[37m[39;49;00m$
  1308^I[37m                [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m*lastTempStack;[37m[39;49;00m$
  1309^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(tempStacks->empty())[37m[39;49;00m$
  1310^I[37m                  [39;49;00mlastTempStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1311^I[37m                [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1312^I[37m                  [39;49;00mlastTempStack[37m [39;49;00m=[37m [39;49;00mtempStacks->back();[37m[39;49;00m$
  1313^I[37m[39;49;00m$
  1314^I[37m                [39;49;00m[37m// if a new block is opened, push a new stack into tempStacks to hold the[39;49;00m$
  1315^I[37m                [39;49;00m[37m// future list of headers in the new block.[39;49;00m$
  1316^I[37m[39;49;00m$
  1317^I[37m                [39;49;00m[37m// take care of the special case: 'else if (...)'[39;49;00m$
  1318^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_IF[37m [39;49;00m&&[37m [39;49;00mlastLineHeader[37m [39;49;00m==[37m [39;49;00m&AS_ELSE)[37m[39;49;00m$
  1319^I[37m                  [39;49;00m{[37m[39;49;00m$
  1320^I[37m                    [39;49;00m[37m//spaceTabCount += indentLength; // to counter the opposite addition that occurs when the 'if' is registered below...[39;49;00m$
  1321^I[37m                    [39;49;00mheaderStack->pop_back();[37m[39;49;00m$
  1322^I[37m                  [39;49;00m}[37m[39;49;00m$
  1323^I[37m[39;49;00m$
  1324^I[37m                [39;49;00m[37m// take care of 'else'[39;49;00m$
  1325^I[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_ELSE)[37m[39;49;00m$
  1326^I[37m                  [39;49;00m{[37m[39;49;00m$
  1327^I[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lastTempStack[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1328^I[37m                      [39;49;00m{[37m[39;49;00m$
  1329^I[37m                        [39;49;00m[36mint[39;49;00m[37m [39;49;00mindexOfIf[37m [39;49;00m=[37m [39;49;00mindexOf(*lastTempStack,[37m [39;49;00m&AS_IF);[37m [39;49;00m[37m// <---[39;49;00m$
  1330^I[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(indexOfIf[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
  1331^I[37m                          [39;49;00m{[37m[39;49;00m$
  1332^I[37m                            [39;49;00m[37m// recreate the header list in headerStack up to the previous 'if'[39;49;00m$
  1333^I[37m                            [39;49;00m[37m// from the temporary snapshot stored in lastTempStack.[39;49;00m$
  1334^I[37m                            [39;49;00m[36mint[39;49;00m[37m [39;49;00mrestackSize[37m [39;49;00m=[37m [39;49;00mlastTempStack->size()[37m [39;49;00m-[37m [39;49;00mindexOfIf[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1335^I[37m                            [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mr=[34m0[39;49;00m;[37m [39;49;00mr<restackSize;[37m [39;49;00mr++)[37m[39;49;00m$
  1336^I[37m                              [39;49;00m{[37m[39;49;00m$
  1337^I[37m                                [39;49;00mheaderStack->push_back(lastTempStack->back());[37m[39;49;00m$
  1338^I[37m                                [39;49;00mlastTempStack->pop_back();[37m[39;49;00m$
  1339^I[37m                              [39;49;00m}[37m[39;49;00m$
  1340^I[37m                            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!closingBracketReached)[37m[39;49;00m$
  1341^I[37m                              [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00mrestackSize;[37m[39;49;00m$
  1342^I[37m                          [39;49;00m}[37m[39;49;00m$
  1343^I[37m                        [39;49;00m[37m/*[39;49;00m$
  1344^I[37m                         * If the above if is not true, i.e. no 'if' before the 'else',[39;49;00m$
  1345^I[37m                         * then nothing beautiful will come out of this...[39;49;00m$
  1346^I[37m                         * I should think about inserting an Exception here to notify the caller of this...[39;49;00m$
  1347^I[37m                         */[39;49;00m[37m[39;49;00m$
  1348^I[37m                      [39;49;00m}[37m[39;49;00m$
  1349^I[37m                  [39;49;00m}[37m[39;49;00m$
  1350^I[37m[39;49;00m$
  1351^I[37m                [39;49;00m[37m// check if 'while' closes a previous 'do'[39;49;00m$
  1352^I[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_WHILE)[37m[39;49;00m$
  1353^I[37m                  [39;49;00m{[37m[39;49;00m$
  1354^I[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lastTempStack[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1355^I[37m                      [39;49;00m{[37m[39;49;00m$
  1356^I[37m                        [39;49;00m[36mint[39;49;00m[37m [39;49;00mindexOfDo[37m [39;49;00m=[37m [39;49;00mindexOf(*lastTempStack,[37m [39;49;00m&AS_DO);[37m [39;49;00m[37m// <---[39;49;00m$
  1357^I[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(indexOfDo[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
  1358^I[37m                          [39;49;00m{[37m[39;49;00m$
  1359^I[37m                            [39;49;00m[37m// recreate the header list in headerStack up to the previous 'do'[39;49;00m$
  1360^I[37m                            [39;49;00m[37m// from the temporary snapshot stored in lastTempStack.[39;49;00m$
  1361^I[37m                            [39;49;00m[36mint[39;49;00m[37m [39;49;00mrestackSize[37m [39;49;00m=[37m [39;49;00mlastTempStack->size()[37m [39;49;00m-[37m [39;49;00mindexOfDo[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1362^I[37m                            [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mr=[34m0[39;49;00m;[37m [39;49;00mr<restackSize;[37m [39;49;00mr++)[37m[39;49;00m$
  1363^I[37m                              [39;49;00m{[37m[39;49;00m$
  1364^I[37m                                [39;49;00mheaderStack->push_back(lastTempStack->back());[37m[39;49;00m$
  1365^I[37m                                [39;49;00mlastTempStack->pop_back();[37m[39;49;00m$
  1366^I[37m                              [39;49;00m}[37m[39;49;00m$
  1367^I[37m                            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!closingBracketReached)[37m[39;49;00m$
  1368^I[37m                              [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00mrestackSize;[37m[39;49;00m$
  1369^I[37m                          [39;49;00m}[37m[39;49;00m$
  1370^I[37m                      [39;49;00m}[37m[39;49;00m$
  1371^I[37m                  [39;49;00m}[37m[39;49;00m$
  1372^I[37m                [39;49;00m[37m// check if 'catch' closes a previous 'try' or 'catch'[39;49;00m$
  1373^I[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_CATCH[37m [39;49;00m||[37m [39;49;00mnewHeader[37m [39;49;00m==[37m [39;49;00m&AS_FINALLY)[37m[39;49;00m$
  1374^I[37m                  [39;49;00m{[37m[39;49;00m$
  1375^I[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lastTempStack[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1376^I[37m                      [39;49;00m{[37m[39;49;00m$
  1377^I[37m                        [39;49;00m[36mint[39;49;00m[37m [39;49;00mindexOfTry[37m [39;49;00m=[37m [39;49;00mindexOf(*lastTempStack,[37m [39;49;00m&AS_TRY);[37m[39;49;00m$
  1378^I[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(indexOfTry[37m [39;49;00m==[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
  1379^I[37m                          [39;49;00mindexOfTry[37m [39;49;00m=[37m [39;49;00mindexOf(*lastTempStack,[37m [39;49;00m&AS_CATCH);[37m[39;49;00m$
  1380^I[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(indexOfTry[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
  1381^I[37m                          [39;49;00m{[37m[39;49;00m$
  1382^I[37m                            [39;49;00m[37m// recreate the header list in headerStack up to the previous 'try'[39;49;00m$
  1383^I[37m                            [39;49;00m[37m// from the temporary snapshot stored in lastTempStack.[39;49;00m$
  1384^I[37m                            [39;49;00m[36mint[39;49;00m[37m [39;49;00mrestackSize[37m [39;49;00m=[37m [39;49;00mlastTempStack->size()[37m [39;49;00m-[37m [39;49;00mindexOfTry[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1385^I[37m                            [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mr=[34m0[39;49;00m;[37m [39;49;00mr<restackSize;[37m [39;49;00mr++)[37m[39;49;00m$
  1386^I[37m                              [39;49;00m{[37m[39;49;00m$
  1387^I[37m                                [39;49;00mheaderStack->push_back(lastTempStack->back());[37m[39;49;00m$
  1388^I[37m                                [39;49;00mlastTempStack->pop_back();[37m[39;49;00m$
  1389^I[37m                              [39;49;00m}[37m[39;49;00m$
  1390^I[37m[39;49;00m$
  1391^I[37m                            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!closingBracketReached)[37m[39;49;00m$
  1392^I[37m                              [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00mrestackSize;[37m[39;49;00m$
  1393^I[37m                          [39;49;00m}[37m[39;49;00m$
  1394^I[37m                      [39;49;00m}[37m[39;49;00m$
  1395^I[37m                  [39;49;00m}[37m[39;49;00m$
  1396^I[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_CASE)[37m[39;49;00m$
  1397^I[37m                  [39;49;00m{[37m[39;49;00m$
  1398^I[37m                    [39;49;00misInCase[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1399^I[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!caseIndent)[37m[39;49;00m$
  1400^I[37m                      [39;49;00m--tabCount;[37m[39;49;00m$
  1401^I[37m                  [39;49;00m}[37m[39;49;00m$
  1402^I[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_DEFAULT)[37m[39;49;00m$
  1403^I[37m                  [39;49;00m{[37m[39;49;00m$
  1404^I[37m                    [39;49;00misInCase[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1405^I[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!caseIndent)[37m[39;49;00m$
  1406^I[37m                      [39;49;00m--tabCount;[37m[39;49;00m$
  1407^I[37m                  [39;49;00m}[37m[39;49;00m$
  1408^I[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_PUBLIC[37m [39;49;00m||[37m [39;49;00mnewHeader[37m [39;49;00m==[37m [39;49;00m&AS_PROTECTED[37m [39;49;00m||[37m [39;49;00mnewHeader[37m [39;49;00m==[37m [39;49;00m&AS_PRIVATE)[37m[39;49;00m$
  1409^I[37m                  [39;49;00m{[37m[39;49;00m$
  1410^I[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00m!isInClassHeader)[37m[39;49;00m$
  1411^I[37m                      [39;49;00m--tabCount;[37m[39;49;00m$
  1412^I[37m                    [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1413^I[37m                  [39;49;00m}[37m[39;49;00m$
  1414^I[37m                [39;49;00m[37m//else if ((newHeader == &STATIC || newHeader == &SYNCHRONIZED) &&[39;49;00m$
  1415^I[37m                [39;49;00m[37m//         !headerStack->empty() &&[39;49;00m$
  1416^I[37m                [39;49;00m[37m//         (headerStack->back() == &STATIC || headerStack->back() == &SYNCHRONIZED))[39;49;00m$
  1417^I[37m                [39;49;00m[37m//{[39;49;00m$
  1418^I[37m                [39;49;00m[37m//    isIndentableHeader = false;[39;49;00m$
  1419^I[37m                [39;49;00m[37m//}[39;49;00m$
  1420^I[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_STATIC[37m[39;49;00m$
  1421^I[37m                         [39;49;00m||[37m [39;49;00mnewHeader[37m [39;49;00m==[37m [39;49;00m&AS_SYNCHRONIZED[37m[39;49;00m$
  1422^I[37m                         [39;49;00m||[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_CONST[37m [39;49;00m&&[37m [39;49;00misCStyle))[37m[39;49;00m$
  1423^I[37m                  [39;49;00m{[37m[39;49;00m$
  1424^I[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!headerStack->empty()[37m [39;49;00m&&[37m[39;49;00m$
  1425^I[37m                        [39;49;00m(headerStack->back()[37m [39;49;00m==[37m [39;49;00m&AS_STATIC[37m[39;49;00m$
  1426^I[37m                         [39;49;00m||[37m [39;49;00mheaderStack->back()[37m [39;49;00m==[37m [39;49;00m&AS_SYNCHRONIZED[37m[39;49;00m$
  1427^I[37m                         [39;49;00m||[37m [39;49;00mheaderStack->back()[37m [39;49;00m==[37m [39;49;00m&AS_CONST))[37m[39;49;00m$
  1428^I[37m                      [39;49;00m{[37m[39;49;00m$
  1429^I[37m                        [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1430^I[37m                      [39;49;00m}[37m[39;49;00m$
  1431^I[37m                    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1432^I[37m                      [39;49;00m{[37m[39;49;00m$
  1433^I[37m                        [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1434^I[37m                        [39;49;00mprobationHeader[37m [39;49;00m=[37m [39;49;00mnewHeader;[37m[39;49;00m$
  1435^I[37m                      [39;49;00m}[37m[39;49;00m$
  1436^I[37m                  [39;49;00m}[37m[39;49;00m$
  1437^I[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_CONST)[37m[39;49;00m$
  1438^I[37m                  [39;49;00m{[37m[39;49;00m$
  1439^I[37m                    [39;49;00m[37m// this will be entered only if NOT in C style[39;49;00m$
  1440^I[37m                    [39;49;00m[37m// since otherwise the CONST would be found to be a probstion header...[39;49;00m$
  1441^I[37m[39;49;00m$
  1442^I[37m                    [39;49;00m[37m//if (isCStyle)[39;49;00m$
  1443^I[37m                    [39;49;00m[37m//  isInConst = true;[39;49;00m$
  1444^I[37m                    [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1445^I[37m                  [39;49;00m}[37m[39;49;00m$
  1446^I[37m                [39;49;00m[37m/*[39;49;00m$
  1447^I[37m                              else if (newHeader == &OPERATOR)[39;49;00m$
  1448^I[37m                              {[39;49;00m$
  1449^I[37m                                  if (isCStyle)[39;49;00m$
  1450^I[37m                                      isInOperator = true;[39;49;00m$
  1451^I[37m                                  isIndentableHeader = false;[39;49;00m$
  1452^I[37m                              }[39;49;00m$
  1453^I[37m                */[39;49;00m[37m[39;49;00m$
  1454^I[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_TEMPLATE)[37m[39;49;00m$
  1455^I[37m                  [39;49;00m{[37m[39;49;00m$
  1456^I[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle)[37m[39;49;00m$
  1457^I[37m                      [39;49;00misInTemplate[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1458^I[37m                    [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1459^I[37m                  [39;49;00m}[37m[39;49;00m$
  1460^I[37m[39;49;00m$
  1461^I[37m[39;49;00m$
  1462^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isIndentableHeader)[37m[39;49;00m$
  1463^I[37m                  [39;49;00m{[37m[39;49;00m$
  1464^I[37m                    [39;49;00m[37m// 3.2.99[39;49;00m$
  1465^I[37m                    [39;49;00m[37m//spaceTabCount-=indentLength;[39;49;00m$
  1466^I[37m                    [39;49;00mheaderStack->push_back(newHeader);[37m[39;49;00m$
  1467^I[37m                    [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1468^I[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(indexOf(nonParenHeaders,[37m [39;49;00mnewHeader)[37m [39;49;00m==[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
  1469^I[37m                      [39;49;00m{[37m[39;49;00m$
  1470^I[37m                        [39;49;00misInConditional[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1471^I[37m                      [39;49;00m}[37m[39;49;00m$
  1472^I[37m                    [39;49;00mlastLineHeader[37m [39;49;00m=[37m [39;49;00mnewHeader;[37m[39;49;00m$
  1473^I[37m                  [39;49;00m}[37m[39;49;00m$
  1474^I[37m                [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1475^I[37m                  [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1476^I[37m[39;49;00m$
  1477^I[37m                [39;49;00m[37m//lastLineHeader = newHeader;[39;49;00m$
  1478^I[37m[39;49;00m$
  1479^I[37m                [39;49;00moutBuffer.append(newHeader->substr([34m1[39;49;00m));[37m[39;49;00m$
  1480^I[37m                [39;49;00mi[37m [39;49;00m+=[37m [39;49;00mnewHeader->length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1481^I[37m[39;49;00m$
  1482^I[37m                [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1483^I[37m              [39;49;00m}[37m[39;49;00m$
  1484^I[37m          [39;49;00m}[37m[39;49;00m$
  1485^I[37m[39;49;00m$
  1486^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00m!isalpha(prevCh)[37m[39;49;00m$
  1487^I[37m            [39;49;00m&&[37m [39;49;00mline.COMPARE(i,[37m [39;49;00m[34m8[39;49;00m,[37m [39;49;00mAS_OPERATOR)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m!isalnum(line[i+[34m8[39;49;00m]))[37m[39;49;00m$
  1488^I[37m          [39;49;00m{[37m[39;49;00m$
  1489^I[37m            [39;49;00misInOperator[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1490^I[37m            [39;49;00moutBuffer.append(AS_OPERATOR.substr([34m1[39;49;00m));[37m[39;49;00m$
  1491^I[37m            [39;49;00mi[37m [39;49;00m+=[37m [39;49;00m[34m7[39;49;00m;[37m[39;49;00m$
  1492^I[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1493^I[37m          [39;49;00m}[37m[39;49;00m$
  1494^I[37m[39;49;00m$
  1495^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m?[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1496^I[37m          [39;49;00misInQuestion[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1497^I[37m[39;49;00m$
  1498^I[37m[39;49;00m$
  1499^I[37m        [39;49;00m[37m// special handling of 'case' statements[39;49;00m$
  1500^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1501^I[37m          [39;49;00m{[37m[39;49;00m$
  1502^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.length()[37m [39;49;00m>[37m [39;49;00mi+[34m1[39;49;00m[37m [39;49;00m&&[37m [39;49;00mline[i+[34m1[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m)[37m [39;49;00m[37m// look for ::[39;49;00m$
  1503^I[37m              [39;49;00m{[37m[39;49;00m$
  1504^I[37m                [39;49;00m++i;[37m[39;49;00m$
  1505^I[37m                [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
  1506^I[37m                [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
  1507^I[37m                [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1508^I[37m              [39;49;00m}[37m[39;49;00m$
  1509^I[37m[39;49;00m$
  1510^I[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00misInClass[37m [39;49;00m&&[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m!=[37m [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1511^I[37m              [39;49;00m{[37m[39;49;00m$
  1512^I[37m              [39;49;00m[37m// BEGIN Content of ASBeautifier.cpp.BITFIELD.patch:[39;49;00m$
  1513^I[37m              [39;49;00m[37m[39;49;00m$
  1514^I[37m                [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mchIndex;[37m[39;49;00m$
  1515^I[37m   ^I^I^I    [39;49;00m[36mchar[39;49;00m[37m [39;49;00mnextCh[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  1516^I[37m                [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(chIndex[37m [39;49;00m=[37m [39;49;00mi+[34m1[39;49;00m;[37m [39;49;00mchIndex[37m [39;49;00m<[37m [39;49;00mline.length();[37m [39;49;00mchIndex++)[37m[39;49;00m$
  1517^I[37m            ^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[chIndex]))[37m[39;49;00m$
  1518^I[37m^I^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1519^I[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(chIndex<[37m [39;49;00mline.length())[37m[39;49;00m$
  1520^I[37m       ^I^I^I^I^I[39;49;00mnextCh[37m [39;49;00m=[37m [39;49;00mline[chIndex];[37m[39;49;00m$
  1521^I[37m^I^I^I^I[39;49;00m[36mint[39;49;00m[37m [39;49;00mnWord[37m [39;49;00m=[34m0[39;49;00m;[37m[39;49;00m$
  1522^I[37m    ^I^I^I[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(chIndex[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mchIndex[37m [39;49;00m<[37m [39;49;00mi;[37m [39;49;00mchIndex++)[37m[39;49;00m$
  1523^I[37m^I^I^I^I[39;49;00m{[37m[39;49;00m$
  1524^I[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[chIndex]))[37m[39;49;00m$
  1525^I[37m^I^I^I^I^I[39;49;00m{[37m[39;49;00m$
  1526^I[37m^I^I^I^I^I^I[39;49;00mnWord[37m [39;49;00m++;[37m[39;49;00m$
  1527^I[37m^I^I^I^I^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[++chIndex]));[37m[39;49;00m$
  1528^I[37m^I^I^I^I^I[39;49;00m}[37m^I^I^I^I^I^I^I^I^I[39;49;00m[37m[39;49;00m$
  1529^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1530^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((nextCh[37m [39;49;00m>=[37m [39;49;00m[33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00mnextCh[37m [39;49;00m<=[37m [39;49;00m[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m)[37m [39;49;00m||[37m [39;49;00m(nWord[37m [39;49;00m>[34m1[39;49;00m))[37m[39;49;00m$
  1531^I[37m^I^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1532^I[37m              [39;49;00m[37m// END Content of ASBeautifier.cpp.BITFIELD.patch:[39;49;00m$
  1533^I[37m                [39;49;00m[37m[39;49;00m$
  1534^I[37m                [39;49;00m--tabCount;[37m[39;49;00m$
  1535^I[37m                [39;49;00m[37m// found a 'private:' or 'public:' inside a class definition[39;49;00m$
  1536^I[37m                [39;49;00m[37m// so do nothing special[39;49;00m$
  1537^I[37m              [39;49;00m}[37m[39;49;00m$
  1538^I[37m[39;49;00m$
  1539^I[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00misInClassHeader)[37m[39;49;00m$
  1540^I[37m              [39;49;00m{[37m[39;49;00m$
  1541^I[37m[39;49;00m$
  1542^I[37m                [39;49;00m[37m// found a 'class A : public B' definition[39;49;00m$
  1543^I[37m                [39;49;00m[37m// so do nothing special[39;49;00m$
  1544^I[37m              [39;49;00m}[37m[39;49;00m$
  1545^I[37m[39;49;00m$
  1546^I[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInQuestion)[37m[39;49;00m$
  1547^I[37m              [39;49;00m{[37m[39;49;00m$
  1548^I[37m                [39;49;00misInQuestion[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1549^I[37m              [39;49;00m}[37m[39;49;00m$
  1550^I[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1551^I[37m              [39;49;00m{[37m[39;49;00m$
  1552^I[37m                [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1553^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i==[34m0[39;49;00m)[37m[39;49;00m$
  1554^I[37m                  [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m$
  1555^I[37m              [39;49;00m}[37m[39;49;00m$
  1556^I[37m            [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1557^I[37m              [39;49;00m{[37m[39;49;00m$
  1558^I[37m                [39;49;00mcurrentNonSpaceCh[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m;[37m [39;49;00m[37m// so that brackets after the ':' will appear as block-openers[39;49;00m$
  1559^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInCase)[37m[39;49;00m$
  1560^I[37m                  [39;49;00m{[37m[39;49;00m$
  1561^I[37m                    [39;49;00misInCase[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1562^I[37m                    [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m;[37m [39;49;00m[37m// from here on, treat char as ';'[39;49;00m$
  1563^I[37m                  [39;49;00m}[37m [39;49;00m[37m[39;49;00m$
  1564^I[37m              [39;49;00m[37m// BEGIN content of ASBeautifier.cpp.BITFIELD.patch.bz2[39;49;00m$
  1565^I[37m              [39;49;00m[34melse[39;49;00m[37m [39;49;00m[37m// bitfield or labels[39;49;00m$
  1566^I[37m^I^I^I^I^I^I^I^I[39;49;00m{[37m[39;49;00m$
  1567^I[37m^I^I^I^I[39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mchIndex;[37m[39;49;00m$
  1568^I[37m^I^I^I^I[39;49;00m[36mchar[39;49;00m[37m [39;49;00mnextCh[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  1569^I[37m^I^I^I^I[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(chIndex[37m [39;49;00m=[37m [39;49;00mi+[34m1[39;49;00m;[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00mchIndex[37m [39;49;00m<[37m [39;49;00mline.length());[37m [39;49;00mchIndex++)[37m[39;49;00m$
  1570^I[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[chIndex]))[37m[39;49;00m$
  1571^I[37m^I^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1572^I[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(chIndex<[37m [39;49;00mline.length())[37m[39;49;00m$
  1573^I[37m^I^I^I^I^I[39;49;00mnextCh[37m [39;49;00m=[37m [39;49;00mline[chIndex];[37m[39;49;00m$
  1574^I[37m[39;49;00m$
  1575^I[37m     ^I^I^I[39;49;00m[36mint[39;49;00m[37m [39;49;00mnWord[37m [39;49;00m=[34m0[39;49;00m;[37m[39;49;00m$
  1576^I[37m ^I^I^I^I[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(chIndex[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mchIndex[37m [39;49;00m<[37m [39;49;00mi;[37m [39;49;00mchIndex++)[37m[39;49;00m$
  1577^I[37m^I^I^I^I[39;49;00m{[37m[39;49;00m$
  1578^I[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[chIndex]))[37m[39;49;00m$
  1579^I[37m^I^I^I^I^I[39;49;00m{[37m[39;49;00m$
  1580^I[37m^I^I^I^I^I^I[39;49;00mnWord[37m [39;49;00m++;[37m[39;49;00m$
  1581^I[37m^I^I^I^I^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[++chIndex]));[37m[39;49;00m$
  1582^I[37m^I^I^I^I^I[39;49;00m}[37m^I^I^I^I^I^I^I^I^I[39;49;00m[37m[39;49;00m$
  1583^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1584^I[37m         ^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m  [39;49;00m(nextCh[37m [39;49;00m>=[37m [39;49;00m[33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00mnextCh[37m [39;49;00m<=[37m [39;49;00m[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m)[37m [39;49;00m||[37m [39;49;00m(nWord[37m [39;49;00m>[34m1[39;49;00m))[37m[39;49;00m$
  1585^I[37m^I^I^I^I[39;49;00m{[37m[39;49;00m$
  1586^I[37m^I^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1587^I[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
  1588^I[37m                [39;49;00m[37m// END content of ASASBeautifier.cpp.BITFIELD.patch.bz2[39;49;00m$
  1589^I[37m[39;49;00m$
  1590^I[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[37m// is in a label (e.g. 'label1:')[39;49;00m$
  1591^I[37m                  [39;49;00m{[37m[39;49;00m$
  1592^I[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(labelIndent)[37m[39;49;00m$
  1593^I[37m                      [39;49;00m--tabCount;[37m [39;49;00m[37m// unindent label by one indent[39;49;00m$
  1594^I[37m                    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1595^I[37m                      [39;49;00mtabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00m[37m// completely flush indent to left[39;49;00m$
  1596^I[37m                  [39;49;00m}[37m[39;49;00m$
  1597^I[37m[39;49;00m$
  1598^I[37m              [39;49;00m[37m// BEGIN content of ASASBeautifier.cpp.BITFIELD.patch.bz2[39;49;00m$
  1599^I[37m                [39;49;00m}[37m[39;49;00m$
  1600^I[37m            [39;49;00m[37m// END content of ASASBeautifier.cpp.BITFIELD.patch.bz2[39;49;00m$
  1601^I[37m[39;49;00m$
  1602^I[37m              [39;49;00m}[37m[39;49;00m$
  1603^I[37m          [39;49;00m}[37m[39;49;00m$
  1604^I[37m[39;49;00m$
  1605^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m((ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m[37m  [39;49;00m||[37m [39;49;00m(parenDepth>[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m,[39;49;00m[33m'[39;49;00m))[37m  [39;49;00m&&[37m [39;49;00m!inStatementIndentStackSizeStack->empty())[37m[39;49;00m$
  1606^I[37m          [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m)inStatementIndentStackSizeStack->back()[37m [39;49;00m+[37m [39;49;00m(parenDepth>[34m0[39;49;00m[37m [39;49;00m?[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m:[37m [39;49;00m[34m0[39;49;00m)[37m  [39;49;00m<[37m [39;49;00minStatementIndentStack->size())[37m[39;49;00m$
  1607^I[37m            [39;49;00minStatementIndentStack->pop_back();[37m[39;49;00m$
  1608^I[37m[39;49;00m$
  1609^I[37m[39;49;00m$
  1610^I[37m        [39;49;00m[37m// handle ends of statements[39;49;00m$
  1611^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00mparenDepth[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m[37m/* || (ch == ',' && parenDepth == 0)*/[39;49;00m)[37m[39;49;00m$
  1612^I[37m          [39;49;00m{[37m[39;49;00m$
  1613^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1614^I[37m              [39;49;00m{[37m[39;49;00m$
  1615^I[37m                [39;49;00m[37m// first check if this '}' closes a previous block, or a static array...[39;49;00m$
  1616^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!bracketBlockStateStack->empty())[37m[39;49;00m$
  1617^I[37m                  [39;49;00m{[37m[39;49;00m$
  1618^I[37m                    [39;49;00m[36mbool[39;49;00m[37m [39;49;00mbracketBlockState[37m [39;49;00m=[37m [39;49;00mbracketBlockStateStack->back();[37m[39;49;00m$
  1619^I[37m                    [39;49;00mbracketBlockStateStack->pop_back();[37m[39;49;00m$
  1620^I[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!bracketBlockState)[37m[39;49;00m$
  1621^I[37m                      [39;49;00m{[37m[39;49;00m$
  1622^I[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStackSizeStack->empty())[37m[39;49;00m$
  1623^I[37m                          [39;49;00m{[37m[39;49;00m$
  1624^I[37m                            [39;49;00m[37m// this bracket is a static array[39;49;00m$
  1625^I[37m[39;49;00m$
  1626^I[37m                            [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mpreviousIndentStackSize[37m [39;49;00m=[37m [39;49;00minStatementIndentStackSizeStack->back();[37m[39;49;00m$
  1627^I[37m                            [39;49;00minStatementIndentStackSizeStack->pop_back();[37m[39;49;00m$
  1628^I[37m                            [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(previousIndentStackSize[37m [39;49;00m<[37m [39;49;00minStatementIndentStack->size())[37m[39;49;00m$
  1629^I[37m                              [39;49;00minStatementIndentStack->pop_back();[37m[39;49;00m$
  1630^I[37m                            [39;49;00mparenDepth--;[37m[39;49;00m$
  1631^I[37m                            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1632^I[37m                              [39;49;00mshouldIndentBrackettedLine[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1633^I[37m[39;49;00m$
  1634^I[37m                            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!parenIndentStack->empty())[37m[39;49;00m$
  1635^I[37m                              [39;49;00m{[37m[39;49;00m$
  1636^I[37m                                [39;49;00m[36mint[39;49;00m[37m [39;49;00mpoppedIndent[37m [39;49;00m=[37m [39;49;00mparenIndentStack->back();[37m[39;49;00m$
  1637^I[37m                                [39;49;00mparenIndentStack->pop_back();[37m[39;49;00m$
  1638^I[37m                                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1639^I[37m                                  [39;49;00mspaceTabCount[37m [39;49;00m=[37m [39;49;00mpoppedIndent;[37m[39;49;00m$
  1640^I[37m                              [39;49;00m}[37m[39;49;00m$
  1641^I[37m                          [39;49;00m}[37m[39;49;00m$
  1642^I[37m                        [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1643^I[37m                      [39;49;00m}[37m[39;49;00m$
  1644^I[37m                  [39;49;00m}[37m[39;49;00m$
  1645^I[37m[39;49;00m$
  1646^I[37m                [39;49;00m[37m// this bracket is block closer...[39;49;00m$
  1647^I[37m[39;49;00m$
  1648^I[37m                [39;49;00m++lineClosingBlocksNum;[37m[39;49;00m$
  1649^I[37m[39;49;00m$
  1650^I[37m                [39;49;00m[34mif[39;49;00m(!inStatementIndentStackSizeStack->empty())[37m[39;49;00m$
  1651^I[37m                  [39;49;00minStatementIndentStackSizeStack->pop_back();[37m[39;49;00m$
  1652^I[37m[39;49;00m$
  1653^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!blockParenDepthStack->empty())[37m[39;49;00m$
  1654^I[37m                  [39;49;00m{[37m[39;49;00m$
  1655^I[37m                    [39;49;00mparenDepth[37m [39;49;00m=[37m [39;49;00mblockParenDepthStack->back();[37m[39;49;00m$
  1656^I[37m                    [39;49;00mblockParenDepthStack->pop_back();[37m[39;49;00m$
  1657^I[37m                    [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00mblockStatementStack->back();[37m[39;49;00m$
  1658^I[37m                    [39;49;00mblockStatementStack->pop_back();[37m[39;49;00m$
  1659^I[37m[39;49;00m$
  1660^I[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInStatement)[37m[39;49;00m$
  1661^I[37m                      [39;49;00mblockTabCount--;[37m[39;49;00m$
  1662^I[37m                  [39;49;00m}[37m[39;49;00m$
  1663^I[37m[39;49;00m$
  1664^I[37m                [39;49;00mclosingBracketReached[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1665^I[37m                [39;49;00m[36mint[39;49;00m[37m [39;49;00mheaderPlace[37m [39;49;00m=[37m [39;49;00mindexOf(*headerStack,[37m [39;49;00m&AS_OPEN_BRACKET);[37m [39;49;00m[37m// <---[39;49;00m$
  1666^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(headerPlace[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
  1667^I[37m                  [39;49;00m{[37m[39;49;00m$
  1668^I[37m                    [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*popped[37m [39;49;00m=[37m [39;49;00mheaderStack->back();[37m[39;49;00m$
  1669^I[37m                    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(popped[37m [39;49;00m!=[37m [39;49;00m&AS_OPEN_BRACKET)[37m[39;49;00m$
  1670^I[37m                      [39;49;00m{[37m[39;49;00m$
  1671^I[37m                        [39;49;00mheaderStack->pop_back();[37m[39;49;00m$
  1672^I[37m                        [39;49;00mpopped[37m [39;49;00m=[37m [39;49;00mheaderStack->back();[37m[39;49;00m$
  1673^I[37m                      [39;49;00m}[37m[39;49;00m$
  1674^I[37m                    [39;49;00mheaderStack->pop_back();[37m[39;49;00m$
  1675^I[37m[39;49;00m$
  1676^I[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!tempStacks->empty())[37m[39;49;00m$
  1677^I[37m                      [39;49;00m{[37m[39;49;00m$
  1678^I[37m                        [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m*temp[37m [39;49;00m=[37m  [39;49;00mtempStacks->back();[37m[39;49;00m$
  1679^I[37m                        [39;49;00mtempStacks->pop_back();[37m[39;49;00m$
  1680^I[37m                        [39;49;00m[34mdelete[39;49;00m[37m [39;49;00mtemp;[37m[39;49;00m$
  1681^I[37m                      [39;49;00m}[37m[39;49;00m$
  1682^I[37m                  [39;49;00m}[37m[39;49;00m$
  1683^I[37m[39;49;00m$
  1684^I[37m[39;49;00m$
  1685^I[37m                [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m;[37m [39;49;00m[37m// needed due to cases such as '}else{', so that headers ('else' tn tih case) will be identified...[39;49;00m$
  1686^I[37m              [39;49;00m}[37m[39;49;00m$
  1687^I[37m[39;49;00m$
  1688^I[37m            [39;49;00m[37m/*[39;49;00m$
  1689^I[37m             * Create a temporary snapshot of the current block's header-list in the[39;49;00m$
  1690^I[37m             * uppermost inner stack in tempStacks, and clear the headerStack up to[39;49;00m$
  1691^I[37m             * the begining of the block.[39;49;00m$
  1692^I[37m             * Thus, the next future statement will think it comes one indent past[39;49;00m$
  1693^I[37m             * the block's '{' unless it specifically checks for a companion-header[39;49;00m$
  1694^I[37m             * (such as a previous 'if' for an 'else' header) within the tempStacks,[39;49;00m$
  1695^I[37m             * and recreates the temporary snapshot by manipulating the tempStacks.[39;49;00m$
  1696^I[37m             */[39;49;00m[37m[39;49;00m$
  1697^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!tempStacks->back()->empty())[37m[39;49;00m$
  1698^I[37m              [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(!tempStacks->back()->empty())[37m[39;49;00m$
  1699^I[37m                [39;49;00mtempStacks->back()->pop_back();[37m[39;49;00m$
  1700^I[37m            [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(!headerStack->empty()[37m [39;49;00m&&[37m [39;49;00mheaderStack->back()[37m [39;49;00m!=[37m [39;49;00m&AS_OPEN_BRACKET)[37m[39;49;00m$
  1701^I[37m              [39;49;00m{[37m[39;49;00m$
  1702^I[37m                [39;49;00mtempStacks->back()->push_back(headerStack->back());[37m[39;49;00m$
  1703^I[37m                [39;49;00mheaderStack->pop_back();[37m[39;49;00m$
  1704^I[37m              [39;49;00m}[37m[39;49;00m$
  1705^I[37m[39;49;00m$
  1706^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(parenDepth[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1707^I[37m              [39;49;00misInStatement=[36mfalse[39;49;00m;[37m[39;49;00m$
  1708^I[37m[39;49;00m$
  1709^I[37m            [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1710^I[37m[39;49;00m$
  1711^I[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1712^I[37m          [39;49;00m}[37m[39;49;00m$
  1713^I[37m[39;49;00m$
  1714^I[37m[39;49;00m$
  1715^I[37m        [39;49;00m[37m// check for preBlockStatements ONLY if not within parenthesies[39;49;00m$
  1716^I[37m        [39;49;00m[37m// (otherwise 'struct XXX' statements would be wrongly interpreted...)[39;49;00m$
  1717^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(prevCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00m!isInTemplate[37m [39;49;00m&&[37m [39;49;00mparenDepth[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1718^I[37m          [39;49;00m{[37m[39;49;00m$
  1719^I[37m            [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*newHeader[37m [39;49;00m=[37m [39;49;00mfindHeader(line,[37m [39;49;00mi,[37m [39;49;00mpreBlockStatements);[37m[39;49;00m$
  1720^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1721^I[37m              [39;49;00m{[37m[39;49;00m$
  1722^I[37m                [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1723^I[37m                [39;49;00moutBuffer.append(newHeader->substr([34m1[39;49;00m));[37m[39;49;00m$
  1724^I[37m                [39;49;00mi[37m [39;49;00m+=[37m [39;49;00mnewHeader->length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1725^I[37m                [39;49;00m[37m//if (isCStyle)[39;49;00m$
  1726^I[37m                [39;49;00mheaderStack->push_back(newHeader);[37m[39;49;00m$
  1727^I[37m              [39;49;00m}[37m[39;49;00m$
  1728^I[37m          [39;49;00m}[37m[39;49;00m$
  1729^I[37m[39;49;00m$
  1730^I[37m        [39;49;00m[37m// Handle operators[39;49;00m$
  1731^I[37m        [39;49;00m[37m//[39;49;00m$
  1732^I[37m[39;49;00m$
  1733^I[37m        [39;49;00m[37m////        // PRECHECK if a '==' or '--' or '++' operator was reached.[39;49;00m$
  1734^I[37m        [39;49;00m[37m////        // If not, then register an indent IF an assignment operator was reached.[39;49;00m$
  1735^I[37m        [39;49;00m[37m////        // The precheck is important, so that statements such as 'i--==2' are not recognized[39;49;00m$
  1736^I[37m        [39;49;00m[37m////        // to have assignment operators (here, '-=') in them . . .[39;49;00m$
  1737^I[37m[39;49;00m$
  1738^I[37m        [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*foundAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1739^I[37m        [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*foundNonAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1740^I[37m[39;49;00m$
  1741^I[37m        [39;49;00mimmediatelyPreviousAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1742^I[37m[39;49;00m$
  1743^I[37m        [39;49;00m[37m// Check if an operator has been reached.[39;49;00m$
  1744^I[37m        [39;49;00mfoundAssignmentOp[37m [39;49;00m=[37m [39;49;00mfindHeader(line,[37m [39;49;00mi,[37m [39;49;00massignmentOperators,[37m [39;49;00m[36mfalse[39;49;00m);[37m[39;49;00m$
  1745^I[37m        [39;49;00mfoundNonAssignmentOp[37m [39;49;00m=[37m [39;49;00mfindHeader(line,[37m [39;49;00mi,[37m [39;49;00mnonAssignmentOperators,[37m [39;49;00m[36mfalse[39;49;00m);[37m[39;49;00m$
  1746^I[37m[39;49;00m$
  1747^I[37m        [39;49;00m[37m// Since findHeader's boundry checking was not used above, it is possible[39;49;00m$
  1748^I[37m        [39;49;00m[37m// that both an assignment op and a non-assignment op where found,[39;49;00m$
  1749^I[37m        [39;49;00m[37m// e.g. '>>' and '>>='. If this is the case, treat the LONGER one as the[39;49;00m$
  1750^I[37m        [39;49;00m[37m// found operator.[39;49;00m$
  1751^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundAssignmentOp[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00mfoundNonAssignmentOp[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1752^I[37m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundAssignmentOp->length()[37m [39;49;00m<[37m [39;49;00mfoundNonAssignmentOp->length())[37m[39;49;00m$
  1753^I[37m            [39;49;00mfoundAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1754^I[37m          [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1755^I[37m            [39;49;00mfoundNonAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1756^I[37m[39;49;00m$
  1757^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundNonAssignmentOp[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1758^I[37m          [39;49;00m{[37m[39;49;00m$
  1759^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundNonAssignmentOp->length()[37m [39;49;00m>[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  1760^I[37m              [39;49;00m{[37m[39;49;00m$
  1761^I[37m                [39;49;00moutBuffer.append(foundNonAssignmentOp->substr([34m1[39;49;00m));[37m[39;49;00m$
  1762^I[37m                [39;49;00mi[37m [39;49;00m+=[37m [39;49;00mfoundNonAssignmentOp->length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1763^I[37m              [39;49;00m}[37m[39;49;00m$
  1764^I[37m          [39;49;00m}[37m[39;49;00m$
  1765^I[37m[39;49;00m$
  1766^I[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundAssignmentOp[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1767^I[37m[39;49;00m$
  1768^I[37m          [39;49;00m{[37m[39;49;00m$
  1769^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundAssignmentOp->length()[37m [39;49;00m>[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  1770^I[37m              [39;49;00m{[37m[39;49;00m$
  1771^I[37m                [39;49;00moutBuffer.append(foundAssignmentOp->substr([34m1[39;49;00m));[37m[39;49;00m$
  1772^I[37m                [39;49;00mi[37m [39;49;00m+=[37m [39;49;00mfoundAssignmentOp->length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1773^I[37m              [39;49;00m}[37m[39;49;00m$
  1774^I[37m[39;49;00m$
  1775^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInOperator[37m [39;49;00m&&[37m [39;49;00m!isInTemplate)[37m[39;49;00m$
  1776^I[37m              [39;49;00m{[37m[39;49;00m$
  1777^I[37m                [39;49;00mregisterInStatementIndent(line,[37m [39;49;00mi,[37m [39;49;00mspaceTabCount,[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00m[36mfalse[39;49;00m);[37m[39;49;00m$
  1778^I[37m                [39;49;00mimmediatelyPreviousAssignmentOp[37m [39;49;00m=[37m [39;49;00mfoundAssignmentOp;[37m[39;49;00m$
  1779^I[37m                [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1780^I[37m              [39;49;00m}[37m[39;49;00m$
  1781^I[37m          [39;49;00m}[37m[39;49;00m$
  1782^I[37m[39;49;00m$
  1783^I[37m        [39;49;00m[37m/*[39;49;00m$
  1784^I[37m                immediatelyPreviousAssignmentOp = NULL;[39;49;00m$
  1785^I[37m                bool isNonAssingmentOperator = false;[39;49;00m$
  1786^I[37m                for (int n = 0; n < nonAssignmentOperators.size(); n++)[39;49;00m$
  1787^I[37m                    if (line.COMPARE(i, nonAssignmentOperators[n]->length(), *(nonAssignmentOperators[n])) == 0)[39;49;00m$
  1788^I[37m                    {[39;49;00m$
  1789^I[37m                        if (nonAssignmentOperators[n]->length() > 1)[39;49;00m$
  1790^I[37m                        {[39;49;00m$
  1791^I[37m                            outBuffer.append(nonAssignmentOperators[n]->substr(1));[39;49;00m$
  1792^I[37m                            i += nonAssignmentOperators[n]->length() - 1;[39;49;00m$
  1793^I[37m                        }[39;49;00m$
  1794^I[37m                        isNonAssingmentOperator = true;[39;49;00m$
  1795^I[37m                        break;[39;49;00m$
  1796^I[37m                    }[39;49;00m$
  1797^I[37m                if (!isNonAssingmentOperator)[39;49;00m$
  1798^I[37m                {[39;49;00m$
  1799^I[37m                    for (int a = 0; a < assignmentOperators.size(); a++)[39;49;00m$
  1800^I[37m                        if (line.COMPARE(i, assignmentOperators[a]->length(), *(assignmentOperators[a])) == 0)[39;49;00m$
  1801^I[37m                        {[39;49;00m$
  1802^I[37m                            if (assignmentOperators[a]->length() > 1)[39;49;00m$
  1803^I[37m                            {[39;49;00m$
  1804^I[37m                                outBuffer.append(assignmentOperators[a]->substr(1));[39;49;00m$
  1805^I[37m                                i += assignmentOperators[a]->length() - 1;[39;49;00m$
  1806^I[37m                            }[39;49;00m$
  1807^I[37m         [39;49;00m$
  1808^I[37m                            if (!isInOperator && !isInTemplate)[39;49;00m$
  1809^I[37m                            {[39;49;00m$
  1810^I[37m                                registerInStatementIndent(line, i, spaceTabCount, 0, false);[39;49;00m$
  1811^I[37m                                immediatelyPreviousAssignmentOp = assignmentOperators[a];[39;49;00m$
  1812^I[37m                                isInStatement = true;[39;49;00m$
  1813^I[37m                            }[39;49;00m$
  1814^I[37m                            break;[39;49;00m$
  1815^I[37m                        }[39;49;00m$
  1816^I[37m                }[39;49;00m$
  1817^I[37m        */[39;49;00m[37m[39;49;00m$
  1818^I[37m[39;49;00m$
  1819^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInOperator)[37m[39;49;00m$
  1820^I[37m          [39;49;00misInOperator[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1821^I[37m      [39;49;00m}[37m[39;49;00m$
  1822^I[37m[39;49;00m$
  1823^I[37m    [39;49;00m[37m// handle special cases of unindentation:[39;49;00m$
  1824^I[37m[39;49;00m$
  1825^I[37m    [39;49;00m[37m/*[39;49;00m$
  1826^I[37m     * if '{' doesn't follow an immediately previous '{' in the headerStack[39;49;00m$
  1827^I[37m     * (but rather another header such as "for" or "if", then unindent it[39;49;00m$
  1828^I[37m     * by one indentation relative to its block.[39;49;00m$
  1829^I[37m     */[39;49;00m[37m[39;49;00m$
  1830^I[37m    [39;49;00m[37m//    cerr << endl << lineOpeningBlocksNum << " " <<  lineClosingBlocksNum << " " <<  previousLastLineHeader << endl;[39;49;00m$
  1831^I[37m[39;49;00m$
  1832^I[37m    [39;49;00m[37m// indent #define lines with one less tab[39;49;00m$
  1833^I[37m    [39;49;00m[37m//if (isInDefine)[39;49;00m$
  1834^I[37m    [39;49;00m[37m//    tabCount -= defineTabCount-1;[39;49;00m$
  1835^I[37m[39;49;00m$
  1836^I[37m[39;49;00m$
  1837^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!lineStartsInComment[37m[39;49;00m$
  1838^I[37m        [39;49;00m&&[37m [39;49;00m!blockIndent[37m[39;49;00m$
  1839^I[37m        [39;49;00m&&[37m [39;49;00moutBuffer.length()>[34m0[39;49;00m[37m[39;49;00m$
  1840^I[37m        [39;49;00m&&[37m [39;49;00moutBuffer[[34m0[39;49;00m]==[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
  1841^I[37m        [39;49;00m&&[37m [39;49;00m!(lineOpeningBlocksNum[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mlineOpeningBlocksNum[37m [39;49;00m==[37m [39;49;00mlineClosingBlocksNum)[37m[39;49;00m$
  1842^I[37m        [39;49;00m&&[37m [39;49;00m!(headerStack->size()[37m [39;49;00m>[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(*headerStack)[headerStack->size()[34m-2[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET)[37m[39;49;00m$
  1843^I[37m        [39;49;00m&&[37m [39;49;00mshouldIndentBrackettedLine)[37m[39;49;00m$
  1844^I[37m      [39;49;00m--tabCount;[37m[39;49;00m$
  1845^I[37m[39;49;00m$
  1846^I[37m    [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!lineStartsInComment[37m[39;49;00m$
  1847^I[37m             [39;49;00m&&[37m [39;49;00moutBuffer.length()>[34m0[39;49;00m[37m[39;49;00m$
  1848^I[37m             [39;49;00m&&[37m [39;49;00moutBuffer[[34m0[39;49;00m]==[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
  1849^I[37m             [39;49;00m&&[37m [39;49;00mshouldIndentBrackettedLine[37m [39;49;00m)[37m[39;49;00m$
  1850^I[37m      [39;49;00m--tabCount;[37m[39;49;00m$
  1851^I[37m[39;49;00m$
  1852^I[37m    [39;49;00m[37m// correctly indent one-line-blocks...[39;49;00m$
  1853^I[37m    [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!lineStartsInComment[37m[39;49;00m$
  1854^I[37m             [39;49;00m&&[37m [39;49;00moutBuffer.length()>[34m0[39;49;00m[37m[39;49;00m$
  1855^I[37m             [39;49;00m&&[37m [39;49;00mlineOpeningBlocksNum[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
  1856^I[37m             [39;49;00m&&[37m [39;49;00mlineOpeningBlocksNum[37m [39;49;00m==[37m [39;49;00mlineClosingBlocksNum[37m[39;49;00m$
  1857^I[37m             [39;49;00m&&[37m [39;49;00mpreviousLastLineHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m[39;49;00m$
  1858^I[37m             [39;49;00m&&[37m [39;49;00mpreviousLastLineHeader[37m [39;49;00m!=[37m [39;49;00m&AS_OPEN_BRACKET)[37m[39;49;00m$
  1859^I[37m      [39;49;00mtabCount[37m [39;49;00m-=[37m [39;49;00m[34m1[39;49;00m;[37m [39;49;00m[37m//lineOpeningBlocksNum - (blockIndent ? 1 : 0);[39;49;00m$
  1860^I[37m[39;49;00m$
  1861^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(tabCount[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1862^I[37m      [39;49;00mtabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  1863^I[37m[39;49;00m$
  1864^I[37m    [39;49;00m[37m// take care of extra bracket indentatation option...[39;49;00m$
  1865^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(bracketIndent[37m [39;49;00m&&[37m [39;49;00moutBuffer.length()>[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mshouldIndentBrackettedLine)[37m[39;49;00m$
  1866^I[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(outBuffer[[34m0[39;49;00m]==[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00moutBuffer[[34m0[39;49;00m]==[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1867^I[37m        [39;49;00mtabCount++;[37m[39;49;00m$
  1868^I[37m[39;49;00m$
  1869^I[37m[39;49;00m$
  1870^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInDefine)[37m[39;49;00m$
  1871^I[37m      [39;49;00m{[37m[39;49;00m$
  1872^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(outBuffer[[34m0[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m#[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1873^I[37m          [39;49;00m{[37m[39;49;00m$
  1874^I[37m            [39;49;00mstring[37m [39;49;00mpreproc[37m [39;49;00m=[37m [39;49;00mtrim(string(outBuffer.c_str()[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m));[37m[39;49;00m$
  1875^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m6[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33mdefine[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1876^I[37m              [39;49;00m{[37m[39;49;00m$
  1877^I[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStack->empty()[37m[39;49;00m$
  1878^I[37m                    [39;49;00m&&[37m [39;49;00minStatementIndentStack->back()[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1879^I[37m                  [39;49;00m{[37m[39;49;00m$
  1880^I[37m                    [39;49;00mdefineTabCount[37m [39;49;00m=[37m [39;49;00mtabCount;[37m[39;49;00m$
  1881^I[37m                  [39;49;00m}[37m[39;49;00m$
  1882^I[37m                [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1883^I[37m                  [39;49;00m{[37m[39;49;00m$
  1884^I[37m                    [39;49;00mdefineTabCount[37m [39;49;00m=[37m [39;49;00mtabCount[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1885^I[37m                    [39;49;00mtabCount--;[37m[39;49;00m$
  1886^I[37m                  [39;49;00m}[37m[39;49;00m$
  1887^I[37m              [39;49;00m}[37m[39;49;00m$
  1888^I[37m          [39;49;00m}[37m[39;49;00m$
  1889^I[37m[39;49;00m$
  1890^I[37m        [39;49;00mtabCount[37m [39;49;00m-=[37m [39;49;00mdefineTabCount;[37m[39;49;00m$
  1891^I[37m      [39;49;00m}[37m[39;49;00m$
  1892^I[37m[39;49;00m$
  1893^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(tabCount[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1894^I[37m      [39;49;00mtabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  1895^I[37m[39;49;00m$
  1896^I[37m[39;49;00m$
  1897^I[37m    [39;49;00m[37m// finally, insert indentations into begining of line[39;49;00m$
  1898^I[37m[39;49;00m$
  1899^I[37m    [39;49;00mprevFinalLineSpaceTabCount[37m [39;49;00m=[37m [39;49;00mspaceTabCount;[37m[39;49;00m$
  1900^I[37m    [39;49;00mprevFinalLineTabCount[37m [39;49;00m=[37m [39;49;00mtabCount;[37m[39;49;00m$
  1901^I[37m[39;49;00m$
  1902^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(shouldForceTabIndentation)[37m[39;49;00m$
  1903^I[37m      [39;49;00m{[37m[39;49;00m$
  1904^I[37m        [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00mspaceTabCount[37m [39;49;00m/[37m [39;49;00mindentLength;[37m[39;49;00m$
  1905^I[37m        [39;49;00mspaceTabCount[37m [39;49;00m=[37m [39;49;00mspaceTabCount[37m [39;49;00m%[37m [39;49;00mindentLength;[37m[39;49;00m$
  1906^I[37m      [39;49;00m}[37m[39;49;00m$
  1907^I[37m[39;49;00m$
  1908^I[37m    [39;49;00moutBuffer[37m [39;49;00m=[37m [39;49;00mpreLineWS(spaceTabCount,tabCount)[37m [39;49;00m+[37m [39;49;00moutBuffer;[37m[39;49;00m$
  1909^I[37m[39;49;00m$
  1910^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lastLineHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1911^I[37m      [39;49;00mpreviousLastLineHeader[37m [39;49;00m=[37m [39;49;00mlastLineHeader;[37m[39;49;00m$
  1912^I[37m[39;49;00m$
  1913^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00moutBuffer;[37m[39;49;00m$
  1914^I[37m  [39;49;00m}[37m[39;49;00m$
  1915^I[37m[39;49;00m$
  1916^I[37m[39;49;00m$
  1917^I[37m  [39;49;00mstring[37m [39;49;00mASBeautifier::preLineWS([36mint[39;49;00m[37m [39;49;00mspaceTabCount,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mtabCount)[37m[39;49;00m$
  1918^I[37m  [39;49;00m{[37m[39;49;00m$
  1919^I[37m    [39;49;00mstring[37m [39;49;00mws;[37m[39;49;00m$
  1920^I[37m[39;49;00m$
  1921^I[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi=[34m0[39;49;00m;[37m [39;49;00mi<tabCount;[37m [39;49;00mi++)[37m[39;49;00m$
  1922^I[37m      [39;49;00mws[37m [39;49;00m+=[37m [39;49;00mindentString;[37m[39;49;00m$
  1923^I[37m[39;49;00m$
  1924^I[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m((spaceTabCount--)[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1925^I[37m      [39;49;00mws[37m [39;49;00m+=[37m [39;49;00mstring([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1926^I[37m[39;49;00m$
  1927^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mws;[37m[39;49;00m$
  1928^I[37m[39;49;00m$
  1929^I[37m  [39;49;00m}[37m[39;49;00m$
  1930^I[37m[39;49;00m$
  1931^I[37m  [39;49;00m[37m/**[39;49;00m$
  1932^I[37m   * register an in-statement indent.[39;49;00m$
  1933^I[37m   */[39;49;00m[37m[39;49;00m$
  1934^I[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::registerInStatementIndent([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mspaceTabCount,[37m[39;49;00m$
  1935^I[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mminIndent,[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mupdateParenStack)[37m[39;49;00m$
  1936^I[37m  [39;49;00m{[37m[39;49;00m$
  1937^I[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00minStatementIndent;[37m[39;49;00m$
  1938^I[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mremainingCharNum[37m [39;49;00m=[37m [39;49;00mline.length()[37m [39;49;00m-[37m [39;49;00mi;[37m[39;49;00m$
  1939^I[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mnextNonWSChar[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1940^I[37m[39;49;00m$
  1941^I[37m    [39;49;00mnextNonWSChar[37m [39;49;00m=[37m [39;49;00mgetNextProgramCharDistance(line,[37m [39;49;00mi);[37m[39;49;00m$
  1942^I[37m[39;49;00m$
  1943^I[37m    [39;49;00m[37m// if indent is around the last char in the line, indent instead 2 spaces from the previous indent[39;49;00m$
  1944^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(nextNonWSChar[37m [39;49;00m==[37m [39;49;00mremainingCharNum)[37m[39;49;00m$
  1945^I[37m      [39;49;00m{[37m[39;49;00m$
  1946^I[37m        [39;49;00m[36mint[39;49;00m[37m [39;49;00mpreviousIndent[37m [39;49;00m=[37m [39;49;00mspaceTabCount;[37m[39;49;00m$
  1947^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStack->empty())[37m[39;49;00m$
  1948^I[37m          [39;49;00mpreviousIndent[37m [39;49;00m=[37m [39;49;00minStatementIndentStack->back();[37m[39;49;00m$
  1949^I[37m[39;49;00m$
  1950^I[37m        [39;49;00minStatementIndentStack->push_back([37m/*2*/[39;49;00m[37m [39;49;00mindentLength[37m [39;49;00m+[37m [39;49;00mpreviousIndent[37m [39;49;00m);[37m[39;49;00m$
  1951^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(updateParenStack)[37m[39;49;00m$
  1952^I[37m          [39;49;00mparenIndentStack->push_back([37m [39;49;00mpreviousIndent[37m [39;49;00m);[37m[39;49;00m$
  1953^I[37m        [39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
  1954^I[37m      [39;49;00m}[37m[39;49;00m$
  1955^I[37m[39;49;00m$
  1956^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(updateParenStack)[37m[39;49;00m$
  1957^I[37m      [39;49;00mparenIndentStack->push_back(i+spaceTabCount);[37m[39;49;00m$
  1958^I[37m[39;49;00m$
  1959^I[37m    [39;49;00minStatementIndent[37m [39;49;00m=[37m [39;49;00mi[37m [39;49;00m+[37m [39;49;00mnextNonWSChar[37m [39;49;00m+[37m [39;49;00mspaceTabCount;[37m[39;49;00m$
  1960^I[37m[39;49;00m$
  1961^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m+[37m [39;49;00mnextNonWSChar[37m [39;49;00m<[37m [39;49;00mminIndent)[37m[39;49;00m$
  1962^I[37m      [39;49;00minStatementIndent[37m [39;49;00m=[37m [39;49;00mminIndent[37m [39;49;00m+[37m [39;49;00mspaceTabCount;[37m[39;49;00m$
  1963^I[37m[39;49;00m$
  1964^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m+[37m [39;49;00mnextNonWSChar[37m [39;49;00m>[37m [39;49;00mmaxInStatementIndent)[37m[39;49;00m$
  1965^I[37m      [39;49;00minStatementIndent[37m [39;49;00m=[37m  [39;49;00mindentLength*[34m2[39;49;00m[37m [39;49;00m+[37m [39;49;00mspaceTabCount;[37m[39;49;00m$
  1966^I[37m[39;49;00m$
  1967^I[37m[39;49;00m$
  1968^I[37m[39;49;00m$
  1969^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStack->empty()[37m [39;49;00m&&[37m[39;49;00m$
  1970^I[37m        [39;49;00minStatementIndent[37m [39;49;00m<[37m [39;49;00minStatementIndentStack->back())[37m[39;49;00m$
  1971^I[37m      [39;49;00minStatementIndent[37m [39;49;00m=[37m [39;49;00minStatementIndentStack->back();[37m[39;49;00m$
  1972^I[37m[39;49;00m$
  1973^I[37m    [39;49;00minStatementIndentStack->push_back(inStatementIndent);[37m[39;49;00m$
  1974^I[37m  [39;49;00m}[37m[39;49;00m$
  1975^I[37m[39;49;00m$
  1976^I[37m  [39;49;00m[37m/**[39;49;00m$
  1977^I[37m   * get distance to the next non-white sspace, non-comment character in the line.[39;49;00m$
  1978^I[37m   * if no such character exists, return the length remaining to the end of the line.[39;49;00m$
  1979^I[37m   */[39;49;00m[37m[39;49;00m$
  1980^I[37m  [39;49;00m[36mint[39;49;00m[37m [39;49;00mASBeautifier::getNextProgramCharDistance([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi)[37m[39;49;00m$
  1981^I[37m  [39;49;00m{[37m[39;49;00m$
  1982^I[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00minComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1983^I[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mremainingCharNum[37m [39;49;00m=[37m [39;49;00mline.length()[37m [39;49;00m-[37m [39;49;00mi;[37m[39;49;00m$
  1984^I[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mcharDistance[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1985^I[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mch;[37m[39;49;00m$
  1986^I[37m[39;49;00m$
  1987^I[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(charDistance[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m [39;49;00mcharDistance[37m [39;49;00m<[37m [39;49;00mremainingCharNum;[37m [39;49;00mcharDistance++)[37m[39;49;00m$
  1988^I[37m      [39;49;00m{[37m[39;49;00m$
  1989^I[37m        [39;49;00mch[37m [39;49;00m=[37m [39;49;00mline[i[37m [39;49;00m+[37m [39;49;00mcharDistance];[37m[39;49;00m$
  1990^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(inComment)[37m[39;49;00m$
  1991^I[37m          [39;49;00m{[37m[39;49;00m$
  1992^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.COMPARE(i[37m [39;49;00m+[37m [39;49;00mcharDistance,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_CLOSE_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1993^I[37m              [39;49;00m{[37m[39;49;00m$
  1994^I[37m                [39;49;00mcharDistance++;[37m[39;49;00m$
  1995^I[37m                [39;49;00minComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1996^I[37m              [39;49;00m}[37m[39;49;00m$
  1997^I[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1998^I[37m          [39;49;00m}[37m[39;49;00m$
  1999^I[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isWhiteSpace(ch))[37m[39;49;00m$
  2000^I[37m          [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2001^I[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  2002^I[37m          [39;49;00m{[37m[39;49;00m$
  2003^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.COMPARE(i[37m [39;49;00m+[37m [39;49;00mcharDistance,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_OPEN_LINE_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  2004^I[37m              [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mremainingCharNum;[37m[39;49;00m$
  2005^I[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.COMPARE(i[37m [39;49;00m+[37m [39;49;00mcharDistance,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_OPEN_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  2006^I[37m              [39;49;00m{[37m[39;49;00m$
  2007^I[37m                [39;49;00mcharDistance++;[37m[39;49;00m$
  2008^I[37m                [39;49;00minComment[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  2009^I[37m              [39;49;00m}[37m[39;49;00m$
  2010^I[37m          [39;49;00m}[37m[39;49;00m$
  2011^I[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2012^I[37m          [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mcharDistance;[37m[39;49;00m$
  2013^I[37m      [39;49;00m}[37m[39;49;00m$
  2014^I[37m[39;49;00m$
  2015^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mcharDistance;[37m[39;49;00m$
  2016^I[37m  [39;49;00m}[37m[39;49;00m$
  2017^I[37m[39;49;00m$
  2018^I[37m[39;49;00m$
  2019^I[37m  [39;49;00m[37m/**[39;49;00m$
  2020^I[37m   * check if a specific character can be used in a legal variable/method/class name[39;49;00m$
  2021^I[37m   *[39;49;00m$
  2022^I[37m   * @return          legality of the char.[39;49;00m$
  2023^I[37m   * @param ch        the character to be checked.[39;49;00m$
  2024^I[37m   */[39;49;00m[37m[39;49;00m$
  2025^I[37m  [39;49;00m[36mbool[39;49;00m[37m [39;49;00mASBeautifier::isLegalNameChar([36mchar[39;49;00m[37m [39;49;00mch)[37m [39;49;00m[34mconst[39;49;00m[37m[39;49;00m$
  2026^I[37m    [39;49;00m{[37m[39;49;00m$
  2027^I[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m(isalnum(ch)[37m [39;49;00m[37m//(ch>='a' && ch<='z') || (ch>='A' && ch<='Z') || (ch>='0' && ch<='9') ||[39;49;00m$
  2028^I[37m              [39;49;00m||[37m [39;49;00mch==[33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch==[33m'[39;49;00m[33m_[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00m(!isCStyle[37m [39;49;00m&&[37m [39;49;00mch==[33m'[39;49;00m[33m$[39;49;00m[33m'[39;49;00m)[37m [39;49;00m||[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00mch==[33m'[39;49;00m[33m~[39;49;00m[33m'[39;49;00m));[37m[39;49;00m$
  2029^I[37m    [39;49;00m}[37m[39;49;00m$
  2030^I[37m[39;49;00m$
  2031^I[37m[39;49;00m$
  2032^I[37m  [39;49;00m[37m/**[39;49;00m$
  2033^I[37m   * check if a specific line position contains a header, out of several possible headers.[39;49;00m$
  2034^I[37m   *[39;49;00m$
  2035^I[37m   * @return    a pointer to the found header. if no header was found then return NULL.[39;49;00m$
  2036^I[37m   */[39;49;00m[37m[39;49;00m$
  2037^I[37m  [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*ASBeautifier::findHeader([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi,[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m&possibleHeaders,[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mcheckBoundry)[37m[39;49;00m$
  2038^I[37m  [39;49;00m{[37m[39;49;00m$
  2039^I[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mmaxHeaders[37m [39;49;00m=[37m [39;49;00mpossibleHeaders.size();[37m[39;49;00m$
  2040^I[37m    [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*header[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2041^I[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mp;[37m[39;49;00m$
  2042^I[37m[39;49;00m$
  2043^I[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(p=[34m0[39;49;00m;[37m [39;49;00mp[37m [39;49;00m<[37m [39;49;00mmaxHeaders;[37m [39;49;00mp++)[37m[39;49;00m$
  2044^I[37m      [39;49;00m{[37m[39;49;00m$
  2045^I[37m        [39;49;00mheader[37m [39;49;00m=[37m [39;49;00mpossibleHeaders[p];[37m[39;49;00m$
  2046^I[37m[39;49;00m$
  2047^I[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.COMPARE(i,[37m [39;49;00mheader->length(),[37m [39;49;00m*header)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  2048^I[37m          [39;49;00m{[37m[39;49;00m$
  2049^I[37m            [39;49;00m[37m// check that this is a header and not a part of a longer word[39;49;00m$
  2050^I[37m            [39;49;00m[37m// (e.g. not at its begining, not at its middle...)[39;49;00m$
  2051^I[37m[39;49;00m$
  2052^I[37m            [39;49;00m[36mint[39;49;00m[37m [39;49;00mlineLength[37m [39;49;00m=[37m [39;49;00mline.length();[37m[39;49;00m$
  2053^I[37m            [39;49;00m[36mint[39;49;00m[37m [39;49;00mheaderEnd[37m [39;49;00m=[37m [39;49;00mi[37m [39;49;00m+[37m [39;49;00mheader->length();[37m[39;49;00m$
  2054^I[37m            [39;49;00m[36mchar[39;49;00m[37m [39;49;00mstartCh[37m [39;49;00m=[37m [39;49;00m(*header)[[34m0[39;49;00m];[37m   [39;49;00m[37m// first char of header[39;49;00m$
  2055^I[37m            [39;49;00m[36mchar[39;49;00m[37m [39;49;00mendCh[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m                [39;49;00m[37m// char just after header[39;49;00m$
  2056^I[37m            [39;49;00m[36mchar[39;49;00m[37m [39;49;00mprevCh[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m               [39;49;00m[37m// char just before header[39;49;00m$
  2057^I[37m[39;49;00m$
  2058^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(headerEnd[37m [39;49;00m<[37m [39;49;00mlineLength)[37m[39;49;00m$
  2059^I[37m              [39;49;00m{[37m[39;49;00m$
  2060^I[37m                [39;49;00mendCh[37m [39;49;00m=[37m [39;49;00mline[headerEnd];[37m[39;49;00m$
  2061^I[37m              [39;49;00m}[37m[39;49;00m$
  2062^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  2063^I[37m              [39;49;00m{[37m[39;49;00m$
  2064^I[37m                [39;49;00mprevCh[37m [39;49;00m=[37m [39;49;00mline[i[34m-1[39;49;00m];[37m[39;49;00m$
  2065^I[37m              [39;49;00m}[37m[39;49;00m$
  2066^I[37m[39;49;00m$
  2067^I[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!checkBoundry)[37m[39;49;00m$
  2068^I[37m              [39;49;00m{[37m[39;49;00m$
  2069^I[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mheader;[37m[39;49;00m$
  2070^I[37m              [39;49;00m}[37m[39;49;00m$
  2071^I[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(prevCh[37m [39;49;00m!=[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
  2072^I[37m                     [39;49;00m&&[37m [39;49;00misLegalNameChar(startCh)[37m[39;49;00m$
  2073^I[37m                     [39;49;00m&&[37m [39;49;00misLegalNameChar(prevCh))[37m[39;49;00m$
  2074^I[37m              [39;49;00m{[37m[39;49;00m$
  2075^I[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2076^I[37m              [39;49;00m}[37m[39;49;00m$
  2077^I[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(headerEnd[37m [39;49;00m>=[37m [39;49;00mlineLength[37m[39;49;00m$
  2078^I[37m                     [39;49;00m||[37m [39;49;00m!isLegalNameChar(startCh)[37m[39;49;00m$
  2079^I[37m                     [39;49;00m||[37m [39;49;00m!isLegalNameChar(endCh))[37m[39;49;00m$
  2080^I[37m              [39;49;00m{[37m[39;49;00m$
  2081^I[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mheader;[37m[39;49;00m$
  2082^I[37m              [39;49;00m}[37m[39;49;00m$
  2083^I[37m            [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2084^I[37m              [39;49;00m{[37m[39;49;00m$
  2085^I[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2086^I[37m              [39;49;00m}[37m[39;49;00m$
  2087^I[37m          [39;49;00m}[37m[39;49;00m$
  2088^I[37m      [39;49;00m}[37m[39;49;00m$
  2089^I[37m[39;49;00m$
  2090^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2091^I[37m  [39;49;00m}[37m[39;49;00m$
  2092^I[37m[39;49;00m$
  2093^I[37m[39;49;00m$
  2094^I[37m  [39;49;00m[37m/**[39;49;00m$
  2095^I[37m   * check if a specific character can be used in a legal variable/method/class name[39;49;00m$
  2096^I[37m   *[39;49;00m$
  2097^I[37m   * @return          legality of the char.[39;49;00m$
  2098^I[37m   * @param ch        the character to be checked.[39;49;00m$
  2099^I[37m   */[39;49;00m[37m[39;49;00m$
  2100^I[37m  [39;49;00m[36mbool[39;49;00m[37m [39;49;00mASBeautifier::isWhiteSpace([36mchar[39;49;00m[37m [39;49;00mch)[37m [39;49;00m[34mconst[39;49;00m[37m[39;49;00m$
  2101^I[37m    [39;49;00m{[37m[39;49;00m$
  2102^I[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m\t[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
  2103^I[37m    [39;49;00m}[37m[39;49;00m$
  2104^I[37m[39;49;00m$
  2105^I[37m  [39;49;00m[37m/**[39;49;00m$
  2106^I[37m   * find the index number of a string element in a container of strings[39;49;00m$
  2107^I[37m   *[39;49;00m$
  2108^I[37m   * @return              the index number of element in the ocntainer. -1 if element not found.[39;49;00m$
  2109^I[37m   * @param container     a vector of strings.[39;49;00m$
  2110^I[37m   * @param element       the element to find .[39;49;00m$
  2111^I[37m   */[39;49;00m[37m[39;49;00m$
  2112^I[37m  [39;49;00m[36mint[39;49;00m[37m [39;49;00mASBeautifier::indexOf(vector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m&container,[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*element)[37m[39;49;00m$
  2113^I[37m  [39;49;00m{[37m[39;49;00m$
  2114^I[37m    [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>::const_iterator[37m [39;49;00mwhere;[37m[39;49;00m$
  2115^I[37m[39;49;00m$
  2116^I[37m    [39;49;00mwhere=[37m [39;49;00mfind(container.begin(),[37m [39;49;00mcontainer.end(),[37m [39;49;00melement);[37m[39;49;00m$
  2117^I[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(where[37m [39;49;00m==[37m [39;49;00mcontainer.end())[37m[39;49;00m$
  2118^I[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
  2119^I[37m    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2120^I[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mwhere[37m [39;49;00m-[37m [39;49;00mcontainer.begin();[37m[39;49;00m$
  2121^I[37m  [39;49;00m}[37m[39;49;00m$
  2122^I[37m[39;49;00m$
  2123^I[37m  [39;49;00m[37m/**[39;49;00m$
  2124^I[37m   * trim removes the white space surrounding a line.[39;49;00m$
  2125^I[37m   *[39;49;00m$
  2126^I[37m   * @return          the trimmed line.[39;49;00m$
  2127^I[37m   * @param str       the line to trim.[39;49;00m$
  2128^I[37m   */[39;49;00m[37m[39;49;00m$
  2129^I[37m  [39;49;00mstring[37m [39;49;00mASBeautifier::trim([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&str)[37m[39;49;00m$
  2130^I[37m  [39;49;00m{[37m[39;49;00m$
  2131^I[37m[39;49;00m$
  2132^I[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mstart[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  2133^I[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mend[37m [39;49;00m=[37m [39;49;00mstr.length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  2134^I[37m[39;49;00m$
  2135^I[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(start[37m [39;49;00m<[37m [39;49;00mend[37m [39;49;00m&&[37m [39;49;00misWhiteSpace(str[start]))[37m[39;49;00m$
  2136^I[37m      [39;49;00mstart++;[37m[39;49;00m$
  2137^I[37m[39;49;00m$
  2138^I[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(start[37m [39;49;00m<=[37m [39;49;00mend[37m [39;49;00m&&[37m [39;49;00misWhiteSpace(str[end]))[37m[39;49;00m$
  2139^I[37m      [39;49;00mend--;[37m[39;49;00m$
  2140^I[37m[39;49;00m$
  2141^I[37m    [39;49;00mstring[37m [39;49;00m[32mreturnStr[39;49;00m(str,[37m [39;49;00mstart,[37m [39;49;00mend+[34m1[39;49;00m-start);[37m[39;49;00m$
  2142^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mreturnStr;[37m[39;49;00m$
  2143^I[37m  [39;49;00m}[37m[39;49;00m$
  2144^I[37m[39;49;00m$
  2145^I[36m#[39;49;00m[36mifdef USES_NAMESPACE[39;49;00m[36m[39;49;00m$
  2146^I}[37m[39;49;00m$
  2147^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  2148^I[37m/*[39;49;00m$
  2149^I[37m * Copyright (c) 1998,1999,2000,2001,2002 Tal Davidson. All rights reserved.[39;49;00m$
  2150^I[37m *[39;49;00m$
  2151^I[37m * compiler_defines.h   (1 January 1999)[39;49;00m$
  2152^I[37m * by Tal Davidson (davidsont@bigfoot.com)[39;49;00m$
  2153^I[37m * This file is a part of "Artistic Style" - an indentater and reformatter[39;49;00m$
  2154^I[37m * of C, C++, C# and Java source files.[39;49;00m$
  2155^I[37m *[39;49;00m$
  2156^I[37m * The "Artistic Style" project, including all files needed to compile it,[39;49;00m$
  2157^I[37m * is free software; you can redistribute it and/or use it and/or modify it[39;49;00m$
  2158^I[37m * under the terms of the GNU General Public License as published [39;49;00m$
  2159^I[37m * by the Free Software Foundation; either version 2 of the License, [39;49;00m$
  2160^I[37m * or (at your option) any later version.[39;49;00m$
  2161^I[37m *[39;49;00m$
  2162^I[37m * This program is distributed in the hope that it will be useful,[39;49;00m$
  2163^I[37m * but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m$
  2164^I[37m * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.[39;49;00m$
  2165^I[37m *[39;49;00m$
  2166^I[37m * You should have received a copy of the GNU General Public[39;49;00m$
  2167^I[37m * License along with this program.[39;49;00m$
  2168^I[37m */[39;49;00m[37m[39;49;00m$
  2169^I[37m[39;49;00m$
  2170^I[37m[39;49;00m$
  2171^I[36m#[39;49;00m[36mifndef ASBEAUTIFIER_H[39;49;00m[36m[39;49;00m$
  2172^I[36m#[39;49;00m[36mdefine ASBEAUTIFIER_H[39;49;00m[36m[39;49;00m$
  2173^I[37m[39;49;00m$
  2174^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"ASResource.h"[39;49;00m[36m[39;49;00m$
  2175^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"compiler_defines.h"[39;49;00m[36m[39;49;00m$
  2176^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"ASSourceIterator.h"[39;49;00m[36m[39;49;00m$
  2177^I[37m[39;49;00m$
  2178^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<string>[39;49;00m[36m[39;49;00m$
  2179^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<vector>[39;49;00m[36m[39;49;00m$
  2180^I[37m[39;49;00m$
  2181^I[37m[39;49;00m$
  2182^I[34musing[39;49;00m[37m [39;49;00m[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mstd[39;49;00m;[37m[39;49;00m$
  2183^I[37m[39;49;00m$
  2184^I[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mastyle[39;49;00m[37m[39;49;00m$
  2185^I[37m  [39;49;00m{[37m[39;49;00m$
  2186^I[37m[39;49;00m$
  2187^I[37m  [39;49;00m[34menum[39;49;00m[37m [39;49;00m[04m[32mBracketMode[39;49;00m[37m   [39;49;00m{[37m [39;49;00mNONE_MODE,[37m [39;49;00mATTACH_MODE,[37m [39;49;00mBREAK_MODE,[37m [39;49;00mBDAC_MODE[37m [39;49;00m};[37m[39;49;00m$
  2188^I[37m  [39;49;00m[34menum[39;49;00m[37m [39;49;00m[04m[32mBracketType[39;49;00m[37m   [39;49;00m{[37m [39;49;00mNULL_TYPE[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m,[37m[39;49;00m$
  2189^I[37m                       [39;49;00mDEFINITION_TYPE[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m[39;49;00m$
  2190^I[37m                       [39;49;00mCOMMAND_TYPE[37m [39;49;00m=[37m [39;49;00m[34m2[39;49;00m,[37m[39;49;00m$
  2191^I[37m                       [39;49;00mARRAY_TYPE[37m  [39;49;00m=[37m [39;49;00m[34m4[39;49;00m,[37m[39;49;00m$
  2192^I[37m                       [39;49;00mSINGLE_LINE_TYPE[37m [39;49;00m=[37m [39;49;00m[34m8[39;49;00m};[37m[39;49;00m$
  2193^I[37m[39;49;00m$
  2194^I[37m[39;49;00m$
  2195^I[37m  [39;49;00m[34mclass[39;49;00m[37m [39;49;00m[04m[32mASBeautifier[39;49;00m[37m [39;49;00m:[37m [39;49;00m[34mprotected[39;49;00m[37m [39;49;00mASResource[37m[39;49;00m$
  2196^I[37m    [39;49;00m{[37m[39;49;00m$
  2197^I[37m    [39;49;00m[34mpublic[39;49;00m:[37m[39;49;00m$
  2198^I[37m      [39;49;00mASBeautifier();[37m[39;49;00m$
  2199^I[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00m~ASBeautifier();[37m[39;49;00m$
  2200^I[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32minit[39;49;00m(ASSourceIterator*[37m [39;49;00miter);[37m [39;49;00m[37m// pointer to dynamically created iterator.[39;49;00m$
  2201^I[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32minit[39;49;00m();[37m[39;49;00m$
  2202^I[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00m[32mhasMoreLines[39;49;00m()[37m [39;49;00m[34mconst[39;49;00m;[37m[39;49;00m$
  2203^I[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00mstring[37m [39;49;00m[32mnextLine[39;49;00m();[37m[39;49;00m$
  2204^I[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00mstring[37m [39;49;00m[32mbeautify[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line);[37m[39;49;00m$
  2205^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetTabIndentation[39;49;00m([36mint[39;49;00m[37m [39;49;00mlength[37m [39;49;00m=[37m [39;49;00m[34m4[39;49;00m,[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mforceTabs[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m);[37m[39;49;00m$
  2206^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetSpaceIndentation[39;49;00m([36mint[39;49;00m[37m [39;49;00mlength[37m [39;49;00m=[37m [39;49;00m[34m4[39;49;00m);[37m[39;49;00m$
  2207^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetMaxInStatementIndentLength[39;49;00m([36mint[39;49;00m[37m [39;49;00mmax);[37m[39;49;00m$
  2208^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetMinConditionalIndentLength[39;49;00m([36mint[39;49;00m[37m [39;49;00mmin);[37m[39;49;00m$
  2209^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetClassIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2210^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetSwitchIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2211^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetCaseIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2212^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetBracketIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2213^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetBlockIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2214^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetNamespaceIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2215^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetLabelIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2216^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetCStyle[39;49;00m();[37m[39;49;00m$
  2217^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetJavaStyle[39;49;00m();[37m[39;49;00m$
  2218^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetEmptyLineFill[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2219^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetPreprocessorIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2220^I[37m[39;49;00m$
  2221^I[37m[39;49;00m$
  2222^I[37m    [39;49;00m[34mprotected[39;49;00m:[37m[39;49;00m$
  2223^I[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mgetNextProgramCharDistance([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi);[37m[39;49;00m$
  2224^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00m[32misLegalNameChar[39;49;00m([36mchar[39;49;00m[37m [39;49;00mch)[37m [39;49;00m[34mconst[39;49;00m;[37m[39;49;00m$
  2225^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00m[32misWhiteSpace[39;49;00m([36mchar[39;49;00m[37m [39;49;00mch)[37m [39;49;00m[34mconst[39;49;00m;[37m[39;49;00m$
  2226^I[37m      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*[32mfindHeader[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi,[37m[39;49;00m$
  2227^I[37m                               [39;49;00m[34mconst[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m&possibleHeaders,[37m[39;49;00m$
  2228^I[37m                               [39;49;00m[36mbool[39;49;00m[37m [39;49;00mcheckBoundry[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m);[37m[39;49;00m$
  2229^I[37m      [39;49;00mstring[37m [39;49;00m[32mtrim[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&str);[37m[39;49;00m$
  2230^I[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mindexOf[39;49;00m(vector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m&container,[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*element);[37m[39;49;00m$
  2231^I[37m[39;49;00m$
  2232^I[37m    [39;49;00m[34mprivate[39;49;00m:[37m[39;49;00m$
  2233^I[37m      [39;49;00mASBeautifier([34mconst[39;49;00m[37m [39;49;00mASBeautifier[37m [39;49;00m&copy);[37m[39;49;00m$
  2234^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[34moperator[39;49;00m=(ASBeautifier&);[37m [39;49;00m[37m// not to be implemented[39;49;00m$
  2235^I[37m[39;49;00m$
  2236^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32minitStatic[39;49;00m();[37m[39;49;00m$
  2237^I[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mregisterInStatementIndent[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mspaceTabCount,[37m[39;49;00m$
  2238^I[37m                                     [39;49;00m[36mint[39;49;00m[37m [39;49;00mminIndent,[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mupdateParenStack);[37m[39;49;00m$
  2239^I[37m      [39;49;00mstring[37m [39;49;00m[32mpreLineWS[39;49;00m([36mint[39;49;00m[37m [39;49;00mspaceTabCount,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mtabCount);[37m[39;49;00m$
  2240^I[37m[39;49;00m$
  2241^I[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mheaders;[37m[39;49;00m$
  2242^I[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mnonParenHeaders;[37m[39;49;00m$
  2243^I[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mpreprocessorHeaders;[37m[39;49;00m$
  2244^I[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mpreBlockStatements;[37m[39;49;00m$
  2245^I[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00massignmentOperators;[37m[39;49;00m$
  2246^I[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mnonAssignmentOperators;[37m[39;49;00m$
  2247^I[37m[39;49;00m$
  2248^I[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mcalledInitStatic;[37m[39;49;00m$
  2249^I[37m[39;49;00m$
  2250^I[37m      [39;49;00mASSourceIterator[37m [39;49;00m*sourceIterator;[37m[39;49;00m$
  2251^I[37m      [39;49;00mvector<ASBeautifier*>[37m [39;49;00m*waitingBeautifierStack;[37m[39;49;00m$
  2252^I[37m      [39;49;00mvector<ASBeautifier*>[37m [39;49;00m*activeBeautifierStack;[37m[39;49;00m$
  2253^I[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*waitingBeautifierStackLengthStack;[37m[39;49;00m$
  2254^I[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*activeBeautifierStackLengthStack;[37m[39;49;00m$
  2255^I[37m      [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m*headerStack;[37m[39;49;00m$
  2256^I[37m      [39;49;00mvector<[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>*[37m [39;49;00m>[37m [39;49;00m*tempStacks;[37m[39;49;00m$
  2257^I[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*blockParenDepthStack;[37m[39;49;00m$
  2258^I[37m      [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m*blockStatementStack;[37m[39;49;00m$
  2259^I[37m      [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m*parenStatementStack;[37m[39;49;00m$
  2260^I[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*inStatementIndentStack;[37m[39;49;00m$
  2261^I[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*inStatementIndentStackSizeStack;[37m[39;49;00m$
  2262^I[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*parenIndentStack;[37m[39;49;00m$
  2263^I[37m      [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m*bracketBlockStateStack;[37m[39;49;00m$
  2264^I[37m      [39;49;00mstring[37m [39;49;00mindentString;[37m[39;49;00m$
  2265^I[37m      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*currentHeader;[37m[39;49;00m$
  2266^I[37m      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*previousLastLineHeader;[37m[39;49;00m$
  2267^I[37m      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*immediatelyPreviousAssignmentOp;[37m[39;49;00m$
  2268^I[37m      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*probationHeader;[37m[39;49;00m$
  2269^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInQuote;[37m[39;49;00m$
  2270^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInComment;[37m[39;49;00m$
  2271^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInCase;[37m[39;49;00m$
  2272^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInQuestion;[37m[39;49;00m$
  2273^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInStatement;[37m[39;49;00m$
  2274^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInHeader;[37m[39;49;00m$
  2275^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misCStyle;[37m[39;49;00m$
  2276^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInOperator;[37m[39;49;00m$
  2277^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInTemplate;[37m[39;49;00m$
  2278^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInConst;[37m[39;49;00m$
  2279^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInDefine;[37m[39;49;00m$
  2280^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInDefineDefinition;[37m[39;49;00m$
  2281^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mclassIndent;[37m[39;49;00m$
  2282^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInClassHeader;[37m[39;49;00m$
  2283^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInClassHeaderTab;[37m[39;49;00m$
  2284^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mswitchIndent;[37m[39;49;00m$
  2285^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mcaseIndent;[37m[39;49;00m$
  2286^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mnamespaceIndent;[37m[39;49;00m$
  2287^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mbracketIndent;[37m[39;49;00m$
  2288^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mblockIndent;[37m[39;49;00m$
  2289^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mlabelIndent;[37m[39;49;00m$
  2290^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mpreprocessorIndent;[37m[39;49;00m$
  2291^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInConditional;[37m[39;49;00m$
  2292^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misMinimalConditinalIndentSet;[37m[39;49;00m$
  2293^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mshouldForceTabIndentation;[37m[39;49;00m$
  2294^I[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mminConditionalIndent;[37m[39;49;00m$
  2295^I[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mparenDepth;[37m[39;49;00m$
  2296^I[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mindentLength;[37m[39;49;00m$
  2297^I[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mblockTabCount;[37m[39;49;00m$
  2298^I[37m      [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mleadingWhiteSpaces;[37m[39;49;00m$
  2299^I[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mmaxInStatementIndent;[37m[39;49;00m$
  2300^I[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mtemplateDepth;[37m[39;49;00m$
  2301^I[37m      [39;49;00m[36mchar[39;49;00m[37m [39;49;00mquoteChar;[37m[39;49;00m$
  2302^I[37m      [39;49;00m[36mchar[39;49;00m[37m [39;49;00mprevNonSpaceCh;[37m[39;49;00m$
  2303^I[37m      [39;49;00m[36mchar[39;49;00m[37m [39;49;00mcurrentNonSpaceCh;[37m[39;49;00m$
  2304^I[37m      [39;49;00m[36mchar[39;49;00m[37m [39;49;00mcurrentNonLegalCh;[37m[39;49;00m$
  2305^I[37m      [39;49;00m[36mchar[39;49;00m[37m [39;49;00mprevNonLegalCh;[37m[39;49;00m$
  2306^I[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mprevFinalLineSpaceTabCount;[37m[39;49;00m$
  2307^I[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mprevFinalLineTabCount;[37m[39;49;00m$
  2308^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00memptyLineFill;[37m[39;49;00m$
  2309^I[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mbackslashEndsPrevLine;[37m[39;49;00m$
  2310^I[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mdefineTabCount;[37m[39;49;00m$
  2311^I[37m    [39;49;00m};[37m[39;49;00m$
  2312^I}[37m[39;49;00m$
  2313^I[37m[39;49;00m$
  2314^I[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  2315^I[37m/*[39;49;00m$
  2316^I[37m * Copyright (c) 1998,1999,2000,2001,2002 Tal Davidson. All rights reserved.[39;49;00m$
  2317^I[37m *[39;49;00m$
  2318^I[37m * ASFormatter.cpp[39;49;00m$
  2319^I[37m * by Tal Davidson (davidsont@bigfoot.com)[39;49;00m$
  2320^I[37m * This file is a part of "Artistic Style" - an indentater and reformatter[39;49;00m$
  2321^I[37m * of C, C++, C# and Java source files.[39;49;00m$
  2322^I[37m *[39;49;00m$
  2323^I[37m * The "Artistic Style" project, including all files needed to compile it,[39;49;00m$
  2324^I[37m * is free software; you can redistribute it and/or use it and/or modify it[39;49;00m$
  2325^I[37m * under the terms of the GNU General Public License as published [39;49;00m$
  2326^I[37m * by the Free Software Foundation; either version 2 of the License, [39;49;00m$
  2327^I[37m * or (at your option) any later version.[39;49;00m$
  2328^I[37m *[39;49;00m$
  2329^I[37m * This program is distributed in the hope that it will be useful,[39;49;00m$
  2330^I[37m * but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m$
  2331^I[37m * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.[39;49;00m$
  2332^I[37m *[39;49;00m$
  2333^I[37m * You should have received a copy of the GNU General Public[39;49;00m$
  2334^I[37m * License along with this program.[39;49;00m$
  2335^I[37m *[39;49;00m$
  2336^I[37m *[39;49;00m$
  2337^I[37m * Patches:[39;49;00m$
  2338^I[37m * 26 November 1998 - Richard Bullington -[39;49;00m$
  2339^I[37m *        A correction of line-breaking in headers following '}',[39;49;00m$
  2340^I[37m [39;49;00m$
  2341^I[37m *        was created using a variation of a  patch by Richard Bullington.[39;49;00m$
  2342^I[37m * 08 May 2004[39;49;00m$
  2343^I[37m *        applied   ASFormatter450670.patch.bz2, ASFormatter.cpp.patch.bz2,[39;49;00m$
  2344^I[37m *                  patch1_ssvb_patch.tar.gz[39;49;00m$
  2345^I[37m */[39;49;00m[37m[39;49;00m$
  2346^I[37m[39;49;00m$
  2347^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"compiler_defines.h"[39;49;00m[36m[39;49;00m$
  2348^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"ASFormatter.h"[39;49;00m[36m[39;49;00m$
  2349^I[37m[39;49;00m$
  2350^I[37m[39;49;00m$
  2351^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<string>[39;49;00m[36m[39;49;00m$
  2352^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<cctype>[39;49;00m[36m[39;49;00m$
  2353^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<vector>[39;49;00m[36m[39;49;00m$
  2354^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<algorithm>[39;49;00m[36m[39;49;00m$
  2355^I[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<iostream>[39;49;00m[36m[39;49;00m$
  2356^I[37m[39;49;00m$
  2357^I[37m[39;49;00m$
  2358^I[36m#[39;49;00m[36mdefine INIT_CONTAINER(container, value)     {if ( (container) != NULL ) delete (container); (container) = (value); }[39;49;00m[36m[39;49;00m$
  2359^I[36m#[39;49;00m[36mdefine DELETE_CONTAINER(container)          {if ( (container) != NULL ) delete (container) ; }[39;49;00m[36m[39;49;00m$
  2360^I[36m#[39;49;00m[36mdefine IS_A(a,b)                            ( ((a) & (b)) == (b))[39;49;00m[36m[39;49;00m$
  2361^I[36m#[39;49;00m[36mifdef USES_NAMESPACE[39;49;00m[36m[39;49;00m$
  2362^I[34musing[39;49;00m[37m [39;49;00m[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mstd[39;49;00m;$
