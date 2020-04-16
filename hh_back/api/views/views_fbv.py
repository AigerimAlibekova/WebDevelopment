import json
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.request import Request
from  rest_framework.response import Response

from django.http.request import HttpRequest
from django.http.response import HttpResponse

from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer

@api_view(['GET', 'POST'])
def companies_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many = True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        request_body = json.loads(request.body)

        serializer = CompanySerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse({'error': serializer.errors},
                        status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        company.delete()

        return Response({'deleted': True})

@api_view(['GET'])
def vacancies_by_company(request, company_id):
		try:
			company = Company.objects.get(id = company_id)
			serializer = CompanySerializer(company, many = True)
		except Company.DoesNotExist as e:
			return Response({'error': str(e)})

		if request.method == "GET":
			vacancies = company.vacancy_set.all();
			serializer = VacancySerializer(vacancies, many = True)
			return Response(serializer.data)

@api_view(['GET', 'POST'])
def vacancies_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many = True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        request_body = json.loads(request.body)

        serializer = VacancySerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def vacancies_detail(request, company_id):
    try:
        vacancy = Vacancy.objects.get(id= vacancy_id)
    except Vacancy.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        vacancy.delete()

        return Response({'deleted': True})

@api_view(['GET'])
def top_vacancies(request):
	if request.method == "GET":
		vacancies = Vacancy.objects.order_by('-salary')[:10]
		serializer = VacancySerializer(vacancies, many = True)
		return Response(serializer.data)
