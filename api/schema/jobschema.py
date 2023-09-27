from api import ma

class JobSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "identifier",
            "position",
            "company",
            "location",
            "site_posted",
            "job_type",
            "time_posted",
            "company_webiste",
            "description",
            "modified",
            "cv_data",
            "date_created",
            "date_updated",
            "year",
            "month",
            "day"
            )


jobschema = JobSchema()
jobsschema = JobSchema(many=True)