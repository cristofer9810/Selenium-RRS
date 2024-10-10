from selenium import webdriver
import os
from rues import test_rues
from rna_redist import test_rna
from simit_redistica_persona import test_simitPerson
from simit_redistica_placa import test_simitPlaca
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime
from selenium.webdriver.common.alert import Alert
import threading
import pdfkit
import jinja2 
from PyPDF2 import PdfMerger


from concurrent.futures import ThreadPoolExecutor
import time


def obtener_dato_usuario():
    # Solicitar un dato al usuario
    print('1. persona ')
    print('2. placa  ')
    print('3. empresa')
    desision = input("selecione un numero: ")
    if desision == '1':
        dato_usuario = input("Por favor, ingrese un dato para persona: ")
        return dato_usuario, desision
    elif desision == '2':
        dato_usuario = input("Por favor, ingrese un dato para placa: ")
        return dato_usuario, desision
    elif desision == '3':
        dato_usuario = input("Por favor, ingrese un dato para empresa: ")
        return dato_usuario, desision

def simit_placa(dato_usuario):
    resumen, comparendo, multas, acuerdos, dato_usuario, total, datos_fila = test_simitPlaca(dato_usuario)
    today_date = datetime.today().strftime("%d %m, %Y")
    texto = {'resumen': resumen,'comparendo': comparendo, 'multas': multas, 'acuerdos': acuerdos, 'total': total, 'datos_fila': datos_fila, 'today_date': today_date} 
    template_loader = jinja2.FileSystemLoader('C:\\Users\\Public\\oet\\GPS\\redistica_selenium\\v2\\plantilla')
    template_env = jinja2.Environment(loader=template_loader)
    html_template = 'plantilla.html'
    template = template_env.get_template(html_template)
    output_text = template.render(texto)
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    output_pdf =dato_usuario+'_pdf_generado.pdf'
    pdfkit.from_string(output_text, output_pdf, configuration=config, css='./plantilla/reporte.css')
    carpetas_entrada = ["C:\\Users\\Public\\oet\\GPS\\redistica_selenium\\"+dato_usuario+"_pdf_generado.pdf", "H:\\Descargas\\Estado de cuenta.pdf"] #C:\Users\crist\Downloads  H:\\Descargas\\Paz y Salvo.pdf
    archivo_salida = dato_del_usuario+"_resultado.pdf"
    unir_pdfs(carpetas_entrada, archivo_salida, dato_del_usuario)

def rna_persona(dato_usuario):
    # Simular la tarea de la automatizacion 1  pip install PyPDF2
    #test_rna(dato_usuario, result_dict)
    estado, licencia, rtm, dato_usuario = test_rna(dato_usuario)
    #texto_uno = {'estado': estado, 'licencia': licencia, 'rtm': rtm}
    print(estado, licencia, rtm, dato_usuario)
    return estado, licencia, rtm

def empresa_rues(dato_usuario):
    
    empresas, registros = test_rues(dato_usuario)
    print(empresas, registros)
    return empresas, registros

def simit_persona(dato_usuario):
    # Simular la tarea de la automatizacion 2
    #test_simitPerson(dato_usuario, result_dict)
    resumen, comparendo, multas, acuerdos, dato_usuario, cedula, total, datos_fila  = test_simitPerson(dato_usuario)
    #texto_dos = {'resumen': resumen, 'comparendo': comparendo, 'multas': multas, 'acuerdos': acuerdos, 'cedula': cedula, 'total': total} 
    print(resumen, comparendo, multas, acuerdos, dato_usuario, cedula, total, datos_fila)
    return resumen, comparendo, multas, acuerdos, dato_usuario, cedula, total, datos_fila

def generar_persona(estado, licencia, rtm, resumen, comparendo, multas, acuerdos, dato_usuario, cedula, total, datos_fila):
    print(estado, licencia, rtm, resumen, comparendo, multas, acuerdos, dato_usuario, total, datos_fila)
    today_date = datetime.today().strftime("%d %m, %Y")
    #resumen, comparendo, multas, acuerdos, cedula, total, datos_fila, dato_usuario, result_dict = test_simitPerson 
    texto = {'estado': estado, 'licencia': licencia, 'rtm': rtm, 'resumen': resumen,
             'comparendo': comparendo, 'multas': multas, 'acuerdos': acuerdos, 'cedula': cedula, 'total': total, 'datos_fila': datos_fila, 'today_date': today_date} 
    template_loader = jinja2.FileSystemLoader('C:\\Users\\Public\\oet\\GPS\\redistica_selenium\\v2\\plantilla')
    template_env = jinja2.Environment(loader=template_loader)
    html_template = 'plantilla.html'
    template = template_env.get_template(html_template)
    output_text = template.render(texto)
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    output_pdf ='pdf_generado.pdf'
    pdfkit.from_string(output_text, output_pdf, configuration=config, css='./plantilla/reporte.css')
    
    

def generar_persona_rues(estado, licencia, rtm, resumen, comparendo, multas, acuerdos, dato_usuario, cedula, total, datos_fila, empresas, registros):
    print(estado, licencia, rtm, resumen, comparendo, multas, acuerdos, dato_usuario, total, datos_fila)
    today_date = datetime.today().strftime("%d %m, %Y")
    #resumen, comparendo, multas, acuerdos, cedula, total, datos_fila, dato_usuario, result_dict = test_simitPerson 
    texto = {'estado': estado, 'licencia': licencia, 'rtm': rtm, 'resumen': resumen,
             'comparendo': comparendo, 'multas': multas, 'acuerdos': acuerdos, 'cedula': cedula, 'dato_usuario': dato_usuario, 'total': total, 'datos_fila': datos_fila, 'empresas': empresas, 'registros': registros, 'today_date': today_date} 
    template_loader = jinja2.FileSystemLoader('C:\\Users\\Public\\oet\\GPS\\redistica_selenium\\v2\\plantilla')
    template_env = jinja2.Environment(loader=template_loader)
    html_template = 'plantilla_rues.html'
    template = template_env.get_template(html_template)
    output_text = template.render(texto)
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    output_pdf ='pdf_generado.pdf'
    pdfkit.from_string(output_text, output_pdf, configuration=config, css='./plantilla/reporte.css')
    

def unir_pdfs(carpetas_entrada, archivo_salida):
    # Crear un objeto PDF merger
    merger = PdfMerger()

    try:
        for carpeta in carpetas_entrada:
             merger.append(carpeta)

        # Escribir el archivo de salida
        with open(archivo_salida, 'wb') as salida:
            merger.write(salida)

        print(f'Se unieron correctamente los archivos en {archivo_salida}')

    except Exception as e:
        print(f'Error al unir los archivos PDF: {e}')


if __name__ == "__main__":
    
    # Obtener el dato del usuario antes de ejecutar las tareas
    dato_del_usuario, decicion  = obtener_dato_usuario()
    # Esperar a que ambas automatizaciones terminen
    if '1' in decicion:
        # Crear un ThreadPoolExecutor con 2 hilos
        with ThreadPoolExecutor(max_workers=2) as executor:
            # Ejecutar las dos automatizaciones al mismo tiempo
            future1 = executor.submit(rna_persona, dato_del_usuario)
            future2 = executor.submit(simit_persona, dato_del_usuario)
            estado, licencia, rtm = future1.result()
            resumen, comparendo, multas, acuerdos, dato_usuario, cedula, total, datos_fila = future2.result()
        generar_persona(estado, licencia, rtm, resumen, comparendo, multas, acuerdos, dato_usuario, cedula, total, datos_fila)
        carpetas_entrada = ["C:\\Users\\Public\\oet\\GPS\\redistica_selenium\\pdf_generado.pdf", "H:\\Descargas\\Paz y Salvo.pdf"]
        archivo_salida = dato_del_usuario+"_resultado.pdf"
        unir_pdfs(carpetas_entrada, archivo_salida)
    elif '2' in decicion:
         simit_placa(dato_del_usuario)
    elif '3' in decicion:
        #empresa_rues(dato_del_usuario)
        with ThreadPoolExecutor(max_workers=3) as executor:
            # Ejecutar las dos automatizaciones al mismo tiempo
            future1 = executor.submit(rna_persona, dato_del_usuario)
            future2 = executor.submit(simit_persona, dato_del_usuario)
            future3 = executor.submit(empresa_rues, dato_del_usuario)
            estado, licencia, rtm = future1.result()
            resumen, comparendo, multas, acuerdos, dato_usuario, cedula, total, datos_fila = future2.result()
            empresa, registro = future3.result()
        generar_persona_rues(estado, licencia, rtm, resumen, comparendo, multas, acuerdos, dato_usuario, cedula, total, datos_fila, empresa, registro)
        carpetas_entrada = ["C:\\Users\\Public\\oet\\GPS\\redistica_selenium\\pdf_generado.pdf", "H:\\Descargas\\Paz y Salvo.pdf"] #C:\Users\crist\Downloads  H:\\Descargas\\Paz y Salvo.pdf
        archivo_salida = dato_del_usuario+"_resultado.pdf"
        unir_pdfs(carpetas_entrada, archivo_salida)
    
