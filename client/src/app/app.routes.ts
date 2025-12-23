import { Routes } from '@angular/router';
import { ErrorComponent } from './pages/error/error.component';
import { ImportComponent } from './pages/import/import.component';

export const routes: Routes = [
    {path: '', component: ImportComponent},

    // error
    {path: 'error', component: ErrorComponent},
    {path: '**', redirectTo: 'error'}
];
