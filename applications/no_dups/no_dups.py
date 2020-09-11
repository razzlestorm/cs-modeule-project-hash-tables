from collections import Counter

def no_dups(s):
    string = ''
    c = Counter(s.split())
    for x in c.keys():
        string += x
        string += ' '
    return string.strip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))