from sys import executable
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time



driver = webdriver.Chrome()
def test_rues(dato_usuario):
	empresa = []
	empresas = []
	registro = []
	registros = []
	driver.get("https://www.rues.org.co/?old=true")
	driver.maximize_window()
	time.sleep(3)
	try:
		rues = driver.find_element(By.XPATH, "//*[@id='modalInformativo']/div/div/div[3]/button")
		rues.click()
		time.sleep(2)
		rues = driver.find_element(By.XPATH, "//*[@id='txtNIT']")
		rues.send_keys(dato_usuario)
		rues.send_keys(Keys.ENTER)
		time.sleep(3)
		try:
			rues = driver.find_element(By.XPATH, "/html/body/div[1]/main[1]/div/div[4]").text
			print(rues) #La consulta por NIT no ha retornado resultados //*[@id="rmTable2_wrapper"]
			if 'La consulta por NIT no ha retornado resultados' in rues:
				time.sleep(2)
				driver.close()
				empresas = ["no hay no existe empresa"]
				registros = ["no hay no existe registro"]
				return empresas, registros
		except NoSuchElementException:
			print("Se continua con la operacion. ")
			time.sleep(2)
		rues = driver.find_element(By.XPATH, "//*[@id='rmTable2']/tbody/tr/td[1]")
		rues.click()
		time.sleep(2)
		rues = driver.find_element(By.XPATH, "//*[@id='rmTable2']/tbody/tr[2]/td/ul/li/span[2]/a")
		rues.click()
		time.sleep(2)
		try:
			valor = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div[1]/table")
		except NoSuchElementException:
			valor = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div[1]/div[1]/table")
		rows = valor.find_elements(By.TAG_NAME, "tr")
		for row in rows:
			cells = row.find_elements(By.TAG_NAME, "td")
			empresa = [cell.text for cell in cells]
			empresas.append(empresa)
			
		
		try:
			valor = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[2]/div/div[1]/div/div[2]/div/table")
		except NoSuchElementException:
			valor = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div[2]/div[2]/div/div[1]/div/div[2]/div/table")
		rows = valor.find_elements(By.TAG_NAME, "tr")
		for row in rows:
			cells = row.find_elements(By.TAG_NAME, "td")
			registro = [cell.text for cell in cells]
			registros.append(registro)
		
		
		registros = [[elemento.replace("'", '') for elemento in sublista] for sublista in registros]
		empresas = [[elemento.replace("'", '') for elemento in sublista] for sublista in empresas]
		print(empresas)
		print(registros)
		return empresas, registros
	except NoSuchElementException:
		print("No se detecto ninguna alerta en el tiempo especificado.")
		rues = driver.find_element(By.XPATH, "//*[@id='txtNIT']")
		rues.send_keys(dato_usuario)
		rues.send_keys(Keys.ENTER)
		time.sleep(3)
		try:
			rues = driver.find_element(By.XPATH, "/html/body/div[1]/main[1]/div/div[4]").text
			print(rues) #La consulta por NIT no ha retornado resultados //*[@id="rmTable2_wrapper"]
			if 'La consulta por NIT no ha retornado resultados' in rues:
				time.sleep(2)
				driver.close()
				empresas = ["no hay no existe empresa"]
				registros = ["no hay no existe registro"]
				return empresas, registros
		except NoSuchElementException:
			print("Se continua con la operacion. ")
			time.sleep(2)
		rues = driver.find_element(By.XPATH, "//*[@id='rmTable2']/tbody/tr/td[1]")
		rues.click()
		time.sleep(2)
		rues = driver.find_element(By.XPATH, "//*[@id='rmTable2']/tbody/tr[2]/td/ul/li[3]/span[2]/a")
		rues.click()
		time.sleep(2)
		""" try:
			rues = driver.find_element(By.XPATH, "//*[@id='card-info']/input")
			rues.click()
			time.sleep(2)
		except TimeoutException:
			print("No se detecto ninguna alerta en el tiempo especificado.") """
		valor = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div[1]/table")
		rows = valor.find_elements(By.TAG_NAME, "tr")
		for row in rows:
			cells = row.find_elements(By.TAG_NAME, "td")
			empresa = [cell.text for cell in cells]
			empresas.append(empresa)
			print(empresas)
		valor = driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[2]/div/div[1]/div/div[2]/div/table")
		rows = valor.find_elements(By.TAG_NAME, "tr")
		for row in rows:
			cells = row.find_elements(By.TAG_NAME, "td")
			registro = [cell.text for cell in cells]
			registros.append(registro)
			print(registros)
		registros = [[elemento.replace("'", '') for elemento in sublista] for sublista in registros]
		empresas = [[elemento.replace("'", '') for elemento in sublista] for sublista in empresas]
		return empresas, registros
	""" finally:
		print('se fue al finally')
		return empresa, registro """
	

#test_rues(dato_usuario= 800021545)