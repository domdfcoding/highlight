Using lexer <pygments.lexers.PhpLexer with {'ensurenl': False, 'tabsize': 0}>
[36m<?php[39;49;00m

[31m$disapproval_ಠ_ಠ_of_php[39;49;00m = [33m'unicode var'[39;49;00m;

[31m$test[39;49;00m = [34mfunction[39;49;00m([31m$a[39;49;00m) { [31m$lambda[39;49;00m = [34m1[39;49;00m; }

[33m/**[39;49;00m
[33m *  Zip class file[39;49;00m
[33m *[39;49;00m
[33m *  @package     fnord.bb[39;49;00m
[33m *  @subpackage  archive[39;49;00m
[33m */[39;49;00m

[37m// Unlock?[39;49;00m
[34mif[39;49;00m(![36mdefined[39;49;00m([33m'UNLOCK'[39;49;00m) || !UNLOCK)
  [34mdie[39;49;00m();

[37m// Load the parent archive class[39;49;00m
[34mrequire_once[39;49;00m(ROOT_PATH.[33m'/classes/archive.class.php'[39;49;00m);

[34mclass[39;49;00m [04m[32mZip\Zippಠ_ಠ_[39;49;00m {

}

[33m/**[39;49;00m
[33m *  Zip class[39;49;00m
[33m *[39;49;00m
[33m *  @author      Manni <manni@fnord.name>[39;49;00m
[33m *  @copyright   Copyright (c) 2006, Manni[39;49;00m
[33m *  @version     1.0[39;49;00m
[33m *  @link        http://www.pkware.com/business_and_developers/developer/popups/appnote.txt[39;49;00m
[33m *  @link        http://mannithedark.is-a-geek.net/[39;49;00m
[33m *  @since       1.0[39;49;00m
[33m *  @package     fnord.bb[39;49;00m
[33m *  @subpackage  archive[39;49;00m
[33m */[39;49;00m
[34mclass[39;49;00m [04m[32mZip[39;49;00m [34mextends[39;49;00m Archive {
 [33m/**[39;49;00m
[33m  *  Outputs the zip file[39;49;00m
[33m  *[39;49;00m
[33m  *  This function creates the zip file with the dirs and files given.[39;49;00m
[33m  *  If the optional parameter $file is given, the zip file is will be[39;49;00m
[33m  *  saved at that location. Otherwise the function returns the zip file's content.[39;49;00m
[33m  *[39;49;00m
[33m  *  @access                   public[39;49;00m
[33m  *[39;49;00m
[33m  *  @link                     http://www.pkware.com/business_and_developers/developer/popups/appnote.txt[39;49;00m
[33m  *  @param  string $filename  The path where the zip file will be saved[39;49;00m
[33m  *[39;49;00m
[33m  *  @return bool|string       Returns either true if the fil is sucessfully created or the content of the zip file[39;49;00m
[33m  */[39;49;00m
  [34mfunction[39;49;00m [32mout[39;49;00m([31m$filename[39;49;00m = [34mfalse[39;49;00m) {
    [37m// Empty output[39;49;00m
    [31m$file_data[39;49;00m = [34marray[39;49;00m(); [37m// Data of the file part[39;49;00m
    [31m$cd_data[39;49;00m   = [34marray[39;49;00m(); [37m// Data of the central directory[39;49;00m

    [37m// Sort dirs and files by path length[39;49;00m
    [36muksort[39;49;00m([31m$this[39;49;00m->[36mdirs[39;49;00m,  [33m'sort_by_length'[39;49;00m);
    [36muksort[39;49;00m([31m$this[39;49;00m->[36mfiles[39;49;00m, [33m'sort_by_length'[39;49;00m);

    [37m// Handle dirs[39;49;00m
    [34mforeach[39;49;00m([31m$this[39;49;00m->[36mdirs[39;49;00m [34mas[39;49;00m [31m$dir[39;49;00m) {
      [31m$dir[39;49;00m .= [33m'/'[39;49;00m;
      [37m// File part[39;49;00m

      [37m// Reset dir data[39;49;00m
      [31m$dir_data[39;49;00m = [33m''[39;49;00m;

      [37m// Local file header[39;49;00m
      [31m$dir_data[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x03[39;49;00m[33m\x04[39;49;00m[33m"[39;49;00m;      [37m// Local file header signature[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m10[39;49;00m);           [37m// Version needed to extract[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// General purpose bit flag[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Compression method[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Last mod file time[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Last mod file date[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// crc-32[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Compressed size[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Uncompressed size[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$dir[39;49;00m)); [37m// File name length[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Extra field length[39;49;00m

      [31m$dir_data[39;49;00m .= [31m$dir[39;49;00m;                    [37m// File name[39;49;00m
      [31m$dir_data[39;49;00m .= [33m''[39;49;00m;                      [37m// Extra field (is empty)[39;49;00m

      [37m// File data[39;49;00m
      [31m$dir_data[39;49;00m .= [33m''[39;49;00m;                      [37m// Dirs have no file data[39;49;00m

      [37m// Data descriptor[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// crc-32[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Compressed size[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Uncompressed size[39;49;00m

      [37m// Save current offset[39;49;00m
      [31m$offset[39;49;00m = [36mstrlen[39;49;00m([36mimplode[39;49;00m([33m''[39;49;00m, [31m$file_data[39;49;00m));

      [37m// Append dir data to the file part[39;49;00m
      [31m$file_data[39;49;00m[] = [31m$dir_data[39;49;00m;

      [37m// Central directory[39;49;00m

      [37m// Reset dir data[39;49;00m
      [31m$dir_data[39;49;00m = [33m''[39;49;00m;

      [37m// File header[39;49;00m
      [31m$dir_data[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x01[39;49;00m[33m\x02[39;49;00m[33m"[39;49;00m;      [37m// Local file header signature[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Version made by[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m10[39;49;00m);           [37m// Version needed to extract[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// General purpose bit flag[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Compression method[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Last mod file time[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Last mod file date[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// crc-32[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Compressed size[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Uncompressed size[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$dir[39;49;00m)); [37m// File name length[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Extra field length[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// File comment length[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Disk number start[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);            [37m// Internal file attributes[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m16[39;49;00m);           [37m// External file attributes[39;49;00m
      [31m$dir_data[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [31m$offset[39;49;00m);      [37m// Relative offset of local header[39;49;00m

      [31m$dir_data[39;49;00m .= [31m$dir[39;49;00m;                    [37m// File name[39;49;00m
      [31m$dir_data[39;49;00m .= [33m''[39;49;00m;                      [37m// Extra field (is empty)[39;49;00m
      [31m$dir_data[39;49;00m .= [33m''[39;49;00m;                      [37m// File comment (is empty)[39;49;00m

      [37m/*[39;49;00m
[37m      // Data descriptor[39;49;00m
[37m      $dir_data .= pack("V", 0);            // crc-32[39;49;00m
[37m      $dir_data .= pack("V", 0);            // Compressed size[39;49;00m
[37m      $dir_data .= pack("V", 0);            // Uncompressed size[39;49;00m
[37m      */[39;49;00m

      [37m// Append dir data to the central directory data[39;49;00m
      [31m$cd_data[39;49;00m[] = [31m$dir_data[39;49;00m;
    }

    [37m// Handle files[39;49;00m
    [34mforeach[39;49;00m([31m$this[39;49;00m->[36mfiles[39;49;00m [34mas[39;49;00m [31m$name[39;49;00m => [31m$file[39;49;00m) {
      [37m// Get values[39;49;00m
      [31m$content[39;49;00m = [31m$file[39;49;00m[[34m0[39;49;00m];

      [37m// File part[39;49;00m

      [37m// Reset file data[39;49;00m
      [31m$fd[39;49;00m = [33m''[39;49;00m;

      [37m// Detect possible compressions[39;49;00m
      [37m// Use deflate[39;49;00m
      [34mif[39;49;00m([36mfunction_exists[39;49;00m([33m'gzdeflate'[39;49;00m)) {
        [31m$method[39;49;00m = [34m8[39;49;00m;

        [37m// Compress file content[39;49;00m
        [31m$compressed_data[39;49;00m = [36mgzdeflate[39;49;00m([31m$content[39;49;00m);

      [37m// Use bzip2[39;49;00m
      } [34melseif[39;49;00m([36mfunction_exists[39;49;00m([33m'bzcompress'[39;49;00m)) {
        [31m$method[39;49;00m = [34m12[39;49;00m;

        [37m// Compress file content[39;49;00m
        [31m$compressed_data[39;49;00m = [36mbzcompress[39;49;00m([31m$content[39;49;00m);

      [37m// No compression[39;49;00m
      } [34melse[39;49;00m {
        [31m$method[39;49;00m = [34m0[39;49;00m;

        [37m// Do not compress the content :P[39;49;00m
        [31m$compressed_data[39;49;00m = [31m$content[39;49;00m;
      }

      [37m// Local file header[39;49;00m
      [31m$fd[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x03[39;49;00m[33m\x04[39;49;00m[33m"[39;49;00m;                  [37m// Local file header signature[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m20[39;49;00m);                       [37m// Version needed to extract[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// General purpose bit flag[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [31m$method[39;49;00m);                  [37m// Compression method[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Last mod file time[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Last mod file date[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mcrc32[39;49;00m([31m$content[39;49;00m));          [37m// crc-32[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$compressed_data[39;49;00m)); [37m// Compressed size[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$content[39;49;00m));         [37m// Uncompressed size[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$name[39;49;00m));            [37m// File name length[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Extra field length[39;49;00m

      [31m$fd[39;49;00m .= [31m$name[39;49;00m;                               [37m// File name[39;49;00m
      [31m$fd[39;49;00m .= [33m''[39;49;00m;                                  [37m// Extra field (is empty)[39;49;00m

      [37m// File data[39;49;00m
      [31m$fd[39;49;00m .= [31m$compressed_data[39;49;00m;

      [37m// Data descriptor[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mcrc32[39;49;00m([31m$content[39;49;00m));          [37m// crc-32[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$compressed_data[39;49;00m)); [37m// Compressed size[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$content[39;49;00m));         [37m// Uncompressed size[39;49;00m

      [37m// Save current offset[39;49;00m
      [31m$offset[39;49;00m = [36mstrlen[39;49;00m([36mimplode[39;49;00m([33m''[39;49;00m, [31m$file_data[39;49;00m));

      [37m// Append file data to the file part[39;49;00m
      [31m$file_data[39;49;00m[] = [31m$fd[39;49;00m;

      [37m// Central directory[39;49;00m

      [37m// Reset file data[39;49;00m
      [31m$fd[39;49;00m = [33m''[39;49;00m;

      [37m// File header[39;49;00m
      [31m$fd[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x01[39;49;00m[33m\x02[39;49;00m[33m"[39;49;00m;                  [37m// Local file header signature[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Version made by[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m20[39;49;00m);                       [37m// Version needed to extract[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// General purpose bit flag[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [31m$method[39;49;00m);                  [37m// Compression method[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Last mod file time[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Last mod file date[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mcrc32[39;49;00m([31m$content[39;49;00m));          [37m// crc-32[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$compressed_data[39;49;00m)); [37m// Compressed size[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$content[39;49;00m));         [37m// Uncompressed size[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$name[39;49;00m));            [37m// File name length[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Extra field length[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// File comment length[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Disk number start[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                        [37m// Internal file attributes[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [34m32[39;49;00m);                       [37m// External file attributes[39;49;00m
      [31m$fd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [31m$offset[39;49;00m);                  [37m// Relative offset of local header[39;49;00m

      [31m$fd[39;49;00m .= [31m$name[39;49;00m;                               [37m// File name[39;49;00m
      [31m$fd[39;49;00m .= [33m''[39;49;00m;                                  [37m// Extra field (is empty)[39;49;00m
      [31m$fd[39;49;00m .= [33m''[39;49;00m;                                  [37m// File comment (is empty)[39;49;00m

      [37m/*[39;49;00m
[37m      // Data descriptor[39;49;00m
[37m      $fd .= pack("V", crc32($content));          // crc-32[39;49;00m
[37m      $fd .= pack("V", strlen($compressed_data)); // Compressed size[39;49;00m
[37m      $fd .= pack("V", strlen($content));         // Uncompressed size[39;49;00m
[37m      */[39;49;00m

      [37m// Append file data to the central directory data[39;49;00m
      [31m$cd_data[39;49;00m[] = [31m$fd[39;49;00m;
    }

    [37m// Digital signature[39;49;00m
    [31m$digital_signature[39;49;00m = [33m''[39;49;00m;
    [31m$digital_signature[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x05[39;49;00m[33m\x05[39;49;00m[33m"[39;49;00m;  [37m// Header signature[39;49;00m
    [31m$digital_signature[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);        [37m// Size of data[39;49;00m
    [31m$digital_signature[39;49;00m .= [33m''[39;49;00m;                  [37m// Signature data (is empty)[39;49;00m

    [31m$tmp_file_data[39;49;00m = [36mimplode[39;49;00m([33m''[39;49;00m, [31m$file_data[39;49;00m);  [37m// File data[39;49;00m
    [31m$tmp_cd_data[39;49;00m   = [36mimplode[39;49;00m([33m''[39;49;00m, [31m$cd_data[39;49;00m).    [37m// Central directory[39;49;00m
                     [31m$digital_signature[39;49;00m;       [37m// Digital signature[39;49;00m

    [37m// End of central directory[39;49;00m
    [31m$eof_cd[39;49;00m = [33m''[39;49;00m;
    [31m$eof_cd[39;49;00m .= [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x05[39;49;00m[33m\x06[39;49;00m[33m"[39;49;00m;                [37m// End of central dir signature[39;49;00m
    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                      [37m// Number of this disk[39;49;00m
    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                      [37m// Number of the disk with the start of the central directory[39;49;00m
    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mcount[39;49;00m([31m$cd_data[39;49;00m));        [37m// Total number of entries in the central directory on this disk[39;49;00m
    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [36mcount[39;49;00m([31m$cd_data[39;49;00m));        [37m// Total number of entries in the central directory[39;49;00m
    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$tmp_cd_data[39;49;00m));   [37m// Size of the central directory[39;49;00m
    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mV[39;49;00m[33m"[39;49;00m, [36mstrlen[39;49;00m([31m$tmp_file_data[39;49;00m)); [37m// Offset of start of central directory with respect to the starting disk number[39;49;00m
    [31m$eof_cd[39;49;00m .= [36mpack[39;49;00m([33m"[39;49;00m[33mv[39;49;00m[33m"[39;49;00m, [34m0[39;49;00m);                      [37m// .ZIP file comment length[39;49;00m
    [31m$eof_cd[39;49;00m .= [33m''[39;49;00m;                                [37m// .ZIP file comment (is empty)[39;49;00m

    [37m// Content of the zip file[39;49;00m
    [31m$data[39;49;00m = [31m$tmp_file_data[39;49;00m.
            [37m// $extra_data_record.[39;49;00m
            [31m$tmp_cd_data[39;49;00m.
            [31m$eof_cd[39;49;00m;

    [37m// Return content?[39;49;00m
    [34mif[39;49;00m(![31m$filename[39;49;00m)
      [34mreturn[39;49;00m [31m$data[39;49;00m;

    [37m// Write to file[39;49;00m
    [34mreturn[39;49;00m [36mfile_put_contents[39;49;00m([31m$filename[39;49;00m, [31m$data[39;49;00m);
  }

 [33m/**[39;49;00m
[33m  *  Load a zip file[39;49;00m
[33m  *[39;49;00m
[33m  *  This function loads the files and dirs from a zip file from the harddrive.[39;49;00m
[33m  *[39;49;00m
[33m  *  @access                public[39;49;00m
[33m  *[39;49;00m
[33m  *  @param  string $file   The path to the zip file[39;49;00m
[33m  *  @param  bool   $reset  Reset the files and dirs before adding the zip file's content?[39;49;00m
[33m  *[39;49;00m
[33m  *  @return bool           Returns true if the file was loaded sucessfully[39;49;00m
[33m  */[39;49;00m
  [34mfunction[39;49;00m [32mload_file[39;49;00m([31m$file[39;49;00m, [31m$reset[39;49;00m = [34mtrue[39;49;00m) {
    [37m// Check whether the file exists[39;49;00m
    [34mif[39;49;00m(![36mfile_exists[39;49;00m([31m$file[39;49;00m))
      [34mreturn[39;49;00m [34mfalse[39;49;00m;

    [37m// Load the files content[39;49;00m
    [31m$content[39;49;00m = @[36mfile_get_contents[39;49;00m([31m$file[39;49;00m);

    [37m// Return false if the file cannot be opened[39;49;00m
    [34mif[39;49;00m(![31m$content[39;49;00m)
      [34mreturn[39;49;00m [34mfalse[39;49;00m;

    [37m// Read the zip[39;49;00m
    [34mreturn[39;49;00m [31m$this[39;49;00m->[36mload_string[39;49;00m([31m$content[39;49;00m, [31m$reset[39;49;00m);
  }

 [33m/**[39;49;00m
[33m  *  Load a zip string[39;49;00m
[33m  *[39;49;00m
[33m  *  This function loads the files and dirs from a string[39;49;00m
[33m  *[39;49;00m
[33m  *  @access                 public[39;49;00m
[33m  *[39;49;00m
[33m  *  @param  string $string  The string the zip is generated from[39;49;00m
[33m  *  @param  bool   $reset   Reset the files and dirs before adding the zip file's content?[39;49;00m
[33m  *[39;49;00m
[33m  *  @return bool            Returns true if the string was loaded sucessfully[39;49;00m
[33m  */[39;49;00m
  [34mfunction[39;49;00m [32mload_string[39;49;00m([31m$string[39;49;00m, [31m$reset[39;49;00m = [34mtrue[39;49;00m) {
    [37m// Reset the zip?[39;49;00m
    [34mif[39;49;00m([31m$reset[39;49;00m) {
      [31m$this[39;49;00m->[36mdirs[39;49;00m  = [34marray[39;49;00m();
      [31m$this[39;49;00m->[36mfiles[39;49;00m = [34marray[39;49;00m();
    }

    [37m// Get the starting position of the end of central directory record[39;49;00m
    [31m$start[39;49;00m = [36mstrpos[39;49;00m([31m$string[39;49;00m, [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x05[39;49;00m[33m\x06[39;49;00m[33m"[39;49;00m);

    [37m// Error[39;49;00m
    [34mif[39;49;00m([31m$start[39;49;00m === [34mfalse[39;49;00m)
      [34mdie[39;49;00m([33m'Could not find the end of central directory record'[39;49;00m);

    [37m// Get the ecdr[39;49;00m
    [31m$eof_cd[39;49;00m = [36msubstr[39;49;00m([31m$string[39;49;00m, [31m$start[39;49;00m+[34m4[39;49;00m, [34m18[39;49;00m);

    [37m// Unpack the ecdr infos[39;49;00m
    [31m$eof_cd[39;49;00m = [36munpack[39;49;00m([33m'vdisc1/'[39;49;00m.
                     [33m'vdisc2/'[39;49;00m.
                     [33m'ventries1/'[39;49;00m.
                     [33m'ventries2/'[39;49;00m.
                     [33m'Vsize/'[39;49;00m.
                     [33m'Voffset/'[39;49;00m.
                     [33m'vcomment_lenght'[39;49;00m, [31m$eof_cd[39;49;00m);

    [37m// Do not allow multi disc zips[39;49;00m
    [34mif[39;49;00m([31m$eof_cd[39;49;00m[[33m'disc1'[39;49;00m] != [34m0[39;49;00m)
      [34mdie[39;49;00m([33m'multi disk stuff is not yet implemented :/'[39;49;00m);

    [37m// Save the interesting values[39;49;00m
    [31m$cd_entries[39;49;00m = [31m$eof_cd[39;49;00m[[33m'entries1'[39;49;00m];
    [31m$cd_size[39;49;00m    = [31m$eof_cd[39;49;00m[[33m'size'[39;49;00m];
    [31m$cd_offset[39;49;00m  = [31m$eof_cd[39;49;00m[[33m'offset'[39;49;00m];

    [37m// Get the central directory record[39;49;00m
    [31m$cdr[39;49;00m = [36msubstr[39;49;00m([31m$string[39;49;00m, [31m$cd_offset[39;49;00m, [31m$cd_size[39;49;00m);

    [37m// Reset the position and the list of the entries[39;49;00m
    [31m$pos[39;49;00m     = [34m0[39;49;00m;
    [31m$entries[39;49;00m = [34marray[39;49;00m();

    [37m// Handle cdr[39;49;00m
    [34mwhile[39;49;00m([31m$pos[39;49;00m < [36mstrlen[39;49;00m([31m$cdr[39;49;00m)) {
      [37m// Check header signature[39;49;00m
      [37m// Digital signature[39;49;00m
      [34mif[39;49;00m([36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m, [34m4[39;49;00m) == [33m"[39;49;00m[33m\x50[39;49;00m[33m\x4b[39;49;00m[33m\x05[39;49;00m[33m\x05[39;49;00m[33m"[39;49;00m) {
        [37m// Get digital signature size[39;49;00m
        [31m$tmp_info[39;49;00m = [36munpack[39;49;00m([33m'vsize'[39;49;00m, [36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m + [34m4[39;49;00m, [34m2[39;49;00m));

        [37m// Read out the digital signature[39;49;00m
        [31m$digital_sig[39;49;00m = [36msubstr[39;49;00m([31m$header[39;49;00m, [31m$pos[39;49;00m + [34m6[39;49;00m, [31m$tmp_info[39;49;00m[[33m'size'[39;49;00m]);

        [34mbreak[39;49;00m;
      }

      [37m// Get file header[39;49;00m
      [31m$header[39;49;00m = [36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m, [34m46[39;49;00m);

      [37m// Unpack the header information[39;49;00m
      [31m$header_info[39;49;00m = @[36munpack[39;49;00m([33m'Vheader/'[39;49;00m.
                             [33m'vversion_made_by/'[39;49;00m.
                             [33m'vversion_needed/'[39;49;00m.
                             [33m'vgeneral_purpose/'[39;49;00m.
                             [33m'vcompression_method/'[39;49;00m.
                             [33m'vlast_mod_time/'[39;49;00m.
                             [33m'vlast_mod_date/'[39;49;00m.
                             [33m'Vcrc32/'[39;49;00m.
                             [33m'Vcompressed_size/'[39;49;00m.
                             [33m'Vuncompressed_size/'[39;49;00m.
                             [33m'vname_length/'[39;49;00m.
                             [33m'vextra_length/'[39;49;00m.
                             [33m'vcomment_length/'[39;49;00m.
                             [33m'vdisk_number/'[39;49;00m.
                             [33m'vinternal_attributes/'[39;49;00m.
                             [33m'Vexternal_attributes/'[39;49;00m.
                             [33m'Voffset'[39;49;00m,
                             [31m$header[39;49;00m);

      [37m// Valid header?[39;49;00m
      [34mif[39;49;00m([31m$header_info[39;49;00m[[33m'header'[39;49;00m] != [34m33639248[39;49;00m)
        [34mreturn[39;49;00m [34mfalse[39;49;00m;

      [37m// New position[39;49;00m
      [31m$pos[39;49;00m += [34m46[39;49;00m;

      [37m// Read out the file name[39;49;00m
      [31m$header_info[39;49;00m[[33m'name'[39;49;00m] = [36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m, [31m$header_info[39;49;00m[[33m'name_length'[39;49;00m]);

      [37m// New position[39;49;00m
      [31m$pos[39;49;00m += [31m$header_info[39;49;00m[[33m'name_length'[39;49;00m];

      [37m// Read out the extra stuff[39;49;00m
      [31m$header_info[39;49;00m[[33m'extra'[39;49;00m] = [36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m, [31m$header_info[39;49;00m[[33m'extra_length'[39;49;00m]);

      [37m// New position[39;49;00m
      [31m$pos[39;49;00m += [31m$header_info[39;49;00m[[33m'extra_length'[39;49;00m];

      [37m// Read out the comment[39;49;00m
      [31m$header_info[39;49;00m[[33m'comment'[39;49;00m] = [36msubstr[39;49;00m([31m$cdr[39;49;00m, [31m$pos[39;49;00m, [31m$header_info[39;49;00m[[33m'comment_length'[39;49;00m]);

      [37m// New position[39;49;00m
      [31m$pos[39;49;00m += [31m$header_info[39;49;00m[[33m'comment_length'[39;49;00m];

      [37m// Append this file/dir to the entry list[39;49;00m
      [31m$entries[39;49;00m[] = [31m$header_info[39;49;00m;
    }

    [37m// Check whether all entries where read sucessfully[39;49;00m
    [34mif[39;49;00m([36mcount[39;49;00m([31m$entries[39;49;00m) != [31m$cd_entries[39;49;00m)
      [34mreturn[39;49;00m [34mfalse[39;49;00m;

    [37m// Handle files/dirs[39;49;00m
    [34mforeach[39;49;00m([31m$entries[39;49;00m [34mas[39;49;00m [31m$entry[39;49;00m) {
      [37m// Is a dir?[39;49;00m
      [34mif[39;49;00m([31m$entry[39;49;00m[[33m'external_attributes'[39;49;00m] & [34m16[39;49;00m) {
        [31m$this[39;49;00m->[36madd_dir[39;49;00m([31m$entry[39;49;00m[[33m'name'[39;49;00m]);
        [34mcontinue[39;49;00m;
      }

      [37m// Get local file header[39;49;00m
      [31m$header[39;49;00m = [36msubstr[39;49;00m([31m$string[39;49;00m, [31m$entry[39;49;00m[[33m'offset'[39;49;00m], [34m30[39;49;00m);

      [37m// Unpack the header information[39;49;00m
      [31m$header_info[39;49;00m = @[36munpack[39;49;00m([33m'Vheader/'[39;49;00m.
                             [33m'vversion_needed/'[39;49;00m.
                             [33m'vgeneral_purpose/'[39;49;00m.
                             [33m'vcompression_method/'[39;49;00m.
                             [33m'vlast_mod_time/'[39;49;00m.
                             [33m'vlast_mod_date/'[39;49;00m.
                             [33m'Vcrc32/'[39;49;00m.
                             [33m'Vcompressed_size/'[39;49;00m.
                             [33m'Vuncompressed_size/'[39;49;00m.
                             [33m'vname_length/'[39;49;00m.
                             [33m'vextra_length'[39;49;00m,
                             [31m$header[39;49;00m);

      [37m// Valid header?[39;49;00m
      [34mif[39;49;00m([31m$header_info[39;49;00m[[33m'header'[39;49;00m] != [34m67324752[39;49;00m)
        [34mreturn[39;49;00m [34mfalse[39;49;00m;

      [37m// Get content start position[39;49;00m
      [31m$start[39;49;00m = [31m$entry[39;49;00m[[33m'offset'[39;49;00m] + [34m30[39;49;00m + [31m$header_info[39;49;00m[[33m'name_length'[39;49;00m] + [31m$header_info[39;49;00m[[33m'extra_length'[39;49;00m];

      [37m// Get the compressed data[39;49;00m
      [31m$data[39;49;00m = [36msubstr[39;49;00m([31m$string[39;49;00m, [31m$start[39;49;00m, [31m$header_info[39;49;00m[[33m'compressed_size'[39;49;00m]);

      [37m// Detect compression type[39;49;00m
      [34mswitch[39;49;00m([31m$header_info[39;49;00m[[33m'compression_method'[39;49;00m]) {
        [37m// No compression[39;49;00m
        [34mcase[39;49;00m [34m0[39;49;00m:
          [37m// Ne decompression needed[39;49;00m
          [31m$content[39;49;00m = [31m$data[39;49;00m;
          [34mbreak[39;49;00m;

        [37m// Gzip[39;49;00m
        [34mcase[39;49;00m [34m8[39;49;00m:
          [34mif[39;49;00m(![36mfunction_exists[39;49;00m([33m'gzinflate'[39;49;00m))
            [34mreturn[39;49;00m [34mfalse[39;49;00m;

          [37m// Uncompress data[39;49;00m
          [31m$content[39;49;00m = [36mgzinflate[39;49;00m([31m$data[39;49;00m);
          [34mbreak[39;49;00m;

        [37m// Bzip2[39;49;00m
        [34mcase[39;49;00m [34m12[39;49;00m:
          [34mif[39;49;00m(![36mfunction_exists[39;49;00m([33m'bzdecompress'[39;49;00m))
            [34mreturn[39;49;00m [34mfalse[39;49;00m;

          [37m// Decompress data[39;49;00m
          [31m$content[39;49;00m = [36mbzdecompress[39;49;00m([31m$data[39;49;00m);
          [34mbreak[39;49;00m;

        [37m// Compression not supported -> error[39;49;00m
        [34mdefault[39;49;00m:
          [34mreturn[39;49;00m [34mfalse[39;49;00m;
      }

      [37m// Try to add file[39;49;00m
      [34mif[39;49;00m(![31m$this[39;49;00m->[36madd_file[39;49;00m([31m$entry[39;49;00m[[33m'name'[39;49;00m], [31m$content[39;49;00m))
        [34mreturn[39;49;00m [34mfalse[39;49;00m;
    }

    [34mreturn[39;49;00m [34mtrue[39;49;00m;
  }
}

[34mfunction[39;49;00m &[32mbyref[39;49;00m() {
    [31m$x[39;49;00m = [34marray[39;49;00m();
    [34mreturn[39;49;00m [31m$x[39;49;00m;
}

[37m// Test highlighting of magic methods and variables[39;49;00m
[34mclass[39;49;00m [04m[32mMagicClass[39;49;00m {
  [34mpublic[39;49;00m [31m$magic_str[39;49;00m;
  [34mpublic[39;49;00m [31m$ordinary_str[39;49;00m;

  [34mpublic[39;49;00m [34mfunction[39;49;00m [32m__construct[39;49;00m([31m$some_var[39;49;00m) {
    [31m$this[39;49;00m->[36mmagic_str[39;49;00m = [31m__FILE__[39;49;00m;
    [31m$this[39;49;00m->[36mordinary_str[39;49;00m = [31m$some_var[39;49;00m;
  }

  [34mpublic[39;49;00m [34mfunction[39;49;00m [32m__toString[39;49;00m() {
    [34mreturn[39;49;00m [31m$this[39;49;00m->[36mmagic_str[39;49;00m;
  }

  [34mpublic[39;49;00m [34mfunction[39;49;00m [32mnonMagic[39;49;00m() {
    [34mreturn[39;49;00m [31m$this[39;49;00m->[36mordinary_str[39;49;00m;
  }
}

[31m$magic[39;49;00m = [34mnew[39;49;00m MagicClass([31m__DIR__[39;49;00m);
__toString();
[31m$magic[39;49;00m->[36mnonMagic[39;49;00m();
[31m$magic[39;49;00m->[36m__toString[39;49;00m();

     [34mecho[39;49;00m [33m<<<[39;49;00m[33mEOF[39;49;00m[33m[39;49;00m
[33m[39;49;00m
[33m     Test the heredocs...[39;49;00m
[33m[39;49;00m
[33m     [39;49;00m[33mEOF[39;49;00m;

[34mecho[39;49;00m [33m<<<[39;49;00m[33m"[39;49;00m[33msome_delimiter[39;49;00m[33m"[39;49;00m
[33mmore heredoc testing[39;49;00m
[33mcontinues on this line[39;49;00m
[33msome_delimiter[39;49;00m;

[36m?>[39;49;00m
