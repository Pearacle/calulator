from calculator.operation import multiplication

param1 = int(input('Entrer un premier nombre :'))
param2 = int(input("Entrer un second nombre :"))
if __name__ == "__main__":
    add = multiplication(param1, param2)
    multiple = multiplication(param1, param2)
    print('La multiplication des deux nombres est: ', multiple)
    print("L\'addition des deux nombres est: ", add)