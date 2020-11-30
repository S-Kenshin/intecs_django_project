from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        #Field名はDBのカラムに対応する。
        fields = ['name','author','code','price']

# =============================================================================
# class FindForm(forms.Form):
#     find = forms.CharField(label='Find', required=False)
# =============================================================================

class SelectForm(forms.Form):
    check = forms.NullBooleanField(label='Check')

class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False)
