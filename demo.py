def quote(x):
    return "Hi, " + x + " just do it!"

def add(num1,num2):
    return num1 + num2 + 1

print(__name__)

if __name__ == '__main__':
    print(quote("DEV"))
    ans = add(5,10)
    print(ans)