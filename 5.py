def main(a, num):
    arr = []
    not_inc = [",", ".", "!", "?", " "]
    for i in a:
    #    ვაშორებ მძიმეებს, კითხივს ნიშნებს და ა.შ.
        if i not in not_inc:
           
                if i.isalpha(): # მხოლოდ ასოები დაამატოს
                    if i.isupper(): # ვიგებ თუ დიდი ასო არის
                        start = ord("A")
                    else:
                        start = ord("a")
                    # ჩვნეს ცხილში მოცემულ ასოებს ანუ  ვაკლებთ საწყის qereqteTs romdaviwyoT aTvala Tavidan 
                    # ამის შემდეგ ვამატებთ თუ რამედენით უნდა წასულიყო ჩვენი ასო
                    # ხოლო საბოლოოდ ვითვლი 26 ასოს რადგნა ვიცი უკვე საწყისი ასო სადაც იქენბა და შესაბამისად 26 ასოზე გამოვითვლი და ამ 26 ასოში იტრუალებს 
                    # აფერ ქეისთაც და ლუერითაც 
                    res = chr((ord(i) - start + num ) % 26 + start)
                    arr.append(res)
                else:
                    arr.append(i) 
        else:
            arr.append(i)
            
    return "".join(arr)

# print(ord('a')) გავიგე საწყისი დაორდერებული ასო ascii ცრილიდან ზემოთ დავწერე ფორმულა 
# print(ord('z'))
# print(ord('A')) აქაც გავიგე დიდი ასოს საწყისი 
# print(ord('Z'))
print(main("abc", 2))
print(main("Abc", 2))
print(main("xyz",  3))
print(main("Hello, World!", 5))
print(main("abc", -1))
print(main("ab22c", -1))