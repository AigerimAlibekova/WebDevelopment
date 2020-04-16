export class Company {
	id: number;
	description: string;
	city: string;
	address: string;
	vacancies: Vacancy[];
}

export class Vacancy {
	id: number;
	description: string;
	salary: number;
}

export class LoginResponse {
  token: string;
}
