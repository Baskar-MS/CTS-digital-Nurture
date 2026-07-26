import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { CourseCard } from '../course-card/course-card';
import { CourseService } from '../course';

@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [CommonModule, FormsModule, CourseCard],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css',
})
export class CourseList implements OnInit {

  // Search text for filtering courses
  searchText: string = '';

  // Stores API data
  courses: any[] = [];

  // Loading spinner flag
  loading: boolean = true;

  // Dependency Injection
  constructor(private courseService: CourseService) {}

  // Called automatically when the component loads
  ngOnInit(): void {

    this.loading = true;

    this.courseService.getCourses().subscribe({

      next: (data) => {
        this.courses = data;
        this.loading = false;
      },

      error: (error) => {
        console.error('Error fetching courses:', error);
        this.loading = false;
      }

    });

  }

  // Search filter
  get filteredCourses() {
    return this.courses.filter(course =>
      (course.title || '')
        .toLowerCase()
        .includes(this.searchText.toLowerCase())
    );
  }

}