import selenium.webdriver as webdriver
from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

class Test(TestCase):

    def test(self):
        driver = webdriver.Chrome()

        try:
            driver.get("http://127.0.0.1:8000/")

            login_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/login_user']"))
            )

            time.sleep(2)


            login_button.click()

            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
            )

            for x in "jan.kowalski@onet.pl":
                time.sleep(0.10)
                email_input.send_keys(x)

            password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
            )

            for x in "Wojtek250":
                time.sleep(0.25)
                password_input.send_keys(x)

            time.sleep(1)

            password_input.send_keys(Keys.ENTER)

            time.sleep(2)

            driver.get("http://127.0.0.1:8000/account")

            time.sleep(5)

            driver.get("http://127.0.0.1:8000/")

            time.sleep(2)

            reservation = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='Zarezerwuj']"))
            )

            reservation.click()

            time.sleep(2)

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(2)

            remove_reservation = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='Zwolnij rezerwacje']"))
            )

            remove_reservation.click()

            time.sleep(2)

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(2)

            driver.execute_script("window.scrollTo(0, 0);")

            time.sleep(2)

            books_filter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='Książki']"))
            )

            books_filter.click()

            time.sleep(2)

            audiobooks_filter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='Audiobooki']"))
            )

            audiobooks_filter.click()

            time.sleep(2)

            films_filter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='Filmy']"))
            )

            films_filter.click()

            time.sleep(2)

            games_filter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='Gry']"))
            )

            games_filter.click()

            time.sleep(2)

            all_filter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='Wszystko']"))
            )

            all_filter.click()

            time.sleep(2)

            logout_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/logout_user']"))
            )

            logout_button.click()

            time.sleep(5)
        finally:
            driver.quit()




