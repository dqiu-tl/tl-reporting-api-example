import os
import requests
from dotenv import load_dotenv


def get_auth():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    api_auth = os.getenv("API_AUTH")
    return (api_key, api_auth)


def run_report(start, end):

    api_key, api_auth = get_auth()
    headers = {
        "Authorization": f"Bearer {api_auth}",
        "X-API-Key": api_key,
        "Content-Type": "application/json",
    }

    dimensions = "[BUYER_MEMBER,BRAND,SUPPLY_SOURCE]"
    metrics = "[RENDERED,REVENUE]"
    filters = '[{dimension: SUPPLY_SOURCE_ID values: ["12"]}]'

    query = """
        query publisherNetworkReport (
          $start: Date!, 
          $end: Date!)
        {{
          publisherNetworkReport(
            sellerMemberId: "7194"
            startDate: $start
            endDate: $end
            dimensions: {dimensions}
            metrics: {metrics}
            filters: {filters}
          ) {{
            rows {{
              dimensions {{
                name
                value
              }}
              metrics {{
                __typename
                ...on
                MetricLong {{
                  name
                  long: value
                }}
                ...on
                MetricDecimal {{
                  name
                  decimal: value
                }}
              }}
            }}
          }}
        }}
    """.format(
        dimensions=dimensions, metrics=metrics, filters=filters
    )

    variables = {
        "start": start,
        "end": end,
    }

    url = "https://reporting-api.triplelift.net/graphql"

    r = requests.post(
        url, headers=headers, json={"query": query, "variables": variables}
    )
    print(r.json())


if __name__ == "__main__":
    run_report("2022-03-29", "2022-03-30")
