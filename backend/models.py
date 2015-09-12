from django.contrib.auth.models import User
from django_resized.forms import ResizedImageField


class SiteUser(User):
    ResizedImageField(size=[150, 150], crop=['middle', 'center'], upload_to='media/uploads/avatars', null=True, blank=True).contribute_to_class(User,'avatar')

    def __unicode__(self):
        return self.fisrt_name + ' '+ self.last_name

    class Meta:
        proxy = True