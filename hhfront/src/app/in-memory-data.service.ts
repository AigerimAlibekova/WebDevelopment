import { Injectable } from '@angular/core';
import { InMemoryDbService } from 'angular-in-memory-web-api';

import { Company } from './interfaces/company';
@Injectable({
  providedIn: 'root'
})
export class InMemoryDataService {
    createDb() {
      const categories = [
        {
          id: 1, name: 'Deloitte', description: 'a', city: 'a', address: 'a'
        },
        {
          id: 2, name: 'PricewaterhouseCoopers', description: 'a', city: 'a', address: 'a'
        },
        {
          id: 3, name: 'Ernst & Young', description: 'a', city: 'a', address: 'a'
        },
        {
          id: 4, name: 'KPMG', description: 'a', city: 'a', address: 'a'
        }
      ];
      return {categories};
    }
}
