def main():
    n=input("Hey, whats up?")
    convert(n)
def convert(x):
    x=x.replace(":)","🙂")
    x=x.replace(":(","🙁")
    print(x)
main()