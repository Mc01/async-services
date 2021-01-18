from typing import List, Union, Dict, Any


class RequestParser:
    def __init__(self):
        self.internal_data = {}

    def prepare_request_data(self, keywords: List[str]) -> Union[List, Dict]:
        raise NotImplementedError

    def parse_response_data(self, response_data: Union[List, Dict]) -> Dict[str, Any]:
        raise NotImplementedError
