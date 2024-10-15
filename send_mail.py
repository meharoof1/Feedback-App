import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'sandbox.smtp.mailtrap.io'
    login= '74b5e6cf135c1e'
    password = 'a5dd62426a7522'
    message = f"<h3>New FeedBack Submision</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"


    sender_mail = 'email@example.com'
    receiver_mail = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus FeedBack'
    msg['From'] = sender_mail
    msg['To'] = receiver_mail

    #send eamil
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_mail, receiver_mail, msg.as_string())

    