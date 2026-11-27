class EmailNotification:
    def send(self, message):
        print(f"Email sent: {message}")

class SMSNotification:
    def send(self, message):
        print(f"SMS sent: {message}")

class WhatsAppNotification:
    def send(self, message):
        print(f"WhatsApp sent: {message}")

notifications = [EmailNotification(), SMSNotification(), WhatsAppNotification()]

for notification in notifications:
    notification.send("Your class begins at 10 a.m.")