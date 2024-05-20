def get_pincode(city_name):
    city_pincodes = {
        "Mumbai": "400001",
        "Pune": "411001",
        "Nagpur": "440001",
        "Nashik": "422001",
        "Aurangabad": "431001",
        "Thane": "400601",
        "Navi Mumbai": "400614",
        "Kalyan-Dombivli": "421201",
        "Solapur": "413001",
        "Kolhapur": "416001",
        "Amravati": "444601",
        "Sangli": "416416",
        "Jalgaon": "425001",
        "Akola": "444001",
        "Latur": "413512",
        "Ahmednagar": "414001",
        "Chandrapur": "442401",
        "Parbhani": "431401",
        "Ichalkaranji": "416115",
        "Malegaon": "423203"
    }
    
    return city_pincodes.get(city_name, "City not found in the list.")

if __name__ == "__main__":
    city_name = input("Enter the name of the city: ")
    pincode = get_pincode(city_name)
    print(f"The PIN code for {city_name} is: {pincode}")
