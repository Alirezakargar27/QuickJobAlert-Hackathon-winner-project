import json

def generate_website():

    with open("user_data.json", "r") as file:
        users = json.load(file)
    html_str = ""
    for user in users:
        name = user["first_name"] + " " + user["last_name"]
        jobs = ""
        for job in user.get("jobs", []):
            job_title = job["title"]
            job_location = job["location"]
            job_company = job["company"]
            job_link = job["link"]
            jobs += f"<li> \
                        <div class=\"card\"> \
                            <img class=\"card-image\" src='https://cdn.pixabay.com/photo/2017/10/17/10/05/job-2860035_1280.jpg' /> \
                            <div class=\"card-body\"> \
                                <h3>{job_title}</h3> \
                                <p> \
                                    <i class=\"fa fa-building\"></i> {job_company} <br> \
                                    <i class=\"fa fa-location-arrow\"></i> {job_location} <br>\
                                    <a target=\"_blank\" href=\"{job_link}\"> Details </a> \
                                </p> \
                            </div> \
                        </div> \
                    </li>"
        html_str += f"<div> \
                        <h1>{name}</h1> \
                        <ul> \
                            {jobs} \
                        </ul> \
                    </div>"
    print("Generated HTML for users:", html_str)
    # Read HTML template
    with open("index.html", "r") as file:
        html_template = file.read()
    updated_template = html_template.replace("PLACEHOLDER", html_str)
    # Write out the HTML to job_index.html
    with open("job_index.html", "w") as file:
        file.write(updated_template)
    print("Done generating website")
