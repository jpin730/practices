<?php

namespace App\Controllers;
use App\Models\{Job, Project};

class IndexController extends BaseController {
    public function indexAction() {
        $jobs = Job::all();

        $project1 = new Project('Project 1', 'Description 1');
        $projects = [$project1];

        /* require_once('jobs.php'); */      
        $name = 'Jaime Pineda';
        $limitMonths = 2000; // TO PRINT LAST X MONTHS 

        // include '../views/index.php';
        return $this->renderHTML('index.twig', [
            'name' => $name,
            'jobs' => $jobs
        ]);
    }
}