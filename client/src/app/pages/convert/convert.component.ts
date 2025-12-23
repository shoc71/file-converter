import { Component, OnInit } from '@angular/core';
import { FileStoreService, StoredFile } from '../../services/file-store.service';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

@Component({
  standalone: true,
  selector: 'app-convert',
  imports: [FormsModule],
  templateUrl: './convert.component.html'
})
export class ConvertComponent implements OnInit {
  files: StoredFile[] = [];
  uploading: boolean = false;

  constructor(
    private fileStore: FileStoreService,
    private http: HttpClient
  ) {}

  ngOnInit() {
    this.files = this.fileStore.getFiles();
    for (const item of this.files) {
      item.targetFormat = this.getTargetFormat(item.file);
    }
  }

  // Determine per-file default target
  getTargetFormat(file: File): string {
    if (file.type === 'application/pdf') return 'png';
    if (file.type.includes('word')) return 'pdf';
    if (file.type === 'text/plain') return 'png';
    return 'pdf';
  }

  convertFile(item: StoredFile) {
    const formData = new FormData();
    formData.append('file', item.file);
    formData.append('target_format', item.targetFormat || 'pdf');

    this.uploading = true;
    this.http.post('https://YOUR-RENDER-BACKEND.onrender.com/convert/', formData, { responseType: 'blob' })
      .subscribe(blob => {
        const url = URL.createObjectURL(blob);
        item.preview = url;
        this.uploading = false;
      }, err => {
        console.error(err);
        this.uploading = false;
      });
  }
}
