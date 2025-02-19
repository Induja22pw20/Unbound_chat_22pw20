from django.core.management.base import BaseCommand
from chat.models import ModelProvider

class Command(BaseCommand):
    help = 'Add sample model data to the database'

    def handle(self, *args, **kwargs):
        models = [
            'openai/gpt-3.5',
            'anthropic/claude-v1',
            'gemini/gemini-alpha'
        ]
        for model_name in models:
            ModelProvider.objects.create(name=model_name)
        self.stdout.write(self.style.SUCCESS('Successfully added model data'))
