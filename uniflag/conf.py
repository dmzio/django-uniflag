from django.conf import settings
from django.utils.translation import ugettext_lazy as _

STATUS = getattr(settings, "UNIFLAG_STATUSES", [
    ("1", _("flagged")),
    ("2", _("flag rejected by moderator")),
    ("3", _("content removed by creator")),
    ("4", _("content removed by moderator")),
])

UNIFLAG_TYPES = getattr(settings, "UNIFLAG_TYPES", {
    1: {  # index of type which stored in the db
        'name': _('Complain'),
        'moderated': True,
        'commented': True,  # Whether to allow comments for flags. Only works together with 'modal'
        'modal': True,  # Reveal form as modal
        'values': [
            ('spam', _("Spam")),  # slug and Title for flag options
            ('obsolete', _("Obsolete info")),
        ]
    },
    2: {
        'name': _('Likes'),
        'moderated': False,
        'commented': False,
        'modal': False,
        'values': [
            ('like', _('Like')),
            ('dislike', _('Dislike'))
        ]
    }
})