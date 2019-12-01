from django import forms
from .models import Users

class UserForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ('username','userid','mobile','category')
        labels = {
            'username':'Name',
            'userid' :'ISBN',
            'mobile' :'Mobile',
            'category':'Category'
        }
    def __init__(self, *args, **kwargs):
        super(UserForm,self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select category"