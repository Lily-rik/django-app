from django.views.generic import TemplateView
from django.urls import reverse_lazy

from letter.models import Letter

from django.contrib.auth.mixins import LoginRequiredMixin

class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['letter_list'] = Letter.objects.order_by("-created")

        return context