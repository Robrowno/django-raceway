import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_transaction_mail(email, receipt):
    """
    Confirmation email with a link to the user's receipt.
    """
    subject = 'Raceway transaction'
    print(receipt)
    content = f"""
            <h2>Hi there</h2>,
            <h3> We can confirm your order has been successfully completed!
            You can check your receipts through this url.
            <a href="{receipt}">Profile</a>
            </h3>
            <br>
        """
    message = Mail(
        from_email='robrowno@icloud.com',
        to_emails=email,
        subject=subject,
        html_content=content)
    secret_key = os.environ.get("SEND_GRID_API")
    try:
        sg = SendGridAPIClient(secret_key)
        response = sg.send(message)
    except Exception as e:
        print(e)
