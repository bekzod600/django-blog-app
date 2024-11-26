from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'blog'

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'tags', views.TagViewSet, basename='tag')
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'comments', views.CommentViewSet, basename='comment')
router.register(r'ratings', views.RatingViewSet, basename='rating')

urlpatterns = [
  path('',include(router.urls))
    # path('', views.home_page, name='home'),
]