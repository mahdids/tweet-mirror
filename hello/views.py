from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import views
from rest_framework.response import Response
from .models import Greeting
from django.http import JsonResponse
import os
from gettingstarted.settings import BASE_DIR
import random
from django.http import JsonResponse
from django.views.generic import TemplateView
# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "Demo.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})



def get_event_names(request):
    # p=BASE_DIR+ '\\hello\\DataFile\\total_tweets.json'
    # json_data = open(p)
    # data = json.load(json_data)
    # event="1"
    # currentList=[]
    # for json_obj in data:
    #     if json_obj['event']!=event:
    #         filename =BASE_DIR+ '\\hello\\DataFiles\\'+ event + '.json'
    #         with open(filename, 'a') as out_json_file:
    #             # Save each obj to their respective filepath
    #             # with pretty formatting thanks to `indent=4`
    #             json.dump(currentList, out_json_file, indent=4)
    #         event=json_obj['event']
    #         currentList=[]
    #         currentList.append(json_obj)
    #     else:
    #         currentList.append(json_obj)
    # filename = BASE_DIR + '\\hello\\DataFile\\' + event + '.json'
    # with open(filename, 'a') as out_json_file:
    #     json.dump(currentList, out_json_file, indent=4)
    event_names=["NEWTOT", "LIVARS", "CHEMCI", "MUNTOT", "MUNMCI", "NEWMCI", "MUNCHE", "TOTMCI", "NEWCHE", "TOTCHE", "CHEARS", "NEWLIV", "MUNNEW", "TOTMUN", "TOTARS", "NEWMUN", "MUNLIV", "NEWARS", "MUNARS"]
    response = HttpResponse(json.dumps(event_names),status=status.HTTP_200_OK)
    _acao_response(response)
    return response

def get_sample_data(request,event_name, count):
    dirname = os.path.dirname(__file__)

    p =os.path.join(dirname,  'DataFiles/'+event_name+'.json')
    json_data = open(p)
    data = json.load(json_data)
    s=random.sample(data,count*4)
    green=[]
    red=[]
    blue=[]
    for tweet in s:
        if tweet['DCT_type']=="after":
            green.append(tweet)
        if tweet['DCT_type']=="before":
            red.append(tweet)
        if tweet['DCT_type']=="ongoing":
            blue.append(tweet)
    result=[]

    countH = count // 2
    countQ = count // 4
    if len(red) + len(green) < countH:
        result.extend(green)
        result.extend(red)
    else:
        if len(red) > countQ and len(green) > countQ:
            result.extend(green[:countQ])
            result.extend(red[:countQ])
        else:
            if len(red) < countQ:
                result.extend(green[:(countH - len(red))])
                result.extend(red)
            else:
                result.extend(red[:(countH - len(green))])
                result.extend(green)
    result.extend(blue[:count - len(result)])
    response = HttpResponse(json.dumps(result), content_type="application/json")
    _acao_response(response)
    return response

def _acao_response(response):
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'GET'

def get_tweet_with_id(request,event_name, tweet_id):
    dirname = os.path.dirname(__file__)

    try:
        p = os.path.join(dirname, 'DataFiles/' + event_name + '.json')
        json_data = open(p)
        data = json.load(json_data)
        for json_obj in data:
            if json_obj['tweet_id'] == tweet_id:
                j=json.dumps(json_obj)
                response = HttpResponse(j, content_type="application/json")
                _acao_response(response)
                return response
        response = HttpResponse({}, content_type="application/json")
        _acao_response(response)
        return response
    except:
        response = HttpResponse("Error",status=status.HTTP_400_BAD_REQUEST,content_type="application/json")
        _acao_response(response)
        return response

