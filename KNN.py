from sklearn import tree

# Laod the dataset
# Football 0
# Cricket  1
# Neither  2

# Male = 0
# Female = 1

def ToyCaseStudy(Age, Zender):
    Features = [[32,0],[40,0],[16,1],[34,1],[55,0],[40,0],[20,1],[15,0],[55,0],[15,0]]

    Labels = [0,2,1,1,2,1,2,1,0,0]

    # design the machine learning algoritham
    obj = tree.DecisionTreeClassifier()

    # perform the trening model
    obj = obj.fit(Features, Labels)

    # perform the testing
    ret = (obj.predict([[Age, Zender]]))
    if ret == 0:
        print("Your objects look like Football")
    elif ret == 1:
        print("Your objects look like Cricket")
    elif ret == 2:
        print("Your objects look like Neither")
    
def main():
    print("-----------------Toy Case Study-------------------")
    
    print("Enter your age.")
    Age = int(input())
    
    print("Enter your zender(male / female)")
    Zender = input()
    
    if Zender.lower() == "male":
        Zender = 0
    elif Zender == "female":
        Zender = 1
    else:
        print("Invalid syntax...")
        exit()
   
    ToyCaseStudy(Age, Zender)
    
if __name__ == "__main__":
    main()