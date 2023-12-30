from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from Books.models import BookstoreModel
from Books.forms import Bookstoreform
from django.contrib import messages
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


class MyTemplateView(TemplateView):
    template_name='index.html'
    
    # def get_context_data(self, **kwargs) :
    #     context=super().get_context_data(**kwargs) #inherit and adding data from link
    #     print(kwargs)
    #     context=({'name': "Hamin", 'age': 12})
    #     context.update(**kwargs)
    #     return context

# class Bookformview(FormView):
#     template_name='store_book.html'
#     form_class=Bookstoreform
#     context_object_name='data'
#     #success_url='/show_books/'
#     #success_url=reverse_lazy('show_books')
#     def form_valid(self,form):
#         print(form.cleaned_data)
#         form.save()
#         return redirect('show_books')

class Bookformview(CreateView):
    model=BookstoreModel
    template_name='store_book.html'
    form_class=Bookstoreform
    success_url=reverse_lazy('show_books')
    #success_url='/show_books/'
    #success_url=reverse_lazy('show_books')


class Booklistview(ListView):
    model=BookstoreModel
    template_name='show_books.html'
    context_object_name='data' #passing the data
    
    #filtering
    
    
    # def get_queryset(self):
    #     return BookstoreModel.objects.filter(author="Faysal")

    # def get_queryset(self):
    #     return BookstoreModel.objects.filter(id=2)
    
    # def get_queryset(self):
    #     range=[1,5]
    #     # queryset = BookstoreModel.objects.filter(id__in=range)
    #     # print(queryset.query)
    #     # return queryset
    #     return BookstoreModel.objects.filter(id__in=range)
    
    # def get_context_data(self, **kwargs: Any) :
    #     super().get_context_data(**kwargs)
    #     return {'data':BookstoreModel.objects.filter(author="Faysal")}
    
    # def get_context_data(self, **kwargs: Any) :
    #     super().get_context_data(**kwargs)
    #     return {'data':BookstoreModel.objects.order_by('author')}
    
    ordering=['id']
    
        
class BookDetailsView(DetailView):
    model = BookstoreModel
    template_name = "book_details.html"
    context_object_name = 'item'
    pk_url_kwarg = 'id'
  


class Bookupdateview(UpdateView): #UpdateView will do the work of update
    form_class=Bookstoreform
    model=BookstoreModel
    template_name='store_book.html'
    success_url=reverse_lazy('show_books')
    

class Deletebookview(DeleteView):
    model=BookstoreModel
    template_name='delete_confirmation.html'
    success_url=reverse_lazy('show_books')
