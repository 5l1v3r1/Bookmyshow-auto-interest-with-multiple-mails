#i added 5 time auto interest button code if you want more times means add from line 3 to 25 and add these code in 122 line for more automatic interest button click and otp will not enter manaully you must enter that one 
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://in.bookmyshow.com/bengaluru/movies/vikram-vedha/ET00319143")  #change url to which movie you want to do auto interest button click and do these process for below code also or else use url open from text file that code in last lines

time.sleep(8)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys("dontknow23@gmail.com") #replace with your mail or use gmail dot generator for generate enormous mails in one mail or use temp mail do replace in below codes also

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(15)

driver.close()

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/vikram-vedha/ET00319143") 

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys("d.ontknow23@gmail.com")

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(15)

driver.close()

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/vikram-vedha/ET00319143") 

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys("dontknow2.3@gmail.com")

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(15)

driver.close()

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/vikram-vedha/ET00319143") 

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys("dontkno.w23@gmail.com")

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(15)

driver.close()

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/vikram-vedha/ET00319143") 

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys("don.tknow23@gmail.com")

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(15)

driver.close()

#if you are bore to add url in every code in driver.get("  ")then open link from text file  use below code(remove the hastag and add) after these line driver =webdriver.Chrome() of every code where they you see 
#and don't forgot to add hastag to driver.get("  ")
#with open("urls.txt") as f:
    #for url in f:
        #driver.get(url)


