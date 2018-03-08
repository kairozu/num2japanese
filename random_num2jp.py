# Prints a random integer between num_start and num_end inclusive, along with
# the hiragana and kanji representations.

from random import *

num_start = 1
num_end = 99999
num_numeric = randint(num_start, num_end)  # Pick a random number between start and end inclusive
print(num_numeric)

kana1to9 = ['いち', 'に', 'さん', 'よん', 'ご', 'ろく', 'なな', 'はち', 'きゅう']
kanji1to9 = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
kana10to90 = ['じゅう', 'にじゅう', 'さんじゅう', 'よんじゅう', 'ごじゅう', 'ろくじゅう', 'ななじゅう', 'はちじゅう', 'きゅうじゅう']
kanji10to90 = ['十', '二十', '三十', '四十', '五十', '六十', '七十', '八十', '九十']
kana100to900 = ['ひゃく', 'にひゃく', 'さんびゃく', 'よんひゃく', 'ごひゃく', 'ろっぴゃく', 'ななひゃく', 'はっぴゃく', 'きゅうひゃく']
kanji100to900 = ['百', '二百', '三百', '四百', '五百', '六百', '七百', '八百', '九百']
kana1000to9000 = ['せん', 'にせん', 'さんぜん', 'よんせん', 'ごせん', 'ろくせん', 'ななせん', 'はっせん', 'きゅうせん']
kanji1000to9000 = ['千', '二千', '三千', '四千', '五千', '六千', '七千', '八千', '九千']
kana10kto90k = ['いちまん', 'にまん', 'さんまん', 'よんまん', 'ごまん', 'ろくまん', 'ななまん', 'はちまん', 'きゅうまん']
kanji10kto90k = ['一万', '二万', '三万', '四万', '五万', '六万', '七万', '八万', '九万']

num_a = ''
num_b = ''
num_c = ''
num_d = ''
num_e = ''
num_f = ''
num_g = ''
num_h = ''
num_ak = ''
num_bk = ''
num_ck = ''
num_dk = ''
num_ek = ''
num_fk = ''
num_gk = ''
num_hk = ''

def collect_ones(ones):
    if int(ones) == 0:
        num = ''
        numk = ''
    else:
        num = kana1to9[int(ones) - 1]
        numk = kanji1to9[int(ones) - 1]
    return num, numk

def collect_tens(tens):
    if int(tens) == 0:
        num = ''
        numk = ''
    else:
        num = kana10to90[int(tens) - 1]
        numk = kanji10to90[int(tens) - 1]
    return num, numk

def collect_hundreds(hundreds):
    if int(hundreds) == 0:
        num = ''
        numk = ''
    else:
        num = kana100to900[int(hundreds) - 1]
        numk = kanji100to900[int(hundreds) - 1]
    return num, numk

def collect_thousands(thousands):
    if int(thousands) == 0:
        num = ''
        numk = ''
    else:
        num = kana1000to9000[int(thousands) - 1]
        numk = kanji1000to9000[int(thousands) - 1]
    return num, numk

num_components = list(str(num_numeric))

if len(num_components) == 1:
    kana = kana1to9[num_numeric - 1]
    kanji = kanji1to9[num_numeric - 1]
elif len(num_components) == 2:
    num_b = kana10to90[int(num_components[0])-1]
    num_bk = kanji10to90[int(num_components[0]) - 1]
    num_a, num_ak = collect_ones(num_components[1])
    kana = num_b + num_a
    kanji = num_bk + num_ak
elif len(num_components) == 3:
    num_c = kana100to900[int(num_components[0])-1]
    num_ck = kanji100to900[int(num_components[0])-1]
    num_b, num_bk = collect_tens(num_components[1])
    num_a, num_ak = collect_ones(num_components[2])
    kana = num_c + num_b + num_a
    kanji = num_ck + num_bk + num_ak
elif len(num_components) == 4:
    num_d = kana1000to9000[int(num_components[0])-1]
    num_dk = kanji1000to9000[int(num_components[0]) - 1]
    num_c, num_ck = collect_hundreds(num_components[1])
    num_b, num_bk = collect_tens(num_components[2])
    num_a, num_ak = collect_ones(num_components[3])
    kana = num_d + num_c + num_b + num_a
    kanji = num_dk + num_ck + num_bk + num_ak
elif len(num_components) == 5:
    num_e = kana10kto90k[int(num_components[0])-1]
    num_ek = kanji10kto90k[int(num_components[0])-1]
    num_d, num_dk = collect_thousands(num_components[1])
    num_c, num_ck = collect_hundreds(num_components[2])
    num_b, num_bk = collect_tens(num_components[3])
    num_a, num_ak = collect_ones(num_components[4])
    kana = num_e + num_d + num_c + num_b + num_a
    kanji = num_ek + num_dk + num_ck + num_bk + num_ak
elif len(num_components) == 6:
    num_f, num_fk = collect_tens(num_components[0])
    num_e, num_ek = collect_ones(num_components[1])
    num_e = num_e + 'まん'
    num_ek = num_ek + '万'
    num_d, num_dk = collect_thousands(num_components[2])
    num_c, num_ck = collect_hundreds(num_components[3])
    num_b, num_bk = collect_tens(num_components[4])
    num_a, num_ak = collect_ones(num_components[5])
    kana = num_f + num_e + num_d + num_c + num_b + num_a
    kanji = num_fk + num_ek + num_dk + num_ck + num_bk + num_ak
elif len(num_components) == 7:
    num_g, num_gk = collect_hundreds(num_components[0])
    num_f, num_fk = collect_tens(num_components[1])
    num_e, num_ek = collect_ones(num_components[2])
    num_e = num_e + 'まん'
    num_ek = num_ek + '万'
    num_d, num_dk = collect_thousands(num_components[3])
    num_c, num_ck = collect_hundreds(num_components[4])
    num_b, num_bk = collect_tens(num_components[5])
    num_a, num_ak = collect_ones(num_components[6])
    kana = num_g + num_f + num_e + num_d + num_c + num_b + num_a
    kanji = num_gk + num_fk + num_ek + num_dk + num_ck + num_bk + num_ak
elif len(num_components) == 8:
    num_h, num_hk = collect_thousands(num_components[0])
    num_g, num_gk = collect_hundreds(num_components[1])
    num_f, num_fk = collect_tens(num_components[2])
    num_e, num_ek = collect_ones(num_components[3])
    num_e = num_e + 'まん'
    num_ek = num_ek + '万'
    num_d, num_dk = collect_thousands(num_components[4])
    num_c, num_ck = collect_hundreds(num_components[5])
    num_b, num_bk = collect_tens(num_components[6])
    num_a, num_ak = collect_ones(num_components[7])
    kana = num_h + num_g + num_f + num_e + num_d + num_c + num_b + num_a
    kanji = num_hk + num_gk + num_fk + num_ek + num_dk + num_ck + num_bk + num_ak

print(kanji)
print(kana)
