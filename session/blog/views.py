from django.shortcuts import render, get_object_or_404, redirect

from .models import Blog
from .forms import BlogForm
# forms.py에서 BlogForm을 import하겠다!


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})


def new(request):
    return render(request, 'new.html')


# def create(request):
#     new_blog = Blog()
#     new_blog.title = request.POST['title']
#     new_blog.content = request.POST['content']
#     new_blog.save()
#     # return render(request, 'detail.html', {'blog': new_blog})
#     return redirect('detail', new_blog.id)

def create(request):
    form = BlogForm(request.POST)
    if form.is_valid():
        new_blog = form.save(commit=False)
        # form을 save를 활용하여 db에 저장(commit(완료)는 바로 하지 않음)
        new_blog.save()
        return redirect('detail', new_blog.id)

    return render(request, "new.html")


def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    # Blog라는 클래스에서 객체를 가져오는데 그것은 pk=blog_id에 해당한다.
    return render(request, 'edit.html', {'edit_blog': edit_blog})
    # edit_blog라는 이름으로 내가 가져온 객체를 edit.html에 결합시키겠다. (edit.html에서 사용할 수 있도록 하겠다.)


# def update(request, blog_id):
#     old_blog = get_object_or_404(Blog, pk=blog_id)
#     old_blog.title = request.POST["title"]
#     old_blog.content = request.POST["content"]
#     old_blog.save()
#     return redirect('detail', old_blog.id)

def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    # old_blog에 id에 해당하는 객체를 받아줌
    form = BlogForm(request.POST, instance=old_blog)
    # form에 request를 list로 만든 것과 old_blog 인스턴스를 넘겨서 유효성 검사 실행

    # if request.method == "POST":

    if form.is_valid():
        # 유효하다면 save를 활용하여 저장.
        new_blog = form.save(commit=False)
        new_blog.save()
        return redirect("detail", new_blog.id)
        # redirect를 활용하여 detail/id로 경로 변경
    return render(request, 'new.html')
    # 유효하지 않다면 new.html로 이동
    # return render(request, "new.html", {"old_blog": old_blog})


def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    # delete()의 쿼리문을 날려서 해당 데이터 삭제
    return redirect("home")
    # redirect를 활용하여 home이라는 이름을 갖는 url로 이동
    # redirect를 쓰는 이유는 만약 POST 메소드를 날리고 새로고침을 할 때,
    # render를 하면 포스트 요청이 계속 날아가지만, redirect를 사용하면 get요청을 날리는 것이 가능함
    # --> 보안을 위해서 redirect를 사용함.


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched_blogs = Blog.objects.filter(title__contains=searched)
        return render(request, 'searched.html', {'searched': searched, 'searched_blogs': searched_blogs})
    else:
        return render(request, 'searched.html', {})
