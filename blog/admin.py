from django.contrib import admin
from .models import Category, Tag, Post, Comment, Rating

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug') 
    fields = ('name',) 
    search_fields = ('name',)        
    prepopulated_fields = {'slug': ('name',)} 

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  # Yangi komment qo'shish uchun bo'sh satrlar soni

class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published', 'on_top', 'views', 'published_data')  
    list_filter = ('published', 'on_top', 'category', 'tags')  
    search_fields = ('title', 'body', 'author')  
    ordering = ('-published_data',)  
    prepopulated_fields = {'slug': ('title',)}  
    inlines = [CommentInline, RatingInline]  # Komment va Reytinglar Post sahifasida ko'rinadi
    filter_horizontal = ('tags',)  # Teglarni tanlash uchun qulay ko'rinish
    list_editable = ('published', 'on_top')  # Admin interfeysda ushbu ustunlarni o'zgartirish mumkin

# Comment modeli uchun admin sozlamalari
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'comment')  # Ko'rsatiladigan ustunlar
    search_fields = ('author', 'comment')         # Qidirish uchun maydon
    list_filter = ('post',)                       # Post bo'yicha filter

# Rating modeli uchun admin sozlamalari
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('post', 'value')  # Ko'rsatiladigan ustunlar
    list_filter = ('post',)           # Post bo'yicha filter
