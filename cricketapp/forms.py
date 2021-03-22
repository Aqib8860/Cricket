from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserLogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class CreateTeamForm(ModelForm):
    class Meta:
        model = Team
        # fields = ['teamName', 'captain', 'viceCap', 'phone', 'email', 'locality', 'city', ]
        fields = '__all__'
        exclude = ['user']


class AddPlayer(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        exclude = ['team']


class AddMatchForm(ModelForm):
    team2Name = forms.CharField(label='Vs')
    tournament = forms.CharField(label='Tournament Name')
    matchDate = forms.DateField(widget=forms.DateInput())
    matchTime = forms.TimeField()

    class Meta:
        model = Match
        fields = ['tournament', 'team2Name', 'matchDate', 'matchTime']


class AddBatsmanForm(ModelForm):
    class Meta:
        model = ScoreCard
        fields = ['batsmanName']


class AddRecentMatchScorcard(ModelForm):
    class Meta:
        model = ScoreCard
        fields = '__all__'


class AddRecentMatchForm(ModelForm):
    class Meta:
        model = Match
        fields = '__all__'


class AddTeamBatsmanForm(ModelForm):
    batsmanName = forms.CharField(label='Batsman Name')
    batsmanRun = forms.CharField(label='Runs')
    batsmanBalls = forms.CharField(label='Balls')
    batsmanStatus = forms.CharField(label='Status')

    class Meta:
        model = ScoreCard
        fields = ['batsmanName', 'batsmanRun', 'batsmanBalls', 'batsmanStatus']
