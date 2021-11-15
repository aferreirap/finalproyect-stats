import requests
from time import sleep
import pandas as pd

apps_data = pd.read_csv('./app_sample.csv')

apps_list = apps_data['App Id'].values
access_token_list = [
 'd5ad39d1fe4d3fc3a8d48cb6d94cd138e39530dd'] 

def get_reviews(apps_list,access_token_list):

    reviews = pd.DataFrame(columns=['app_id','review'])
    url = 'https://data.42matters.com/api/v4.0/android/apps/reviews.json'
    params = {
        "p": '',
        "access_token": '',
        "days": 30,
        "lang": "en",
        'limit': 30,}

    i = 0
    r = 0

    for token in access_token_list:
        params['access_token'] = token

        for i in range(r,r+1000):
            params['p'] = apps_list[i]
            review = requests.get(url, params=params)
            reviews = reviews.append({'app' : apps_list[i], 'review': review , 'token':token} , ignore_index=True)
            print(apps_list[i],review)
        r = i + 1
    return reviews

app_reviews = get_reviews(apps_list=apps_list,access_token_list=access_token_list)
app_reviews.to_csv('app_reviews.csv')