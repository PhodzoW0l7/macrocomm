import { Component, inject, OnInit } from '@angular/core';
import { DefaultService } from '../api/generated';
import { CommonModule } from '@angular/common';
import { TableModule } from 'primeng/table';
import { ButtonModule } from 'primeng/button';
import { TagModule } from 'primeng/tag';
import { CardModule } from 'primeng/card';
import { DialogModule } from 'primeng/dialog';
import { ToastModule } from 'primeng/toast';
import { MessageService } from 'primeng/api';
import { SelectModule } from 'primeng/select';
import { RefreshService } from '../services/refresh-service';

type TagSeverity = 'success' | 'secondary' | 'info' | 'warn' | 'danger' | 'contrast' | null | undefined;

@Component({
  selector: 'app-dispatct-board',
  standalone: true,
  imports: [CommonModule, TableModule, ButtonModule, TagModule, CardModule,
    DialogModule, ToastModule, SelectModule],
  providers: [MessageService],
  templateUrl: './dispatct-board.html',
  styleUrls: ['./dispatct-board.css'],
})
export class DispatctBoard implements OnInit{
  incidents: any[] = [];
  summary: any = null;
  showNewDialog = false;
  apiStatus = '';

  constructor(
    private api: DefaultService,
    private messageService: MessageService,
    private refreshService:RefreshService,
  ) {}

   ngOnInit(): void {
    this.checkHealth();
    this.loadIncidents();
    this.loadSummary();

    this.refreshService.incidentChanged$.subscribe(() => {
      this.loadIncidents();
      this.loadSummary();
    });
  }

  

  checkHealth(): void {
    this.api.getApihealthApiHealthGet().subscribe({
      next: (res) => {
        this.apiStatus = res?.message ?? 'API online';
      },
      error: () => {
        this.apiStatus = 'API unreachable';
      },
    });
  }

  loadIncidents(): void {
    this.api.getIncidentsApiIncidentsGet().subscribe({
      next: (data) => {
        this.incidents = data ?? [];
      },
      error: () => {
        this.messageService.add({
          severity: 'error',
          summary: 'Error',
          detail: 'Failed to load incidents. Displaying mock data.',
        });
      },
    });
  }

   loadSummary(): void {
    this.api.getIncidentSummaryApiSummaryGet().subscribe({
      next: (data) => (this.summary = data),
      error: () => console.warn('Summary endpoint unavailable'),
    });
  }

  getSeverityClass(severity: string): TagSeverity {
  const map: Record<string, TagSeverity> = {
    low: 'success',
    medium: 'warn',
    high: 'danger',
    critical: 'contrast',
  };
  return map[severity?.toLowerCase()] ?? 'info';
}

getStatusClass(status: string): TagSeverity {
  const map: Record<string, TagSeverity> = {
    new: 'info',
    assigned: 'secondary',
    in_progress: 'warn', 
    resolved: 'success',
  };
  return map[status?.toLowerCase()] ?? 'secondary';
}

  openNewDialog(): void {
    this.showNewDialog = true;
  }

}
