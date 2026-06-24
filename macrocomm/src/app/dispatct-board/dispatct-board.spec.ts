import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DispatctBoard } from './dispatct-board';

describe('DispatctBoard', () => {
  let component: DispatctBoard;
  let fixture: ComponentFixture<DispatctBoard>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DispatctBoard]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DispatctBoard);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
