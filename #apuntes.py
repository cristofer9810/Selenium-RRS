# Importar las bibliotecas necesarias
from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializar el controlador de Selenium
driver = webdriver.Chrome()

# Navegar a la página web que contiene la tabla
driver.get("https://www.example.com")

# Encontrar la tabla por su identificador o clase
table = driver.find_element(By.ID, "table_id")

# Obtener todas las filas de la tabla
rows = table.find_elements(By.TAG_NAME, "tr")

# Iterar a través de cada fila y extraer los datos de las celdas
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        print(cell.text)
    #print(valor)
""" 					rows = len(driver.find_elements(By.XPATH, "//*[@id='cursosTable']/tbody/tr"))
					print(rows)
					col = len(driver.find_elements(By.XPATH, "//*[@id='cursosTable']/tbody/tr[1]/th"))
					print(col)
					for n in range(2, rows+1):
						for b in range(1, col+1):
							celdas = driver.find_element(By.XPATH, "//*[@id='cursosTable']/tbody/tr["+str(n)+"]/td["+str(b)+"]").text
							print(celdas, end='                         ') """