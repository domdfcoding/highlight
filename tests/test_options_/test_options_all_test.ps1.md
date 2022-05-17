     1^I[37m<#[39;49;00m[37m[39;49;00m$
     2^I[33m.SYNOPSIS[39;49;00m[37m[39;49;00m$
     3^I[37mRuns a T-SQL Query and optional outputs results to a delimited file[39;49;00m[37m.[39;49;00m[37m[39;49;00m$
     4^I[33m.DESCRIPTION[39;49;00m[37m[39;49;00m$
     5^I[37mInvoke-Sql script will run a T-SQL query or stored procedure and optionally outputs a delimited file[39;49;00m[37m.[39;49;00m[37m[39;49;00m$
     6^I[33m.EXAMPLE[39;49;00m[37m[39;49;00m$
     7^I[37mPowerShell[39;49;00m[37m.[39;49;00m[37mexe -File "C:\Scripts\Invoke-Sql[39;49;00m[37m.[39;49;00m[37mps1" -ServerInstance "Z003\sqlprod2" -Database orders -Query "EXEC usp_accounts '12445678'"[39;49;00m$
     8^I[37mThis example connects to Z003\sqlprod2[39;49;00m[37m.[39;49;00m[37mOrders and executes a stored procedure which does not return a result set[39;49;00m$
     9^I[33m.EXAMPLE[39;49;00m[37m[39;49;00m$
    10^I[37mPowerShell[39;49;00m[37m.[39;49;00m[37mexe -File "C:\Scripts\Invoke-Sql[39;49;00m[37m.[39;49;00m[37mps1" -ServerInstance "Z003\sqlprod2" -Database orders -Query "SELECT * FROM dbo[39;49;00m[37m.[39;49;00m[37maccounts" -FilePath "C:\Scripts\accounts[39;49;00m[37m.[39;49;00m[37mtxt" -Delimiter ","[39;49;00m$
    11^I[37mThis example connects to Z003\sqlprod2[39;49;00m[37m.[39;49;00m[37mOrders and selects the records from the accounts tables, the data is outputed to a CSV file[39;49;00m$
    12^I[33m.NOTES[39;49;00m[37m[39;49;00m$
    13^I[37mVersion History[39;49;00m$
    14^I[37mv1[39;49;00m[37m.[39;49;00m[37m0   - Chad Miller - 12/14/2010 - Initial release[39;49;00m$
    15^I[37mIMPORTANT!!! The EventLog source which is set to the application needs to be registered with[39;49;00m$
    16^I[37mthe Event log:[39;49;00m$
    17^I[37mNew-EventLog -LogName Application -Source  $Application[39;49;00m$
    18^I[37m#>[39;49;00m$
    19^I[34mparam[39;49;00m($
    20^I[37m#ServerInstance is Mandatory![39;49;00m$
    21^I[[34mParameter[39;49;00m([34mPosition[39;49;00m=0, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$ServerInstance[39;49;00m,$
    22^I[37m#Database is Mandatory![39;49;00m$
    23^I[[34mParameter[39;49;00m([34mPosition[39;49;00m=1, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$Database[39;49;00m,$
    24^I[37m#Query is Mandatory![39;49;00m$
    25^I[[34mParameter[39;49;00m([34mPosition[39;49;00m=2, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$Query[39;49;00m,$
    26^I[[34mParameter[39;49;00m([34mPosition[39;49;00m=3, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$Application[39;49;00m=[33m"[39;49;00m[33mInvoke-Sql.ps1[39;49;00m[33m"[39;49;00m,$
    27^I[[34mParameter[39;49;00m([34mPosition[39;49;00m=4, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$FilePath[39;49;00m,$
    28^I[[34mParameter[39;49;00m([34mPosition[39;49;00m=7, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$Delimiter[39;49;00m=[33m"[39;49;00m[33m|[39;49;00m[33m"[39;49;00m,$
    29^I[37m#If UserName isn't supplied a trusted connection will be used[39;49;00m$
    30^I[[34mParameter[39;49;00m([34mPosition[39;49;00m=5, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$UserName[39;49;00m,$
    31^I[[34mParameter[39;49;00m([34mPosition[39;49;00m=6, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$Password[39;49;00m,$
    32^I[[34mParameter[39;49;00m([34mPosition[39;49;00m=8, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[Int32][39;49;00m[31m$QueryTimeout[39;49;00m=600,$
    33^I[[34mParameter[39;49;00m([34mPosition[39;49;00m=9, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[Int32][39;49;00m[31m$ConnectionTimeout[39;49;00m=15$
    34^I)$
    35^I $
    36^I $
    37^I[37m#This must be run as administrator on Windows 2008 and higher![39;49;00m$
    38^I[36mNew-EventLog[39;49;00m -LogName Application -Source [31m$Application[39;49;00m -EA SilentlyContinue$
    39^I[31m$Error[39;49;00m.Clear()$
    40^I $
    41^I[37m#######################[39;49;00m$
    42^I[34mfunction[39;49;00m [36mInvoke-SqlCmd2[39;49;00m$
    43^I{$
    44^I    [34mparam[39;49;00m($
    45^I    [[34mParameter[39;49;00m([34mPosition[39;49;00m=0, [34mMandatory[39;49;00m=[31m$true[39;49;00m)] [31m[string][39;49;00m[31m$ServerInstance[39;49;00m,$
    46^I    [[34mParameter[39;49;00m([34mPosition[39;49;00m=1, [34mMandatory[39;49;00m=[31m$true[39;49;00m)] [31m[string][39;49;00m[31m$Database[39;49;00m,$
    47^I    [[34mParameter[39;49;00m([34mPosition[39;49;00m=2, [34mMandatory[39;49;00m=[31m$true[39;49;00m)] [31m[string][39;49;00m[31m$Query[39;49;00m,$
    48^I    [[34mParameter[39;49;00m([34mPosition[39;49;00m=3, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$UserName[39;49;00m,$
    49^I    [[34mParameter[39;49;00m([34mPosition[39;49;00m=4, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$Password[39;49;00m,$
    50^I    [[34mParameter[39;49;00m([34mPosition[39;49;00m=5, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[Int32][39;49;00m[31m$QueryTimeout[39;49;00m,$
    51^I    [[34mParameter[39;49;00m([34mPosition[39;49;00m=6, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[Int32][39;49;00m[31m$ConnectionTimeout[39;49;00m$
    52^I    )$
    53^I $
    54^I    [34mtry[39;49;00m {$
    55^I        [34mif[39;49;00m ([31m$Username[39;49;00m)$
    56^I        { [31m$ConnectionString[39;49;00m = [33m"[39;49;00m[33mServer={0};Database={1};User ID={2};Password={3};Trusted_Connection=False;Connect Timeout={4}[39;49;00m[33m"[39;49;00m -f [31m$ServerInstance[39;49;00m,[31m$Database[39;49;00m,[31m$Username[39;49;00m,[31m$Password[39;49;00m,[31m$ConnectionTimeout[39;49;00m }$
    57^I        [34melse[39;49;00m$
    58^I        { [31m$ConnectionString[39;49;00m = [33m"[39;49;00m[33mServer={0};Database={1};Integrated Security=True;Connect Timeout={2}[39;49;00m[33m"[39;49;00m -f [31m$ServerInstance[39;49;00m,[31m$Database[39;49;00m,[31m$ConnectionTimeout[39;49;00m }$
    59^I        [31m$conn[39;49;00m=[36mnew-object[39;49;00m System.Data.SqlClient.SQLConnection$
    60^I        [31m$conn[39;49;00m.ConnectionString=[31m$ConnectionString[39;49;00m$
    61^I        [31m$conn[39;49;00m.Open()$
    62^I        [31m$cmd[39;49;00m=[36mnew-object[39;49;00m system.Data.SqlClient.SqlCommand([31m$Query[39;49;00m,[31m$conn[39;49;00m)$
    63^I        [31m$cmd[39;49;00m.CommandTimeout=[31m$QueryTimeout[39;49;00m$
    64^I        [31m$ds[39;49;00m=[36mNew-Object[39;49;00m system.Data.DataSet$
    65^I        [31m$da[39;49;00m=[36mNew-Object[39;49;00m system.Data.SqlClient.SqlDataAdapter([31m$cmd[39;49;00m)$
    66^I        [31m[void][39;49;00m[31m$da[39;49;00m.fill([31m$ds[39;49;00m)$
    67^I        [36mWrite-Output[39;49;00m ([31m$ds[39;49;00m.Tables[0])$
    68^I    }$
    69^I    [34mfinally[39;49;00m {$
    70^I        [31m$conn[39;49;00m.Dispose()$
    71^I    }$
    72^I $
    73^I} [37m#Invoke-SqlCmd2[39;49;00m$
    74^I $
    75^I[37m#######################[39;49;00m$
    76^I[37m#       MAIN          #[39;49;00m$
    77^I[37m#######################[39;49;00m$
    78^I[34mif[39;49;00m ([31m$PSBoundParameters[39;49;00m.Count -eq 0)$
    79^I{$
    80^I [36mget-help[39;49;00m [31m$myInvocation[39;49;00m.MyCommand.Path -full$
    81^I [34mbreak[39;49;00m$
    82^I}$
    83^I $
    84^I[34mtry[39;49;00m {$
    85^I    [31m$msg[39;49;00m = [31m$null[39;49;00m$
    86^I    [31m$msg[39;49;00m += [33m"[39;49;00m[33mApplication/Job Name: [39;49;00m[33m$[39;49;00m[33mApplication[39;49;00m[33m`n[39;49;00m[33m"[39;49;00m$
    87^I    [31m$msg[39;49;00m += [33m"[39;49;00m[33mQuery: [39;49;00m[33m$[39;49;00m[33mQuery[39;49;00m[33m`n[39;49;00m[33m"[39;49;00m$
    88^I    [31m$msg[39;49;00m += [33m"[39;49;00m[33mServerInstance: [39;49;00m[33m$[39;49;00m[33mServerInstance[39;49;00m[33m`n[39;49;00m[33m"[39;49;00m$
    89^I    [31m$msg[39;49;00m += [33m"[39;49;00m[33mDatabase: [39;49;00m[33m$[39;49;00m[33mDatabase[39;49;00m[33m`n[39;49;00m[33m"[39;49;00m$
    90^I    [31m$msg[39;49;00m += [33m"[39;49;00m[33mFilePath: [39;49;00m[33m$[39;49;00m[33mFilePath[39;49;00m[33m`n[39;49;00m[33m"[39;49;00m$
    91^I   $
    92^I    [36mWrite-EventLog[39;49;00m -LogName Application -Source [33m"[39;49;00m[33m$[39;49;00m[33mApplication[39;49;00m[33m"[39;49;00m -EntryType Information -EventId 12345 -Message [33m"[39;49;00m[33mStarting[39;49;00m[33m`n[39;49;00m[33m$[39;49;00m[33mmsg[39;49;00m[33m"[39;49;00m$
    93^I    [31m$dt[39;49;00m = [36mInvoke-SqlCmd2[39;49;00m -ServerInstance [31m$ServerInstance[39;49;00m -Database [31m$Database[39;49;00m -Query [31m$Query[39;49;00m -UserName [31m$UserName[39;49;00m -Password [31m$Password[39;49;00m -QueryTimeOut [31m$QueryTimeOut[39;49;00m -ConnectionTimeout [31m$ConnectionTimeout[39;49;00m$
    94^I    [34mif[39;49;00m ([31m$FilePath[39;49;00m)$
    95^I    {$
    96^I        [34mif[39;49;00m ([31m$dt[39;49;00m)$
    97^I        { [31m$dt[39;49;00m | [36mexport-csv[39;49;00m -Delimiter [31m$Delimiter[39;49;00m -Path [31m$FilePath[39;49;00m -NoTypeInformation }$
    98^I        [34melse[39;49;00m [37m#Query Returned No Output![39;49;00m$
    99^I        {[36mWrite-EventLog[39;49;00m -LogName Application -Source [33m"[39;49;00m[33m$[39;49;00m[33mApplication[39;49;00m[33m"[39;49;00m -EntryType Warning -EventId 12345 -Message [33m"[39;49;00m[33mNoOutput[39;49;00m[33m`n[39;49;00m[33m$[39;49;00m[33mmsg[39;49;00m[33m"[39;49;00m }$
   100^I    }$
   101^I $
   102^I    [36mWrite-EventLog[39;49;00m -LogName Application -Source [33m"[39;49;00m[33m$[39;49;00m[33mApplication[39;49;00m[33m"[39;49;00m -EntryType Information -EventId 12345 -Message [33m"[39;49;00m[33mCompleted[39;49;00m[33m`n[39;49;00m[33m$[39;49;00m[33mmsg[39;49;00m[33m"[39;49;00m$
   103^I}$
   104^I[34mcatch[39;49;00m {$
   105^I    [31m$Exception[39;49;00m = [33m"[39;49;00m[33m{0}, {1}[39;49;00m[33m"[39;49;00m -f  [31m$_[39;49;00m.Exception.GetType().FullName,$( [31m$_[39;49;00m.Exception.Message -replace [33m"[39;49;00m[33m'[39;49;00m[33m"[39;49;00m )$
   106^I    [36mWrite-EventLog[39;49;00m -LogName Application -Source [33m"[39;49;00m[33m$[39;49;00m[33mApplication[39;49;00m[33m"[39;49;00m -EntryType Error -EventId 12345 -Message [33m"[39;49;00m[33mError[39;49;00m[33m`n[39;49;00m[33m$[39;49;00m[33mmsg[39;49;00m[33m`n[39;49;00m[33m$[39;49;00m[33mException[39;49;00m[33m"[39;49;00m$
   107^I    [34mthrow[39;49;00m$
   108^I}$
