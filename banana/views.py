import json
from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from .mango.transformdata import transformData
from .mango.requestData import requestData
from .mango.shared import BLOCK_ID

## Serializers
# from .serializers import PostSerializer

ANSWER = ["극히 드물다","가끔 있었다","종종 있었다","대부분 그랬다","우울증 자가진단 시작하기"]

@csrf_exempt
def hello(request):
    rData = requestData(request)
    block_id = rData.getBlockId()
    print(block_id)
    utterance = rData.getUtterance()
    print(utterance)
    answer = reverseQ(rData.getPreBlockIndex(), utterance)
    block_name = rData.getBlockName()
    preBlock = str(rData.getPreBlockIndex())
    print(block_name)
    user_id = rData.getUserId()
    print(user_id)
    if(ANSWER.__contains__(utterance)):
        user = User.objects.get(user=user_id)
        if user is None:
            user = User(user=user_id)
            user.save()
        question = Question.objects.all().filter(userId=user)
        if question:
            question.get(question='질문{}'.format(preBlock))
            question.answer = answer
            question.save()
        else:
            question = Question(question='질문{}'.format(preBlock), answer=answer, userId=user)
            question.save()
        data = transformData(block_id,user).getJsonData()
    else:
        data = transformData(block_id,user).getJsonDump()
    return data

def reverseQ(block_index, utterance):
    answer = 0
    if block_index == 5 or block_index == 10 or block_index == 15 :
        if(utterance==ANSWER[0]):
            answer = 3
        elif(utterance==ANSWER[1]):
            answer = 2
        elif(utterance==ANSWER[2]):
            answer = 1
        elif(utterance==ANSWER[3]):
            answer = 0
    else:
        if(utterance==ANSWER[0]):
            answer = 0
        elif(utterance==ANSWER[1]):
            answer = 1
        elif(utterance==ANSWER[2]):
            answer = 2
        elif(utterance==ANSWER[3]):
            answer = 3
    return answer
        
    
    
    

# Create your views he`re.
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer