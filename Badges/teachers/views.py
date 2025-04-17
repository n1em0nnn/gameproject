from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from teachers.models import Teacher, ChildProfile
from .forms import TeacherProfileForm, ChildProfileForm

@login_required
def profile_view(request):
    user = request.user

    # Проверяем роль пользователя
    if hasattr(user, 'teacher'):
        # Профиль преподавателя
        teacher = user.teacher
        if request.method == 'POST':
            form = TeacherProfileForm(request.POST, instance=teacher)
            if form.is_valid():
                form.save()
                return redirect('profile_view')
        else:
            form = TeacherProfileForm(instance=teacher)
        return render(request, 'profile_teachild/teacher_profile.html', {'form': form})

    elif hasattr(user, 'childprofile'):
        # Профиль ученика (только просмотр)
        child = user.childprofile
        return render(request, 'profile_teachild/child_profile.html', {'child': child})

    else:
        # Если пользователь не является ни преподавателем, ни учеником
        return render(request, 'profile_teachild/no_profile.html')

@login_required
def edit_child_profile(request, child_id):
    child = get_object_or_404(ChildProfile, id=child_id)
    user = request.user

    # Проверка прав доступа
    if not (user.is_staff or (hasattr(user, 'teacher') and child.teacher == user.teacher)):
        return render(request, 'profile_teachild/access_denied.html')

    if request.method == 'POST':
        form = ChildProfileForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ChildProfileForm(instance=child)

    return render(request, 'profile_teachild/edit_child_profile.html', {'form': form})