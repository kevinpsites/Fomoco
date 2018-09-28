from django.conf import settings
from django_mako_plus import view_function, jscontext
from django import forms
from django.http import HttpResponseRedirect
from formlib.form import Formless

@view_function
def process_request(request):

    form = TestForm(request)

    if form.is_valid():
        #work goes here
        return HttpResponseRedirect('/')





#render the format
    context = {
        'form': form,

    }
    return request.dmp.render('formtest.html',context)


class TestForm(Formless):
    def init(self):
        self.fields['Your_name'] = forms.CharField(label='Your Name', max_length=100)
        self.fields['age']= forms.IntegerField(label='Your Age')
        self.fields['comment'] = forms.CharField(label='Your Comment')
        self.fields['Renewal_Date'] = forms.DateField(label='Renewal Date', help_text="enter a date between now and next year")
