from django.db import models
from django.utils.translation import gettext_lazy as _
from cities_light.models import Country, City
# Create your models here.
class Address(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.country}, {self.city}"




class Language(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    release_date = models.DateField(_("Release Date"))
    director = models.CharField(_("Director"), max_length=255)
    description = models.TextField(_("Description"))
    poster = models.ImageField(_("Poster"), upload_to='movie_posters/', null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Language"))

    def __str__(self):
        return self.title
   


# class Theater(models.Model):
#     name = models.CharField(_("Name"), max_length=255)
#     location = models.CharField(_("Location"), max_length=255)
#     capacity = models.PositiveIntegerField(_("Capacity"))
#     description = models.TextField(_("Description"))
#     photo = models.ImageField(_("Photo"), upload_to='theater_photos/', null=True, blank=True)
#     city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name=_("City"))

#     def __str__(self):
#         return self.name
    

# class Showtime(models.Model):
#     theater = models.ForeignKey(Theater, on_delete=models.CASCADE, verbose_name=_("Theater"))
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name=_("Movie"))
#     start_time = models.DateTimeField(_("Start Time"))
#     end_time = models.DateTimeField(_("End Time"))
#     ticket_price = models.DecimalField(_("Ticket Price"), max_digits=8, decimal_places=2)

#     def __str__(self):
#         return f"{self.movie} at {self.theater} - {self.start_time}"

# class Booking(models.Model):
#     showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, verbose_name=_("Showtime"))
#     customer_name = models.CharField(_("Customer Name"), max_length=255)
#     customer_email = models.EmailField(_("Customer Email"))
#     booked_seats = models.PositiveIntegerField(_("Booked Seats"))
#     booking_date = models.DateTimeField(_("Booking Date"), auto_now_add=True)

#     def __str__(self):
#         return f"{self.customer_name} - {self.showtime} - Seats: {self.booked_seats}"
    
# class Ticket(models.Model):
#     showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, verbose_name=_("Showtime"))
#     seat_number = models.CharField(_("Seat Number"), max_length=10)
#     price = models.DecimalField(_("Price"), max_digits=8, decimal_places=2)
#     is_booked = models.BooleanField(_("Is Booked"), default=False)

#     def __str__(self):
#         return f"Ticket for {self.showtime} - Seat: {self.seat_number}" 