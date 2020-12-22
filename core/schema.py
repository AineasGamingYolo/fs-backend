import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from .models import Thread, Comment, CustomUser

class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser

class ThreadType(DjangoObjectType):
    class Meta:
        model = Thread


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

class Query(ObjectType):
    thread = graphene.Field(ThreadType, id=graphene.Int())
    comment = graphene.Field(CommentType, id=graphene.Int())
    threads = graphene.List(ThreadType)
    comments = graphene.List(CommentType)

    def resolve_thread(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Thread.objects.get(pk=id)

        return None

    def resolve_comment(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Comment.objects.get(pk=id)

        return None

    def resolve_threads(self, info, **kwargs):
        return Thread.objects.all()

    def resolve_comments(self, info, **kwargs):
        return Comment.objects.all()
