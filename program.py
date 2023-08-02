import requests
from datetime import datetime

WEATHER_API="https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

#get json data from api
def get_from_api():
    try:
        resp=requests.get(WEATHER_API)
        if resp.status_code == 200: #request success
            json_data=resp.json()
            return json_data
        else:
            print("Request failed with status code: ",response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error occurred: ",e)
        return None

#get temperature of given date
def get_temp(data,date):
    for element in data["list"]:
        if date in element["dt_txt"]:
            return element["main"]["temp"]
    return None

#get windspeed of given date
def get_speed(data,date):
    for element in data["list"]:
        if date in element["dt_txt"]:
            return element["wind"]["speed"]
    return None

#get pressure of given date
def get_pressure(data,date):
    for element in data["list"]:
        if date in element["dt_txt"]:
            return element["main"]["pressure"]
    return None

#check whether date is in valid format
def check_date(date):
    format="%Y-%m-%d %H:%M:%S"
    try:
        valid=bool(datetime.strptime(date, format))
    except ValueError:
        valid=False
    return valid

if __name__ == "__main__":
    api_data=get_from_api()
    if api_data==None:
        exit()

    while True:
        print("\n1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit\n")
        option=int(input("Enter your option: "))

        if option==0:
            print("\nTerminating the program\n")
            break

        elif option==1:
            user_date=input("\nEnter date (YYYY-MM-DD HH:MM:SS): ")
            valid_date=check_date(user_date)
            if valid_date is False:
                print("Incorrect date format\n")
                continue
            temperature=get_temp(api_data,user_date)
            if temperature is None:
                print("Data not found\n")
            else:
                print("Temperature: ", temperature)
        
        elif option==2:
            user_date=input("\nEnter date (YYYY-MM-DD HH:MM:SS): ")
            valid_date=check_date(user_date)
            if valid_date is False:
                print("Incorrect date format\n")
                continue
            wind=get_speed(api_data,user_date)
            if wind is None:
                print("Data not found\n")
            else:
                print("Wind speed: ", wind)

        elif option==3:
            user_date=input("\nEnter date (YYYY-MM-DD HH:MM:SS): ")
            valid_date=check_date(user_date)
            if valid_date is False:
                print("Incorrect date format\n")
                continue
            pressure=get_pressure(api_data,user_date)
            if pressure is None:
                print("Data not found\n")
            else:
                print("Pressure: ", pressure)
        
        else:
            print("\nInvalid selection. Try again\n")
