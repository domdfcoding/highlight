     1^I[36m#[39;49;00m[36mpike __REAL_VERSION__[39;49;00m[36m[39;49;00m$
     2^I[37m[39;49;00m$
     3^I[34mconstant[39;49;00m[37m [39;49;00mGeneric[37m [39;49;00m=[37m [39;49;00m__builtin.GenericError;[37m[39;49;00m$
     4^I[37m[39;49;00m$
     5^I[34mconstant[39;49;00m[37m [39;49;00mIndex[37m [39;49;00m=[37m [39;49;00m__builtin.IndexError;[37m[39;49;00m$
     6^I[37m[39;49;00m$
     7^I[34mconstant[39;49;00m[37m [39;49;00mBadArgument[37m [39;49;00m=[37m [39;49;00m__builtin.BadArgumentError;[37m[39;49;00m$
     8^I[37m[39;49;00m$
     9^I[34mconstant[39;49;00m[37m [39;49;00mMath[37m [39;49;00m=[37m [39;49;00m__builtin.MathError;[37m[39;49;00m$
    10^I[37m[39;49;00m$
    11^I[34mconstant[39;49;00m[37m [39;49;00mResource[37m [39;49;00m=[37m [39;49;00m__builtin.ResourceError;[37m[39;49;00m$
    12^I[37m[39;49;00m$
    13^I[34mconstant[39;49;00m[37m [39;49;00mPermission[37m [39;49;00m=[37m [39;49;00m__builtin.PermissionError;[37m[39;49;00m$
    14^I[37m[39;49;00m$
    15^I[34mconstant[39;49;00m[37m [39;49;00mDecode[37m [39;49;00m=[37m [39;49;00m__builtin.DecodeError;[37m[39;49;00m$
    16^I[37m[39;49;00m$
    17^I[34mconstant[39;49;00m[37m [39;49;00mCpp[37m [39;49;00m=[37m [39;49;00m__builtin.CppError;[37m[39;49;00m$
    18^I[37m[39;49;00m$
    19^I[34mconstant[39;49;00m[37m [39;49;00mCompilation[37m [39;49;00m=[37m [39;49;00m__builtin.CompilationError;[37m[39;49;00m$
    20^I[37m[39;49;00m$
    21^I[34mconstant[39;49;00m[37m [39;49;00mMasterLoad[37m [39;49;00m=[37m [39;49;00m__builtin.MasterLoadError;[37m[39;49;00m$
    22^I[37m[39;49;00m$
    23^I[34mconstant[39;49;00m[37m [39;49;00mModuleLoad[37m [39;49;00m=[37m [39;49;00m__builtin.ModuleLoadError;[37m[39;49;00m$
    24^I[37m[39;49;00m$
    25^I[37m//! Returns an Error object for any argument it receives. If the[39;49;00m$
    26^I[37m//! argument already is an Error object or is empty, it does nothing.[39;49;00m$
    27^I[36mobject[39;49;00m[37m [39;49;00m[32mmkerror[39;49;00m([36mmixed[39;49;00m[37m [39;49;00merror)[37m[39;49;00m$
    28^I{[37m[39;49;00m$
    29^I[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m(error[37m [39;49;00m==[37m [39;49;00mUNDEFINED)[37m[39;49;00m$
    30^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00merror;[37m[39;49;00m$
    31^I[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m(objectp(error)[37m [39;49;00m&&[37m [39;49;00merror->is_generic_error)[37m[39;49;00m$
    32^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00merror;[37m[39;49;00m$
    33^I[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m(arrayp(error))[37m[39;49;00m$
    34^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mError.Generic(@error);[37m[39;49;00m$
    35^I[37m  [39;49;00m[34mif[39;49;00m[37m [39;49;00m(stringp(error))[37m[39;49;00m$
    36^I[37m    [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mError.Generic(error);[37m[39;49;00m$
    37^I[37m  [39;49;00m[34mreturn[39;49;00m[37m [39;49;00mError.Generic(sprintf([33m"[39;49;00m[33m%O[39;49;00m[33m"[39;49;00m,[37m [39;49;00merror));[37m[39;49;00m$
    38^I}$
