if __name__ == '_main_':
    nom = int(input("Dame un dia de la semana "))
    nomdia=""
    match nom:
        case "cris": nomdia = "31 de mayo"
        case "David": nomdia = "24 de enero"
        case "viviana": nomdia = "5 de diciembre"
        case "Ana Yeli": nomdia = "21 de diciembre"
        case "Hugo": nomdia = "28 de enero"
    print(f"La fecha de compleaños es : {nomdia}")