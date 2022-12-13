from django import forms 

class MyForm(forms.Form):
    #CharFiels
    #EmailField
    # IntegerField 
    # MultipleChoice
    # FileField

    #Arguments (required, label, help_text, initial )
    FAVORITE_FOODS = [ 
        ("italian", "Italian"),
        ("greek", "Greek"),
        ("zimbo", "Zimbabwe"),
    ]
    name = forms.CharField(initial="John Doe")
    story = forms.CharField(widget=forms.Textarea(attrs={"rows": 2}))
    email = forms.EmailField()
    reservation_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    fav_dish = forms.ChoiceField(choices=FAVORITE_FOODS)
    fav_dish_radio = forms.ChoiceField(choices=FAVORITE_FOODS, widget=forms.RadioSelect)
