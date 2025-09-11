from django.db import models

# class MainPage(models.Model):
#     title = models.CharField(max_length=100, blank=True)

#     def __str__(self):
#         return self.title or f"MainPage {self.id}"

# class Banner(models.Model):
#     page = models.ForeignKey(MainPage, related_name="banners", on_delete=models.CASCADE)
#     image = models.ImageField(upload_to="banners/", verbose_name="بنر")
#     title = models.CharField(max_length=100, blank=True)

#     def __str__(self):
#         return self.title or f"Banner {self.id}"

# class Image(models.Model):
#     page = models.ForeignKey(MainPage, related_name="images", on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='images/')
#     link  = models.URLField(max_length=500, blank=True, null=True)
#     title = models.CharField(max_length=100, blank=True) 
#     link1  = models.URLField(max_length=500, blank=True,null=True)
#     title1 = models.CharField(max_length=100, blank=True) 

#     def __str__(self):
#         return self.title or f"Image {self.id}"



class MainPage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)   

    class Meta:
        ordering = ['order']  

    def __str__(self):
        return self.title or f"MainPage {self.id}"


class Banner(models.Model):
    page = models.ForeignKey(MainPage, related_name="banners", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="banners/", verbose_name="بنر")
    title = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)  

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or f"Banner {self.id}"


class Image(models.Model):
    page = models.ForeignKey(MainPage, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    link  = models.URLField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True) 
    link1  = models.URLField(max_length=500, blank=True, null=True)
    title1 = models.CharField(max_length=100, blank=True) 
    link2  = models.URLField(max_length=500, blank=True, null=True)
    title2 = models.CharField(max_length=100, blank=True) 
    order = models.PositiveIntegerField(default=0)   

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or f"Image {self.id}"
