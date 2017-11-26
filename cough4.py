def main():
    cough(3)
    sneeze(3)

def cough(n):
    say("cough", n)

def say(k,n):
    for i in range(n):
        print(k)

def sneeze(n):
    say("achoo", n)

main()