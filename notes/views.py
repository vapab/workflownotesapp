from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from notes.models import Note
from notes.serializers import NoteSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "tutorials/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = Note.objects.all()
    return render(request, "notes/index.html", {'notes': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'notes/index.html'

    def get(self, request):
        queryset = Note.objects.all()
        return Response({'notes': queryset})


class ListAllNotes(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'notes/note_list.html'

    def get(self, request):
        queryset = Note.objects.all()
        return Response({'notes': queryset})

class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'notes/login.html'

    def get(self, request):
        queryset = Note.objects.all()
        return Response({'notes': queryset})
      
class CreateNote(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'notes/create_note.html'

    def get(self, request):
        queryset = Note.objects.all()
        return Response({'notes': queryset})

class EditNote(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'notes/edit_note.html'

    def get(self, request):
        queryset = Note.objects.all()
        return Response({'notes': queryset})

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def note_list(request):
    if request.method == 'GET':
        notes = Note.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            notes = notes.filter(title__icontains=title)

        notes_serializer = NoteSerializer(notes, many=True)
        return JsonResponse(notes_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        note_data = JSONParser().parse(request)
        note_serializer = NoteSerializer(data=note_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return JsonResponse(note_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(note_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Note.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Notes were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def note_detail(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return JsonResponse({'message': 'The note does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        note_serializer = NoteSerializer(note)
        return JsonResponse(note_serializer.data)

    elif request.method == 'PUT':
        note_data = JSONParser().parse(request)
        note_serializer = NoteSerializer(note, data=note_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return JsonResponse(note_serializer.data)
        return JsonResponse(note_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        note.delete()
        return JsonResponse({'message': 'Note was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def note_list_published(request):
    notes = Note.objects.filter(published=True)

    if request.method == 'GET':
        notes_serializer = NoteSerializer(notes, many=True)
        return JsonResponse(notes_serializer.data, safe=False)