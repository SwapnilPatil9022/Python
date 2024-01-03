





import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('RSL_superadmin.Swapnil.csv')

# Extracting labels and counts
categories = data['NO']
counts = data['chat']

# Plotting the bar graph
plt.figure(figsize=(8, 6))
plt.bar(categories, counts, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph of Categories and Values')
plt.xticks(rotation=45)  # Rotating x-axis labels for better readability
plt.tight_layout()

# Show the plot
plt.show()

















"""

import pymongo
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient


# डेटाबेसमध्ये मिळालेल्या डेटाची Pandas DataFrame मध्ये रूपांतरित करा
data = pd.read_csv('RSL_superadmin.Swapnil.csv')

print(data)

categories = data['Name'].unique()
category_mapping = {cat: i for i, cat in enumerate(categories)}
data['Category_Numeric'] = data['Name'].map(category_mapping)

plt.bar(data['Category_Numeric'], data['PinCode'])
plt.xlabel('Name')
plt.ylabel('PinCode')
plt.title('String Format Data from CSV file')
plt.xticks(data['Category_Numeric'], data['Name'])  # Set x-axis ticks as original categories
plt.show()




"""


















"""

import pymongo
from datetime import datetime
import matplotlib.pyplot as plt

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]  # Replace 'your_database_name' with your database name
collection = db["user_stats"]  # Collection to store user statistics

def update_user_stats(Name,Business_Name,Email,Phone,City,PinCode,Password,Confirm_Password,):
    # Create a document to insert into the collection 
    stats = {
        "timestamp": datetime.now(),
        "Name": Name,
        "Business_Name": Business_Name,
        "Email_id": Email,
        "Phone_Number": Phone,
        "City ": City,
        "PinCode ": PinCode,
        "Password ": Password,
        "Confirm_Password ": Confirm_Password,
    }

    # Insert the document into the collection
    collection.insert_one(stats)
    print("User statistics updated.")

def main():
    # Example usage to update user statistics
    Name = input("Enter your Name : ")
    Business_Name = input("Enter Your Business name : ")
    Email = input("Enter your Email is : ")
    Phone = int(input("Enter your phone number : "))
    City = input("Enter your City : ")
    PinCode = int(input("Enter your PinCode : "))
    Password = input("Enter your Password : ")
    Confirm_Password = input("Enter your confirm Password :")

    update_user_stats(Name,Business_Name,Email,Phone,City,PinCode,Password,Confirm_Password)

if __name__ == "__main__":
    main()


"""