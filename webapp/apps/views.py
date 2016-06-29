from django.views.generic import DetailView, TemplateView

from company.models import Employee
from products.models import Product
from about.models import ContentBox
from services.models import ServiceGroup


class Index(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Index, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books


        context['team'] = Employee.objects.filter(executive=True)

        context['products'] = Product.objects.filter(public=False)

        context['contentboxes'] = ContentBox.objects.all()

        context['service_groups'] = ServiceGroup.objects.all()
        return context


'''


'''