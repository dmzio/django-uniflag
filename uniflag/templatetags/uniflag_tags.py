from django import template
from django.contrib.contenttypes.models import ContentType
from uniflag import conf
from uniflag.models import Flag
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('uniflag/_flag_add_form.html', takes_context=False)
def add_flag_for(obj, user, flag_type):
    if flag_type not in conf.UNIFLAG_TYPES:
        raise KeyError('Flag type not in the configured UNIFLAG_TYPES')

    if not conf.USER_CAN_FLAG_FUNC(user, obj, flag_type):
        return {'flag_forbidden': True}

    ctx = {
        'flag_type_idx': flag_type,
        'values': conf.UNIFLAG_TYPES[flag_type]['values'],
        'flag_name': conf.UNIFLAG_TYPES[flag_type]['name'],
        'obj_type': ContentType.objects.get_for_model(obj),
        'obj_id': obj.id,
        'commented': conf.UNIFLAG_TYPES[flag_type]['commented'],
        'modal': conf.UNIFLAG_TYPES[flag_type]['modal'],
        'moderated': conf.UNIFLAG_TYPES[flag_type]['moderated'],
    }

    try:
        existent_flag = Flag.objects.get(content_type=ctx['obj_type'], object_id=obj.id, flag_type=flag_type, user=user)
        ctx.update({'flag': existent_flag})
    except ObjectDoesNotExist:
        pass

    return ctx


@register.inclusion_tag('uniflag/_flagform_js_snippet.html', takes_context=False)
def flagform_js():
    return {}