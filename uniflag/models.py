from datetime import datetime

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _

from uniflag import conf


class Flag(models.Model):
    FLAG_TYPES = [(k, conf.UNIFLAG_TYPES[k]['name']) for k in conf.UNIFLAG_TYPES.keys()]
    ALL_VALUES = []
    for k in conf.UNIFLAG_TYPES:
        for i in conf.UNIFLAG_TYPES[k]['values']:
            ALL_VALUES.append(i)

    flag_type = models.PositiveSmallIntegerField(choices=FLAG_TYPES, default=1)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")

    user = models.ForeignKey(User)  # user flagging the content
    when_added = models.DateTimeField(default=datetime.now)

    value = models.CharField(max_length=20, choices=ALL_VALUES)
    comment = models.TextField(blank=True)  # comment by the flagger

    status = models.CharField(max_length=1, choices=conf.STATUS, default="1", blank=True)
    moderator = models.ForeignKey(User, null=True, blank=True,
                                  related_name="moderated_content")  # moderator responsible for last status change

    class Meta:
        unique_together = [("content_type", "object_id", "flag_type", "user")]

    def __unicode__(self):
        return u'{0} - {1}: {2}'.format(self.content_object, self.get_flag_type_display(), self.get_value_display())


