def count(a,b):
    counter = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            counter += 1
    return counter


if __name__ == '__main__':
    data = open('datasets/rosalind_hamm.txt').read()
    a, b = data.split()
    print(count(a,b))