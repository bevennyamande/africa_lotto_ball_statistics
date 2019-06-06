import requests
import pygal
from bs4 import BeautifulSoup
import numpy as np

# two most interesting urls
africa_lotto__url = 'https://africalotto.co.zw/statistics-bonus-lotto-two'

def scrap_africa_lotto(africa_lotto__url):
    bonusdata = []
    try:
        balls = requests.get(africa_lotto__url)
        soup = BeautifulSoup(balls.text, 'html.parser')
        bonus_ball_table = bonus_soup.find('table').get_text()
        bonusdata = [line for line in bonus_ball_table.split('\n') if line.strip()]
        with open('bonusdata.txt', 'a+') as fileobj:
            fileobj.write(bonus_ball_table)
    except Exception as e:
        pass
    return bonusdata


def clean_saved_data(filename):
    with open(filename, 'w+') as fileobj:
        for line in fileobj.readline():
            print(line)

if __name__ == '__main__':
    scrap_africa_lotto(africa_lotto__url)
    clean_saved_data('bonusdata.txt')

# TODO: create an excel sheet or plot the results in a graph
# preferable pygal and renter it to a website

