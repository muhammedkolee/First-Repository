listNum = {
    'one': 1,
    'two': 2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
    'ten':10,
    'eleven':11,
    'twelve':12,
    'twenty':20,
    'thirty':30,
    'forty':40,
    'fifty':50,
    'sixty':60,
    'seventy':70,
    'eighty':80,
    'ninety':90,
    'hundred':100,
    'thousand':1000,
    'million':1000000
}

result = 0
text = input("Enter the number as a text: ")
text = text.lower()

if 'teen' in text:
    listText = text.split()
    for i in range(len(listText)):
        if 'teen' in listText[i]:
            listText[i] = listText[i].replace('teen', '')
            result += listText[i]
            listText.remove(listText[i])

else:
    listText = text.split()

for i in listText:
    if i == 'million' or i == 'thousand' or i == 'hundred':
        result *= listNum[i]
    else:
        result += listNum[i]

print(result)