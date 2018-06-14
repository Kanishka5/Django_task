
from django.views import generic
from homepage.models import Member

class IndexView(generic.ListView):

    template_name='memberpage/member.html'


    def get_queryset(self):
        return Member.objects.all()
