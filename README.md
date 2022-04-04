# To Run the Example

Tested with python 3.9.9. Create venv and install requirements.txt.
```
➜  report-api-test python -m venv venv
➜  report-api-test ls
main.py          requirements.txt venv
➜  report-api-test . ./venv/bin/activate
(venv) ➜  report-api-test pip install -r requirements.txt 
Collecting requests
  Using cached requests-2.27.1-py2.py3-none-any.whl (63 kB)
Collecting python-dotenv
  Using cached python_dotenv-0.20.0-py3-none-any.whl (17 kB)
Collecting charset-normalizer~=2.0.0
  Using cached charset_normalizer-2.0.12-py3-none-any.whl (39 kB)
Collecting certifi>=2017.4.17
  Using cached certifi-2021.10.8-py2.py3-none-any.whl (149 kB)
Collecting idna<4,>=2.5
  Using cached idna-3.3-py3-none-any.whl (61 kB)
Collecting urllib3<1.27,>=1.21.1
  Using cached urllib3-1.26.9-py2.py3-none-any.whl (138 kB)
Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests, python-dotenv
Successfully installed certifi-2021.10.8 charset-normalizer-2.0.12 idna-3.3 python-dotenv-0.20.0 requests-2.27.1 urllib3-1.26.9
WARNING: You are using pip version 21.2.4; however, version 22.0.4 is available.
You should consider upgrading via the '/Users/dqiu/trepo/report-api-test/venv/bin/python -m pip install --upgrade pip' command.
```

Edit .env file to populate the `API_KEY` and `API_AUTH`. Then run `main.py`.
```
(venv) ➜  report-api-test python main.py 
{'data': {'publisherNetworkReport': {'rows': [{'dimensions': [{'name': 'buyer_me...
```

# Take-Away Notes
The easiest way to write query and variables separately is to use the following pattern:
```
    r = requests.post(
        url, headers=headers, json={"query": query, "variables": variables}
    )
```

For some parameters like dimensions/metrics/filters it's difficult to provide them as part of the query 
parameter due to Enum typing conflict with python code. For these I opted to format the value as part 
of the query string. In order to properly utilze python string `.format()` method (which expects the formatted params in curly braces), we need to escape all other curly braces by doubling them up (`{{` and `}}`)
