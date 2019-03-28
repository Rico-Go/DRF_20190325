# from django.http import JsonResponse, HttpResponse
# from django.shortcuts import render
#
# # Create your views here.
# from django.views import View
# from jsonpickle import json
#
# from stuapp.models import Actor
#
#
# class ActorListView(View):
#     """
#     查询所有演员信息、增加演员信息
#     """
#     def get(self, request):
#         """
#         查询所有演员
#         路由：GET/actors/
#         :param request:
#         :return:
#         """
#         queryset = Actor.objects.all()
#         actor_list = []
#
#         for actor in queryset:
#             actor_list.append({
#                 'aid': actor.aid,
#                 'aname': actor.aname,
#                 'age': actor.age,
#                 'agender': actor.agender,
#                 'birth_date': actor.birth_date,
#                 'photo': actor.photo.url if actor.photo else ''
#
#             })
#         return JsonResponse(actor_list, safe=False)
#
#     def post(self, request):
#         """
#         新增演员信息
#
#         路由： POST/actors/
#         :param request:
#         :return:
#         """
#
#         json_bytes = request.body
#         json_str = json_bytes.decode()
#         actor_dict = json.loads(json_str)
#
#         print(actor_dict)
#
#         # 此处详细的校验参数省略
#
#         actor = Actor.objects.create(
#             aname=actor_dict.get('aname'),
#             age=actor_dict.get('age'),
#             agender=actor_dict.get('agender'),
#             birth_date=actor_dict.get('birth_date')
#         )
#
#         return JsonResponse({
#             'aid': actor.aid,
#             'aname': actor.aname,
#             'age': actor.age,
#             'agender': actor.agender,
#             'birth_date': actor.birth_date,
#             'photo': actor.photo.url if actor.photo else ''
#
#         }, status=201)
#
#
# class ActorDetailView(View):
#     def get(self, request, pk):
#
#         """
#         查询单个演员信息
#         路由  GET  /actors/<pk>/
#         :param request:
#         :param pk:
#         :return:
#         """
#         print(pk)
#         try:
#             actor = Actor.objects.get(aid=pk)
#         except Actor.DoesNotExist:
#             return HttpResponse(status=404)
#
#         return JsonResponse({
#             'aid': actor.aid,
#             'aname': actor.aname,
#             'age': actor.age,
#             'agender': actor.agender,
#             'birth_date': actor.birth_date,
#             'photo': actor.photo.url if actor.photo else ''
#
#         })
#
#     def put(self, request, pk):
#         print(pk, '===========12')
#         """
#         修改单个演员信息
#         路由  PUT  /actors/<pk>/
#         :param request:
#         :param pk:
#         :return:
#         """
#         try:
#             actor = Actor.objects.get(aid=pk)
#         except Actor.DoesNotExist:
#             return HttpResponse(status=404)
#
#         actor_dict = json.loads(request.body)
#
#         # 此处详细的校验参数省略
#
#         actor.aname = actor_dict.get('aname', '')
#         actor.age = actor_dict.get('age', '')
#         actor.save()
#
#         return JsonResponse({
#             'aid': actor.aid,
#             'aname': actor.aname,
#             'age': actor.age,
#             'agender': actor.agender,
#             'birth_date': actor.birth_date,
#             'photo': actor.photo.url if actor.photo else ''
#
#         })
#
#     def delete(self, request, pk):
#         """
#         删除单个演员信息
#         路由  DELETE  /actors/<pk>/
#         :param request:
#         :param pk:
#         :return:
#         """
#         try:
#             actor = Actor.objects.get(aid=pk)
#         except Actor.DoesNotExist:
#             return HttpResponse(status=404)
#
#         actor.delete()
#
#         return HttpResponse(status=204)



from stuapp.models import Actor, Movie
from rest_framework.viewsets import ModelViewSet
from stuapp.serializers import ActorSerializer, MovieSerializer


class ActorListView(ModelViewSet):
    """查询所有演员信息、增加演员信息、修改、删除操作"""
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieListView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

