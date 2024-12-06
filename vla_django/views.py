from datetime import date
from django.shortcuts import render
from django.views import View
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from communication.models import Communication
from predication.models import PredicationMeeting


class HomeView(View):
    def get(self, request):
        today = datetime.today().date()
        one_week_ago = today - timedelta(weeks=1)

        communications = Communication.objects.filter(date__gte=one_week_ago).order_by(
            "date"
        )

        today = date.today()
        predication = PredicationMeeting.objects.filter(date=today).first()

        url = "https://www.jw.org/fr/"

        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")

            # Main title
            main_title = soup.find("h3", class_="billboardTitle")
            main_title_text = None
            main_title_link = None

            if main_title:
                a_tag = main_title.find("a")

                if a_tag:
                    main_title_text = a_tag.get_text(strip=True)
                    main_title_link = a_tag.get("href")
                else:
                    print("Aucun lien trouvé.")
            else:
                print("Aucun titre principal trouvé.")

            # Synopses
            synopses = soup.find_all("div", class_="synopsis", limit=3)
            data = []

            for synopsis in synopses:
                syn_img_div = synopsis.find("div", class_="syn-img")
                a_tag = syn_img_div.find("a") if syn_img_div else None
                img_tag = a_tag.find("img") if a_tag else None

                syn_body_div = synopsis.find("div", class_="syn-body")
                h3_tag = syn_body_div.find("h3") if syn_body_div else None
                h3_a_tag = h3_tag.find("a") if h3_tag else None

                if h3_a_tag and img_tag and a_tag:
                    title = h3_a_tag.get_text(strip=True)
                    href = h3_a_tag.get("href")
                    img_src = img_tag.get("src")
                    data.append((title, href, img_src))

            for title, href, img_src in data:
                print(f"Titre: {title}\nLien: {href}\nImage URL: {img_src}\n")

        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la récupération de la page : {e}")

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
