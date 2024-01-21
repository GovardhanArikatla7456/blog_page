from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
list_posts = [
    {
        "slug": "graduate-degree",
        "image": "Grad.jpg",
        "author": "Govardhan",
        "date": date(2023,12, 21),
        "title": "Graduate degree",
        "excerpt": "I have recently completed my masters and obtained Graduate degree from SUNY Buffalo.",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "udemy",
        "image": "coding.png",
        "author": "Govardhan",
        "date": date(2024, 1, 18),
        "title": "Backend development with python.",
        "excerpt": "I am currently working on django projects.",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "projects",
        "image": "projects.jpeg",
        "author": "Govardhan",
        "date": date(2024, 1, 19),
        "title": "Projects I have worked on.",
        "excerpt": "These are projects that I have contributed and learnt many skills.",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
]
def get_date(post):
    return post['date']
def intial_page(request):
    sorted_posts = sorted(list_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {"posts": latest_posts})
def all_posts(request):
    return render(request,'blog/posts.html', {"posts": list_posts})
def post_page(request, slug):
    id_post =next( post for post in list_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {"post":id_post})

