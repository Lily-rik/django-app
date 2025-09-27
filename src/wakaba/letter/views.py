from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages

from .models import Letter


class LetterListView(ListView):
  model = Letter

class LetterCreateView(CreateView):
    model = Letter
    fields = ["title", "content", "image"]
    success_url = reverse_lazy("letter:index")

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "保存できませんでした")
        return super().form_invalid(form)

class LetterDetailView(DetailView):
    model = Letter

class LetterUpdateView(UpdateView):
    model = Letter
    fields = ["title", "content", "image"]

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse("letter:detail", kwargs={"pk": pk})

    def form_valid(self, form):
        messages.success(self.request, "更新しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新できませんでした")
        return super().form_invalid(form)

class LetterDeleteView(DeleteView):
    model = Letter
    success_url = reverse_lazy("letter:index")

    def form_valid(self, form):
        messages.success(self.request, "削除しました")
        return super().form_valid(form)
