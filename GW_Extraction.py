from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome()
driver.get("https://indiawris.gov.in/wris/#/groundWater")
driver.implicitly_wait(150)
time.sleep(10)
#implicitly wait will set the same amount of wait for all the elements in the driver

#wait = WebDriverWait(driver, 10)
#time_step_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "time_step")))

#Switching to frame to acess elements
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='ng-star-inserted']"))

#selecting timestep
time_step = Select(driver.find_element(By.ID,"time_step"))
time_step.select_by_value("Seasonly")
print("Time Step Selected")
time.sleep(10)

#selecting season
season = Select(driver.find_element(By.ID, "seasonSelect"))
season.select_by_value("1")
print("Season Selected")
time.sleep(10)

#selecting year
year = Select(driver.find_element(By.ID, "select_seasonal_year"))
year.select_by_value("2011")
print("Year Selected")
time.sleep(30)

#selecting State
state = Select(driver.find_element(By.ID, "select_state"))
state.select_by_value("UK")
print("State Selected")
time.sleep(20)

#Downloading the excel 
Dowload = driver.find_element(By.CSS_SELECTOR, "button[class='dt-button buttons-excel buttons-html5 float-end'] span") 
Dowload.click()
print("Download Clicked")
time.sleep(5)

#filling the survey form (optional)
try:
    Student = driver.find_element(By.ID, "Student")
    Student.click()

    Name = driver.find_element(By.ID, "nameID")
    Name.send_keys("Aryaman")
    
    Email = driver.find_element(By.ID, "emailID")
    Email.send_keys("sriva.aryaman@protonmail.com")
    
    Submit = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
    Submit.click()
    print("Survey filled")
except:
    print("Survey Not Needed")

time.sleep(30)

print("Finished")