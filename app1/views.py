from django.shortcuts import render
from django.http import HttpResponse
from .models import Touroku
from .forms import IdKensaku
from .forms import KenkoRecord
from django.shortcuts import redirect

def index(request):

    params = {
        'title':'生活データ',
        'msg':'all records',
        'form':IdKensaku(),
        'data':[],
        'gopage':'create',
    }

    if (request.method =='POST'):
        number = request.POST['id']
        item = Touroku.objects.get(id = number)
        params['data'] = [item]
        params['form'] = IdKensaku(request.POST)
    else:
        params['data'] = Touroku.objects.all().order_by('-id')
    return render(request, 'app1/index.html', params)


def create(request):

    params = {
        'title':'生活データ',
        'msg':'入力してください',
        'form':KenkoRecord(),
    }

    if (request.method =='POST'):
        obj = Touroku()
        record = KenkoRecord(request.POST, instance = obj)
        record.save()
        return redirect(to='/app1')
    return render(request, 'app1/create.html',params)


def edit(request,number):
    obj = Touroku.objects.get(id = number)
    if (request.method =='POST'):
        record = KenkoRecord(request.POST, instance = obj)
        record.save()
        return redirect(to='/app1')
    params = {
        'title':'生活データ',
        'id':number,
        'form':KenkoRecord(),
    }
    return render(request, 'app1/edit.html',params)

def delete(request,number):

    record = Touroku.objects.get(id = number)
    if (request.method =='POST'):
        record.delete()
        return redirect(to='/app1')
    params = {
        'title':'生活データ',
        'msg':"こちらのデータを削除しますか？",
        'id':number,
        'obj':record,
        }
    return render(request, 'app1/delete.html',params)