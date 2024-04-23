import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class Practica09(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"./Activities/Classroom/Selenium/chromedriver.exe")
        self.driver.maximize_window()
        
    def test_openWindow(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(1)
        searchByName = driver.find_element_by_name("q")
        searchByName.send_keys("Selenium con el profe: Juan Antonio")
        time.sleep(1)
        searchByName.send_keys(Keys.RETURN)
        time.sleep(1)
        
        driver.execute_script('window.open('');')
        driver.switch_to.window(driver.window_handles[1])
        driver.get('https://incentivos.agenciaandaluzadelaenergia.es/Orden2016SIG/listado.jsp')
        time.sleep(3)
        inputName = driver.find_element_by_name('NOMBRE')
        inputName.send_keys('Barcelona')
        time.sleep(1)
        
        comboboxLine = driver.find_element_by_xpath('//*[@id="LINEA"]')
        option = comboboxLine.find_elements_by_tag_name('option')
        time.sleep(1)
        option[2].click()
        time.sleep(1)
        
        comboboxLine = driver.find_element_by_xpath('//*[@id="COMO"]')
        option = comboboxLine.find_elements_by_tag_name('option')
        time.sleep(1)
        option[2].click()
        time.sleep(1)
        
        comboboxLine = driver.find_element_by_xpath('//*[@id="CATEG"]')
        option = comboboxLine.find_elements_by_tag_name('option')
        time.sleep(1)
        option[2].click()
        time.sleep(1)
        
        comboboxLine = driver.find_element_by_xpath('//*[@id="PROV"]')
        option = comboboxLine.find_elements_by_tag_name('option')
        time.sleep(1)
        option[2].click()
        time.sleep(1)
        
        comboboxLine = driver.find_element_by_xpath('//*[@id="TIPOL"]')
        option = comboboxLine.find_elements_by_tag_name('option')
        time.sleep(1)
        option[2].click()
        time.sleep(1)
        
        comboboxLine = driver.find_element_by_xpath('//*[@id="LOCALIDAD"]')
        option = comboboxLine.find_elements_by_tag_name('option')
        time.sleep(1)
        option[2].click()
        time.sleep(1)
        
        comboboxLine = driver.find_element_by_xpath('//*[@id="ACT"]')
        option = comboboxLine.find_elements_by_tag_name('option')
        time.sleep(1)
        option[2].click()
        time.sleep(1)
        
        # for optionLine in option:
        #     optionLine.click()
        #     time.sleep(1)
        
        option[2].click()
        time.sleep(1)

    def tearDown(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass 
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main() 