from django.db import models
# from challenge_info.models import ChallengeInfo

class ChallengeSpoiler(models.Model):
    day = models.CharField(max_length=1)
    title = models.CharField(max_length=255)
    content = models.TextField()

    # challenge_info_id = models.ForeignKey(ChallngeInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title