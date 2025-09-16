from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('rooms/', views.RoomListCreateView.as_view(), name='room-list-create'),
    path('rooms/<int:id>/', views.RoomDetailView.as_view(), name='room-detail'),
    path('messages/', views.MessageCreateView.as_view(), name='message-create'),
    path("token/", TokenObtainPairView.as_view()),
    # path("register/", views.RegistrationView.as_view()),
]
