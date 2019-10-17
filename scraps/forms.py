from django import forms

class RequestForm(forms.Form):
    url = forms.URLField(label='Web page url', required=True)
   
    def clean(self):
        cleaned_data = super(RequestForm, self).clean()
        url = cleaned_data.get('url')
        if not url:
            raise forms.ValidationError('You have to write something!')