     1	[37m/**[39;49;00m$
     2	[37m *  This script is an example recommender (using made up data) showing how you might modify item-item links[39;49;00m$
     3	[37m *  by defining similar relations between items in a dataset and customizing the change in weighting.[39;49;00m$
     4	[37m *  This example creates metadata by using the genre field as the metadata_field.  The items with[39;49;00m$
     5	[37m *  the same genre have it's weight cut in half in order to boost the signals of movies that do not have the same genre.[39;49;00m$
     6	[37m *  This technique requires a customization of the standard GetItemItemRecommendations macro[39;49;00m$
     7	[37m */[39;49;00m[37m[39;49;00m$
     8	[34mimport[39;49;00m[37m [39;49;00m[33m'recommenders.pig'[39;49;00m;[37m[39;49;00m$
     9	[37m[39;49;00m$
    10	[37m[39;49;00m$
    11	[37m[39;49;00m$
    12	[34m%default[39;49;00m[37m [39;49;00mINPUT_PATH_PURCHASES[37m [39;49;00m[33m'../data/retail/purchases.json'[39;49;00m[37m[39;49;00m$
    13	[34m%default[39;49;00m[37m [39;49;00mINPUT_PATH_WISHLIST[37m [39;49;00m[33m'../data/retail/wishlists.json'[39;49;00m[37m[39;49;00m$
    14	[34m%default[39;49;00m[37m [39;49;00mINPUT_PATH_INVENTORY[37m [39;49;00m[33m'../data/retail/inventory.json'[39;49;00m[37m[39;49;00m$
    15	[34m%default[39;49;00m[37m [39;49;00mOUTPUT_PATH[37m [39;49;00m[33m'../data/retail/out/modify_item_item'[39;49;00m[37m[39;49;00m$
    16	[37m[39;49;00m$
    17	[37m[39;49;00m$
    18	[37m/******** Custom GetItemItemRecommnedations *********/[39;49;00m[37m[39;49;00m$
    19	[34mdefine[39;49;00m[37m [39;49;00m[32mrecsys__GetItemItemRecommendations_ModifyCustom[39;49;00m(user_item_signals,[37m [39;49;00mmetadata)[37m [39;49;00m[34mreturns[39;49;00m[37m [39;49;00mitem_item_recs[37m [39;49;00m{[37m[39;49;00m$
    20	[37m[39;49;00m$
    21	[37m    [39;49;00m[37m-- Convert user_item_signals to an item_item_graph[39;49;00m[37m[39;49;00m$
    22	[37m    [39;49;00mii_links_raw,[37m [39;49;00mitem_weights[37m   [39;49;00m=[37m   [39;49;00m[32mrecsys__BuildItemItemGraph[39;49;00m([37m[39;49;00m$
    23	[37m                                       [39;49;00m$user_item_signals,[37m[39;49;00m$
    24	[37m                                       [39;49;00m$LOGISTIC_PARAM,[37m[39;49;00m$
    25	[37m                                       [39;49;00m$MIN_LINK_WEIGHT,[37m[39;49;00m$
    26	[37m                                       [39;49;00m$MAX_LINKS_PER_USER[37m[39;49;00m$
    27	[37m                                     [39;49;00m);[37m[39;49;00m$
    28	[37m    [39;49;00m[37m-- NOTE this function is added in order to combine metadata with item-item links[39;49;00m[37m[39;49;00m$
    29	[37m        [39;49;00m[37m-- See macro for more detailed explination[39;49;00m[37m[39;49;00m$
    30	[37m    [39;49;00mii_links_metadata[37m           [39;49;00m=[37m   [39;49;00m[32mrecsys__AddMetadataToItemItemLinks[39;49;00m([37m[39;49;00m$
    31	[37m                                        [39;49;00mii_links_raw,[37m[39;49;00m$
    32	[37m                                        [39;49;00m$metadata[37m[39;49;00m$
    33	[37m                                    [39;49;00m);[37m[39;49;00m$
    34	[37m[39;49;00m$
    35	[37m    [39;49;00m[37m/********* Custom Code starts here ********/[39;49;00m[37m[39;49;00m$
    36	[37m[39;49;00m$
    37	[37m    [39;49;00m[37m--The code here should adjust the weights based on an item-item link and the equality of metadata.[39;49;00m[37m[39;49;00m$
    38	[37m    [39;49;00m[37m-- In this case, if the metadata is the same, the weight is reduced.  Otherwise the weight is left alone.[39;49;00m[37m[39;49;00m$
    39	[37m    [39;49;00mii_links_adjusted[37m           [39;49;00m=[37m  [39;49;00m[34mforeach[39;49;00m[37m [39;49;00mii_links_metadata[37m [39;49;00m[34mgenerate[39;49;00m[37m [39;49;00mitem_A,[37m [39;49;00mitem_B,[37m[39;49;00m$
    40	[37m                                        [39;49;00m[37m-- the amount of weight adjusted is dependant on the domain of data and what is expected[39;49;00m[37m[39;49;00m$
    41	[37m                                        [39;49;00m[37m-- It is always best to adjust the weight by multiplying it by a factor rather than addition with a constant[39;49;00m[37m[39;49;00m$
    42	[37m                                        [39;49;00m(metadata_B[37m [39;49;00m==[37m [39;49;00mmetadata_A[37m [39;49;00m?[37m [39;49;00m(weight[37m [39;49;00m*[37m [39;49;00m[34m0.5[39;49;00m):[37m [39;49;00mweight)[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00mweight;[37m[39;49;00m$
    43	[37m[39;49;00m$
    44	[37m[39;49;00m$
    45	[37m    [39;49;00m[37m/******** Custom Code stops here *********/[39;49;00m[37m[39;49;00m$
    46	[37m[39;49;00m$
    47	[37m    [39;49;00m[37m-- remove negative numbers just incase[39;49;00m[37m[39;49;00m$
    48	[37m    [39;49;00mii_links_adjusted_filt[37m [39;49;00m=[37m [39;49;00m[34mforeach[39;49;00m[37m [39;49;00mii_links_adjusted[37m [39;49;00m[34mgenerate[39;49;00m[37m [39;49;00mitem_A,[37m [39;49;00mitem_B,[37m[39;49;00m$
    49	[37m                                      [39;49;00m(weight[37m [39;49;00m<=[37m [39;49;00m[34m0[39;49;00m[37m [39;49;00m?[37m [39;49;00m[34m0[39;49;00m:[37m [39;49;00mweight)[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00mweight;[37m[39;49;00m$
    50	[37m    [39;49;00m[37m-- Adjust the weights of the graph to improve recommendations.[39;49;00m[37m[39;49;00m$
    51	[37m    [39;49;00mii_links[37m                    [39;49;00m=[37m   [39;49;00m[32mrecsys__AdjustItemItemGraphWeight[39;49;00m([37m[39;49;00m$
    52	[37m                                        [39;49;00mii_links_adjusted_filt,[37m[39;49;00m$
    53	[37m                                        [39;49;00mitem_weights,[37m[39;49;00m$
    54	[37m                                        [39;49;00m$BAYESIAN_PRIOR[37m[39;49;00m$
    55	[37m                                    [39;49;00m);[37m[39;49;00m$
    56	[37m[39;49;00m$
    57	[37m    [39;49;00m[37m-- Use the item-item graph to create item-item recommendations.[39;49;00m[37m[39;49;00m$
    58	[37m    [39;49;00m$item_item_recs[37m [39;49;00m=[37m  [39;49;00m[32mrecsys__BuildItemItemRecommendationsFromGraph[39;49;00m([37m[39;49;00m$
    59	[37m                           [39;49;00mii_links,[37m[39;49;00m$
    60	[37m                           [39;49;00m$NUM_RECS_PER_ITEM,[37m[39;49;00m$
    61	[37m                           [39;49;00m$NUM_RECS_PER_ITEM[37m[39;49;00m$
    62	[37m                       [39;49;00m);[37m[39;49;00m$
    63	};[37m[39;49;00m$
    64	[37m[39;49;00m$
    65	[37m[39;49;00m$
    66	[37m/******* Load Data **********/[39;49;00m[37m[39;49;00m$
    67	[37m[39;49;00m$
    68	[37m--Get purchase signals[39;49;00m[37m[39;49;00m$
    69	purchase_input[37m [39;49;00m=[37m [39;49;00m[34mload[39;49;00m[37m [39;49;00m[33m'$INPUT_PATH_PURCHASES'[39;49;00m[37m [39;49;00m[34musing[39;49;00m[37m [39;49;00morg.apache.pig.piggybank.storage.JsonLoader([37m[39;49;00m$
    70	[37m                    [39;49;00m'row_id: [36mint[39;49;00m,[37m[39;49;00m$
    71	[37m                     [39;49;00mmovie_id:[37m [39;49;00m[36mchararray[39;49;00m,[37m[39;49;00m$
    72	[37m                     [39;49;00mmovie_name:[37m [39;49;00m[36mchararray[39;49;00m,[37m[39;49;00m$
    73	[37m                     [39;49;00muser_id:[37m [39;49;00m[36mchararray[39;49;00m,[37m[39;49;00m$
    74	[37m                     [39;49;00mpurchase_price:[37m [39;49;00m[36mint[39;49;00m');$
    75	$
    76	[37m--Get wishlist signals[39;49;00m[37m[39;49;00m$
    77	wishlist_input[37m [39;49;00m=[37m  [39;49;00m[34mload[39;49;00m[37m [39;49;00m[33m'$INPUT_PATH_WISHLIST'[39;49;00m[37m [39;49;00m[34musing[39;49;00m[37m [39;49;00morg.apache.pig.piggybank.storage.JsonLoader([37m[39;49;00m$
    78	[37m                     [39;49;00m'row_id: [36mint[39;49;00m,[37m[39;49;00m$
    79	[37m                      [39;49;00mmovie_id:[37m [39;49;00m[36mchararray[39;49;00m,[37m[39;49;00m$
    80	[37m                      [39;49;00mmovie_name:[37m [39;49;00m[36mchararray[39;49;00m,[37m[39;49;00m$
    81	[37m                      [39;49;00muser_id:[37m [39;49;00m[36mchararray[39;49;00m');$
    82	$
    83	$
    84	[37m/******* Convert Data to Signals **********/[39;49;00m[37m[39;49;00m$
    85	[37m[39;49;00m$
    86	[37m-- Start with choosing 1 as max weight for a signal.[39;49;00m[37m[39;49;00m$
    87	purchase_signals[37m [39;49;00m=[37m [39;49;00m[34mforeach[39;49;00m[37m [39;49;00mpurchase_input[37m [39;49;00m[34mgenerate[39;49;00m[37m[39;49;00m$
    88	[37m                        [39;49;00muser_id[37m    [39;49;00m[34mas[39;49;00m[37m [39;49;00muser,[37m[39;49;00m$
    89	[37m                        [39;49;00mmovie_name[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00mitem,[37m[39;49;00m$
    90	[37m                        [39;49;00m[34m1.0[39;49;00m[37m        [39;49;00m[34mas[39;49;00m[37m [39;49;00mweight;[37m[39;49;00m$
    91	[37m[39;49;00m$
    92	[37m[39;49;00m$
    93	[37m-- Start with choosing 0.5 as weight for wishlist items because that is a weaker signal than[39;49;00m[37m[39;49;00m$
    94	[37m-- purchasing an item.[39;49;00m[37m[39;49;00m$
    95	wishlist_signals[37m [39;49;00m=[37m [39;49;00m[34mforeach[39;49;00m[37m [39;49;00mwishlist_input[37m [39;49;00m[34mgenerate[39;49;00m[37m[39;49;00m$
    96	[37m                        [39;49;00muser_id[37m    [39;49;00m[34mas[39;49;00m[37m [39;49;00muser,[37m[39;49;00m$
    97	[37m                        [39;49;00mmovie_name[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00mitem,[37m[39;49;00m$
    98	[37m                        [39;49;00m[34m0.5[39;49;00m[37m        [39;49;00m[34mas[39;49;00m[37m [39;49;00mweight;[37m[39;49;00m$
    99	[37m[39;49;00m$
   100	user_signals[37m [39;49;00m=[37m [39;49;00m[34munion[39;49;00m[37m [39;49;00mpurchase_signals,[37m [39;49;00mwishlist_signals;[37m[39;49;00m$
   101	[37m[39;49;00m$
   102	[37m[39;49;00m$
   103	[37m/******** Changes for Modifying item-item links ******/[39;49;00m[37m[39;49;00m$
   104	inventory_input[37m [39;49;00m=[37m [39;49;00m[34mload[39;49;00m[37m [39;49;00m[33m'$INPUT_PATH_INVENTORY'[39;49;00m[37m [39;49;00m[34musing[39;49;00m[37m [39;49;00morg.apache.pig.piggybank.storage.JsonLoader([37m[39;49;00m$
   105	[37m                     [39;49;00m'movie_title: [36mchararray[39;49;00m,[37m[39;49;00m$
   106	[37m                      [39;49;00mgenres:[37m [39;49;00m[34mbag[39;49;00m{[36mtuple[39;49;00m(content:[36mchararray[39;49;00m)}');$
   107	$
   108	$
   109	metadata[37m [39;49;00m=[37m [39;49;00m[34mforeach[39;49;00m[37m [39;49;00minventory_input[37m [39;49;00m[34mgenerate[39;49;00m[37m[39;49;00m$
   110	[37m              [39;49;00m[34mFLATTEN[39;49;00m(genres)[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00mmetadata_field,[37m[39;49;00m$
   111	[37m              [39;49;00mmovie_title[37m [39;49;00m[34mas[39;49;00m[37m [39;49;00mitem;[37m[39;49;00m$
   112	[37m-- requires the macro to be written seperately[39;49;00m[37m[39;49;00m$
   113	[37m  [39;49;00m[37m--NOTE this macro is defined within this file for clarity[39;49;00m[37m[39;49;00m$
   114	item_item_recs[37m [39;49;00m=[37m [39;49;00m[32mrecsys__GetItemItemRecommendations_ModifyCustom[39;49;00m(user_signals,[37m [39;49;00mmetadata);[37m[39;49;00m$
   115	[37m/******* No more changes ********/[39;49;00m[37m[39;49;00m$
   116	[37m[39;49;00m$
   117	[37m[39;49;00m$
   118	user_item_recs[37m [39;49;00m=[37m [39;49;00m[32mrecsys__GetUserItemRecommendations[39;49;00m(user_signals,[37m [39;49;00mitem_item_recs);[37m[39;49;00m$
   119	[37m[39;49;00m$
   120	[37m--Completely unrelated code stuck in the middle[39;49;00m[37m[39;49;00m$
   121	data[37m        [39;49;00m=[37m    [39;49;00m[34mLOAD[39;49;00m[37m [39;49;00m[33m's3n://my-s3-bucket/path/to/responses'[39;49;00m[37m[39;49;00m$
   122	[37m                 [39;49;00m[34mUSING[39;49;00m[37m [39;49;00morg.apache.pig.piggybank.storage.JsonLoader();[37m[39;49;00m$
   123	responses[37m   [39;49;00m=[37m    [39;49;00m[34mFOREACH[39;49;00m[37m [39;49;00mdata[37m [39;49;00m[34mGENERATE[39;49;00m[37m [39;49;00mobject#[33m'response'[39;49;00m[37m [39;49;00m[34mAS[39;49;00m[37m [39;49;00mresponse:[37m [39;49;00m[34mmap[39;49;00m[];[37m[39;49;00m$
   124	out[37m         [39;49;00m=[37m    [39;49;00m[34mFOREACH[39;49;00m[37m [39;49;00mresponses[37m[39;49;00m$
   125	[37m                 [39;49;00m[34mGENERATE[39;49;00m[37m [39;49;00mresponse#[33m'id'[39;49;00m[37m [39;49;00m[34mAS[39;49;00m[37m [39;49;00mid:[37m [39;49;00m[36mint[39;49;00m,[37m [39;49;00mresponse#[33m'thread'[39;49;00m[37m [39;49;00m[34mAS[39;49;00m[37m [39;49;00mthread:[37m [39;49;00m[36mchararray[39;49;00m,[37m[39;49;00m$
   126	[37m                          [39;49;00mresponse#[33m'comments'[39;49;00m[37m [39;49;00m[34mAS[39;49;00m[37m [39;49;00mcomments:[37m [39;49;00m{t:[37m [39;49;00m(comment:[37m [39;49;00m[36mchararray[39;49;00m)};[37m[39;49;00m$
   127	[34mSTORE[39;49;00m[37m [39;49;00mout[37m [39;49;00m[34mINTO[39;49;00m[37m [39;49;00m[33m's3n://path/to/output'[39;49;00m[37m [39;49;00m[34mUSING[39;49;00m[37m [39;49;00m[36mPigStorage[39;49;00m([33m'|'[39;49;00m);[37m[39;49;00m$
   128	[37m[39;49;00m$
   129	[37m[39;49;00m$
   130	[37m/******* Store recommendations **********/[39;49;00m[37m[39;49;00m$
   131	[37m[39;49;00m$
   132	[37m--  If your output folder exists already, hadoop will refuse to write data to it.[39;49;00m[37m[39;49;00m$
   133	[37m[39;49;00m$
   134	[34mrmf[39;49;00m[37m [39;49;00m$OUTPUT_PATH/item_item_recs;[37m[39;49;00m$
   135	[34mrmf[39;49;00m[37m [39;49;00m$OUTPUT_PATH/user_item_recs;[37m[39;49;00m$
   136	[37m[39;49;00m$
   137	[34mstore[39;49;00m[37m [39;49;00mitem_item_recs[37m [39;49;00m[34minto[39;49;00m[37m [39;49;00m[33m'$OUTPUT_PATH/item_item_recs'[39;49;00m[37m [39;49;00m[34musing[39;49;00m[37m [39;49;00m[36mPigStorage[39;49;00m();[37m[39;49;00m$
   138	[34mstore[39;49;00m[37m [39;49;00muser_item_recs[37m [39;49;00m[34minto[39;49;00m[37m [39;49;00m[33m'$OUTPUT_PATH/user_item_recs'[39;49;00m[37m [39;49;00m[34musing[39;49;00m[37m [39;49;00m[36mPigStorage[39;49;00m();[37m[39;49;00m$
   139	[37m[39;49;00m$
   140	[37m-- STORE the item_item_recs into dynamo[39;49;00m[37m[39;49;00m$
   141	[34mSTORE[39;49;00m[37m [39;49;00mitem_item_recs[37m[39;49;00m$
   142	[37m [39;49;00m[34mINTO[39;49;00m[37m [39;49;00m[33m'$OUTPUT_PATH/unused-ii-table-data'[39;49;00m[37m[39;49;00m$
   143	[34mUSING[39;49;00m[37m [39;49;00mcom.mortardata.pig.storage.DynamoDBStorage([33m'$II_TABLE'[39;49;00m,[37m [39;49;00m[33m'$AWS_ACCESS_KEY_ID'[39;49;00m,[37m [39;49;00m[33m'$AWS_SECRET_ACCESS_KEY'[39;49;00m);[37m[39;49;00m$
   144	[37m[39;49;00m$
   145	[37m-- STORE the user_item_recs into dynamo[39;49;00m[37m[39;49;00m$
   146	[34mSTORE[39;49;00m[37m [39;49;00muser_item_recs[37m[39;49;00m$
   147	[37m [39;49;00m[34mINTO[39;49;00m[37m [39;49;00m[33m'$OUTPUT_PATH/unused-ui-table-data'[39;49;00m[37m[39;49;00m$
   148	[34mUSING[39;49;00m[37m [39;49;00mcom.mortardata.pig.storage.DynamoDBStorage([33m'$UI_TABLE'[39;49;00m,[37m [39;49;00m[33m'$AWS_ACCESS_KEY_ID'[39;49;00m,[37m [39;49;00m[33m'$AWS_SECRET_ACCESS_KEY'[39;49;00m);$
