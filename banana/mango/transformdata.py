from django.http import JsonResponse
from ..models import Question
from .shared import QUESTION, BLOCK_ID
class transformData:
    def __init__(self,blockId , user):
        self.blockId = blockId
        self.user = user
        self.block_index = BLOCK_ID.index(blockId) ## 2
        self.question = QUESTION[self.block_index] ## 먹고 싶지 않다.
        if(len(BLOCK_ID) > self.block_index+1): ## 
            self.nextBlockId = BLOCK_ID[self.block_index+1] ## 3
        else:
            self.nextBlockId = 0
    
    def getJsonData(self):
        if self.block_index - 4 == 20:
            total = 0
            questions = Question.objects.all().filter(userId=self.user)
            for question in questions:
                total = total + question.answer
            
            data = {
                "version": "2.0",
                "template": {
                    "outputs":None
                }
            }
            if total >= 25:
                outputs =  [
                        {
                            "simpleText": {
                                "text": "당신의 우울증 점수는 {} 입니다.".format(str(total))
                            }
                        },{
                            "simpleText": {
                                "text": "ㅠㅠ 많이 우울하신가요? 우울증이 의심돼요"
                            }
                        },{
                            "simpleText": {
                                "text": "전문가와 상담이 필요해보여요.."
                            }
                        }
                    ]
                data["template"]["outputs"] = outputs
            else:
                outputs =  [
                        {
                            "simpleText": {
                                "text": "당신의 우울증 점수는 {} 입니다.".format(str(total))
                            }
                        },{
                            "simpleText": {
                                "text": "음.. 심각한 정도까지는 아닌것 같아요"
                            }
                        },{
                            "simpleText": {
                                "text": "하지만 만약 우울한 기분이 계속된다면 전문가를 만나보는걸 추천해요!"
                            }
                        }
                    ]
                data["template"]["outputs"] = outputs
                
                
        else:
            data = {
                "version": "2.0",
                "template": {
                    "outputs": [
                    {
                        "simpleText": {
                        "text": self.question
                        }
                    }
                    ],
                    "quickReplies": [
                    {
                        "messageText": "극히 드물다",
                        "action": "block",
                        "blockId": self.nextBlockId,
                        "label": "극히 드물다"
                    },
                    {
                        "messageText": "가끔 있었다",
                        "action": "block",
                        "blockId": self.nextBlockId,
                        "label": "가끔 있었다"
                    },
                    {
                        "messageText": "종종 있었다",
                        "action": "block",
                        "blockId": self.nextBlockId,
                        "label": "종종 있었다"
                    },
                    {
                        "messageText": "대부분 그랬다",
                        "action": "block",
                        "blockId": self.nextBlockId,
                        "label": "대부분 그랬다"
                    }
                    ]
                }
            }
        return JsonResponse(data)
    
    def getJsonDump(self):
        data = {
            "version": "2.0",
            "template": {
            "outputs": [
                {
                "simpleText": {
                    "text": "진단을 종료합니다."
                }
                }
            ]
            }
        }
        return JsonResponse(data)