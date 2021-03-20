from models.rabotabyparser import RabotaByParser
from http_client.httpclient import HttpClient
from utils.utils import get_flat_list, count_word_occurrences, count_average_word_occurrence

URL = 'https://rabota.by/search/vacancy'
KEYWORD = "python"
PARAMS = {"area": "1002", "text": KEYWORD}
HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/39.0.2171.95 Safari/537.36'}

if __name__ == '__main__':
    # Initializing client and parser objects
    client = HttpClient()
    parser = RabotaByParser()

    # Getting the first search page html code
    start_page = client.get_html(URL, params=PARAMS, header=HEADER)
    # Getting numbers of pages of a search query
    pages_range = parser.get_page_numbers(start_page)

    # Getting the list of vacancy urls on an every search page
    vacancy_urls = []
    for number in range(pages_range["first"], pages_range["last"]):
        PARAMS["page"] = number
        page = client.get_html(URL, params=PARAMS, header=HEADER)
        vacancy_urls.append(parser.parse_vacancy_hrefs(page))

    # Merging all urls to one flat list
    all_vacancies_urls = get_flat_list(vacancy_urls)

    # Getting html code of every vacancy page and adding it to a list
    vacancy_description_raw = []
    for vacancy_url in all_vacancies_urls:
        vacancy_description_raw.append(client.get_html(vacancy_url, header=HEADER))

    # Parsing vacancy title and description and adding it to a list
    vacancies_parsed = []
    for vacancy in vacancy_description_raw:
        parsed = parser.parse_vacancy_description(vacancy)
        vacancies_parsed.append(parsed)

    # Counting occurrences of the given words in each vacancy description
    counted = count_word_occurrences(vacancies_parsed, "python", "linux", "flask")
    # Counting average occurrences of the given words
    avg_occurrence = count_average_word_occurrence(vacancies_parsed, "python", "linux", "flask")
