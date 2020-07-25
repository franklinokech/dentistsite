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


# Define method to handle bookings data
def booking(request):
    # Check if it was post or get request
    if request.method != 'POST':

        return render(request, 'homepage/booking.html', {})

    else:
        # Get posted data
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_time = request.POST['your-time']
        your_message = request.POST['your-message']

        # put data in context dict
        context = {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_time': your_time,
            'your_message': your_message,
        }

        # handle emailing the booking data
        # Send email with the posted data
        email_subject = 'New Booking from ' + your_name
        email_message = 'Phone: ' + your_phone + " Email: " + your_email + " Address: " + your_address + " Schedule: " \
                        + your_schedule \
                        + " Time: " + your_time + " Message: " + your_message
        from_email = your_email
        if email_subject and email_message and from_email:

            try:

                send_mail(email_subject, email_message, from_email, ['franklinokech@gmail.com'])
            except BadHeaderError:

                return render(request, 'homepage/booking_fail.html', {})

            return render(request, 'homepage/booking_success.html', context)

        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return render(request, 'homepage/booking_fail.html', {})


# Define a handler for newsletter signup
def newsletter(request):

    # check the request type
    if request.method != 'POST':

        return render(request, 'homepage/index.html', {})

    else:
        nl_email = request.POST['nl-email']

        # define context variable
        context = {
            'nl_email': nl_email
        }

        # handle emailing the booking data
        # Send email with the posted data
        email_subject = 'Subscription confirmation '
        email_message = 'Thank you for subscribing to our newsletter, we shall bring you the best health tips ever'
        from_email = 'franklinokech@gmail.com'

        if email_subject and email_message and from_email:

            try:

                send_mail(email_subject, email_message, from_email, [nl_email])
            except BadHeaderError:

                return render(request, 'homepage/newsletter_fail.html', {})

            return render(request, 'homepage/newsletter_success.html', context)

        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return render(request, 'homepage/newsletter_fail.html', {})
