import name
import adress
import random
import user_agents

firstLast = ""
female = False
randomFemale = random.randint(0, 1)
age = random.randint(1, 50)
ip = ".".join(map(str, (random.randint(0, 255)
                        for _ in range(4))))
ssn = lambda: f"{random.randint(0, 999):03}-{random.randint(0, 99):02}-{random.randint(0, 9999):04}"
phone_number = lambda: f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
email = lambda first_name, last_name: f"{first_name.lower()}.{last_name.lower()}@{random.choice(['yahoo.com', 'gmail.com', 'outlook.com', 'hotmail.com', 'aol.com'])}"

if randomFemale == 0:
    female = False
else:
    female = True

firstLast = name.name(female)
first_name, last_name = firstLast.split()

print("Fake identity generator by Evelynn (github.com/evelynndevv)\n")
print("Full name: " + firstLast)
print("Age: " + str(age))
print("IP: " + str(ip))
print("SSN: " + ssn())
print("Phone number: " + "+1 " + phone_number())
print("Home address: " + adress.generate_random_address())
print("User agent: " + user_agents.gen_useragent())
print("Email: " + email(first_name, last_name))
