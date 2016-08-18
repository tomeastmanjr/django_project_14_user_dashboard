from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^signin$', views.signin, name = "signin"),
    url(r'^register$', views.register, name = "register"),
    url(r'^dashboard$', views.dashboard, name = "dashboard"),
    url(r'^dashboard/admin$', views.admin, name = "admin"),
    url(r'^users/show$', views.show, name = "show"),
    url(r'^users/new$', views.new, name = "new"),
    url(r'^users/edit$', views.edit, name = "edit"),
    url(r'^create$', views.create, name = "create"),
    url(r'^update$', views.update, name = "update"),
    url(r'^delete$', views.delete, name = "delete"),
    url(r'^destroy$', views.destroy, name = "destroy")
    ]
