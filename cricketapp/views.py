from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.forms import formset_factory

# Create your views here.


def home(request):
    players = Player.objects.all()
    teams = Team.objects.all()
    upcoming_match = Match.objects.filter(status='Upcoming').order_by('matchDate')
    completed_match = Match.objects.filter(status='Finished').order_by('-matchDate')
    # players = Player.objects.filter(teams__id__in=teams.all())
    context = {
        'players': players,
        'teams': teams,
        'upcoming_match': upcoming_match,
        'completed_match': completed_match,
    }
    return render(request, 'cricketapp/home.html', context)


def register_team(request):
    step1 = True
    form = UserRegisterForm
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('cricket_app:create-team')
            # return render(request, 'cricketapp/register_team.html')
    context = {
        'form': form,
        'step1': step1,
    }
    return render(request, 'cricketapp/register_team.html', context)


def create_team(request):
    step1 = False
    step2 = True
    user = request.user
    form = CreateTeamForm
    if request.method == 'POST':
        form = CreateTeamForm(request.POST)
        if form.is_valid():
            form.save()
            teamName = form.cleaned_data.get('teamName')
            messages.success(request, 'Successfully created team ' + teamName)
            return redirect('cricket_app:add-player')
    context = {
        'step1': step1,
        'step2': step2,
        'form': form,
        'user': user,
    }
    return render(request, 'cricketapp/register_team.html', context)


def add_players(request):
    step1 = False
    step2 = False
    step3 = True
    form = AddPlayer
    if request.method == 'POST':
        form = AddPlayer(request.POST)
        if form.is_valid:
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, 'Successfully Add Player ' + name)
            return redirect('cricket_app:add-player')
    context = {
        'step1': step1,
        'step2': step2,
        'step3': step3,
        'form': form,
    }
    return render(request, 'cricketapp/register_team.html', context)


def userRegister(request):
    form = UserRegisterForm
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('cricket_app:user-login')
            # return render(request, 'cricketapp/register_team.html')
    return render(request, 'cricketapp/userRegister.html', {'form': form})


def userLogin(request):
    form = UserLogin
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cricket_app:home')
        else:
            messages.info(request, 'Username OR Password is Incorrect')
    return render(request, 'cricketapp/login.html', {'form': form})


def userLogout(request):
    logout(request)
    return redirect('cricket_app:user-login')


def createTeam(request):
    form = CreateTeamForm
    if request.method == 'POST':
        form = CreateTeamForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            # teamName = form.cleaned_data.get('teamName')
            form.user = request.user
            form.save()

            # messages.success(request, 'Successfully created team ' + teamName)
            return redirect('cricket_app:my-team')

    return render(request, 'cricketapp/myTeam.html', {'form': form})


def myTeam(request):
    # team = get_object_or_404(Team, pk=user_id)
    match = request.user.team.match_set.all()
    team = Team.objects.filter(user=request.user)
    form = CreateTeamForm
    context = {
        'match': match,
        'form': form,
        'team': team,
    }

    return render(request, 'cricketapp/myTeam.html', context)


def teamPlayers(request):
    team = Team.objects.filter(user=request.user)
    players = Player.objects.filter(team__id__in=team.all())

    form = AddPlayer
    context = {
        'form': form,
        'players': players,
    }
    return render(request, 'cricketapp/TeamPlayers.html', context)


def addPlayer(request):
    if request.method == 'POST':
        form = AddPlayer(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            team = Team.objects.get(user=request.user)
            form = form.save(commit=False)
            form.team = team
            form.save()
            messages.success(request, 'Successfully Add Player ' + name)
            return redirect('cricket_app:team-players')


def teamMatches(request):
    form = AddMatchForm
    match = request.user.team.match_set.all()
    upcoming_match = match.filter(status='Upcoming').order_by('matchDate')
    completed_match = match.filter(status='Finished').order_by('-matchDate')
    context = {
        'form': form,
        'match': match,
        'upcoming_match': upcoming_match,
        'completed_match': completed_match,
    }
    return render(request, 'cricketapp/TeamMatches.html', context)


def addUpcomingMatch(request):
    if request.method == 'POST':
        form = AddMatchForm(request.POST)
        if form.is_valid():
            team = Team.objects.get(user=request.user)

            form = form.save(commit=False)
            form.team = team
            form.status = 'Upcoming'
            form.save()
            return redirect('cricket_app:team-matches')


def startMatch(request, pk):
    # AddBattingScoreFormSet = formset_factory(AddBattingScoreForm, max_num=11, extra=11)
    # formset = AddBattingScoreFormSet()
    # match = request.user.team.match_set.all()
    match = get_object_or_404(Match, pk=pk)
    # score = ScoreCard.objects.filter(match__id__in=match.all())
    score = match.scorecard_set.all()
    form = AddBatsmanForm
    context = {
        'form': form,
        'score': score,
        'match': match,
    }
    return render(request, 'cricketapp/StartMatch.html', context)


def addBatsman(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == 'POST':
        form = AddBatsmanForm(request.POST)
        if form.is_valid():
            team = Team.objects.get(user=request.user)
            # match = request.user.team.match_set.all()
            form = form.save(commit=False)
            form.match = match
            form.team = team
            # form.match = match
            form.save()
            return redirect(reverse('cricket_app:start-match', args=(match.id,)))


def add1(request, pk):

    # match = Match.objects.get(id=pk)
    # score = match.scorecard_set.all()
    # score.objects.update(batsmanRun=1)
    scorecard = get_object_or_404(ScoreCard, pk=pk)

    sc = ScoreCard.objects.filter(id=pk).update(batsmanRun=1)
    match = get_object_or_404(Match, pk=pk)
    return redirect(reverse('cricket_app:start-match', args=(match.id,)))
    # return redirect('cricket_app:start-match')


def addRecentMatch(request):
    form = AddMatchForm
    if request.method == 'POST':
        form = AddMatchForm(request.POST)
        if form.is_valid():
            team = Team.objects.get(user=request.user)
            form = form.save(commit=False)
            form.team = team
            form.status = 'Finished'
            form.save()

            match_id = Match.objects.filter(id=form.id)
            form = AddTeamBatsmanForm
            context = {
                'form': form,
                'match_id': match_id,
            }
            # return redirect('cricket_app:add-recent-match')
            return render(request, 'cricketapp/AddScoreCard.html', context)
    return render(request, 'cricketapp/AddRecentMatch.html', {'form': form})


def addScoreCard(request, pk):
    match = get_object_or_404(Match, pk=pk)
    form = AddTeamBatsmanForm
    if request.method == 'POST':
        form = AddBatsmanForm(request.POST)
        if form.is_valid():
            team = Team.objects.get(user=request.user)
            # match = request.user.team.match_set.all()
            form = form.save(commit=False)
            form.match = match
            form.team = team
            # form.match = match
            form.save()
            form = AddTeamBatsmanForm
            score = match.scorecard_set.all()
            return render(request, 'cricketapp/AddScoreCard.html', {'form': form, 'score': score})
    return render(request, 'cricketapp/AddScoreCard.html', {'form': form})
