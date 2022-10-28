import random

print("Welcome to Password Generator")
letters_lower = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
letters_upper = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
symbols = ['@', '&', '%', '$', '!', '#', '^', '(', ')']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

capital_char=int(input("How many uppecase charecters do you want in your password?: "))
small_char=int(input("How many lowercase charecters do you want in your password?: "))
symbol=int(input("How many symbols do you want in your password?: "))
number=int(input("How many numbers do you want in your password?: "))
def generate_pwd(input1,input2,input3,input4):
    if((capital_char>len(letters_upper)) or (small_char>len(letters_lower )) or (symbol>(len(symbols))) or (number>(len(numbers)))):
        print("invalid input")
    else:
        final_password=[]
        passwrod=""
        for i in range(capital_char):
            random_upper=random.randint(0,len(letters_upper)-1)
            final_password.append(letters_upper[random_upper])

        for j in range(small_char):
            random_lower=random.randint(0,len(letters_lower)-1)
            final_password.append(letters_lower[random_lower])

        for s in range(symbol):
            random_symbol=random.randint(0,len(symbols)-1)
            final_password.append(symbols[random_symbol])
        for n in range(number):
            random_num=random.randint(0,len(numbers)-1)
            final_password.append(numbers[random_num])
        random.shuffle(final_password)
    return("".join(final_password))
print(generate_pwd(capital_char,small_char,symbol,number))


