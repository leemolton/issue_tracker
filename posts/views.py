from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.conf import settings
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
    return render(request, "postdetail.html", {'post': post})


def new_post(request):
    template = 'blogpostform.html'
    form = BlogPostForm(request.POST or None)
    
    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post was saved to the database')
    except Exception as e:
        messages.warning(request, 'Blog post was not saved. Error: {}'. format)
        
    else:
        form = BlogPostForm()
        
    context = {
        'form': form,
    }
    return render(request, template, context)
    
    
    
    

    