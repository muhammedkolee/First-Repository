import turtle

def maskify(cc):
    liste = list(str(cc))
    for i in range(len(liste) - 4):
        liste[i] = '#'
    metin = ''.join(liste)
    return metin

def count_bits(n):
    liste = list(str(n))
    count = 0
    for i in range(len(liste)):
        if liste[i] == '0':
            count += 0
        elif liste[i] == '1' or liste[i] == '2' or liste[i] == '4' or liste[i] == '8':
            count += 1
        elif liste[i] == '3' or liste[i] == '5' or liste[i] == '6' or liste[i] == '9':
            count += 2
        elif liste[i] == '7':
            count += 3
        else:
            return "Something Wrong!"
    return count

def digital_root(n):    
    count = 0
    if n > 9:
        liste = list(str(n))
        for i in range(len(liste)):
            count += int(liste[i])
        if count > 9:
            x = digital_root(count)
            return x
        else:
            return count
    else:
        return n

def title_ends_with(book_title, ending):
    return book_title.lower().endswith(ending.lower())

def calculate(num):
    global say
    if num > 9:
        count = 1
        for i in str(num):
            count *= int(i)
        say += 1
        calculate(count)
    else:
        return 0

def hearth():
    window = turtle.Screen()
    t = turtle.Turtle()
    window.bgcolor("black")

    t.setposition(0, -100)
    t.color("red", "red")
    t.pensize(3)
    t.begin_fill()
    t.right(-45)
    t.forward(200)
    t.circle(100, 180)
    t.right(90)
    t.circle(100, 180)
    t.forward(200)

    t.end_fill()

    t.setpos(-80, 50)
    t.color("white")
    t.write("AŞIĞIM SANA", font=("Arial", 20, "bold"))
    t.ht()

    window.exitonclick()

def extract_domain(url):
    dizi = url.split("/")
    return dizi[2]

def is_leap_year(year):
    return bool(year%4 == 0)

def CodelandUsernameValidation(strParam):
    letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'z', 'x', 'w', 'q'}
    if 4 <= len(strParam) <= 25:
        if(list(strParam)[len(strParam) - 1] != "_"):
            if list(strParam)[0] in letters:
                return "true"
            else:
                return "false"
        else:
            return "false"
    else:
        return "false"

def LongestWord(sen):
    dizi = sen.split(" ")
    for i in range(len(dizi)):
        for j in range(1, len(dizi)):
            if len(dizi[i]) >= len(dizi[j]):
                max = dizi[i]
            else:
                max = dizi[j]
    for i in range(len(sen)):
        if len(max) >= len(dizi[i]):
            return max
        else:
            dizi.remove(max)
            metin = ''.join(dizi)
            LongestWord(metin)
            
def count_occurrences(str, ch):
    count = 0
    for i in str:
        if i == ch:
            count = count + 1
    return count

def func(num):
    result = 0
    for i in range(1, 10001):
        result += i
    return f"{result}\n" * num
  
def sigma(n):
    result = 0
    for i in range(n+1):
        result += i
    return result

def are_anagrams(str1, str2):
    arr1 = list(str1)
    arr2 = list(str2)
    count = 0
    for i in str1:
        for j in str2:
            if i == j:
                count += 1
                break
    if count == len(arr1):
        return True
    else:
        return False
    
def change_element(lst, index, new_element):
    lst[index] = new_element
    return lst

def ratio(x):
    if x[0] == 7 and x[1] == 8 and x[2] == 9:
        return True
    else:
        return False
    
def merge(lst1, lst2):
    arr_size = len(lst1) + len(lst2)
    arr = [0] * arr_size
    for i in range((len(lst1))):
        arr[i] = lst1[i]
    for i in range(len(lst2)):
        arr[i+len(lst1)] = lst2[i]
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr 

def reverse(lst):
    return lst[::-1]

def tree(n):
    for i in range(1, n+2, 2):
        if n != i:
            print(" "*(int(((n+2)-i)/2)-2), "*"*i, " "*(int(((n+2)-i)/2)-2))
        elif n == i:
            print("*"*i)

def transpose(lst):
    if len(lst) == 0 or len(lst) == 1:
        if lst[0][1] != "":
            arr1 = lst[0][0]
            arr2 = lst[0][1]
            return f"[[{arr1}], [{arr2}]]"
        else:
            return lst
    else:
        for i in range(0, len(lst)-1):   
            for j in range(i+1, len(lst)):
                lst[i][j], lst[j][i] = lst[j][i], lst[i][j]        
        return lst
    
def adversarial_color(a_string):
    return a_string.replace("red", "green").replace("blue", "green")

def remove(s, i):
    arr = list(s)
    del arr[i]
    return "".join(arr)

def fibo(i):
    if i == 0:
        return 0
    if i == 1 or i == 2:
        return 1
    if i > 2:
        return fibo(i-1) + fibo(i-2)
    
def isPrime(num):
    for i in range(2, num-1):
        if num % i == 0:
            return False       
    return True
        
def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return fact(num-1) * num

def isPalindrome(num):
    arr = list(str(num))
    if str(num) == "".join(arr[::-1]):
        return True
    else:
        return False
    
def reverse_words(sentence):
    arr = sentence.split(" ")
    return " ".join(arr[::-1])

def lens(arr):
    nums = [0]*len(arr)
    for i in range(len(arr)):
        nums[i] = len(str(arr[i]))
    return nums

def alternate(a1, a2):
    j = 0
    arr = [0]*(len(a1)+len(a2))
    for i in range(len(a1)):
        arr[j] = a1[i]
        arr[j+1] = a2[i]
        j += 2
    return arr

def rotate(arr):
    arr.insert(0, arr[len(arr)-1])
    arr.pop()
    return arr

def sort(s):
    return "".join(sorted(s))

def sum_proper_divisors(n):
    count = 0
    for i in range(1, int(n/2)+1):
        if n%i == 0:
            count += i
    return count


#***
def occurMax(a):
    max_count = 0
    max_value = None
    for i in a:
        count = 0
        for j in a:
            if i == j:
                count += 1
        if count > max_count:
            max_count = count
            max_value = i
    return max_value


#***
def longestCommonPrefix(a):
    if not a:
        return ""

    önek = a[0]
    for s in a[1:]: 
        i = 0
        while i < len(önek) and i < len(s) and önek[i] == s[i]:  
            i += 1
        önek = önek[:i]  
    return önek


#***
def whatToBuy(prices, quantities, price_restriction, construction_names):
    items_removed = 0
    affordable_names = []

    for price, quantity, name in zip(prices, quantities, construction_names):
        total_price = (quantity * price) / (sum(quantities) / len(quantities) * sum(prices) / len(prices))
        if total_price <= price_restriction:
            affordable_names.append(name)
        else:
            items_removed += 1

    return [sorted(affordable_names), items_removed]
    
def seconds_to_minutes_seconds(s):
    if s == 0:
        return f"00:00:00"
    if s >= 60:
        minute = int(s/60)
        if minute >= 60:
            hour = int(minute/60)
            if hour < 10 and minute%60 < 10 and s%60 < 10:
                return f"0{hour}:0{minute%60}:0{s%60}"
            elif hour < 10 and minute%60 < 10:
                return f"0{hour}:0{minute%60}:{s%60}"
            elif hour < 10:
                return f"0{hour}:{minute%60}:{s%60}"
            elif minute%60 < 10:
                return f"{hour}:0{minute%60}:{s%60}"
            elif s%60 < 10:
                return f"{hour}:{minute%60}:0{s%60}"
            elif hour < 10 and s%60 < 60:
                return f"0{hour}:{minute%60}:0{s%60}"
            elif minute%60 < 10 and s%60 < 60:
                return f"{hour}:0{minute%60}:0{s%60}"
            return f"{hour}:{minute%60}:{s%60}"
        else:
            if minute%60 < 10 and s%60 < 60:
                return f"00:0{minute}:0{s%60}"
            elif minute%60 < 10:
                return f"00:0{minute}:{s%60}"
            elif s%60 < 60:
                return f"00:{minute}:0{s%60}"
            return f"00:{minute}:{s%60}"
    else:
        return f"00:00:{s}"
    
def find_missing_number(arr):
    numbers = [0,1,2,3,4,5,6,7,8,9]
    for num in numbers:
        if num not in arr:
            return num
        
def calc(operator = None, num1 = None, num2 = None):
    if operator == None and num1 == None and num2 == None:
        return "Please entry value"
    elif num2 == None:
        if type(num1) != int and type(num1) != float:
            return f'Invalid number "{num1}"'
        if operator == "+" or operator == "add":
            return num1
        elif operator == "-" or operator == "sub":
            return -num1
        else:
            return f'Invalid operator "{operator}"'
    else:
        if type(num1) != int and type(num1) != float:
            return f'Invalid number "{num1}"'
        if type(num2) != int and type(num2) != float:
            return f'Invalid number "{num2}"'
        if operator == "add" or operator == "+":
            return num1 + num2
        elif operator == "sub" or operator == "-":
            return num1 - num2
        elif operator == "div":
            if num2 == 0:
                return "Division by zero"
            return num1 / num2
        elif operator == "mul":
            return num1 * num2
        elif operator == "pow":
            return num1 ** num2
        elif operator == "mod":
            if num2 == 0:
                return "Division by zero"
            return num1 % num2
        else:
            return f"Invalid operator {operator}"
        
def decimal_to_binary(num):
    if num == 0:
        return 0
    dec = ""
    while num > 0:
        dec = str(num%2) + dec 
        num //= 2
    return dec
    
def nth_catalan_number(n):
    return int((1/(n + 1)) * (fact(2*n) / (fact(n) ** 2)))

def is_omnipresent(a, n):
    for i in a:
        if n in i:
            continue
        else:
            return False
    return True

def levenshtein_distance(s1, s2):
    arr1 = list(s1)
    arr2 = list(s2)
    if len(arr1) == len(arr2):
        count = 0
        for i in range(len(arr2)):
            if arr1[i] == arr2[i]:
                count += 1
        return len(arr1)-count
    count = 0
    for i in range(len(arr1)-1):
        if arr1[i] == arr2[i]:
            count += 1
            continue
        elif arr1[i] == arr2[i+1]:
            count += 1
            continue
        if len(arr2) != i+2:
            if arr1[i] == arr2[i+2]:
                count += 1
                continue
    return len(arr2) - count

def euclidAlgorithm(num1, num2):
    if num1 > num2:
        return euclidAlgorithm(num2, num1)
    
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

