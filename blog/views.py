from django.shortcuts import render
# Create your views here.
posts = [
    {
        "author" : "Vaibhav Khanna",
        "title" : "Post 1",
        "content" : "Content of 1st post",
        "date_posted" : "27th Sept, 2021"
    },
    {
        "author" : "Jake Peralta",
        "title" : "Post 2",
        "content" : "Content of 2nd post",
        "date_posted" : "27th Sept, 2021"
    }
]
def home(request):
    context={
        "posts" : posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {"title" : "About"})