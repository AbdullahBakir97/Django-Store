from .models import Company


def get_company_data(request):
    data = Company.objects.last()
    return {'company_data':data}
