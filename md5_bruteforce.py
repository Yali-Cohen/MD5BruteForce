import hashlib
HASH_PASS = "0a7eab610f12cb73aa0a4aa7c0acf691"
for i in range(1000000,10000000):
    if hashlib.md5(str(i).encode()).hexdigest() == HASH_PASS:
        print(f"The password is {i} of the hashed md5 password")
        break
else:
    print("Password not found")
