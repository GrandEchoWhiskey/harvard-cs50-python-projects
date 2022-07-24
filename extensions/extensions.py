types = {
    '.gif': "image/gif",
    '.jpg': "image/jpeg",
    '.jpeg': "image/jpeg",
    '.png': "image/png",
    '.pdf': "application/pdf",
    '.txt': "text/plain",
    '.zip': "application/zip"
}

def main():
    name = input("File name: ")
    ext = name.split('.')[-1].lower().replace(' ', '')
    if '.'+ext in types.keys():
        print(types['.'+ext])
        return
    print("application/octet-stream")
    return

if __name__ == "__main__":
    main()