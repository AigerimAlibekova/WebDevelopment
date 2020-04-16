import { Component, OnInit } from '@angular/core';

import {ActivatedRoute} from "@angular/router";
import {Company} from '../../interfaces/company';
import {CompanyListService} from '../../company-list.service'

@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html',
  styleUrls: ['./company-list.component.css']
})
export class CompanyListComponent implements OnInit {

  constructor( private route: ActivatedRoute, private companyListService: CompanyListService) { }

    companies: Company[];

  ngOnInit(): void {
    this.getCompany();
  }

  getCompany(): void {
    this.companyListService.getCompany().subscribe(companies => this.companies = companies);
  }

}
