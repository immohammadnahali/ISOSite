from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def article(request):
    return render(request,'article.html')
def blog(request):
    return render(request,'blog.html')
def category(request):
    return render(request,'category.html')
def contact_us(request):
    return render(request,'contact_us.html')
def course(request):
    return render(request,'course.html')
def forget_password(request):
    return render(request,'forget_password.html')
def login(request):
    return render(request,'login.html')
def panel_user(request):
    return render(request,'panel_user.html')
def sign_up(request):
    return render(request,'sign_up.html')
def search(request):
    return render(request,'search.html')
def teach(request):
    return render(request,'teach.html')
def error_404(request, exception=None):
    return render(request, 'error404.html', status=404)