num=int(input("enter status code number 2,3,4,5="))

match num:
    case 2:print("success")
    case 3:print("redirect")
    case 4:print("client error")
    case 5:print("server error")
    case _:print("invalid")
