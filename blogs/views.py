from django.shortcuts import render
from . models import Articls
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect , HttpResponseNotFound

from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.


def homePageView(request):
    return render(request, 'home.html')

def ArticlsView(request):


    articls = Articls.objects.all()
    
    context = {
        "articls" : articls
    }

    return render(request,"articls.html",context=context)

def CreateArticls(request):

    if request.user.is_authenticated == False:
        return  HttpResponseNotFound("hello")    

    template_name = 'new_article.html'

    return render(request, template_name, {})


class CreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'new_article.html'
    model = Articls
    fields = ('title','contents')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser

# def add(request):

#     if request.user.is_authenticated == False:
#         return  HttpResponseNotFound("hello")    

#     title = request.POST['title']
#     content = request.POST['content']
#     author = request.session['_auth_user_id']
#     model = Articls(
#         title,
#         content,
#         author
#     )
    
#     model.save()
#     id = model.id
#     try:
#         return HttpResponseRedirect(reverse('content_article', kwargs={'id' : id}))
#     except:
#         return HttpResponseRedirect(reverse('articls'))

def UpdateView(request, id):
    pass

def ContentView(request, id):
    model = Articls.objects.get(id=id)
    if request.user.is_authenticated == False:
        return  HttpResponseNotFound("hello")    
    
    context = {
        'article': model
    }
    template_name = 'content_view.html'
    return render(request=request, template_name=template_name, context=context)

def DeleteArticle(request, id):
    article = Articls.objects.get(id=id)
    auth_user = request.session['_auth_user_id']

    if request.user.is_authenticated == False:
        return  HttpResponseNotFound("hello")    
    
    try:
        if article.author.id == int(auth_user) or request.user.is_superuser:
            article.delete()
    except:
        pass
    return redirect('articls')


    