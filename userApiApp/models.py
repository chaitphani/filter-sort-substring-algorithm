from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_len(value):
    if len(str(value)) > 6 or len(str(value)) < 5 :
        raise ValidationError(
            _('%(value)s should be min 5 and max 6 digit value.'),
            params={'value': value},
        )

class UserData(models.Model):

    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    company_name = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    zip = models.IntegerField(validators=[validate_len])
    email = models.EmailField(max_length=120, unique=True)
    web = models.URLField(max_length=120)
    age = models.IntegerField()

    def __str__(self):
        return '{}={}'.format(self.first_name, self.last_name)
        