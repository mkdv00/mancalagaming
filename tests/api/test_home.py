from requests import Response

from lib.base_case import BaseCase
from lib.all_requests import AllRequests


class TestHome(BaseCase):

    def test_resource_does_not_have_status_code_404(self):
        response: Response = AllRequests.get(url="https://mancalagaming.org/")

        if response.status_code == 404:
            assert False, f"Got status code 404."
        else:
            assert True
