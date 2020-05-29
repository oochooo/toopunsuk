#from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import datetime

from .gmap_req import get_current_loc, haversine_func_for_calculating_distance_between_two_points_on_our_very_precious_planet_earth as hs_distance


class Cabinet(models.Model):
    name_text = models.CharField(max_length=230)
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    image = models.ImageField(upload_to='cabinets', null=True)
    lat = models.DecimalField(('lat'), max_digits=10, decimal_places=8, null=True)
    lng = models.DecimalField(('lng'), max_digits=11, decimal_places=8, null=True)

    def distance(self):
        current_loc = get_current_loc()
        dist = hs_distance(current_loc, {'lat' : self.lat, 'lng' : self.lng})
        return {'dist': round(dist, 2), 'accuracy': current_loc['accuracy']/1000}

    def open_map_directions(self):
        link = "https://www.google.com/maps/dir/?api=1&destination=" + str(self.lat) + ',' + str(self.lng)
        return link


    def __str__(self):
        return self.name_text

class Update(models.Model):
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    need_refill = models.BooleanField(default=True)
    image_update = models.ImageField(upload_to='cabinets/uploads', blank=True, null=True)

    def __str__(self):
        return self.comment_text


