import re

def calc(*args):
    if len(args) == 2 or args[2] == None:
        if type(args[1]) != int and type(args[1]) != float:
            return f'Invalid number "{args[1]}"' 
        if args[0] == "-" or args[0] == "sub":
            return -args[1]
        elif args[0] == "+" or args[0] == "add":
            return args[1]
        else:
            return f'Invalid operator "{args[0]}"'       
    elif len(args) == 3:
        if type(args[1]) != int and type(args[1]) != float:
            return f'Invalid number "{args[1]}"'
        if type(args[2]) != int and type(args[2]) != float:
            return f'Invalid number "{args[2]}"'
        if args[0] == '+' or args[0] == "add":
            return args[1] + args[2]
        elif args[0] == '-' or args[0] == "sub":
            return args[1]-args[2]
        elif args[0] == '*' or args[0] == "mul":
            return args[1] * args[2]
        elif args[0] == '/' or args[0] == "div":
            return args[1] / args[2]
        elif args[0] == '%' or args[0] == "mod":
            return args[1] % args[2]
        elif args[0] == '^' or args[0] == "pow":
            return args[1] ** args[2]
        
def eval(*args):
    if isinstance(args[0], list):
        if len(args[0]) == 3:
            for i in range(3):
                if isinstance(args[0][i], list):
                    args[0][i] = eval(args[0][i])               
            return calc(args[0][0], args[0][1], args[0][2])
        elif len(args[0]) == 2:
            for i in range(2):
                if isinstance(args[0][i], list):
                    args[0][i] = eval(args[0][i])
            return calc(args[0][0], args[0][1])
        else:
            return f'Failed to evaluate "{args[0]}"'
    else:
        return f'Failed to evaluate "{args[0]}"'

def struct(arr):
    if len(arr) == 2:
        if arr[0] != str or chr:
            arr[0], arr[1] = arr[1], arr[0]
            return arr
    elif len(arr) == 3:
        if any(i in "(" for i in arr):
            liste = list(arr[any(i in "(" for i in arr)])
            del liste[0], liste[len(liste-1)]
            arr[any(i in "(" for i in arr)] = struct(liste)
        if arr[0] != str or chr:
            arr[0], arr[1] = arr[1], arr[0]
            return arr
    elif len(arr) % 2 != 0:
        if any(i in "(" for i in arr):
            liste = list(arr[any(i in "(" for i in arr)])
            del liste[0], liste[len(liste-1)]
            arr[any(i in "(" for i in arr)] = struct(liste)
        elif "pow" in arr or '^' in arr:
            if "pow" in arr: nick = "pow"
            else: nick = '^'
            dizi = [0]*3
            num = arr.index(nick)
            dizi[0] = arr[num]
            dizi[1] = arr[num-1]
            dizi[2] = arr[num+1]
            del arr[num], arr[num]
            arr[num-1] = dizi
            struct(arr)

            if type(arr[0]) != str and type(arr[0]) != chr:
                dizi1 = [0]*3
                dizi1[0] = arr[1]
                dizi1[1] = arr[0]
                dizi1[2] = arr[2]
                arr[0] = dizi1[0]
                arr[1] = dizi1[1]
                arr[2] = dizi1[2]
            return arr
        
        elif "mul" in arr or '*' in arr:
            if "mul" in arr: nick = "mul"
            else: nick = '*'
            dizi = [0]*3
            num = arr.index(nick)
            dizi[0] = arr[num]
            dizi[1] = arr[num-1]
            dizi[2] = arr[num+1]
            del arr[num], arr[num]
            arr[num-1] = dizi
            struct(arr)

            if type(arr[0]) != str and type(arr[0]) != chr:
                dizi1 = [0]*3
                dizi1[0] = arr[1]
                dizi1[1] = arr[0]
                dizi1[2] = arr[2]
                arr[0] = dizi1[0]
                arr[1] = dizi1[1]
                arr[2] = dizi1[2]
            return arr
        
        elif "div" in arr or '/' in arr:
            if "div" in arr: nick = "div"
            else: nick = '/'
            dizi = [0]*3
            num = arr.index(nick)
            dizi[0] = arr[num]
            dizi[1] = arr[num-1]
            dizi[2] = arr[num+1]
            del arr[num], arr[num]
            arr[num-1] = dizi
            struct(arr)

            if type(arr[0]) != str and type(arr[0]) != chr:
                dizi1 = [0]*3
                dizi1[0] = arr[1]
                dizi1[1] = arr[0]
                dizi1[2] = arr[2]
                arr[0] = dizi1[0]
                arr[1] = dizi1[1]
                arr[2] = dizi1[2]
            return arr         
            
        elif "mod" in arr or '%' in arr:
            if "mod" in arr: nick = "mod"
            else: nick = '%'
            dizi = [0]*3
            num = arr.index(nick)
            dizi[0] = arr[num]
            dizi[1] = arr[num-1]
            dizi[2] = arr[num+1]
            del arr[num], arr[num]
            arr[num-1] = dizi
            struct(arr)

            if type(arr[0]) != str and type(arr[0]) != chr:
                dizi1 = [0]*3
                dizi1[0] = arr[1]
                dizi1[1] = arr[0]
                dizi1[2] = arr[2]
                arr[0] = dizi1[0]
                arr[1] = dizi1[1]
                arr[2] = dizi1[2]
            return arr
        else:
            if len(arr[1]) < len(arr[3]):
                dizi = [0]*3
                dizi[0] = arr[1]
                dizi[1] = arr[0]
                dizi[2] = arr[2]
                arr[0] = arr[3]
                del arr[2], arr[2]
                arr[1] = dizi
                struct(arr)
                if type(arr[0]) != str and type(arr[0]) != chr:
                    dizi1 = [0]*3
                    dizi1[0] = arr[1]
                    dizi1[1] = arr[0]
                    dizi1[2] = arr[2]
                    arr[0] = dizi1[0]
                    arr[1] = dizi1[1]
                    arr[2] = dizi1[2]
                return arr
            else:
                dizi = [0]*3
                dizi[0] = arr[1]
                dizi[1] = arr[0]
                dizi[2] = arr[2]
                del arr[1], arr[1]
                arr[0] = dizi
                struct(arr)
                if type(arr[0]) != str and type(arr[0]) != chr:
                    dizi1 = [0]*3
                    dizi1[0] = arr[1]
                    dizi1[1] = arr[0]
                    dizi1[2] = arr[2]
                    arr[0] = dizi1[0]
                    arr[1] = dizi1[1]
                    arr[2] = dizi1[2]
                return arr

def get_next(string):
    if type(string) != list:
        string = string.replace(" ", "")
    arr = list(string)
    for i in range(len(arr)):
        if arr[i].isdigit():
            arr[i] = int(arr[i])
    i = 0
    while i < len(arr):
        if i+1 == len(arr):
            return arr
        if arr[i] == "(":
            if arr[i+1] == "(":
                j = i+1
                dizi = []
                while arr[j] != ")":
                    dizi.append(arr[j])
                    del arr[j]
                dizi.append(")")
                arr[i+1] = get_next(dizi)
            while arr[i+1] != ")":
                if arr[i+1] == "(":
                    j = i+1
                    dizi = []
                    while arr[j] != ")":
                        dizi.append(arr[j])
                        del arr[j]
                    dizi.append(")")
                    del arr[j]
                    arr[i+1] = get_next(dizi)
                arr[i] = str(arr[i]) + str(arr[i+1])
                del arr[i+1]
            arr[i] = str(arr[i]) + str(arr[i+1])
            del arr[i+1]
            i += 1
            continue
        if arr[i+1] == "(":
            j = i+1
            while arr[j+1] != ")":
                arr[i+1] = str(arr[i+1]) + str(arr[i+2])
                del arr[i+2]
            arr[i+1] = str(arr[i+1]) + str(arr[i+2])
            del arr[i+2]
            i += 2
            continue
        if type(arr[i]) == type(arr[i+1]):
            arr[i] = str(arr[i]) + str(arr[i+1])
            if arr[i].isdigit():
                arr[i] = int(arr[i])
            del arr[i+1]
            continue
        elif arr[i+1] == ".":
            arr[i] = str(arr[i]) + str(arr[i+1])
            del arr[i+1]
            j = i+1
            while j < len(arr):
                if j+1 == len(arr):
                    arr[i] = str(arr[i]) + str(arr[i+1])
                    del arr[i+1]
                    break
                if type(arr[j]) == type(arr[j+1]):
                    arr[j] = str(arr[j]) + str(arr[j+1])
                    if arr[j].isdigit():
                        arr[j] = int(arr[j])
                    del arr[j+1]
                    continue
                else:
                    arr[i] = str(arr[i]) + str(arr[i+1])
                    del arr[i+1]
                    arr[i] = float(arr[i])
                    break
            arr[i] = float(arr[i])
            continue
        i += 1
    return arr

def parse(string):
    string = string.replace(" ", "")
    return struct(get_next(string))


print(get_next("(1 * (15 - 4) - 8) add 3 mul 2 sub (1 + 5)"))








# print(get_next("1+3", 2)) # +
#        ["1", "2", "+", "3", "4"]













        # ["t", "e", "s", "t", "2", "3", "4", ".", "5"]
        # ["t", "e", "s", "t", 2, 3, 4, ".", 5]
        # ["test", "234.5"]

# for i in range(len(arr)):
#     if arr[i].isdigit():
#         arr[i] = int(arr[i])














# def get_next(string, index):
#     arr = re.split("([+\-*/(add)])", string)
#     arr = [i for i in arr if i != '']
#     return arr[index]
    












# def get_next(string):
#     arr = list(string)
#     for i in range(len(arr)):
#         if arr[i].isdigit():
#             arr[i] = int(arr[i])
#     i = 0
#     while i < len(arr)-1:
#         if type(arr[i]) == type(arr[i+1]):
#             arr[i] = str(arr[i]) + str(arr[i+1])
#             del arr[i+1]
#             if arr[i].isdigit():
#                 arr[i] = int(arr[i])
#             i = 0
#             continue
#         elif type(arr[i]) == int and arr[i+1] == ".":
#             arr[i] = str(arr[i]) + str(arr[i+1])
#             del arr[i+1]
#             if type(arr[i+1]) == int or arr[i+1].isdigit():
#                 arr[i] = str(arr[i]) +str(arr[i+1])
#                 del arr[i+1]
#                 arr[i] = float(arr[i])
#                 i = 0
#                 continue
#         i += 1
#     return arr












# struct([3, '*', 2])  ->  ['*', 3, 2]          
# struct([1, '+', 2, 'mul', 3])  ->  ['+', 1, ['mul', 2, 3]]   
# struct([2, 'mod', 3, '-', 4, '/', 5.2])  ->  ['-', ['mod', 2, 3], ['/', 4, 5.2]] 
            
# struct(4)  ->  Failed to structure "4"
# struct(['+'])  ->  Failed to structure "['+']"
# struct([2, '+', 3, '+'])  ->  Failed to structure "[2, '+', 3, '+']"
            
# struct([2, '?', 3])  ->  ['?', 2, 3]



