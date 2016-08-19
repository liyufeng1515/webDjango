from django.conf.urls import url
import views

urlpatterns = [
    url(r'^hello/', views.hello,name='hello'),
]
