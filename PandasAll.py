import pandas as pd
import matplotlib.pyplot as plt

def Matplotlib():
    excel_file = 'Marvellous.xlsx'
    data = pd.read_excel(excel_file)

    print("All data from excel file")
    print(data)

    print("First 5 rows from file")
    print(data.head())

    print("First 4 rows from file")
    print(data.head(4))

    print("First 3 rows from file")
    print(data.tail(3))

    print(data.shape)

    Sorted_data = data.sort_values(['Name'],ascending = False)
    print("Sorted data")
    print(Sorted_data)

    data['Age'].plot(kind="hist")
    plt.show()

    data['Age'].plot(kind="barh")
    plt.show()

def main():
    Matplotlib()

if __name__ == "__main__":
    main()

