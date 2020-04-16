import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CompanyListComponent } from './company-list/company-list.component'
import {CompanyDetailComponent} from './company-detail/company-detail.component';
//import {VacancyListComponent} from "./vacancy-list/vacancy-list.component";


const routes: Routes = [
  {path: '', component: CompanyListComponent},
	{path: 'companies/:companyId/vacancies', component: CompanyDetailComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
