from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Team(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    teamName = models.CharField(max_length=200, null=True)
    captain = models.CharField(max_length=200, null=True)
    viceCap = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True, blank=True)
    dateCreated = models.DateField(auto_now_add=True, null=True)
    locality = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    # team_pic = models.ImageField(null=True blank=True)

    def __str__(self):
        return str(self.teamName)


class Player(models.Model):
    ROLE = (
        ('Batsman', 'Batsman'),
        ('Bowler', 'Bowler'),
        ('All Rounder', 'All Rounder'),
        ('Wicket Keeper', 'Wicket Keeper'),
        ('Umpire', 'Umpire'),
    )
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    role = models.CharField(max_length=200, null=True, choices=ROLE)
    age = models.IntegerField(null=True, blank=True)
    is_cap = models.BooleanField(default=False)
    is_vcap = models.BooleanField(default=False)
    # player_pic = models.ImageField(null=True blank=True)

    def __str__(self):
        return self.name


class Match(models.Model):
    STATUS = (
        ('Running', 'Running'),
        ('Finished', 'Finished'),
        ('Pending', 'Pending'),
        ('Canceled', 'Canceled'),
        ('Upcoming', 'Upcoming'),
    )
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    team2Name = models.CharField(max_length=200, null=True)
    team1Score = models.CharField(max_length=200, null=True, blank=True)
    team2Score = models.CharField(max_length=200, null=True, blank=True)
    tournament = models.CharField(max_length=200, null=True, blank=True)
    win = models.BooleanField(null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default='Upcoming')
    mom = models.CharField(max_length=200, null=True, blank=True)
    matchDate = models.DateField(null=True)
    matchTime = models.TimeField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.team)


class TeamMatches(models.Model):
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    totalMatches = models.IntegerField(null=True, blank=True)
    wins = models.IntegerField(null=True, blank=True)
    lost = models.IntegerField(null=True, blank=True)
    noResult = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.team)


class ScoreCard(models.Model):
    CHOICES = (
        ('Out', 'Out',),
        ('Not Out', 'Not Out'),
    )
    team = models.CharField(null=True, max_length=100)
    match = models.ForeignKey(Match, null=True, on_delete=models.SET_NULL)
    batsmanName = models.CharField(null=True, max_length=100)
    batsmanRun = models.IntegerField(null=True, blank=True)
    batsmanFours = models.IntegerField(null=True, blank=True)
    batsmanSix = models.IntegerField(null=True, blank=True)
    batsmanBalls = models.IntegerField(null=True, blank=True)
    batsmanStrikeRate = models.FloatField(null=True, blank=True)
    batsmanStatus = models.CharField(max_length=100, null=True, choices=CHOICES)
    bowlerName = models.CharField(null=True, blank=True, max_length=100)
    bowlerRun = models.IntegerField(null=True, blank=True)
    bowlerMaidenOver = models.IntegerField(null=True, blank=True)
    bowlerOvers = models.FloatField(null=True, blank=True)
    bowlerEconomy = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.match)


"""class ScoreCard2(models.Model):
    team = models.CharField(null=True, max_length=100)
    match = models.ForeignKey(Match, null=True, on_delete=models.SET_NULL)
    player1 = models.IntegerField(null=True, blank=True)
    player1Name = models.CharField(null=True, blank=True)
    player1Run = models.IntegerField(null=True, blank=True)
    player1Fours = models.IntegerField(null=True, blank=True)
    player1Six = models.IntegerField(null=True, blank=True)
    player1Balls = models.IntegerField(null=True, blank=True)
    player1StrikeRate = models.FloatField(null=True, blank=True)

    player2 = models.IntegerField(null=True, blank=True)
    player2Name = models.CharField(null=True, blank=True)
    player2Run = models.IntegerField(null=True, blank=True)
    player2Fours = models.IntegerField(null=True, blank=True)
    player2Six = models.IntegerField(null=True, blank=True)
    player2Balls = models.IntegerField(null=True, blank=True)
    player2StrikeRate = models.FloatField(null=True, blank=True)

    player3 = models.IntegerField(null=True, blank=True)
    player3Name = models.CharField(null=True, blank=True)
    player3Run = models.IntegerField(null=True, blank=True)
    player3Fours = models.IntegerField(null=True, blank=True)
    player3Six = models.IntegerField(null=True, blank=True)
    player3Balls = models.IntegerField(null=True, blank=True)
    player3StrikeRate = models.FloatField(null=True, blank=True)

    player4 = models.IntegerField(null=True, blank=True)
    player4Name = models.CharField(null=True, blank=True)
    player4Run = models.IntegerField(null=True, blank=True)
    player4Fours = models.IntegerField(null=True, blank=True)
    player4Six = models.IntegerField(null=True, blank=True)
    player4Balls = models.IntegerField(null=True, blank=True)
    player4StrikeRate = models.FloatField(null=True, blank=True)

    player5 = models.IntegerField(null=True, blank=True)
    player5Name = models.CharField(null=True, blank=True)
    player5Run = models.IntegerField(null=True, blank=True)
    player5Fours = models.IntegerField(null=True, blank=True)
    player5Six = models.IntegerField(null=True, blank=True)
    player5Balls = models.IntegerField(null=True, blank=True)
    player5StrikeRate = models.FloatField(null=True, blank=True)

    player6 = models.IntegerField(null=True, blank=True)
    player6Name = models.CharField(null=True, blank=True)
    player6Run = models.IntegerField(null=True, blank=True)
    player6Fours = models.IntegerField(null=True, blank=True)
    player6Six = models.IntegerField(null=True, blank=True)
    player6Balls = models.IntegerField(null=True, blank=True)
    player6StrikeRate = models.FloatField(null=True, blank=True)

    player7 = models.IntegerField(null=True, blank=True)
    player7Name = models.CharField(null=True, blank=True)
    player7Run = models.IntegerField(null=True, blank=True)
    player7Fours = models.IntegerField(null=True, blank=True)
    player7Six = models.IntegerField(null=True, blank=True)
    player7Balls = models.IntegerField(null=True, blank=True)
    player7StrikeRate = models.FloatField(null=True, blank=True)

    player8 = models.IntegerField(null=True, blank=True)
    player8Name = models.CharField(null=True, blank=True)
    player8Run = models.IntegerField(null=True, blank=True)
    player8Fours = models.IntegerField(null=True, blank=True)
    player8Six = models.IntegerField(null=True, blank=True)
    player8Balls = models.IntegerField(null=True, blank=True)
    player8StrikeRate = models.FloatField(null=True, blank=True)

    player9 = models.IntegerField(null=True, blank=True)
    player9Name = models.CharField(null=True, blank=True)
    player9Run = models.IntegerField(null=True, blank=True)
    player9Fours = models.IntegerField(null=True, blank=True)
    player9Six = models.IntegerField(null=True, blank=True)
    player9Balls = models.IntegerField(null=True, blank=True)
    player9StrikeRate = models.FloatField(null=True, blank=True)

    player10 = models.IntegerField(null=True, blank=True)
    player10Name = models.CharField(null=True, blank=True)
    player10Run = models.IntegerField(null=True, blank=True)
    player10Fours = models.IntegerField(null=True, blank=True)
    player10Six = models.IntegerField(null=True, blank=True)
    player10Balls = models.IntegerField(null=True, blank=True)
    player10StrikeRate = models.FloatField(null=True, blank=True)

    player11 = models.IntegerField(null=True, blank=True)
    player11Name = models.CharField(null=True, blank=True)
    player11Run = models.IntegerField(null=True, blank=True)
    player11Fours = models.IntegerField(null=True, blank=True)
    player11Six = models.IntegerField(null=True, blank=True)
    player11Balls = models.IntegerField(null=True, blank=True)
    player11StrikeRate = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return str(self.match)"""
