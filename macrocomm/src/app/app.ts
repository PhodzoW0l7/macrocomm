import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DispatctBoard } from './dispatct-board/dispatct-board';

//angular main component connect service to display data to the webpage
@Component({
  selector: 'app-root',
  imports: [CommonModule,DispatctBoard],//marks this as a standalone component
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
      
}
