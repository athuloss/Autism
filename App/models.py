from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class AnimalImageGame(models.Model):
    image1 = models.ImageField(upload_to='games')
    image2 = models.ImageField(upload_to='games')
    image3 = models.ImageField(upload_to='games')
    image4 = models.ImageField(upload_to='games')

    image_1_label = models.CharField(default="",max_length=1000)
    image_2_label = models.CharField(default="",max_length=1000)
    image_3_label = models.CharField(default="",max_length=1000)
    image_4_label = models.CharField(default="",max_length=1000)

    time = models.IntegerField(default=0)
    choices = (
        ('image1','image1'),
        ('image2','image2'),
        ('image3','image3'),
        ('image4','image4'),
    )
    is_visible=models.BooleanField(null=True,blank=True,default=False)

    answer = models.CharField(choices=choices,max_length=1000)

    def str(self):
        return "Animal Images"


class ImagePuzzle(models.Model):
    image = models.ImageField(upload_to='ImagePuzzle')
    is_visible=models.BooleanField(null=True,blank=True,default=False)

    def str(self):
        return "Image Puzzle Game"
    


class ObjectIdentification(models.Model):
    image1 = models.ImageField(upload_to='games')
    image2 = models.ImageField(upload_to='games')
    image3 = models.ImageField(upload_to='games')
    image4 = models.ImageField(upload_to='games')

    image_1_label = models.CharField(default="",max_length=1000)
    image_2_label = models.CharField(default="",max_length=1000)
    image_3_label = models.CharField(default="",max_length=1000)
    image_4_label = models.CharField(default="",max_length=1000)

    time = models.IntegerField(default=0)
    choices = (
        ('image1','image1'),
        ('image2','image2'),
        ('image3','image3'),
        ('image4','image4'),
    )
    is_visible=models.BooleanField(null=True,blank=True,default=False)

    answer = models.CharField(choices=choices,max_length=1000)
    class Meta:
        verbose_name = "Object Identification"
    def str(self):
        return "Game Images"



class NumberIdentification(models.Model):
    image1 = models.ImageField(upload_to='games',null=True)
    image2 = models.ImageField(upload_to='games',null=True)
    image3 = models.ImageField(upload_to='games',null=True)
    image4 = models.ImageField(upload_to='games',null=True)
    image5 = models.ImageField(upload_to='games',null=True)
    image6 = models.ImageField(upload_to='games',null=True)

    image_1_label = models.CharField(default="",max_length=1000)
    image_2_label = models.CharField(default="",max_length=1000)
    image_3_label = models.CharField(default="",max_length=1000)
    image_4_label = models.CharField(default="",max_length=1000)
    image_5_label = models.CharField(default="",max_length=1000)
    image_6_label = models.CharField(default="",max_length=1000)

    time = models.IntegerField(default=0)
    choices = (
        ('image1','image1'),
        ('image2','image2'),
        ('image3','image3'),
        ('image4','image4'),
        ('image5','image5'),
        ('image6','image6'),
    )
    is_visible=models.BooleanField(null=True,blank=True,default=False)


    answer = models.CharField(choices=choices,max_length=1000)
    class Meta:
        verbose_name = "Number Identification"
    def str(self):
        return "Number Images"


class GameCount(models.Model):
    user_id = models.CharField(max_length=1000, default="")
    count = models.IntegerField(default=0)
    

    def str(self):
        return "Game Count"
    
    from django.db import models

class Numbergame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    game_result = models.CharField(max_length=10, choices=[('win', 'Win'), ('lose', 'Lose')])
    dots = models.IntegerField(default=0) 
    time_taken = models.IntegerField()  
    count=models.IntegerField(null=True ,blank=True, default="")
    
    created_at = models.DateTimeField(auto_now_add=True)

  
    class Meta:
        verbose_name = "Numbergame Data"
    def _str_(self):
        return "numbergame result"
    
        
class imagepuzzlegame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    game_result = models.CharField(max_length=10, choices=[('win', 'Win'), ('lose', 'Lose')])
    dots = models.IntegerField(default=0)  
    time_taken = models.IntegerField() 
    count=models.IntegerField(null=True, blank=True, default="")
    
    created_at = models.DateTimeField(auto_now_add=True) 

  
    class Meta:
        verbose_name = "imagepuzzlegame Data"
    def _str_(self):
        return "numbergame result"
    
class imagetile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    game_result = models.CharField(max_length=10, choices=[('win', 'Win'), ('lose', 'Lose')])
    dots = models.IntegerField(default=0) 
    time_taken = models.IntegerField() 
    count=models.IntegerField(null=True, blank=True, default="")
    
    created_at = models.DateTimeField(auto_now_add=True)  

 
    
    class Meta:
        verbose_name = "Imagetile Data"
    def _str_(self):
        return "numbergame result"
    
class animalgame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    game_result = models.CharField(max_length=10, choices=[('win', 'Win'), ('lose', 'Lose')])
    dots = models.IntegerField(default=0)  
    time_taken = models.IntegerField() 
    count=models.IntegerField(null=True, blank=True, default="")
    
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when record is created

  
    created_at = models.DateTimeField(auto_now_add=True)  
     
    class Meta:
        verbose_name = "Animalgame Data"
    def _str_(self):
        return "numbergame result"
    
class Blog(models.Model):
    image=models.ImageField(upload_to='images/')
    description=models.CharField(max_length=300)
    title=models.CharField(max_length=300)
    
    def str(self):
        return self.title
 
class Post(models.Model):
    title = models.CharField(max_length=500, null=True)
    artist = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    category=models.CharField(max_length=300,null=True,blank=True)

    def _str_(self):
        return self.title
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, related_name='replies')
    content = models.TextField(null=True, blank=True)  
    created = models.DateTimeField(auto_now_add=True)
    def get_replies(self):
        replies = []
        for reply in self.replies.all(): 
            replies.append(reply)
            replies.extend(reply.get_replies())  
        return replies 

class Doctors(models.Model):
    image=models.ImageField(upload_to='imagess/',null=True)
    fees=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=300,blank=True,null=True)
    hospitalname=models.CharField(max_length=300,blank=True,null=True)


    def _str_(self):
        return self.name


class Chat_bot(models.Model):
    user=models.CharField(max_length=300,blank=True,null=True)
    user_msg = models.CharField(max_length=300,blank=True,null=True)
    bot = models.CharField(max_length=300,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)


class Faq(models.Model):
    questions=models.CharField(max_length=300,null=True,blank=True)
    answer=models.CharField(max_length=300,null=True,blank=True)
    category=models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return self.questions


class Feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    content=models.CharField(max_length=300)
    date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.content

class Videosection(models.Model):
    video=models.FileField(upload_to='videos/',null=True,blank=True)
    title=models.CharField(max_length=300,null=True,blank=True)
    description=models.CharField(max_length=300,null=True,blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title
    