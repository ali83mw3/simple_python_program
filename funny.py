

def compress(string):
    
    text = ""

    count = 1

    text += string[0]

    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count+=1
        else:
            if(count > 1):
                text += str(count)
            text += string[i+1]
            count = 1
    if(count > 1):
        text += str(count)

    return text

i = ''
a = 'Hello'
b = [ord(c) for c in a]
for c in a:
    i += str(ord(c))
j = compress(i)

def hash(x):
    while len(str(x)) < 32:
        x = (x + int('123abc', 18)) * (x << 19)
        x = (x + int('abc123', 18)) + (x >> 5)
        x = (x + int('321cba', 18)) ^ (x << 7)
        x = (x + int('213bca', 18)) * (x >> 13)
        x = (x + int('bac312', 18)) + (x << 3)
        x = (x + int('cba123', 18)) ^ (x >> 5)

    textX = str(hex(int(x)))


    while (len(textX) < 32):
        counter = 1
        x = str(x) + (counter << 5)
        counter += 1
        textX = str(hex(int(x)))
        textX = textX[2:]

    while len(textX) > 32:
        import re
        textX2 = re.sub("\D", "", textX)
        textX = str(hex(int(textX2)))
        textX = textX.replace('0x', '')    

    while (len(textX)) < 32:
        repeat = 32 - len(textX)
        textX = textX + textX[:repeat]

    print(str(textX))


def num_to_bin(num):
    return bin(num)


def bin_to_num(binary):
    return int(binary,2)

def exit():
    mes = input("Do Wanna Exit Or Not[Y/N]:")
    mes = mes.lower().startswith('y')
    if mes:
        return True
    else:
        return False
    

while True:
    program_selecte = input('\n Hello There\n\nDo Your Wanna Convert Num To Bin[1]\nor You Wanna Convert from bin to num[2]\nor you wanna Hash Something[3]?')
    if program_selecte.lower().startswith('1'):
        num = int(input("Enter Your Number To Convert from Num To Bin?"))
        print(num_to_bin(num))
        e = exit()
        if e == True:
            print("thank you bye bye.................................")
            break
        else:
            pass
    elif program_selecte.lower().startswith('2'):
        binary = input("Enter Your Binary Code Start With 0b To Convert from Binary to num:")
        print(bin_to_num(binary))
        e = exit()
        if e == True:
            print("thank you bye bye.................................")
            break
        else:
            pass
    else:
        number = int(input('Ok Hash then allright! Enter Your Number:'))
        print(hash(number))
        e = exit()
        if e == True:
            print("thank you bye bye.................................")
            break
        else:
            pass
