from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
import logging
from .models import Employee

user_logger = logging.getLogger("user")
@receiver(user_logged_in)
def log_user_login(sender, user, **kwargs):
    """ log user login to user log """
    # user.is_staff = True
    
    if user.is_staff:
        employee_active = Employee(user=user)
        employee_active.save()
    
    user_logger.info('%s login successful', user, type(user))


 