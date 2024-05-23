from django.urls import path

from message.apps import MessageConfig

app_name = MessageConfig.name

urlpatterns = [
    # path('', BoatListView.as_view(), name='boat_list'),
    # path('<int:pk>/', BoatDetailView.as_view(), name='boat_detail'),
    ]
