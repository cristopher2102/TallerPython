if __name__ == '_main_':
    num = int (input("Dame un numero"))
    potencia = int (input("Dame la potencia"))
    i=1
    while i<potencia:
        num=num*num
        i=i+1
    print(f"la potencia es {num}")