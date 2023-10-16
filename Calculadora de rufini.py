print("                           ************************** ")
print("                           * Calculadora de Ruffini * ")
print("                           ************************** ")
grado = int(input("-Introduzca la cantidad de grados(4 como maximo) que tendra el polinomio: "))

if (grado == 1):
    int_1 = int(input("-introduzca el primer numero: " ))
    int_2 = int(input("-introduzca el segundo numero: " ))
    print("tu polinomio es:" ,int_1,"x",int_2)
    raiz = int(input("ahora introduzca la raiz por la cual se va a dividir al polinomio: "))
    n1 = int_1
    n2 = (n1 * raiz) + int_2
    while n2 != 0: 
            print(raiz, "no es raiz, intente nuevamente...")
            raiz = input()
    print(raiz,"es raiz y tu polinomio es: ",n1)


if (grado == 2):
    int_1 = int(input("-introduzca el primer numero: " ))
    int_2 = int(input("-introduzca el segundo numero: " ))
    int_3 = int(input("-introduzca el tercer numero: " ))
    print("tu polinomio es:" ,int_1,"x² ",int_2,"x ",int_3)
    raiz = int(input("ahora introduzca la raiz por la cual se va a dividir al polinomio: "))
    n1 = int_1
    n2 = (int_1 * raiz) + int_2
    n3 = (int_2 * raiz) + int_3
    if (n3 == 0): 
        print("tu polinomio es: ",n1,"x",n2)
    else:
        print(raiz, "no es raiz, intente nuevamente")
        

if (grado == 3):
    int_1 = int(input("-introduzca el primer numero: " ))
    int_2 = int(input("-introduzca el segundo numero: " ))
    int_3 = int(input("-introduzca el tercer numero: " ))
    int_4 = int(input("-introduzca el cuarto numero: " ))
    print("tu polinomio es:" ,int_1,"x³ ",int_2,"x² ", int_3,"x " ,int_4)
    raiz = int(input("ahora introduzca la raiz por la cual se va a dividir al polinomio: "))
    n1 = int_1
    n2 = (int_1 * raiz) + int_2
    n3 = (int_2 * raiz) + int_3
    n4 = (int_3 * raiz) + int_4
    if (n4 == 0): 
        print("tu polinomio es: ",n1,"x²",n2,"x",n3)
    else:
         print(raiz, "no es raiz, intente nuevamente")

if (grado == 4):
    int_1 = int(input("-introduzca el primer numero: " ))
    int_2 = int(input("-introduzca el segundo numero: " ))
    int_3 = int(input("-introduzca el tercer numero: " ))
    int_4 = int(input("-introduzca el cuarto numero: " ))
    int_5 = int(input("-introduzca el quinto numero: " ))
    print("tu polinomio es:" ,int_1,"x⁴ ",int_2,"x³ ",int_3,"x² ",int_4,"x ",int_5)
    raiz = int(input("ahora introduzca la raiz por la cual se va a dividir al polinomio: "))
    n1 = int_1
    n2 = (n1 * raiz) + int_2
    n3 = (n2 * raiz) + int_3
    n4 = (n3 * raiz) + int_4
    n5 = (n4 * raiz) + int_5
    if (n5 == 0): 
        print("tu polinomio es: ",n1,"x³",n2,"x²",n3,"x",n4)
    else:
        print(raiz, "no es raiz, intente nuevamente")

