
def main():
    name = input("File name: ")
    output = media_type(name)
    print(output)

def media_type(name):
    name = name.lower().strip()
    
    if name.endswith(".gif"):
        return "image/gif"
    elif name.endswith((".jpg", ".jpeg")): #tuple used here as only 1st argument in supposed to be passed to the method.
        return "image/jpeg" #can also add start and end but 2nd is not that.
    elif name.endswith(".png"):
        return "image/png"
    elif name.endswith(".pdf"):
        return "application/pdf"
    elif name.endswith(".txt"):
        return "text/plain"
    elif name.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

if __name__ == "__main__":
    main()
