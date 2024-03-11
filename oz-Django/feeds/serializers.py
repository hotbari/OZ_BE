## feeds/serializers.py

from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer
from reviews.serializers import ReviewSerializer

# ModelSerializer는 직렬화를 해주는 역할
class FeedSerializer(ModelSerializer):
    # 직렬할 것에 대한 특징
    
    # 여기서 user는 FeedUserSerializer에서 해석해줘
    user = FeedUserSerializer(read_only=True)
    
    # 댓글은 게시글이 작성될 때 변경되면 안되고
    # 한 개의 게시글에 여러개의 댓글이 들어갈 수 있다.
    review_set = ReviewSerializer(read_only=True, many=True)
    
    class Meta:
        model = Feed
        fields = "__all__"
        depth = 1
        