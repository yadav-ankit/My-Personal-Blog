

# Create your views here.
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib import  messages
from django.shortcuts import render ,get_object_or_404,Http404
from .models import Post
from django.shortcuts import redirect
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def post_create(request):
    form = PostForm(request.POST or None,request.FILES or None)
    if not request.user.is_authenticated():
        raise Http404

    if form.is_valid():
            instance = form.save(commit=False)
            instance.user  = request.user
            instance.save()
            #messages.success(request, "Item created")
            return redirect("posts:list")

    context ={
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_update(request,id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,request.FILES or None,instance =instance)
    if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            #messages.success(request,"Item Saved")
            return redirect("posts:list")
    context = {
        "title": instance.title,
        "instance": instance,
        "form":form,
    }
    return render(request, "post_form.html", context)


def post_detail(request,id=None):
    instance = get_object_or_404(Post,id=id)
    context = {
        "instance": instance,
        "title": instance.title,
    }
    return render(request,"post_detail.html",context)

def post_delete(request,id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    #messages.success(request,"messsage succesfully deleted")
    return redirect("posts:list")




def post_list(request):
    queryset_list = Post.objects.all().order_by("-timestamp")

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(title__icontains=query)

    paginator = Paginator(queryset_list, 6)  # Show 25 contacts per page


    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context ={
        "obj_list":queryset,
        "title" : "List",
              }
    return render(request,"post_list.html",context)




