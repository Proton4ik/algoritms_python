from hashlib import sha256

salt = "соленый огурчик"
user_pwd = input("Введите пароль: ")
hash_obj_1 = sha256(salt.encode() + user_pwd.encode()).hexdigest()
print(hash_obj_1)
while True:
    user_pwd = input("Введите пароль еще раз: ")
    hash_obj_2 = sha256(salt.encode() + user_pwd.encode()).hexdigest()
    print(hash_obj_2)
    if hash_obj_1 == hash_obj_2:
        print("Пароли совпадают")
        break
    else:
        print("Пароли не совпадают.")
