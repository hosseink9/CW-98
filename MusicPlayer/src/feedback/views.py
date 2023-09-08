from typing import Any
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView,ListView,DetailView,CreateView,View
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, JsonResponse
from datetime import datetime



# from django.contrib.auth import REDIRECT_FIELD_NAME
# from typing import Any


# class AuthenticateRequierd:

#     def __init__(self, function,url_name='feedback:set'):
#         self.function = function
#         self.url_name=url_name


#     def __call__(self,request) -> Any:
#         # request = args[0]
#         # print(request)
#         # if args[0].user.is_authenticated:
#         if self.is_authenticated(request):
#             return self.function(request)
#         return redirect(self.url_name)

#     def is_authenticated(self,request):
#         token = request['headers'].get('token')
#         return token=='1234'

# @AuthenticateRequierd
# class API:
#     def __init__(self,request) -> None:
#         self.request = request

#     def call(self):
#         return 'OK'

# @AuthenticateRequierd
# def show_hello(request):
#     return HttpResponse('Hello World')

# request = {'headers':{'token':"1234"}}
# api = show_hello(request)
# result = API.call()
# print(result)

# def set_token(request):
#     request.META['TOKEN'] = '1234'
#     return HttpResponse()


class LikeView(View):
    # login_url = reverse_lazy('users:login')

    def post(self,request):
        if request.user.is_authenticated:
            song_id = request.POST.get('song')
            song = Song.objects.get(id=song_id)
            if Like.objects.filter(user=request.user,song=song):
                likes = Like.objects.filter(user=request.user,song=song)
                for like in likes:
                    like.delete()
                return JsonResponse({"success": "unliked successfully"})
            like = Like.objects.create(user=request.user,song=song)
            response = JsonResponse({"success": "liked successfully"})
            return response
        response = JsonResponse({"error": "you don't have permission to like until login"})
        response.status_code = 403
        return response


class CommentView(View):
    form_class = CommentForm

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        print('1'*25)
        print(request.POST)
        print(request.POST.get('text'))
        if request.user.is_authenticated:
            print('2'*25)
            form = self.form_class(request.POST)
            print(form.errors)
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            user_image = comment.user.photo.url if comment.user.photo else ""
            response = JsonResponse({"message": "comment created successfully",
                                    "comment_text" : comment.text, "comment_author": comment.user.get_full_name() or comment.user.username or comment.user.phone,
                                    "comment_created_at": str(datetime.strftime(comment.created_at, '%Y-%m-%d %H:%M:%S')), "user_image": user_image})
            return response

        print('4'*25)
        response = JsonResponse({"error": "Please login to write comment."})
        response = JsonResponse({"error": "Please login to write comment."},)
        response.status_code = 403
        return response
