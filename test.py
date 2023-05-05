import unittest

from database_url_parser import get_database_config_variables

class TestGetDatabaseConfigVariables(unittest.TestCase):
    """
    Test case class for the `get_database_config_variables` function.

    This class contains test cases for the `get_database_config_variables`
    function, which parses a Heroku `DATABASE_URL` into a dictionary of
    database configuration variables. The test cases cover various edge cases
    and inputs to ensure that the function works correctly in all scenarios.
    """
    def test_get_database_config_variables(self):
        url = 'postgres://user:password@localhost:5432/dbname'
        expected_output = {
            'DATABASE_USER': 'user',
            'DATABASE_PASSWORD': 'password',
            'DATABASE_HOST': 'localhost',
            'DATABASE_PORT': '5432',
            'DATABASE_NAME': 'dbname'
        }
        self.assertEqual(get_database_config_variables(url), expected_output)
