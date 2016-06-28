from django.views.generic import DetailView, TemplateView

from company.models import Employee
from products.models import Product
from about.models import ContentBox


class Index(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Index, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books


        context['team'] = Employee.objects.filter(executive=True)

        context['products'] = Product.objects.filter(private=False)

        context['contentboxes'] = ContentBox.objects.all()
        return context


'''


'''