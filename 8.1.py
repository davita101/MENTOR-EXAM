def main(arr, k):
    # თუ ცარიელი მასივი ან მეტი იყო k - th რიცხვზე მეტი 
    if(arr == []):
        return []
    if(k > len(arr)): return []
    # საბოლოდ კი ვასორტიტებ და kt- 1 რიცხვს და ვიღებთ პაუსხს
    return sorted(arr)[k-1]

print(main([3, 2, 1, 5, 6, 4], 2))
print(main([3, 2, 1, 5, 6, 4], 4))
print(main([7, 10, 4, 3, 20, 15], 3))
print(main([1, 2, 3, 4, 5], 1))
print(main([1, 2, 3, 4, 5], 5))
print(main([1, 2, 3, 4, 5], 6))

print(main([], 3))