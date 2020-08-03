<?php
use App\Models\{Job, Project};

/* $job1 = new Job('PHP Developer', 'This is an awesome job!!!');
$job1->months = 16;

$job2 = new Job('Python Developer', 'This is an awesome job!!!');
$job2->months = 24;

$job3 = new Job('Devops', 'This is an awesome job!!!');
$job3->months = 32; */

/* $jobs = [
  $job1,
  $job2,
  $job3
]; */

$jobs = Job::all();

$project1 = new Project('Project 1', 'Description 1');

$projects = [
    $project1
];