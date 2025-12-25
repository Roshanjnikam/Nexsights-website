from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')




def about(request):
    return render(request, 'about.html')




def services(request):
    services_list = [
        {
            'title': 'Data Analysis',
            'desc': 'Analyze data to uncover trends, insights, and business opportunities.'
        },
        {
            'title': 'Business Analysis',
            'desc': 'Understand business problems and translate them into data-driven solutions.'
        },
        {
            'title': 'MIS Reporting',
            'desc': 'Automated MIS reports for accurate and timely decision-making.'
        },
        {
            'title': 'Excel & Power BI Dashboards',
            'desc': 'Interactive dashboards for real-time performance tracking.'
        },
        {
            'title': 'Data Cleanup & Automation',
            'desc': 'Clean, validate, and automate data workflows to reduce errors.'
        },
        {
            'title': 'AI Model Building',
            'desc': 'Custom AI and ML models designed to solve real business problems.'
        }
    ]
    return render(request, 'services.html', {'services': services_list})



def contact(request):
    return render(request, 'contact.html')



from django.http import Http404

from django.http import Http404

def service_detail(request, service_slug):
    services = {
        'data-analysis': {
            'title': 'Data Analysis',
            'desc': 'Turn raw data into meaningful insights that support smarter business decisions.',
            'problem': 'Businesses often have data but lack clarity on what it means.',
            'offers': [
                'Sales & performance analysis',
                'Customer behavior insights',
                'Trend & KPI analysis',
                'Excel, SQL & Python analysis'
            ],
            'process': [
                'Understand business objectives',
                'Collect and explore data',
                'Perform analysis and identify insights',
                'Present findings with recommendations',
                'Support decision implementation'
            ],
            'tools': 'Excel, SQL, Python, Pandas, Power BI',
        },

        'business-analysis': {
            'title': 'Business Analysis',
            'desc': 'Understand business problems and convert them into structured solutions.',
            'problem': 'Organizations struggle to convert requirements into clear solutions.',
            'offers': [
                'Requirement gathering (BRD/FRD)',
                'Process & gap analysis',
                'Stakeholder alignment',
                'Solution documentation'
            ],
            'process': [
                'Stakeholder discussions',
                'Requirement documentation',
                'Process mapping & gap analysis',
                'Solution design',
                'Business validation & sign-off'
            ],
            'tools': 'Excel, PowerPoint, Process Mapping Tools',
        },

        'mis-reporting': {
            'title': 'MIS Reporting',
            'desc': 'Automated MIS reporting for accurate and timely management decisions.',
            'problem': 'Manual MIS reports are time-consuming and error-prone.',
            'offers': [
                'Daily / weekly / monthly MIS',
                'Automated reporting',
                'Management dashboards',
                'Data accuracy improvements'
            ],
            'process': [
                'Understand reporting requirements',
                'Identify data sources',
                'Design report structure',
                'Automate report generation',
                'Ongoing monitoring & enhancement'
            ],
            'tools': 'Excel, Power Query, Python Automation',
        },

        'excel-power-bi-dashboards': {
            'title': 'Excel & Power BI Dashboards',
            'desc': 'Interactive dashboards for real-time performance visibility.',
            'problem': 'Static reports fail to provide actionable insights.',
            'offers': [
                'KPI dashboards',
                'Interactive visuals',
                'Drill-down analysis',
                'Automated data refresh'
            ],
            'process': [
                'Define KPIs and metrics',
                'Prepare and model data',
                'Design dashboard visuals',
                'Validate with stakeholders',
                'Deploy and train users'
            ],
            'tools': 'Excel, Power BI, DAX, Power Query',
        },

        'data-cleanup-automation': {
            'title': 'Data Cleanup & Automation',
            'desc': 'Clean, reliable data with automated workflows.',
            'problem': 'Poor data quality leads to incorrect decisions.',
            'offers': [
                'Data cleansing',
                'Validation rules',
                'Workflow automation',
                'Standardized datasets'
            ],
            'process': [
                'Audit existing data',
                'Identify errors and inconsistencies',
                'Apply cleanup rules',
                'Automate recurring processes',
                'Maintain data quality'
            ],
            'tools': 'Python, Excel, SQL',
        },


        'website-development': {
            'title': 'Website Development',
            'desc': 'Professional websites designed for performance, scalability, and business growth.',
            'problem': 'Many businesses struggle with slow, outdated, or unprofessional websites.',
            'offers': [
                'Django-based website development',
                 'Responsive & mobile-friendly design',
                 'SEO-ready structure',
                 'Secure & scalable architecture',
                 'Deployment & hosting support'
            ],
            'process': [
                 'Understand business goals',
                 'Design site structure & UI',
                 'Develop backend & frontend',
                 'Testing & optimization',
                 'Deployment & ongoing support'
            ],
            'tools': 'Django, HTML, CSS, JavaScript, Git, Hosting Platforms',
        },

        
        'sample-work': {
           'title': 'Sample Work & Case Studies',
           'desc': 'A practical showcase of dashboards, reports, automation, and analytics solutions.',
           'is_sample': True,   #
        },



        'ai-model-building': {
            'title': 'AI Model Building',
            'desc': 'Custom AI and ML models built for real business use cases.',
            'problem': 'Businesses want AI but lack deployable solutions.',
            'offers': [
                'Predictive models',
                'Classification systems',
                'Forecasting models',
                'Model deployment support'
            ],
            'process': [
                'Understand use case & data',
                'Prepare and engineer features',
                'Train and tune models',
                'Validate performance',
                'Deploy and monitor models'
            ],
            'tools': 'Python, Scikit-learn, TensorFlow, Pandas',
        }
        
    }

    service = services.get(service_slug)

    if not service:
        raise Http404("Service not found")

    return render(request, 'service_detail.html', {'service': service})
