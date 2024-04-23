from selenium import webdriver
PATH = ".\Activities\Classroom\selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=_eeS24nuHUm_P6918HPgz8kGucio5uRAucnQjmvXLKJUNURCSlVMNDg4RTBQRk9JNkhYMEFSUFJMOS4u")

arreglo = ['Jesus Emmanuel', 'Guzman Covarrubias', 'Ingenieria en Computacion', 'Universidad de Especialidades UNE']

search_box = driver.find_elements_by_tag_name('input')
button = driver.find_elements_by_tag_name('button')

num_inputs = len(search_box)

for x in range(len(search_box)):
    search_box[x].send_keys(arreglo[x])
    
button[1].click()

time.sleep(5)
driver.quit()