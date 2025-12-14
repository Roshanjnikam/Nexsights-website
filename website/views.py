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
            'title': 'Data Analytics & Insights',
            'desc': 'Transform raw data into actionable business insights.'
        },
        {
            'title': 'Website Development',
            'desc': 'Modern, responsive, and scalable websites built using Django and modern web technologies.'
        },
        {
            'title': 'Machine Learning Solutions',
            'desc': 'Predictive and intelligent ML models for business problems.'
        },
        {
            'title': 'AI Model Development',
            'desc': 'Custom AI models aligned with business goals.'
        },
        {
        'title': 'Business Consulting',
        'desc': 'Strategy-driven consulting using data and AI.'
        }
        
    ]
    return render(request, 'services.html', {'services': services_list})


def contact(request):
    return render(request, 'contact.html')



from django.http import Http404

def service_detail(request, service_slug):
    services = {
        'data-analytics': {
            'title': 'Data Analytics',
            'desc': 'We help businesses turn raw data into actionable insights.',
            'points': [
                'Dashboard & KPI reporting',
                'Customer behavior analysis',
                'Sales & performance insights',
                'Excel, Power BI, Python solutions'
            ]
        },
        'machine-learning': {
            'title': 'Machine Learning',
            'desc': 'Predictive models that automate and improve decision making.',
            'points': [
                'Forecasting models',
                'Recommendation systems',
                'Classification & clustering',
                'Model deployment support'
            ]
        },
        'ai-models': {
            'title': 'AI Model Building',
            'desc': 'Custom AI solutions aligned with your business goals.',
            'points': [
                'Custom AI model design',
                'Model training & tuning',
                'Automation using AI',
                'Scalable solutions'
            ]
        },
        'consulting': {
            'title': 'Business Consulting',
            'desc': 'Data-driven strategy consulting for growth.',
            'points': [
                'Business process optimization',
                'Data-led strategy',
                'Digital transformation',
                'Decision support systems'
            ]
        },
        'website-development': {
            'title': 'Website Development',
            'desc': 'Modern, fast, and scalable websites.',
            'points': [
                'Django-based websites',
                'Responsive design',
                'SEO-friendly structure',
                'Fast & secure deployment'
            ]
        }
    }

    service = services.get(service_slug)

    if not service:
        raise Http404("Service not found")

    return render(request, 'service_detail.html', {'service': service})


