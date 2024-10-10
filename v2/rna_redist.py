from sys import executable
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


driver = webdriver.Chrome()
	
def test_rna(dato_usuario):
	licencia = 'no existe'
	estado = 'no existe'
	rtm = 'no existe'
	result_dict = 'no existe'
	#80186171 19317310 1024574241
	driver.get("https://rndc.mintransporte.gov.co/MenuPrincipal/tabid/204/language/es-MX/Default.aspx?returnurl=%2f")
	time.sleep(3)
	rna = driver.find_element(By.XPATH, "//*[@id='dnn_ctr678_VigiaPublico_Cat']").text
	print(rna)
	partes = rna.split('+')
	suma_uno = partes[0].strip()
	suma_dos = partes[1].strip()		
	suma_uno = int(suma_uno)
	suma_dos = int(suma_dos)
	resultado = suma_uno + suma_dos
	print(resultado)
	try:
		rna = driver.find_element(By.XPATH, "//*[@id='dnn_ctr678_VigiaPublico_Resultado']")
		rna.send_keys(resultado)
		rna = driver.find_element(By.XPATH, "//*[@id='dnn_ctr678_VigiaPublico_CEDULA']")
		rna.send_keys(dato_usuario)
		rna = driver.find_element(By.XPATH, "//*[@id='dnn_ctr678_VigiaPublico_btEstado']")
		rna.click()
		time.sleep(3)		
		rna = driver.find_element(By.NAME, "dnn$ctr678$VigiaPublico$ESTADOMATRICULA")
		estado = rna.get_attribute("value")
		print(estado)		
		rna = driver.find_element(By.XPATH, "//*[@id='dnn_ctr678_VigiaPublico_SOAT']")
		licencia = rna.get_attribute("value")
		print(licencia)		
		rna = driver.find_element(By.XPATH, "//*[@id='dnn_ctr678_VigiaPublico_RTM']")
		rtm = rna.get_attribute("value")
		print(rtm)
		return estado, licencia, rtm, dato_usuario
	except NoSuchElementException:		
			print('no existe')
				
				
				
				
				
				
				
				
