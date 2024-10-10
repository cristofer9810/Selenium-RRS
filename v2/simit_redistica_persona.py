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
def test_simitPerson(dato_usuario):
	resumen = 'no existe' 
	comparendo = 'no existe'
	multas = 'no existe'
	acuerdos = 'no existe'
	cedula = 'no existe'
	total = 'no existe'
	datos_fila = ['no existe']
	driver.get("https://fcm.org.co/simit/#/home-public")
	time.sleep(3)
	try:
		print()
		WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//*[@id='whcModal']/div/div/div")))
		print("Manejando la alerta modal...")
		time.sleep(10)
		#WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//*[@id='whcModal']/div/div/div")))
		#print("Manejando la alerta modal x2...")
		#time.sleep(10)
	except TimeoutException:
		print("No se detecto ninguna alerta en el tiempo especificado.")
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='modalInformation']/div/div/div[1]/button")))
	simit = driver.find_element(By.XPATH, "//*[@id='modalInformation']/div/div/div[1]/button")
	simit.click()
	simit = driver.find_element(By.XPATH, "//*[@id='txtBusqueda']")
	simit.send_keys(dato_usuario)
	simit.send_keys(Keys.ENTER)
	time.sleep(7)
	try:
		simit = driver.find_element(By.XPATH, "//*[@id='mainView']/div/div[1]/div/div[2]/div[2]/h3").text
		print(simit)
		if "No tienes comparendos ni multas registradas en Simit" in simit: 
			resumen = driver.find_element(By.XPATH, "//*[@id='mainView']/div/div[1]/div/div[1]/div/div/div[1]").text
			print(resumen)
			comparendo = driver.find_element(By.XPATH, "//*[@id='mainView']/div/div[1]/div/div[1]/div/div/div[2]").text
			print(comparendo)
			multas = driver.find_element(By.XPATH, "//*[@id='mainView']/div/div[1]/div/div[1]/div/div/div[3]").text
			print(multas)
			acuerdos = driver.find_element(By.XPATH, "//*[@id='mainView']/div/div[1]/div/div[1]/div/div/div[4]").text
			print(acuerdos)
			total = driver.find_element(By.XPATH, "//*[@id='mainView']/div/div[1]/div/div[1]/div/div/div[5]").text
			print(total)
			#boton paz y salvo 
			simit = driver.find_element(By.XPATH, "//*[@id='mainView']/div/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]/a")
			simit.click()
			simit = driver.find_element(By.XPATH, "//*[@id='formPazSalvo']/div[2]/button")
			simit.click()
			time.sleep(2)
			ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
			time.sleep(2)
			simil = driver.find_element(By.XPATH, "//*[@id='mainView']/div/div[1]/div/div[2]/div[2]").text
			partes = simil.split('.')
			simil = partes[0].strip()
			simil_dos = partes[1].strip()
			simil = driver.find_element(By.XPATH, "//*[@id='mainView']/div/div[1]/div/div[2]/div[2]/a").text
			partes = simil.split('(')
			historial = partes[1].strip()
			partes = historial.split(')')
			historial = partes[0].strip()
			print(historial)
			if "0" in historial:
				print("no tiene historial")
				return resumen, comparendo, multas, acuerdos, dato_usuario, cedula, total, datos_fila
			else:
				simit = driver.find_element(By.XPATH, "//*[@id='mainView']/div/div[1]/div/div[2]/div[2]/a")
				simit.click()
				time.sleep(3)
				valor = driver.find_element(By.XPATH, "//*[@id='cursosTable']")
				rows = valor.find_elements(By.TAG_NAME, "tr")
				for row in rows:
					cells = row.find_elements(By.TAG_NAME, "td")
					datos_filas = [cell.text for cell in cells]
					datos_fila.append(datos_filas)
					print(datos_fila)
				return resumen, comparendo, multas, acuerdos, dato_usuario, cedula, total, datos_fila
		else: 
			print('ocurrio algo')
	except NoSuchElementException:
		resumen = driver.find_element(By.XPATH, "//*[@id='resumenEstadoCuenta']/div/div/div[5]").text
		print(resumen)
		comparendo = driver.find_element(By.XPATH, "//*[@id='resumenEstadoCuenta']/div/div/div[2]").text
		print(comparendo)
		multas = driver.find_element(By.XPATH, "//*[@id='resumenEstadoCuenta']/div/div/div[3]").text
		print(multas)
		acuerdos = driver.find_element(By.XPATH, "//*[@id='resumenEstadoCuenta']/div/div/div[4]").text
		print(acuerdos)
		cedula = driver.find_element(By.XPATH, "//*[@id='resumenEstadoCuenta']/div/div/div[6]").text
		print(cedula)
		total = driver.find_element(By.XPATH, "//*[@id='resumenEstadoCuenta']/div/div/div[7]").text
		print(total)
		#guardar paz y salvo
		simit = driver.find_element(By.XPATH, "//*[@id='generaPazSalvo']/div/a")
		simit.click()
		simit = driver.find_element(By.XPATH, "//*[@id='modal-paz-salvo']/div/div/div[2]/div/div[2]/a")
		simit.click()
		time.sleep(2)
		ActionChains(driver).key_down(Keys.ESCAPE).key_up(Keys.ESCAPE).perform()
		time.sleep(2)
		#guardar estado
		simit = driver.find_element(By.XPATH, "//*[@id='enviarCorreo']/div/a")
		simit.click()
		simit = driver.find_element(By.XPATH, "//*[@id='modal-estado-cuenta']/div/div/div[2]/div/div[2]/a")
		simit.click()
		time.sleep(2)
		ActionChains(driver).key_down(Keys.ESCAPE).key_up(Keys.ESCAPE).perform()
		time.sleep(2)
		# ver historial
		simil = driver.find_element(By.XPATH, "//*[@id='historialCursos']/div/a").text
		partes = simil.split('(')
		historial = partes[1].strip()
		partes = historial.split(')')
		historial = partes[0].strip()
		print(historial)
		if "0" in historial:
				print("no tiene historial")
				return resumen, comparendo, multas, acuerdos, dato_usuario, cedula, total, datos_fila
		else:
				simit = driver.find_element(By.XPATH, "//*[@id='historialCursos']/div/a")
				simit.click()
				time.sleep(3)
				valor = driver.find_element(By.XPATH, "//*[@id='cursosTable']")
				rows = valor.find_elements(By.TAG_NAME, "tr")
				for row in rows:
					cells = row.find_elements(By.TAG_NAME, "td")
					datos_filas = [cell.text for cell in cells]
					datos_fila.append(datos_filas)
					print(datos_fila)
				return resumen, comparendo, multas, acuerdos, dato_usuario, cedula, total, datos_fila
		
		
		
#test_simitPerson(dato_usuario=1233903863)		
		
		
