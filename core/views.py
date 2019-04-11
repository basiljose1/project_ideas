from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils import timezone

from core.models import Idea


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
        return super().form_valid(form)


class IdeaUpdate(LoginRequiredMixin, UpdateView):
    model = Idea
    fields = ['title', 'detail']
    template_name = 'idea-add.html'

    def get_success_url(self):
        return reverse_lazy('idea_details', kwargs={'pk': self.object.id})


class IdeaDelete(LoginRequiredMixin, DeleteView):
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
        return HttpResponseRedirect(self.success_url)


class IdeaListView(LoginRequiredMixin, ListView):
    model = Idea
    paginate_by = 10
    template_name = "idea-listing.html"


class IdeaDetailView(LoginRequiredMixin, DetailView):
    model = Idea
    template_name = "idea-details.html"
