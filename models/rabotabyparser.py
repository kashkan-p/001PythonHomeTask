from bs4 import BeautifulSoup


class RabotaByParser:
    """RabotaByParser provides parsing of particular data from raw html code of rabota.by pages"""
    @staticmethod
    def get_page_numbers(raw_html):
        """This method takes html code of a search page and returns the range of pages of a search query"""
        soup = BeautifulSoup(raw_html, "lxml")
        first_page = soup.find("span", class_="bloko-button bloko-button_pressed").text
        last_page = soup.find_all("span", class_="pager-item-not-in-short-range")[-1].find("a").text
        return {"first": int(first_page) - 1, "last": int(last_page)}

    @staticmethod
    def parse_vacancy_hrefs(raw_html):
        """This method takes html code of a search page and returns list of urls of every vacancy on a page"""
        soup = BeautifulSoup(raw_html, "lxml")
        vacancies = soup.find_all("div", class_="vacancy-serp-item__row vacancy-serp-item__row_header")
        vacancy_list = []
        for item in vacancies:
            vacancy_list.append(item.find("a", class_="bloko-link").get("href"))
        return vacancy_list

    @staticmethod
    def parse_vacancy_description(raw_html):
        """This method takes html code of a vacancy page and returns string representation of vacancy title and
        description """
        soup = BeautifulSoup(raw_html, "lxml")
        title = soup.find("div", class_="vacancy-title").find("h1").text
        vacancy_desc = soup.find("div", class_="vacancy-section").prettify()
        return {title: vacancy_desc}
