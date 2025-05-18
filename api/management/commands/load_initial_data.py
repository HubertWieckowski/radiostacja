from django.core.management.base import BaseCommand
from api.models import Artist, Hit
print("Ładuję komendę load_initial_data")

class Command(BaseCommand):
    help = 'Ładuje dane początkowe: 3 artystów i 20 hitów'

    def handle(self, *args, **kwargs):
        # Opcjonalnie: wyczyść istniejące dane
        Hit.objects.all().delete()
        Artist.objects.all().delete()

        artists_data = [
            {'first_name': 'Jan', 'last_name': 'Kowalski'},
            {'first_name': 'Anna', 'last_name': 'Nowak'},
            {'first_name': 'Piotr', 'last_name': 'Wiśniewski'},
        ]
        artists = []
        for art in artists_data:
            artist = Artist.objects.create(**art)
            artists.append(artist)
            self.stdout.write(self.style.SUCCESS(f"Dodano artystę: {artist}"))

        # Tworzymy 20 hitów, przypisując artystom cyklicznie
        for i in range(1, 21):
            title = f"Hit number {i}"
            artist = artists[i % len(artists)]
            hit = Hit.objects.create(title=title, artist=artist)
            self.stdout.write(self.style.SUCCESS(f"Dodano hit: {hit}"))

        self.stdout.write(self.style.SUCCESS("Dane początkowe zostały załadowane."))
