from django import forms
from app.models import *


class TopicForm(forms.Form):
    topic_name = forms.CharField()

#Model Form Creation
class TopicMForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'



class WebpageForm(forms.Form):
    topic_name = forms.ModelChoiceField(queryset=Topic.objects.all())
    name = forms.CharField()
    url = forms.URLField()
    email = forms.EmailField()


class WebpageMForm(forms.ModelForm):
    class Meta:
        model = Webpage
        fields = '__all__'