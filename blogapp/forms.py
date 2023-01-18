from django.forms import ModelForm
from .models import Blog, Message, Comment

class CreateBlogPost(ModelForm):
    class Meta:
        model = Blog
        fields = ['title','thumbnail','body']

    def __init__(self, *args, **kwargs):
        super(CreateBlogPost, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'h-full-width h-remove-bottom','id':'cName'})
        self.fields['body'].widget.attrs.update({'class': 'h-full-width','id':'cMessage'})

class ContactForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'h-full-width h-remove-bottom','id':'cName'})
        self.fields['email'].widget.attrs.update({'class': 'h-full-width h-remove-bottom','id':'cName'})
        self.fields['subject'].widget.attrs.update({'class': 'h-full-width h-remove-bottom','id':'cName'})
        self.fields['body'].widget.attrs.update({'class': 'h-full-width','id':'cMessage'})


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude =['blog']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'h-full-width h-remove-bottom','id':'cName'})
        self.fields['body'].widget.attrs.update({'class': 'h-full-width','id':'cMessage'})
