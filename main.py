
import random
import pandas
import datetime as dt
import smtplib

MY_EMAIL = "Your email"
MY_PASSWORD = "Your password"

today = dt.datetime.now()
month = today.month
day = today.day


def generate_letter(name):
    letter_no = random.randint(1, 3)
    with open(f"./letter_templates/letter_{letter_no}.txt") as letter_file:
        return letter_file.read().replace("[NAME]", name)


birthday_dataframe = pandas.read_csv('birthdays.csv')
for (index, row) in birthday_dataframe.iterrows():
    if row.month == month and row.day == day:
        print("yes")
        letter_to_be_send = generate_letter(row['name'])
        with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=row.email, msg=f"Subject:It's your birthday!!\n\n{letter_to_be_send}")

