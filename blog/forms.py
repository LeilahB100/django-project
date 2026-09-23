from django.forms import ModelForm
from blog.models import Authors, article

class AuthorForm(ModelForm):
    class Meta:
        model = Authors
        fields = '__all__'