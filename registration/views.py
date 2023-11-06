from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import Registrant
from django.db.models import Q


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new Registrant object from the form's cleaned data
            registrant = Registrant(
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                facebook=form.cleaned_data['facebook'],
                mobile=form.cleaned_data['mobile'],
                bloodgroup=form.cleaned_data['bloodgroup'],
                profession=form.cleaned_data['profession'],
                tshirt_size=form.cleaned_data['tshirt_size'],
                spouse_check=form.cleaned_data['spouse_check'],
                child_checkbox=form.cleaned_data['child_checkbox'],
                number_of_children=form.cleaned_data.get(
                    'number_of_children', 0),
                payment_method=form.cleaned_data['payment_method'],
                hand_cash_to=form.cleaned_data.get('hand_cash_to', ''),
                transaction_id=form.cleaned_data.get('transaction_id', ''),
                total_member=form.cleaned_data['total_member'],
                amount=form.cleaned_data['amount'],
                service_charge=form.cleaned_data['service_charge'],
                total_amount=form.cleaned_data['total_amount'],
            )
            registrant.save()  # Save the new Registrant to the database
            # Redirect to a new URL after POST
            # Replace 'success_url' with the name of the url you want to redirect to
            request.session['registrant_name'] = registrant.full_name
            request.session['registrant_id'] = registrant.unique_id
            request.session['payment_method'] = registrant.payment_method
            request.session['transaction_id'] = registrant.transaction_id
            request.session['email'] = registrant.email
            request.session['total_member'] = registrant.total_member

            # Make sure to use the correct URL name
            return redirect('success_url')

    else:
        form = RegistrationForm()  # An unbound form

    return render(request, 'register.html', {'form': form})


def registration_success(request):
    # Retrieve the values from the session
    registrant_name = request.session.get('registrant_name', 'Guest')
    registrant_id = request.session.get('registrant_id', 'Unknown ID')
    payment_method = request.session.get('payment_method', 'Not Specified')
    transaction_id = request.session.get('transaction_id', 'N/A')
    email = request.session.get('email', 'Not Known')

    # Construct the context dictionary
    context = {
        'registrant_name': registrant_name,
        'registrant_id': registrant_id,
        'payment_method': payment_method,
        'transaction_id': transaction_id,
        'email': email,
    }

    # Pass the context to the template
    return render(request, 'success.html', context)


def check_approval_status(request):
    status_message = ''
    query = request.POST.get('email_or_id', '')

    if request.method == 'POST':
        # Filter for either email or unique ID
        registrants = Registrant.objects.filter(
            Q(email=query) | Q(unique_id=query)
        )

        if registrants.exists():
            registrant = registrants.first()
            # Check if the registrant is approved or not
            if registrant.approved:
                status_message = 'Approved'
            else:
                status_message = 'Pending'
        else:
            status_message = 'No registrant found with the provided information.'

    return render(request, 'approval_status.html', {
        'status_message': status_message,
        'query': query
    })


def home(request):
    return render(request, 'home.html')
