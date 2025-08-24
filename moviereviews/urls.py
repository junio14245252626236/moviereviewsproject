from django.contrib import admin
from django.urls import path, include
from movie import views as movie_views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movie_views.home, name='home'),
    path('about/', movie_views.about, name='about'),
    path('news/', include('news.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('statistics/', movie_views.statistics_view, name='statistics'),
    path('signup/', movie_views.signup, name='signup'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
