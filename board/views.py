from django.shortcuts import render, redirect
from board.models import Post, Comment
from django.core.paginator import Paginator
from django.core.files.storage import default_storage
from datetime import datetime
from django.conf import settings



def board(request):
    # 게시글 리스트
    if request.method == "GET":
        page = int(request.GET.get('page', 1))

        post_set = Post.objects.all().order_by('-id')
        paginator = Paginator(post_set, 6)
        post_set = paginator.get_page(page)
        context = {
            'post_set': post_set,
        }
        return render(request, 'page/board/board.html', context)


def post_write(request):
    if request.method == "GET":
        return render(request, 'page/board/post_write.html')

    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        img = request.FILES.get('img', None)
        img_path = None
        if img:
            img_path = f"{datetime.now().strftime('%Y%m%d%H%M%S')}.{str(img.name).split('.')[-1]}"
            default_storage.save(img_path, img)
        Post(
            user_id=request.user.id,
            title=title,
            content=content,
            img_url=img_path
        ).save()
        return redirect('board')


def post_detail(request, post_id):
    # 게시글 상세보기
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        context = {
            'post': post,
        }
        return render(request, 'page/board/post_detail.html', context)

    # 댓글 쓰기
    if request.method == "POST":
        content = request.POST['content']
        Comment(
            post_id=post_id,
            content=content,
        ).save()
        return redirect('post_detail', post_id)
