'''Автоматизувати процес замовлення робота за допомогою Selenium
1. Отримайте та прочитайте дані з "https://robotsparebinindustries.com/orders.csv". 
Увага! Файл має бути прочитаний з сервера кожного разу при запускі скрипта, не зберігайте файл локально.
2. Зайдіть на сайт "https://robotsparebinindustries.com/"
3. Перейдіть у вкладку "Order your robot"
4. Для кожного замовлення з файлу реалізуйте наступне:
    - закрийте pop-up, якщо він з'явився. Підказка: не кожна кнопка його закриває.
    - оберіть/заповніть відповідні поля для замовлення
    - натисніть кнопку Preview та збережіть зображення отриманого робота. 
    Увага! Зберігати треба тільки зображення робота, а не всієї сторінки сайту.
    - натисніть кнопку Order та збережіть номер чеку. Увага! Інколи сервер тупить 
    і видає помилку, але повторне натискання кнопки частіше всього вирішує проблему. 
    Дослідіть цей кейс.
    - переіменуйте отримане зображення у формат <номер чеку>_robot. 
    Покладіть зображення в директорію output (яка має створюватися/очищатися під час запуску скрипта).
    - замовте наступного робота (шляхом натискання відповідної кнопки)
5. Для загального розуміння можна переглянути відео https://www.youtube.com/watch?v=0uvexJyJwxA&ab_channel=Robocorp'''

import requests
import os
import time
import shutil

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


class RobotPlacer:
	BASE_URL = 'https://robotsparebinindustries.com/orders.csv'

	def __init__(self):
		self.list_of_orders = self.get_data()
		self.url = "https://robotsparebinindustries.com/"
		self.driver = None
		self.folder = 'output' 

	def get_data(self):
		page = requests.get(self.BASE_URL).text
		lines = [line.split(',') for line in page.split('\n')]
		return lines[1:]

	def placer_order(self):
		self._folder()
		self.open_site()
		self.robot_order()
		for order in self.list_of_orders:
			self.pop_up_close()
			self.fill_inform(order)
			self._wait_for_element('[id="preview"]').click()
			self.submit_order()
			self.get_screenshot_robot()
			self._wait_for_element('[id="order-another"]').click()

	def open_site(self):
		self.driver.get(self.url)
		self._wait_for_element('.nav-link')

	def _wait_for_element(self, selector, by=By.CSS_SELECTOR, timeout=10):
		condition = EC.presence_of_element_located((by, selector))
		element = WebDriverWait(self.driver, timeout).until(condition)
		return element

	def robot_order(self):
		self._wait_for_element('[class="nav-link"]').click()
		self._wait_for_element('.btn-dark')
		
	def pop_up_close(self):
		self._wait_for_element('.btn-dark').click()
		self._wait_for_element('a.nav-link')

	def fill_inform(self, data_item):
		#head
		self._wait_for_element('[id="head"]').click()
		Select(self._wait_for_element('[id="head"]')).select_by_index(data_item[1])
		self._wait_for_element('[id="head"]').click()
		#body
		self._wait_for_element(f'[for="id-body-{data_item[2]}"]').click()
		#legs
		self._wait_for_element("input[placeholder='Enter the part number for the legs']").send_keys(data_item[3])
		#Adress
		self._wait_for_element('[name="address"]').clear()
		self._wait_for_element('[name="address"]').send_keys(data_item[4])

	def submit_order(self):
		self._wait_for_element('[id="robot-preview-image"]')
		self._wait_for_element('[id="order"]').click()
		try:
			self._wait_for_element('[id="order-completion"]')
		except TimeoutException:
			self.submit_order()

	def get_screenshot_robot(self):
		time.sleep(1)
		chek_number = self.driver.find_element(By.CSS_SELECTOR,'.badge.badge-success').text
		self._wait_for_element('[id="robot-preview-image"]')
		robot_preview = self.driver.find_element(By.ID, 'robot-preview-image')
		robot_preview.screenshot(f'output/{chek_number}_robot.png')

	def _folder(self):
		chek_folder = os.path.exists(self.folder)
		if chek_folder:
			shutil.rmtree(self.folder)
		os.makedirs(self.folder)

	def __enter__(self):
		self.driver = self.__init_driver()
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.driver.close()

	def __init_driver(self):
		service = Service(ChromeDriverManager().install())
		chrome_options = ChromeOptions()
		service_args = [
			'--start-maximized',
			'--no-sandbox',
			'--disable-web-security',
			'--allow-running-insecure-content',
			'--hide-scrollbars',
			'--disable-setuid-sandbox',
			'--profile-directory=Default',
			'--ignore-ssl-errors=true',
			'--disable-dev-shm-usage'
		]
		for arg in service_args:
			chrome_options.add_argument(arg)
		chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
		chrome_options.add_experimental_option('prefs', {
				'profile.default_content_setting_values.notifications': 2,
				'profile.default_content_settings.popups': 0
			})
		driver = Chrome(service=service, options=chrome_options)
		#driver.maximize_window()
		return driver
		

if __name__ == '__main__':
	with RobotPlacer() as placer:
		placer.placer_order()
