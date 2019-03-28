from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views
urlpatterns = [
    # url(r'^actor/$', views.ActorListView.as_view()),
    # url(r'^actor/(?P<pk>\d+)/$', views.ActorDetailView.as_view())
]
# 可以处理视图的路由集
router = DefaultRouter()
# 向路由中注册视图集
router.register('actors', views.ActorListView, basename='actors')
router.register('movies', views.MovieListView, basename='movies')

# 将路由器中的所以路由信息追到到django的路由列表中
urlpatterns += router.urls