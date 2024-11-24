from django.shortcuts import render
from django.views import View
import requests
from bs4 import BeautifulSoup


class HomeView(View):
    def get(self, request):
        url = "https://www.jw.org/fr/"
        billboard_title = None
        h3_titles = []

        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")

            billboard_element = soup.find("h3", class_="billboardTitle")
            if billboard_element:
                billboard_title = billboard_element.get_text(strip=True)

            h3_elements = soup.find_all("h3", limit=4)
            h3_titles = [element.get_text(strip=True) for element in h3_elements]

        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la récupération de la page : {e}")

        return render(
            request,
            "vla_django/index.html",
            {
                "billboard_title": billboard_title,
                "h3_titles": h3_titles,
            },
        )
