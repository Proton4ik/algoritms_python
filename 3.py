from hashlib import sha256


my_set = set()
my_str = "papa"
for i in range(len(my_str)):
    for j in range(i + 1, len(my_str) + 1):
        if my_str[i:j] != my_str:
            my_set.add(sha256(my_str[i:j].encode()).hexdigest())
print(f'\n'.join(my_set), f'\nКоличество подстрок: {len(my_set)}')
