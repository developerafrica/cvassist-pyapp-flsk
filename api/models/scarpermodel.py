from api import db
from datetime import datetime

# jobs
class Scrape(db.Model):
    __tablename__ = "scape"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # variables
    results = db.Column(db.Text, nullable=False)
    # dates
    identifier =  db.Column(db.Text, default=datetime.utcnow().strftime('%j'),  nullable=False) 
    year = db.Column(db.Text, default=datetime.utcnow().strftime('%G'), nullable=False) 
    month =db.Column(db.Text, default=datetime.utcnow().strftime('%m'), nullable=False) 
    day = db.Column(db.Text, default=datetime.utcnow().strftime('%d'), nullable=False) 
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)