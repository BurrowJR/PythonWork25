import random

def predict_weather():
    sunshine = random.choice([True, False]) # Boolean do not have ''

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()