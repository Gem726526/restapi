from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View 
from .models import Update
import json
from cfeapi import JsonResponseMixin

def update_model_list_view(request):
    data={
        "count": 1

    }
    #json_data = json.dumps(data)
    #return HttpResponse(json_data, content_type= 'application/json') 
    return JsonResponse(data)

class SerializedView(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data={
            "user": obj.user.username,
            "content": obj.content
        }


        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type= 'application/json')

