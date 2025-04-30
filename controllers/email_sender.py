import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    def __init__(self, smtp_server, port, sender_email, app_password):
        self.smtp_server = smtp_server
        self.port = port
        self.sender_email = sender_email
        self.app_password = app_password

    def send_email(self, view, recipient_email, subject, body):
       
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
        
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()
                server.login(self.sender_email, self.app_password)
                server.send_message(msg)
            view.show_message("\n✅ Email sent successfully.\n", "bold green")
            return True
        except Exception as e:
            view.show_message(f"\n❌ Failed to send email: {e}\n", "bold red")
            return False