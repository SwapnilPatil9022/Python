def Square(No):
    return (No*No)

def main():
    Data = [1,2,3,4,5]
    Result = []

    for Value in Data:
        Result.append(Square(Value))

    print("Result afer square operatiuon is ",Result)

if __name__ == "__main__":
    main()