from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import sys
import sqlite3
import config
import csv

options = Options()
options.page_load_strategy = 'normal'
options.set_preference('javascript.enabled', True)
options.headless = True
db = sqlite3.connect('items.db')
cur = db.cursor()
url = "https://evemarketer.com/types/"
driver = webdriver.Firefox(options=options, executable_path= "geckodriver.exe")

def search(ids):
	driver.get((str(url)+str(ids)))
	driver.implicitly_wait(config.delay)

	item_name_div = driver.find_element(By.CLASS_NAME, "item-name")
	item_name_h = item_name_div.find_element(By.TAG_NAME, "h2")
	name = item_name_h.text
	# print(item_name_h.text)

	type_ul = driver.find_element(By.CLASS_NAME, "item-group")
	type_li = type_ul.find_elements(By.TAG_NAME, "li")
	type_text = ""
	for e in type_li:
		type_text = type_text + str(e.text) + "/"

	if(not(is_in_base(ids))):
		insert_in_base(ids, name, type_text)
		print(str(ids) + " | " + str(name) + " | " + str(type_text))

	driver.quit()
	db.close()

def is_in_base(ids):
	for row in cur.execute("SELECT * FROM items"):
		if(row[0] == ids):
			return True
	return False

def insert_in_base(ids, name, types):
	cur.execute("INSERT INTO items VALUES (" + str(ids) + ",'" + str(name) + "','" + str(types) + "')")
	db.commit()
	

if __name__ == "__main__":
	with open(sys.argv[1], newline='') as f:
		reader = csv.reader(f)
		for row in reader:
			search(row[0])