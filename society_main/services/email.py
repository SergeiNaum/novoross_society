from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def send_contact_email_message(subj, email, message, ip):
    """
    Function to send contact form email
    """
    message = render_to_string('society_main/system/email/feedback_email_send.html', {

        'email': email,
        'message': message,
        'ip': ip,
    })

    email = EmailMessage(subj, message, settings.EMAIL_SERVER, settings.EMAIL_ADMIN)
    email.send(fail_silently=False)
