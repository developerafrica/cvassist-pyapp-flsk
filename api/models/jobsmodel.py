from api import db
from datetime import datetime

# roles

# users

# jobs
class Job(db.Model):
    __tablename__ = "jobs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # variables
    position = db.Column(db.String(length=100), nullable=False)
    company = db.Column(db.String(length=100), nullable=False)
    location = db.Column(db.String(length=100), nullable=False)
    site_posted = db.Column(db.String(length=100), nullable=False)
    job_type = db.Column(db.String(length=100), nullable=False)
    time_posted = db.Column(db.String(length=100), nullable=False)
    cv_data = db.Column(db.Text(), default=False, nullable=False)
    description = db.Column(db.Text(), nullable=False)
    modified = db.Column(db.String(length=10), default=False, nullable=False)
    company_website = db.Column(db.String(length=100), nullable=False)
    # dates
    identifier =  db.Column(db.Text, default=datetime.utcnow().strftime('%j'),  nullable=False) 
    year = db.Column(db.Text, default=datetime.utcnow().strftime('%G'), nullable=False) 
    month =db.Column(db.Text, default=datetime.utcnow().strftime('%m'), nullable=False) 
    day = db.Column(db.Text, default=datetime.utcnow().strftime('%d'), nullable=False) 
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    date_updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, position, company, location, site_posted, job_type, time_posted, company_website, cv_data, description, modified):
        self.position = position 
        self.company = company 
        self.location = location 
        self.site_posted = site_posted
        self.job_type = job_type 
        self.time_posted = time_posted
        self.cv_data = cv_data 
        self.description = description
        self.modified =  modified 
        self.company_website = company_website
