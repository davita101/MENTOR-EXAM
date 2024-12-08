def prime(n):
    # prime number ვიგებ ამ ფუქნციით
    if n < 1: 
        return False
    for i in range(2, int(n** .5) + 1):
        if n % i == 0:
            return False
    return True

# მთავირ უფნქცი რომელიც ფაქტორიალს გამოითვლის და იგებს prim numbers მხოლოდ
def main(fact):
    arr = 1
    for num in range(1, fact + 1 ):
        if prime(num):
            arr *= num
    return arr

print(main(5))
print(main(6))
print(main(7))
print(main(10))
print(main(1))