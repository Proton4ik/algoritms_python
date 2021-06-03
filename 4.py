from hashlib import sha256


salt = "томаты в собственном соку"
cash = {}


def site(url):
    if cash.get(url):
        print("Адрес есть в кэше")
    else:
        cash[url] = sha256(salt.encode() + url.encode()).hexdigest()
        print(f"Сайт добавлен {cash}")


while True:
    page = input("Введите адрес страницы или q для завершения программы: ")
    if page == "q":
        break
    else:
        site(page)
