from django.core.mail import send_mail

def send_email(subject, message, to):
    send_mail(
        subject, message,'basil@live.com',[to],fail_silently=False,
    )
    return True