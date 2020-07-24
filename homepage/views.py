from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail


# Define method to handle requests to index page
def index(request):
    return render(request, 'homepage/index.html', {})


# Define method to handle requests to about page
def about(request):
    return render(request, 'homepage/about.html', {})


# Define method to handle requests to service page
def service(request):
    return render(request, 'homepage/service.html', {})


# Define a method to handle requests to the pricing page
def pricing(request):
    return render(request, 'homepage/pricing.html', {})


# Define a method to handle requests to the contact page
def contact(request):
    # If request is get, return the form
    if request.method != 'POST':
        return render(request, 'homepage/contact.html', {})

    # If request is post, process the data
    else:
        # Get posted data
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # Define context variable
        context = {
            'message_name': message_name,
            'message_email': message_email,
            'message': message
        }

        # Send email with the posted data
        email_subject = 'New Message from ' + message_name
        email_message = message
        from_email = message_email
        if email_subject and email_message and from_email:
            try:
                send_mail(email_subject, email_message, from_email, ['franklinokech@gmail.com'])
            except BadHeaderError:
                return render(request, 'homepage/contact_fail.html', {})
            return render(request, 'homepage/contact_success.html', context)
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return render(request, 'homepage/contact_fail.html', {})
