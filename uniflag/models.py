from datetime import datetime

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _

from uniflag import conf


flag_types = [(k, conf.UNIFLAG_TYPES[k]['name']) for k in conf.UNIFLAG_TYPES.keys()]

all_values = []
for k in conf.UNIFLAG_TYPES:
    for i in conf.UNIFLAG_TYPES[k]['values']:
        all_values.append(i)


class Flag(models.Model):
    flag_type = models.PositiveSmallIntegerField(choices=flag_types, default=1)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")

    user = models.ForeignKey(User)  # user flagging the content
    when_added = models.DateTimeField(default=datetime.now)

    value = models.CharField(max_length=20, choices=all_values)
    comment = models.TextField(blank=True)  # comment by the flagger

    status = models.CharField(max_length=1, choices=conf.STATUS, default="1", blank=True)
    moderator = models.ForeignKey(User, null=True, blank=True,
                                  related_name="moderated_content")  # moderator responsible for last status change

    class Meta:
        unique_together = [("content_type", "object_id", "flag_type", "user")]

    def __unicode__(self):
        return u'{} - {}'.format(self.content_object, self.get_flag_type_display())


