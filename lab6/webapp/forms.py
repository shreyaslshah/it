from django import forms

# A list of car manufacturers
MANUFACTURERS = [
    ('toyota', 'Toyota'),
    ('honda', 'Honda'),
    ('ford', 'Ford'),
    ('chevrolet', 'Chevrolet'),
    ('nissan', 'Nissan'),
]


class CarModelForm(forms.Form):
    manufacturer = forms.ChoiceField(
        choices=MANUFACTURERS, widget=forms.Select())
    model_name = forms.CharField(max_length=100, widget=forms.TextInput())


class FirstPageForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=False)
    roll = forms.CharField(label='Roll', max_length=10, required=False)
    subjects = forms.ChoiceField(label='Subjects', choices=[
        ('maths', 'Maths'),
        ('science', 'Science'),
        ('history', 'History'),
        ('english', 'English'),
    ])

class Q3Form(forms.Form):
    username = forms.CharField(required=True)
    email = forms.CharField(required=False)
    contact = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class Q4Form(forms.Form):
    BRAND_CHOICES = [
        ('HP', 'HP'),
        ('Nokia', 'Nokia'),
        ('Samsung', 'Samsung'),
        ('Motorola', 'Motorola'),
        ('Apple', 'Apple'),
    ]
    brand = forms.ChoiceField(choices=BRAND_CHOICES, widget=forms.RadioSelect)
    items = forms.MultipleChoiceField(choices=[('mobile', 'mobile'), ('laptop', 'laptop')], widget=forms.CheckboxSelectMultiple)
    quantity = forms.IntegerField()