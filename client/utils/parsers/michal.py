from typing import List, Dict, Any, Union

from ..request_parser import RequestParser


class MichalRequestParser(RequestParser):
    def prepare_request_data(self, keywords: List[str]) -> Union[List, Dict]:
        """
        curl
            -X POST http://localhost:8000/api/
            -H 'Content-Type: application/json'
            -d '["banana split", "how to make a sushi"]'
        """
        return keywords

    def parse_response_data(self, response_data: Union[List, Dict]) -> Dict[str, Any]:
        """
        {
          "keyword": "result",
          ...
        }
        """
        return response_data
