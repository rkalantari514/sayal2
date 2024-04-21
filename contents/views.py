from django.shortcuts import render
from contents.models import About, Team, Projects, ProjectPicture, Services, Articles, ArticlesFile, Customer, Grades
from PIL import Image


# Create your views here.
def home_page(request):
    about = About.objects.filter(active=True).last()
    projects = Projects.objects.filter(active=True).all()
    services=Services.objects.filter(active=True).last()
    team=Team.objects.filter(active=True,super=True ).all()
    articles=Articles.objects.filter(active=True).all()
    customer=Customer.objects.filter(active=True).all()
    grades=Grades.objects.filter(active=True).all()

    #icon from https://icon-sets.iconify.design/heroicons-outline/
    d11 = "M19 21V5a2 2 0 0 0-2-2H7a2 2 0 0 0-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v5m-4 0h4"
    d10="M9.53 16.122a3 3 0 00-5.78 1.128 2.25 2.25 0 01-2.4 2.245 4.5 4.5 0 008.4-2.245c0-.399-.078-.78-.22-1.128zm0 0a15.998 15.998 0 003.388-1.62m-5.043-.025a15.994 15.994 0 011.622-3.395m3.42 3.42a15.995 15.995 0 004.764-4.648l3.876-5.814a1.151 1.151 0 00-1.597-1.597L14.146 6.32a15.996 15.996 0 00-4.649 4.763m3.42 3.42a6.776 6.776 0 00-3.42-3.42"
    d30="M3.75 6A2.25 2.25 0 016 3.75h2.25A2.25 2.25 0 0110.5 6v2.25a2.25 2.25 0 01-2.25 2.25H6a2.25 2.25 0 01-2.25-2.25V6zM3.75 15.75A2.25 2.25 0 016 13.5h2.25a2.25 2.25 0 012.25 2.25V18a2.25 2.25 0 01-2.25 2.25H6A2.25 2.25 0 013.75 18v-2.25zM13.5 6a2.25 2.25 0 012.25-2.25H18A2.25 2.25 0 0120.25 6v2.25A2.25 2.25 0 0118 10.5h-2.25a2.25 2.25 0 01-2.25-2.25V6zM13.5 15.75a2.25 2.25 0 012.25-2.25H18a2.25 2.25 0 012.25 2.25V18A2.25 2.25 0 0118 20.25h-2.25A2.25 2.25 0 0113.5 18v-2.25z"
    d40="M6.429 9.75L2.25 12l4.179 2.25m0-4.5l5.571 3 5.571-3m-11.142 0L2.25 7.5 12 2.25l9.75 5.25-4.179 2.25m0 0L21.75 12l-4.179 2.25m0 0l4.179 2.25L12 21.75 2.25 16.5l4.179-2.25m11.142 0l-5.571 3-5.571-3"


    d1="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2"
    d2 = "M19 7s-5 7-12.5 7c-2 0-5.5 1-5.5 5v4h11v-4c0-2.5 3-1 7-8l-1.5-1.5M3 5V2h20v14h-3M11 1h4v2h-4zM6.5 14a3.5 3.5 0 1 0 0-7a3.5 3.5 0 0 0 0 7Z"

    d3="M1 5c0-2 1-4 2-4l2 4h2l2-4c1 0 2 2 2 4c0 2.254-1 4-3 5v11c0 1 0 2-2 2s-2-1-2-2V10C2 9 1 7.254 1 5Zm18 7v6m-2 0l1 5h2l1-5zm-3-6h10zm7 0V3a2 2 0 1 0-4 0v9"
    d4="M6 9a3 3 0 1 0 0-6a3 3 0 0 0 0 6Zm0-6V0m0 12V9M0 6h3m6 0h3M2 2l2 2m4 4l2 2m0-8L8 4M4 8l-2 2m16 2a3 3 0 1 0 0-6a3 3 0 0 0 0 6Zm0-6V3m0 12v-3m-6-3h3m6 0h3M14 5l2 2m4 4l2 2m0-8l-2 2m-4 4l-2 2m-5 8a3 3 0 1 0 0-6a3 3 0 0 0 0 6Zm0-6v-3m0 12v-3m-6-3h3m6 0h3M5 14l2 2m4 4l2 2m0-8l-2 2m-4 4l-2 2"


    context = {
        'title': 'شرکت مهندسی سیال کار|صفحه اصلی',
        'about': about,
        'projects': projects,
        'services': services,
        'articles': articles,
        'customer': customer,
        'grades': grades,
        'team': team,
        'd1':d1,
        'd2':d2,
        'd3':d3,
        'd4':d4,
    }
    return render(request, 'home_page.html', context)


def about_us(request):
    about = About.objects.filter(active=True).last()
    team = Team.objects.filter(active=True).all()
    grades=Grades.objects.filter(active=True).all()

    context = {
        'title': 'شرکت مهندسی سیال کار|درباره ما',
        'about': about,
        'team': team,
        'grades': grades,
    }
    return render(request, 'about_us.html', context)

def contact_us(request):
    about = About.objects.filter(active=True).last()

    context = {
        'title': 'شرکت مهندسی سیال کار|تماس با ما',
        'about': about,
    }
    return render(request, 'contact-us.html', context)



def projects(request):
    projects=Projects.objects.filter(active=True).all()

    context = {
        'title': 'شرکت مهندسی سیال کار|پروژه ها',
        'projects': projects,
    }
    return render(request, 'projects.html', context)


def project(request, *args, **kwargs):
    prid=kwargs['prid']
    project=Projects.objects.filter(id=prid).first()
    picture=ProjectPicture.objects.filter(project__id=prid).all()
    context = {
        'title': 'شرکت مهندسی سیال کار|پروژه',
        'project': project,
        'picture': picture,

    }

    propic = ProjectPicture.objects.all()
    for p in propic:
        img = Image.open(p.pimage.path)
        width, height = img.size  # Get dimensions
        w = 10240
        h = 6140
        if width / height > w / h:
            w2 = w * height / h
            left = (width - w2) / 2
            right = left + w2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(p.pimage.path)
            p.save()

        if width / height < w / h:
            h2 = h * width / w
            left = 0
            right = width
            top = (height - h2) / 2
            bottom = top + h2
            img = img.crop((left, top, right, bottom))
            img.thumbnail((w, h))
            img.save(p.pimage.path)
            print("p.pimage.path")
            print(p.pimage.path)
            p.save()
        if width / height == w / h:
            img.thumbnail((w, h))
            img.save(p.pimage.path)
            p.save()

    return render(request, 'project.html', context)


def article(request, *args, **kwargs):
    arid=kwargs['arid']
    article=Articles.objects.filter(id=arid).first()
    # picture=ProjectPicture.objects.filter(project__id=prid).all()
    files=ArticlesFile.objects.filter(article__id=arid).all()


    context = {
        'title': 'شرکت مهندسی سیال کار|مقاله',
        'article': article,
        'files': files,
        # 'picture': picture,

    }
    return render(request, 'article.html', context)


def articles(request):
    article=Articles.objects.filter(active=True).all()

    context = {
        'title': 'شرکت مهندسی سیال کار|مقالات',
        'article': article,
    }
    return render(request, 'articles.html', context)


