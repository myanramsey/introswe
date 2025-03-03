import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  constructor(private http: HttpClient) {}

  onSubmit() {
    this.http.post('http://localhost:5000/api/login', { username: this.username, password: this.password })
      .subscribe(
        (response) => console.log('Login successful', response),
        (error) => console.error('Login failed', error)
      );
  }
}
