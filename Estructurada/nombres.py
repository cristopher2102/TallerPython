if __name__ == '__main__':
    nom = input("Dame un nombre ")
    fecha=""
    match nom:
        case "cris": fecha = "31 de mayo"
        case "David": fecha = "24 de enero"
        case "viviana": fecha = "5 de diciembre"
        case "Ana Yeli": fecha = "21 de diciembre"
        case "Hugo": fecha = "28 de enero"
    print(f"La fecha de compleaños es : {fecha}")
else:
    print("te equvocaste en el main")
