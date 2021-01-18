from typing import List, Dict, Any, Union

from ..request_parser import RequestParser


class AniaRequestParser(RequestParser):
    def prepare_request_data(self, keywords: List[str]) -> Union[List, Dict]:
        """
        curl
            --request POST 'http://localhost:5000/api/'
            --header 'Content-Type: application/json'
            --data-raw '["string1", "string2", "string3", ...]'
        """
        return keywords

    def parse_response_data(self, response_data: Union[List, Dict]) -> Dict[str, Any]:
        """
        [
            {
                "string": "string1",
                "image_url": "https://async-memes.s3-eu-central-1.amazonaws.com/meme-xxx.png"
            },
            ...
        ]
        """
        return {
            response_dict["string"]: response_dict["image_url"]
            for response_dict in response_data
        }
