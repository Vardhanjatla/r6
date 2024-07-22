from django.db import models

class Server(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Folder(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    path = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.server.name} - {self.path}"
  