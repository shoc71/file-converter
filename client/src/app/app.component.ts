import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass'],
})
export class AppComponent {
  title = 'client';

  files: File[] = [];
  previews: { file: File; url?: string }[] = [];
  dragOver = false;

  // Handle files from input or drag-drop
  onFilesSelected(event: Event | FileList) {
    let selectedFiles: File[] = [];

    if (event instanceof FileList) {
      selectedFiles = Array.from(event);
    } else {
      const input = event.target as HTMLInputElement;
      if (!input.files) return;
      selectedFiles = Array.from(input.files);
      input.value = '';
    }

    // Add new files without replacing old ones
    for (const file of selectedFiles) {
      if (!this.files.find(f => f.name === file.name && f.size === file.size)) {
        this.files.push(file);

        if (file.type.startsWith('image/')) {
          const reader = new FileReader();
          reader.onload = () => {
            this.previews.push({ file, url: reader.result as string });
          };
          reader.readAsDataURL(file);
        } else {
          // non-image placeholder
          const placeholder = this.getRandomPlaceholder(file);
          console.log('Placeholder path:', placeholder);
          this.previews.push({ file, url: placeholder });
        }
      }
    }
  }

  // helper to return a random placeholder for docs/pdfs/txt
  getRandomPlaceholder(file: File): string {
    const ext = file.name.split('.').pop()?.toLowerCase();
    const basePath = 'assets/file-icons/';

    if (ext === 'pdf') {
      const idx = Math.floor(Math.random() * 4) + 1;
      return `${basePath}pdf${idx}.png`;
    } else if (ext === 'doc' || ext === 'docx') {
      const idx = Math.floor(Math.random() * 4) + 1;
      return `${basePath}doc${idx}.png`;
    } else if (ext === 'txt') {
      const idx = Math.floor(Math.random() * 4) + 1;
      return `${basePath}txt${idx}.png`;
    }

    // fallback icon
    return `${basePath}folder.png`;
  }

  // Remove a file
  removeFile(index: number) {
    this.previews.splice(index, 1);
    this.files.splice(index, 1);
  }

  // Example confirm button
  confirmSelection() {
    console.log('Selected files:', this.files);
    // Navigate to next page logic goes here
  }

  // Drag & Drop handlers
  onDragOver(event: DragEvent) {
    event.preventDefault();
    event.stopPropagation();
    this.dragOver = true;
  }

  onDragLeave(event: DragEvent) {
    event.preventDefault();
    this.dragOver = false;
  }

  onDrop(event: DragEvent) {
    event.preventDefault();
    event.stopPropagation();
    this.dragOver = false;

    if (event.dataTransfer?.files) {
      this.onFilesSelected(event.dataTransfer.files);
    }
  }
}
