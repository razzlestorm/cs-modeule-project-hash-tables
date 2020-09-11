import string
from collections import Counter
def word_count(s):
    output = s
    for ele in output:  
        if ele in '":;,.-+=/\|[]}{()*^&':  
            output = output.replace(ele, "")

    output = output.lower()
    print(output)    
    return dict(Counter(output.split()))



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))