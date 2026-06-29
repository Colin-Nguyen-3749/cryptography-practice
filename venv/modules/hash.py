import hashlib

text = "Hello World!"
hash_object = hashlib.sha256(text.encode())
hash_digest = hash_object.hexdigest()
print("SHA Hash of ", text, " is ", hash_object)