from django.forms import ModelForm
from .models import Blog

class CreateBlogPost(ModelForm):
    class Meta:
        model = Blog
        fields = ['title','thumbnail','body']

    def __init__(self, *args, **kwargs):
        super(CreateBlogPost, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'h-full-width h-remove-bottom','id':'cName'})
        self.fields['body'].widget.attrs.update({'class': 'h-full-width','id':'cMessage'})
