# Deltek-API-Wrapper

## Example Usage
```python
from deltek import Deltek, PASSWORD, USER_NAME

deltekapi = Deltek(username=USER_NAME, password=PASSWORD)

restriction = {
  "thedate": {"value": "date(2020,5,1)", "operator": ">"},
}
data = deltekapi.get_dailytimesheetlines(limit=1000, restriction=restriction)
```
