from bs4 import BeautifulSoup
import requests


def scrap_jw_org():
    url = "https://www.jw.org/fr/"
    data = []
    main_title_text = None
    main_title_link = None

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        # Main title
        main_title = soup.find("h3", class_="billboardTitle")
        if main_title:
            a_tag = main_title.find("a")
            if a_tag:
                main_title_text = a_tag.get_text(strip=True)
                main_title_link = a_tag.get("href")
        else:
            print("Aucun titre principal trouvé.")

        # Synopses
        synopses = soup.find_all("div", class_="synopsis", limit=3)

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

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération de la page : {e}")

    return main_title_text, main_title_link, data
