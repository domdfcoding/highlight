     1	[36m<?php[39;49;00m$
     2	$
     3	[31m$disapproval_ಠ_ಠ_of_php[39;49;00m = [33m'unicode var'[39;49;00m;$
     4	$
     5	[31m$test[39;49;00m = [34mfunction[39;49;00m([31m$a[39;49;00m) { [31m$lambda[39;49;00m = [34m1[39;49;00m; }$
     6	$
     7	[33m/**[39;49;00m$
     8	[33m *  Zip class file[39;49;00m$
     9	[33m *[39;49;00m$
    10	[33m *  @package     fnord.bb[39;49;00m$
    11	[33m *  @subpackage  archive[39;49;00m$
    12	[33m */[39;49;00m$
    13	$
    14	[37m// Unlock?[39;49;00m$
    15	[34mif[39;49;00m(![36mdefined[39;49;00m([33m'UNLOCK'[39;49;00m) || !UNLOCK)$
    16	  [34mdie[39;49;00m();$
    17	  $
    18	[37m// Load the parent archive class[39;49;00m$
    19	[34mrequire_once[39;49;00m(ROOT_PATH.[33m'/classes/archive.class.php'[39;49;00m);$
    20	$
    21	[34mclass[39;49;00m [04m[32mZip\Zippಠ_ಠ_[39;49;00m {$
    22	$
    23	}$
    24	$
    25	[33m/**[39;49;00m$
    26	[33m *  Zip class[39;49;00m$
    27	[33m *[39;49;00m$
    28	[33m *  @author      Manni <manni@fnord.name>[39;49;00m$
    29	[33m *  @copyright   Copyright (c) 2006, Manni[39;49;00m$
    30	[33m *  @version     1.0[39;49;00m$
    31	[33m *  @link        http://www.pkware.com/business_and_developers/developer/popups/appnote.txt[39;49;00m$
    32	[33m *  @link        http://mannithedark.is-a-geek.net/[39;49;00m$
    33	[33m *  @since       1.0[39;49;00m$
    34	[33m *  @package     fnord.bb[39;49;00m$
    35	[33m *  @subpackage  archive[39;49;00m$
    36	[33m */[39;49;00m$
    37	[34mclass[39;49;00m [04m[32mZip[39;49;00m [34mextends[39;49;00m Archive {$
    38	 [33m/**[39;49;00m$
    39	[33m  *  Outputs the zip file[39;49;00m$
    40	[33m  *[39;49;00m$
    41	[33m  *  This function creates the zip file with the dirs and files given.[39;49;00m$
    42	[33m  *  If the optional parameter $file is given, the zip file is will be[39;49;00m$
    43	[33m  *  saved at that location. Otherwise the function returns the zip file's content.[39;49;00m$
    44	[33m  *[39;49;00m$
    45	[33m  *  @access                   public[39;49;00m$
    46	[33m  *[39;49;00m$
    47	[33m  *  @link                     http://www.pkware.com/business_and_developers/developer/popups/appnote.txt[39;49;00m$
    48	[33m  *  @param  string $filename  The path where the zip file will be saved[39;49;00m$
    49	[33m  *[39;49;00m$
    50	[33m  *  @return bool|string       Returns either true if the fil is sucessfully created or the content of the zip file[39;49;00m$
    51	[33m  */[39;49;00m$
    52	  [34mfunction[39;49;00m [32mout[39;49;00m([31m$filename[39;49;00m = [34mfalse[39;49;00m) {$
    53	    [37m// Empty output[39;49;00m$
    54	    [31m$file_data[39;49;00m = [34marray[39;49;00m(); [37m// Data of the file part[39;49;00m$
    55	    [31m$cd_data[39;49;00m   = [34marray[39;49;00m(); [37m// Data of the central directory[39;49;00m$
    56	$
    57	    [37m// Sort dirs and files by path length[39;49;00m$
    58	    [36muksort[39;49;00m([31m$this[39;49;00m->[36mdirs[39;49;00m,  [33m'sort_by_length'[39;49;00m);$
    59	    [36muksort[39;49;00m([31m$this[39;49;00m->[36mfiles[39;49;00m, [33m'sort_by_length'[39;49;00m);$
    60	$
    61	    [37m// Handle dirs[39;49;00m$
    62	    [34mforeach[39;49;00m([31m$this[39;49;00m->[36mdirs[39;49;00m [34mas[39;49;00m [31m$dir[39;49;00m) {$
    63	      [31m$dir[39;49;00m .= [33m'/'[39;49;00m;$
    64	      [37m// File part[39;49;00m$
    65	$
    66	      [37m// Reset dir data[39;49;00m$
    67	      [31m$dir_data[39;49;00m = [33m''[39;49;00m;$
    68	$
    69	      [37m// Local file header[39;49;00m$
    70	      [31m$dir_data[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x03[39;49;00m[33m\x04[39;49;00m[33m"[39;49;00m;      [37m// Local file header signature[39;49;00m$
    71	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m10[39;49;00m);           [37m// Version needed to extract[39;49;00m$
    72	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// General purpose bit flag[39;49;00m$
    73	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Compression method[39;49;00m$
    74	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Last mod file time[39;49;00m$
    75	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Last mod file date[39;49;00m$
    76	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// crc-32[39;49;00m$
    77	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Compressed size[39;49;00m$
    78	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Uncompressed size[39;49;00m$
    79	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$dir[39;49;00m)); [37m// File name length[39;49;00m$
    80	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Extra field length[39;49;00m$
    81	$
    82	      [31m$dir_data[39;49;00m .= [31m$dir[39;49;00m;                    [37m// File name[39;49;00m$
    83	      [31m$dir_data[39;49;00m .= [33m''[39;49;00m;                      [37m// Extra field (is empty)[39;49;00m$
    84	$
    85	      [37m// File data[39;49;00m$
    86	      [31m$dir_data[39;49;00m .= [33m''[39;49;00m;                      [37m// Dirs have no file data[39;49;00m$
    87	$
    88	      [37m// Data descriptor[39;49;00m$
    89	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// crc-32[39;49;00m$
    90	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Compressed size[39;49;00m$
    91	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Uncompressed size[39;49;00m$
    92	$
    93	      [37m// Save current offset[39;49;00m$
    94	      [31m$offset[39;49;00m = [36mstrlen[39;49;00m([36mimplode[39;49;00m([33m''[39;49;00m, [31m$file_data[39;49;00m));$
    95	$
    96	      [37m// Append dir data to the file part[39;49;00m$
    97	      [31m$file_data[39;49;00m[] = [31m$dir_data[39;49;00m;$
    98	$
    99	      [37m// Central directory[39;49;00m$
   100	$
   101	      [37m// Reset dir data[39;49;00m$
   102	      [31m$dir_data[39;49;00m = [33m''[39;49;00m;$
   103	$
   104	      [37m// File header[39;49;00m$
   105	      [31m$dir_data[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x01[39;49;00m[33m\x02[39;49;00m[33m"[39;49;00m;      [37m// Local file header signature[39;49;00m$
   106	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Version made by[39;49;00m$
   107	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m10[39;49;00m);           [37m// Version needed to extract[39;49;00m$
   108	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// General purpose bit flag[39;49;00m$
   109	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Compression method[39;49;00m$
   110	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Last mod file time[39;49;00m$
   111	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Last mod file date[39;49;00m$
   112	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// crc-32[39;49;00m$
   113	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Compressed size[39;49;00m$
   114	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Uncompressed size[39;49;00m$
   115	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$dir[39;49;00m)); [37m// File name length[39;49;00m$
   116	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Extra field length[39;49;00m$
   117	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// File comment length[39;49;00m$
   118	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Disk number start[39;49;00m$
   119	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Internal file attributes[39;49;00m$
   120	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m16[39;49;00m);           [37m// External file attributes[39;49;00m$
   121	      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [31m$offset[39;49;00m);      [37m// Relative offset of local header[39;49;00m$
   122	$
   123	      [31m$dir_data[39;49;00m .= [31m$dir[39;49;00m;                    [37m// File name[39;49;00m$
   124	      [31m$dir_data[39;49;00m .= [33m''[39;49;00m;                      [37m// Extra field (is empty)[39;49;00m$
   125	      [31m$dir_data[39;49;00m .= [33m''[39;49;00m;                      [37m// File comment (is empty)[39;49;00m$
   126	$
   127	      [37m/*[39;49;00m$
   128	[37m      // Data descriptor[39;49;00m$
   129	[37m      $dir_data .= pack("V", 0);            // crc-32[39;49;00m$
   130	[37m      $dir_data .= pack("V", 0);            // Compressed size[39;49;00m$
   131	[37m      $dir_data .= pack("V", 0);            // Uncompressed size[39;49;00m$
   132	[37m      */[39;49;00m$
   133	      $
   134	      [37m// Append dir data to the central directory data[39;49;00m$
   135	      [31m$cd_data[39;49;00m[] = [31m$dir_data[39;49;00m;$
   136	    }$
   137	$
   138	    [37m// Handle files[39;49;00m$
   139	    [34mforeach[39;49;00m([31m$this[39;49;00m->[36mfiles[39;49;00m [34mas[39;49;00m [31m$name[39;49;00m => [31m$file[39;49;00m) {$
   140	      [37m// Get values[39;49;00m$
   141	      [31m$content[39;49;00m = [31m$file[39;49;00m[[34m0[39;49;00m];$
   142	    $
   143	      [37m// File part[39;49;00m$
   144	$
   145	      [37m// Reset file data[39;49;00m$
   146	      [31m$fd[39;49;00m = [33m''[39;49;00m;$
   147	      $
   148	      [37m// Detect possible compressions[39;49;00m$
   149	      [37m// Use deflate[39;49;00m$
   150	      [34mif[39;49;00m([36mfunction_exists[39;49;00m([33m'gzdeflate'[39;49;00m)) {$
   151	        [31m$method[39;49;00m = [34m8[39;49;00m;$
   152	$
   153	        [37m// Compress file content[39;49;00m$
   154	        [31m$compressed_data[39;49;00m = [36mgzdeflate[39;49;00m([31m$content[39;49;00m);$
   155	$
   156	      [37m// Use bzip2[39;49;00m$
   157	      } [34melseif[39;49;00m([36mfunction_exists[39;49;00m([33m'bzcompress'[39;49;00m)) {$
   158	        [31m$method[39;49;00m = [34m12[39;49;00m;$
   159	$
   160	        [37m// Compress file content[39;49;00m$
   161	        [31m$compressed_data[39;49;00m = [36mbzcompress[39;49;00m([31m$content[39;49;00m);$
   162	$
   163	      [37m// No compression[39;49;00m$
   164	      } [34melse[39;49;00m {$
   165	        [31m$method[39;49;00m = [34m0[39;49;00m;$
   166	$
   167	        [37m// Do not compress the content :P[39;49;00m$
   168	        [31m$compressed_data[39;49;00m = [31m$content[39;49;00m;$
   169	      }$
   170	$
   171	      [37m// Local file header[39;49;00m$
   172	      [31m$fd[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x03[39;49;00m[33m\x04[39;49;00m[33m"[39;49;00m;                  [37m// Local file header signature[39;49;00m$
   173	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m20[39;49;00m);                       [37m// Version needed to extract[39;49;00m$
   174	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// General purpose bit flag[39;49;00m$
   175	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [31m$method[39;49;00m);                  [37m// Compression method[39;49;00m$
   176	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Last mod file time[39;49;00m$
   177	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Last mod file date[39;49;00m$
   178	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mcrc32[39;49;00m([31m$content[39;49;00m));          [37m// crc-32[39;49;00m$
   179	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$compressed_data[39;49;00m)); [37m// Compressed size[39;49;00m$
   180	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$content[39;49;00m));         [37m// Uncompressed size[39;49;00m$
   181	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$name[39;49;00m));            [37m// File name length[39;49;00m$
   182	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Extra field length[39;49;00m$
   183	$
   184	      [31m$fd[39;49;00m .= [31m$name[39;49;00m;                               [37m// File name[39;49;00m$
   185	      [31m$fd[39;49;00m .= [33m''[39;49;00m;                                  [37m// Extra field (is empty)[39;49;00m$
   186	$
   187	      [37m// File data[39;49;00m$
   188	      [31m$fd[39;49;00m .= [31m$compressed_data[39;49;00m;$
   189	      $
   190	      [37m// Data descriptor[39;49;00m$
   191	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mcrc32[39;49;00m([31m$content[39;49;00m));          [37m// crc-32[39;49;00m$
   192	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$compressed_data[39;49;00m)); [37m// Compressed size[39;49;00m$
   193	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$content[39;49;00m));         [37m// Uncompressed size[39;49;00m$
   194	$
   195	      [37m// Save current offset[39;49;00m$
   196	      [31m$offset[39;49;00m = [36mstrlen[39;49;00m([36mimplode[39;49;00m([33m''[39;49;00m, [31m$file_data[39;49;00m));$
   197	$
   198	      [37m// Append file data to the file part[39;49;00m$
   199	      [31m$file_data[39;49;00m[] = [31m$fd[39;49;00m;$
   200	$
   201	      [37m// Central directory[39;49;00m$
   202	$
   203	      [37m// Reset file data[39;49;00m$
   204	      [31m$fd[39;49;00m = [33m''[39;49;00m;$
   205	$
   206	      [37m// File header[39;49;00m$
   207	      [31m$fd[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x01[39;49;00m[33m\x02[39;49;00m[33m"[39;49;00m;                  [37m// Local file header signature[39;49;00m$
   208	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Version made by[39;49;00m$
   209	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m20[39;49;00m);                       [37m// Version needed to extract[39;49;00m$
   210	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// General purpose bit flag[39;49;00m$
   211	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [31m$method[39;49;00m);                  [37m// Compression method[39;49;00m$
   212	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Last mod file time[39;49;00m$
   213	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Last mod file date[39;49;00m$
   214	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mcrc32[39;49;00m([31m$content[39;49;00m));          [37m// crc-32[39;49;00m$
   215	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$compressed_data[39;49;00m)); [37m// Compressed size[39;49;00m$
   216	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$content[39;49;00m));         [37m// Uncompressed size[39;49;00m$
   217	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$name[39;49;00m));            [37m// File name length[39;49;00m$
   218	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Extra field length[39;49;00m$
   219	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// File comment length[39;49;00m$
   220	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Disk number start[39;49;00m$
   221	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Internal file attributes[39;49;00m$
   222	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m32[39;49;00m);                       [37m// External file attributes[39;49;00m$
   223	      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [31m$offset[39;49;00m);                  [37m// Relative offset of local header[39;49;00m$
   224	$
   225	      [31m$fd[39;49;00m .= [31m$name[39;49;00m;                               [37m// File name[39;49;00m$
   226	      [31m$fd[39;49;00m .= [33m''[39;49;00m;                                  [37m// Extra field (is empty)[39;49;00m$
   227	      [31m$fd[39;49;00m .= [33m''[39;49;00m;                                  [37m// File comment (is empty)[39;49;00m$
   228	$
   229	      [37m/*[39;49;00m$
   230	[37m      // Data descriptor[39;49;00m$
   231	[37m      $fd .= pack("V", crc32($content));          // crc-32[39;49;00m$
   232	[37m      $fd .= pack("V", strlen($compressed_data)); // Compressed size[39;49;00m$
   233	[37m      $fd .= pack("V", strlen($content));         // Uncompressed size[39;49;00m$
   234	[37m      */[39;49;00m$
   235	$
   236	      [37m// Append file data to the central directory data[39;49;00m$
   237	      [31m$cd_data[39;49;00m[] = [31m$fd[39;49;00m;$
   238	    }$
   239	$
   240	    [37m// Digital signature[39;49;00m$
   241	    [31m$digital_signature[39;49;00m = [33m''[39;49;00m;$
   242	    [31m$digital_signature[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x05[39;49;00m[33m\x05[39;49;00m[33m"[39;49;00m;  [37m// Header signature[39;49;00m$
   243	    [31m$digital_signature[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);        [37m// Size of data[39;49;00m$
   244	    [31m$digital_signature[39;49;00m .= [33m''[39;49;00m;                  [37m// Signature data (is empty)[39;49;00m$
   245	$
   246	    [31m$tmp_file_data[39;49;00m = [36mimplode[39;49;00m([33m''[39;49;00m, [31m$file_data[39;49;00m);  [37m// File data[39;49;00m$
   247	    [31m$tmp_cd_data[39;49;00m   = [36mimplode[39;49;00m([33m''[39;49;00m, [31m$cd_data[39;49;00m).    [37m// Central directory[39;49;00m$
   248	                     [31m$digital_signature[39;49;00m;       [37m// Digital signature[39;49;00m$
   249	$
   250	    [37m// End of central directory[39;49;00m$
   251	    [31m$eof_cd[39;49;00m = [33m''[39;49;00m;$
   252	    [31m$eof_cd[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x05[39;49;00m[33m\x06[39;49;00m[33m"[39;49;00m;                [37m// End of central dir signature[39;49;00m$
   253	    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                      [37m// Number of this disk[39;49;00m$
   254	    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                      [37m// Number of the disk with the start of the central directory[39;49;00m$
   255	    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mcount[39;49;00m([31m$cd_data[39;49;00m));        [37m// Total number of entries in the central directory on this disk[39;49;00m$
   256	    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mcount[39;49;00m([31m$cd_data[39;49;00m));        [37m// Total number of entries in the central directory[39;49;00m$
   257	    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$tmp_cd_data[39;49;00m));   [37m// Size of the central directory[39;49;00m$
   258	    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$tmp_file_data[39;49;00m)); [37m// Offset of start of central directory with respect to the starting disk number[39;49;00m$
   259	    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                      [37m// .ZIP file comment length[39;49;00m$
   260	    [31m$eof_cd[39;49;00m .= [33m''[39;49;00m;                                [37m// .ZIP file comment (is empty)[39;49;00m$
   261	$
   262	    [37m// Content of the zip file[39;49;00m$
   263	    [31m$data[39;49;00m = [31m$tmp_file_data[39;49;00m.$
   264	            [37m// $extra_data_record.[39;49;00m$
   265	            [31m$tmp_cd_data[39;49;00m.$
   266	            [31m$eof_cd[39;49;00m;$
   267	$
   268	    [37m// Return content?[39;49;00m$
   269	    [34mif[39;49;00m(![31m$filename[39;49;00m)$
   270	      [34mreturn[39;49;00m [31m$data[39;49;00m;$
   271	      $
   272	    [37m// Write to file[39;49;00m$
   273	    [34mreturn[39;49;00m [36mfile_put_contents[39;49;00m([31m$filename[39;49;00m, [31m$data[39;49;00m);$
   274	  }$
   275	  $
   276	 [33m/**[39;49;00m$
   277	[33m  *  Load a zip file[39;49;00m$
   278	[33m  *[39;49;00m$
   279	[33m  *  This function loads the files and dirs from a zip file from the harddrive.[39;49;00m$
   280	[33m  *[39;49;00m$
   281	[33m  *  @access                public[39;49;00m$
   282	[33m  *[39;49;00m$
   283	[33m  *  @param  string $file   The path to the zip file[39;49;00m$
   284	[33m  *  @param  bool   $reset  Reset the files and dirs before adding the zip file's content?[39;49;00m$
   285	[33m  *[39;49;00m$
   286	[33m  *  @return bool           Returns true if the file was loaded sucessfully[39;49;00m$
   287	[33m  */[39;49;00m$
   288	  [34mfunction[39;49;00m [32mload_file[39;49;00m([31m$file[39;49;00m, [31m$reset[39;49;00m = [34mtrue[39;49;00m) {$
   289	    [37m// Check whether the file exists[39;49;00m$
   290	    [34mif[39;49;00m(![36mfile_exists[39;49;00m([31m$file[39;49;00m))$
   291	      [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   292	$
   293	    [37m// Load the files content[39;49;00m$
   294	    [31m$content[39;49;00m = @[36mfile_get_contents[39;49;00m([31m$file[39;49;00m);$
   295	$
   296	    [37m// Return false if the file cannot be opened[39;49;00m$
   297	    [34mif[39;49;00m(![31m$content[39;49;00m)$
   298	      [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   299	$
   300	    [37m// Read the zip[39;49;00m$
   301	    [34mreturn[39;49;00m [31m$this[39;49;00m->[36mload_string[39;49;00m([31m$content[39;49;00m, [31m$reset[39;49;00m);$
   302	  }$
   303	  $
   304	 [33m/**[39;49;00m$
   305	[33m  *  Load a zip string[39;49;00m$
   306	[33m  *[39;49;00m$
   307	[33m  *  This function loads the files and dirs from a string[39;49;00m$
   308	[33m  *[39;49;00m$
   309	[33m  *  @access                 public[39;49;00m$
   310	[33m  *[39;49;00m$
   311	[33m  *  @param  string $string  The string the zip is generated from[39;49;00m$
   312	[33m  *  @param  bool   $reset   Reset the files and dirs before adding the zip file's content?[39;49;00m$
   313	[33m  *[39;49;00m$
   314	[33m  *  @return bool            Returns true if the string was loaded sucessfully[39;49;00m$
   315	[33m  */[39;49;00m$
   316	  [34mfunction[39;49;00m [32mload_string[39;49;00m([31m$string[39;49;00m, [31m$reset[39;49;00m = [34mtrue[39;49;00m) {$
   317	    [37m// Reset the zip?[39;49;00m$
   318	    [34mif[39;49;00m([31m$reset[39;49;00m) {$
   319	      [31m$this[39;49;00m->[36mdirs[39;49;00m  = [34marray[39;49;00m();$
   320	      [31m$this[39;49;00m->[36mfiles[39;49;00m = [34marray[39;49;00m();$
   321	    }$
   322	$
   323	    [37m// Get the starting position of the end of central directory record[39;49;00m$
   324	    [31m$start[39;49;00m = [36mstrpos[39;49;00m([31m$string[39;49;00m, [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x05[39;49;00m[33m\x06[39;49;00m[33m"[39;49;00m);$
   325	$
   326	    [37m// Error[39;49;00m$
   327	    [34mif[39;49;00m([31m$start[39;49;00m === [34mfalse[39;49;00m)$
   328	      [34mdie[39;49;00m([33m'Could not find the end of central directory record'[39;49;00m);$
   329	$
   330	    [37m// Get the ecdr[39;49;00m$
   331	    [31m$eof_cd[39;49;00m = [36msubstr[39;49;00m([31m$string[39;49;00m, [31m$start[39;49;00m+[34m4[39;49;00m, [34m18[39;49;00m);$
   332	$
   333	    [37m// Unpack the ecdr infos[39;49;00m$
   334	    [31m$eof_cd[39;49;00m = [36munpack[39;49;00m([33m'vdisc1/'[39;49;00m.$
   335	                     [33m'vdisc2/'[39;49;00m.$
   336	                     [33m'ventries1/'[39;49;00m.$
   337	                     [33m'ventries2/'[39;49;00m.$
   338	                     [33m'Vsize/'[39;49;00m.$
   339	                     [33m'Voffset/'[39;49;00m.$
   340	                     [33m'vcomment_lenght'[39;49;00m, [31m$eof_cd[39;49;00m);$
   341	$
   342	    [37m// Do not allow multi disc zips[39;49;00m$
   343	    [34mif[39;49;00m([31m$eof_cd[39;49;00m[[33m'disc1'[39;49;00m] != [34m0[39;49;00m)$
   344	      [34mdie[39;49;00m([33m'multi disk stuff is not yet implemented :/'[39;49;00m);$
   345	$
   346	    [37m// Save the interesting values[39;49;00m$
   347	    [31m$cd_entries[39;49;00m = [31m$eof_cd[39;49;00m[[33m'entries1'[39;49;00m];$
   348	    [31m$cd_size[39;49;00m    = [31m$eof_cd[39;49;00m[[33m'size'[39;49;00m];$
   349	    [31m$cd_offset[39;49;00m  = [31m$eof_cd[39;49;00m[[33m'offset'[39;49;00m];$
   350	$
   351	    [37m// Get the central directory record[39;49;00m$
   352	    [31m$cdr[39;49;00m = [36msubstr[39;49;00m([31m$string[39;49;00m, [31m$cd_offset[39;49;00m, [31m$cd_size[39;49;00m);$
   353	$
   354	    [37m// Reset the position and the list of the entries[39;49;00m$
   355	    [31m$pos[39;49;00m     = [34m0[39;49;00m;$
   356	    [31m$entries[39;49;00m = [34marray[39;49;00m();$
   357	$
   358	    [37m// Handle cdr[39;49;00m$
   359	    [34mwhile[39;49;00m([31m$pos[39;49;00m < [36mstrlen[39;49;00m([31m$cdr[39;49;00m)) {$
   360	      [37m// Check header signature[39;49;00m$
   361	      [37m// Digital signature[39;49;00m$
   362	      [34mif[39;49;00m([36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m, [34m4[39;49;00m) == [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x05[39;49;00m[33m\x05[39;49;00m[33m"[39;49;00m) {$
   363	        [37m// Get digital signature size[39;49;00m$
   364	        [31m$tmp_info[39;49;00m = [36munpack[39;49;00m([33m'vsize'[39;49;00m, [36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m + [34m4[39;49;00m, [34m2[39;49;00m));$
   365	$
   366	        [37m// Read out the digital signature[39;49;00m$
   367	        [31m$digital_sig[39;49;00m = [36msubstr[39;49;00m([31m$header[39;49;00m, [31m$pos[39;49;00m + [34m6[39;49;00m, [31m$tmp_info[39;49;00m[[33m'size'[39;49;00m]);$
   368	$
   369	        [34mbreak[39;49;00m;$
   370	      }$
   371	$
   372	      [37m// Get file header[39;49;00m$
   373	      [31m$header[39;49;00m = [36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m, [34m46[39;49;00m);$
   374	$
   375	      [37m// Unpack the header information[39;49;00m$
   376	      [31m$header_info[39;49;00m = @[36munpack[39;49;00m([33m'Vheader/'[39;49;00m.$
   377	                             [33m'vversion_made_by/'[39;49;00m.$
   378	                             [33m'vversion_needed/'[39;49;00m.$
   379	                             [33m'vgeneral_purpose/'[39;49;00m.$
   380	                             [33m'vcompression_method/'[39;49;00m.$
   381	                             [33m'vlast_mod_time/'[39;49;00m.$
   382	                             [33m'vlast_mod_date/'[39;49;00m.$
   383	                             [33m'Vcrc32/'[39;49;00m.$
   384	                             [33m'Vcompressed_size/'[39;49;00m.$
   385	                             [33m'Vuncompressed_size/'[39;49;00m.$
   386	                             [33m'vname_length/'[39;49;00m.$
   387	                             [33m'vextra_length/'[39;49;00m.$
   388	                             [33m'vcomment_length/'[39;49;00m.$
   389	                             [33m'vdisk_number/'[39;49;00m.$
   390	                             [33m'vinternal_attributes/'[39;49;00m.$
   391	                             [33m'Vexternal_attributes/'[39;49;00m.$
   392	                             [33m'Voffset'[39;49;00m,$
   393	                             [31m$header[39;49;00m);$
   394	$
   395	      [37m// Valid header?[39;49;00m$
   396	      [34mif[39;49;00m([31m$header_info[39;49;00m[[33m'header'[39;49;00m] != [34m33639248[39;49;00m)$
   397	        [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   398	$
   399	      [37m// New position[39;49;00m$
   400	      [31m$pos[39;49;00m += [34m46[39;49;00m;$
   401	$
   402	      [37m// Read out the file name[39;49;00m$
   403	      [31m$header_info[39;49;00m[[33m'name'[39;49;00m] = [36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m, [31m$header_info[39;49;00m[[33m'name_length'[39;49;00m]);$
   404	$
   405	      [37m// New position[39;49;00m$
   406	      [31m$pos[39;49;00m += [31m$header_info[39;49;00m[[33m'name_length'[39;49;00m];$
   407	$
   408	      [37m// Read out the extra stuff[39;49;00m$
   409	      [31m$header_info[39;49;00m[[33m'extra'[39;49;00m] = [36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m, [31m$header_info[39;49;00m[[33m'extra_length'[39;49;00m]);$
   410	$
   411	      [37m// New position[39;49;00m$
   412	      [31m$pos[39;49;00m += [31m$header_info[39;49;00m[[33m'extra_length'[39;49;00m];$
   413	$
   414	      [37m// Read out the comment[39;49;00m$
   415	      [31m$header_info[39;49;00m[[33m'comment'[39;49;00m] = [36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m, [31m$header_info[39;49;00m[[33m'comment_length'[39;49;00m]);$
   416	$
   417	      [37m// New position[39;49;00m$
   418	      [31m$pos[39;49;00m += [31m$header_info[39;49;00m[[33m'comment_length'[39;49;00m];$
   419	$
   420	      [37m// Append this file/dir to the entry list[39;49;00m$
   421	      [31m$entries[39;49;00m[] = [31m$header_info[39;49;00m;$
   422	    }$
   423	$
   424	    [37m// Check whether all entries where read sucessfully[39;49;00m$
   425	    [34mif[39;49;00m([36mcount[39;49;00m([31m$entries[39;49;00m) != [31m$cd_entries[39;49;00m)$
   426	      [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   427	$
   428	    [37m// Handle files/dirs[39;49;00m$
   429	    [34mforeach[39;49;00m([31m$entries[39;49;00m [34mas[39;49;00m [31m$entry[39;49;00m) {$
   430	      [37m// Is a dir?[39;49;00m$
   431	      [34mif[39;49;00m([31m$entry[39;49;00m[[33m'external_attributes'[39;49;00m] & [34m16[39;49;00m) {$
   432	        [31m$this[39;49;00m->[36madd_dir[39;49;00m([31m$entry[39;49;00m[[33m'name'[39;49;00m]);$
   433	        [34mcontinue[39;49;00m;$
   434	      }$
   435	$
   436	      [37m// Get local file header[39;49;00m$
   437	      [31m$header[39;49;00m = [36msubstr[39;49;00m([31m$string[39;49;00m, [31m$entry[39;49;00m[[33m'offset'[39;49;00m], [34m30[39;49;00m);$
   438	$
   439	      [37m// Unpack the header information[39;49;00m$
   440	      [31m$header_info[39;49;00m = @[36munpack[39;49;00m([33m'Vheader/'[39;49;00m.$
   441	                             [33m'vversion_needed/'[39;49;00m.$
   442	                             [33m'vgeneral_purpose/'[39;49;00m.$
   443	                             [33m'vcompression_method/'[39;49;00m.$
   444	                             [33m'vlast_mod_time/'[39;49;00m.$
   445	                             [33m'vlast_mod_date/'[39;49;00m.$
   446	                             [33m'Vcrc32/'[39;49;00m.$
   447	                             [33m'Vcompressed_size/'[39;49;00m.$
   448	                             [33m'Vuncompressed_size/'[39;49;00m.$
   449	                             [33m'vname_length/'[39;49;00m.$
   450	                             [33m'vextra_length'[39;49;00m,$
   451	                             [31m$header[39;49;00m);$
   452	$
   453	      [37m// Valid header?[39;49;00m$
   454	      [34mif[39;49;00m([31m$header_info[39;49;00m[[33m'header'[39;49;00m] != [34m67324752[39;49;00m)$
   455	        [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   456	$
   457	      [37m// Get content start position[39;49;00m$
   458	      [31m$start[39;49;00m = [31m$entry[39;49;00m[[33m'offset'[39;49;00m] + [34m30[39;49;00m + [31m$header_info[39;49;00m[[33m'name_length'[39;49;00m] + [31m$header_info[39;49;00m[[33m'extra_length'[39;49;00m];$
   459	$
   460	      [37m// Get the compressed data[39;49;00m$
   461	      [31m$data[39;49;00m = [36msubstr[39;49;00m([31m$string[39;49;00m, [31m$start[39;49;00m, [31m$header_info[39;49;00m[[33m'compressed_size'[39;49;00m]);$
   462	$
   463	      [37m// Detect compression type[39;49;00m$
   464	      [34mswitch[39;49;00m([31m$header_info[39;49;00m[[33m'compression_method'[39;49;00m]) {$
   465	        [37m// No compression[39;49;00m$
   466	        [34mcase[39;49;00m [34m0[39;49;00m:$
   467	          [37m// Ne decompression needed[39;49;00m$
   468	          [31m$content[39;49;00m = [31m$data[39;49;00m;$
   469	          [34mbreak[39;49;00m;$
   470	$
   471	        [37m// Gzip[39;49;00m$
   472	        [34mcase[39;49;00m [34m8[39;49;00m:$
   473	          [34mif[39;49;00m(![36mfunction_exists[39;49;00m([33m'gzinflate'[39;49;00m))$
   474	            [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   475	$
   476	          [37m// Uncompress data[39;49;00m$
   477	          [31m$content[39;49;00m = [36mgzinflate[39;49;00m([31m$data[39;49;00m);$
   478	          [34mbreak[39;49;00m;$
   479	$
   480	        [37m// Bzip2[39;49;00m$
   481	        [34mcase[39;49;00m [34m12[39;49;00m:$
   482	          [34mif[39;49;00m(![36mfunction_exists[39;49;00m([33m'bzdecompress'[39;49;00m))$
   483	            [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   484	$
   485	          [37m// Decompress data[39;49;00m$
   486	          [31m$content[39;49;00m = [36mbzdecompress[39;49;00m([31m$data[39;49;00m);$
   487	          [34mbreak[39;49;00m;$
   488	$
   489	        [37m// Compression not supported -> error[39;49;00m$
   490	        [34mdefault[39;49;00m:$
   491	          [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   492	      }$
   493	$
   494	      [37m// Try to add file[39;49;00m$
   495	      [34mif[39;49;00m(![31m$this[39;49;00m->[36madd_file[39;49;00m([31m$entry[39;49;00m[[33m'name'[39;49;00m], [31m$content[39;49;00m))$
   496	        [34mreturn[39;49;00m [34mfalse[39;49;00m;$
   497	    }$
   498	$
   499	    [34mreturn[39;49;00m [34mtrue[39;49;00m;$
   500	  }$
   501	}$
   502	$
   503	[34mfunction[39;49;00m &[32mbyref[39;49;00m() {$
   504	    [31m$x[39;49;00m = [34marray[39;49;00m();$
   505	    [34mreturn[39;49;00m [31m$x[39;49;00m;$
   506	}$
   507	$
   508	[37m// Test highlighting of magic methods and variables[39;49;00m$
   509	[34mclass[39;49;00m [04m[32mMagicClass[39;49;00m {$
   510	  [34mpublic[39;49;00m [31m$magic_str[39;49;00m;$
   511	  [34mpublic[39;49;00m [31m$ordinary_str[39;49;00m;$
   512	$
   513	  [34mpublic[39;49;00m [34mfunction[39;49;00m [32m__construct[39;49;00m([31m$some_var[39;49;00m) {$
   514	    [31m$this[39;49;00m->[36mmagic_str[39;49;00m = [31m__FILE__[39;49;00m;$
   515	    [31m$this[39;49;00m->[36mordinary_str[39;49;00m = [31m$some_var[39;49;00m;$
   516	  }$
   517	$
   518	  [34mpublic[39;49;00m [34mfunction[39;49;00m [32m__toString[39;49;00m() {$
   519	    [34mreturn[39;49;00m [31m$this[39;49;00m->[36mmagic_str[39;49;00m;$
   520	  }$
   521	$
   522	  [34mpublic[39;49;00m [34mfunction[39;49;00m [32mnonMagic[39;49;00m() {$
   523	    [34mreturn[39;49;00m [31m$this[39;49;00m->[36mordinary_str[39;49;00m;$
   524	  }$
   525	}$
   526	$
   527	[31m$magic[39;49;00m = [34mnew[39;49;00m MagicClass([31m__DIR__[39;49;00m);$
   528	__toString();$
   529	[31m$magic[39;49;00m->[36mnonMagic[39;49;00m();$
   530	[31m$magic[39;49;00m->[36m__toString[39;49;00m();$
   531	$
   532	     [34mecho[39;49;00m [33m<<<[39;49;00m[33mEOF[39;49;00m[33m[39;49;00m$
   533	[33m[39;49;00m$
   534	[33m     Test the heredocs...[39;49;00m$
   535	[33m[39;49;00m$
   536	[33m     [39;49;00m[33mEOF[39;49;00m;$
   537	$
   538	[34mecho[39;49;00m [33m<<<[39;49;00m[33m"[39;49;00m[33msome_delimiter[39;49;00m[33m"[39;49;00m$
   539	[33mmore heredoc testing[39;49;00m$
   540	[33mcontinues on this line[39;49;00m$
   541	[33msome_delimiter[39;49;00m;$
   542	$
   543	[36m?>[39;49;00m$
