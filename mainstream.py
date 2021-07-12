# importing the libraries
import pandas as pd
import numpy as np
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import random


# scraping from The Quint
def quint(start, end):
    quint_list = []
    for pagenumber in range(start, end+1):
        time.sleep(random.randint(10, 15))
        pagenum = str(pagenumber)

        url_top_story = 'https://www.thequint.com/collection/top-story-news/' + pagenum
        url_politics = 'https://www.thequint.com/news/politics/' + pagenum
        url_india = 'https://www.thequint.com/news/india/' + pagenum
        url_world = 'https://www.thequint.com/news/world/' + pagenum
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

        webpage_top_story = requests.get(url_top_story, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_politics = requests.get(url_politics, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_india = requests.get(url_india, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_world = requests.get(url_world, headers=headers)

        soup_top_story = BeautifulSoup(webpage_top_story.text, 'html.parser')
        soup_politics = BeautifulSoup(webpage_politics.text, 'html.parser')
        soup_india = BeautifulSoup(webpage_india.text, 'html.parser')
        soup_world = BeautifulSoup(webpage_world.text, 'html.parser')

        headline_top_story = soup_top_story.find_all('h2')
        headline_politics = soup_politics.find_all('h2')
        headline_india = soup_india.find_all('h2')
        headline_world = soup_world.find_all('h2')

        for i in headline_top_story:
            headline = i.text.strip()
            quint_list.append(headline)

        for i in headline_politics:
            headline = i.text.strip()
            quint_list.append(headline)

        for i in headline_india:
            headline = i.text.strip()
            quint_list.append(headline)

        for i in headline_world:
            headline = i.text.strip()
            quint_list.append(headline)
        print(f'Page {pagenum} of The Quint')
    quint_list = list(dict.fromkeys(quint_list))
    return quint_list


# scraping from News18
def news18(start, end):
    news18_list = []
    for pagenumber in range(start, end+1):
        time.sleep(random.randint(10, 15))
        pagenum = str(pagenumber)

        url_india = 'https://www.news18.com/india/page-'+pagenum
        url_tech = 'https://www.news18.com/tech/page-'+pagenum
        url_auto = 'https://www.news18.com/auto/page-'+pagenum
        url_buzz = 'https://www.news18.com/buzz/page-' + pagenum
        headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}
        proxies = {"http": "http://10.10.1.10:3128",
                   "https": "http://10.10.1.10:1080"}

        webpage_india = requests.get(url_india, headers=headers)
        time.sleep(random.randint(2, 9))
        webpage_tech = requests.get(url_tech, headers=headers)
        time.sleep(random.randint(2, 9))
        webpage_auto = requests.get(url_auto, headers=headers)
        time.sleep(random.randint(2, 9))
        webpage_buzz = requests.get(url_buzz, headers=headers)

        soup_india = BeautifulSoup(webpage_india.text, 'html.parser')
        soup_tech = BeautifulSoup(webpage_tech.text, 'html.parser')
        soup_auto = BeautifulSoup(webpage_auto.text, 'html.parser')
        soup_buzz = BeautifulSoup(webpage_buzz.text, 'html.parser')

        headline_india = soup_india.find_all('h4')
        headline_tech = soup_tech.find_all('h4')
        headline_auto = soup_auto.find_all('h4')
        headline_buzz = soup_buzz.find_all('h4')

        for i in headline_india:
            link1 = i.find_all('a')
            headline = link1[0].text.strip()
            news18_list.append(headline)

        for i in headline_tech:
            link2 = i.find_all('a')
            headline = link2[0].text.strip()
            news18_list.append(headline)

        for i in headline_auto:
            link3 = i.find_all('a')
            headline = link3[0].text.strip()
            news18_list.append(headline)

        for i in headline_buzz:
            link4 = i.find_all('a')
            headline = link4[0].text.strip()
            news18_list.append(headline)
        print(f'Page {pagenum} of News18')
    news18_list = list(dict.fromkeys(news18_list))
    return news18_list


# scraping from Times Of India
def toi(start, end):
    toi_list = []
    for pagenumber in range(start, end+1):
        time.sleep(random.randint(5, 9))
        pagenum = str(pagenumber)

        url_india = 'https://timesofindia.indiatimes.com/india/'+pagenum
        url_chennai = 'https://timesofindia.indiatimes.com/city/chennai/'+pagenum
        url_coimbatore = 'https://timesofindia.indiatimes.com/city/coimbatore/'+pagenum
        url_madurai = 'https://timesofindia.indiatimes.com/city/madurai/' + pagenum
        url_trichy = 'https://timesofindia.indiatimes.com/city/trichy/' + pagenum
        url_world_us = 'https://timesofindia.indiatimes.com/world/us/' + pagenum
        url_world_pakistan = 'https://timesofindia.indiatimes.com/world/pakistan/' + pagenum
        url_world_south_asia = 'https://timesofindia.indiatimes.com/world/south-asia/' + pagenum
        url_world_uk = 'https://timesofindia.indiatimes.com/world/uk/' + pagenum
        url_world_europe = 'https://timesofindia.indiatimes.com/world/europe/' + pagenum
        url_world_china = 'https://timesofindia.indiatimes.com/world/china/' + pagenum
        url_world_middle_east = 'https://timesofindia.indiatimes.com/world/middle-east/' + pagenum
        url_world_others = 'https://timesofindia.indiatimes.com/world/rest-of-world/' + pagenum
        headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

        webpage_india = requests.get(url_india, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_chennai = requests.get(url_chennai, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_coimbatore = requests.get(url_coimbatore, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_madurai = requests.get(url_madurai, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_trichy = requests.get(url_trichy, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_world_us = requests.get(url_world_us, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_world_pakistan = requests.get(url_world_pakistan, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_world_south_asia = requests.get(url_world_south_asia, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_world_uk = requests.get(url_world_uk , headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_world_europe = requests.get(url_world_europe, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_world_china = requests.get(url_world_china, headers=headers)
        time.sleep(random.randint(2, 9))
        webpage_world_middle_east = requests.get(url_world_middle_east, headers=headers)
        time.sleep(random.randint(2, 9))
        webpage_world_others = requests.get(url_world_others, headers=headers)

        soup_india = BeautifulSoup(webpage_india.text, 'html.parser')
        soup_chennai = BeautifulSoup(webpage_chennai.text, 'html.parser')
        soup_coimbatore = BeautifulSoup(webpage_coimbatore.text, 'html.parser')
        soup_madurai = BeautifulSoup(webpage_madurai.text, 'html.parser')
        soup_trichy = BeautifulSoup(webpage_trichy .text, 'html.parser')
        soup_world_us = BeautifulSoup(webpage_world_us.text, 'html.parser')
        soup_world_pakistan = BeautifulSoup(webpage_world_pakistan.text, 'html.parser')
        soup_world_south_asia = BeautifulSoup(webpage_world_south_asia.text, 'html.parser')
        soup_world_uk = BeautifulSoup(webpage_world_uk.text, 'html.parser')
        soup_world_europe = BeautifulSoup(webpage_world_europe.text, 'html.parser')
        soup_world_china = BeautifulSoup(webpage_world_china.text, 'html.parser')
        soup_world_middle_east = BeautifulSoup(webpage_world_middle_east.text, 'html.parser')
        soup_world_others = BeautifulSoup(webpage_world_others.text, 'html.parser')


        headline_india = soup_india.find_all('span', attrs={'class': 'w_tle'})
        headline_chennai = soup_chennai.find_all('span', attrs={'class': 'w_tle'})
        headline_coimbatore = soup_coimbatore.find_all('span', attrs={'class': 'w_tle'})
        headline_madurai = soup_madurai.find_all('span', attrs={'class': 'w_tle'})
        headline_trichy = soup_trichy.find_all('span', attrs={'class': 'w_tle'})
        headline_world_us = soup_world_us.find_all('span', attrs={'class': 'w_tle'})
        headline_world_pakistan = soup_world_pakistan.find_all('span', attrs={'class': 'w_tle'})
        headline_world_south_asia = soup_world_south_asia.find_all('span', attrs={'class': 'w_tle'})
        headline_world_uk = soup_world_uk.find_all('span', attrs={'class': 'w_tle'})
        headline_world_europe = soup_world_europe.find_all('span', attrs={'class': 'w_tle'})
        headline_world_china = soup_world_china.find_all('span', attrs={'class': 'w_tle'})
        headline_world_middle_east = soup_world_middle_east.find_all('span', attrs={'class': 'w_tle'})
        headline_world_others = soup_world_others.find_all('span', attrs={'class': 'w_tle'})


        for i in headline_india:
            link1 = i.find_all('a')
            headline = link1[0].text.strip()
            toi_list.append(headline)

        for i in headline_chennai:
            link2 = i.find_all('a')
            headline = link2[0].text.strip()
            toi_list.append(headline)

        for i in headline_coimbatore:
            link3 = i.find_all('a')
            headline = link3[0].text.strip()
            toi_list.append(headline)

        for i in headline_madurai:
            link4 = i.find_all('a')
            headline = link4[0].text.strip()
            toi_list.append(headline)

        for i in headline_trichy:
            link5 = i.find_all('a')
            headline = link5[0].text.strip()
            toi_list.append(headline)

        for i in headline_world_us:
            link6 = i.find_all('a')
            headline = link6[0].text.strip()
            toi_list.append(headline)

        for i in headline_world_pakistan:
            link7 = i.find_all('a')
            headline = link7[0].text.strip()
            toi_list.append(headline)

        for i in headline_world_south_asia:
            link8 = i.find_all('a')
            headline = link8[0].text.strip()
            toi_list.append(headline)

        for i in headline_world_uk:
            link9 = i.find_all('a')
            headline = link9[0].text.strip()
            toi_list.append(headline)

        for i in headline_world_europe:
            link10 = i.find_all('a')
            headline = link10[0].text.strip()
            toi_list.append(headline)

        for i in headline_world_china:
            link11 = i.find_all('a')
            headline = link11[0].text.strip()
            toi_list.append(headline)

        for i in headline_world_middle_east:
            link12 = i.find_all('a')
            headline = link12[0].text.strip()
            toi_list.append(headline)

        for i in headline_world_others:
            link13 = i.find_all('a')
            headline = link13[0].text.strip()
            toi_list.append(headline)
        print(f'Page {pagenum} of Times of India')
    toi_list = list(dict.fromkeys(toi_list))
    return toi_list


# scraping from The Indian Express
def tie(start, end):
    tie_list = []
    for pagenumber in range(start, end+1):
        time.sleep(random.randint(5, 9))
        pagenum = str(pagenumber)

        url_india = 'https://indianexpress.com/section/india/page/' + pagenum
        url_chennai = 'https://indianexpress.com/section/cities/chennai/page/'+pagenum
        url_world = 'https://indianexpress.com/section/world/page/'+pagenum
        url_hyderabad = 'https://indianexpress.com/section/cities/hyderabad/page/' + pagenum
        url_bangalore = 'https://indianexpress.com/section/cities/bangalore/page/' + pagenum
        url_delhi = 'https://indianexpress.com/section/cities/delhi/page/' + pagenum
        url_mumbai = 'https://indianexpress.com/section/cities/mumbai/page/' + pagenum
        url_kolkata = 'https://indianexpress.com/section/cities/kolkata/page/' + pagenum
        headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

        webpage_india = requests.get(url_india, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_chennai = requests.get(url_chennai, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_world = requests.get(url_world, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_hyderabad = requests.get(url_hyderabad, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_bangalore = requests.get(url_bangalore, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_delhi = requests.get(url_delhi, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_mumbai = requests.get(url_mumbai, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_kolkata = requests.get(url_kolkata, headers=headers)

        soup_india = BeautifulSoup(webpage_india.text, 'html.parser')
        soup_chennai = BeautifulSoup(webpage_chennai.text, 'html.parser')
        soup_world = BeautifulSoup(webpage_world.text, 'html.parser')
        soup_hyderabad = BeautifulSoup(webpage_hyderabad.text, 'html.parser')
        soup_bangalore = BeautifulSoup(webpage_bangalore.text, 'html.parser')
        soup_delhi = BeautifulSoup(webpage_delhi.text, 'html.parser')
        soup_mumbai = BeautifulSoup(webpage_mumbai.text, 'html.parser')
        soup_kolkata = BeautifulSoup(webpage_kolkata.text, 'html.parser')

        headline_india = soup_india.find_all('h2', attrs={'class': 'title'})
        headline_chennai = soup_chennai.find_all('h2', attrs={'class': 'title'})
        headline_world = soup_world.find_all('h3')
        headline_hyderabad = soup_hyderabad.find_all('h2', attrs={'class': 'title'})
        headline_bangalore = soup_bangalore.find_all('h3')
        headline_delhi = soup_delhi.find_all('h3')
        headline_mumbai = soup_mumbai.find_all('h3')
        headline_kolkata = soup_kolkata.find_all('h3')


        for i in headline_india:
            link1 = i.find_all('a')
            headline = link1[0].text.strip()
            tie_list.append(headline)

        for i in headline_chennai:
            link2 = i.find_all('a')
            headline = link2[0].text.strip()
            tie_list.append(headline)

        for i in headline_world:
            link3 = i.find_all('a')
            headline = link3[0].text.strip()
            tie_list.append(headline)

        for i in headline_hyderabad:
            link4 = i.find_all('a')
            headline = link4[0].text.strip()
            tie_list.append(headline)

        for i in headline_bangalore:
            link5 = i.find_all('a')
            headline = link5[0].text.strip()
            tie_list.append(headline)

        for i in headline_mumbai:
            link6 = i.find_all('a')
            headline = link6[0].text.strip()
            tie_list.append(headline)

        for i in headline_delhi:
            link7 = i.find_all('a')
            headline = link7[0].text.strip()
            tie_list.append(headline)

        for i in headline_kolkata:
            link8 = i.find_all('a')
            headline = link8[0].text.strip()
            tie_list.append(headline)
        print(f'Page {pagenum} of The Indian Express')
    tie_list = list(dict.fromkeys(tie_list))
    return tie_list


# scraping from Money Control
def moneycontrol(start, end):
    mc_list = []
    for pagenumber in range(start, end+1):
        time.sleep(random.randint(5, 9))
        pagenum = str(pagenumber)

        url_markets = 'https://www.moneycontrol.com/news/business/markets/page-'+pagenum
        url_stock = 'https://www.moneycontrol.com/news/business/stocks/page-'+pagenum
        url_economy = 'https://www.moneycontrol.com/news/business/economy/page-' + pagenum
        url_companies = 'https://www.moneycontrol.com/news/business/companies/page-' + pagenum
        headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

        webpage_markets = requests.get(url_markets, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_stock = requests.get(url_stock, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_economy = requests.get(url_economy, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_companies = requests.get(url_companies, headers=headers)

        soup_markets = BeautifulSoup(webpage_markets.text, 'html.parser')
        soup_stock = BeautifulSoup(webpage_stock.text, 'html.parser')
        soup_economy = BeautifulSoup(webpage_economy.text, 'html.parser')
        soup_companies = BeautifulSoup(webpage_companies.text, 'html.parser')

        headline_markets = soup_markets.find_all('h2')
        headline_stock = soup_stock.find_all('h2')
        headline_economy = soup_economy.find_all('h2')
        headline_companies = soup_companies.find_all('h2')

        for i in headline_markets:
            link2 = i.find_all('a')
            if link2:
                headline = link2[0].text.strip()
                mc_list.append(headline)

        for i in headline_stock:
            link3 = i.find_all('a')
            if link3:
                headline = link3[0].text.strip()
                mc_list.append(headline)

        for i in headline_economy:
            link4 = i.find_all('a')
            if link4:
                headline = link4[0].text.strip()
                mc_list.append(headline)

        for i in headline_companies:
            link5 = i.find_all('a')
            if link5:
                headline = link5[0].text.strip()
                mc_list.append(headline)
        print(f'Page {pagenum} of Money Control')
    mc_list = list(dict.fromkeys(mc_list))
    return mc_list


# scraping from The Financial Express
def financial_express(start, end):
    fe_list = []
    for pagenumber in range(start, end+1):
        time.sleep(random.randint(5, 9))
        pagenum = str(pagenumber)

        url_markets = 'https://www.financialexpress.com/market/page/' + pagenum
        url_industry = 'https://www.financialexpress.com/industry/page/'+pagenum
        url_economy = 'https://www.financialexpress.com/economy/page/'+pagenum
        url_money = 'https://www.financialexpress.com/money/page/' + pagenum
        url_infrastructure = 'https://www.financialexpress.com/infrastructure/page/' + pagenum
        url_sme = 'https://www.financialexpress.com/industry/sme/page/' + pagenum
        headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

        webpage_markets = requests.get(url_markets, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_industry = requests.get(url_industry, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_economy = requests.get(url_economy, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_money = requests.get(url_money, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_infrastructure = requests.get(url_infrastructure, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_sme = requests.get(url_sme, headers=headers)

        soup_markets = BeautifulSoup(webpage_markets.text, 'html.parser')
        soup_industry = BeautifulSoup(webpage_industry.text, 'html.parser')
        soup_economy = BeautifulSoup(webpage_economy.text, 'html.parser')
        soup_money = BeautifulSoup(webpage_money.text, 'html.parser')
        soup_infrastructure = BeautifulSoup(webpage_infrastructure.text, 'html.parser')
        soup_sme = BeautifulSoup(webpage_sme.text, 'html.parser')

        headline_markets = soup_markets.find_all('h3')
        headline_industry = soup_industry.find_all('h3')
        headline_economy = soup_economy.find_all('h3')
        headline_money = soup_money.find_all('h3')
        headline_infrastructure = soup_infrastructure.find_all('h3')
        headline_sme = soup_sme.find_all('h3')

        for i in headline_markets:
            link1 = i.find_all('a')
            if link1:
                headline = link1[0].text.strip()
                fe_list.append(headline)

        for i in headline_industry:
            link2 = i.find_all('a')
            if link2:
                headline = link2[0].text.strip()
                fe_list.append(headline)

        for i in headline_economy:
            link3 = i.find_all('a')
            if link3:
                headline = link3[0].text.strip()
                fe_list.append(headline)

        for i in headline_money:
            link4 = i.find_all('a')
            if link4:
                headline = link4[0].text.strip()
                fe_list.append(headline)

        for i in headline_infrastructure:
            link5 = i.find_all('a')
            if link5:
                headline = link5[0].text.strip()
                fe_list.append(headline)

        for i in headline_sme:
            link6 = i.find_all('a')
            if link6:
                headline = link6[0].text.strip()
                fe_list.append(headline)
        print(f'Page {pagenum} of The Financial Express')
    fe_list = list(dict.fromkeys(fe_list))
    return fe_list


# scraping from The Republic
def republic(start, end):
    republic_list = []
    for pagenumber in range(start, end+1):
        time.sleep(random.randint(5, 9))
        pagenum = str(pagenumber)

        url_india_politics = 'https://www.republicworld.com/india-news/politics/' + pagenum
        url_india_general = 'https://www.republicworld.com/india-news/general-news/'+pagenum
        url_india_education = 'https://www.republicworld.com/india-news/education/'+pagenum
        url_india_elections = 'https://www.republicworld.com/india-news/elections/' + pagenum
        url_india_economy = 'https://www.republicworld.com/india-news/economy/' + pagenum
        url_city = 'https://www.republicworld.com/india-news/city-news/' + pagenum
        url_accidents = 'https://www.republicworld.com/india-news/accidents-and-disasters/' + pagenum
        url_law = 'https://www.republicworld.com/india-news/law-and-order/' + pagenum
        url_railways = 'https://www.republicworld.com/india-news/irctc/' + pagenum
        headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

        webpage_india_politics = requests.get(url_india_politics, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_india_general = requests.get(url_india_general, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_india_education = requests.get(url_india_education, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_india_elections = requests.get(url_india_elections, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_india_economy = requests.get(url_india_economy, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_city = requests.get(url_city, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_accidents = requests.get(url_accidents, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_law = requests.get(url_law, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_railways = requests.get(url_railways, headers=headers)

        soup_india_politics = BeautifulSoup(webpage_india_politics.text, 'html.parser')
        soup_india_general = BeautifulSoup(webpage_india_general.text, 'html.parser')
        soup_india_education = BeautifulSoup(webpage_india_education.text, 'html.parser')
        soup_india_elections = BeautifulSoup(webpage_india_elections.text, 'html.parser')
        soup_india_economy = BeautifulSoup(webpage_india_economy.text, 'html.parser')
        soup_city = BeautifulSoup(webpage_city.text, 'html.parser')
        soup_accidents = BeautifulSoup(webpage_accidents.text, 'html.parser')
        soup_law = BeautifulSoup(webpage_law.text, 'html.parser')
        soup_railways = BeautifulSoup(webpage_railways.text, 'html.parser')

        headline_india_politics = soup_india_politics.find_all('h2', attrs={'class': 'font16 lineHeight21px'})
        headline_india_general = soup_india_general.find_all('h2', attrs={'class': 'font16 lineHeight21px'})
        headline_india_education = soup_india_education.find_all('h2', attrs={'class': 'font16 lineHeight21px'})
        headline_india_elections = soup_india_elections.find_all('h2', attrs={'class': 'font16 lineHeight21px'})
        headline_india_economy = soup_india_economy.find_all('h2', attrs={'class': 'font16 lineHeight21px'})
        headline_city = soup_city.find_all('h2', attrs={'class': 'font16 lineHeight21px'})
        headline_accidents = soup_accidents.find_all('h2', attrs={'class': 'font16 lineHeight21px'})
        headline_law = soup_law.find_all('h2', attrs={'class': 'font16 lineHeight21px'})
        headline_railways = soup_railways.find_all('h2', attrs={'class': 'font16 lineHeight21px'})

        for i in headline_india_politics:
            headline = i.text.strip()
            republic_list.append(headline)


        for i in headline_india_general:
            headline = i.text.strip()
            republic_list.append(headline)


        for i in headline_india_education:
            headline = i.text.strip()
            republic_list.append(headline)


        for i in headline_india_elections:
            headline = i.text.strip()
            republic_list.append(headline)


        for i in headline_india_economy:
            headline = i.text.strip()
            republic_list.append(headline)

        for i in headline_city:
            headline = i.text.strip()
            republic_list.append(headline)

        for i in headline_accidents:
            headline = i.text.strip()
            republic_list.append(headline)

        for i in headline_law:
            headline = i.text.strip()
            republic_list.append(headline)

        for i in headline_railways:
            headline = i.text.strip()
            republic_list.append(headline)
        print(f'Page {pagenum} of Republic World')
    republic_list = list(dict.fromkeys(republic_list))
    return republic_list


# scraping from India TV
def india_tv(start, end):
    india_tv_list = []
    for pagenumber in range(start, end+1):
        time.sleep(random.randint(5, 9))
        pagenum = str(pagenumber)

        url_india = 'https://www.indiatvnews.com/india/' + pagenum
        url_world = 'https://www.indiatvnews.com/world/'+pagenum
        url_entertainment = 'https://www.indiatvnews.com/entertainment/' + pagenum
        url_business = 'https://www.indiatvnews.com/business/' + pagenum
        url_sports = 'https://www.indiatvnews.com/sports/' + pagenum
        url_technology = 'https://www.indiatvnews.com/technology/' + pagenum
        headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

        webpage_india = requests.get(url_india, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_world = requests.get(url_world, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_entertainment = requests.get(url_entertainment, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_business = requests.get(url_business, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_sports = requests.get(url_sports, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_technology = requests.get(url_technology, headers=headers)
        time.sleep(random.randint(5, 9))

        soup_india = BeautifulSoup(webpage_india.text, 'html.parser')
        soup_world = BeautifulSoup(webpage_world.text, 'html.parser')
        soup_entertainment = BeautifulSoup(webpage_entertainment.text, 'html.parser')
        soup_business = BeautifulSoup(webpage_business.text, 'html.parser')
        soup_sports = BeautifulSoup(webpage_sports.text, 'html.parser')
        soup_technology = BeautifulSoup(webpage_technology.text, 'html.parser')

        headline_india = soup_india.find_all('h3', attrs={'class': 'title'})
        headline_world = soup_world.find_all('h3', attrs={'class': 'title'})
        headline_entertainment = soup_entertainment.find_all('h3', attrs={'class': 'title'})
        headline_business = soup_business.find_all('h3', attrs={'class': 'title'})
        headline_sports = soup_sports.find_all('h3', attrs={'class': 'title'})
        headline_technology = soup_technology.find_all('h3', attrs={'class': 'title'})

        for i in headline_india:
            link1 = i.find_all('a')
            if link1:
                headline = link1[0].text.strip()
                india_tv_list.append(headline)

        for i in headline_world:
            link2 = i.find_all('a')
            if link2:
                headline = link2[0].text.strip()
                india_tv_list.append(headline)

        for i in headline_entertainment:
            link3 = i.find_all('a')
            if link3:
                headline = link3[0].text.strip()
                india_tv_list.append(headline)

        for i in headline_business:
            link4 = i.find_all('a')
            if link4:
                headline = link4[0].text.strip()
                india_tv_list.append(headline)

        for i in headline_sports:
            link5 = i.find_all('a')
            if link5:
                headline = link5[0].text.strip()
                india_tv_list.append(headline)

        for i in headline_technology:
            link6 = i.find_all('a')
            if link6:
                headline = link6[0].text.strip()
                india_tv_list.append(headline)
        print(f'Page {pagenum} of India TV')
    india_tv_list = list(dict.fromkeys(india_tv_list))
    return india_tv_list

