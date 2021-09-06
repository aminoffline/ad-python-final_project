from bs4 import BeautifulSoup
#from Database import Insert_Table
import re
import requests
import time
import datetime
import csv
#from geopy.geocoders import Nominatim

#geolocator = Nominatim(user_agent="scrape")

today = datetime.date.today()
table_name = 'dataset'
table_key = ['model', 'mileage', 'age','color', 'accident', 'owners','price']]
csv_file = open(f'results-{today.strftime("%y-%d-%m")}.csv', 'w')
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
while i <= 330:
    if i==100 or i==200 or i==300:
        time.sleep(300)
    else:
        pass

    response = requests.get(f'https://www.truecar.com/used-cars-for-sale/listings/', params={'page': i}, timeout=30)
    if response.ok == True:
        print(response.url)
        soup = BeautifulSoup(response.text, 'lxml')
        for post in soup.find_all('div', attrs={"data-test": "cardContent"}):
            try:
                heading = post.find('div', class_="vehicle-card-top")
                v_model = heading.find('span', class_="vehicle-header-make-model text-truncate")
                v_year = heading.find('span', class_="vehicle-card-year font-size-1")
                v_age = today.year - int(v_year.text)
                v_mileage = post.find('div', attrs={"data-test": "vehicleMileage"})
                mileage = re.match(r'(.+)\smiles', v_mileage.text)
                mileage = int(mileage.group(1).replace(',', ''))
                v_color = post.find('div', attrs={"data-test": "vehicleCardColors"})
                v_color = re.match(r'(.+)\sexterior', v_color.text)
                v_color = v_color.group(1)
                v_condition = post.find('div', attrs={"data-test": "vehicleCardCondition"})
                condition = re.match(r'(.+)\saccident[s]?.*(.+)\sOwner[s]?', v_condition.text)
                if condition.group(1) == 'No':
                    accident = 0
                else:
                    accident = int(condition.group(1))
                owners = int(condition.group(2))
                v_price = post.find('div', attrs={"data-test": "vehicleListingPriceAmount"})
                price = re.match(r'\$(.+)', v_price.text)
                price = int(price.group(1).replace(',', ''))
                """
                v_location = post.find('div', attrs={"data-test": "vehicleCardLocation"})
                location = geolocator.geocode(f"{v_location.text}")
                location_lat = float(location.latitude)
                location_long = float(location.longitude)
                """
                values = [v_model.text, mileage, v_age, v_color, accident, owners, price]
                csv.writer.writerow(values)
                #Insert_Table(table_name, table_key, values)
            except Exception as err:
                print(err)
        i += 1
        time.sleep(1)
    else:
        time.sleep(60)

csv_file.close()