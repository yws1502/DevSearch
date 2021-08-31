from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .models import Skill, Profile

def paginator_profile(request, profiles, results):
    page = request.GET.get('page')
    paginator = Paginator(profiles, results)

    # 터무니없는 친구 검문소
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    left_idx = (int(page) - 4)
    if left_idx < 1:
        left_idx = 1
    
    right_idx = (int(page) + 5)
    if right_idx > paginator.num_pages + 1:
        right_idx = paginator.num_pages + 1
    
    custom_range = range(left_idx, right_idx)
    return custom_range, profiles


def search_profile(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills)
    )

    return profiles, search_query