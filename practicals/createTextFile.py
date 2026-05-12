fileName = "sample.txt"
content = "Hello, This is a sample text file"

with open(fileName, "w") as file:
    file.write(content)
    print(f"Content succesfully written")