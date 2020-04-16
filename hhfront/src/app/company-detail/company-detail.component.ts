import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {VacancyListService} from "../vacancy-list.service";
import { Vacancy, Company } from '../models';

@Component({
  selector: 'app-company-detail',
  templateUrl: './company-detail.component.html',
  styleUrls: ['./company-detail.component.css']
})
export class CompanyDetailComponent implements OnInit {

  company: Company;
  vacancyOfCompany: Vacancy[];

  constructor(private route: ActivatedRoute,
              private vacancyListService: VacancyListService) { }

  ngOnInit(): void {
    this.getVacancyList();
  }
  getVacancyList(){
    const id = +this.route.snapshot.paramMap.get('id');
    this.vacancyListService. getVacancyByCompany(id).subscribe(vs => this.vacancyOfCompany = vs);
  }
}
