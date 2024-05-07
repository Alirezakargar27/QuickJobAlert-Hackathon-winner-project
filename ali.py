import http.client
import json
from datetime import datetime
from fuzzywuzzy import fuzz

def fetch_job_listing(api_key, user_data):
    """Fetches the latest job listing from Jooble job platform for a user using their API"""

    host = 'jooble.org'

    filters = {
        "keywords": user_data["job_title"],
        "location": user_data["location"],
    }

    body = json.dumps({
        "keywords": filters.get("keywords", ""),
        "location": filters.get("location", ""),
    })

    try:
        connection = http.client.HTTPConnection(host)
        headers = {"Content-type": "application/json"}
        connection.request('POST', '/api/' + api_key, body, headers)
        response = connection.getresponse()

        if response.status == 200:
            response_data = json.loads(response.read().decode("utf-8"))

            latest_job_listing = None
            latest_update_date = datetime.min

            for job in response_data.get("jobs", []):
                job_title = job.get("title", "")
                if fuzz.partial_ratio(filters["keywords"].lower(), job_title.lower()) > 70:
                    job_updated = datetime.strptime(job.get("updated").split('T')[0], "%Y-%m-%d")
                    if job_updated >= latest_update_date:
                        latest_job_listing = {
                            "id": job.get("id"),
                            "title": job_title,
                            "location": job.get("location", ""),
                            "company": job.get("company", ""),
                            "updated": job.get("updated", ""),
                            "link": job.get("link", "")
                        }
                        latest_update_date = job_updated

            return latest_job_listing
        else:
            print(f"Error: {response.status} - {response.reason}")
            return None
    except Exception as e:
        print("Error fetching job listing:", e)
        return None
    finally:
        # Close the connection
        connection.close()
