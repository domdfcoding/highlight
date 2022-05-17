     1	[37m<#[39;49;00m[37m[39;49;00m$
     2	[33m.SYNOPSIS[39;49;00m[37m[39;49;00m$
     3	[37mRuns a T-SQL Query and optional outputs results to a delimited file[39;49;00m[37m.[39;49;00m[37m[39;49;00m$
     4	[33m.DESCRIPTION[39;49;00m[37m[39;49;00m$
     5	[37mInvoke-Sql script will run a T-SQL query or stored procedure and optionally outputs a delimited file[39;49;00m[37m.[39;49;00m[37m[39;49;00m$
     6	[33m.EXAMPLE[39;49;00m[37m[39;49;00m$
     7	[37mPowerShell[39;49;00m[37m.[39;49;00m[37mexe -File "C:\Scripts\Invoke-Sql[39;49;00m[37m.[39;49;00m[37mps1" -ServerInstance "Z003\sqlprod2" -Database orders -Query "EXEC usp_accounts '12445678'"[39;49;00m$
     8	[37mThis example connects to Z003\sqlprod2[39;49;00m[37m.[39;49;00m[37mOrders and executes a stored procedure which does not return a result set[39;49;00m$
     9	[33m.EXAMPLE[39;49;00m[37m[39;49;00m$
    10	[37mPowerShell[39;49;00m[37m.[39;49;00m[37mexe -File "C:\Scripts\Invoke-Sql[39;49;00m[37m.[39;49;00m[37mps1" -ServerInstance "Z003\sqlprod2" -Database orders -Query "SELECT * FROM dbo[39;49;00m[37m.[39;49;00m[37maccounts" -FilePath "C:\Scripts\accounts[39;49;00m[37m.[39;49;00m[37mtxt" -Delimiter ","[39;49;00m$
    11	[37mThis example connects to Z003\sqlprod2[39;49;00m[37m.[39;49;00m[37mOrders and selects the records from the accounts tables, the data is outputed to a CSV file[39;49;00m$
    12	[33m.NOTES[39;49;00m[37m[39;49;00m$
    13	[37mVersion History[39;49;00m$
    14	[37mv1[39;49;00m[37m.[39;49;00m[37m0   - Chad Miller - 12/14/2010 - Initial release[39;49;00m$
    15	[37mIMPORTANT!!! The EventLog source which is set to the application needs to be registered with[39;49;00m$
    16	[37mthe Event log:[39;49;00m$
    17	[37mNew-EventLog -LogName Application -Source  $Application[39;49;00m$
    18	[37m#>[39;49;00m$
    19	[34mparam[39;49;00m($
    20	[37m#ServerInstance is Mandatory![39;49;00m$
    21	[[34mParameter[39;49;00m([34mPosition[39;49;00m=0, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$ServerInstance[39;49;00m,$
    22	[37m#Database is Mandatory![39;49;00m$
    23	[[34mParameter[39;49;00m([34mPosition[39;49;00m=1, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$Database[39;49;00m,$
    24	[37m#Query is Mandatory![39;49;00m$
    25	[[34mParameter[39;49;00m([34mPosition[39;49;00m=2, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$Query[39;49;00m,$
    26	[[34mParameter[39;49;00m([34mPosition[39;49;00m=3, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$Application[39;49;00m=[33m"[39;49;00m[33mInvoke-Sql.ps1[39;49;00m[33m"[39;49;00m,$
    27	[[34mParameter[39;49;00m([34mPosition[39;49;00m=4, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$FilePath[39;49;00m,$
    28	[[34mParameter[39;49;00m([34mPosition[39;49;00m=7, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$Delimiter[39;49;00m=[33m"[39;49;00m[33m|[39;49;00m[33m"[39;49;00m,$
    29	[37m#If UserName isn't supplied a trusted connection will be used[39;49;00m$
    30	[[34mParameter[39;49;00m([34mPosition[39;49;00m=5, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$UserName[39;49;00m,$
    31	[[34mParameter[39;49;00m([34mPosition[39;49;00m=6, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$Password[39;49;00m,$
    32	[[34mParameter[39;49;00m([34mPosition[39;49;00m=8, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[Int32][39;49;00m[31m$QueryTimeout[39;49;00m=600,$
    33	[[34mParameter[39;49;00m([34mPosition[39;49;00m=9, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[Int32][39;49;00m[31m$ConnectionTimeout[39;49;00m=15$
    34	)$
    35	 $
    36	 $
    37	[37m#This must be run as administrator on Windows 2008 and higher![39;49;00m$
    38	[36mNew-EventLog[39;49;00m -LogName Application -Source [31m$Application[39;49;00m -EA SilentlyContinue$
    39	[31m$Error[39;49;00m.Clear()$
    40	 $
    41	[37m#######################[39;49;00m$
    42	[34mfunction[39;49;00m [36mInvoke-SqlCmd2[39;49;00m$
    43	{$
    44	    [34mparam[39;49;00m($
    45	    [[34mParameter[39;49;00m([34mPosition[39;49;00m=0, [34mMandatory[39;49;00m=[31m$true[39;49;00m)] [31m[string][39;49;00m[31m$ServerInstance[39;49;00m,$
    46	    [[34mParameter[39;49;00m([34mPosition[39;49;00m=1, [34mMandatory[39;49;00m=[31m$true[39;49;00m)] [31m[string][39;49;00m[31m$Database[39;49;00m,$
    47	    [[34mParameter[39;49;00m([34mPosition[39;49;00m=2, [34mMandatory[39;49;00m=[31m$true[39;49;00m)] [31m[string][39;49;00m[31m$Query[39;49;00m,$
    48	    [[34mParameter[39;49;00m([34mPosition[39;49;00m=3, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$UserName[39;49;00m,$
    49	    [[34mParameter[39;49;00m([34mPosition[39;49;00m=4, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[string][39;49;00m[31m$Password[39;49;00m,$
    50	    [[34mParameter[39;49;00m([34mPosition[39;49;00m=5, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[Int32][39;49;00m[31m$QueryTimeout[39;49;00m,$
    51	    [[34mParameter[39;49;00m([34mPosition[39;49;00m=6, [34mMandatory[39;49;00m=[31m$false[39;49;00m)] [31m[Int32][39;49;00m[31m$ConnectionTimeout[39;49;00m$
    52	    )$
    53	 $
    54	    [34mtry[39;49;00m {$
    55	        [34mif[39;49;00m ([31m$Username[39;49;00m)$
    56	        { [31m$ConnectionString[39;49;00m = [33m"[39;49;00m[33mServer={0};Database={1};User ID={2};Password={3};Trusted_Connection=False;Connect Timeout={4}[39;49;00m[33m"[39;49;00m -f [31m$ServerInstance[39;49;00m,[31m$Database[39;49;00m,[31m$Username[39;49;00m,[31m$Password[39;49;00m,[31m$ConnectionTimeout[39;49;00m }$
    57	        [34melse[39;49;00m$
    58	        { [31m$ConnectionString[39;49;00m = [33m"[39;49;00m[33mServer={0};Database={1};Integrated Security=True;Connect Timeout={2}[39;49;00m[33m"[39;49;00m -f [31m$ServerInstance[39;49;00m,[31m$Database[39;49;00m,[31m$ConnectionTimeout[39;49;00m }$
    59	        [31m$conn[39;49;00m=[36mnew-object[39;49;00m System.Data.SqlClient.SQLConnection$
    60	        [31m$conn[39;49;00m.ConnectionString=[31m$ConnectionString[39;49;00m$
    61	        [31m$conn[39;49;00m.Open()$
    62	        [31m$cmd[39;49;00m=[36mnew-object[39;49;00m system.Data.SqlClient.SqlCommand([31m$Query[39;49;00m,[31m$conn[39;49;00m)$
    63	        [31m$cmd[39;49;00m.CommandTimeout=[31m$QueryTimeout[39;49;00m$
    64	        [31m$ds[39;49;00m=[36mNew-Object[39;49;00m system.Data.DataSet$
    65	        [31m$da[39;49;00m=[36mNew-Object[39;49;00m system.Data.SqlClient.SqlDataAdapter([31m$cmd[39;49;00m)$
    66	        [31m[void][39;49;00m[31m$da[39;49;00m.fill([31m$ds[39;49;00m)$
    67	        [36mWrite-Output[39;49;00m ([31m$ds[39;49;00m.Tables[0])$
    68	    }$
    69	    [34mfinally[39;49;00m {$
    70	        [31m$conn[39;49;00m.Dispose()$
    71	    }$
    72	 $
    73	} [37m#Invoke-SqlCmd2[39;49;00m$
    74	 $
    75	[37m#######################[39;49;00m$
    76	[37m#       MAIN          #[39;49;00m$
    77	[37m#######################[39;49;00m$
    78	[34mif[39;49;00m ([31m$PSBoundParameters[39;49;00m.Count -eq 0)$
    79	{$
    80	 [36mget-help[39;49;00m [31m$myInvocation[39;49;00m.MyCommand.Path -full$
    81	 [34mbreak[39;49;00m$
    82	}$
    83	 $
    84	[34mtry[39;49;00m {$
    85	    [31m$msg[39;49;00m = [31m$null[39;49;00m$
    86	    [31m$msg[39;49;00m += [33m"[39;49;00m[33mApplication/Job Name: [39;49;00m[33m$[39;49;00m[33mApplication[39;49;00m[33m`n[39;49;00m[33m"[39;49;00m$
    87	    [31m$msg[39;49;00m += [33m"[39;49;00m[33mQuery: [39;49;00m[33m$[39;49;00m[33mQuery[39;49;00m[33m`n[39;49;00m[33m"[39;49;00m$
    88	    [31m$msg[39;49;00m += [33m"[39;49;00m[33mServerInstance: [39;49;00m[33m$[39;49;00m[33mServerInstance[39;49;00m[33m`n[39;49;00m[33m"[39;49;00m$
    89	    [31m$msg[39;49;00m += [33m"[39;49;00m[33mDatabase: [39;49;00m[33m$[39;49;00m[33mDatabase[39;49;00m[33m`n[39;49;00m[33m"[39;49;00m$
    90	    [31m$msg[39;49;00m += [33m"[39;49;00m[33mFilePath: [39;49;00m[33m$[39;49;00m[33mFilePath[39;49;00m[33m`n[39;49;00m[33m"[39;49;00m$
    91	   $
    92	    [36mWrite-EventLog[39;49;00m -LogName Application -Source [33m"[39;49;00m[33m$[39;49;00m[33mApplication[39;49;00m[33m"[39;49;00m -EntryType Information -EventId 12345 -Message [33m"[39;49;00m[33mStarting[39;49;00m[33m`n[39;49;00m[33m$[39;49;00m[33mmsg[39;49;00m[33m"[39;49;00m$
    93	    [31m$dt[39;49;00m = [36mInvoke-SqlCmd2[39;49;00m -ServerInstance [31m$ServerInstance[39;49;00m -Database [31m$Database[39;49;00m -Query [31m$Query[39;49;00m -UserName [31m$UserName[39;49;00m -Password [31m$Password[39;49;00m -QueryTimeOut [31m$QueryTimeOut[39;49;00m -ConnectionTimeout [31m$ConnectionTimeout[39;49;00m$
    94	    [34mif[39;49;00m ([31m$FilePath[39;49;00m)$
    95	    {$
    96	        [34mif[39;49;00m ([31m$dt[39;49;00m)$
    97	        { [31m$dt[39;49;00m | [36mexport-csv[39;49;00m -Delimiter [31m$Delimiter[39;49;00m -Path [31m$FilePath[39;49;00m -NoTypeInformation }$
    98	        [34melse[39;49;00m [37m#Query Returned No Output![39;49;00m$
    99	        {[36mWrite-EventLog[39;49;00m -LogName Application -Source [33m"[39;49;00m[33m$[39;49;00m[33mApplication[39;49;00m[33m"[39;49;00m -EntryType Warning -EventId 12345 -Message [33m"[39;49;00m[33mNoOutput[39;49;00m[33m`n[39;49;00m[33m$[39;49;00m[33mmsg[39;49;00m[33m"[39;49;00m }$
   100	    }$
   101	 $
   102	    [36mWrite-EventLog[39;49;00m -LogName Application -Source [33m"[39;49;00m[33m$[39;49;00m[33mApplication[39;49;00m[33m"[39;49;00m -EntryType Information -EventId 12345 -Message [33m"[39;49;00m[33mCompleted[39;49;00m[33m`n[39;49;00m[33m$[39;49;00m[33mmsg[39;49;00m[33m"[39;49;00m$
   103	}$
   104	[34mcatch[39;49;00m {$
   105	    [31m$Exception[39;49;00m = [33m"[39;49;00m[33m{0}, {1}[39;49;00m[33m"[39;49;00m -f  [31m$_[39;49;00m.Exception.GetType().FullName,$( [31m$_[39;49;00m.Exception.Message -replace [33m"[39;49;00m[33m'[39;49;00m[33m"[39;49;00m )$
   106	    [36mWrite-EventLog[39;49;00m -LogName Application -Source [33m"[39;49;00m[33m$[39;49;00m[33mApplication[39;49;00m[33m"[39;49;00m -EntryType Error -EventId 12345 -Message [33m"[39;49;00m[33mError[39;49;00m[33m`n[39;49;00m[33m$[39;49;00m[33mmsg[39;49;00m[33m`n[39;49;00m[33m$[39;49;00m[33mException[39;49;00m[33m"[39;49;00m$
   107	    [34mthrow[39;49;00m$
   108	}$
