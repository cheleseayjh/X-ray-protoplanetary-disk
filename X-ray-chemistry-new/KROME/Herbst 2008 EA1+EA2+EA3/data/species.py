#This file is a script to initialize the species indexes for gnuplot


#if(!exists("nkrome")) print "ERROR: first set the value of the column-offset nkrome"
nkrome = 0
krome_idx_E = 1 + nkrome
krome_idx_GRAINk = 2 + nkrome
krome_idx_Hk = 3 + nkrome
krome_idx_Ck = 4 + nkrome
krome_idx_CNk = 5 + nkrome
krome_idx_Ok = 6 + nkrome
krome_idx_OHk = 7 + nkrome
krome_idx_Sk = 8 + nkrome
krome_idx_GRAIN0 = 9 + nkrome
krome_idx_C = 10 + nkrome
krome_idx_FE = 11 + nkrome
krome_idx_H = 12 + nkrome
krome_idx_HE = 13 + nkrome
krome_idx_MG = 14 + nkrome
krome_idx_N = 15 + nkrome
krome_idx_NA = 16 + nkrome
krome_idx_O = 17 + nkrome
krome_idx_S = 18 + nkrome
krome_idx_SI = 19 + nkrome
krome_idx_H2 = 20 + nkrome
krome_idx_CO = 21 + nkrome
krome_idx_CL = 22 + nkrome
krome_idx_P = 23 + nkrome
krome_idx_C2 = 24 + nkrome
krome_idx_CCL = 25 + nkrome
krome_idx_CH = 26 + nkrome
krome_idx_CLO = 27 + nkrome
krome_idx_CN = 28 + nkrome
krome_idx_CP = 29 + nkrome
krome_idx_CS = 30 + nkrome
krome_idx_HCL = 31 + nkrome
krome_idx_HF = 32 + nkrome
krome_idx_F = 33 + nkrome
krome_idx_HS = 34 + nkrome
krome_idx_MGH = 35 + nkrome
krome_idx_N2 = 36 + nkrome
krome_idx_NAH = 37 + nkrome
krome_idx_NH = 38 + nkrome
krome_idx_NO = 39 + nkrome
krome_idx_NS = 40 + nkrome
krome_idx_O2 = 41 + nkrome
krome_idx_OH = 42 + nkrome
krome_idx_PH = 43 + nkrome
krome_idx_PN = 44 + nkrome
krome_idx_PO = 45 + nkrome
krome_idx_S2 = 46 + nkrome
krome_idx_SIC = 47 + nkrome
krome_idx_SIH = 48 + nkrome
krome_idx_SIN = 49 + nkrome
krome_idx_SIO = 50 + nkrome
krome_idx_SIS = 51 + nkrome
krome_idx_SO = 52 + nkrome
krome_idx_C2H = 53 + nkrome
krome_idx_C2N = 54 + nkrome
krome_idx_C2S = 55 + nkrome
krome_idx_C3 = 56 + nkrome
krome_idx_CCO = 57 + nkrome
krome_idx_CCP = 58 + nkrome
krome_idx_CH2 = 59 + nkrome
krome_idx_CO2 = 60 + nkrome
krome_idx_H2O = 61 + nkrome
krome_idx_H2S = 62 + nkrome
krome_idx_HCN = 63 + nkrome
krome_idx_HCO = 64 + nkrome
krome_idx_HCP = 65 + nkrome
krome_idx_HCS = 66 + nkrome
krome_idx_HCSI = 67 + nkrome
krome_idx_HNC = 68 + nkrome
krome_idx_HNO = 69 + nkrome
krome_idx_HNSI = 70 + nkrome
krome_idx_HPO = 71 + nkrome
krome_idx_HS2 = 72 + nkrome
krome_idx_N2O = 73 + nkrome
krome_idx_NAOH = 74 + nkrome
krome_idx_NH2 = 75 + nkrome
krome_idx_NO2 = 76 + nkrome
krome_idx_O2H = 77 + nkrome
krome_idx_OCN = 78 + nkrome
krome_idx_OCS = 79 + nkrome
krome_idx_PH2 = 80 + nkrome
krome_idx_SIC2 = 81 + nkrome
krome_idx_SIH2 = 82 + nkrome
krome_idx_SINC = 83 + nkrome
krome_idx_SIO2 = 84 + nkrome
krome_idx_SO2 = 85 + nkrome
krome_idx_C2H2 = 86 + nkrome
krome_idx_C3H = 87 + nkrome
krome_idx_HC3 = 88 + nkrome
krome_idx_C3N = 89 + nkrome
krome_idx_C3O = 90 + nkrome
krome_idx_C3P = 91 + nkrome
krome_idx_C3S = 92 + nkrome
krome_idx_C4 = 93 + nkrome
krome_idx_CH3 = 94 + nkrome
krome_idx_H2CO = 95 + nkrome
krome_idx_H2CS = 96 + nkrome
krome_idx_H2O2 = 97 + nkrome
krome_idx_H2S2 = 98 + nkrome
krome_idx_H2SIO = 99 + nkrome
krome_idx_HCCP = 100 + nkrome
krome_idx_NH3 = 101 + nkrome
krome_idx_SIC2H = 102 + nkrome
krome_idx_SIC3 = 103 + nkrome
krome_idx_SICH2 = 104 + nkrome
krome_idx_SIH3 = 105 + nkrome
krome_idx_C2H2N = 106 + nkrome
krome_idx_C2H2O = 107 + nkrome
krome_idx_C2H3 = 108 + nkrome
krome_idx_C3H2 = 109 + nkrome
krome_idx_H2C3 = 110 + nkrome
krome_idx_C4H = 111 + nkrome
krome_idx_C4N = 112 + nkrome
krome_idx_C4P = 113 + nkrome
krome_idx_C4S = 114 + nkrome
krome_idx_C5 = 115 + nkrome
krome_idx_CH2O2 = 116 + nkrome
krome_idx_CH2PH = 117 + nkrome
krome_idx_CH3N = 118 + nkrome
krome_idx_CH4 = 119 + nkrome
krome_idx_HC3N = 120 + nkrome
krome_idx_SIC2H2 = 121 + nkrome
krome_idx_SIC3H = 122 + nkrome
krome_idx_SIC4 = 123 + nkrome
krome_idx_SICH3 = 124 + nkrome
krome_idx_SIH4 = 125 + nkrome
krome_idx_C2H3N = 126 + nkrome
krome_idx_C2H4 = 127 + nkrome
krome_idx_C3H3 = 128 + nkrome
krome_idx_C4H2 = 129 + nkrome
krome_idx_C5H = 130 + nkrome
krome_idx_C5N = 131 + nkrome
krome_idx_C6 = 132 + nkrome
krome_idx_CH4O = 133 + nkrome
krome_idx_C2H4O = 134 + nkrome
krome_idx_C2H5 = 135 + nkrome
krome_idx_C3H3N = 136 + nkrome
krome_idx_C3H4 = 137 + nkrome
krome_idx_C5H2 = 138 + nkrome
krome_idx_C6H = 139 + nkrome
krome_idx_C7 = 140 + nkrome
krome_idx_CH5N = 141 + nkrome
krome_idx_HC5N = 142 + nkrome
krome_idx_C6H2 = 143 + nkrome
krome_idx_C7H = 144 + nkrome
krome_idx_C7N = 145 + nkrome
krome_idx_C8 = 146 + nkrome
krome_idx_CH3C3N = 147 + nkrome
krome_idx_HCOOCH3 = 148 + nkrome
krome_idx_C2H5OH = 149 + nkrome
krome_idx_C7H2 = 150 + nkrome
krome_idx_C8H = 151 + nkrome
krome_idx_C9 = 152 + nkrome
krome_idx_CH3C4H = 153 + nkrome
krome_idx_CH3OCH3 = 154 + nkrome
krome_idx_HC7N = 155 + nkrome
krome_idx_C2H6CO = 156 + nkrome
krome_idx_C8H2 = 157 + nkrome
krome_idx_C9H = 158 + nkrome
krome_idx_C9N = 159 + nkrome
krome_idx_CH3C5N = 160 + nkrome
krome_idx_C9H2 = 161 + nkrome
krome_idx_CH3C6H = 162 + nkrome
krome_idx_CH3C7N = 163 + nkrome
krome_idx_HC9N = 164 + nkrome
krome_idx_HCNC2 = 165 + nkrome
krome_idx_HC2NC = 166 + nkrome
krome_idx_HNC3 = 167 + nkrome
krome_idx_NH2CHO = 168 + nkrome
krome_idx_C4H3 = 169 + nkrome
krome_idx_NH2CN = 170 + nkrome
krome_idx_C6H6 = 171 + nkrome
krome_idx_H2CN = 172 + nkrome
krome_idx_C10 = 173 + nkrome
krome_idx_C11 = 174 + nkrome
krome_idx_SIC3H3 = 175 + nkrome
krome_idx_SIC4H = 176 + nkrome
krome_idx_SIC6H = 177 + nkrome
krome_idx_SIC8H = 178 + nkrome
krome_idx_SIC2H3 = 179 + nkrome
krome_idx_C3H6 = 180 + nkrome
krome_idx_SIC3H5 = 181 + nkrome
krome_idx_C4H4 = 182 + nkrome
krome_idx_C4H6 = 183 + nkrome
krome_idx_HC4N = 184 + nkrome
krome_idx_HC6N = 185 + nkrome
krome_idx_HC8N = 186 + nkrome
krome_idx_HC10N = 187 + nkrome
krome_idx_HC11N = 188 + nkrome
krome_idx_HC12N = 189 + nkrome
krome_idx_NC4N = 190 + nkrome
krome_idx_NC6N = 191 + nkrome
krome_idx_NC8N = 192 + nkrome
krome_idx_NC10N = 193 + nkrome
krome_idx_NC12N = 194 + nkrome
krome_idx_HC13N = 195 + nkrome
krome_idx_Cj = 196 + nkrome
krome_idx_FEj = 197 + nkrome
krome_idx_Hj = 198 + nkrome
krome_idx_HEj = 199 + nkrome
krome_idx_MGj = 200 + nkrome
krome_idx_Nj = 201 + nkrome
krome_idx_NAj = 202 + nkrome
krome_idx_Oj = 203 + nkrome
krome_idx_Sj = 204 + nkrome
krome_idx_SIj = 205 + nkrome
krome_idx_H3j = 206 + nkrome
krome_idx_HCOj = 207 + nkrome
krome_idx_CLj = 208 + nkrome
krome_idx_Pj = 209 + nkrome
krome_idx_COj = 210 + nkrome
krome_idx_H2j = 211 + nkrome
krome_idx_NOj = 212 + nkrome
krome_idx_O2j = 213 + nkrome
krome_idx_CH2j = 214 + nkrome
krome_idx_H2Sj = 215 + nkrome
krome_idx_HCSj = 216 + nkrome
krome_idx_HNOj = 217 + nkrome
krome_idx_NH2j = 218 + nkrome
krome_idx_OCSj = 219 + nkrome
krome_idx_C2H2j = 220 + nkrome
krome_idx_CH3j = 221 + nkrome
krome_idx_NH3j = 222 + nkrome
krome_idx_C2H2Oj = 223 + nkrome
krome_idx_CH2O2j = 224 + nkrome
krome_idx_C2H3Nj = 225 + nkrome
krome_idx_C2H4j = 226 + nkrome
krome_idx_C4H2j = 227 + nkrome
krome_idx_H3COj = 228 + nkrome
krome_idx_CH4Oj = 229 + nkrome
krome_idx_C2H4Oj = 230 + nkrome
krome_idx_C3H4j = 231 + nkrome
krome_idx_CH5Nj = 232 + nkrome
krome_idx_C2H5OHj = 233 + nkrome
krome_idx_CH3OCH3j = 234 + nkrome
krome_idx_CHj = 235 + nkrome
krome_idx_CCLj = 236 + nkrome
krome_idx_C2j = 237 + nkrome
krome_idx_CLOj = 238 + nkrome
krome_idx_CPj = 239 + nkrome
krome_idx_CFj = 240 + nkrome
krome_idx_CSj = 241 + nkrome
krome_idx_CNj = 242 + nkrome
krome_idx_NSj = 243 + nkrome
krome_idx_PHj = 244 + nkrome
krome_idx_POj = 245 + nkrome
krome_idx_SICj = 246 + nkrome
krome_idx_SINj = 247 + nkrome
krome_idx_SISj = 248 + nkrome
krome_idx_SOj = 249 + nkrome
krome_idx_C3j = 250 + nkrome
krome_idx_C2Sj = 251 + nkrome
krome_idx_C2Oj = 252 + nkrome
krome_idx_CCPj = 253 + nkrome
krome_idx_C2Hj = 254 + nkrome
krome_idx_HOCj = 255 + nkrome
krome_idx_C2Nj = 256 + nkrome
krome_idx_CNCj = 257 + nkrome
krome_idx_HCPj = 258 + nkrome
krome_idx_SIC2j = 259 + nkrome
krome_idx_SINCj = 260 + nkrome
krome_idx_HPOj = 261 + nkrome
krome_idx_HCNj = 262 + nkrome
krome_idx_CHSIj = 263 + nkrome
krome_idx_SIH2j = 264 + nkrome
krome_idx_C3Hj = 265 + nkrome
krome_idx_C4j = 266 + nkrome
krome_idx_C3Oj = 267 + nkrome
krome_idx_C3Sj = 268 + nkrome
krome_idx_H2COj = 269 + nkrome
krome_idx_H2SIOj = 270 + nkrome
krome_idx_HCNHj = 271 + nkrome
krome_idx_SIC2Hj = 272 + nkrome
krome_idx_SIC3j = 273 + nkrome
krome_idx_CH2SIj = 274 + nkrome
krome_idx_SIH3j = 275 + nkrome
krome_idx_C2H2Nj = 276 + nkrome
krome_idx_C2H3j = 277 + nkrome
krome_idx_C3H2j = 278 + nkrome
krome_idx_H2C3j = 279 + nkrome
krome_idx_C4Hj = 280 + nkrome
krome_idx_C5j = 281 + nkrome
krome_idx_C4Sj = 282 + nkrome
krome_idx_PC2Hj = 283 + nkrome
krome_idx_C3Nj = 284 + nkrome
krome_idx_C4Nj = 285 + nkrome
krome_idx_C3HNj = 286 + nkrome
krome_idx_HNCj = 287 + nkrome
krome_idx_SIC3Hj = 288 + nkrome
krome_idx_SIC4j = 289 + nkrome
krome_idx_SIC2H2j = 290 + nkrome
krome_idx_SICH3j = 291 + nkrome
krome_idx_HC2NCHj = 292 + nkrome
krome_idx_C3H3j = 293 + nkrome
krome_idx_H3C3j = 294 + nkrome
krome_idx_C5Hj = 295 + nkrome
krome_idx_C6j = 296 + nkrome
krome_idx_C2H3Oj = 297 + nkrome
krome_idx_C2H5j = 298 + nkrome
krome_idx_C3H3Nj = 299 + nkrome
krome_idx_C5H2j = 300 + nkrome
krome_idx_C4H3j = 301 + nkrome
krome_idx_C6Hj = 302 + nkrome
krome_idx_C7j = 303 + nkrome
krome_idx_CH4Nj = 304 + nkrome
krome_idx_C5HNj = 305 + nkrome
krome_idx_C7Hj = 306 + nkrome
krome_idx_C8j = 307 + nkrome
krome_idx_COOCH4j = 308 + nkrome
krome_idx_C2H5Oj = 309 + nkrome
krome_idx_C8Hj = 310 + nkrome
krome_idx_C9j = 311 + nkrome
krome_idx_C5H3j = 312 + nkrome
krome_idx_C6H2j = 313 + nkrome
krome_idx_C6H3j = 314 + nkrome
krome_idx_C2H6COj = 315 + nkrome
krome_idx_C9Hj = 316 + nkrome
krome_idx_C10j = 317 + nkrome
krome_idx_C7H3j = 318 + nkrome
krome_idx_C8H2j = 319 + nkrome
krome_idx_C8H3j = 320 + nkrome
krome_idx_HCLj = 321 + nkrome
krome_idx_Fj = 322 + nkrome
krome_idx_HFj = 323 + nkrome
krome_idx_HSj = 324 + nkrome
krome_idx_NHj = 325 + nkrome
krome_idx_OHj = 326 + nkrome
krome_idx_PNj = 327 + nkrome
krome_idx_S2j = 328 + nkrome
krome_idx_SIHj = 329 + nkrome
krome_idx_SIOj = 330 + nkrome
krome_idx_H2Oj = 331 + nkrome
krome_idx_HNSIj = 332 + nkrome
krome_idx_S2Hj = 333 + nkrome
krome_idx_PH2j = 334 + nkrome
krome_idx_H2CSj = 335 + nkrome
krome_idx_H2S2j = 336 + nkrome
krome_idx_HSIOj = 337 + nkrome
krome_idx_C4Pj = 338 + nkrome
krome_idx_HCO2j = 339 + nkrome
krome_idx_PCH3j = 340 + nkrome
krome_idx_CH4j = 341 + nkrome
krome_idx_C2NHj = 342 + nkrome
krome_idx_SIH4j = 343 + nkrome
krome_idx_NH4j = 344 + nkrome
krome_idx_H2NCj = 345 + nkrome
krome_idx_C3H2Nj = 346 + nkrome
krome_idx_C7H2j = 347 + nkrome
krome_idx_C5H4j = 348 + nkrome
krome_idx_C7HNj = 349 + nkrome
krome_idx_C9H2j = 350 + nkrome
krome_idx_C7H4j = 351 + nkrome
krome_idx_C9HNj = 352 + nkrome
krome_idx_N2j = 353 + nkrome
krome_idx_CO2j = 354 + nkrome
krome_idx_HEHj = 355 + nkrome
krome_idx_SO2j = 356 + nkrome
krome_idx_C6H5j = 357 + nkrome
krome_idx_C5H5j = 358 + nkrome
krome_idx_N2Hj = 359 + nkrome
krome_idx_NO2j = 360 + nkrome
krome_idx_PC2H2j = 361 + nkrome
krome_idx_PNH2j = 362 + nkrome
krome_idx_PCH2j = 363 + nkrome
krome_idx_HC2Sj = 364 + nkrome
krome_idx_HC3Sj = 365 + nkrome
krome_idx_H3CSj = 366 + nkrome
krome_idx_HC4Sj = 367 + nkrome
krome_idx_SIFj = 368 + nkrome
krome_idx_SINH2j = 369 + nkrome
krome_idx_SIC2H3j = 370 + nkrome
krome_idx_SIC3H2j = 371 + nkrome
krome_idx_C2HOj = 372 + nkrome
krome_idx_H3Oj = 373 + nkrome
krome_idx_H3Sj = 374 + nkrome
krome_idx_HOCSj = 375 + nkrome
krome_idx_CH5Oj = 376 + nkrome
krome_idx_NCOj = 377 + nkrome
krome_idx_HNCOj = 378 + nkrome
krome_idx_C2N2j = 379 + nkrome
krome_idx_O2Hj = 380 + nkrome
krome_idx_CH5j = 381 + nkrome
krome_idx_H2CLj = 382 + nkrome
krome_idx_H2Fj = 383 + nkrome
krome_idx_CH3O2j = 384 + nkrome
krome_idx_H2POj = 385 + nkrome
krome_idx_PNH3j = 386 + nkrome
krome_idx_PCH4j = 387 + nkrome
krome_idx_PC2H3j = 388 + nkrome
krome_idx_HSISj = 389 + nkrome
krome_idx_HSOj = 390 + nkrome
krome_idx_HNSj = 391 + nkrome
krome_idx_HPNj = 392 + nkrome
krome_idx_H2NOj = 393 + nkrome
krome_idx_NAH2Oj = 394 + nkrome
krome_idx_PH3j = 395 + nkrome
krome_idx_SINCHj = 396 + nkrome
krome_idx_HSIO2j = 397 + nkrome
krome_idx_HSO2j = 398 + nkrome
krome_idx_HC3Oj = 399 + nkrome
krome_idx_PC3Hj = 400 + nkrome
krome_idx_H3S2j = 401 + nkrome
krome_idx_H3SIOj = 402 + nkrome
krome_idx_PC4Hj = 403 + nkrome
krome_idx_NH2CNHj = 404 + nkrome
krome_idx_SIC4Hj = 405 + nkrome
krome_idx_SICH4j = 406 + nkrome
krome_idx_SIH5j = 407 + nkrome
krome_idx_C2H4Nj = 408 + nkrome
krome_idx_NH2CH2Oj = 409 + nkrome
krome_idx_C2H6j = 410 + nkrome
krome_idx_C3H4Nj = 411 + nkrome
krome_idx_C3H5j = 412 + nkrome
krome_idx_C4H4j = 413 + nkrome
krome_idx_CH6Nj = 414 + nkrome
krome_idx_C5H2Nj = 415 + nkrome
krome_idx_C4H4Nj = 416 + nkrome
krome_idx_H5C2O2j = 417 + nkrome
krome_idx_C2H5OH2j = 418 + nkrome
krome_idx_CH3OCH4j = 419 + nkrome
krome_idx_C7H2Nj = 420 + nkrome
krome_idx_C3H6OHj = 421 + nkrome
krome_idx_C6H4Nj = 422 + nkrome
krome_idx_C9H3j = 423 + nkrome
krome_idx_C7H5j = 424 + nkrome
krome_idx_C8H4Nj = 425 + nkrome
krome_idx_C9H2Nj = 426 + nkrome
krome_idx_C6H7j = 427 + nkrome
krome_idx_NAH2j = 428 + nkrome
krome_idx_PC2H4j = 429 + nkrome
krome_idx_C4H5j = 430 + nkrome
krome_idx_H2CCLj = 431 + nkrome
krome_idx_PC4H2j = 432 + nkrome
krome_idx_C6H4j = 433 + nkrome
krome_idx_C8H4j = 434 + nkrome
krome_idx_C9H4j = 435 + nkrome
krome_idx_C4H7j = 436 + nkrome
krome_idx_HC4Nj = 437 + nkrome
krome_idx_HC4Oj = 438 + nkrome
krome_idx_C5Nj = 439 + nkrome
krome_idx_H2C4Nj = 440 + nkrome
krome_idx_H3C4Nj = 441 + nkrome
krome_idx_C7Nj = 442 + nkrome
krome_idx_C5H3Nj = 443 + nkrome
krome_idx_C9Nj = 444 + nkrome
krome_idx_C7H3Nj = 445 + nkrome
krome_idx_C9H3Nj = 446 + nkrome
krome_idx_OCSjH2 = 447 + nkrome
krome_idx_H2C3Oj = 448 + nkrome
krome_idx_H3C3Oj = 449 + nkrome
krome_idx_C5H4Nj = 450 + nkrome
krome_idx_C8H5j = 451 + nkrome
krome_idx_C9H5j = 452 + nkrome
krome_idx_HEjj = 453 + nkrome
krome_idx_dust_C_1 = 454 + nkrome
krome_idx_dust_C_2 = 455 + nkrome
krome_idx_dust_C_3 = 456 + nkrome
krome_idx_dust_C_4 = 457 + nkrome
krome_idx_dust_C_5 = 458 + nkrome
krome_idx_dust_C_6 = 459 + nkrome
krome_idx_dust_C_7 = 460 + nkrome
krome_idx_dust_C_8 = 461 + nkrome
krome_idx_dust_C_9 = 462 + nkrome
krome_idx_dust_C_10 = 463 + nkrome
krome_idx_dust_Si_1 = 464 + nkrome
krome_idx_dust_Si_2 = 465 + nkrome
krome_idx_dust_Si_3 = 466 + nkrome
krome_idx_dust_Si_4 = 467 + nkrome
krome_idx_dust_Si_5 = 468 + nkrome
krome_idx_dust_Si_6 = 469 + nkrome
krome_idx_dust_Si_7 = 470 + nkrome
krome_idx_dust_Si_8 = 471 + nkrome
krome_idx_dust_Si_9 = 472 + nkrome
krome_idx_dust_Si_10 = 473 + nkrome
krome_idx_CR = 474 + nkrome
krome_idx_g = 475 + nkrome
krome_idx_Tgas = 476 + nkrome
krome_idx_dummy = 477 + nkrome
print("All variables set as e.g. krome_idx_H2")
print("plot 'your_output' u 1:krome_idx_H2")
print(" the offset is nkrome=",nkrome)
