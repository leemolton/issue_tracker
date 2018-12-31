from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from .models import Post, Entry
from .forms import BlogPostForm, EntryForm

# Create your views here.
def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntryForm()
    
    context= {'form' : form}
    
    return render(request, 'add.html', context)
    

def get_posts(request):
    """
    Create a view that will return a
    list of Posts that were published prior to'now'
    and render them to the 'blogposts.html' template
    """
    posts = Post.objects.filter(published_date__lte=timezone.now
    ()).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is 
    not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    entry=Entry.objects.filter(comment=pk)
    return render(request, "postdetail.html", {'post': post},{'entry': entry})


def new_post(request):
    template = 'blogpostform.html'
    form = BlogPostForm(request.POST or None)
    
    try:
        if form.is_valid():
            title = request.POST.get('title', '')
            content = request.POST.get('content', '')
            image = request.POST.get('image', '')
            tag = request.POST.get('tag', '')
            published_date = request.POST.get('published_date', '')
            form.save()
            print(messages.success)
            messages.success(request, 'Blog post was saved to the database')
    except Exception as e:
        messages.warning(request, 'Blog post was not saved. Error: {}'. format(e))
        
    else:
        form = BlogPostForm()
        
    context = {'form': form,}
    return render(request, template, context)
    
    
def edit_post(request, pk=None):
    """
    Create a view that allows us to edit a post
    object depending if the post ID is null or not 
    """
    post = get_object_or_404(Post, pk-pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form' : form})
    
    
    

    