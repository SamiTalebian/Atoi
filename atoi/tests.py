from locale import atoi
from django.test import Client, TestCase

from atoi.models import AtoiLog

class AtoiTestCase(TestCase):
    def setUp(self):
        client = Client()
        client.post("http://127.0.0.1:8000/atoi/",{'atoi' : '1234'})
        client.post("http://127.0.0.1:8000/atoi/",{'atoi' : '1234 with words'})
        client.post("http://127.0.0.1:8000/atoi/",{'atoi' : '00134'})
        client.post("http://127.0.0.1:8000/atoi/",{'atoi' : '-134'})

    def test_list_of_plyaer_records_success(self):
        logs = AtoiLog.objects.all()
        log_with_zeros = AtoiLog.objects.get(atoi_number=134)
        log_with_words = AtoiLog.objects.get(atoi_string='1234 with words')
        log_negetive = AtoiLog.objects.get(atoi_string='-134')
        
        assert logs.count() == 4
        assert log_with_zeros.atoi_string == "00134"
        assert log_with_words.atoi_number == 1234
        assert log_negetive.atoi_number == -134