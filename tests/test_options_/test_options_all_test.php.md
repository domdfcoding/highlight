     1^I[36m<?php[39;49;00m$
     2^I$
     3^I[31m$disapproval_ಠ_ಠ_of_php[39;49;00m = [33m'unicode var'[39;49;00m;$
     4^I$
     5^I[31m$test[39;49;00m = [34mfunction[39;49;00m([31m$a[39;49;00m) { [31m$lambda[39;49;00m = [34m1[39;49;00m; }$
     6^I$
     7^I[33m/**[39;49;00m$
     8^I[33m *  Zip class file[39;49;00m$
     9^I[33m *[39;49;00m$
    10^I[33m *  @package     fnord.bb[39;49;00m$
    11^I[33m *  @subpackage  archive[39;49;00m$
    12^I[33m */[39;49;00m$
    13^I$
    14^I[37m// Unlock?[39;49;00m$
    15^I[34mif[39;49;00m(![36mdefined[39;49;00m([33m'UNLOCK'[39;49;00m) || !UNLOCK)$
    16^I  [34mdie[39;49;00m();$
    17^I  $
    18^I[37m// Load the parent archive class[39;49;00m$
    19^I[34mrequire_once[39;49;00m(ROOT_PATH.[33m'/classes/archive.class.php'[39;49;00m);$
    20^I$
    21^I[34mclass[39;49;00m [04m[32mZip\Zippಠ_ಠ_[39;49;00m {$
    22^I$
    23^I}$
    24^I$
    25^I[33m/**[39;49;00m$
    26^I[33m *  Zip class[39;49;00m$
    27^I[33m *[39;49;00m$
    28^I[33m *  @author      Manni <manni@fnord.name>[39;49;00m$
    29^I[33m *  @copyright   Copyright (c) 2006, Manni[39;49;00m$
    30^I[33m *  @version     1.0[39;49;00m$
    31^I[33m *  @link        http://www.pkware.com/business_and_developers/developer/popups/appnote.txt[39;49;00m$
    32^I[33m *  @link        http://mannithedark.is-a-geek.net/[39;49;00m$
    33^I[33m *  @since       1.0[39;49;00m$
    34^I[33m *  @package     fnord.bb[39;49;00m$
    35^I[33m *  @subpackage  archive[39;49;00m$
    36^I[33m */[39;49;00m$
    37^I[34mclass[39;49;00m [04m[32mZip[39;49;00m [34mextends[39;49;00m Archive {$
    38^I [33m/**[39;49;00m$
    39^I[33m  *  Outputs the zip file[39;49;00m$
    40^I[33m  *[39;49;00m$
    41^I[33m  *  This function creates the zip file with the dirs and files given.[39;49;00m$
    42^I[33m  *  If the optional parameter $file is given, the zip file is will be[39;49;00m$
    43^I[33m  *  saved at that location. Otherwise the function returns the zip file's content.[39;49;00m$
    44^I[33m  *[39;49;00m$
    45^I[33m  *  @access                   public[39;49;00m$
    46^I[33m  *[39;49;00m$
    47^I[33m  *  @link                     http://www.pkware.com/business_and_developers/developer/popups/appnote.txt[39;49;00m$
    48^I[33m  *  @param  string $filename  The path where the zip file will be saved[39;49;00m$
    49^I[33m  *[39;49;00m$
    50^I[33m  *  @return bool|string       Returns either true if the fil is sucessfully created or the content of the zip file[39;49;00m$
    51^I[33m  */[39;49;00m$
    52^I  [34mfunction[39;49;00m [32mout[39;49;00m([31m$filename[39;49;00m = [34mfalse[39;49;00m) {$
    53^I    [37m// Empty output[39;49;00m$
    54^I    [31m$file_data[39;49;00m = [34marray[39;49;00m(); [37m// Data of the file part[39;49;00m$
    55^I    [31m$cd_data[39;49;00m   = [34marray[39;49;00m(); [37m// Data of the central directory[39;49;00m$
    56^I$
    57^I    [37m// Sort dirs and files by path length[39;49;00m$
    58^I    [36muksort[39;49;00m([31m$this[39;49;00m->[36mdirs[39;49;00m,  [33m'sort_by_length'[39;49;00m);$
    59^I    [36muksort[39;49;00m([31m$this[39;49;00m->[36mfiles[39;49;00m, [33m'sort_by_length'[39;49;00m);$
    60^I$
    61^I    [37m// Handle dirs[39;49;00m$
    62^I    [34mforeach[39;49;00m([31m$this[39;49;00m->[36mdirs[39;49;00m [34mas[39;49;00m [31m$dir[39;49;00m) {$
    63^I      [31m$dir[39;49;00m .= [33m'/'[39;49;00m;$
    64^I      [37m// File part[39;49;00m$
    65^I$
    66^I      [37m// Reset dir data[39;49;00m$
    67^I      [31m$dir_data[39;49;00m = [33m''[39;49;00m;$
    68^I$
    69^I      [37m// Local file header[39;49;00m$
    70^I      [31m$dir_data[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x03[39;49;00m[33m\x04[39;49;00m[33m"[39;49;00m;      [37m// Local file header signature[39;49;00m$
    71^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m10[39;49;00m);           [37m// Version needed to extract[39;49;00m$
    72^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// General purpose bit flag[39;49;00m$
    73^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Compression method[39;49;00m$
    74^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Last mod file time[39;49;00m$
    75^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Last mod file date[39;49;00m$
    76^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// crc-32[39;49;00m$
    77^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Compressed size[39;49;00m$
    78^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Uncompressed size[39;49;00m$
    79^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$dir[39;49;00m)); [37m// File name length[39;49;00m$
    80^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Extra field length[39;49;00m$
    81^I$
    82^I      [31m$dir_data[39;49;00m .= [31m$dir[39;49;00m;                    [37m// File name[39;49;00m$
    83^I      [31m$dir_data[39;49;00m .= [33m''[39;49;00m;                      [37m// Extra field (is empty)[39;49;00m$
    84^I$
    85^I      [37m// File data[39;49;00m$
    86^I      [31m$dir_data[39;49;00m .= [33m''[39;49;00m;                      [37m// Dirs have no file data[39;49;00m$
    87^I$
    88^I      [37m// Data descriptor[39;49;00m$
    89^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// crc-32[39;49;00m$
    90^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Compressed size[39;49;00m$
    91^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Uncompressed size[39;49;00m$
    92^I$
    93^I      [37m// Save current offset[39;49;00m$
    94^I      [31m$offset[39;49;00m = [36mstrlen[39;49;00m([36mimplode[39;49;00m([33m''[39;49;00m, [31m$file_data[39;49;00m));$
    95^I$
    96^I      [37m// Append dir data to the file part[39;49;00m$
    97^I      [31m$file_data[39;49;00m[] = [31m$dir_data[39;49;00m;$
    98^I$
    99^I      [37m// Central directory[39;49;00m$
   100^I$
   101^I      [37m// Reset dir data[39;49;00m$
   102^I      [31m$dir_data[39;49;00m = [33m''[39;49;00m;$
   103^I$
   104^I      [37m// File header[39;49;00m$
   105^I      [31m$dir_data[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x01[39;49;00m[33m\x02[39;49;00m[33m"[39;49;00m;      [37m// Local file header signature[39;49;00m$
   106^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Version made by[39;49;00m$
   107^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m10[39;49;00m);           [37m// Version needed to extract[39;49;00m$
   108^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// General purpose bit flag[39;49;00m$
   109^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Compression method[39;49;00m$
   110^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Last mod file time[39;49;00m$
   111^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Last mod file date[39;49;00m$
   112^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// crc-32[39;49;00m$
   113^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Compressed size[39;49;00m$
   114^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Uncompressed size[39;49;00m$
   115^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$dir[39;49;00m)); [37m// File name length[39;49;00m$
   116^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Extra field length[39;49;00m$
   117^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// File comment length[39;49;00m$
   118^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Disk number start[39;49;00m$
   119^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Internal file attributes[39;49;00m$
   120^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m16[39;49;00m);           [37m// External file attributes[39;49;00m$
   121^I      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [31m$offset[39;49;00m);      [37m// Relative offset of local header[39;49;00m$
   122^I$
   123^I      [31m$dir_data[39;49;00m .= [31m$dir[39;49;00m;                    [37m// File name[39;49;00m$
   124^I      [31m$dir_data[39;49;00m .= [33m''[39;49;00m;                      [37m// Extra field (is empty)[39;49;00m$
   125^I      [31m$dir_data[39;49;00m .= [33m''[39;49;00m;                      [37m// File comment (is empty)[39;49;00m$
   126^I$
   127^I      [37m/*[39;49;00m$
   128^I[37m      // Data descriptor[39;49;00m$
   129^I[37m      $dir_data .= pack("V", 0);            // crc-32[39;49;00m$
   130^I[37m      $dir_data .= pack("V", 0);            // Compressed size[39;49;00m$
   131^I[37m      $dir_data .= pack("V", 0);            // Uncompressed size[39;49;00m$
   132^I[37m      */[39;49;00m$
   133^I      $
   134^I      [37m// Append dir data to the central directory data[39;49;00m$
   135^I      [31m$cd_data[39;49;00m[] = [31m$dir_data[39;49;00m;$
   136^I    }$
   137^I$
   138^I    [37m// Handle files[39;49;00m$
   139^I    [34mforeach[39;49;00m([31m$this[39;49;00m->[36mfiles[39;49;00m [34mas[39;49;00m [31m$name[39;49;00m => [31m$file[39;49;00m) {$
   140^I      [37m// Get values[39;49;00m$
   141^I      [31m$content[39;49;00m = [31m$file[39;49;00m[[34m0[39;49;00m];$
   142^I    $
   143^I      [37m// File part[39;49;00m$
   144^I$
   145^I      [37m// Reset file data[39;49;00m$
   146^I      [31m$fd[39;49;00m = [33m''[39;49;00m;$
   147^I      $
   148^I      [37m// Detect possible compressions[39;49;00m$
   149^I      [37m// Use deflate[39;49;00m$
   150^I      [34mif[39;49;00m([36mfunction_exists[39;49;00m([33m'gzdeflate'[39;49;00m)) {$
   151^I        [31m$method[39;49;00m = [34m8[39;49;00m;$
   152^I$
   153^I        [37m// Compress file content[39;49;00m$
   154^I        [31m$compressed_data[39;49;00m = [36mgzdeflate[39;49;00m([31m$content[39;49;00m);$
   155^I$
   156^I      [37m// Use bzip2[39;49;00m$
   157^I      } [34melseif[39;49;00m([36mfunction_exists[39;49;00m([33m'bzcompress'[39;49;00m)) {$
   158^I        [31m$method[39;49;00m = [34m12[39;49;00m;$
   159^I$
   160^I        [37m// Compress file content[39;49;00m$
   161^I        [31m$compressed_data[39;49;00m = [36mbzcompress[39;49;00m([31m$content[39;49;00m);$
   162^I$
   163^I      [37m// No compression[39;49;00m$
   164^I      } [34melse[39;49;00m {$
   165^I        [31m$method[39;49;00m = [34m0[39;49;00m;$
   166^I$
   167^I        [37m// Do not compress the content :P[39;49;00m$
   168^I        [31m$compressed_data[39;49;00m = [31m$content[39;49;00m;$
   169^I      }$
   170^I$
   171^I      [37m// Local file header[39;49;00m$
   172^I      [31m$fd[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x03[39;49;00m[33m\x04[39;49;00m[33m"[39;49;00m;                  [37m// Local file header signature[39;49;00m$
   173^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m20[39;49;00m);                       [37m// Version needed to extract[39;49;00m$
   174^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// General purpose bit flag[39;49;00m$
   175^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [31m$method[39;49;00m);                  [37m// Compression method[39;49;00m$
   176^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Last mod file time[39;49;00m$
   177^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Last mod file date[39;49;00m$
   178^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mcrc32[39;49;00m([31m$content[39;49;00m));          [37m// crc-32[39;49;00m$
   179^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$compressed_data[39;49;00m)); [37m// Compressed size[39;49;00m$
   180^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$content[39;49;00m));         [37m// Uncompressed size[39;49;00m$
   181^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$name[39;49;00m));            [37m// File name length[39;49;00m$
   182^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Extra field length[39;49;00m$
   183^I$
   184^I      [31m$fd[39;49;00m .= [31m$name[39;49;00m;                               [37m// File name[39;49;00m$
   185^I      [31m$fd[39;49;00m .= [33m''[39;49;00m;                                  [37m// Extra field (is empty)[39;49;00m$
   186^I$
   187^I      [37m// File data[39;49;00m$
   188^I      [31m$fd[39;49;00m .= [31m$compressed_data[39;49;00m;$
   189^I      $
   190^I      [37m// Data descriptor[39;49;00m$
   191^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mcrc32[39;49;00m([31m$content[39;49;00m));          [37m// crc-32[39;49;00m$
   192^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$compressed_data[39;49;00m)); [37m// Compressed size[39;49;00m$
   193^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$content[39;49;00m));         [37m// Uncompressed size[39;49;00m$
   194^I$
   195^I      [37m// Save current offset[39;49;00m$
   196^I      [31m$offset[39;49;00m = [36mstrlen[39;49;00m([36mimplode[39;49;00m([33m''[39;49;00m, [31m$file_data[39;49;00m));$
   197^I$
   198^I      [37m// Append file data to the file part[39;49;00m$
   199^I      [31m$file_data[39;49;00m[] = [31m$fd[39;49;00m;$
   200^I$
   201^I      [37m// Central directory[39;49;00m$
   202^I$
   203^I      [37m// Reset file data[39;49;00m$
   204^I      [31m$fd[39;49;00m = [33m''[39;49;00m;$
   205^I$
   206^I      [37m// File header[39;49;00m$
   207^I      [31m$fd[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x01[39;49;00m[33m\x02[39;49;00m[33m"[39;49;00m;                  [37m// Local file header signature[39;49;00m$
   208^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Version made by[39;49;00m$
   209^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m20[39;49;00m);                       [37m// Version needed to extract[39;49;00m$
   210^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// General purpose bit flag[39;49;00m$
   211^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [31m$method[39;49;00m);                  [37m// Compression method[39;49;00m$
   212^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Last mod file time[39;49;00m$
   213^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Last mod file date[39;49;00m$
   214^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mcrc32[39;49;00m([31m$content[39;49;00m));          [37m// crc-32[39;49;00m$
   215^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$compressed_data[39;49;00m)); [37m// Compressed size[39;49;00m$
   216^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$content[39;49;00m));         [37m// Uncompressed size[39;49;00m$
   217^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$name[39;49;00m));            [37m// File name length[39;49;00m$
   218^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Extra field length[39;49;00m$
   219^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// File comment length[39;49;00m$
   220^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Disk number start[39;49;00m$
   221^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Internal file attributes[39;49;00m$
   222^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m32[39;49;00m);                       [37m// External file attributes[39;49;00m$
   223^I      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [31m$offset[39;49;00m);                  [37m// Relative offset of local header[39;49;00m$
   224^I$
   225^I      [31m$fd[39;49;00m .= [31m$name[39;49;00m;                               [37m// File name[39;49;00m$
   226^I      [31m$fd[39;49;00m .= [33m''[39;49;00m;                                  [37m// Extra field (is empty)[39;49;00m$
   227^I      [31m$fd[39;49;00m .= [33m''[39;49;00m;                                  [37m// File comment (is empty)[39;49;00m$
   228^I$
   229^I      [37m/*[39;49;00m$
   230^I[37m      // Data descriptor[39;49;00m$
   231^I[37m      $fd .= pack("V", crc32($content));          // crc-32[39;49;00m$
   232^I[37m      $fd .= pack("V", strlen($compressed_data)); // Compressed size[39;49;00m$
   233^I[37m      $fd .= pack("V", strlen($content));         // Uncompressed size[39;49;00m$
   234^I[37m      */[39;49;00m$
   235^I$
   236^I      [37m// Append file data to the central directory data[39;49;00m$
   237^I      [31m$cd_data[39;49;00m[] = [31m$fd[39;49;00m;$
   238^I    }$
   239^I$
   240^I    [37m// Digital signature[39;49;00m$
   241^I    [31m$digital_signature[39;49;00m = [33m''[39;49;00m;$
   242^I    [31m$digital_signature[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x05[39;49;00m[33m\x05[39;49;00m[33m"[39;49;00m;  [37m// Header signature[39;49;00m$
   243^I    [31m$digital_signature[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);        [37m// Size of data[39;49;00m$
   244^I    [31m$digital_signature[39;49;00m .= [33m''[39;49;00m;                  [37m// Signature data (is empty)[39;49;00m$
   245^I$
   246^I    [31m$tmp_file_data[39;49;00m = [36mimplode[39;49;00m([33m''[39;49;00m, [31m$file_data[39;49;00m);  [37m// File data[39;49;00m$
   247^I    [31m$tmp_cd_data[39;49;00m   = [36mimplode[39;49;00m([33m''[39;49;00m, [31m$cd_data[39;49;00m).    [37m// Central directory[39;49;00m$
   248^I                     [31m$digital_signature[39;49;00m;       [37m// Digital signature[39;49;00m$
   249^I$
   250^I    [37m// End of central directory[39;49;00m$
   251^I    [31m$eof_cd[39;49;00m = [33m''[39;49;00m;$
   252^I    [31m$eof_cd[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x05[39;49;00m[33m\x06[39;49;00m[33m"[39;49;00m;                [37m// End of central dir signature[39;49;00m$
   253^I    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                      [37m// Number of this disk[39;49;00m$
   254^I    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                      [37m// Number of the disk with the start of the central directory[39;49;00m$
   255^I    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mcount[39;49;00m([31m$cd_data[39;49;00m));        [37m// Total number of entries in the central directory on this disk[39;49;00m$
   256^I    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mcount[39;49;00m([31m$cd_data[39;49;00m));        [37m// Total number of entries in the central directory[39;49;00m$
   257^I    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$tmp_cd_data[39;49;00m));   [37m// Size of the central directory[39;49;00m$
   258^I    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$tmp_file_data[39;49;00m)); [37m// Offset of start of central directory with respect to the starting disk number[39;49;00m$
   259^I    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                      [37m// .ZIP file comment length[39;49;00m$
   260^I    [31m$eof_cd[39;49;00m .= [33m''[39;49;00m;                                [37m// .ZIP file comment (is empty)[39;49;00m$
   261^I$
   262^I    [37m// Content of the zip file[39;49;00m$
   263^I    [31m$data[39;49;00m = [31m$tmp_file_data[39;49;00m.$
   264^I            [37m// $extra_data_record.[39;49;00m$
   265^I            [31m$tmp_cd_data[39;49;00m.$
   266^I            [31m$eof_cd[39;49;00m;$
   267^I$
   268^I    [37m// Return content?[39;49;00m$
   269^I    [34mif[39;49;00m(![31m$filename[39;49;00m)$
   270^I      [34mreturn[39;49;00m [31m$data[39;49;00m;$
   271^I      $
   272^I    [37m// Write to file[39;49;00m$
   273^I    [34mreturn[39;49;00m [36mfile_put_contents[39;49;00m([31m$filename[39;49;00m, [31m$data[39;49;00m);$
   274^I  }$
   275^I  $
   276^I [33m/**[39;49;00m$
   277^I[33m  *  Load a zip file[39;49;00m$
   278^I[33m  *[39;49;00m$
   279^I[33m  *  This function loads the files and dirs from a zip file from the harddrive.[39;49;00m$
   280^I[33m  *[39;49;00m$
   281^I[33m  *  @access                public[39;49;00m$
   282^I[33m  *[39;49;00m$
   283^I[33m  *  @param  string $file   The path to the zip file[39;49;00m$
   284^I[33m  *  @param  bool   $reset  Reset the files and dirs before adding the zip file's content?[39;49;00m$
   285^I[33m  *[39;49;00m$
   286^I[33m  *  @return bool           Returns true if the file was loaded sucessfully[39;49;00m$
   287^I[33m  */[39;49;00m$
   288^I  [34mfunction[39;49;00m [32mload_file[39;49;00m([31m$file[39;49;00m, [31m$reset[39;49;00m = [34mtrue[39;49;00m) {$
   289^I    [37m// Check whether the file exists[39;49;00m$
   290^I    [34mif[39;49;00m(![36mfile_exists[39;49;00m([31m$file[39;49;00m))$
   291^I      [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   292^I$
   293^I    [37m// Load the files content[39;49;00m$
   294^I    [31m$content[39;49;00m = @[36mfile_get_contents[39;49;00m([31m$file[39;49;00m);$
   295^I$
   296^I    [37m// Return false if the file cannot be opened[39;49;00m$
   297^I    [34mif[39;49;00m(![31m$content[39;49;00m)$
   298^I      [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   299^I$
   300^I    [37m// Read the zip[39;49;00m$
   301^I    [34mreturn[39;49;00m [31m$this[39;49;00m->[36mload_string[39;49;00m([31m$content[39;49;00m, [31m$reset[39;49;00m);$
   302^I  }$
   303^I  $
   304^I [33m/**[39;49;00m$
   305^I[33m  *  Load a zip string[39;49;00m$
   306^I[33m  *[39;49;00m$
   307^I[33m  *  This function loads the files and dirs from a string[39;49;00m$
   308^I[33m  *[39;49;00m$
   309^I[33m  *  @access                 public[39;49;00m$
   310^I[33m  *[39;49;00m$
   311^I[33m  *  @param  string $string  The string the zip is generated from[39;49;00m$
   312^I[33m  *  @param  bool   $reset   Reset the files and dirs before adding the zip file's content?[39;49;00m$
   313^I[33m  *[39;49;00m$
   314^I[33m  *  @return bool            Returns true if the string was loaded sucessfully[39;49;00m$
   315^I[33m  */[39;49;00m$
   316^I  [34mfunction[39;49;00m [32mload_string[39;49;00m([31m$string[39;49;00m, [31m$reset[39;49;00m = [34mtrue[39;49;00m) {$
   317^I    [37m// Reset the zip?[39;49;00m$
   318^I    [34mif[39;49;00m([31m$reset[39;49;00m) {$
   319^I      [31m$this[39;49;00m->[36mdirs[39;49;00m  = [34marray[39;49;00m();$
   320^I      [31m$this[39;49;00m->[36mfiles[39;49;00m = [34marray[39;49;00m();$
   321^I    }$
   322^I$
   323^I    [37m// Get the starting position of the end of central directory record[39;49;00m$
   324^I    [31m$start[39;49;00m = [36mstrpos[39;49;00m([31m$string[39;49;00m, [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x05[39;49;00m[33m\x06[39;49;00m[33m"[39;49;00m);$
   325^I$
   326^I    [37m// Error[39;49;00m$
   327^I    [34mif[39;49;00m([31m$start[39;49;00m === [34mfalse[39;49;00m)$
   328^I      [34mdie[39;49;00m([33m'Could not find the end of central directory record'[39;49;00m);$
   329^I$
   330^I    [37m// Get the ecdr[39;49;00m$
   331^I    [31m$eof_cd[39;49;00m = [36msubstr[39;49;00m([31m$string[39;49;00m, [31m$start[39;49;00m+[34m4[39;49;00m, [34m18[39;49;00m);$
   332^I$
   333^I    [37m// Unpack the ecdr infos[39;49;00m$
   334^I    [31m$eof_cd[39;49;00m = [36munpack[39;49;00m([33m'vdisc1/'[39;49;00m.$
   335^I                     [33m'vdisc2/'[39;49;00m.$
   336^I                     [33m'ventries1/'[39;49;00m.$
   337^I                     [33m'ventries2/'[39;49;00m.$
   338^I                     [33m'Vsize/'[39;49;00m.$
   339^I                     [33m'Voffset/'[39;49;00m.$
   340^I                     [33m'vcomment_lenght'[39;49;00m, [31m$eof_cd[39;49;00m);$
   341^I$
   342^I    [37m// Do not allow multi disc zips[39;49;00m$
   343^I    [34mif[39;49;00m([31m$eof_cd[39;49;00m[[33m'disc1'[39;49;00m] != [34m0[39;49;00m)$
   344^I      [34mdie[39;49;00m([33m'multi disk stuff is not yet implemented :/'[39;49;00m);$
   345^I$
   346^I    [37m// Save the interesting values[39;49;00m$
   347^I    [31m$cd_entries[39;49;00m = [31m$eof_cd[39;49;00m[[33m'entries1'[39;49;00m];$
   348^I    [31m$cd_size[39;49;00m    = [31m$eof_cd[39;49;00m[[33m'size'[39;49;00m];$
   349^I    [31m$cd_offset[39;49;00m  = [31m$eof_cd[39;49;00m[[33m'offset'[39;49;00m];$
   350^I$
   351^I    [37m// Get the central directory record[39;49;00m$
   352^I    [31m$cdr[39;49;00m = [36msubstr[39;49;00m([31m$string[39;49;00m, [31m$cd_offset[39;49;00m, [31m$cd_size[39;49;00m);$
   353^I$
   354^I    [37m// Reset the position and the list of the entries[39;49;00m$
   355^I    [31m$pos[39;49;00m     = [34m0[39;49;00m;$
   356^I    [31m$entries[39;49;00m = [34marray[39;49;00m();$
   357^I$
   358^I    [37m// Handle cdr[39;49;00m$
   359^I    [34mwhile[39;49;00m([31m$pos[39;49;00m < [36mstrlen[39;49;00m([31m$cdr[39;49;00m)) {$
   360^I      [37m// Check header signature[39;49;00m$
   361^I      [37m// Digital signature[39;49;00m$
   362^I      [34mif[39;49;00m([36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m, [34m4[39;49;00m) == [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x05[39;49;00m[33m\x05[39;49;00m[33m"[39;49;00m) {$
   363^I        [37m// Get digital signature size[39;49;00m$
   364^I        [31m$tmp_info[39;49;00m = [36munpack[39;49;00m([33m'vsize'[39;49;00m, [36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m + [34m4[39;49;00m, [34m2[39;49;00m));$
   365^I$
   366^I        [37m// Read out the digital signature[39;49;00m$
   367^I        [31m$digital_sig[39;49;00m = [36msubstr[39;49;00m([31m$header[39;49;00m, [31m$pos[39;49;00m + [34m6[39;49;00m, [31m$tmp_info[39;49;00m[[33m'size'[39;49;00m]);$
   368^I$
   369^I        [34mbreak[39;49;00m;$
   370^I      }$
   371^I$
   372^I      [37m// Get file header[39;49;00m$
   373^I      [31m$header[39;49;00m = [36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m, [34m46[39;49;00m);$
   374^I$
   375^I      [37m// Unpack the header information[39;49;00m$
   376^I      [31m$header_info[39;49;00m = @[36munpack[39;49;00m([33m'Vheader/'[39;49;00m.$
   377^I                             [33m'vversion_made_by/'[39;49;00m.$
   378^I                             [33m'vversion_needed/'[39;49;00m.$
   379^I                             [33m'vgeneral_purpose/'[39;49;00m.$
   380^I                             [33m'vcompression_method/'[39;49;00m.$
   381^I                             [33m'vlast_mod_time/'[39;49;00m.$
   382^I                             [33m'vlast_mod_date/'[39;49;00m.$
   383^I                             [33m'Vcrc32/'[39;49;00m.$
   384^I                             [33m'Vcompressed_size/'[39;49;00m.$
   385^I                             [33m'Vuncompressed_size/'[39;49;00m.$
   386^I                             [33m'vname_length/'[39;49;00m.$
   387^I                             [33m'vextra_length/'[39;49;00m.$
   388^I                             [33m'vcomment_length/'[39;49;00m.$
   389^I                             [33m'vdisk_number/'[39;49;00m.$
   390^I                             [33m'vinternal_attributes/'[39;49;00m.$
   391^I                             [33m'Vexternal_attributes/'[39;49;00m.$
   392^I                             [33m'Voffset'[39;49;00m,$
   393^I                             [31m$header[39;49;00m);$
   394^I$
   395^I      [37m// Valid header?[39;49;00m$
   396^I      [34mif[39;49;00m([31m$header_info[39;49;00m[[33m'header'[39;49;00m] != [34m33639248[39;49;00m)$
   397^I        [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   398^I$
   399^I      [37m// New position[39;49;00m$
   400^I      [31m$pos[39;49;00m += [34m46[39;49;00m;$
   401^I$
   402^I      [37m// Read out the file name[39;49;00m$
   403^I      [31m$header_info[39;49;00m[[33m'name'[39;49;00m] = [36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m, [31m$header_info[39;49;00m[[33m'name_length'[39;49;00m]);$
   404^I$
   405^I      [37m// New position[39;49;00m$
   406^I      [31m$pos[39;49;00m += [31m$header_info[39;49;00m[[33m'name_length'[39;49;00m];$
   407^I$
   408^I      [37m// Read out the extra stuff[39;49;00m$
   409^I      [31m$header_info[39;49;00m[[33m'extra'[39;49;00m] = [36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m, [31m$header_info[39;49;00m[[33m'extra_length'[39;49;00m]);$
   410^I$
   411^I      [37m// New position[39;49;00m$
   412^I      [31m$pos[39;49;00m += [31m$header_info[39;49;00m[[33m'extra_length'[39;49;00m];$
   413^I$
   414^I      [37m// Read out the comment[39;49;00m$
   415^I      [31m$header_info[39;49;00m[[33m'comment'[39;49;00m] = [36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m, [31m$header_info[39;49;00m[[33m'comment_length'[39;49;00m]);$
   416^I$
   417^I      [37m// New position[39;49;00m$
   418^I      [31m$pos[39;49;00m += [31m$header_info[39;49;00m[[33m'comment_length'[39;49;00m];$
   419^I$
   420^I      [37m// Append this file/dir to the entry list[39;49;00m$
   421^I      [31m$entries[39;49;00m[] = [31m$header_info[39;49;00m;$
   422^I    }$
   423^I$
   424^I    [37m// Check whether all entries where read sucessfully[39;49;00m$
   425^I    [34mif[39;49;00m([36mcount[39;49;00m([31m$entries[39;49;00m) != [31m$cd_entries[39;49;00m)$
   426^I      [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   427^I$
   428^I    [37m// Handle files/dirs[39;49;00m$
   429^I    [34mforeach[39;49;00m([31m$entries[39;49;00m [34mas[39;49;00m [31m$entry[39;49;00m) {$
   430^I      [37m// Is a dir?[39;49;00m$
   431^I      [34mif[39;49;00m([31m$entry[39;49;00m[[33m'external_attributes'[39;49;00m] & [34m16[39;49;00m) {$
   432^I        [31m$this[39;49;00m->[36madd_dir[39;49;00m([31m$entry[39;49;00m[[33m'name'[39;49;00m]);$
   433^I        [34mcontinue[39;49;00m;$
   434^I      }$
   435^I$
   436^I      [37m// Get local file header[39;49;00m$
   437^I      [31m$header[39;49;00m = [36msubstr[39;49;00m([31m$string[39;49;00m, [31m$entry[39;49;00m[[33m'offset'[39;49;00m], [34m30[39;49;00m);$
   438^I$
   439^I      [37m// Unpack the header information[39;49;00m$
   440^I      [31m$header_info[39;49;00m = @[36munpack[39;49;00m([33m'Vheader/'[39;49;00m.$
   441^I                             [33m'vversion_needed/'[39;49;00m.$
   442^I                             [33m'vgeneral_purpose/'[39;49;00m.$
   443^I                             [33m'vcompression_method/'[39;49;00m.$
   444^I                             [33m'vlast_mod_time/'[39;49;00m.$
   445^I                             [33m'vlast_mod_date/'[39;49;00m.$
   446^I                             [33m'Vcrc32/'[39;49;00m.$
   447^I                             [33m'Vcompressed_size/'[39;49;00m.$
   448^I                             [33m'Vuncompressed_size/'[39;49;00m.$
   449^I                             [33m'vname_length/'[39;49;00m.$
   450^I                             [33m'vextra_length'[39;49;00m,$
   451^I                             [31m$header[39;49;00m);$
   452^I$
   453^I      [37m// Valid header?[39;49;00m$
   454^I      [34mif[39;49;00m([31m$header_info[39;49;00m[[33m'header'[39;49;00m] != [34m67324752[39;49;00m)$
   455^I        [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   456^I$
   457^I      [37m// Get content start position[39;49;00m$
   458^I      [31m$start[39;49;00m = [31m$entry[39;49;00m[[33m'offset'[39;49;00m] + [34m30[39;49;00m + [31m$header_info[39;49;00m[[33m'name_length'[39;49;00m] + [31m$header_info[39;49;00m[[33m'extra_length'[39;49;00m];$
   459^I$
   460^I      [37m// Get the compressed data[39;49;00m$
   461^I      [31m$data[39;49;00m = [36msubstr[39;49;00m([31m$string[39;49;00m, [31m$start[39;49;00m, [31m$header_info[39;49;00m[[33m'compressed_size'[39;49;00m]);$
   462^I$
   463^I      [37m// Detect compression type[39;49;00m$
   464^I      [34mswitch[39;49;00m([31m$header_info[39;49;00m[[33m'compression_method'[39;49;00m]) {$
   465^I        [37m// No compression[39;49;00m$
   466^I        [34mcase[39;49;00m [34m0[39;49;00m:$
   467^I          [37m// Ne decompression needed[39;49;00m$
   468^I          [31m$content[39;49;00m = [31m$data[39;49;00m;$
   469^I          [34mbreak[39;49;00m;$
   470^I$
   471^I        [37m// Gzip[39;49;00m$
   472^I        [34mcase[39;49;00m [34m8[39;49;00m:$
   473^I          [34mif[39;49;00m(![36mfunction_exists[39;49;00m([33m'gzinflate'[39;49;00m))$
   474^I            [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   475^I$
   476^I          [37m// Uncompress data[39;49;00m$
   477^I          [31m$content[39;49;00m = [36mgzinflate[39;49;00m([31m$data[39;49;00m);$
   478^I          [34mbreak[39;49;00m;$
   479^I$
   480^I        [37m// Bzip2[39;49;00m$
   481^I        [34mcase[39;49;00m [34m12[39;49;00m:$
   482^I          [34mif[39;49;00m(![36mfunction_exists[39;49;00m([33m'bzdecompress'[39;49;00m))$
   483^I            [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   484^I$
   485^I          [37m// Decompress data[39;49;00m$
   486^I          [31m$content[39;49;00m = [36mbzdecompress[39;49;00m([31m$data[39;49;00m);$
   487^I          [34mbreak[39;49;00m;$
   488^I$
   489^I        [37m// Compression not supported -> error[39;49;00m$
   490^I        [34mdefault[39;49;00m:$
   491^I          [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   492^I      }$
   493^I$
   494^I      [37m// Try to add file[39;49;00m$
   495^I      [34mif[39;49;00m(![31m$this[39;49;00m->[36madd_file[39;49;00m([31m$entry[39;49;00m[[33m'name'[39;49;00m], [31m$content[39;49;00m))$
   496^I        [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   497^I    }$
   498^I$
   499^I    [34mreturn[39;49;00m [34mtrue[39;49;00m;$
   500^I  }$
   501^I}$
   502^I$
   503^I[34mfunction[39;49;00m &[32mbyref[39;49;00m() {$
   504^I    [31m$x[39;49;00m = [34marray[39;49;00m();$
   505^I    [34mreturn[39;49;00m [31m$x[39;49;00m;$
   506^I}$
   507^I$
   508^I[37m// Test highlighting of magic methods and variables[39;49;00m$
   509^I[34mclass[39;49;00m [04m[32mMagicClass[39;49;00m {$
   510^I  [34mpublic[39;49;00m [31m$magic_str[39;49;00m;$
   511^I  [34mpublic[39;49;00m [31m$ordinary_str[39;49;00m;$
   512^I$
   513^I  [34mpublic[39;49;00m [34mfunction[39;49;00m [32m__construct[39;49;00m([31m$some_var[39;49;00m) {$
   514^I    [31m$this[39;49;00m->[36mmagic_str[39;49;00m = [31m__FILE__[39;49;00m;$
   515^I    [31m$this[39;49;00m->[36mordinary_str[39;49;00m = [31m$some_var[39;49;00m;$
   516^I  }$
   517^I$
   518^I  [34mpublic[39;49;00m [34mfunction[39;49;00m [32m__toString[39;49;00m() {$
   519^I    [34mreturn[39;49;00m [31m$this[39;49;00m->[36mmagic_str[39;49;00m;$
   520^I  }$
   521^I$
   522^I  [34mpublic[39;49;00m [34mfunction[39;49;00m [32mnonMagic[39;49;00m() {$
   523^I    [34mreturn[39;49;00m [31m$this[39;49;00m->[36mordinary_str[39;49;00m;$
   524^I  }$
   525^I}$
   526^I$
   527^I[31m$magic[39;49;00m = [34mnew[39;49;00m MagicClass([31m__DIR__[39;49;00m);$
   528^I__toString();$
   529^I[31m$magic[39;49;00m->[36mnonMagic[39;49;00m();$
   530^I[31m$magic[39;49;00m->[36m__toString[39;49;00m();$
   531^I$
   532^I     [34mecho[39;49;00m [33m<<<[39;49;00m[33mEOF[39;49;00m[33m[39;49;00m$
   533^I[33m[39;49;00m$
   534^I[33m     Test the heredocs...[39;49;00m$
   535^I[33m[39;49;00m$
   536^I[33m     [39;49;00m[33mEOF[39;49;00m;$
   537^I$
   538^I[34mecho[39;49;00m [33m<<<[39;49;00m[33m"[39;49;00m[33msome_delimiter[39;49;00m[33m"[39;49;00m$
   539^I[33mmore heredoc testing[39;49;00m$
   540^I[33mcontinues on this line[39;49;00m$
   541^I[33msome_delimiter[39;49;00m;$
   542^I$
   543^I[36m?>[39;49;00m$
