import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager

# Ruta donde se debe descargar el archivo
ruta_descarga = r"C:\Users\crsitian\Downloads"
nombre_archivo = "sampleFile.jpeg"
ruta_archivo_descargado = os.path.join(ruta_descarga, nombre_archivo)

# Configurar opciones de Chrome para descarga automática
options = Options()
prefs = {
    "download.default_directory": ruta_descarga,  # carpeta donde guardar descargas
    "download.prompt_for_download": False,        # no preguntar al descargar
    "directory_upgrade": True,
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs", prefs)
options.add_argument('--start-maximized')

# Ruta común para descargas
download_dir = os.path.join("C:", os.sep, "downloads")  # Cambiar a ~/downloads si usas Mac/Linux

# Función para iniciar el driver
def iniciar_driver(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")
    
    options.add_argument("--start-maximized")
    options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

# Función para registrar usuario
def prueba_registro_usuario(driver):
     # 1. Navegar a la página del formulario
    driver.get("https://demoqa.com/automation-practice-form")
    time.sleep(1)

    # 2. Llenar campos obligatorios
    driver.find_element(By.ID, "firstName").send_keys("Cristian")
    driver.find_element(By.ID, "lastName").send_keys("Castro")
    driver.find_element(By.ID, "userEmail").send_keys("cristian.castro@email.com")
    driver.find_element(By.XPATH, "//label[text()='Male']").click()
    driver.find_element(By.ID, "userNumber").send_keys("3011234567")

    # 3. Bajar al botón y enviar
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.find_element(By.ID, "submit").click()

    # 4. Verificar mensaje de éxito
    time.sleep(1)
    modal = driver.find_element(By.CLASS_NAME, "modal-body").text
    if "Thanks for submitting the form" in modal:
        print("✅ Prueba exitosa: mensaje encontrado.")
    else:
        print("❌ Error: mensaje esperado no encontrado.")
    time.sleep(3)

# Función para cargar archivo
def prueba_carga_archivo(driver):
    driver.get("https://demoqa.com/upload-download")
    time.sleep(2)

    file_path = r"C:\Users\crsitian\Desktop\trabajos univerisdad\pruebas de software\codigos\Proyecto Segundo Corte\resources\texto.txt"
    driver.find_element(By.ID, "uploadFile").send_keys(file_path)
    time.sleep(2)

    uploaded_file_name = driver.find_element(By.ID, "uploadedFilePath").text
    if "texto.txt" in uploaded_file_name:
        print("✅ Carga de archivo: Éxito")
    else:
        print("❌ Carga de archivo: Fallido")
    time.sleep(3)

# Función para alertas
def prueba_alertas(driver):
     # 1. Ir a la página de alertas
    driver.get("https://demoqa.com/alerts")
    time.sleep(2)

    ### ALERTA DE CONFIRMACIÓN ###
    # Hacer clic en el botón que lanza la confirmación
    driver.find_element(By.ID, "confirmButton").click()
    time.sleep(1)

    # Aceptar la alerta
    alert = Alert(driver)
    alert.accept()

    # Validar el mensaje en pantalla
    resultado_confirm = driver.find_element(By.ID, "confirmResult").text
    if "You selected Ok" in resultado_confirm:
        print("✅ Confirmación aceptada correctamente.")
    else:
        print("❌ Falló la validación del mensaje de confirmación.")

    ### ALERTA DE PROMPT ###
    driver.find_element(By.ID, "promtButton").click()
    time.sleep(1)

    # Capturar la alerta y enviar texto
    alert = Alert(driver)
    texto_ingresado = "Cristian"
    alert.send_keys(texto_ingresado)
    alert.accept()

    # Validar que el texto aparezca en la página
    resultado_prompt = driver.find_element(By.ID, "promptResult").text
    if texto_ingresado in resultado_prompt:
        print(f"✅ Texto del prompt capturado correctamente: {texto_ingresado}")
    else:
        print("❌ El texto ingresado no fue mostrado correctamente.")
    time.sleep(3)

def prueba_descarga(driver):
    # 1. Ir a la página
    driver.get("https://demoqa.com/upload-download")
    time.sleep(2)

    # 2. Hacer clic en el botón de descarga
    boton_descarga = driver.find_element(By.ID, "downloadButton")
    boton_descarga.click()

    # 3. Esperar a que el archivo se descargue (ajustar si tu conexión es lenta)
    tiempo_espera = 5
    time.sleep(tiempo_espera)

    # 4. Verificar si el archivo fue descargado
    if os.path.exists(ruta_archivo_descargado):
        print(f"✅ El archivo '{nombre_archivo}' fue descargado correctamente en {ruta_descarga}")
    else:
        print("❌ No se encontró el archivo descargado.")
    time.sleep(3)  # Espera para ver resultados antes de cerrar
    driver.quit()

# Función para prueba de descarga (modo headless)
def prueba_descarga_archivo_headless():
    driver = iniciar_driver(headless=True)
    try:
        driver.get("https://demoqa.com/upload-download")
        time.sleep(2)

        driver.find_element(By.ID, "downloadButton").click()
        time.sleep(5)

        downloaded_file = os.path.join(download_dir, "sampleFile.jpeg")
        if os.path.exists(downloaded_file):
            print(f"✅ Descarga de archivo (headless): Éxito en {downloaded_file}")
        else:
            print("❌ Descarga de archivo (headless): Fallido")
    finally:
        driver.quit()

# Ejecutar todo
def ejecutar_pruebas():
    driver = iniciar_driver(headless=False)

    try:
        print("Iniciando pruebas normales...")
        prueba_registro_usuario(driver)
        prueba_carga_archivo(driver)
        prueba_alertas(driver)
        prueba_descarga(driver)
    finally:
        driver.quit()

    print("\nEjecutando prueba de descarga en modo headless...")
    prueba_descarga_archivo_headless()

# Inicia todo
ejecutar_pruebas()
