from selenium import webdriver
import urllib

WEBDRIVER_PATH = "/Users/patrickmenendez/PycharmProjects/reddit_bot/chromedriver 3"
URL = "https://www.reddit.com/r/ProgrammerHumor/"

if __name__ == '__main__':

    # Setting up web driver
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(WEBDRIVER_PATH, options=options)

    # Opening webpage
    driver.get(URL)
    image_x_path = "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[4]/div[3]/div/div/div[2]"
    driver.find_element_by_xpath(image_x_path).click()
    image_x_path = "/html/body/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[5]/div/a"
    img_div = driver.find_element_by_xpath(image_x_path)
    href = img_div.get_attribute('href')
    print(href)
    # Close webdriver
    driver.quit()

