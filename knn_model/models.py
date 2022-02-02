from django.db import models
from django.contrib.auth.models import User

class History(models.Model):
    id_history = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    hero_name = models.CharField(max_length=200)
    hero_damage = models.IntegerField(null=False)
    turret_damage = models.IntegerField(null=False)
    damage_taken = models.IntegerField(null=False)
    war_participation = models.IntegerField(null=False)
    result = models.CharField(max_length=200)

    def __str__(self):
        return self.hero_name

class Message(models.Model):
    id_message = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.message

class Statistic(models.Model):
    id_statistic = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    winrate = models.IntegerField(null=False)
   
    def __str__(self):
        return self.hero_name