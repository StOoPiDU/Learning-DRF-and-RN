from rest_framework import serializers
from .models import FGFPost

class FGFPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FGFPost
        fields = [
        'id',
        'title',
        'author',
        'thumbnail',
        'post_flair',
        'reddit_id',
        'direct_link',
        'nsfw',
        'date_posted'
        ]

    # def validate_something(self, value):
    #   pass

class FGFPostInfoSerializer(serializers.Serializer):
    fgfposts = FGFPostSerializer(many=True)
    count = serializers.IntegerField()