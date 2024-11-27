def parol(n):
    if n > 2 and n < 21:
        password = ""
        for x_ in range(1, n):
            for x_2 in range(1, n):
                if n % (x_ + x_2) ==0:
                    if x_ < x_2:
                        password += f"{x_}, {x_2}"
        return password
    else:
        return  "Неверный дтапозон"
n = int(input("Введите число от 3 до 20  "))
print(parol(n))

