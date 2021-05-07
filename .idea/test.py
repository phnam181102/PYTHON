import textwrap

def wrap(string, max_width):
    n = len(string)
    re = []
    for i in range(0,n,max_width):
        re.append(string[i:i+max_width])
    return "\n".join(re)

if __name__ == '__main__':
    #string, max_width = input(), int(input())
    string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    max_width = 4
    result = wrap(string, max_width)
    print(result)