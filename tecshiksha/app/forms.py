from django import forms

DESIGNATION_CHOICES= [
    ('student', 'Student'),
    ('working', 'Working'),
    ]

class ContactForm(forms.Form):
    fname = forms.CharField(required=True)
    lname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    city = forms.CharField(required=True)
    designation = forms.CharField(widget=forms.Select(choices= DESIGNATION_CHOICES))
    m_number = forms.IntegerField(required=True)
    form_content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

class InternForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    m_number = forms.IntegerField(required=True)
    # cv = forms.FileField()
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    form_content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
