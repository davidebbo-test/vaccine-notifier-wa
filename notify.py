import re

from bs4 import BeautifulSoup
import requests as requests


def check_availability():
    url = "https://prepmod.doh.wa.gov/clinic/search?q[services_name_in][]=covid&q[age_groups_name_in][" \
          "]=Adults&location=98004&search_radius=10+miles&q[venue_search_name_or_venue_name_i_cont]=&clinic_date_eq[" \
          "year]=2021&clinic_date_eq[month]=4&clinic_date_eq[day]=10&q[" \
          "vaccinations_name_i_cont]=Moderna&commit=Search#search_results "
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    found = False
    for div in soup.findAll("div", {"class": "md:flex-shrink"}):
        text = div.getText()
        match = re.search(r"Available Appointments:\s*(\d+)", text, re.MULTILINE)
        if match is not None:
            appointments = int(match.group(1))
            if appointments >= 0:
                print(text)
                found = True

    if found:
        print("Found appointments!")
    else:
        print("Hard luck!")


if __name__ == "__main__":
    check_availability()
