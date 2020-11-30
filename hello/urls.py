from django.urls import path
from .views import Index, Create, Edit, Delete, Find

# ''ということは、django.appのurlsで呼び出した'hello/'でhello内のviewを呼び出すことができる
urlpatterns = [
    #as_view()により、HelloViewクラスを呼び出す
    path('', Index.as_view(), name='index'),
    path('create', Create.as_view(), name='create'),
    path('edit/<int:num>', Edit.as_view(), name='edit'),
    path('delete/<int:num>', Delete.as_view(), name='delete'),
    path('find/', Find.as_view(), name='find'),
    ]