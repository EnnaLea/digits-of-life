def sum_digits(date):
    date = list(date)
    total = sum(int(d) for d in date)

    while total > 9:
        total = sum(int(t) for t in str(total))
    return total


birthday = (input("Enter your birthday in DD/MM/YYYY format: "))
result = sum_digits(birthday)

print(result)

