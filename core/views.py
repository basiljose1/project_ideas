from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils import timezone

from core.models import Idea
from core.tasks import send_email


class IdeaCreate(LoginRequiredMixin, CreateView):
    model = Idea
    fields = ['title', 'detail']
    template_name = 'idea-add.html'

    def get_success_url(self):
        return reverse_lazy('idea_details', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        send_email('New idea created!', 'Hi, your new idea created', obj.owner.email)
        return super().form_valid(form)


class IdeaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Idea
    fields = ['title', 'detail']
    template_name = 'idea-add.html'

    def get_success_url(self):
        return reverse_lazy('idea_details', kwargs={'pk': self.object.id})

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class IdeaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Idea
    success_url = reverse_lazy('ideas')

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        self.object.deleted_at = timezone.now()
        self.object.save()
        send_email('Your idea deleted successfully!', 'Hi, your deleted successfully', self.object.owner.email)
        return HttpResponseRedirect(self.success_url)

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class IdeaListView(LoginRequiredMixin, ListView):
    model = Idea
    paginate_by = 10
    template_name = "idea-listing.html"


class IdeaDetailView(LoginRequiredMixin, DetailView):
    model = Idea
    template_name = "idea-details.html"
