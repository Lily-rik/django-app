from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Daily

class UserroomMixin(LoginRequiredMixin):
    login_url = reverse_lazy("login")

class DailyListView(UserroomMixin, ListView):
    model = Daily

    def get_queryset(self):
        return self.model.objects.filter(
            user=self.request.user,
        )

class DailyCreateView(UserroomMixin, CreateView):
    model = Daily
    fields = ["bt", "meal", "sleep", "stool", "medicine", "mood", "contact"]
    success_url = reverse_lazy("daily:index")

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "保存できませんでした")
        return super().form_invalid(form)

class DailyDetailView(UserroomMixin, DetailView):
    model = Daily

class DailyUpdateView(UserroomMixin, UpdateView):
    model = Daily
    fields = ["bt", "meal", "sleep", "stool", "medicine", "mood", "contact"]

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse("daily:detail", kwargs={"pk": pk})

    def form_valid(self, form):
        messages.success(self.request, "更新しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新できませんでした")
        return super().form_invalid(form)

class DailyDeleteView(UserroomMixin, DeleteView):
    model = Daily
    success_url = reverse_lazy("daily:index")

    def form_valid(self, form):
        messages.success(self.request, "削除しました")
        return super().form_valid(form)

