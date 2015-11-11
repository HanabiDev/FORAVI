from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django_resized.forms import ResizedImageField

class SiteUser(User):
    ResizedImageField(
        size=[150, 150], crop=['middle', 'center'], upload_to='media/uploads/avatars',
        default='media/uploads/avatars/foravi_avatar.png',  null=True, blank=True
    ).contribute_to_class(User,'avatar')

    def save(self, *args, **kwargs):
        super(SiteUser, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.first_name + ' '+ self.last_name

    class Meta:
        proxy = True

