from django.contrib import admin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

csrf_protect_m = method_decorator(csrf_protect)


class PreferencesAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        """
        If we only have a single preference object redirect to it,
        otherwise display listing.
        """
        model = self.model
        if model.objects.all().count() > 1:
            return super(PreferencesAdmin, self).changelist_view(request)
        else:
            obj = model.singleton.get()
            return redirect(
                reverse(
                    'admin:%s_%s_change' % (
                        model._meta.app_label, model._meta.model_name
                    ),
                    args=(obj.id,)
                )
            )
