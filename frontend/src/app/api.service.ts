import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://127.0.0.1:5000/api';

  constructor(private http: HttpClient) { }

  testConnection(): Observable<any> {
    return this.http.get(`${this.apiUrl}/test`);
  }
}
