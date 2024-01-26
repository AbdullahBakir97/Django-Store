from celery import shared_task
import time
from django.core.mail import send_mail


@shared_task
def send_emails(data):
    # for x in range(10):
    #     time.sleep(2)
    #     print(f'sending email to {x}')
    for user in data:
        send_mail(
            "Activate Your Account",
            f"Welcome {user.username} \nUse this code  to activate your account\nMystroTeam",
            "abdullah.bakir.204@gmail.com",  # send from 
            [user.email],  # send to
            fail_silently=False,
        )