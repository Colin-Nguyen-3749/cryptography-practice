import hashlib

# text = "Hello World!"
# hash_object = hashlib.sha256(text.encode())
# hash_digest = hash_object.hexdigest()
# print("SHA Hash of ", text, " is ", hash_object)

def hash_file(file_path):
    h = hashlib.new("sha256")

    # rb = read in binary since our hash object expects 
    # a binary 
    with open(file_path, "rb") as file:
        while True:
            
            # read chunks
            chunk = file.read(1024)
            
            # stop when empty
            if chunk == b"":
                break

            h.update(chunk)

    # return everything in hexadecimal    
    return h.hexdigest()

# this code will only run if we're running this 
# specific file, acting as a tester
if __name__ == "__main__":
    print("SHA Hash of File is: ", hash_file("C:/Users/colin/OneDrive/Desktop/Repos/cryptography-practice/venv/sample files/sample.txt"))
