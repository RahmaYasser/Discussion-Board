from boards import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<int:board_id>/', views.board_topics, name='board_topics')
]
