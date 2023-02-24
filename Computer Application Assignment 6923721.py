#https://github.com/users/DENNISADU891/emails/242080212/confirm_verification/35621233?via_launch_code_email=true
#list of available cars and their prices
cars = {"Toyota Corolla": 30000,"Lamborghini": 95000,"SUV":35000,"Ford Explorer":50000,"Grand Xcent":55950,"Accent Executive":65950,"Accent Elegance":92950,"Creta Executive":82950,"RAV4 2018":2800,"Corolla 2020":4200,"honda \
civic 2020":32000, "honda civic 2019":2800,"toyota hilux 2019":4700,"honda crv":34000,"vitz 4plugs":2200,"highlander 2020":7500,"camry se 2020":32000,"honda crv 2021":4200,"chevrolet \
equinox 2019":3050,"rangerover velar 2021":23000,"hyundai tucson 2019":2800,"landcruiser prado 2020":11000,"toyota fortuner 2020":85000,"honda civic 2018":22000,"Ford Figo 1.2 \
Titanium Blu 2019":10000,"Nissan Magnite XV DT 2023":10000,"Suzuki Ignis Zeta AMT 2023":10000,"Tata Altroz XE Plus Diesel":9990,"Chery EQ1 EV 2023":9910,"Renault Kiger RXT 2023":9880}
#get user input for car name
car_name=input('Enter a car_name:')
#check if car name is in the list of available cars
if car_name in cars:
 print('Yes')
 #if car name is present, get its price
 car_price = cars[car_name]
 print(f'The price of {car_name} is ${car_price}.' )
else:
    #if car name is not present, inform the user
    print(f'Sorry, {car_name} is not available.' )