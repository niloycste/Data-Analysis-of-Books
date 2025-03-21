import time
import pandas as pd
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By

book_details = []

columns = ['title', 'author' ,'description', 'genres', 'ratings', 'number of ratings', 'number of reviews', '5 star', '4 star', '3 star', '2 star', '1 star']

def main():

    driver = webdriver.Chrome()
    
    df = pd.read_csv("url_files/book_urls_exceeded_expectations.csv")

    urls = df['urls'].to_list()
    
    for url in tqdm(urls[0:len(urls)]):

        driver.get(url=url)

        # print(f"{url}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        try:
            if driver.find_element(by=By.XPATH, value="//div[@class='Overlay__window']").is_displayed():
                print("Advertisement found....")
                driver.find_element(by=By.XPATH, value="//i[@class='Icon CloseIcon']").click()
            time.sleep(2)
        except:
            pass
        
        try:
            title = driver.find_element(by=By.XPATH, value="//h1[@class='Text Text__title1']").text
        except:
            title = None
        
        try:
            author_name = driver.find_element(by=By.XPATH, value="//a[@class='ContributorLink']/span").text
        except:
            author_name = None
        
        try:
            description = driver.find_element(by=By.XPATH, value="//div[@class='BookPageMetadataSection__description']/div/div[@class='TruncatedContent__text TruncatedContent__text--large']/div/div/span").text.replace("\n", "")
        except:
            description = None
        
        try:
            ratings = driver.find_element(by=By.XPATH, value="//div[@class='RatingStatistics__rating']").text
        except:
            ratings = None

        try:
            count_of_ratings = driver.find_element(by=By.XPATH, value="//div[@class='RatingStatistics__meta']/span[@data-testid='ratingsCount'][1]").text
        except:
            count_of_ratings = None

        try:
            number_of_reviews = driver.find_element(by=By.XPATH, value="//span[@data-testid='reviewsCount']").text
        except:
            number_of_reviews = None

        try:
            _5_star = driver.find_element(by=By.XPATH, value="//div[@data-testid='labelTotal-5']").text.split()[0]
        except:
            _5_star = None

        try:
            _4_star = driver.find_element(by=By.XPATH, value="//div[@data-testid='labelTotal-4']").text.split()[0]
        except:
            _4_star = None

        try:
            _3_star = driver.find_element(by=By.XPATH, value="//div[@data-testid='labelTotal-3']").text.split()[0]
        except:
            _3_star = None

        try:
            _2_star = driver.find_element(by=By.XPATH, value="//div[@data-testid='labelTotal-2']").text.split()[0]
        except:
            _2_star = None

        try:
            _1_star = driver.find_element(by=By.XPATH, value="//div[@data-testid='labelTotal-1']").text.split()[0]
        except:
            _1_star = None

        try: 
            genres = driver.find_elements(by=By.XPATH, value="//div[@class='BookPageMetadataSection__genres']/ul/span[1]/span/a")

            text_genres = []

            for genre in genres:
                text_genres.append(genre.text) 

            buttons = driver.find_elements(by=By.XPATH, value="//div[@class='Button__container']/button[@class='Button Button--tag-inline Button--small']")
            buttons[0].click()

            genres = driver.find_elements(by=By.XPATH, value="//div[@class='BookPageMetadataSection__genres']/ul/span[2]/span/a")
            for genre in genres:
                text_genres.append(genre.text) 
        except:
            text_genres = []

        book_details.append({
            'title': title,
            'author': author_name,
            "description": description,
            'genres': text_genres,
            'ratings': ratings,
            "number of ratings": count_of_ratings,
            "number of reviews": number_of_reviews,
            "5 star": _5_star,
            "4 star": _4_star,
            "3 star": _3_star,
            "2 star": _2_star,
            "1 star": _1_star,
        })

        # print(book_details)

        df = pd.DataFrame(columns=columns, data=book_details)
        df.to_csv("books_details_files/book_details_exceeded_expectations.csv", index=False)
        
if __name__ == "__main__":
    main()