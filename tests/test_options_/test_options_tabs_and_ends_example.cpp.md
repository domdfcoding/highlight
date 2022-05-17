[37m/***************************************************************************[39;49;00m$
[37m                    ansigenerator.cpp  -  description[39;49;00m$
[37m                             -------------------[39;49;00m$
[37m    begin                : Jul 5 2004[39;49;00m$
[37m    copyright            : (C) 2004 by André Simon[39;49;00m$
[37m    email                : andre.simon1@gmx.de[39;49;00m$
[37m ***************************************************************************/[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m/***************************************************************************[39;49;00m$
[37m *                                                                         *[39;49;00m$
[37m *   This program is free software; you can redistribute it and/or modify  *[39;49;00m$
[37m *   it under the terms of the GNU General Public License as published by  *[39;49;00m$
[37m *   the Free Software Foundation; either version 2 of the License, or     *[39;49;00m$
[37m *   (at your option) any later version.                                   *[39;49;00m$
[37m *                                                                         *[39;49;00m$
[37m ***************************************************************************/[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"ansigenerator.h"[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[34musing[39;49;00m[37m [39;49;00m[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mstd[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mhighlight[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
string[37m  [39;49;00m[32mAnsiGenerator::getOpenTag[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring&font,[37m[39;49;00m$
[37m                                  [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring&fgCol,[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring&bgCol)[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mostringstream[37m [39;49;00ms;[37m[39;49;00m$
[37m    [39;49;00ms[37m  [39;49;00m<<[37m [39;49;00m[33m"[39;49;00m[33m\033[39;49;00m[33m[[39;49;00m[33m"[39;49;00m<<font;[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!fgCol.empty())[37m[39;49;00m$
[37m        [39;49;00ms<<[33m"[39;49;00m[33m;[39;49;00m[33m"[39;49;00m<<fgCol;[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!bgCol.empty())[37m[39;49;00m$
[37m        [39;49;00ms<<[33m"[39;49;00m[33m;[39;49;00m[33m"[39;49;00m<<bgCol;[37m[39;49;00m$
[37m    [39;49;00ms[37m [39;49;00m<<[37m [39;49;00m[33m"[39;49;00m[33mm[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[34mreturn[39;49;00m[37m  [39;49;00ms.str();[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
AnsiGenerator::AnsiGenerator([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&colourTheme)[37m[39;49;00m$
[37m        [39;49;00m:[37m [39;49;00mCodeGenerator(colourTheme)[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mstyleTagOpen.push_back([33m"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m31[39;49;00m[33m"[39;49;00m));[37m [39;49;00m[37m//str[39;49;00m$
[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m34[39;49;00m[33m"[39;49;00m));[37m//number[39;49;00m$
[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m34[39;49;00m[33m"[39;49;00m));[37m//sl comment[39;49;00m$
[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m34[39;49;00m[33m"[39;49;00m));[37m//ml comment[39;49;00m$
[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m35[39;49;00m[33m"[39;49;00m));[37m//escapeChar[39;49;00m$
[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m35[39;49;00m[33m"[39;49;00m));[37m//directive[39;49;00m$
[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m01[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m31[39;49;00m[33m"[39;49;00m));[37m//directive string[39;49;00m$
[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m30[39;49;00m[33m"[39;49;00m));[37m//linenum[39;49;00m$
[37m    [39;49;00mstyleTagOpen.push_back(getOpenTag([33m"[39;49;00m[33m01[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m));[37m//symbol[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mstyleTagClose.push_back([33m"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi=[34m1[39;49;00m;i<NUMBER_BUILTIN_STYLES;[37m [39;49;00mi++)[37m [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00mstyleTagClose.push_back([33m"[39;49;00m[33m\033[39;49;00m[33m[m[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00m}[37m[39;49;00m$
[37m    [39;49;00mnewLineTag[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mspacer[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
AnsiGenerator::AnsiGenerator()[37m [39;49;00m{}[37m[39;49;00m$
AnsiGenerator::~AnsiGenerator()[37m [39;49;00m{}[37m[39;49;00m$
[37m[39;49;00m$
string[37m [39;49;00mAnsiGenerator::getHeader([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&[37m [39;49;00mtitle)[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mstring();[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36mvoid[39;49;00m[37m [39;49;00mAnsiGenerator::printBody()[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mprocessRootState();[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
string[37m [39;49;00mAnsiGenerator::getFooter()[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mstring();[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
string[37m [39;49;00mAnsiGenerator::maskCharacter([36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00mc)[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mstring[37m [39;49;00mm;[37m[39;49;00m$
[37m    [39;49;00mm+=c;[37m[39;49;00m$
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mm;[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
string[37m [39;49;00mAnsiGenerator::getMatchingOpenTag([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mstyleID)[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m(styleID)?getOpenTag([33m"[39;49;00m[33m01[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m32[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m"[39;49;00m):getOpenTag([33m"[39;49;00m[33m00[39;49;00m[33m"[39;49;00m,[37m [39;49;00m[33m"[39;49;00m[33m33[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
string[37m [39;49;00mAnsiGenerator::getMatchingCloseTag([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mstyleID)[37m [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[33m"[39;49;00m[33m\033[39;49;00m[33m[m[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
}[37m[39;49;00m$
[37m/***************************************************************************[39;49;00m$
[37m                         ansicode.h  -  description[39;49;00m$
[37m                             -------------------[39;49;00m$
[37m    begin                : Jul 5 2004[39;49;00m$
[37m    copyright            : (C) 2004 by Andre Simon[39;49;00m$
[37m    email                : andre.simon1@gmx.de[39;49;00m$
[37m ***************************************************************************/[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m/***************************************************************************[39;49;00m$
[37m *                                                                         *[39;49;00m$
[37m *   This program is free software; you can redistribute it and/or modify  *[39;49;00m$
[37m *   it under the terms of the GNU General Public License as published by  *[39;49;00m$
[37m *   the Free Software Foundation; either version 2 of the License, or     *[39;49;00m$
[37m *   (at your option) any later version.                                   *[39;49;00m$
[37m *                                                                         *[39;49;00m$
[37m ***************************************************************************/[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifndef ANSIGENERATOR_H[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine ANSIGENERATOR_H[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<iostream>[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<fstream>[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<string>[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<sstream>[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"codegenerator.h"[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"charcodes.h"[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"version.h"[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mhighlight[39;49;00m[37m [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m/**[39;49;00m$
[37m   \brief This class generates ANSI escape sequences.[39;49;00m$
[37m[39;49;00m$
[37m   It contains information about the resulting document structure (document[39;49;00m$
[37m   header and footer), the colour system, white space handling and text[39;49;00m$
[37m   formatting attributes.[39;49;00m$
[37m[39;49;00m$
[37m* @author Andre Simon[39;49;00m$
[37m*/[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[34mclass[39;49;00m[37m [39;49;00m[04m[32mAnsiGenerator[39;49;00m[37m [39;49;00m:[37m [39;49;00m[34mpublic[39;49;00m[37m [39;49;00mhighlight::CodeGenerator[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m  [39;49;00m[34mpublic[39;49;00m:[37m[39;49;00m$
[37m[39;49;00m$
[37m   [39;49;00m[37m/** Constructor[39;49;00m$
[37m     \param colourTheme Name of Colour theme to use[39;49;00m$
[37m    */[39;49;00m[37m[39;49;00m$
[37m    [39;49;00mAnsiGenerator([37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&colourTheme);[37m[39;49;00m$
[37m    [39;49;00mAnsiGenerator();[37m[39;49;00m$
[37m    [39;49;00m~AnsiGenerator();[37m[39;49;00m$
[37m[39;49;00m$
[37m   [39;49;00m[37m/** prints document header[39;49;00m$
[37m       \param  title Title of the document[39;49;00m$
[37m    */[39;49;00m[37m[39;49;00m$
[37m    [39;49;00mstring[37m [39;49;00m[32mgetHeader[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&[37m [39;49;00mtitle);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m/** Prints document footer*/[39;49;00m[37m[39;49;00m$
[37m    [39;49;00mstring[37m [39;49;00m[32mgetFooter[39;49;00m();[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m/** Prints document body*/[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mprintBody[39;49;00m();[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[34mprivate[39;49;00m:[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m/** \return escaped character*/[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00mstring[37m [39;49;00mmaskCharacter([36munsigned[39;49;00m[37m [39;49;00m[36mchar[39;49;00m[37m [39;49;00m);[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m/** gibt ANSI-"Tags" zurueck (Farbindex+bold+kursiv)*/[39;49;00m[37m[39;49;00m$
[37m    [39;49;00mstring[37m [39;49;00m[32mgetOpenTag[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring&font,[37m[39;49;00m$
[37m                      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring&fgCol,[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring&bgCol=[33m"[39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mstring[37m [39;49;00m[32mgetMatchingOpenTag[39;49;00m([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mstyleID);[37m[39;49;00m$
[37m    [39;49;00mstring[37m [39;49;00m[32mgetMatchingCloseTag[39;49;00m([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mstyleID);[37m[39;49;00m$
[37m  [39;49;00m};[37m[39;49;00m$
[37m[39;49;00m$
}[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m/*[39;49;00m$
[37m * Copyright (c) 1998,1999,2000,2001,2002 Tal Davidson. All rights reserved.[39;49;00m$
[37m *[39;49;00m$
[37m * ASBeautifier.cpp[39;49;00m$
[37m * by Tal Davidson (davidsont@bigfoot.com)[39;49;00m$
[37m * This file is a part of "Artistic Style" - an indentater and reformatter[39;49;00m$
[37m * of C, C, C# and Java source files.[39;49;00m$
[37m *[39;49;00m$
[37m * The "Artistic Style" project, including all files needed to compile it,[39;49;00m$
[37m * is free software; you can redistribute it and/or use it and/or modify it[39;49;00m$
[37m * under the terms of the GNU General Public License as published [39;49;00m$
[37m * by the Free Software Foundation; either version 2 of the License, [39;49;00m$
[37m * or (at your option) any later version.[39;49;00m$
[37m *[39;49;00m$
[37m * This program is distributed in the hope that it will be useful,[39;49;00m$
[37m * but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m$
[37m * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.[39;49;00m$
[37m *[39;49;00m$
[37m * You should have received a copy of the GNU General Public[39;49;00m$
[37m * License along with this program.[39;49;00m$
[37m *[39;49;00m$
[37m * Patches:[39;49;00m$
[37m * 18 March 1999 - Brian Rampel -[39;49;00m$
[37m *       Fixed inverse insertion of spaces vs. tabs when in -t mode.[39;49;00m$
[37m * 08 may 2004 [39;49;00m$
[37m *       applied ASBeautifier.cpp.BITFIELD.patch.bz2[39;49;00m$
[37m */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"compiler_defines.h"[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"ASBeautifier.h"[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<vector>[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<string>[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<cctype>[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<algorithm>[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<iostream>[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mdefine INIT_CONTAINER(container, value)     {if ( (container) != NULL ) delete (container); (container) = (value); }[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine DELETE_CONTAINER(container)          {if ( (container) != NULL ) delete (container) ; }[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifdef USES_NAMESPACE[39;49;00m[36m[39;49;00m$
[34musing[39;49;00m[37m [39;49;00m[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mstd[39;49;00m;[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifdef USES_NAMESPACE[39;49;00m[36m[39;49;00m$
[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mastyle[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[36mbool[39;49;00m[37m [39;49;00mASBeautifier::calledInitStatic[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mASBeautifier::headers;[37m[39;49;00m$
[37m  [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mASBeautifier::nonParenHeaders;[37m[39;49;00m$
[37m  [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mASBeautifier::preBlockStatements;[37m[39;49;00m$
[37m  [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mASBeautifier::assignmentOperators;[37m[39;49;00m$
[37m  [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mASBeautifier::nonAssignmentOperators;[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/*[39;49;00m$
[37m   * initialize the static vars[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mASBeautifier::initStatic[39;49;00m()[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(calledInitStatic)[37m[39;49;00m$
[37m      [39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mcalledInitStatic[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_IF);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_ELSE);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_FOR);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_WHILE);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_DO);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_TRY);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_CATCH);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_FINALLY);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_SYNCHRONIZED);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_SWITCH);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_CASE);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_DEFAULT);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_FOREACH);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_LOCK);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_UNSAFE);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_FIXED);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_GET);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_SET);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_ADD);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_REMOVE);[37m[39;49;00m$
[37m    [39;49;00m[37m//headers.push_back(&AS_PUBLIC);[39;49;00m$
[37m    [39;49;00m[37m//headers.push_back(&AS_PRIVATE);[39;49;00m$
[37m    [39;49;00m[37m//headers.push_back(&AS_PROTECTED);[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m//headers.push_back(&AS_OPERATOR);[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_TEMPLATE);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_CONST);[37m[39;49;00m$
[37m    [39;49;00m[37m/**/[39;49;00m[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_STATIC);[37m[39;49;00m$
[37m    [39;49;00mheaders.push_back(&AS_EXTERN);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_ELSE);[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_DO);[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_TRY);[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_FINALLY);[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_STATIC);[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_CONST);[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_EXTERN);[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_CASE);[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_DEFAULT);[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_UNSAFE);[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_GET);[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_SET);[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_ADD);[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_REMOVE);[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_PUBLIC);[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_PRIVATE);[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_PROTECTED);[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_TEMPLATE);[37m[39;49;00m$
[37m    [39;49;00mnonParenHeaders.push_back(&AS_CONST);[37m[39;49;00m$
[37m    [39;49;00m[37m///    nonParenHeaders.push_back(&AS_ASM);[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mpreBlockStatements.push_back(&AS_CLASS);[37m[39;49;00m$
[37m    [39;49;00mpreBlockStatements.push_back(&AS_STRUCT);[37m[39;49;00m$
[37m    [39;49;00mpreBlockStatements.push_back(&AS_UNION);[37m[39;49;00m$
[37m    [39;49;00mpreBlockStatements.push_back(&AS_INTERFACE);[37m[39;49;00m$
[37m    [39;49;00mpreBlockStatements.push_back(&AS_NAMESPACE);[37m[39;49;00m$
[37m    [39;49;00mpreBlockStatements.push_back(&AS_THROWS);[37m[39;49;00m$
[37m    [39;49;00mpreBlockStatements.push_back(&AS_EXTERN);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00massignmentOperators.push_back(&AS_ASSIGN);[37m[39;49;00m$
[37m    [39;49;00massignmentOperators.push_back(&AS_PLUS_ASSIGN);[37m[39;49;00m$
[37m    [39;49;00massignmentOperators.push_back(&AS_MINUS_ASSIGN);[37m[39;49;00m$
[37m    [39;49;00massignmentOperators.push_back(&AS_MULT_ASSIGN);[37m[39;49;00m$
[37m    [39;49;00massignmentOperators.push_back(&AS_DIV_ASSIGN);[37m[39;49;00m$
[37m    [39;49;00massignmentOperators.push_back(&AS_MOD_ASSIGN);[37m[39;49;00m$
[37m    [39;49;00massignmentOperators.push_back(&AS_OR_ASSIGN);[37m[39;49;00m$
[37m    [39;49;00massignmentOperators.push_back(&AS_AND_ASSIGN);[37m[39;49;00m$
[37m    [39;49;00massignmentOperators.push_back(&AS_XOR_ASSIGN);[37m[39;49;00m$
[37m    [39;49;00massignmentOperators.push_back(&AS_GR_GR_GR_ASSIGN);[37m[39;49;00m$
[37m    [39;49;00massignmentOperators.push_back(&AS_GR_GR_ASSIGN);[37m[39;49;00m$
[37m    [39;49;00massignmentOperators.push_back(&AS_LS_LS_LS_ASSIGN);[37m[39;49;00m$
[37m    [39;49;00massignmentOperators.push_back(&AS_LS_LS_ASSIGN);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00massignmentOperators.push_back(&AS_RETURN);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_EQUAL);[37m[39;49;00m$
[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_PLUS_PLUS);[37m[39;49;00m$
[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_MINUS_MINUS);[37m[39;49;00m$
[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_NOT_EQUAL);[37m[39;49;00m$
[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_GR_EQUAL);[37m[39;49;00m$
[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_GR_GR_GR);[37m[39;49;00m$
[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_GR_GR);[37m[39;49;00m$
[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_LS_EQUAL);[37m[39;49;00m$
[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_LS_LS_LS);[37m[39;49;00m$
[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_LS_LS);[37m[39;49;00m$
[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_ARROW);[37m[39;49;00m$
[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_AND);[37m[39;49;00m$
[37m    [39;49;00mnonAssignmentOperators.push_back(&AS_OR);[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * ASBeautifier's constructor[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00mASBeautifier::ASBeautifier()[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00minitStatic();[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mwaitingBeautifierStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mactiveBeautifierStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mwaitingBeautifierStackLengthStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mactiveBeautifierStackLengthStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mheaderStack[37m  [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mtempStacks[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mblockParenDepthStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mblockStatementStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mparenStatementStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mbracketBlockStateStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00minStatementIndentStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00minStatementIndentStackSizeStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mparenIndentStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00msourceIterator[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00misMinimalConditinalIndentSet[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mshouldForceTabIndentation[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00msetSpaceIndentation([34m4[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00msetMaxInStatementIndentLength([34m40[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00msetClassIndent([36mfalse[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00msetSwitchIndent([36mfalse[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00msetCaseIndent([36mfalse[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00msetBlockIndent([36mfalse[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00msetBracketIndent([36mfalse[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00msetNamespaceIndent([36mfalse[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00msetLabelIndent([36mfalse[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00msetEmptyLineFill([36mfalse[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00msetCStyle();[37m[39;49;00m$
[37m    [39;49;00msetPreprocessorIndent([36mfalse[39;49;00m);[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00mASBeautifier::ASBeautifier([34mconst[39;49;00m[37m [39;49;00mASBeautifier[37m [39;49;00m&other)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mwaitingBeautifierStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mactiveBeautifierStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mwaitingBeautifierStackLengthStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mactiveBeautifierStackLengthStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mheaderStack[37m  [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>;[37m[39;49;00m$
[37m    [39;49;00m*headerStack[37m [39;49;00m=[37m [39;49;00m*other.headerStack;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mtempStacks[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>*[37m [39;49;00m>;[37m[39;49;00m$
[37m    [39;49;00mvector<[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>*[37m [39;49;00m>::iterator[37m [39;49;00miter;[37m[39;49;00m$
[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(iter[37m [39;49;00m=[37m [39;49;00mother.tempStacks->begin();[37m[39;49;00m$
[37m         [39;49;00miter[37m [39;49;00m!=[37m [39;49;00mother.tempStacks->end();[37m[39;49;00m$
[37m         [39;49;00m++iter)[37m[39;49;00m$
[37m      [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m*newVec[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>;[37m[39;49;00m$
[37m        [39;49;00m*newVec[37m [39;49;00m=[37m [39;49;00m**iter;[37m[39;49;00m$
[37m        [39;49;00mtempStacks->push_back(newVec);[37m[39;49;00m$
[37m      [39;49;00m}[37m[39;49;00m$
[37m    [39;49;00mblockParenDepthStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>;[37m[39;49;00m$
[37m    [39;49;00m*blockParenDepthStack[37m [39;49;00m=[37m [39;49;00m*other.blockParenDepthStack;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mblockStatementStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>;[37m[39;49;00m$
[37m    [39;49;00m*blockStatementStack[37m [39;49;00m=[37m [39;49;00m*other.blockStatementStack;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mparenStatementStack[37m [39;49;00m=[37m  [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>;[37m[39;49;00m$
[37m    [39;49;00m*parenStatementStack[37m [39;49;00m=[37m [39;49;00m*other.parenStatementStack;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mbracketBlockStateStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>;[37m[39;49;00m$
[37m    [39;49;00m*bracketBlockStateStack[37m [39;49;00m=[37m [39;49;00m*other.bracketBlockStateStack;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00minStatementIndentStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>;[37m[39;49;00m$
[37m    [39;49;00m*inStatementIndentStack[37m [39;49;00m=[37m [39;49;00m*other.inStatementIndentStack;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00minStatementIndentStackSizeStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>;[37m[39;49;00m$
[37m    [39;49;00m*inStatementIndentStackSizeStack[37m [39;49;00m=[37m [39;49;00m*other.inStatementIndentStackSizeStack;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mparenIndentStack[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>;[37m[39;49;00m$
[37m    [39;49;00m*parenIndentStack[37m [39;49;00m=[37m [39;49;00m*other.parenIndentStack;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00msourceIterator[37m [39;49;00m=[37m [39;49;00mother.sourceIterator;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mindentString[37m [39;49;00m=[37m [39;49;00mother.indentString;[37m[39;49;00m$
[37m    [39;49;00mcurrentHeader[37m [39;49;00m=[37m [39;49;00mother.currentHeader;[37m[39;49;00m$
[37m    [39;49;00mpreviousLastLineHeader[37m [39;49;00m=[37m [39;49;00mother.previousLastLineHeader;[37m[39;49;00m$
[37m    [39;49;00mimmediatelyPreviousAssignmentOp[37m [39;49;00m=[37m [39;49;00mother.immediatelyPreviousAssignmentOp;[37m[39;49;00m$
[37m    [39;49;00misInQuote[37m [39;49;00m=[37m [39;49;00mother.isInQuote;[37m[39;49;00m$
[37m    [39;49;00misInComment[37m [39;49;00m=[37m [39;49;00mother.isInComment;[37m[39;49;00m$
[37m    [39;49;00misInCase[37m [39;49;00m=[37m [39;49;00mother.isInCase;[37m[39;49;00m$
[37m    [39;49;00misInQuestion[37m [39;49;00m=[37m [39;49;00mother.isInQuestion;[37m[39;49;00m$
[37m    [39;49;00misInStatement[37m [39;49;00m=other.[37m [39;49;00misInStatement;[37m[39;49;00m$
[37m    [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00mother.isInHeader;[37m[39;49;00m$
[37m    [39;49;00misCStyle[37m [39;49;00m=[37m [39;49;00mother.isCStyle;[37m[39;49;00m$
[37m    [39;49;00misInOperator[37m [39;49;00m=[37m [39;49;00mother.isInOperator;[37m[39;49;00m$
[37m    [39;49;00misInTemplate[37m [39;49;00m=[37m [39;49;00mother.isInTemplate;[37m[39;49;00m$
[37m    [39;49;00misInConst[37m [39;49;00m=[37m [39;49;00mother.isInConst;[37m[39;49;00m$
[37m    [39;49;00mclassIndent[37m [39;49;00m=[37m [39;49;00mother.classIndent;[37m[39;49;00m$
[37m    [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00mother.isInClassHeader;[37m[39;49;00m$
[37m    [39;49;00misInClassHeaderTab[37m [39;49;00m=[37m [39;49;00mother.isInClassHeaderTab;[37m[39;49;00m$
[37m    [39;49;00mswitchIndent[37m [39;49;00m=[37m [39;49;00mother.switchIndent;[37m[39;49;00m$
[37m    [39;49;00mcaseIndent[37m [39;49;00m=[37m [39;49;00mother.caseIndent;[37m[39;49;00m$
[37m    [39;49;00mnamespaceIndent[37m [39;49;00m=[37m [39;49;00mother.namespaceIndent;[37m[39;49;00m$
[37m    [39;49;00mbracketIndent[37m [39;49;00m=[37m [39;49;00mother.bracketIndent;[37m[39;49;00m$
[37m    [39;49;00mblockIndent[37m [39;49;00m=[37m [39;49;00mother.blockIndent;[37m[39;49;00m$
[37m    [39;49;00mlabelIndent[37m [39;49;00m=[37m [39;49;00mother.labelIndent;[37m[39;49;00m$
[37m    [39;49;00mpreprocessorIndent[37m [39;49;00m=[37m [39;49;00mother.preprocessorIndent;[37m[39;49;00m$
[37m    [39;49;00mparenDepth[37m [39;49;00m=[37m [39;49;00mother.parenDepth;[37m[39;49;00m$
[37m    [39;49;00mindentLength[37m [39;49;00m=[37m [39;49;00mother.indentLength;[37m[39;49;00m$
[37m    [39;49;00mblockTabCount[37m [39;49;00m=[37m [39;49;00mother.blockTabCount;[37m[39;49;00m$
[37m    [39;49;00mleadingWhiteSpaces[37m [39;49;00m=[37m [39;49;00mother.leadingWhiteSpaces;[37m[39;49;00m$
[37m    [39;49;00mmaxInStatementIndent[37m [39;49;00m=[37m [39;49;00mother.maxInStatementIndent;[37m[39;49;00m$
[37m    [39;49;00mtemplateDepth[37m [39;49;00m=[37m [39;49;00mother.templateDepth;[37m[39;49;00m$
[37m    [39;49;00mquoteChar[37m [39;49;00m=[37m [39;49;00mother.quoteChar;[37m[39;49;00m$
[37m    [39;49;00mprevNonSpaceCh[37m [39;49;00m=[37m [39;49;00mother.prevNonSpaceCh;[37m[39;49;00m$
[37m    [39;49;00mcurrentNonSpaceCh[37m [39;49;00m=[37m [39;49;00mother.currentNonSpaceCh;[37m[39;49;00m$
[37m    [39;49;00mcurrentNonLegalCh[37m [39;49;00m=[37m [39;49;00mother.currentNonLegalCh;[37m[39;49;00m$
[37m    [39;49;00mprevNonLegalCh[37m [39;49;00m=[37m [39;49;00mother.prevNonLegalCh;[37m[39;49;00m$
[37m    [39;49;00misInConditional[37m [39;49;00m=[37m [39;49;00mother.isInConditional;[37m[39;49;00m$
[37m    [39;49;00mminConditionalIndent[37m [39;49;00m=[37m [39;49;00mother.minConditionalIndent;[37m[39;49;00m$
[37m    [39;49;00mprevFinalLineSpaceTabCount[37m [39;49;00m=[37m [39;49;00mother.prevFinalLineSpaceTabCount;[37m[39;49;00m$
[37m    [39;49;00mprevFinalLineTabCount[37m [39;49;00m=[37m [39;49;00mother.prevFinalLineTabCount;[37m[39;49;00m$
[37m    [39;49;00memptyLineFill[37m [39;49;00m=[37m [39;49;00mother.emptyLineFill;[37m[39;49;00m$
[37m    [39;49;00mprobationHeader[37m [39;49;00m=[37m [39;49;00mother.probationHeader;[37m[39;49;00m$
[37m    [39;49;00misInDefine[37m [39;49;00m=[37m [39;49;00mother.isInDefine;[37m[39;49;00m$
[37m    [39;49;00misInDefineDefinition[37m [39;49;00m=[37m [39;49;00mother.isInDefineDefinition;[37m[39;49;00m$
[37m    [39;49;00mbackslashEndsPrevLine[37m [39;49;00m=[37m [39;49;00mother.backslashEndsPrevLine;[37m[39;49;00m$
[37m    [39;49;00mdefineTabCount[37m [39;49;00m=[37m [39;49;00mother.defineTabCount;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * ASBeautifier's destructor[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00mASBeautifier::~ASBeautifier()[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mheaderStack[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mtempStacks[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mblockParenDepthStack[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mblockStatementStack[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mparenStatementStack[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mbracketBlockStateStack[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00minStatementIndentStack[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00minStatementIndentStackSizeStack[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mDELETE_CONTAINER([37m [39;49;00mparenIndentStack[37m [39;49;00m);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m// DELETE_CONTAINER( sourceIterator );[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * initialize the ASBeautifier.[39;49;00m$
[37m   *[39;49;00m$
[37m   * init() should be called every time a ABeautifier object is to start[39;49;00m$
[37m   * beautifying a NEW source file.[39;49;00m$
[37m   * init() recieves a pointer to a DYNAMICALLY CREATED ASSourceIterator object[39;49;00m$
[37m   * that will be used to iterate through the source code. This object will be[39;49;00m$
[37m   * deleted during the ASBeautifier's destruction, and thus should not be[39;49;00m$
[37m   * deleted elsewhere.[39;49;00m$
[37m   *[39;49;00m$
[37m   * @param iter     a pointer to the DYNAMICALLY CREATED ASSourceIterator object.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::init(ASSourceIterator[37m [39;49;00m*iter)[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00msourceIterator[37m [39;49;00m=[37m [39;49;00miter;[37m[39;49;00m$
[37m    [39;49;00minit();[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * initialize the ASBeautifier.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::init()[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mwaitingBeautifierStack,[37m  [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<ASBeautifier*>[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mactiveBeautifierStack,[37m  [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<ASBeautifier*>[37m [39;49;00m);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mwaitingBeautifierStackLengthStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mactiveBeautifierStackLengthStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mheaderStack,[37m  [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mtempStacks,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>*[37m [39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mtempStacks->push_back([34mnew[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mblockParenDepthStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mblockStatementStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mparenStatementStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mbracketBlockStateStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mbracketBlockStateStack->push_back([36mtrue[39;49;00m);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00minStatementIndentStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00minStatementIndentStackSizeStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
[37m    [39;49;00minStatementIndentStackSizeStack->push_back([34m0[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mINIT_CONTAINER([37m [39;49;00mparenIndentStack,[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mimmediatelyPreviousAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mpreviousLastLineHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00misInQuote[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00misInComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00misInCase[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00misInQuestion[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00misInClassHeaderTab[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00misInOperator[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00misInTemplate[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00misInConst[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00misInConditional[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mtemplateDepth[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mparenDepth=[34m0[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mblockTabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mleadingWhiteSpaces[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mprevNonSpaceCh[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mcurrentNonSpaceCh[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mprevNonLegalCh[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mcurrentNonLegalCh[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mprevFinalLineSpaceTabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mprevFinalLineTabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mprobationHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mbackslashEndsPrevLine[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00misInDefine[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00misInDefineDefinition[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mdefineTabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * set indentation style to ANSI C/C++.  [39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setCStyle()[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00misCStyle[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * set indentation style to Java / K&R.  [39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setJavaStyle()[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00misCStyle[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * indent using one tab per indentation[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setTabIndentation([36mint[39;49;00m[37m [39;49;00mlength,[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mforceTabs)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mindentString[37m [39;49;00m=[37m [39;49;00m[33m"[39;49;00m[33m\t[39;49;00m[33m"[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00mindentLength[37m [39;49;00m=[37m [39;49;00mlength;[37m[39;49;00m$
[37m    [39;49;00mshouldForceTabIndentation[37m [39;49;00m=[37m [39;49;00mforceTabs;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isMinimalConditinalIndentSet)[37m[39;49;00m$
[37m      [39;49;00mminConditionalIndent[37m [39;49;00m=[37m [39;49;00mindentLength[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   [39;49;00m$
[37m   * indent using a number of spaces per indentation.[39;49;00m$
[37m   *[39;49;00m$
[37m   * @param   length     number of spaces per indent.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setSpaceIndentation([36mint[39;49;00m[37m [39;49;00mlength)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mindentString=string(length,[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00mindentLength[37m [39;49;00m=[37m [39;49;00mlength;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isMinimalConditinalIndentSet)[37m[39;49;00m$
[37m      [39;49;00mminConditionalIndent[37m [39;49;00m=[37m [39;49;00mindentLength[37m [39;49;00m*[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * set the maximum indentation between two lines in a multi-line statement.[39;49;00m$
[37m   *[39;49;00m$
[37m   * @param   max     maximum indentation length.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setMaxInStatementIndentLength([36mint[39;49;00m[37m [39;49;00mmax)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mmaxInStatementIndent[37m [39;49;00m=[37m [39;49;00mmax;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * set the minimum indentation between two lines in a multi-line condition.[39;49;00m$
[37m   *[39;49;00m$
[37m   * @param   min     minimal indentation length.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setMinConditionalIndentLength([36mint[39;49;00m[37m [39;49;00mmin)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mminConditionalIndent[37m [39;49;00m=[37m [39;49;00mmin;[37m[39;49;00m$
[37m    [39;49;00misMinimalConditinalIndentSet[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * set the state of the bracket indentation option. If true, brackets will [39;49;00m$
[37m   * be indented one additional indent.[39;49;00m$
[37m   *[39;49;00m$
[37m   * @param   state             state of option.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setBracketIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mbracketIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * set the state of the block indentation option. If true, entire blocks [39;49;00m$
[37m   * will be indented one additional indent, similar to the GNU indent style.[39;49;00m$
[37m   *[39;49;00m$
[37m   * @param   state             state of option.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setBlockIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(state)[37m[39;49;00m$
[37m      [39;49;00msetBracketIndent([36mfalse[39;49;00m);[37m [39;49;00m[37m// so that we don't have both bracket and block indent[39;49;00m$
[37m    [39;49;00mblockIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * set the state of the class indentation option. If true, C++ class[39;49;00m$
[37m   * definitions will be indented one additional indent.[39;49;00m$
[37m   *[39;49;00m$
[37m   * @param   state             state of option.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setClassIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mclassIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * set the state of the switch indentation option. If true, blocks of 'switch' [39;49;00m$
[37m   * statements will be indented one additional indent.[39;49;00m$
[37m   *[39;49;00m$
[37m   * @param   state             state of option.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setSwitchIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mswitchIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * set the state of the case indentation option. If true, lines of 'case' [39;49;00m$
[37m   * statements will be indented one additional indent.[39;49;00m$
[37m   *[39;49;00m$
[37m   * @param   state             state of option.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setCaseIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mcaseIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * set the state of the namespace indentation option. [39;49;00m$
[37m   * If true, blocks of 'namespace' statements will be indented one [39;49;00m$
[37m   * additional indent. Otherwise, NO indentation will be added.[39;49;00m$
[37m   *[39;49;00m$
[37m   * @param   state             state of option.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setNamespaceIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mnamespaceIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * set the state of the label indentation option. [39;49;00m$
[37m   * If true, labels will be indented one indent LESS than the[39;49;00m$
[37m   * current indentation level.[39;49;00m$
[37m   * If false, labels will be flushed to the left with NO[39;49;00m$
[37m   * indent at all.[39;49;00m$
[37m   *[39;49;00m$
[37m   * @param   state             state of option.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setLabelIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mlabelIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * set the state of the preprocessor indentation option. [39;49;00m$
[37m   * If true, multiline #define statements will be indented.[39;49;00m$
[37m   *[39;49;00m$
[37m   * @param   state             state of option.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setPreprocessorIndent([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mpreprocessorIndent[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * set the state of the empty line fill option. [39;49;00m$
[37m   * If true, empty lines will be filled with the whitespace.[39;49;00m$
[37m   * of their previous lines.[39;49;00m$
[37m   * If false, these lines will remain empty.[39;49;00m$
[37m   *[39;49;00m$
[37m   * @param   state             state of option.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::setEmptyLineFill([36mbool[39;49;00m[37m [39;49;00mstate)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00memptyLineFill[37m [39;49;00m=[37m [39;49;00mstate;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * check if there are any indented lines ready to be read by nextLine()[39;49;00m$
[37m   *[39;49;00m$
[37m   * @return    are there any indented lines ready?[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mbool[39;49;00m[37m [39;49;00mASBeautifier::hasMoreLines()[37m [39;49;00m[34mconst[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m{[37m[39;49;00m$
[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00msourceIterator->hasMoreLines();[37m[39;49;00m$
[37m    [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * get the next indented line.[39;49;00m$
[37m   *[39;49;00m$
[37m   * @return    indented line.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00mstring[37m [39;49;00mASBeautifier::nextLine()[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mbeautify(sourceIterator->nextLine());[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * beautify a line of source code.[39;49;00m$
[37m   * every line of source code in a source code file should be sent[39;49;00m$
[37m   * one after the other to the beautify method.[39;49;00m$
[37m   *[39;49;00m$
[37m   * @return      the indented line.[39;49;00m$
[37m   * @param originalLine       the original unindented line.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00mstring[37m [39;49;00mASBeautifier::beautify([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&originalLine)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mstring[37m [39;49;00mline;[37m[39;49;00m$
[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInLineComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00mlineStartsInComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInClass[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInSwitch[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00misImmediatelyAfterConst[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00misSpecialChar[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36mchar[39;49;00m[37m [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[36mchar[39;49;00m[37m [39;49;00mprevCh;[37m[39;49;00m$
[37m    [39;49;00mstring[37m [39;49;00moutBuffer;[37m [39;49;00m[37m// the newly idented line is bufferd here[39;49;00m$
[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mtabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*lastLineHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00mclosingBracketReached[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mspaceTabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[36mchar[39;49;00m[37m [39;49;00mtempCh;[37m[39;49;00m$
[37m    [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mheaderStackSize[37m [39;49;00m=[37m [39;49;00mheaderStack->size();[37m[39;49;00m$
[37m    [39;49;00m[37m//bool isLineInStatement = isInStatement;[39;49;00m$
[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00mshouldIndentBrackettedLine[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mlineOpeningBlocksNum[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mlineClosingBlocksNum[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00mpreviousLineProbation[37m [39;49;00m=[37m [39;49;00m(probationHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mcurrentHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mlineStartsInComment[37m [39;49;00m=[37m [39;49;00misInComment;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m// handle and remove white spaces around the line:[39;49;00m$
[37m    [39;49;00m[37m// If not in comment, first find out size of white space before line,[39;49;00m$
[37m    [39;49;00m[37m// so that possible comments starting in the line continue in[39;49;00m$
[37m    [39;49;00m[37m// relation to the preliminary white-space.[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInComment)[37m[39;49;00m$
[37m      [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00mleadingWhiteSpaces[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m        [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(leadingWhiteSpaces<originalLine.length()[37m [39;49;00m&&[37m [39;49;00moriginalLine[leadingWhiteSpaces][37m [39;49;00m<=[37m [39;49;00m[34m0x20[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00mleadingWhiteSpaces++;[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00mline[37m [39;49;00m=[37m [39;49;00mtrim(originalLine);[37m[39;49;00m$
[37m      [39;49;00m}[37m[39;49;00m$
[37m    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mtrimSize;[37m[39;49;00m$
[37m        [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(trimSize=[34m0[39;49;00m;[37m[39;49;00m$
[37m             [39;49;00mtrimSize[37m [39;49;00m<[37m [39;49;00moriginalLine.length()[37m [39;49;00m&&[37m [39;49;00mtrimSize<leadingWhiteSpaces[37m [39;49;00m&&[37m [39;49;00moriginalLine[trimSize][37m [39;49;00m<=[37m [39;49;00m[34m0x20[39;49;00m[37m [39;49;00m;[37m[39;49;00m$
[37m             [39;49;00mtrimSize++)[37m[39;49;00m$
[37m          [39;49;00m;[37m[39;49;00m$
[37m        [39;49;00mline[37m [39;49;00m=[37m [39;49;00moriginalLine.substr(trimSize);[37m[39;49;00m$
[37m      [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.length()[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(emptyLineFill)[37m[39;49;00m$
[37m          [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mpreLineWS(prevFinalLineSpaceTabCount,[37m [39;49;00mprevFinalLineTabCount);[37m[39;49;00m$
[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mline;[37m[39;49;00m$
[37m      [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m// handle preprocessor commands[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00m!isInComment[37m [39;49;00m&&[37m [39;49;00m(line[[34m0[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m#[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mbackslashEndsPrevLine))[37m[39;49;00m$
[37m      [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line[[34m0[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m#[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00mstring[37m [39;49;00mpreproc[37m [39;49;00m=[37m [39;49;00mtrim(string(line.c_str()[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m));[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[37m// When finding a multi-lined #define statement, the original beautifier[39;49;00m$
[37m            [39;49;00m[37m// 1. sets its isInDefineDefinition flag[39;49;00m$
[37m            [39;49;00m[37m// 2. clones a new beautifier that will be used for the actual indentation[39;49;00m$
[37m            [39;49;00m[37m//    of the #define. This clone is put into the activeBeautifierStack in order[39;49;00m$
[37m            [39;49;00m[37m//    to be called for the actual indentation.[39;49;00m$
[37m            [39;49;00m[37m// The original beautifier will have isInDefineDefinition = true, isInDefine = false[39;49;00m$
[37m            [39;49;00m[37m// The cloned beautifier will have   isInDefineDefinition = true, isInDefine = true[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preprocessorIndent[37m [39;49;00m&&[37m [39;49;00mpreproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m6[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33mdefine[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m  [39;49;00mline[line.length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInDefineDefinition)[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00mASBeautifier[37m [39;49;00m*defineBeautifier;[37m[39;49;00m$
[37m[39;49;00m$
[37m                    [39;49;00m[37m// this is the original beautifier[39;49;00m$
[37m                    [39;49;00misInDefineDefinition[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m                    [39;49;00m[37m// push a new beautifier into the active stack[39;49;00m$
[37m                    [39;49;00m[37m// this breautifier will be used for the indentation of this define[39;49;00m$
[37m                    [39;49;00mdefineBeautifier[37m [39;49;00m=[37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mASBeautifier(*[34mthis[39;49;00m);[37m[39;49;00m$
[37m                    [39;49;00m[37m//defineBeautifier->init();[39;49;00m$
[37m                    [39;49;00m[37m//defineBeautifier->isInDefineDefinition = true;[39;49;00m$
[37m                    [39;49;00m[37m//defineBeautifier->beautify("");[39;49;00m$
[37m                    [39;49;00mactiveBeautifierStack->push_back(defineBeautifier);[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m                [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00m[37m// the is the cloned beautifier that is in charge of indenting the #define.[39;49;00m$
[37m                    [39;49;00misInDefine[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33mif[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m[37m// push a new beautifier into the stack[39;49;00m$
[37m                [39;49;00mwaitingBeautifierStackLengthStack->push_back(waitingBeautifierStack->size());[37m[39;49;00m$
[37m                [39;49;00mactiveBeautifierStackLengthStack->push_back(activeBeautifierStack->size());[37m[39;49;00m$
[37m                [39;49;00mwaitingBeautifierStack->push_back([34mnew[39;49;00m[37m [39;49;00mASBeautifier(*[34mthis[39;49;00m));[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m4[39;49;00m[37m/*2*/[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33melse[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!waitingBeautifierStack->empty())[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00m[37m// MOVE current waiting beautifier to active stack.[39;49;00m$
[37m                    [39;49;00mactiveBeautifierStack->push_back(waitingBeautifierStack->back());[37m[39;49;00m$
[37m                    [39;49;00mwaitingBeautifierStack->pop_back();[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m4[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33melif[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!waitingBeautifierStack->empty())[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00m[37m// append a COPY current waiting beautifier to active stack, WITHOUT deleting the original.[39;49;00m$
[37m                    [39;49;00mactiveBeautifierStack->push_back([37m [39;49;00m[34mnew[39;49;00m[37m [39;49;00mASBeautifier([37m [39;49;00m*(waitingBeautifierStack->back())[37m [39;49;00m)[37m [39;49;00m);[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m5[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33mendif[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mstackLength;[37m[39;49;00m$
[37m                [39;49;00mASBeautifier[37m [39;49;00m*beautifier;[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!waitingBeautifierStackLengthStack->empty())[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00mstackLength[37m [39;49;00m=[37m [39;49;00mwaitingBeautifierStackLengthStack->back();[37m[39;49;00m$
[37m                    [39;49;00mwaitingBeautifierStackLengthStack->pop_back();[37m[39;49;00m$
[37m                    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(waitingBeautifierStack->size()[37m [39;49;00m>[37m [39;49;00mstackLength)[37m[39;49;00m$
[37m                      [39;49;00m{[37m[39;49;00m$
[37m                        [39;49;00mbeautifier[37m [39;49;00m=[37m [39;49;00mwaitingBeautifierStack->back();[37m[39;49;00m$
[37m                        [39;49;00mwaitingBeautifierStack->pop_back();[37m[39;49;00m$
[37m                        [39;49;00m[34mdelete[39;49;00m[37m [39;49;00mbeautifier;[37m[39;49;00m$
[37m                      [39;49;00m}[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!activeBeautifierStackLengthStack->empty())[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00mstackLength[37m [39;49;00m=[37m [39;49;00mactiveBeautifierStackLengthStack->back();[37m[39;49;00m$
[37m                    [39;49;00mactiveBeautifierStackLengthStack->pop_back();[37m[39;49;00m$
[37m                    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(activeBeautifierStack->size()[37m [39;49;00m>[37m [39;49;00mstackLength)[37m[39;49;00m$
[37m                      [39;49;00m{[37m[39;49;00m$
[37m                        [39;49;00mbeautifier[37m [39;49;00m=[37m [39;49;00mactiveBeautifierStack->back();[37m[39;49;00m$
[37m                        [39;49;00mactiveBeautifierStack->pop_back();[37m[39;49;00m$
[37m                        [39;49;00m[34mdelete[39;49;00m[37m [39;49;00mbeautifier;[37m[39;49;00m$
[37m                      [39;49;00m}[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m// check if the last char is a backslash[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m(line.length()[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00mbackslashEndsPrevLine[37m [39;49;00m=[37m [39;49;00m(line[line.length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m          [39;49;00mbackslashEndsPrevLine[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m// check if this line ends a multi-line #define[39;49;00m$
[37m        [39;49;00m[37m// if so, use the #define's cloned beautifier for the line's indentation[39;49;00m$
[37m        [39;49;00m[37m// and then remove it from the active beautifier stack and delete it.[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!backslashEndsPrevLine[37m [39;49;00m&&[37m [39;49;00misInDefineDefinition[37m [39;49;00m&&[37m [39;49;00m!isInDefine)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00mstring[37m [39;49;00mbeautifiedLine;[37m[39;49;00m$
[37m            [39;49;00mASBeautifier[37m [39;49;00m*defineBeautifier;[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00misInDefineDefinition[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m            [39;49;00mdefineBeautifier[37m [39;49;00m=[37m [39;49;00mactiveBeautifierStack->back();[37m[39;49;00m$
[37m            [39;49;00mactiveBeautifierStack->pop_back();[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00mbeautifiedLine[37m [39;49;00m=[37m [39;49;00mdefineBeautifier->beautify(line);[37m[39;49;00m$
[37m            [39;49;00m[34mdelete[39;49;00m[37m [39;49;00mdefineBeautifier;[37m[39;49;00m$
[37m            [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mbeautifiedLine;[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m// unless this is a multi-line #define, return this precompiler line as is.[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInDefine[37m [39;49;00m&&[37m [39;49;00m!isInDefineDefinition)[37m[39;49;00m$
[37m          [39;49;00m[34mreturn[39;49;00m[37m [39;49;00moriginalLine;[37m[39;49;00m$
[37m      [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m// if there exists any worker beautifier in the activeBeautifierStack,[39;49;00m$
[37m    [39;49;00m[37m// then use it instead of me to indent the current line.[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInDefine[37m [39;49;00m&&[37m [39;49;00mactiveBeautifierStack[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00m!activeBeautifierStack->empty())[37m[39;49;00m$
[37m      [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mactiveBeautifierStack->back()->beautify(line);[37m[39;49;00m$
[37m      [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m// calculate preliminary indentation based on data from past lines[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStack->empty())[37m[39;49;00m$
[37m      [39;49;00mspaceTabCount[37m [39;49;00m=[37m [39;49;00minStatementIndentStack->back();[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(i=[34m0[39;49;00m;[37m [39;49;00mi<headerStackSize;[37m [39;49;00mi++)[37m[39;49;00m$
[37m      [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00misInClass[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(blockIndent[37m [39;49;00m||[37m [39;49;00m(!(i>[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(*headerStack)[i[34m-1[39;49;00m][37m [39;49;00m!=[37m [39;49;00m&AS_OPEN_BRACKET[37m[39;49;00m$
[37m                              [39;49;00m&&[37m [39;49;00m(*headerStack)[i][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET)))[37m[39;49;00m$
[37m          [39;49;00m++tabCount;[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00m!namespaceIndent[37m [39;49;00m&&[37m [39;49;00mi[37m [39;49;00m>=[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m&&[37m [39;49;00m(*headerStack)[i[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_NAMESPACE[37m[39;49;00m$
[37m            [39;49;00m&&[37m [39;49;00m(*headerStack)[i][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET)[37m[39;49;00m$
[37m          [39;49;00m--tabCount;[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00mi[37m [39;49;00m>=[37m [39;49;00m[34m1[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m&&[37m [39;49;00m(*headerStack)[i[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_CLASS[37m[39;49;00m$
[37m            [39;49;00m&&[37m [39;49;00m(*headerStack)[i][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET[37m [39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(classIndent)[37m[39;49;00m$
[37m              [39;49;00m++tabCount;[37m[39;49;00m$
[37m            [39;49;00misInClass[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m// is the switchIndent option is on, indent switch statements an additional indent.[39;49;00m$
[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(switchIndent[37m [39;49;00m&&[37m [39;49;00mi[37m [39;49;00m>[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m&&[37m[39;49;00m$
[37m                 [39;49;00m(*headerStack)[i[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_SWITCH[37m [39;49;00m&&[37m[39;49;00m$
[37m                 [39;49;00m(*headerStack)[i][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET[37m[39;49;00m$
[37m                [39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00m++tabCount;[37m[39;49;00m$
[37m            [39;49;00misInSwitch[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m      [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!lineStartsInComment[37m[39;49;00m$
[37m        [39;49;00m&&[37m [39;49;00misCStyle[37m[39;49;00m$
[37m        [39;49;00m&&[37m [39;49;00misInClass[37m[39;49;00m$
[37m        [39;49;00m&&[37m [39;49;00mclassIndent[37m[39;49;00m$
[37m        [39;49;00m&&[37m [39;49;00mheaderStackSize[37m [39;49;00m>=[37m [39;49;00m[34m2[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m&&(*headerStack)[headerStackSize[34m-2[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_CLASS[37m[39;49;00m$
[37m        [39;49;00m&&[37m [39;49;00m(*headerStack)[headerStackSize[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET[37m[39;49;00m$
[37m        [39;49;00m&&[37m [39;49;00mline[[34m0[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m--tabCount;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!lineStartsInComment[37m[39;49;00m$
[37m             [39;49;00m&&[37m [39;49;00misInSwitch[37m[39;49;00m$
[37m             [39;49;00m&&[37m [39;49;00mswitchIndent[37m[39;49;00m$
[37m             [39;49;00m&&[37m [39;49;00mheaderStackSize[37m [39;49;00m>=[37m [39;49;00m[34m2[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m&&[37m [39;49;00m(*headerStack)[headerStackSize[34m-2[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_SWITCH[37m[39;49;00m$
[37m             [39;49;00m&&[37m [39;49;00m(*headerStack)[headerStackSize[34m-1[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET[37m[39;49;00m$
[37m             [39;49;00m&&[37m [39;49;00mline[[34m0[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m--tabCount;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInClassHeader)[37m[39;49;00m$
[37m      [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00misInClassHeaderTab[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m        [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m$
[37m      [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInConditional)[37m[39;49;00m$
[37m      [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00m--tabCount;[37m[39;49;00m$
[37m      [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m// parse characters in the current line.[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(i=[34m0[39;49;00m;[37m [39;49;00mi<line.length();[37m [39;49;00mi++)[37m[39;49;00m$
[37m      [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00mtempCh[37m [39;49;00m=[37m [39;49;00mline[i];[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00mprevCh[37m [39;49;00m=[37m [39;49;00mch;[37m[39;49;00m$
[37m        [39;49;00mch[37m [39;49;00m=[37m [39;49;00mtempCh;[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00mch);[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isWhiteSpace(ch))[37m[39;49;00m$
[37m          [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m// handle special characters (i.e. backslash+character such as \n, \t, ...)[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isSpecialChar)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00misSpecialChar[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00mline.COMPARE(i,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
[37m            [39;49;00mi++;[37m[39;49;00m$
[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00mch==[33m'[39;49;00m[33m\\[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00misSpecialChar[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m// handle quotes (such as 'x' and "Hello Dolly")[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00m(ch==[33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch==[33m'[39;49;00m[33m\'[39;49;00m[33m'[39;49;00m))[37m[39;49;00m$
[37m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInQuote)[37m[39;49;00m$
[37m            [39;49;00m{[37m[39;49;00m$
[37m              [39;49;00mquoteChar[37m [39;49;00m=[37m [39;49;00mch;[37m[39;49;00m$
[37m              [39;49;00misInQuote[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m            [39;49;00m}[37m[39;49;00m$
[37m          [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(quoteChar[37m [39;49;00m==[37m [39;49;00mch)[37m[39;49;00m$
[37m            [39;49;00m{[37m[39;49;00m$
[37m              [39;49;00misInQuote[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m              [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m              [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m            [39;49;00m}[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInQuote)[37m[39;49;00m$
[37m          [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m// handle comments[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m!(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00mline.COMPARE(i,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_OPEN_LINE_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00misInLineComment[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m            [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
[37m            [39;49;00mi++;[37m[39;49;00m$
[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m!(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00mline.COMPARE(i,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_OPEN_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00misInComment[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m            [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33m*[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
[37m            [39;49;00mi++;[37m[39;49;00m$
[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m(isInComment[37m [39;49;00m||[37m [39;49;00misInLineComment)[37m [39;49;00m&&[37m [39;49;00mline.COMPARE(i,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_CLOSE_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00misInComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m            [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
[37m            [39;49;00mi++;[37m[39;49;00m$
[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInComment||isInLineComment)[37m[39;49;00m$
[37m          [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m// if we have reached this far then we are NOT in a comment or string of special character...[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(probationHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m((probationHeader[37m [39;49;00m==[37m [39;49;00m&AS_STATIC[37m [39;49;00m||[37m [39;49;00mprobationHeader[37m [39;49;00m==[37m [39;49;00m&AS_CONST)[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m                 [39;49;00m||[37m [39;49;00m(probationHeader[37m [39;49;00m==[37m [39;49;00m&AS_SYNCHRONIZED[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m))[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m[37m// insert the probation header as a new header[39;49;00m$
[37m                [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m                [39;49;00mheaderStack->push_back(probationHeader);[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[37m// handle the specific probation header[39;49;00m$
[37m                [39;49;00misInConditional[37m [39;49;00m=[37m [39;49;00m(probationHeader[37m [39;49;00m==[37m [39;49;00m&AS_SYNCHRONIZED);[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(probationHeader[37m [39;49;00m==[37m [39;49;00m&AS_CONST)[37m[39;49;00m$
[37m                  [39;49;00misImmediatelyAfterConst[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m                [39;49;00m[37m//  isInConst = true;[39;49;00m$
[37m                [39;49;00m[37m/* TODO:[39;49;00m$
[37m                 * There is actually no more need for the global isInConst variable.[39;49;00m$
[37m                               * The only reason for checking const is to see if there is a const[39;49;00m$
[37m                 * immediately before an open-bracket.[39;49;00m$
[37m                 * Since CONST is now put into probation and is checked during itspost-char,[39;49;00m$
[37m                 * isImmediatelyAfterConst can be set by its own...[39;49;00m$
[37m                 */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m                [39;49;00m[37m// if the probation comes from the previous line, then indent by 1 tab count.[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(previousLineProbation[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m                  [39;49;00mtabCount++;[37m[39;49;00m$
[37m                [39;49;00mpreviousLineProbation[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[37m// dismiss the probation header[39;49;00m$
[37m            [39;49;00mprobationHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00mprevNonSpaceCh[37m [39;49;00m=[37m [39;49;00mcurrentNonSpaceCh;[37m[39;49;00m$
[37m        [39;49;00mcurrentNonSpaceCh[37m [39;49;00m=[37m [39;49;00mch;[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isLegalNameChar(ch)[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m!=[37m [39;49;00m[33m'[39;49;00m[33m,[39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m!=[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m[37m [39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00mprevNonLegalCh[37m [39;49;00m=[37m [39;49;00mcurrentNonLegalCh;[37m[39;49;00m$
[37m            [39;49;00mcurrentNonLegalCh[37m [39;49;00m=[37m [39;49;00mch;[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m//if (isInConst)[39;49;00m$
[37m        [39;49;00m[37m//{[39;49;00m$
[37m        [39;49;00m[37m//    isInConst = false;[39;49;00m$
[37m        [39;49;00m[37m//    isImmediatelyAfterConst = true;[39;49;00m$
[37m        [39;49;00m[37m//}[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInHeader)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m            [39;49;00mcurrentHeader[37m [39;49;00m=[37m [39;49;00mheaderStack->back();[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m          [39;49;00mcurrentHeader[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00misInTemplate[37m[39;49;00m$
[37m            [39;49;00m&&[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m<[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m>[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m            [39;49;00m&&[37m  [39;49;00mfindHeader(line,[37m [39;49;00mi,[37m [39;49;00mnonAssignmentOperators)[37m [39;49;00m==[37m [39;49;00m[36mNULL[39;49;00m)[37m [39;49;00m[37m//;[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m<[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m++templateDepth;[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m>[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(--templateDepth[37m [39;49;00m<=[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInTemplate)[37m[39;49;00m$
[37m                      [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
[37m                    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m                      [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33mt[39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
[37m                    [39;49;00misInTemplate[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m                    [39;49;00mtemplateDepth[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m// handle parenthesies[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m[[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m][39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m[[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(parenDepth[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00mparenStatementStack->push_back(isInStatement);[37m[39;49;00m$
[37m                    [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m                [39;49;00mparenDepth++;[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00minStatementIndentStackSizeStack->push_back(inStatementIndentStack->size());[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(currentHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m                  [39;49;00mregisterInStatementIndent(line,[37m [39;49;00mi,[37m [39;49;00mspaceTabCount,[37m [39;49;00mminConditionalIndent[37m/*indentLength*2*/[39;49;00m,[37m [39;49;00m[36mtrue[39;49;00m);[37m[39;49;00m$
[37m                [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m                  [39;49;00mregisterInStatementIndent(line,[37m [39;49;00mi,[37m [39;49;00mspaceTabCount,[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00m[36mtrue[39;49;00m);[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m][39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00mparenDepth--;[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(parenDepth[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00mparenStatementStack->back();[37m[39;49;00m$
[37m                    [39;49;00mparenStatementStack->pop_back();[37m[39;49;00m$
[37m                    [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m                    [39;49;00misInConditional[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStackSizeStack->empty())[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mpreviousIndentStackSize[37m [39;49;00m=[37m [39;49;00minStatementIndentStackSizeStack->back();[37m[39;49;00m$
[37m                    [39;49;00minStatementIndentStackSizeStack->pop_back();[37m[39;49;00m$
[37m                    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(previousIndentStackSize[37m [39;49;00m<[37m [39;49;00minStatementIndentStack->size())[37m[39;49;00m$
[37m                      [39;49;00minStatementIndentStack->pop_back();[37m[39;49;00m$
[37m[39;49;00m$
[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!parenIndentStack->empty())[37m[39;49;00m$
[37m                      [39;49;00m{[37m[39;49;00m$
[37m                        [39;49;00m[36mint[39;49;00m[37m [39;49;00mpoppedIndent[37m [39;49;00m=[37m [39;49;00mparenIndentStack->back();[37m[39;49;00m$
[37m                        [39;49;00mparenIndentStack->pop_back();[37m[39;49;00m$
[37m[39;49;00m$
[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m                          [39;49;00mspaceTabCount[37m [39;49;00m=[37m [39;49;00mpoppedIndent;[37m[39;49;00m$
[37m                      [39;49;00m}[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00m[36mbool[39;49;00m[37m [39;49;00misBlockOpener[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[37m// first, check if '{' is a block-opener or an static-array opener[39;49;00m$
[37m            [39;49;00misBlockOpener[37m [39;49;00m=[37m [39;49;00m([37m [39;49;00m(prevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00mbracketBlockStateStack->back())[37m[39;49;00m$
[37m                              [39;49;00m||[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
[37m                              [39;49;00m||[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
[37m                              [39;49;00m||[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
[37m                              [39;49;00m||[37m [39;49;00misInClassHeader[37m[39;49;00m$
[37m                              [39;49;00m||[37m [39;49;00misBlockOpener[37m[39;49;00m$
[37m                              [39;49;00m||[37m [39;49;00misImmediatelyAfterConst[37m[39;49;00m$
[37m                              [39;49;00m||[37m [39;49;00m(isInDefine[37m [39;49;00m&&[37m[39;49;00m$
[37m                                  [39;49;00m(prevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m([39;49;00m[33m'[39;49;00m[37m[39;49;00m$
[37m                                   [39;49;00m||[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m_[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
[37m                                   [39;49;00m||[37m [39;49;00misalnum(prevNonSpaceCh)))[37m [39;49;00m);[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isBlockOpener[37m [39;49;00m&&[37m [39;49;00mcurrentHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mn=[34m0[39;49;00m;[37m [39;49;00mn[37m [39;49;00m<[37m [39;49;00mnonParenHeaders.size();[37m [39;49;00mn++)[37m[39;49;00m$
[37m                  [39;49;00m[34mif[39;49;00m[37m [39;49;00m(currentHeader[37m [39;49;00m==[37m [39;49;00mnonParenHeaders[n])[37m[39;49;00m$
[37m                    [39;49;00m{[37m[39;49;00m$
[37m                      [39;49;00misBlockOpener[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m                      [39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m                    [39;49;00m}[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m            [39;49;00mbracketBlockStateStack->push_back(isBlockOpener);[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isBlockOpener)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00minStatementIndentStackSizeStack->push_back(inStatementIndentStack->size());[37m[39;49;00m$
[37m                [39;49;00mregisterInStatementIndent(line,[37m [39;49;00mi,[37m [39;49;00mspaceTabCount,[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00m[36mtrue[39;49;00m);[37m[39;49;00m$
[37m                [39;49;00mparenDepth++;[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m                  [39;49;00mshouldIndentBrackettedLine[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[37m// this bracket is a block opener...[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m++lineOpeningBlocksNum;[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInClassHeader)[37m[39;49;00m$
[37m              [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInClassHeaderTab)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00misInClassHeaderTab[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m                [39;49;00mtabCount[37m [39;49;00m-=[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00mblockParenDepthStack->push_back(parenDepth);[37m[39;49;00m$
[37m            [39;49;00mblockStatementStack->push_back(isInStatement);[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00minStatementIndentStackSizeStack->push_back(inStatementIndentStack->size());[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00mblockTabCount[37m [39;49;00m+=[37m [39;49;00misInStatement?[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m:[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m            [39;49;00mparenDepth[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m            [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00mtempStacks->push_back([34mnew[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>);[37m[39;49;00m$
[37m            [39;49;00mheaderStack->push_back(&AS_OPEN_BRACKET);[37m[39;49;00m$
[37m            [39;49;00mlastLineHeader[37m [39;49;00m=[37m [39;49;00m&AS_OPEN_BRACKET;[37m [39;49;00m[37m// <------[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m//check if a header has been reached[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(prevCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00m[36mbool[39;49;00m[37m [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m            [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*newHeader[37m [39;49;00m=[37m [39;49;00mfindHeader(line,[37m [39;49;00mi,[37m [39;49;00mheaders);[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m[37m// if we reached here, then this is a header...[39;49;00m$
[37m                [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m*lastTempStack;[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(tempStacks->empty())[37m[39;49;00m$
[37m                  [39;49;00mlastTempStack[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m                [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m                  [39;49;00mlastTempStack[37m [39;49;00m=[37m [39;49;00mtempStacks->back();[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[37m// if a new block is opened, push a new stack into tempStacks to hold the[39;49;00m$
[37m                [39;49;00m[37m// future list of headers in the new block.[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[37m// take care of the special case: 'else if (...)'[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_IF[37m [39;49;00m&&[37m [39;49;00mlastLineHeader[37m [39;49;00m==[37m [39;49;00m&AS_ELSE)[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00m[37m//spaceTabCount += indentLength; // to counter the opposite addition that occurs when the 'if' is registered below...[39;49;00m$
[37m                    [39;49;00mheaderStack->pop_back();[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[37m// take care of 'else'[39;49;00m$
[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_ELSE)[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lastTempStack[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m                      [39;49;00m{[37m[39;49;00m$
[37m                        [39;49;00m[36mint[39;49;00m[37m [39;49;00mindexOfIf[37m [39;49;00m=[37m [39;49;00mindexOf(*lastTempStack,[37m [39;49;00m&AS_IF);[37m [39;49;00m[37m// <---[39;49;00m$
[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(indexOfIf[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
[37m                          [39;49;00m{[37m[39;49;00m$
[37m                            [39;49;00m[37m// recreate the header list in headerStack up to the previous 'if'[39;49;00m$
[37m                            [39;49;00m[37m// from the temporary snapshot stored in lastTempStack.[39;49;00m$
[37m                            [39;49;00m[36mint[39;49;00m[37m [39;49;00mrestackSize[37m [39;49;00m=[37m [39;49;00mlastTempStack->size()[37m [39;49;00m-[37m [39;49;00mindexOfIf[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[37m                            [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mr=[34m0[39;49;00m;[37m [39;49;00mr<restackSize;[37m [39;49;00mr++)[37m[39;49;00m$
[37m                              [39;49;00m{[37m[39;49;00m$
[37m                                [39;49;00mheaderStack->push_back(lastTempStack->back());[37m[39;49;00m$
[37m                                [39;49;00mlastTempStack->pop_back();[37m[39;49;00m$
[37m                              [39;49;00m}[37m[39;49;00m$
[37m                            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!closingBracketReached)[37m[39;49;00m$
[37m                              [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00mrestackSize;[37m[39;49;00m$
[37m                          [39;49;00m}[37m[39;49;00m$
[37m                        [39;49;00m[37m/*[39;49;00m$
[37m                         * If the above if is not true, i.e. no 'if' before the 'else',[39;49;00m$
[37m                         * then nothing beautiful will come out of this...[39;49;00m$
[37m                         * I should think about inserting an Exception here to notify the caller of this...[39;49;00m$
[37m                         */[39;49;00m[37m[39;49;00m$
[37m                      [39;49;00m}[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[37m// check if 'while' closes a previous 'do'[39;49;00m$
[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_WHILE)[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lastTempStack[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m                      [39;49;00m{[37m[39;49;00m$
[37m                        [39;49;00m[36mint[39;49;00m[37m [39;49;00mindexOfDo[37m [39;49;00m=[37m [39;49;00mindexOf(*lastTempStack,[37m [39;49;00m&AS_DO);[37m [39;49;00m[37m// <---[39;49;00m$
[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(indexOfDo[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
[37m                          [39;49;00m{[37m[39;49;00m$
[37m                            [39;49;00m[37m// recreate the header list in headerStack up to the previous 'do'[39;49;00m$
[37m                            [39;49;00m[37m// from the temporary snapshot stored in lastTempStack.[39;49;00m$
[37m                            [39;49;00m[36mint[39;49;00m[37m [39;49;00mrestackSize[37m [39;49;00m=[37m [39;49;00mlastTempStack->size()[37m [39;49;00m-[37m [39;49;00mindexOfDo[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[37m                            [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mr=[34m0[39;49;00m;[37m [39;49;00mr<restackSize;[37m [39;49;00mr++)[37m[39;49;00m$
[37m                              [39;49;00m{[37m[39;49;00m$
[37m                                [39;49;00mheaderStack->push_back(lastTempStack->back());[37m[39;49;00m$
[37m                                [39;49;00mlastTempStack->pop_back();[37m[39;49;00m$
[37m                              [39;49;00m}[37m[39;49;00m$
[37m                            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!closingBracketReached)[37m[39;49;00m$
[37m                              [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00mrestackSize;[37m[39;49;00m$
[37m                          [39;49;00m}[37m[39;49;00m$
[37m                      [39;49;00m}[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m                [39;49;00m[37m// check if 'catch' closes a previous 'try' or 'catch'[39;49;00m$
[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_CATCH[37m [39;49;00m||[37m [39;49;00mnewHeader[37m [39;49;00m==[37m [39;49;00m&AS_FINALLY)[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lastTempStack[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m                      [39;49;00m{[37m[39;49;00m$
[37m                        [39;49;00m[36mint[39;49;00m[37m [39;49;00mindexOfTry[37m [39;49;00m=[37m [39;49;00mindexOf(*lastTempStack,[37m [39;49;00m&AS_TRY);[37m[39;49;00m$
[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(indexOfTry[37m [39;49;00m==[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
[37m                          [39;49;00mindexOfTry[37m [39;49;00m=[37m [39;49;00mindexOf(*lastTempStack,[37m [39;49;00m&AS_CATCH);[37m[39;49;00m$
[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(indexOfTry[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
[37m                          [39;49;00m{[37m[39;49;00m$
[37m                            [39;49;00m[37m// recreate the header list in headerStack up to the previous 'try'[39;49;00m$
[37m                            [39;49;00m[37m// from the temporary snapshot stored in lastTempStack.[39;49;00m$
[37m                            [39;49;00m[36mint[39;49;00m[37m [39;49;00mrestackSize[37m [39;49;00m=[37m [39;49;00mlastTempStack->size()[37m [39;49;00m-[37m [39;49;00mindexOfTry[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[37m                            [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mr=[34m0[39;49;00m;[37m [39;49;00mr<restackSize;[37m [39;49;00mr++)[37m[39;49;00m$
[37m                              [39;49;00m{[37m[39;49;00m$
[37m                                [39;49;00mheaderStack->push_back(lastTempStack->back());[37m[39;49;00m$
[37m                                [39;49;00mlastTempStack->pop_back();[37m[39;49;00m$
[37m                              [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m                            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!closingBracketReached)[37m[39;49;00m$
[37m                              [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00mrestackSize;[37m[39;49;00m$
[37m                          [39;49;00m}[37m[39;49;00m$
[37m                      [39;49;00m}[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_CASE)[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00misInCase[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!caseIndent)[37m[39;49;00m$
[37m                      [39;49;00m--tabCount;[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_DEFAULT)[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00misInCase[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!caseIndent)[37m[39;49;00m$
[37m                      [39;49;00m--tabCount;[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_PUBLIC[37m [39;49;00m||[37m [39;49;00mnewHeader[37m [39;49;00m==[37m [39;49;00m&AS_PROTECTED[37m [39;49;00m||[37m [39;49;00mnewHeader[37m [39;49;00m==[37m [39;49;00m&AS_PRIVATE)[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00m!isInClassHeader)[37m[39;49;00m$
[37m                      [39;49;00m--tabCount;[37m[39;49;00m$
[37m                    [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m                [39;49;00m[37m//else if ((newHeader == &STATIC || newHeader == &SYNCHRONIZED) &&[39;49;00m$
[37m                [39;49;00m[37m//         !headerStack->empty() &&[39;49;00m$
[37m                [39;49;00m[37m//         (headerStack->back() == &STATIC || headerStack->back() == &SYNCHRONIZED))[39;49;00m$
[37m                [39;49;00m[37m//{[39;49;00m$
[37m                [39;49;00m[37m//    isIndentableHeader = false;[39;49;00m$
[37m                [39;49;00m[37m//}[39;49;00m$
[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_STATIC[37m[39;49;00m$
[37m                         [39;49;00m||[37m [39;49;00mnewHeader[37m [39;49;00m==[37m [39;49;00m&AS_SYNCHRONIZED[37m[39;49;00m$
[37m                         [39;49;00m||[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_CONST[37m [39;49;00m&&[37m [39;49;00misCStyle))[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!headerStack->empty()[37m [39;49;00m&&[37m[39;49;00m$
[37m                        [39;49;00m(headerStack->back()[37m [39;49;00m==[37m [39;49;00m&AS_STATIC[37m[39;49;00m$
[37m                         [39;49;00m||[37m [39;49;00mheaderStack->back()[37m [39;49;00m==[37m [39;49;00m&AS_SYNCHRONIZED[37m[39;49;00m$
[37m                         [39;49;00m||[37m [39;49;00mheaderStack->back()[37m [39;49;00m==[37m [39;49;00m&AS_CONST))[37m[39;49;00m$
[37m                      [39;49;00m{[37m[39;49;00m$
[37m                        [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m                      [39;49;00m}[37m[39;49;00m$
[37m                    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m                      [39;49;00m{[37m[39;49;00m$
[37m                        [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m                        [39;49;00mprobationHeader[37m [39;49;00m=[37m [39;49;00mnewHeader;[37m[39;49;00m$
[37m                      [39;49;00m}[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_CONST)[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00m[37m// this will be entered only if NOT in C style[39;49;00m$
[37m                    [39;49;00m[37m// since otherwise the CONST would be found to be a probstion header...[39;49;00m$
[37m[39;49;00m$
[37m                    [39;49;00m[37m//if (isCStyle)[39;49;00m$
[37m                    [39;49;00m[37m//  isInConst = true;[39;49;00m$
[37m                    [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m                [39;49;00m[37m/*[39;49;00m$
[37m                              else if (newHeader == &OPERATOR)[39;49;00m$
[37m                              {[39;49;00m$
[37m                                  if (isCStyle)[39;49;00m$
[37m                                      isInOperator = true;[39;49;00m$
[37m                                  isIndentableHeader = false;[39;49;00m$
[37m                              }[39;49;00m$
[37m                */[39;49;00m[37m[39;49;00m$
[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m==[37m [39;49;00m&AS_TEMPLATE)[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle)[37m[39;49;00m$
[37m                      [39;49;00misInTemplate[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m                    [39;49;00misIndentableHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isIndentableHeader)[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00m[37m// 3.2.99[39;49;00m$
[37m                    [39;49;00m[37m//spaceTabCount-=indentLength;[39;49;00m$
[37m                    [39;49;00mheaderStack->push_back(newHeader);[37m[39;49;00m$
[37m                    [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(indexOf(nonParenHeaders,[37m [39;49;00mnewHeader)[37m [39;49;00m==[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
[37m                      [39;49;00m{[37m[39;49;00m$
[37m                        [39;49;00misInConditional[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m                      [39;49;00m}[37m[39;49;00m$
[37m                    [39;49;00mlastLineHeader[37m [39;49;00m=[37m [39;49;00mnewHeader;[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m                [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m                  [39;49;00misInHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[37m//lastLineHeader = newHeader;[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00moutBuffer.append(newHeader->substr([34m1[39;49;00m));[37m[39;49;00m$
[37m                [39;49;00mi[37m [39;49;00m+=[37m [39;49;00mnewHeader->length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00m!isalpha(prevCh)[37m[39;49;00m$
[37m            [39;49;00m&&[37m [39;49;00mline.COMPARE(i,[37m [39;49;00m[34m8[39;49;00m,[37m [39;49;00mAS_OPERATOR)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00m!isalnum(line[i+[34m8[39;49;00m]))[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00misInOperator[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m            [39;49;00moutBuffer.append(AS_OPERATOR.substr([34m1[39;49;00m));[37m[39;49;00m$
[37m            [39;49;00mi[37m [39;49;00m+=[37m [39;49;00m[34m7[39;49;00m;[37m[39;49;00m$
[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m?[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00misInQuestion[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m// special handling of 'case' statements[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.length()[37m [39;49;00m>[37m [39;49;00mi+[34m1[39;49;00m[37m [39;49;00m&&[37m [39;49;00mline[i+[34m1[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m)[37m [39;49;00m[37m// look for ::[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m++i;[37m[39;49;00m$
[37m                [39;49;00moutBuffer.append([34m1[39;49;00m,[37m [39;49;00m[33m'[39;49;00m[33m:[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
[37m                [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m;[37m[39;49;00m$
[37m                [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00misInClass[37m [39;49;00m&&[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m!=[37m [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m              [39;49;00m[37m// BEGIN Content of ASBeautifier.cpp.BITFIELD.patch:[39;49;00m$
[37m              [39;49;00m[37m[39;49;00m$
[37m                [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mchIndex;[37m[39;49;00m$
[37m   ^I^I^I    [39;49;00m[36mchar[39;49;00m[37m [39;49;00mnextCh[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m                [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(chIndex[37m [39;49;00m=[37m [39;49;00mi+[34m1[39;49;00m;[37m [39;49;00mchIndex[37m [39;49;00m<[37m [39;49;00mline.length();[37m [39;49;00mchIndex++)[37m[39;49;00m$
[37m            ^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[chIndex]))[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(chIndex<[37m [39;49;00mline.length())[37m[39;49;00m$
[37m       ^I^I^I^I^I[39;49;00mnextCh[37m [39;49;00m=[37m [39;49;00mline[chIndex];[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[36mint[39;49;00m[37m [39;49;00mnWord[37m [39;49;00m=[34m0[39;49;00m;[37m[39;49;00m$
[37m    ^I^I^I[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(chIndex[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mchIndex[37m [39;49;00m<[37m [39;49;00mi;[37m [39;49;00mchIndex++)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[chIndex]))[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00mnWord[37m [39;49;00m++;[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[++chIndex]));[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m}[37m^I^I^I^I^I^I^I^I^I[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m((nextCh[37m [39;49;00m>=[37m [39;49;00m[33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00mnextCh[37m [39;49;00m<=[37m [39;49;00m[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m)[37m [39;49;00m||[37m [39;49;00m(nWord[37m [39;49;00m>[34m1[39;49;00m))[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m              [39;49;00m[37m// END Content of ASBeautifier.cpp.BITFIELD.patch:[39;49;00m$
[37m                [39;49;00m[37m[39;49;00m$
[37m                [39;49;00m--tabCount;[37m[39;49;00m$
[37m                [39;49;00m[37m// found a 'private:' or 'public:' inside a class definition[39;49;00m$
[37m                [39;49;00m[37m// so do nothing special[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00misInClassHeader)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[37m// found a 'class A : public B' definition[39;49;00m$
[37m                [39;49;00m[37m// so do nothing special[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInQuestion)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00misInQuestion[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00mprevNonSpaceCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m)[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i==[34m0[39;49;00m)[37m[39;49;00m$
[37m                  [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00m[34m2[39;49;00m;[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m            [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00mcurrentNonSpaceCh[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m;[37m [39;49;00m[37m// so that brackets after the ':' will appear as block-openers[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInCase)[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00misInCase[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m                    [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m;[37m [39;49;00m[37m// from here on, treat char as ';'[39;49;00m$
[37m                  [39;49;00m}[37m [39;49;00m[37m[39;49;00m$
[37m              [39;49;00m[37m// BEGIN content of ASBeautifier.cpp.BITFIELD.patch.bz2[39;49;00m$
[37m              [39;49;00m[34melse[39;49;00m[37m [39;49;00m[37m// bitfield or labels[39;49;00m$
[37m^I^I^I^I^I^I^I^I[39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mchIndex;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[36mchar[39;49;00m[37m [39;49;00mnextCh[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(chIndex[37m [39;49;00m=[37m [39;49;00mi+[34m1[39;49;00m;[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00mchIndex[37m [39;49;00m<[37m [39;49;00mline.length());[37m [39;49;00mchIndex++)[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[chIndex]))[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00m[34mbreak[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(chIndex<[37m [39;49;00mline.length())[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00mnextCh[37m [39;49;00m=[37m [39;49;00mline[chIndex];[37m[39;49;00m$
[37m[39;49;00m$
[37m     ^I^I^I[39;49;00m[36mint[39;49;00m[37m [39;49;00mnWord[37m [39;49;00m=[34m0[39;49;00m;[37m[39;49;00m$
[37m ^I^I^I^I[39;49;00m[34mfor[39;49;00m[37m [39;49;00m(chIndex[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00mchIndex[37m [39;49;00m<[37m [39;49;00mi;[37m [39;49;00mchIndex++)[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[chIndex]))[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00mnWord[37m [39;49;00m++;[37m[39;49;00m$
[37m^I^I^I^I^I^I[39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(!isWhiteSpace(line[++chIndex]));[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m}[37m^I^I^I^I^I^I^I^I^I[39;49;00m[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m         ^I^I[39;49;00m[34mif[39;49;00m[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m  [39;49;00m(nextCh[37m [39;49;00m>=[37m [39;49;00m[33m'[39;49;00m[33m0[39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00mnextCh[37m [39;49;00m<=[37m [39;49;00m[33m'[39;49;00m[33m9[39;49;00m[33m'[39;49;00m)[37m [39;49;00m||[37m [39;49;00m(nWord[37m [39;49;00m>[34m1[39;49;00m))[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m{[37m[39;49;00m$
[37m^I^I^I^I^I[39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m^I^I^I^I[39;49;00m}[37m[39;49;00m$
[37m                [39;49;00m[37m// END content of ASASBeautifier.cpp.BITFIELD.patch.bz2[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[34melse[39;49;00m[37m [39;49;00m[37m// is in a label (e.g. 'label1:')[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(labelIndent)[37m[39;49;00m$
[37m                      [39;49;00m--tabCount;[37m [39;49;00m[37m// unindent label by one indent[39;49;00m$
[37m                    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m                      [39;49;00mtabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m [39;49;00m[37m// completely flush indent to left[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m              [39;49;00m[37m// BEGIN content of ASASBeautifier.cpp.BITFIELD.patch.bz2[39;49;00m$
[37m                [39;49;00m}[37m[39;49;00m$
[37m            [39;49;00m[37m// END content of ASASBeautifier.cpp.BITFIELD.patch.bz2[39;49;00m$
[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m((ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m[37m  [39;49;00m||[37m [39;49;00m(parenDepth>[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m,[39;49;00m[33m'[39;49;00m))[37m  [39;49;00m&&[37m [39;49;00m!inStatementIndentStackSizeStack->empty())[37m[39;49;00m$
[37m          [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(([36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m)inStatementIndentStackSizeStack->back()[37m [39;49;00m+[37m [39;49;00m(parenDepth>[34m0[39;49;00m[37m [39;49;00m?[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m:[37m [39;49;00m[34m0[39;49;00m)[37m  [39;49;00m<[37m [39;49;00minStatementIndentStack->size())[37m[39;49;00m$
[37m            [39;49;00minStatementIndentStack->pop_back();[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m// handle ends of statements[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m([37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00mparenDepth[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m[37m/* || (ch == ',' && parenDepth == 0)*/[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m[37m// first check if this '}' closes a previous block, or a static array...[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!bracketBlockStateStack->empty())[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00m[36mbool[39;49;00m[37m [39;49;00mbracketBlockState[37m [39;49;00m=[37m [39;49;00mbracketBlockStateStack->back();[37m[39;49;00m$
[37m                    [39;49;00mbracketBlockStateStack->pop_back();[37m[39;49;00m$
[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!bracketBlockState)[37m[39;49;00m$
[37m                      [39;49;00m{[37m[39;49;00m$
[37m                        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStackSizeStack->empty())[37m[39;49;00m$
[37m                          [39;49;00m{[37m[39;49;00m$
[37m                            [39;49;00m[37m// this bracket is a static array[39;49;00m$
[37m[39;49;00m$
[37m                            [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mpreviousIndentStackSize[37m [39;49;00m=[37m [39;49;00minStatementIndentStackSizeStack->back();[37m[39;49;00m$
[37m                            [39;49;00minStatementIndentStackSizeStack->pop_back();[37m[39;49;00m$
[37m                            [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(previousIndentStackSize[37m [39;49;00m<[37m [39;49;00minStatementIndentStack->size())[37m[39;49;00m$
[37m                              [39;49;00minStatementIndentStack->pop_back();[37m[39;49;00m$
[37m                            [39;49;00mparenDepth--;[37m[39;49;00m$
[37m                            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m                              [39;49;00mshouldIndentBrackettedLine[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m                            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!parenIndentStack->empty())[37m[39;49;00m$
[37m                              [39;49;00m{[37m[39;49;00m$
[37m                                [39;49;00m[36mint[39;49;00m[37m [39;49;00mpoppedIndent[37m [39;49;00m=[37m [39;49;00mparenIndentStack->back();[37m[39;49;00m$
[37m                                [39;49;00mparenIndentStack->pop_back();[37m[39;49;00m$
[37m                                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m                                  [39;49;00mspaceTabCount[37m [39;49;00m=[37m [39;49;00mpoppedIndent;[37m[39;49;00m$
[37m                              [39;49;00m}[37m[39;49;00m$
[37m                          [39;49;00m}[37m[39;49;00m$
[37m                        [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m                      [39;49;00m}[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[37m// this bracket is block closer...[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m++lineClosingBlocksNum;[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m(!inStatementIndentStackSizeStack->empty())[37m[39;49;00m$
[37m                  [39;49;00minStatementIndentStackSizeStack->pop_back();[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!blockParenDepthStack->empty())[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00mparenDepth[37m [39;49;00m=[37m [39;49;00mblockParenDepthStack->back();[37m[39;49;00m$
[37m                    [39;49;00mblockParenDepthStack->pop_back();[37m[39;49;00m$
[37m                    [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00mblockStatementStack->back();[37m[39;49;00m$
[37m                    [39;49;00mblockStatementStack->pop_back();[37m[39;49;00m$
[37m[39;49;00m$
[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInStatement)[37m[39;49;00m$
[37m                      [39;49;00mblockTabCount--;[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00mclosingBracketReached[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m                [39;49;00m[36mint[39;49;00m[37m [39;49;00mheaderPlace[37m [39;49;00m=[37m [39;49;00mindexOf(*headerStack,[37m [39;49;00m&AS_OPEN_BRACKET);[37m [39;49;00m[37m// <---[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(headerPlace[37m [39;49;00m!=[37m [39;49;00m[34m-1[39;49;00m)[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*popped[37m [39;49;00m=[37m [39;49;00mheaderStack->back();[37m[39;49;00m$
[37m                    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(popped[37m [39;49;00m!=[37m [39;49;00m&AS_OPEN_BRACKET)[37m[39;49;00m$
[37m                      [39;49;00m{[37m[39;49;00m$
[37m                        [39;49;00mheaderStack->pop_back();[37m[39;49;00m$
[37m                        [39;49;00mpopped[37m [39;49;00m=[37m [39;49;00mheaderStack->back();[37m[39;49;00m$
[37m                      [39;49;00m}[37m[39;49;00m$
[37m                    [39;49;00mheaderStack->pop_back();[37m[39;49;00m$
[37m[39;49;00m$
[37m                    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!tempStacks->empty())[37m[39;49;00m$
[37m                      [39;49;00m{[37m[39;49;00m$
[37m                        [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m*temp[37m [39;49;00m=[37m  [39;49;00mtempStacks->back();[37m[39;49;00m$
[37m                        [39;49;00mtempStacks->pop_back();[37m[39;49;00m$
[37m                        [39;49;00m[34mdelete[39;49;00m[37m [39;49;00mtemp;[37m[39;49;00m$
[37m                      [39;49;00m}[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m                [39;49;00mch[37m [39;49;00m=[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m;[37m [39;49;00m[37m// needed due to cases such as '}else{', so that headers ('else' tn tih case) will be identified...[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[37m/*[39;49;00m$
[37m             * Create a temporary snapshot of the current block's header-list in the[39;49;00m$
[37m             * uppermost inner stack in tempStacks, and clear the headerStack up to[39;49;00m$
[37m             * the begining of the block.[39;49;00m$
[37m             * Thus, the next future statement will think it comes one indent past[39;49;00m$
[37m             * the block's '{' unless it specifically checks for a companion-header[39;49;00m$
[37m             * (such as a previous 'if' for an 'else' header) within the tempStacks,[39;49;00m$
[37m             * and recreates the temporary snapshot by manipulating the tempStacks.[39;49;00m$
[37m             */[39;49;00m[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!tempStacks->back()->empty())[37m[39;49;00m$
[37m              [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(!tempStacks->back()->empty())[37m[39;49;00m$
[37m                [39;49;00mtempStacks->back()->pop_back();[37m[39;49;00m$
[37m            [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(!headerStack->empty()[37m [39;49;00m&&[37m [39;49;00mheaderStack->back()[37m [39;49;00m!=[37m [39;49;00m&AS_OPEN_BRACKET)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00mtempStacks->back()->push_back(headerStack->back());[37m[39;49;00m$
[37m                [39;49;00mheaderStack->pop_back();[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(parenDepth[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m;[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00misInStatement=[36mfalse[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m// check for preBlockStatements ONLY if not within parenthesies[39;49;00m$
[37m        [39;49;00m[37m// (otherwise 'struct XXX' statements would be wrongly interpreted...)[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(prevCh[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m[37m [39;49;00m&&[37m [39;49;00m!isInTemplate[37m [39;49;00m&&[37m [39;49;00mparenDepth[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*newHeader[37m [39;49;00m=[37m [39;49;00mfindHeader(line,[37m [39;49;00mi,[37m [39;49;00mpreBlockStatements);[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(newHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00misInClassHeader[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m                [39;49;00moutBuffer.append(newHeader->substr([34m1[39;49;00m));[37m[39;49;00m$
[37m                [39;49;00mi[37m [39;49;00m+=[37m [39;49;00mnewHeader->length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[37m                [39;49;00m[37m//if (isCStyle)[39;49;00m$
[37m                [39;49;00mheaderStack->push_back(newHeader);[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m// Handle operators[39;49;00m$
[37m        [39;49;00m[37m//[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m////        // PRECHECK if a '==' or '--' or '++' operator was reached.[39;49;00m$
[37m        [39;49;00m[37m////        // If not, then register an indent IF an assignment operator was reached.[39;49;00m$
[37m        [39;49;00m[37m////        // The precheck is important, so that statements such as 'i--==2' are not recognized[39;49;00m$
[37m        [39;49;00m[37m////        // to have assignment operators (here, '-=') in them . . .[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*foundAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m        [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*foundNonAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00mimmediatelyPreviousAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m// Check if an operator has been reached.[39;49;00m$
[37m        [39;49;00mfoundAssignmentOp[37m [39;49;00m=[37m [39;49;00mfindHeader(line,[37m [39;49;00mi,[37m [39;49;00massignmentOperators,[37m [39;49;00m[36mfalse[39;49;00m);[37m[39;49;00m$
[37m        [39;49;00mfoundNonAssignmentOp[37m [39;49;00m=[37m [39;49;00mfindHeader(line,[37m [39;49;00mi,[37m [39;49;00mnonAssignmentOperators,[37m [39;49;00m[36mfalse[39;49;00m);[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m// Since findHeader's boundry checking was not used above, it is possible[39;49;00m$
[37m        [39;49;00m[37m// that both an assignment op and a non-assignment op where found,[39;49;00m$
[37m        [39;49;00m[37m// e.g. '>>' and '>>='. If this is the case, treat the LONGER one as the[39;49;00m$
[37m        [39;49;00m[37m// found operator.[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundAssignmentOp[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m [39;49;00m&&[37m [39;49;00mfoundNonAssignmentOp[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundAssignmentOp->length()[37m [39;49;00m<[37m [39;49;00mfoundNonAssignmentOp->length())[37m[39;49;00m$
[37m            [39;49;00mfoundAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m          [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m            [39;49;00mfoundNonAssignmentOp[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundNonAssignmentOp[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundNonAssignmentOp->length()[37m [39;49;00m>[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00moutBuffer.append(foundNonAssignmentOp->substr([34m1[39;49;00m));[37m[39;49;00m$
[37m                [39;49;00mi[37m [39;49;00m+=[37m [39;49;00mfoundNonAssignmentOp->length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundAssignmentOp[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(foundAssignmentOp->length()[37m [39;49;00m>[37m [39;49;00m[34m1[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00moutBuffer.append(foundAssignmentOp->substr([34m1[39;49;00m));[37m[39;49;00m$
[37m                [39;49;00mi[37m [39;49;00m+=[37m [39;49;00mfoundAssignmentOp->length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!isInOperator[37m [39;49;00m&&[37m [39;49;00m!isInTemplate)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00mregisterInStatementIndent(line,[37m [39;49;00mi,[37m [39;49;00mspaceTabCount,[37m [39;49;00m[34m0[39;49;00m,[37m [39;49;00m[36mfalse[39;49;00m);[37m[39;49;00m$
[37m                [39;49;00mimmediatelyPreviousAssignmentOp[37m [39;49;00m=[37m [39;49;00mfoundAssignmentOp;[37m[39;49;00m$
[37m                [39;49;00misInStatement[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[37m/*[39;49;00m$
[37m                immediatelyPreviousAssignmentOp = NULL;[39;49;00m$
[37m                bool isNonAssingmentOperator = false;[39;49;00m$
[37m                for (int n = 0; n < nonAssignmentOperators.size(); n++)[39;49;00m$
[37m                    if (line.COMPARE(i, nonAssignmentOperators[n]->length(), *(nonAssignmentOperators[n])) == 0)[39;49;00m$
[37m                    {[39;49;00m$
[37m                        if (nonAssignmentOperators[n]->length() > 1)[39;49;00m$
[37m                        {[39;49;00m$
[37m                            outBuffer.append(nonAssignmentOperators[n]->substr(1));[39;49;00m$
[37m                            i += nonAssignmentOperators[n]->length() - 1;[39;49;00m$
[37m                        }[39;49;00m$
[37m                        isNonAssingmentOperator = true;[39;49;00m$
[37m                        break;[39;49;00m$
[37m                    }[39;49;00m$
[37m                if (!isNonAssingmentOperator)[39;49;00m$
[37m                {[39;49;00m$
[37m                    for (int a = 0; a < assignmentOperators.size(); a++)[39;49;00m$
[37m                        if (line.COMPARE(i, assignmentOperators[a]->length(), *(assignmentOperators[a])) == 0)[39;49;00m$
[37m                        {[39;49;00m$
[37m                            if (assignmentOperators[a]->length() > 1)[39;49;00m$
[37m                            {[39;49;00m$
[37m                                outBuffer.append(assignmentOperators[a]->substr(1));[39;49;00m$
[37m                                i += assignmentOperators[a]->length() - 1;[39;49;00m$
[37m                            }[39;49;00m$
[37m         [39;49;00m$
[37m                            if (!isInOperator && !isInTemplate)[39;49;00m$
[37m                            {[39;49;00m$
[37m                                registerInStatementIndent(line, i, spaceTabCount, 0, false);[39;49;00m$
[37m                                immediatelyPreviousAssignmentOp = assignmentOperators[a];[39;49;00m$
[37m                                isInStatement = true;[39;49;00m$
[37m                            }[39;49;00m$
[37m                            break;[39;49;00m$
[37m                        }[39;49;00m$
[37m                }[39;49;00m$
[37m        */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInOperator)[37m[39;49;00m$
[37m          [39;49;00misInOperator[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m      [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m// handle special cases of unindentation:[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m/*[39;49;00m$
[37m     * if '{' doesn't follow an immediately previous '{' in the headerStack[39;49;00m$
[37m     * (but rather another header such as "for" or "if", then unindent it[39;49;00m$
[37m     * by one indentation relative to its block.[39;49;00m$
[37m     */[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m[37m//    cerr << endl << lineOpeningBlocksNum << " " <<  lineClosingBlocksNum << " " <<  previousLastLineHeader << endl;[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m// indent #define lines with one less tab[39;49;00m$
[37m    [39;49;00m[37m//if (isInDefine)[39;49;00m$
[37m    [39;49;00m[37m//    tabCount -= defineTabCount-1;[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!lineStartsInComment[37m[39;49;00m$
[37m        [39;49;00m&&[37m [39;49;00m!blockIndent[37m[39;49;00m$
[37m        [39;49;00m&&[37m [39;49;00moutBuffer.length()>[34m0[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m&&[37m [39;49;00moutBuffer[[34m0[39;49;00m]==[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
[37m        [39;49;00m&&[37m [39;49;00m!(lineOpeningBlocksNum[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mlineOpeningBlocksNum[37m [39;49;00m==[37m [39;49;00mlineClosingBlocksNum)[37m[39;49;00m$
[37m        [39;49;00m&&[37m [39;49;00m!(headerStack->size()[37m [39;49;00m>[37m [39;49;00m[34m1[39;49;00m[37m [39;49;00m&&[37m [39;49;00m(*headerStack)[headerStack->size()[34m-2[39;49;00m][37m [39;49;00m==[37m [39;49;00m&AS_OPEN_BRACKET)[37m[39;49;00m$
[37m        [39;49;00m&&[37m [39;49;00mshouldIndentBrackettedLine)[37m[39;49;00m$
[37m      [39;49;00m--tabCount;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!lineStartsInComment[37m[39;49;00m$
[37m             [39;49;00m&&[37m [39;49;00moutBuffer.length()>[34m0[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m&&[37m [39;49;00moutBuffer[[34m0[39;49;00m]==[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m&&[37m [39;49;00mshouldIndentBrackettedLine[37m [39;49;00m)[37m[39;49;00m$
[37m      [39;49;00m--tabCount;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m// correctly indent one-line-blocks...[39;49;00m$
[37m    [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!lineStartsInComment[37m[39;49;00m$
[37m             [39;49;00m&&[37m [39;49;00moutBuffer.length()>[34m0[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m&&[37m [39;49;00mlineOpeningBlocksNum[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m&&[37m [39;49;00mlineOpeningBlocksNum[37m [39;49;00m==[37m [39;49;00mlineClosingBlocksNum[37m[39;49;00m$
[37m             [39;49;00m&&[37m [39;49;00mpreviousLastLineHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m[37m[39;49;00m$
[37m             [39;49;00m&&[37m [39;49;00mpreviousLastLineHeader[37m [39;49;00m!=[37m [39;49;00m&AS_OPEN_BRACKET)[37m[39;49;00m$
[37m      [39;49;00mtabCount[37m [39;49;00m-=[37m [39;49;00m[34m1[39;49;00m;[37m [39;49;00m[37m//lineOpeningBlocksNum - (blockIndent ? 1 : 0);[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(tabCount[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00mtabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m// take care of extra bracket indentatation option...[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(bracketIndent[37m [39;49;00m&&[37m [39;49;00moutBuffer.length()>[34m0[39;49;00m[37m [39;49;00m&&[37m [39;49;00mshouldIndentBrackettedLine)[37m[39;49;00m$
[37m      [39;49;00m[34mif[39;49;00m[37m [39;49;00m(outBuffer[[34m0[39;49;00m]==[33m'[39;49;00m[33m{[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00moutBuffer[[34m0[39;49;00m]==[33m'[39;49;00m[33m}[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m        [39;49;00mtabCount++;[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isInDefine)[37m[39;49;00m$
[37m      [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(outBuffer[[34m0[39;49;00m][37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m#[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00mstring[37m [39;49;00mpreproc[37m [39;49;00m=[37m [39;49;00mtrim(string(outBuffer.c_str()[37m [39;49;00m+[37m [39;49;00m[34m1[39;49;00m));[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(preproc.COMPARE([34m0[39;49;00m,[37m [39;49;00m[34m6[39;49;00m,[37m [39;49;00mstring([33m"[39;49;00m[33mdefine[39;49;00m[33m"[39;49;00m))[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStack->empty()[37m[39;49;00m$
[37m                    [39;49;00m&&[37m [39;49;00minStatementIndentStack->back()[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00mdefineTabCount[37m [39;49;00m=[37m [39;49;00mtabCount;[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m                [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m                  [39;49;00m{[37m[39;49;00m$
[37m                    [39;49;00mdefineTabCount[37m [39;49;00m=[37m [39;49;00mtabCount[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[37m                    [39;49;00mtabCount--;[37m[39;49;00m$
[37m                  [39;49;00m}[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00mtabCount[37m [39;49;00m-=[37m [39;49;00mdefineTabCount;[37m[39;49;00m$
[37m      [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(tabCount[37m [39;49;00m<[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00mtabCount[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m// finally, insert indentations into begining of line[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mprevFinalLineSpaceTabCount[37m [39;49;00m=[37m [39;49;00mspaceTabCount;[37m[39;49;00m$
[37m    [39;49;00mprevFinalLineTabCount[37m [39;49;00m=[37m [39;49;00mtabCount;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(shouldForceTabIndentation)[37m[39;49;00m$
[37m      [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00mtabCount[37m [39;49;00m+=[37m [39;49;00mspaceTabCount[37m [39;49;00m/[37m [39;49;00mindentLength;[37m[39;49;00m$
[37m        [39;49;00mspaceTabCount[37m [39;49;00m=[37m [39;49;00mspaceTabCount[37m [39;49;00m%[37m [39;49;00mindentLength;[37m[39;49;00m$
[37m      [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00moutBuffer[37m [39;49;00m=[37m [39;49;00mpreLineWS(spaceTabCount,tabCount)[37m [39;49;00m+[37m [39;49;00moutBuffer;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(lastLineHeader[37m [39;49;00m!=[37m [39;49;00m[36mNULL[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00mpreviousLastLineHeader[37m [39;49;00m=[37m [39;49;00mlastLineHeader;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00moutBuffer;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00mstring[37m [39;49;00mASBeautifier::preLineWS([36mint[39;49;00m[37m [39;49;00mspaceTabCount,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mtabCount)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mstring[37m [39;49;00mws;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m([36mint[39;49;00m[37m [39;49;00mi=[34m0[39;49;00m;[37m [39;49;00mi<tabCount;[37m [39;49;00mi++)[37m[39;49;00m$
[37m      [39;49;00mws[37m [39;49;00m+=[37m [39;49;00mindentString;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m((spaceTabCount--)[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m      [39;49;00mws[37m [39;49;00m+=[37m [39;49;00mstring([33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mws;[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * register an in-statement indent.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mvoid[39;49;00m[37m [39;49;00mASBeautifier::registerInStatementIndent([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mspaceTabCount,[37m[39;49;00m$
[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mminIndent,[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mupdateParenStack)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00minStatementIndent;[37m[39;49;00m$
[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mremainingCharNum[37m [39;49;00m=[37m [39;49;00mline.length()[37m [39;49;00m-[37m [39;49;00mi;[37m[39;49;00m$
[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mnextNonWSChar[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mnextNonWSChar[37m [39;49;00m=[37m [39;49;00mgetNextProgramCharDistance(line,[37m [39;49;00mi);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[37m// if indent is around the last char in the line, indent instead 2 spaces from the previous indent[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(nextNonWSChar[37m [39;49;00m==[37m [39;49;00mremainingCharNum)[37m[39;49;00m$
[37m      [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00m[36mint[39;49;00m[37m [39;49;00mpreviousIndent[37m [39;49;00m=[37m [39;49;00mspaceTabCount;[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStack->empty())[37m[39;49;00m$
[37m          [39;49;00mpreviousIndent[37m [39;49;00m=[37m [39;49;00minStatementIndentStack->back();[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00minStatementIndentStack->push_back([37m/*2*/[39;49;00m[37m [39;49;00mindentLength[37m [39;49;00m+[37m [39;49;00mpreviousIndent[37m [39;49;00m);[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(updateParenStack)[37m[39;49;00m$
[37m          [39;49;00mparenIndentStack->push_back([37m [39;49;00mpreviousIndent[37m [39;49;00m);[37m[39;49;00m$
[37m        [39;49;00m[34mreturn[39;49;00m;[37m[39;49;00m$
[37m      [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(updateParenStack)[37m[39;49;00m$
[37m      [39;49;00mparenIndentStack->push_back(i+spaceTabCount);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00minStatementIndent[37m [39;49;00m=[37m [39;49;00mi[37m [39;49;00m+[37m [39;49;00mnextNonWSChar[37m [39;49;00m+[37m [39;49;00mspaceTabCount;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m+[37m [39;49;00mnextNonWSChar[37m [39;49;00m<[37m [39;49;00mminIndent)[37m[39;49;00m$
[37m      [39;49;00minStatementIndent[37m [39;49;00m=[37m [39;49;00mminIndent[37m [39;49;00m+[37m [39;49;00mspaceTabCount;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m+[37m [39;49;00mnextNonWSChar[37m [39;49;00m>[37m [39;49;00mmaxInStatementIndent)[37m[39;49;00m$
[37m      [39;49;00minStatementIndent[37m [39;49;00m=[37m  [39;49;00mindentLength*[34m2[39;49;00m[37m [39;49;00m+[37m [39;49;00mspaceTabCount;[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!inStatementIndentStack->empty()[37m [39;49;00m&&[37m[39;49;00m$
[37m        [39;49;00minStatementIndent[37m [39;49;00m<[37m [39;49;00minStatementIndentStack->back())[37m[39;49;00m$
[37m      [39;49;00minStatementIndent[37m [39;49;00m=[37m [39;49;00minStatementIndentStack->back();[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00minStatementIndentStack->push_back(inStatementIndent);[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * get distance to the next non-white sspace, non-comment character in the line.[39;49;00m$
[37m   * if no such character exists, return the length remaining to the end of the line.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mint[39;49;00m[37m [39;49;00mASBeautifier::getNextProgramCharDistance([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00m[36mbool[39;49;00m[37m [39;49;00minComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mremainingCharNum[37m [39;49;00m=[37m [39;49;00mline.length()[37m [39;49;00m-[37m [39;49;00mi;[37m[39;49;00m$
[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mcharDistance[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mch;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(charDistance[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m;[37m [39;49;00mcharDistance[37m [39;49;00m<[37m [39;49;00mremainingCharNum;[37m [39;49;00mcharDistance++)[37m[39;49;00m$
[37m      [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00mch[37m [39;49;00m=[37m [39;49;00mline[i[37m [39;49;00m+[37m [39;49;00mcharDistance];[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(inComment)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.COMPARE(i[37m [39;49;00m+[37m [39;49;00mcharDistance,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_CLOSE_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00mcharDistance++;[37m[39;49;00m$
[37m                [39;49;00minComment[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m;[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m            [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(isWhiteSpace(ch))[37m[39;49;00m$
[37m          [39;49;00m[34mcontinue[39;49;00m;[37m[39;49;00m$
[37m        [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m/[39;49;00m[33m'[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.COMPARE(i[37m [39;49;00m+[37m [39;49;00mcharDistance,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_OPEN_LINE_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mremainingCharNum;[37m[39;49;00m$
[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.COMPARE(i[37m [39;49;00m+[37m [39;49;00mcharDistance,[37m [39;49;00m[34m2[39;49;00m,[37m [39;49;00mAS_OPEN_COMMENT)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00mcharDistance++;[37m[39;49;00m$
[37m                [39;49;00minComment[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m;[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m        [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m          [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mcharDistance;[37m[39;49;00m$
[37m      [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mcharDistance;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * check if a specific character can be used in a legal variable/method/class name[39;49;00m$
[37m   *[39;49;00m$
[37m   * @return          legality of the char.[39;49;00m$
[37m   * @param ch        the character to be checked.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mbool[39;49;00m[37m [39;49;00mASBeautifier::isLegalNameChar([36mchar[39;49;00m[37m [39;49;00mch)[37m [39;49;00m[34mconst[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m{[37m[39;49;00m$
[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m(isalnum(ch)[37m [39;49;00m[37m//(ch>='a' && ch<='z') || (ch>='A' && ch<='Z') || (ch>='0' && ch<='9') ||[39;49;00m$
[37m              [39;49;00m||[37m [39;49;00mch==[33m'[39;49;00m[33m.[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch==[33m'[39;49;00m[33m_[39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00m(!isCStyle[37m [39;49;00m&&[37m [39;49;00mch==[33m'[39;49;00m[33m$[39;49;00m[33m'[39;49;00m)[37m [39;49;00m||[37m [39;49;00m(isCStyle[37m [39;49;00m&&[37m [39;49;00mch==[33m'[39;49;00m[33m~[39;49;00m[33m'[39;49;00m));[37m[39;49;00m$
[37m    [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * check if a specific line position contains a header, out of several possible headers.[39;49;00m$
[37m   *[39;49;00m$
[37m   * @return    a pointer to the found header. if no header was found then return NULL.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*ASBeautifier::findHeader([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi,[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m&possibleHeaders,[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mcheckBoundry)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mmaxHeaders[37m [39;49;00m=[37m [39;49;00mpossibleHeaders.size();[37m[39;49;00m$
[37m    [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*header[37m [39;49;00m=[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mp;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mfor[39;49;00m[37m [39;49;00m(p=[34m0[39;49;00m;[37m [39;49;00mp[37m [39;49;00m<[37m [39;49;00mmaxHeaders;[37m [39;49;00mp++)[37m[39;49;00m$
[37m      [39;49;00m{[37m[39;49;00m$
[37m        [39;49;00mheader[37m [39;49;00m=[37m [39;49;00mpossibleHeaders[p];[37m[39;49;00m$
[37m[39;49;00m$
[37m        [39;49;00m[34mif[39;49;00m[37m [39;49;00m(line.COMPARE(i,[37m [39;49;00mheader->length(),[37m [39;49;00m*header)[37m [39;49;00m==[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m          [39;49;00m{[37m[39;49;00m$
[37m            [39;49;00m[37m// check that this is a header and not a part of a longer word[39;49;00m$
[37m            [39;49;00m[37m// (e.g. not at its begining, not at its middle...)[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[36mint[39;49;00m[37m [39;49;00mlineLength[37m [39;49;00m=[37m [39;49;00mline.length();[37m[39;49;00m$
[37m            [39;49;00m[36mint[39;49;00m[37m [39;49;00mheaderEnd[37m [39;49;00m=[37m [39;49;00mi[37m [39;49;00m+[37m [39;49;00mheader->length();[37m[39;49;00m$
[37m            [39;49;00m[36mchar[39;49;00m[37m [39;49;00mstartCh[37m [39;49;00m=[37m [39;49;00m(*header)[[34m0[39;49;00m];[37m   [39;49;00m[37m// first char of header[39;49;00m$
[37m            [39;49;00m[36mchar[39;49;00m[37m [39;49;00mendCh[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m                [39;49;00m[37m// char just after header[39;49;00m$
[37m            [39;49;00m[36mchar[39;49;00m[37m [39;49;00mprevCh[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m               [39;49;00m[37m// char just before header[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(headerEnd[37m [39;49;00m<[37m [39;49;00mlineLength)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00mendCh[37m [39;49;00m=[37m [39;49;00mline[headerEnd];[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(i[37m [39;49;00m>[37m [39;49;00m[34m0[39;49;00m)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00mprevCh[37m [39;49;00m=[37m [39;49;00mline[i[34m-1[39;49;00m];[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m            [39;49;00m[34mif[39;49;00m[37m [39;49;00m(!checkBoundry)[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mheader;[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(prevCh[37m [39;49;00m!=[37m [39;49;00m[34m0[39;49;00m[37m[39;49;00m$
[37m                     [39;49;00m&&[37m [39;49;00misLegalNameChar(startCh)[37m[39;49;00m$
[37m                     [39;49;00m&&[37m [39;49;00misLegalNameChar(prevCh))[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m            [39;49;00m[34melse[39;49;00m[37m [39;49;00m[34mif[39;49;00m[37m [39;49;00m(headerEnd[37m [39;49;00m>=[37m [39;49;00mlineLength[37m[39;49;00m$
[37m                     [39;49;00m||[37m [39;49;00m!isLegalNameChar(startCh)[37m[39;49;00m$
[37m                     [39;49;00m||[37m [39;49;00m!isLegalNameChar(endCh))[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mheader;[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m            [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m              [39;49;00m{[37m[39;49;00m$
[37m                [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m              [39;49;00m}[37m[39;49;00m$
[37m          [39;49;00m}[37m[39;49;00m$
[37m      [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[36mNULL[39;49;00m;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * check if a specific character can be used in a legal variable/method/class name[39;49;00m$
[37m   *[39;49;00m$
[37m   * @return          legality of the char.[39;49;00m$
[37m   * @param ch        the character to be checked.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mbool[39;49;00m[37m [39;49;00mASBeautifier::isWhiteSpace([36mchar[39;49;00m[37m [39;49;00mch)[37m [39;49;00m[34mconst[39;49;00m[37m[39;49;00m$
[37m    [39;49;00m{[37m[39;49;00m$
[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m(ch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m[37m [39;49;00m||[37m [39;49;00mch[37m [39;49;00m==[37m [39;49;00m[33m'[39;49;00m[33m\t[39;49;00m[33m'[39;49;00m);[37m[39;49;00m$
[37m    [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * find the index number of a string element in a container of strings[39;49;00m$
[37m   *[39;49;00m$
[37m   * @return              the index number of element in the ocntainer. -1 if element not found.[39;49;00m$
[37m   * @param container     a vector of strings.[39;49;00m$
[37m   * @param element       the element to find .[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m[36mint[39;49;00m[37m [39;49;00mASBeautifier::indexOf(vector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m&container,[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*element)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>::const_iterator[37m [39;49;00mwhere;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mwhere=[37m [39;49;00mfind(container.begin(),[37m [39;49;00mcontainer.end(),[37m [39;49;00melement);[37m[39;49;00m$
[37m    [39;49;00m[34mif[39;49;00m[37m [39;49;00m(where[37m [39;49;00m==[37m [39;49;00mcontainer.end())[37m[39;49;00m$
[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00m[34m-1[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[34melse[39;49;00m[37m[39;49;00m$
[37m      [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mwhere[37m [39;49;00m-[37m [39;49;00mcontainer.begin();[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[37m/**[39;49;00m$
[37m   * trim removes the white space surrounding a line.[39;49;00m$
[37m   *[39;49;00m$
[37m   * @return          the trimmed line.[39;49;00m$
[37m   * @param str       the line to trim.[39;49;00m$
[37m   */[39;49;00m[37m[39;49;00m$
[37m  [39;49;00mstring[37m [39;49;00mASBeautifier::trim([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&str)[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mstart[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m;[37m[39;49;00m$
[37m    [39;49;00m[36mint[39;49;00m[37m [39;49;00mend[37m [39;49;00m=[37m [39;49;00mstr.length()[37m [39;49;00m-[37m [39;49;00m[34m1[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(start[37m [39;49;00m<[37m [39;49;00mend[37m [39;49;00m&&[37m [39;49;00misWhiteSpace(str[start]))[37m[39;49;00m$
[37m      [39;49;00mstart++;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mwhile[39;49;00m[37m [39;49;00m(start[37m [39;49;00m<=[37m [39;49;00mend[37m [39;49;00m&&[37m [39;49;00misWhiteSpace(str[end]))[37m[39;49;00m$
[37m      [39;49;00mend--;[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00mstring[37m [39;49;00m[32mreturnStr[39;49;00m(str,[37m [39;49;00mstart,[37m [39;49;00mend+[34m1[39;49;00m-start);[37m[39;49;00m$
[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mreturnStr;[37m[39;49;00m$
[37m  [39;49;00m}[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifdef USES_NAMESPACE[39;49;00m[36m[39;49;00m$
}[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m/*[39;49;00m$
[37m * Copyright (c) 1998,1999,2000,2001,2002 Tal Davidson. All rights reserved.[39;49;00m$
[37m *[39;49;00m$
[37m * compiler_defines.h   (1 January 1999)[39;49;00m$
[37m * by Tal Davidson (davidsont@bigfoot.com)[39;49;00m$
[37m * This file is a part of "Artistic Style" - an indentater and reformatter[39;49;00m$
[37m * of C, C++, C# and Java source files.[39;49;00m$
[37m *[39;49;00m$
[37m * The "Artistic Style" project, including all files needed to compile it,[39;49;00m$
[37m * is free software; you can redistribute it and/or use it and/or modify it[39;49;00m$
[37m * under the terms of the GNU General Public License as published [39;49;00m$
[37m * by the Free Software Foundation; either version 2 of the License, [39;49;00m$
[37m * or (at your option) any later version.[39;49;00m$
[37m *[39;49;00m$
[37m * This program is distributed in the hope that it will be useful,[39;49;00m$
[37m * but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m$
[37m * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.[39;49;00m$
[37m *[39;49;00m$
[37m * You should have received a copy of the GNU General Public[39;49;00m$
[37m * License along with this program.[39;49;00m$
[37m */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mifndef ASBEAUTIFIER_H[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine ASBEAUTIFIER_H[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"ASResource.h"[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"compiler_defines.h"[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"ASSourceIterator.h"[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<string>[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<vector>[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[34musing[39;49;00m[37m [39;49;00m[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mstd[39;49;00m;[37m[39;49;00m$
[37m[39;49;00m$
[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mastyle[39;49;00m[37m[39;49;00m$
[37m  [39;49;00m{[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[34menum[39;49;00m[37m [39;49;00m[04m[32mBracketMode[39;49;00m[37m   [39;49;00m{[37m [39;49;00mNONE_MODE,[37m [39;49;00mATTACH_MODE,[37m [39;49;00mBREAK_MODE,[37m [39;49;00mBDAC_MODE[37m [39;49;00m};[37m[39;49;00m$
[37m  [39;49;00m[34menum[39;49;00m[37m [39;49;00m[04m[32mBracketType[39;49;00m[37m   [39;49;00m{[37m [39;49;00mNULL_TYPE[37m [39;49;00m=[37m [39;49;00m[34m0[39;49;00m,[37m[39;49;00m$
[37m                       [39;49;00mDEFINITION_TYPE[37m [39;49;00m=[37m [39;49;00m[34m1[39;49;00m,[37m[39;49;00m$
[37m                       [39;49;00mCOMMAND_TYPE[37m [39;49;00m=[37m [39;49;00m[34m2[39;49;00m,[37m[39;49;00m$
[37m                       [39;49;00mARRAY_TYPE[37m  [39;49;00m=[37m [39;49;00m[34m4[39;49;00m,[37m[39;49;00m$
[37m                       [39;49;00mSINGLE_LINE_TYPE[37m [39;49;00m=[37m [39;49;00m[34m8[39;49;00m};[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m  [39;49;00m[34mclass[39;49;00m[37m [39;49;00m[04m[32mASBeautifier[39;49;00m[37m [39;49;00m:[37m [39;49;00m[34mprotected[39;49;00m[37m [39;49;00mASResource[37m[39;49;00m$
[37m    [39;49;00m{[37m[39;49;00m$
[37m    [39;49;00m[34mpublic[39;49;00m:[37m[39;49;00m$
[37m      [39;49;00mASBeautifier();[37m[39;49;00m$
[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00m~ASBeautifier();[37m[39;49;00m$
[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32minit[39;49;00m(ASSourceIterator*[37m [39;49;00miter);[37m [39;49;00m[37m// pointer to dynamically created iterator.[39;49;00m$
[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32minit[39;49;00m();[37m[39;49;00m$
[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00m[32mhasMoreLines[39;49;00m()[37m [39;49;00m[34mconst[39;49;00m;[37m[39;49;00m$
[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00mstring[37m [39;49;00m[32mnextLine[39;49;00m();[37m[39;49;00m$
[37m      [39;49;00m[34mvirtual[39;49;00m[37m [39;49;00mstring[37m [39;49;00m[32mbeautify[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line);[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetTabIndentation[39;49;00m([36mint[39;49;00m[37m [39;49;00mlength[37m [39;49;00m=[37m [39;49;00m[34m4[39;49;00m,[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mforceTabs[37m [39;49;00m=[37m [39;49;00m[36mfalse[39;49;00m);[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetSpaceIndentation[39;49;00m([36mint[39;49;00m[37m [39;49;00mlength[37m [39;49;00m=[37m [39;49;00m[34m4[39;49;00m);[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetMaxInStatementIndentLength[39;49;00m([36mint[39;49;00m[37m [39;49;00mmax);[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetMinConditionalIndentLength[39;49;00m([36mint[39;49;00m[37m [39;49;00mmin);[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetClassIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetSwitchIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetCaseIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetBracketIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetBlockIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetNamespaceIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetLabelIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetCStyle[39;49;00m();[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetJavaStyle[39;49;00m();[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetEmptyLineFill[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32msetPreprocessorIndent[39;49;00m([36mbool[39;49;00m[37m [39;49;00mstate);[37m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mprotected[39;49;00m:[37m[39;49;00m$
[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mgetNextProgramCharDistance([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi);[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00m[32misLegalNameChar[39;49;00m([36mchar[39;49;00m[37m [39;49;00mch)[37m [39;49;00m[34mconst[39;49;00m;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00m[32misWhiteSpace[39;49;00m([36mchar[39;49;00m[37m [39;49;00mch)[37m [39;49;00m[34mconst[39;49;00m;[37m[39;49;00m$
[37m      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*[32mfindHeader[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi,[37m[39;49;00m$
[37m                               [39;49;00m[34mconst[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m&possibleHeaders,[37m[39;49;00m$
[37m                               [39;49;00m[36mbool[39;49;00m[37m [39;49;00mcheckBoundry[37m [39;49;00m=[37m [39;49;00m[36mtrue[39;49;00m);[37m[39;49;00m$
[37m      [39;49;00mstring[37m [39;49;00m[32mtrim[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&str);[37m[39;49;00m$
[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00m[32mindexOf[39;49;00m(vector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m&container,[37m [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*element);[37m[39;49;00m$
[37m[39;49;00m$
[37m    [39;49;00m[34mprivate[39;49;00m:[37m[39;49;00m$
[37m      [39;49;00mASBeautifier([34mconst[39;49;00m[37m [39;49;00mASBeautifier[37m [39;49;00m&copy);[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[34moperator[39;49;00m=(ASBeautifier&);[37m [39;49;00m[37m// not to be implemented[39;49;00m$
[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32minitStatic[39;49;00m();[37m[39;49;00m$
[37m      [39;49;00m[36mvoid[39;49;00m[37m [39;49;00m[32mregisterInStatementIndent[39;49;00m([34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m&line,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mi,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mspaceTabCount,[37m[39;49;00m$
[37m                                     [39;49;00m[36mint[39;49;00m[37m [39;49;00mminIndent,[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mupdateParenStack);[37m[39;49;00m$
[37m      [39;49;00mstring[37m [39;49;00m[32mpreLineWS[39;49;00m([36mint[39;49;00m[37m [39;49;00mspaceTabCount,[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mtabCount);[37m[39;49;00m$
[37m[39;49;00m$
[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mheaders;[37m[39;49;00m$
[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mnonParenHeaders;[37m[39;49;00m$
[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mpreprocessorHeaders;[37m[39;49;00m$
[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mpreBlockStatements;[37m[39;49;00m$
[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00massignmentOperators;[37m[39;49;00m$
[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00mnonAssignmentOperators;[37m[39;49;00m$
[37m[39;49;00m$
[37m      [39;49;00m[34mstatic[39;49;00m[37m [39;49;00m[36mbool[39;49;00m[37m [39;49;00mcalledInitStatic;[37m[39;49;00m$
[37m[39;49;00m$
[37m      [39;49;00mASSourceIterator[37m [39;49;00m*sourceIterator;[37m[39;49;00m$
[37m      [39;49;00mvector<ASBeautifier*>[37m [39;49;00m*waitingBeautifierStack;[37m[39;49;00m$
[37m      [39;49;00mvector<ASBeautifier*>[37m [39;49;00m*activeBeautifierStack;[37m[39;49;00m$
[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*waitingBeautifierStackLengthStack;[37m[39;49;00m$
[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*activeBeautifierStackLengthStack;[37m[39;49;00m$
[37m      [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>[37m [39;49;00m*headerStack;[37m[39;49;00m$
[37m      [39;49;00mvector<[37m [39;49;00mvector<[34mconst[39;49;00m[37m [39;49;00mstring*>*[37m [39;49;00m>[37m [39;49;00m*tempStacks;[37m[39;49;00m$
[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*blockParenDepthStack;[37m[39;49;00m$
[37m      [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m*blockStatementStack;[37m[39;49;00m$
[37m      [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m*parenStatementStack;[37m[39;49;00m$
[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*inStatementIndentStack;[37m[39;49;00m$
[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*inStatementIndentStackSizeStack;[37m[39;49;00m$
[37m      [39;49;00mvector<[36mint[39;49;00m>[37m [39;49;00m*parenIndentStack;[37m[39;49;00m$
[37m      [39;49;00mvector<[36mbool[39;49;00m>[37m [39;49;00m*bracketBlockStateStack;[37m[39;49;00m$
[37m      [39;49;00mstring[37m [39;49;00mindentString;[37m[39;49;00m$
[37m      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*currentHeader;[37m[39;49;00m$
[37m      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*previousLastLineHeader;[37m[39;49;00m$
[37m      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*immediatelyPreviousAssignmentOp;[37m[39;49;00m$
[37m      [39;49;00m[34mconst[39;49;00m[37m [39;49;00mstring[37m [39;49;00m*probationHeader;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInQuote;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInComment;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInCase;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInQuestion;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInStatement;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInHeader;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misCStyle;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInOperator;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInTemplate;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInConst;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInDefine;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInDefineDefinition;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mclassIndent;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInClassHeader;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInClassHeaderTab;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mswitchIndent;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mcaseIndent;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mnamespaceIndent;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mbracketIndent;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mblockIndent;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mlabelIndent;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mpreprocessorIndent;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misInConditional;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00misMinimalConditinalIndentSet;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mshouldForceTabIndentation;[37m[39;49;00m$
[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mminConditionalIndent;[37m[39;49;00m$
[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mparenDepth;[37m[39;49;00m$
[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mindentLength;[37m[39;49;00m$
[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mblockTabCount;[37m[39;49;00m$
[37m      [39;49;00m[36munsigned[39;49;00m[37m [39;49;00m[36mint[39;49;00m[37m [39;49;00mleadingWhiteSpaces;[37m[39;49;00m$
[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mmaxInStatementIndent;[37m[39;49;00m$
[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mtemplateDepth;[37m[39;49;00m$
[37m      [39;49;00m[36mchar[39;49;00m[37m [39;49;00mquoteChar;[37m[39;49;00m$
[37m      [39;49;00m[36mchar[39;49;00m[37m [39;49;00mprevNonSpaceCh;[37m[39;49;00m$
[37m      [39;49;00m[36mchar[39;49;00m[37m [39;49;00mcurrentNonSpaceCh;[37m[39;49;00m$
[37m      [39;49;00m[36mchar[39;49;00m[37m [39;49;00mcurrentNonLegalCh;[37m[39;49;00m$
[37m      [39;49;00m[36mchar[39;49;00m[37m [39;49;00mprevNonLegalCh;[37m[39;49;00m$
[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mprevFinalLineSpaceTabCount;[37m[39;49;00m$
[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mprevFinalLineTabCount;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00memptyLineFill;[37m[39;49;00m$
[37m      [39;49;00m[36mbool[39;49;00m[37m [39;49;00mbackslashEndsPrevLine;[37m[39;49;00m$
[37m      [39;49;00m[36mint[39;49;00m[37m [39;49;00mdefineTabCount;[37m[39;49;00m$
[37m    [39;49;00m};[37m[39;49;00m$
}[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mendif[39;49;00m[36m[39;49;00m$
[37m/*[39;49;00m$
[37m * Copyright (c) 1998,1999,2000,2001,2002 Tal Davidson. All rights reserved.[39;49;00m$
[37m *[39;49;00m$
[37m * ASFormatter.cpp[39;49;00m$
[37m * by Tal Davidson (davidsont@bigfoot.com)[39;49;00m$
[37m * This file is a part of "Artistic Style" - an indentater and reformatter[39;49;00m$
[37m * of C, C++, C# and Java source files.[39;49;00m$
[37m *[39;49;00m$
[37m * The "Artistic Style" project, including all files needed to compile it,[39;49;00m$
[37m * is free software; you can redistribute it and/or use it and/or modify it[39;49;00m$
[37m * under the terms of the GNU General Public License as published [39;49;00m$
[37m * by the Free Software Foundation; either version 2 of the License, [39;49;00m$
[37m * or (at your option) any later version.[39;49;00m$
[37m *[39;49;00m$
[37m * This program is distributed in the hope that it will be useful,[39;49;00m$
[37m * but WITHOUT ANY WARRANTY; without even the implied warranty of[39;49;00m$
[37m * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.[39;49;00m$
[37m *[39;49;00m$
[37m * You should have received a copy of the GNU General Public[39;49;00m$
[37m * License along with this program.[39;49;00m$
[37m *[39;49;00m$
[37m *[39;49;00m$
[37m * Patches:[39;49;00m$
[37m * 26 November 1998 - Richard Bullington -[39;49;00m$
[37m *        A correction of line-breaking in headers following '}',[39;49;00m$
[37m [39;49;00m$
[37m *        was created using a variation of a  patch by Richard Bullington.[39;49;00m$
[37m * 08 May 2004[39;49;00m$
[37m *        applied   ASFormatter450670.patch.bz2, ASFormatter.cpp.patch.bz2,[39;49;00m$
[37m *                  patch1_ssvb_patch.tar.gz[39;49;00m$
[37m */[39;49;00m[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"compiler_defines.h"[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m"ASFormatter.h"[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<string>[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<cctype>[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<vector>[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<algorithm>[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36minclude[39;49;00m[37m [39;49;00m[37m<iostream>[39;49;00m[36m[39;49;00m$
[37m[39;49;00m$
[37m[39;49;00m$
[36m#[39;49;00m[36mdefine INIT_CONTAINER(container, value)     {if ( (container) != NULL ) delete (container); (container) = (value); }[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine DELETE_CONTAINER(container)          {if ( (container) != NULL ) delete (container) ; }[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mdefine IS_A(a,b)                            ( ((a) & (b)) == (b))[39;49;00m[36m[39;49;00m$
[36m#[39;49;00m[36mifdef USES_NAMESPACE[39;49;00m[36m[39;49;00m$
[34musing[39;49;00m[37m [39;49;00m[34mnamespace[39;49;00m[37m [39;49;00m[04m[36mstd[39;49;00m;$
