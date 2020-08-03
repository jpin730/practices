<?php

namespace App\Controllers;

use App\Models\Job;
use Respect\Validation\Validator as v;

class JobsController extends BaseController {
    public function getAddJobAction($request) {       
        // use App\Models\Job;
        // var_dump($_POST);
        // if (!empty($_POST)) {
            //     $job = new Job();
            //     $job->title = $_POST['title'];
            //     $job->description = $_POST['description'];
            //     $job->visible = true;
            //     $job->months = 0;
            //     $job->save();
            // }
        
        // PSR-7 methods (zend-diactoros)
        // var_dump($request->getMethod());
        // var_dump((string)$request->getBody());
        // var_dump($request->getParsedBody());
        
        $responseMessage = null;

        if ($request->getMethod() == 'POST') {
            $postData = $request->getParsedBody();
            $jobValidator =
                v::key('title', v::stringType()->notEmpty())
                ->key('description', v::stringType()->notEmpty());
            
            try {
                $jobValidator->assert($postData);
                
                $postData = $request->getParsedBody();
                
                $files = $request->getUploadedFiles();
                // var_dump($files);
                $logo = $files['logo'];

                if ($logo->getError() == UPLOAD_ERR_OK) {
                    $fileName = $logo->getClientFilename();
                    $logo->moveTo("uploads/$fileName");
                }


                // $job = new Job();
                // $job->title = $postData['title'];
                // $job->description = $postData['description'];
                // $job->visible = true;
                // $job->months = 0;
                // $job->save();

                $responseMessage = 'Saved';

            } catch (\Exception $e) {
                $responseMessage = $e->getMessage();
            }

            // var_dump($jobValidator->validate($postData)); // BOOLEAN WITHOUT REASON WHY

        }
        
        // include '../views/addJob.php';
        return $this->renderHTML('addJob.twig', [
            'responseMessage' => $responseMessage
        ]);
    }
}