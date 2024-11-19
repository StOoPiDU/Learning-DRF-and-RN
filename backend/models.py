from django.db import models

class FGFPost(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  thumbnail = models.CharField(max_length=255, blank=True, null=True)
  post_flair = models.CharField(max_length=255, blank=True, null=True)
  reddit_id = models.CharField(max_length=30)
  direct_link = models.CharField(max_length=255, blank=True, null=True)
  nsfw = models.BooleanField(default=False)
  date_posted = models.DateTimeField(auto_now_add=True) #temp, this would come from reddit)

  def __str__(self):
      return self.title