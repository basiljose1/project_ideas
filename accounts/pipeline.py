from django.core.mail import send_mail


def create_user(strategy, details, backend, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}

    if not details:
        return

    fields = {'name': details.get('fullname'), 'email': details.get('email'), 'username': details.get('username')}

    send_mail(
        'Welcome! you have signed up successfully.',
        'Hi %s, You have been successfully registered and logged in with email: %s' % (
        details.get('fullname'), details.get('email')),
        'from@example.com',
        [details.get('email')],
        fail_silently=False,
    )

    return {
        'is_new': True,
        'user': strategy.create_user(**fields)
    }
