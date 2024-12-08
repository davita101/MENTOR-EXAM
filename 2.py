# Write a function that counts the number of unique words in a string, ignoring case sensitivity
# and punctuation.
# Test Cases:
# 1. Input: "The quick brown fox jumps over the lazy dog" → Output: 8
# 2. Input: "Hello hello world!" → Output: 2
# 3. Input: "" → Output: 0
# 4. Input: "Python is fun. Python is cool." → Output: 4
# 5. Input: "One word" → Output: 2

# ფუნცქიცა რომელიც შლის პუნქტუციურ ნიშნებს 
def remove_punctuation(a):
    arr = [",", ".", "!", "?"]
    _a = a
    for i in arr:
        _a = _a.replace(i, "")
    return _a
# ყველა ასოს აპატავრებს და აგდებს ყველა გამოერებულ სიტყვას
def make_all_low(a):
    _a = [i.lower() for i in remove_punctuation(a).split()]
    for i in _a:
        if _a.count(i) > 1:
          _a.remove(i)
    
    return _a

# საბლო შედეგი
def main(a):
    if len(make_all_low(a)) == 0:
        return 0
    _a = len(make_all_low(a))
    return _a

print(main("The quick brown fox jumps over the lazy dog"))
print(main("Hello hello world!"))
print(main(""))
print(main("Python is fun. Python is cool."))
print(main("One word"))
print(main("One word ! Lomi ,3"))
        
    