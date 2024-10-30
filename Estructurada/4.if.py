if __name__ == '_main_':

    a = int(input("Teclea e ingresa un numero: "))
    b = int(input("Teclea e ingresa un numero más: "))
    c = int(input("Teclea e ingresa un numero: "))

    if a > b:
        if a > c:
            print(f"el mayor es {a}")
        else:
            print(f"el mayor es {c}")

    elif b > c:
        print(f"el mayor es {b}")
    else:
        print(f"el mayor es {c}")