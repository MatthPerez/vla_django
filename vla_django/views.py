from datetime import date
from django.shortcuts import render
from django.views import View
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from communication.models import Communication
from predication.models import PredicationMeeting
from vla_django.static.scripts.scrap import scrap_jw_org


class HomeView(View):
    def get(self, request):
        today = datetime.today().date()
        one_week_ago = today - timedelta(weeks=1)

        communications = Communication.objects.filter(date__gte=one_week_ago).order_by(
            "date"
        )

        predication = PredicationMeeting.objects.filter(date=today).first()

        main_title_text, main_title_link, data = scrap_jw_org()

        return render(
            request,
            "vla_django/index.html",
            {
                "main_title_text": main_title_text,
                "main_title_link": main_title_link,
                "data": data,
                "communications": communications,
                "predication": predication,
            },
        )
