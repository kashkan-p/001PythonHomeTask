import requests


class HttpClient:
    """HttpClient provides getting response from a server. The response contains raw html code of the requested page"""
    @staticmethod
    def get_html(base_url, params=None, header=None):
        return requests.get(base_url, params=params, headers=header).text
