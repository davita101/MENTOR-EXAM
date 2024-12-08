# Task:
# Write a function to generate Pascal's Triangle up to the specified number of rows.
# Test Cases:
# 1. Input: 1 → Output: [[1]]
# 2. Input: 2 → Output: [[1], [1, 1]]
# 3. Input: 3 → Output: [[1], [1, 1], [1, 2, 1]]
# 4. Input: 5 → Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6,
# 4, 1]]
# 5. Input: 0 → Output: []

def main(a):
    # თუ 0 არის დააბურნოს 0
    if a == 0:
        return 0
    # ცარიელი ლისტი სადაც პასუხს დავაბურნებთ
    res = []
    for char in range(a):
        # ლისტი რომელიც არის 1
        arr = [1]
        # თუ არ იყო დამატებული პასუხი res ში მაშინ დავამატოთ [1]
        if(res):
            # როცა გავიგებთ რომ [1] არის ჩვენს სამკუთხედში 
            # ფორ ლუპს გამოვიყენბთ რომ დავამატო ბოლო და მომდევნო რიცხვის ჯამი
            for i in range(len(res[-1])-1):
                #               ბოლო    მმდევნო
                arr.append(res[-1][i] + res[-1][i + 1])
            # საბოლოდ კი 1 დამეტაოს მასივს რადგნა სამკუთხედი ესე მუშაობს ;))
            arr.append(1)
        res.append(arr)
    return res


print(main(1))
print(main(2))
print(main(3))
print(main(4))
print(main(5))
print(main(0))