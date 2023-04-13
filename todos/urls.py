from django.urls import path, include
from . import views
from rest_framework import routers

from .views import TodoViewSet, todo_list

app_name='todos'
router = routers.DefaultRouter()
router.register(r'api', TodoViewSet)

urlpatterns = [
    path('view/',todo_list),
    path('v1/', include(router.urls)),
    path('', views.IndexView.as_view(), name='index'),
    path('unique/<str:param>', views.unique, name='unique'),
    path('<uuid:id>/delete', views.delete, name='delete'),
    path('<uuid:id>/update', views.update, name='update'),
    path('add/', views.add, name='add')
]
