from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Team, Member
from .forms import TeamRegistrationForm

#
# def register_team(request):
#     if request.method == 'POST':
#         form = TeamRegistrationForm(request.POST)
#         members = []
#         count = int(request.POST.get('member_count', 0))
#
#         for i in range(count):
#             fname = request.POST.get(f'first_name_{i}', '')
#             lname = request.POST.get(f'last_name_{i}', '')
#             grade = request.POST.get(f'grade_{i}', '')
#             classroom = request.POST.get(f'classroom_{i}', '')
#             if fname and lname and grade and classroom:
#                 members.append({'first_name': fname, 'last_name': lname, 'grade': grade, 'classroom': classroom})
#
#         team_name = request.POST.get('team_name', '').strip()
#         form.initial['team_name'] = team_name  # نگه داشتن نام تیم در فرم
#
#         if form.is_valid():
#             # بررسی تکراری بودن نام تیم
#             if Team.objects.filter(name__iexact=team_name).exists():
#                 messages.error(request, f"تیم '{team_name}' قبلاً ثبت شده است.")
#                 return render(request, 'team_register.html', {'form': form, 'members': members})
#
#             if len(members) < 3 or len(members) > 5:
#                 messages.error(request, 'تعداد اعضای تیم باید بین ۳ تا ۵ نفر باشد.')
#                 return render(request, 'team_register.html', {'form': form, 'members': members})
#
#             # بررسی اعضای تکراری
#             duplicates = []
#             for m in members:
#                 if Member.objects.filter(first_name=m['first_name'], last_name=m['last_name'],
#                                          grade=m['grade'], classroom=m['classroom']).exists():
#                     duplicates.append(f"{m['first_name']} {m['last_name']} ({m['classroom']})")
#             if duplicates:
#                 messages.error(request, f"اعضای زیر قبلاً در تیم دیگری ثبت شده‌اند: {', '.join(duplicates)}")
#                 return render(request, 'team_register.html', {'form': form, 'members': members})
#
#             # ثبت تیم
#             team = Team.objects.create(name=team_name)
#             for m in members:
#                 Member.objects.create(
#                     team=team,
#                     first_name=m['first_name'],
#                     last_name=m['last_name'],
#                     grade=m['grade'],
#                     classroom=m['classroom']
#                 )
#             return render(request, 'team_success.html', {'team': team})
#
#         else:
#             messages.error(request, 'فرم نامعتبر است.')
#             return render(request, 'team_register.html', {'form': form, 'members': members})
#
#     else:
#         form = TeamRegistrationForm()
#         members = [{'first_name': '', 'last_name': '', 'grade': '', 'classroom': ''}]  # حداقل یک عضو اولیه
#
#     return render(request, 'team_register.html', {'form': form, 'members': members})
# from django.shortcuts import render
# from .models import Team

def teams_view(request):
    teams = Team.objects.prefetch_related('members').all()
    return render(request, 'teams.html', {'teams': teams})
