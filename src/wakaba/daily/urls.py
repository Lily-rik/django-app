from django.urls import path

from daily.views import (DailyListView, DailyCreateView,
                            DailyDetailView, DailyUpdateView, DailyDeleteView)

app_name = "daily"

urlpatterns = [

    path("", DailyListView.as_view(), name="index"),
    path("create", DailyCreateView.as_view(), name="create"),

    path("<int:pk>/update", DailyUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", DailyDeleteView.as_view(), name="delete"),
    path("<int:pk>", DailyDetailView.as_view(), name="detail"),

]
