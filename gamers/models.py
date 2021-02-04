from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122,default=0)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
class Game(models.Model):
    gname=models.CharField(max_length=122)
    waiting_list=models.IntegerField(default=0)
    image=models.ImageField(upload_to='imageforgames/',default=0)

    def __str__(self):
        return self.gname
    @staticmethod
    def get_all_games():
        return Game.objects.all()
    @staticmethod
    def get_game(ids):
        return Game.objects.filter(id=ids)
    @staticmethod
    def get_wl(ggid):
        return Game.objects.get(id=ggid).waiting_list


class Matchpt(models.Model):
    game=models.ForeignKey(Game,on_delete=models.CASCADE)
    name=models.CharField(max_length=122)
    gameid=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    #opt11=models.IntegerField(default=0)
    option=models.IntegerField(default=0)
    def __str__(self):
        return self.name
    @staticmethod
    def return_acc(n):
        try:
             return Matchpt.objects.get(name=n)
        except:
             return False



