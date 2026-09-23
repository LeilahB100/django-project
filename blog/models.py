from django.db import models

class Authors(models.Model):
    GENDER_OPTIONS = [
        ("M", "Male"),
        ("F", "Female")
    ]
    name = models.CharField(max_length=50, verbose_name="Author Name")
    contact = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=100, null=True, blank=True, default="N/A")
    gender = models.CharField(max_length=2, choices=GENDER_OPTIONS)

class article(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField()
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    publish_date = models.DateField(auto_now=False)
    is_published = models.BooleanField(default=False)
