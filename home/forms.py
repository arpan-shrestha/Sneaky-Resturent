from django import forms

class contactForm(forms.Form):
    name = forms.CharField(required=True, max_length=30,widget=forms.TextInput(attrs={'placeholder':'Enter your Name'}), label='')
    
    
    
    subject = forms.CharField(
        max_length=30,
        widget= forms.TextInput(
            attrs={
                'placeholder':'Enter subject '
            }
        ),
        label=''
    )



    Email = forms.EmailField(
        required= True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter your email address'
            }
        ),
        label=''
        
        )
    message = forms.CharField(widget = forms.Textarea(attrs={'placeholder':'Type your message'}) ,required= True, label='')
