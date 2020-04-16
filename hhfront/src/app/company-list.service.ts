import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';
//import {Company} from './interfaces/company';
import {Company} from "./models";
import { HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CompanyListService {
  private categoriesUrl = 'api/categories';


  getCompany(): Observable<Company[]> {
    return this.http.get<Company[]>(this.categoriesUrl);
  }

  constructor(private http: HttpClient) { }
}
