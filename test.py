import os
import random
import unittest

import pandas as pd

from deltek import Deltek, PASSWORD, USER_NAME


class TestDeltek(unittest.TestCase):
    def setUp(self):
        self.dapi = Deltek(username=USER_NAME, password=PASSWORD)

    def test_get_employees(self):
        limit = random.randint(0, 1000)
        emp_list = self.dapi.get_employees(limit=limit, offset=0)
        self.assertTrue(isinstance(emp_list, list))
        self.assertTrue(len(emp_list) == limit)

    def test_get_dailytimesheetlines(self):
        limit = random.randint(0, 1000)
        emp_list = self.dapi.get_employees(limit=limit, offset=0)
        employee = random.choice(emp_list)
        restriction = {
            "employeenumber": {"value": employee["employeenumber"], "operator": "like"},
        }
        data = self.dapi.get_dailytimesheetlines(limit=limit, restriction=restriction)
        self.assertTrue(isinstance(data, list))
        df = pd.DataFrame(data)
        self.assertTrue(df["employeenumber"].unique().tolist()[0] == employee["employeenumber"])

    def test_get_companies(self):
        limit = random.randint(0, 1000)
        offset = random.randint(0, 1000)
        company_list = self.dapi.get_companies(limit=limit, offset=offset)
        self.assertTrue(isinstance(company_list, list))
        self.assertTrue(len(company_list) == limit)

    def test_get_expensesheets(self):
        limit = random.randint(0, 1000)
        offset = random.randint(0, 1000)
        expensesheets_list = self.dapi.get_expensesheets(limit=limit, offset=offset)
        self.assertTrue(isinstance(expensesheets_list, list))
        self.assertTrue(len(expensesheets_list) == limit)

    def tearDown(self):
        self.dapi.close()


if __name__ == "__main__":
    unittest.main()
