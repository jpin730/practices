from datetime import datetime

def bubbleSort(array):
  n = len(array)
  for i in range(n):
    swap = False
    for j in range(n-i-1):
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]
        swap = True
    if not swap:
      break

def selectionSort(array):
  for i in range(len(array)):
    indexOfSmallest = i
    for j in range(i+1, len(array)):
      if array[indexOfSmallest] > array[j]:
        indexOfSmallest = j
    array[indexOfSmallest], array[i] =  array[i], array[indexOfSmallest]

ARRAY = [7398,7123,4055,62,5371,1542,2657,3863,2290,3442,2900,1064,2427,4063,2825,993,7406,7245,3761,6190,6382,1736,3280,2146,564,1058,763,2158,4093,1527,4704,6714,3791,344,4061,273,4328,1551,1203,3745,5876,6630,7461,5091,3165,2385,1853,5145,1102,5432,7367,3396,7513,3260,2428,3521,1123,1345,5061,529,4564,2641,3500,2650,5544,7134,5474,1905,5948,3745,5965,5616,1668,5345,6293,5523,3331,1466,6769,778,4729,2860,6732,524,1912,1317,7337,4843,4057,5108,7483,5144,3047,4262,1852,6379,5961,4663,2940,6989,5016,5712,4892,1280,5421,5491,6239,115,6200,815,6181,1295,2248,41,694,4319,5750,3366,147,6999,5810,4414,5729,6757,3188,2465,6021,2315,3060,2697,3102,3857,5708,3924,1121,3864,2263,167,7278,4611,1528,2687,369,7391,5749,7090,6428,3757,2929,5391,5686,2916,1352,363,6781,4354,276,4591,4012,3192,3812,3840,3264,4074,5296,5729,1832,6232,5947,7145,6874,6301,2947,7126,5796,156,2860,6962,442,7022,6539,6159,2093,4643,6665,363,4994,2779,5090,5243,6801,1451,245,4845,197,2712,6061,7507,2300,1956,157,3778,4003,3365,849,371,2133,4007,4523,2875,7426,4538,3755,72,459,1592,2818,1934,5280,4593,6514,1693,4687,1521,98,7351,6890,1974,5219,2640,6817,1109,4261,1117,4591,7139,5197,932,3485,6443,3841,1520,1191,2064,415,3230,7084,1368,1836,1789,5095,165,5517,686,6692,1996,5991,3385,5617,6799,2680,5650,3651,1001,1950,464,1476,1716,229,7245,6256,7540,2484,4337,98,2868,2947,86,2407,4765,5788,2774,3968,3409,4396,2897,5896,2544,5920,2886,5659,7295,7540,10,7260,1009,5651,321,2464,638,5849,6092,4874,4522,1897,7362,5024,3460,6000,2490,6022,4718,1033,5275,4825,7519,6145,4399,142,169,6748,5675,5817,4231,5525,6716,3761,3282,1282,5390,1190,2221,5610,5214,2590,1705,4452,4892,4228,4496,3613,1501,991,6162,5284,4023,776,2041,4538,884,2140,3919,3127,3684,1884,2165,7017,4270,5605,290,755,312,3841,3670,7219,4099,6236,7125,3408,1115,3182,5657,3813,619,1916,3214,5230,1391,2901,721,5224,6548,6836,6308,2878,4610,1578,2998,2709,2008,7014,2396,543,5163,848,774,17,3274,3255,5993,398,5540,6160,428,3523,3891,6034,7078,2850,3998,6058,3748,4099,1657,1533,2949,3575,6374,3503,5574,1702,5061,2128,3774,1074,5531,2719,5888,1992,4178,5957,4053,763,2808,3388,5489,6660,1159,6901,4008,5349,3022,3628,1715,5293,5445,6497,5516,7416,3499,3128,5917,7528,6293,7538,2220,2657,4930,353,3901,5679,3753,5716,4481,7130,2981,4908,521,6215,776,5390,4136,87,5870,6585,7165,7118,33,5828,1292,5144,6658,7211,1662,2644,3716,5449,5255,4750,5887,3551,105,2083,6514,4569,6297,1885,789,2303,4356,6079,6052,3021,5356,7038,4009,1829,4763,7430,5126,682,3939,2185,6502,4075,495,1635,4325,6085,512,1341,7363,5887,1061,3211,6015,4560,4401,6759,2831,3796,7567,4916,4409,845,7316,7293,4548,4747,870,5827,2770,6316,2697,3141,355,460,1197,718,2343,6955,2339,1448,3565,3637,2868,3001,7516,323,3352,718,7171,3107,4087,7499,1229,1710,359,2002,5325,5101,6164,4553,6327,2318,4245,7046,6484,6724,6107,2740,6726,4061,729,1432,4122,5347,6727,2293,3420,5487,368,5074,34,3815,7401,5537,2162,4217,2375,5704,7041,5958,4807,44,2012,4566,2985,5633,685,46,6490,560,1243,5028,7119,29,5340,1482,4856,5668,2706,1241,3606,4600,4182,2713,789,5127,2655,4505,1359,2535,5710,4677,3202,3245,3334,6700,2982,4651,273,3765,2555,3364,6895,4989,6302,5219,739,3921,1705,1733,5015,5052,5146,3351,4766,7461,431,96,4183,5610,6129,6744,4062,7344,1575,6100,107,6613,6506,3140,4258,7090,2183,1664,2971,4860,2937,7361,3314,7416,6914,540,5126,4288,1833,2814,2065,3811,5414,6195,5900,825,3541,2153,16,1518,6396,7273,7396,2229,1319,917,7200,6669,2419,6839,3903,3030,65,4521,2699,2103,6591,4854,2745,1031,5861,6305,4467,7067,1853,416,5088,4578,5733,5593,3961,4464,7184,3051,2008,2795,5921,142,3295,2952,7170,1035,1482,80,595,3144,4369,1059,1344,4168,3245,6895,5899,3807,5643,6069,955,1163,5771,5815,6162,454,991,7356,5507,3882,3858,3744,1666,221,6845,4890,6199,5469,3703,3998,2695,2571,5488,5659,222,7304,6034,5368,1213,4852,5690,6756,27,231,4129,1835,7111,828,7157,6326,2545,2625,7557,5037,390,7436,1097,6000,1995,2761,413,4403,6576,4962,4722,5902,3405,92,4191,5371,289,7289,6332,5299,6917,1903,2245,6237,3771,1725,7400,513,4131,2286,3556,1042,7040,140,6154,1635,5869,4323,5963,269,6289,3337,5161,2334,2245,3959,746,6733,1635,7006,708,3506,1131,3676,7023,3985,6791,471,748,2545,5116,1629,279,7059,3334,36,7388,6298,6830,3479,473,1176,3375,5480,522,3983,3531,136,5316,1491,5021,863,2819,3853,3452,2796,2441,3981,7448,1122,1319,4968,3854,7264,3126,5500,5072,2408,218,6050,4432,4563,5714,1393,1172,2570,4045,7532,322,2881,6186,2152,101,4664,2756,1790,1080,7084,5940,2024,7313,1668,5543,7560,3650,5117,6935,5170,834,1848,47,3633,6708,1903,378,479,6668,2777,7013,1542,5033,3295,1784,7547,2841,4643,4191,2860,6851,3715,3723,884,7083,3420,1890,174,1933,786,2327,2293,6807,1880,4517,6923,7128,5267,3863,2343,3770,1123,3122,2450,6627,4170,1450,5790,5217,1499,3201,5367,3593,64,2544,6623,6743,4762,4791,910,1666,714,7248,533,5767,1328,2151,6673,6524,3108,7082,4989,4839,620,5702,4833,6903,6798,5827,6731,1336,3841,7357,2176,1736,1604,5430,679,7256,4441,7509,3335,4461,2910,7039,2507,361,1757,6880,7076,6062,2321,2869,3872,5380,7482,916,1286,4921,1601,2088,2298,2509,3289,7234,278,5025,6981,2976,3257,255,1099,6049,7286,4802,5469,4661,732,918,6276,1384,3880,1691,3057,4016,6687,291,5378,3795,4612,4066,7547,6260,6257,1290,230,4851,4528,2187,4205,4137,6725,4440,663,5209,646,4472,1251,7304,6630,1579,7458,4514,2941,54,7050,6546,5045,3264,3981,4137,2683,3588,616,1459,5819,5039,2864,2551,3306,2890,1885,4038,726,4662,6087,4045,5837,453,7497,4152,5373,4824,5252,3496,5587,1831,3393,6239,2424,469,1271,6132,596,301,4457,2055,477,5363,3548,1686,3596,3304,4964,5939,6082,7033,1563,4618,2137,3339,3099,4649,5126,6179,1197,420,6292,3225,3987,5527,5090,254,4160,7313,6072,3819,3402,2584,6661,55,1355,2297,2382,4104,5671,3297,6035,6637,4347,2585,5788,2489,7177,1861,3894,2984,7341,5960,54,1891,4803,4090,919,7428,3235,2713,5633,3577,3859,2981,4871,2156,4032,111,5185,816,4767,1089,180,6006,3382,361,7173,4239,1534,4228,5022,7498,17,1433,1956,5447,3527,6536,4512,7550,4988,2514,4605,3344,6788,4279,3991,3315,2223,5806,2039,2360,5589,1267,2825,2576,6693,4615,2730,142,7482,6540,5064,3018,3074,6628,647,4818,1995,7529,482,3548,1969,4774,6755,3712,3237,2638,822,1241,404,7402,2081,4226,3104,5926,5687,1100,6524,7017,741,4541,1408,4483,4548,1297,4767,2245,5249,7019,6304,1664,6938,2971,3606,2359,1580,4456,812,3612,6564,670,3554,7479,4738,4745,4305,6319,731,891,6145,4288,2181,74,6921,3936,2933,1146,1963,5607,5346,1355,5301,6722,6803,2445,6192,6786,2348,3890,1394,7061,2444,1330,6936,2159,7022,3531,6690,3733,1108,2348,4510,2577,4111,2995,6540,2753,2089,3820,7250,3270,2972,904,3145,3773,2641,5455,2772,2043,5845,260,7540,2484,2884,3528,4686,6179,2771,5786,4976,2968,3049,761,308,5582,5583,1808,6354,5840,6224,3262,1568,315,6273,4868,6771,3974,6021,6678,6768,1866,7474,513,1940,4449,4211,7267,7118,3192,1363,4543,1177,201,7337,893,1304,7125,5672,3293,2503,5292,3295,1663,4808,4274,2716,2608,3634,1762,7039,7212,5821,7516,7523,535,352,1526,7393,1956,5429,5213,3019,706,726,1029,94,5684,3866,5780,330,931,4871,1882,6630,5740,6145,5720,5435,6881,6088,1784,1557,4064,7176,3572,1339,4658,2059,6315,4926,2141,4396,4766,3473,5588,57,956,378,6055,7211,4175,2648,5432,4241,5627,7363,7347,3500,1072,3534,7268,7273,944,3164,1434,2369,6871,553,1169,1217,6190,1339,6192,5452,7080,2933,2847,5081,4490,5471,6318,4093,1826,3063,5775,3766,1615,5007,1421,4743,5366,4446,2529,102,3549,4577,2593,701,6785,1628,3703,4317,3509,5960,6416,3629,6258,4473,966,5906,5016,6696,518,4130,2777,6039,4042,7386,6254,6924,1570,2511,4873,2733,4942,3027,4964,6492,1509,6971,2252,707,3516,4988,6660,109,1335,5511,2733,3487,2190,1684,4114,5713,921,6776,3311,1505,1404,6960,5948,6022,4196,1604,1679,456,7561,180,1399,3311,939,1721,3752,2507,3702,2646,3386,4443,1242,459,1170,4772,5813,7064,2903,6406,2001,2915,3009,95,2339,16,5942,3837,1214,6737,147,4979,2634,4306,7140,6559,2458,1063,6271,4156,5997,1237,3064,5519,5956,4228,2781,5963,999,3756,1145,4375,2035,1727,3166,2098,4059,7073,1588,594,5159,2013,302,396,7520,6282,3768,3688,2888,37,7311,296,4624,3451,6627,522,5023,5959,7211,943,6780,3645,1373,1552,3417,3136,4321,5125,463,4725,1701,517,4514,1882,2236,6341,308,6918,5147,5660,167,5172,1250,7109,6575,6236,5641,1237,7267,4531,4117,5150,7428,6561,305,3456,3443,6566,7422,1720,6377,1025,4400,4959,3601,3210,3964,6631,6688,5401,5550,1366,3193,1469,1066,4531,4391,3774,5268,2023,6388,3462,4471,3508,4802,1866,6038,2945,941,5035,2047,639,2577,7221,4949,5523,6374,6068,4528,2021,1265,1179,793,5398,5895,2843,1559,3343,1816,354,2174,6445,1560,2601,706,6089,6272,4054,7535,3175,1541,4527,2070,6901,4725,4160,2214,4131,3725,1941,2190,3276,7069,3163,5063,6537,11,2476,879,1888,5605,2090,6777,6833,6725,6006,2970,4821,5333,2082,1144,6299,1619,1906,2402,4916,6516,202,5276,6330,2945,6436,710,3362,896,6114,1963,2943,5638,1022,5385,7579,3785,6782,6281,3686,2026,5113,6651,7096,7351,1694,7470,3501,1293,643,3440,2681,3151,1577,6153,1429,6669,3521,7181,1652,6064,2942,1439,526,419,3914,466,2830,2492,4050,6291,7043,6367,149,5754,4980,2794,7528,7408,1613,6985,921,3786,5868,560,2386,654,5659,621,4239,6552,3350,2871,6529,5396,6867,1264,1910,4844,3083,6451,2652,6955,7086,2670,5511,5344,3363,4343,2178,2624,3156,3580,4003,309,830,2998,2115,5408,6738,6880,5688,5183,5458,3722,5800,6921,5127,2286,533,2725,481,2972,661,1704,3383,1823,1526,4283,7580,487,2316,7465,1344,605,1445,3077,2819,586,1055,338,3440,7290,1616,2251,2000,2055,1435,3593,5330,4821,1056,938,4107,5392,7509,7524,5793,4824,1065,7035,1003,1146,1319,1646,3605,3612,7298,239,1170,5391,6064,2965,1174,5641,7109,1937,6729,1990,5159,3463,4113,3594,7142,3510,3235,998,5899,1939,2336,6240,5162,4036,2414,4875,7476,4555,6885,3721,1622,4273,5837,1659,6606,904,4977,3689,4103,392,3865,7383,3185,5189,22,4707,2081,1274,5006,3348,2202,6008,427,5606,2016,4501,2308,4272,1576,6518,3968,6339,6939,6569,6194,658,6100,3096,6700,2635,4141,660,3308,3394,792,6725,4061,3677,5138,3537,7323,5143,288,5733,1310,5454,5226,7559,879,539,5364,6050,7072,2918,4121,6930,1928,1005,457,5525,6279,325,1665,5546,5267,5665,837,3490,2723,4922,6066,274,577,3080,7153,1381,509,1581,147,5322,2702,1874,6152,6977,6801,2881,544,3866,3784,5220,354,298,7488,3204,7414,5645,5981,3212,3940,577,6994,4220,2320,3168,1101,421,4311,1017,3416,6555,1158,6621,6597,4435,3581,1916,4606,3941,4509,3149,6671,341,1506,1018,6964,2216,1395,1223,3551,6177,1333,6938,4451,4899,6629,6718,725,2327,563,2809,4311,4389,4612,394,3327,4180,4060,1144,3615,4841,6108,3985,4542,1429,5825,4407,4348,238,1407,1759,4997,2399,3033,3701,4313,3772,1947,4121,1601,966,3340,5566,4370,3170,7202,4998,2943,3338,4314,945,3540,7082,4854,4572,5968,7183,2082,3111,5193,1462,600,3231,1523,2047,2533,3048,4371,4156,7368,5850,966,3161,2149,1680,1973,5658,6427,3769,3709,1591,1634,1190,6165,890,5598,1907,1784,5138,6315,1178,3004,1347,6192,5032,3850,2051,4256,4838,6471,6205,7019,603,6646,393,523,3828,3148,148,2353,431,965,4927,1533,345,7413,3477,2201,4173,3638,1362,443,6405,7035,3426,3626,6533,4183,6011,2688,303,7138,4601,2142,6890,2421,3010,5839,5714,5296,2760,2969,7125,1944,1457,2100,2307,220,2700,3772,776,5145,6275,5053,828,7219,3435,1364,6685,1294,124,4278,4926,1897,3488,2355,2895,3750,4582,3232,6702,4419,3790,6717,1078,76,958,6794,699,1599,3152,1138,4064,5641,1235,7437,6281,2114,6947,4048,789,952,829,530,2299,5704,4701,458,5007,5172,4023,2356,5763,5852,3762,2033,2300,1962,3198,5598,2875,1482,6313,4959,4376,7075,4630,7234,2779,4085,1060,2657,4493,6201,7425,6839,3543,4614,214,5945,4591,4233,6654,4016,6260,7286,7250,7487,4438,1897,2906,2274,5202,691,2107,5997,2909,3144,876,6646,165,6193,4014,490,1264,3972,5546,3693,5843,1099,2888,6142,5080,1402,6328,4172,4368,3319,1156,7097,197,3903,6349,2580,208,5457,1562,7394,7245,6729,5092,4426,3945,1264,3591,1902,1840,4317,4397,2847,4469,6613,7195,7281,1476,4371,5490,6719,2317,4912,4867,4727,1468,1051,3952,1395,1364,882,3346,7495,3142,567,7452,5016,1907,5359,4513,6007,4221,3944,4434,477,2981,1128,1036,7293,557,7062,948,4402,6427,6035,5962,7017,339,3175,7281,3622,5440,2483,1271,4001,1809,6686,6867,1262,2959,2117,7135,4830,4354,3320,5927,197,5250,3738,1277,2883,4520,2769,2745,3497,2958,968,1381,6813,2923,850,516,2924,4688,2173,3657,265,2153,1544,3707,6178,5714,6690,515,1241,1349,5978,6274,2444,2333,3369,3747,889,3574,5461,5234,7031,4299,417,1438,4369,1962,3334,6389,3845,708,4048,7197,5452,1695,1267,4217,3415,3999,2067,5523,7169,1694,1894,5298,5120,1767,5151,2467,3257,6173,6109,1957,3513,1254,1343,5655,573,2830,4940,3721,4337,1286,6647,3355,1700,3428,2430,644,7001,4476,4829,2593,3327,5325,6526,2571,1547,4126,2330,285,4779,3457,247,5298,670,4094,4542,2268,4641,5752,1271,2288,671,6316,2633,6572,5489,1979,2995,6440,1020,3469,6807,2810,7103,2893,3849,5343,414,3129,6309,1882,7251,7226,3228,5305,3786,1356,5081,6488,2782,4345,6672,5425,601,7435,5314,316,4206,1028,1480,3118,3684,4076,2969,4418,1206,4913,6980,6600,6857,7279,3457,6304,2701,635,481,4443,6080,4361,7449,7585,2051,3038,422,3583,1388,6174,4486,1662,7559,2149,1473,2508,1463,6445,6446,3993,686,4679,1910,5492,4689,1149,6098,5043,239,4005,7262,202,5759,3171,3558,680,6079,5542,7448,111,1505,5328,3050,1733,4878,660,5662,626,1351,6370,138,5157,5117,6440,5845,1624,7101,4827,2573,2047,5900,6633,1309,1159,247,2624,6816,4073,5020,373,5531,1945,6602,6097,804,1402,1139,6759,2420,6972,3610,5272,7466,1631,846,153,2879,6254,3799,1918,5734,2709,3605,971,2400,2611,1681,5128,3571,1095,2238,2475,952,5080,6025,1944,1389,896,6946,5335,2778,6152,5029,6202,4700,4416,3138,4697,5994,2535,5971,4615,3633,3361,7453,5346,4802,907,1892,5839,1002,4573,2406,1281,1681,2143,4278,4044,1788,3887,6041,4457,4557,1943,1921,2804,7484,4616,3593,1661,2895,6397,5849,6430,6933,7236,3767,3855,2526,754,2109,2382,410,3886,4354,4537,384,3823,6554,6735,5606,7361,1567,198,6012,52,403,454,2234,6336,2020,4087,6084,5921,4365,4387,3665,1041,4527,2428,6582,1631,4875,5865,1016,6836,1891,2444,6756,5392,2143,4719,480,4835,7443,6673,5974,5950,3382,5570,5844,7511,1239,3414,4349,2013,7399,6229,2354,3854,2460,1842,1609,319,2446,5244,1065,3301,6211,907,1871,1437,2901,447,2271,1360,298,7302,5960,2386,4783,699,1354,1886,5148,7298,1065,5833,2821,2124,2529,7533,5617,294,443,5805,5064,3716,7535,39,4297,1846,2495,2731,818,6590,5224,4654,3556,1830,2783,5037,6359,5181,2783,1797,2157,6887,4248,5696,6339,4815,3231,1417,5534,1250,1424,4604,6995,4035,143,6530,7049,1116,3227,4587,2874,6429,2025,2425,1246,6933,2163,1601,3149,16,4873,4655,2899,3162,623,6585,4139,2449,2408,4657,6340,4263,5858,1117,3427,564,4415,4638,5725,5331,3346,3748,4503,6653,4711,6494,5274,6713,6785,865,7500,6572,3417,3605,2761,371,4423,4677,4966,7513,6761,1407,6704,662,6921,7579,4866,2376,208,3854,5767,5034,1841,2574,1736,6263,3096,256,2172,7088,5301,7137,5050,6531,407,2754,214,2840,2472,4253,2761,3161,5376,581,2248,202,5518,5828,7024,7279,1517,1350,3085,3584,7280,1843,2502,1919,1524,6624,5624,6435,4369,5636,4101,6028,5754,7006,1409,1559,3640,2273,2165,440,3980,4836,6872,7582,1992,5358,6698,6588,4869,7357,2143,1454,693,4239,2051,1804,3231,6378,685,3517,2666,6643,3141,232,3255,5491,5289,2738,6374,3373,2073,1190,3551,3627,6364,6318,4637,3554,3222,4096,3390,4655,2648,3403,4768,2543,2497,741,4271,2223,3997,3158,6117,5463,4180,7076,4401,3227,5916,423,2223,6135,3807,644,5990,1516,3656,6357,4820,17,2410,429,7277,4059,1873,1545,1497,4933,2746,535,3460,5608,4637,3039,4979,7557,2482,6214,5802,3403,319,5227,1323,2565,7062,6576,6041,2577,5766,7124,3259,5690,2747,6338,1321,5074,6188,489,4736,1804,2793,1857,6094,4839,4129,109,412,5780,165,4692,1990,2864,6340,2925,5436,2643,5621,220,4548,2748,4251,3406,980,4517,4655,3947,1352,4288,505,648,791,7544,6779,36,1428,7533,3972,4237,7221,6748,4077,6038,3426,609,2859,3122,5900,5094,5862,6580,6962,4969,1387,426,5695,4632,4849,6853,2275,778,3525,3065,4542,5879,4692,3386,2668,7014,4116,4718,5775,2496,3395,6298,4979,2338,1147,6354,3558,6471,2454,3653,895,160,7157,4535,5599,4290,607,5819,5288,5766,4197,6157,4640,5322,593,7156,5996,797,3686,7390,3831,7362,258,2749,1702,4229,5783,1794,6437,3459,2253,4295,3772,4506,3525,5507,3399,592,7074,1168,7503,6342,5177,2415,264,5594,5857,1928,6370,4943,1947,4961,3214,2560,3997,6457,6931,1304,6342,1250,4105,5520,4678,1611,5820,1288,3790,4550,1514,7169,364,4495,6105,3191,622,6818,5053,6087,448,2016,3776,168,7458,813,701,2460,3449,3394,2108,4666,7018,2909,3001,6441,5564,1927,2008,7083,4996,54,4794,1571,3091,3845,925,6263,4803,292,2047,193,2792,4993,3361,3615,1623,4925,3819,4870,6355,5813,2963,3721,6926,4897,1485,227,7275,3450,3202,771,3244,3711,2307,5605,4644,1952,6762,3576,7110,1147,7114,1774,7137,2111,5482,1316,6893,6785,953,2154,6591,4361,1005,1841,5398,3295,7355,2395,1669,5055,1756,1954,3597,413,4195,451,80,6890,3387,1045,2802,3013,3589,3248,2775,5547,4141,612,3944,6177,4911,2162,4739,3945,5918,6211,804,2274,6106,4611,5843,4418,1003,5379,6163,2260,3403,2115,754,5143,3653,3907,2847,4324,6965,6922,2098,5426,6381,388,3048,879,235,3723,4781,1604,5469,2081,5987,1256,3346,2899,6589,2663,2685,3887,5185,5854,3721,437,6143,3991,96,5244,6538,4085,3470,4148,5781,2222,3105,3665,3540,5465,7523,7370,5870,7419,2485,4546,3537,496,757,3823,6320,4322,2991,7324,7104,5306,2422,214,4999,3123,2477,6005,338,1174,7272,1929,980,1624,3334,260,29,368,6500,1280,7198,2495,1918,1025,3277,1602,6027,6331,2396,5871,1035,6256,217,1094,6092,3483,2275,6126,4786,7036,7025,4316,193,5854,964,4473,7550,670,7281,6629,5418,5988,4604,2265,3315,308,4498,6007,3667,1974,4384,3711,2136,3718,4960,6361,5435,318,7512,6882,508,1101,804,168,7431,2473,5062,4370,4160,5961,1328,5846,1432,606,1330,661,3006,4841,1932,415,3982,86,594,4028,6588,3762,6184,2458,6535,146,2076,1122,7141,7291,249,915,6870,1251,3829,513,2931,6673,2182,2961,5830,4247,1169,1500,6718,4631,2018,3102,4074,1024,6012,2874,6847,4564,6091,4880,7408,6913,4925,2688,5205,5367,6077,5507,2532,633,7160,3441,1431,6518,5724,1345,4207,582,5987,199,7398,6712,1830,3235,6926,1755,4317,6706,991,3653,1674,5872,5274,1631,4420,416,1846,5625,6608,1710,249,2447,3511,4011,5817,6430,6911,1526,6857,5304,733,6830,1537,3252,4781,5169,1656,4267,6894,1544,5183,576,6812,2636,1693,7450,7003,5670,508,5621,2376,1508,5770,6335,3363,1906,7499,121,1189,5815,6861,1695,6273,4821,4072,1299,2947,3709,1108,1138,3030,6370,167,1082,3551,2271,7144,937,6541,1529,6697,6050,3742,1601,2508,32,3532,6325,1603,2313,4104,6619,3297,1888,3184,3489,236,1014,3190,354,4517,7023,1354,2505,1670,5296,882,6733,209,2025,2906,5508,5285,4210,2540,1785,5537,6638,3399,6230,4188,1823,963,2786,4003,1111,3577,6192,3773,5507,562,4541,2062,3877,2181,751,5359,5743,5814,5117,3892,5594,6892,3905,3029,2919,4264,7004,3137,2321,1766,1782,6360,5927,1027,5149,3683,3737,226,7390,6468,1914,5222,2023,4355,1971,1337,4049,6801,7487,5110,16,5623,727,5721,7485,6639,4223,3304,5023,3987,6252,3837,6379,770,5243,3691,6268,1734,7368,987,1270,7450,4086,3700,2549,7164,903,3623,6019,758,1428,4405,737,4875,1547,4228,2726,1804,3896,2919,2731,5710,7356,4048,1851,525,7479,5716,2092,849,6870,5459,7462,1181,5723,2387,7565,814,4022,1198,4723,5631,5152,1309,4876,1358,1175,2213,6219,4607,1305,2994,136,5035,7368,3611,2556,2797,1741,7233,2507,4739,3966,6574,2270,971,5969,3759,5429,4053,3137,3198,3148,2841,332,4844,1588,383,2299,2792,3843,4868,4312,6899,3603,6725,4284,1004,1124,6249,155,3654,728,5750,991,2066,3737,4341,2057,4072,3542,1181,7101,4119,6312,182,606,3558,169,680,6375,4990,2303,2368,1583,619,562,5287,4488,6901,2455,4282,5309,2218,4047,4327,6214,4621,2487,985,4782,5427,2407,3425,6857,5646,6283,2253,1172,4775,977,3778,3406,493,4698,4444,4639,4774,4857,1911,2925,3757,5556,4865,3797,3782,2262,2586,4573,2815,7530,1047,1568,5544,3077,4399,4608,5022,6750,1341,1905,85,6824,2192,4929,4970,6484,6829,2976,393,7360,778,2492,6368,234,6738,2951,6496,4500,5663,1012,3912,213,5611,1686,745,951,5995,1532,5741,4716,1655,4946,209,3937,536,5302,1727,1621,5676,4457,1264,6697,696,2619,752,2853,3268,4364,2778,3961,3463,2890,6424,1258,6168,1788,3355,3576,1629,4975,4020,6299,6909,725,2746,3713,3613,3199,3964,7411,5898,521,6470,4907,982,3089,1098,4847,6167,6002,1922,1529,7285,2969,5953,6727,3746,1816,618,1384,2979,5824,2794,3125,6615,4881,3578,6370,3510,4694,7426,2052,4028,865,2495,364,2579,4741,3086,4267,471,7388,1778,689,5905,7481,4127,3856,1910,792,3842,6485,3861,2636,3664,946,4123,4423,2503,3608,2331,6367,6421,4162,1172,9,6807,4564,3394,7093,7404,5539,4182,2163,3853,3999,1793,4590,5332,6092,6114,6787,7553,1434,2145,5597,3591,5,1554,4692,5855,5662,5731,2598,6263,98,3366,5423,6976,2559,7165,472,377,1530,4183,6694,6084,1416,4445,4714,5540,5968,4290,4922,4514,3253,5182,3803,5417,6642,301,1909,1310,2313,841,7431,2896,970,5682,4621,734,4534,3236,1790,5365,6712,2172,129,2799,1708,1065,749,6352,3321,3572,3281,83,7435,1048,3507,5260,6502,6965,4367,3277,6322,1634,4948,2872,6611,6190,2535,5433,7541,7554,2407,1635,7008,3959,1649,1645,4512,936,1913,2511,6650,5611,7334,5718,873,5507,1165,6858,2326,700,499,4608,7017,3029,4389,1161,4626,3575,2173,855,691,6080,4808,3066,2723,7520,2725,2848,1569,769,3288,4181,5103,3018,4271,7216,648,5899,4795,6329,3335,2602,3441,7165,6928,1541,1304,3363,6146,3346,3897,2589,4923,6738,3980,2279,3329,5639,5914,29,5208,614,1354,5868,1348,7402,4759,3100,3721,978,3410,1516,5140,3106,4125,3049,4280,2778,2632,2813,6371,4705,2012,1059,1686,6592,6032,1293,5396,6354,4845,6711,6192,6490,6,3328,5011,2716,6225,922,7205,5812,6472,1906,5313,2361,1906,7245,6728,1082,3182,964,2351,2668,1652,4049,3649,470,2883,1620,3733,3770,6114,3925,2206,311,5804,3631,377,3432,4543,260,6528,2234,363,1413,527,505,6836,1825,6764,4192,6387,2386,625,2034,1652,7269,2035,4946,1461,4410,4240,105,6023,1863,4896,3451,6083,3991,6915,2943,2957,612,4101,5032,4025,6046,6785,2314,5437,7467,1380,6318,4562,4752,7399,3426,842,4573,6279,4217,2731,1834,4171,6639,6450,1326,793,3399,4040,4108,1507,4460,2931,6000,2998,96,2445,5864,4940,5339,794,5008,819,3790,929,1977,5913,6498,4871,2636,5543,6582,1660,3063,957,3120,3686,4626,1499,2584,5865,1244,1246,7510,6926,4701,2345,3531,2252,5313,376,7268,5693,3150,6417,2585,2131,3137,646,3914,1499,6929,3592,3144,1399,3841,2614,5033,5815,1557,2440,3178,3374,2653,4547,1144,5801,1611,3747,307,5111,901,6329,3242,1486,185,339,7060,3170,7014,389,6432,5534,1322,7361,3829,638,4199,5654,7223,5181,2635,2309,5966,6459,5174,6364,6153,2953,765,3016,6775,4369,6293,2381,5252,5795,6430,6072,551,7517,6007,575,6451,3378,6913,1640,5455,5709,6983,5253,4877,1882,6777,2403,5916,592,798,2976,2681,2719,6481,5261,2216,2650,2882,2846,6359,2022,2609,1598,2218,5554,3598,2244,3984,6478,3155,7436,7065,1605,5551,6994,4336,1298,6702,493,2923,7409,7082,4879,3666,4952,3390,5172,2598,845,710,145,577,204,7365,2687,7224,5508,2712,4161,3200,4894,5784,2268,5642,6752,3654,4873,2688,3810,6137,5827,3266,4248,6612,3830,813,6328,2008,3302,6653,2473,193,7018,3317,2869,1010,7421,6427,3689,1197,5196,3370,605,2471,3147,797,3715,444,824,5292,5934,862,5553,1517,1242,3910,5794,5911,7227,505,943,5871,5982,3357,7017,3275,97,5074,2414,3602,1768,6452,3826,2967,1092,4785,4244,7488,5190,683,5010,3955,5621,5388,4412,4008,4407,3155,3149,1455,1190,3759,7553,5293,3682,955,1399,1255,5407,2008,37,4989,2293,1574,6311,7253,5703,5130,6330,7427,3702,3172,2694,1059,1861,278,4719,1247,2345,6662,2289,2669,1990,1697,453,302,1223,1938,189,4526,4196,6345,4219,3938,5907,6331,2742,6955,2826,2944,3180,4396,2096,3504,3594,1695,3544,4961,6726,3509,3449,6866,1716,4956,293,1771,3446,4072,3917,1507,4310,2546,1322,2529,1736,2430,1965,7082,286,5129,1082,4560,5454,793,6444,7196,6734,5144,2524,1133,5845,6932,7274,6652,2403,1662,6436,3508,1949,4555,6787,5107,7151,6995,2801,1920,7196,1163,5317,2992,4112,5432,5797,6636,4207,6783,4782,5081,5531,6167,7214,2062,4714,3920,4383,248,4472,7338,558,1742,1519,6759,7585,6467,5097,3175,906,7143,6982,2884,6662,7562,1189,1594,1453,4718,5826,2770,1087,2906,1563,668,5883,5784,3681,7428,5862,7535,6172,7519,3515,2887,3577,5417,6344,2200,2284,1008,3563,7418,2459,5849,1158,4068,1423,1644,1519,1812,5456,3640,6470,2257,3832,4497,4966,6880,3326,1311,3967,4095,904,455,3041,5149,1910,5170,4418,2026,328,4494,3128,1270,5117,3501,2115,7275,7349,7428,5781,2958,1880,3572,5976,3631,2753,5206,5299,4306,6405,4679,7151,6166,5668,6520,1596,1400,5499,2882,2326,6094,1641,3893,552,2942,3957,2923,7378,730,4901,4257,2039,2777,6030,5647,3225,6657,187,1240,2715,6335,1038,2739,692,3918]

print("Bubble Sort")
array = ARRAY
tic = datetime.now()
bubbleSort(array)
toc = datetime.now()
print("Time: %s"%(toc - tic))

print("Selection Sort")
array = ARRAY
tic = datetime.now()
selectionSort(array)
toc = datetime.now()
print("Time: %s"%(toc - tic))