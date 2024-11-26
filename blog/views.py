from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Tag, Post, Comment, Rating
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import CategorySerializer, TagSerializer, PostSerializer, CommentSerializer, RatingSerializer
from .pagination import (
    CategoryPagination,
    TagPagination,
    PostPagination,
    CommentPagination,
    RatingPagination,
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    filter_backends = [SearchFilter]
    search_fields = ['name']

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = TagPagination

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'author', 'category__name', 'tags__name']
    ordering_fields = ['published_data', 'views']
    ordering = ['-published_data']

    lookup_field = 'slug'
    def get_post_by_slug(self, request, slug=None):
        try:
            post = Post.objects.get(slug=slug)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CommentPagination

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    pagination_class = RatingPagination
