file = input("Enter file's name: ").strip().lower()

if "." in file:
    file = "." + file.rpartition(".")[2]
    match file:
        case ".jpg" | ".jpeg":
            print("image/jpeg")
        case ".pdf":
            print("application/pdf")
        case ".gif":
            print("image/gif")
        case ".png":
            print("image/png")
        case ".txt":
            print("text/plain")
        case ".zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

else:
    print("application/octet-stream")
