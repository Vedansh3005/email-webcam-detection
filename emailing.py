import smtplib
import mimetypes
from email.message import EmailMessage

PASSWORD = "xwsf pbsz ewfu gifa"
SENDER = "rathodvedansh3005@gmail.com"
RECEIVER = "rathodvedansh3005@gmail.com"

def sendEmail(image_path):
    print("send_email fuction started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer show up!"
    email_message.set_content("Hey, we just saw a new customer.")

    with open(image_path, "rb") as file:
        content = file.read()

    mimetype, _ = mimetypes.guess_type(image_path)
    maintype, subtype = mimetype.split('/', 1)
    email_message.add_attachment(content, maintype=maintype, subtype=subtype)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_email fuction ended")


if __name__ == "__main__":
    sendEmail("images/170403-marvel_earth_trn700-spider_man-miles_morales-poster-trends_international-3840x2160.jpg")