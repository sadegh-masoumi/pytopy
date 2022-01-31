from .models import WorkWithUs
from .forms import WorkWithUsForm
from django.views.generic import FormView


class WorkWithUsView(FormView):
    template_name = 'work_with_us.html'
    form_class = WorkWithUsForm
    success_url = '/work-with-us'

    def form_valid(self, form):
        WorkWithUs.objects.create(
            **form.cleaned_data
        )
        return self.render_to_response(self.get_context_data(message=True, form=form))

    def get_context_data(self, message: bool = False, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = message
        return context
