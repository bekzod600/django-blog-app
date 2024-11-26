from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
  name = models.CharField(verbose_name='Category name', max_length=200,)
  slug = models.SlugField(verbose_name='Category slug', max_length=200, unique=True, blank=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      base_slug = slugify(self.name)
      slug = base_slug
      num = 1
      while Category.objects.filter(slug=slug).exists():
          slug = f"{base_slug}-{num}"
          num += 1
      self.slug = slug
    super(Category, self).save(*args, **kwargs)

  def __str__(self):
    return str(self.name)
  
class Tag(models.Model):
  name = models.CharField(verbose_name='Tag name', max_length=200)
  slug = models.SlugField(verbose_name='Tag slug', max_length=200, unique=True)

  def __str__(self):
    return str(self.name)
  
class Post(models.Model):
  title = models.CharField(verbose_name='Post name', max_length=550)
  slug = models.SlugField(verbose_name='Post slug', max_length=200, unique=True)
  body = models.TextField(verbose_name="Post body")
  author = models.CharField(verbose_name='Post author', default="Admin", max_length=100)
  category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='categories')
  tags = models.ManyToManyField(Tag)
  views = models.PositiveIntegerField(default=0)
  published_data = models.DateTimeField(verbose_name='Published time', auto_now_add=True)
  published = models.BooleanField(default=False)
  on_top = models.BooleanField(default=False)

  def __str__(self):
    return str(self.title)

class Comment(models.Model):
  author = models.CharField(verbose_name="Comment author", max_length=100, blank=False)
  comment = models.TextField(verbose_name="Comment text")
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

  def __str__(self):
    return str(self.author)
  
class Rating(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings')
  value = models.PositiveSmallIntegerField(verbose_name='Post rating', default=0)

  def __str__(self):
    return str(self.value)
