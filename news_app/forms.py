from django import forms

from news_app.models import Comment


# class NewsUpdateForm(forms.ModelForm):
#     class Meta:
#         model = News
#         fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
