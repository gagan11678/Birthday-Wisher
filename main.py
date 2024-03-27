import pandas as pd
import random
import smtplib
from datetime import datetime as dt

today = (dt.today().month, dt.today().day)

data = pd.read_csv("birthdays.csv")
birthday_dic = {(row['month'], row['day']): row for _, row in data.iterrows()}

# 2. Check if today matches a birthday in the birthdays.csv. if true, pick a random letter from templates and replace
# [NAME]
if today in birthday_dic:
    birthday_person = birthday_dic[today]
    letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
    letter_path = random.choice(letters)
    with open(file=letter_path, mode='r') as letter:
        file = letter.read()
        modified_letter = file.replace("[NAME]", birthday_person['name'])

    # 4. Send the letter generated in step 3 to that person's email address.
    email = "your@email"
    birthday_person_email = birthday_person['email']
    password = "password"

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr=email, to_addrs=birthday_person_email, msg=f"subject: Happy birthday\n\n"
                                                                                 "{modified_letter}")
