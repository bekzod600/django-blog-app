from rest_framework.pagination import PageNumberPagination

class CategoryPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  
    max_page_size = 100 

class TagPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  
    max_page_size = 100 

class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  
    max_page_size = 100 

class CommentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  
    max_page_size = 100 

class RatingPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  
    max_page_size = 100 
