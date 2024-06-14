import random

def generate_random_address():
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego",
              "Dallas", "San Jose"]
    streets = ["Main St", "First Ave", "Broadway", "Oak St", "Elm St", "Maple Ave", "Cedar St", "Pine St",
               "Washington St", "Jefferson Ave"]

    random_city = random.choice(cities)
    random_street = random.choice(streets)
    random_zip_code = ''.join([str(random.randint(0, 9)) for _ in range(5)])

    return f"{random_street}, {random_city}, {random_zip_code}"
