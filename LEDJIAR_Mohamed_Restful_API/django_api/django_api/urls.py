from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from my_app import views 
router = routers.DefaultRouter()
router.register(r'artist', views.ArtistViewSet)
router.register(r'song', views.SongViewSet)
router.register(r'album', views.AlbumViewSet)# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]