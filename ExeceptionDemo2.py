def main():
    try:
        print("Enter First number :")
        No1 = int(input())

        print("Enter Secound number :")
        No2 = int(input())

        Ans = No1 / No2
        print("Division is :",Ans)
        
    except ZeroDivisionError:
        print("Inside zero division error")
        
    except ValueError:
        print("Inside value error")
        
    except Exception:
        print("Inside last except block")

    finally:
        print("Inside finally block")
    
if __name__ == "__main__":
    main()