from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm, SelectForm, FindForm
from django.views.generic import TemplateView
from django.db.models import Q

#前表示
class Index(TemplateView):
    def __init__(self):
        self.data = Book.objects.all()
        self.params = {
            'title': '図書管理アプリ',
            'msg': '好きな本が探せるよ！',
            'form': '',
            'data': '',
            }
        
    def post(self, request):
        self.params['msg'] = 'search result:'
        self.params['form'] = FindForm(request.POST)
        str = request.POST['find']
        #val = str.split()
        self.params['data'] = Book.objects.filter(
                                                    Q(name__contains = str) |
                                                    Q(author__contains = str) |
                                                    Q(code__contains = str)
                                                    )  
        return render(request, 'library/index.html', self.params)
    
    def get(self, request):
        self.params['msg'] = 'search word:'
        self.params['form'] = FindForm()
        self.params['data'] = Book.objects.all()
        return render(request, 'library/index.html', self.params)

# =============================================================================
# def index(request):
#     data = Book.objects.all()
#     params = {
#         'title':'図書管理アプリ',
#         'msg':'好きな本が探せるよ！',
#         #'select_form':SelectForm(),
#         #'find':FindForm(),
#         'data': data
#         }
#     return render(request, 'library/index.html', params)
# =============================================================================

#create:本の情報を登録する
def create(request):
    if(request.method == 'POST'):
        obj = Book()
        book = BookForm(request.POST, instance=obj)
        book.save()
        return redirect(to='/library')
    params = {
        'title':'図書管理アプリ',
        'msg':'本の情報を、登録してね！',
        'form': BookForm()
        }
    return render(request, 'library/create.html', params)

#edit:本の情報を更新する
def edit(request, num):
    obj = Book.objects.get(id=num)
    if(request.method == 'POST'):
        book = BookForm(request.POST, instance=obj)
        book.save()
        return redirect(to='/library')
    params = {
        'title':'図書管理アプリ',
        'msg':'本の情報を、編集できるよ！',
        'id': num,
        'form': BookForm(instance=obj),
    }
    return render(request, 'library/edit.html', params)

#delete:本の情報を削除する
def delete(request, num):
    book = Book.objects.get(id=num)
    if(request.method == 'POST'):
        book.delete()
        return redirect(to='/library')
    params = {
        'title':'図書管理アプリ',
        'id': num,
        'obj': book,
    }
    return render(request, 'library/delete.html', params)

# =============================================================================
# #本の情報を検索する
# def find(request):
#     if(request.method == 'POST'):
#         msg = 'search result:'
#         form = BookForm(request.POST)
#         str = request.POST
#         data = Book.objects.filter(name__contain=str)
# =============================================================================


    







