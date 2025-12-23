import { Injectable } from '@angular/core';

export interface StoredFile {
  file: File;
  preview?: string;
  targetFormat?: string;
}

@Injectable({ providedIn: 'root' })
export class FileStoreService {
  private files: StoredFile[] = [];

  setFiles(files: StoredFile[]) {
    this.files = files;
  }

  getFiles(): StoredFile[] {
    return this.files;
  }

  clear() {
    this.files = [];
  }
}
