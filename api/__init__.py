from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from os.path import dirname, abspath, join, exists
from flask_login import LoginManager
from datetime import datetime
BASE = abspath(dirname(__file__))
DB_NAME = "database.db"
db = SQLAlchemy()
ma = Marshmallow()

def create_database(app):
    if not exists(join(BASE + f"{DB_NAME}")):
        with app.app_context():
            db.create_all()
    
def data_scheduler(app, Scarpe, jobdb, scrapedb):
    with app.app_context():
        db_date = Scarpe.query.get(1)

        if db_date == None:
            db.session.add(scrapedb)
            db.session.commit()

            for jobdb_item in jobdb:
                    db.session.add(jobdb_item)
                    db.session.commit()

        else:
            date = db_date.identifier
            today = datetime.utcnow().strftime('%j')
           
            if today > date:
                db.session.add(scrapedb)
                db.session.commit()

                for jobdb_item in jobdb:
                        db.session.add(jobdb_item)
                        db.session.commit()

            else:
                print(f"date:{date}")
                print(f"today:{today}")

  
def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + join(BASE, f"{DB_NAME}")
    app.config["SECRET_KEY"] = "dev"

    db.init_app(app)
    ma.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'ui.index'
    login_manager.init_app(app)


    from api.views.auth import auth
    from api.views.jobs import jobs
    from api.views.interface import ui
    app.register_blueprint(auth)
    app.register_blueprint(jobs)
    app.register_blueprint(ui)

    from api.models.usersmodel import Users  
    from api.models.jobsmodel import Job
    from api.models.scarpermodel import Scrape  
    create_database(app)

    from api.scraper.scraper import scrape_db, job_db
    data_scheduler(app, Scrape, job_db, scrape_db)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))
        
    return app
