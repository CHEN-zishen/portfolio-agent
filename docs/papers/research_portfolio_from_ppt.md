# Zishen Chen - Research Portfolio

## Surgi-Diff

Paper title: Surgi-Diff: A Diffusion-Based Generative Framework for Postoperative Outcome Prediction and Surgical Planning in Adolescent Idiopathic Scoliosis.

Research content: This research proposes Surgi-Diff, a diffusion generative framework integrated with a Spine Alignment Encoder. The framework generates anatomically consistent postoperative spinal X-rays and predicts implant structures for automated preoperative surgical planning and postoperative outcome prediction of adolescent idiopathic scoliosis.

Research results: Experiments on a cohort of 612 AIS patients show that Surgi-Diff achieves the highest SSIM among comparison methods. It accurately predicts fusion segments, rods, and screw distributions, and generates postoperative X-rays highly consistent with real ground truth, demonstrating clinical value for scoliosis surgical decision support.

Key quantitative results:

- Surgi-Diff PSNR: 14.25 ± 2.07 dB.
- Surgi-Diff SSIM: 0.35 ± 0.14, the highest SSIM among the comparison methods listed in the portfolio.
- Fusion level identification accuracy: 75.8% within a 10-pixel tolerance.
- Boundary index error for UIV: 8.40 pixels.
- Boundary index error for LIV: 7.88 pixels.
- Rod centerline error: 2.41 pixels.
- Screw quantity error: 1.09.
- Screw position error: 5.49 pixels.

## G2Net

Paper title: G2Net: A Geometry-Guided Network for Accurate Spine Morphology Estimation from a Single RGB Image of Human Back.

Research content: This study proposes a two-stage geometry-guided G2Net for radiation-free spinal morphology estimation from single back RGB images of AIS patients. In the first stage, it predicts high-fidelity back-surface depth through global-local feature fusion and Mamba modules. In the second stage, it uses RGB-depth cues to train a LoRA-based conditional diffusion model to generate anatomically consistent spine curves.

Research results: Experiments on 2,213 clinical samples show that G2Net surpasses mainstream comparison methods and achieves a spine curve SSIM of 0.950 with low shape errors. Ablation studies verify the necessity of the ConvNeXt image encoder, Mamba-based feature integrator, cross-scale feature fusion module, and cascade upsampling decoder.

Core technical contributions:

- Combines global depth continuity and local image-block detail preservation.
- Uses a Mamba-based feature integrator to improve cross-level feature fusion.
- Uses a cross-scale feature fusion module to enhance semantic-geometric synergy.
- Uses a cascade upsampling decoder to restore resolution progressively and preserve contour fidelity.
- Introduces SpineLoRANet with LoRA blocks for parameter-efficient adaptation.

Representative ablation result:

- The full G2Net model achieves 0.158, 0.060, and 0.011 on the three reported error metrics, with delta metrics of 0.821, 0.940, and 0.976.
- Removing the image encoder, Mamba-based feature integrator, cross-scale feature fusion module, or cascade upsampling decoder degrades performance, confirming that all four modules are necessary.

## MDHGFN

Paper title: MDHGFN: Multiscale Dual Hypergraph Fusion Spatiotemporal Network for Traffic Flow Prediction.

Publication information: Published in Chaos, Solitons and Fractals, an SCI Q1 top journal with a 2026 JCR impact factor of 5.7.

Patent information: An invention patent was filed for a traffic flow prediction method based on multiscale dual hypergraph fusion. Application number: 202510759638.1.

Research content: MDHGFN models traffic flow prediction through multiscale dual hypergraph construction and spatiotemporal feature fusion. It uses microscopic, mesoscopic, and macroscopic dual hypergraphs to capture travel correlation, functional community relationships, and regional conduction patterns.

Datasets: The model is evaluated on PEMS03, PEMS04, PEMS07, and PEMS08, which are public traffic datasets collected by the California Department of Transportation through the Highway Performance Measurement System. The data split follows the baseline setting of 60% training, 20% validation, and 20% testing.

Evaluation metrics: Mean Absolute Error, Mean Absolute Percentage Error, and Root Mean Square Error.

Research results: Evaluation results across all datasets reach state-of-the-art performance. The model performs especially well on large-scale datasets. Ablation results show that joint learning of multiscale dual hypergraphs effectively integrates high-order spatial information at different scales and improves traffic prediction performance.

Representative ablation results:

- On PEMS03, full MDHGFN achieves RMSE 22.52, MAE 14.12, and MAPE 12.95%.
- On PEMS08, full MDHGFN achieves RMSE 25.20, MAE 15.45, and MAPE 11.50%.
- Removing HSAM or TAEM degrades performance, confirming their importance in spatiotemporal modeling.
- The hyperparameter study analyzes K for the functional community dual hypergraph and Top-k for the regional conduction dual hypergraph. The portfolio explains that too-small values miss useful dependency information, while too-large values introduce redundant or irrelevant nodes.

## ScolioLDM

Paper title: ScolioLDM: Towards Accurate Postoperative Radiograph Synthesis for Scoliosis with Morphology-Guided Latent Diffusion Model.

Research content: This work designs ScolioLDM, which uses predicted spine contour maps and a Morphology-Guided Control Module to guide latent diffusion for high-fidelity AIS postoperative X-ray synthesis. The method is validated on a clinical dataset of 612 patients.

Research results: Experiments on 612 AIS cases show that ScolioLDM outperforms mainstream generative models and achieves top PSNR and NCC results. Ablation studies verify that spine contour maps and the Morphology-Guided Control Module are critical for realistic spine and implant reconstruction.

Representative quantitative results:

- ScolioLDM achieves SSIM 0.841 ± 0.011.
- ScolioLDM achieves PSNR 20.436 ± 1.322.
- ScolioLDM achieves MAE 0.032 ± 0.006.
- ScolioLDM achieves GradMAE 0.051 ± 0.006.
- ScolioLDM achieves NCC 0.892 ± 0.035.

Main conclusion: Both quantitative and qualitative results demonstrate that ScolioLDM can synthesize postoperative radiographs with high anatomical fidelity, structural consistency, and visual realism. The Morphology-Guided Control Module and postoperative curve map guidance significantly enhance anatomical accuracy and visual quality.
