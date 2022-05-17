     1^I[37m/**[39;49;00m$
     2^I[37m *  This script is an example recommender (using made up data) showing how you might modify item-item links[39;49;00m$
     3^I[37m *  by defining similar relations between items in a dataset and customizing the change in weighting.[39;49;00m$
     4^I[37m *  This example creates metadata by using the genre field as the metadata_field.  The items with[39;49;00m$
     5^I[37m *  the same genre have it's weight cut in half in order to boost the signals of movies that do not have the same genre.[39;49;00m$
     6^I[37m *  This technique requires a customization of the standard GetItemItemRecommendations macro[39;49;00m$
     7^I[37m */[39;49;00m[37m[39;49;00m$
     8^I[34mimport[39;49;00m[37m [39;49;00m[33m'recommenders.pig'[39;49;00m;[37m[39;49;00m$
     9^I[37m[39;49;00m$
    10^I[37m[39;49;00m$
    11^I[37m[39;49;00m$
    12^I[34m%default[39;49;00m[37m [39;49;00mINPUT_PATH_PURCHASES[37m [39;49;00m[33m'../data/retail/purchases.json'[39;49;00m[37m[39;49;00m$
    13^I[34m%default[39;49;00m[37m [39;49;00mINPUT_PATH_WISHLIST[37m [39;49;00m[33m'../data/retail/wishlists.json'[39;49;00m[37m[39;49;00m$
    14^I[34m%default[39;49;00m[37m [39;49;00mINPUT_PATH_INVENTORY[37m [39;49;00m[33m'../data/retail/inventory.json'[39;49;00m[37m[39;49;00m$
    15^I[34m%default[39;49;00m[37m [39;49;00mOUTPUT_PATH[37m [39;49;00m[33m'../data/retail/out/modify_item_item'[39;49;00m[37m[39;49;00m$
    16^I[37m[39;49;00m$
    17^I[37m[39;49;00m$
    18^I[37m/******** Custom GetItemItemRecommnedations *********/[39;49;00m[37m[39;49;00m$
    19^I[34mdefine[39;49;00m[37m [39;49;00m[32mrecsys__GetItemItemRecommendations_ModifyCustom[39;49;00m(user_item_signals,[37m [39;49;00mmetadata)[37m [39;49;00m[34mreturns[39;49;00m[37m [39;49;00mitem_item_recs[37m [39;49;00m{[37m[39;49;00m$
    20^I[37m[39;49;00m$
    21^I[37m    [39;49;00m[37m-- Convert user_item_signals to an item_item_graph[39;49;00m[37m[39;49;00m$
    22^I[37m    [39;49;00mii_links_raw,[37m [39;49;00mitem_weights[37m   [39;49;00m=[37m   [39;49;00m[32mrecsys__BuildItemItemGraph[39;49;00m([37m[39;49;00m$
    23^I[37m                                       [39;49;00m$user_item_signals,[37m[39;49;00m$
    24^I[37m                                       [39;49;00m$LOGISTIC_PARAM,[37m[39;49;00m$
    25^I[37m                                       [39;49;00m$MIN_LINK_WEIGHT,[37m[39;49;00m$
    26^I[37m                                       [39;49;00m$MAX_LINKS_PER_USER[37m[39;49;00m$
    27^I[37m                                     [39;49;00m);[37m[39;49;00m$
    28^I[37m    [39;49;00m[37m-- NOTE this function is added in order to combine metadata with item-item links[39;49;00m[37m[39;49;00m$
    29^I[37m        [39;49;00m[37m-- See macro for more detailed explination[39;49;00m[37m[39;49;00m$
    30^I[37m    [39;49;00mii_links_metadata[37m           [39;49;00m=[37m   [39;49;00m[32mrecsys__AddMetadataToItemItemLinks[39;49;00m([37m[39;49;00m$
    31^I[37m                                        [39;49;00mii_links_raw,[37m[39;49;00m$
    32^I[37m                                        [39;49;00m$metadata[37m[39;49;00m$
    33^I[37m                                    [39;49;00m);[37m[39;49;00m$
    34^I[37m[39;49;00m$
    35^I[37m    [39;49;00m[37m/********* Custom Code starts here ********/[39;49;00m[37m[39;49;00m$
    36^I[37m[39;49;00m$
    37^I[37m    [39;49;00m[37m--The code here should adjust the weights based on an item-item link and the equality of metadata.[39;49;00m[37m[39;49;00m$
    38^I[37m    [39;49;00m[37m-- In this case, if the metadata is the same, the weight is reduced.  Otherwise the weight is left alone.[39;49;00m[37m[39;49;00m$
    39^I[37m    [39;49;00mii_links_adjusted[37m           [39;49;00m=[37m  [39;49;00m[34mforeach[39;49;00m[37m [39;49;00mii_links_metadata[37m [39;49;00m[34mgenerate[39;49;00m[37m [39;49;00mitem_A,[37m [39;49;00mitem_B,[37m[39;49;00m$
    40^I[37m                                        [39;49;00m[37m-- the amount of weight adjusted is dependant on the domain of data and what is expected[39;49;00m[37m[39;49;00m$
    41^I[37m                                        [39;49;00m[37m-- It is always best to adjust the weight by multiplying it by a factor rather than addition with a constant[39;49;00m[37m[39;49;00m$
    42^I[37m                                        [39;49;00m(metadata_B[37m [39;49;00m==[37m [39;49;00mmetadata_A[37m [39;49;00m?[37m [39;49;00m(weight[37m [39;49;00m*[37m [39;49;00m[34m0.5[39;49;00m):[37m [39;49;00mweight)[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00mweight;[37m[39;49;00m$
    43^I[37m[39;49;00m$
    44^I[37m[39;49;00m$
    45^I[37m    [39;49;00m[37m/******** Custom Code stops here *********/[39;49;00m[37m[39;49;00m$
    46^I[37m[39;49;00m$
    47^I[37m    [39;49;00m[37m-- remove negative numbers just incase[39;49;00m[37m[39;49;00m$
    48^I[37m    [39;49;00mii_links_adjusted_filt[37m [39;49;00m=[37m [39;49;00m[34mforeach[39;49;00m[37m [39;49;00mii_links_adjusted[37m [39;49;00m[34mgenerate[39;49;00m[37m [39;49;00mitem_A,[37m [39;49;00mitem_B,[37m[39;49;00m$
    49^I[37m                                      [39;49;00m(weight[37m [39;49;00m<=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m?[37m [39;49;00m[34m0[39;49;00m:[37m [39;49;00mweight)[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00mweight;[37m[39;49;00m$
    50^I[37m    [39;49;00m[37m-- Adjust the weights of the graph to improve recommendations.[39;49;00m[37m[39;49;00m$
    51^I[37m    [39;49;00mii_links[37m                    [39;49;00m=[37m   [39;49;00m[32mrecsys__AdjustItemItemGraphWeight[39;49;00m([37m[39;49;00m$
    52^I[37m                                        [39;49;00mii_links_adjusted_filt,[37m[39;49;00m$
    53^I[37m                                        [39;49;00mitem_weights,[37m[39;49;00m$
    54^I[37m                                        [39;49;00m$BAYESIAN_PRIOR[37m[39;49;00m$
    55^I[37m                                    [39;49;00m);[37m[39;49;00m$
    56^I[37m[39;49;00m$
    57^I[37m    [39;49;00m[37m-- Use the item-item graph to create item-item recommendations.[39;49;00m[37m[39;49;00m$
    58^I[37m    [39;49;00m$item_item_recs[37m [39;49;00m=[37m  [39;49;00m[32mrecsys__BuildItemItemRecommendationsFromGraph[39;49;00m([37m[39;49;00m$
    59^I[37m                           [39;49;00mii_links,[37m[39;49;00m$
    60^I[37m                           [39;49;00m$NUM_RECS_PER_ITEM,[37m[39;49;00m$
    61^I[37m                           [39;49;00m$NUM_RECS_PER_ITEM[37m[39;49;00m$
    62^I[37m                       [39;49;00m);[37m[39;49;00m$
    63^I};[37m[39;49;00m$
    64^I[37m[39;49;00m$
    65^I[37m[39;49;00m$
    66^I[37m/******* Load Data **********/[39;49;00m[37m[39;49;00m$
    67^I[37m[39;49;00m$
    68^I[37m--Get purchase signals[39;49;00m[37m[39;49;00m$
    69^Ipurchase_input[37m [39;49;00m=[37m [39;49;00m[34mload[39;49;00m[37m [39;49;00m[33m'$INPUT_PATH_PURCHASES'[39;49;00m[37m [39;49;00m[34musing[39;49;00m[37m [39;49;00morg.apache.pig.piggybank.storage.JsonLoader([37m[39;49;00m$
    70^I[37m                    [39;49;00m'row_id: [36mint[39;49;00m,[37m[39;49;00m$
    71^I[37m                     [39;49;00mmovie_id:[37m [39;49;00m[36mchararray[39;49;00m,[37m[39;49;00m$
    72^I[37m                     [39;49;00mmovie_name:[37m [39;49;00m[36mchararray[39;49;00m,[37m[39;49;00m$
    73^I[37m                     [39;49;00muser_id:[37m [39;49;00m[36mchararray[39;49;00m,[37m[39;49;00m$
    74^I[37m                     [39;49;00mpurchase_price:[37m [39;49;00m[36mint[39;49;00m');$
    75^I$
    76^I[37m--Get wishlist signals[39;49;00m[37m[39;49;00m$
    77^Iwishlist_input[37m [39;49;00m=[37m  [39;49;00m[34mload[39;49;00m[37m [39;49;00m[33m'$INPUT_PATH_WISHLIST'[39;49;00m[37m [39;49;00m[34musing[39;49;00m[37m [39;49;00morg.apache.pig.piggybank.storage.JsonLoader([37m[39;49;00m$
    78^I[37m                     [39;49;00m'row_id: [36mint[39;49;00m,[37m[39;49;00m$
    79^I[37m                      [39;49;00mmovie_id:[37m [39;49;00m[36mchararray[39;49;00m,[37m[39;49;00m$
    80^I[37m                      [39;49;00mmovie_name:[37m [39;49;00m[36mchararray[39;49;00m,[37m[39;49;00m$
    81^I[37m                      [39;49;00muser_id:[37m [39;49;00m[36mchararray[39;49;00m');$
    82^I$
    83^I$
    84^I[37m/******* Convert Data to Signals **********/[39;49;00m[37m[39;49;00m$
    85^I[37m[39;49;00m$
    86^I[37m-- Start with choosing 1 as max weight for a signal.[39;49;00m[37m[39;49;00m$
    87^Ipurchase_signals[37m [39;49;00m=[37m [39;49;00m[34mforeach[39;49;00m[37m [39;49;00mpurchase_input[37m [39;49;00m[34mgenerate[39;49;00m[37m[39;49;00m$
    88^I[37m                        [39;49;00muser_id[37m    [39;49;00m[34mas[39;49;00m[37m [39;49;00muser,[37m[39;49;00m$
    89^I[37m                        [39;49;00mmovie_name[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00mitem,[37m[39;49;00m$
    90^I[37m                        [39;49;00m[34m1.0[39;49;00m[37m        [39;49;00m[34mas[39;49;00m[37m [39;49;00mweight;[37m[39;49;00m$
    91^I[37m[39;49;00m$
    92^I[37m[39;49;00m$
    93^I[37m-- Start with choosing 0.5 as weight for wishlist items because that is a weaker signal than[39;49;00m[37m[39;49;00m$
    94^I[37m-- purchasing an item.[39;49;00m[37m[39;49;00m$
    95^Iwishlist_signals[37m [39;49;00m=[37m [39;49;00m[34mforeach[39;49;00m[37m [39;49;00mwishlist_input[37m [39;49;00m[34mgenerate[39;49;00m[37m[39;49;00m$
    96^I[37m                        [39;49;00muser_id[37m    [39;49;00m[34mas[39;49;00m[37m [39;49;00muser,[37m[39;49;00m$
    97^I[37m                        [39;49;00mmovie_name[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00mitem,[37m[39;49;00m$
    98^I[37m                        [39;49;00m[34m0.5[39;49;00m[37m        [39;49;00m[34mas[39;49;00m[37m [39;49;00mweight;[37m[39;49;00m$
    99^I[37m[39;49;00m$
   100^Iuser_signals[37m [39;49;00m=[37m [39;49;00m[34munion[39;49;00m[37m [39;49;00mpurchase_signals,[37m [39;49;00mwishlist_signals;[37m[39;49;00m$
   101^I[37m[39;49;00m$
   102^I[37m[39;49;00m$
   103^I[37m/******** Changes for Modifying item-item links ******/[39;49;00m[37m[39;49;00m$
   104^Iinventory_input[37m [39;49;00m=[37m [39;49;00m[34mload[39;49;00m[37m [39;49;00m[33m'$INPUT_PATH_INVENTORY'[39;49;00m[37m [39;49;00m[34musing[39;49;00m[37m [39;49;00morg.apache.pig.piggybank.storage.JsonLoader([37m[39;49;00m$
   105^I[37m                     [39;49;00m'movie_title: [36mchararray[39;49;00m,[37m[39;49;00m$
   106^I[37m                      [39;49;00mgenres:[37m [39;49;00m[34mbag[39;49;00m{[36mtuple[39;49;00m(content:[36mchararray[39;49;00m)}');$
   107^I$
   108^I$
   109^Imetadata[37m [39;49;00m=[37m [39;49;00m[34mforeach[39;49;00m[37m [39;49;00minventory_input[37m [39;49;00m[34mgenerate[39;49;00m[37m[39;49;00m$
   110^I[37m              [39;49;00m[34mFLATTEN[39;49;00m(genres)[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00mmetadata_field,[37m[39;49;00m$
   111^I[37m              [39;49;00mmovie_title[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00mitem;[37m[39;49;00m$
   112^I[37m-- requires the macro to be written seperately[39;49;00m[37m[39;49;00m$
   113^I[37m  [39;49;00m[37m--NOTE this macro is defined within this file for clarity[39;49;00m[37m[39;49;00m$
   114^Iitem_item_recs[37m [39;49;00m=[37m [39;49;00m[32mrecsys__GetItemItemRecommendations_ModifyCustom[39;49;00m(user_signals,[37m [39;49;00mmetadata);[37m[39;49;00m$
   115^I[37m/******* No more changes ********/[39;49;00m[37m[39;49;00m$
   116^I[37m[39;49;00m$
   117^I[37m[39;49;00m$
   118^Iuser_item_recs[37m [39;49;00m=[37m [39;49;00m[32mrecsys__GetUserItemRecommendations[39;49;00m(user_signals,[37m [39;49;00mitem_item_recs);[37m[39;49;00m$
   119^I[37m[39;49;00m$
   120^I[37m--Completely unrelated code stuck in the middle[39;49;00m[37m[39;49;00m$
   121^Idata[37m        [39;49;00m=[37m    [39;49;00m[34mLOAD[39;49;00m[37m [39;49;00m[33m's3n://my-s3-bucket/path/to/responses'[39;49;00m[37m[39;49;00m$
   122^I[37m                 [39;49;00m[34mUSING[39;49;00m[37m [39;49;00morg.apache.pig.piggybank.storage.JsonLoader();[37m[39;49;00m$
   123^Iresponses[37m   [39;49;00m=[37m    [39;49;00m[34mFOREACH[39;49;00m[37m [39;49;00mdata[37m [39;49;00m[34mGENERATE[39;49;00m[37m [39;49;00mobject#[33m'response'[39;49;00m[37m [39;49;00m[34mAS[39;49;00m[37m [39;49;00mresponse:[37m [39;49;00m[34mmap[39;49;00m[];[37m[39;49;00m$
   124^Iout[37m         [39;49;00m=[37m    [39;49;00m[34mFOREACH[39;49;00m[37m [39;49;00mresponses[37m[39;49;00m$
   125^I[37m                 [39;49;00m[34mGENERATE[39;49;00m[37m [39;49;00mresponse#[33m'id'[39;49;00m[37m [39;49;00m[34mAS[39;49;00m[37m [39;49;00mid:[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00mresponse#[33m'thread'[39;49;00m[37m [39;49;00m[34mAS[39;49;00m[37m [39;49;00mthread:[37m [39;49;00m[36mchararray[39;49;00m,[37m[39;49;00m$
   126^I[37m                          [39;49;00mresponse#[33m'comments'[39;49;00m[37m [39;49;00m[34mAS[39;49;00m[37m [39;49;00mcomments:[37m [39;49;00m{t:[37m [39;49;00m(comment:[37m [39;49;00m[36mchararray[39;49;00m)};[37m[39;49;00m$
   127^I[34mSTORE[39;49;00m[37m [39;49;00mout[37m [39;49;00m[34mINTO[39;49;00m[37m [39;49;00m[33m's3n://path/to/output'[39;49;00m[37m [39;49;00m[34mUSING[39;49;00m[37m [39;49;00m[36mPigStorage[39;49;00m([33m'|'[39;49;00m);[37m[39;49;00m$
   128^I[37m[39;49;00m$
   129^I[37m[39;49;00m$
   130^I[37m/******* Store recommendations **********/[39;49;00m[37m[39;49;00m$
   131^I[37m[39;49;00m$
   132^I[37m--  If your output folder exists already, hadoop will refuse to write data to it.[39;49;00m[37m[39;49;00m$
   133^I[37m[39;49;00m$
   134^I[34mrmf[39;49;00m[37m [39;49;00m$OUTPUT_PATH/item_item_recs;[37m[39;49;00m$
   135^I[34mrmf[39;49;00m[37m [39;49;00m$OUTPUT_PATH/user_item_recs;[37m[39;49;00m$
   136^I[37m[39;49;00m$
   137^I[34mstore[39;49;00m[37m [39;49;00mitem_item_recs[37m [39;49;00m[34minto[39;49;00m[37m [39;49;00m[33m'$OUTPUT_PATH/item_item_recs'[39;49;00m[37m [39;49;00m[34musing[39;49;00m[37m [39;49;00m[36mPigStorage[39;49;00m();[37m[39;49;00m$
   138^I[34mstore[39;49;00m[37m [39;49;00muser_item_recs[37m [39;49;00m[34minto[39;49;00m[37m [39;49;00m[33m'$OUTPUT_PATH/user_item_recs'[39;49;00m[37m [39;49;00m[34musing[39;49;00m[37m [39;49;00m[36mPigStorage[39;49;00m();[37m[39;49;00m$
   139^I[37m[39;49;00m$
   140^I[37m-- STORE the item_item_recs into dynamo[39;49;00m[37m[39;49;00m$
   141^I[34mSTORE[39;49;00m[37m [39;49;00mitem_item_recs[37m[39;49;00m$
   142^I[37m [39;49;00m[34mINTO[39;49;00m[37m [39;49;00m[33m'$OUTPUT_PATH/unused-ii-table-data'[39;49;00m[37m[39;49;00m$
   143^I[34mUSING[39;49;00m[37m [39;49;00mcom.mortardata.pig.storage.DynamoDBStorage([33m'$II_TABLE'[39;49;00m,[37m [39;49;00m[33m'$AWS_ACCESS_KEY_ID'[39;49;00m,[37m [39;49;00m[33m'$AWS_SECRET_ACCESS_KEY'[39;49;00m);[37m[39;49;00m$
   144^I[37m[39;49;00m$
   145^I[37m-- STORE the user_item_recs into dynamo[39;49;00m[37m[39;49;00m$
   146^I[34mSTORE[39;49;00m[37m [39;49;00muser_item_recs[37m[39;49;00m$
   147^I[37m [39;49;00m[34mINTO[39;49;00m[37m [39;49;00m[33m'$OUTPUT_PATH/unused-ui-table-data'[39;49;00m[37m[39;49;00m$
   148^I[34mUSING[39;49;00m[37m [39;49;00mcom.mortardata.pig.storage.DynamoDBStorage([33m'$UI_TABLE'[39;49;00m,[37m [39;49;00m[33m'$AWS_ACCESS_KEY_ID'[39;49;00m,[37m [39;49;00m[33m'$AWS_SECRET_ACCESS_KEY'[39;49;00m);$
