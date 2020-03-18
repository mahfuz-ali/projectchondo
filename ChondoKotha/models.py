from django.db import models

class Divisions(models.Model):
    name = models.CharField(max_length=200)
    bn_name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=200)
    bn_name = models.CharField(max_length=200)
    division = models.ForeignKey(Divisions,on_delete=models.CASCADE)
    lat = models.CharField(max_length=200, null=True)
    lon = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    bn_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Chondokotha(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    list_display = ['category_name', 'district_name', 'division_name']


    def category_name(self):
        return self.category.name

    def district_name(self):
        return self.district.name

    def division_name(self):
        return self.district.division.name


    def __str__(self):
        return self.title










#######################################################################

class QueryStrings(models.Model):

    data = models.CharField(max_length=200)

    report = models.TextField(max_length=500)



    class Meta:

        ordering = ['-id']



    def __str__(self):

        return self.data
