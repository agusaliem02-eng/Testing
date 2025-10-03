a = int(input())
b = int(input())
ope = input()

def tambah(a, b):
    return a+b

def kurang(a, b):
    return a-b

def kali(a, b):
    return a*b

def bagi(a, b):
    if b == 0:
        return "Error"
    return a/b

def operator(a, b, ope):
    if ope == '+':
        return tambah(a, b)
    elif ope == '-':
        return kurang(a, b)
    elif ope == '*':
        return kali(a, b)
    elif ope == '/':
        return bagi(a, b)
    else:
        return "Operator tidak valid"

# Output hasil
hasil = operator(a, b, ope)
print("Hasil:", hasil)