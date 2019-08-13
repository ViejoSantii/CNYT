from sys import stdin
import math

def suma(a,b):
    S = (a[0]+b[0],a[1]+b[1])
    print(complex(S[0],S[1]))
def resta(a,b):
    R = (a[0]-b[0],a[1]-b[1])
    print(complex(R[0],R[1]))        
def multiplicacion(a,b):
    a1 = complex(a[0],a[1])
    b1 = complex(b[0],b[1])
    M = a1 * b1
    print(M)
def modulo(a,b):
    mod = complex(a[0],a[1])
    mod2 = complex(b[0],b[1])
    print(abs(mod))
    print(abs(mod2))   
def conjugado(a,b):
    C = complex(a[0],a[1])
    C2 = complex(b[0],b[1])
    print(C.conjugate())
    print(C2.conjugate())
def division(a,b):
    D = complex(a[0],a[1])
    D2 = complex(b[0],b[1])
    print(D/D2)
def producto(a,b):
    print("Ingrese escalar")
    escalar = int(stdin.readline().strip())
    pro = complex(a[0],a[1])
    pro2 = complex(b[0],b[1])
    print(escalar*pro)
    print(escalar*pro2)
def fase(a,b):
    f = (a[0],a[1])
    f1 = (b[0],b[1])
    rad = math.atan(f[1]/f[0])
    rad2 = math.atan(f1[1]/f1[0])
    print((rad*180)/math.pi)
    print((rad2*180)/math.pi)  
def main():
    print("Ingrese numeros complejos para operar")
    a = [int(x) for x in stdin.readline().strip().split()]
    b = [int(x) for x in stdin.readline().strip().split()]
    print("Que operacion desea realizar?")
    print("1. Sumar")
    print("2. Multiplicacion")
    print("3. Resta")
    print("4. Division")
    print("5. Modulo")
    print("6. Conjugado")
    print("7. Producto por escalar")
    print("8. Fase numero complejo")
    print("9. Conversion polar y cartesiano")
    op = int(stdin.readline().strip())
    if op == 1:
        suma(a,b)
    elif op == 2:
        multiplicacion(a,b)
    elif op == 3:
        resta(a,b)
    elif op == 4:
        division(a,b)
    elif op == 5:
        modulo(a,b)
    elif op == 6:
        conjugado(a,b)
    elif op == 7:
        producto(a,b)
    elif op == 8:
        fase(a,b)
main()


