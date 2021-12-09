import hashlib
#from login_info import logins # This is an array containing the tuples.
logins = [('04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb',"8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),]

def hasher(string: str) -> bytes:
    stringer = bytes(string,'utf-8')
    return hashlib.sha256(stringer).hexdigest()

def login(username: str, password: str) -> int: # Returns 1 = Trueif login correct, else 0 - False.
    user = hasher(username)
    passwd = hasher(password)
    print(user)
    print(passwd)
    for i in range(len(logins)):
        if logins[i][0] == user:
            if logins[i][1] == passwd:
                return 1
            else:
                return 0
        else:
            return 0

u = hasher('user')
p = hasher('123456')
print(u)
print(p)

print(login('user','1234568'))
for item in logins:
    print(" ")
    print(item[0])
    print(item[1])
