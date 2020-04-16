import { TestBed } from '@angular/core/testing';

import { VacancyListService } from './vacancy-list.service';

describe('VacancyListService', () => {
  let service: VacancyListService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(VacancyListService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
