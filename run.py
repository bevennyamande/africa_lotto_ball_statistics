import requests
import pygal
from bs4 import BeautifulSoup

# two most interesting urls
bonus_ball_url = 'https://africalotto.co.zw/statistics-bonus-lotto-two'
lucky_number_url = 'https://africalotto.co.zw/statistics-bonus-lotto-two'
get_bonus_ball = requests.get(bonus_ball_url)
get_lucky_ball = requests.get(lucky_number_url)
bonus_soup = BeautifulSoup(get_bonus_ball.text, 'html.parser')
lucky_soup = BeautifulSoup(get_bonus_ball.text, 'html.parser')

# print(bonus_soup.find_all('table'))
table_bonus = bonus_soup.find('table').get_text()
table_lucky = lucky_soup.find('table').get_text()
bonusdata = [line for line in table_bonus.split('\n') if line.strip()]
luckydata = [line for line in table_lucky.split('\n') if line.strip()]

print(bonusdata)
print(luckydata)

# TODO: create an excel sheet or plot the results in a graph
# preferable pygal and renter it to a website

