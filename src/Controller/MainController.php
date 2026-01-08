<?php

namespace App\Controller;

use Parsedown;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\BinaryFileResponse;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpFoundation\ResponseHeaderBag;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\Filesystem\Filesystem;

class MainController extends AbstractController
{
    #[Route('/', name: 'accueil')]
    public function home(): Response
    {
        $projectRoot = $this->getParameter('kernel.project_dir');
        $reportPath = $projectRoot . DIRECTORY_SEPARATOR . 'Network_Report.md';

        $reportContentRaw = "Le rapport n'a pas encore été généré. Cliquez sur « Actualiser » pour lancer l'analyse.";

        if (file_exists($reportPath)) {
            $reportContentRaw = file_get_contents($reportPath);
        }

        // Transformation Markdown -> HTML
        $parsedown = new Parsedown();
        $reportContentHtml = $parsedown->text($reportContentRaw);

        return $this->render('main/accueil.html.twig', [
            'reportContent' => $reportContentHtml,
        ]);
    }

    #[Route('/run-python', name: 'run_python')]
    public function runPython(): Response
    {
        $projectRoot = $this->getParameter('kernel.project_dir');
        $scriptsDir = $projectRoot . DIRECTORY_SEPARATOR . 'scripts';

        // Commande Windows : se placer dans scripts/ puis lancer les deux scripts
        $command = "cd /d $scriptsDir && python txt_csv.py && python csv_to_md.py";
        shell_exec($command);

        $this->addFlash('success', 'Analyse terminée avec succès ! Le rapport a été mis à jour.');
        return $this->redirectToRoute('accueil');
    }

    #[Route('/export-report', name: 'export_report')]
    public function exportReport(): Response
    {
        $projectRoot = $this->getParameter('kernel.project_dir');
        $reportPath = $projectRoot . DIRECTORY_SEPARATOR . 'Network_Report.md';

        if (!file_exists($reportPath)) {
            $this->addFlash('warning', "Aucun rapport à exporter pour l'instant.");
            return $this->redirectToRoute('accueil');
        }

        // Téléchargement du fichier Markdown
        return $this->file(
            $reportPath,
            'Network_Report.md',
            ResponseHeaderBag::DISPOSITION_ATTACHMENT
        );
    }

    #[Route('/mark-report-reviewed', name: 'mark_report_reviewed')]
    public function markReportReviewed(): Response
    {
        $this->addFlash('success', 'Ce rapport a été marqué comme analysé.');
        return $this->redirectToRoute('accueil');
    }

    #[Route('/mon_portfolio', name: 'mon_portfolio')]
    public function portfolio(): Response
    {
        return $this->render('main/mon_portfolio.html.twig');
    }
    #[Route('/reset-report', name: 'reset_report')]
public function resetReport(): Response
    {
        $projectRoot = $this->getParameter('kernel.project_dir');
        $reportPath = $projectRoot . DIRECTORY_SEPARATOR . 'Network_Report.md';

        $fs = new Filesystem();

        if ($fs->exists($reportPath)) {
            $fs->remove($reportPath); // supprime le fichier de rapport
            $this->addFlash('success', 'Le rapport a été réinitialisé.');
        } else {
            $this->addFlash('warning', "Aucun rapport à réinitialiser.");
        }
        return $this->redirectToRoute('accueil');
    }
}