from requests_html import HTMLSession

class JobObj:
    def __init__(self,id, position, company, location, siteposted, jobtype, timeposted, companywebsite, description):
        self.uuid = id
        self.position = position
        self.company = company
        self.location = location
        self.site_posted = siteposted
        self.job_type = [*set(jobtype)]
        self.time_posted = [*set(timeposted)]
        self.company_website = [*companywebsite]
        self.description = description

query_dictionary = {
    "ibp" : "htl%3Bjobs",
    "q" : "agriculture++Malawi+",
    "htivrt" : "jobs",
    "htiq" : "agriculture++Malawi+",
    "htilrad" : "300.0"
}

google = f"https://www.google.com/search?ibp={query_dictionary['ibp']}&q={query_dictionary['q']}&htidocid=uY63E0IL9QlKfFqQAAAAAA%3D%3D&hl=en-US&kgs=f2ea076c5a7aaed9&shndl=-1&source=sh%2Fx%2Fim%2Ftextlists%2Fdetail%2Fm1%2F1&ibp=htl%3Bjobs&htidocid=al89beNIYm5QIlhvAAAAAA%3D%3D&ibp=htl%3Bjobs&htidocid=HbJen4buvq57bhiIAAAAAA%3D%3D&mysharpfpstate=tldetail&htivrt={query_dictionary['htivrt']}&htiq={query_dictionary['htiq']}&htidocid=HbJen4buvq57bhiIAAAAAA%3D%3D#htivrt=jobs&fpstate=tldetail&htitab=&htilrad={query_dictionary['htilrad']}&htichips=&htischips=&htidocid=uY63E0IL9QlKfFqQAAAAAA%3D%3D"

def load_request(response):
    data = response.html.find(".gws-plugins-horizon-jobs__li-ed")
    job_list = []
    
    for index, elements  in enumerate(data):

        title = elements.find(".BjJfJf") 
        company = elements.find(".vNEEBe") 
        location_site = elements.find(".Qk80Jf") 
        time = elements.find(".LL4CDc")
        time_data = []
        job_type = []
        company_website = elements.find(".F8xMkc")[0].absolute_links
        description = [ desc.text for desc in elements.find(".YgLbBe")[0].find('span') ]   

        for i in time:
            if "min" not in i.text:
                if "day" not in i.text:
                    job_type.append(i.text)

            if "day" in  i.text:
                time_data.append(i.text)
            
        job = JobObj(
            index,
            title[0].text, 
            company[0].text, 
            location_site[0].text, 
            location_site[1].text, 
            job_type,
            time_data,
            company_website,
            description[0]
            ).__dict__

        job_list.append(job)

    return job_list
    

def session_connection(url_param):
    try:
        session = HTMLSession()
        res = session.get(url_param)
        session_data = load_request(res)
        return session_data

    except:
        print("connection error")
        return []

# export_data = session_connection(google)
export_data = [{'uuid': 0, 'position': 'Sales Executives', 'company': 'Synthesis Agriculture', 'location': 'Malawi', 'site_posted': 'via LinkedIn Malawi', 'job_type': ['Full-time'], 'time_posted': ['2 days ago'], 'company_website': [], 'description': 'The company intends to recruit a suitably qualifie'}, {'uuid': 1, 'position': 'Individual Consultant: Technical Assistant to the Government of...', 'company': 'Alliance for a Green Revolution in Africa (AGRA)', 'location': 'Malawi', 'site_posted': 'via Devex', 'job_type': ['Contractor'], 'time_posted': ['9 days ago'], 'company_website': ['http://www.agra.org/'], 'description': 'Background AGRA’s work in Malawi complements that '}, {'uuid': 2, 'position': 'Chief of Party', 'company': 'NCBA CLUSA', 'location': 'Lilongwe', 'site_posted': 'via SmartRecruiters Job Search', 'job_type': ['Full-time and Contractor'], 'time_posted': [], 'company_website': ['http://www.ncba.coop/'], 'description': 'Company Description The National Cooperative Busin'}, {'uuid': 3, 'position': 'Sustainable agriculture and food security volunteer', 'company': 'CSE MW', 'location': 'Malawi', 'site_posted': 'via CSEMW', 'job_type': ['Volunteer'], 'time_posted': [], 'company_website': [], 'description': 'Volunteers supporting sustainable agricultural com'}, {'uuid': 4, 'position': 'Individual Consultants', 'company': 'Civil Society Agriculture Network (CISANET)', 'location': 'Malawi', 'site_posted': 'via Job Search Malawi', 'job_type': ['Full-time'], 'time_posted': ['6 days ago'], 'company_website': [], 'description': 'INDIVIDUAL CONSULTANCY SERVICES REQUEST FOR EXPRES'}, {'uuid': 5, 'position': 'Spices Manager', 'company': 'JobnetAfrica', 'location': 'Malawi', 'site_posted': 'via JobnetAfrica', 'job_type': ['Full-time'], 'time_posted': ['13 days ago'], 'company_website': [], 'description': 'Vacancy Summary • Field of Expertise: General Mana'}, {'uuid': 6, 'position': 'In-Country Grants Officer', 'company': 'Alliance for a Green Revolution in Africa (AGRA)', 'location': 'Lilongwe', 'site_posted': 'via Job Search Malawi', 'job_type': ['Temp work'], 'time_posted': ['7 days ago'], 'company_website': ['http://www.agra.org/'], 'description': 'Job Reference: AGO/ML/09/2023 About AGRA AGRA and '}, {'uuid': 7, 'position': 'Head Agronomist – Malawi at aQysta Malawi', 'company': 'aQysta Malawi', 'location': 'Lilongwe', 'site_posted': 'via Current Jobs In Malawi 2023', 'job_type': ['Full-time'], 'time_posted': ['14 days ago'], 'company_website': [], 'description': 'Agriculture, Agronomy, Agroforestry BASIC JOB INFO'}, {'uuid': 8, 'position': 'Field agents for Malawi', 'company': 'Trade In Malawi', 'location': 'Malawi', 'site_posted': 'via Trade In Malawi', 'job_type': ['Full-time, Part-time and Contractor'], 'time_posted': [], 'company_website': [], 'description': 'Field agents (Agriculture) for Malawi Job Descript'}, {'uuid': 9, 'position': 'Program Officer – Youth, Gender and Enterprise Development', 'company': 'Alliance for a Green Revolution in Africa (AGRA)', 'location': 'Lilongwe', 'site_posted': 'via Job Search Malawi', 'job_type': ['Temp work'], 'time_posted': ['7 days ago'], 'company_website': ['http://www.agra.org/'], 'description': 'Job Reference: POYGED/ML/09/2023 About AGRA AGRA a'}]



