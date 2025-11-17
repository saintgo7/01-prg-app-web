import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <div class="app">
      <h1>Welcome to Angular!</h1>
      <p>Edit src/app/app.component.ts to get started</p>
    </div>
  `,
  styles: [`
    .app {
      text-align: center;
      padding: 40px;
      font-family: Arial, sans-serif;
    }
    h1 { color: #dd0031; }
  `]
})
export class AppComponent {
  title = 'angular-app';
}
