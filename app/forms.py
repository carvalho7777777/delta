from django import forms
from . models import Feedback, Post


class FeedbackForm(forms.ModelForm):
    """форма обратной связи"""
    class Meta:
        model = Feedback
        fields = ["name", "email", "phone", 'text']
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ваше имя"}),
            "email": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Email"}),
            "phone": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Номер телефона +79000000000"}),
            "text": forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Текст сообщения", 'rows': 5}),

        }
        labels = {
            'name': '',
            'email': '',
            'phone': '',
            'text': '',
        }

class PostForm(forms.ModelForm):
    """форма редактирования поста"""
    class Meta:
        model = Post
        fields = '__all__'        


# class CommentForm(forms.ModelForm):
#     """форма комментариев"""
#     body = forms.CharField(widget=forms.Textarea(attrs={'class': 'inputtext form-control', 'placeholder': "Ваш комментарий ...", 'rows': 3, "cols": 50,}), required=True)

#     class Meta:
#         model = Comment
#         fields = ('body',)
#         # widgets = {
#         #     "body": forms.Textarea(attrs={'class': 'inputtext form-control', 'placeholder': "Ваш комментарий ...", 'rows': 3, "cols": 2,}),

#         # }
#         # labels = {
#         #     'body': '',
#         # }