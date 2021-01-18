from typing import List, Dict, Any, Union

from ..request_parser import RequestParser


class JanekRequestParser(RequestParser):
    def prepare_request_data(self, keywords: List[str]) -> Union[List, Dict]:
        """
        curl
            --location
            --request POST '0.0.0.0:8000/firstone/'
            --header 'Content-Type: application/json'
            --data-raw '{"body": ["first search", "second search"]}'
        """
        return {"body": keywords}

    def parse_response_data(self, response_data: Union[List, Dict]) -> Dict[str, Any]:
        """
        [
            {
                "first search": {
                    "Google": "google first page",
                    "Youtube": "youtube first video",
                    "StackOverflow": "etc.",
                    "Yahoo": "etc.",
                    "Baidu": "etc.",
                    "DuckDuckGo": "etc.",
                    "Bing": "etc.",
                    "GitHub": "etc.",
                    "Yandex": "etc.",
                    "Aol": "etc.",
                    "Ask": "etc.","etc.",
                    "Coursera": "etc.",
                },
                "second search": {
                    "Google": "google first page",
                    "Youtube": "youtube first video",
                    "StackOverflow": "etc.",
                    "Yahoo": "etc.",
                    "Baidu": "etc.",
                    "DuckDuckGo": "etc.",
                    "Bing": "etc.",
                    "GitHub": "etc.",
                    "Yandex": "etc.",
                    "Aol": "etc.",
                    "Ask": "etc.","etc.",
                    "Coursera": "etc.",
                },
            }
        ]
        """
        response_dict = response_data[0]
        return {
            keyword: values for keyword, values in response_dict.items()
        }
