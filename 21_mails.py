import smtplib

hostname = 'smtp.gmail.com'
email = 'vinayakp.de@gmail.com'
password = 'cmxyqzpwmpzprvkg'

with smtplib.SMTP(host=hostname) as connection:
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs='vinayakmpotadar96@gmail.com',

        msg=f'Subject: Test Python E-Mail \n\n '
            f'The weather is nice here in Bremerhaven\n\n'
            f'you also should come over hear\n\n'
            f'I am enjoying here\n\n'
            f'with regards,\n\n'
            f'Vinayak P\n\n'
            f'Deutschland'

    )