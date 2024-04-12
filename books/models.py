from django.db import models

# Create your models here.

class Book(models.Model):
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_desc  = models.CharField(max_length=300)
    book_image = models.ImageField(upload_to='media')
    book_price = models.DecimalField(max_digits=8,decimal_places=2)
    slug = models.SlugField(max_length=150,unique=True)
    
    def __str__(self) -> str:
        return self.book_title
    
    class Meta:
        verbose_name_plural = 'Books'
        

class Articles(models.Model):
    article_name = models.CharField(max_length=200)
    article_author =models.CharField(max_length=100)
    article_content = models.TextField()
    article_image = models.ImageField(upload_to='articles_images')
    slug = models.SlugField(max_length=50,unique=True,null=True)
    
    def __str__(self) -> str:
        return self.article_name
    
    class Meta:
        verbose_name_plural = 'Articles'