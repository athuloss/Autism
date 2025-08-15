from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from.models import*
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect  
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.db.models import Sum
# Create your views here.

from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
# from . import gazedetection




def loginviews(request):
   if request.POST:
      # messages=0
      username=request.POST['username']
      password=request.POST['password']
      user=authenticate(username=username,password=password)
      if user:
         login(request,user)
         print("login success.....")
         messages=0
         # return redirect('home')
      else:
         messages=1
      return JsonResponse({"messages":messages})
      

def gamecontrol(request):  
    animal_game = AnimalImageGame.objects.first()
    Imagepuzzle = ImagePuzzle.objects.first()
    objectIdentification = ObjectIdentification.objects.first()
    numberIdentification = NumberIdentification.objects.first()
    return render(request,'gamecontrol.html',{'animal':animal_game,'imagepuzzle':Imagepuzzle,'objectIdent':objectIdentification,'number':numberIdentification})

def delete_view(request,pk):
   delete_post=Post.objects.get(id=pk)
   delete_post.delete()
   return redirect('forum')


def logoutviews(request):
   logout(request)
   return redirect('home')
   

def home(request):
   
   blog=Blog.objects.all()
   doctor=Doctors.objects.all()
   # doctor=Doctors.objects.all().order_by('-id')[:4]  

   videos=Videosection.objects.all().order_by('-id')[:4]
   
#    detection_running = gazedetection.thread is not None and gazedetection.thread.is_alive()
   user_msgs = Chat_bot.objects.filter(user = request.user.username)

   animal_game = AnimalImageGame.objects.first()
   Imagepuzzle = ImagePuzzle.objects.first()
   objectIdentification = ObjectIdentification.objects.first()
   numberIdentification = NumberIdentification.objects.first()
   return render(request,'home.html',{'doct':blog,'doctor':doctor,'messages':user_msgs,"detection_running": None,'animal_game': animal_game,'ImagePuzzle':Imagepuzzle,'ObjectIdentification':objectIdentification,'NumberIdentification':numberIdentification,'videos':videos})








def verifing(request,pk):
    Imagepuzzle = AnimalImageGame.objects.get(id=pk)
    if not Imagepuzzle.is_visible:
                Imagepuzzle.is_visible=True
                Imagepuzzle.save()
    return redirect('gamecontrol')

def disverifing(request,pk):
    Imagepuzzle = AnimalImageGame.objects.get(id=pk)
    if  Imagepuzzle.is_visible:
         Imagepuzzle.is_visible=False
         Imagepuzzle.save()
    return redirect('gamecontrol')


def verifingimage(request,pk):
    Imagepuzzle = ImagePuzzle.objects.get(id=pk)
    if not Imagepuzzle.is_visible:
                Imagepuzzle.is_visible=True
                Imagepuzzle.save()
    return redirect('gamecontrol')

def disverifingimage(request,pk):
    Imagepuzzle = ImagePuzzle.objects.get(id=pk)
    if  Imagepuzzle.is_visible:
         Imagepuzzle.is_visible=False
         Imagepuzzle.save()
    return redirect('gamecontrol')

def verifingnumber(request,pk):
    Imagepuzzle = NumberIdentification.objects.get(id=pk)
    if not Imagepuzzle.is_visible:
                Imagepuzzle.is_visible=True
                Imagepuzzle.save()
    return redirect('gamecontrol')

def disverifingnumber(request,pk):
    Imagepuzzle = NumberIdentification.objects.get(id=pk)
    if  Imagepuzzle.is_visible:
         Imagepuzzle.is_visible=False
         Imagepuzzle.save()
    return redirect('gamecontrol')

def verifingident(request,pk):
    Imagepuzzle = ObjectIdentification.objects.get(id=pk)
    if not Imagepuzzle.is_visible:
                Imagepuzzle.is_visible=True
                Imagepuzzle.save()
    return redirect('gamecontrol')

def disverifingident(request,pk):
    Imagepuzzle = ObjectIdentification.objects.get(id=pk)
    if  Imagepuzzle.is_visible:
         Imagepuzzle.is_visible=False
         Imagepuzzle.save()
    return redirect('gamecontrol')








def parentDashboard(request):
   return render(request,'parentDashboard.html')


def checksignin(request):
      message=0
      username=request.POST['fullname']
      user=User.objects.filter(username=username)
      if user:
         message=0
      else:
         message=1
      return JsonResponse({'message':message})
        



def signup(request):
    if request.method == "POST":
      email = request.POST.get('email')
   
      password = request.POST.get('password')
      fullname = request.POST.get('fullname')


      user = User.objects.create_user(username=fullname, email=email, password=password)
      user.first_name = fullname
      user.save()

      print('USER SIGNUP')
   #  return JsonResponse({"status": "success",})
    return redirect('home')
        





import random
def puzzle(request):
   choices = ['image1','image2','image3','image4']
   game = ObjectIdentification.objects.all().first()
   game.answer = random.choice(choices)
   print(game)
   return render(request,'puzzlegame.html',{"game":game})

def parentDashboard(request):
   
   user=request.user
   userdata=User.objects.get(username=user)
   return render(request,'parentDashboard.html',{'profile':userdata})




def number(request):
   return render(request,'number.html')

# def feedbackpage(request):
#    return render(request,'feedback.html')

def feedtest(request):
   feedback=Feedback.objects.all().order_by('-id')
   return render(request,'feedbackpage.html',{'feedback_data':feedback})

def data_feedback(request):
    user=request.user
    if request.POST:
        content=request.POST['content']
        feed_back=Feedback.objects.create(user=user,content=content)
        feed_back.save()
    return redirect('feedtest')
        


# def shuffel(request):
   
#    return render(request,'shuffel.html')


def forum(request):
    posts = Post.objects.all().order_by('-id')
    category=request.POST.get('data','')
    if category:
        filtered_data=Post.objects.filter(category=category)
    else:
        filtered_data=posts

    return render(request, 'forumnew.html', {'posts': posts,'filtered':filtered_data})

def replay_loop(request):
    return render(request, 'reply_loop.html')

from django.shortcuts import get_object_or_404, redirect

def add_comment(request, pk):

    
    if request.method == "POST":
        post = get_object_or_404(Post, id=pk) 
        content = request.POST.get("content") 
        parent_id = request.POST.get("parent_id")

        if content:  
            if parent_id:
                parent = Comment.objects.get(id=parent_id)
                Comment.objects.create(post=post, user=request.user, content=content, parent=parent)
            else:
                Comment.objects.create(post=post, user=request.user, content=content)

        return redirect("forum") 


def uploadpost(request):
    user=request.user
    if request.POST:
        title=request.POST['title']
        category=request.POST['category']
        media = request.FILES.get('images')
        upload=Post.objects.create(author=user,title=title,category=category)
        if media:
           
            if media.content_type.startswith('image'):
                upload.image = media
            elif media.content_type.startswith('video'):
                upload.video = media
            upload.save()
       
    return redirect('forum')





import requests

def chat_bot(request):

    if request.POST:
        
        Text_message=request.POST['sendmsg']

        data = {
            'message': Text_message,
            
        }
       
        response = requests.post('https://app369.pythonanywhere.com/chatbotMsg/', data=data)
        result = json.loads(response.text)
        print(type(response.text))
        chat_bot = Chat_bot.objects.create(user = request.user.username,bot = result['result'],user_msg = Text_message)
        # chat_bot = Chat_bot.objects.create(user = request.user.username,bot = "Hello there",user_msg = Text_message)
        print(Text_message)
        return JsonResponse({"user_msg":chat_bot.user_msg,"bot_msg":chat_bot.bot,
                            
                             })



def update_post(request):
    message = 0
    if request.method == "POST":
        post_id = request.POST.get("post_id")  
        title = request.POST.get("title")
        new_imagepost = request.FILES.get("new_imagepost")


        post = Post.objects.get(id=post_id)  
        post.title = title

        if new_imagepost:
            if new_imagepost.content_type.startswith('image'):
                post.image = new_imagepost
                post.video = None 
            elif new_imagepost.content_type.startswith('video'):
                post.video = new_imagepost
                post.image = None  

        post.save()
        message = 1  

    return JsonResponse({'message': message})






def update_comment(request):
    message = 0
    if request.POST:
        newcomment = request.POST['newcomment']
        comment_id = request.POST.get('comment_id')

        try:
            new = Comment.objects.get(id=comment_id) 
            new.content = newcomment
            new.save()
            message = 0 
        except Comment.DoesNotExist:
            message = 1  

    return JsonResponse({'message': message})




def update_comment_replay(request):
    message = 1 
    if request.method == "POST":
        newcomment = request.POST.get("newcomment", "")
        comment_id = request.POST.get("comment_id")
        if newcomment and comment_id:
            comment = get_object_or_404(Comment, id=comment_id)
            comment.content = newcomment
            comment.save()
            message = 0  
    return JsonResponse({'message': message})







# def update_post(request):
#     message=0
#     if request.method == "POST":
#         title = request.POST.get("title")
#         description = request.POST.get("description")

#         if title and description:
#             post = upload.objects.first()  
#             post.caption = title
#             post.des = description
#             post.save()
#             message=0
#     return JsonResponse({'message':message})


# from django.shortcuts import render, redirect, get_object_or_404
# def replay(request, pk):
#     user=request.user
#     profile=User.objects.get(username=user)
#     if request.method == "POST":
#         comment = get_object_or_404(Comments, id=pk)  
#         replay_text = request.POST.get('replay')

#         if replay_text:  # Check if replay text is not empty
#             Replay.objects.create(
#                 comment=comment,
#                 user=profile,
#                 replay=replay_text  
#             )
    
#     return redirect('forum') 






@require_POST
def start_gaze(request):
    gazedetection.start_gaze_detection()
    return redirect("home")

@require_POST
def stop_gaze(request):
    gazedetection.stop_gaze_detection()
    return redirect("home")

import random 
def ImageGame(request):
   choices = ['image1','image2','image3','image4']
   image_game = AnimalImageGame.objects.all().first()
   image_game.answer = random.choice(choices)
   image_game.save()
   return render(request,'ImageGame.html',{'game':image_game})


def ImageTileGame(request):
   image_game = ImagePuzzle.objects.all().first()
   return render(request,'ImagePuzzle.html',{'game':image_game})

   
choices = ['image1','image2','image3','image4','image5','image6']
import random 
def number(request):
   number_game = NumberIdentification.objects.all().first()
   number_game.answer = random.choice(choices)
   number_game.save()
   print("number_game")
   return render(request,'number.html',{"game":number_game})


@csrf_protect
def update_game_count(request):
    if request.method == "POST":
        data = json.loads(request.body)
        new_count = data.get("count", 0)  # Get count from request

        # Get or create a single row for tracking count
        game_count, created = GameCount.objects.get_or_create(id=1)
        game_count.count = new_count
        game_count.save()

        return JsonResponse({"message": "Game count updated", "new_count": game_count.count})

    elif request.method == "GET":  # Fetch the latest count
        game_count, created = GameCount.objects.get_or_create(id=1)
        return JsonResponse({"count": game_count.count})

    return JsonResponse({"error": "Invalid request"}, status=400)



@require_POST
def game_result(request):
    # Get data from POST request
    game_result_status = request.POST.get("game_result")
    dots = request.POST.get("dots")
    time_taken = request.POST.get("time_taken")
   #  count=count+1

    # Validate required fields
    if not all([game_result_status, dots, time_taken]):
        return JsonResponse({"error": "Missing data!"}, status=400)
    print(Numbergame.objects.filter(user = request.user).count())
    count=Numbergame.objects.filter(user = request.user).count()
    try:
        # Create and save GameResult instance
        print(game_result_status)
        Numbergame.objects.create(
            user=request.user if request.user.is_authenticated else None,
            game_result=game_result_status,
            dots=int(dots),
            time_taken=int(time_taken),
            count = count
        )
        return JsonResponse({"message": "Data saved successfully!"})
    except Exception as e:
        print(f"❌ Error: {e}")
        return JsonResponse({"error": "Server error"}, status=500)
    
def gett(request):
   user=request.user
   value=Numbergame.objects.filter(user=user)
   return JsonResponse({"value":value})




def blog_view(request):
   if request.POST:
      image=request.FILES['image']
      description=request.POST['description']
      title=request.POST['title']
      blog=Blog.objects.create(image=image,description=description,title=title)
      blog.save()

   
   return redirect('blogview')


@require_POST
def imagepuzzlegame_gameresult(request):
    # Get data from POST request
    game_result_status = request.POST.get("game_result")
    time_taken = request.POST.get("time_taken")
   #  count=count+1

    # Validate required fields
    if not all([game_result_status, time_taken]):
        return JsonResponse({"error": "Missing data!"}, status=400)
    count=imagepuzzlegame.objects.filter(user = request.user).count()
    try:
        # Create and save GameResult instance
        print(game_result_status)
        imagepuzzlegame.objects.create(
            user=request.user if request.user.is_authenticated else None,
            game_result=game_result_status,
            time_taken=int(time_taken),
            count = count
        )
        return JsonResponse({"message": "Data saved successfully!"})
    except Exception as e:
        return JsonResponse({"error": "Server error"}, status=500)
    

@require_POST
def imagetile_gameresult(request):
    # Get data from POST request
    game_result_status = request.POST.get("game_result")
    time_taken = request.POST.get("time_taken")
   #  count=count+1

    # Validate required fields
    if not all([game_result_status, time_taken]):
        return JsonResponse({"error": "Missing data!"}, status=400)
    count=imagetile.objects.filter(user = request.user).count()
    try:
        # Create and save GameResult instance
        print(game_result_status)
        imagetile.objects.create(
            user=request.user if request.user.is_authenticated else None,
            game_result=game_result_status,
            time_taken=int(time_taken),
            count = count
        )
        return JsonResponse({"message": "Data saved successfully!"})
    except Exception as e:
        return JsonResponse({"error": "Server error"}, status=500)
    
    
@require_POST
def animalgame_gameresult(request):
    # Get data from POST request
    game_result_status = request.POST.get("game_result")
    time_taken = request.POST.get("time_taken")
   #  count=count+1

    # Validate required fields
    if not all([game_result_status, time_taken]):
        return JsonResponse({"error": "Missing data!"}, status=400)
    count=animalgame.objects.filter(user = request.user).count()
    try:
        # Create and save GameResult instance
        print(game_result_status)
        animalgame.objects.create(
            user=request.user if request.user.is_authenticated else None,
            game_result=game_result_status,
            time_taken=int(time_taken),
            count = count
        )
        return JsonResponse({"message": "Data saved successfully!"})
    except Exception as e:
        return JsonResponse({"error": "Server error"}, status=500)
    
print(ImagePuzzle.objects.all().first().pk)
print(ObjectIdentification.objects.all().first().pk)
print(NumberIdentification.objects.all().first().pk)
print(imagepuzzlegame.objects.all().first().pk)


def get_game_stats(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=403)

    user = request.user  

    data = {
        "Numbergame_count": Numbergame.objects.filter(user=user).count(),
        "imagepuzzlegame_count": imagepuzzlegame.objects.filter(user=user).count(),
        "imagetile_count": imagetile.objects.filter(user=user).count(),
        "animalgame_count": animalgame.objects.filter(user=user).count(),

        "Numbergame_wins": Numbergame.objects.filter(user=user, game_result="win").count(),
        "Numbergame_losses": Numbergame.objects.filter(user=user, game_result="lose").count(),

        "imagepuzzlegame_wins": imagepuzzlegame.objects.filter(user=user, game_result="win").count(),
        "imagepuzzlegame_losses": imagepuzzlegame.objects.filter(user=user, game_result="lose").count(),

        "imagetile_wins": imagetile.objects.filter(user=user, game_result="win").count(),
        "imagetile_losses": imagetile.objects.filter(user=user, game_result="lose").count(),

        "animalgame_wins": animalgame.objects.filter(user=user, game_result="win").count(),
        "animalgame_losses": animalgame.objects.filter(user=user, game_result="lose").count(),

        # Here is the updated code to get all individual times
        "Numbergame_time": list(Numbergame.objects.filter(user=user).values_list("time_taken", flat=True)),
        "imagepuzzlegame_time": list(imagepuzzlegame.objects.filter(user=user).values_list("time_taken", flat=True)),
        "imagetile_time": list(imagetile.objects.filter(user=user).values_list("time_taken", flat=True)),
        "animalgame_time": list(animalgame.objects.filter(user=user).values_list("time_taken", flat=True)),
    }
    return JsonResponse(data)




# def get_user_game_stats(request, user_id):
#     try:
#         user = User.objects.get(id=user_id)
#     except User.DoesNotExist:
#         return JsonResponse({"error": "User not found"}, status=404)

#     # Collecting wins & losses in the correct format
#     results = [
#         [Numbergame.objects.filter(user=user, game_result="win").count(),
#          Numbergame.objects.filter(user=user, game_result="lose").count()],
#         [imagepuzzlegame.objects.filter(user=user, game_result="win").count(),
#          imagepuzzlegame.objects.filter(user=user, game_result="lose").count()],
#         [imagetile.objects.filter(user=user, game_result="win").count(),
#          imagetile.objects.filter(user=user, game_result="lose").count()],
#         [animalgame.objects.filter(user=user, game_result="win").count(),
#          animalgame.objects.filter(user=user, game_result="lose").count()],
#     ]

#     # Collecting total time taken per game
#     time_taken = [
#         Numbergame.objects.filter(user=user).aggregate(Sum("time_taken"))["time_taken__sum"] or 0,
#         imagepuzzlegame.objects.filter(user=user).aggregate(Sum("time_taken"))["time_taken__sum"] or 0,
#         imagetile.objects.filter(user=user).aggregate(Sum("time_taken"))["time_taken__sum"] or 0,
#         animalgame.objects.filter(user=user).aggregate(Sum("time_taken"))["time_taken__sum"] or 0,
#     ]

#     return JsonResponse({"results": results, "time_taken": time_taken})

def get_user_game_stats(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
    
    data = {
        "results": [
            [Numbergame.objects.filter(user=user, game_result="win").count(), 
             Numbergame.objects.filter(user=user, game_result="lose").count()],
            
            [imagepuzzlegame.objects.filter(user=user, game_result="win").count(), 
             imagepuzzlegame.objects.filter(user=user, game_result="lose").count()],
            
            [imagetile.objects.filter(user=user, game_result="win").count(), 
             imagetile.objects.filter(user=user, game_result="lose").count()],
            
            [animalgame.objects.filter(user=user, game_result="win").count(), 
             animalgame.objects.filter(user=user, game_result="lose").count()]
        ],
        "time_taken": {
            "Numbergame": list(Numbergame.objects.filter(user=user).values_list("time_taken", flat=True)),
            "imagepuzzlegame": list(imagepuzzlegame.objects.filter(user=user).values_list("time_taken", flat=True)),
            "imagetile": list(imagetile.objects.filter(user=user).values_list("time_taken", flat=True)),
            "animalgame": list(animalgame.objects.filter(user=user).values_list("time_taken", flat=True)),
        }

    }
    
    return JsonResponse(data)




def adminDashboard(request):
   user=User.objects.filter(is_superuser=False)
   print("----")
   print(user)
   return render(request, 'adminDashboard.html', {'profile': user})


def doctorview(request):
    if request.POST:
        image=request.FILES['image']
        name=request.POST['name']
        hospitalname=request.POST['hospitalname']     
        fees=request.POST['fees']
        doctor=Doctors.objects.create(name=name,hospitalname=hospitalname,fees=fees,image=image)
        doctor.save()
    
    return redirect('adminDashboard')




def deletecmt(request,pk):
    cmt=Comment.objects.get(id=pk)
    cmt.delete()
    return redirect('forum')


from collections import defaultdict

def faq(request):
    faqs = Faq.objects.all()
    
  
    grouped_faqs = defaultdict(list)
    for faq in faqs:
        grouped_faqs[faq.category].append(faq)

    return render(request, 'faq.html', {'grouped_faqs': dict(grouped_faqs)})



from django.contrib.auth import update_session_auth_hash
def updatedata(request):
    user=request.user
    if request.POST:
        get_username=request.POST.get('username')
        get_email=request.POST.get('email')
        get_pass=request.POST.get('password')
        print(get_username)
    data_user=User.objects.get(username=user.username)
    data_user.username=get_username
    data_user.email=get_email
    data_user.set_password(get_pass)
    data_user.save()
    update_session_auth_hash(request, data_user)
    return JsonResponse({'messages':"Profile has sucessfully updated"})



def videosection(request):

    if request.POST:
        Videosection.objects.create(

        video=request.FILES['video_file'],
        title=request.POST['title'],
        description=request.POST['desc'],
        )

        return HttpResponseRedirect(reverse('adminDashboard'))

