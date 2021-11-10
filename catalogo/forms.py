from django.db.models import fields
from django.forms import ModelForm
from catalogo.models import Author

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'