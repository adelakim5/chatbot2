from django.http import JsonResponse
from .shared import QUESTION, BLOCK_ID
class transformData:
    
    def __init__(self,blockId):
        self.blockId = blockId
        self.block_index = BLOCK_ID.index(blockId)
        self.question = QUESTION[self.block_index]
        
    def getJsonData(self):
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
                    "blockId": self.blockId,
                    "label": "극히 드물다"
                },
                {
                    "messageText": "가끔 있었다",
                    "action": "block",
                    "blockId": self.blockId,
                    "label": "가끔 있었다"
                },
                {
                    "messageText": "종종 있었다",
                    "action": "block",
                    "blockId": self.blockId,
                    "label": "종종 있었다"
                },
                {
                    "messageText": "대부분 그랬다",
                    "action": "block",
                    "blockId": self.blockId,
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
                    "text": "설문을 종료합니다."
                }
                }
            ]
            }
        }
        return JsonResponse(data)