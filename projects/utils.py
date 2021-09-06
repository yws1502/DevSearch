from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .models import Project, Tag


def paginate_projects(request, projects, results):
    page = request.GET.get('page')
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # page가 없으면
        page = 1 # 처음으로
        projects = paginator.page(page)
    except EmptyPage:
        # page가 해당 page보다 더 많으면
        page = paginator.num_pages # 마지막으로
        projects = paginator.page(page)

    # 페이지 시작 칸 정의!
    left_idx = (int(page) - 4)
    if left_idx < 1:
        left_idx = 1
    
    # 페이지 끝 칸 정의
    right_idx = (int(page) + 5)
    if right_idx > paginator.num_pages + 1:
        right_idx = paginator.num_pages + 1

    custom_range = range(left_idx, right_idx)
    return custom_range, projects

def search_project(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )
    return search_query, projects