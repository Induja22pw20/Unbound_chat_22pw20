from django.db import models

class ModelProvider(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RegexPolicy(models.Model):
    pattern = models.CharField(max_length=100)
    model_provider = models.ForeignKey(ModelProvider, on_delete=models.CASCADE)

    def __str__(self):
        return self.pattern
