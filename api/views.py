from rest_framework import generics, status
from rest_framework.response import Response
from .models import Hit, Artist
from .serializers import HitSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .forms import HitForm

class HitListCreateView(generics.ListCreateAPIView):
    serializer_class = HitSerializer

    def get_queryset(self):
        # Pobieramy 20 hitów posortowanych względem daty dodania (najświeższe pierwsze)
        return Hit.objects.all().order_by('-created_at')[:20]

    def create(self, request, *args, **kwargs):
        serializer = HitSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response(HitSerializer(instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HitDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HitSerializer
    lookup_field = 'title_url'
    queryset = Hit.objects.all()

    def put(self, request, *args, **kwargs):
        hit = self.get_object()
        serializer = HitSerializer(hit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        hit = self.get_object()
        hit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def home(request):
    hits = Hit.objects.all().order_by('-created_at')[:20]
    artists = Artist.objects.all()
    return render(request, 'home.html', {'hits': hits, 'artists': artists})

def hit_detail(request, title_url):
    hit = get_object_or_404(Hit, title_url=title_url)
    return render(request, 'hit_detail.html', {'hit': hit})

def create_hit(request):
    if request.method == 'POST':
        form = HitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HitForm()
    return render(request, 'create_hit.html', {'form': form})

def edit_hit(request, title_url):
    hit = get_object_or_404(Hit, title_url=title_url)
    if request.method == 'POST':
        form = HitForm(request.POST, instance=hit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HitForm(instance=hit)
    return render(request, 'edit_hit.html', {'form': form})

def delete_hit(request, title_url):
    hit = get_object_or_404(Hit, title_url=title_url)
    hit.delete()
    return redirect('home')