from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import HttpResponse

from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

from chatterbot.ext.django_chatterbot import settings

class ChatterBotAppView(TemplateView):
    template_name = "app.html"

class ChatterBotInitializeView(View):
    def get(self, request, *args, **kargs):
        return self.post(request, *args, **kargs)

    def post(self, request, *args, **kargs):
        chatterbot = ChatBot(**settings.CHATTERBOT)
        chatterbot.set_trainer(ChatterBotCorpusTrainer)
        chatterbot.train("data.fies",
                         "chatterbot.corpus.portuguese.greetings"
                        )
        return HttpResponse("OK", content_type="text/plain")
