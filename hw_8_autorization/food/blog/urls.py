from django.urls import path
from .views import NewsListView, RegisterNews, NewsDetailView, MyLogoutView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('news-list/', NewsListView.as_view(), name='news-list'),
    path('new_news/', RegisterNews.as_view(), name='register-news'),
    path('news-list/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('login/', LoginView.as_view(
        template_name='blog/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),

]
