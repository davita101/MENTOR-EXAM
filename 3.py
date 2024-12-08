# . Reverse the Order of Words in a Sentence
# Task:
# Write a function that takes a sentence and reverses the order of its words.
# Test Cases:
# Input: "Hello World" → Output: "World Hello"
# Input: "Python is great" → Output: "great is Python"
# Input: "a b c" → Output: "c b a"
# Input: "" → Output: ""
# Input: " Spaces " → Output: "Spaces"

# გავხლჩე სტრინგი დავარევერსე და დავაჯოინე 
def main(a):
    _a = " ".join(a.split()[::-1])
    return _a

print(main("Hello World"))
print(main("Python is great"))
print(main("a b c"))
print(main(""))
print(main(" Spaces "))