     1	[37m/***************************************************************************[39;49;00m$
     2	[37m                    ansigenerator.cpp  -  description[39;49;00m$
     3	[37m                             -------------------[39;49;00m$
     4	[37m    begin                : Jul 5 2004[39;49;00m$
     5	[37m    copyright            : (C) 2004 by André Simon[39;49;00m$
     6	[37m    email                : andre.simon1@gmx.de[39;49;00m$
     7	[37m ***************************************************************************/[39;49;00m[37m[39;49;00m$
     8	[37m[39;49;00m$
     9	[37m/***************************************************************************[39;49;00m$
    10	[37m *                                                                         *[39;49;00m$
    11	[37m *   This program is free software; you can redistribute it and/or modify  *[39;49;00m$
    12	[37m *   it under the terms of the GNU General Public License as published by  *[39;49;00m$
    13	[37m *   the Free Software Foundation; either version 2 of the License, or     *[39;49;00m$
    14	[37m *   (at your option) any later version.                                   *[39;49;00m$
    15	[37m *                                                                         *[39;49;00m$
    16	[37m ***************************************************************************/[39;49;00m[37m[39;49;00m$
    17	[37m[39;49;00m$
    18	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"ansigenerator.h"[39;49;00m[36m[39;49;00m$
    19	[37m[39;49;00m$
    20	[34musing[39;49;00m[37m [39;49;00m[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mstd[39;49;00m;[37m[39;49;00m$
    21	[37m[39;49;00m$
    22	[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mhighlight[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
    23	[37m[39;49;00m$
    24	[37m[39;49;00m$
    25	string[37m  [39;49;00m[32mAnsiGenerator::getOpenTag[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring&font,[37m[39;49;00m$
    26	[37m                                  [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring&fgCol,[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring&bgCol)[37m [39;49;00m{[37m[39;49;00m$
    27	[37m    [39;49;00mostringstream[37m [39;49;00ms;[37m[39;49;00m$
    28	[37m    [39;49;00ms[37m  [39;49;00m<<[37m [39;49;00m[33m"[39;49;00m[33m\033[39;49;00m[33m[[39;49;00m[33m"[39;49;00m<<font;[37m[39;49;00m$
    29	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!fgCol.empty())[37m[39;49;00m$
    30	[37m        [39;49;00ms<<[33m"[39;49;00m[33m;[39;49;00m[33m"[39;49;00m<<fgCol;[37m[39;49;00m$
    31	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!bgCol.empty())[37m[39;49;00m$
    32	[37m        [39;49;00ms<<[33m"[39;49;00m[33m;[39;49;00m[33m"[39;49;00m<<bgCol;[37m[39;49;00m$
    33	[37m    [39;49;00ms[37m [39;49;00m<<[37m [39;49;00m[33m"[39;49;00m[33mm[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
    34	[37m    [39;49;00m[34mreturn[39;49;00m[37m  [39;49;00ms.str();[37m[39;49;00m$
    35	}[37m[39;49;00m$
    36	[37m[39;49;00m$
    37	[37m[39;49;00m$
    38	AnsiGenerator::AnsiGenerator([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&colourTheme)[37m[39;49;00m$
    39	[37m        [39;49;00m:[37m [39;49;00mCodeGenerator(colourTheme)[37m [39;49;00m{[37m[39;49;00m$
    40	[37m    [39;49;00mstyleTagOpen.push_back([33m"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
    41	[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m31[39;49;00m[33m"[39;49;00m));[37m [39;49;00m[37m//str[39;49;00m$
    42	[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m34[39;49;00m[33m"[39;49;00m));[37m//number[39;49;00m$
    43	[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m34[39;49;00m[33m"[39;49;00m));[37m//sl comment[39;49;00m$
    44	[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m34[39;49;00m[33m"[39;49;00m));[37m//ml comment[39;49;00m$
    45	[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m35[39;49;00m[33m"[39;49;00m));[37m//escapeChar[39;49;00m$
    46	[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m35[39;49;00m[33m"[39;49;00m));[37m//directive[39;49;00m$
    47	[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m01[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m31[39;49;00m[33m"[39;49;00m));[37m//directive string[39;49;00m$
    48	[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m30[39;49;00m[33m"[39;49;00m));[37m//linenum[39;49;00m$
    49	[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m01[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m));[37m//symbol[39;49;00m$
    50	[37m[39;49;00m$
    51	[37m    [39;49;00mstyleTagClose.push_back([33m"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
    52	[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi=[34m1[39;49;00m;i<NUMBER_BUILTIN_STYLES;[37m [39;49;00mi++)[37m [39;49;00m{[37m[39;49;00m$
    53	[37m        [39;49;00mstyleTagClose.push_back([33m"[39;49;00m[33m\033[39;49;00m[33m[m[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
    54	[37m    [39;49;00m}[37m[39;49;00m$
    55	[37m    [39;49;00mnewLineTag[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
    56	[37m    [39;49;00mspacer[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
    57	}[37m[39;49;00m$
    58	[37m[39;49;00m$
    59	AnsiGenerator::AnsiGenerator()[37m [39;49;00m{}[37m[39;49;00m$
    60	AnsiGenerator::~AnsiGenerator()[37m [39;49;00m{}[37m[39;49;00m$
    61	[37m[39;49;00m$
    62	string[37m [39;49;00mAnsiGenerator::getHeader([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&[37m [39;49;00mtitle)[37m [39;49;00m{[37m[39;49;00m$
    63	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mstring();[37m[39;49;00m$
    64	}[37m[39;49;00m$
    65	[37m[39;49;00m$
    66	[36mvoid[39;49;00m[37m [39;49;00mAnsiGenerator::printBody()[37m [39;49;00m{[37m[39;49;00m$
    67	[37m    [39;49;00mprocessRootState();[37m[39;49;00m$
    68	}[37m[39;49;00m$
    69	[37m[39;49;00m$
    70	string[37m [39;49;00mAnsiGenerator::getFooter()[37m [39;49;00m{[37m[39;49;00m$
    71	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mstring();[37m[39;49;00m$
    72	}[37m[39;49;00m$
    73	[37m[39;49;00m$
    74	string[37m [39;49;00mAnsiGenerator::maskCharacter([36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00mc)[37m [39;49;00m{[37m[39;49;00m$
    75	[37m    [39;49;00mstring[37m [39;49;00mm;[37m[39;49;00m$
    76	[37m    [39;49;00mm+=c;[37m[39;49;00m$
    77	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mm;[37m[39;49;00m$
    78	}[37m[39;49;00m$
    79	[37m[39;49;00m$
    80	string[37m [39;49;00mAnsiGenerator::getMatchingOpenTag([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mstyleID)[37m [39;49;00m{[37m[39;49;00m$
    81	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m(styleID)?getOpenTag([33m"[39;49;00m[33m01[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m32[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m):getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m33[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
    82	}[37m[39;49;00m$
    83	[37m[39;49;00m$
    84	string[37m [39;49;00mAnsiGenerator::getMatchingCloseTag([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mstyleID)[37m [39;49;00m{[37m[39;49;00m$
    85	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\033[39;49;00m[33m[m[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
    86	}[37m[39;49;00m$
    87	[37m[39;49;00m$
    88	}[37m[39;49;00m$
    89	[37m/***************************************************************************[39;49;00m$
    90	[37m                         ansicode.h  -  description[39;49;00m$
    91	[37m                             -------------------[39;49;00m$
    92	[37m    begin                : Jul 5 2004[39;49;00m$
    93	[37m    copyright            : (C) 2004 by Andre Simon[39;49;00m$
    94	[37m    email                : andre.simon1@gmx.de[39;49;00m$
    95	[37m ***************************************************************************/[39;49;00m[37m[39;49;00m$
    96	[37m[39;49;00m$
    97	[37m/***************************************************************************[39;49;00m$
    98	[37m *                                                                         *[39;49;00m$
    99	[37m *   This program is free software; you can redistribute it and/or modify  *[39;49;00m$
   100	[37m *   it under the terms of the GNU General Public License as published by  *[39;49;00m$
   101	[37m *   the Free Software Foundation; either version 2 of the License, or     *[39;49;00m$
   102	[37m *   (at your option) any later version.                                   *[39;49;00m$
   103	[37m *                                                                         *[39;49;00m$
   104	[37m ***************************************************************************/[39;49;00m[37m[39;49;00m$
   105	[37m[39;49;00m$
   106	[36m#[39;49;00m[36mifndef ANSIGENERATOR_H[39;49;00m[36m[39;49;00m$
   107	[36m#[39;49;00m[36mdefine ANSIGENERATOR_H[39;49;00m[36m[39;49;00m$
   108	[37m[39;49;00m$
   109	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<iostream>[39;49;00m[36m[39;49;00m$
   110	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<fstream>[39;49;00m[36m[39;49;00m$
   111	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<string>[39;49;00m[36m[39;49;00m$
   112	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<sstream>[39;49;00m[36m[39;49;00m$
   113	[37m[39;49;00m$
   114	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"codegenerator.h"[39;49;00m[36m[39;49;00m$
   115	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"charcodes.h"[39;49;00m[36m[39;49;00m$
   116	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"version.h"[39;49;00m[36m[39;49;00m$
   117	[37m[39;49;00m$
   118	[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mhighlight[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
   119	[37m[39;49;00m$
   120	[37m/**[39;49;00m$
   121	[37m   \brief This class generates ANSI escape sequences.[39;49;00m$
   122	[37m[39;49;00m$
   123	[37m   It contains information about the resulting document structure (document[39;49;00m$
   124	[37m   header and footer), the colour system, white space handling and text[39;49;00m$
   125	[37m   formatting attributes.[39;49;00m$
   126	[37m[39;49;00m$
   127	[37m* @author Andre Simon[39;49;00m$
   128	[37m*/[39;49;00m[37m[39;49;00m$
   129	[37m[39;49;00m$
   130	[34mclass[39;49;00m[37m [39;49;00m[04m[32mAnsiGenerator[39;49;00m[37m [39;49;00m:[37m [39;49;00m[34mpublic[39;49;00m[37m [39;49;00mhighlight::CodeGenerator[37m[39;49;00m$
   131	[37m  [39;49;00m{[37m[39;49;00m$
   132	[37m  [39;49;00m[34mpublic[39;49;00m:[37m[39;49;00m$
   133	[37m[39;49;00m$
   134	[37m   [39;49;00m[37m/** Constructor[39;49;00m$
   135	[37m     \param colourTheme Name of Colour theme to use[39;49;00m$
   136	[37m    */[39;49;00m[37m[39;49;00m$
   137	[37m    [39;49;00mAnsiGenerator([37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&colourTheme);[37m[39;49;00m$
   138	[37m    [39;49;00mAnsiGenerator();[37m[39;49;00m$
   139	[37m    [39;49;00m~AnsiGenerator();[37m[39;49;00m$
   140	[37m[39;49;00m$
   141	[37m   [39;49;00m[37m/** prints document header[39;49;00m$
   142	[37m       \param  title Title of the document[39;49;00m$
   143	[37m    */[39;49;00m[37m[39;49;00m$
   144	[37m    [39;49;00mstring[37m [39;49;00m[32mgetHeader[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&[37m [39;49;00mtitle);[37m[39;49;00m$
   145	[37m[39;49;00m$
   146	[37m    [39;49;00m[37m/** Prints document footer*/[39;49;00m[37m[39;49;00m$
   147	[37m    [39;49;00mstring[37m [39;49;00m[32mgetFooter[39;49;00m();[37m[39;49;00m$
   148	[37m[39;49;00m$
   149	[37m    [39;49;00m[37m/** Prints document body*/[39;49;00m[37m[39;49;00m$
   150	[37m    [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mprintBody[39;49;00m();[37m[39;49;00m$
   151	[37m[39;49;00m$
   152	[37m  [39;49;00m[34mprivate[39;49;00m:[37m[39;49;00m$
   153	[37m[39;49;00m$
   154	[37m    [39;49;00m[37m/** \return escaped character*/[39;49;00m[37m[39;49;00m$
   155	[37m    [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00mstring[37m [39;49;00mmaskCharacter([36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m);[37m[39;49;00m$
   156	[37m[39;49;00m$
   157	[37m[39;49;00m$
   158	[37m    [39;49;00m[37m/** gibt ANSI-"Tags" zurueck (Farbindex+bold+kursiv)*/[39;49;00m[37m[39;49;00m$
   159	[37m    [39;49;00mstring[37m [39;49;00m[32mgetOpenTag[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring&font,[37m[39;49;00m$
   160	[37m                      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring&fgCol,[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring&bgCol=[33m"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
   161	[37m[39;49;00m$
   162	[37m[39;49;00m$
   163	[37m[39;49;00m$
   164	[37m    [39;49;00mstring[37m [39;49;00m[32mgetMatchingOpenTag[39;49;00m([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mstyleID);[37m[39;49;00m$
   165	[37m    [39;49;00mstring[37m [39;49;00m[32mgetMatchingCloseTag[39;49;00m([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mstyleID);[37m[39;49;00m$
   166	[37m  [39;49;00m};[37m[39;49;00m$
   167	[37m[39;49;00m$
   168	}[37m[39;49;00m$
   169	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   170	[37m/*[39;49;00m$
   171	[37m * Copyright (c) 1998,1999,2000,2001,2002 Tal Davidson. All rights reserved.[39;49;00m$
   172	[37m *[39;49;00m$
   173	[37m * ASBeautifier.cpp[39;49;00m$
   174	[37m * by Tal Davidson (davidsont@bigfoot.com)[39;49;00m$
   175	[37m * This file is a part of "Artistic Style" - an indentater and reformatter[39;49;00m$
   176	[37m * of C, C, C# and Java source files.[39;49;00m$
   177	[37m *[39;49;00m$
   178	[37m * The "Artistic Style" project, including all files needed to compile it,[39;49;00m$
   179	[37m * is free software; you can redistribute it and/or use it and/or modify it[39;49;00m$
   180	[37m * under the terms of the GNU General Public License as published [39;49;00m$
   181	[37m * by the Free Software Foundation; either version 2 of the License, [39;49;00m$
   182	[37m * or (at your option) any later version.[39;49;00m$
   183	[37m *[39;49;00m$
   184	[37m * This program is distributed in the hope that it will be useful,[39;49;00m$
   185	[37m * but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m$
   186	[37m * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.[39;49;00m$
   187	[37m *[39;49;00m$
   188	[37m * You should have received a copy of the GNU General Public[39;49;00m$
   189	[37m * License along with this program.[39;49;00m$
   190	[37m *[39;49;00m$
   191	[37m * Patches:[39;49;00m$
   192	[37m * 18 March 1999 - Brian Rampel -[39;49;00m$
   193	[37m *       Fixed inverse insertion of spaces vs. tabs when in -t mode.[39;49;00m$
   194	[37m * 08 may 2004 [39;49;00m$
   195	[37m *       applied ASBeautifier.cpp.BITFIELD.patch.bz2[39;49;00m$
   196	[37m */[39;49;00m[37m[39;49;00m$
   197	[37m[39;49;00m$
   198	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"compiler_defines.h"[39;49;00m[36m[39;49;00m$
   199	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"ASBeautifier.h"[39;49;00m[36m[39;49;00m$
   200	[37m[39;49;00m$
   201	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<vector>[39;49;00m[36m[39;49;00m$
   202	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<string>[39;49;00m[36m[39;49;00m$
   203	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<cctype>[39;49;00m[36m[39;49;00m$
   204	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<algorithm>[39;49;00m[36m[39;49;00m$
   205	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<iostream>[39;49;00m[36m[39;49;00m$
   206	[37m[39;49;00m$
   207	[37m[39;49;00m$
   208	[36m#[39;49;00m[36mdefine INIT_CONTAINER(container, value)     {if ( (container) != NULL ) delete (container); (container) = (value); }[39;49;00m[36m[39;49;00m$
   209	[36m#[39;49;00m[36mdefine DELETE_CONTAINER(container)          {if ( (container) != NULL ) delete (container) ; }[39;49;00m[36m[39;49;00m$
   210	[37m[39;49;00m$
   211	[36m#[39;49;00m[36mifdef USES_NAMESPACE[39;49;00m[36m[39;49;00m$
   212	[34musing[39;49;00m[37m [39;49;00m[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mstd[39;49;00m;[37m[39;49;00m$
   213	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   214	[37m[39;49;00m$
   215	[37m[39;49;00m$
   216	[37m[39;49;00m$
   217	[37m[39;49;00m$
   218	[36m#[39;49;00m[36mifdef USES_NAMESPACE[39;49;00m[36m[39;49;00m$
   219	[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mastyle[39;49;00m[37m[39;49;00m$
   220	[37m  [39;49;00m{[37m[39;49;00m$
   221	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
   222	[37m[39;49;00m$
   223	[37m  [39;49;00m[36mbool[39;49;00m[37m [39;49;00mASBeautifier::calledInitStatic[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   224	[37m[39;49;00m$
   225	[37m  [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mASBeautifier::headers;[37m[39;49;00m$
   226	[37m  [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mASBeautifier::nonParenHeaders;[37m[39;49;00m$
   227	[37m  [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mASBeautifier::preBlockStatements;[37m[39;49;00m$
   228	[37m  [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mASBeautifier::assignmentOperators;[37m[39;49;00m$
   229	[37m  [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mASBeautifier::nonAssignmentOperators;[37m[39;49;00m$
   230	[37m[39;49;00m$
   231	[37m  [39;49;00m[37m/*[39;49;00m$
   232	[37m   * initialize the static vars[39;49;00m$
   233	[37m   */[39;49;00m[37m[39;49;00m$
   234	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mASBeautifier::initStatic[39;49;00m()[37m[39;49;00m$
   235	[37m  [39;49;00m{[37m[39;49;00m$
   236	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(calledInitStatic)[37m[39;49;00m$
   237	[37m      [39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
   238	[37m[39;49;00m$
   239	[37m    [39;49;00mcalledInitStatic[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
   240	[37m[39;49;00m$
   241	[37m    [39;49;00mheaders.push_back(&AS_IF);[37m[39;49;00m$
   242	[37m    [39;49;00mheaders.push_back(&AS_ELSE);[37m[39;49;00m$
   243	[37m    [39;49;00mheaders.push_back(&AS_FOR);[37m[39;49;00m$
   244	[37m    [39;49;00mheaders.push_back(&AS_WHILE);[37m[39;49;00m$
   245	[37m    [39;49;00mheaders.push_back(&AS_DO);[37m[39;49;00m$
   246	[37m    [39;49;00mheaders.push_back(&AS_TRY);[37m[39;49;00m$
   247	[37m    [39;49;00mheaders.push_back(&AS_CATCH);[37m[39;49;00m$
   248	[37m    [39;49;00mheaders.push_back(&AS_FINALLY);[37m[39;49;00m$
   249	[37m    [39;49;00mheaders.push_back(&AS_SYNCHRONIZED);[37m[39;49;00m$
   250	[37m    [39;49;00mheaders.push_back(&AS_SWITCH);[37m[39;49;00m$
   251	[37m    [39;49;00mheaders.push_back(&AS_CASE);[37m[39;49;00m$
   252	[37m    [39;49;00mheaders.push_back(&AS_DEFAULT);[37m[39;49;00m$
   253	[37m    [39;49;00mheaders.push_back(&AS_FOREACH);[37m[39;49;00m$
   254	[37m    [39;49;00mheaders.push_back(&AS_LOCK);[37m[39;49;00m$
   255	[37m    [39;49;00mheaders.push_back(&AS_UNSAFE);[37m[39;49;00m$
   256	[37m    [39;49;00mheaders.push_back(&AS_FIXED);[37m[39;49;00m$
   257	[37m    [39;49;00mheaders.push_back(&AS_GET);[37m[39;49;00m$
   258	[37m    [39;49;00mheaders.push_back(&AS_SET);[37m[39;49;00m$
   259	[37m    [39;49;00mheaders.push_back(&AS_ADD);[37m[39;49;00m$
   260	[37m    [39;49;00mheaders.push_back(&AS_REMOVE);[37m[39;49;00m$
   261	[37m    [39;49;00m[37m//headers.push_back(&AS_PUBLIC);[39;49;00m$
   262	[37m    [39;49;00m[37m//headers.push_back(&AS_PRIVATE);[39;49;00m$
   263	[37m    [39;49;00m[37m//headers.push_back(&AS_PROTECTED);[39;49;00m$
   264	[37m[39;49;00m$
   265	[37m    [39;49;00m[37m//headers.push_back(&AS_OPERATOR);[39;49;00m$
   266	[37m    [39;49;00mheaders.push_back(&AS_TEMPLATE);[37m[39;49;00m$
   267	[37m    [39;49;00mheaders.push_back(&AS_CONST);[37m[39;49;00m$
   268	[37m    [39;49;00m[37m/**/[39;49;00m[37m[39;49;00m$
   269	[37m    [39;49;00mheaders.push_back(&AS_STATIC);[37m[39;49;00m$
   270	[37m    [39;49;00mheaders.push_back(&AS_EXTERN);[37m[39;49;00m$
   271	[37m[39;49;00m$
   272	[37m    [39;49;00mnonParenHeaders.push_back(&AS_ELSE);[37m[39;49;00m$
   273	[37m    [39;49;00mnonParenHeaders.push_back(&AS_DO);[37m[39;49;00m$
   274	[37m    [39;49;00mnonParenHeaders.push_back(&AS_TRY);[37m[39;49;00m$
   275	[37m    [39;49;00mnonParenHeaders.push_back(&AS_FINALLY);[37m[39;49;00m$
   276	[37m    [39;49;00mnonParenHeaders.push_back(&AS_STATIC);[37m[39;49;00m$
   277	[37m    [39;49;00mnonParenHeaders.push_back(&AS_CONST);[37m[39;49;00m$
   278	[37m    [39;49;00mnonParenHeaders.push_back(&AS_EXTERN);[37m[39;49;00m$
   279	[37m    [39;49;00mnonParenHeaders.push_back(&AS_CASE);[37m[39;49;00m$
   280	[37m    [39;49;00mnonParenHeaders.push_back(&AS_DEFAULT);[37m[39;49;00m$
   281	[37m    [39;49;00mnonParenHeaders.push_back(&AS_UNSAFE);[37m[39;49;00m$
   282	[37m    [39;49;00mnonParenHeaders.push_back(&AS_GET);[37m[39;49;00m$
   283	[37m    [39;49;00mnonParenHeaders.push_back(&AS_SET);[37m[39;49;00m$
   284	[37m    [39;49;00mnonParenHeaders.push_back(&AS_ADD);[37m[39;49;00m$
   285	[37m    [39;49;00mnonParenHeaders.push_back(&AS_REMOVE);[37m[39;49;00m$
   286	[37m[39;49;00m$
   287	[37m[39;49;00m$
   288	[37m[39;49;00m$
   289	[37m    [39;49;00mnonParenHeaders.push_back(&AS_PUBLIC);[37m[39;49;00m$
   290	[37m    [39;49;00mnonParenHeaders.push_back(&AS_PRIVATE);[37m[39;49;00m$
   291	[37m    [39;49;00mnonParenHeaders.push_back(&AS_PROTECTED);[37m[39;49;00m$
   292	[37m    [39;49;00mnonParenHeaders.push_back(&AS_TEMPLATE);[37m[39;49;00m$
   293	[37m    [39;49;00mnonParenHeaders.push_back(&AS_CONST);[37m[39;49;00m$
   294	[37m    [39;49;00m[37m///    nonParenHeaders.push_back(&AS_ASM);[39;49;00m$
   295	[37m[39;49;00m$
   296	[37m    [39;49;00mpreBlockStatements.push_back(&AS_CLASS);[37m[39;49;00m$
   297	[37m    [39;49;00mpreBlockStatements.push_back(&AS_STRUCT);[37m[39;49;00m$
   298	[37m    [39;49;00mpreBlockStatements.push_back(&AS_UNION);[37m[39;49;00m$
   299	[37m    [39;49;00mpreBlockStatements.push_back(&AS_INTERFACE);[37m[39;49;00m$
   300	[37m    [39;49;00mpreBlockStatements.push_back(&AS_NAMESPACE);[37m[39;49;00m$
   301	[37m    [39;49;00mpreBlockStatements.push_back(&AS_THROWS);[37m[39;49;00m$
   302	[37m    [39;49;00mpreBlockStatements.push_back(&AS_EXTERN);[37m[39;49;00m$
   303	[37m[39;49;00m$
   304	[37m    [39;49;00massignmentOperators.push_back(&AS_ASSIGN);[37m[39;49;00m$
   305	[37m    [39;49;00massignmentOperators.push_back(&AS_PLUS_ASSIGN);[37m[39;49;00m$
   306	[37m    [39;49;00massignmentOperators.push_back(&AS_MINUS_ASSIGN);[37m[39;49;00m$
   307	[37m    [39;49;00massignmentOperators.push_back(&AS_MULT_ASSIGN);[37m[39;49;00m$
   308	[37m    [39;49;00massignmentOperators.push_back(&AS_DIV_ASSIGN);[37m[39;49;00m$
   309	[37m    [39;49;00massignmentOperators.push_back(&AS_MOD_ASSIGN);[37m[39;49;00m$
   310	[37m    [39;49;00massignmentOperators.push_back(&AS_OR_ASSIGN);[37m[39;49;00m$
   311	[37m    [39;49;00massignmentOperators.push_back(&AS_AND_ASSIGN);[37m[39;49;00m$
   312	[37m    [39;49;00massignmentOperators.push_back(&AS_XOR_ASSIGN);[37m[39;49;00m$
   313	[37m    [39;49;00massignmentOperators.push_back(&AS_GR_GR_GR_ASSIGN);[37m[39;49;00m$
   314	[37m    [39;49;00massignmentOperators.push_back(&AS_GR_GR_ASSIGN);[37m[39;49;00m$
   315	[37m    [39;49;00massignmentOperators.push_back(&AS_LS_LS_LS_ASSIGN);[37m[39;49;00m$
   316	[37m    [39;49;00massignmentOperators.push_back(&AS_LS_LS_ASSIGN);[37m[39;49;00m$
   317	[37m[39;49;00m$
   318	[37m    [39;49;00massignmentOperators.push_back(&AS_RETURN);[37m[39;49;00m$
   319	[37m[39;49;00m$
   320	[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_EQUAL);[37m[39;49;00m$
   321	[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_PLUS_PLUS);[37m[39;49;00m$
   322	[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_MINUS_MINUS);[37m[39;49;00m$
   323	[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_NOT_EQUAL);[37m[39;49;00m$
   324	[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_GR_EQUAL);[37m[39;49;00m$
   325	[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_GR_GR_GR);[37m[39;49;00m$
   326	[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_GR_GR);[37m[39;49;00m$
   327	[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_LS_EQUAL);[37m[39;49;00m$
   328	[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_LS_LS_LS);[37m[39;49;00m$
   329	[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_LS_LS);[37m[39;49;00m$
   330	[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_ARROW);[37m[39;49;00m$
   331	[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_AND);[37m[39;49;00m$
   332	[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_OR);[37m[39;49;00m$
   333	[37m  [39;49;00m}[37m[39;49;00m$
   334	[37m[39;49;00m$
   335	[37m  [39;49;00m[37m/**[39;49;00m$
   336	[37m   * ASBeautifier's constructor[39;49;00m$
   337	[37m   */[39;49;00m[37m[39;49;00m$
   338	[37m  [39;49;00mASBeautifier::ASBeautifier()[37m[39;49;00m$
   339	[37m  [39;49;00m{[37m[39;49;00m$
   340	[37m    [39;49;00minitStatic();[37m[39;49;00m$
   341	[37m[39;49;00m$
   342	[37m    [39;49;00mwaitingBeautifierStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   343	[37m    [39;49;00mactiveBeautifierStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   344	[37m    [39;49;00mwaitingBeautifierStackLengthStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   345	[37m    [39;49;00mactiveBeautifierStackLengthStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   346	[37m[39;49;00m$
   347	[37m    [39;49;00mheaderStack[37m  [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   348	[37m    [39;49;00mtempStacks[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   349	[37m    [39;49;00mblockParenDepthStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   350	[37m    [39;49;00mblockStatementStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   351	[37m    [39;49;00mparenStatementStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   352	[37m    [39;49;00mbracketBlockStateStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   353	[37m    [39;49;00minStatementIndentStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   354	[37m    [39;49;00minStatementIndentStackSizeStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   355	[37m    [39;49;00mparenIndentStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   356	[37m    [39;49;00msourceIterator[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   357	[37m[39;49;00m$
   358	[37m    [39;49;00misMinimalConditinalIndentSet[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   359	[37m    [39;49;00mshouldForceTabIndentation[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   360	[37m[39;49;00m$
   361	[37m    [39;49;00msetSpaceIndentation([34m4[39;49;00m);[37m[39;49;00m$
   362	[37m    [39;49;00msetMaxInStatementIndentLength([34m40[39;49;00m);[37m[39;49;00m$
   363	[37m    [39;49;00msetClassIndent([36mfalse[39;49;00m);[37m[39;49;00m$
   364	[37m    [39;49;00msetSwitchIndent([36mfalse[39;49;00m);[37m[39;49;00m$
   365	[37m    [39;49;00msetCaseIndent([36mfalse[39;49;00m);[37m[39;49;00m$
   366	[37m    [39;49;00msetBlockIndent([36mfalse[39;49;00m);[37m[39;49;00m$
   367	[37m    [39;49;00msetBracketIndent([36mfalse[39;49;00m);[37m[39;49;00m$
   368	[37m    [39;49;00msetNamespaceIndent([36mfalse[39;49;00m);[37m[39;49;00m$
   369	[37m    [39;49;00msetLabelIndent([36mfalse[39;49;00m);[37m[39;49;00m$
   370	[37m    [39;49;00msetEmptyLineFill([36mfalse[39;49;00m);[37m[39;49;00m$
   371	[37m    [39;49;00msetCStyle();[37m[39;49;00m$
   372	[37m    [39;49;00msetPreprocessorIndent([36mfalse[39;49;00m);[37m[39;49;00m$
   373	[37m  [39;49;00m}[37m[39;49;00m$
   374	[37m[39;49;00m$
   375	[37m  [39;49;00mASBeautifier::ASBeautifier([34mconst[39;49;00m[37m [39;49;00mASBeautifier[37m [39;49;00m&other)[37m[39;49;00m$
   376	[37m  [39;49;00m{[37m[39;49;00m$
   377	[37m    [39;49;00mwaitingBeautifierStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   378	[37m    [39;49;00mactiveBeautifierStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   379	[37m    [39;49;00mwaitingBeautifierStackLengthStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   380	[37m    [39;49;00mactiveBeautifierStackLengthStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   381	[37m[39;49;00m$
   382	[37m    [39;49;00mheaderStack[37m  [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>;[37m[39;49;00m$
   383	[37m    [39;49;00m*headerStack[37m [39;49;00m=[37m [39;49;00m*other.headerStack;[37m[39;49;00m$
   384	[37m[39;49;00m$
   385	[37m    [39;49;00mtempStacks[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>*[37m [39;49;00m>;[37m[39;49;00m$
   386	[37m    [39;49;00mvector<[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>*[37m [39;49;00m>::iterator[37m [39;49;00miter;[37m[39;49;00m$
   387	[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(iter[37m [39;49;00m=[37m [39;49;00mother.tempStacks->begin();[37m[39;49;00m$
   388	[37m         [39;49;00miter[37m [39;49;00m!=[37m [39;49;00mother.tempStacks->end();[37m[39;49;00m$
   389	[37m         [39;49;00m++iter)[37m[39;49;00m$
   390	[37m      [39;49;00m{[37m[39;49;00m$
   391	[37m        [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m*newVec[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>;[37m[39;49;00m$
   392	[37m        [39;49;00m*newVec[37m [39;49;00m=[37m [39;49;00m**iter;[37m[39;49;00m$
   393	[37m        [39;49;00mtempStacks->push_back(newVec);[37m[39;49;00m$
   394	[37m      [39;49;00m}[37m[39;49;00m$
   395	[37m    [39;49;00mblockParenDepthStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>;[37m[39;49;00m$
   396	[37m    [39;49;00m*blockParenDepthStack[37m [39;49;00m=[37m [39;49;00m*other.blockParenDepthStack;[37m[39;49;00m$
   397	[37m[39;49;00m$
   398	[37m    [39;49;00mblockStatementStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>;[37m[39;49;00m$
   399	[37m    [39;49;00m*blockStatementStack[37m [39;49;00m=[37m [39;49;00m*other.blockStatementStack;[37m[39;49;00m$
   400	[37m[39;49;00m$
   401	[37m    [39;49;00mparenStatementStack[37m [39;49;00m=[37m  [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>;[37m[39;49;00m$
   402	[37m    [39;49;00m*parenStatementStack[37m [39;49;00m=[37m [39;49;00m*other.parenStatementStack;[37m[39;49;00m$
   403	[37m[39;49;00m$
   404	[37m    [39;49;00mbracketBlockStateStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>;[37m[39;49;00m$
   405	[37m    [39;49;00m*bracketBlockStateStack[37m [39;49;00m=[37m [39;49;00m*other.bracketBlockStateStack;[37m[39;49;00m$
   406	[37m[39;49;00m$
   407	[37m    [39;49;00minStatementIndentStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>;[37m[39;49;00m$
   408	[37m    [39;49;00m*inStatementIndentStack[37m [39;49;00m=[37m [39;49;00m*other.inStatementIndentStack;[37m[39;49;00m$
   409	[37m[39;49;00m$
   410	[37m    [39;49;00minStatementIndentStackSizeStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>;[37m[39;49;00m$
   411	[37m    [39;49;00m*inStatementIndentStackSizeStack[37m [39;49;00m=[37m [39;49;00m*other.inStatementIndentStackSizeStack;[37m[39;49;00m$
   412	[37m[39;49;00m$
   413	[37m    [39;49;00mparenIndentStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>;[37m[39;49;00m$
   414	[37m    [39;49;00m*parenIndentStack[37m [39;49;00m=[37m [39;49;00m*other.parenIndentStack;[37m[39;49;00m$
   415	[37m[39;49;00m$
   416	[37m    [39;49;00msourceIterator[37m [39;49;00m=[37m [39;49;00mother.sourceIterator;[37m[39;49;00m$
   417	[37m[39;49;00m$
   418	[37m    [39;49;00mindentString[37m [39;49;00m=[37m [39;49;00mother.indentString;[37m[39;49;00m$
   419	[37m    [39;49;00mcurrentHeader[37m [39;49;00m=[37m [39;49;00mother.currentHeader;[37m[39;49;00m$
   420	[37m    [39;49;00mpreviousLastLineHeader[37m [39;49;00m=[37m [39;49;00mother.previousLastLineHeader;[37m[39;49;00m$
   421	[37m    [39;49;00mimmediatelyPreviousAssignmentOp[37m [39;49;00m=[37m [39;49;00mother.immediatelyPreviousAssignmentOp;[37m[39;49;00m$
   422	[37m    [39;49;00misInQuote[37m [39;49;00m=[37m [39;49;00mother.isInQuote;[37m[39;49;00m$
   423	[37m    [39;49;00misInComment[37m [39;49;00m=[37m [39;49;00mother.isInComment;[37m[39;49;00m$
   424	[37m    [39;49;00misInCase[37m [39;49;00m=[37m [39;49;00mother.isInCase;[37m[39;49;00m$
   425	[37m    [39;49;00misInQuestion[37m [39;49;00m=[37m [39;49;00mother.isInQuestion;[37m[39;49;00m$
   426	[37m    [39;49;00misInStatement[37m [39;49;00m=other.[37m [39;49;00misInStatement;[37m[39;49;00m$
   427	[37m    [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00mother.isInHeader;[37m[39;49;00m$
   428	[37m    [39;49;00misCStyle[37m [39;49;00m=[37m [39;49;00mother.isCStyle;[37m[39;49;00m$
   429	[37m    [39;49;00misInOperator[37m [39;49;00m=[37m [39;49;00mother.isInOperator;[37m[39;49;00m$
   430	[37m    [39;49;00misInTemplate[37m [39;49;00m=[37m [39;49;00mother.isInTemplate;[37m[39;49;00m$
   431	[37m    [39;49;00misInConst[37m [39;49;00m=[37m [39;49;00mother.isInConst;[37m[39;49;00m$
   432	[37m    [39;49;00mclassIndent[37m [39;49;00m=[37m [39;49;00mother.classIndent;[37m[39;49;00m$
   433	[37m    [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00mother.isInClassHeader;[37m[39;49;00m$
   434	[37m    [39;49;00misInClassHeaderTab[37m [39;49;00m=[37m [39;49;00mother.isInClassHeaderTab;[37m[39;49;00m$
   435	[37m    [39;49;00mswitchIndent[37m [39;49;00m=[37m [39;49;00mother.switchIndent;[37m[39;49;00m$
   436	[37m    [39;49;00mcaseIndent[37m [39;49;00m=[37m [39;49;00mother.caseIndent;[37m[39;49;00m$
   437	[37m    [39;49;00mnamespaceIndent[37m [39;49;00m=[37m [39;49;00mother.namespaceIndent;[37m[39;49;00m$
   438	[37m    [39;49;00mbracketIndent[37m [39;49;00m=[37m [39;49;00mother.bracketIndent;[37m[39;49;00m$
   439	[37m    [39;49;00mblockIndent[37m [39;49;00m=[37m [39;49;00mother.blockIndent;[37m[39;49;00m$
   440	[37m    [39;49;00mlabelIndent[37m [39;49;00m=[37m [39;49;00mother.labelIndent;[37m[39;49;00m$
   441	[37m    [39;49;00mpreprocessorIndent[37m [39;49;00m=[37m [39;49;00mother.preprocessorIndent;[37m[39;49;00m$
   442	[37m    [39;49;00mparenDepth[37m [39;49;00m=[37m [39;49;00mother.parenDepth;[37m[39;49;00m$
   443	[37m    [39;49;00mindentLength[37m [39;49;00m=[37m [39;49;00mother.indentLength;[37m[39;49;00m$
   444	[37m    [39;49;00mblockTabCount[37m [39;49;00m=[37m [39;49;00mother.blockTabCount;[37m[39;49;00m$
   445	[37m    [39;49;00mleadingWhiteSpaces[37m [39;49;00m=[37m [39;49;00mother.leadingWhiteSpaces;[37m[39;49;00m$
   446	[37m    [39;49;00mmaxInStatementIndent[37m [39;49;00m=[37m [39;49;00mother.maxInStatementIndent;[37m[39;49;00m$
   447	[37m    [39;49;00mtemplateDepth[37m [39;49;00m=[37m [39;49;00mother.templateDepth;[37m[39;49;00m$
   448	[37m    [39;49;00mquoteChar[37m [39;49;00m=[37m [39;49;00mother.quoteChar;[37m[39;49;00m$
   449	[37m    [39;49;00mprevNonSpaceCh[37m [39;49;00m=[37m [39;49;00mother.prevNonSpaceCh;[37m[39;49;00m$
   450	[37m    [39;49;00mcurrentNonSpaceCh[37m [39;49;00m=[37m [39;49;00mother.currentNonSpaceCh;[37m[39;49;00m$
   451	[37m    [39;49;00mcurrentNonLegalCh[37m [39;49;00m=[37m [39;49;00mother.currentNonLegalCh;[37m[39;49;00m$
   452	[37m    [39;49;00mprevNonLegalCh[37m [39;49;00m=[37m [39;49;00mother.prevNonLegalCh;[37m[39;49;00m$
   453	[37m    [39;49;00misInConditional[37m [39;49;00m=[37m [39;49;00mother.isInConditional;[37m[39;49;00m$
   454	[37m    [39;49;00mminConditionalIndent[37m [39;49;00m=[37m [39;49;00mother.minConditionalIndent;[37m[39;49;00m$
   455	[37m    [39;49;00mprevFinalLineSpaceTabCount[37m [39;49;00m=[37m [39;49;00mother.prevFinalLineSpaceTabCount;[37m[39;49;00m$
   456	[37m    [39;49;00mprevFinalLineTabCount[37m [39;49;00m=[37m [39;49;00mother.prevFinalLineTabCount;[37m[39;49;00m$
   457	[37m    [39;49;00memptyLineFill[37m [39;49;00m=[37m [39;49;00mother.emptyLineFill;[37m[39;49;00m$
   458	[37m    [39;49;00mprobationHeader[37m [39;49;00m=[37m [39;49;00mother.probationHeader;[37m[39;49;00m$
   459	[37m    [39;49;00misInDefine[37m [39;49;00m=[37m [39;49;00mother.isInDefine;[37m[39;49;00m$
   460	[37m    [39;49;00misInDefineDefinition[37m [39;49;00m=[37m [39;49;00mother.isInDefineDefinition;[37m[39;49;00m$
   461	[37m    [39;49;00mbackslashEndsPrevLine[37m [39;49;00m=[37m [39;49;00mother.backslashEndsPrevLine;[37m[39;49;00m$
   462	[37m    [39;49;00mdefineTabCount[37m [39;49;00m=[37m [39;49;00mother.defineTabCount;[37m[39;49;00m$
   463	[37m  [39;49;00m}[37m[39;49;00m$
   464	[37m[39;49;00m$
   465	[37m  [39;49;00m[37m/**[39;49;00m$
   466	[37m   * ASBeautifier's destructor[39;49;00m$
   467	[37m   */[39;49;00m[37m[39;49;00m$
   468	[37m  [39;49;00mASBeautifier::~ASBeautifier()[37m[39;49;00m$
   469	[37m  [39;49;00m{[37m[39;49;00m$
   470	[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mheaderStack[37m [39;49;00m);[37m[39;49;00m$
   471	[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mtempStacks[37m [39;49;00m);[37m[39;49;00m$
   472	[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mblockParenDepthStack[37m [39;49;00m);[37m[39;49;00m$
   473	[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mblockStatementStack[37m [39;49;00m);[37m[39;49;00m$
   474	[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mparenStatementStack[37m [39;49;00m);[37m[39;49;00m$
   475	[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mbracketBlockStateStack[37m [39;49;00m);[37m[39;49;00m$
   476	[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00minStatementIndentStack[37m [39;49;00m);[37m[39;49;00m$
   477	[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00minStatementIndentStackSizeStack[37m [39;49;00m);[37m[39;49;00m$
   478	[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mparenIndentStack[37m [39;49;00m);[37m[39;49;00m$
   479	[37m[39;49;00m$
   480	[37m    [39;49;00m[37m// DELETE_CONTAINER( sourceIterator );[39;49;00m$
   481	[37m  [39;49;00m}[37m[39;49;00m$
   482	[37m[39;49;00m$
   483	[37m  [39;49;00m[37m/**[39;49;00m$
   484	[37m   * initialize the ASBeautifier.[39;49;00m$
   485	[37m   *[39;49;00m$
   486	[37m   * init() should be called every time a ABeautifier object is to start[39;49;00m$
   487	[37m   * beautifying a NEW source file.[39;49;00m$
   488	[37m   * init() recieves a pointer to a DYNAMICALLY CREATED ASSourceIterator object[39;49;00m$
   489	[37m   * that will be used to iterate through the source code. This object will be[39;49;00m$
   490	[37m   * deleted during the ASBeautifier's destruction, and thus should not be[39;49;00m$
   491	[37m   * deleted elsewhere.[39;49;00m$
   492	[37m   *[39;49;00m$
   493	[37m   * @param iter     a pointer to the DYNAMICALLY CREATED ASSourceIterator object.[39;49;00m$
   494	[37m   */[39;49;00m[37m[39;49;00m$
   495	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::init(ASSourceIterator[37m [39;49;00m*iter)[37m[39;49;00m$
   496	[37m[39;49;00m$
   497	[37m  [39;49;00m{[37m[39;49;00m$
   498	[37m    [39;49;00msourceIterator[37m [39;49;00m=[37m [39;49;00miter;[37m[39;49;00m$
   499	[37m    [39;49;00minit();[37m[39;49;00m$
   500	[37m  [39;49;00m}[37m[39;49;00m$
   501	[37m[39;49;00m$
   502	[37m  [39;49;00m[37m/**[39;49;00m$
   503	[37m   * initialize the ASBeautifier.[39;49;00m$
   504	[37m   */[39;49;00m[37m[39;49;00m$
   505	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::init()[37m[39;49;00m$
   506	[37m  [39;49;00m{[37m[39;49;00m$
   507	[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mwaitingBeautifierStack,[37m  [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<ASBeautifier*>[37m [39;49;00m);[37m[39;49;00m$
   508	[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mactiveBeautifierStack,[37m  [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<ASBeautifier*>[37m [39;49;00m);[37m[39;49;00m$
   509	[37m[39;49;00m$
   510	[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mwaitingBeautifierStackLengthStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   511	[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mactiveBeautifierStackLengthStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   512	[37m[39;49;00m$
   513	[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mheaderStack,[37m  [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m);[37m[39;49;00m$
   514	[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mtempStacks,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>*[37m [39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   515	[37m    [39;49;00mtempStacks->push_back([34mnew[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>);[37m[39;49;00m$
   516	[37m[39;49;00m$
   517	[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mblockParenDepthStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   518	[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mblockStatementStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   519	[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mparenStatementStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   520	[37m[39;49;00m$
   521	[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mbracketBlockStateStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   522	[37m    [39;49;00mbracketBlockStateStack->push_back([36mtrue[39;49;00m);[37m[39;49;00m$
   523	[37m[39;49;00m$
   524	[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00minStatementIndentStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   525	[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00minStatementIndentStackSizeStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   526	[37m    [39;49;00minStatementIndentStackSizeStack->push_back([34m0[39;49;00m);[37m[39;49;00m$
   527	[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mparenIndentStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
   528	[37m[39;49;00m$
   529	[37m    [39;49;00mimmediatelyPreviousAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   530	[37m    [39;49;00mpreviousLastLineHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   531	[37m[39;49;00m$
   532	[37m    [39;49;00misInQuote[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   533	[37m    [39;49;00misInComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   534	[37m    [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   535	[37m    [39;49;00misInCase[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   536	[37m    [39;49;00misInQuestion[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   537	[37m    [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   538	[37m    [39;49;00misInClassHeaderTab[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   539	[37m    [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   540	[37m    [39;49;00misInOperator[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   541	[37m    [39;49;00misInTemplate[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   542	[37m    [39;49;00misInConst[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   543	[37m    [39;49;00misInConditional[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   544	[37m    [39;49;00mtemplateDepth[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   545	[37m    [39;49;00mparenDepth=[34m0[39;49;00m;[37m[39;49;00m$
   546	[37m    [39;49;00mblockTabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   547	[37m    [39;49;00mleadingWhiteSpaces[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   548	[37m    [39;49;00mprevNonSpaceCh[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
   549	[37m    [39;49;00mcurrentNonSpaceCh[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
   550	[37m    [39;49;00mprevNonLegalCh[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
   551	[37m    [39;49;00mcurrentNonLegalCh[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
   552	[37m    [39;49;00mprevFinalLineSpaceTabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   553	[37m    [39;49;00mprevFinalLineTabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   554	[37m    [39;49;00mprobationHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   555	[37m    [39;49;00mbackslashEndsPrevLine[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   556	[37m    [39;49;00misInDefine[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   557	[37m    [39;49;00misInDefineDefinition[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   558	[37m    [39;49;00mdefineTabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   559	[37m  [39;49;00m}[37m[39;49;00m$
   560	[37m[39;49;00m$
   561	[37m  [39;49;00m[37m/**[39;49;00m$
   562	[37m   * set indentation style to ANSI C/C++.  [39;49;00m$
   563	[37m   */[39;49;00m[37m[39;49;00m$
   564	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setCStyle()[37m[39;49;00m$
   565	[37m  [39;49;00m{[37m[39;49;00m$
   566	[37m    [39;49;00misCStyle[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
   567	[37m  [39;49;00m}[37m[39;49;00m$
   568	[37m[39;49;00m$
   569	[37m  [39;49;00m[37m/**[39;49;00m$
   570	[37m   * set indentation style to Java / K&R.  [39;49;00m$
   571	[37m   */[39;49;00m[37m[39;49;00m$
   572	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setJavaStyle()[37m[39;49;00m$
   573	[37m  [39;49;00m{[37m[39;49;00m$
   574	[37m    [39;49;00misCStyle[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   575	[37m  [39;49;00m}[37m[39;49;00m$
   576	[37m[39;49;00m$
   577	[37m  [39;49;00m[37m/**[39;49;00m$
   578	[37m   * indent using one tab per indentation[39;49;00m$
   579	[37m   */[39;49;00m[37m[39;49;00m$
   580	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setTabIndentation([36mint[39;49;00m[37m [39;49;00mlength,[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mforceTabs)[37m[39;49;00m$
   581	[37m  [39;49;00m{[37m[39;49;00m$
   582	[37m    [39;49;00mindentString[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m\t[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
   583	[37m    [39;49;00mindentLength[37m [39;49;00m=[37m [39;49;00mlength;[37m[39;49;00m$
   584	[37m    [39;49;00mshouldForceTabIndentation[37m [39;49;00m=[37m [39;49;00mforceTabs;[37m[39;49;00m$
   585	[37m[39;49;00m$
   586	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isMinimalConditinalIndentSet)[37m[39;49;00m$
   587	[37m      [39;49;00mminConditionalIndent[37m [39;49;00m=[37m [39;49;00mindentLength[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m$
   588	[37m  [39;49;00m}[37m[39;49;00m$
   589	[37m[39;49;00m$
   590	[37m  [39;49;00m[37m/**[39;49;00m$
   591	[37m   [39;49;00m$
   592	[37m   * indent using a number of spaces per indentation.[39;49;00m$
   593	[37m   *[39;49;00m$
   594	[37m   * @param   length     number of spaces per indent.[39;49;00m$
   595	[37m   */[39;49;00m[37m[39;49;00m$
   596	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setSpaceIndentation([36mint[39;49;00m[37m [39;49;00mlength)[37m[39;49;00m$
   597	[37m  [39;49;00m{[37m[39;49;00m$
   598	[37m    [39;49;00mindentString=string(length,[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
   599	[37m    [39;49;00mindentLength[37m [39;49;00m=[37m [39;49;00mlength;[37m[39;49;00m$
   600	[37m[39;49;00m$
   601	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isMinimalConditinalIndentSet)[37m[39;49;00m$
   602	[37m      [39;49;00mminConditionalIndent[37m [39;49;00m=[37m [39;49;00mindentLength[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m$
   603	[37m  [39;49;00m}[37m[39;49;00m$
   604	[37m[39;49;00m$
   605	[37m  [39;49;00m[37m/**[39;49;00m$
   606	[37m   * set the maximum indentation between two lines in a multi-line statement.[39;49;00m$
   607	[37m   *[39;49;00m$
   608	[37m   * @param   max     maximum indentation length.[39;49;00m$
   609	[37m   */[39;49;00m[37m[39;49;00m$
   610	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setMaxInStatementIndentLength([36mint[39;49;00m[37m [39;49;00mmax)[37m[39;49;00m$
   611	[37m  [39;49;00m{[37m[39;49;00m$
   612	[37m    [39;49;00mmaxInStatementIndent[37m [39;49;00m=[37m [39;49;00mmax;[37m[39;49;00m$
   613	[37m  [39;49;00m}[37m[39;49;00m$
   614	[37m[39;49;00m$
   615	[37m  [39;49;00m[37m/**[39;49;00m$
   616	[37m   * set the minimum indentation between two lines in a multi-line condition.[39;49;00m$
   617	[37m   *[39;49;00m$
   618	[37m   * @param   min     minimal indentation length.[39;49;00m$
   619	[37m   */[39;49;00m[37m[39;49;00m$
   620	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setMinConditionalIndentLength([36mint[39;49;00m[37m [39;49;00mmin)[37m[39;49;00m$
   621	[37m  [39;49;00m{[37m[39;49;00m$
   622	[37m    [39;49;00mminConditionalIndent[37m [39;49;00m=[37m [39;49;00mmin;[37m[39;49;00m$
   623	[37m    [39;49;00misMinimalConditinalIndentSet[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
   624	[37m  [39;49;00m}[37m[39;49;00m$
   625	[37m[39;49;00m$
   626	[37m  [39;49;00m[37m/**[39;49;00m$
   627	[37m   * set the state of the bracket indentation option. If true, brackets will [39;49;00m$
   628	[37m   * be indented one additional indent.[39;49;00m$
   629	[37m   *[39;49;00m$
   630	[37m   * @param   state             state of option.[39;49;00m$
   631	[37m   */[39;49;00m[37m[39;49;00m$
   632	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setBracketIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   633	[37m  [39;49;00m{[37m[39;49;00m$
   634	[37m    [39;49;00mbracketIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   635	[37m  [39;49;00m}[37m[39;49;00m$
   636	[37m[39;49;00m$
   637	[37m  [39;49;00m[37m/**[39;49;00m$
   638	[37m   * set the state of the block indentation option. If true, entire blocks [39;49;00m$
   639	[37m   * will be indented one additional indent, similar to the GNU indent style.[39;49;00m$
   640	[37m   *[39;49;00m$
   641	[37m   * @param   state             state of option.[39;49;00m$
   642	[37m   */[39;49;00m[37m[39;49;00m$
   643	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setBlockIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   644	[37m  [39;49;00m{[37m[39;49;00m$
   645	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(state)[37m[39;49;00m$
   646	[37m      [39;49;00msetBracketIndent([36mfalse[39;49;00m);[37m [39;49;00m[37m// so that we don't have both bracket and block indent[39;49;00m$
   647	[37m    [39;49;00mblockIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   648	[37m  [39;49;00m}[37m[39;49;00m$
   649	[37m[39;49;00m$
   650	[37m  [39;49;00m[37m/**[39;49;00m$
   651	[37m   * set the state of the class indentation option. If true, C++ class[39;49;00m$
   652	[37m   * definitions will be indented one additional indent.[39;49;00m$
   653	[37m   *[39;49;00m$
   654	[37m   * @param   state             state of option.[39;49;00m$
   655	[37m   */[39;49;00m[37m[39;49;00m$
   656	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setClassIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   657	[37m  [39;49;00m{[37m[39;49;00m$
   658	[37m    [39;49;00mclassIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   659	[37m  [39;49;00m}[37m[39;49;00m$
   660	[37m[39;49;00m$
   661	[37m  [39;49;00m[37m/**[39;49;00m$
   662	[37m   * set the state of the switch indentation option. If true, blocks of 'switch' [39;49;00m$
   663	[37m   * statements will be indented one additional indent.[39;49;00m$
   664	[37m   *[39;49;00m$
   665	[37m   * @param   state             state of option.[39;49;00m$
   666	[37m   */[39;49;00m[37m[39;49;00m$
   667	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setSwitchIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   668	[37m  [39;49;00m{[37m[39;49;00m$
   669	[37m    [39;49;00mswitchIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   670	[37m  [39;49;00m}[37m[39;49;00m$
   671	[37m[39;49;00m$
   672	[37m  [39;49;00m[37m/**[39;49;00m$
   673	[37m   * set the state of the case indentation option. If true, lines of 'case' [39;49;00m$
   674	[37m   * statements will be indented one additional indent.[39;49;00m$
   675	[37m   *[39;49;00m$
   676	[37m   * @param   state             state of option.[39;49;00m$
   677	[37m   */[39;49;00m[37m[39;49;00m$
   678	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setCaseIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   679	[37m  [39;49;00m{[37m[39;49;00m$
   680	[37m    [39;49;00mcaseIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   681	[37m  [39;49;00m}[37m[39;49;00m$
   682	[37m  [39;49;00m[37m/**[39;49;00m$
   683	[37m   * set the state of the namespace indentation option. [39;49;00m$
   684	[37m   * If true, blocks of 'namespace' statements will be indented one [39;49;00m$
   685	[37m   * additional indent. Otherwise, NO indentation will be added.[39;49;00m$
   686	[37m   *[39;49;00m$
   687	[37m   * @param   state             state of option.[39;49;00m$
   688	[37m   */[39;49;00m[37m[39;49;00m$
   689	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setNamespaceIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   690	[37m  [39;49;00m{[37m[39;49;00m$
   691	[37m    [39;49;00mnamespaceIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   692	[37m  [39;49;00m}[37m[39;49;00m$
   693	[37m[39;49;00m$
   694	[37m  [39;49;00m[37m/**[39;49;00m$
   695	[37m   * set the state of the label indentation option. [39;49;00m$
   696	[37m   * If true, labels will be indented one indent LESS than the[39;49;00m$
   697	[37m   * current indentation level.[39;49;00m$
   698	[37m   * If false, labels will be flushed to the left with NO[39;49;00m$
   699	[37m   * indent at all.[39;49;00m$
   700	[37m   *[39;49;00m$
   701	[37m   * @param   state             state of option.[39;49;00m$
   702	[37m   */[39;49;00m[37m[39;49;00m$
   703	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setLabelIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   704	[37m  [39;49;00m{[37m[39;49;00m$
   705	[37m    [39;49;00mlabelIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   706	[37m  [39;49;00m}[37m[39;49;00m$
   707	[37m[39;49;00m$
   708	[37m  [39;49;00m[37m/**[39;49;00m$
   709	[37m   * set the state of the preprocessor indentation option. [39;49;00m$
   710	[37m   * If true, multiline #define statements will be indented.[39;49;00m$
   711	[37m   *[39;49;00m$
   712	[37m   * @param   state             state of option.[39;49;00m$
   713	[37m   */[39;49;00m[37m[39;49;00m$
   714	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setPreprocessorIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   715	[37m  [39;49;00m{[37m[39;49;00m$
   716	[37m    [39;49;00mpreprocessorIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   717	[37m  [39;49;00m}[37m[39;49;00m$
   718	[37m[39;49;00m$
   719	[37m  [39;49;00m[37m/**[39;49;00m$
   720	[37m   * set the state of the empty line fill option. [39;49;00m$
   721	[37m   * If true, empty lines will be filled with the whitespace.[39;49;00m$
   722	[37m   * of their previous lines.[39;49;00m$
   723	[37m   * If false, these lines will remain empty.[39;49;00m$
   724	[37m   *[39;49;00m$
   725	[37m   * @param   state             state of option.[39;49;00m$
   726	[37m   */[39;49;00m[37m[39;49;00m$
   727	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setEmptyLineFill([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
   728	[37m  [39;49;00m{[37m[39;49;00m$
   729	[37m    [39;49;00memptyLineFill[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
   730	[37m  [39;49;00m}[37m[39;49;00m$
   731	[37m[39;49;00m$
   732	[37m  [39;49;00m[37m/**[39;49;00m$
   733	[37m   * check if there are any indented lines ready to be read by nextLine()[39;49;00m$
   734	[37m   *[39;49;00m$
   735	[37m   * @return    are there any indented lines ready?[39;49;00m$
   736	[37m   */[39;49;00m[37m[39;49;00m$
   737	[37m  [39;49;00m[36mbool[39;49;00m[37m [39;49;00mASBeautifier::hasMoreLines()[37m [39;49;00m[34mconst[39;49;00m[37m[39;49;00m$
   738	[37m    [39;49;00m{[37m[39;49;00m$
   739	[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00msourceIterator->hasMoreLines();[37m[39;49;00m$
   740	[37m    [39;49;00m}[37m[39;49;00m$
   741	[37m[39;49;00m$
   742	[37m  [39;49;00m[37m/**[39;49;00m$
   743	[37m   * get the next indented line.[39;49;00m$
   744	[37m   *[39;49;00m$
   745	[37m   * @return    indented line.[39;49;00m$
   746	[37m   */[39;49;00m[37m[39;49;00m$
   747	[37m  [39;49;00mstring[37m [39;49;00mASBeautifier::nextLine()[37m[39;49;00m$
   748	[37m  [39;49;00m{[37m[39;49;00m$
   749	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mbeautify(sourceIterator->nextLine());[37m[39;49;00m$
   750	[37m  [39;49;00m}[37m[39;49;00m$
   751	[37m[39;49;00m$
   752	[37m  [39;49;00m[37m/**[39;49;00m$
   753	[37m   * beautify a line of source code.[39;49;00m$
   754	[37m   * every line of source code in a source code file should be sent[39;49;00m$
   755	[37m   * one after the other to the beautify method.[39;49;00m$
   756	[37m   *[39;49;00m$
   757	[37m   * @return      the indented line.[39;49;00m$
   758	[37m   * @param originalLine       the original unindented line.[39;49;00m$
   759	[37m   */[39;49;00m[37m[39;49;00m$
   760	[37m  [39;49;00mstring[37m [39;49;00mASBeautifier::beautify([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&originalLine)[37m[39;49;00m$
   761	[37m  [39;49;00m{[37m[39;49;00m$
   762	[37m    [39;49;00mstring[37m [39;49;00mline;[37m[39;49;00m$
   763	[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInLineComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   764	[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00mlineStartsInComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   765	[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInClass[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   766	[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInSwitch[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   767	[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00misImmediatelyAfterConst[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   768	[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00misSpecialChar[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   769	[37m[39;49;00m$
   770	[37m    [39;49;00m[36mchar[39;49;00m[37m [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
   771	[37m    [39;49;00m[36mchar[39;49;00m[37m [39;49;00mprevCh;[37m[39;49;00m$
   772	[37m    [39;49;00mstring[37m [39;49;00moutBuffer;[37m [39;49;00m[37m// the newly idented line is bufferd here[39;49;00m$
   773	[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mtabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   774	[37m    [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*lastLineHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   775	[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00mclosingBracketReached[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   776	[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mspaceTabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   777	[37m    [39;49;00m[36mchar[39;49;00m[37m [39;49;00mtempCh;[37m[39;49;00m$
   778	[37m    [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mheaderStackSize[37m [39;49;00m=[37m [39;49;00mheaderStack->size();[37m[39;49;00m$
   779	[37m    [39;49;00m[37m//bool isLineInStatement = isInStatement;[39;49;00m$
   780	[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00mshouldIndentBrackettedLine[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
   781	[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mlineOpeningBlocksNum[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   782	[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mlineClosingBlocksNum[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   783	[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00mpreviousLineProbation[37m [39;49;00m=[37m [39;49;00m(probationHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
   784	[37m    [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi;[37m[39;49;00m$
   785	[37m[39;49;00m$
   786	[37m    [39;49;00mcurrentHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
   787	[37m[39;49;00m$
   788	[37m    [39;49;00mlineStartsInComment[37m [39;49;00m=[37m [39;49;00misInComment;[37m[39;49;00m$
   789	[37m[39;49;00m$
   790	[37m    [39;49;00m[37m// handle and remove white spaces around the line:[39;49;00m$
   791	[37m    [39;49;00m[37m// If not in comment, first find out size of white space before line,[39;49;00m$
   792	[37m    [39;49;00m[37m// so that possible comments starting in the line continue in[39;49;00m$
   793	[37m    [39;49;00m[37m// relation to the preliminary white-space.[39;49;00m$
   794	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInComment)[37m[39;49;00m$
   795	[37m      [39;49;00m{[37m[39;49;00m$
   796	[37m        [39;49;00mleadingWhiteSpaces[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
   797	[37m        [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(leadingWhiteSpaces<originalLine.length()[37m [39;49;00m&&[37m [39;49;00moriginalLine[leadingWhiteSpaces][37m [39;49;00m<=[37m [39;49;00m[34m0x20[39;49;00m)[37m[39;49;00m$
   798	[37m          [39;49;00mleadingWhiteSpaces++;[37m[39;49;00m$
   799	[37m[39;49;00m$
   800	[37m        [39;49;00mline[37m [39;49;00m=[37m [39;49;00mtrim(originalLine);[37m[39;49;00m$
   801	[37m      [39;49;00m}[37m[39;49;00m$
   802	[37m    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
   803	[37m      [39;49;00m{[37m[39;49;00m$
   804	[37m        [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mtrimSize;[37m[39;49;00m$
   805	[37m        [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(trimSize=[34m0[39;49;00m;[37m[39;49;00m$
   806	[37m             [39;49;00mtrimSize[37m [39;49;00m<[37m [39;49;00moriginalLine.length()[37m [39;49;00m&&[37m [39;49;00mtrimSize<leadingWhiteSpaces[37m [39;49;00m&&[37m [39;49;00moriginalLine[trimSize][37m [39;49;00m<=[37m [39;49;00m[34m0x20[39;49;00m[37m [39;49;00m;[37m[39;49;00m$
   807	[37m             [39;49;00mtrimSize++)[37m[39;49;00m$
   808	[37m          [39;49;00m;[37m[39;49;00m$
   809	[37m        [39;49;00mline[37m [39;49;00m=[37m [39;49;00moriginalLine.substr(trimSize);[37m[39;49;00m$
   810	[37m      [39;49;00m}[37m[39;49;00m$
   811	[37m[39;49;00m$
   812	[37m[39;49;00m$
   813	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.length()[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   814	[37m      [39;49;00m{[37m[39;49;00m$
   815	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(emptyLineFill)[37m[39;49;00m$
   816	[37m          [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mpreLineWS(prevFinalLineSpaceTabCount,[37m [39;49;00mprevFinalLineTabCount);[37m[39;49;00m$
   817	[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
   818	[37m          [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mline;[37m[39;49;00m$
   819	[37m      [39;49;00m}[37m[39;49;00m$
   820	[37m[39;49;00m$
   821	[37m    [39;49;00m[37m// handle preprocessor commands[39;49;00m$
   822	[37m[39;49;00m$
   823	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00m!isInComment[37m [39;49;00m&&[37m [39;49;00m(line[[34m0[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m#[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mbackslashEndsPrevLine))[37m[39;49;00m$
   824	[37m      [39;49;00m{[37m[39;49;00m$
   825	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line[[34m0[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m#[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
   826	[37m          [39;49;00m{[37m[39;49;00m$
   827	[37m            [39;49;00mstring[37m [39;49;00mpreproc[37m [39;49;00m=[37m [39;49;00mtrim(string(line.c_str()[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m));[37m[39;49;00m$
   828	[37m[39;49;00m$
   829	[37m[39;49;00m$
   830	[37m            [39;49;00m[37m// When finding a multi-lined #define statement, the original beautifier[39;49;00m$
   831	[37m            [39;49;00m[37m// 1. sets its isInDefineDefinition flag[39;49;00m$
   832	[37m            [39;49;00m[37m// 2. clones a new beautifier that will be used for the actual indentation[39;49;00m$
   833	[37m            [39;49;00m[37m//    of the #define. This clone is put into the activeBeautifierStack in order[39;49;00m$
   834	[37m            [39;49;00m[37m//    to be called for the actual indentation.[39;49;00m$
   835	[37m            [39;49;00m[37m// The original beautifier will have isInDefineDefinition = true, isInDefine = false[39;49;00m$
   836	[37m            [39;49;00m[37m// The cloned beautifier will have   isInDefineDefinition = true, isInDefine = true[39;49;00m$
   837	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preprocessorIndent[37m [39;49;00m&&[37m [39;49;00mpreproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m6[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33mdefine[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m  [39;49;00mline[line.length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
   838	[37m              [39;49;00m{[37m[39;49;00m$
   839	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInDefineDefinition)[37m[39;49;00m$
   840	[37m                  [39;49;00m{[37m[39;49;00m$
   841	[37m                    [39;49;00mASBeautifier[37m [39;49;00m*defineBeautifier;[37m[39;49;00m$
   842	[37m[39;49;00m$
   843	[37m                    [39;49;00m[37m// this is the original beautifier[39;49;00m$
   844	[37m                    [39;49;00misInDefineDefinition[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
   845	[37m[39;49;00m$
   846	[37m                    [39;49;00m[37m// push a new beautifier into the active stack[39;49;00m$
   847	[37m                    [39;49;00m[37m// this breautifier will be used for the indentation of this define[39;49;00m$
   848	[37m                    [39;49;00mdefineBeautifier[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mASBeautifier(*[34mthis[39;49;00m);[37m[39;49;00m$
   849	[37m                    [39;49;00m[37m//defineBeautifier->init();[39;49;00m$
   850	[37m                    [39;49;00m[37m//defineBeautifier->isInDefineDefinition = true;[39;49;00m$
   851	[37m                    [39;49;00m[37m//defineBeautifier->beautify("");[39;49;00m$
   852	[37m                    [39;49;00mactiveBeautifierStack->push_back(defineBeautifier);[37m[39;49;00m$
   853	[37m                  [39;49;00m}[37m[39;49;00m$
   854	[37m                [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
   855	[37m                  [39;49;00m{[37m[39;49;00m$
   856	[37m                    [39;49;00m[37m// the is the cloned beautifier that is in charge of indenting the #define.[39;49;00m$
   857	[37m                    [39;49;00misInDefine[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
   858	[37m                  [39;49;00m}[37m[39;49;00m$
   859	[37m              [39;49;00m}[37m[39;49;00m$
   860	[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33mif[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   861	[37m              [39;49;00m{[37m[39;49;00m$
   862	[37m                [39;49;00m[37m// push a new beautifier into the stack[39;49;00m$
   863	[37m                [39;49;00mwaitingBeautifierStackLengthStack->push_back(waitingBeautifierStack->size());[37m[39;49;00m$
   864	[37m                [39;49;00mactiveBeautifierStackLengthStack->push_back(activeBeautifierStack->size());[37m[39;49;00m$
   865	[37m                [39;49;00mwaitingBeautifierStack->push_back([34mnew[39;49;00m[37m [39;49;00mASBeautifier(*[34mthis[39;49;00m));[37m[39;49;00m$
   866	[37m              [39;49;00m}[37m[39;49;00m$
   867	[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m4[39;49;00m[37m/*2*/[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33melse[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   868	[37m              [39;49;00m{[37m[39;49;00m$
   869	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!waitingBeautifierStack->empty())[37m[39;49;00m$
   870	[37m                  [39;49;00m{[37m[39;49;00m$
   871	[37m                    [39;49;00m[37m// MOVE current waiting beautifier to active stack.[39;49;00m$
   872	[37m                    [39;49;00mactiveBeautifierStack->push_back(waitingBeautifierStack->back());[37m[39;49;00m$
   873	[37m                    [39;49;00mwaitingBeautifierStack->pop_back();[37m[39;49;00m$
   874	[37m                  [39;49;00m}[37m[39;49;00m$
   875	[37m              [39;49;00m}[37m[39;49;00m$
   876	[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m4[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33melif[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   877	[37m              [39;49;00m{[37m[39;49;00m$
   878	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!waitingBeautifierStack->empty())[37m[39;49;00m$
   879	[37m                  [39;49;00m{[37m[39;49;00m$
   880	[37m                    [39;49;00m[37m// append a COPY current waiting beautifier to active stack, WITHOUT deleting the original.[39;49;00m$
   881	[37m                    [39;49;00mactiveBeautifierStack->push_back([37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mASBeautifier([37m [39;49;00m*(waitingBeautifierStack->back())[37m [39;49;00m)[37m [39;49;00m);[37m[39;49;00m$
   882	[37m                  [39;49;00m}[37m[39;49;00m$
   883	[37m              [39;49;00m}[37m[39;49;00m$
   884	[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m5[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33mendif[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   885	[37m              [39;49;00m{[37m[39;49;00m$
   886	[37m                [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mstackLength;[37m[39;49;00m$
   887	[37m                [39;49;00mASBeautifier[37m [39;49;00m*beautifier;[37m[39;49;00m$
   888	[37m[39;49;00m$
   889	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!waitingBeautifierStackLengthStack->empty())[37m[39;49;00m$
   890	[37m                  [39;49;00m{[37m[39;49;00m$
   891	[37m                    [39;49;00mstackLength[37m [39;49;00m=[37m [39;49;00mwaitingBeautifierStackLengthStack->back();[37m[39;49;00m$
   892	[37m                    [39;49;00mwaitingBeautifierStackLengthStack->pop_back();[37m[39;49;00m$
   893	[37m                    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(waitingBeautifierStack->size()[37m [39;49;00m>[37m [39;49;00mstackLength)[37m[39;49;00m$
   894	[37m                      [39;49;00m{[37m[39;49;00m$
   895	[37m                        [39;49;00mbeautifier[37m [39;49;00m=[37m [39;49;00mwaitingBeautifierStack->back();[37m[39;49;00m$
   896	[37m                        [39;49;00mwaitingBeautifierStack->pop_back();[37m[39;49;00m$
   897	[37m                        [39;49;00m[34mdelete[39;49;00m[37m [39;49;00mbeautifier;[37m[39;49;00m$
   898	[37m                      [39;49;00m}[37m[39;49;00m$
   899	[37m                  [39;49;00m}[37m[39;49;00m$
   900	[37m[39;49;00m$
   901	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!activeBeautifierStackLengthStack->empty())[37m[39;49;00m$
   902	[37m                  [39;49;00m{[37m[39;49;00m$
   903	[37m                    [39;49;00mstackLength[37m [39;49;00m=[37m [39;49;00mactiveBeautifierStackLengthStack->back();[37m[39;49;00m$
   904	[37m                    [39;49;00mactiveBeautifierStackLengthStack->pop_back();[37m[39;49;00m$
   905	[37m                    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(activeBeautifierStack->size()[37m [39;49;00m>[37m [39;49;00mstackLength)[37m[39;49;00m$
   906	[37m                      [39;49;00m{[37m[39;49;00m$
   907	[37m                        [39;49;00mbeautifier[37m [39;49;00m=[37m [39;49;00mactiveBeautifierStack->back();[37m[39;49;00m$
   908	[37m                        [39;49;00mactiveBeautifierStack->pop_back();[37m[39;49;00m$
   909	[37m                        [39;49;00m[34mdelete[39;49;00m[37m [39;49;00mbeautifier;[37m[39;49;00m$
   910	[37m                      [39;49;00m}[37m[39;49;00m$
   911	[37m                  [39;49;00m}[37m[39;49;00m$
   912	[37m[39;49;00m$
   913	[37m[39;49;00m$
   914	[37m              [39;49;00m}[37m[39;49;00m$
   915	[37m          [39;49;00m}[37m[39;49;00m$
   916	[37m[39;49;00m$
   917	[37m        [39;49;00m[37m// check if the last char is a backslash[39;49;00m$
   918	[37m        [39;49;00m[34mif[39;49;00m(line.length()[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
   919	[37m          [39;49;00mbackslashEndsPrevLine[37m [39;49;00m=[37m [39;49;00m(line[line.length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
   920	[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
   921	[37m          [39;49;00mbackslashEndsPrevLine[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   922	[37m[39;49;00m$
   923	[37m        [39;49;00m[37m// check if this line ends a multi-line #define[39;49;00m$
   924	[37m        [39;49;00m[37m// if so, use the #define's cloned beautifier for the line's indentation[39;49;00m$
   925	[37m        [39;49;00m[37m// and then remove it from the active beautifier stack and delete it.[39;49;00m$
   926	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!backslashEndsPrevLine[37m [39;49;00m&&[37m [39;49;00misInDefineDefinition[37m [39;49;00m&&[37m [39;49;00m!isInDefine)[37m[39;49;00m$
   927	[37m          [39;49;00m{[37m[39;49;00m$
   928	[37m            [39;49;00mstring[37m [39;49;00mbeautifiedLine;[37m[39;49;00m$
   929	[37m            [39;49;00mASBeautifier[37m [39;49;00m*defineBeautifier;[37m[39;49;00m$
   930	[37m[39;49;00m$
   931	[37m            [39;49;00misInDefineDefinition[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   932	[37m            [39;49;00mdefineBeautifier[37m [39;49;00m=[37m [39;49;00mactiveBeautifierStack->back();[37m[39;49;00m$
   933	[37m            [39;49;00mactiveBeautifierStack->pop_back();[37m[39;49;00m$
   934	[37m[39;49;00m$
   935	[37m            [39;49;00mbeautifiedLine[37m [39;49;00m=[37m [39;49;00mdefineBeautifier->beautify(line);[37m[39;49;00m$
   936	[37m            [39;49;00m[34mdelete[39;49;00m[37m [39;49;00mdefineBeautifier;[37m[39;49;00m$
   937	[37m            [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mbeautifiedLine;[37m[39;49;00m$
   938	[37m          [39;49;00m}[37m[39;49;00m$
   939	[37m[39;49;00m$
   940	[37m        [39;49;00m[37m// unless this is a multi-line #define, return this precompiler line as is.[39;49;00m$
   941	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInDefine[37m [39;49;00m&&[37m [39;49;00m!isInDefineDefinition)[37m[39;49;00m$
   942	[37m          [39;49;00m[34mreturn[39;49;00m[37m [39;49;00moriginalLine;[37m[39;49;00m$
   943	[37m      [39;49;00m}[37m[39;49;00m$
   944	[37m[39;49;00m$
   945	[37m    [39;49;00m[37m// if there exists any worker beautifier in the activeBeautifierStack,[39;49;00m$
   946	[37m    [39;49;00m[37m// then use it instead of me to indent the current line.[39;49;00m$
   947	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInDefine[37m [39;49;00m&&[37m [39;49;00mactiveBeautifierStack[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00m!activeBeautifierStack->empty())[37m[39;49;00m$
   948	[37m      [39;49;00m{[37m[39;49;00m$
   949	[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mactiveBeautifierStack->back()->beautify(line);[37m[39;49;00m$
   950	[37m      [39;49;00m}[37m[39;49;00m$
   951	[37m[39;49;00m$
   952	[37m    [39;49;00m[37m// calculate preliminary indentation based on data from past lines[39;49;00m$
   953	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStack->empty())[37m[39;49;00m$
   954	[37m      [39;49;00mspaceTabCount[37m [39;49;00m=[37m [39;49;00minStatementIndentStack->back();[37m[39;49;00m$
   955	[37m[39;49;00m$
   956	[37m[39;49;00m$
   957	[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(i=[34m0[39;49;00m;[37m [39;49;00mi<headerStackSize;[37m [39;49;00mi++)[37m[39;49;00m$
   958	[37m      [39;49;00m{[37m[39;49;00m$
   959	[37m        [39;49;00misInClass[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
   960	[37m[39;49;00m$
   961	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(blockIndent[37m [39;49;00m||[37m [39;49;00m(!(i>[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(*headerStack)[i[34m-1[39;49;00m][37m [39;49;00m!=[37m [39;49;00m&AS_OPEN_BRACKET[37m[39;49;00m$
   962	[37m                              [39;49;00m&&[37m [39;49;00m(*headerStack)[i][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET)))[37m[39;49;00m$
   963	[37m          [39;49;00m++tabCount;[37m[39;49;00m$
   964	[37m[39;49;00m$
   965	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00m!namespaceIndent[37m [39;49;00m&&[37m [39;49;00mi[37m [39;49;00m>=[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
   966	[37m            [39;49;00m&&[37m [39;49;00m(*headerStack)[i[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_NAMESPACE[37m[39;49;00m$
   967	[37m            [39;49;00m&&[37m [39;49;00m(*headerStack)[i][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET)[37m[39;49;00m$
   968	[37m          [39;49;00m--tabCount;[37m[39;49;00m$
   969	[37m[39;49;00m$
   970	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00mi[37m [39;49;00m>=[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
   971	[37m            [39;49;00m&&[37m [39;49;00m(*headerStack)[i[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_CLASS[37m[39;49;00m$
   972	[37m            [39;49;00m&&[37m [39;49;00m(*headerStack)[i][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET[37m [39;49;00m)[37m[39;49;00m$
   973	[37m          [39;49;00m{[37m[39;49;00m$
   974	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(classIndent)[37m[39;49;00m$
   975	[37m              [39;49;00m++tabCount;[37m[39;49;00m$
   976	[37m            [39;49;00misInClass[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
   977	[37m          [39;49;00m}[37m[39;49;00m$
   978	[37m[39;49;00m$
   979	[37m        [39;49;00m[37m// is the switchIndent option is on, indent switch statements an additional indent.[39;49;00m$
   980	[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(switchIndent[37m [39;49;00m&&[37m [39;49;00mi[37m [39;49;00m>[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m&&[37m[39;49;00m$
   981	[37m                 [39;49;00m(*headerStack)[i[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_SWITCH[37m [39;49;00m&&[37m[39;49;00m$
   982	[37m                 [39;49;00m(*headerStack)[i][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET[37m[39;49;00m$
   983	[37m                [39;49;00m)[37m[39;49;00m$
   984	[37m          [39;49;00m{[37m[39;49;00m$
   985	[37m            [39;49;00m++tabCount;[37m[39;49;00m$
   986	[37m            [39;49;00misInSwitch[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
   987	[37m          [39;49;00m}[37m[39;49;00m$
   988	[37m[39;49;00m$
   989	[37m      [39;49;00m}[37m[39;49;00m$
   990	[37m[39;49;00m$
   991	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!lineStartsInComment[37m[39;49;00m$
   992	[37m        [39;49;00m&&[37m [39;49;00misCStyle[37m[39;49;00m$
   993	[37m        [39;49;00m&&[37m [39;49;00misInClass[37m[39;49;00m$
   994	[37m        [39;49;00m&&[37m [39;49;00mclassIndent[37m[39;49;00m$
   995	[37m        [39;49;00m&&[37m [39;49;00mheaderStackSize[37m [39;49;00m>=[37m [39;49;00m[34m2[39;49;00m[37m[39;49;00m$
   996	[37m        [39;49;00m&&(*headerStack)[headerStackSize[34m-2[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_CLASS[37m[39;49;00m$
   997	[37m        [39;49;00m&&[37m [39;49;00m(*headerStack)[headerStackSize[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET[37m[39;49;00m$
   998	[37m        [39;49;00m&&[37m [39;49;00mline[[34m0[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
   999	[37m      [39;49;00m--tabCount;[37m[39;49;00m$
  1000	[37m[39;49;00m$
  1001	[37m    [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!lineStartsInComment[37m[39;49;00m$
  1002	[37m             [39;49;00m&&[37m [39;49;00misInSwitch[37m[39;49;00m$
  1003	[37m             [39;49;00m&&[37m [39;49;00mswitchIndent[37m[39;49;00m$
  1004	[37m             [39;49;00m&&[37m [39;49;00mheaderStackSize[37m [39;49;00m>=[37m [39;49;00m[34m2[39;49;00m[37m[39;49;00m$
  1005	[37m             [39;49;00m&&[37m [39;49;00m(*headerStack)[headerStackSize[34m-2[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_SWITCH[37m[39;49;00m$
  1006	[37m             [39;49;00m&&[37m [39;49;00m(*headerStack)[headerStackSize[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET[37m[39;49;00m$
  1007	[37m             [39;49;00m&&[37m [39;49;00mline[[34m0[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1008	[37m      [39;49;00m--tabCount;[37m[39;49;00m$
  1009	[37m[39;49;00m$
  1010	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInClassHeader)[37m[39;49;00m$
  1011	[37m      [39;49;00m{[37m[39;49;00m$
  1012	[37m        [39;49;00misInClassHeaderTab[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1013	[37m        [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m$
  1014	[37m      [39;49;00m}[37m[39;49;00m$
  1015	[37m[39;49;00m$
  1016	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInConditional)[37m[39;49;00m$
  1017	[37m      [39;49;00m{[37m[39;49;00m$
  1018	[37m        [39;49;00m--tabCount;[37m[39;49;00m$
  1019	[37m      [39;49;00m}[37m[39;49;00m$
  1020	[37m[39;49;00m$
  1021	[37m[39;49;00m$
  1022	[37m    [39;49;00m[37m// parse characters in the current line.[39;49;00m$
  1023	[37m[39;49;00m$
  1024	[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(i=[34m0[39;49;00m;[37m [39;49;00mi<line.length();[37m [39;49;00mi++)[37m[39;49;00m$
  1025	[37m      [39;49;00m{[37m[39;49;00m$
  1026	[37m        [39;49;00mtempCh[37m [39;49;00m=[37m [39;49;00mline[i];[37m[39;49;00m$
  1027	[37m[39;49;00m$
  1028	[37m        [39;49;00mprevCh[37m [39;49;00m=[37m [39;49;00mch;[37m[39;49;00m$
  1029	[37m        [39;49;00mch[37m [39;49;00m=[37m [39;49;00mtempCh;[37m[39;49;00m$
  1030	[37m[39;49;00m$
  1031	[37m        [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00mch);[37m[39;49;00m$
  1032	[37m[39;49;00m$
  1033	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isWhiteSpace(ch))[37m[39;49;00m$
  1034	[37m          [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1035	[37m[39;49;00m$
  1036	[37m[39;49;00m$
  1037	[37m        [39;49;00m[37m// handle special characters (i.e. backslash+character such as \n, \t, ...)[39;49;00m$
  1038	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isSpecialChar)[37m[39;49;00m$
  1039	[37m          [39;49;00m{[37m[39;49;00m$
  1040	[37m            [39;49;00misSpecialChar[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1041	[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1042	[37m          [39;49;00m}[37m[39;49;00m$
  1043	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00mline.COMPARE(i,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1044	[37m          [39;49;00m{[37m[39;49;00m$
  1045	[37m            [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
  1046	[37m            [39;49;00mi++;[37m[39;49;00m$
  1047	[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1048	[37m          [39;49;00m}[37m[39;49;00m$
  1049	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00mch==[33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1050	[37m          [39;49;00m{[37m[39;49;00m$
  1051	[37m            [39;49;00misSpecialChar[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1052	[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1053	[37m          [39;49;00m}[37m[39;49;00m$
  1054	[37m[39;49;00m$
  1055	[37m        [39;49;00m[37m// handle quotes (such as 'x' and "Hello Dolly")[39;49;00m$
  1056	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00m(ch==[33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch==[33m'[39;49;00m[33m\'[39;49;00m[33m'[39;49;00m))[37m[39;49;00m$
  1057	[37m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInQuote)[37m[39;49;00m$
  1058	[37m            [39;49;00m{[37m[39;49;00m$
  1059	[37m              [39;49;00mquoteChar[37m [39;49;00m=[37m [39;49;00mch;[37m[39;49;00m$
  1060	[37m              [39;49;00misInQuote[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1061	[37m            [39;49;00m}[37m[39;49;00m$
  1062	[37m          [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(quoteChar[37m [39;49;00m==[37m [39;49;00mch)[37m[39;49;00m$
  1063	[37m            [39;49;00m{[37m[39;49;00m$
  1064	[37m              [39;49;00misInQuote[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1065	[37m              [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1066	[37m              [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1067	[37m            [39;49;00m}[37m[39;49;00m$
  1068	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInQuote)[37m[39;49;00m$
  1069	[37m          [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1070	[37m[39;49;00m$
  1071	[37m        [39;49;00m[37m// handle comments[39;49;00m$
  1072	[37m[39;49;00m$
  1073	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m!(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00mline.COMPARE(i,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_OPEN_LINE_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
  1074	[37m          [39;49;00m{[37m[39;49;00m$
  1075	[37m            [39;49;00misInLineComment[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1076	[37m            [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
  1077	[37m            [39;49;00mi++;[37m[39;49;00m$
  1078	[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1079	[37m          [39;49;00m}[37m[39;49;00m$
  1080	[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m!(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00mline.COMPARE(i,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_OPEN_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
  1081	[37m          [39;49;00m{[37m[39;49;00m$
  1082	[37m            [39;49;00misInComment[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1083	[37m            [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
  1084	[37m            [39;49;00mi++;[37m[39;49;00m$
  1085	[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1086	[37m          [39;49;00m}[37m[39;49;00m$
  1087	[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00mline.COMPARE(i,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_CLOSE_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
  1088	[37m          [39;49;00m{[37m[39;49;00m$
  1089	[37m            [39;49;00misInComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1090	[37m            [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
  1091	[37m            [39;49;00mi++;[37m[39;49;00m$
  1092	[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1093	[37m          [39;49;00m}[37m[39;49;00m$
  1094	[37m[39;49;00m$
  1095	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInComment||isInLineComment)[37m[39;49;00m$
  1096	[37m          [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1097	[37m[39;49;00m$
  1098	[37m        [39;49;00m[37m// if we have reached this far then we are NOT in a comment or string of special character...[39;49;00m$
  1099	[37m[39;49;00m$
  1100	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(probationHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1101	[37m          [39;49;00m{[37m[39;49;00m$
  1102	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m((probationHeader[37m [39;49;00m==[37m [39;49;00m&AS_STATIC[37m [39;49;00m||[37m [39;49;00mprobationHeader[37m [39;49;00m==[37m [39;49;00m&AS_CONST)[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1103	[37m                 [39;49;00m||[37m [39;49;00m(probationHeader[37m [39;49;00m==[37m [39;49;00m&AS_SYNCHRONIZED[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m))[37m[39;49;00m$
  1104	[37m              [39;49;00m{[37m[39;49;00m$
  1105	[37m                [39;49;00m[37m// insert the probation header as a new header[39;49;00m$
  1106	[37m                [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1107	[37m                [39;49;00mheaderStack->push_back(probationHeader);[37m[39;49;00m$
  1108	[37m[39;49;00m$
  1109	[37m                [39;49;00m[37m// handle the specific probation header[39;49;00m$
  1110	[37m                [39;49;00misInConditional[37m [39;49;00m=[37m [39;49;00m(probationHeader[37m [39;49;00m==[37m [39;49;00m&AS_SYNCHRONIZED);[37m[39;49;00m$
  1111	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(probationHeader[37m [39;49;00m==[37m [39;49;00m&AS_CONST)[37m[39;49;00m$
  1112	[37m                  [39;49;00misImmediatelyAfterConst[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1113	[37m                [39;49;00m[37m//  isInConst = true;[39;49;00m$
  1114	[37m                [39;49;00m[37m/* TODO:[39;49;00m$
  1115	[37m                 * There is actually no more need for the global isInConst variable.[39;49;00m$
  1116	[37m                               * The only reason for checking const is to see if there is a const[39;49;00m$
  1117	[37m                 * immediately before an open-bracket.[39;49;00m$
  1118	[37m                 * Since CONST is now put into probation and is checked during itspost-char,[39;49;00m$
  1119	[37m                 * isImmediatelyAfterConst can be set by its own...[39;49;00m$
  1120	[37m                 */[39;49;00m[37m[39;49;00m$
  1121	[37m[39;49;00m$
  1122	[37m                [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1123	[37m                [39;49;00m[37m// if the probation comes from the previous line, then indent by 1 tab count.[39;49;00m$
  1124	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(previousLineProbation[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1125	[37m                  [39;49;00mtabCount++;[37m[39;49;00m$
  1126	[37m                [39;49;00mpreviousLineProbation[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1127	[37m              [39;49;00m}[37m[39;49;00m$
  1128	[37m[39;49;00m$
  1129	[37m            [39;49;00m[37m// dismiss the probation header[39;49;00m$
  1130	[37m            [39;49;00mprobationHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1131	[37m          [39;49;00m}[37m[39;49;00m$
  1132	[37m[39;49;00m$
  1133	[37m        [39;49;00mprevNonSpaceCh[37m [39;49;00m=[37m [39;49;00mcurrentNonSpaceCh;[37m[39;49;00m$
  1134	[37m        [39;49;00mcurrentNonSpaceCh[37m [39;49;00m=[37m [39;49;00mch;[37m[39;49;00m$
  1135	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isLegalNameChar(ch)[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m!=[37m [39;49;00m[33m'[39;49;00m[33m,[39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m!=[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
  1136	[37m          [39;49;00m{[37m[39;49;00m$
  1137	[37m            [39;49;00mprevNonLegalCh[37m [39;49;00m=[37m [39;49;00mcurrentNonLegalCh;[37m[39;49;00m$
  1138	[37m            [39;49;00mcurrentNonLegalCh[37m [39;49;00m=[37m [39;49;00mch;[37m[39;49;00m$
  1139	[37m          [39;49;00m}[37m[39;49;00m$
  1140	[37m[39;49;00m$
  1141	[37m        [39;49;00m[37m//if (isInConst)[39;49;00m$
  1142	[37m        [39;49;00m[37m//{[39;49;00m$
  1143	[37m        [39;49;00m[37m//    isInConst = false;[39;49;00m$
  1144	[37m        [39;49;00m[37m//    isImmediatelyAfterConst = true;[39;49;00m$
  1145	[37m        [39;49;00m[37m//}[39;49;00m$
  1146	[37m[39;49;00m$
  1147	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInHeader)[37m[39;49;00m$
  1148	[37m          [39;49;00m{[37m[39;49;00m$
  1149	[37m            [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1150	[37m            [39;49;00mcurrentHeader[37m [39;49;00m=[37m [39;49;00mheaderStack->back();[37m[39;49;00m$
  1151	[37m          [39;49;00m}[37m[39;49;00m$
  1152	[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1153	[37m          [39;49;00mcurrentHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1154	[37m[39;49;00m$
  1155	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00misInTemplate[37m[39;49;00m$
  1156	[37m            [39;49;00m&&[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m<[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m>[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1157	[37m            [39;49;00m&&[37m  [39;49;00mfindHeader(line,[37m [39;49;00mi,[37m [39;49;00mnonAssignmentOperators)[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[37m//;[39;49;00m$
  1158	[37m          [39;49;00m{[37m[39;49;00m$
  1159	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m<[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1160	[37m              [39;49;00m{[37m[39;49;00m$
  1161	[37m                [39;49;00m++templateDepth;[37m[39;49;00m$
  1162	[37m              [39;49;00m}[37m[39;49;00m$
  1163	[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m>[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1164	[37m              [39;49;00m{[37m[39;49;00m$
  1165	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(--templateDepth[37m [39;49;00m<=[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1166	[37m                  [39;49;00m{[37m[39;49;00m$
  1167	[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInTemplate)[37m[39;49;00m$
  1168	[37m                      [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
  1169	[37m                    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1170	[37m                      [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33mt[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
  1171	[37m                    [39;49;00misInTemplate[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1172	[37m                    [39;49;00mtemplateDepth[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  1173	[37m                  [39;49;00m}[37m[39;49;00m$
  1174	[37m[39;49;00m$
  1175	[37m              [39;49;00m}[37m[39;49;00m$
  1176	[37m          [39;49;00m}[37m[39;49;00m$
  1177	[37m[39;49;00m$
  1178	[37m        [39;49;00m[37m// handle parenthesies[39;49;00m$
  1179	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m[[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m][39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1180	[37m          [39;49;00m{[37m[39;49;00m$
  1181	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m[[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1182	[37m              [39;49;00m{[37m[39;49;00m$
  1183	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(parenDepth[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1184	[37m                  [39;49;00m{[37m[39;49;00m$
  1185	[37m                    [39;49;00mparenStatementStack->push_back(isInStatement);[37m[39;49;00m$
  1186	[37m                    [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1187	[37m                  [39;49;00m}[37m[39;49;00m$
  1188	[37m                [39;49;00mparenDepth++;[37m[39;49;00m$
  1189	[37m[39;49;00m$
  1190	[37m                [39;49;00minStatementIndentStackSizeStack->push_back(inStatementIndentStack->size());[37m[39;49;00m$
  1191	[37m[39;49;00m$
  1192	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(currentHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1193	[37m                  [39;49;00mregisterInStatementIndent(line,[37m [39;49;00mi,[37m [39;49;00mspaceTabCount,[37m [39;49;00mminConditionalIndent[37m/*indentLength*2*/[39;49;00m,[37m [39;49;00m[36mtrue[39;49;00m);[37m[39;49;00m$
  1194	[37m                [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1195	[37m                  [39;49;00mregisterInStatementIndent(line,[37m [39;49;00mi,[37m [39;49;00mspaceTabCount,[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00m[36mtrue[39;49;00m);[37m[39;49;00m$
  1196	[37m              [39;49;00m}[37m[39;49;00m$
  1197	[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m][39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1198	[37m              [39;49;00m{[37m[39;49;00m$
  1199	[37m                [39;49;00mparenDepth--;[37m[39;49;00m$
  1200	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(parenDepth[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1201	[37m                  [39;49;00m{[37m[39;49;00m$
  1202	[37m                    [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00mparenStatementStack->back();[37m[39;49;00m$
  1203	[37m                    [39;49;00mparenStatementStack->pop_back();[37m[39;49;00m$
  1204	[37m                    [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
  1205	[37m[39;49;00m$
  1206	[37m                    [39;49;00misInConditional[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1207	[37m                  [39;49;00m}[37m[39;49;00m$
  1208	[37m[39;49;00m$
  1209	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStackSizeStack->empty())[37m[39;49;00m$
  1210	[37m                  [39;49;00m{[37m[39;49;00m$
  1211	[37m                    [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mpreviousIndentStackSize[37m [39;49;00m=[37m [39;49;00minStatementIndentStackSizeStack->back();[37m[39;49;00m$
  1212	[37m                    [39;49;00minStatementIndentStackSizeStack->pop_back();[37m[39;49;00m$
  1213	[37m                    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(previousIndentStackSize[37m [39;49;00m<[37m [39;49;00minStatementIndentStack->size())[37m[39;49;00m$
  1214	[37m                      [39;49;00minStatementIndentStack->pop_back();[37m[39;49;00m$
  1215	[37m[39;49;00m$
  1216	[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!parenIndentStack->empty())[37m[39;49;00m$
  1217	[37m                      [39;49;00m{[37m[39;49;00m$
  1218	[37m                        [39;49;00m[36mint[39;49;00m[37m [39;49;00mpoppedIndent[37m [39;49;00m=[37m [39;49;00mparenIndentStack->back();[37m[39;49;00m$
  1219	[37m                        [39;49;00mparenIndentStack->pop_back();[37m[39;49;00m$
  1220	[37m[39;49;00m$
  1221	[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1222	[37m                          [39;49;00mspaceTabCount[37m [39;49;00m=[37m [39;49;00mpoppedIndent;[37m[39;49;00m$
  1223	[37m                      [39;49;00m}[37m[39;49;00m$
  1224	[37m                  [39;49;00m}[37m[39;49;00m$
  1225	[37m              [39;49;00m}[37m[39;49;00m$
  1226	[37m[39;49;00m$
  1227	[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1228	[37m          [39;49;00m}[37m[39;49;00m$
  1229	[37m[39;49;00m$
  1230	[37m[39;49;00m$
  1231	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1232	[37m          [39;49;00m{[37m[39;49;00m$
  1233	[37m            [39;49;00m[36mbool[39;49;00m[37m [39;49;00misBlockOpener[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1234	[37m[39;49;00m$
  1235	[37m            [39;49;00m[37m// first, check if '{' is a block-opener or an static-array opener[39;49;00m$
  1236	[37m            [39;49;00misBlockOpener[37m [39;49;00m=[37m [39;49;00m([37m [39;49;00m(prevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00mbracketBlockStateStack->back())[37m[39;49;00m$
  1237	[37m                              [39;49;00m||[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
  1238	[37m                              [39;49;00m||[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
  1239	[37m                              [39;49;00m||[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
  1240	[37m                              [39;49;00m||[37m [39;49;00misInClassHeader[37m[39;49;00m$
  1241	[37m                              [39;49;00m||[37m [39;49;00misBlockOpener[37m[39;49;00m$
  1242	[37m                              [39;49;00m||[37m [39;49;00misImmediatelyAfterConst[37m[39;49;00m$
  1243	[37m                              [39;49;00m||[37m [39;49;00m(isInDefine[37m [39;49;00m&&[37m[39;49;00m$
  1244	[37m                                  [39;49;00m(prevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[37m[39;49;00m$
  1245	[37m                                   [39;49;00m||[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m_[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
  1246	[37m                                   [39;49;00m||[37m [39;49;00misalnum(prevNonSpaceCh)))[37m [39;49;00m);[37m[39;49;00m$
  1247	[37m[39;49;00m$
  1248	[37m            [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1249	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isBlockOpener[37m [39;49;00m&&[37m [39;49;00mcurrentHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1250	[37m              [39;49;00m{[37m[39;49;00m$
  1251	[37m                [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mn=[34m0[39;49;00m;[37m [39;49;00mn[37m [39;49;00m<[37m [39;49;00mnonParenHeaders.size();[37m [39;49;00mn++)[37m[39;49;00m$
  1252	[37m                  [39;49;00m[34mif[39;49;00m[37m [39;49;00m(currentHeader[37m [39;49;00m==[37m [39;49;00mnonParenHeaders[n])[37m[39;49;00m$
  1253	[37m                    [39;49;00m{[37m[39;49;00m$
  1254	[37m                      [39;49;00misBlockOpener[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1255	[37m                      [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1256	[37m                    [39;49;00m}[37m[39;49;00m$
  1257	[37m              [39;49;00m}[37m[39;49;00m$
  1258	[37m            [39;49;00mbracketBlockStateStack->push_back(isBlockOpener);[37m[39;49;00m$
  1259	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isBlockOpener)[37m[39;49;00m$
  1260	[37m              [39;49;00m{[37m[39;49;00m$
  1261	[37m                [39;49;00minStatementIndentStackSizeStack->push_back(inStatementIndentStack->size());[37m[39;49;00m$
  1262	[37m                [39;49;00mregisterInStatementIndent(line,[37m [39;49;00mi,[37m [39;49;00mspaceTabCount,[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00m[36mtrue[39;49;00m);[37m[39;49;00m$
  1263	[37m                [39;49;00mparenDepth++;[37m[39;49;00m$
  1264	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1265	[37m                  [39;49;00mshouldIndentBrackettedLine[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1266	[37m[39;49;00m$
  1267	[37m                [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1268	[37m              [39;49;00m}[37m[39;49;00m$
  1269	[37m[39;49;00m$
  1270	[37m            [39;49;00m[37m// this bracket is a block opener...[39;49;00m$
  1271	[37m[39;49;00m$
  1272	[37m            [39;49;00m++lineOpeningBlocksNum;[37m[39;49;00m$
  1273	[37m[39;49;00m$
  1274	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInClassHeader)[37m[39;49;00m$
  1275	[37m              [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1276	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInClassHeaderTab)[37m[39;49;00m$
  1277	[37m              [39;49;00m{[37m[39;49;00m$
  1278	[37m                [39;49;00misInClassHeaderTab[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1279	[37m                [39;49;00mtabCount[37m [39;49;00m-=[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m$
  1280	[37m              [39;49;00m}[37m[39;49;00m$
  1281	[37m[39;49;00m$
  1282	[37m            [39;49;00mblockParenDepthStack->push_back(parenDepth);[37m[39;49;00m$
  1283	[37m            [39;49;00mblockStatementStack->push_back(isInStatement);[37m[39;49;00m$
  1284	[37m[39;49;00m$
  1285	[37m            [39;49;00minStatementIndentStackSizeStack->push_back(inStatementIndentStack->size());[37m[39;49;00m$
  1286	[37m[39;49;00m$
  1287	[37m            [39;49;00mblockTabCount[37m [39;49;00m+=[37m [39;49;00misInStatement?[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m:[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  1288	[37m            [39;49;00mparenDepth[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  1289	[37m            [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1290	[37m[39;49;00m$
  1291	[37m            [39;49;00mtempStacks->push_back([34mnew[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>);[37m[39;49;00m$
  1292	[37m            [39;49;00mheaderStack->push_back(&AS_OPEN_BRACKET);[37m[39;49;00m$
  1293	[37m            [39;49;00mlastLineHeader[37m [39;49;00m=[37m [39;49;00m&AS_OPEN_BRACKET;[37m [39;49;00m[37m// <------[39;49;00m$
  1294	[37m[39;49;00m$
  1295	[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1296	[37m          [39;49;00m}[37m[39;49;00m$
  1297	[37m[39;49;00m$
  1298	[37m        [39;49;00m[37m//check if a header has been reached[39;49;00m$
  1299	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(prevCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1300	[37m          [39;49;00m{[37m[39;49;00m$
  1301	[37m            [39;49;00m[36mbool[39;49;00m[37m [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1302	[37m            [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*newHeader[37m [39;49;00m=[37m [39;49;00mfindHeader(line,[37m [39;49;00mi,[37m [39;49;00mheaders);[37m[39;49;00m$
  1303	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1304	[37m              [39;49;00m{[37m[39;49;00m$
  1305	[37m                [39;49;00m[37m// if we reached here, then this is a header...[39;49;00m$
  1306	[37m                [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1307	[37m[39;49;00m$
  1308	[37m                [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m*lastTempStack;[37m[39;49;00m$
  1309	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(tempStacks->empty())[37m[39;49;00m$
  1310	[37m                  [39;49;00mlastTempStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1311	[37m                [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1312	[37m                  [39;49;00mlastTempStack[37m [39;49;00m=[37m [39;49;00mtempStacks->back();[37m[39;49;00m$
  1313	[37m[39;49;00m$
  1314	[37m                [39;49;00m[37m// if a new block is opened, push a new stack into tempStacks to hold the[39;49;00m$
  1315	[37m                [39;49;00m[37m// future list of headers in the new block.[39;49;00m$
  1316	[37m[39;49;00m$
  1317	[37m                [39;49;00m[37m// take care of the special case: 'else if (...)'[39;49;00m$
  1318	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_IF[37m [39;49;00m&&[37m [39;49;00mlastLineHeader[37m [39;49;00m==[37m [39;49;00m&AS_ELSE)[37m[39;49;00m$
  1319	[37m                  [39;49;00m{[37m[39;49;00m$
  1320	[37m                    [39;49;00m[37m//spaceTabCount += indentLength; // to counter the opposite addition that occurs when the 'if' is registered below...[39;49;00m$
  1321	[37m                    [39;49;00mheaderStack->pop_back();[37m[39;49;00m$
  1322	[37m                  [39;49;00m}[37m[39;49;00m$
  1323	[37m[39;49;00m$
  1324	[37m                [39;49;00m[37m// take care of 'else'[39;49;00m$
  1325	[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_ELSE)[37m[39;49;00m$
  1326	[37m                  [39;49;00m{[37m[39;49;00m$
  1327	[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lastTempStack[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1328	[37m                      [39;49;00m{[37m[39;49;00m$
  1329	[37m                        [39;49;00m[36mint[39;49;00m[37m [39;49;00mindexOfIf[37m [39;49;00m=[37m [39;49;00mindexOf(*lastTempStack,[37m [39;49;00m&AS_IF);[37m [39;49;00m[37m// <---[39;49;00m$
  1330	[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(indexOfIf[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
  1331	[37m                          [39;49;00m{[37m[39;49;00m$
  1332	[37m                            [39;49;00m[37m// recreate the header list in headerStack up to the previous 'if'[39;49;00m$
  1333	[37m                            [39;49;00m[37m// from the temporary snapshot stored in lastTempStack.[39;49;00m$
  1334	[37m                            [39;49;00m[36mint[39;49;00m[37m [39;49;00mrestackSize[37m [39;49;00m=[37m [39;49;00mlastTempStack->size()[37m [39;49;00m-[37m [39;49;00mindexOfIf[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1335	[37m                            [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mr=[34m0[39;49;00m;[37m [39;49;00mr<restackSize;[37m [39;49;00mr++)[37m[39;49;00m$
  1336	[37m                              [39;49;00m{[37m[39;49;00m$
  1337	[37m                                [39;49;00mheaderStack->push_back(lastTempStack->back());[37m[39;49;00m$
  1338	[37m                                [39;49;00mlastTempStack->pop_back();[37m[39;49;00m$
  1339	[37m                              [39;49;00m}[37m[39;49;00m$
  1340	[37m                            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!closingBracketReached)[37m[39;49;00m$
  1341	[37m                              [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00mrestackSize;[37m[39;49;00m$
  1342	[37m                          [39;49;00m}[37m[39;49;00m$
  1343	[37m                        [39;49;00m[37m/*[39;49;00m$
  1344	[37m                         * If the above if is not true, i.e. no 'if' before the 'else',[39;49;00m$
  1345	[37m                         * then nothing beautiful will come out of this...[39;49;00m$
  1346	[37m                         * I should think about inserting an Exception here to notify the caller of this...[39;49;00m$
  1347	[37m                         */[39;49;00m[37m[39;49;00m$
  1348	[37m                      [39;49;00m}[37m[39;49;00m$
  1349	[37m                  [39;49;00m}[37m[39;49;00m$
  1350	[37m[39;49;00m$
  1351	[37m                [39;49;00m[37m// check if 'while' closes a previous 'do'[39;49;00m$
  1352	[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_WHILE)[37m[39;49;00m$
  1353	[37m                  [39;49;00m{[37m[39;49;00m$
  1354	[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lastTempStack[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1355	[37m                      [39;49;00m{[37m[39;49;00m$
  1356	[37m                        [39;49;00m[36mint[39;49;00m[37m [39;49;00mindexOfDo[37m [39;49;00m=[37m [39;49;00mindexOf(*lastTempStack,[37m [39;49;00m&AS_DO);[37m [39;49;00m[37m// <---[39;49;00m$
  1357	[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(indexOfDo[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
  1358	[37m                          [39;49;00m{[37m[39;49;00m$
  1359	[37m                            [39;49;00m[37m// recreate the header list in headerStack up to the previous 'do'[39;49;00m$
  1360	[37m                            [39;49;00m[37m// from the temporary snapshot stored in lastTempStack.[39;49;00m$
  1361	[37m                            [39;49;00m[36mint[39;49;00m[37m [39;49;00mrestackSize[37m [39;49;00m=[37m [39;49;00mlastTempStack->size()[37m [39;49;00m-[37m [39;49;00mindexOfDo[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1362	[37m                            [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mr=[34m0[39;49;00m;[37m [39;49;00mr<restackSize;[37m [39;49;00mr++)[37m[39;49;00m$
  1363	[37m                              [39;49;00m{[37m[39;49;00m$
  1364	[37m                                [39;49;00mheaderStack->push_back(lastTempStack->back());[37m[39;49;00m$
  1365	[37m                                [39;49;00mlastTempStack->pop_back();[37m[39;49;00m$
  1366	[37m                              [39;49;00m}[37m[39;49;00m$
  1367	[37m                            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!closingBracketReached)[37m[39;49;00m$
  1368	[37m                              [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00mrestackSize;[37m[39;49;00m$
  1369	[37m                          [39;49;00m}[37m[39;49;00m$
  1370	[37m                      [39;49;00m}[37m[39;49;00m$
  1371	[37m                  [39;49;00m}[37m[39;49;00m$
  1372	[37m                [39;49;00m[37m// check if 'catch' closes a previous 'try' or 'catch'[39;49;00m$
  1373	[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_CATCH[37m [39;49;00m||[37m [39;49;00mnewHeader[37m [39;49;00m==[37m [39;49;00m&AS_FINALLY)[37m[39;49;00m$
  1374	[37m                  [39;49;00m{[37m[39;49;00m$
  1375	[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lastTempStack[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1376	[37m                      [39;49;00m{[37m[39;49;00m$
  1377	[37m                        [39;49;00m[36mint[39;49;00m[37m [39;49;00mindexOfTry[37m [39;49;00m=[37m [39;49;00mindexOf(*lastTempStack,[37m [39;49;00m&AS_TRY);[37m[39;49;00m$
  1378	[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(indexOfTry[37m [39;49;00m==[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
  1379	[37m                          [39;49;00mindexOfTry[37m [39;49;00m=[37m [39;49;00mindexOf(*lastTempStack,[37m [39;49;00m&AS_CATCH);[37m[39;49;00m$
  1380	[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(indexOfTry[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
  1381	[37m                          [39;49;00m{[37m[39;49;00m$
  1382	[37m                            [39;49;00m[37m// recreate the header list in headerStack up to the previous 'try'[39;49;00m$
  1383	[37m                            [39;49;00m[37m// from the temporary snapshot stored in lastTempStack.[39;49;00m$
  1384	[37m                            [39;49;00m[36mint[39;49;00m[37m [39;49;00mrestackSize[37m [39;49;00m=[37m [39;49;00mlastTempStack->size()[37m [39;49;00m-[37m [39;49;00mindexOfTry[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1385	[37m                            [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mr=[34m0[39;49;00m;[37m [39;49;00mr<restackSize;[37m [39;49;00mr++)[37m[39;49;00m$
  1386	[37m                              [39;49;00m{[37m[39;49;00m$
  1387	[37m                                [39;49;00mheaderStack->push_back(lastTempStack->back());[37m[39;49;00m$
  1388	[37m                                [39;49;00mlastTempStack->pop_back();[37m[39;49;00m$
  1389	[37m                              [39;49;00m}[37m[39;49;00m$
  1390	[37m[39;49;00m$
  1391	[37m                            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!closingBracketReached)[37m[39;49;00m$
  1392	[37m                              [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00mrestackSize;[37m[39;49;00m$
  1393	[37m                          [39;49;00m}[37m[39;49;00m$
  1394	[37m                      [39;49;00m}[37m[39;49;00m$
  1395	[37m                  [39;49;00m}[37m[39;49;00m$
  1396	[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_CASE)[37m[39;49;00m$
  1397	[37m                  [39;49;00m{[37m[39;49;00m$
  1398	[37m                    [39;49;00misInCase[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1399	[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!caseIndent)[37m[39;49;00m$
  1400	[37m                      [39;49;00m--tabCount;[37m[39;49;00m$
  1401	[37m                  [39;49;00m}[37m[39;49;00m$
  1402	[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_DEFAULT)[37m[39;49;00m$
  1403	[37m                  [39;49;00m{[37m[39;49;00m$
  1404	[37m                    [39;49;00misInCase[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1405	[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!caseIndent)[37m[39;49;00m$
  1406	[37m                      [39;49;00m--tabCount;[37m[39;49;00m$
  1407	[37m                  [39;49;00m}[37m[39;49;00m$
  1408	[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_PUBLIC[37m [39;49;00m||[37m [39;49;00mnewHeader[37m [39;49;00m==[37m [39;49;00m&AS_PROTECTED[37m [39;49;00m||[37m [39;49;00mnewHeader[37m [39;49;00m==[37m [39;49;00m&AS_PRIVATE)[37m[39;49;00m$
  1409	[37m                  [39;49;00m{[37m[39;49;00m$
  1410	[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00m!isInClassHeader)[37m[39;49;00m$
  1411	[37m                      [39;49;00m--tabCount;[37m[39;49;00m$
  1412	[37m                    [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1413	[37m                  [39;49;00m}[37m[39;49;00m$
  1414	[37m                [39;49;00m[37m//else if ((newHeader == &STATIC || newHeader == &SYNCHRONIZED) &&[39;49;00m$
  1415	[37m                [39;49;00m[37m//         !headerStack->empty() &&[39;49;00m$
  1416	[37m                [39;49;00m[37m//         (headerStack->back() == &STATIC || headerStack->back() == &SYNCHRONIZED))[39;49;00m$
  1417	[37m                [39;49;00m[37m//{[39;49;00m$
  1418	[37m                [39;49;00m[37m//    isIndentableHeader = false;[39;49;00m$
  1419	[37m                [39;49;00m[37m//}[39;49;00m$
  1420	[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_STATIC[37m[39;49;00m$
  1421	[37m                         [39;49;00m||[37m [39;49;00mnewHeader[37m [39;49;00m==[37m [39;49;00m&AS_SYNCHRONIZED[37m[39;49;00m$
  1422	[37m                         [39;49;00m||[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_CONST[37m [39;49;00m&&[37m [39;49;00misCStyle))[37m[39;49;00m$
  1423	[37m                  [39;49;00m{[37m[39;49;00m$
  1424	[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!headerStack->empty()[37m [39;49;00m&&[37m[39;49;00m$
  1425	[37m                        [39;49;00m(headerStack->back()[37m [39;49;00m==[37m [39;49;00m&AS_STATIC[37m[39;49;00m$
  1426	[37m                         [39;49;00m||[37m [39;49;00mheaderStack->back()[37m [39;49;00m==[37m [39;49;00m&AS_SYNCHRONIZED[37m[39;49;00m$
  1427	[37m                         [39;49;00m||[37m [39;49;00mheaderStack->back()[37m [39;49;00m==[37m [39;49;00m&AS_CONST))[37m[39;49;00m$
  1428	[37m                      [39;49;00m{[37m[39;49;00m$
  1429	[37m                        [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1430	[37m                      [39;49;00m}[37m[39;49;00m$
  1431	[37m                    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1432	[37m                      [39;49;00m{[37m[39;49;00m$
  1433	[37m                        [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1434	[37m                        [39;49;00mprobationHeader[37m [39;49;00m=[37m [39;49;00mnewHeader;[37m[39;49;00m$
  1435	[37m                      [39;49;00m}[37m[39;49;00m$
  1436	[37m                  [39;49;00m}[37m[39;49;00m$
  1437	[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_CONST)[37m[39;49;00m$
  1438	[37m                  [39;49;00m{[37m[39;49;00m$
  1439	[37m                    [39;49;00m[37m// this will be entered only if NOT in C style[39;49;00m$
  1440	[37m                    [39;49;00m[37m// since otherwise the CONST would be found to be a probstion header...[39;49;00m$
  1441	[37m[39;49;00m$
  1442	[37m                    [39;49;00m[37m//if (isCStyle)[39;49;00m$
  1443	[37m                    [39;49;00m[37m//  isInConst = true;[39;49;00m$
  1444	[37m                    [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1445	[37m                  [39;49;00m}[37m[39;49;00m$
  1446	[37m                [39;49;00m[37m/*[39;49;00m$
  1447	[37m                              else if (newHeader == &OPERATOR)[39;49;00m$
  1448	[37m                              {[39;49;00m$
  1449	[37m                                  if (isCStyle)[39;49;00m$
  1450	[37m                                      isInOperator = true;[39;49;00m$
  1451	[37m                                  isIndentableHeader = false;[39;49;00m$
  1452	[37m                              }[39;49;00m$
  1453	[37m                */[39;49;00m[37m[39;49;00m$
  1454	[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_TEMPLATE)[37m[39;49;00m$
  1455	[37m                  [39;49;00m{[37m[39;49;00m$
  1456	[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle)[37m[39;49;00m$
  1457	[37m                      [39;49;00misInTemplate[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1458	[37m                    [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1459	[37m                  [39;49;00m}[37m[39;49;00m$
  1460	[37m[39;49;00m$
  1461	[37m[39;49;00m$
  1462	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isIndentableHeader)[37m[39;49;00m$
  1463	[37m                  [39;49;00m{[37m[39;49;00m$
  1464	[37m                    [39;49;00m[37m// 3.2.99[39;49;00m$
  1465	[37m                    [39;49;00m[37m//spaceTabCount-=indentLength;[39;49;00m$
  1466	[37m                    [39;49;00mheaderStack->push_back(newHeader);[37m[39;49;00m$
  1467	[37m                    [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1468	[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(indexOf(nonParenHeaders,[37m [39;49;00mnewHeader)[37m [39;49;00m==[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
  1469	[37m                      [39;49;00m{[37m[39;49;00m$
  1470	[37m                        [39;49;00misInConditional[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1471	[37m                      [39;49;00m}[37m[39;49;00m$
  1472	[37m                    [39;49;00mlastLineHeader[37m [39;49;00m=[37m [39;49;00mnewHeader;[37m[39;49;00m$
  1473	[37m                  [39;49;00m}[37m[39;49;00m$
  1474	[37m                [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1475	[37m                  [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1476	[37m[39;49;00m$
  1477	[37m                [39;49;00m[37m//lastLineHeader = newHeader;[39;49;00m$
  1478	[37m[39;49;00m$
  1479	[37m                [39;49;00moutBuffer.append(newHeader->substr([34m1[39;49;00m));[37m[39;49;00m$
  1480	[37m                [39;49;00mi[37m [39;49;00m+=[37m [39;49;00mnewHeader->length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1481	[37m[39;49;00m$
  1482	[37m                [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1483	[37m              [39;49;00m}[37m[39;49;00m$
  1484	[37m          [39;49;00m}[37m[39;49;00m$
  1485	[37m[39;49;00m$
  1486	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00m!isalpha(prevCh)[37m[39;49;00m$
  1487	[37m            [39;49;00m&&[37m [39;49;00mline.COMPARE(i,[37m [39;49;00m[34m8[39;49;00m,[37m [39;49;00mAS_OPERATOR)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m!isalnum(line[i+[34m8[39;49;00m]))[37m[39;49;00m$
  1488	[37m          [39;49;00m{[37m[39;49;00m$
  1489	[37m            [39;49;00misInOperator[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1490	[37m            [39;49;00moutBuffer.append(AS_OPERATOR.substr([34m1[39;49;00m));[37m[39;49;00m$
  1491	[37m            [39;49;00mi[37m [39;49;00m+=[37m [39;49;00m[34m7[39;49;00m;[37m[39;49;00m$
  1492	[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1493	[37m          [39;49;00m}[37m[39;49;00m$
  1494	[37m[39;49;00m$
  1495	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m?[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1496	[37m          [39;49;00misInQuestion[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1497	[37m[39;49;00m$
  1498	[37m[39;49;00m$
  1499	[37m        [39;49;00m[37m// special handling of 'case' statements[39;49;00m$
  1500	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1501	[37m          [39;49;00m{[37m[39;49;00m$
  1502	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.length()[37m [39;49;00m>[37m [39;49;00mi+[34m1[39;49;00m[37m [39;49;00m&&[37m [39;49;00mline[i+[34m1[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m)[37m [39;49;00m[37m// look for ::[39;49;00m$
  1503	[37m              [39;49;00m{[37m[39;49;00m$
  1504	[37m                [39;49;00m++i;[37m[39;49;00m$
  1505	[37m                [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
  1506	[37m                [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
  1507	[37m                [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1508	[37m              [39;49;00m}[37m[39;49;00m$
  1509	[37m[39;49;00m$
  1510	[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00misInClass[37m [39;49;00m&&[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m!=[37m [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1511	[37m              [39;49;00m{[37m[39;49;00m$
  1512	[37m              [39;49;00m[37m// BEGIN Content of ASBeautifier.cpp.BITFIELD.patch:[39;49;00m$
  1513	[37m              [39;49;00m[37m[39;49;00m$
  1514	[37m                [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mchIndex;[37m[39;49;00m$
  1515	[37m   			    [39;49;00m[36mchar[39;49;00m[37m [39;49;00mnextCh[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  1516	[37m                [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(chIndex[37m [39;49;00m=[37m [39;49;00mi+[34m1[39;49;00m;[37m [39;49;00mchIndex[37m [39;49;00m<[37m [39;49;00mline.length();[37m [39;49;00mchIndex++)[37m[39;49;00m$
  1517	[37m            		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[chIndex]))[37m[39;49;00m$
  1518	[37m						[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1519	[37m					[39;49;00m[34mif[39;49;00m[37m [39;49;00m(chIndex<[37m [39;49;00mline.length())[37m[39;49;00m$
  1520	[37m       					[39;49;00mnextCh[37m [39;49;00m=[37m [39;49;00mline[chIndex];[37m[39;49;00m$
  1521	[37m				[39;49;00m[36mint[39;49;00m[37m [39;49;00mnWord[37m [39;49;00m=[34m0[39;49;00m;[37m[39;49;00m$
  1522	[37m    			[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(chIndex[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mchIndex[37m [39;49;00m<[37m [39;49;00mi;[37m [39;49;00mchIndex++)[37m[39;49;00m$
  1523	[37m				[39;49;00m{[37m[39;49;00m$
  1524	[37m					[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[chIndex]))[37m[39;49;00m$
  1525	[37m					[39;49;00m{[37m[39;49;00m$
  1526	[37m						[39;49;00mnWord[37m [39;49;00m++;[37m[39;49;00m$
  1527	[37m						[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[++chIndex]));[37m[39;49;00m$
  1528	[37m					[39;49;00m}[37m									[39;49;00m[37m[39;49;00m$
  1529	[37m				[39;49;00m}[37m[39;49;00m$
  1530	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m((nextCh[37m [39;49;00m>=[37m [39;49;00m[33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00mnextCh[37m [39;49;00m<=[37m [39;49;00m[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m)[37m [39;49;00m||[37m [39;49;00m(nWord[37m [39;49;00m>[34m1[39;49;00m))[37m[39;49;00m$
  1531	[37m					[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1532	[37m              [39;49;00m[37m// END Content of ASBeautifier.cpp.BITFIELD.patch:[39;49;00m$
  1533	[37m                [39;49;00m[37m[39;49;00m$
  1534	[37m                [39;49;00m--tabCount;[37m[39;49;00m$
  1535	[37m                [39;49;00m[37m// found a 'private:' or 'public:' inside a class definition[39;49;00m$
  1536	[37m                [39;49;00m[37m// so do nothing special[39;49;00m$
  1537	[37m              [39;49;00m}[37m[39;49;00m$
  1538	[37m[39;49;00m$
  1539	[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00misInClassHeader)[37m[39;49;00m$
  1540	[37m              [39;49;00m{[37m[39;49;00m$
  1541	[37m[39;49;00m$
  1542	[37m                [39;49;00m[37m// found a 'class A : public B' definition[39;49;00m$
  1543	[37m                [39;49;00m[37m// so do nothing special[39;49;00m$
  1544	[37m              [39;49;00m}[37m[39;49;00m$
  1545	[37m[39;49;00m$
  1546	[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInQuestion)[37m[39;49;00m$
  1547	[37m              [39;49;00m{[37m[39;49;00m$
  1548	[37m                [39;49;00misInQuestion[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1549	[37m              [39;49;00m}[37m[39;49;00m$
  1550	[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1551	[37m              [39;49;00m{[37m[39;49;00m$
  1552	[37m                [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1553	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i==[34m0[39;49;00m)[37m[39;49;00m$
  1554	[37m                  [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m$
  1555	[37m              [39;49;00m}[37m[39;49;00m$
  1556	[37m            [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1557	[37m              [39;49;00m{[37m[39;49;00m$
  1558	[37m                [39;49;00mcurrentNonSpaceCh[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m;[37m [39;49;00m[37m// so that brackets after the ':' will appear as block-openers[39;49;00m$
  1559	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInCase)[37m[39;49;00m$
  1560	[37m                  [39;49;00m{[37m[39;49;00m$
  1561	[37m                    [39;49;00misInCase[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1562	[37m                    [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m;[37m [39;49;00m[37m// from here on, treat char as ';'[39;49;00m$
  1563	[37m                  [39;49;00m}[37m [39;49;00m[37m[39;49;00m$
  1564	[37m              [39;49;00m[37m// BEGIN content of ASBeautifier.cpp.BITFIELD.patch.bz2[39;49;00m$
  1565	[37m              [39;49;00m[34melse[39;49;00m[37m [39;49;00m[37m// bitfield or labels[39;49;00m$
  1566	[37m								[39;49;00m{[37m[39;49;00m$
  1567	[37m				[39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mchIndex;[37m[39;49;00m$
  1568	[37m				[39;49;00m[36mchar[39;49;00m[37m [39;49;00mnextCh[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  1569	[37m				[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(chIndex[37m [39;49;00m=[37m [39;49;00mi+[34m1[39;49;00m;[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00mchIndex[37m [39;49;00m<[37m [39;49;00mline.length());[37m [39;49;00mchIndex++)[37m[39;49;00m$
  1570	[37m					[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[chIndex]))[37m[39;49;00m$
  1571	[37m						[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
  1572	[37m				[39;49;00m[34mif[39;49;00m[37m [39;49;00m(chIndex<[37m [39;49;00mline.length())[37m[39;49;00m$
  1573	[37m					[39;49;00mnextCh[37m [39;49;00m=[37m [39;49;00mline[chIndex];[37m[39;49;00m$
  1574	[37m[39;49;00m$
  1575	[37m     			[39;49;00m[36mint[39;49;00m[37m [39;49;00mnWord[37m [39;49;00m=[34m0[39;49;00m;[37m[39;49;00m$
  1576	[37m 				[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(chIndex[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mchIndex[37m [39;49;00m<[37m [39;49;00mi;[37m [39;49;00mchIndex++)[37m[39;49;00m$
  1577	[37m				[39;49;00m{[37m[39;49;00m$
  1578	[37m					[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[chIndex]))[37m[39;49;00m$
  1579	[37m					[39;49;00m{[37m[39;49;00m$
  1580	[37m						[39;49;00mnWord[37m [39;49;00m++;[37m[39;49;00m$
  1581	[37m						[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[++chIndex]));[37m[39;49;00m$
  1582	[37m					[39;49;00m}[37m									[39;49;00m[37m[39;49;00m$
  1583	[37m				[39;49;00m}[37m[39;49;00m$
  1584	[37m         		[39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m  [39;49;00m(nextCh[37m [39;49;00m>=[37m [39;49;00m[33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00mnextCh[37m [39;49;00m<=[37m [39;49;00m[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m)[37m [39;49;00m||[37m [39;49;00m(nWord[37m [39;49;00m>[34m1[39;49;00m))[37m[39;49;00m$
  1585	[37m				[39;49;00m{[37m[39;49;00m$
  1586	[37m					[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1587	[37m				[39;49;00m}[37m[39;49;00m$
  1588	[37m                [39;49;00m[37m// END content of ASASBeautifier.cpp.BITFIELD.patch.bz2[39;49;00m$
  1589	[37m[39;49;00m$
  1590	[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[37m// is in a label (e.g. 'label1:')[39;49;00m$
  1591	[37m                  [39;49;00m{[37m[39;49;00m$
  1592	[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(labelIndent)[37m[39;49;00m$
  1593	[37m                      [39;49;00m--tabCount;[37m [39;49;00m[37m// unindent label by one indent[39;49;00m$
  1594	[37m                    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1595	[37m                      [39;49;00mtabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00m[37m// completely flush indent to left[39;49;00m$
  1596	[37m                  [39;49;00m}[37m[39;49;00m$
  1597	[37m[39;49;00m$
  1598	[37m              [39;49;00m[37m// BEGIN content of ASASBeautifier.cpp.BITFIELD.patch.bz2[39;49;00m$
  1599	[37m                [39;49;00m}[37m[39;49;00m$
  1600	[37m            [39;49;00m[37m// END content of ASASBeautifier.cpp.BITFIELD.patch.bz2[39;49;00m$
  1601	[37m[39;49;00m$
  1602	[37m              [39;49;00m}[37m[39;49;00m$
  1603	[37m          [39;49;00m}[37m[39;49;00m$
  1604	[37m[39;49;00m$
  1605	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m((ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m[37m  [39;49;00m||[37m [39;49;00m(parenDepth>[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m,[39;49;00m[33m'[39;49;00m))[37m  [39;49;00m&&[37m [39;49;00m!inStatementIndentStackSizeStack->empty())[37m[39;49;00m$
  1606	[37m          [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m)inStatementIndentStackSizeStack->back()[37m [39;49;00m+[37m [39;49;00m(parenDepth>[34m0[39;49;00m[37m [39;49;00m?[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m:[37m [39;49;00m[34m0[39;49;00m)[37m  [39;49;00m<[37m [39;49;00minStatementIndentStack->size())[37m[39;49;00m$
  1607	[37m            [39;49;00minStatementIndentStack->pop_back();[37m[39;49;00m$
  1608	[37m[39;49;00m$
  1609	[37m[39;49;00m$
  1610	[37m        [39;49;00m[37m// handle ends of statements[39;49;00m$
  1611	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00mparenDepth[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m[37m/* || (ch == ',' && parenDepth == 0)*/[39;49;00m)[37m[39;49;00m$
  1612	[37m          [39;49;00m{[37m[39;49;00m$
  1613	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1614	[37m              [39;49;00m{[37m[39;49;00m$
  1615	[37m                [39;49;00m[37m// first check if this '}' closes a previous block, or a static array...[39;49;00m$
  1616	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!bracketBlockStateStack->empty())[37m[39;49;00m$
  1617	[37m                  [39;49;00m{[37m[39;49;00m$
  1618	[37m                    [39;49;00m[36mbool[39;49;00m[37m [39;49;00mbracketBlockState[37m [39;49;00m=[37m [39;49;00mbracketBlockStateStack->back();[37m[39;49;00m$
  1619	[37m                    [39;49;00mbracketBlockStateStack->pop_back();[37m[39;49;00m$
  1620	[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!bracketBlockState)[37m[39;49;00m$
  1621	[37m                      [39;49;00m{[37m[39;49;00m$
  1622	[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStackSizeStack->empty())[37m[39;49;00m$
  1623	[37m                          [39;49;00m{[37m[39;49;00m$
  1624	[37m                            [39;49;00m[37m// this bracket is a static array[39;49;00m$
  1625	[37m[39;49;00m$
  1626	[37m                            [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mpreviousIndentStackSize[37m [39;49;00m=[37m [39;49;00minStatementIndentStackSizeStack->back();[37m[39;49;00m$
  1627	[37m                            [39;49;00minStatementIndentStackSizeStack->pop_back();[37m[39;49;00m$
  1628	[37m                            [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(previousIndentStackSize[37m [39;49;00m<[37m [39;49;00minStatementIndentStack->size())[37m[39;49;00m$
  1629	[37m                              [39;49;00minStatementIndentStack->pop_back();[37m[39;49;00m$
  1630	[37m                            [39;49;00mparenDepth--;[37m[39;49;00m$
  1631	[37m                            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1632	[37m                              [39;49;00mshouldIndentBrackettedLine[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1633	[37m[39;49;00m$
  1634	[37m                            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!parenIndentStack->empty())[37m[39;49;00m$
  1635	[37m                              [39;49;00m{[37m[39;49;00m$
  1636	[37m                                [39;49;00m[36mint[39;49;00m[37m [39;49;00mpoppedIndent[37m [39;49;00m=[37m [39;49;00mparenIndentStack->back();[37m[39;49;00m$
  1637	[37m                                [39;49;00mparenIndentStack->pop_back();[37m[39;49;00m$
  1638	[37m                                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1639	[37m                                  [39;49;00mspaceTabCount[37m [39;49;00m=[37m [39;49;00mpoppedIndent;[37m[39;49;00m$
  1640	[37m                              [39;49;00m}[37m[39;49;00m$
  1641	[37m                          [39;49;00m}[37m[39;49;00m$
  1642	[37m                        [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1643	[37m                      [39;49;00m}[37m[39;49;00m$
  1644	[37m                  [39;49;00m}[37m[39;49;00m$
  1645	[37m[39;49;00m$
  1646	[37m                [39;49;00m[37m// this bracket is block closer...[39;49;00m$
  1647	[37m[39;49;00m$
  1648	[37m                [39;49;00m++lineClosingBlocksNum;[37m[39;49;00m$
  1649	[37m[39;49;00m$
  1650	[37m                [39;49;00m[34mif[39;49;00m(!inStatementIndentStackSizeStack->empty())[37m[39;49;00m$
  1651	[37m                  [39;49;00minStatementIndentStackSizeStack->pop_back();[37m[39;49;00m$
  1652	[37m[39;49;00m$
  1653	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!blockParenDepthStack->empty())[37m[39;49;00m$
  1654	[37m                  [39;49;00m{[37m[39;49;00m$
  1655	[37m                    [39;49;00mparenDepth[37m [39;49;00m=[37m [39;49;00mblockParenDepthStack->back();[37m[39;49;00m$
  1656	[37m                    [39;49;00mblockParenDepthStack->pop_back();[37m[39;49;00m$
  1657	[37m                    [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00mblockStatementStack->back();[37m[39;49;00m$
  1658	[37m                    [39;49;00mblockStatementStack->pop_back();[37m[39;49;00m$
  1659	[37m[39;49;00m$
  1660	[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInStatement)[37m[39;49;00m$
  1661	[37m                      [39;49;00mblockTabCount--;[37m[39;49;00m$
  1662	[37m                  [39;49;00m}[37m[39;49;00m$
  1663	[37m[39;49;00m$
  1664	[37m                [39;49;00mclosingBracketReached[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1665	[37m                [39;49;00m[36mint[39;49;00m[37m [39;49;00mheaderPlace[37m [39;49;00m=[37m [39;49;00mindexOf(*headerStack,[37m [39;49;00m&AS_OPEN_BRACKET);[37m [39;49;00m[37m// <---[39;49;00m$
  1666	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(headerPlace[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
  1667	[37m                  [39;49;00m{[37m[39;49;00m$
  1668	[37m                    [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*popped[37m [39;49;00m=[37m [39;49;00mheaderStack->back();[37m[39;49;00m$
  1669	[37m                    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(popped[37m [39;49;00m!=[37m [39;49;00m&AS_OPEN_BRACKET)[37m[39;49;00m$
  1670	[37m                      [39;49;00m{[37m[39;49;00m$
  1671	[37m                        [39;49;00mheaderStack->pop_back();[37m[39;49;00m$
  1672	[37m                        [39;49;00mpopped[37m [39;49;00m=[37m [39;49;00mheaderStack->back();[37m[39;49;00m$
  1673	[37m                      [39;49;00m}[37m[39;49;00m$
  1674	[37m                    [39;49;00mheaderStack->pop_back();[37m[39;49;00m$
  1675	[37m[39;49;00m$
  1676	[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!tempStacks->empty())[37m[39;49;00m$
  1677	[37m                      [39;49;00m{[37m[39;49;00m$
  1678	[37m                        [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m*temp[37m [39;49;00m=[37m  [39;49;00mtempStacks->back();[37m[39;49;00m$
  1679	[37m                        [39;49;00mtempStacks->pop_back();[37m[39;49;00m$
  1680	[37m                        [39;49;00m[34mdelete[39;49;00m[37m [39;49;00mtemp;[37m[39;49;00m$
  1681	[37m                      [39;49;00m}[37m[39;49;00m$
  1682	[37m                  [39;49;00m}[37m[39;49;00m$
  1683	[37m[39;49;00m$
  1684	[37m[39;49;00m$
  1685	[37m                [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m;[37m [39;49;00m[37m// needed due to cases such as '}else{', so that headers ('else' tn tih case) will be identified...[39;49;00m$
  1686	[37m              [39;49;00m}[37m[39;49;00m$
  1687	[37m[39;49;00m$
  1688	[37m            [39;49;00m[37m/*[39;49;00m$
  1689	[37m             * Create a temporary snapshot of the current block's header-list in the[39;49;00m$
  1690	[37m             * uppermost inner stack in tempStacks, and clear the headerStack up to[39;49;00m$
  1691	[37m             * the begining of the block.[39;49;00m$
  1692	[37m             * Thus, the next future statement will think it comes one indent past[39;49;00m$
  1693	[37m             * the block's '{' unless it specifically checks for a companion-header[39;49;00m$
  1694	[37m             * (such as a previous 'if' for an 'else' header) within the tempStacks,[39;49;00m$
  1695	[37m             * and recreates the temporary snapshot by manipulating the tempStacks.[39;49;00m$
  1696	[37m             */[39;49;00m[37m[39;49;00m$
  1697	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!tempStacks->back()->empty())[37m[39;49;00m$
  1698	[37m              [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(!tempStacks->back()->empty())[37m[39;49;00m$
  1699	[37m                [39;49;00mtempStacks->back()->pop_back();[37m[39;49;00m$
  1700	[37m            [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(!headerStack->empty()[37m [39;49;00m&&[37m [39;49;00mheaderStack->back()[37m [39;49;00m!=[37m [39;49;00m&AS_OPEN_BRACKET)[37m[39;49;00m$
  1701	[37m              [39;49;00m{[37m[39;49;00m$
  1702	[37m                [39;49;00mtempStacks->back()->push_back(headerStack->back());[37m[39;49;00m$
  1703	[37m                [39;49;00mheaderStack->pop_back();[37m[39;49;00m$
  1704	[37m              [39;49;00m}[37m[39;49;00m$
  1705	[37m[39;49;00m$
  1706	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(parenDepth[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1707	[37m              [39;49;00misInStatement=[36mfalse[39;49;00m;[37m[39;49;00m$
  1708	[37m[39;49;00m$
  1709	[37m            [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1710	[37m[39;49;00m$
  1711	[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1712	[37m          [39;49;00m}[37m[39;49;00m$
  1713	[37m[39;49;00m$
  1714	[37m[39;49;00m$
  1715	[37m        [39;49;00m[37m// check for preBlockStatements ONLY if not within parenthesies[39;49;00m$
  1716	[37m        [39;49;00m[37m// (otherwise 'struct XXX' statements would be wrongly interpreted...)[39;49;00m$
  1717	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(prevCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00m!isInTemplate[37m [39;49;00m&&[37m [39;49;00mparenDepth[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1718	[37m          [39;49;00m{[37m[39;49;00m$
  1719	[37m            [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*newHeader[37m [39;49;00m=[37m [39;49;00mfindHeader(line,[37m [39;49;00mi,[37m [39;49;00mpreBlockStatements);[37m[39;49;00m$
  1720	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1721	[37m              [39;49;00m{[37m[39;49;00m$
  1722	[37m                [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1723	[37m                [39;49;00moutBuffer.append(newHeader->substr([34m1[39;49;00m));[37m[39;49;00m$
  1724	[37m                [39;49;00mi[37m [39;49;00m+=[37m [39;49;00mnewHeader->length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1725	[37m                [39;49;00m[37m//if (isCStyle)[39;49;00m$
  1726	[37m                [39;49;00mheaderStack->push_back(newHeader);[37m[39;49;00m$
  1727	[37m              [39;49;00m}[37m[39;49;00m$
  1728	[37m          [39;49;00m}[37m[39;49;00m$
  1729	[37m[39;49;00m$
  1730	[37m        [39;49;00m[37m// Handle operators[39;49;00m$
  1731	[37m        [39;49;00m[37m//[39;49;00m$
  1732	[37m[39;49;00m$
  1733	[37m        [39;49;00m[37m////        // PRECHECK if a '==' or '--' or '++' operator was reached.[39;49;00m$
  1734	[37m        [39;49;00m[37m////        // If not, then register an indent IF an assignment operator was reached.[39;49;00m$
  1735	[37m        [39;49;00m[37m////        // The precheck is important, so that statements such as 'i--==2' are not recognized[39;49;00m$
  1736	[37m        [39;49;00m[37m////        // to have assignment operators (here, '-=') in them . . .[39;49;00m$
  1737	[37m[39;49;00m$
  1738	[37m        [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*foundAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1739	[37m        [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*foundNonAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1740	[37m[39;49;00m$
  1741	[37m        [39;49;00mimmediatelyPreviousAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1742	[37m[39;49;00m$
  1743	[37m        [39;49;00m[37m// Check if an operator has been reached.[39;49;00m$
  1744	[37m        [39;49;00mfoundAssignmentOp[37m [39;49;00m=[37m [39;49;00mfindHeader(line,[37m [39;49;00mi,[37m [39;49;00massignmentOperators,[37m [39;49;00m[36mfalse[39;49;00m);[37m[39;49;00m$
  1745	[37m        [39;49;00mfoundNonAssignmentOp[37m [39;49;00m=[37m [39;49;00mfindHeader(line,[37m [39;49;00mi,[37m [39;49;00mnonAssignmentOperators,[37m [39;49;00m[36mfalse[39;49;00m);[37m[39;49;00m$
  1746	[37m[39;49;00m$
  1747	[37m        [39;49;00m[37m// Since findHeader's boundry checking was not used above, it is possible[39;49;00m$
  1748	[37m        [39;49;00m[37m// that both an assignment op and a non-assignment op where found,[39;49;00m$
  1749	[37m        [39;49;00m[37m// e.g. '>>' and '>>='. If this is the case, treat the LONGER one as the[39;49;00m$
  1750	[37m        [39;49;00m[37m// found operator.[39;49;00m$
  1751	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundAssignmentOp[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00mfoundNonAssignmentOp[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1752	[37m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundAssignmentOp->length()[37m [39;49;00m<[37m [39;49;00mfoundNonAssignmentOp->length())[37m[39;49;00m$
  1753	[37m            [39;49;00mfoundAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1754	[37m          [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1755	[37m            [39;49;00mfoundNonAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  1756	[37m[39;49;00m$
  1757	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundNonAssignmentOp[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1758	[37m          [39;49;00m{[37m[39;49;00m$
  1759	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundNonAssignmentOp->length()[37m [39;49;00m>[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  1760	[37m              [39;49;00m{[37m[39;49;00m$
  1761	[37m                [39;49;00moutBuffer.append(foundNonAssignmentOp->substr([34m1[39;49;00m));[37m[39;49;00m$
  1762	[37m                [39;49;00mi[37m [39;49;00m+=[37m [39;49;00mfoundNonAssignmentOp->length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1763	[37m              [39;49;00m}[37m[39;49;00m$
  1764	[37m          [39;49;00m}[37m[39;49;00m$
  1765	[37m[39;49;00m$
  1766	[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundAssignmentOp[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1767	[37m[39;49;00m$
  1768	[37m          [39;49;00m{[37m[39;49;00m$
  1769	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundAssignmentOp->length()[37m [39;49;00m>[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
  1770	[37m              [39;49;00m{[37m[39;49;00m$
  1771	[37m                [39;49;00moutBuffer.append(foundAssignmentOp->substr([34m1[39;49;00m));[37m[39;49;00m$
  1772	[37m                [39;49;00mi[37m [39;49;00m+=[37m [39;49;00mfoundAssignmentOp->length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1773	[37m              [39;49;00m}[37m[39;49;00m$
  1774	[37m[39;49;00m$
  1775	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInOperator[37m [39;49;00m&&[37m [39;49;00m!isInTemplate)[37m[39;49;00m$
  1776	[37m              [39;49;00m{[37m[39;49;00m$
  1777	[37m                [39;49;00mregisterInStatementIndent(line,[37m [39;49;00mi,[37m [39;49;00mspaceTabCount,[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00m[36mfalse[39;49;00m);[37m[39;49;00m$
  1778	[37m                [39;49;00mimmediatelyPreviousAssignmentOp[37m [39;49;00m=[37m [39;49;00mfoundAssignmentOp;[37m[39;49;00m$
  1779	[37m                [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  1780	[37m              [39;49;00m}[37m[39;49;00m$
  1781	[37m          [39;49;00m}[37m[39;49;00m$
  1782	[37m[39;49;00m$
  1783	[37m        [39;49;00m[37m/*[39;49;00m$
  1784	[37m                immediatelyPreviousAssignmentOp = NULL;[39;49;00m$
  1785	[37m                bool isNonAssingmentOperator = false;[39;49;00m$
  1786	[37m                for (int n = 0; n < nonAssignmentOperators.size(); n++)[39;49;00m$
  1787	[37m                    if (line.COMPARE(i, nonAssignmentOperators[n]->length(), *(nonAssignmentOperators[n])) == 0)[39;49;00m$
  1788	[37m                    {[39;49;00m$
  1789	[37m                        if (nonAssignmentOperators[n]->length() > 1)[39;49;00m$
  1790	[37m                        {[39;49;00m$
  1791	[37m                            outBuffer.append(nonAssignmentOperators[n]->substr(1));[39;49;00m$
  1792	[37m                            i += nonAssignmentOperators[n]->length() - 1;[39;49;00m$
  1793	[37m                        }[39;49;00m$
  1794	[37m                        isNonAssingmentOperator = true;[39;49;00m$
  1795	[37m                        break;[39;49;00m$
  1796	[37m                    }[39;49;00m$
  1797	[37m                if (!isNonAssingmentOperator)[39;49;00m$
  1798	[37m                {[39;49;00m$
  1799	[37m                    for (int a = 0; a < assignmentOperators.size(); a++)[39;49;00m$
  1800	[37m                        if (line.COMPARE(i, assignmentOperators[a]->length(), *(assignmentOperators[a])) == 0)[39;49;00m$
  1801	[37m                        {[39;49;00m$
  1802	[37m                            if (assignmentOperators[a]->length() > 1)[39;49;00m$
  1803	[37m                            {[39;49;00m$
  1804	[37m                                outBuffer.append(assignmentOperators[a]->substr(1));[39;49;00m$
  1805	[37m                                i += assignmentOperators[a]->length() - 1;[39;49;00m$
  1806	[37m                            }[39;49;00m$
  1807	[37m         [39;49;00m$
  1808	[37m                            if (!isInOperator && !isInTemplate)[39;49;00m$
  1809	[37m                            {[39;49;00m$
  1810	[37m                                registerInStatementIndent(line, i, spaceTabCount, 0, false);[39;49;00m$
  1811	[37m                                immediatelyPreviousAssignmentOp = assignmentOperators[a];[39;49;00m$
  1812	[37m                                isInStatement = true;[39;49;00m$
  1813	[37m                            }[39;49;00m$
  1814	[37m                            break;[39;49;00m$
  1815	[37m                        }[39;49;00m$
  1816	[37m                }[39;49;00m$
  1817	[37m        */[39;49;00m[37m[39;49;00m$
  1818	[37m[39;49;00m$
  1819	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInOperator)[37m[39;49;00m$
  1820	[37m          [39;49;00misInOperator[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1821	[37m      [39;49;00m}[37m[39;49;00m$
  1822	[37m[39;49;00m$
  1823	[37m    [39;49;00m[37m// handle special cases of unindentation:[39;49;00m$
  1824	[37m[39;49;00m$
  1825	[37m    [39;49;00m[37m/*[39;49;00m$
  1826	[37m     * if '{' doesn't follow an immediately previous '{' in the headerStack[39;49;00m$
  1827	[37m     * (but rather another header such as "for" or "if", then unindent it[39;49;00m$
  1828	[37m     * by one indentation relative to its block.[39;49;00m$
  1829	[37m     */[39;49;00m[37m[39;49;00m$
  1830	[37m    [39;49;00m[37m//    cerr << endl << lineOpeningBlocksNum << " " <<  lineClosingBlocksNum << " " <<  previousLastLineHeader << endl;[39;49;00m$
  1831	[37m[39;49;00m$
  1832	[37m    [39;49;00m[37m// indent #define lines with one less tab[39;49;00m$
  1833	[37m    [39;49;00m[37m//if (isInDefine)[39;49;00m$
  1834	[37m    [39;49;00m[37m//    tabCount -= defineTabCount-1;[39;49;00m$
  1835	[37m[39;49;00m$
  1836	[37m[39;49;00m$
  1837	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!lineStartsInComment[37m[39;49;00m$
  1838	[37m        [39;49;00m&&[37m [39;49;00m!blockIndent[37m[39;49;00m$
  1839	[37m        [39;49;00m&&[37m [39;49;00moutBuffer.length()>[34m0[39;49;00m[37m[39;49;00m$
  1840	[37m        [39;49;00m&&[37m [39;49;00moutBuffer[[34m0[39;49;00m]==[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
  1841	[37m        [39;49;00m&&[37m [39;49;00m!(lineOpeningBlocksNum[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mlineOpeningBlocksNum[37m [39;49;00m==[37m [39;49;00mlineClosingBlocksNum)[37m[39;49;00m$
  1842	[37m        [39;49;00m&&[37m [39;49;00m!(headerStack->size()[37m [39;49;00m>[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(*headerStack)[headerStack->size()[34m-2[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET)[37m[39;49;00m$
  1843	[37m        [39;49;00m&&[37m [39;49;00mshouldIndentBrackettedLine)[37m[39;49;00m$
  1844	[37m      [39;49;00m--tabCount;[37m[39;49;00m$
  1845	[37m[39;49;00m$
  1846	[37m    [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!lineStartsInComment[37m[39;49;00m$
  1847	[37m             [39;49;00m&&[37m [39;49;00moutBuffer.length()>[34m0[39;49;00m[37m[39;49;00m$
  1848	[37m             [39;49;00m&&[37m [39;49;00moutBuffer[[34m0[39;49;00m]==[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
  1849	[37m             [39;49;00m&&[37m [39;49;00mshouldIndentBrackettedLine[37m [39;49;00m)[37m[39;49;00m$
  1850	[37m      [39;49;00m--tabCount;[37m[39;49;00m$
  1851	[37m[39;49;00m$
  1852	[37m    [39;49;00m[37m// correctly indent one-line-blocks...[39;49;00m$
  1853	[37m    [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!lineStartsInComment[37m[39;49;00m$
  1854	[37m             [39;49;00m&&[37m [39;49;00moutBuffer.length()>[34m0[39;49;00m[37m[39;49;00m$
  1855	[37m             [39;49;00m&&[37m [39;49;00mlineOpeningBlocksNum[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
  1856	[37m             [39;49;00m&&[37m [39;49;00mlineOpeningBlocksNum[37m [39;49;00m==[37m [39;49;00mlineClosingBlocksNum[37m[39;49;00m$
  1857	[37m             [39;49;00m&&[37m [39;49;00mpreviousLastLineHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m[39;49;00m$
  1858	[37m             [39;49;00m&&[37m [39;49;00mpreviousLastLineHeader[37m [39;49;00m!=[37m [39;49;00m&AS_OPEN_BRACKET)[37m[39;49;00m$
  1859	[37m      [39;49;00mtabCount[37m [39;49;00m-=[37m [39;49;00m[34m1[39;49;00m;[37m [39;49;00m[37m//lineOpeningBlocksNum - (blockIndent ? 1 : 0);[39;49;00m$
  1860	[37m[39;49;00m$
  1861	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(tabCount[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1862	[37m      [39;49;00mtabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  1863	[37m[39;49;00m$
  1864	[37m    [39;49;00m[37m// take care of extra bracket indentatation option...[39;49;00m$
  1865	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(bracketIndent[37m [39;49;00m&&[37m [39;49;00moutBuffer.length()>[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mshouldIndentBrackettedLine)[37m[39;49;00m$
  1866	[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(outBuffer[[34m0[39;49;00m]==[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00moutBuffer[[34m0[39;49;00m]==[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1867	[37m        [39;49;00mtabCount++;[37m[39;49;00m$
  1868	[37m[39;49;00m$
  1869	[37m[39;49;00m$
  1870	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInDefine)[37m[39;49;00m$
  1871	[37m      [39;49;00m{[37m[39;49;00m$
  1872	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(outBuffer[[34m0[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m#[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  1873	[37m          [39;49;00m{[37m[39;49;00m$
  1874	[37m            [39;49;00mstring[37m [39;49;00mpreproc[37m [39;49;00m=[37m [39;49;00mtrim(string(outBuffer.c_str()[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m));[37m[39;49;00m$
  1875	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m6[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33mdefine[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1876	[37m              [39;49;00m{[37m[39;49;00m$
  1877	[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStack->empty()[37m[39;49;00m$
  1878	[37m                    [39;49;00m&&[37m [39;49;00minStatementIndentStack->back()[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1879	[37m                  [39;49;00m{[37m[39;49;00m$
  1880	[37m                    [39;49;00mdefineTabCount[37m [39;49;00m=[37m [39;49;00mtabCount;[37m[39;49;00m$
  1881	[37m                  [39;49;00m}[37m[39;49;00m$
  1882	[37m                [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  1883	[37m                  [39;49;00m{[37m[39;49;00m$
  1884	[37m                    [39;49;00mdefineTabCount[37m [39;49;00m=[37m [39;49;00mtabCount[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1885	[37m                    [39;49;00mtabCount--;[37m[39;49;00m$
  1886	[37m                  [39;49;00m}[37m[39;49;00m$
  1887	[37m              [39;49;00m}[37m[39;49;00m$
  1888	[37m          [39;49;00m}[37m[39;49;00m$
  1889	[37m[39;49;00m$
  1890	[37m        [39;49;00mtabCount[37m [39;49;00m-=[37m [39;49;00mdefineTabCount;[37m[39;49;00m$
  1891	[37m      [39;49;00m}[37m[39;49;00m$
  1892	[37m[39;49;00m$
  1893	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(tabCount[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1894	[37m      [39;49;00mtabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  1895	[37m[39;49;00m$
  1896	[37m[39;49;00m$
  1897	[37m    [39;49;00m[37m// finally, insert indentations into begining of line[39;49;00m$
  1898	[37m[39;49;00m$
  1899	[37m    [39;49;00mprevFinalLineSpaceTabCount[37m [39;49;00m=[37m [39;49;00mspaceTabCount;[37m[39;49;00m$
  1900	[37m    [39;49;00mprevFinalLineTabCount[37m [39;49;00m=[37m [39;49;00mtabCount;[37m[39;49;00m$
  1901	[37m[39;49;00m$
  1902	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(shouldForceTabIndentation)[37m[39;49;00m$
  1903	[37m      [39;49;00m{[37m[39;49;00m$
  1904	[37m        [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00mspaceTabCount[37m [39;49;00m/[37m [39;49;00mindentLength;[37m[39;49;00m$
  1905	[37m        [39;49;00mspaceTabCount[37m [39;49;00m=[37m [39;49;00mspaceTabCount[37m [39;49;00m%[37m [39;49;00mindentLength;[37m[39;49;00m$
  1906	[37m      [39;49;00m}[37m[39;49;00m$
  1907	[37m[39;49;00m$
  1908	[37m    [39;49;00moutBuffer[37m [39;49;00m=[37m [39;49;00mpreLineWS(spaceTabCount,tabCount)[37m [39;49;00m+[37m [39;49;00moutBuffer;[37m[39;49;00m$
  1909	[37m[39;49;00m$
  1910	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lastLineHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
  1911	[37m      [39;49;00mpreviousLastLineHeader[37m [39;49;00m=[37m [39;49;00mlastLineHeader;[37m[39;49;00m$
  1912	[37m[39;49;00m$
  1913	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00moutBuffer;[37m[39;49;00m$
  1914	[37m  [39;49;00m}[37m[39;49;00m$
  1915	[37m[39;49;00m$
  1916	[37m[39;49;00m$
  1917	[37m  [39;49;00mstring[37m [39;49;00mASBeautifier::preLineWS([36mint[39;49;00m[37m [39;49;00mspaceTabCount,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mtabCount)[37m[39;49;00m$
  1918	[37m  [39;49;00m{[37m[39;49;00m$
  1919	[37m    [39;49;00mstring[37m [39;49;00mws;[37m[39;49;00m$
  1920	[37m[39;49;00m$
  1921	[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi=[34m0[39;49;00m;[37m [39;49;00mi<tabCount;[37m [39;49;00mi++)[37m[39;49;00m$
  1922	[37m      [39;49;00mws[37m [39;49;00m+=[37m [39;49;00mindentString;[37m[39;49;00m$
  1923	[37m[39;49;00m$
  1924	[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m((spaceTabCount--)[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1925	[37m      [39;49;00mws[37m [39;49;00m+=[37m [39;49;00mstring([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
  1926	[37m[39;49;00m$
  1927	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mws;[37m[39;49;00m$
  1928	[37m[39;49;00m$
  1929	[37m  [39;49;00m}[37m[39;49;00m$
  1930	[37m[39;49;00m$
  1931	[37m  [39;49;00m[37m/**[39;49;00m$
  1932	[37m   * register an in-statement indent.[39;49;00m$
  1933	[37m   */[39;49;00m[37m[39;49;00m$
  1934	[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::registerInStatementIndent([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mspaceTabCount,[37m[39;49;00m$
  1935	[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mminIndent,[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mupdateParenStack)[37m[39;49;00m$
  1936	[37m  [39;49;00m{[37m[39;49;00m$
  1937	[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00minStatementIndent;[37m[39;49;00m$
  1938	[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mremainingCharNum[37m [39;49;00m=[37m [39;49;00mline.length()[37m [39;49;00m-[37m [39;49;00mi;[37m[39;49;00m$
  1939	[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mnextNonWSChar[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1940	[37m[39;49;00m$
  1941	[37m    [39;49;00mnextNonWSChar[37m [39;49;00m=[37m [39;49;00mgetNextProgramCharDistance(line,[37m [39;49;00mi);[37m[39;49;00m$
  1942	[37m[39;49;00m$
  1943	[37m    [39;49;00m[37m// if indent is around the last char in the line, indent instead 2 spaces from the previous indent[39;49;00m$
  1944	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(nextNonWSChar[37m [39;49;00m==[37m [39;49;00mremainingCharNum)[37m[39;49;00m$
  1945	[37m      [39;49;00m{[37m[39;49;00m$
  1946	[37m        [39;49;00m[36mint[39;49;00m[37m [39;49;00mpreviousIndent[37m [39;49;00m=[37m [39;49;00mspaceTabCount;[37m[39;49;00m$
  1947	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStack->empty())[37m[39;49;00m$
  1948	[37m          [39;49;00mpreviousIndent[37m [39;49;00m=[37m [39;49;00minStatementIndentStack->back();[37m[39;49;00m$
  1949	[37m[39;49;00m$
  1950	[37m        [39;49;00minStatementIndentStack->push_back([37m/*2*/[39;49;00m[37m [39;49;00mindentLength[37m [39;49;00m+[37m [39;49;00mpreviousIndent[37m [39;49;00m);[37m[39;49;00m$
  1951	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(updateParenStack)[37m[39;49;00m$
  1952	[37m          [39;49;00mparenIndentStack->push_back([37m [39;49;00mpreviousIndent[37m [39;49;00m);[37m[39;49;00m$
  1953	[37m        [39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
  1954	[37m      [39;49;00m}[37m[39;49;00m$
  1955	[37m[39;49;00m$
  1956	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(updateParenStack)[37m[39;49;00m$
  1957	[37m      [39;49;00mparenIndentStack->push_back(i+spaceTabCount);[37m[39;49;00m$
  1958	[37m[39;49;00m$
  1959	[37m    [39;49;00minStatementIndent[37m [39;49;00m=[37m [39;49;00mi[37m [39;49;00m+[37m [39;49;00mnextNonWSChar[37m [39;49;00m+[37m [39;49;00mspaceTabCount;[37m[39;49;00m$
  1960	[37m[39;49;00m$
  1961	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m+[37m [39;49;00mnextNonWSChar[37m [39;49;00m<[37m [39;49;00mminIndent)[37m[39;49;00m$
  1962	[37m      [39;49;00minStatementIndent[37m [39;49;00m=[37m [39;49;00mminIndent[37m [39;49;00m+[37m [39;49;00mspaceTabCount;[37m[39;49;00m$
  1963	[37m[39;49;00m$
  1964	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m+[37m [39;49;00mnextNonWSChar[37m [39;49;00m>[37m [39;49;00mmaxInStatementIndent)[37m[39;49;00m$
  1965	[37m      [39;49;00minStatementIndent[37m [39;49;00m=[37m  [39;49;00mindentLength*[34m2[39;49;00m[37m [39;49;00m+[37m [39;49;00mspaceTabCount;[37m[39;49;00m$
  1966	[37m[39;49;00m$
  1967	[37m[39;49;00m$
  1968	[37m[39;49;00m$
  1969	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStack->empty()[37m [39;49;00m&&[37m[39;49;00m$
  1970	[37m        [39;49;00minStatementIndent[37m [39;49;00m<[37m [39;49;00minStatementIndentStack->back())[37m[39;49;00m$
  1971	[37m      [39;49;00minStatementIndent[37m [39;49;00m=[37m [39;49;00minStatementIndentStack->back();[37m[39;49;00m$
  1972	[37m[39;49;00m$
  1973	[37m    [39;49;00minStatementIndentStack->push_back(inStatementIndent);[37m[39;49;00m$
  1974	[37m  [39;49;00m}[37m[39;49;00m$
  1975	[37m[39;49;00m$
  1976	[37m  [39;49;00m[37m/**[39;49;00m$
  1977	[37m   * get distance to the next non-white sspace, non-comment character in the line.[39;49;00m$
  1978	[37m   * if no such character exists, return the length remaining to the end of the line.[39;49;00m$
  1979	[37m   */[39;49;00m[37m[39;49;00m$
  1980	[37m  [39;49;00m[36mint[39;49;00m[37m [39;49;00mASBeautifier::getNextProgramCharDistance([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi)[37m[39;49;00m$
  1981	[37m  [39;49;00m{[37m[39;49;00m$
  1982	[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00minComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1983	[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mremainingCharNum[37m [39;49;00m=[37m [39;49;00mline.length()[37m [39;49;00m-[37m [39;49;00mi;[37m[39;49;00m$
  1984	[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mcharDistance[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  1985	[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mch;[37m[39;49;00m$
  1986	[37m[39;49;00m$
  1987	[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(charDistance[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m [39;49;00mcharDistance[37m [39;49;00m<[37m [39;49;00mremainingCharNum;[37m [39;49;00mcharDistance++)[37m[39;49;00m$
  1988	[37m      [39;49;00m{[37m[39;49;00m$
  1989	[37m        [39;49;00mch[37m [39;49;00m=[37m [39;49;00mline[i[37m [39;49;00m+[37m [39;49;00mcharDistance];[37m[39;49;00m$
  1990	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(inComment)[37m[39;49;00m$
  1991	[37m          [39;49;00m{[37m[39;49;00m$
  1992	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.COMPARE(i[37m [39;49;00m+[37m [39;49;00mcharDistance,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_CLOSE_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  1993	[37m              [39;49;00m{[37m[39;49;00m$
  1994	[37m                [39;49;00mcharDistance++;[37m[39;49;00m$
  1995	[37m                [39;49;00minComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
  1996	[37m              [39;49;00m}[37m[39;49;00m$
  1997	[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  1998	[37m          [39;49;00m}[37m[39;49;00m$
  1999	[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isWhiteSpace(ch))[37m[39;49;00m$
  2000	[37m          [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
  2001	[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
  2002	[37m          [39;49;00m{[37m[39;49;00m$
  2003	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.COMPARE(i[37m [39;49;00m+[37m [39;49;00mcharDistance,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_OPEN_LINE_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  2004	[37m              [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mremainingCharNum;[37m[39;49;00m$
  2005	[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.COMPARE(i[37m [39;49;00m+[37m [39;49;00mcharDistance,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_OPEN_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  2006	[37m              [39;49;00m{[37m[39;49;00m$
  2007	[37m                [39;49;00mcharDistance++;[37m[39;49;00m$
  2008	[37m                [39;49;00minComment[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
  2009	[37m              [39;49;00m}[37m[39;49;00m$
  2010	[37m          [39;49;00m}[37m[39;49;00m$
  2011	[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2012	[37m          [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mcharDistance;[37m[39;49;00m$
  2013	[37m      [39;49;00m}[37m[39;49;00m$
  2014	[37m[39;49;00m$
  2015	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mcharDistance;[37m[39;49;00m$
  2016	[37m  [39;49;00m}[37m[39;49;00m$
  2017	[37m[39;49;00m$
  2018	[37m[39;49;00m$
  2019	[37m  [39;49;00m[37m/**[39;49;00m$
  2020	[37m   * check if a specific character can be used in a legal variable/method/class name[39;49;00m$
  2021	[37m   *[39;49;00m$
  2022	[37m   * @return          legality of the char.[39;49;00m$
  2023	[37m   * @param ch        the character to be checked.[39;49;00m$
  2024	[37m   */[39;49;00m[37m[39;49;00m$
  2025	[37m  [39;49;00m[36mbool[39;49;00m[37m [39;49;00mASBeautifier::isLegalNameChar([36mchar[39;49;00m[37m [39;49;00mch)[37m [39;49;00m[34mconst[39;49;00m[37m[39;49;00m$
  2026	[37m    [39;49;00m{[37m[39;49;00m$
  2027	[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m(isalnum(ch)[37m [39;49;00m[37m//(ch>='a' && ch<='z') || (ch>='A' && ch<='Z') || (ch>='0' && ch<='9') ||[39;49;00m$
  2028	[37m              [39;49;00m||[37m [39;49;00mch==[33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch==[33m'[39;49;00m[33m_[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00m(!isCStyle[37m [39;49;00m&&[37m [39;49;00mch==[33m'[39;49;00m[33m$[39;49;00m[33m'[39;49;00m)[37m [39;49;00m||[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00mch==[33m'[39;49;00m[33m~[39;49;00m[33m'[39;49;00m));[37m[39;49;00m$
  2029	[37m    [39;49;00m}[37m[39;49;00m$
  2030	[37m[39;49;00m$
  2031	[37m[39;49;00m$
  2032	[37m  [39;49;00m[37m/**[39;49;00m$
  2033	[37m   * check if a specific line position contains a header, out of several possible headers.[39;49;00m$
  2034	[37m   *[39;49;00m$
  2035	[37m   * @return    a pointer to the found header. if no header was found then return NULL.[39;49;00m$
  2036	[37m   */[39;49;00m[37m[39;49;00m$
  2037	[37m  [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*ASBeautifier::findHeader([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi,[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m&possibleHeaders,[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mcheckBoundry)[37m[39;49;00m$
  2038	[37m  [39;49;00m{[37m[39;49;00m$
  2039	[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mmaxHeaders[37m [39;49;00m=[37m [39;49;00mpossibleHeaders.size();[37m[39;49;00m$
  2040	[37m    [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*header[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2041	[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mp;[37m[39;49;00m$
  2042	[37m[39;49;00m$
  2043	[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(p=[34m0[39;49;00m;[37m [39;49;00mp[37m [39;49;00m<[37m [39;49;00mmaxHeaders;[37m [39;49;00mp++)[37m[39;49;00m$
  2044	[37m      [39;49;00m{[37m[39;49;00m$
  2045	[37m        [39;49;00mheader[37m [39;49;00m=[37m [39;49;00mpossibleHeaders[p];[37m[39;49;00m$
  2046	[37m[39;49;00m$
  2047	[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.COMPARE(i,[37m [39;49;00mheader->length(),[37m [39;49;00m*header)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  2048	[37m          [39;49;00m{[37m[39;49;00m$
  2049	[37m            [39;49;00m[37m// check that this is a header and not a part of a longer word[39;49;00m$
  2050	[37m            [39;49;00m[37m// (e.g. not at its begining, not at its middle...)[39;49;00m$
  2051	[37m[39;49;00m$
  2052	[37m            [39;49;00m[36mint[39;49;00m[37m [39;49;00mlineLength[37m [39;49;00m=[37m [39;49;00mline.length();[37m[39;49;00m$
  2053	[37m            [39;49;00m[36mint[39;49;00m[37m [39;49;00mheaderEnd[37m [39;49;00m=[37m [39;49;00mi[37m [39;49;00m+[37m [39;49;00mheader->length();[37m[39;49;00m$
  2054	[37m            [39;49;00m[36mchar[39;49;00m[37m [39;49;00mstartCh[37m [39;49;00m=[37m [39;49;00m(*header)[[34m0[39;49;00m];[37m   [39;49;00m[37m// first char of header[39;49;00m$
  2055	[37m            [39;49;00m[36mchar[39;49;00m[37m [39;49;00mendCh[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m                [39;49;00m[37m// char just after header[39;49;00m$
  2056	[37m            [39;49;00m[36mchar[39;49;00m[37m [39;49;00mprevCh[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m               [39;49;00m[37m// char just before header[39;49;00m$
  2057	[37m[39;49;00m$
  2058	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(headerEnd[37m [39;49;00m<[37m [39;49;00mlineLength)[37m[39;49;00m$
  2059	[37m              [39;49;00m{[37m[39;49;00m$
  2060	[37m                [39;49;00mendCh[37m [39;49;00m=[37m [39;49;00mline[headerEnd];[37m[39;49;00m$
  2061	[37m              [39;49;00m}[37m[39;49;00m$
  2062	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
  2063	[37m              [39;49;00m{[37m[39;49;00m$
  2064	[37m                [39;49;00mprevCh[37m [39;49;00m=[37m [39;49;00mline[i[34m-1[39;49;00m];[37m[39;49;00m$
  2065	[37m              [39;49;00m}[37m[39;49;00m$
  2066	[37m[39;49;00m$
  2067	[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!checkBoundry)[37m[39;49;00m$
  2068	[37m              [39;49;00m{[37m[39;49;00m$
  2069	[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mheader;[37m[39;49;00m$
  2070	[37m              [39;49;00m}[37m[39;49;00m$
  2071	[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(prevCh[37m [39;49;00m!=[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
  2072	[37m                     [39;49;00m&&[37m [39;49;00misLegalNameChar(startCh)[37m[39;49;00m$
  2073	[37m                     [39;49;00m&&[37m [39;49;00misLegalNameChar(prevCh))[37m[39;49;00m$
  2074	[37m              [39;49;00m{[37m[39;49;00m$
  2075	[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2076	[37m              [39;49;00m}[37m[39;49;00m$
  2077	[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(headerEnd[37m [39;49;00m>=[37m [39;49;00mlineLength[37m[39;49;00m$
  2078	[37m                     [39;49;00m||[37m [39;49;00m!isLegalNameChar(startCh)[37m[39;49;00m$
  2079	[37m                     [39;49;00m||[37m [39;49;00m!isLegalNameChar(endCh))[37m[39;49;00m$
  2080	[37m              [39;49;00m{[37m[39;49;00m$
  2081	[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mheader;[37m[39;49;00m$
  2082	[37m              [39;49;00m}[37m[39;49;00m$
  2083	[37m            [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2084	[37m              [39;49;00m{[37m[39;49;00m$
  2085	[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2086	[37m              [39;49;00m}[37m[39;49;00m$
  2087	[37m          [39;49;00m}[37m[39;49;00m$
  2088	[37m      [39;49;00m}[37m[39;49;00m$
  2089	[37m[39;49;00m$
  2090	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
  2091	[37m  [39;49;00m}[37m[39;49;00m$
  2092	[37m[39;49;00m$
  2093	[37m[39;49;00m$
  2094	[37m  [39;49;00m[37m/**[39;49;00m$
  2095	[37m   * check if a specific character can be used in a legal variable/method/class name[39;49;00m$
  2096	[37m   *[39;49;00m$
  2097	[37m   * @return          legality of the char.[39;49;00m$
  2098	[37m   * @param ch        the character to be checked.[39;49;00m$
  2099	[37m   */[39;49;00m[37m[39;49;00m$
  2100	[37m  [39;49;00m[36mbool[39;49;00m[37m [39;49;00mASBeautifier::isWhiteSpace([36mchar[39;49;00m[37m [39;49;00mch)[37m [39;49;00m[34mconst[39;49;00m[37m[39;49;00m$
  2101	[37m    [39;49;00m{[37m[39;49;00m$
  2102	[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m\t[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
  2103	[37m    [39;49;00m}[37m[39;49;00m$
  2104	[37m[39;49;00m$
  2105	[37m  [39;49;00m[37m/**[39;49;00m$
  2106	[37m   * find the index number of a string element in a container of strings[39;49;00m$
  2107	[37m   *[39;49;00m$
  2108	[37m   * @return              the index number of element in the ocntainer. -1 if element not found.[39;49;00m$
  2109	[37m   * @param container     a vector of strings.[39;49;00m$
  2110	[37m   * @param element       the element to find .[39;49;00m$
  2111	[37m   */[39;49;00m[37m[39;49;00m$
  2112	[37m  [39;49;00m[36mint[39;49;00m[37m [39;49;00mASBeautifier::indexOf(vector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m&container,[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*element)[37m[39;49;00m$
  2113	[37m  [39;49;00m{[37m[39;49;00m$
  2114	[37m    [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>::const_iterator[37m [39;49;00mwhere;[37m[39;49;00m$
  2115	[37m[39;49;00m$
  2116	[37m    [39;49;00mwhere=[37m [39;49;00mfind(container.begin(),[37m [39;49;00mcontainer.end(),[37m [39;49;00melement);[37m[39;49;00m$
  2117	[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(where[37m [39;49;00m==[37m [39;49;00mcontainer.end())[37m[39;49;00m$
  2118	[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
  2119	[37m    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
  2120	[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mwhere[37m [39;49;00m-[37m [39;49;00mcontainer.begin();[37m[39;49;00m$
  2121	[37m  [39;49;00m}[37m[39;49;00m$
  2122	[37m[39;49;00m$
  2123	[37m  [39;49;00m[37m/**[39;49;00m$
  2124	[37m   * trim removes the white space surrounding a line.[39;49;00m$
  2125	[37m   *[39;49;00m$
  2126	[37m   * @return          the trimmed line.[39;49;00m$
  2127	[37m   * @param str       the line to trim.[39;49;00m$
  2128	[37m   */[39;49;00m[37m[39;49;00m$
  2129	[37m  [39;49;00mstring[37m [39;49;00mASBeautifier::trim([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&str)[37m[39;49;00m$
  2130	[37m  [39;49;00m{[37m[39;49;00m$
  2131	[37m[39;49;00m$
  2132	[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mstart[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
  2133	[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mend[37m [39;49;00m=[37m [39;49;00mstr.length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
  2134	[37m[39;49;00m$
  2135	[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(start[37m [39;49;00m<[37m [39;49;00mend[37m [39;49;00m&&[37m [39;49;00misWhiteSpace(str[start]))[37m[39;49;00m$
  2136	[37m      [39;49;00mstart++;[37m[39;49;00m$
  2137	[37m[39;49;00m$
  2138	[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(start[37m [39;49;00m<=[37m [39;49;00mend[37m [39;49;00m&&[37m [39;49;00misWhiteSpace(str[end]))[37m[39;49;00m$
  2139	[37m      [39;49;00mend--;[37m[39;49;00m$
  2140	[37m[39;49;00m$
  2141	[37m    [39;49;00mstring[37m [39;49;00m[32mreturnStr[39;49;00m(str,[37m [39;49;00mstart,[37m [39;49;00mend+[34m1[39;49;00m-start);[37m[39;49;00m$
  2142	[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mreturnStr;[37m[39;49;00m$
  2143	[37m  [39;49;00m}[37m[39;49;00m$
  2144	[37m[39;49;00m$
  2145	[36m#[39;49;00m[36mifdef USES_NAMESPACE[39;49;00m[36m[39;49;00m$
  2146	}[37m[39;49;00m$
  2147	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  2148	[37m/*[39;49;00m$
  2149	[37m * Copyright (c) 1998,1999,2000,2001,2002 Tal Davidson. All rights reserved.[39;49;00m$
  2150	[37m *[39;49;00m$
  2151	[37m * compiler_defines.h   (1 January 1999)[39;49;00m$
  2152	[37m * by Tal Davidson (davidsont@bigfoot.com)[39;49;00m$
  2153	[37m * This file is a part of "Artistic Style" - an indentater and reformatter[39;49;00m$
  2154	[37m * of C, C++, C# and Java source files.[39;49;00m$
  2155	[37m *[39;49;00m$
  2156	[37m * The "Artistic Style" project, including all files needed to compile it,[39;49;00m$
  2157	[37m * is free software; you can redistribute it and/or use it and/or modify it[39;49;00m$
  2158	[37m * under the terms of the GNU General Public License as published [39;49;00m$
  2159	[37m * by the Free Software Foundation; either version 2 of the License, [39;49;00m$
  2160	[37m * or (at your option) any later version.[39;49;00m$
  2161	[37m *[39;49;00m$
  2162	[37m * This program is distributed in the hope that it will be useful,[39;49;00m$
  2163	[37m * but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m$
  2164	[37m * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.[39;49;00m$
  2165	[37m *[39;49;00m$
  2166	[37m * You should have received a copy of the GNU General Public[39;49;00m$
  2167	[37m * License along with this program.[39;49;00m$
  2168	[37m */[39;49;00m[37m[39;49;00m$
  2169	[37m[39;49;00m$
  2170	[37m[39;49;00m$
  2171	[36m#[39;49;00m[36mifndef ASBEAUTIFIER_H[39;49;00m[36m[39;49;00m$
  2172	[36m#[39;49;00m[36mdefine ASBEAUTIFIER_H[39;49;00m[36m[39;49;00m$
  2173	[37m[39;49;00m$
  2174	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"ASResource.h"[39;49;00m[36m[39;49;00m$
  2175	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"compiler_defines.h"[39;49;00m[36m[39;49;00m$
  2176	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"ASSourceIterator.h"[39;49;00m[36m[39;49;00m$
  2177	[37m[39;49;00m$
  2178	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<string>[39;49;00m[36m[39;49;00m$
  2179	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<vector>[39;49;00m[36m[39;49;00m$
  2180	[37m[39;49;00m$
  2181	[37m[39;49;00m$
  2182	[34musing[39;49;00m[37m [39;49;00m[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mstd[39;49;00m;[37m[39;49;00m$
  2183	[37m[39;49;00m$
  2184	[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mastyle[39;49;00m[37m[39;49;00m$
  2185	[37m  [39;49;00m{[37m[39;49;00m$
  2186	[37m[39;49;00m$
  2187	[37m  [39;49;00m[34menum[39;49;00m[37m [39;49;00m[04m[32mBracketMode[39;49;00m[37m   [39;49;00m{[37m [39;49;00mNONE_MODE,[37m [39;49;00mATTACH_MODE,[37m [39;49;00mBREAK_MODE,[37m [39;49;00mBDAC_MODE[37m [39;49;00m};[37m[39;49;00m$
  2188	[37m  [39;49;00m[34menum[39;49;00m[37m [39;49;00m[04m[32mBracketType[39;49;00m[37m   [39;49;00m{[37m [39;49;00mNULL_TYPE[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m,[37m[39;49;00m$
  2189	[37m                       [39;49;00mDEFINITION_TYPE[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m[39;49;00m$
  2190	[37m                       [39;49;00mCOMMAND_TYPE[37m [39;49;00m=[37m [39;49;00m[34m2[39;49;00m,[37m[39;49;00m$
  2191	[37m                       [39;49;00mARRAY_TYPE[37m  [39;49;00m=[37m [39;49;00m[34m4[39;49;00m,[37m[39;49;00m$
  2192	[37m                       [39;49;00mSINGLE_LINE_TYPE[37m [39;49;00m=[37m [39;49;00m[34m8[39;49;00m};[37m[39;49;00m$
  2193	[37m[39;49;00m$
  2194	[37m[39;49;00m$
  2195	[37m  [39;49;00m[34mclass[39;49;00m[37m [39;49;00m[04m[32mASBeautifier[39;49;00m[37m [39;49;00m:[37m [39;49;00m[34mprotected[39;49;00m[37m [39;49;00mASResource[37m[39;49;00m$
  2196	[37m    [39;49;00m{[37m[39;49;00m$
  2197	[37m    [39;49;00m[34mpublic[39;49;00m:[37m[39;49;00m$
  2198	[37m      [39;49;00mASBeautifier();[37m[39;49;00m$
  2199	[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00m~ASBeautifier();[37m[39;49;00m$
  2200	[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32minit[39;49;00m(ASSourceIterator*[37m [39;49;00miter);[37m [39;49;00m[37m// pointer to dynamically created iterator.[39;49;00m$
  2201	[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32minit[39;49;00m();[37m[39;49;00m$
  2202	[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00m[32mhasMoreLines[39;49;00m()[37m [39;49;00m[34mconst[39;49;00m;[37m[39;49;00m$
  2203	[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00mstring[37m [39;49;00m[32mnextLine[39;49;00m();[37m[39;49;00m$
  2204	[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00mstring[37m [39;49;00m[32mbeautify[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line);[37m[39;49;00m$
  2205	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetTabIndentation[39;49;00m([36mint[39;49;00m[37m [39;49;00mlength[37m [39;49;00m=[37m [39;49;00m[34m4[39;49;00m,[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mforceTabs[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m);[37m[39;49;00m$
  2206	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetSpaceIndentation[39;49;00m([36mint[39;49;00m[37m [39;49;00mlength[37m [39;49;00m=[37m [39;49;00m[34m4[39;49;00m);[37m[39;49;00m$
  2207	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetMaxInStatementIndentLength[39;49;00m([36mint[39;49;00m[37m [39;49;00mmax);[37m[39;49;00m$
  2208	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetMinConditionalIndentLength[39;49;00m([36mint[39;49;00m[37m [39;49;00mmin);[37m[39;49;00m$
  2209	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetClassIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2210	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetSwitchIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2211	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetCaseIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2212	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetBracketIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2213	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetBlockIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2214	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetNamespaceIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2215	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetLabelIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2216	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetCStyle[39;49;00m();[37m[39;49;00m$
  2217	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetJavaStyle[39;49;00m();[37m[39;49;00m$
  2218	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetEmptyLineFill[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2219	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetPreprocessorIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
  2220	[37m[39;49;00m$
  2221	[37m[39;49;00m$
  2222	[37m    [39;49;00m[34mprotected[39;49;00m:[37m[39;49;00m$
  2223	[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mgetNextProgramCharDistance([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi);[37m[39;49;00m$
  2224	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00m[32misLegalNameChar[39;49;00m([36mchar[39;49;00m[37m [39;49;00mch)[37m [39;49;00m[34mconst[39;49;00m;[37m[39;49;00m$
  2225	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00m[32misWhiteSpace[39;49;00m([36mchar[39;49;00m[37m [39;49;00mch)[37m [39;49;00m[34mconst[39;49;00m;[37m[39;49;00m$
  2226	[37m      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*[32mfindHeader[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi,[37m[39;49;00m$
  2227	[37m                               [39;49;00m[34mconst[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m&possibleHeaders,[37m[39;49;00m$
  2228	[37m                               [39;49;00m[36mbool[39;49;00m[37m [39;49;00mcheckBoundry[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m);[37m[39;49;00m$
  2229	[37m      [39;49;00mstring[37m [39;49;00m[32mtrim[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&str);[37m[39;49;00m$
  2230	[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mindexOf[39;49;00m(vector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m&container,[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*element);[37m[39;49;00m$
  2231	[37m[39;49;00m$
  2232	[37m    [39;49;00m[34mprivate[39;49;00m:[37m[39;49;00m$
  2233	[37m      [39;49;00mASBeautifier([34mconst[39;49;00m[37m [39;49;00mASBeautifier[37m [39;49;00m&copy);[37m[39;49;00m$
  2234	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[34moperator[39;49;00m=(ASBeautifier&);[37m [39;49;00m[37m// not to be implemented[39;49;00m$
  2235	[37m[39;49;00m$
  2236	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32minitStatic[39;49;00m();[37m[39;49;00m$
  2237	[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mregisterInStatementIndent[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mspaceTabCount,[37m[39;49;00m$
  2238	[37m                                     [39;49;00m[36mint[39;49;00m[37m [39;49;00mminIndent,[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mupdateParenStack);[37m[39;49;00m$
  2239	[37m      [39;49;00mstring[37m [39;49;00m[32mpreLineWS[39;49;00m([36mint[39;49;00m[37m [39;49;00mspaceTabCount,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mtabCount);[37m[39;49;00m$
  2240	[37m[39;49;00m$
  2241	[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mheaders;[37m[39;49;00m$
  2242	[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mnonParenHeaders;[37m[39;49;00m$
  2243	[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mpreprocessorHeaders;[37m[39;49;00m$
  2244	[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mpreBlockStatements;[37m[39;49;00m$
  2245	[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00massignmentOperators;[37m[39;49;00m$
  2246	[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mnonAssignmentOperators;[37m[39;49;00m$
  2247	[37m[39;49;00m$
  2248	[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mcalledInitStatic;[37m[39;49;00m$
  2249	[37m[39;49;00m$
  2250	[37m      [39;49;00mASSourceIterator[37m [39;49;00m*sourceIterator;[37m[39;49;00m$
  2251	[37m      [39;49;00mvector<ASBeautifier*>[37m [39;49;00m*waitingBeautifierStack;[37m[39;49;00m$
  2252	[37m      [39;49;00mvector<ASBeautifier*>[37m [39;49;00m*activeBeautifierStack;[37m[39;49;00m$
  2253	[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*waitingBeautifierStackLengthStack;[37m[39;49;00m$
  2254	[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*activeBeautifierStackLengthStack;[37m[39;49;00m$
  2255	[37m      [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m*headerStack;[37m[39;49;00m$
  2256	[37m      [39;49;00mvector<[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>*[37m [39;49;00m>[37m [39;49;00m*tempStacks;[37m[39;49;00m$
  2257	[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*blockParenDepthStack;[37m[39;49;00m$
  2258	[37m      [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m*blockStatementStack;[37m[39;49;00m$
  2259	[37m      [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m*parenStatementStack;[37m[39;49;00m$
  2260	[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*inStatementIndentStack;[37m[39;49;00m$
  2261	[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*inStatementIndentStackSizeStack;[37m[39;49;00m$
  2262	[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*parenIndentStack;[37m[39;49;00m$
  2263	[37m      [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m*bracketBlockStateStack;[37m[39;49;00m$
  2264	[37m      [39;49;00mstring[37m [39;49;00mindentString;[37m[39;49;00m$
  2265	[37m      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*currentHeader;[37m[39;49;00m$
  2266	[37m      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*previousLastLineHeader;[37m[39;49;00m$
  2267	[37m      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*immediatelyPreviousAssignmentOp;[37m[39;49;00m$
  2268	[37m      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*probationHeader;[37m[39;49;00m$
  2269	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInQuote;[37m[39;49;00m$
  2270	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInComment;[37m[39;49;00m$
  2271	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInCase;[37m[39;49;00m$
  2272	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInQuestion;[37m[39;49;00m$
  2273	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInStatement;[37m[39;49;00m$
  2274	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInHeader;[37m[39;49;00m$
  2275	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misCStyle;[37m[39;49;00m$
  2276	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInOperator;[37m[39;49;00m$
  2277	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInTemplate;[37m[39;49;00m$
  2278	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInConst;[37m[39;49;00m$
  2279	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInDefine;[37m[39;49;00m$
  2280	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInDefineDefinition;[37m[39;49;00m$
  2281	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mclassIndent;[37m[39;49;00m$
  2282	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInClassHeader;[37m[39;49;00m$
  2283	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInClassHeaderTab;[37m[39;49;00m$
  2284	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mswitchIndent;[37m[39;49;00m$
  2285	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mcaseIndent;[37m[39;49;00m$
  2286	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mnamespaceIndent;[37m[39;49;00m$
  2287	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mbracketIndent;[37m[39;49;00m$
  2288	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mblockIndent;[37m[39;49;00m$
  2289	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mlabelIndent;[37m[39;49;00m$
  2290	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mpreprocessorIndent;[37m[39;49;00m$
  2291	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInConditional;[37m[39;49;00m$
  2292	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misMinimalConditinalIndentSet;[37m[39;49;00m$
  2293	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mshouldForceTabIndentation;[37m[39;49;00m$
  2294	[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mminConditionalIndent;[37m[39;49;00m$
  2295	[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mparenDepth;[37m[39;49;00m$
  2296	[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mindentLength;[37m[39;49;00m$
  2297	[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mblockTabCount;[37m[39;49;00m$
  2298	[37m      [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mleadingWhiteSpaces;[37m[39;49;00m$
  2299	[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mmaxInStatementIndent;[37m[39;49;00m$
  2300	[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mtemplateDepth;[37m[39;49;00m$
  2301	[37m      [39;49;00m[36mchar[39;49;00m[37m [39;49;00mquoteChar;[37m[39;49;00m$
  2302	[37m      [39;49;00m[36mchar[39;49;00m[37m [39;49;00mprevNonSpaceCh;[37m[39;49;00m$
  2303	[37m      [39;49;00m[36mchar[39;49;00m[37m [39;49;00mcurrentNonSpaceCh;[37m[39;49;00m$
  2304	[37m      [39;49;00m[36mchar[39;49;00m[37m [39;49;00mcurrentNonLegalCh;[37m[39;49;00m$
  2305	[37m      [39;49;00m[36mchar[39;49;00m[37m [39;49;00mprevNonLegalCh;[37m[39;49;00m$
  2306	[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mprevFinalLineSpaceTabCount;[37m[39;49;00m$
  2307	[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mprevFinalLineTabCount;[37m[39;49;00m$
  2308	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00memptyLineFill;[37m[39;49;00m$
  2309	[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mbackslashEndsPrevLine;[37m[39;49;00m$
  2310	[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mdefineTabCount;[37m[39;49;00m$
  2311	[37m    [39;49;00m};[37m[39;49;00m$
  2312	}[37m[39;49;00m$
  2313	[37m[39;49;00m$
  2314	[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
  2315	[37m/*[39;49;00m$
  2316	[37m * Copyright (c) 1998,1999,2000,2001,2002 Tal Davidson. All rights reserved.[39;49;00m$
  2317	[37m *[39;49;00m$
  2318	[37m * ASFormatter.cpp[39;49;00m$
  2319	[37m * by Tal Davidson (davidsont@bigfoot.com)[39;49;00m$
  2320	[37m * This file is a part of "Artistic Style" - an indentater and reformatter[39;49;00m$
  2321	[37m * of C, C++, C# and Java source files.[39;49;00m$
  2322	[37m *[39;49;00m$
  2323	[37m * The "Artistic Style" project, including all files needed to compile it,[39;49;00m$
  2324	[37m * is free software; you can redistribute it and/or use it and/or modify it[39;49;00m$
  2325	[37m * under the terms of the GNU General Public License as published [39;49;00m$
  2326	[37m * by the Free Software Foundation; either version 2 of the License, [39;49;00m$
  2327	[37m * or (at your option) any later version.[39;49;00m$
  2328	[37m *[39;49;00m$
  2329	[37m * This program is distributed in the hope that it will be useful,[39;49;00m$
  2330	[37m * but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m$
  2331	[37m * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.[39;49;00m$
  2332	[37m *[39;49;00m$
  2333	[37m * You should have received a copy of the GNU General Public[39;49;00m$
  2334	[37m * License along with this program.[39;49;00m$
  2335	[37m *[39;49;00m$
  2336	[37m *[39;49;00m$
  2337	[37m * Patches:[39;49;00m$
  2338	[37m * 26 November 1998 - Richard Bullington -[39;49;00m$
  2339	[37m *        A correction of line-breaking in headers following '}',[39;49;00m$
  2340	[37m [39;49;00m$
  2341	[37m *        was created using a variation of a  patch by Richard Bullington.[39;49;00m$
  2342	[37m * 08 May 2004[39;49;00m$
  2343	[37m *        applied   ASFormatter450670.patch.bz2, ASFormatter.cpp.patch.bz2,[39;49;00m$
  2344	[37m *                  patch1_ssvb_patch.tar.gz[39;49;00m$
  2345	[37m */[39;49;00m[37m[39;49;00m$
  2346	[37m[39;49;00m$
  2347	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"compiler_defines.h"[39;49;00m[36m[39;49;00m$
  2348	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"ASFormatter.h"[39;49;00m[36m[39;49;00m$
  2349	[37m[39;49;00m$
  2350	[37m[39;49;00m$
  2351	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<string>[39;49;00m[36m[39;49;00m$
  2352	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<cctype>[39;49;00m[36m[39;49;00m$
  2353	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<vector>[39;49;00m[36m[39;49;00m$
  2354	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<algorithm>[39;49;00m[36m[39;49;00m$
  2355	[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<iostream>[39;49;00m[36m[39;49;00m$
  2356	[37m[39;49;00m$
  2357	[37m[39;49;00m$
  2358	[36m#[39;49;00m[36mdefine INIT_CONTAINER(container, value)     {if ( (container) != NULL ) delete (container); (container) = (value); }[39;49;00m[36m[39;49;00m$
  2359	[36m#[39;49;00m[36mdefine DELETE_CONTAINER(container)          {if ( (container) != NULL ) delete (container) ; }[39;49;00m[36m[39;49;00m$
  2360	[36m#[39;49;00m[36mdefine IS_A(a,b)                            ( ((a) & (b)) == (b))[39;49;00m[36m[39;49;00m$
  2361	[36m#[39;49;00m[36mifdef USES_NAMESPACE[39;49;00m[36m[39;49;00m$
  2362	[34musing[39;49;00m[37m [39;49;00m[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mstd[39;49;00m;$
