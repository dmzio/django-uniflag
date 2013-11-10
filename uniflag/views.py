from django.views.generic.edit import CreateView, UpdateView, DeleteView, BaseCreateView, BaseUpdateView
from uniflag.forms import FlagForm
from uniflag.models import Flag


import json

from django.http import HttpResponse
from django.views.generic.edit import CreateView


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form. Stoles from django documentation
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json; charset=utf-8'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return super(AjaxableResponseMixin, self).form_invalid(form)

    def form_valid(self, form):
        if self.request.is_ajax():
            self.object = form.save()

            data = {
                'pk': form.instance.pk,
                }
            return self.render_to_json_response(data)
        else:
            return super(AjaxableResponseMixin, self).form_valid(form)

#TODO access control
class FlagCreate(AjaxableResponseMixin, BaseCreateView):
    form_class = FlagForm
    model = Flag
    def get_form(self, form_class):
        form = super(FlagCreate, self).get_form(form_class)
        form.instance.user = self.request.user

        return form


class FlagUpdate(AjaxableResponseMixin, BaseUpdateView):
    form_class = FlagForm
    model = Flag

    def get_form(self, form_class):
        form = super(FlagUpdate, self).get_form(form_class)
        form.instance.user = self.request.user
        return form