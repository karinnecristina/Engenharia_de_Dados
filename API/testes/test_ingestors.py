import datetime
import pytest
from unittest.mock import patch
from ingestors import DataIngestor
from writes import DataWriter


@pytest.fixture
@patch("ingestors.DataIngestor.__abstractmethods__", set())
def data_ingestor_fixture():
    return DataIngestor(
        writer=DataWriter,
        coins=["TEST", "HOW"],
        default_start_date=datetime.date(2021, 6, 21),
    )


@patch("ingestors.DataIngestor.__abstractmethods__", set())
class TestIngestors:
    def test_checkpoint_filename(self, data_ingestor_fixture):
        actual = data_ingestor_fixture._checkpoint_filename
        expected = "DataIngestor.checkpoint"
        assert actual == expected

    @patch("ingestors.DataIngestor._write_checkpoint", return_value=None)
    def test_update_checkpoint_checkpoint_written(self, mock, data_ingestor_fixture):
        data_ingestor_fixture._update_checkpoint(value=datetime.date(2019, 1, 1))
        mock.assert_called_once()
