# importing the libraries
import pandas as pd
import numpy as np
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import random


# Scraping from OpIndia
def op_india(start, end):
    op_india_list = []
    for pagenumber in range(start, end+1):
        time.sleep(random.randint(10, 15))
        pagenum = str(pagenumber)

        url_politics = 'https://www.opindia.com/category/politics/page/' + pagenum
        url_media = 'https://www.opindia.com/category/media/page/'+pagenum
        url_variety = 'https://www.opindia.com/category/variety/page/'+pagenum
        url_specials = 'https://www.opindia.com/category/explainer/page/' + pagenum
        url_social_media = ' https://www.opindia.com/category/virtual-world/page/' + pagenum
        url_entertainment = 'https://www.opindia.com/category/entertainment/page/' + pagenum
        url_political_history = 'https://www.opindia.com/category/political-history-of-india/page/' + pagenum
        url_govt = 'https://www.opindia.com/category/government-and-policy/page/' + pagenum
        url_economy = 'https://www.opindia.com/category/economy-and-finance/page/' + pagenum
        url_sports = 'https://www.opindia.com/category/sports/page/' + pagenum
        url_world = 'https://www.opindia.com/category/international/page/' + pagenum
        url_crime = 'https://www.opindia.com/category/crime/page/' + pagenum
        url_law = 'https://www.opindia.com/category/law/page/' + pagenum
        headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

        webpage_politics = requests.get(url_politics, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_media = requests.get(url_media, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_variety = requests.get(url_variety, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_specials = requests.get(url_specials, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_social_media = requests.get(url_social_media, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_entertainment = requests.get(url_entertainment, headers=headers)
        time.sleep(random.randint(10,15))
        webpage_political_history = requests.get(url_political_history, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_govt = requests.get(url_govt, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_economy = requests.get(url_economy, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_sports = requests.get(url_sports, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_world = requests.get(url_world, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_crime = requests.get(url_crime, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_law = requests.get(url_law, headers=headers)
        time.sleep(random.randint(5, 9))

        soup_politics = BeautifulSoup(webpage_politics.text, 'html.parser')
        soup_media = BeautifulSoup(webpage_media.text, 'html.parser')
        soup_variety = BeautifulSoup(webpage_variety.text, 'html.parser')
        soup_specials = BeautifulSoup(webpage_specials.text, 'html.parser')
        soup_social_media = BeautifulSoup(webpage_social_media.text, 'html.parser')
        soup_entertainment = BeautifulSoup(webpage_entertainment.text, 'html.parser')
        soup_political_history = BeautifulSoup(webpage_political_history.text, 'html.parser')
        soup_govt = BeautifulSoup(webpage_govt.text, 'html.parser')
        soup_economy = BeautifulSoup(webpage_economy.text, 'html.parser')
        soup_sports = BeautifulSoup(webpage_sports.text, 'html.parser')
        soup_world = BeautifulSoup(webpage_world.text, 'html.parser')
        soup_crime = BeautifulSoup(webpage_crime.text, 'html.parser')
        soup_law = BeautifulSoup(webpage_law.text, 'html.parser')

        headline_politics = soup_politics.find_all('h3', attrs={'class': 'entry-title td-module-title'})
        headline_media = soup_media.find_all('h3', attrs={'class': 'entry-title td-module-title'})
        headline_variety = soup_variety.find_all('h3', attrs={'class': 'entry-title td-module-title'})
        headline_specials = soup_specials.find_all('h3', attrs={'class': 'entry-title td-module-title'})
        headline_social_media = soup_social_media.find_all('h3', attrs={'class': 'entry-title td-module-title'})
        headline_entertainment = soup_entertainment.find_all('h3', attrs={'class': 'entry-title td-module-title'})
        headline_political_history = soup_political_history.find_all('h3', attrs={'class': 'entry-title td-module-title'})
        headline_govt = soup_govt.find_all('h3', attrs={'class': 'entry-title td-module-title'})
        headline_economy = soup_economy.find_all('h3', attrs={'class': 'entry-title td-module-title'})
        headline_sports = soup_sports.find_all('h3', attrs={'class': 'entry-title td-module-title'})
        headline_crime = soup_crime.find_all('h3', attrs={'class': 'entry-title td-module-title'})
        headline_law = soup_law.find_all('h3', attrs={'class': 'entry-title td-module-title'})
        headline_world = soup_world.find_all('h3', attrs={'class': 'entry-title td-module-title'})

        for i in headline_politics:
            link1 = i.find_all('a')
            if link1:
                headline = link1[0].text.strip()
                op_india_list.append(headline)

        for i in headline_media:
            link2 = i.find_all('a')
            if link2:
                headline = link2[0].text.strip()
                op_india_list.append(headline)

        for i in headline_variety:
            link3 = i.find_all('a')
            if link3:
                headline = link3[0].text.strip()
                op_india_list.append(headline)

        for i in headline_specials:
            link4 = i.find_all('a')
            if link4:
                headline = link4[0].text.strip()
                op_india_list.append(headline)

        for i in headline_social_media:
            link5 = i.find_all('a')
            if link5:
                headline = link5[0].text.strip()
                op_india_list.append(headline)

        for i in headline_entertainment:
            link6 = i.find_all('a')
            if link6:
                headline = link6[0].text.strip()
                op_india_list.append(headline)

        for i in  headline_political_history:
            link7 = i.find_all('a')
            if link7:
                headline = link7[0].text.strip()
                op_india_list.append(headline)

        for i in headline_govt:
            link8 = i.find_all('a')
            if link8:
                headline = link8[0].text.strip()
                op_india_list.append(headline)

        for i in headline_economy:
            link9 = i.find_all('a')
            if link9:
                headline = link9[0].text.strip()
                op_india_list.append(headline)

        for i in headline_sports:
            link10 = i.find_all('a')
            if link10:
                headline = link10[0].text.strip()
                op_india_list.append(headline)

        for i in headline_crime:
            link11 = i.find_all('a')
            if link11:
                headline = link11[0].text.strip()
                op_india_list.append(headline)

        for i in headline_law:
            link12 = i.find_all('a')
            if link12:
                headline = link12[0].text.strip()
                op_india_list.append(headline)

        for i in headline_world:
            link13 = i.find_all('a')
            if link13:
                headline = link13[0].text.strip()
                op_india_list.append(headline)
        print(f'Page {pagenum} of Op India')
    op_india_list = list(dict.fromkeys(op_india_list))
    return op_india_list


# Scraping from Zero Hedge
def zero_hedge(start, end):
    zero_hedge_list = []
    for pagenumber in range(start, end+1):
        time.sleep(random.randint(10, 15))
        pagenum = str(pagenumber)

        url = 'https://www.zerohedge.com/page/' + pagenum

        headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

        time.sleep(random.randint(5, 9))

        webpage = requests.get(url, headers=headers)

        soup = BeautifulSoup(webpage.text, 'html.parser')

        headline_list = soup.find_all('h2', attrs={'class': 'Article_title__ySJA_ Article_lineClamp__2F1zd'})

        for i in headline_list:
            link1 = i.find_all('a')
            if link1:
                headline = link1[0].text.strip()
                zero_hedge_list.append(headline)
        print(f'Page {pagenum} of Zero Hedge')
    zero_hedge_list = list(dict.fromkeys(zero_hedge_list))
    return zero_hedge_list


# Scraping from US Daily Info
def us_daily_info():
    us_daily_info_list = []
    url_news = 'https://usdailyinfo.com/category/news/'
    url_world = 'https://usdailyinfo.com/category/world/'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

    webpage_news = requests.get(url_news, headers=headers)
    time.sleep(random.randint(5, 9))
    webpage_world = requests.get(url_world, headers=headers)

    soup_news = BeautifulSoup(webpage_news.text, 'html.parser')
    soup_world = BeautifulSoup(webpage_world.text, 'html.parser')

    headline_news = soup_news.find_all('h3', attrs={'class': 'jeg_post_title'})
    headline_world = soup_world.find_all('h3', attrs={'class': 'jeg_post_title'})

    for i in headline_news:
        link1 = i.find_all('a')
        if link1:
            headline = link1[0].text.strip()
            us_daily_info_list.append(headline)

    for i in headline_world:
        link2 = i.find_all('a')
        if link2:
            headline = link2[0].text.strip()
            us_daily_info_list.append(headline)
    us_daily_info_list = list(dict.fromkeys(us_daily_info_list))
    print('Getting data from US Daily Info')
    return us_daily_info_list


# Scraping from News Punch
def news_punch(start, end):
    news_punch_list = []
    for pagenumber in range(start, end+1):
        time.sleep(random.randint(10, 15))
        pagenum = str(pagenumber)

        url_US = 'https://newspunch.com/category/news/us/page/' + pagenum
        url_UK = 'https://newspunch.com/category/news/uk/page/'+pagenum
        url_middle_east = 'https://newspunch.com/category/news/the-middle-east/page/'+pagenum
        url_world = 'https://newspunch.com/category/news/world-news/page/' + pagenum
        url_health = 'https://newspunch.com/category/health/page/' + pagenum
        url_science_env = ' https://newspunch.com/category/science-environment/page/' + pagenum
        url_technology = 'https://newspunch.com/category/technology-2/page/' + pagenum
        url_entertainment = ' https://newspunch.com/category/entertainment/page/' + pagenum
        headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

        webpage_US = requests.get(url_US, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_UK = requests.get(url_UK, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_middle_east = requests.get(url_middle_east, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_world = requests.get(url_world, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_health = requests.get(url_health, headers=headers)
        time.sleep(random.randint(5, 9))
        webpage_science_env = requests.get(url_science_env, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_technology = requests.get(url_technology, headers=headers)
        time.sleep(random.randint(10, 15))
        webpage_entertainment = requests.get(url_entertainment, headers=headers)

        soup_US = BeautifulSoup(webpage_US.text, 'html.parser')
        soup_UK = BeautifulSoup(webpage_UK.text, 'html.parser')
        soup_middle_east = BeautifulSoup(webpage_middle_east.text, 'html.parser')
        soup_world = BeautifulSoup(webpage_world.text, 'html.parser')
        soup_health = BeautifulSoup(webpage_health.text, 'html.parser')
        soup_science_env = BeautifulSoup(webpage_science_env.text, 'html.parser')
        soup_technology = BeautifulSoup(webpage_technology.text, 'html.parser')
        soup_entertainment = BeautifulSoup(webpage_entertainment.text, 'html.parser')

        headline_US = soup_US.find_all('h3', attrs={'class': 'entry-title mh-posts-list-title'})
        headline_UK = soup_UK.find_all('h3', attrs={'class': 'entry-title mh-posts-list-title'})
        headline_middle_east = soup_middle_east.find_all('h3', attrs={'class': 'entry-title mh-posts-list-title'})
        headline_world = soup_world.find_all('h3', attrs={'class': 'entry-title mh-posts-list-title'})
        headline_health = soup_health.find_all('h3', attrs={'class': 'entry-title mh-posts-list-title'})
        headline_science_env = soup_science_env.find_all('h3', attrs={'class': 'entry-title mh-posts-list-title'})
        headline_technology = soup_technology.find_all('h3', attrs={'class': 'entry-title mh-posts-list-title'})
        headline_entertainment = soup_entertainment.find_all('h3', attrs={'class': 'entry-title mh-posts-list-title'})


        for i in headline_US:
            link1 = i.find_all('a')
            if link1:
                headline = link1[0].text.strip()
                news_punch_list.append(headline)


        for i in headline_UK:
            link2 = i.find_all('a')
            if link2:
                headline = link2[0].text.strip()
                news_punch_list.append(headline)


        for i in headline_middle_east:
            link3 = i.find_all('a')
            if link3:
                headline = link3[0].text.strip()
                news_punch_list.append(headline)


        for i in headline_world:
            link4 = i.find_all('a')
            if link4:
                headline = link4[0].text.strip()
                news_punch_list.append(headline)


        for i in headline_health:
            link5 = i.find_all('a')
            if link5:
                headline = link5[0].text.strip()
                news_punch_list.append(headline)

        for i in headline_science_env:
            link6 = i.find_all('a')
            if link6:
                headline = link6[0].text.strip()
                news_punch_list.append(headline)

        for i in headline_technology:
            link7 = i.find_all('a')
            if link7:
                headline = link7[0].text.strip()
                news_punch_list.append(headline)

        for i in headline_entertainment:
            link8 = i.find_all('a')
            if link8:
                headline = link8[0].text.strip()
                news_punch_list.append(headline)
        print(f'Page {pagenum} of News Punch')
    news_punch_list = list(dict.fromkeys(news_punch_list))
    return news_punch_list


# Scraping from News Target
def news_target():
    news_target_list = []
    url_health_freedom = ' https://www.newstarget.com/category/health-freedom/'
    url_second_amendment = 'https://www.newstarget.com/category/second-amendment-cat/'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

    webpage_health_freedom = requests.get(url_health_freedom, headers=headers)
    time.sleep(random.randint(5, 9))
    webpage_second_amendment = requests.get(url_second_amendment, headers=headers)

    soup_health_freedom = BeautifulSoup(webpage_health_freedom.text, 'html.parser')
    soup_second_amendment = BeautifulSoup(webpage_second_amendment.text, 'html.parser')

    headline_health_freedom = soup_health_freedom.find_all('div', attrs={'class': 'Headline'})
    headline_second_amendment = soup_second_amendment.find_all('div', attrs={'class': 'Headline'})

    for i in headline_health_freedom:
        link1 = i.find_all('a')
        if link1:
            headline = link1[0].text.strip()
            news_target_list.append(headline)

    for i in headline_second_amendment:
        link2 = i.find_all('a')
        if link2:
            headline = link2[0].text.strip()
            news_target_list.append(headline)
    news_target_list = list(dict.fromkeys(news_target_list))
    print('Getting data from News Target')
    return news_target_list


# Scraping from The Epoch Times
def the_epoch_times():
    the_epoch_times_list = []
    url = 'https://www.censored.news/TheEpochTimes.htm'

    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

    time.sleep(random.randint(5, 9))

    webpage = requests.get(url, headers=headers)

    soup = BeautifulSoup(webpage.text, 'html.parser')

    headline_list = soup.find_all('p', attrs={'class': 'Headline'})

    for i in headline_list:
        link1 = i.find_all('a')
        if link1:
            headline = link1[0].text.strip()
            the_epoch_times_list.append(headline)
    the_epoch_times_list = list(dict.fromkeys(the_epoch_times_list))
    print('Getting data from The Epoch Times')
    return the_epoch_times_list


# Scraping from Right Scoop
def right_scoop():
    right_scoop_list = []
    url = 'https://www.censored.news/TheRightScoop.htm'

    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

    time.sleep(random.randint(5, 9))

    webpage = requests.get(url, headers=headers)

    soup = BeautifulSoup(webpage.text, 'html.parser')

    headline_list = soup.find_all('p', attrs={'class': 'Headline'})

    for i in headline_list:
        link1 = i.find_all('a')
        if link1:
            headline = link1[0].text.strip()
            right_scoop_list.append(headline)
    print('Getting data from The Right Scoop')
    return right_scoop_list


# Scraping from News Busters
def news_busters():
    news_busters_list = []
    url = 'https://www.censored.news/NewsBusters.htm'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

    time.sleep(random.randint(5, 9))

    webpage = requests.get(url, headers=headers)

    soup = BeautifulSoup(webpage.text, 'html.parser')

    headline_list = soup.find_all('p', attrs={'class': 'Headline'})

    for i in headline_list:
        link1 = i.find_all('a')
        if link1:
            headline = link1[0].text.strip()
            news_busters_list.append(headline)
    print('Getting data from News Busters')
    return news_busters_list


# Scraping from Big League Politics
def big_league_politics():
    big_league_politics_list = []
    url = 'https://www.censored.news/BigLeaguePolitics.htm'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

    time.sleep(random.randint(5, 9))

    webpage = requests.get(url, headers=headers)

    soup = BeautifulSoup(webpage.text, 'html.parser')

    headline_list = soup.find_all('p', attrs={'class': 'Headline'})

    for i in headline_list:
        link1 = i.find_all('a')
        if link1:
            headline = link1[0].text.strip()
            big_league_politics_list.append(headline)
    print('Getting data from Big League Politics')
    return big_league_politics_list


# Scraping from Children Health Defense
def children_health_defense():
    children_health_defense_list = []
    url = 'https://www.censored.news/ChildrensHealthDefense.htm'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

    time.sleep(random.randint(5, 9))

    webpage = requests.get(url, headers=headers)

    soup = BeautifulSoup(webpage.text, 'html.parser')

    headline_list = soup.find_all('p', attrs={'class': 'Headline'})

    for i in headline_list:
        link1 = i.find_all('a')
        if link1:
            headline = link1[0].text.strip()
            children_health_defense_list.append(headline)
    print('Getting data from Children Health Defense')
    return children_health_defense_list


# Scraping from Breibart
def breitbart():
    breitbart_list = []
    url = 'https://www.censored.news/Breitbart.htm'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

    time.sleep(random.randint(5, 9))

    webpage = requests.get(url, headers=headers)

    soup = BeautifulSoup(webpage.text, 'html.parser')

    headline_list = soup.find_all('p', attrs={'class': 'Headline'})

    for i in headline_list:
        link1 = i.find_all('a')
        if link1:
            headline = link1[0].text.strip()
            breitbart_list.append(headline)
    print('Getting data from Breitbart')
    return breitbart_list


# Scraping from Info Wars
def info_wars():
    info_wars_list = []
    url = 'https://www.censored.news/InfoWars.htm'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

    time.sleep(random.randint(5, 9))

    webpage = requests.get(url, headers=headers)

    soup = BeautifulSoup(webpage.text, 'html.parser')

    headline_list = soup.find_all('p', attrs={'class': 'Headline'})

    for i in headline_list:
        link1 = i.find_all('a')
        if link1:
            headline = link1[0].text.strip()
            info_wars_list.append(headline)
    print('Getting data from Info Wars')
    return info_wars_list


# Scraping from All News Pipeline
def all_news_pipeline():
    all_news_pipeline_list = []
    url = 'https://www.censored.news/AllNewsPipeline.htm'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

    time.sleep(random.randint(5, 9))

    webpage = requests.get(url, headers=headers)

    soup = BeautifulSoup(webpage.text, 'html.parser')

    headline_list = soup.find_all('p', attrs={'class': 'Headline'})

    for i in headline_list:
        link1 = i.find_all('a')
        if link1:
            headline = link1[0].text.strip()
            all_news_pipeline_list.append(headline)
    print('Getting data from All News Pipeline')
    return all_news_pipeline_list


# Scraping from True Pundit
def true_pundit():
    true_pundit_list = []
    url = 'https://www.censored.news/TruePundit.htm'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

    time.sleep(random.randint(5, 9))

    webpage = requests.get(url, headers=headers)

    soup = BeautifulSoup(webpage.text, 'html.parser')

    headline_list = soup.find_all('p', attrs={'class': 'Headline'})

    for i in headline_list:
        link1 = i.find_all('a')
        if link1:
            headline = link1[0].text.strip()
            true_pundit_list.append(headline)
    print('Getting data from True Pundit')
    return true_pundit_list


# Scraping from Survival News
def survival_news():
    survival_news_list = []
    url = 'https://www.censored.news/SurvivalNews.htm'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

    time.sleep(random.randint(5, 9))

    webpage = requests.get(url, headers=headers)

    soup = BeautifulSoup(webpage.text, 'html.parser')

    headline_list = soup.find_all('p', attrs={'class': 'Headline'})

    for i in headline_list:
        link1 = i.find_all('a')
        if link1:
            headline = link1[0].text.strip()
            survival_news_list.append(headline)
    print('Getting data from Survival News')
    return survival_news_list


# Scraping from DC Clothes Line
def dc_clothes_line():
    dc_clothes_line_list = []
    url = 'https://www.censored.news/DCClothesLine.htm'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

    time.sleep(random.randint(5, 9))

    webpage = requests.get(url, headers=headers)

    soup = BeautifulSoup(webpage.text, 'html.parser')

    headline_list = soup.find_all('p', attrs={'class': 'Headline'})

    for i in headline_list:
        link1 = i.find_all('a')
        if link1:
            headline = link1[0].text.strip()
            dc_clothes_line_list.append(headline)
    print('Getting data from DC Clothes Line')
    return dc_clothes_line_list


# Scraping from Great Game India
def great_game_india():
    great_game_india_list = []
    url = 'https://www.censored.news/GreatGameIndia.htm'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

    time.sleep(random.randint(5, 9))

    webpage = requests.get(url, headers=headers)

    soup = BeautifulSoup(webpage.text, 'html.parser')

    headline_list = soup.find_all('p', attrs={'class': 'Headline'})

    for i in headline_list:
        link1 = i.find_all('a')
        if link1:
            headline = link1[0].text.strip()
            great_game_india_list.append(headline)
    print('Getting data from Great Game India')
    return great_game_india_list


# Scraping from Forward_Observer
def forward_observer():
    forward_observer_list = []
    url = 'https://www.censored.news/ForwardObserver.htm'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

    time.sleep(random.randint(5, 9))

    webpage = requests.get(url, headers=headers)

    soup = BeautifulSoup(webpage.text, 'html.parser')

    headline_list = soup.find_all('p', attrs={'class': 'Headline'})

    for i in headline_list:
        link1 = i.find_all('a')
        if link1:
            headline = link1[0].text.strip()
            forward_observer_list.append(headline)
    print('Getting data from Forward Observer')
    return forward_observer_list


# Scraping from OANN
def oann():
    oann_list = []
    url = 'https://www.censored.news/OANN.htm'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

    time.sleep(random.randint(5, 9))

    webpage = requests.get(url, headers=headers)

    soup = BeautifulSoup(webpage.text, 'html.parser')

    headline_list = soup.find_all('p', attrs={'class': 'Headline'})

    for i in headline_list:
        link1 = i.find_all('a')
        if link1:
            headline = link1[0].text.strip()
            oann_list.append(headline)
    print('Getting data from OANN')
    return oann_list


# Scraping from The Post Millennial
def the_post_millennial():
    the_post_millennial_list = []
    url = 'https://www.censored.news/ThePostMillenial.htm'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106  Safari/537.36'}

    time.sleep(random.randint(5, 9))

    webpage = requests.get(url, headers=headers)

    soup = BeautifulSoup(webpage.text, 'html.parser')

    headline_list = soup.find_all('p', attrs={'class': 'Headline'})

    for i in headline_list:
        link1 = i.find_all('a')
        if link1:
            headline = link1[0].text.strip()
            the_post_millennial_list.append(headline)
    print('Getting data from The Post Millennial')
    return the_post_millennial_list
