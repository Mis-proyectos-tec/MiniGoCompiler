# Generated from C:/Users/Ismael/Documents/Semestres/V semestre/Compiladores e interpretes/Proyecto final/MiniGoCompiler/MiniGo.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,73,480,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,1,0,1,0,1,0,1,
        0,1,0,1,0,1,1,1,1,1,1,5,1,100,8,1,10,1,12,1,103,9,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,112,8,2,1,2,1,2,3,2,116,8,2,1,3,1,3,1,3,1,3,
        1,3,5,3,123,8,3,10,3,12,3,126,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,3,4,138,8,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,
        6,150,8,6,1,6,1,6,3,6,154,8,6,1,7,1,7,1,7,1,7,1,7,5,7,161,8,7,10,
        7,12,7,164,9,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,3,
        10,177,8,10,1,10,1,10,3,10,181,8,10,1,11,1,11,1,11,5,11,186,8,11,
        10,11,12,11,189,9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,
        199,8,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,
        1,15,3,15,213,8,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,5,16,222,8,
        16,10,16,12,16,225,9,16,1,17,1,17,1,17,5,17,230,8,17,10,17,12,17,
        233,9,17,1,18,1,18,1,18,5,18,238,8,18,10,18,12,18,241,9,18,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,253,8,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,5,19,273,8,19,10,19,12,19,276,9,19,1,20,1,20,
        1,21,1,21,1,22,1,22,1,23,1,23,1,23,1,23,5,23,288,8,23,10,23,12,23,
        291,9,23,1,23,1,23,1,23,3,23,296,8,23,1,24,1,24,1,24,1,24,1,24,1,
        24,3,24,304,8,24,1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,3,27,314,
        8,27,1,27,1,27,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,32,5,32,339,
        8,32,10,32,12,32,342,9,32,1,33,1,33,1,33,1,33,1,34,1,34,1,34,3,34,
        351,8,34,1,34,1,34,1,34,1,34,1,34,3,34,358,8,34,1,34,1,34,1,34,1,
        34,3,34,364,8,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,
        34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,3,
        34,388,8,34,1,35,3,35,391,8,35,1,36,1,36,1,36,1,36,1,36,1,36,1,36,
        3,36,400,8,36,3,36,402,8,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,
        37,3,37,412,8,37,1,38,1,38,1,39,1,39,1,39,1,39,3,39,420,8,39,1,39,
        1,39,1,39,1,39,1,39,3,39,427,8,39,3,39,429,8,39,1,40,1,40,1,40,1,
        40,1,40,1,40,1,40,1,40,3,40,439,8,40,1,40,1,40,3,40,443,8,40,1,40,
        1,40,3,40,447,8,40,1,40,3,40,450,8,40,1,41,1,41,1,41,1,41,3,41,456,
        8,41,1,41,3,41,459,8,41,1,41,1,41,1,41,1,41,1,42,5,42,466,8,42,10,
        42,12,42,469,9,42,1,43,1,43,1,43,1,43,1,44,1,44,1,44,3,44,478,8,
        44,1,44,0,1,38,45,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,
        78,80,82,84,86,88,0,6,2,0,40,42,48,51,2,0,46,47,52,53,2,0,32,35,
        44,45,1,0,65,69,1,0,38,39,1,0,21,31,506,0,90,1,0,0,0,2,101,1,0,0,
        0,4,115,1,0,0,0,6,117,1,0,0,0,8,137,1,0,0,0,10,139,1,0,0,0,12,153,
        1,0,0,0,14,155,1,0,0,0,16,165,1,0,0,0,18,168,1,0,0,0,20,172,1,0,
        0,0,22,182,1,0,0,0,24,198,1,0,0,0,26,200,1,0,0,0,28,204,1,0,0,0,
        30,209,1,0,0,0,32,216,1,0,0,0,34,226,1,0,0,0,36,234,1,0,0,0,38,252,
        1,0,0,0,40,277,1,0,0,0,42,279,1,0,0,0,44,281,1,0,0,0,46,295,1,0,
        0,0,48,303,1,0,0,0,50,305,1,0,0,0,52,307,1,0,0,0,54,311,1,0,0,0,
        56,317,1,0,0,0,58,320,1,0,0,0,60,327,1,0,0,0,62,332,1,0,0,0,64,340,
        1,0,0,0,66,343,1,0,0,0,68,387,1,0,0,0,70,390,1,0,0,0,72,401,1,0,
        0,0,74,411,1,0,0,0,76,413,1,0,0,0,78,415,1,0,0,0,80,449,1,0,0,0,
        82,451,1,0,0,0,84,467,1,0,0,0,86,470,1,0,0,0,88,477,1,0,0,0,90,91,
        5,1,0,0,91,92,5,70,0,0,92,93,5,62,0,0,93,94,3,2,1,0,94,95,5,0,0,
        1,95,1,1,0,0,0,96,100,3,4,2,0,97,100,3,12,6,0,98,100,3,18,9,0,99,
        96,1,0,0,0,99,97,1,0,0,0,99,98,1,0,0,0,100,103,1,0,0,0,101,99,1,
        0,0,0,101,102,1,0,0,0,102,3,1,0,0,0,103,101,1,0,0,0,104,105,5,2,
        0,0,105,106,3,8,4,0,106,107,5,62,0,0,107,116,1,0,0,0,108,109,5,2,
        0,0,109,111,5,55,0,0,110,112,3,6,3,0,111,110,1,0,0,0,111,112,1,0,
        0,0,112,113,1,0,0,0,113,114,5,56,0,0,114,116,5,62,0,0,115,104,1,
        0,0,0,115,108,1,0,0,0,116,5,1,0,0,0,117,118,3,8,4,0,118,124,5,62,
        0,0,119,120,3,8,4,0,120,121,5,62,0,0,121,123,1,0,0,0,122,119,1,0,
        0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,7,1,0,0,
        0,126,124,1,0,0,0,127,128,3,34,17,0,128,129,3,24,12,0,129,130,5,
        43,0,0,130,131,3,36,18,0,131,138,1,0,0,0,132,133,3,34,17,0,133,134,
        5,43,0,0,134,135,3,36,18,0,135,138,1,0,0,0,136,138,3,10,5,0,137,
        127,1,0,0,0,137,132,1,0,0,0,137,136,1,0,0,0,138,9,1,0,0,0,139,140,
        3,34,17,0,140,141,3,24,12,0,141,11,1,0,0,0,142,143,5,3,0,0,143,144,
        3,16,8,0,144,145,5,62,0,0,145,154,1,0,0,0,146,147,5,3,0,0,147,149,
        5,55,0,0,148,150,3,14,7,0,149,148,1,0,0,0,149,150,1,0,0,0,150,151,
        1,0,0,0,151,152,5,56,0,0,152,154,5,62,0,0,153,142,1,0,0,0,153,146,
        1,0,0,0,154,13,1,0,0,0,155,156,3,16,8,0,156,162,5,62,0,0,157,158,
        3,16,8,0,158,159,5,62,0,0,159,161,1,0,0,0,160,157,1,0,0,0,161,164,
        1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,15,1,0,0,0,164,162,1,
        0,0,0,165,166,5,70,0,0,166,167,3,24,12,0,167,17,1,0,0,0,168,169,
        3,20,10,0,169,170,3,66,33,0,170,171,5,62,0,0,171,19,1,0,0,0,172,
        173,5,4,0,0,173,174,5,70,0,0,174,176,5,55,0,0,175,177,3,22,11,0,
        176,175,1,0,0,0,176,177,1,0,0,0,177,178,1,0,0,0,178,180,5,56,0,0,
        179,181,3,24,12,0,180,179,1,0,0,0,180,181,1,0,0,0,181,21,1,0,0,0,
        182,187,3,10,5,0,183,184,5,61,0,0,184,186,3,10,5,0,185,183,1,0,0,
        0,186,189,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,23,1,0,0,0,
        189,187,1,0,0,0,190,191,5,55,0,0,191,192,3,24,12,0,192,193,5,56,
        0,0,193,199,1,0,0,0,194,199,5,70,0,0,195,199,3,26,13,0,196,199,3,
        28,14,0,197,199,3,30,15,0,198,190,1,0,0,0,198,194,1,0,0,0,198,195,
        1,0,0,0,198,196,1,0,0,0,198,197,1,0,0,0,199,25,1,0,0,0,200,201,5,
        59,0,0,201,202,5,60,0,0,202,203,3,24,12,0,203,27,1,0,0,0,204,205,
        5,59,0,0,205,206,5,66,0,0,206,207,5,60,0,0,207,208,3,24,12,0,208,
        29,1,0,0,0,209,210,5,5,0,0,210,212,5,57,0,0,211,213,3,32,16,0,212,
        211,1,0,0,0,212,213,1,0,0,0,213,214,1,0,0,0,214,215,5,58,0,0,215,
        31,1,0,0,0,216,217,3,10,5,0,217,223,5,62,0,0,218,219,3,10,5,0,219,
        220,5,62,0,0,220,222,1,0,0,0,221,218,1,0,0,0,222,225,1,0,0,0,223,
        221,1,0,0,0,223,224,1,0,0,0,224,33,1,0,0,0,225,223,1,0,0,0,226,231,
        5,70,0,0,227,228,5,61,0,0,228,230,5,70,0,0,229,227,1,0,0,0,230,233,
        1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,35,1,0,0,0,233,231,1,
        0,0,0,234,239,3,38,19,0,235,236,5,61,0,0,236,238,3,38,19,0,237,235,
        1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,37,1,
        0,0,0,241,239,1,0,0,0,242,243,6,19,-1,0,243,253,3,46,23,0,244,245,
        5,46,0,0,245,253,3,38,19,9,246,247,5,47,0,0,247,253,3,38,19,8,248,
        249,5,54,0,0,249,253,3,38,19,7,250,251,5,53,0,0,251,253,3,38,19,
        6,252,242,1,0,0,0,252,244,1,0,0,0,252,246,1,0,0,0,252,248,1,0,0,
        0,252,250,1,0,0,0,253,274,1,0,0,0,254,255,10,5,0,0,255,256,3,40,
        20,0,256,257,3,38,19,6,257,273,1,0,0,0,258,259,10,4,0,0,259,260,
        3,42,21,0,260,261,3,38,19,5,261,273,1,0,0,0,262,263,10,3,0,0,263,
        264,3,44,22,0,264,265,3,38,19,4,265,273,1,0,0,0,266,267,10,2,0,0,
        267,268,5,36,0,0,268,273,3,38,19,3,269,270,10,1,0,0,270,271,5,37,
        0,0,271,273,3,38,19,2,272,254,1,0,0,0,272,258,1,0,0,0,272,262,1,
        0,0,0,272,266,1,0,0,0,272,269,1,0,0,0,273,276,1,0,0,0,274,272,1,
        0,0,0,274,275,1,0,0,0,275,39,1,0,0,0,276,274,1,0,0,0,277,278,7,0,
        0,0,278,41,1,0,0,0,279,280,7,1,0,0,280,43,1,0,0,0,281,282,7,2,0,
        0,282,45,1,0,0,0,283,289,3,48,24,0,284,288,3,56,28,0,285,288,3,52,
        26,0,286,288,3,54,27,0,287,284,1,0,0,0,287,285,1,0,0,0,287,286,1,
        0,0,0,288,291,1,0,0,0,289,287,1,0,0,0,289,290,1,0,0,0,290,296,1,
        0,0,0,291,289,1,0,0,0,292,296,3,58,29,0,293,296,3,60,30,0,294,296,
        3,62,31,0,295,283,1,0,0,0,295,292,1,0,0,0,295,293,1,0,0,0,295,294,
        1,0,0,0,296,47,1,0,0,0,297,304,3,50,25,0,298,304,5,70,0,0,299,300,
        5,55,0,0,300,301,3,38,19,0,301,302,5,56,0,0,302,304,1,0,0,0,303,
        297,1,0,0,0,303,298,1,0,0,0,303,299,1,0,0,0,304,49,1,0,0,0,305,306,
        7,3,0,0,306,51,1,0,0,0,307,308,5,59,0,0,308,309,3,38,19,0,309,310,
        5,60,0,0,310,53,1,0,0,0,311,313,5,55,0,0,312,314,3,36,18,0,313,312,
        1,0,0,0,313,314,1,0,0,0,314,315,1,0,0,0,315,316,5,56,0,0,316,55,
        1,0,0,0,317,318,5,64,0,0,318,319,5,70,0,0,319,57,1,0,0,0,320,321,
        5,17,0,0,321,322,5,55,0,0,322,323,3,38,19,0,323,324,5,61,0,0,324,
        325,3,38,19,0,325,326,5,56,0,0,326,59,1,0,0,0,327,328,5,18,0,0,328,
        329,5,55,0,0,329,330,3,38,19,0,330,331,5,56,0,0,331,61,1,0,0,0,332,
        333,5,19,0,0,333,334,5,55,0,0,334,335,3,38,19,0,335,336,5,56,0,0,
        336,63,1,0,0,0,337,339,3,68,34,0,338,337,1,0,0,0,339,342,1,0,0,0,
        340,338,1,0,0,0,340,341,1,0,0,0,341,65,1,0,0,0,342,340,1,0,0,0,343,
        344,5,57,0,0,344,345,3,64,32,0,345,346,5,58,0,0,346,67,1,0,0,0,347,
        348,5,15,0,0,348,350,5,55,0,0,349,351,3,36,18,0,350,349,1,0,0,0,
        350,351,1,0,0,0,351,352,1,0,0,0,352,353,5,56,0,0,353,388,5,62,0,
        0,354,355,5,16,0,0,355,357,5,55,0,0,356,358,3,36,18,0,357,356,1,
        0,0,0,357,358,1,0,0,0,358,359,1,0,0,0,359,360,5,56,0,0,360,388,5,
        62,0,0,361,363,5,14,0,0,362,364,3,38,19,0,363,362,1,0,0,0,363,364,
        1,0,0,0,364,365,1,0,0,0,365,388,5,62,0,0,366,367,5,12,0,0,367,388,
        5,62,0,0,368,369,5,13,0,0,369,388,5,62,0,0,370,371,3,70,35,0,371,
        372,5,62,0,0,372,388,1,0,0,0,373,374,3,66,33,0,374,375,5,62,0,0,
        375,388,1,0,0,0,376,377,3,82,41,0,377,378,5,62,0,0,378,388,1,0,0,
        0,379,380,3,78,39,0,380,381,5,62,0,0,381,388,1,0,0,0,382,383,3,80,
        40,0,383,384,5,62,0,0,384,388,1,0,0,0,385,388,3,12,6,0,386,388,3,
        4,2,0,387,347,1,0,0,0,387,354,1,0,0,0,387,361,1,0,0,0,387,366,1,
        0,0,0,387,368,1,0,0,0,387,370,1,0,0,0,387,373,1,0,0,0,387,376,1,
        0,0,0,387,379,1,0,0,0,387,382,1,0,0,0,387,385,1,0,0,0,387,386,1,
        0,0,0,388,69,1,0,0,0,389,391,3,72,36,0,390,389,1,0,0,0,390,391,1,
        0,0,0,391,71,1,0,0,0,392,402,3,74,37,0,393,394,3,36,18,0,394,395,
        5,20,0,0,395,396,3,36,18,0,396,402,1,0,0,0,397,399,3,38,19,0,398,
        400,7,4,0,0,399,398,1,0,0,0,399,400,1,0,0,0,400,402,1,0,0,0,401,
        392,1,0,0,0,401,393,1,0,0,0,401,397,1,0,0,0,402,73,1,0,0,0,403,404,
        3,36,18,0,404,405,5,43,0,0,405,406,3,36,18,0,406,412,1,0,0,0,407,
        408,3,38,19,0,408,409,3,76,38,0,409,410,3,38,19,0,410,412,1,0,0,
        0,411,403,1,0,0,0,411,407,1,0,0,0,412,75,1,0,0,0,413,414,7,5,0,0,
        414,77,1,0,0,0,415,419,5,6,0,0,416,417,3,72,36,0,417,418,5,62,0,
        0,418,420,1,0,0,0,419,416,1,0,0,0,419,420,1,0,0,0,420,421,1,0,0,
        0,421,422,3,38,19,0,422,428,3,66,33,0,423,426,5,7,0,0,424,427,3,
        78,39,0,425,427,3,66,33,0,426,424,1,0,0,0,426,425,1,0,0,0,427,429,
        1,0,0,0,428,423,1,0,0,0,428,429,1,0,0,0,429,79,1,0,0,0,430,431,5,
        8,0,0,431,450,3,66,33,0,432,433,5,8,0,0,433,434,3,38,19,0,434,435,
        3,66,33,0,435,450,1,0,0,0,436,438,5,8,0,0,437,439,3,72,36,0,438,
        437,1,0,0,0,438,439,1,0,0,0,439,440,1,0,0,0,440,442,5,62,0,0,441,
        443,3,38,19,0,442,441,1,0,0,0,442,443,1,0,0,0,443,444,1,0,0,0,444,
        446,5,62,0,0,445,447,3,72,36,0,446,445,1,0,0,0,446,447,1,0,0,0,447,
        448,1,0,0,0,448,450,3,66,33,0,449,430,1,0,0,0,449,432,1,0,0,0,449,
        436,1,0,0,0,450,81,1,0,0,0,451,455,5,9,0,0,452,453,3,72,36,0,453,
        454,5,62,0,0,454,456,1,0,0,0,455,452,1,0,0,0,455,456,1,0,0,0,456,
        458,1,0,0,0,457,459,3,38,19,0,458,457,1,0,0,0,458,459,1,0,0,0,459,
        460,1,0,0,0,460,461,5,57,0,0,461,462,3,84,42,0,462,463,5,58,0,0,
        463,83,1,0,0,0,464,466,3,86,43,0,465,464,1,0,0,0,466,469,1,0,0,0,
        467,465,1,0,0,0,467,468,1,0,0,0,468,85,1,0,0,0,469,467,1,0,0,0,470,
        471,3,88,44,0,471,472,5,63,0,0,472,473,3,64,32,0,473,87,1,0,0,0,
        474,475,5,10,0,0,475,478,3,36,18,0,476,478,5,11,0,0,477,474,1,0,
        0,0,477,476,1,0,0,0,478,89,1,0,0,0,45,99,101,111,115,124,137,149,
        153,162,176,180,187,198,212,223,231,239,252,272,274,287,289,295,
        303,313,340,350,357,363,387,390,399,401,411,419,426,428,438,442,
        446,449,455,458,467,477
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'package'", "'var'", "'type'", "'func'", 
                     "'struct'", "'if'", "'else'", "'for'", "'switch'", 
                     "'case'", "'default'", "'break'", "'continue'", "'return'", 
                     "'print'", "'println'", "'append'", "'len'", "'cap'", 
                     "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'&='", 
                     "'|='", "'^='", "'<<='", "'>>='", "'&^='", "'=='", 
                     "'!='", "'<='", "'>='", "'&&'", "'||'", "'++'", "'--'", 
                     "'<<'", "'>>'", "'&^'", "'='", "'<'", "'>'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'&'", "'|'", "'^'", "'!'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'", 
                     "':'", "'.'" ]

    symbolicNames = [ "<INVALID>", "PACKAGE", "VAR", "TYPE", "FUNC", "STRUCT", 
                      "IF", "ELSE", "FOR", "SWITCH", "CASE", "DEFAULT", 
                      "BREAK", "CONTINUE", "RETURN", "PRINT", "PRINTLN", 
                      "APPEND", "LEN", "CAP", "DECLARE_ASSIGN", "PLUS_ASSIGN", 
                      "MINUS_ASSIGN", "STAR_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "AMP_ASSIGN", "PIPE_ASSIGN", "CARET_ASSIGN", "LSHIFT_ASSIGN", 
                      "RSHIFT_ASSIGN", "BIT_CLEAR_ASSIGN", "EQUALS", "NOT_EQUALS", 
                      "LTE", "GTE", "AND", "LOGICAL_OR", "INC", "DEC", "LSHIFT", 
                      "RSHIFT", "BIT_CLEAR", "ASSIGN", "LT", "GT", "PLUS", 
                      "MINUS", "STAR", "DIV", "MOD", "AMP", "PIPE", "CARET", 
                      "NOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "COMMA", "SEMI", "COLON", "DOT", "FLOATLITERAL", 
                      "INTLITERAL", "RUNELITERAL", "RAWSTRINGLITERAL", "INTERPRETEDSTRINGLITERAL", 
                      "IDENTIFIER", "LINE_COMMENT", "BLOCK_COMMENT", "WS" ]

    RULE_root = 0
    RULE_topDeclarationList = 1
    RULE_variableDecl = 2
    RULE_innerVarDecls = 3
    RULE_singleVarDecl = 4
    RULE_singleVarDeclNoExps = 5
    RULE_typeDecl = 6
    RULE_innerTypeDecls = 7
    RULE_singleTypeDecl = 8
    RULE_funcDecl = 9
    RULE_funcFrontDecl = 10
    RULE_funcArgDecls = 11
    RULE_declType = 12
    RULE_sliceDeclType = 13
    RULE_arrayDeclType = 14
    RULE_structDeclType = 15
    RULE_structMemDecls = 16
    RULE_identifierList = 17
    RULE_expressionList = 18
    RULE_expression = 19
    RULE_multiplicativeOp = 20
    RULE_additiveOp = 21
    RULE_relationalOp = 22
    RULE_primaryExpression = 23
    RULE_operand = 24
    RULE_literal = 25
    RULE_index = 26
    RULE_arguments = 27
    RULE_selector = 28
    RULE_appendExpression = 29
    RULE_lengthExpression = 30
    RULE_capExpression = 31
    RULE_statementList = 32
    RULE_block = 33
    RULE_statement = 34
    RULE_simpleStatement = 35
    RULE_nonEmptySimpleStatement = 36
    RULE_assignmentStatement = 37
    RULE_assignmentOp = 38
    RULE_ifStatement = 39
    RULE_loop = 40
    RULE_switchStmt = 41
    RULE_expressionCaseClauseList = 42
    RULE_expressionCaseClause = 43
    RULE_expressionSwitchCase = 44

    ruleNames =  [ "root", "topDeclarationList", "variableDecl", "innerVarDecls", 
                   "singleVarDecl", "singleVarDeclNoExps", "typeDecl", "innerTypeDecls", 
                   "singleTypeDecl", "funcDecl", "funcFrontDecl", "funcArgDecls", 
                   "declType", "sliceDeclType", "arrayDeclType", "structDeclType", 
                   "structMemDecls", "identifierList", "expressionList", 
                   "expression", "multiplicativeOp", "additiveOp", "relationalOp", 
                   "primaryExpression", "operand", "literal", "index", "arguments", 
                   "selector", "appendExpression", "lengthExpression", "capExpression", 
                   "statementList", "block", "statement", "simpleStatement", 
                   "nonEmptySimpleStatement", "assignmentStatement", "assignmentOp", 
                   "ifStatement", "loop", "switchStmt", "expressionCaseClauseList", 
                   "expressionCaseClause", "expressionSwitchCase" ]

    EOF = Token.EOF
    PACKAGE=1
    VAR=2
    TYPE=3
    FUNC=4
    STRUCT=5
    IF=6
    ELSE=7
    FOR=8
    SWITCH=9
    CASE=10
    DEFAULT=11
    BREAK=12
    CONTINUE=13
    RETURN=14
    PRINT=15
    PRINTLN=16
    APPEND=17
    LEN=18
    CAP=19
    DECLARE_ASSIGN=20
    PLUS_ASSIGN=21
    MINUS_ASSIGN=22
    STAR_ASSIGN=23
    DIV_ASSIGN=24
    MOD_ASSIGN=25
    AMP_ASSIGN=26
    PIPE_ASSIGN=27
    CARET_ASSIGN=28
    LSHIFT_ASSIGN=29
    RSHIFT_ASSIGN=30
    BIT_CLEAR_ASSIGN=31
    EQUALS=32
    NOT_EQUALS=33
    LTE=34
    GTE=35
    AND=36
    LOGICAL_OR=37
    INC=38
    DEC=39
    LSHIFT=40
    RSHIFT=41
    BIT_CLEAR=42
    ASSIGN=43
    LT=44
    GT=45
    PLUS=46
    MINUS=47
    STAR=48
    DIV=49
    MOD=50
    AMP=51
    PIPE=52
    CARET=53
    NOT=54
    LPAREN=55
    RPAREN=56
    LBRACE=57
    RBRACE=58
    LBRACK=59
    RBRACK=60
    COMMA=61
    SEMI=62
    COLON=63
    DOT=64
    FLOATLITERAL=65
    INTLITERAL=66
    RUNELITERAL=67
    RAWSTRINGLITERAL=68
    INTERPRETEDSTRINGLITERAL=69
    IDENTIFIER=70
    LINE_COMMENT=71
    BLOCK_COMMENT=72
    WS=73

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PACKAGE(self):
            return self.getToken(MiniGoParser.PACKAGE, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def topDeclarationList(self):
            return self.getTypedRuleContext(MiniGoParser.TopDeclarationListContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = MiniGoParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(MiniGoParser.PACKAGE)
            self.state = 91
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 92
            self.match(MiniGoParser.SEMI)
            self.state = 93
            self.topDeclarationList()
            self.state = 94
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopDeclarationListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.VariableDeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.VariableDeclContext,i)


        def typeDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.TypeDeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.TypeDeclContext,i)


        def funcDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FuncDeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FuncDeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_topDeclarationList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopDeclarationList" ):
                return visitor.visitTopDeclarationList(self)
            else:
                return visitor.visitChildren(self)




    def topDeclarationList(self):

        localctx = MiniGoParser.TopDeclarationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_topDeclarationList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0):
                self.state = 99
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 96
                    self.variableDecl()
                    pass
                elif token in [3]:
                    self.state = 97
                    self.typeDecl()
                    pass
                elif token in [4]:
                    self.state = 98
                    self.funcDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def singleVarDecl(self):
            return self.getTypedRuleContext(MiniGoParser.SingleVarDeclContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def innerVarDecls(self):
            return self.getTypedRuleContext(MiniGoParser.InnerVarDeclsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variableDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDecl" ):
                return visitor.visitVariableDecl(self)
            else:
                return visitor.visitChildren(self)




    def variableDecl(self):

        localctx = MiniGoParser.VariableDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDecl)
        self._la = 0 # Token type
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(MiniGoParser.VAR)
                self.state = 105
                self.singleVarDecl()
                self.state = 106
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.match(MiniGoParser.VAR)
                self.state = 109
                self.match(MiniGoParser.LPAREN)
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==70:
                    self.state = 110
                    self.innerVarDecls()


                self.state = 113
                self.match(MiniGoParser.RPAREN)
                self.state = 114
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InnerVarDeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleVarDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.SingleVarDeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.SingleVarDeclContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_innerVarDecls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInnerVarDecls" ):
                return visitor.visitInnerVarDecls(self)
            else:
                return visitor.visitChildren(self)




    def innerVarDecls(self):

        localctx = MiniGoParser.InnerVarDeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_innerVarDecls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.singleVarDecl()
            self.state = 118
            self.match(MiniGoParser.SEMI)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==70:
                self.state = 119
                self.singleVarDecl()
                self.state = 120
                self.match(MiniGoParser.SEMI)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleVarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierListContext,0)


        def declType(self):
            return self.getTypedRuleContext(MiniGoParser.DeclTypeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionListContext,0)


        def singleVarDeclNoExps(self):
            return self.getTypedRuleContext(MiniGoParser.SingleVarDeclNoExpsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_singleVarDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleVarDecl" ):
                return visitor.visitSingleVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def singleVarDecl(self):

        localctx = MiniGoParser.SingleVarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_singleVarDecl)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.identifierList()
                self.state = 128
                self.declType()
                self.state = 129
                self.match(MiniGoParser.ASSIGN)
                self.state = 130
                self.expressionList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.identifierList()
                self.state = 133
                self.match(MiniGoParser.ASSIGN)
                self.state = 134
                self.expressionList()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
                self.singleVarDeclNoExps()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleVarDeclNoExpsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierList(self):
            return self.getTypedRuleContext(MiniGoParser.IdentifierListContext,0)


        def declType(self):
            return self.getTypedRuleContext(MiniGoParser.DeclTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_singleVarDeclNoExps

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleVarDeclNoExps" ):
                return visitor.visitSingleVarDeclNoExps(self)
            else:
                return visitor.visitChildren(self)




    def singleVarDeclNoExps(self):

        localctx = MiniGoParser.SingleVarDeclNoExpsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_singleVarDeclNoExps)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.identifierList()
            self.state = 140
            self.declType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def singleTypeDecl(self):
            return self.getTypedRuleContext(MiniGoParser.SingleTypeDeclContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def innerTypeDecls(self):
            return self.getTypedRuleContext(MiniGoParser.InnerTypeDeclsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typeDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDecl" ):
                return visitor.visitTypeDecl(self)
            else:
                return visitor.visitChildren(self)




    def typeDecl(self):

        localctx = MiniGoParser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typeDecl)
        self._la = 0 # Token type
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(MiniGoParser.TYPE)
                self.state = 143
                self.singleTypeDecl()
                self.state = 144
                self.match(MiniGoParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(MiniGoParser.TYPE)
                self.state = 147
                self.match(MiniGoParser.LPAREN)
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==70:
                    self.state = 148
                    self.innerTypeDecls()


                self.state = 151
                self.match(MiniGoParser.RPAREN)
                self.state = 152
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InnerTypeDeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleTypeDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.SingleTypeDeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.SingleTypeDeclContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_innerTypeDecls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInnerTypeDecls" ):
                return visitor.visitInnerTypeDecls(self)
            else:
                return visitor.visitChildren(self)




    def innerTypeDecls(self):

        localctx = MiniGoParser.InnerTypeDeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_innerTypeDecls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.singleTypeDecl()
            self.state = 156
            self.match(MiniGoParser.SEMI)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==70:
                self.state = 157
                self.singleTypeDecl()
                self.state = 158
                self.match(MiniGoParser.SEMI)
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleTypeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def declType(self):
            return self.getTypedRuleContext(MiniGoParser.DeclTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_singleTypeDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleTypeDecl" ):
                return visitor.visitSingleTypeDecl(self)
            else:
                return visitor.visitChildren(self)




    def singleTypeDecl(self):

        localctx = MiniGoParser.SingleTypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_singleTypeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 166
            self.declType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcFrontDecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncFrontDeclContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = MiniGoParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.funcFrontDecl()
            self.state = 169
            self.block()
            self.state = 170
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncFrontDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def funcArgDecls(self):
            return self.getTypedRuleContext(MiniGoParser.FuncArgDeclsContext,0)


        def declType(self):
            return self.getTypedRuleContext(MiniGoParser.DeclTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcFrontDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncFrontDecl" ):
                return visitor.visitFuncFrontDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcFrontDecl(self):

        localctx = MiniGoParser.FuncFrontDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcFrontDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(MiniGoParser.FUNC)
            self.state = 173
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 174
            self.match(MiniGoParser.LPAREN)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==70:
                self.state = 175
                self.funcArgDecls()


            self.state = 178
            self.match(MiniGoParser.RPAREN)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 612489549322387488) != 0) or _la==70:
                self.state = 179
                self.declType()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncArgDeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleVarDeclNoExps(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.SingleVarDeclNoExpsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.SingleVarDeclNoExpsContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcArgDecls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncArgDecls" ):
                return visitor.visitFuncArgDecls(self)
            else:
                return visitor.visitChildren(self)




    def funcArgDecls(self):

        localctx = MiniGoParser.FuncArgDeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcArgDecls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.singleVarDeclNoExps()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==61:
                self.state = 183
                self.match(MiniGoParser.COMMA)
                self.state = 184
                self.singleVarDeclNoExps()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def declType(self):
            return self.getTypedRuleContext(MiniGoParser.DeclTypeContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def sliceDeclType(self):
            return self.getTypedRuleContext(MiniGoParser.SliceDeclTypeContext,0)


        def arrayDeclType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDeclTypeContext,0)


        def structDeclType(self):
            return self.getTypedRuleContext(MiniGoParser.StructDeclTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclType" ):
                return visitor.visitDeclType(self)
            else:
                return visitor.visitChildren(self)




    def declType(self):

        localctx = MiniGoParser.DeclTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_declType)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(MiniGoParser.LPAREN)
                self.state = 191
                self.declType()
                self.state = 192
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.sliceDeclType()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                self.arrayDeclType()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 197
                self.structDeclType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SliceDeclTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def declType(self):
            return self.getTypedRuleContext(MiniGoParser.DeclTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_sliceDeclType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSliceDeclType" ):
                return visitor.visitSliceDeclType(self)
            else:
                return visitor.visitChildren(self)




    def sliceDeclType(self):

        localctx = MiniGoParser.SliceDeclTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_sliceDeclType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(MiniGoParser.LBRACK)
            self.state = 201
            self.match(MiniGoParser.RBRACK)
            self.state = 202
            self.declType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDeclTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def INTLITERAL(self):
            return self.getToken(MiniGoParser.INTLITERAL, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def declType(self):
            return self.getTypedRuleContext(MiniGoParser.DeclTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayDeclType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDeclType" ):
                return visitor.visitArrayDeclType(self)
            else:
                return visitor.visitChildren(self)




    def arrayDeclType(self):

        localctx = MiniGoParser.ArrayDeclTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arrayDeclType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(MiniGoParser.LBRACK)
            self.state = 205
            self.match(MiniGoParser.INTLITERAL)
            self.state = 206
            self.match(MiniGoParser.RBRACK)
            self.state = 207
            self.declType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def structMemDecls(self):
            return self.getTypedRuleContext(MiniGoParser.StructMemDeclsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structDeclType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDeclType" ):
                return visitor.visitStructDeclType(self)
            else:
                return visitor.visitChildren(self)




    def structDeclType(self):

        localctx = MiniGoParser.StructDeclTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_structDeclType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(MiniGoParser.STRUCT)
            self.state = 210
            self.match(MiniGoParser.LBRACE)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==70:
                self.state = 211
                self.structMemDecls()


            self.state = 214
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructMemDeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleVarDeclNoExps(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.SingleVarDeclNoExpsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.SingleVarDeclNoExpsContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structMemDecls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructMemDecls" ):
                return visitor.visitStructMemDecls(self)
            else:
                return visitor.visitChildren(self)




    def structMemDecls(self):

        localctx = MiniGoParser.StructMemDeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_structMemDecls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.singleVarDeclNoExps()
            self.state = 217
            self.match(MiniGoParser.SEMI)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==70:
                self.state = 218
                self.singleVarDeclNoExps()
                self.state = 219
                self.match(MiniGoParser.SEMI)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_identifierList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierList" ):
                return visitor.visitIdentifierList(self)
            else:
                return visitor.visitChildren(self)




    def identifierList(self):

        localctx = MiniGoParser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_identifierList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==61:
                self.state = 227
                self.match(MiniGoParser.COMMA)
                self.state = 228
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expressionList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = MiniGoParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.expression(0)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==61:
                self.state = 235
                self.match(MiniGoParser.COMMA)
                self.state = 236
                self.expression(0)
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class UnaryMinusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinusExpression" ):
                return visitor.visitUnaryMinusExpression(self)
            else:
                return visitor.visitChildren(self)


    class UnaryBitNotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CARET(self):
            return self.getToken(MiniGoParser.CARET, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryBitNotExpression" ):
                return visitor.visitUnaryBitNotExpression(self)
            else:
                return visitor.visitChildren(self)


    class UnaryPlusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryPlusExpression" ):
                return visitor.visitUnaryPlusExpression(self)
            else:
                return visitor.visitChildren(self)


    class UnaryNotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryNotExpression" ):
                return visitor.visitUnaryNotExpression(self)
            else:
                return visitor.visitChildren(self)


    class AdditiveExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)

        def additiveOp(self):
            return self.getTypedRuleContext(MiniGoParser.AdditiveOpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)


    class PrimaryExpressionOnlyContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primaryExpression(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpressionOnly" ):
                return visitor.visitPrimaryExpressionOnly(self)
            else:
                return visitor.visitChildren(self)


    class RelationalExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)

        def relationalOp(self):
            return self.getTypedRuleContext(MiniGoParser.RelationalOpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)


    class LogicalAndExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpression" ):
                return visitor.visitLogicalAndExpression(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicativeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)

        def multiplicativeOp(self):
            return self.getTypedRuleContext(MiniGoParser.MultiplicativeOpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)


    class LogicalOrExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)

        def LOGICAL_OR(self):
            return self.getToken(MiniGoParser.LOGICAL_OR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpression" ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 19, 55, 65, 66, 67, 68, 69, 70]:
                localctx = MiniGoParser.PrimaryExpressionOnlyContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 243
                self.primaryExpression()
                pass
            elif token in [46]:
                localctx = MiniGoParser.UnaryPlusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 244
                self.match(MiniGoParser.PLUS)
                self.state = 245
                self.expression(9)
                pass
            elif token in [47]:
                localctx = MiniGoParser.UnaryMinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 246
                self.match(MiniGoParser.MINUS)
                self.state = 247
                self.expression(8)
                pass
            elif token in [54]:
                localctx = MiniGoParser.UnaryNotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 248
                self.match(MiniGoParser.NOT)
                self.state = 249
                self.expression(7)
                pass
            elif token in [53]:
                localctx = MiniGoParser.UnaryBitNotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 250
                self.match(MiniGoParser.CARET)
                self.state = 251
                self.expression(6)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 274
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 272
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.MultiplicativeExpressionContext(self, MiniGoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 254
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 255
                        self.multiplicativeOp()
                        self.state = 256
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.AdditiveExpressionContext(self, MiniGoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 258
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 259
                        self.additiveOp()
                        self.state = 260
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.RelationalExpressionContext(self, MiniGoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 262
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 263
                        self.relationalOp()
                        self.state = 264
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.LogicalAndExpressionContext(self, MiniGoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 266
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 267
                        self.match(MiniGoParser.AND)
                        self.state = 268
                        self.expression(3)
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.LogicalOrExpressionContext(self, MiniGoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 269
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 270
                        self.match(MiniGoParser.LOGICAL_OR)
                        self.state = 271
                        self.expression(2)
                        pass

             
                self.state = 276
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultiplicativeOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(MiniGoParser.STAR, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def LSHIFT(self):
            return self.getToken(MiniGoParser.LSHIFT, 0)

        def RSHIFT(self):
            return self.getToken(MiniGoParser.RSHIFT, 0)

        def AMP(self):
            return self.getToken(MiniGoParser.AMP, 0)

        def BIT_CLEAR(self):
            return self.getToken(MiniGoParser.BIT_CLEAR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_multiplicativeOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeOp" ):
                return visitor.visitMultiplicativeOp(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeOp(self):

        localctx = MiniGoParser.MultiplicativeOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_multiplicativeOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4229821232054272) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def PIPE(self):
            return self.getToken(MiniGoParser.PIPE, 0)

        def CARET(self):
            return self.getToken(MiniGoParser.CARET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_additiveOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveOp" ):
                return visitor.visitAdditiveOp(self)
            else:
                return visitor.visitChildren(self)




    def additiveOp(self):

        localctx = MiniGoParser.AdditiveOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_additiveOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 13721905114644480) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(MiniGoParser.EQUALS, 0)

        def NOT_EQUALS(self):
            return self.getToken(MiniGoParser.NOT_EQUALS, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LTE(self):
            return self.getToken(MiniGoParser.LTE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GTE(self):
            return self.getToken(MiniGoParser.GTE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_relationalOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalOp" ):
                return visitor.visitRelationalOp(self)
            else:
                return visitor.visitChildren(self)




    def relationalOp(self):

        localctx = MiniGoParser.RelationalOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_relationalOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 52840982642688) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def selector(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.SelectorContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.SelectorContext,i)


        def index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IndexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IndexContext,i)


        def arguments(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ArgumentsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ArgumentsContext,i)


        def appendExpression(self):
            return self.getTypedRuleContext(MiniGoParser.AppendExpressionContext,0)


        def lengthExpression(self):
            return self.getTypedRuleContext(MiniGoParser.LengthExpressionContext,0)


        def capExpression(self):
            return self.getTypedRuleContext(MiniGoParser.CapExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_primaryExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = MiniGoParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_primaryExpression)
        try:
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [55, 65, 66, 67, 68, 69, 70]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.operand()
                self.state = 289
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 287
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [64]:
                            self.state = 284
                            self.selector()
                            pass
                        elif token in [59]:
                            self.state = 285
                            self.index()
                            pass
                        elif token in [55]:
                            self.state = 286
                            self.arguments()
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 291
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.appendExpression()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 293
                self.lengthExpression()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 294
                self.capExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_operand)
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65, 66, 67, 68, 69]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.literal()
                pass
            elif token in [70]:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 3)
                self.state = 299
                self.match(MiniGoParser.LPAREN)
                self.state = 300
                self.expression(0)
                self.state = 301
                self.match(MiniGoParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLITERAL(self):
            return self.getToken(MiniGoParser.INTLITERAL, 0)

        def FLOATLITERAL(self):
            return self.getToken(MiniGoParser.FLOATLITERAL, 0)

        def RUNELITERAL(self):
            return self.getToken(MiniGoParser.RUNELITERAL, 0)

        def RAWSTRINGLITERAL(self):
            return self.getToken(MiniGoParser.RAWSTRINGLITERAL, 0)

        def INTERPRETEDSTRINGLITERAL(self):
            return self.getToken(MiniGoParser.INTERPRETEDSTRINGLITERAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            _la = self._input.LA(1)
            if not(((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 31) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = MiniGoParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(MiniGoParser.LBRACK)
            self.state = 308
            self.expression(0)
            self.state = 309
            self.match(MiniGoParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = MiniGoParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(MiniGoParser.LPAREN)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 17733406179721223) != 0):
                self.state = 312
                self.expressionList()


            self.state = 315
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_selector

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelector" ):
                return visitor.visitSelector(self)
            else:
                return visitor.visitChildren(self)




    def selector(self):

        localctx = MiniGoParser.SelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_selector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(MiniGoParser.DOT)
            self.state = 318
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AppendExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def APPEND(self):
            return self.getToken(MiniGoParser.APPEND, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_appendExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAppendExpression" ):
                return visitor.visitAppendExpression(self)
            else:
                return visitor.visitChildren(self)




    def appendExpression(self):

        localctx = MiniGoParser.AppendExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_appendExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(MiniGoParser.APPEND)
            self.state = 321
            self.match(MiniGoParser.LPAREN)
            self.state = 322
            self.expression(0)
            self.state = 323
            self.match(MiniGoParser.COMMA)
            self.state = 324
            self.expression(0)
            self.state = 325
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LengthExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEN(self):
            return self.getToken(MiniGoParser.LEN, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lengthExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLengthExpression" ):
                return visitor.visitLengthExpression(self)
            else:
                return visitor.visitChildren(self)




    def lengthExpression(self):

        localctx = MiniGoParser.LengthExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_lengthExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(MiniGoParser.LEN)
            self.state = 328
            self.match(MiniGoParser.LPAREN)
            self.state = 329
            self.expression(0)
            self.state = 330
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CapExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAP(self):
            return self.getToken(MiniGoParser.CAP, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_capExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCapExpression" ):
                return visitor.visitCapExpression(self)
            else:
                return visitor.visitChildren(self)




    def capExpression(self):

        localctx = MiniGoParser.CapExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_capExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(MiniGoParser.CAP)
            self.state = 333
            self.match(MiniGoParser.LPAREN)
            self.state = 334
            self.expression(0)
            self.state = 335
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statementList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = MiniGoParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4819062707520009036) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 63) != 0):
                self.state = 337
                self.statement()
                self.state = 342
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(MiniGoParser.LBRACE)
            self.state = 344
            self.statementList()
            self.state = 345
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(MiniGoParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def expressionList(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionListContext,0)


        def PRINTLN(self):
            return self.getToken(MiniGoParser.PRINTLN, 0)

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def simpleStatement(self):
            return self.getTypedRuleContext(MiniGoParser.SimpleStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def switchStmt(self):
            return self.getTypedRuleContext(MiniGoParser.SwitchStmtContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniGoParser.IfStatementContext,0)


        def loop(self):
            return self.getTypedRuleContext(MiniGoParser.LoopContext,0)


        def typeDecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypeDeclContext,0)


        def variableDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VariableDeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 387
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.match(MiniGoParser.PRINT)
                self.state = 348
                self.match(MiniGoParser.LPAREN)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 17733406179721223) != 0):
                    self.state = 349
                    self.expressionList()


                self.state = 352
                self.match(MiniGoParser.RPAREN)
                self.state = 353
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.match(MiniGoParser.PRINTLN)
                self.state = 355
                self.match(MiniGoParser.LPAREN)
                self.state = 357
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 17733406179721223) != 0):
                    self.state = 356
                    self.expressionList()


                self.state = 359
                self.match(MiniGoParser.RPAREN)
                self.state = 360
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 361
                self.match(MiniGoParser.RETURN)
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 17733406179721223) != 0):
                    self.state = 362
                    self.expression(0)


                self.state = 365
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 366
                self.match(MiniGoParser.BREAK)
                self.state = 367
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 368
                self.match(MiniGoParser.CONTINUE)
                self.state = 369
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [17, 18, 19, 46, 47, 53, 54, 55, 62, 65, 66, 67, 68, 69, 70]:
                self.enterOuterAlt(localctx, 6)
                self.state = 370
                self.simpleStatement()
                self.state = 371
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 7)
                self.state = 373
                self.block()
                self.state = 374
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 8)
                self.state = 376
                self.switchStmt()
                self.state = 377
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 9)
                self.state = 379
                self.ifStatement()
                self.state = 380
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 10)
                self.state = 382
                self.loop()
                self.state = 383
                self.match(MiniGoParser.SEMI)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 11)
                self.state = 385
                self.typeDecl()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 12)
                self.state = 386
                self.variableDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonEmptySimpleStatement(self):
            return self.getTypedRuleContext(MiniGoParser.NonEmptySimpleStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_simpleStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleStatement" ):
                return visitor.visitSimpleStatement(self)
            else:
                return visitor.visitChildren(self)




    def simpleStatement(self):

        localctx = MiniGoParser.SimpleStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_simpleStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 17733406179721223) != 0):
                self.state = 389
                self.nonEmptySimpleStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NonEmptySimpleStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentStatementContext,0)


        def expressionList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionListContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionListContext,i)


        def DECLARE_ASSIGN(self):
            return self.getToken(MiniGoParser.DECLARE_ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def INC(self):
            return self.getToken(MiniGoParser.INC, 0)

        def DEC(self):
            return self.getToken(MiniGoParser.DEC, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_nonEmptySimpleStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonEmptySimpleStatement" ):
                return visitor.visitNonEmptySimpleStatement(self)
            else:
                return visitor.visitChildren(self)




    def nonEmptySimpleStatement(self):

        localctx = MiniGoParser.NonEmptySimpleStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_nonEmptySimpleStatement)
        self._la = 0 # Token type
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.assignmentStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.expressionList()
                self.state = 394
                self.match(MiniGoParser.DECLARE_ASSIGN)
                self.state = 395
                self.expressionList()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 397
                self.expression(0)
                self.state = 399
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==38 or _la==39:
                    self.state = 398
                    _la = self._input.LA(1)
                    if not(_la==38 or _la==39):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionListContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionListContext,i)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def assignmentOp(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentOpContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignmentStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = MiniGoParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_assignmentStatement)
        try:
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.expressionList()
                self.state = 404
                self.match(MiniGoParser.ASSIGN)
                self.state = 405
                self.expressionList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.expression(0)
                self.state = 408
                self.assignmentOp()
                self.state = 409
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS_ASSIGN(self):
            return self.getToken(MiniGoParser.PLUS_ASSIGN, 0)

        def AMP_ASSIGN(self):
            return self.getToken(MiniGoParser.AMP_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(MiniGoParser.MINUS_ASSIGN, 0)

        def PIPE_ASSIGN(self):
            return self.getToken(MiniGoParser.PIPE_ASSIGN, 0)

        def STAR_ASSIGN(self):
            return self.getToken(MiniGoParser.STAR_ASSIGN, 0)

        def CARET_ASSIGN(self):
            return self.getToken(MiniGoParser.CARET_ASSIGN, 0)

        def LSHIFT_ASSIGN(self):
            return self.getToken(MiniGoParser.LSHIFT_ASSIGN, 0)

        def RSHIFT_ASSIGN(self):
            return self.getToken(MiniGoParser.RSHIFT_ASSIGN, 0)

        def BIT_CLEAR_ASSIGN(self):
            return self.getToken(MiniGoParser.BIT_CLEAR_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignmentOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOp" ):
                return visitor.visitAssignmentOp(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOp(self):

        localctx = MiniGoParser.AssignmentOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_assignmentOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4292870144) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def nonEmptySimpleStatement(self):
            return self.getTypedRuleContext(MiniGoParser.NonEmptySimpleStatementContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def ifStatement(self):
            return self.getTypedRuleContext(MiniGoParser.IfStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniGoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(MiniGoParser.IF)
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 416
                self.nonEmptySimpleStatement()
                self.state = 417
                self.match(MiniGoParser.SEMI)


            self.state = 421
            self.expression(0)
            self.state = 422
            self.block()
            self.state = 428
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 423
                self.match(MiniGoParser.ELSE)
                self.state = 426
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 424
                    self.ifStatement()
                    pass
                elif token in [57]:
                    self.state = 425
                    self.block()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def nonEmptySimpleStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NonEmptySimpleStatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NonEmptySimpleStatementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = MiniGoParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_loop)
        self._la = 0 # Token type
        try:
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.match(MiniGoParser.FOR)
                self.state = 431
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.match(MiniGoParser.FOR)
                self.state = 433
                self.expression(0)
                self.state = 434
                self.block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 436
                self.match(MiniGoParser.FOR)
                self.state = 438
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 17733406179721223) != 0):
                    self.state = 437
                    self.nonEmptySimpleStatement()


                self.state = 440
                self.match(MiniGoParser.SEMI)
                self.state = 442
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 17733406179721223) != 0):
                    self.state = 441
                    self.expression(0)


                self.state = 444
                self.match(MiniGoParser.SEMI)
                self.state = 446
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 17733406179721223) != 0):
                    self.state = 445
                    self.nonEmptySimpleStatement()


                self.state = 448
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(MiniGoParser.SWITCH, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def expressionCaseClauseList(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionCaseClauseListContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def nonEmptySimpleStatement(self):
            return self.getTypedRuleContext(MiniGoParser.NonEmptySimpleStatementContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_switchStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStmt" ):
                return visitor.visitSwitchStmt(self)
            else:
                return visitor.visitChildren(self)




    def switchStmt(self):

        localctx = MiniGoParser.SwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_switchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(MiniGoParser.SWITCH)
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 452
                self.nonEmptySimpleStatement()
                self.state = 453
                self.match(MiniGoParser.SEMI)


            self.state = 458
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & 17733406179721223) != 0):
                self.state = 457
                self.expression(0)


            self.state = 460
            self.match(MiniGoParser.LBRACE)
            self.state = 461
            self.expressionCaseClauseList()
            self.state = 462
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionCaseClauseListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionCaseClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionCaseClauseContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionCaseClauseContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expressionCaseClauseList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionCaseClauseList" ):
                return visitor.visitExpressionCaseClauseList(self)
            else:
                return visitor.visitChildren(self)




    def expressionCaseClauseList(self):

        localctx = MiniGoParser.ExpressionCaseClauseListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expressionCaseClauseList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==11:
                self.state = 464
                self.expressionCaseClause()
                self.state = 469
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionCaseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionSwitchCase(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionSwitchCaseContext,0)


        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expressionCaseClause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionCaseClause" ):
                return visitor.visitExpressionCaseClause(self)
            else:
                return visitor.visitChildren(self)




    def expressionCaseClause(self):

        localctx = MiniGoParser.ExpressionCaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expressionCaseClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.expressionSwitchCase()
            self.state = 471
            self.match(MiniGoParser.COLON)
            self.state = 472
            self.statementList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionSwitchCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(MiniGoParser.CASE, 0)

        def expressionList(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionListContext,0)


        def DEFAULT(self):
            return self.getToken(MiniGoParser.DEFAULT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expressionSwitchCase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionSwitchCase" ):
                return visitor.visitExpressionSwitchCase(self)
            else:
                return visitor.visitChildren(self)




    def expressionSwitchCase(self):

        localctx = MiniGoParser.ExpressionSwitchCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expressionSwitchCase)
        try:
            self.state = 477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.match(MiniGoParser.CASE)
                self.state = 475
                self.expressionList()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 476
                self.match(MiniGoParser.DEFAULT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[19] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




