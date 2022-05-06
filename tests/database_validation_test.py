# project/tests/database_validation_test.py
import os

from click.testing import CliRunner

from app import create_database

runner = CliRunner()


def test_database_exists():
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) == True
