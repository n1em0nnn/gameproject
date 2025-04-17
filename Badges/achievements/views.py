from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Achievement, ChildAchievement
from .forms import AchievementForm
from teachers.models import Teacher, ChildProfile

@login_required
def achievement_list(request):
    achievements = Achievement.objects.all()
    user = request.user

    if hasattr(user, 'teacher'):
        # Преподаватель видит все достижения с возможностью редактирования
        return render(request, 'achievements/achievement_list.html', {'achievements': achievements})

    elif hasattr(user, 'childprofile'):
        # Ученик видит свои достижения с проверкой статуса
        child = user.childprofile
        child_achievements = ChildAchievement.objects.filter(child=child)
        return render(request, 'achievements/child_achievement_list.html', {
            'achievements': achievements,
            'child_achievements': child_achievements,
        })

    else:
        return render(request, 'achievements/no_access.html')

@login_required
def achievement_detail(request, achievement_id):
    achievement = get_object_or_404(Achievement, id=achievement_id)
    user = request.user

    if hasattr(user, 'teacher'):
        # Преподаватель может редактировать достижение
        if request.method == 'POST':
            form = AchievementForm(request.POST, request.FILES, instance=achievement)
            if form.is_valid():
                form.save()
                return redirect('achievement_list')
        else:
            form = AchievementForm(instance=achievement)
        return render(request, 'achievements/achievement_detail.html', {'form': form, 'achievement': achievement})

    elif hasattr(user, 'childprofile'):
        # Ученик видит детали достижения
        child = user.childprofile
        child_achievement = ChildAchievement.objects.filter(child=child, achievement=achievement).first()

        if child_achievement and child_achievement.unlocked:
            # Если достижение разблокировано
            return render(request, 'achievements/unlocked_achievement.html', {
                'achievement': achievement,
                'unlock_date': child_achievement.unlock_date,
            })
        else:
            # Если достижение заблокировано
            return render(request, 'achievements/locked_achievement.html', {
                'achievement': achievement,
            })

    else:
        return render(request, 'achievements/no_access.html')