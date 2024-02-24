from django.urls import path, include
from api.models import CourseResource, CategoryResource
from tastypie.api import Api

api = Api(api_name='v1')
course_res = CourseResource()
category_res = CategoryResource()
api.register(course_res)
api.register(category_res)

urlpatterns = [
    path('', include(api.urls), name='index')
]