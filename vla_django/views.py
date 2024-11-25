from django.shortcuts import render
from django.views import View
import requests
from bs4 import BeautifulSoup


class HomeView(View):
    def get(self, request):
        url = "https://www.jw.org/fr/"
        h3_titles = []
        h3_data = []

        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")

            h3_titles = soup.find_all("h3", limit=4)

            for h3 in h3_titles:
                a_tag = h3.find("a")
                if a_tag:
                    h3_data.append((a_tag.get_text(strip=True), a_tag.get("href")))

        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la récupération de la page : {e}")

        print("Données :", h3_data)

        return render(
            request,
            "vla_django/index.html",
            {
                "h3_data": h3_data,
            },
        )
