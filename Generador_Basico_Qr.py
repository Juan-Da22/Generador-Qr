import qrcode #-------> Se implento una libreria propia de python.

#Este apartado se encarga de tomar la Url y codificarla.

url = " " #-------> En esta variable se ingresa la informacion a codificar (Textos, URLS, Imagnes, etc.)
Nombre_archivo = " " #-------> En esta variable se le debe asignar el nombre y el formato en el que se desea guardar. (Ej. Prueba.png , Prueba.JPG, etc.)
qr = qrcode.QRCode( version=1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 10, border = 4)

#Este apratado  se encarga de crear una mascara y cargar los datos al Qr    
qr.add_data(url)
qr.make(fit=True)
print("Datos añadidos y Qr generado")

#Este apartado  se encarga de Guardar y asignar parametros al Qr

img = qr.make_image(fill_color = "black", back_color = "white")
img.save(Nombre_archivo)
print(f"Qr guardado como {Nombre_archivo}")
