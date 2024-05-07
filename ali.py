import http.client
import json
from datetime import datetime
from fuzzywuzzy import fuzz

def fetch_job_listings(api_key, user_data):
    """Fetches job listings from Jooble job platform using their API"""

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

            filtered_listings = []
            for job in response_data.get("jobs", []):
                job_title = job.get("title", "")
                if fuzz.partial_ratio(filters["keywords"].lower(), job_title.lower()) > 70:  # Adjust the threshold as needed
                    job_updated = datetime.strptime(job.get("updated").split('T')[0], "%Y-%m-%d")
                    if job_updated >= datetime(2024, 5, 1):
                        filtered_job = {
                            "title": job_title,
                            "location": job.get("location", ""),
                            "company": job.get("company", ""),
                            "updated": job.get("updated", ""),
                            "link": job.get("link", "")
                        }
                        filtered_listings.append(filtered_job)

            return filtered_listings
        else:
            print(f"Error: {response.status} - {response.reason}")
            return None
    except Exception as e:
        print("Error fetching job listings:", e)
        return None
    finally:
        # Close the connection
        connection.close()
