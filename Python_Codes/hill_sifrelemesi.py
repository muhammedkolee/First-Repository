ilkAlfabe = {
    "A": 0,
    "B": 1,
    "C": 2,
    "Ç": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "Ğ": 8,
    "H": 9,
    "I": 10,
    "İ": 11,
    "J": 12,
    "K": 13,
    "L": 14,
    "M": 15,
    "N": 16,
    "O": 17,
    "Ö": 18,
    "P": 19,
    "R": 20,
    "S": 21,
    "Ş": 22,
    "T": 23,
    "U": 24,
    "Ü": 25,
    "V": 26,
    "Y": 27,
    "Z": 28,
    " ": 29,
    ".": 30,
    ",": 31,
    "?": 32,
    "!": 33,
    "+": 34,
    "-": 35,
    "*": 36,
    "/": 37,
    "a": 38,
    "b": 39,
    "c": 40,
    "ç": 41,
    "d": 42,
    "e": 43,
    "f": 44,
    "g": 45,
    "ğ": 46,
    "h": 47,
    "ı": 48,
    "i": 49,
    "j": 50,
    "k": 51,
    "l": 52,
    "m": 53,
    "n": 54,
    "o": 55,
    "ö": 56,
    "p": 57,
    "r": 58,
    "s": 59,
    "ş": 60,
    "t": 61,
    "u": 62,
    "ü": 63,
    "v": 64,
    "y": 65,
    "z": 66
}
sonAlfabe = {
    0: "A",
    1: "B",
    2: "C",
    3: "Ç",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "Ğ",
    9: "H",
    10: "I",
    11: "İ",
    12: "J",
    13: "K",
    14: "L",
    15: "M",
    16: "N",
    17: "O",
    18: "Ö",
    19: "P",
    20: "R",
    21: "S",
    22: "Ş",
    23: "T",
    24: "U",
    25: "Ü",
    26: "V",
    27: "Y",
    28: "Z",
    29: " ",
    30: ".",
    31: ",",
    32: "?",
    33: "!",
    34: "+",
    35: "-",
    36: "*",
    37: "/",
    38: "a",
    39: "b",
    40: "c",
    41: "ç",
    42: "d",
    43: "e",
    44: "f",
    45: "g",
    46: "ğ",
    47: "h",
    48: "ı",
    49: "i",
    50: "j",
    51: "k",
    52: "l",
    53: "m",
    54: "n",
    55: "o",
    56: "ö",
    57: "p",
    58: "r",
    59: "s",
    60: "ş",
    61: "t",
    62: "u",
    63: "ü",
    64: "v",
    65: "y",
    66: "z"
}

matris = [
    [1, 3],
    [8, 13]
]

tersmatris = [
    [11, 49],
    [19, 6]
]

def mul(arr1, arr2):
    new = [0]*2
    new[0] = (arr1[0]*arr2[0][0] + arr1[1]*arr2[1][0])%67
    new[1] = (arr1[0]*arr2[0][1] + arr1[1]*arr2[1][1])%67
    new[0] = sonAlfabe[new[0]]
    new[1] = sonAlfabe[new[1]]
    return new

def sifrele(string):
    if len(string)%2 != 0:
        string += ' '
    result = []
    arr = list(string)
    dizi = [0]*2
    for i in range(0, len(arr)-1, 2):
        dizi[0] = ilkAlfabe[arr[i]]
        dizi[1] = ilkAlfabe[arr[i+1]]
        deger = mul(dizi, matris)
        result.append(deger[0])
        result.append(deger[1])
    return "".join(result)

def sifreyiCöz(string):
    result = []
    arr = list(string)
    dizi = [0]*2
    for i in range(0, len(string)-1, 2):
        dizi[0] = ilkAlfabe[arr[i]]
        dizi[1] = ilkAlfabe[arr[i+1]]
        deger = mul(dizi, tersmatris)
        result.append(deger[0])
        result.append(deger[1])
    return "".join(result)

print(f"Şifrelenmiş mesaj:")
print(sifrele("Ne hasta bekler sabahı,"))
print(sifrele("Ne taze ölüyü mezar."))
print(sifrele("Ne de şeytan, bir günahı,"))
print(sifrele("Seni beklediğim kadar."))
print("\nAsıl mesaj:")
print(sifreyiCöz(sifrele("Ne hasta bekler sabahı,")))
print(sifreyiCöz(sifrele("Ne taze ölüyü mezar.")))
print(sifreyiCöz(sifrele("Ne de şeytan, bir günahı,")))
print(sifreyiCöz(sifrele("Seni beklediğim kadar.")))