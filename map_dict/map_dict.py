# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


def main():
    file = sys.stdin
    # reading input
    n = int(file.readline())
    
    book = dict()
    for i in range(n):
        name, number = file.readline().split()
        book[name] = number
    
    while True:
        query = file.readline().strip()
        if not query or query=="":
            break
        else:
            if query in book:
                print(query+"="+book[query])
            else:
                print("Not found")

main()
