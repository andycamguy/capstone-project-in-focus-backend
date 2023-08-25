from django.db import models
from django.db import models

class FStop(models.Model):
    value = models.FloatField()

class Lens(models.Model):
    length = models.CharField(max_length=255)
    fstop_min = models.FloatField()
    fstop_max = models.FloatField()

class CameraModel(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    f_stop_num = models.FloatField()
    f_stops = models.ManyToManyField(FStop, through='ModelFStop')
    lenses = models.ManyToManyField(Lens, through='ModelLens')

class ModelFStop(models.Model):
    fstop_id = models.ForeignKey(FStop, on_delete=models.CASCADE)
    model_id = models.ForeignKey(CameraModel, on_delete=models.CASCADE)

class ModelLens(models.Model):
    lens_id = models.ForeignKey(Lens, on_delete=models.CASCADE)
    model_id = models.ForeignKey(CameraModel, on_delete=models.CASCADE)

class DSLRCamera(models.Model):
    f_stop = models.ForeignKey(FStop, on_delete=models.CASCADE)
    lens = models.ForeignKey(Lens, on_delete=models.CASCADE)
    iso = models.IntegerField()
    model = models.ForeignKey(CameraModel, on_delete=models.CASCADE)

class ISO(models.Model):
    value = models.IntegerField()

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)

class UserCameraSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    camera_model = models.ForeignKey(CameraModel, on_delete=models.CASCADE)

class UserCameraObjectDistance(models.Model):
    user_settings = models.ForeignKey(UserCameraSettings, on_delete=models.CASCADE)
    object_distance = models.ForeignKey(ObjectDistance, on_delete=models.CASCADE)