import json

import pandas as pd
import requests

USER_NAME = "xxxUSERNAMExxx"
PASSWORD = "xxxPASSWORDxxx"

class Deltek(object):
    def __init__(self, username, password):
        self.BASE_URL = "https://deltek.example.com/containers/v1/example_production"
        self.username = username
        self.password = password
        self.headers = {"Content-Type": "application/json", "Accept-Language": "en-US"}
        self.AUTH = (self.username, self.password)
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.session.auth = self.AUTH

    def close(self):
        self.session.close()

    def get_data(self, container, limit=1000, offset=0, restriction={}, fields=[]):
        timeout = None
        url = f"{self.BASE_URL}/{container}/filter?limit={limit}&offset={offset}"
        if fields:
            url += f"&fields={','.join(fields)}"
        restrictions = []
        if restriction:
            for k, v in restriction.items():
                value = '"%s"' % (v["value"])
                if "date" in str(v["value"]):
                    value = v["value"]
                string = "%s %s %s" % (k, v["operator"], value)
                restrictions.append(string)
            url += f"&restriction={' and '.join(restrictions)}"
        url = requests.utils.requote_uri(url)
        data = []
        print(url)
        r = self.session.get(url, timeout=timeout)
        print(r)
        if r.status_code == 200:
            data = [sheet["data"] for sheet in r.json()["panes"]["filter"]["records"]]
            for sheet in data:
                sheet["instancekey"] = sheet["instancekey"][-36:]
        else:
            print(r.json())
        return data

    def get_employees(self, limit=1000, offset=0, restriction={}, fields=[]):
        fields = []
        container = "employees"
        data = self.get_data(
            container,
            limit=limit,
            offset=offset,
            restriction=restriction,
            fields=fields,
        )
        return data

    def get_dailytimesheetlines(
        self, limit=1000, offset=0, restriction={}, fields=[]
    ):
        fields = []
        container = "DailyTimeSheetLines"
        data = self.get_data(
            container,
            limit=limit,
            offset=offset,
            restriction=restriction,
            fields=fields,
        )
        return data

    def get_companies(self, limit=1000, offset=0, restriction={}, fields=[]):
        container = "CompanyCustomerCard"
        data = self.get_data(
            container,
            limit=limit,
            offset=offset,
            restriction=restriction,
            fields=fields,
        )
        return data

    def get_jobreallocation(self, limit=1000, offset=0, restriction={}, fields=[]):
        container = "jobreallocation"
        data = self.get_data(container, limit=limit, offset=offset, restriction=restriction, fields=fields)
        return data

    def get_expensesheets(self, limit=1000, offset=0, restriction={}, fields=[]):
        container = "ExpenseSheets"
        data = self.get_data(
            container,
            limit=limit,
            offset=offset,
            restriction=restriction,
            fields=fields,
        )
        return data

    def get_invoices(self, limit=1000, offset=0, restriction={}, fields=[]):
        container = "find_invoice"
        data = self.get_data(
            container,
            limit=limit,
            offset=offset,
            restriction=restriction,
            fields=fields,
        )
        return data

    def get_projects(self, limit=1000, offset=0, restriction={}, fields=[]):
        container = "projects"
        data = self.get_data(
            container,
            limit=limit,
            offset=offset,
            restriction=restriction,
            fields=fields,
        )
        return data

    def get_jobs(self, limit=1000, offset=0, restriction={}, fields=[]):
        fields = []
        container = "jobs"
        data = self.get_data(
            container,
            limit=limit,
            offset=offset,
            restriction=restriction,
            fields=fields,
        )
        return data

    def get_customerpayments(self, limit=1000, offset=0, restriction={}, fields=[]):
        container = "showcustomerpaymentjournals"
        data = self.get_data(
            container,
            limit=limit,
            offset=offset,
            restriction=restriction,
            fields=fields,
        )
        return data
