from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

# Create a router that automatically register all the urls
# produced by the provided view
router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

app_name = 'recipe'

urlpatterns = [
    # All the path that match 'recipe' will include all the urls
    # generated by the router
    path('', include(router.urls))
]
