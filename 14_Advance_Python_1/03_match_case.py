def https_status(status):
    match status:
        case 200:
            return "OK"
        case 400:
            return "Not Found"
        case 500:
            return "Internal server error"
        case _:
            return "Unknown error"
    

print(https_status(400))