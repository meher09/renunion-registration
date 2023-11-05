from django import forms


class RegistrationForm(forms.Form):
    full_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    facebook = forms.URLField(required=False, widget=forms.URLInput(
        attrs={'class': 'form-control'}))
    mobile = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    bloodgroup = forms.ChoiceField(choices=[
        ('O +ve', 'O +ve'), ('O -ve', 'O -ve'),
        ('A +ve', 'A +ve'), ('A -ve', 'A -ve'),
        ('B +ve', 'B +ve'), ('B -ve', 'B -ve')
    ], widget=forms.Select(attrs={'class': 'form-select'}))
    profession = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tshirt_size = forms.ChoiceField(choices=[
        ('S', 'S - Small'), ('M', 'M - Medium'), ('L', 'L - Large'),
        ('XL', 'XL - Extra Large'), ('XXL', 'XXL - Extra Extra Large'),
        ('XXXL', 'XXXL - Extra Extra Extra Large')
    ], widget=forms.Select(attrs={'class': 'form-select'}))
    spouse_check = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    child_checkbox = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    number_of_children = forms.IntegerField(
        required=False, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    payment_method = forms.ChoiceField(choices=[
        ('bkash', 'Bkash'), ('nagad', 'Nagad'), ('handcash', 'Hand Cash')
    ], widget=forms.Select(attrs={'class': 'form-select'}))
    hand_cash_to = forms.CharField(
        max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    transaction_id = forms.CharField(
        max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    total_member = forms.IntegerField(min_value=1, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'readonly': 'readonly'}))
    amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'readonly': 'readonly'}))
    service_charge = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'readonly': 'readonly'}))
    total_amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'readonly': 'readonly'}))


class ApprovalStatusCheckForm(forms.Form):
    email_or_id = forms.CharField(label='Email or Unique ID', max_length=100)

    def clean_email_or_id(self):
        data = self.cleaned_data['email_or_id']
        # You can add more validation here if needed
        return data
