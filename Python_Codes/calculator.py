def calc(operator = None, num1 = None, num2 = None):
    if num2 == None:
        if operator == '-' or operator == 'sub':
            if type(num1) != int and type(num1) != float:
                return f'Invalid number "{num1}"'
            return -num1
        elif operator == '+' or operator == 'add': 
            if type(num1) != int and type(num1) != float:
                return f'Invalid number "{num1}"'
            return num1
        else:
            return f'Invalid operator "{operator}"'
    if type(num1) != int and type(num1) != float:
        return f'Invalid number "{num1}"'
    elif type(num2) != int and type(num2) != float:
        return f'Invalid number "{num2}"'
    
    if operator == '+' or operator == 'add':
        return num1+num2
    elif operator == '-' or operator == 'sub':
        return num1-num2
    elif operator == '*' or operator == 'mul':
        return num1*num2
    elif operator == '/' or operator == 'div':
        if num2 == 0:
            return "Division by zero"
        return num1/num2
    elif operator == '%' or operator == 'mod':
        if num2 == 0:
            return "Division by zero"
        return num1%num2
    elif operator == '^' or operator == 'pow':
        return num1**num2
    else:
        return f'Invalid operator "{operator}"'
    
def eval(arr):
    if type(arr) != list:
        return f'Failed to evaluate "{arr}"'
    elif len(arr) == 2:
        if type(arr[1]) == list:
            arr[1] = eval(arr[1])
        return calc(arr[0], arr[1])
    elif len(arr) == 3:
        if type(arr[1]) == list:
            arr[1] = eval(arr[1])
            eval(arr)
        elif type(arr[2]) == list:
            arr[2] = eval(arr[2])
            eval(arr)
        return calc(arr[0], arr[1], arr[2])
    else:
        return f'Failed to evaluate "{arr}"'
    
def struct(arr):
    if type(arr) != list:
        return f'Failed to structer "{arr}"'
    
    if len(arr) == 2:
        if type(arr[0]) != str:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    
    if len(arr) % 2 == 0:
        return f'Failed to structer "{arr}"'
    
    if '^' in arr or 'pow' in arr:
        if '^' in arr:
            num = arr.index('^')
        elif 'pow' in arr:
            num = arr.index('pow')
        temp = []
        temp.append(arr[num])
        temp.append(arr[num-1])
        temp.append(arr[num+1])
        del arr[num-1], arr[num-1]
        arr[num-1] = temp
        struct(arr)

    elif '%' in arr or 'mod' in arr:
        if '%' in arr:
            num = arr.index('%')
        elif 'mod' in arr:
            num = arr.index('mod')
        temp = []
        temp.append(arr[num])
        temp.append(arr[num-1])
        temp.append(arr[num+1])
        del arr[num-1], arr[num-1]
        arr[num-1] = temp
        struct(arr)

    elif '*' in arr or 'mul' in arr:
        if '*' in arr:
            num = arr.index('*')
        elif 'mul' in arr:
            num = arr.index('mul')
        temp = []
        temp.append(arr[num])
        temp.append(arr[num-1])
        temp.append(arr[num+1])
        del arr[num-1], arr[num-1]
        arr[num-1] = temp
        struct(arr)

    elif '/' in arr or 'div' in arr:
        if '/' in arr:
            num = arr.index('/')
        elif 'div' in arr:
            num = arr.index('div')
        temp = []
        temp.append(arr[num])
        temp.append(arr[num-1])
        temp.append(arr[num+1])
        del arr[num-1], arr[num-1]
        arr[num-1] = temp
        struct(arr)
    else:

        if len(arr) > 3:
            if '+' in arr or 'add' in arr or '-' in arr or 'sub' in arr:
                    for i in range(1, len(arr), 2):
                        if arr[i] == '+' or arr[i] == 'add':
                            if arr[i] == '+':
                                name = '+'
                                break
                            elif arr[i] == 'add':
                                name = 'add'
                                break 
                        elif arr[i] == '-' or arr[i] == 'sub':
                            if arr[i] == '-':
                                name = '-'
                                break
                            elif arr[i] == 'sub':
                                name = 'sub'
                                break
                    num = arr.index(name)
                    temp = []
                    temp.append(arr[num])
                    temp.append(arr[num-1])
                    temp.append(arr[num+1])
                    del arr[num-1], arr[num]
                    arr[num-1] = temp
                    struct(arr)
                    return arr    
                        
            temp = [i for i in arr if isinstance(i, str)]
            mini = min(temp, key=len)
            temp = []
            temp.append(mini)
            temp.append(arr[arr.index(mini)-1])
            temp.append(arr[arr.index(mini)+1])
            del arr[arr.index(mini)-1], arr[arr.index(mini)+1]
            arr[arr.index(mini)] = temp
            struct(arr)
            return arr
        
    if len(arr) == 3:
        if type(arr[0]) != str:
            arr[0], arr[1] = arr[1], arr[0]
            return arr
        
    if len(arr) == 1:
        if not arr[0][0]:
            return f'Failed to structer "{arr}"'
        if len(arr[0]) == 1:
            return f'Failed to structer "{arr}"'
        return arr[0]
    if len(arr) < 3:
        return arr[0]
    return arr

print(struct([2, '?', 3])) #--> ['?', 2, 3]
print(struct([3, 'test', 4.3, '+', 1])) #--> ['test', 3, ['+', 4.3, 1]]
print(struct([1, 't', 3, '??', 5]))  #--> ['??', ['t', 1, 3], 5]
print(struct([1, '+', 2, 'mol', 3, '+', 4])) # --> ['mol', ['+', 1, 2], ['+', 3, 4]]

print("")

print(struct(['add', 5]))

print("")

print(struct([2, '-', 3]))                           #--> ['-', 2, 3]
print(struct([1, '-', 3, '+', 2]))                   #--> ['+', ['-', 1, 3], 2]
print(struct([1, '+', 2, '+', 3, '+', 4]))           #--> ['+', ['+', ['+', 1, 2], 3], 4]
print(struct([1, 'sub', 2, 'add', 3, 'sub', 4]))     #--> ['sub', ['add', ['sub', 1, 2], 3], 4] ▓

print("")

print(struct([3, '*', 2]))                           #--> ['*', 3, 2]
print(struct([1, '+', 2, '*', 3]))                   #--> ['+', 1, ['*', 2, 3]]
print(struct([2, '%', 3, '-', 4, '/', 5.2]))         #--> ['-', ['%', 2, 3], ['/', 4, 5.2]]
print(struct([1, 'add', 2, 'mod', 3, '-', 4]))       #--> ['-', ['add', 1, ['mod', 2, 3]], 4]   
print(struct([5, '-', 5, 'mul', 5, 'div', 5]))       #--> ['-', 5, ['div', ['mul', 5, 5], 5]]

print("")

print(struct([2, '^', 3]))                           #--> ['^', 2, 3]
print(struct([4, '*', 2, 'pow', 3]))                 #--> ['*', 4, ['pow', 2, 3]]
print(struct([3, '^', 4, 'div', 2, 'pow', 3]))       #--> ['div', ['^', 3, 4], ['pow', 2, 3]]

print("")

print(struct(['-', 5]))             #--> ['-', 5]
print(struct([2, '-', 5]))          #--> ['-', 2, 5]
print(struct(['add', 5]))           #--> ['add', 5]

print("")

print(struct(4))                    #--> Failed to structure "4"
print(struct(['+']))                #--> Failed to structure "['+']"                   
print(struct([2, '+', 3, '+']))     #--> Failed to structure "[2, '+', 3, '+']"        
print(struct([2, 'mul', '+']))      #--> ['mul', 2, '+']