# Importing the datetime module from the built-in package
import datetime

current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

current_date = datetime.date.today()
print("Current Date:", current_date)

formatted_date = current_date.strftime("%Y-%m-%d")
print("Formatted Date:", formatted_date)
