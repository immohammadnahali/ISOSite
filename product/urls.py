# url product
from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='index'),
    path('article/', views.article, name='article'),
    path('blog/', views.blog, name='blog'),
    path('category/', views.category, name='category'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('course/', views.course, name='course'),
    path('error404/', views.error_404, name='error404'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('login/', views.login, name='login'),
    path('panel_user/', views.panel_user, name='panel_user'),
    path('search/', views.search, name='search'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('teach/', views.teach, name='teach'),

]
