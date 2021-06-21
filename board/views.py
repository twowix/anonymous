from django.core import paginator
from django.shortcuts import render
from board.models import Post
from django.core.paginator import Paginator

# Create your views here.
def board(request):
    if request.method=="GET":
        page = request.GET.get('page')
        
        post_set = Post.objects.all()
        paginator = Paginator(post_set, 1)
        post_set = paginator.get_page(page)
        context = {
            'post_set':post_set,
        }
        return render(request, 'page/board/board.html', context)