from django.db.models import manager
from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)
    reviews = serializers.SerializerMethodField()
    # 원하는 형식으로 조회하고 싶은 경우 `SerializerMethodField`를 사용
    #   사용자 정의 함수를 클래스 내에 정의한다.
    # 조회하는 클래스와 상관관계가 없는 

    class Meta:
        model = Project
        fields = '__all__'
    
    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data