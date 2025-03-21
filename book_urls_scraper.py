from tqdm import tqdm
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

columns = ['title', 'urls']
book_urls = []

def main():
    # base_url = "https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once"
    # base_url = "https://www.goodreads.com/list/show/1043.Books_That_Should_Be_Made_Into_Movies"
    # base_url = "https://www.goodreads.com/list/show/1.Best_Books_Ever"
    # base_url = "https://www.goodreads.com/list/show/94.Books_With_Unforgettable_Characters"
    # base_url = "https://www.goodreads.com/list/show/19106.MUST_READS_"
    base_url = "https://www.goodreads.com/list/show/423.Books_That_Exceeded_Your_Expectations"

    driver = webdriver.Chrome()
    
    df = pd.read_csv("url_files/book_urls.csv")

    titles = df['title'].to_list()
    urls = df['urls'].to_list()

    for page_no in tqdm(range(100)):
        url = f"{base_url}?page={page_no+1}" 
        driver.get(url=url)
        table = driver.find_element(by=By.XPATH, value="//table[@class='tableList js-dataTooltip']")
        rows = table.find_elements(by=By.XPATH, value="./tbody/tr[@itemtype='http://schema.org/Book']/td[@width='100%']/a")

        for row in rows:
            title = row.text
            url = row.get_attribute("href")
            # print(f"title: {title}, Urls: {url}")

            if title not in titles or url not in urls:
                print("Match Not Found....")
                book_urls.append({
                    'title': title,
                    "urls": url
                })
            # print(book_urls)
            else:
                print("Match Found..")
                continue

        df = pd.DataFrame(columns=columns, data=book_urls)
        df.to_csv("url_files/book_urls_exceeded_Expectations.csv", index=False)

if __name__ == "__main__":
    main()