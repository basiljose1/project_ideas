from django.views.generic import FormView
from django.core.mail import send_mail
from django.urls import reverse_lazy

from django.contrib.auth import login
from accounts.forms import UserForm


class RegisterView(FormView):
    template_name = "register.html"
    form_class = UserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        send_mail(
            'Welcome! you have signed up successfully.',
            'Hi %s, You have been successfully registered and logged in with email: %s' % (
                form.data.get('name'), form.data.get('email')),
            'from@example.com',
            [form.data.get('email')],
            fail_silently=False,
        )
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return super().form_valid(form)
