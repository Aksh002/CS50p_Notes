def main():
    plate=input("Plate: ")
    if is_valid(plate):
        print("VALID")
    else:
        print("INVALID")
def is_valid(n):
    if len(n)==6:
        for i in n:
            if i<int((len(n))/2) and i not in (1,2,3,4,5,6,7,8,9) and i[0] != 0:
                return True
            else:
                return False
    else:
        return False
if __name__=="__main__":
    main()