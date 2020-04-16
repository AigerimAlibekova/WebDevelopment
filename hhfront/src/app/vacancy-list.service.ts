import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {Vacancy} from './models';
// import {ProductList} from '../data/product-list';
// import {CategoryList} from '../data/category-list';
import {HttpClient} from '@angular/common/http';
import {catchError} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class VacancyListService {
  private companiesUrl = 'api/companies';
  private vacanciesUrl = 'api/vacancies';
  vacancies: Vacancy[];

    getVacancyByCompany(id: number): Observable<Vacancy[]> {
    const url = `${this.vacanciesUrl}/?company=${id}`;
    return this.http.get<Vacancy[]>(url);
  }
  constructor(private http: HttpClient) { }
}
