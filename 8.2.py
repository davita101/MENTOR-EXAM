def main(x, n):
    
    seq = [1]* x
    for i  in range(x, x + n):
        seq.append(seq[:x])
    return seq
print(main(1, 10))
# print(main(5, 10))