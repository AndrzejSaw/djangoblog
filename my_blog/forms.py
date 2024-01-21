from django import forms
from myblog.my_blog.models import Post  # Предполагая, что модель Post находится в приложении my_blog

class ImgForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image']
