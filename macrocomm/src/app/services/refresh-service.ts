import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class RefreshService {
  private incidentChangedSubject = new Subject<void>();

  incidentChanged$ = this.incidentChangedSubject.asObservable();

  notifyIncidentChanged(): void {
    this.incidentChangedSubject.next();
  }
}
