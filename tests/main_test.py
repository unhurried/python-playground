import datetime
from unittest.mock import MagicMock

import freezegun
from src.main import next_13th_friday


@freezegun.freeze_time('2024-01-01')
def test_next_13th_friday():

    expected = datetime.datetime(2024, 9, 13)
    assert next_13th_friday() == expected
