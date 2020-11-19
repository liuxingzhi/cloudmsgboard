from django.shortcuts import render
from datetime import datetime
from django.http.response import HttpResponse, JsonResponse, FileResponse, Http404
from django.views.decorators.http import require_http_methods
import os, json
from .models import MsgBoard
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.
@require_http_methods(["GET", "POST"])
def msgproc(request):
    datalist = []
    if request.method == "POST":
        userA = request.POST.get('UserA', None)
        userB = request.POST.get('UserB', None)
        msg = request.POST.get('msg', None)
        time = datetime.now()
        record = MsgBoard(userA, userB, msg, time.strftime("%Y-%m-%d %H:%M:%S"))
        record.save()

    if request.method == "GET":
        pass

    fields = MsgBoard._meta.fields
    for index, f in enumerate(fields):
        if f.verbose_name != '留言目标':
            print(f.verbose_name)
            datalist.append(f.verbose_name)
    print(datalist)
    datalist.remove("read")
    print(datalist)
    return render(request, "MsgSingleWeb.html", {"data": datalist})


def homeproc(request):
    response = HttpResponse()
    response.write("<h1>This is homepage,more functions are <a href='./msggate'>here</a></h1>")
    response.write("<h2>this is a small title</h2>")
    return response


def all_msg_ajax(request, receiver):
    print("collecting receiver's all messages")
    if receiver is not None:
        try:
            records = MsgBoard.objects.filter(receiver=receiver)
            for record in records:
                record.read = True
                record.save()
            json_dict = serialize('json', records)
            # print(json_dict)
            # something = json.loads(json_dict)
            # print(type(something))
            # for a in something:
            #     print(a)
            json_response = JsonResponse(json_dict, safe=False)
            return json_response
        except MsgBoard.DoesNotExist:
            raise Http404("No message left to this user")


def unread_msg_ajax(request, receiver):
    print("collect unread messages")
    print("receive print request from 前端")
    if receiver is not None:
        try:
            records = MsgBoard.objects.filter(receiver=receiver).filter(read=False)
            for record in records:
                record.read = True
                record.save()
            json_dict = serialize('json', records)
            json_response = JsonResponse(json_dict, safe=False)
            # return None
            return json_response
        except MsgBoard.DoesNotExist:
            # raise Http404("No message left to this user")
            return None


def homeproc2(request):
    dic = {'Abel': 'xingzhi2'}
    response = JsonResponse(dic)
    return response


def download_lingxiang(request):
    cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(cwd + "/msgapp/templates/mymosaic.png", "rb"))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="lingxiang_mosaic.png"'
    return response
