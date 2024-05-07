import http.client
import json
from datetime import datetime


def fetch_job_listings(api_key, filters):
    """Fetches job listings from Jooble job platform using their API"""

    host = 'jooble.org'

    # Construct JSON query with keywords, location, and other filters
    body = json.dumps({
        "keywords": filters.get("keywords", ""),
        "location": filters.get("location", ""),
    })

    try:
        # Establish connection to Jooble API
        connection = http.client.HTTPConnection(host)

        # Request headers
        headers = {"Content-type": "application/json"}

        # Send POST request with API key
        connection.request('POST', '/api/' + api_key, body, headers)

        # Get response from the API
        response = connection.getresponse()

        # Check response status
        if response.status == 200:
            # Read and parse the response JSON
            response_data = json.loads(response.read().decode("utf-8"))

            # Filter job listings updated from May 1, 2024, onwards
            filtered_listings = []
            for job in response_data.get("jobs", []):
                job_updated = datetime.strptime(job.get("updated").split('T')[0], "%Y-%m-%d")
                if job_updated >= datetime(2024, 5, 1):
                    filtered_job = {
                        "title": job.get("title", ""),
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


# Example usage:
api_key = "471cdc11-45b6-419c-8c52-2c1a99f3d072"

filters = {
    "keywords": "Software",
    "location": "Hamburg",
}

job_listings = fetch_job_listings(api_key, filters)
if job_listings:
    for job in job_listings:
        print(job)
else:
    print("No job listings found.")
