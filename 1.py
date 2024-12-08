# Input: ("listen", "silent") → Output: True
# 2. Input: ("triangle", "integral") → Output: True
# 3. Input: ("apple", "pale") → Output: False
# 4. Input: ("a", "a") → Output: True
# 5. Input: ("rat", "car") → Output: False


# ფუნქცია რომელიც შლის სტრინგს ელემენტებად
def splitter(a):
    return [i for i in a]

# ფუცნქიცა რომელიც ამოწემბს აკმაყოფილებს თუ არა ჩვენს მოცემულ პირობას
def funk(a,b):
    _a = splitter(a)
    _b = splitter(b) # ვიყენებ ჩემოთ დაწერილ ფუნცქიას 
    _new = []
    for char in _a:
        if char in _b:
            _new.append(char)
            _b.remove(char)
    RES = len(_new) == len(_a)
    return RES

print(funk("listen", "silent"))
print(funk("triangle", "integral"))
print(funk("apple", "pale"))
print(funk("a", "a"))
print(funk("rat", "car"))
print(funk("ll", "ll"))
print(funk("lp", "ll"))
print(funk("rrrr", "rrrs"))
print(funk("rrrr", "rrrr"))