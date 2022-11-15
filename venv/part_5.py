#Fizz Buzz

def fizz_buzz(num)->str:
    if num%5==0 and num%3==0:
        return "Fizz Buzz"
    elif num%3==0 and num%5!=0:
        return "Fizz"
    elif num%5==0 and num%3!=0:
        return "Buzz"
    else:
        return str(num)

# Оценка числа
def estimate_num(num)->str:
    return (
            "Плохо" if num%2!=0 else
            "Неплохо" if num%2==0 and num>=2 and num<=5 else
            "Так себе" if num%2==0 and num>=6 and num<=20 else
            "Отлично" if num%2==0 and num>20 else
            "Некорректное число"
            )

# последовательность
def sequence(num)->str:
    i=1
    string = ""
    while i<=num: #пока i меньше или равно полученному числу, прибавляем к результату i
        string+=str(i)
        i+=1
    return string

# Секретное сообщение
def secter_message(string)->str:
    secret = ""
    for i in string:
        if i.isupper(): #если буква большая, то прибавляем к результату
            secret+=i
    return secret


