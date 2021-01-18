from typing import List, Dict, Any, Union

from ..request_parser import RequestParser


class MagdaRequestParser(RequestParser):
    def prepare_request_data(self, keywords: List[str]) -> Union[List, Dict]:
        """
        curl
            -X POST http://localhost:8007/api/
            -H 'Content-Type: application/json'
            -d '["bangkok", "miami vice", ...]'
        """
        return keywords

    def parse_response_data(self, response_data: Union[List, Dict]) -> Dict[str, Any]:
        """
        [
            {
                "keyword": "bangkok",
                "image": "http://localhost:8007/static/images/1610298025_XL5aqCjXWwu1rZBd.jpeg"
            },
            {
                "keyword": "miami vice",
                "image": "http://localhost:8007/static/images/1610298026_Wudu3BrWEyUgbM1f.jpeg"
            },
            ...
        ]
        """
        return {
            response_dict["keyword"]: response_data["image"]
            for response_dict in response_data
        }
