[34mmodule[39;49;00m [04m[36mCodeRay[39;49;00m$
	[34mmodule[39;49;00m [04m[36mScanners[39;49;00m$
$
[34mclass[39;49;00m [04m[32mRuby[39;49;00m < [31mScanner[39;49;00m$
$
	[31mRESERVED_WORDS[39;49;00m = [$
		[33m'[39;49;00m[33mand[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mdef[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mend[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33min[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mor[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33munless[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mbegin[39;49;00m[33m'[39;49;00m,$
		[33m'[39;49;00m[33mdefined?[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mensure[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mmodule[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mredo[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33msuper[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33muntil[39;49;00m[33m'[39;49;00m,$
		[33m'[39;49;00m[33mBEGIN[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mbreak[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mdo[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mnext[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mrescue[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mthen[39;49;00m[33m'[39;49;00m,$
		[33m'[39;49;00m[33mwhen[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mEND[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mcase[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33melse[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mfor[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mretry[39;49;00m[33m'[39;49;00m,$
		[33m'[39;49;00m[33mwhile[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33malias[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mclass[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33melsif[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mif[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mnot[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mreturn[39;49;00m[33m'[39;49;00m,$
		[33m'[39;49;00m[33mundef[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33myield[39;49;00m[33m'[39;49;00m,$
	]$
$
	[31mDEF_KEYWORDS[39;49;00m = [[33m'[39;49;00m[33mdef[39;49;00m[33m'[39;49;00m]$
	[31mMODULE_KEYWORDS[39;49;00m = [[33m'[39;49;00m[33mclass[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mmodule[39;49;00m[33m'[39;49;00m]$
	[31mDEF_NEW_STATE[39;49;00m = [31mWordList[39;49;00m.new([33m:initial[39;49;00m).$
		add([31mDEF_KEYWORDS[39;49;00m, [33m:def_expected[39;49;00m).$
		add([31mMODULE_KEYWORDS[39;49;00m, [33m:module_expected[39;49;00m)$
$
	[31mWORDS_ALLOWING_REGEXP[39;49;00m = [$
		[33m'[39;49;00m[33mand[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mor[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mnot[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mwhile[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33muntil[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33munless[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mif[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33melsif[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mwhen[39;49;00m[33m'[39;49;00m$
	]$
	[31mREGEXP_ALLOWED[39;49;00m = [31mWordList[39;49;00m.new([34mfalse[39;49;00m).$
		add([31mWORDS_ALLOWING_REGEXP[39;49;00m, [33m:set[39;49;00m)$
$
	[31mPREDEFINED_CONSTANTS[39;49;00m = [$
		[33m'[39;49;00m[33mnil[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mtrue[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mfalse[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mself[39;49;00m[33m'[39;49;00m,$
		[33m'[39;49;00m[33mDATA[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mARGV[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mARGF[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m__FILE__[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33m__LINE__[39;49;00m[33m'[39;49;00m,$
	]$
$
	[31mIDENT_KIND[39;49;00m = [31mWordList[39;49;00m.new([33m:ident[39;49;00m).$
		add([31mRESERVED_WORDS[39;49;00m, [33m:reserved[39;49;00m).$
		add([31mPREDEFINED_CONSTANTS[39;49;00m, [33m:pre_constant[39;49;00m)$
$
	[31mMETHOD_NAME[39;49;00m = [33m/[39;49;00m[33m [39;49;00m[33m#{[39;49;00m[31mIDENT[39;49;00m[33m}[39;49;00m[33m [?!]? [39;49;00m[33m/xo[39;49;00m$
	[31mMETHOD_NAME_EX[39;49;00m = [33m/[39;49;00m[33m[39;49;00m$
[33m	 [39;49;00m[33m#{[39;49;00m[31mMETHOD_NAME[39;49;00m[33m}[39;49;00m[33m  [39;49;00m[33m#[39;49;00m[33m common methods: split, foo=, empty?, gsub![39;49;00m$
[33m	 | [39;49;00m[33m\[39;49;00m[33m*[39;49;00m[33m\[39;49;00m[33m*?         [39;49;00m[33m#[39;49;00m[33m multiplication and power[39;49;00m$
[33m	 | [-+~]@?       [39;49;00m[33m#[39;49;00m[33m plus, minus[39;49;00m$
[33m	 | [[39;49;00m[33m\/[39;49;00m[33m%&|^`]     [39;49;00m[33m#[39;49;00m[33m division, modulo or format strings, &and, |or, ^xor, `system`[39;49;00m$
[33m	 | [39;49;00m[33m\[39;49;00m[33m[[39;49;00m[33m\[39;49;00m[33m]=?        [39;49;00m[33m#[39;49;00m[33m array getter and setter[39;49;00m$
[33m	 | <=?>? | >=?   [39;49;00m[33m#[39;49;00m[33m comparison, rocket operator[39;49;00m$
[33m	 | << | >>       [39;49;00m[33m#[39;49;00m[33m append or shift left, shift right[39;49;00m$
[33m	 | ===?          [39;49;00m[33m#[39;49;00m[33m simple equality and case equality[39;49;00m$
[33m	[39;49;00m[33m/ox[39;49;00m$
	[31mGLOBAL_VARIABLE[39;49;00m = [33m/[39;49;00m[33m [39;49;00m[33m\[39;49;00m[33m$ (?: [39;49;00m[33m#{[39;49;00m[31mIDENT[39;49;00m[33m}[39;49;00m[33m | [39;49;00m[33m\[39;49;00m[33md+ | [~&+`'=[39;49;00m[33m\/[39;49;00m[33m,;_.<>!@0$?*":F[39;49;00m[33m\\[39;49;00m[33m] | -[a-zA-Z_0-9] ) [39;49;00m[33m/ox[39;49;00m$
$
	[31mDOUBLEQ[39;49;00m = [33m/[39;49;00m[33m "  [^"[39;49;00m[33m\[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m]*  (?: (?: [39;49;00m[33m\[39;49;00m[33m#[39;49;00m[33m\[39;49;00m[33m{.*?[39;49;00m[33m\[39;49;00m[33m} | [39;49;00m[33m\[39;49;00m[33m#[39;49;00m[33m(?:$")?  | [39;49;00m[33m\\[39;49;00m[33m. ) [^"[39;49;00m[33m\[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m]*  )* "?  [39;49;00m[33m/ox[39;49;00m$
	[31mSINGLEQ[39;49;00m = [33m/[39;49;00m[33m '  [^'[39;49;00m[33m\\[39;49;00m[33m]*    (?:                              [39;49;00m[33m\\[39;49;00m[33m.   [^'[39;49;00m[33m\\[39;49;00m[33m]*    )* '?  [39;49;00m[33m/ox[39;49;00m$
	[31mSTRING[39;49;00m  = [33m/[39;49;00m[33m [39;49;00m[33m#{[39;49;00m[31mSINGLEQ[39;49;00m[33m}[39;49;00m[33m | [39;49;00m[33m#{[39;49;00m[31mDOUBLEQ[39;49;00m[33m}[39;49;00m[33m [39;49;00m[33m/ox[39;49;00m$
	[31mSHELL[39;49;00m   = [33m/[39;49;00m[33m `  [^`[39;49;00m[33m\[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m]*  (?: (?: [39;49;00m[33m\[39;49;00m[33m#[39;49;00m[33m\[39;49;00m[33m{.*?[39;49;00m[33m\[39;49;00m[33m} | [39;49;00m[33m\[39;49;00m[33m#[39;49;00m[33m(?:$`)?  | [39;49;00m[33m\\[39;49;00m[33m. ) [^`[39;49;00m[33m\[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m]*  )* `?  [39;49;00m[33m/ox[39;49;00m$
	[31mREGEXP[39;49;00m  = [33m/[39;49;00m[33m [39;49;00m[33m\/[39;49;00m[33m [^[39;49;00m[33m\/[39;49;00m[33m\[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m]* (?: (?: [39;49;00m[33m\[39;49;00m[33m#[39;49;00m[33m\[39;49;00m[33m{.*?[39;49;00m[33m\[39;49;00m[33m} | [39;49;00m[33m\[39;49;00m[33m#[39;49;00m[33m(?:$[39;49;00m[33m\/[39;49;00m[33m)? | [39;49;00m[33m\\[39;49;00m[33m. ) [^[39;49;00m[33m\/[39;49;00m[33m\[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m]* )* [39;49;00m[33m\/[39;49;00m[33m? [39;49;00m[33m/ox[39;49;00m$
$
	[31mDECIMAL[39;49;00m = [33m/[39;49;00m[33m\[39;49;00m[33md+(?:_[39;49;00m[33m\[39;49;00m[33md+)*[39;49;00m[33m/[39;49;00m  [37m# doesn't recognize 09 as octal error[39;49;00m$
	[31mOCTAL[39;49;00m = [33m/[39;49;00m[33m0_?[0-7]+(?:_[0-7]+)*[39;49;00m[33m/[39;49;00m$
	[31mHEXADECIMAL[39;49;00m = [33m/[39;49;00m[33m0x[0-9A-Fa-f]+(?:_[0-9A-Fa-f]+)*[39;49;00m[33m/[39;49;00m$
	[31mBINARY[39;49;00m = [33m/[39;49;00m[33m0b[01]+(?:_[01]+)*[39;49;00m[33m/[39;49;00m$
$
	[31mEXPONENT[39;49;00m = [33m/[39;49;00m[33m [eE] [+-]? [39;49;00m[33m#{[39;49;00m[31mDECIMAL[39;49;00m[33m}[39;49;00m[33m [39;49;00m[33m/ox[39;49;00m$
	[31mFLOAT[39;49;00m = [33m/[39;49;00m[33m [39;49;00m[33m#{[39;49;00m[31mDECIMAL[39;49;00m[33m}[39;49;00m[33m (?: [39;49;00m[33m#{[39;49;00m[31mEXPONENT[39;49;00m[33m}[39;49;00m[33m | [39;49;00m[33m\[39;49;00m[33m. [39;49;00m[33m#{[39;49;00m[31mDECIMAL[39;49;00m[33m}[39;49;00m[33m [39;49;00m[33m#{[39;49;00m[31mEXPONENT[39;49;00m[33m}[39;49;00m[33m? ) [39;49;00m[33m/[39;49;00m$
	[31mINTEGER[39;49;00m = [33m/[39;49;00m[33m#{[39;49;00m[31mOCTAL[39;49;00m[33m}[39;49;00m[33m|[39;49;00m[33m#{[39;49;00m[31mHEXADECIMAL[39;49;00m[33m}[39;49;00m[33m|[39;49;00m[33m#{[39;49;00m[31mBINARY[39;49;00m[33m}[39;49;00m[33m|[39;49;00m[33m#{[39;49;00m[31mDECIMAL[39;49;00m[33m}[39;49;00m[33m/[39;49;00m$
$
	[34mdef[39;49;00m [32mreset[39;49;00m$
		[34msuper[39;49;00m$
		[31m@regexp_allowed[39;49;00m = [34mfalse[39;49;00m$
	[34mend[39;49;00m$
$
	[34mdef[39;49;00m [32mnext_token[39;49;00m$
		[34mreturn[39;49;00m [34mif[39;49;00m [31m@scanner[39;49;00m.eos?$
$
		kind = [33m:error[39;49;00m$
		[34mif[39;49;00m [31m@scanner[39;49;00m.scan([33m/[39;49;00m[33m\[39;49;00m[33ms+[39;49;00m[33m/[39;49;00m)  [37m# in every state[39;49;00m$
			kind = [33m:space[39;49;00m$
			[31m@regexp_allowed[39;49;00m = [33m:set[39;49;00m [34mif[39;49;00m [31m@regexp_allowed[39;49;00m [35mor[39;49;00m [31m@scanner[39;49;00m.matched.index([33m?\n[39;49;00m)  [37m# delayed flag setting[39;49;00m$
$
		[34melsif[39;49;00m [31m@state[39;49;00m == [33m:def_expected[39;49;00m$
			[34mif[39;49;00m [31m@scanner[39;49;00m.scan([33m/[39;49;00m[33m (?: (?:[39;49;00m[33m#{[39;49;00m[31mIDENT[39;49;00m[33m}[39;49;00m[33m(?:[39;49;00m[33m\[39;49;00m[33m.|::))* | (?:@@?|$)? [39;49;00m[33m#{[39;49;00m[31mIDENT[39;49;00m[33m}[39;49;00m[33m(?:[39;49;00m[33m\[39;49;00m[33m.|::) ) [39;49;00m[33m#{[39;49;00m[31mMETHOD_NAME_EX[39;49;00m[33m}[39;49;00m[33m [39;49;00m[33m/ox[39;49;00m)$
				kind = [33m:method[39;49;00m$
				[31m@state[39;49;00m = [33m:initial[39;49;00m$
			[34melse[39;49;00m$
				[31m@scanner[39;49;00m.getch$
			[34mend[39;49;00m$
			[31m@state[39;49;00m = [33m:initial[39;49;00m$
$
		[34melsif[39;49;00m [31m@state[39;49;00m == [33m:module_expected[39;49;00m$
			[34mif[39;49;00m [31m@scanner[39;49;00m.scan([33m/[39;49;00m[33m<<[39;49;00m[33m/[39;49;00m)$
				kind = [33m:operator[39;49;00m$
			[34melse[39;49;00m$
				[34mif[39;49;00m [31m@scanner[39;49;00m.scan([33m/[39;49;00m[33m (?: [39;49;00m[33m#{[39;49;00m[31mIDENT[39;49;00m[33m}[39;49;00m[33m (?:[39;49;00m[33m\[39;49;00m[33m.|::))* [39;49;00m[33m#{[39;49;00m[31mIDENT[39;49;00m[33m}[39;49;00m[33m [39;49;00m[33m/ox[39;49;00m)$
					kind = [33m:method[39;49;00m$
				[34melse[39;49;00m$
					[31m@scanner[39;49;00m.getch$
				[34mend[39;49;00m$
				[31m@state[39;49;00m = [33m:initial[39;49;00m$
			[34mend[39;49;00m$
$
		[34melsif[39;49;00m [37m# state == :initial[39;49;00m$
			[37m# IDENTIFIERS, KEYWORDS[39;49;00m$
			[34mif[39;49;00m [31m@scanner[39;49;00m.scan([31mGLOBAL_VARIABLE[39;49;00m)$
				kind = [33m:global_variable[39;49;00m$
			[34melsif[39;49;00m [31m@scanner[39;49;00m.scan([33m/[39;49;00m[33m @@ [39;49;00m[33m#{[39;49;00m[31mIDENT[39;49;00m[33m}[39;49;00m[33m [39;49;00m[33m/ox[39;49;00m)$
				kind = [33m:class_variable[39;49;00m$
			[34melsif[39;49;00m [31m@scanner[39;49;00m.scan([33m/[39;49;00m[33m @ [39;49;00m[33m#{[39;49;00m[31mIDENT[39;49;00m[33m}[39;49;00m[33m [39;49;00m[33m/ox[39;49;00m)$
				kind = [33m:instance_variable[39;49;00m$
			[34melsif[39;49;00m [31m@scanner[39;49;00m.scan([33m/[39;49;00m[33m __END__[39;49;00m[33m\[39;49;00m[33mn ( (?![39;49;00m[33m\[39;49;00m[33m#[39;49;00m[33mCODE[39;49;00m[33m\[39;49;00m[33m#[39;49;00m[33m) .* )? | [39;49;00m[33m\[39;49;00m[33m#[39;49;00m[33m[^[39;49;00m[33m\[39;49;00m[33mn]* | =begin(?=[39;49;00m[33m\[39;49;00m[33ms).*? [39;49;00m[33m\[39;49;00m[33mn=end(?=[39;49;00m[33m\[39;49;00m[33ms|[39;49;00m[33m\[39;49;00m[33mz)(?:[^[39;49;00m[33m\[39;49;00m[33mn]*)? [39;49;00m[33m/mx[39;49;00m)$
				kind = [33m:comment[39;49;00m$
			[34melsif[39;49;00m [31m@scanner[39;49;00m.scan([31mMETHOD_NAME[39;49;00m)$
				[34mif[39;49;00m [31m@last_token_dot[39;49;00m$
					kind = [33m:ident[39;49;00m$
				[34melse[39;49;00m$
					matched = [31m@scanner[39;49;00m.matched$
					kind = [31mIDENT_KIND[39;49;00m[matched]$
					[34mif[39;49;00m kind == [33m:ident[39;49;00m [35mand[39;49;00m matched =~ [33m/[39;49;00m[33m^[A-Z][39;49;00m[33m/[39;49;00m$
						kind = [33m:constant[39;49;00m$
					[34melsif[39;49;00m kind == [33m:reserved[39;49;00m$
						[31m@state[39;49;00m = [31mDEF_NEW_STATE[39;49;00m[matched]$
						[31m@regexp_allowed[39;49;00m = [31mREGEXP_ALLOWED[39;49;00m[matched]$
					[34mend[39;49;00m$
				[34mend[39;49;00m$
$
			[34melsif[39;49;00m [31m@scanner[39;49;00m.scan([31mSTRING[39;49;00m)$
				kind = [33m:string[39;49;00m$
			[34melsif[39;49;00m [31m@scanner[39;49;00m.scan([31mSHELL[39;49;00m)$
				kind = [33m:shell[39;49;00m$
			[34melsif[39;49;00m [31m@scanner[39;49;00m.scan([33m/[39;49;00m[33m<<[39;49;00m$
[33m				(?:[39;49;00m$
[33m					([a-zA-Z_0-9]+)[39;49;00m$
[33m						(?: .*? ^[39;49;00m[33m\[39;49;00m[33m1$ | .* )[39;49;00m$
[33m				|[39;49;00m$
[33m					-([a-zA-Z_0-9]+)[39;49;00m$
[33m						(?: .*? ^[39;49;00m[33m\[39;49;00m[33ms*[39;49;00m[33m\[39;49;00m[33m2$ | .* )[39;49;00m$
[33m				|[39;49;00m$
[33m					(["[39;49;00m[33m\[39;49;00m[33m'`]) (.+?) [39;49;00m[33m\[39;49;00m[33m3[39;49;00m$
[33m						(?: .*? ^[39;49;00m[33m\[39;49;00m[33m4$ | .* )[39;49;00m$
[33m				|[39;49;00m$
[33m					- (["[39;49;00m[33m\[39;49;00m[33m'`]) (.+?) [39;49;00m[33m\[39;49;00m[33m5[39;49;00m$
[33m						(?: .*? ^[39;49;00m[33m\[39;49;00m[33ms*[39;49;00m[33m\[39;49;00m[33m6$ | .* )[39;49;00m$
[33m				)[39;49;00m$
[33m			[39;49;00m[33m/mxo[39;49;00m)$
				kind = [33m:string[39;49;00m$
			[34melsif[39;49;00m [31m@scanner[39;49;00m.scan([33m/[39;49;00m[33m\/[39;49;00m[33m/[39;49;00m) [35mand[39;49;00m [31m@regexp_allowed[39;49;00m$
				[31m@scanner[39;49;00m.unscan$
				[31m@scanner[39;49;00m.scan([31mREGEXP[39;49;00m)$
				kind = [33m:regexp[39;49;00m$
[33m/[39;49;00m[33m%(?:[Qqxrw](?:[39;49;00m[33m\[39;49;00m[33m([^)[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*(?:(?:[39;49;00m[33m#[39;49;00m[33m\[39;49;00m[33m{.*?[39;49;00m[33m\[39;49;00m[33m}|[39;49;00m[33m#[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m.)[^)[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*)*[39;49;00m[33m\[39;49;00m[33m)?|[39;49;00m[33m\[39;49;00m[33m[[^[39;49;00m[33m\[39;49;00m[33m][39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*(?:(?:[39;49;00m[33m#[39;49;00m[33m\[39;49;00m[33m{.*?[39;49;00m[33m\[39;49;00m[33m}|[39;49;00m[33m#[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m.)[^[39;49;00m[33m\[39;49;00m[33m][39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*)*[39;49;00m[33m\[39;49;00m[33m]?|[39;49;00m[33m\[39;49;00m[33m{[^}[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*(?:(?:[39;49;00m[33m#[39;49;00m[33m\[39;49;00m[33m{.*?[39;49;00m[33m\[39;49;00m[33m}|[39;49;00m[33m#[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m.)[^}[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*)*[39;49;00m[33m\[39;49;00m[33m}?|<[^>[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*(?:(?:[39;49;00m[33m#[39;49;00m[33m\[39;49;00m[33m{.*?[39;49;00m[33m\[39;49;00m[33m}|[39;49;00m[33m#[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m.)[^>[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*)*>?|([^a-zA-Z[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m])(?:(?![39;49;00m[33m\[39;49;00m[33m1)[^[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m])*(?:(?:[39;49;00m[33m#[39;49;00m[33m\[39;49;00m[33m{.*?[39;49;00m[33m\[39;49;00m[33m}|[39;49;00m[33m#[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m.)(?:(?![39;49;00m[33m\[39;49;00m[33m1)[^[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m])*)*[39;49;00m[33m\[39;49;00m[33m1?)|[39;49;00m[33m\[39;49;00m[33m([^)[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*(?:(?:[39;49;00m[33m#[39;49;00m[33m\[39;49;00m[33m{.*?[39;49;00m[33m\[39;49;00m[33m}|[39;49;00m[33m#[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m.)[^)[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*)*[39;49;00m[33m\[39;49;00m[33m)?|[39;49;00m[33m\[39;49;00m[33m[[^[39;49;00m[33m\[39;49;00m[33m][39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*(?:(?:[39;49;00m[33m#[39;49;00m[33m\[39;49;00m[33m{.*?[39;49;00m[33m\[39;49;00m[33m}|[39;49;00m[33m#[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m.)[^[39;49;00m[33m\[39;49;00m[33m][39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*)*[39;49;00m[33m\[39;49;00m[33m]?|[39;49;00m[33m\[39;49;00m[33m{[^}[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*(?:(?:[39;49;00m[33m#[39;49;00m[33m\[39;49;00m[33m{.*?[39;49;00m[33m\[39;49;00m[33m}|[39;49;00m[33m#[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m.)[^}[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*)*[39;49;00m[33m\[39;49;00m[33m}?|<[^>[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*(?:(?:[39;49;00m[33m#[39;49;00m[33m\[39;49;00m[33m{.*?[39;49;00m[33m\[39;49;00m[33m}|[39;49;00m[33m#[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m.)[^>[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*)*>?|([^a-zA-Z[39;49;00m[33m\[39;49;00m[33ms[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m])(?:(?![39;49;00m[33m\[39;49;00m[33m2)[^[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m])*(?:(?:[39;49;00m[33m#[39;49;00m[33m\[39;49;00m[33m{.*?[39;49;00m[33m\[39;49;00m[33m}|[39;49;00m[33m#[39;49;00m[33m|[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m.)(?:(?![39;49;00m[33m\[39;49;00m[33m2)[^[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m])*)*[39;49;00m[33m\[39;49;00m[33m2?|[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m[^[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*(?:(?:[39;49;00m[33m#[39;49;00m[33m\[39;49;00m[33m{.*?[39;49;00m[33m\[39;49;00m[33m}|[39;49;00m[33m#[39;49;00m[33m)[^[39;49;00m[33m#[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m]*)*[39;49;00m[33m\\[39;49;00m[33m\\[39;49;00m[33m?)[39;49;00m[33m/[39;49;00m$
			[34melsif[39;49;00m [31m@scanner[39;49;00m.scan([33m/[39;49;00m[33m:(?:[39;49;00m[33m#{[39;49;00m[31mGLOBAL_VARIABLE[39;49;00m[33m}[39;49;00m[33m|[39;49;00m[33m#{[39;49;00m[31mMETHOD_NAME_EX[39;49;00m[33m}[39;49;00m[33m|[39;49;00m[33m#{[39;49;00m[31mSTRING[39;49;00m[33m}[39;49;00m[33m)[39;49;00m[33m/ox[39;49;00m)$
				kind = [33m:symbol[39;49;00m$
			[34melsif[39;49;00m [31m@scanner[39;49;00m.scan([33m/[39;49;00m[33m[39;49;00m$
[33m				[39;49;00m[33m\[39;49;00m[33m? (?:[39;49;00m$
[33m					[^[39;49;00m[33m\[39;49;00m[33ms[39;49;00m[33m\\[39;49;00m[33m][39;49;00m$
[33m				|[39;49;00m$
[33m					[39;49;00m[33m\\[39;49;00m[33m (?:M-[39;49;00m[33m\\[39;49;00m[33mC-|C-[39;49;00m[33m\\[39;49;00m[33mM-|M-[39;49;00m[33m\\[39;49;00m[33mc|c[39;49;00m[33m\\[39;49;00m[33mM-|c|C-|M-))? (?: [39;49;00m[33m\\[39;49;00m[33m (?: . | [0-7]{3} | x[0-9A-Fa-f][0-9A-Fa-f] )[39;49;00m$
[33m				)[39;49;00m$
[33m			[39;49;00m[33m/mox[39;49;00m)$
				kind = [33m:integer[39;49;00m$
$
			[34melsif[39;49;00m [31m@scanner[39;49;00m.scan([33m/[39;49;00m[33m [-+*[39;49;00m[33m\/[39;49;00m[33m%=<>;,|&!()[39;49;00m[33m\[39;49;00m[33m[[39;49;00m[33m\[39;49;00m[33m]{}~?] | [39;49;00m[33m\[39;49;00m[33m.[39;49;00m[33m\[39;49;00m[33m.?[39;49;00m[33m\[39;49;00m[33m.? | ::? [39;49;00m[33m/x[39;49;00m)$
				kind = [33m:operator[39;49;00m$
				[31m@regexp_allowed[39;49;00m = [33m:set[39;49;00m [34mif[39;49;00m [31m@scanner[39;49;00m.matched[-[34m1[39;49;00m,[34m1[39;49;00m] =~ [33m/[39;49;00m[33m[~=!<>|&^,[39;49;00m[33m\[39;49;00m[33m([39;49;00m[33m\[39;49;00m[33m[+[39;49;00m[33m\[39;49;00m[33m-[39;49;00m[33m\/[39;49;00m[33m\[39;49;00m[33m*%][39;49;00m[33m\[39;49;00m[33mz[39;49;00m[33m/[39;49;00m$
			[34melsif[39;49;00m [31m@scanner[39;49;00m.scan([31mFLOAT[39;49;00m)$
				kind = [33m:float[39;49;00m$
			[34melsif[39;49;00m [31m@scanner[39;49;00m.scan([31mINTEGER[39;49;00m)$
				kind = [33m:integer[39;49;00m$
			[34melse[39;49;00m$
				[31m@scanner[39;49;00m.getch$
			[34mend[39;49;00m$
		[34mend[39;49;00m$
$
		token = [31mToken[39;49;00m.new [31m@scanner[39;49;00m.matched, kind$
$
		[34mif[39;49;00m kind == [33m:regexp[39;49;00m$
			token.text << [31m@scanner[39;49;00m.scan([33m/[39;49;00m[33m[eimnosux]*[39;49;00m[33m/[39;49;00m)$
		[34mend[39;49;00m$
$
		[31m@regexp_allowed[39;49;00m = ([31m@regexp_allowed[39;49;00m == [33m:set[39;49;00m)  [37m# delayed flag setting[39;49;00m$
$
		token$
	[34mend[39;49;00m$
[34mend[39;49;00m$
$
register [31mRuby[39;49;00m, [33m'[39;49;00m[33mruby[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mrb[39;49;00m[33m'[39;49;00m$
$
	[34mend[39;49;00m$
[34mend[39;49;00m$
[34mclass[39;49;00m [04m[32mSet[39;49;00m$
  [34minclude[39;49;00m [31mEnumerable[39;49;00m$
$
  [37m# Creates a new set containing the given objects.[39;49;00m$
  [34mdef[39;49;00m [04m[32mself[39;49;00m.[32m[][39;49;00m(*ary)$
    [34mnew[39;49;00m(ary)$
  [34mend[39;49;00m$
$
  [37m# Creates a new set containing the elements of the given enumerable[39;49;00m$
  [37m# object.[39;49;00m$
  [37m#[39;49;00m$
  [37m# If a block is given, the elements of enum are preprocessed by the[39;49;00m$
  [37m# given block.[39;49;00m$
  [34mdef[39;49;00m [32minitialize[39;49;00m(enum = [34mnil[39;49;00m, &block) [37m# :yields: o[39;49;00m$
    [31m@hash[39;49;00m ||= [31mHash[39;49;00m.new$
$
    enum.nil? [35mand[39;49;00m [34mreturn[39;49;00m$
$
    [34mif[39;49;00m block$
      enum.each { |o| add(block[o]) }$
    [34melse[39;49;00m$
      merge(enum)$
    [34mend[39;49;00m$
  [34mend[39;49;00m$
$
  [37m# Copy internal hash.[39;49;00m$
  [34mdef[39;49;00m [32minitialize_copy[39;49;00m(orig)$
    [31m@hash[39;49;00m = orig.instance_eval{[31m@hash[39;49;00m}.dup$
  [34mend[39;49;00m$
$
  [37m# Returns the number of elements.[39;49;00m$
  [34mdef[39;49;00m [32msize[39;49;00m$
    [31m@hash[39;49;00m.size$
  [34mend[39;49;00m$
  [34malias[39;49;00m length size$
$
  [37m# Returns true if the set contains no elements.[39;49;00m$
  [34mdef[39;49;00m [32mempty?[39;49;00m$
    [31m@hash[39;49;00m.empty?$
  [34mend[39;49;00m$
$
  [37m# Removes all elements and returns self.[39;49;00m$
  [34mdef[39;49;00m [32mclear[39;49;00m$
    [31m@hash[39;49;00m.clear$
    [36mself[39;49;00m$
  [34mend[39;49;00m$
$
  [37m# Replaces the contents of the set with the contents of the given[39;49;00m$
  [37m# enumerable object and returns self.[39;49;00m$
  [34mdef[39;49;00m [32mreplace[39;49;00m(enum)$
    [34mif[39;49;00m enum.class == [36mself[39;49;00m.class$
      [31m@hash[39;49;00m.replace(enum.instance_eval { [31m@hash[39;49;00m })$
    [34melse[39;49;00m$
      enum.is_a?([31mEnumerable[39;49;00m) [35mor[39;49;00m [34mraise[39;49;00m [31mArgumentError[39;49;00m, [33m"[39;49;00m[33mvalue must be enumerable[39;49;00m[33m"[39;49;00m$
      clear$
      enum.each { |o| add(o) }$
    [34mend[39;49;00m$
$
    [36mself[39;49;00m$
  [34mend[39;49;00m$
$
  [37m# Converts the set to an array.  The order of elements is uncertain.[39;49;00m$
  [34mdef[39;49;00m [32mto_a[39;49;00m$
    [31m@hash[39;49;00m.keys$
  [34mend[39;49;00m$
$
  [34mdef[39;49;00m [32mflatten_merge[39;49;00m(set, seen = [31mSet[39;49;00m.new)$
    set.each { |e|$
      [34mif[39;49;00m e.is_a?([31mSet[39;49;00m)$
	[34mif[39;49;00m seen.include?(e_id = e.object_id)$
	  [34mraise[39;49;00m [31mArgumentError[39;49;00m, [33m"[39;49;00m[33mtried to flatten recursive Set[39;49;00m[33m"[39;49;00m$
	[34mend[39;49;00m$
$
	seen.add(e_id)$
	flatten_merge(e, seen)$
	seen.delete(e_id)$
      [34melse[39;49;00m$
	add(e)$
      [34mend[39;49;00m$
    }$
$
    [36mself[39;49;00m$
  [34mend[39;49;00m$
  [34mprotected[39;49;00m [33m:flatten_merge[39;49;00m$
$
  [37m# Returns a new set that is a copy of the set, flattening each[39;49;00m$
  [37m# containing set recursively.[39;49;00m$
  [34mdef[39;49;00m [32mflatten[39;49;00m$
    [36mself[39;49;00m.class.new.flatten_merge([36mself[39;49;00m)$
  [34mend[39;49;00m$
$
  [37m# Equivalent to Set#flatten, but replaces the receiver with the[39;49;00m$
  [37m# result in place.  Returns nil if no modifications were made.[39;49;00m$
  [34mdef[39;49;00m [32mflatten![39;49;00m$
    [34mif[39;49;00m detect { |e| e.is_a?([31mSet[39;49;00m) }$
      replace(flatten())$
    [34melse[39;49;00m$
      [34mnil[39;49;00m$
    [34mend[39;49;00m$
  [34mend[39;49;00m$
$
  [37m# Returns true if the set contains the given object.[39;49;00m$
  [34mdef[39;49;00m [32minclude?[39;49;00m(o)$
    [31m@hash[39;49;00m.include?(o)$
  [34mend[39;49;00m$
  [34malias[39;49;00m member? [34minclude[39;49;00m?$
$
  [37m# Returns true if the set is a superset of the given set.[39;49;00m$
  [34mdef[39;49;00m [32msuperset?[39;49;00m(set)$
    set.is_a?([31mSet[39;49;00m) [35mor[39;49;00m [34mraise[39;49;00m [31mArgumentError[39;49;00m, [33m"[39;49;00m[33mvalue must be a set[39;49;00m[33m"[39;49;00m$
    [34mreturn[39;49;00m [34mfalse[39;49;00m [34mif[39;49;00m size < set.size$
    set.all? { |o| [34minclude[39;49;00m?(o) }$
  [34mend[39;49;00m$
$
  [37m# Returns true if the set is a proper superset of the given set.[39;49;00m$
  [34mdef[39;49;00m [32mproper_superset?[39;49;00m(set)$
    set.is_a?([31mSet[39;49;00m) [35mor[39;49;00m [34mraise[39;49;00m [31mArgumentError[39;49;00m, [33m"[39;49;00m[33mvalue must be a set[39;49;00m[33m"[39;49;00m$
    [34mreturn[39;49;00m [34mfalse[39;49;00m [34mif[39;49;00m size <= set.size$
    set.all? { |o| [34minclude[39;49;00m?(o) }$
  [34mend[39;49;00m$
$
  [37m# Returns true if the set is a subset of the given set.[39;49;00m$
  [34mdef[39;49;00m [32msubset?[39;49;00m(set)$
    set.is_a?([31mSet[39;49;00m) [35mor[39;49;00m [34mraise[39;49;00m [31mArgumentError[39;49;00m, [33m"[39;49;00m[33mvalue must be a set[39;49;00m[33m"[39;49;00m$
    [34mreturn[39;49;00m [34mfalse[39;49;00m [34mif[39;49;00m set.size < size$
    all? { |o| set.include?(o) }$
  [34mend[39;49;00m$
$
  [37m# Returns true if the set is a proper subset of the given set.[39;49;00m$
  [34mdef[39;49;00m [32mproper_subset?[39;49;00m(set)$
    set.is_a?([31mSet[39;49;00m) [35mor[39;49;00m [34mraise[39;49;00m [31mArgumentError[39;49;00m, [33m"[39;49;00m[33mvalue must be a set[39;49;00m[33m"[39;49;00m$
    [34mreturn[39;49;00m [34mfalse[39;49;00m [34mif[39;49;00m set.size <= size$
    all? { |o| set.include?(o) }$
  [34mend[39;49;00m$
$
  [37m# Calls the given block once for each element in the set, passing[39;49;00m$
  [37m# the element as parameter.[39;49;00m$
  [34mdef[39;49;00m [32meach[39;49;00m$
    [31m@hash[39;49;00m.each_key { |o| [34myield[39;49;00m(o) }$
    [36mself[39;49;00m$
  [34mend[39;49;00m$
$
  [37m# Adds the given object to the set and returns self.  Use +merge+ to[39;49;00m$
  [37m# add several elements at once.[39;49;00m$
  [34mdef[39;49;00m [32madd[39;49;00m(o)$
    [31m@hash[39;49;00m[o] = [34mtrue[39;49;00m$
    [36mself[39;49;00m$
  [34mend[39;49;00m$
  [34malias[39;49;00m << add$
$
  [37m# Adds the given object to the set and returns self.  If the[39;49;00m$
  [37m# object is already in the set, returns nil.[39;49;00m$
  [34mdef[39;49;00m [32madd?[39;49;00m(o)$
    [34mif[39;49;00m [34minclude[39;49;00m?(o)$
      [34mnil[39;49;00m$
    [34melse[39;49;00m$
      add(o)$
    [34mend[39;49;00m$
  [34mend[39;49;00m$
$
  [37m# Deletes the given object from the set and returns self.  Use +subtract+ to[39;49;00m$
  [37m# delete several items at once.[39;49;00m$
  [34mdef[39;49;00m [32mdelete[39;49;00m(o)$
    [31m@hash[39;49;00m.delete(o)$
    [36mself[39;49;00m$
  [34mend[39;49;00m$
$
  [37m# Deletes the given object from the set and returns self.  If the[39;49;00m$
  [37m# object is not in the set, returns nil.[39;49;00m$
  [34mdef[39;49;00m [32mdelete?[39;49;00m(o)$
    [34mif[39;49;00m [34minclude[39;49;00m?(o)$
      delete(o)$
    [34melse[39;49;00m$
      [34mnil[39;49;00m$
    [34mend[39;49;00m$
  [34mend[39;49;00m$
$
  [37m# Deletes every element of the set for which block evaluates to[39;49;00m$
  [37m# true, and returns self.[39;49;00m$
  [34mdef[39;49;00m [32mdelete_if[39;49;00m$
    [31m@hash[39;49;00m.delete_if { |o,| [34myield[39;49;00m(o) }$
    [36mself[39;49;00m$
  [34mend[39;49;00m$
$
  [37m# Do collect() destructively.[39;49;00m$
  [34mdef[39;49;00m [32mcollect![39;49;00m$
    set = [36mself[39;49;00m.class.new$
    each { |o| set << [34myield[39;49;00m(o) }$
    replace(set)$
  [34mend[39;49;00m$
  [34malias[39;49;00m map! collect!$
$
  [37m# Equivalent to Set#delete_if, but returns nil if no changes were[39;49;00m$
  [37m# made.[39;49;00m$
  [34mdef[39;49;00m [32mreject![39;49;00m$
    n = size$
    delete_if { |o| [34myield[39;49;00m(o) }$
    size == n ? [34mnil[39;49;00m : [36mself[39;49;00m$
  [34mend[39;49;00m$
$
  [37m# Merges the elements of the given enumerable object to the set and[39;49;00m$
  [37m# returns self.[39;49;00m$
  [34mdef[39;49;00m [32mmerge[39;49;00m(enum)$
    [34mif[39;49;00m enum.is_a?([31mSet[39;49;00m)$
      [31m@hash[39;49;00m.update(enum.instance_eval { [31m@hash[39;49;00m })$
    [34melse[39;49;00m$
      enum.is_a?([31mEnumerable[39;49;00m) [35mor[39;49;00m [34mraise[39;49;00m [31mArgumentError[39;49;00m, [33m"[39;49;00m[33mvalue must be enumerable[39;49;00m[33m"[39;49;00m$
      enum.each { |o| add(o) }$
    [34mend[39;49;00m$
$
    [36mself[39;49;00m$
  [34mend[39;49;00m$
$
  [37m# Deletes every element that appears in the given enumerable object[39;49;00m$
  [37m# and returns self.[39;49;00m$
  [34mdef[39;49;00m [32msubtract[39;49;00m(enum)$
    enum.is_a?([31mEnumerable[39;49;00m) [35mor[39;49;00m [34mraise[39;49;00m [31mArgumentError[39;49;00m, [33m"[39;49;00m[33mvalue must be enumerable[39;49;00m[33m"[39;49;00m$
    enum.each { |o| delete(o) }$
    [36mself[39;49;00m$
  [34mend[39;49;00m$
$
  [37m# Returns a new set built by merging the set and the elements of the[39;49;00m$
  [37m# given enumerable object.[39;49;00m$
  [34mdef[39;49;00m [32m|[39;49;00m(enum)$
    enum.is_a?([31mEnumerable[39;49;00m) [35mor[39;49;00m [34mraise[39;49;00m [31mArgumentError[39;49;00m, [33m"[39;49;00m[33mvalue must be enumerable[39;49;00m[33m"[39;49;00m$
    [36mdup[39;49;00m.merge(enum)$
  [34mend[39;49;00m$
  [34malias[39;49;00m + |		[37m##[39;49;00m$
  [34malias[39;49;00m union |		[37m##[39;49;00m$
$
  [37m# Returns a new set built by duplicating the set, removing every[39;49;00m$
  [37m# element that appears in the given enumerable object.[39;49;00m$
  [34mdef[39;49;00m [32m-[39;49;00m(enum)$
    enum.is_a?([31mEnumerable[39;49;00m) [35mor[39;49;00m [34mraise[39;49;00m [31mArgumentError[39;49;00m, [33m"[39;49;00m[33mvalue must be enumerable[39;49;00m[33m"[39;49;00m$
    [36mdup[39;49;00m.subtract(enum)$
  [34mend[39;49;00m$
  [34malias[39;49;00m difference -	[37m##[39;49;00m$
$
  [37m# Returns a new array containing elements common to the set and the[39;49;00m$
  [37m# given enumerable object.[39;49;00m$
  [34mdef[39;49;00m [32m&[39;49;00m(enum)$
    enum.is_a?([31mEnumerable[39;49;00m) [35mor[39;49;00m [34mraise[39;49;00m [31mArgumentError[39;49;00m, [33m"[39;49;00m[33mvalue must be enumerable[39;49;00m[33m"[39;49;00m$
    n = [36mself[39;49;00m.class.new$
    enum.each { |o| n.add(o) [34mif[39;49;00m [34minclude[39;49;00m?(o) }$
    n$
  [34mend[39;49;00m$
  [34malias[39;49;00m intersection &	[37m##[39;49;00m$
$
  [37m# Returns a new array containing elements exclusive between the set[39;49;00m$
  [37m# and the given enumerable object.  (set ^ enum) is equivalent to[39;49;00m$
  [37m# ((set | enum) - (set & enum)).[39;49;00m$
  [34mdef[39;49;00m [32m^[39;49;00m(enum)$
    enum.is_a?([31mEnumerable[39;49;00m) [35mor[39;49;00m [34mraise[39;49;00m [31mArgumentError[39;49;00m, [33m"[39;49;00m[33mvalue must be enumerable[39;49;00m[33m"[39;49;00m$
    n = [36mdup[39;49;00m$
    enum.each { |o| [34mif[39;49;00m n.include?(o) [34mthen[39;49;00m n.delete(o) [34melse[39;49;00m n.add(o) [34mend[39;49;00m }$
    n$
  [34mend[39;49;00m$
$
  [37m# Returns true if two sets are equal.  The equality of each couple[39;49;00m$
  [37m# of elements is defined according to Object#eql?.[39;49;00m$
  [34mdef[39;49;00m [32m==[39;49;00m(set)$
    [36mequal?[39;49;00m(set) [35mand[39;49;00m [34mreturn[39;49;00m [34mtrue[39;49;00m$
$
    set.is_a?([31mSet[39;49;00m) && size == set.size [35mor[39;49;00m [34mreturn[39;49;00m [34mfalse[39;49;00m$
$
    [36mhash[39;49;00m = [31m@hash[39;49;00m.dup$
    set.all? { |o| [36mhash[39;49;00m.include?(o) }$
  [34mend[39;49;00m$
$
  [34mdef[39;49;00m [32mhash[39;49;00m	[37m# :nodoc:[39;49;00m$
    [31m@hash[39;49;00m.hash$
  [34mend[39;49;00m$
$
  [34mdef[39;49;00m [32meql?[39;49;00m(o)	[37m# :nodoc:[39;49;00m$
    [34mreturn[39;49;00m [34mfalse[39;49;00m [34munless[39;49;00m o.is_a?([31mSet[39;49;00m)$
    [31m@hash[39;49;00m.eql?(o.instance_eval{[31m@hash[39;49;00m})$
  [34mend[39;49;00m$
$
  [37m# Classifies the set by the return value of the given block and[39;49;00m$
  [37m# returns a hash of {value => set of elements} pairs.  The block is[39;49;00m$
  [37m# called once for each element of the set, passing the element as[39;49;00m$
  [37m# parameter.[39;49;00m$
  [37m#[39;49;00m$
  [37m# e.g.:[39;49;00m$
  [37m#[39;49;00m$
  [37m#   require 'set'[39;49;00m$
  [37m#   files = Set.new(Dir.glob("*.rb"))[39;49;00m$
  [37m#   hash = files.classify { |f| File.mtime(f).year }[39;49;00m$
  [37m#   p hash    # => {2000=>#<Set: {"a.rb", "b.rb"}>,[39;49;00m$
  [37m#             #     2001=>#<Set: {"c.rb", "d.rb", "e.rb"}>,[39;49;00m$
  [37m#             #     2002=>#<Set: {"f.rb"}>}[39;49;00m$
  [34mdef[39;49;00m [32mclassify[39;49;00m [37m# :yields: o[39;49;00m$
    h = {}$
$
    each { |i|$
      x = [34myield[39;49;00m(i)$
      (h[x] ||= [36mself[39;49;00m.class.new).add(i)$
    }$
$
    h$
  [34mend[39;49;00m$
$
  [37m# Divides the set into a set of subsets according to the commonality[39;49;00m$
  [37m# defined by the given block.[39;49;00m$
  [37m#[39;49;00m$
  [37m# If the arity of the block is 2, elements o1 and o2 are in common[39;49;00m$
  [37m# if block.call(o1, o2) is true.  Otherwise, elements o1 and o2 are[39;49;00m$
  [37m# in common if block.call(o1) == block.call(o2).[39;49;00m$
  [37m#[39;49;00m$
  [37m# e.g.:[39;49;00m$
  [37m#[39;49;00m$
  [37m#   require 'set'[39;49;00m$
  [37m#   numbers = Set[1, 3, 4, 6, 9, 10, 11][39;49;00m$
  [37m#   set = numbers.divide { |i,j| (i - j).abs == 1 }[39;49;00m$
  [37m#   p set     # => #<Set: {#<Set: {1}>,[39;49;00m$
  [37m#             #            #<Set: {11, 9, 10}>,[39;49;00m$
  [37m#             #            #<Set: {3, 4}>,[39;49;00m$
  [37m#             #            #<Set: {6}>}>[39;49;00m$
  [34mdef[39;49;00m [32mdivide[39;49;00m(&func)$
    [34mif[39;49;00m func.arity == [34m2[39;49;00m$
      [36mrequire[39;49;00m [33m'[39;49;00m[33mtsort[39;49;00m[33m'[39;49;00m$
$
      [34mclass[39;49;00m << dig = {}		[37m# :nodoc:[39;49;00m$
	[34minclude[39;49;00m [31mTSort[39;49;00m$
$
	[34malias[39;49;00m tsort_each_node each_key$
	[34mdef[39;49;00m [32mtsort_each_child[39;49;00m(node, &block)$
	  fetch(node).each(&block)$
	[34mend[39;49;00m$
      [34mend[39;49;00m$
$
      each { |u|$
	dig[u] = a = []$
	each{ |v| func.call(u, v) [35mand[39;49;00m a << v }$
      }$
$
      set = [31mSet[39;49;00m.new()$
      dig.each_strongly_connected_component { |css|$
	set.add([36mself[39;49;00m.class.new(css))$
      }$
      set$
    [34melse[39;49;00m$
      [31mSet[39;49;00m.new(classify(&func).values)$
    [34mend[39;49;00m$
  [34mend[39;49;00m$
$
  [31mInspectKey[39;49;00m = [33m:__inspect_key__[39;49;00m         [37m# :nodoc:[39;49;00m$
$
  [37m# Returns a string containing a human-readable representation of the[39;49;00m$
  [37m# set. ("#<Set: {element1, element2, ...}>")[39;49;00m$
  [34mdef[39;49;00m [32minspect[39;49;00m$
    ids = ([31mThread[39;49;00m.current[[31mInspectKey[39;49;00m] ||= [])$
$
    [34mif[39;49;00m ids.include?([36mobject_id[39;49;00m)$
      [34mreturn[39;49;00m [36msprintf[39;49;00m([33m'[39;49;00m[33m#[39;49;00m[33m<%s: {...}>[39;49;00m[33m'[39;49;00m, [36mself[39;49;00m.class.name)$
    [34mend[39;49;00m$
$
    [34mbegin[39;49;00m$
      ids << [36mobject_id[39;49;00m$
      [34mreturn[39;49;00m [36msprintf[39;49;00m([33m'[39;49;00m[33m#[39;49;00m[33m<%s: {%s}>[39;49;00m[33m'[39;49;00m, [36mself[39;49;00m.class, [36mto_a[39;49;00m.inspect[[34m1[39;49;00m..-[34m2[39;49;00m])$
    [34mensure[39;49;00m$
      ids.pop$
    [34mend[39;49;00m$
  [34mend[39;49;00m$
$
  [34mdef[39;49;00m [32mpretty_print[39;49;00m(pp)	[37m# :nodoc:[39;49;00m$
    pp.text [36msprintf[39;49;00m([33m'[39;49;00m[33m#[39;49;00m[33m<%s: {[39;49;00m[33m'[39;49;00m, [36mself[39;49;00m.class.name)$
    pp.nest([34m1[39;49;00m) {$
      pp.seplist([36mself[39;49;00m) { |o|$
	pp.pp o$
      }$
    }$
    pp.text [33m"[39;49;00m[33m}>[39;49;00m[33m"[39;49;00m$
  [34mend[39;49;00m$
$
  [34mdef[39;49;00m [32mpretty_print_cycle[39;49;00m(pp)	[37m# :nodoc:[39;49;00m$
    pp.text [36msprintf[39;49;00m([33m'[39;49;00m[33m#[39;49;00m[33m<%s: {%s}>[39;49;00m[33m'[39;49;00m, [36mself[39;49;00m.class.name, empty? ? [33m'[39;49;00m[33m'[39;49;00m : [33m'[39;49;00m[33m...[39;49;00m[33m'[39;49;00m)$
  [34mend[39;49;00m$
[34mend[39;49;00m$
$
[37m# SortedSet implements a set which elements are sorted in order.  See Set.[39;49;00m$
[34mclass[39;49;00m [04m[32mSortedSet[39;49;00m < [31mSet[39;49;00m$
  [31m@@setup[39;49;00m = [34mfalse[39;49;00m$
$
  [34mclass[39;49;00m << [36mself[39;49;00m$
    [34mdef[39;49;00m [32m[][39;49;00m(*ary)	[37m# :nodoc:[39;49;00m$
      [34mnew[39;49;00m(ary)$
    [34mend[39;49;00m$
$
    [34mdef[39;49;00m [32msetup[39;49;00m	[37m# :nodoc:[39;49;00m$
      [31m@@setup[39;49;00m [35mand[39;49;00m [34mreturn[39;49;00m$
$
      [34mbegin[39;49;00m$
	[36mrequire[39;49;00m [33m'[39;49;00m[33mrbtree[39;49;00m[33m'[39;49;00m$
$
	[36mmodule_eval[39;49;00m [33m%{[39;49;00m[33m[39;49;00m$
[33m	  def initialize(*args, &block)[39;49;00m$
[33m	    @hash = RBTree.new[39;49;00m$
[33m	    super[39;49;00m$
[33m	  end[39;49;00m$
[33m	[39;49;00m[33m}[39;49;00m$
      [34mrescue[39;49;00m [31mLoadError[39;49;00m$
	[36mmodule_eval[39;49;00m [33m%{[39;49;00m[33m[39;49;00m$
[33m	  def initialize(*args, &block)[39;49;00m$
[33m	    @keys = nil[39;49;00m$
[33m	    super[39;49;00m$
[33m	  end[39;49;00m$
[33m[39;49;00m$
[33m	  def clear[39;49;00m$
[33m	    @keys = nil[39;49;00m$
[33m	    super[39;49;00m$
[33m	  end[39;49;00m$
[33m[39;49;00m$
[33m	  def replace(enum)[39;49;00m$
[33m	    @keys = nil[39;49;00m$
[33m	    super[39;49;00m$
[33m	  end[39;49;00m$
[33m[39;49;00m$
[33m	  def add(o)[39;49;00m$
[33m	    @keys = nil[39;49;00m$
[33m	    @hash[o] = true[39;49;00m$
[33m	    self[39;49;00m$
[33m	  end[39;49;00m$
[33m	  alias << add[39;49;00m$
[33m[39;49;00m$
[33m	  def delete(o)[39;49;00m$
[33m	    @keys = nil[39;49;00m$
[33m	    @hash.delete(o)[39;49;00m$
[33m	    self[39;49;00m$
[33m	  end[39;49;00m$
[33m[39;49;00m$
[33m	  def delete_if[39;49;00m$
[33m	    n = @hash.size[39;49;00m$
[33m	    @hash.delete_if [39;49;00m[33m{[39;49;00m[33m |o,| yield(o) [39;49;00m[33m}[39;49;00m[33m[39;49;00m$
[33m	    @keys = nil if @hash.size != n[39;49;00m$
[33m	    self[39;49;00m$
[33m	  end[39;49;00m$
[33m[39;49;00m$
[33m	  def merge(enum)[39;49;00m$
[33m	    @keys = nil[39;49;00m$
[33m	    super[39;49;00m$
[33m	  end[39;49;00m$
[33m[39;49;00m$
[33m	  def each[39;49;00m$
[33m	    to_a.each [39;49;00m[33m{[39;49;00m[33m |o| yield(o) [39;49;00m[33m}[39;49;00m[33m[39;49;00m$
[33m	  end[39;49;00m$
[33m[39;49;00m$
[33m	  def to_a[39;49;00m$
[33m	    (@keys = @hash.keys).sort! unless @keys[39;49;00m$
[33m	    @keys[39;49;00m$
[33m	  end[39;49;00m$
[33m	[39;49;00m[33m}[39;49;00m$
      [34mend[39;49;00m$
$
      [31m@@setup[39;49;00m = [34mtrue[39;49;00m$
    [34mend[39;49;00m$
  [34mend[39;49;00m$
$
  [34mdef[39;49;00m [32minitialize[39;49;00m(*args, &block)	[37m# :nodoc:[39;49;00m$
    [31mSortedSet[39;49;00m.setup$
    [34minitialize[39;49;00m(*args, &block)$
  [34mend[39;49;00m$
[34mend[39;49;00m$
$
[34mmodule[39;49;00m [04m[36mEnumerable[39;49;00m$
  [37m# Makes a set from the enumerable object with given arguments.[39;49;00m$
  [34mdef[39;49;00m [32mto_set[39;49;00m(klass = [31mSet[39;49;00m, *args, &block)$
    klass.new([36mself[39;49;00m, *args, &block)$
  [34mend[39;49;00m$
[34mend[39;49;00m$
$
[37m# =begin[39;49;00m$
[37m# == RestricedSet class[39;49;00m$
[37m# RestricedSet implements a set with restrictions defined by a given[39;49;00m$
[37m# block.[39;49;00m$
[37m#[39;49;00m$
[37m# === Super class[39;49;00m$
[37m#     Set[39;49;00m$
[37m#[39;49;00m$
[37m# === Class Methods[39;49;00m$
[37m# --- RestricedSet::new(enum = nil) { |o| ... }[39;49;00m$
[37m# --- RestricedSet::new(enum = nil) { |rset, o| ... }[39;49;00m$
[37m#     Creates a new restricted set containing the elements of the given[39;49;00m$
[37m#     enumerable object.  Restrictions are defined by the given block.[39;49;00m$
[37m#[39;49;00m$
[37m#     If the block's arity is 2, it is called with the RestrictedSet[39;49;00m$
[37m#     itself and an object to see if the object is allowed to be put in[39;49;00m$
[37m#     the set.[39;49;00m$
[37m#[39;49;00m$
[37m#     Otherwise, the block is called with an object to see if the object[39;49;00m$
[37m#     is allowed to be put in the set.[39;49;00m$
[37m#[39;49;00m$
[37m# === Instance Methods[39;49;00m$
[37m# --- restriction_proc[39;49;00m$
[37m#     Returns the restriction procedure of the set.[39;49;00m$
[37m#[39;49;00m$
[37m# =end[39;49;00m$
[37m#[39;49;00m$
[37m# class RestricedSet < Set[39;49;00m$
[37m#   def initialize(*args, &block)[39;49;00m$
[37m#     @proc = block or raise ArgumentError, "missing a block"[39;49;00m$
[37m#[39;49;00m$
[37m#     if @proc.arity == 2[39;49;00m$
[37m#       instance_eval %{[39;49;00m$
[37m# 	def add(o)[39;49;00m$
[37m# 	  @hash[o] = true if @proc.call(self, o)[39;49;00m$
[37m# 	  self[39;49;00m$
[37m# 	end[39;49;00m$
[37m# 	alias << add[39;49;00m$
[37m#[39;49;00m$
[37m# 	def add?(o)[39;49;00m$
[37m# 	  if include?(o) || !@proc.call(self, o)[39;49;00m$
[37m# 	    nil[39;49;00m$
[37m# 	  else[39;49;00m$
[37m# 	    @hash[o] = true[39;49;00m$
[37m# 	    self[39;49;00m$
[37m# 	  end[39;49;00m$
[37m# 	end[39;49;00m$
[37m#[39;49;00m$
[37m# 	def replace(enum)[39;49;00m$
[37m# 	  enum.is_a?(Enumerable) or raise ArgumentError, "value must be enumerable"[39;49;00m$
[37m# 	  clear[39;49;00m$
[37m# 	  enum.each { |o| add(o) }[39;49;00m$
[37m#[39;49;00m$
[37m# 	  self[39;49;00m$
[37m# 	end[39;49;00m$
[37m#[39;49;00m$
[37m# 	def merge(enum)[39;49;00m$
[37m# 	  enum.is_a?(Enumerable) or raise ArgumentError, "value must be enumerable"[39;49;00m$
[37m# 	  enum.each { |o| add(o) }[39;49;00m$
[37m#[39;49;00m$
[37m# 	  self[39;49;00m$
[37m# 	end[39;49;00m$
[37m#       }[39;49;00m$
[37m#     else[39;49;00m$
[37m#       instance_eval %{[39;49;00m$
[37m# 	def add(o)[39;49;00m$
[37m#         if @proc.call(o)[39;49;00m$
[37m# 	    @hash[o] = true[39;49;00m$
[37m#         end[39;49;00m$
[37m# 	  self[39;49;00m$
[37m# 	end[39;49;00m$
[37m# 	alias << add[39;49;00m$
[37m#[39;49;00m$
[37m# 	def add?(o)[39;49;00m$
[37m# 	  if include?(o) || !@proc.call(o)[39;49;00m$
[37m# 	    nil[39;49;00m$
[37m# 	  else[39;49;00m$
[37m# 	    @hash[o] = true[39;49;00m$
[37m# 	    self[39;49;00m$
[37m# 	  end[39;49;00m$
[37m# 	end[39;49;00m$
[37m#       }[39;49;00m$
[37m#     end[39;49;00m$
[37m#[39;49;00m$
[37m#     super(*args)[39;49;00m$
[37m#   end[39;49;00m$
[37m#[39;49;00m$
[37m#   def restriction_proc[39;49;00m$
[37m#     @proc[39;49;00m$
[37m#   end[39;49;00m$
[37m# end[39;49;00m$
$
[34mif[39;49;00m [31m$0[39;49;00m == [36m__FILE__[39;49;00m$
  [36meval[39;49;00m [31mDATA[39;49;00m.read, [34mnil[39;49;00m, [31m$0[39;49;00m, [36m__LINE__[39;49;00m+[34m4[39;49;00m$
[34mend[39;49;00m$
$
[37m# = rweb - CGI Support Library[39;49;00m$
[37m#[39;49;00m$
[37m# Author:: Johannes Barre (mailto:rweb@igels.net)[39;49;00m$
[37m# Copyright:: Copyright (c) 2003, 04 by Johannes Barre[39;49;00m$
[37m# License:: GNU Lesser General Public License (COPYING, http://www.gnu.org/copyleft/lesser.html)[39;49;00m$
[37m# Version:: 0.1.0[39;49;00m$
[37m# CVS-ID:: $Id: example.rb 39 2005-11-05 03:33:55Z murphy $[39;49;00m$
[37m#[39;49;00m$
[37m# == What is Rweb?[39;49;00m$
[37m# Rweb is a replacement for the cgi class included in the ruby distribution.[39;49;00m$
[37m#[39;49;00m$
[37m# == How to use[39;49;00m$
[37m#[39;49;00m$
[37m# === Basics[39;49;00m$
[37m#[39;49;00m$
[37m# This class is made to be as easy as possible to use. An example:[39;49;00m$
[37m#[39;49;00m$
[37m# 	require "rweb"[39;49;00m$
[37m#[39;49;00m$
[37m# 	web = Rweb.new[39;49;00m$
[37m# 	web.out do[39;49;00m$
[37m# 		web.puts "Hello world!"[39;49;00m$
[37m# 	end[39;49;00m$
[37m#[39;49;00m$
[37m# The visitor will get a simple "Hello World!" in his browser. Please notice,[39;49;00m$
[37m# that won't set html-tags for you, so you should better do something like this:[39;49;00m$
[37m#[39;49;00m$
[37m# 	require "rweb"[39;49;00m$
[37m#[39;49;00m$
[37m# 	web = Rweb.new[39;49;00m$
[37m# 	web.out do[39;49;00m$
[37m# 		web.puts "<html><body>Hello world!</body></html>"[39;49;00m$
[37m# 	end[39;49;00m$
[37m#[39;49;00m$
[37m# === Set headers[39;49;00m$
[37m# Of course, it's also possible to tell the browser, that the content of this[39;49;00m$
[37m# page is plain text instead of html code:[39;49;00m$
[37m#[39;49;00m$
[37m# 	require "rweb"[39;49;00m$
[37m#[39;49;00m$
[37m# 	web = Rweb.new[39;49;00m$
[37m# 	web.out do[39;49;00m$
[37m# 		web.header("content-type: text/plain")[39;49;00m$
[37m# 		web.puts "Hello plain world!"[39;49;00m$
[37m# 	end[39;49;00m$
[37m#[39;49;00m$
[37m# Please remember, headers can't be set after the page content has been send.[39;49;00m$
[37m# You have to set all nessessary headers before the first puts oder print. It's[39;49;00m$
[37m# possible to cache the content until everything is complete. Doing it this[39;49;00m$
[37m# way, you can set headers everywhere.[39;49;00m$
[37m#[39;49;00m$
[37m# If you set a header twice, the second header will replace the first one. The[39;49;00m$
[37m# header name is not casesensitive, it will allways converted in to the[39;49;00m$
[37m# capitalised form suggested by the w3c (http://w3.org)[39;49;00m$
[37m#[39;49;00m$
[37m# === Set cookies[39;49;00m$
[37m# Setting cookies is quite easy:[39;49;00m$
[37m# 	include 'rweb'[39;49;00m$
[37m#[39;49;00m$
[37m# 	web = Rweb.new[39;49;00m$
[37m# 	Cookie.new("Visits", web.cookies['visits'].to_i +1)[39;49;00m$
[37m# 	web.out do[39;49;00m$
[37m# 		web.puts "Welcome back! You visited this page #{web.cookies['visits'].to_i +1} times"[39;49;00m$
[37m# 	end[39;49;00m$
[37m#[39;49;00m$
[37m# See the class Cookie for more details.[39;49;00m$
[37m#[39;49;00m$
[37m# === Get form and cookie values[39;49;00m$
[37m# There are four ways to submit data from the browser to the server and your[39;49;00m$
[37m# ruby script: via GET, POST, cookies and file upload. Rweb doesn't support[39;49;00m$
[37m# file upload by now.[39;49;00m$
[37m#[39;49;00m$
[37m# 	include 'rweb'[39;49;00m$
[37m#[39;49;00m$
[37m# 	web = Rweb.new[39;49;00m$
[37m# 	web.out do[39;49;00m$
[37m# 		web.print "action: #{web.get['action']} "[39;49;00m$
[37m# 		web.puts "The value of the cookie 'visits' is #{web.cookies['visits']}"[39;49;00m$
[37m# 		web.puts "The post parameter 'test['x']' is #{web.post['test']['x']}"[39;49;00m$
[37m# 	end[39;49;00m$
$
[31mRWEB_VERSION[39;49;00m = [33m"[39;49;00m[33m0.1.0[39;49;00m[33m"[39;49;00m$
[31mRWEB[39;49;00m = [33m"[39;49;00m[33mrweb/[39;49;00m[33m#{[39;49;00m[31mRWEB_VERSION[39;49;00m[33m}[39;49;00m[33m"[39;49;00m$
$
[37m#require 'rwebcookie' -> edit by bunny :-)[39;49;00m$
$
[34mclass[39;49;00m [04m[32mRweb[39;49;00m$
    [37m# All parameter submitted via the GET method are available in attribute[39;49;00m$
		[37m# get. This is Hash, where every parameter is available as a key-value[39;49;00m$
		[37m# pair.[39;49;00m$
		[37m#[39;49;00m$
		[37m# If your input tag has a name like this one, it's value will be available[39;49;00m$
		[37m# as web.get["fieldname"][39;49;00m$
		[37m#  <input name="fieldname">[39;49;00m$
		[37m# You can submit values as a Hash[39;49;00m$
		[37m#  <input name="text['index']">[39;49;00m$
		[37m#  <input name="text['index2']">[39;49;00m$
		[37m# will be available as[39;49;00m$
		[37m#  web.get["text"]["index"][39;49;00m$
		[37m#  web.get["text"]["index2"][39;49;00m$
		[37m# Integers are also possible[39;49;00m$
		[37m#  <input name="int[2]">[39;49;00m$
		[37m#  <input name="int[3]['hi']>[39;49;00m$
		[37m# will be available as[39;49;00m$
		[37m#  web.get["int"][2][39;49;00m$
		[37m#  web.get["int"][3]["hi"][39;49;00m$
		[37m# If you specify no index, the lowest unused index will be used:[39;49;00m$
		[37m#  <input name="int[]"><!-- First Field -->[39;49;00m$
		[37m#  <input name="int[]"><!-- Second one -->[39;49;00m$
		[37m# will be available as[39;49;00m$
		[37m#  web.get["int"][0] # First Field[39;49;00m$
		[37m#  web.get["int"][1] # Second one[39;49;00m$
		[37m# Please notice, this doesn'd work like you might expect:[39;49;00m$
		[37m#  <input name="text[index]">[39;49;00m$
		[37m# It will not be available as web.get["text"]["index"] but[39;49;00m$
		[37m#  web.get["text[index]"][39;49;00m$
    [34mattr_reader[39;49;00m [33m:get[39;49;00m$
$
    [37m# All parameters submitted via POST are available in the attribute post. It[39;49;00m$
		[37m# works like the get attribute.[39;49;00m$
		[37m#  <input name="text[0]">[39;49;00m$
		[37m# will be available as[39;49;00m$
		[37m#  web.post["text"][0][39;49;00m$
		[34mattr_reader[39;49;00m [33m:post[39;49;00m$
$
    [37m# All cookies submitted by the browser are available in cookies. This is a[39;49;00m$
		[37m# Hash, where every cookie is a key-value pair.[39;49;00m$
		[34mattr_reader[39;49;00m [33m:cookies[39;49;00m$
$
    [37m# The name of the browser identification is submitted as USER_AGENT and[39;49;00m$
		[37m# available in this attribute.[39;49;00m$
		[34mattr_reader[39;49;00m [33m:user_agent[39;49;00m$
$
    [37m# The IP address of the client.[39;49;00m$
		[34mattr_reader[39;49;00m [33m:remote_addr[39;49;00m$
$
    [37m# Creates a new Rweb object. This should only done once. You can set various[39;49;00m$
    [37m# options via the settings hash.[39;49;00m$
    [37m#[39;49;00m$
    [37m# "cache" => true: Everything you script send to the client will be cached[39;49;00m$
    [37m# until the end of the out block or until flush is called. This way, you[39;49;00m$
    [37m# can modify headers and cookies even after printing something to the client.[39;49;00m$
    [37m#[39;49;00m$
    [37m# "safe" => level: Changes the $SAFE attribute. By default, $SAFE will be set[39;49;00m$
    [37m# to 1. If $SAFE is already higher than this value, it won't be changed.[39;49;00m$
    [37m#[39;49;00m$
    [37m# "silend" => true: Normaly, Rweb adds automaticly a header like this[39;49;00m$
    [37m# "X-Powered-By: Rweb/x.x.x (Ruby/y.y.y)". With the silend option you can[39;49;00m$
    [37m# suppress this.[39;49;00m$
    [34mdef[39;49;00m [32minitialize[39;49;00m (settings = {})$
        [37m# {{{[39;49;00m$
        [31m@header[39;49;00m = {}$
        [31m@cookies[39;49;00m = {}$
        [31m@get[39;49;00m = {}$
        [31m@post[39;49;00m = {}$
$
        [37m# Internal attributes[39;49;00m$
        [31m@status[39;49;00m = [34mnil[39;49;00m$
        [31m@reasonPhrase[39;49;00m = [34mnil[39;49;00m$
        [31m@setcookies[39;49;00m = []$
        [31m@output_started[39;49;00m = [34mfalse[39;49;00m;$
        [31m@output_allowed[39;49;00m = [34mfalse[39;49;00m;$
$
        [31m@mod_ruby[39;49;00m = [34mfalse[39;49;00m$
        [31m@env[39;49;00m = [31mENV[39;49;00m.to_hash$
$
        [34mif[39;49;00m defined?([31mMOD_RUBY[39;49;00m)$
            [31m@output_method[39;49;00m = [33m"[39;49;00m[33mmod_ruby[39;49;00m[33m"[39;49;00m$
            [31m@mod_ruby[39;49;00m = [34mtrue[39;49;00m$
        [34melsif[39;49;00m [31m@env[39;49;00m[[33m'[39;49;00m[33mSERVER_SOFTWARE[39;49;00m[33m'[39;49;00m] =~ [33m/[39;49;00m[33m^Microsoft-IIS[39;49;00m[33m/i[39;49;00m$
            [31m@output_method[39;49;00m = [33m"[39;49;00m[33mnph[39;49;00m[33m"[39;49;00m$
        [34melse[39;49;00m$
            [31m@output_method[39;49;00m = [33m"[39;49;00m[33mph[39;49;00m[33m"[39;49;00m$
        [34mend[39;49;00m$
$
        [34munless[39;49;00m settings.is_a?([31mHash[39;49;00m)$
            [34mraise[39;49;00m [31mTypeError[39;49;00m, [33m"[39;49;00m[33msettings must be a Hash[39;49;00m[33m"[39;49;00m$
        [34mend[39;49;00m$
        [31m@settings[39;49;00m = settings$
$
        [34munless[39;49;00m [31m@settings[39;49;00m.has_key?([33m"[39;49;00m[33msafe[39;49;00m[33m"[39;49;00m)$
            [31m@settings[39;49;00m[[33m"[39;49;00m[33msafe[39;49;00m[33m"[39;49;00m] = [34m1[39;49;00m$
        [34mend[39;49;00m$
$
        [34mif[39;49;00m [31m$SAFE[39;49;00m < [31m@settings[39;49;00m[[33m"[39;49;00m[33msafe[39;49;00m[33m"[39;49;00m]$
            [31m$SAFE[39;49;00m = [31m@settings[39;49;00m[[33m"[39;49;00m[33msafe[39;49;00m[33m"[39;49;00m]$
        [34mend[39;49;00m$
$
        [34munless[39;49;00m [31m@settings[39;49;00m.has_key?([33m"[39;49;00m[33mcache[39;49;00m[33m"[39;49;00m)$
            [31m@settings[39;49;00m[[33m"[39;49;00m[33mcache[39;49;00m[33m"[39;49;00m] = [34mfalse[39;49;00m$
        [34mend[39;49;00m$
$
        [37m# mod_ruby sets no QUERY_STRING variable, if no GET-Parameters are given[39;49;00m$
        [34munless[39;49;00m [31m@env[39;49;00m.has_key?([33m"[39;49;00m[33mQUERY_STRING[39;49;00m[33m"[39;49;00m)$
            [31m@env[39;49;00m[[33m"[39;49;00m[33mQUERY_STRING[39;49;00m[33m"[39;49;00m] = [33m"[39;49;00m[33m"[39;49;00m$
        [34mend[39;49;00m$
$
        [37m# Now we split the QUERY_STRING by the seperators & and ; or, if[39;49;00m$
        [37m# specified, settings['get seperator'][39;49;00m$
        [34munless[39;49;00m [31m@settings[39;49;00m.has_key?([33m"[39;49;00m[33mget seperator[39;49;00m[33m"[39;49;00m)$
            get_args = [31m@env[39;49;00m[[33m'[39;49;00m[33mQUERY_STRING[39;49;00m[33m'[39;49;00m].split([33m/[39;49;00m[33m[&;][39;49;00m[33m/[39;49;00m)$
        [34melse[39;49;00m$
            get_args = [31m@env[39;49;00m[[33m'[39;49;00m[33mQUERY_STRING[39;49;00m[33m'[39;49;00m].split([31m@settings[39;49;00m[[33m'[39;49;00m[33mget seperator[39;49;00m[33m'[39;49;00m])$
        [34mend[39;49;00m$
$
        get_args.each [34mdo[39;49;00m | arg |$
            arg_key, arg_val = arg.split([33m/[39;49;00m[33m=[39;49;00m[33m/[39;49;00m, [34m2[39;49;00m)$
            arg_key = [31mRweb[39;49;00m::unescape(arg_key)$
            arg_val = [31mRweb[39;49;00m::unescape(arg_val)$
$
            [37m# Parse names like name[0], name['text'] or name[][39;49;00m$
            pattern = [33m/[39;49;00m[33m^(.+)[39;49;00m[33m\[39;49;00m[33m[("[^[39;49;00m[33m\[39;49;00m[33m]]*"|'[^[39;49;00m[33m\[39;49;00m[33m]]*'|[0-9]*)[39;49;00m[33m\[39;49;00m[33m]$[39;49;00m[33m/[39;49;00m$
            keys = []$
            [34mwhile[39;49;00m match = pattern.match(arg_key)$
                arg_key = match[[34m1[39;49;00m]$
                keys = [match[[34m2[39;49;00m]] + keys$
            [34mend[39;49;00m$
            keys = [arg_key] + keys$
$
            akt = [31m@get[39;49;00m$
            last = [34mnil[39;49;00m$
            lastkey = [34mnil[39;49;00m$
            keys.each [34mdo[39;49;00m |key|$
                [34mif[39;49;00m key == [33m"[39;49;00m[33m"[39;49;00m$
                    [37m# No key specified (like in "test[]"), so we use the[39;49;00m$
                    [37m# lowerst unused Integer as key[39;49;00m$
                    key = [34m0[39;49;00m$
                    [34mwhile[39;49;00m akt.has_key?(key)$
                        key += [34m1[39;49;00m$
                    [34mend[39;49;00m$
                [34melsif[39;49;00m [33m/[39;49;00m[33m^[0-9]*$[39;49;00m[33m/[39;49;00m =~ key$
                    [37m# If the index is numerical convert it to an Integer[39;49;00m$
                    key = key.to_i$
                [34melsif[39;49;00m key[[34m0[39;49;00m].chr == [33m"[39;49;00m[33m'[39;49;00m[33m"[39;49;00m || key[[34m0[39;49;00m].chr == [33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m$
                    key = key[[34m1[39;49;00m, key.length() -[34m2[39;49;00m]$
                [34mend[39;49;00m$
                [34mif[39;49;00m !akt.has_key?(key) || !akt[key].class == [31mHash[39;49;00m$
                    [37m# create an empty Hash if there isn't already one[39;49;00m$
                    akt[key] = {}$
                [34mend[39;49;00m$
                last = akt$
                lastkey = key$
                akt = akt[key]$
            [34mend[39;49;00m$
            last[lastkey] = arg_val$
        [34mend[39;49;00m$
$
        [34mif[39;49;00m [31m@env[39;49;00m[[33m'[39;49;00m[33mREQUEST_METHOD[39;49;00m[33m'[39;49;00m] == [33m"[39;49;00m[33mPOST[39;49;00m[33m"[39;49;00m$
            [34mif[39;49;00m [31m@env[39;49;00m.has_key?([33m"[39;49;00m[33mCONTENT_TYPE[39;49;00m[33m"[39;49;00m) && [31m@env[39;49;00m[[33m'[39;49;00m[33mCONTENT_TYPE[39;49;00m[33m'[39;49;00m] == [33m"[39;49;00m[33mapplication/x-www-form-urlencoded[39;49;00m[33m"[39;49;00m && [31m@env[39;49;00m.has_key?([33m'[39;49;00m[33mCONTENT_LENGTH[39;49;00m[33m'[39;49;00m)$
                [34munless[39;49;00m [31m@settings[39;49;00m.has_key?([33m"[39;49;00m[33mpost seperator[39;49;00m[33m"[39;49;00m)$
                    post_args = [31m$stdin[39;49;00m.read([31m@env[39;49;00m[[33m'[39;49;00m[33mCONTENT_LENGTH[39;49;00m[33m'[39;49;00m].to_i).split([33m/[39;49;00m[33m[&;][39;49;00m[33m/[39;49;00m)$
                [34melse[39;49;00m$
                    post_args = [31m$stdin[39;49;00m.read([31m@env[39;49;00m[[33m'[39;49;00m[33mCONTENT_LENGTH[39;49;00m[33m'[39;49;00m].to_i).split([31m@settings[39;49;00m[[33m'[39;49;00m[33mpost seperator[39;49;00m[33m'[39;49;00m])$
                [34mend[39;49;00m$
                post_args.each [34mdo[39;49;00m | arg |$
                    arg_key, arg_val = arg.split([33m/[39;49;00m[33m=[39;49;00m[33m/[39;49;00m, [34m2[39;49;00m)$
                    arg_key = [31mRweb[39;49;00m::unescape(arg_key)$
                    arg_val = [31mRweb[39;49;00m::unescape(arg_val)$
$
                    [37m# Parse names like name[0], name['text'] or name[][39;49;00m$
                    pattern = [33m/[39;49;00m[33m^(.+)[39;49;00m[33m\[39;49;00m[33m[("[^[39;49;00m[33m\[39;49;00m[33m]]*"|'[^[39;49;00m[33m\[39;49;00m[33m]]*'|[0-9]*)[39;49;00m[33m\[39;49;00m[33m]$[39;49;00m[33m/[39;49;00m$
                    keys = []$
                    [34mwhile[39;49;00m match = pattern.match(arg_key)$
                        arg_key = match[[34m1[39;49;00m]$
                        keys = [match[[34m2[39;49;00m]] + keys$
                    [34mend[39;49;00m$
                    keys = [arg_key] + keys$
$
                    akt = [31m@post[39;49;00m$
                    last = [34mnil[39;49;00m$
                    lastkey = [34mnil[39;49;00m$
                    keys.each [34mdo[39;49;00m |key|$
                        [34mif[39;49;00m key == [33m"[39;49;00m[33m"[39;49;00m$
                            [37m# No key specified (like in "test[]"), so we use[39;49;00m$
                            [37m# the lowerst unused Integer as key[39;49;00m$
                            key = [34m0[39;49;00m$
                            [34mwhile[39;49;00m akt.has_key?(key)$
                                key += [34m1[39;49;00m$
                            [34mend[39;49;00m$
                        [34melsif[39;49;00m [33m/[39;49;00m[33m^[0-9]*$[39;49;00m[33m/[39;49;00m =~ key$
                            [37m# If the index is numerical convert it to an Integer[39;49;00m$
                            key = key.to_i$
                        [34melsif[39;49;00m key[[34m0[39;49;00m].chr == [33m"[39;49;00m[33m'[39;49;00m[33m"[39;49;00m || key[[34m0[39;49;00m].chr == [33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m$
                            key = key[[34m1[39;49;00m, key.length() -[34m2[39;49;00m]$
                        [34mend[39;49;00m$
                        [34mif[39;49;00m !akt.has_key?(key) || !akt[key].class == [31mHash[39;49;00m$
                            [37m# create an empty Hash if there isn't already one[39;49;00m$
                            akt[key] = {}$
                        [34mend[39;49;00m$
                        last = akt$
                        lastkey = key$
                        akt = akt[key]$
                    [34mend[39;49;00m$
                    last[lastkey] = arg_val$
                [34mend[39;49;00m$
            [34melse[39;49;00m$
                [37m# Maybe we should print a warning here?[39;49;00m$
                [31m$stderr[39;49;00m.print([33m"[39;49;00m[33mUnidentified form data recived and discarded.[39;49;00m[33m"[39;49;00m)$
            [34mend[39;49;00m$
        [34mend[39;49;00m$
$
        [34mif[39;49;00m [31m@env[39;49;00m.has_key?([33m"[39;49;00m[33mHTTP_COOKIE[39;49;00m[33m"[39;49;00m)$
            cookie = [31m@env[39;49;00m[[33m'[39;49;00m[33mHTTP_COOKIE[39;49;00m[33m'[39;49;00m].split([33m/[39;49;00m[33m; ?[39;49;00m[33m/[39;49;00m)$
            cookie.each [34mdo[39;49;00m | c |$
                cookie_key, cookie_val = c.split([33m/[39;49;00m[33m=[39;49;00m[33m/[39;49;00m, [34m2[39;49;00m)$
$
                [31m@cookies[39;49;00m [[31mRweb[39;49;00m::unescape(cookie_key)] = [31mRweb[39;49;00m::unescape(cookie_val)$
            [34mend[39;49;00m$
        [34mend[39;49;00m$
$
        [34mif[39;49;00m defined?([31m@env[39;49;00m[[33m'[39;49;00m[33mHTTP_USER_AGENT[39;49;00m[33m'[39;49;00m])$
            [31m@user_agent[39;49;00m = [31m@env[39;49;00m[[33m'[39;49;00m[33mHTTP_USER_AGENT[39;49;00m[33m'[39;49;00m]$
        [34melse[39;49;00m$
            [31m@user_agent[39;49;00m = [34mnil[39;49;00m;$
        [34mend[39;49;00m$
$
        [34mif[39;49;00m defined?([31m@env[39;49;00m[[33m'[39;49;00m[33mREMOTE_ADDR[39;49;00m[33m'[39;49;00m])$
            [31m@remote_addr[39;49;00m = [31m@env[39;49;00m[[33m'[39;49;00m[33mREMOTE_ADDR[39;49;00m[33m'[39;49;00m]$
        [34melse[39;49;00m$
            [31m@remote_addr[39;49;00m = [34mnil[39;49;00m$
        [34mend[39;49;00m$
        [37m# }}}[39;49;00m$
    [34mend[39;49;00m$
$
    [37m# Prints a String to the client. If caching is enabled, the String will[39;49;00m$
    [37m# buffered until the end of the out block ends.[39;49;00m$
    [34mdef[39;49;00m [32mprint[39;49;00m(str = [33m"[39;49;00m[33m"[39;49;00m)$
        [37m# {{{[39;49;00m$
        [34munless[39;49;00m [31m@output_allowed[39;49;00m$
            [34mraise[39;49;00m [33m"[39;49;00m[33mYou just can write to output inside of a Rweb::out-block[39;49;00m[33m"[39;49;00m$
        [34mend[39;49;00m$
$
        [34mif[39;49;00m [31m@settings[39;49;00m[[33m"[39;49;00m[33mcache[39;49;00m[33m"[39;49;00m]$
            [31m@buffer[39;49;00m += [str.to_s]$
        [34melse[39;49;00m$
            [34munless[39;49;00m [31m@output_started[39;49;00m$
                sendHeaders$
            [34mend[39;49;00m$
            [31m$stdout[39;49;00m.print(str)$
        [34mend[39;49;00m$
        [34mnil[39;49;00m$
        [37m# }}}[39;49;00m$
    [34mend[39;49;00m$
$
    [37m# Prints a String to the client and adds a line break at the end. Please[39;49;00m$
		[37m# remember, that a line break is not visible in HTML, use the <br> HTML-Tag[39;49;00m$
		[37m# for this. If caching is enabled, the String will buffered until the end[39;49;00m$
		[37m# of the out block ends.[39;49;00m$
    [34mdef[39;49;00m [32mputs[39;49;00m(str = [33m"[39;49;00m[33m"[39;49;00m)$
        [37m# {{{[39;49;00m$
        [36mself[39;49;00m.print(str + [33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m)$
        [37m# }}}[39;49;00m$
    [34mend[39;49;00m$
$
		[37m# Alias to print.[39;49;00m$
    [34mdef[39;49;00m [32mwrite[39;49;00m(str = [33m"[39;49;00m[33m"[39;49;00m)$
        [37m# {{{[39;49;00m$
        [36mself[39;49;00m.print(str)$
        [37m# }}}[39;49;00m$
    [34mend[39;49;00m$
$
    [37m# If caching is enabled, all cached data are send to the cliend and the[39;49;00m$
		[37m# cache emptied.[39;49;00m$
    [34mdef[39;49;00m [32mflush[39;49;00m$
        [37m# {{{[39;49;00m$
        [34munless[39;49;00m [31m@output_allowed[39;49;00m$
            [34mraise[39;49;00m [33m"[39;49;00m[33mYou can't use flush outside of a Rweb::out-block[39;49;00m[33m"[39;49;00m$
        [34mend[39;49;00m$
        buffer = [31m@buffer[39;49;00m.join$
$
        [34munless[39;49;00m [31m@output_started[39;49;00m$
            sendHeaders$
        [34mend[39;49;00m$
        [31m$stdout[39;49;00m.print(buffer)$
$
        [31m@buffer[39;49;00m = []$
        [37m# }}}[39;49;00m$
    [34mend[39;49;00m$
$
    [37m# Sends one or more header to the client. All headers are cached just[39;49;00m$
		[37m# before body data are send to the client. If the same header are set[39;49;00m$
		[37m# twice, only the last value is send.[39;49;00m$
		[37m#[39;49;00m$
		[37m# Example:[39;49;00m$
		[37m#  web.header("Last-Modified: Mon, 16 Feb 2004 20:15:41 GMT")[39;49;00m$
		[37m#  web.header("Location: http://www.ruby-lang.org")[39;49;00m$
		[37m#[39;49;00m$
		[37m# You can specify more than one header at the time by doing something like[39;49;00m$
		[37m# this:[39;49;00m$
		[37m#  web.header("Content-Type: text/plain\nContent-Length: 383")[39;49;00m$
		[37m# or[39;49;00m$
		[37m#  web.header(["Content-Type: text/plain", "Content-Length: 383"])[39;49;00m$
    [34mdef[39;49;00m [32mheader[39;49;00m(str)$
        [37m# {{{[39;49;00m$
        [34mif[39;49;00m [31m@output_started[39;49;00m$
            [34mraise[39;49;00m [33m"[39;49;00m[33mHTTP-Headers are already send. You can't change them after output has started![39;49;00m[33m"[39;49;00m$
        [34mend[39;49;00m$
        [34munless[39;49;00m [31m@output_allowed[39;49;00m$
            [34mraise[39;49;00m [33m"[39;49;00m[33mYou just can set headers inside of a Rweb::out-block[39;49;00m[33m"[39;49;00m$
        [34mend[39;49;00m$
        [34mif[39;49;00m str.is_a?[36mArray[39;49;00m$
            str.each [34mdo[39;49;00m | value |$
                [36mself[39;49;00m.header(value)$
            [34mend[39;49;00m$
$
        [34melsif[39;49;00m str.split([33m/[39;49;00m[33m\[39;49;00m[33mn[39;49;00m[33m/[39;49;00m).length > [34m1[39;49;00m$
            str.split([33m/[39;49;00m[33m\[39;49;00m[33mn[39;49;00m[33m/[39;49;00m).each [34mdo[39;49;00m | value |$
                [36mself[39;49;00m.header(value)$
            [34mend[39;49;00m$
$
        [34melsif[39;49;00m str.is_a? [36mString[39;49;00m$
            str.gsub!([33m/[39;49;00m[33m\[39;49;00m[33mr[39;49;00m[33m/[39;49;00m, [33m"[39;49;00m[33m"[39;49;00m)$
$
            [34mif[39;49;00m (str =~ [33m/[39;49;00m[33m^HTTP[39;49;00m[33m\/[39;49;00m[33m1[39;49;00m[33m\[39;49;00m[33m.[01] [0-9]{3} ?.*$[39;49;00m[33m/[39;49;00m) == [34m0[39;49;00m$
                pattern = [33m/[39;49;00m[33m^HTTP[39;49;00m[33m\/[39;49;00m[33m1.[01] ([0-9]{3}) ?(.*)$[39;49;00m[33m/[39;49;00m$
$
                result = pattern.match(str)$
                [36mself[39;49;00m.setstatus(result[[34m0[39;49;00m], result[[34m1[39;49;00m])$
            [34melsif[39;49;00m (str =~ [33m/[39;49;00m[33m^status: [0-9]{3} ?.*$[39;49;00m[33m/i[39;49;00m) == [34m0[39;49;00m$
                pattern = [33m/[39;49;00m[33m^status: ([0-9]{3}) ?(.*)$[39;49;00m[33m/i[39;49;00m$
$
                result = pattern.match(str)$
                [36mself[39;49;00m.setstatus(result[[34m0[39;49;00m], result[[34m1[39;49;00m])$
            [34melse[39;49;00m$
                a = str.split([33m/[39;49;00m[33m: ?[39;49;00m[33m/[39;49;00m, [34m2[39;49;00m)$
$
                [31m@header[39;49;00m[a[[34m0[39;49;00m].downcase] = a[[34m1[39;49;00m]$
            [34mend[39;49;00m$
        [34mend[39;49;00m$
        [37m# }}}[39;49;00m$
    [34mend[39;49;00m$
$
    [37m# Changes the status of this page. There are several codes like "200 OK",[39;49;00m$
		[37m# "302 Found", "404 Not Found" or "500 Internal Server Error". A list of[39;49;00m$
		[37m# all codes is available at[39;49;00m$
		[37m# http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10[39;49;00m$
		[37m#[39;49;00m$
		[37m# You can just send the code number, the reason phrase will be added[39;49;00m$
		[37m# automaticly with the recommendations from the w3c if not specified. If[39;49;00m$
		[37m# you set the status twice or more, only the last status will be send.[39;49;00m$
		[37m# Examples:[39;49;00m$
		[37m#  web.status("401 Unauthorized")[39;49;00m$
		[37m#  web.status("410 Sad but true, this lonely page is gone :(")[39;49;00m$
		[37m#  web.status(206)[39;49;00m$
		[37m#  web.status("400")[39;49;00m$
		[37m#[39;49;00m$
		[37m# The default status is "200 OK". If a "Location" header is set, the[39;49;00m$
		[37m# default status is "302 Found".[39;49;00m$
    [34mdef[39;49;00m [32mstatus[39;49;00m(str)$
        [37m# {{{[39;49;00m$
        [34mif[39;49;00m [31m@output_started[39;49;00m$
            [34mraise[39;49;00m [33m"[39;49;00m[33mHTTP-Headers are already send. You can't change them after output has started![39;49;00m[33m"[39;49;00m$
        [34mend[39;49;00m$
        [34munless[39;49;00m [31m@output_allowed[39;49;00m$
            [34mraise[39;49;00m [33m"[39;49;00m[33mYou just can set headers inside of a Rweb::out-block[39;49;00m[33m"[39;49;00m$
        [34mend[39;49;00m$
        [34mif[39;49;00m str.is_a?[36mInteger[39;49;00m$
            [31m@status[39;49;00m = str$
        [34melsif[39;49;00m str.is_a?[36mString[39;49;00m$
            p1 = [33m/[39;49;00m[33m^([0-9]{3}) ?(.*)$[39;49;00m[33m/[39;49;00m$
            p2 = [33m/[39;49;00m[33m^HTTP[39;49;00m[33m\/[39;49;00m[33m1[39;49;00m[33m\[39;49;00m[33m.[01] ([0-9]{3}) ?(.*)$[39;49;00m[33m/[39;49;00m$
            p3 = [33m/[39;49;00m[33m^status: ([0-9]{3}) ?(.*)$[39;49;00m[33m/i[39;49;00m$
$
            [34mif[39;49;00m (a = p1.match(str)) == [34mnil[39;49;00m$
                [34mif[39;49;00m (a = p2.match(str)) == [34mnil[39;49;00m$
                    [34mif[39;49;00m (a = p3.match(str)) == [34mnil[39;49;00m$
                        [34mraise[39;49;00m [31mArgumentError[39;49;00m, [33m"[39;49;00m[33mInvalid argument[39;49;00m[33m"[39;49;00m, [36mcaller[39;49;00m$
                    [34mend[39;49;00m$
                [34mend[39;49;00m$
            [34mend[39;49;00m$
            [31m@status[39;49;00m = a[[34m1[39;49;00m].to_i$
            [34mif[39;49;00m a[[34m2[39;49;00m] != [33m"[39;49;00m[33m"[39;49;00m$
                [31m@reasonPhrase[39;49;00m = a[[34m2[39;49;00m]$
            [34melse[39;49;00m$
                [31m@reasonPhrase[39;49;00m = getReasonPhrase([31m@status[39;49;00m)$
            [34mend[39;49;00m$
        [34melse[39;49;00m$
            [34mraise[39;49;00m [31mArgumentError[39;49;00m, [33m"[39;49;00m[33mArgument of setstatus must be integer or string[39;49;00m[33m"[39;49;00m, [36mcaller[39;49;00m$
        [34mend[39;49;00m$
        [37m# }}}[39;49;00m$
    [34mend[39;49;00m$
$
    [37m# Handles the output of your content and rescues all exceptions. Send all[39;49;00m$
		[37m# data in the block to this method. For example:[39;49;00m$
		[37m#  web.out do[39;49;00m$
		[37m#      web.header("Content-Type: text/plain")[39;49;00m$
		[37m#      web.puts("Hello, plain world!")[39;49;00m$
		[37m#  end[39;49;00m$
    [34mdef[39;49;00m [32mout[39;49;00m$
        [37m# {{{[39;49;00m$
        [31m@output_allowed[39;49;00m = [34mtrue[39;49;00m$
        [31m@buffer[39;49;00m = []; [37m# We use an array as buffer, because it's more performant :)[39;49;00m$
$
        [34mbegin[39;49;00m$
            [34myield[39;49;00m$
        [34mrescue[39;49;00m [31mException[39;49;00m => exception$
            [31m$stderr[39;49;00m.puts [33m"[39;49;00m[33mRuby exception rescued ([39;49;00m[33m#{[39;49;00mexception.class[33m}[39;49;00m[33m): [39;49;00m[33m#{[39;49;00mexception.message[33m}[39;49;00m[33m"[39;49;00m$
            [31m$stderr[39;49;00m.puts exception.backtrace.join([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m)$
$
            [34munless[39;49;00m [31m@output_started[39;49;00m$
                [36mself[39;49;00m.setstatus([34m500[39;49;00m)$
                [31m@header[39;49;00m = {}$
            [34mend[39;49;00m$
$
            [34munless[39;49;00m ([31m@settings[39;49;00m.has_key?([33m"[39;49;00m[33mhide errors[39;49;00m[33m"[39;49;00m) [35mand[39;49;00m [31m@settings[39;49;00m[[33m"[39;49;00m[33mhide errors[39;49;00m[33m"[39;49;00m] == [34mtrue[39;49;00m)$
                [34munless[39;49;00m [31m@output_started[39;49;00m$
                    [36mself[39;49;00m.header([33m"[39;49;00m[33mContent-Type: text/html[39;49;00m[33m"[39;49;00m)$
                    [36mself[39;49;00m.puts [33m"[39;49;00m[33m<!DOCTYPE HTML PUBLIC [39;49;00m[33m\"[39;49;00m[33m-//W3C//DTD HTML 4.01 Strict//EN[39;49;00m[33m\"[39;49;00m[33m [39;49;00m[33m\"[39;49;00m[33mhttp://www.w3.org/TR/html4/strict.dtd[39;49;00m[33m\"[39;49;00m[33m>[39;49;00m[33m"[39;49;00m$
                    [36mself[39;49;00m.puts [33m"[39;49;00m[33m<html>[39;49;00m[33m"[39;49;00m$
                    [36mself[39;49;00m.puts [33m"[39;49;00m[33m<head>[39;49;00m[33m"[39;49;00m$
                    [36mself[39;49;00m.puts [33m"[39;49;00m[33m<title>500 Internal Server Error</title>[39;49;00m[33m"[39;49;00m$
                    [36mself[39;49;00m.puts [33m"[39;49;00m[33m</head>[39;49;00m[33m"[39;49;00m$
                    [36mself[39;49;00m.puts [33m"[39;49;00m[33m<body>[39;49;00m[33m"[39;49;00m$
                [34mend[39;49;00m$
                [34mif[39;49;00m [31m@header[39;49;00m.has_key?([33m"[39;49;00m[33mcontent-type[39;49;00m[33m"[39;49;00m) [35mand[39;49;00m ([31m@header[39;49;00m[[33m"[39;49;00m[33mcontent-type[39;49;00m[33m"[39;49;00m] =~ [33m/[39;49;00m[33m^text[39;49;00m[33m\/[39;49;00m[33mhtml[39;49;00m[33m/i[39;49;00m) == [34m0[39;49;00m$
                    [36mself[39;49;00m.puts [33m"[39;49;00m[33m<h1>Internal Server Error</h1>[39;49;00m[33m"[39;49;00m$
                    [36mself[39;49;00m.puts [33m"[39;49;00m[33m<p>The server encountered an exception and was unable to complete your request.</p>[39;49;00m[33m"[39;49;00m$
                    [36mself[39;49;00m.puts [33m"[39;49;00m[33m<p>The exception has provided the following information:</p>[39;49;00m[33m"[39;49;00m$
                    [36mself[39;49;00m.puts [33m"[39;49;00m[33m<pre style=[39;49;00m[33m\"[39;49;00m[33mbackground: [39;49;00m[33m#[39;49;00m[33mFFCCCC; border: black solid 2px; margin-left: 2cm; margin-right: 2cm; padding: 2mm;[39;49;00m[33m\"[39;49;00m[33m><b>[39;49;00m[33m#{[39;49;00mexception.class[33m}[39;49;00m[33m</b>: [39;49;00m[33m#{[39;49;00mexception.message[33m}[39;49;00m[33m <b>on</b>[39;49;00m[33m"[39;49;00m$
                    [36mself[39;49;00m.puts$
                    [36mself[39;49;00m.puts [33m"[39;49;00m[33m#{[39;49;00mexception.backtrace.join([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m)[33m}[39;49;00m[33m</pre>[39;49;00m[33m"[39;49;00m$
                    [36mself[39;49;00m.puts [33m"[39;49;00m[33m</body>[39;49;00m[33m"[39;49;00m$
                    [36mself[39;49;00m.puts [33m"[39;49;00m[33m</html>[39;49;00m[33m"[39;49;00m$
                [34melse[39;49;00m$
                    [36mself[39;49;00m.puts [33m"[39;49;00m[33mThe server encountered an exception and was unable to complete your request[39;49;00m[33m"[39;49;00m$
                    [36mself[39;49;00m.puts [33m"[39;49;00m[33mThe exception has provided the following information:[39;49;00m[33m"[39;49;00m$
                    [36mself[39;49;00m.puts [33m"[39;49;00m[33m#{[39;49;00mexception.class[33m}[39;49;00m[33m: [39;49;00m[33m#{[39;49;00mexception.message[33m}[39;49;00m[33m"[39;49;00m$
                    [36mself[39;49;00m.puts$
                    [36mself[39;49;00m.puts exception.backtrace.join([33m"[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m)$
                [34mend[39;49;00m$
            [34mend[39;49;00m$
        [34mend[39;49;00m$
$
        [34mif[39;49;00m [31m@settings[39;49;00m[[33m"[39;49;00m[33mcache[39;49;00m[33m"[39;49;00m]$
            buffer = [31m@buffer[39;49;00m.join$
$
            [34munless[39;49;00m [31m@output_started[39;49;00m$
                [34munless[39;49;00m [31m@header[39;49;00m.has_key?([33m"[39;49;00m[33mcontent-length[39;49;00m[33m"[39;49;00m)$
                    [36mself[39;49;00m.header([33m"[39;49;00m[33mcontent-length: [39;49;00m[33m#{[39;49;00mbuffer.length[33m}[39;49;00m[33m"[39;49;00m)$
                [34mend[39;49;00m$
$
                sendHeaders$
            [34mend[39;49;00m$
            [31m$stdout[39;49;00m.print(buffer)$
        [34melsif[39;49;00m ![31m@output_started[39;49;00m$
            sendHeaders$
        [34mend[39;49;00m$
        [31m@output_allowed[39;49;00m = [34mfalse[39;49;00m;$
        [37m# }}}[39;49;00m$
    [34mend[39;49;00m$
$
    [37m# Decodes URL encoded data, %20 for example stands for a space.[39;49;00m$
    [34mdef[39;49;00m [04m[32mRweb[39;49;00m.[32munescape[39;49;00m(str)$
        [37m# {{{[39;49;00m$
        [34mif[39;49;00m defined? str [35mand[39;49;00m str.is_a? [36mString[39;49;00m$
            str.gsub!([33m/[39;49;00m[33m\[39;49;00m[33m+[39;49;00m[33m/[39;49;00m, [33m"[39;49;00m[33m [39;49;00m[33m"[39;49;00m)$
            str.gsub([33m/[39;49;00m[33m%.{2}[39;49;00m[33m/[39;49;00m) [34mdo[39;49;00m | s |$
                s[[34m1[39;49;00m,[34m2[39;49;00m].hex.chr$
            [34mend[39;49;00m$
        [34mend[39;49;00m$
        [37m# }}}[39;49;00m$
    [34mend[39;49;00m$
$
    [34mprotected[39;49;00m$
    [34mdef[39;49;00m [32msendHeaders[39;49;00m$
        [37m# {{{[39;49;00m$
$
        [31mCookie[39;49;00m.disallow [37m# no more cookies can be set or modified[39;49;00m$
        [34mif[39;49;00m !([31m@settings[39;49;00m.has_key?([33m"[39;49;00m[33msilent[39;49;00m[33m"[39;49;00m) [35mand[39;49;00m [31m@settings[39;49;00m[[33m"[39;49;00m[33msilent[39;49;00m[33m"[39;49;00m] == [34mtrue[39;49;00m) [35mand[39;49;00m ![31m@header[39;49;00m.has_key?([33m"[39;49;00m[33mx-powered-by[39;49;00m[33m"[39;49;00m)$
            [34mif[39;49;00m [31m@mod_ruby[39;49;00m$
                header([33m"[39;49;00m[33mx-powered-by: [39;49;00m[33m#{[39;49;00m[31mRWEB[39;49;00m[33m}[39;49;00m[33m (Ruby/[39;49;00m[33m#{[39;49;00m[31mRUBY_VERSION[39;49;00m[33m}[39;49;00m[33m, [39;49;00m[33m#{[39;49;00m[31mMOD_RUBY[39;49;00m[33m}[39;49;00m[33m)[39;49;00m[33m"[39;49;00m);$
            [34melse[39;49;00m$
                header([33m"[39;49;00m[33mx-powered-by: [39;49;00m[33m#{[39;49;00m[31mRWEB[39;49;00m[33m}[39;49;00m[33m (Ruby/[39;49;00m[33m#{[39;49;00m[31mRUBY_VERSION[39;49;00m[33m}[39;49;00m[33m)[39;49;00m[33m"[39;49;00m);$
            [34mend[39;49;00m$
        [34mend[39;49;00m$
$
        [34mif[39;49;00m [31m@output_method[39;49;00m == [33m"[39;49;00m[33mph[39;49;00m[33m"[39;49;00m$
            [34mif[39;49;00m (([31m@status[39;49;00m == [34mnil[39;49;00m [35mor[39;49;00m [31m@status[39;49;00m == [34m200[39;49;00m) [35mand[39;49;00m ![31m@header[39;49;00m.has_key?([33m"[39;49;00m[33mcontent-type[39;49;00m[33m"[39;49;00m) [35mand[39;49;00m ![31m@header[39;49;00m.has_key?([33m"[39;49;00m[33mlocation[39;49;00m[33m"[39;49;00m))$
                header([33m"[39;49;00m[33mcontent-type: text/html[39;49;00m[33m"[39;49;00m)$
            [34mend[39;49;00m$
$
            [34mif[39;49;00m [31m@status[39;49;00m != [34mnil[39;49;00m$
                [31m$stdout[39;49;00m.print [33m"[39;49;00m[33mStatus: [39;49;00m[33m#{[39;49;00m[31m@status[39;49;00m[33m}[39;49;00m[33m [39;49;00m[33m#{[39;49;00m[31m@reasonPhrase[39;49;00m[33m}[39;49;00m[33m\r[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
            [34mend[39;49;00m$
$
            [31m@header[39;49;00m.each [34mdo[39;49;00m |key, value|$
                key = key *[34m1[39;49;00m [37m# "unfreeze" key :)[39;49;00m$
                key[[34m0[39;49;00m] = key[[34m0[39;49;00m,[34m1[39;49;00m].upcase![[34m0[39;49;00m]$
$
                key = key.gsub([33m/[39;49;00m[33m-[a-z][39;49;00m[33m/[39;49;00m) [34mdo[39;49;00m |char|$
                    [33m"[39;49;00m[33m-[39;49;00m[33m"[39;49;00m + char[[34m1[39;49;00m,[34m1[39;49;00m].upcase$
                [34mend[39;49;00m$
$
                [31m$stdout[39;49;00m.print [33m"[39;49;00m[33m#{[39;49;00mkey[33m}[39;49;00m[33m: [39;49;00m[33m#{[39;49;00mvalue[33m}[39;49;00m[33m\r[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
            [34mend[39;49;00m$
            cookies = [31mCookie[39;49;00m.getHttpHeader [37m# Get all cookies as an HTTP Header[39;49;00m$
            [34mif[39;49;00m cookies$
                [31m$stdout[39;49;00m.print cookies$
            [34mend[39;49;00m$
$
            [31m$stdout[39;49;00m.print [33m"[39;49;00m[33m\r[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
$
        [34melsif[39;49;00m [31m@output_method[39;49;00m == [33m"[39;49;00m[33mnph[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m [31m@output_method[39;49;00m == [33m"[39;49;00m[33mmod_ruby[39;49;00m[33m"[39;49;00m$
            r = [31mApache[39;49;00m.request$
$
            [34mif[39;49;00m (([31m@status[39;49;00m == [34mnil[39;49;00m [35mor[39;49;00m [31m@status[39;49;00m == [34m200[39;49;00m) [35mand[39;49;00m ![31m@header[39;49;00m.has_key?([33m"[39;49;00m[33mcontent-type[39;49;00m[33m"[39;49;00m) [35mand[39;49;00m ![31m@header[39;49;00m.has_key?([33m"[39;49;00m[33mlocation[39;49;00m[33m"[39;49;00m))$
                header([33m"[39;49;00m[33mtext/html[39;49;00m[33m"[39;49;00m)$
            [34mend[39;49;00m$
$
            [34mif[39;49;00m [31m@status[39;49;00m != [34mnil[39;49;00m$
                r.status_line = [33m"[39;49;00m[33m#{[39;49;00m[31m@status[39;49;00m[33m}[39;49;00m[33m [39;49;00m[33m#{[39;49;00m[31m@reasonPhrase[39;49;00m[33m}[39;49;00m[33m"[39;49;00m$
            [34mend[39;49;00m$
$
            r.send_http_header$
            [31m@header[39;49;00m.each [34mdo[39;49;00m |key, value|$
                key = key *[34m1[39;49;00m [37m# "unfreeze" key :)[39;49;00m$
$
                key[[34m0[39;49;00m] = key[[34m0[39;49;00m,[34m1[39;49;00m].upcase![[34m0[39;49;00m]$
                key = key.gsub([33m/[39;49;00m[33m-[a-z][39;49;00m[33m/[39;49;00m) [34mdo[39;49;00m |char|$
                    [33m"[39;49;00m[33m-[39;49;00m[33m"[39;49;00m + char[[34m1[39;49;00m,[34m1[39;49;00m].upcase$
                [34mend[39;49;00m$
                [36mputs[39;49;00m [33m"[39;49;00m[33m#{[39;49;00mkey[33m}[39;49;00m[33m: [39;49;00m[33m#{[39;49;00mvalue.class[33m}[39;49;00m[33m"[39;49;00m$
                [37m#r.headers_out[key] = value[39;49;00m$
            [34mend[39;49;00m$
        [34mend[39;49;00m$
        [31m@output_started[39;49;00m = [34mtrue[39;49;00m$
        [37m# }}}[39;49;00m$
    [34mend[39;49;00m$
$
    [34mdef[39;49;00m [32mgetReasonPhrase[39;49;00m (status)$
        [37m# {{{[39;49;00m$
        [34mif[39;49;00m status == [34m100[39;49;00m$
            [33m"[39;49;00m[33mContinue[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m101[39;49;00m$
            [33m"[39;49;00m[33mSwitching Protocols[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m200[39;49;00m$
            [33m"[39;49;00m[33mOK[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m201[39;49;00m$
            [33m"[39;49;00m[33mCreated[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m202[39;49;00m$
            [33m"[39;49;00m[33mAccepted[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m203[39;49;00m$
            [33m"[39;49;00m[33mNon-Authoritative Information[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m204[39;49;00m$
            [33m"[39;49;00m[33mNo Content[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m205[39;49;00m$
            [33m"[39;49;00m[33mReset Content[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m206[39;49;00m$
            [33m"[39;49;00m[33mPartial Content[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m300[39;49;00m$
            [33m"[39;49;00m[33mMultiple Choices[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m301[39;49;00m$
            [33m"[39;49;00m[33mMoved Permanently[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m302[39;49;00m$
            [33m"[39;49;00m[33mFound[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m303[39;49;00m$
            [33m"[39;49;00m[33mSee Other[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m304[39;49;00m$
            [33m"[39;49;00m[33mNot Modified[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m305[39;49;00m$
            [33m"[39;49;00m[33mUse Proxy[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m307[39;49;00m$
            [33m"[39;49;00m[33mTemporary Redirect[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m400[39;49;00m$
            [33m"[39;49;00m[33mBad Request[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m401[39;49;00m$
            [33m"[39;49;00m[33mUnauthorized[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m402[39;49;00m$
            [33m"[39;49;00m[33mPayment Required[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m403[39;49;00m$
            [33m"[39;49;00m[33mForbidden[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m404[39;49;00m$
            [33m"[39;49;00m[33mNot Found[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m405[39;49;00m$
            [33m"[39;49;00m[33mMethod Not Allowed[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m406[39;49;00m$
            [33m"[39;49;00m[33mNot Acceptable[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m407[39;49;00m$
            [33m"[39;49;00m[33mProxy Authentication Required[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m408[39;49;00m$
            [33m"[39;49;00m[33mRequest Time-out[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m409[39;49;00m$
            [33m"[39;49;00m[33mConflict[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m410[39;49;00m$
            [33m"[39;49;00m[33mGone[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m411[39;49;00m$
            [33m"[39;49;00m[33mLength Required[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m412[39;49;00m$
            [33m"[39;49;00m[33mPrecondition Failed[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m413[39;49;00m$
            [33m"[39;49;00m[33mRequest Entity Too Large[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m414[39;49;00m$
            [33m"[39;49;00m[33mRequest-URI Too Large[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m415[39;49;00m$
            [33m"[39;49;00m[33mUnsupported Media Type[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m416[39;49;00m$
            [33m"[39;49;00m[33mRequested range not satisfiable[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m417[39;49;00m$
            [33m"[39;49;00m[33mExpectation Failed[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m500[39;49;00m$
            [33m"[39;49;00m[33mInternal Server Error[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m501[39;49;00m$
            [33m"[39;49;00m[33mNot Implemented[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m502[39;49;00m$
            [33m"[39;49;00m[33mBad Gateway[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m503[39;49;00m$
            [33m"[39;49;00m[33mService Unavailable[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m504[39;49;00m$
            [33m"[39;49;00m[33mGateway Time-out[39;49;00m[33m"[39;49;00m$
        [34melsif[39;49;00m status == [34m505[39;49;00m$
            [33m"[39;49;00m[33mHTTP Version not supported[39;49;00m[33m"[39;49;00m$
        [34melse[39;49;00m$
            [34mraise[39;49;00m [33m"[39;49;00m[33mUnknown Statuscode. See http://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html[39;49;00m[33m#[39;49;00m[33msec6.1 for more information.[39;49;00m[33m"[39;49;00m$
        [34mend[39;49;00m$
        [37m# }}}[39;49;00m$
    [34mend[39;49;00m$
[34mend[39;49;00m$
$
[34mclass[39;49;00m [04m[32mCookie[39;49;00m$
	[34mattr_reader[39;49;00m [33m:name[39;49;00m, [33m:value[39;49;00m, [33m:maxage[39;49;00m, [33m:path[39;49;00m, [33m:domain[39;49;00m, [33m:secure[39;49;00m, [33m:comment[39;49;00m$
$
	[37m# Sets a cookie. Please see below for details of the attributes.[39;49;00m$
	[34mdef[39;49;00m [32minitialize[39;49;00m ([36mname[39;49;00m, value = [34mnil[39;49;00m, maxage = [34mnil[39;49;00m, path = [34mnil[39;49;00m, domain = [34mnil[39;49;00m, secure = [34mfalse[39;49;00m)$
		[37m# {{{[39;49;00m$
		[37m# HTTP headers (Cookies are a HTTP header) can only set, while no content[39;49;00m$
		[37m# is send. So an exception will be raised, when @@allowed is set to false[39;49;00m$
		[37m# and a new cookie has set.[39;49;00m$
		[34munless[39;49;00m defined?([31m@@allowed[39;49;00m)$
			[31m@@allowed[39;49;00m = [34mtrue[39;49;00m$
		[34mend[39;49;00m$
		[34munless[39;49;00m [31m@@allowed[39;49;00m$
			[34mraise[39;49;00m [33m"[39;49;00m[33mYou can't set cookies after the HTTP headers are send.[39;49;00m[33m"[39;49;00m$
		[34mend[39;49;00m$
$
		[34munless[39;49;00m defined?([31m@@list[39;49;00m)$
			[31m@@list[39;49;00m = []$
		[34mend[39;49;00m$
		[31m@@list[39;49;00m += [[36mself[39;49;00m]$
$
		[34munless[39;49;00m defined?([31m@@type[39;49;00m)$
			[31m@@type[39;49;00m = [33m"[39;49;00m[33mnetscape[39;49;00m[33m"[39;49;00m$
		[34mend[39;49;00m$
$
		[34munless[39;49;00m [36mname[39;49;00m.class == [36mString[39;49;00m$
			[34mraise[39;49;00m [31mTypeError[39;49;00m, [33m"[39;49;00m[33mThe name of a cookie must be a string[39;49;00m[33m"[39;49;00m, [36mcaller[39;49;00m$
		[34mend[39;49;00m$
		[34mif[39;49;00m value.class.superclass == [36mInteger[39;49;00m || value.class == [36mFloat[39;49;00m$
			value = value.to_s$
		[34melsif[39;49;00m value.class != [36mString[39;49;00m && value != [34mnil[39;49;00m$
			[34mraise[39;49;00m [31mTypeError[39;49;00m, [33m"[39;49;00m[33mThe value of a cookie must be a string, integer, float or nil[39;49;00m[33m"[39;49;00m, [36mcaller[39;49;00m$
		[34mend[39;49;00m$
		[34mif[39;49;00m maxage.class == [31mTime[39;49;00m$
			maxage = maxage - [31mTime[39;49;00m.now$
		[34melsif[39;49;00m !maxage.class.superclass == [36mInteger[39;49;00m  || !maxage == [34mnil[39;49;00m$
			[34mraise[39;49;00m [31mTypeError[39;49;00m, [33m"[39;49;00m[33mThe maxage date of a cookie must be an Integer or Time object or nil.[39;49;00m[33m"[39;49;00m, [36mcaller[39;49;00m$
		[34mend[39;49;00m$
		[34munless[39;49;00m path.class == [36mString[39;49;00m  || path == [34mnil[39;49;00m$
			[34mraise[39;49;00m [31mTypeError[39;49;00m, [33m"[39;49;00m[33mThe path of a cookie must be nil or a string[39;49;00m[33m"[39;49;00m, [36mcaller[39;49;00m$
		[34mend[39;49;00m$
		[34munless[39;49;00m domain.class == [36mString[39;49;00m  || domain == [34mnil[39;49;00m$
			[34mraise[39;49;00m [31mTypeError[39;49;00m, [33m"[39;49;00m[33mThe value of a cookie must be nil or a string[39;49;00m[33m"[39;49;00m, [36mcaller[39;49;00m$
		[34mend[39;49;00m$
		[34munless[39;49;00m secure == [34mtrue[39;49;00m  || secure == [34mfalse[39;49;00m$
			[34mraise[39;49;00m [31mTypeError[39;49;00m, [33m"[39;49;00m[33mThe secure field of a cookie must be true or false[39;49;00m[33m"[39;49;00m, [36mcaller[39;49;00m$
		[34mend[39;49;00m$
$
		[31m@name[39;49;00m, [31m@value[39;49;00m, [31m@maxage[39;49;00m, [31m@path[39;49;00m, [31m@domain[39;49;00m, [31m@secure[39;49;00m = [36mname[39;49;00m, value, maxage, path, domain, secure$
		[31m@comment[39;49;00m = [34mnil[39;49;00m$
		[37m# }}}[39;49;00m$
	[34mend[39;49;00m$
$
	[37m# Modifies the value of this cookie. The information you want to store. If the[39;49;00m$
	[37m# value is nil, the cookie will be deleted by the client.[39;49;00m$
	[37m#[39;49;00m$
	[37m# This attribute can be a String, Integer or Float object or nil.[39;49;00m$
	[34mdef[39;49;00m [32mvalue=[39;49;00m(value)$
		[37m# {{{[39;49;00m$
		[34mif[39;49;00m value.class.superclass == [36mInteger[39;49;00m || value.class == [36mFloat[39;49;00m$
			value = value.to_s$
		[34melsif[39;49;00m value.class != [36mString[39;49;00m && value != [34mnil[39;49;00m$
			[34mraise[39;49;00m [31mTypeError[39;49;00m, [33m"[39;49;00m[33mThe value of a cookie must be a string, integer, float or nil[39;49;00m[33m"[39;49;00m, [36mcaller[39;49;00m$
		[34mend[39;49;00m$
		[31m@value[39;49;00m = value$
		[37m# }}}[39;49;00m$
	[34mend[39;49;00m$
$
	[37m# Modifies the maxage of this cookie. This attribute defines the lifetime of[39;49;00m$
	[37m# the cookie, in seconds. A value of 0 means the cookie should be discarded[39;49;00m$
	[37m# imediatly. If it set to nil, the cookie will be deleted when the browser[39;49;00m$
	[37m# will be closed.[39;49;00m$
	[37m#[39;49;00m$
	[37m# Attention: This is different from other implementations like PHP, where you[39;49;00m$
	[37m# gives the seconds since 1/1/1970 0:00:00 GMT.[39;49;00m$
	[37m#[39;49;00m$
	[37m# This attribute must be an Integer or Time object or nil.[39;49;00m$
	[34mdef[39;49;00m [32mmaxage=[39;49;00m(maxage)$
		[37m# {{{[39;49;00m$
		[34mif[39;49;00m maxage.class == [31mTime[39;49;00m$
			maxage = maxage - [31mTime[39;49;00m.now$
		[34melsif[39;49;00m maxage.class.superclass == [36mInteger[39;49;00m  || !maxage == [34mnil[39;49;00m$
			[34mraise[39;49;00m [31mTypeError[39;49;00m, [33m"[39;49;00m[33mThe maxage of a cookie must be an Interger or Time object or nil.[39;49;00m[33m"[39;49;00m, [36mcaller[39;49;00m$
		[34mend[39;49;00m$
		[31m@maxage[39;49;00m = maxage$
		[37m# }}}[39;49;00m$
	[34mend[39;49;00m$
$
	[37m# Modifies the path value of this cookie. The client will send this cookie[39;49;00m$
	[37m# only, if the requested document is this directory or a subdirectory of it.[39;49;00m$
	[37m#[39;49;00m$
	[37m# The value of the attribute must be a String object or nil.[39;49;00m$
	[34mdef[39;49;00m [32mpath=[39;49;00m(path)$
		[37m# {{{[39;49;00m$
		[34munless[39;49;00m path.class == [36mString[39;49;00m  || path == [34mnil[39;49;00m$
			[34mraise[39;49;00m [31mTypeError[39;49;00m, [33m"[39;49;00m[33mThe path of a cookie must be nil or a string[39;49;00m[33m"[39;49;00m, [36mcaller[39;49;00m$
		[34mend[39;49;00m$
		[31m@path[39;49;00m = path$
		[37m# }}}[39;49;00m$
	[34mend[39;49;00m$
$
	[37m# Modifies the domain value of this cookie. The client will send this cookie[39;49;00m$
	[37m# only if it's connected with this domain (or a subdomain, if the first[39;49;00m$
	[37m# character is a dot like in ".ruby-lang.org")[39;49;00m$
	[37m#[39;49;00m$
	[37m# The value of this attribute must be a String or nil.[39;49;00m$
	[34mdef[39;49;00m [32mdomain=[39;49;00m(domain)$
		[37m# {{{[39;49;00m$
		[34munless[39;49;00m domain.class == [36mString[39;49;00m  || domain == [34mnil[39;49;00m$
			[34mraise[39;49;00m [31mTypeError[39;49;00m, [33m"[39;49;00m[33mThe domain of a cookie must be a String or nil.[39;49;00m[33m"[39;49;00m, [36mcaller[39;49;00m$
		[34mend[39;49;00m$
		[31m@domain[39;49;00m = domain$
		[37m# }}}[39;49;00m$
	[34mend[39;49;00m$
$
	[37m# Modifies the secure flag of this cookie. If it's true, the client will only[39;49;00m$
	[37m# send this cookie if it is secured connected with us.[39;49;00m$
	[37m#[39;49;00m$
	[37m# The value od this attribute has to be true or false.[39;49;00m$
	[34mdef[39;49;00m [32msecure=[39;49;00m(secure)$
		[37m# {{{[39;49;00m$
		[34munless[39;49;00m secure == [34mtrue[39;49;00m  || secure == [34mfalse[39;49;00m$
			[34mraise[39;49;00m [31mTypeError[39;49;00m, [33m"[39;49;00m[33mThe secure field of a cookie must be true or false[39;49;00m[33m"[39;49;00m, [36mcaller[39;49;00m$
		[34mend[39;49;00m$
		[31m@secure[39;49;00m = secure$
		[37m# }}}[39;49;00m$
	[34mend[39;49;00m$
$
	[37m# Modifies the comment value of this cookie. The comment won't be send, if[39;49;00m$
	[37m# type is "netscape".[39;49;00m$
	[34mdef[39;49;00m [32mcomment=[39;49;00m(comment)$
		[37m# {{{[39;49;00m$
		[34munless[39;49;00m comment.class == [36mString[39;49;00m || comment == [34mnil[39;49;00m$
			[34mraise[39;49;00m [31mTypeError[39;49;00m, [33m"[39;49;00m[33mThe comment of a cookie must be a string or nil[39;49;00m[33m"[39;49;00m, [36mcaller[39;49;00m$
		[34mend[39;49;00m$
		[31m@comment[39;49;00m = comment$
		[37m# }}}[39;49;00m$
	[34mend[39;49;00m$
$
	[37m# Changes the type of all cookies.[39;49;00m$
	[37m# Allowed values are RFC2109 and netscape (default).[39;49;00m$
	[34mdef[39;49;00m [04m[32mCookie[39;49;00m.[32mtype=[39;49;00m(type)$
		[37m# {{{[39;49;00m$
		[34munless[39;49;00m [31m@@allowed[39;49;00m$
			[34mraise[39;49;00m [33m"[39;49;00m[33mThe cookies are allready send, so you can't change the type anymore.[39;49;00m[33m"[39;49;00m$
		[34mend[39;49;00m$
		[34munless[39;49;00m type.downcase == [33m"[39;49;00m[33mrfc2109[39;49;00m[33m"[39;49;00m && type.downcase == [33m"[39;49;00m[33mnetscape[39;49;00m[33m"[39;49;00m$
			[34mraise[39;49;00m [33m"[39;49;00m[33mThe type of the cookies must be [39;49;00m[33m\"[39;49;00m[33mRFC2109[39;49;00m[33m\"[39;49;00m[33m or [39;49;00m[33m\"[39;49;00m[33mnetscape[39;49;00m[33m\"[39;49;00m[33m.[39;49;00m[33m"[39;49;00m$
		[34mend[39;49;00m$
		[31m@@type[39;49;00m = type;$
		[37m# }}}[39;49;00m$
	[34mend[39;49;00m$
$
	[37m# After sending this message, no cookies can be set or modified. Use it, when[39;49;00m$
	[37m# HTTP-Headers are send. Rweb does this for you.[39;49;00m$
	[34mdef[39;49;00m [04m[32mCookie[39;49;00m.[32mdisallow[39;49;00m$
		[37m# {{{[39;49;00m$
		[31m@@allowed[39;49;00m = [34mfalse[39;49;00m$
		[34mtrue[39;49;00m$
		[37m# }}}[39;49;00m$
	[34mend[39;49;00m$
$
	[37m# Returns a HTTP header (type String) with all cookies. Rweb does this for[39;49;00m$
	[37m# you.[39;49;00m$
	[34mdef[39;49;00m [04m[32mCookie[39;49;00m.[32mgetHttpHeader[39;49;00m$
		[37m# {{{[39;49;00m$
		[34mif[39;49;00m defined?([31m@@list[39;49;00m)$
			[34mif[39;49;00m [31m@@type[39;49;00m == [33m"[39;49;00m[33mnetscape[39;49;00m[33m"[39;49;00m$
				str = [33m"[39;49;00m[33m"[39;49;00m$
				[31m@@list[39;49;00m.each [34mdo[39;49;00m |cookie|$
					[34mif[39;49;00m cookie.value == [34mnil[39;49;00m$
						cookie.maxage = [34m0[39;49;00m$
						cookie.value = [33m"[39;49;00m[33m"[39;49;00m$
					[34mend[39;49;00m$
					[37m# TODO: Name and value should be escaped![39;49;00m$
					str += [33m"[39;49;00m[33mSet-Cookie: [39;49;00m[33m#{[39;49;00mcookie.name[33m}[39;49;00m[33m=[39;49;00m[33m#{[39;49;00mcookie.value[33m}[39;49;00m[33m"[39;49;00m$
					[34munless[39;49;00m cookie.maxage == [34mnil[39;49;00m$
						expire = [31mTime[39;49;00m.now + cookie.maxage$
						expire.gmtime$
						str += [33m"[39;49;00m[33m; Expire=[39;49;00m[33m#{[39;49;00mexpire.strftime([33m"[39;49;00m[33m%a, %d-%b-%Y %H:%M:%S %Z[39;49;00m[33m"[39;49;00m)[33m}[39;49;00m[33m"[39;49;00m$
					[34mend[39;49;00m$
					[34munless[39;49;00m cookie.domain == [34mnil[39;49;00m$
						str += [33m"[39;49;00m[33m; Domain=[39;49;00m[33m#{[39;49;00mcookie.domain[33m}[39;49;00m[33m"[39;49;00m$
					[34mend[39;49;00m$
					[34munless[39;49;00m cookie.path == [34mnil[39;49;00m$
						str += [33m"[39;49;00m[33m; Path=[39;49;00m[33m#{[39;49;00mcookie.path[33m}[39;49;00m[33m"[39;49;00m$
					[34mend[39;49;00m$
					[34mif[39;49;00m cookie.secure$
						str += [33m"[39;49;00m[33m; Secure[39;49;00m[33m"[39;49;00m$
					[34mend[39;49;00m$
					str += [33m"[39;49;00m[33m\r[39;49;00m[33m\n[39;49;00m[33m"[39;49;00m$
				[34mend[39;49;00m$
				[34mreturn[39;49;00m str$
			[34melse[39;49;00m [37m# type == "RFC2109"[39;49;00m$
				str = [33m"[39;49;00m[33mSet-Cookie: [39;49;00m[33m"[39;49;00m$
				comma = [34mfalse[39;49;00m;$
$
				[31m@@list[39;49;00m.each [34mdo[39;49;00m |cookie|$
					[34mif[39;49;00m cookie.value == [34mnil[39;49;00m$
						cookie.maxage = [34m0[39;49;00m$
						cookie.value = [33m"[39;49;00m[33m"[39;49;00m$
					[34mend[39;49;00m$
					[34mif[39;49;00m comma$
						str += [33m"[39;49;00m[33m,[39;49;00m[33m"[39;49;00m$
					[34mend[39;49;00m$
					comma = [34mtrue[39;49;00m$
$
					str += [33m"[39;49;00m[33m#{[39;49;00mcookie.name[33m}[39;49;00m[33m=[39;49;00m[33m\"[39;49;00m[33m#{[39;49;00mcookie.value[33m}[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m$
					[34munless[39;49;00m cookie.maxage == [34mnil[39;49;00m$
						str += [33m"[39;49;00m[33m; Max-Age=[39;49;00m[33m\"[39;49;00m[33m#{[39;49;00mcookie.maxage[33m}[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m$
					[34mend[39;49;00m$
					[34munless[39;49;00m cookie.domain == [34mnil[39;49;00m$
						str += [33m"[39;49;00m[33m; Domain=[39;49;00m[33m\"[39;49;00m[33m#{[39;49;00mcookie.domain[33m}[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m$
					[34mend[39;49;00m$
					[34munless[39;49;00m cookie.path == [34mnil[39;49;00m$
						str += [33m"[39;49;00m[33m; Path=[39;49;00m[33m\"[39;49;00m[33m#{[39;49;00mcookie.path[33m}[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m$
					[34mend[39;49;00m$
					[34mif[39;49;00m cookie.secure$
						str += [33m"[39;49;00m[33m; Secure[39;49;00m[33m"[39;49;00m$
					[34mend[39;49;00m$
					[34munless[39;49;00m cookie.comment == [34mnil[39;49;00m$
						str += [33m"[39;49;00m[33m; Comment=[39;49;00m[33m\"[39;49;00m[33m#{[39;49;00mcookie.comment[33m}[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m$
					[34mend[39;49;00m$
					str += [33m"[39;49;00m[33m; Version=[39;49;00m[33m\"[39;49;00m[33m1[39;49;00m[33m\"[39;49;00m[33m"[39;49;00m$
				[34mend[39;49;00m$
				str$
			[34mend[39;49;00m$
		[34melse[39;49;00m$
			[34mfalse[39;49;00m$
		[34mend[39;49;00m$
		[37m# }}}[39;49;00m$
	[34mend[39;49;00m$
[34mend[39;49;00m$
$
[36mrequire[39;49;00m [33m'[39;49;00m[33mstrscan[39;49;00m[33m'[39;49;00m$
$
[34mmodule[39;49;00m [04m[36mBBCode[39;49;00m$
	[31mDEBUG[39;49;00m = [34mtrue[39;49;00m$
$
	use [33m'[39;49;00m[33mencoder[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mtags[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33mtagstack[39;49;00m[33m'[39;49;00m, [33m'[39;49;00m[33msmileys[39;49;00m[33m'[39;49;00m$
$
[37m=begin[39;49;00m$
[37m	The Parser class takes care of the encoding.[39;49;00m$
[37m	It scans the given BBCode (as plain text), finds tags[39;49;00m$
[37m	and smilies and also makes links of urls in text.[39;49;00m$
[37m[39;49;00m$
[37m	Normal text is send directly to the encoder.[39;49;00m$
[37m[39;49;00m$
[37m	If a tag was found, an instance of a Tag subclass is created[39;49;00m$
[37m	to handle the case.[39;49;00m$
[37m[39;49;00m$
[37m	The @tagstack manages tag nesting and ensures valid HTML.[39;49;00m$
[37m=end[39;49;00m$
$
	[34mclass[39;49;00m [04m[32mParser[39;49;00m$
		[34mclass[39;49;00m [04m[32mAttribute[39;49;00m$
			[37m# flatten and use only one empty_arg[39;49;00m$
			[34mdef[39;49;00m [04m[32mself[39;49;00m.[32mcreate[39;49;00m [34mattr[39;49;00m$
				[34mattr[39;49;00m = flatten [34mattr[39;49;00m$
				[34mreturn[39;49;00m [31m@@empty_attr[39;49;00m [34mif[39;49;00m [34mattr[39;49;00m.empty?$
				[34mnew[39;49;00m [34mattr[39;49;00m$
			[34mend[39;49;00m$
$
			[36mprivate_class_method[39;49;00m [33m:new[39;49;00m$
$
			[37m# remove leading and trailing whitespace; concat lines[39;49;00m$
			[34mdef[39;49;00m [04m[32mself[39;49;00m.[32mflatten[39;49;00m [34mattr[39;49;00m$
				[34mattr[39;49;00m.strip.gsub([33m/[39;49;00m[33m\[39;49;00m[33mn[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m [39;49;00m[33m'[39;49;00m)$
				[37m# -> ^ and $ can only match at begin and end now[39;49;00m$
			[34mend[39;49;00m$
$
			[31mATTRIBUTE_SCAN[39;49;00m = [33m/[39;49;00m[33m[39;49;00m$
[33m				(?!$)  [39;49;00m[33m#[39;49;00m[33m don't match at end[39;49;00m$
[33m				[39;49;00m[33m\[39;49;00m[33ms*[39;49;00m$
[33m				( [39;49;00m[33m#[39;49;00m[33m $1 = key[39;49;00m$
[33m					[^=[39;49;00m[33m\[39;49;00m[33ms[39;49;00m[33m\[39;49;00m[33m]"[39;49;00m[33m\\[39;49;00m[33m]*[39;49;00m$
[33m					(?:[39;49;00m$
[33m						(?: [39;49;00m[33m\\[39;49;00m[33m. | "[^"[39;49;00m[33m\\[39;49;00m[33m]*(?:[39;49;00m[33m\\[39;49;00m[33m.[^"[39;49;00m[33m\\[39;49;00m[33m]*)*"? )[39;49;00m$
[33m						[^=[39;49;00m[33m\[39;49;00m[33ms[39;49;00m[33m\[39;49;00m[33m]"[39;49;00m[33m\\[39;49;00m[33m]*[39;49;00m$
[33m					)*[39;49;00m$
[33m				)[39;49;00m$
[33m				(?:[39;49;00m$
[33m					=[39;49;00m$
[33m					( [39;49;00m[33m#[39;49;00m[33m $2 = value[39;49;00m$
[33m						[^[39;49;00m[33m\[39;49;00m[33ms[39;49;00m[33m\[39;49;00m[33m]"[39;49;00m[33m\\[39;49;00m[33m]*[39;49;00m$
[33m						(?:[39;49;00m$
[33m							(?: [39;49;00m[33m\\[39;49;00m[33m. | "[^"[39;49;00m[33m\\[39;49;00m[33m]*(?:[39;49;00m[33m\\[39;49;00m[33m.[^"[39;49;00m[33m\\[39;49;00m[33m]*)*"? )[39;49;00m$
[33m							[^[39;49;00m[33m\[39;49;00m[33ms[39;49;00m[33m\[39;49;00m[33m]"[39;49;00m[33m\\[39;49;00m[33m]*[39;49;00m$
[33m						)*[39;49;00m$
[33m					)?[39;49;00m$
[33m				)?[39;49;00m$
[33m				[39;49;00m[33m\[39;49;00m[33ms*[39;49;00m$
[33m			[39;49;00m[33m/x[39;49;00m$
$
			[34mdef[39;49;00m [04m[32mself[39;49;00m.[32mparse[39;49;00m source$
				source = source.dup$
				[37m# empty_tag: the tag looks like [... /][39;49;00m$
				[37m# slice!: this deletes the \s*/] at the end[39;49;00m$
				[37m# \s+ because [url=http://rubybb.org/forum/] is NOT an empty tag.[39;49;00m$
				[37m# In RubyBBCode, you can use [url=http://rubybb.org/forum/ /], and this has to be[39;49;00m$
				[37m# interpreted correctly.[39;49;00m$
				empty_tag = source.sub!([33m/[39;49;00m[33m^:[39;49;00m[33m/[39;49;00m, [33m'[39;49;00m[33m=[39;49;00m[33m'[39;49;00m) [35mor[39;49;00m source.slice!([33m/[39;49;00m[33m\/[39;49;00m[33m$[39;49;00m[33m/[39;49;00m)$
				debug [33m'[39;49;00m[33mPARSE: [39;49;00m[33m'[39;49;00m + source.inspect + [33m'[39;49;00m[33m => [39;49;00m[33m'[39;49;00m + empty_tag.inspect$
				[37m#-> we have now an attr that's EITHER empty OR begins and ends with non-whitespace.[39;49;00m$
$
				[34mattr[39;49;00m = [31mHash[39;49;00m.new$
				[34mattr[39;49;00m[[33m:flags[39;49;00m] = []$
				source.scan([31mATTRIBUTE_SCAN[39;49;00m) { |key, value|$
					[34mif[39;49;00m [35mnot[39;49;00m value$
						[34mattr[39;49;00m[[33m:flags[39;49;00m] << unescape(key)$
					[34melse[39;49;00m$
						[34mnext[39;49;00m [34mif[39;49;00m value.empty? [35mand[39;49;00m key.empty?$
						[34mattr[39;49;00m[unescape(key)] = unescape(value)$
					[34mend[39;49;00m$
				}$
				debug [34mattr[39;49;00m.inspect$
$
				[34mreturn[39;49;00m empty_tag, [34mattr[39;49;00m$
			[34mend[39;49;00m$
$
			[34mdef[39;49;00m [04m[32mself[39;49;00m.[32munescape_char[39;49;00m esc$
				esc[[34m1[39;49;00m]$
			[34mend[39;49;00m$
$
			[34mdef[39;49;00m [04m[32mself[39;49;00m.[32munquote[39;49;00m qt$
				qt[[34m1[39;49;00m..-[34m1[39;49;00m].chomp([33m'[39;49;00m[33m"[39;49;00m[33m'[39;49;00m).gsub([33m/[39;49;00m[33m\\[39;49;00m[33m.[39;49;00m[33m/[39;49;00m) { |esc| unescape_char esc }$
			[34mend[39;49;00m$
$
			[34mdef[39;49;00m [04m[32mself[39;49;00m.[32munescape[39;49;00m str$
				str.gsub([33m/[39;49;00m[33m ([39;49;00m[33m\\[39;49;00m[33m.) | (" [^"[39;49;00m[33m\\[39;49;00m[33m]* (?:[39;49;00m[33m\\[39;49;00m[33m.[^"[39;49;00m[33m\\[39;49;00m[33m]*)* "?) [39;49;00m[33m/x[39;49;00m) {$
					[34mif[39;49;00m [31m$1[39;49;00m$
						unescape_char [31m$1[39;49;00m$
					[34melse[39;49;00m$
						unquote [31m$2[39;49;00m$
					[34mend[39;49;00m$
				}$
			[34mend[39;49;00m$
$
			[34minclude[39;49;00m [31mEnumerable[39;49;00m$
			[34mdef[39;49;00m [32meach[39;49;00m &block$
				[31m@args[39;49;00m.each(&block)$
			[34mend[39;49;00m$
$
			[34mattr_reader[39;49;00m [33m:source[39;49;00m, [33m:args[39;49;00m, [33m:value[39;49;00m$
$
			[34mdef[39;49;00m [32minitialize[39;49;00m source$
				[31m@source[39;49;00m = source$
				debug [33m'[39;49;00m[33mAttribute[39;49;00m[33m#[39;49;00m[33mnew(%p)[39;49;00m[33m'[39;49;00m % source$
				[31m@empty_tag[39;49;00m, [31m@attr[39;49;00m = [31mAttribute[39;49;00m.parse source$
				[31m@value[39;49;00m = [31m@attr[39;49;00m[[33m'[39;49;00m[33m'[39;49;00m].to_s$
			[34mend[39;49;00m$
$
			[34mdef[39;49;00m [32mempty?[39;49;00m$
				[36mself[39;49;00m == [31m@@empty_attr[39;49;00m$
			[34mend[39;49;00m$
$
			[34mdef[39;49;00m [32mempty_tag?[39;49;00m$
				[31m@empty_tag[39;49;00m$
			[34mend[39;49;00m$
$
			[34mdef[39;49;00m [32m[][39;49;00m *keys$
				res = [31m@attr[39;49;00m[*keys]$
			[34mend[39;49;00m$
$
			[34mdef[39;49;00m [32mflags[39;49;00m$
				[34mattr[39;49;00m[[33m:flags[39;49;00m]$
			[34mend[39;49;00m$
$
			[34mdef[39;49;00m [32mto_s[39;49;00m$
				[31m@attr[39;49;00m$
			[34mend[39;49;00m$
$
			[34mdef[39;49;00m [32minspect[39;49;00m$
				[33m'[39;49;00m[33mATTR[[39;49;00m[33m'[39;49;00m + [31m@attr[39;49;00m.inspect + ([31m@empty_tag[39;49;00m ? [33m'[39;49;00m[33m | empty tag[39;49;00m[33m'[39;49;00m : [33m'[39;49;00m[33m'[39;49;00m) + [33m'[39;49;00m[33m][39;49;00m[33m'[39;49;00m$
			[34mend[39;49;00m$
		[34mend[39;49;00m$
		[34mclass[39;49;00m [04m[32mAttribute[39;49;00m$
			[31m@@empty_attr[39;49;00m = [34mnew[39;49;00m [33m'[39;49;00m[33m'[39;49;00m$
		[34mend[39;49;00m$
	[34mend[39;49;00m$
