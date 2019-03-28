from rest_framework import serializers
from stuapp.models import Actor, Movie


# class ActorSerializer(serializers.ModelSerializer):
#     """演员序列化器"""
#     class Meta:
#         model = Actor
#         fields = '__all__'

class ActorSerializer(serializers.Serializer):
    """演员序列化器"""
    GENDER_ID = (
        ('0', '男'),
        ('1', '女')
    )
    aid = serializers.IntegerField(label='编号', read_only=True)
    aname = serializers.CharField(label='姓名', max_length=30)
    age = serializers.IntegerField(label='年龄', required=False)
    agender = serializers.ChoiceField(choices=GENDER_ID, label='性别', required=False)
    birth_date = serializers.DateField(label='出生年月', required=False)
    photo = serializers.ImageField(label='头像', required=False)
    def create(self, validated_data):
        instance = Actor.objects.create(**validated_data)
        return instance

class MovieSerializer(serializers.Serializer):
    mid = serializers.IntegerField(label='影片编号', read_only=True)
    mname = serializers.CharField(label='影片名称', max_length=30)
    m_pub_date = serializers.DateField(label='上映日期', required=False)
    mread = serializers.IntegerField(label='阅读量')
    mcomment = serializers.CharField(label='评论', max_length=300, required=False, allow_null=True)
    mimage = serializers.ImageField(label='图片', required=False)
    actors = serializers.PrimaryKeyRelatedField(label='演员', queryset=Actor.objects.all())
    # actors = serializers.IntegerField(label='演员')



    def create(self, validated_data):
        instance = Movie.objects.create(**validated_data)
        return instance
