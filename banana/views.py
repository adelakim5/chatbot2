import json
from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from .mango.transformdata import transformData
from .mango.responseData import responseData
from .mango.shared import BLOCK_ID

## Serializers
# from .serializers import PostSerializer

ANSWER = ["극히 드물다","가끔 있었다","종종 있었다","대부분 그랬다","우울증 자가진단 시작하기"]

@csrf_exempt
def hello(request):
    rData = responseData(request)
    block_id = rData.getBlockId()
    print(block_id)
    utterance = rData.getUtterance()
    print(utterance)
    answer = 0
    if(utterance==ANSWER[0]):
        answer = 0
    elif(utterance==ANSWER[1]):
        answer = 1
    elif(utterance==ANSWER[2]):
        answer = 2
    elif(utterance==ANSWER[3]):
        answer = 3 
    block_name = rData.getBlockName()
    print(block_name)
    user_id = rData.getUserId()
    print(user_id)
    if(ANSWER.__contains__(utterance)):
        # 내가 현재 가지고 있는 값. => USER_ID 내가 구해야하는 값 
        # => 유저가 있는지 없는지 => MODEL:USER => USER_ID 있는지 없는지 확인
        user = User.objects.get(user=user_id)
        if user is None:
            user = User(user=user_id)
            user.save()
            
        post = Question(question=block_name, answer=answer, userId=user)
        post.save()
        data = transformData(block_id).getJsonData() 
    else:
        data = transformData(block_id).getJsonDump()
    return data
    

# Create your views he`re.
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

