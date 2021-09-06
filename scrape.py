from bs4 import BeautifulSoup
from Database import Insert_Table, Read_all_Data
import requests
import time
import datetime
import csv

today = datetime.date.today()
table_name = 'dataset'
table_key = ['vehicle_title', 'vehicle_mileage', 'vehicle_color', 'vehicle_condition', 'vehicle_location', 'vehicle_price']
csv_file = open(f'results-{today.strftime("%x")}', 'w')
csv.writer = csv.writer(csv_file)
csv.writer.writerow(table_key)

"""print('Please enter vehicle Brand for example Alfa-romeo \nEntering WRONG name may cause problem ')
brand = input('>>>')
brand = brand.casefold()
brand = brand.replace(" ", "-")

print('Please enter vehicle model for example giulia \nEntering WRONG name may cause problem ')
model = input('>>>')
model = model.casefold()
model = model.replace(' ', '-')
"""
i = 1
while True:
    response = requests.get(f'https://www.truecar.com/used-cars-for-sale/listings/', params={'page': i}, timeout=30)
    if response.ok == True:
        print(response.url)
        soup = BeautifulSoup(response.text, 'lxml')
        for post in soup.find_all('div', attrs={"data-test": "cardContent"}):
            try:
                heading = post.find('div', class_="vehicle-card-top")
                v_maker_model = heading.find('span', class_="vehicle-header-make-model text-truncate")
                v_trim = heading.find('div', attrs={"data-test": "vehicleCardTrim"})
                v_year = heading.find('span', class_="vehicle-card-year font-size-1")
                car_title = f'{v_maker_model.text} {v_year.text} ,{v_trim.text} '
                v_mileage = post.find('div', attrs={"data-test": "vehicleMileage"})
                v_color = post.find('div', attrs={"data-test": "vehicleCardColors"})
                v_condition = post.find('div', attrs={"data-test": "vehicleCardCondition"})
                v_location = post.find('div', attrs={"data-test": "vehicleCardLocation"})
                v_price = post.find('div', attrs={"data-test": "vehicleListingPriceAmount"})
                values = [car_title, v_mileage.text, v_color.text, v_condition.text, v_location.text, v_price.text]
                csv.writer.writerow([car_title, v_mileage.text, v_color.text, v_condition.text, v_location.text, v_price.text])
                Insert_Table(table_name, table_key, values)
            except Exception as err:
                print(err)
        i += 1
        time.sleep(1)
    else:
        time.sleep(60)

