# Practica Envio de correos LPC
# Alumno: Víctor Manuel Cárdenas Cavazos
# Matrícula: 1919410

# Importacion de modulos
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Correo Remitente y Destinatario
sender_email = "<Correo Remitente>" # Correo desde donde se envio
receiver_email = "<Correo Destinatario>" # Correo a donde llego

# Mensaje de asunto
message = MIMEMultipart("alternative")
message["Subject"] = "Prueba de envio (script_correo) - 1919410" # Asunto del correo
message["From"] = sender_email
message["To"] = receiver_email

# Estructura HTML del correo a enviar
text = """\
imagen
Practica 12
Ejercicio de la practica 12 para envio de correos
Alumno: Victor Manuel Cardenas Cavazos
Matricula: 1919410"""
html = """\
<html>
  <body>
    <p><img src="C:/Users/carde/Downloads/fcfm_cool.png"><br><br
      <h2><strong>Practica 12</strong></h2><br><br>
       Ejercicio de la practica 12 para envio de correos<br><br>
       <strong>Alumno</strong>: Victor Manuel Cardenas Cavazos<br><br>
       <strong>Matricula</strong>: 1919410<br><br>
    </p>
  </body>
</html>
"""

# Conversion de los Objetos MIME
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
part3 = MIMEText("png")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)
message.attach(part3)

# Crea la conexion segura con los correos
context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.ehlo()
    server.starttls(context=context)
    server.login(sender_email, '<contraseña creada para esta practica>') # Contraseña temporal
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
    server.quit()
