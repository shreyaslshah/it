from django import forms


class RegForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    views = forms.IntegerField()
    available = forms.BooleanField()


class SmartphoneEg(forms.Form):
    YES_SMARTPHONE = 'Yes'
    NO_SMARTPHONE = 'No'
    SMART_PHONE_OWNERSHIP = ((YES_SMARTPHONE, 'Yes'), (NO_SMARTPHONE, 'No'))
    smart_phone_ownership = forms.ChoiceField(widget=forms.RadioSelect(),
                                              choices=SMART_PHONE_OWNERSHIP,
                                              initial="",
                                              label='Do you own a Smartphone',
                                              required=False)


class GeeksForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(widget=forms.CheckboxInput)
    views = forms.IntegerField(widget=forms.TextInput)
    available = forms.BooleanField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    contact_num = forms.IntegerField()

class SessLoginForm(forms.Form):
    username = forms.CharField(max_length = 100)
    password= forms.CharField(widget= forms.PasswordInput())