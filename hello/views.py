from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm, FindForm
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Min, Max

#indexクラス
class Index(TemplateView):
    def __init__(self):
        #object.all()→オブジェクトを全て取得する/all()でクエリーセットを取得
        self.data = Friend.objects.all()
        re1 = Friend.objects.aggregate(Count('age'))
        re2 = Friend.objects.aggregate(Sum('age'))
        re3 = Friend.objects.aggregate(Avg('age'))
        re4 = Friend.objects.aggregate(Min('age'))
        re5 = Friend.objects.aggregate(Max('age'))
        msg = 'count:' + str(re1['age__count'])\
            + '<br>Sum:' + str(re2['age__sum'])\
            + '<br>Average:' + str(re3['age__avg'])\
            + '<br>Min:' + str(re4['age__min'])\
            + '<br>Max' + str(re5['age__max'])
        self.params = {
            'title':'Hello',
            'message':msg,
            'data': self.data,
            }

    #getアクセスの際に実行(普通にアクセスしたとき)
    def get(self, request):
        return render(request, 'hello/crud_check.html', self.params)


#Createクラス
class Create(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'Hello',
            'form': FriendForm(),
            }
    
    def get(self,request):
        return render(request, 'hello/create.html', self.params)
    
    #この部分でCREATEしている
    def post(self,request):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')

#Editクラス:編集する
class Edit(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'Hello World',
            'id': 0,
            'form': ''
            }

    def post(self, request, num):
        obj = Friend.objects.get(id=num)
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    
    def get(self, request, num):
        obj = Friend.objects.get(id=num)
        self.params['id'] = num
        self.params['form'] = FriendForm(instance=obj)
        return render(request, 'hello/edit.html', self.params)

#Deleteクラス
class Delete(TemplateView):
    def __init__(self):
        self.params = {
            'title':'Hello World',
            'id': 0,
            'obj':'',
            }
        
    def post(self, request, num):
        friend = Friend.objects.get(id=num)
        friend.delete()
        return redirect(to='/hello')
    
    def get(self, request, num):
        self.params['id'] = num
        self.params['obj'] = Friend.objects.get(id=num)
        return render(request, "hello/delete.html", self.params)

#findクラス
class Find(TemplateView):
    def  __init__(self):
        self.params = {
            'title': 'Hello World',
            'msg': '',
            'form': '',
            'data': '',
            }

    def post(self, request):
        msg = request.POST['find']
        form = FindForm(request.POST)
        sql = 'select * from hello_friend'
        if msg != '':
            sql += 'where ' + msg
        data = Friend.objects.raw(sql)
        msg = sql
        self.params['msg'] = msg
        self.params['form'] = form
        self.params['data'] = data
        
        return render(request, 'hello/find.html', self.params)
    
    
    def get(self, request):
        self.params['msg'] = 'search words'
        self.params['form'] = FindForm()
        self.params['data'] = Friend.objects.all()
        return render(request, 'hello/find.html', self.params)