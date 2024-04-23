from selenium import webdriver
import time

# PATH = "C:/Users/guzma/OneDrive/Escritorio/chromedriver.exe"
PATH = ".\Activities\Classroom\selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://google.com.mx")

# Buscar el cuadro de búsqueda de Google por su nombre
search_box = driver.find_element_by_name('q')

# Simular la escritura en el cuadro de búsqueda
search_box.send_keys("peso pluma")

# Enviar el formulario (simulando presionar la tecla Enter)
search_box.submit()



driver.quit()
