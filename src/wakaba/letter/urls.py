from django.urls import path

from letter.views import (LetterListView, LetterCreateView,
                            LetterDetailView, LetterUpdateView, LetterDeleteView)

app_name = "letter"

urlpatterns = [

    path("", LetterListView.as_view(), name="index"),
    path("create", LetterCreateView.as_view(), name="create"),

    path("<int:pk>/update", LetterUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", LetterDeleteView.as_view(), name="delete"),
    path("<int:pk>", LetterDetailView.as_view(), name="detail"),

]
