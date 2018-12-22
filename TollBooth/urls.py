from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from Registration import views as user_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', user_views.register, name='register'),
    url(r'^profile/', user_views.profile, name='profile'),
    url(r'^home/', user_views.home, name='home'),
    url(r'^login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^$',user_views.index, name='index'),
]
