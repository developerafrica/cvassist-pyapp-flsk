from api.scraper.google import export_data
from api.models.jobsmodel import Job
from api.models.scarpermodel import Scrape

def save_jobdata(data):
    job_db_list = []
    for items in data:
        db = Job(
            position = items["position"],
            company = items["company"],
            location = items["location"],
            site_posted = items["site_posted"],
            job_type = "".join(items["job_type"]),
            time_posted = "".join(items["time_posted"]),
            cv_data = "",
            description = items["description"],
            modified = "False",
            company_website = "".join(items["company_website"])
        )
        job_db_list.append(db)

    return job_db_list

def save_scrapedata(data):
    scrape_positions = str([items["position"] for items in data])
    return Scrape( results = scrape_positions )

    
scrape_db  = save_scrapedata(export_data)
job_db = save_jobdata(export_data)

