# -*- coding:utf-8 -*-
# @ProjectName  :django_test
# @FileName     :forms.py
# @Time         :2020/11/23 21:16
# @Author       :Wang D.Q
# @Descripion   :

from django import forms

from .models import System,Entry

class SystemForm(forms.ModelForm):
    class Meta:
        model = System
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols': 80})}

if __name__ == "__main__":
    run_code = 0