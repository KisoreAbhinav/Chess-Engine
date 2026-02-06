from enum import IntEnum

U64 = int
# arbitrary precision
# instead of using unsigned long long int in C, we just define it, as python handles it

ENGINE_NAME = "Hydra 1.0"
# Name of the engine - can be anything but i am obsessed with Hydra so...

BOARD_SQ_NUM = 120
# Size of the board, including the actual chess board along with the excess squares to check for invalid positions 
# Prevents the flow of calculation to cross the board limits

class Pieces (IntEnum):
    EMPTY = 0

    wP = 1
    wN = 2
    wB = 3
    wR = 4
    wQ = 5
    wK = 6

    bP = 7
    bN = 8
    bB = 9
    bR = 10
    bQ = 11
    bK = 12
# Assigned values to the pieces so instead of using variables, we can just use the value of each piece to make these calculations simpler

    
class Ranks (IntEnum):
    RANK_1 = 0
    RANK_2 = 1
    RANK_3 = 2
    RANK_4 = 3
    RANK_5 = 4
    RANK_6 = 5
    RANK_7 = 6
    RANK_8 = 7
    RANK_NONE= 8
# defining each rank, with rank 1 being white's home square and 8 being black's.
# RANK_NONE here is used to calculate the overflow

class File (IntEnum):
    FILE_1 = 0
    FILE_2 = 1
    FILE_3 = 2
    FILE_4 = 3
    FILE_5 = 4
    FILE_6 = 5
    FILE_7 = 6
    FILE_8 = 7
    FILE_NONE= 8
#defining each file where file a = file 1 and so on, upto file h = 8
# FILE_NONE here is used to calculate the overflow

class Side(IntEnum):
    WHITE = 0
    BLACK = 1
    BOTH = 2
# teams definition
# BOTH will be used to check for total number of pieces, attacks, moves, etc
# Ex- if after a move, the condition says BOTH, means a piece was captured

class Square(IntEnum):
    A1 = 21; B1 = 22; C1 = 23; D1 = 24; E1 = 25; F1 = 26; G1 = 27; H1 = 28
    A2 = 31; B2 = 32; C2 = 33; D2 = 34; E2 = 35; F2 = 36; G2 = 37; H2 = 38
    A3 = 41; B3 = 42; C3 = 43; D3 = 44; E3 = 45; F3 = 46; G3 = 47; H3 = 48
    A4 = 51; B4 = 52; C4 = 53; D4 = 54; E4 = 55; F4 = 56; G4 = 57; H4 = 58
    A5 = 61; B5 = 62; C5 = 63; D5 = 64; E5 = 65; F5 = 66; G5 = 67; H5 = 68
    A6 = 71; B6 = 72; C6 = 73; D6 = 74; E6 = 75; F6 = 76; G6 = 77; H6 = 78
    A7 = 81; B7 = 82; C7 = 83; D7 = 84; E7 = 85; F7 = 86; G7 = 87; H7 = 88
    A8 = 91; B8 = 92; C8 = 93; D8 = 94; E8 = 95; F8 = 96; G8 = 97; H8 = 98

    NO_SQ = 99