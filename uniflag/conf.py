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


def user_can_flag(user, obj, flag_type):
    """
    whether particular user can set flag for the object or not
    f.e. forbid flagging of own content
    """
    return True

USER_CAN_FLAG = getattr(settings, "USER_CAN_FLAG", None)
if USER_CAN_FLAG is not None:
    from importlib import import_module
    from django.core.exceptions import ImproperlyConfigured
    module_name = '.'.join(USER_CAN_FLAG.split('.')[:-1])
    func_name = USER_CAN_FLAG.split('.')[-1]
    try:
        USER_CAN_FLAG_FUNC = getattr(import_module(module_name), func_name)
    except ImportError:
        raise ImproperlyConfigured('"USER_CAN_FLAG" function can\'t be imported')
else:
    USER_CAN_FLAG_FUNC = user_can_flag
