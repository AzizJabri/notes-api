from django.shortcuts import render
from rest_framework import status

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import NoteSerializer
from .models import Note
# Create your views here.


@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List': '/note-list/',
        'Detail View': '/note-detail/<str:pk>/',
        'Create': '/note-create/',
        'Update': '/note-update/<str:pk>/',
        'Delete': '/note-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def noteList(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def noteDetail(request, pk):
    notes = Note.objects.get(note_id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def noteCreate(request):
    serializer = NoteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PATCH'])
def noteUpdate(request, pk):
    note = Note.objects.get(note_id=pk)
    serializer = NoteSerializer(instance=note, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def noteDelete(request, pk):
    note = Note.objects.get(note_id=pk)
    note.delete()
    return Response("ITEM DELETED")
