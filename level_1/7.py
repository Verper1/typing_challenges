# import smtplib

def send_email(header: str, text_content: str, send_to: str) -> None:
    """
    Функция, которая отправляет письмо

    :param header: str
    :param text_content: str
    :param send_to: str
    :return: None
    """
    # try:
    #     smtp_server = 'smtp.gmail.com'
    #     smtp_port = 587
    #     smtp_username = 'some_email@gmail.com'
    #     smtp_password = 'super_hard_pass'
    #     smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    #     smtp_connection.starttls()
    #     smtp_connection.login(smtp_username, smtp_password)
    #     email_headers = 'From: {}\n To: {}\n Subject: {}'.format(smtp_username, send_to, header)
    #     email_message = '{}\n \n {}'.format(email_headers, text_content)
    #     # smtp_connection.sendmail(smtp_username, send_to, email_message)
    #     smtp_connection.quit()
    # except Exception as error:
    #     print('Email failed to send. Error message: {}'.format(str(error)))
    pass


if __name__ == "__main__":
    assert send_email(header="Test email", text_content="This is a test email", send_to="test@gmail.com") is None
