import { Location } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-footer-back',
  imports: [],
  standalone: true,
  templateUrl: './footer-back.component.html',
  styleUrl: './footer-back.component.sass'
})
export class FooterBackComponent {
  constructor(private location: Location) {}
  goBack() {
    this.location.back();
  }
}
