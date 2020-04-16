from django.shortcuts import render

# Create your views here.
#функции,которые обрабатываеют request? возвр response

from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from api.models import Company, Vacancy
from django.http import Http404
from django.db.models import Count

def companies_list(request):
	if request.method == "GET":
		companies = Company.objects.all()
		companies_json = [company.to_json() for company in companies]
		return JsonResponse(companies_json, safe=False)

def company_detail(request, company_id):
	if request.method == "GET":
		try:
			company = Company.objects.get(id=company_id)
		except Company.DoesNotExist as e:
			return JsonResponse({'error': 'company does not exist'})

		return JsonResponse(company.to_json())

def vacancies_by_company(request, company_id):
	if request.method == "GET":
		try:
			company = Company.objects.get(id=company_id)
		except Company.DoesNotExist as e:
			return JsonResponse({'error': 'does not exist'})

		vacancies = company.vacancy_set.all();
		vacancies_json = [vacancy.to_json() for vacancy in vacancies]
		return JsonResponse(vacancies_json, safe=False)

def vacancies_list(request):
	if request.method == "GET":
		vacancies = Vacancy.objects.all()
		vacancies_json = [vacancy.to_json() for vacancy in vacancies]
		return JsonResponse(vacancies_json, safe=False)

def vacancies_detail(request, vacancy_id):
	if request.method == "GET":
		try:
			vacancy = Vacancy.objects.get(id=vacancy_id)
		except Vacancy.DoesNotExist as e:
			return JsonResponse({'error': 'does not exist'})
		return JsonResponse(vacancy.to_json())

def top_vacancies(request):
	if request.method == "GET":
		vacancies = Vacancy.objects.annotate(Count('salary')).order_by('-salary')[:10]
		vacancies_json = [vacancy.to_json() for vacancy in vacancies]
		return JsonResponse(vacancies_json, safe = False)