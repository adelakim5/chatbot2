# from rest_framework.routers import DefaultRouter 
from django.urls import path, include 
from . import views

# router = DefaultRouter()

# router.register('post', views.PostViewSet),

urlpatterns = [
    # path('', include(router.urls)),
    path('hello',views.hello, name="hello"),
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
    path('reserve', views.reserve, name="reserve"),
    path('diary', views.diary, name="diary"),
    path('accounts/', include('allauth.urls')),
    path('oauth/', views.oauth, name="oauth"),
    path('verification', views.verification, name="verification"),
] 