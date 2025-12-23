import { Routes } from '@angular/router';
import { ErrorComponent } from './pages/error/error.component';
import { ImportComponent } from './pages/import/import.component';
import { ConvertComponent } from './pages/convert/convert.component';

export const routes: Routes = [
    {path: '', component: ImportComponent},
    {path: 'convert', component: ConvertComponent},

    // error
    {path: 'error', component: ErrorComponent},
    {path: '**', redirectTo: 'error'}
];
