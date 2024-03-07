from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()
chrome_driver.get("https://the-internet.herokuapp.com/login")

USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"

username_input_element = chrome_driver.find_element(By.ID, 'username')
password_input_element = chrome_driver.find_element(By.ID, 'password')
boton_element = chrome_driver.find_element(By.XPATH, '//*[@id="login"]/button')

def hacer_login(username: str, password: str):
    username_input_element.send_keys(username)
    password_input_element.send_keys(password)
    boton_element.click()


def caso_de_prueba_1_login_falla():
    """
    Caso de prueba 1:
        Criterios de aceptación:
            - Que falle cuando se ingresa usuario y contraseña "admin"
            - Que muestre una alerta del fallo
    """
    username = "admin"
    password = "admin"
    hacer_login(username, password)
    
    sleep(2)

    bandera_fallo_element = chrome_driver.find_element(By.XPATH, '//*[@id="flash"]')
    
    if bandera_fallo_element.is_displayed():
        print("Fallo de manera visible para el usuario")
    else:
        print("No fallo de manera visible para el usuario")

def caso_de_prueba_2_login_exitoso():
    """
    Caso de prueba 2:
        Criterios de aceptación:
            - Que sea exitoso cuando se ingresa usuario "tomsmith" y contraseña "SuperSecretPassword!"
            - Que muestre una alerta de que todo salio bien
    """
    pass

def caso_de_prueba_3_login_exitoso():
    """
    Caso de prueba 3:
        Criterios de aceptación:
            - Que cuando se precione el boton Logout, ocurra logueo exitoso
            - Que muestre una alerta de que todo salio bien
    """
    pass


caso_de_prueba_1_login_falla()

sleep(5)