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
    " ": 29
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
    29: " "
}

matris = [
    [1, 3],
    [8, 13]
]

tersmatris = [
    [7, 3],
    [28, 19]
]

def mul(arr1, arr2):
    new = [0]*2
    new[0] = (arr1[0]*arr2[0][0] + arr1[1]*arr2[1][0])%30
    new[1] = (arr1[0]*arr2[0][1] + arr1[1]*arr2[1][1])%30
    new[0] = sonAlfabe.get(new[0])
    new[1] = sonAlfabe.get(new[1])
    return new
def sifrele(string):
    result = []
    string = string.upper()
    arr = list(string)
    dizi = [0]*2
    for i in range(0, len(arr)-1, 2):
        dizi[0] = ilkAlfabe.get(arr[i])
        dizi[1] = ilkAlfabe.get(arr[i+1])
        deger = mul(dizi, matris)
        result.append(deger[0])
        result.append(deger[1])
    return "".join(result)
def sifreyiCöz(string):
    result = []
    arr = list(string)
    dizi = [0]*2
    for i in range(0, len(string)-1, 2):
        dizi[0] = ilkAlfabe.get(arr[i])
        dizi[1] = ilkAlfabe.get(arr[i+1])
        deger = mul(dizi, tersmatris)
        result.append(deger[0])
        result.append(deger[1])
    return "".join(result)

print(f"Şifrelenmiş mesaj: {sifrele('bugün seni eskisinden daha çok özledim')}\nAsıl mesaj: {sifreyiCöz(sifrele('bugün seni eskisinden daha çok özledim'))}")