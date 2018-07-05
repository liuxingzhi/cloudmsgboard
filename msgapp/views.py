from django.shortcuts import render
from datetime import datetime
from django.http.response import HttpResponse, JsonResponse, FileResponse, Http404
from django.views.decorators.http import require_http_methods
import os,json
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
        # return render(request, "MsgSingleWeb.html", {'data': datalist})
        # return render(request, "MsgSingleWeb.html")
        # with open('msgdata.txt', 'a+') as f:
        #     print("time==========", time)
        #     f.write("{}--{}--{}--{}--\n".format(userB, userA, msg, time.strftime("%Y-%m-%d %H:%M:%S")))

    if request.method == "GET":
        pass
        # userC = request.GET.get("userC", None)
        # if userC != None:
        #     try:
        #         records = MsgBoard.objects.filter(receiver=userC)
        #         datalist = serialize('json', records)
        #         print(datalist)
        #     except MsgBoard.DoesNotExist:
        #         raise Http404("No message left to this user")
            # with open("msgdata.txt", "r") as f:
            #     cnt = 0
            #     for line in f:
            #         linedata = line.split("--")
            #         if linedata[0] == userC:
            #             cnt += 1
            #             d = {"userA": linedata[1], "msg": linedata[2], "time": linedata[3]}
            #             datalist.append(d)
            #         if cnt >= 10:
            #             break

    return render(request, "MsgSingleWeb.html")


def homeproc(request):
    response = HttpResponse()
    response.write("<h1>This is homepage,more functions are <a href='./msggate'>here</a></h1>")
    response.write("<h2>this is a small title</h2>")
    return response


def msg_ajax(request, receiver):
    if receiver != None:
        try:
            records = MsgBoard.objects.filter(receiver=receiver)
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
