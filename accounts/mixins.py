from django.shortcuts import redirect


class AnonymousRequiredMixin:
    anonymous_required_redirect_url = '/'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.anonymous_required_redirect_url)

        return super().dispatch(*args, **kwargs)


class StaffRequiredMixin:
    staff_required_redirect_url = '/'

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect(self.staff_required_redirect_url)

        return super().dispatch(*args, **kwargs)
