from .config import BASE_DIR, COMPETITION_DIR, RESEARCH_DIR, PROJECTS_DIR

# Edit this dictionary directly to update the profile card.
PERSONAL_INFO = {
    "Name": "Zishen Chen",
    "Date of Birth": "July 26, 2004",
    "University": "Shantou University",
    "Major": "Data Science and Big Data Technology",
    "GPA": "4/5",
    "Academic Ranking": "Top 10%",
    "Research Interests": "Generative AI, Visual Depth Estimation, Traffic Flow Prediction, AI Large Models, Computer Vision",
    "Technical Stack": "Python / Diffusion Models / LoRA / Mamba / Hypergraph Neural Networks / Data Visualization / Web Application Technology",
    "Career Goal": "AI Research / Machine Learning Engineer / Large-scale AI Application Developer",
}

MAIN_COURSES = [
    {"name": "Principles of Computer Organization", "score": 95, "icon": "💻"},
    {"name": "Human-computer interaction", "score": 94, "icon": "🤝"},
    {"name": "Data Acquisition Technology", "score": 95, "icon": "📊"},
    {"name": "Web application technology", "score": 93, "icon": "🌐"},
    {"name": "Data Structures and Algorithms", "score": 93, "icon": "🧠"},
    {"name": "Cloud computing and data centers", "score": 93, "icon": "☁️"},
    {"name": "Data Visualization", "score": 97, "icon": "📈"},
    {"name": "Biological and medical big data", "score": 96, "icon": "🧬"},
    {"name": "Large Language Models & Agent Theory", "score": 98, "icon": "🤖"},
    {"name": "Parallel Computing", "score": 94, "icon": "⚡"},
]

RESEARCH_DIRECTIONS = [
    {
        "title": "Generative Artificial Intelligence",
        "description": "Focus on diffusion models and controllable generation, especially morphology-guided medical image synthesis, postoperative radiograph generation, and AI-assisted content generation.",
        "projects": ["ScolioLDM", "Surgi-Diff"],
    },
    {
        "title": "Visual Depth Estimation",
        "description": "Study monocular visual depth estimation, RGB back-image depth reconstruction, global-local feature fusion, and geometry-guided radiation-free spine morphology estimation.",
        "projects": ["G²Net"],
    },
    {
        "title": "Traffic Flow Prediction",
        "description": "Explore spatiotemporal forecasting, multiscale dual hypergraph learning, and high-order dependency modeling for urban traffic network prediction.",
        "projects": ["MDHGFN"],
    },
    {
        "title": "Future Research: AI Large Models & Computer Vision",
        "description": "Plan to further investigate multimodal large models, computer vision, medical vision-language systems, and intelligent perception for real-world AI applications.",
        "projects": ["AI Large Models", "Computer Vision", "Multimodal AI"],
    },
]

INTERNSHIP_EXPERIENCES = [
    {
        "organization": "AIMed Lab, Department of Orthopaedics and Traumatology, The University of Hong Kong",
        "role": "Research Internship",
        "period": "2025.10 - 2026.03",
        "icon": BASE_DIR / "data" / "4648bb29690ecb6955b67ca2b81b883-removebg-preview.png",
        "work": [
            "Collected and standardized over 1,000 paired preoperative and postoperative X-ray images, building a rigorously matched medical imaging dataset.",
            "Used Photoshop and open-source super-resolution methods such as ESRGAN and SRGAN to enhance low-quality X-ray images.",
            "Developed Diffusion-based radiograph generation and medical image translation experiments with reference to cGAN, CycleGAN, MeanFlow, VAE, and Transformer-based methods.",
            "Benchmarked G²Net against Depth Anything and Marigold for human back-image depth estimation, supporting 3D structure estimation and surgical planning analysis.",
        ],
        "outcomes": [
            "Independently developed the ScolioLDM model and submitted the first-author manuscript to IEEE TBME.",
            "Received the HKIE Transactions Best Paper Award from the Hong Kong Institution of Engineers.",
            "Designed and implemented the G²Net geometry-guided network, with the first-author manuscript submitted to IEEE JBHI.",
        ],
    },
    {
        "organization": "Key Laboratory of Creative Industry and Big Data, Guizhou University",
        "role": "Research Internship",
        "period": "2024.09 - 2025.02",
        "icon": BASE_DIR / "data" / "image-removebg-preview (3).png",
        "work": [
            "Built spatial perception modules with PyTorch and DGL, modeling static and dynamic graph representations with gated mechanisms and multi-head attention.",
            "Designed temporal perception modules using dynamic temporal convolution and temporal multi-head attention to capture short-term fluctuation and long-term trend patterns in traffic flow.",
        ],
        "outcomes": [
            "Published research on traffic flow prediction in Chaos, Solitons and Fractals, a TOP SCI Q1 journal.",
            "Independently designed and open-sourced a traffic-flow prediction visualization system based on urban functional-area relationships.",
            "Co-invented an invention patent for a multiscale dual-hypergraph traffic-flow prediction method.",
        ],
    },
    {
        "organization": "Guangzhou Xinyi Technology Co., Ltd.",
        "role": "Technical Department Internship",
        "period": "2025.06 - 2025.09",
        "icon": BASE_DIR / "data" / "image-removebg-preview (2).png",
        "work": [
            "Developed targeted web crawlers with Python, Scrapy, Requests, and BeautifulSoup to collect structured and semi-structured patent database records.",
            "Processed more than 10,000 records and completed data cleaning, deduplication, standardization, and field extraction with Pandas, NumPy, regular expressions, and text matching.",
            "Performed statistical analysis and feature modeling on patent data, then built Excel and Power BI dashboards for technology distribution and innovation-trend analysis.",
        ],
        "outcomes": [
            "Produced technical analysis reports and visualization dashboards to support business decision-making.",
        ],
    },
]

MDHGFN_DIR = RESEARCH_DIR / "research papers" / "MDHGFN"
HK_AWARD_DIR = RESEARCH_DIR / "research papers" / "hk_award"
SCOLIOLDM_DIR = RESEARCH_DIR / "research papers" / "ScolioLDM"

RESEARCH_PAPERS = [
    {
        "id": "mdhgfn",
        "title": "MDHGFN: Multiscale Dual Hypergraph Fusion Spatiotemporal Network for Traffic Flow Prediction",
        "tag": "Traffic Flow Prediction",
        "venue": "Chaos, Solitons and Fractals | SCI Q1",
        "cover": MDHGFN_DIR / "Cover.png",
        "pdf": MDHGFN_DIR / "Chaos_Solitons_Fractals.pdf",
        "summary": "A spatiotemporal prediction framework that constructs multiscale dual hypergraphs to model microscopic travel correlations, mesoscopic functional communities, and macroscopic regional conduction patterns in road networks.",
        "explanation": "The work addresses the limitation of low-order graph structures in traffic forecasting. By jointly learning multiple dual hypergraphs, the model captures high-order spatial dependencies across different traffic scales and improves prediction on PEMS benchmark datasets.",
        "contribution": "Designed the multiscale dual hypergraph modeling idea, validated it against 14 baseline methods, and supported the work with ablation studies on HSAM, TAEM, and hypergraph scale combinations.",
        "highlights": ["SCI Q1 journal", "PEMS03/04/07/08 benchmarks", "Invention patent filed"],
        "experiment_focus": "The experimental section evaluates forecasting accuracy on PEMS03, PEMS04, PEMS07, and PEMS08 using MAE, RMSE, and MAPE. It compares 14 baselines and shows that the complete model improves large-scale traffic forecasting through multiscale dual hypergraph learning.",
        "experiment_pages": [9, 10, 12, 13, 14, 15],
        "figure_note": "Use the architecture and result-table pages to explain how microscopic, mesoscopic, and macroscopic hypergraphs contribute to the final traffic prediction performance.",
        "portfolio_pages": [9, 10, 11, 13, 14],
        "gallery": {
            "figures": [
                {
                    "file": MDHGFN_DIR / "figure1.pdf",
                    "title": "Figure 1: Overall Architecture of MDHGFN",
                    "description": "The overall framework of the proposed Multiscale Dual Hypergraph Fusion Spatiotemporal Network. It shows the input traffic flow features, the multiscale dual hypergraph construction module at three scales (microscopic, mesoscopic, macroscopic), the Hypergraph Spatial Attention Module (HSAM), the Temporal Adaptive Enhancement Module (TAEM), the multi-scale fusion layer, and the final prediction output layer with predicted traffic flow distributions.",
                    "section": "Methodology"
                },
                {
                    "file": MDHGFN_DIR / "figure2.pdf",
                    "title": "Figure 2: Hypergraph Construction Mechanism",
                    "description": "Detailed visualization of the dual hypergraph construction at different scales. (a) Microscopic travel correlation hypergraph modeling individual road segment interactions. (b) Mesoscopic functional community hypergraph capturing urban district-level patterns. (c) Macroscopic regional conduction hypergraph showing cross-region propagation. (d) Hypergraph edge and node aggregation mechanism demonstrating high-order message passing.",
                    "section": "Methodology"
                },
                {
                    "file": MDHGFN_DIR / "figure3.pdf",
                    "title": "Figure 3: Qualitative Prediction Visualization",
                    "description": "Visual comparison of traffic flow prediction results on PEMS04 and PEMS08 datasets. The heatmaps show ground truth vs. MDHGFN predictions across 12 time steps (15min to 60min horizons). The zoomed windows highlight peak-hour prediction accuracy and edge-case handling, demonstrating that MDHGFN preserves fine-grained spatiotemporal patterns better than baselines.",
                    "section": "Results"
                },
                {
                    "file": MDHGFN_DIR / "figure4.pdf",
                    "title": "Figure 4: Ablation Visualization & Convergence",
                    "description": "Left: Training convergence curves comparing the full MDHGFN model against its ablated variants (w/o micro-hypergraph, w/o meso-hypergraph, w/o HSAM, w/o TAEM) on PEMS04. Right: Spatial attention heatmaps visualizing learned hypergraph adjacency patterns at each scale, showing that the model learns semantically meaningful connectivity (commuting corridors, functional districts, regional flows).",
                    "section": "Analysis"
                },
            ],
            "tables": [
                {
                    "file": MDHGFN_DIR / "table1.pdf",
                    "title": "Table 1: Performance on PEMS03 and PEMS04",
                    "description": "Quantitative comparison of 14 baseline methods (AGCRN, ASTGCN, DMSTGCN, DCRNN, Graph WaveNet, MTGNN, STGCN, STSGCN, etc.) vs. MDHGFN on PEMS03 (358 sensors) and PEMS04 (307 sensors) at horizons 15min / 30min / 60min. Metrics: MAE, RMSE, MAPE (%). MDHGFN consistently outperforms all baselines, with improvements most pronounced at longer horizons (60 min), confirming the value of multi-scale high-order hypergraph dependencies.",
                    "section": "Quantitative Results"
                },
                {
                    "file": MDHGFN_DIR / "table2.pdf",
                    "title": "Table 2: Performance on PEMS07 and PEMS08",
                    "description": "Quantitative comparison on PEMS07 (883 sensors, large rural-urban network) and PEMS08 (170 sensors, dense urban arterial network). MDHGFN improves over the strongest baselines (e.g., MTGNN, AGCRN) especially in MAPE for PEMS07, indicating robustness to heterogeneous road-network topology scales.",
                    "section": "Quantitative Results"
                },
                {
                    "file": MDHGFN_DIR / "table3.pdf",
                    "title": "Table 3: Ablation Study - Module Contribution",
                    "description": "Ablation of MDHGFN on all four datasets to validate each module: (1) w/o Micro-HG: removing microscopic travel hypergraph degrades short-horizon MAE by 4.2-5.8%; (2) w/o Meso-HG: removing mesoscopic community hypergraph degrades medium-horizon MAE by 3.5-4.9%; (3) w/o Macro-HG: removing macroscopic regional hypergraph degrades long-horizon MAE by 5.1-6.7%; (4) w/o HSAM + w/o TAEM: attention/temporal modules together account for 7-9% accuracy. All modules are statistically necessary.",
                    "section": "Ablation"
                },
                {
                    "file": MDHGFN_DIR / "table4.pdf",
                    "title": "Table 4: Parameter Analysis & Computational Cost",
                    "description": "Sensitivity analysis for hyperparameters (hypergraph K-order, hidden channels, attention heads) and model complexity comparison. MDHGFN has comparable parameters to MTGNN but lower inference latency per batch due to sparse hypergraph aggregation, confirming it is an efficient and practical spatiotemporal learner.",
                    "section": "Analysis"
                },
            ]
        }
    },
    {
        "id": "g2net",
        "title": "G²Net: A Geometry-Guided Network for Accurate Spine Morphology Estimation from a Single RGB Image",
        "tag": "Medical AI",
        "venue": "Clinical AIS Dataset",
        "cover": RESEARCH_DIR / "research papers" / "G²Net.png",
        "pdf": RESEARCH_DIR / "research papers" / "G2.pdf",
        "summary": "A two-stage geometry-guided framework for radiation-free spine morphology estimation from a single RGB back image of AIS patients.",
        "explanation": "G²Net first estimates high-fidelity back-surface depth using global-local feature fusion and Mamba-based integration, then uses RGB-depth conditions to generate anatomically consistent spine curves with a LoRA-based conditional diffusion model.",
        "contribution": "Built a geometry-aware pipeline that balances global depth continuity and local anatomical detail. Ablation studies verify the value of the image encoder, Mamba integrator, cross-scale fusion, and cascade upsampling decoder.",
        "highlights": ["2,213 clinical samples", "Spine curve SSIM 0.950", "Radiation-free estimation"],
        "experiment_focus": "The experiments compare depth estimation and spine morphology generation quality on 2,213 clinical AIS samples. The ablation results show that the image encoder, Mamba-based feature integrator, cross-scale fusion module, and cascade upsampling decoder are all necessary for accurate anatomical estimation.",
        "experiment_pages": [4, 5, 6, 7, 8],
        "figure_note": "The most important visuals are the framework diagram, qualitative spine morphology comparisons, and ablation tables showing the impact of each module.",
        "portfolio_pages": [4, 5, 6, 7, 8],
    },
    {
        "id": "smo_diff",
        "title": "SMO-Diff: A Spinal Morphology Oriented Diffusion Model for Postoperative Radiographic Outcomes Prediction in Scoliosis Surgery",
        "tag": "Diffusion Model",
        "venue": "AIS Surgical Outcome Prediction",
        "cover": RESEARCH_DIR / "research papers" / "SMO_Diff.png",
        "pdf": RESEARCH_DIR / "research papers" / "SMO_Diff__A_Spinal_Morphology_Oriented_Diffusion_Model_for_Postoperative_Radiographic_Outcomes_Prediction_in_Scoliosis_Surgery.pdf",
        "summary": "A spinal morphology oriented diffusion model for predicting postoperative radiographic outcomes in scoliosis surgery with enhanced anatomical consistency.",
        "explanation": "SMO-Diff integrates spinal morphology features into the diffusion process, enabling accurate prediction of postoperative radiographs by conditioning on preoperative spine geometry and surgical planning parameters.",
        "contribution": "Developed a morphology-aware diffusion framework that explicitly models spinal structure and surgical instrumentation, validated through quantitative comparisons and clinical case studies.",
        "highlights": ["AIS surgical planning", "Morphology-guided diffusion", "Postoperative radiograph prediction"],
        "experiment_focus": "The experiments evaluate postoperative radiograph synthesis quality and surgical outcome prediction accuracy on clinical AIS datasets. Quantitative metrics include SSIM, PSNR, MAE, and NCC, with ablation studies validating the morphology-guided design.",
        "experiment_pages": [1, 2, 3, 4, 5],
        "figure_note": "Key visuals include the SMO-Diff framework, qualitative synthesis comparisons, quantitative results, and ablation studies demonstrating morphology guidance impact.",
        "portfolio_pages": [1, 2, 3, 4, 5],
    },
    {
        "id": "scolioldm",
        "title": "ScolioLDM: Morphology-Guided Latent Diffusion for Postoperative Radiograph Synthesis",
        "tag": "Diffusion Model",
        "venue": "AIS Postoperative X-ray Synthesis",
        "cover": RESEARCH_DIR / "research papers" / "ScolioLDM.png",
        "pdf": RESEARCH_DIR / "research papers" / "ScolioLDM Towards Accurate Postoperative Radiograph Synthesis for Scoliosis with Morphology-Guided Latent Diffusion Model.pdf",
        "summary": "A morphology-guided latent diffusion model for synthesizing postoperative scoliosis radiographs with high anatomical fidelity and visual realism.",
        "explanation": "The method uses predicted spine contour maps and a Morphology-Guided Control Module to guide the denoising process, improving structural consistency for postoperative spine and implant reconstruction.",
        "contribution": "Introduced morphology-guided control into latent diffusion and validated the design through quantitative comparisons and ablations on 612 AIS cases.",
        "highlights": ["612 AIS cases", "Top PSNR and NCC", "MGCM ablation validated"],
        "experiment_focus": "The experimental section compares ScolioLDM with ControlNet, pix2pix, ControlNeXt, BBDM, and Fast-DDPM. It reports SSIM, PSNR, MAE, GradMAE, and NCC, and uses ablations to verify that MGCM and postoperative curve maps improve anatomical fidelity.",
        "experiment_pages": [16, 17, 18],
        "figure_note": "Use the model framework, qualitative comparison, and quantitative table pages to explain why morphology-guided control matters for postoperative X-ray synthesis.",
        "portfolio_pages": [16, 17, 18],
        "gallery": {
            "figures": [
                {
                    "file": SCOLIOLDM_DIR / "figure1.pdf",
                    "title": "Figure 1: Failure Cases of Generic Generative Models",
                    "description": "Illustration of direct postoperative radiograph synthesis using mainstream conditional generative models. DDIB and pix2pix fail to preserve postoperative spinal anatomy and implant configuration, producing structural artifacts and distorted regions compared with the GT postoperative radiograph.",
                    "section": "Motivation"
                },
                {
                    "file": SCOLIOLDM_DIR / "figure2.pdf",
                    "title": "Figure 2: Overall ScolioLDM Framework",
                    "description": "Overview of ScolioLDM. A preoperative radiograph and predicted postoperative spine contour map guide the latent diffusion model. The Morphology-Guided Conditioning Module injects morphology-aware control features into the denoising U-Net for anatomically consistent postoperative radiograph synthesis.",
                    "section": "Methodology"
                },
                {
                    "file": SCOLIOLDM_DIR / "figure3.pdf",
                    "title": "Figure 3: Morphology-Guided Conditioning Module",
                    "description": "Detailed architecture of MGCM. The module combines deform refinement, spatial gating, deformation-field prediction, adaptive scaling, and differentiable grid sampling to align structural morphology features before injecting them into the diffusion process.",
                    "section": "Methodology"
                },
                {
                    "file": SCOLIOLDM_DIR / "figure4.pdf",
                    "title": "Figure 4: Ablation Visual Comparison",
                    "description": "Visual comparison between the full ScolioLDM model and variants without MGCM or postoperative curve map guidance. The complete model preserves clearer vertebral structures, better spinal correction, and more coherent screw-rod implant configurations.",
                    "section": "Ablation"
                },
                {
                    "file": SCOLIOLDM_DIR / "figure5.pdf",
                    "title": "Figure 5: Qualitative Comparison with Baselines",
                    "description": "Qualitative comparison with ControlNet, pix2pix, ControlNeXt, BBDM, and Fast-DDPM. ScolioLDM generates postoperative radiographs that more closely resemble GT in spinal correction morphology and implant placement.",
                    "section": "Results"
                },
            ],
            "tables": [
                {
                    "file": SCOLIOLDM_DIR / "table1.pdf",
                    "title": "Table 1: Quantitative Comparison on Postoperative Radiograph Synthesis",
                    "description": "Comparison against ControlNet, pix2pix, ControlNeXt, BBDM, and Fast-DDPM using SSIM, PSNR, MAE, GradMAE, and NCC. ScolioLDM achieves the best PSNR, MAE, GradMAE, and NCC, with competitive SSIM.",
                    "section": "Quantitative Results"
                },
                {
                    "file": SCOLIOLDM_DIR / "table2.pdf",
                    "title": "Table 2: Ablation Study on MGCM and Curve Map Guidance",
                    "description": "Ablation of MGCM and postoperative curve map guidance. Removing the curve map causes the largest degradation, confirming that explicit morphology guidance is central to ScolioLDM.",
                    "section": "Ablation"
                },
            ]
        },
    },
    {
        "id": "surgidiff",
        "title": "Surgi-Diff: Diffusion-Based Surgical Planning and Outcome Prediction for AIS",
        "tag": "Surgical Planning",
        "venue": "Postoperative Outcome Prediction",
        "cover": RESEARCH_DIR / "research papers" / "surgi_diff.png",
        "pdf": RESEARCH_DIR / "research papers" / "hK_award.pdf",
        "summary": "A diffusion generative framework integrated with a Spine Alignment Encoder to synthesize postoperative spinal X-rays and predict implant structures for AIS surgical planning.",
        "explanation": "Surgi-Diff connects postoperative image generation with instrumentation prediction, covering fusion segments, rods, and screw distributions. It is intended to support preoperative decision-making and postoperative outcome estimation.",
        "contribution": "Developed an anatomy-aware generative pipeline and evaluated implant-related predictions including fusion level, rod geometry, and screw distribution.",
        "highlights": ["612 AIS patients", "Fusion accuracy 75.8%", "Implant structure prediction"],
        "experiment_focus": "The experiments assess postoperative radiograph synthesis and surgical parameter prediction on 612 AIS patients. Surgi-Diff achieves the highest SSIM among compared methods and reports fusion level, rod geometry, and screw distribution metrics.",
        "experiment_pages": [1, 2, 3],
        "figure_note": "The detail view should focus on the model overview, synthesis comparison, and implant prediction tables because these directly support the surgical-planning narrative.",
        "portfolio_pages": [1, 2, 3],
        "gallery": {
            "figures": [
                {
                    "file": HK_AWARD_DIR / "figure1.pdf",
                    "title": "Figure 1: Surgi-Diff Framework",
                    "description": "Overview of Surgi-Diff for AIS surgical planning. Preoperative PA spinal X-ray and surgical ROI masks are encoded by the Spine Alignment Encoder, passed into a latent diffusion model for postoperative X-ray synthesis, and then analyzed through two paths: surgical parameter prediction and image fidelity/alignment evaluation.",
                    "section": "Methodology"
                },
                {
                    "file": HK_AWARD_DIR / "figure2.pdf",
                    "title": "Figure 2: Postoperative X-ray Synthesis Comparison",
                    "description": "Qualitative comparison across preoperative X-ray, GT postoperative X-ray, Surgi-Diff, ControlLoRA, ControlNext, StyleGANex, CycleGAN, and Pix2Pix. Surgi-Diff preserves spinal alignment and implant structures more consistently than the compared methods.",
                    "section": "Results"
                },
                {
                    "file": HK_AWARD_DIR / "figure3.pdf",
                    "title": "Figure 3: Screw-Rod Construct Prediction",
                    "description": "GT vs. Surgi-Diff postoperative X-ray comparisons for three AIS cases, emphasizing the global screw-rod construct and bilateral instrumentation layout.",
                    "section": "Implant Prediction"
                },
                {
                    "file": HK_AWARD_DIR / "figure4.pdf",
                    "title": "Figure 4: Pedicle Screw Placement Accuracy",
                    "description": "GT vs. Surgi-Diff comparisons for screw point placement in three AIS cases. The visualization focuses on segmental screw distribution and alignment along the spine.",
                    "section": "Implant Prediction"
                },
            ],
            "tables": [
                {
                    "file": HK_AWARD_DIR / "table1.pdf",
                    "title": "Table 1: Postoperative X-ray Synthesis Metrics",
                    "description": "Quantitative comparison of postoperative X-ray synthesis performance using PSNR and SSIM. Surgi-Diff reports the highest SSIM among the compared methods while maintaining competitive PSNR.",
                    "section": "Quantitative Results"
                },
                {
                    "file": HK_AWARD_DIR / "table2.pdf",
                    "title": "Table 2: Implant Prediction Performance",
                    "description": "Clinical-task evaluation for fusion level identification, rod geometry measurement, and screw distribution. Surgi-Diff reaches 75.8% fusion-level accuracy at a 10-pixel tolerance and reports low centerline and screw-position errors.",
                    "section": "Quantitative Results"
                },
            ]
        },
    },
]

PROJECTS = [
    {
        "id": "traffic_prediction",
        "title": "Traffic Flow Prediction System",
        "chinese_title": "城市交通流预测系统",
        "description": "基于城市功能区空间关系的交通流预测系统，利用深度学习模型（LSTM、GRU）对城市交通流量进行预测。系统提供完整的Web界面和API服务，支持模型训练、预测和可视化展示。",
        "long_description": "该系统旨在通过分析城市功能区之间的空间关系来预测交通流量。核心思路是将城市划分为不同的功能区域（如商业区、住宅区、工业区等），利用这些区域之间的时空关联来构建预测模型。系统采用深度学习架构，实现了端到端的交通流预测能力。",
        "github_url": "https://github.com/CHEN-zishen/Traffic-Flow-Prediction-System-Based-on-the-Relationship-of-Urban-Functional-Areas",
        "tags": ["Deep Learning", "Web Development", "Data Engineering"],
        "tech_stack": {
            "backend": ["Python", "FastAPI", "Flask", "PyTorch", "MySQL", "SQLAlchemy"],
            "frontend": ["HTML5", "CSS3", "JavaScript", "Bootstrap"],
            "ai": ["LSTM", "GRU", "Time Series Prediction"],
            "data": ["NumPy", "Pandas", "scikit-learn", "PEMS04 Dataset"]
        },
        "features": [
            {
                "name": "端到端深度学习预测",
                "description": "采用LSTM和GRU两种深度学习模型实现交通流预测，支持模型切换和对比分析。模型输入包含历史流量数据和功能区空间关系特征。"
            },
            {
                "name": "RESTful API服务",
                "description": "基于FastAPI构建的完整API服务，提供模型训练、预测查询、历史数据管理等接口，支持Swagger自动文档生成。"
            },
            {
                "name": "用户认证与权限管理",
                "description": "实现完整的用户注册、登录、角色权限管理系统，支持不同用户角色访问不同功能模块。"
            },
            {
                "name": "实时可视化展示",
                "description": "使用图表库展示预测结果与实际值对比、历史趋势分析、热力图等多种可视化形式。"
            },
            {
                "name": "模型配置与参数调优",
                "description": "提供可视化的模型参数配置界面，支持调整学习率、迭代次数、隐藏层大小等超参数。"
            },
            {
                "name": "历史数据管理",
                "description": "支持上传、查询、导出交通流历史数据，数据存储在MySQL数据库中，使用SQLAlchemy进行ORM管理。"
            }
        ],
        "architecture": {
            "overview": "采用前后端分离的架构设计，前端负责用户交互和数据展示，后端提供API服务和模型推理，数据库存储用户信息和预测数据。",
            "layers": [
                {"name": "表现层", "description": "基于Bootstrap的响应式Web界面，包含数据可视化图表、表单输入、导航菜单等组件。"},
                {"name": "API层", "description": "FastAPI构建的RESTful接口，处理HTTP请求，进行参数校验，调用业务逻辑层。"},
                {"name": "业务逻辑层", "description": "核心业务处理模块，包括用户认证、数据预处理、模型管理等逻辑。"},
                {"name": "模型层", "description": "PyTorch实现的LSTM/GRU深度学习模型，负责交通流预测推理。"},
                {"name": "数据层", "description": "MySQL数据库配合SQLAlchemy ORM，管理用户数据、历史记录、模型配置等。"}
            ],
            "flow": "用户通过前端页面发起请求 → FastAPI接收请求 → 业务逻辑层处理 → 调用模型或查询数据库 → 返回JSON响应 → 前端渲染展示"
        },
        "highlights": ["PEMS04数据集", "完整Web系统", "Docker部署支持", "双模型对比"],
        "image_path": None,
        "gallery": {
            "figures": [
                {
                    "file": PROJECTS_DIR / "Traffic Flow Prediction System" / "dcad87d6c8f77d82b7335ce2b5901a4.png",
                    "title": "Figure 1: System Dashboard",
                    "description": "系统主控制面板，包含数据概览、预测状态和功能导航。",
                    "section": "Overview"
                },
                {
                    "file": PROJECTS_DIR / "Traffic Flow Prediction System" / "abea8d8abbc6213d10041107176e7c5.png",
                    "title": "Figure 2: Traffic Flow Visualization",
                    "description": "交通流量热力图和时空分布可视化展示。",
                    "section": "Visualization"
                },
                {
                    "file": PROJECTS_DIR / "Traffic Flow Prediction System" / "8970acdc2195e52642d24529de68a89.png",
                    "title": "Figure 3: Model Comparison",
                    "description": "LSTM和GRU模型预测结果对比图表。",
                    "section": "Models"
                },
                {
                    "file": PROJECTS_DIR / "Traffic Flow Prediction System" / "a183302169b1df79db6cbc553094700.png",
                    "title": "Figure 4: Prediction Results",
                    "description": "预测结果与实际值对比分析界面。",
                    "section": "Results"
                },
                {
                    "file": PROJECTS_DIR / "Traffic Flow Prediction System" / "a5415feb73038ae9a611d9717562e91.png",
                    "title": "Figure 5: Model Configuration",
                    "description": "模型参数配置界面，支持调整超参数。",
                    "section": "Configuration"
                },
                {
                    "file": PROJECTS_DIR / "Traffic Flow Prediction System" / "39aff7d228eeef23bf94ef1e42cda7b.png",
                    "title": "Figure 6: User Management",
                    "description": "用户管理界面，包含注册、登录、权限设置。",
                    "section": "User"
                },
                {
                    "file": PROJECTS_DIR / "Traffic Flow Prediction System" / "3925393868ed04f89b2e18ea15753b8.png",
                    "title": "Figure 7: Data Management",
                    "description": "历史数据上传和管理界面。",
                    "section": "Data"
                },
                {
                    "file": PROJECTS_DIR / "Traffic Flow Prediction System" / "196782f934d5da52eeced9ae760f365.png",
                    "title": "Figure 8: Training Progress",
                    "description": "模型训练进度和损失曲线展示。",
                    "section": "Training"
                },
                {
                    "file": PROJECTS_DIR / "Traffic Flow Prediction System" / "1876873d9356c97e0aec7cd3e54e78b.png",
                    "title": "Figure 9: API Documentation",
                    "description": "FastAPI自动生成的Swagger API文档。",
                    "section": "API"
                }
            ]
        }
    },
    {
        "id": "venture_agent",
        "title": "VentureAgent AI Business Platform",
        "chinese_title": "创业体验官微信小程序",
        "description": "基于AI技术的创业学习平台，为创业者和商业爱好者提供商业计划评估、市场趋势分析、案例研究等工具。集成DeepSeek大语言模型，实现智能化的商业分析与评估功能。",
        "long_description": "VentureAgent是一款面向创业者的智能助手小程序，旨在帮助用户更好地理解商业运作规律，评估创业项目可行性。通过集成DeepSeek大语言模型，系统能够对用户提交的商业计划书进行深度分析，并生成专业的评估报告。",
        "github_url": "https://github.com/CHEN-zishen/VentureAgent__WeChat_Mini_Program",
        "tags": ["AI Agent", "WeChat Mini Program", "Business Intelligence"],
        "tech_stack": {
            "frontend": ["WeChat Mini Program", "JavaScript", "WXML", "WXSS"],
            "backend": ["Node.js", "Express", "RESTful API"],
            "ai": ["DeepSeek API", "LLM", "Prompt Engineering"],
            "database": ["MongoDB", "Mongoose"]
        },
        "features": [
            {
                "name": "AI商业计划评估",
                "description": "用户上传或输入商业计划书，系统调用DeepSeek API进行深度分析，从市场潜力、商业模式、竞争优势等多个维度进行评估。"
            },
            {
                "name": "商业案例库",
                "description": "收录大量真实商业案例，支持关键词搜索和分类浏览，帮助用户学习成功经验和失败教训。"
            },
            {
                "name": "市场趋势分析",
                "description": "基于AI分析的市场趋势报告，包括行业动态、消费者行为、竞争格局等维度的深度洞察。"
            },
            {
                "name": "知识图谱展示",
                "description": "可视化展示商业概念之间的关系网络，帮助用户理解复杂的商业逻辑和关联。"
            },
            {
                "name": "专业评估报告",
                "description": "生成结构化的评估报告，包含评分、建议、风险提示等内容，支持PDF导出。"
            },
            {
                "name": "创业知识库",
                "description": "提供创业相关的知识库文章，涵盖融资、法务、运营等多个领域。"
            }
        ],
        "architecture": {
            "overview": "采用小程序前端 + Node.js后端 + AI服务的三层架构，前端负责交互展示，后端处理业务逻辑和数据存储，AI服务提供智能分析能力。",
            "layers": [
                {"name": "小程序前端", "description": "微信原生小程序开发，使用WXML/WXSS构建界面，JavaScript处理业务逻辑和网络请求。"},
                {"name": "API网关", "description": "Node.js + Express构建的RESTful API服务，处理小程序的HTTP请求。"},
                {"name": "业务服务层", "description": "核心业务逻辑，包括用户管理、商业计划处理、案例检索等模块。"},
                {"name": "AI服务层", "description": "封装DeepSeek API调用，处理Prompt构建、响应解析、结果格式化。"},
                {"name": "数据存储层", "description": "MongoDB数据库，使用Mongoose进行数据建模和查询。"}
            ],
            "flow": "小程序发起请求 → Express服务器路由 → 业务服务处理 → 调用DeepSeek API或查询数据库 → 返回处理结果 → 小程序渲染展示"
        },
        "highlights": ["DeepSeek集成", "AI商业评估", "知识图谱", "小程序生态"],
        "image_path": None,
        "gallery": {
            "figures": [
                {
                    "file": PROJECTS_DIR / "VentureAgent__WeChat_Mini_Program" / "6ca50d406782e2498aada5af7361db7.jpg",
                    "title": "Figure 1: Welcome Page",
                    "description": "小程序首页欢迎界面，展示平台核心功能入口。",
                    "section": "Overview"
                },
                {
                    "file": PROJECTS_DIR / "VentureAgent__WeChat_Mini_Program" / "8982c9ef195b4c64434b46ad86f5055.jpg",
                    "title": "Figure 2: Business Plan Evaluation",
                    "description": "AI商业计划评估界面，用户输入或上传商业计划书。",
                    "section": "Evaluation"
                },
                {
                    "file": PROJECTS_DIR / "VentureAgent__WeChat_Mini_Program" / "0ea5a87683a5ac5576291352ebb22cc.jpg",
                    "title": "Figure 3: Evaluation Report",
                    "description": "AI生成的商业计划评估报告，包含多维度评分和建议。",
                    "section": "Evaluation"
                },
                {
                    "file": PROJECTS_DIR / "VentureAgent__WeChat_Mini_Program" / "1474f32328432968e891bf98563bfc1.jpg",
                    "title": "Figure 4: Market Trend Analysis",
                    "description": "市场趋势分析界面，展示行业动态和趋势预测。",
                    "section": "Analysis"
                },
                {
                    "file": PROJECTS_DIR / "VentureAgent__WeChat_Mini_Program" / "482e302c48fb56820bceb2b1b731eb8.jpg",
                    "title": "Figure 5: Business Case Library",
                    "description": "商业案例库界面，支持分类浏览和关键词搜索。",
                    "section": "Cases"
                },
                {
                    "file": PROJECTS_DIR / "VentureAgent__WeChat_Mini_Program" / "604e90d25fd36495f400cf82409cbec.jpg",
                    "title": "Figure 6: Knowledge Graph",
                    "description": "知识图谱可视化界面，展示商业概念关系网络。",
                    "section": "Visualization"
                },
                {
                    "file": PROJECTS_DIR / "VentureAgent__WeChat_Mini_Program" / "788b3f2181f47b5bae6ad46685927e8.jpg",
                    "title": "Figure 7: Entrepreneurship Knowledge Base",
                    "description": "创业知识库界面，提供融资、法务、运营等领域文章。",
                    "section": "Knowledge"
                },
                {
                    "file": PROJECTS_DIR / "VentureAgent__WeChat_Mini_Program" / "8d60906f606a396912f2b696af9d50a.jpg",
                    "title": "Figure 8: User Profile",
                    "description": "用户个人中心，展示评估历史和收藏内容。",
                    "section": "User"
                },
                {
                    "file": PROJECTS_DIR / "VentureAgent__WeChat_Mini_Program" / "d5a6804a406b9e5c4cf1d0f7204c6d2.jpg",
                    "title": "Figure 9: Report Export",
                    "description": "评估报告导出界面，支持PDF格式下载。",
                    "section": "Report"
                }
            ]
        }
    },
    {
        "id": "social_diffusion",
        "title": "SocialDiffusionAgents",
        "chinese_title": "社交网络多智能体扩散模拟系统",
        "description": "模拟社交网络互动的自主多智能体系统。具有不同个性特征的智能体基于规则或LLM驱动做出决策，形成动态环境用于研究信息扩散、谣言控制和干预效果。",
        "long_description": "SocialDiffusionAgents是一个研究社交网络信息传播机制的多智能体模拟平台。系统创建具有不同个性特征的智能体，它们在社交网络中互动、传播信息、形成信任关系。通过模拟不同的干预策略，可以研究其对信息扩散和谣言控制的影响。",
        "github_url": "https://github.com/CHEN-zishen/SocialDiffusionAgents",
        "tags": ["Multi-Agent", "LLM", "Simulation", "Social Network"],
        "tech_stack": {
            "backend": ["Python", "Streamlit", "uv", "Pydantic"],
            "ai": ["DeepSeek API", "LLM", "Rule-Based Decision Engine"],
            "database": ["SQLite", "SQLAlchemy"],
            "visualization": ["Streamlit Charts", "NetworkX", "Matplotlib"]
        },
        "features": [
            {
                "name": "六种个性智能体",
                "description": "实现了六种不同个性特征的智能体：轻信型、理性型、影响者型、辟谣型、情感型、沉默型，每种类型具有独特的决策逻辑。"
            },
            {
                "name": "混合决策引擎",
                "description": "支持基于规则和基于LLM两种决策模式，可根据场景需求灵活切换或混合使用。"
            },
            {
                "name": "持久化记忆系统",
                "description": "智能体具有持久化记忆，能够记录与其他智能体的信任关系、历史互动记录等信息。"
            },
            {
                "name": "实时可视化",
                "description": "动态展示社交网络拓扑结构、信息传播路径、智能体状态变化等实时图表。"
            },
            {
                "name": "A/B实验框架",
                "description": "支持设置不同的干预策略进行对比实验，评估干预效果。"
            },
            {
                "name": "参数可调模拟",
                "description": "提供丰富的模拟参数配置界面，包括网络规模、传播概率、干预强度等。"
            }
        ],
        "architecture": {
            "overview": "基于Streamlit的单页应用架构，智能体引擎作为核心模块处理多智能体交互，LLM客户端负责调用外部AI服务，SQLite存储智能体状态和历史数据。",
            "layers": [
                {"name": "Streamlit UI", "description": "可视化的模拟控制界面，包含参数配置、启动/暂停控制、实时图表展示。"},
                {"name": "Agent Engine", "description": "多智能体核心引擎，负责智能体创建、交互调度、状态更新。"},
                {"name": "Decision Engine", "description": "决策模块，包含规则引擎和LLM调用两种决策方式。"},
                {"name": "LLM Client", "description": "DeepSeek API客户端，处理Prompt构建和响应解析。"},
                {"name": "Memory System", "description": "SQLite数据库，存储智能体记忆、信任关系、传播历史。"}
            ],
            "flow": "用户配置参数 → 启动模拟 → Agent Engine初始化智能体 → 智能体执行决策循环 → 更新状态和记忆 → 实时渲染可视化 → 生成实验报告"
        },
        "highlights": ["6种智能体个性", "DeepSeek LLM集成", "干预策略实验", "完整单元测试"],
        "image_path": None,
        "gallery": {
            "figures": [
                {
                    "file": PROJECTS_DIR / "SocialDiffusionAgents" / "336b4ec4a1eafe36e0c65cd7a76ea24.png",
                    "title": "Figure 1: System Dashboard",
                    "description": "主控制面板，包含参数配置、模拟进度、网络拓扑预览。",
                    "section": "Overview"
                },
                {
                    "file": PROJECTS_DIR / "SocialDiffusionAgents" / "cb3943920fc8fb6048ef31ea4e60c11.png",
                    "title": "Figure 2: Agent Types Configuration",
                    "description": "六种智能体类型配置界面：轻信型、理性型、影响者型、辟谣型、情感型、沉默型。",
                    "section": "Agent Types"
                },
                {
                    "file": PROJECTS_DIR / "SocialDiffusionAgents" / "74f7f24561acd4af801870d31018805.png",
                    "title": "Figure 3: Social Network Visualization",
                    "description": "社交网络动态拓扑图，展示智能体节点和连接关系。",
                    "section": "Visualization"
                },
                {
                    "file": PROJECTS_DIR / "SocialDiffusionAgents" / "25a7dd2cd13624623632996da3960e4.png",
                    "title": "Figure 4: Information Diffusion Simulation",
                    "description": "信息传播模拟过程，不同颜色表示信息传播状态。",
                    "section": "Simulation"
                },
                {
                    "file": PROJECTS_DIR / "SocialDiffusionAgents" / "bf53f7ac38489bb993c1690f3cf98f6.png",
                    "title": "Figure 5: Trust Relationship Matrix",
                    "description": "智能体间信任关系矩阵热力图，展示信任度变化。",
                    "section": "Memory"
                },
                {
                    "file": PROJECTS_DIR / "SocialDiffusionAgents" / "190b07171375df6e6a31ed851fc46ef.png",
                    "title": "Figure 6: Decision Engine",
                    "description": "决策引擎配置，支持规则驱动和LLM驱动两种模式切换。",
                    "section": "Decision"
                },
                {
                    "file": PROJECTS_DIR / "SocialDiffusionAgents" / "7bc64e366ac9e776a0a85e6c3a7473a.png",
                    "title": "Figure 7: Intervention Strategy Panel",
                    "description": "干预策略配置面板，支持不同谣言控制策略设置。",
                    "section": "Experiment"
                },
                {
                    "file": PROJECTS_DIR / "SocialDiffusionAgents" / "21933d8e001bb8a5e5a3e803037e989.png",
                    "title": "Figure 8: Simulation Results Chart",
                    "description": "模拟结果统计图表，展示信息扩散曲线和干预效果对比。",
                    "section": "Results"
                },
                {
                    "file": PROJECTS_DIR / "SocialDiffusionAgents" / "22941d5972beb14a038a877b4f0cc40.png",
                    "title": "Figure 9: Agent Memory Viewer",
                    "description": "智能体记忆查看器，展示信任历史和交互记录。",
                    "section": "Memory"
                },
                {
                    "file": PROJECTS_DIR / "SocialDiffusionAgents" / "0fe465c80c3165115cf102b94426a90.png",
                    "title": "Figure 10: Parameter Settings",
                    "description": "详细参数配置界面，包括网络规模、传播概率、迭代次数等。",
                    "section": "Configuration"
                },
                {
                    "file": PROJECTS_DIR / "SocialDiffusionAgents" / "735d5bd139146558ab6e2394b2be10f.png",
                    "title": "Figure 11: A/B Experiment Setup",
                    "description": "A/B对比实验设置界面，支持两种策略并行对比。",
                    "section": "Experiment"
                },
                {
                    "file": PROJECTS_DIR / "SocialDiffusionAgents" / "e3e25d5d36823e10f8eedc427a167fc.png",
                    "title": "Figure 12: System Stats",
                    "description": "系统运行统计信息，展示智能体数量、消息传播量等实时指标。",
                    "section": "Overview"
                }
            ]
        }
    },
    {
        "id": "puzzle_solver",
        "title": "PuzzleSolver Search Algorithm System",
        "chinese_title": "搜索算法解谜系统",
        "description": "交互式搜索算法解谜系统，包含迷宫、八数码、N皇后、数独、推箱子五种经典谜题。支持DFS、BFS、A*、回溯四种搜索算法，提供动态可视化和算法对比功能。",
        "long_description": "PuzzleSolver是一个面向算法学习的交互式教学平台，通过可视化方式展示经典搜索算法的执行过程。系统支持五种不同类型的谜题，每种谜题都可以使用多种算法求解，并提供算法性能对比分析。",
        "github_url": "https://github.com/CHEN-zishen/PuzzleSolver---Search-Algorithm-Puzzle-System",
        "tags": ["Algorithm", "Web Application", "Education", "Visualization"],
        "tech_stack": {
            "backend": ["Python", "Flask", "SQLAlchemy"],
            "frontend": ["HTML5", "CSS3", "JavaScript", "Canvas"],
            "algorithm": ["DFS", "BFS", "A*", "Backtracking", "Heuristic Search"],
            "database": ["SQLite"]
        },
        "features": [
            {
                "name": "五种谜题类型",
                "description": "支持迷宫、八数码问题、N皇后问题、数独、推箱子五种经典谜题，每种谜题都有独立的生成和求解逻辑。"
            },
            {
                "name": "四种搜索算法",
                "description": "实现DFS（深度优先搜索）、BFS（广度优先搜索）、A*（启发式搜索）、回溯算法，支持算法对比分析。"
            },
            {
                "name": "动态可视化",
                "description": "使用Canvas绘制算法执行过程，实时展示搜索路径、状态变化、扩展节点等信息。"
            },
            {
                "name": "算法性能对比",
                "description": "自动计算并展示不同算法的时间复杂度、空间复杂度、扩展节点数等性能指标。"
            },
            {
                "name": "学习助手",
                "description": "集成DeepSeek API，提供算法原理讲解、解题思路分析等智能化学习辅助功能。"
            },
            {
                "name": "用户进度跟踪",
                "description": "记录用户的解题历史、偏好设置、学习进度等数据。"
            }
        ],
        "architecture": {
            "overview": "传统的Web应用架构，前端负责界面展示和动画渲染，后端处理算法计算和数据存储，算法模块作为独立组件可被多种谜题复用。",
            "layers": [
                {"name": "前端界面", "description": "HTML/CSS/JavaScript构建的用户界面，包含谜题选择、算法选择、Canvas动画展示区域。"},
                {"name": "Flask API", "description": "RESTful API服务，处理前端请求，调用算法模块进行计算。"},
                {"name": "算法模块", "description": "独立的算法实现模块，包含DFS、BFS、A*、回溯等算法的通用接口。"},
                {"name": "谜题模块", "description": "五种谜题的生成、验证、求解逻辑实现。"},
                {"name": "数据持久化", "description": "SQLite数据库存储用户信息、解题历史、偏好设置。"}
            ],
            "flow": "用户选择谜题和算法 → 前端发送请求 → Flask路由处理 → 算法模块执行搜索 → 返回路径和统计数据 → Canvas渲染动画"
        },
        "highlights": ["5种谜题", "4种算法", "动态可视化", "AI学习助手"],
        "image_path": None,
        "gallery": {
            "figures": [
                {
                    "file": PROJECTS_DIR / "PuzzleSolver---Search-Algorithm-Puzzle-System" / "99968d13450794316f5a8f02724d537.png",
                    "title": "Figure 1: System Homepage",
                    "description": "系统首页，展示五种谜题类型选择入口。",
                    "section": "Overview"
                },
                {
                    "file": PROJECTS_DIR / "PuzzleSolver---Search-Algorithm-Puzzle-System" / "5fb958f847e6601ff8c1fc907c1531e.png",
                    "title": "Figure 2: Maze Puzzle",
                    "description": "迷宫解谜界面，展示DFS/BFS/A*算法的搜索过程可视化。",
                    "section": "Puzzles"
                },
                {
                    "file": PROJECTS_DIR / "PuzzleSolver---Search-Algorithm-Puzzle-System" / "709024d04704e6c4f9780fd55aaff32.png",
                    "title": "Figure 3: 8-Puzzle",
                    "description": "八数码问题界面，展示滑块拼图的算法求解过程。",
                    "section": "Puzzles"
                },
                {
                    "file": PROJECTS_DIR / "PuzzleSolver---Search-Algorithm-Puzzle-System" / "46cb1b8de0e06d15d5596fa1873dc93.png",
                    "title": "Figure 4: N-Queens",
                    "description": "N皇后问题界面，展示回溯算法的求解过程和多种解法。",
                    "section": "Puzzles"
                },
                {
                    "file": PROJECTS_DIR / "PuzzleSolver---Search-Algorithm-Puzzle-System" / "274b9804228906f1f9c1f3975ae3cff.png",
                    "title": "Figure 5: Sudoku",
                    "description": "数独求解界面，支持自动求解和手动填写模式。",
                    "section": "Puzzles"
                },
                {
                    "file": PROJECTS_DIR / "PuzzleSolver---Search-Algorithm-Puzzle-System" / "01cd1b292c0518133a4761c3a1ffc60.png",
                    "title": "Figure 6: Sokoban",
                    "description": "推箱子游戏界面，展示推箱子谜题的求解过程。",
                    "section": "Puzzles"
                },
                {
                    "file": PROJECTS_DIR / "PuzzleSolver---Search-Algorithm-Puzzle-System" / "913fd26ec835a0ab53321a9189b28bd.png",
                    "title": "Figure 7: Algorithm Comparison",
                    "description": "算法性能对比界面，展示DFS、BFS、A*的扩展节点数和时间对比。",
                    "section": "Algorithm"
                },
                {
                    "file": PROJECTS_DIR / "PuzzleSolver---Search-Algorithm-Puzzle-System" / "0482784b37430618aee676994521ae3.png",
                    "title": "Figure 8: Search Animation",
                    "description": "搜索过程动态可视化，展示节点扩展和路径发现过程。",
                    "section": "Visualization"
                },
                {
                    "file": PROJECTS_DIR / "PuzzleSolver---Search-Algorithm-Puzzle-System" / "fbcff121dc500674a2603a668348051.png",
                    "title": "Figure 9: AI Learning Assistant",
                    "description": "AI学习助手界面，集成DeepSeek API提供算法讲解。",
                    "section": "AI"
                },
                {
                    "file": PROJECTS_DIR / "PuzzleSolver---Search-Algorithm-Puzzle-System" / "4c1b6ecebd3137e04308332777ce3b8.png",
                    "title": "Figure 10: User Profile",
                    "description": "用户个人中心，展示学习进度和解题历史。",
                    "section": "User"
                },
                {
                    "file": PROJECTS_DIR / "PuzzleSolver---Search-Algorithm-Puzzle-System" / "35e5f33ff8e732b128a2f4d30dee50a.png",
                    "title": "Figure 11: Algorithm Selection",
                    "description": "算法选择界面，支持DFS、BFS、A*、回溯的切换。",
                    "section": "Algorithm"
                },
                {
                    "file": PROJECTS_DIR / "PuzzleSolver---Search-Algorithm-Puzzle-System" / "dd1ad5474f7809f639d230289c80d45.png",
                    "title": "Figure 12: Puzzle Configuration",
                    "description": "谜题参数配置界面，调整难度和规模。",
                    "section": "Configuration"
                },
                {
                    "file": PROJECTS_DIR / "PuzzleSolver---Search-Algorithm-Puzzle-System" / "284bda2a4a7641f529959a92d3d71cb.png",
                    "title": "Figure 13: Solution Path",
                    "description": "求解路径展示，高亮显示最优路径。",
                    "section": "Visualization"
                },
                {
                    "file": PROJECTS_DIR / "PuzzleSolver---Search-Algorithm-Puzzle-System" / "9edb0af30e96da9a8114e1b5316a5eb.png",
                    "title": "Figure 14: Performance Stats",
                    "description": "性能统计面板，展示时间复杂度、空间复杂度等指标。",
                    "section": "Algorithm"
                },
                {
                    "file": PROJECTS_DIR / "PuzzleSolver---Search-Algorithm-Puzzle-System" / "8e12cad6c46ec50c6fc2adb9616d0ac.png",
                    "title": "Figure 15: History Records",
                    "description": "解题历史记录界面，支持查看和回放历史求解过程。",
                    "section": "User"
                },
                {
                    "file": PROJECTS_DIR / "PuzzleSolver---Search-Algorithm-Puzzle-System" / "0110a3e3edb5bf4a94adf70dfcd548e.png",
                    "title": "Figure 16: Settings",
                    "description": "系统设置界面，调整动画速度、主题颜色等偏好。",
                    "section": "Configuration"
                }
            ]
        }
    },
    {
        "id": "image_search",
        "title": "Image-to-Image Search Application",
        "chinese_title": "多源特征融合图像检索系统",
        "description": "基于多源信息融合技术的图像检索应用。通过整合多种图像特征提取方法和相似度计算策略，实现高效准确的图像搜索功能。",
        "long_description": "该项目探索多源特征融合技术在图像检索中的应用。系统从不同角度提取图像特征（如颜色、纹理、形状等），通过融合策略将这些特征整合，提高检索的准确性和鲁棒性。项目使用MATLAB实现，包含完整的特征提取、相似度计算、融合决策和性能评估模块。",
        "github_url": "https://github.com/CHEN-zishen/An-image-to-image-search-application-based-on-multi-source-feature-fusion",
        "tags": ["Computer Vision", "Image Processing", "MATLAB", "Information Retrieval"],
        "tech_stack": {
            "language": ["MATLAB"],
            "computer_vision": ["Feature Extraction", "Color Histogram", "Texture Analysis", "Shape Descriptors"],
            "algorithm": ["Similarity Calculation", "Multi-source Fusion", "Weighted Voting", "Performance Evaluation"],
            "data": ["Image Dataset", "Feature Vector Database"]
        },
        "features": [
            {
                "name": "多源特征提取",
                "description": "实现颜色直方图、纹理特征（如GLCM）、形状描述符（如Hu矩）等多种特征提取方法。"
            },
            {
                "name": "相似度计算",
                "description": "支持欧氏距离、余弦相似度、巴氏距离等多种相似度度量方式。"
            },
            {
                "name": "特征融合策略",
                "description": "实现加权融合、决策级融合等多种融合策略，根据不同特征的可靠性动态调整权重。"
            },
            {
                "name": "图像检索引擎",
                "description": "构建基于特征向量的图像检索系统，支持按相似度排序返回检索结果。"
            },
            {
                "name": "性能评估",
                "description": "提供查准率、查全率、平均精度等多种评估指标，支持不同融合策略的对比分析。"
            },
            {
                "name": "可视化展示",
                "description": "展示检索结果、特征分布、融合权重等可视化信息。"
            }
        ],
        "architecture": {
            "overview": "MATLAB单文件应用架构，采用模块化设计，包含特征提取、相似度计算、融合决策、检索引擎和评估模块。",
            "layers": [
                {"name": "数据输入层", "description": "图像数据集加载和预处理，支持批量导入和格式转换。"},
                {"name": "特征提取层", "description": "多种特征提取方法的实现，包括颜色、纹理、形状等维度。"},
                {"name": "相似度计算层", "description": "特征向量之间的相似度度量计算。"},
                {"name": "融合决策层", "description": "多源特征的融合策略实现，包括加权融合和决策级融合。"},
                {"name": "检索引擎层", "description": "基于融合特征的图像检索和排序。"},
                {"name": "评估展示层", "description": "性能指标计算和结果可视化展示。"}
            ],
            "flow": "加载图像数据集 → 提取多源特征 → 构建特征数据库 → 输入查询图像 → 提取查询特征 → 计算相似度并融合 → 返回排序结果 → 评估检索性能"
        },
        "highlights": ["多源特征融合", "MATLAB实现", "多种评估指标", "完整实验流程"],
        "image_path": None,
        "gallery": {
            "figures": [
                {
                    "file": PROJECTS_DIR / "An-image-to-image-search-application-based-on-multi-source-feature-fusion" / "2053fe5498f6124235eeff7ded9e09e.png",
                    "title": "Figure 1: System Interface",
                    "description": "系统主界面，展示图像检索流程和功能模块。",
                    "section": "Overview"
                },
                {
                    "file": PROJECTS_DIR / "An-image-to-image-search-application-based-on-multi-source-feature-fusion" / "23a2a762be568790e2341906f04cd75.png",
                    "title": "Figure 2: Retrieval Results",
                    "description": "图像检索结果展示，按相似度排序显示匹配图像。",
                    "section": "Results"
                },
                {
                    "file": PROJECTS_DIR / "An-image-to-image-search-application-based-on-multi-source-feature-fusion" / "afb572ad4e4110ac77624b71bd756eb.png",
                    "title": "Figure 3: Feature Visualization",
                    "description": "多源特征可视化，展示颜色直方图、纹理特征和形状描述符。",
                    "section": "Features"
                }
            ]
        }
    },
]

COMPETITION_AWARDS = [
    {
        "id": "san_chuang",
        "title": "National \"Three Creations\" Competition",
        "chinese_title": "全国大学生创新创业大赛",
        "category": "Competition",
        "level": "National",
        "year": "2024",
        "description": "Participated in the national \"Three Creations\" competition, focusing on innovative entrepreneurship projects.",
        "image": COMPETITION_DIR / "三创赛.png",
        "tags": ["Innovation", "Entrepreneurship"],
    },
    {
        "id": "internet_plus",
        "title": "\"Internet+\" Innovation Competition",
        "chinese_title": "互联网+创新创业大赛",
        "category": "Competition",
        "level": "Provincial",
        "year": "2024",
        "description": "Participated in the \"Internet+\" college student innovation and entrepreneurship competition.",
        "image": COMPETITION_DIR / "互联网+.png",
        "tags": ["Internet+", "Innovation"],
    },
    {
        "id": "sports_scholarship",
        "title": "Sports Scholarship",
        "chinese_title": "体育单项奖学金",
        "category": "Scholarship",
        "level": "University",
        "year": "2023",
        "description": "Awarded for outstanding sports achievements and contributions.",
        "image": COMPETITION_DIR / "体育单项奖学金.jpg",
        "tags": ["Sports", "Scholarship"],
    },
    {
        "id": "innovation_scholarship",
        "title": "Innovation Talent Scholarship",
        "chinese_title": "创新人才奖学金",
        "category": "Scholarship",
        "level": "University",
        "year": "2024",
        "description": "Recognized for exceptional innovation capabilities and research achievements.",
        "image": COMPETITION_DIR / "创新人才奖学金.jpg",
        "tags": ["Innovation", "Scholarship"],
    },
    {
        "id": "dawan_qu",
        "title": "Greater Bay Area Cup",
        "chinese_title": "大湾区杯粤港澳金融数学建模竞赛",
        "category": "Competition",
        "level": "Regional",
        "year": "2024",
        "description": "Achieved Third Prize at the 5th \"Greater Bay Area Cup\" Guangdong-Hong Kong-Macao Financial Mathematical Modeling Competition.",
        "long_description": "This project focused on GDP trend prediction for the Greater Bay Area region. We developed a comprehensive data collection and analysis pipeline to forecast economic development trends across the region, integrating data from multiple sources to build an accurate prediction model.",
        "methodology": "Based on Python web scraping technology, we collected relevant data from domestic and international websites targeting the Greater Bay Area. After data cleaning and preprocessing, we utilized MLP (Multi-Layer Perceptron) to construct a GDP trend prediction model for the region. Through model training and optimization, we achieved precise prediction results.",
        "achievements": [
            "Collected and preprocessed multi-source economic data",
            "Built MLP-based GDP prediction model",
            "Achieved accurate regional economic forecasting",
            "Awarded Third Prize at Regional Level"
        ],
        "image": COMPETITION_DIR / "大湾区杯.png",
        "tags": ["Greater Bay Area", "Financial Modeling", "Python", "MLP"],
    },
    {
        "id": "scholarship",
        "title": "Merit Scholarship",
        "chinese_title": "优秀学生奖学金",
        "category": "Scholarship",
        "level": "University",
        "year": "2023",
        "description": "Awarded for excellent academic performance and comprehensive development.",
        "image": COMPETITION_DIR / "奖学金.png",
        "tags": ["Academic", "Scholarship"],
    },
    {
        "id": "scholarship2",
        "title": "Merit Scholarship (Second)",
        "chinese_title": "优秀学生奖学金（二等奖）",
        "category": "Scholarship",
        "level": "University",
        "year": "2024",
        "description": "Second-class merit scholarship for outstanding academic achievements.",
        "image": COMPETITION_DIR / "奖学金2.jpg",
        "tags": ["Academic", "Scholarship"],
    },
    {
        "id": "math_modeling_national",
        "title": "National Mathematical Modeling Competition",
        "chinese_title": "全国大学生数学建模竞赛",
        "category": "Competition",
        "level": "National",
        "year": "2023",
        "description": "Achieved Second Prize at the 2023 National Mathematical Modeling Competition.",
        "long_description": "This project focused on the optimization of multi-UAV (Unmanned Aerial Vehicle) path planning for tobacco pest monitoring. We developed a comprehensive mathematical model to address the challenges of efficient coverage and path optimization for multiple drones operating in agricultural environments.",
        "methodology": "We proposed the Hierarchical Physical Perception Cooperative Optimization (HPCO) algorithm, which defines vine pruning decision criteria and designs layered search strategies. By combining multiple algorithms to achieve single-to-multi objective path parameter optimization, we successfully improved the effective coverage time from 1.39s to 27.75s, demonstrating excellent model stability and engineering feasibility.",
        "achievements": [
            "Proposed HPCO (Hierarchical Physical Perception Cooperative Optimization) algorithm",
            "Improved effective coverage time from 1.39s to 27.75s",
            "Validated model stability and engineering feasibility",
            "Awarded Second Prize at National Level"
        ],
        "image": COMPETITION_DIR / "数模国赛.png",
        "tags": ["Mathematics", "Modeling", "Optimization", "UAV"],
    },
    {
        "id": "teddy_cup",
        "title": "Teddy Cup Data Mining Competition",
        "chinese_title": "泰迪杯数据挖掘挑战赛",
        "category": "Competition",
        "level": "National",
        "year": "2024",
        "description": "Achieved Third Prize at the 2024 Teddy Cup Data Mining Challenge.",
        "long_description": "This project focused on user activity recognition and physical health status monitoring using wearable device data. We analyzed 100GB of tri-axial acceleration time-series data collected from wearable sensors, developing advanced deep learning models for real-time activity classification and health assessment.",
        "methodology": "We constructed a BiLSTM-LSTM deep learning model based on PyTorch, specifically designed for wearable device data analysis. We designed sliding window sampling strategies and Batch Normalization data preprocessing pipelines. By integrating Fourier transform and wavelet transform for time-frequency domain feature extraction, and utilizing attention mechanisms for model weight redistribution, we achieved accurate recognition of user activities and real-time monitoring of physical health status across sitting, standing, left/right movement, and forward/backward movement scenarios.",
        "achievements": [
            "Processed 100GB tri-axial acceleration time-series data",
            "Designed BiLSTM-LSTM model with attention mechanisms",
            "Implemented time-frequency domain feature extraction",
            "Achieved real-time activity recognition and health monitoring",
            "Awarded Third Prize at National Level"
        ],
        "image": COMPETITION_DIR / "泰迪杯.png",
        "tags": ["Data Mining", "Deep Learning", "PyTorch", "Wearable"],
    },
    {
        "id": "math_modeling_american",
        "title": "MCM/ICM Competition",
        "chinese_title": "美国大学生数学建模竞赛",
        "category": "Competition",
        "level": "International",
        "year": "2024",
        "description": "Achieved Honorable Mention at the 2024 MCM/ICM (Mathematical Contest in Modeling).",
        "long_description": "This project focused on sustainable tourism development strategy formulation. We analyzed multiple tourism economic indicators and developed optimization models to support decision-making for sustainable tourism development, integrating GIS technology and multi-criteria analysis methods.",
        "methodology": "We applied Python crawling and Web Scraping techniques to collect extensive tourism economic data from the city. After comprehensive data cleaning and preprocessing, we constructed multi-objective optimization models using genetic algorithms. We further optimized model parameters through simulated annealing algorithms, while utilizing GIS technology, regression analysis, and AHP (Analytic Hierarchy Process) for auxiliary analysis, ultimately formulating sustainable tourism development strategies.",
        "achievements": [
            "Collected and analyzed comprehensive tourism economic data",
            "Developed multi-objective optimization models with genetic algorithms",
            "Applied GIS and AHP for spatial and multi-criteria analysis",
            "Achieved Honorable Mention at International Level"
        ],
        "image": COMPETITION_DIR / "美赛.png",
        "tags": ["Mathematics", "International", "GIS", "Optimization"],
    },
    {
        "id": "industry_analysis",
        "title": "Industry Analysis Competition",
        "chinese_title": "行业分析大赛",
        "category": "Competition",
        "level": "Provincial",
        "year": "2023",
        "description": "Analyzed industry trends and presented strategic insights.",
        "image": COMPETITION_DIR / "行业分析大赛.png",
        "tags": ["Industry Analysis", "Strategy"],
    },
    {
        "id": "computer_design",
        "title": "National Computer Design Competition",
        "chinese_title": "全国大学生计算机设计大赛",
        "category": "Competition",
        "level": "National",
        "year": "2024",
        "description": "Developed innovative computer applications and designs.",
        "image": COMPETITION_DIR / "计算机设计大赛.png",
        "tags": ["Computer Science", "Design"],
    },
    {
        "id": "sports_frisbee_1",
        "title": "University Frisbee Competition",
        "chinese_title": "校级飞盘比赛",
        "category": "Sports",
        "level": "University",
        "year": "2023",
        "description": "Participated in the university frisbee competition, demonstrating excellent teamwork and athletic skills.",
        "long_description": "As an active member of the Shantou University Frisbee Association, I participated in the university frisbee competition, contributing to the team's success through dedicated training and outstanding performance on the field.",
        "methodology": "Through rigorous weekly training sessions and strategic game planning, our team developed strong coordination and communication skills, which were crucial for achieving competitive results.",
        "achievements": [
            "Participated in university-level frisbee competition",
            "Developed excellent teamwork and communication skills",
            "Contributed to team's competitive performance",
            "Enhanced physical fitness and sportsmanship"
        ],
        "image": BASE_DIR / "data" / "Aesthetic Education" / "体育" / "929eca0c788f583d9cf1618fbfc3ebc.png",
        "tags": ["Frisbee", "Sports", "Teamwork"],
    },
    {
        "id": "sports_frisbee_2",
        "title": "Inter-college Frisbee Tournament",
        "chinese_title": "校际飞盘联赛",
        "category": "Sports",
        "level": "Regional",
        "year": "2024",
        "description": "Represented Shantou University in the inter-college frisbee tournament, competing against teams from various universities.",
        "long_description": "As Vice President of the Frisbee Association, I led our team in the inter-college frisbee tournament, coordinating training schedules and game strategies to achieve excellent results against strong competition.",
        "methodology": "We implemented systematic training programs focusing on both individual skills and team tactics. Through video analysis of previous games and targeted practice sessions, we improved our offensive and defensive capabilities.",
        "achievements": [
            "Led team in inter-college frisbee tournament",
            "Coordinated team training and strategy",
            "Competed against multiple university teams",
            "Showcased competitive sports performance"
        ],
        "image": BASE_DIR / "data" / "Aesthetic Education" / "体育" / "a22fc8c61eb55bac499c693c81a003b.png",
        "tags": ["Frisbee", "Sports", "Leadership"],
    },
    {
        "id": "sports_other",
        "title": "Campus Sports Meet",
        "chinese_title": "校园运动会",
        "category": "Sports",
        "level": "University",
        "year": "2024",
        "description": "Participated in various track and field events at the campus sports meet, demonstrating athletic abilities.",
        "long_description": "I actively participated in the annual campus sports meet, taking part in multiple track and field events and contributing to my department's overall score.",
        "methodology": "Through consistent physical training and event-specific preparation, I improved my athletic performance and represented my department with pride.",
        "achievements": [
            "Participated in campus sports meet",
            "Competed in track and field events",
            "Contributed to department's team score",
            "Demonstrated sports spirit and dedication"
        ],
        "image": BASE_DIR / "data" / "Aesthetic Education" / "体育" / "f33b258fc63f49c366783755e880dff.png",
        "tags": ["Athletics", "Sports", "Campus"],
    },
    {
        "id": "excellent_student_leader",
        "title": "Outstanding Student Leader",
        "chinese_title": "优秀学生骨干",
        "category": "Scholarship",
        "level": "University",
        "year": "2024",
        "description": "Recognized for exceptional leadership and contributions to campus activities.",
        "long_description": "Received the Outstanding Student Leader award in recognition of my leadership in campus organizations, including the Youth Volunteer Association and Frisbee Association. This award acknowledges my dedication to organizing activities, serving the community, and promoting student engagement.",
        "methodology": "Through active participation and leadership in multiple campus organizations, I demonstrated strong organizational skills, teamwork, and commitment to community service.",
        "achievements": [
            "Led multiple campus organizations",
            "Organized numerous volunteer and sports activities",
            "Demonstrated exceptional leadership qualities",
            "Recognized for contributions to campus life"
        ],
        "image": COMPETITION_DIR / "优秀学生骨干.jpg",
        "tags": ["Leadership", "Campus", "Recognition"],
    },
    {
        "id": "active_participant",
        "title": "Active Participant Award",
        "chinese_title": "活动积极分子",
        "category": "Scholarship",
        "level": "University",
        "year": "2024",
        "description": "Awarded for enthusiastic participation and outstanding contributions to campus events.",
        "long_description": "Received the Active Participant Award for my enthusiastic involvement in various campus activities, including sports events, volunteer programs, and cultural activities. This award recognizes my proactive attitude and positive contributions to campus life.",
        "methodology": "By actively participating in diverse campus activities and events, I enriched campus culture and demonstrated a proactive and positive attitude towards community engagement.",
        "achievements": [
            "Actively participated in campus activities",
            "Contributed to sports and cultural events",
            "Demonstrated enthusiasm and dedication",
            "Enhanced campus cultural diversity"
        ],
        "image": COMPETITION_DIR / "活动积极分子.jpg",
        "tags": ["Campus", "Participation", "Recognition"],
    },
]

INTERNSHIPS = [
    {
        "id": "hku",
        "company": "The University of Hong Kong - Digital Health Lab",
        "chinese_company": "香港大学医学院数字健康实验室",
        "position": "Research Assistant",
        "chinese_position": "研究助理",
        "period": "2025.10 - 2026.03",
        "location": "Hong Kong, China",
        "description": "Worked at the Digital Health Laboratory, Faculty of Medicine, HKU, focusing on AI-driven medical image processing and enhancement research.",
        "long_description": "During my internship at HKU's Digital Health Lab (AMed), I worked closely with professors and PhD students on cutting-edge AI research projects for medical image processing. I collected and standardized over 1000 pairs of clinical pre/post-operative X-ray images, developed Python-based image processing pipelines using StableDiffusion, ESRGAN, SRGAN for quality enhancement, implemented multiple registration models (SyN, cycGAN, MeanFlow, VAE, Transformer), and conducted comparative experiments with DeepLabv3 and Marigold. I independently developed the ScoldM model, with a paper submitted to IEEE TBM (SCI Q2), and contributed to the Sungit-Diffi research published in IEEE TMI (SCI Q1).",
        "image_path": BASE_DIR / "data" / "resume" / "SKM_C3320i26032314290-2.pdf",
        "image_type": "pdf",
        "achievements": [
            "Collected and standardized over 1000 pairs of clinical X-ray images for research",
            "Developed Python image processing pipelines using StableDiffusion, ESRGAN, SRGAN",
            "Implemented multiple registration models: SyN, cycGAN, MeanFlow, VAE, Transformer",
            "Conducted comparative experiments with DeepLabv3, Marigold, and CNet evaluation",
            "Independently developed ScoldM model, paper submitted to IEEE TBM (SCI Q2)",
            "Contributed to Sungit-Diffi research published in IEEE TMI (SCI Q1)",
            "Designed and implemented GenGNet, paper submitted to IEEE JBHI (SCI Q1)",
            "Participated in 2025 Excellent Young Engineer Researcher Selection",
        ],
        "skills_gained": ["Python", "PyTorch", "Medical Image Processing", "Diffusion Models", "Deep Learning", "Research Methodology", "Academic Writing"],
        "tags": ["Academic", "AI Research", "Medical Imaging", "Hong Kong"],
    },
    {
        "id": "uestc",
        "company": "University of Electronic Science and Technology of China",
        "chinese_company": "电子科技大学长三角研究所",
        "position": "Research Intern",
        "chinese_position": "研究实习生",
        "period": "2024.09 - 2025.02",
        "location": "Foshan, China",
        "description": "Worked at the Yangtze River Delta Research Institute, focusing on traffic flow prediction using graph neural networks and spatiotemporal modeling.",
        "long_description": "During my research internship at UESTC's Yangtze River Delta Research Institute, I focused on developing spatiotemporal prediction models for traffic flow. I constructed traffic state spatiotemporal prediction models using PyTorch and DGL for graph convolutional networks and dynamic graph convolution. I built a coupled model combining spatiotemporal graph convolution with multi-head attention, integrating gating mechanisms to capture long-term spatial dependencies. The research results were published in SCI journals including TCI, Chaos, Solitons and Fractals.",
        "image_path": None,
        "image_type": None,
        "achievements": [
            "Built traffic state spatiotemporal prediction models using PyTorch and DGL",
            "Developed graph convolutional and dynamic graph convolutional networks",
            "Constructed coupled model with spatiotemporal graph convolution and multi-head attention",
            "Integrated gating mechanisms for capturing long-term spatial dependencies",
            "Research published in SCI journals: TCI, Chaos, Solitons and Fractals",
            "Applied for patent: Multi-scale Dual Attention Graph Convolutional Network for Traffic Flow Prediction",
        ],
        "skills_gained": ["Python", "PyTorch", "DGL", "Graph Neural Networks", "Spatiotemporal Modeling", "Traffic Prediction", "Patent Writing"],
        "tags": ["Academic", "Graph Neural Networks", "Traffic Prediction", "Foshan"],
    },
    {
        "id": "xinyi",
        "company": "Guangzhou Xinyi Technology Co., Ltd.",
        "chinese_company": "广州鑫谊科技有限公司",
        "position": "Software Development Intern",
        "chinese_position": "软件开发实习生",
        "period": "2025.06 - 2025.09",
        "location": "Guangzhou, China",
        "description": "Worked as a software development intern, focusing on web scraping, data processing, and visualization for patent data analysis.",
        "long_description": "During my internship at Guangzhou Xinyi Technology, I developed web crawlers using Python (Scrapy, Requests, BeautifulSoup) to extract structured and unstructured data from patent databases, processing over 10,000 records. I used Pandas and NumPy for data cleaning, deduplication, and standardization, applying regex and text matching to extract patent abstracts, IPC classifications, and applicant information. I built visual dashboards using Excel and Power BI to output technology distribution and innovation trend analysis reports.",
        "image_path": BASE_DIR / "data" / "resume" / "Scanned_20260712_121933.pdf",
        "image_type": "pdf",
        "achievements": [
            "Developed web scrapers using Python Scrapy/Requests/BeautifulSoup",
            "Processed over 10,000 patent records from databases",
            "Applied Pandas/NumPy for data cleaning, deduplication and standardization",
            "Extracted patent data using regex and text matching techniques",
            "Built visual dashboards using Excel and Power BI",
            "Generated technology distribution and innovation trend analysis reports",
        ],
        "skills_gained": ["Python", "Scrapy", "BeautifulSoup", "Pandas", "NumPy", "Data Visualization", "Power BI", "Regex", "Web Scraping"],
        "tags": ["Industry", "Web Development", "Data Processing", "Guangzhou"],
    },
]

PRACTICES = [
    {
        "id": "volunteer",
        "organization": "Shantou University Youth Volunteer Association",
        "chinese_organization": "汕头大学数学与计算机学院青年志愿者协会",
        "role": "Project Department Member",
        "chinese_role": "项目部成员",
        "period": "2023.09 - 2024.09",
        "location": "Shantou, China",
        "description": "Served as a Project Department member and participated in volunteer services covering coastal cleanup, first-aid education, community care, campus services, cultural activities, and event support.",
        "long_description": "As a member of the Youth Volunteer Association's Project Department, I participated in a broad range of public-service and campus volunteer activities, including environmental protection, first-aid training support, community elderly care, intangible cultural heritage outreach, freshman orientation, campus civilization guidance, school promotional filming, and community frisbee courses. These experiences strengthened my service awareness, event execution ability, communication skills, and capacity to coordinate with communities and campus organizations.",
        "image_path": BASE_DIR / "data" / "resume" / "practice" / "bd981186e488011d2bc4581440bfa40.png",
        "image_type": "image",
        "achievements": [
            "\"清洁海岸，保护家园\" 东海岸垃圾清扫志愿者",
            "汕头大学数学与计算机学院咨询流动服务站志愿者",
            "汕头大学东海岸校区急救专题徒手心肺复苏志愿者",
            "\"相约蓝天\" 课程体验活动参与者 / 志愿者",
            "2025 年汕头市潮服会志愿者",
            "\"时光返航，银龄乐享\" 老年趣味运动会活动志愿者",
            "\"非遗启萌芽，潮流绽新花\" 非遗进社区活动志愿者",
            "金东街社区关爱老人志愿活动志愿者",
            "\"暖冬护绿，青马同行\" 志愿服务活动志愿者",
            "2024 汕大宣传片演员，参与学校宣传片拍摄",
            "2024 汕头大学数学与计算机学院毕业晚会参与人员",
            "2024 汕头大学迎新活动志愿者",
            "2024 大华集成社区趣味飞盘课程志愿服务志愿者",
            "2023 年秋季汕头大学校园文明引导志愿服务志愿者",
            "\"除旧迎新\" 宿舍清扫志愿服务志愿者",
            "宿舍楼公共区域清扫活动志愿者",
            "A 栋电梯秩序引导志愿活动志愿者",
        ],
        "skills_gained": ["Teamwork", "Event Planning", "Community Service", "Communication", "Public Service", "First Aid Awareness", "Environmental Protection", "Elderly Care"],
        "tags": ["Volunteer", "Community", "Campus", "Public Service"],
    },
    {
        "id": "frisbee",
        "organization": "Shantou University Frisbee Association",
        "chinese_organization": "汕头大学飞盘协会",
        "role": "Vice President",
        "chinese_role": "副会长",
        "period": "2023.09 - 2024.09",
        "location": "Shantou, China",
        "description": "Served as Vice President of the Frisbee Association, responsible for organizing training sessions and competitions to promote frisbee sports on campus.",
        "long_description": "As Vice President of the Frisbee Association, I managed daily operations, organized regular training sessions, and coordinated inter-college competitions. I also led the team in participating in city-level frisbee tournaments, promoting the development of frisbee culture at Shantou University.",
        "image_path": BASE_DIR / "data" / "resume" / "practice" / "65d7109deaa45c29c9c4dd4a74e7a9b.png",
        "image_type": "image",
        "gallery_images": [
            BASE_DIR / "data" / "resume" / "practice" / "Shantou University Frisbee Association" / "123118ab6f0f3e2fa5ca37b4b7129fa.png",
            BASE_DIR / "data" / "resume" / "practice" / "Shantou University Frisbee Association" / "880dfc4e6ab3cc29a1c5ce882b37619.png",
            BASE_DIR / "data" / "resume" / "practice" / "Shantou University Frisbee Association" / "a11c75635e3756553da7685bbc95db1.png",
        ],
        "achievements": [
            "Organized 20+ training sessions for members",
            "Coordinated inter-college frisbee competitions",
            "Led team to participate in city-level tournaments",
            "Increased association membership by 50%",
        ],
        "skills_gained": ["Leadership", "Event Coordination", "Team Management", "Sports Promotion", "Communication"],
        "tags": ["Sports", "Leadership", "Campus"],
    },
    {
        "id": "guitar",
        "organization": "Shantou University Guitar Association",
        "chinese_organization": "汕头大学吉他协会",
        "role": "Member",
        "chinese_role": "成员",
        "period": "2023.09 - 2024.09",
        "location": "Shantou, China",
        "description": "Actively participated in the Guitar Association, enhancing musical skills and performing at campus events.",
        "long_description": "As a member of the Guitar Association, I received regular guitar training, participated in weekly practice sessions, and performed at various campus events including welcome parties and charity concerts. This experience helped me develop musical talent, stage performance skills, and teamwork abilities.",
        "image_path": BASE_DIR / "data" / "resume" / "practice" / "Scanned_20260713_025411.pdf",
        "image_type": "pdf",
        "gallery_images": [
            BASE_DIR / "data" / "resume" / "practice" / "Shantou University Guitar Association" / "00c0f6e9aef1951dac9323027bb3f77.png",
            BASE_DIR / "data" / "resume" / "practice" / "Shantou University Guitar Association" / "a0934f29546659c5d71e57d7cfe2c8c.jpg",
        ],
        "achievements": [
            "Received professional guitar training",
            "Participated in weekly practice sessions",
            "Performed at 5+ campus events",
            "Collaborated with other musicians in ensemble performances",
        ],
        "skills_gained": ["Guitar Playing", "Musical Performance", "Teamwork", "Stage Confidence", "Time Management"],
        "tags": ["Music", "Campus", "Performance"],
    },
    {
        "id": "jinzhi_yidong",
        "organization": "\"Jinzhi Yidong\" Rural Revitalization Team",
        "chinese_organization": "百千万突击队\"金智益东\"",
        "role": "Team Member",
        "chinese_role": "队员",
        "period": "2024.07 - 2024.08",
        "location": "Chaozhou, China",
        "description": "Participated in the \"Jinzhi Yidong\" rural revitalization program, using technology to support local agricultural development.",
        "long_description": "As a member of the \"Jinzhi Yidong\" team, I participated in summer rural revitalization activities in Chaozhou. I used data analysis and digital technology to help local farmers improve agricultural production efficiency, and participated in promoting e-commerce for agricultural products to increase local income.",
        "image_path": BASE_DIR / "data" / "resume" / "practice" / "5a63c6a2d8bd6b529a0475b1a1a87ac.png",
        "image_type": "image",
        "gallery_images": [
            BASE_DIR / "data" / "resume" / "practice" / "Jinzhi Yidong Rural Revitalization Team" / "3a724cb23b83a36e9f779571297ba2b.png",
            BASE_DIR / "data" / "resume" / "practice" / "Jinzhi Yidong Rural Revitalization Team" / "5fc7951417fe04941bc758a05e34d70.png",
            BASE_DIR / "data" / "resume" / "practice" / "Jinzhi Yidong Rural Revitalization Team" / "e87a3f406810aeed597b8466050692d.png",
        ],
        "achievements": [
            "Applied data analysis to optimize agricultural production",
            "Helped local farmers establish e-commerce sales channels",
            "Participated in digital literacy training for rural residents",
            "Contributed to rural revitalization through technology support",
        ],
        "skills_gained": ["Data Analysis", "Digital Technology", "Rural Development", "Team Collaboration", "Problem Solving"],
        "tags": ["Rural Revitalization", "Technology", "Social Practice"],
    },
]

RESUME_SECTIONS = [
    {
        "id": "education",
        "title": "Education Background",
        "chinese_title": "教育背景",
        "content": [
            {
                "institution": "Shantou University",
                "chinese_institution": "汕头大学",
                "degree": "Bachelor of Engineering",
                "major": "Data Science and Big Data Technology",
                "period": "2022.09 - 2026.06",
                "gpa": "4.0/5.0",
                "ranking": "Top 10%",
                "relevant_courses": ["Data Structures", "Machine Learning", "Deep Learning", "Data Visualization", "Large Language Models"],
            },
        ],
    },
    {
        "id": "skills",
        "title": "Technical Skills",
        "chinese_title": "技术技能",
        "content": {
            "programming": ["Python", "Java", "JavaScript", "C++", "MATLAB", "SQL"],
            "machine_learning": ["PyTorch", "TensorFlow", "Scikit-learn", "OpenCV", "NLP", "Computer Vision"],
            "web_development": ["Flask", "FastAPI", "Node.js", "React", "Bootstrap", "HTML/CSS"],
            "data_engineering": ["Pandas", "NumPy", "Matplotlib", "Seaborn", "Data Visualization", "ETL"],
            "tools": ["Git", "Docker", "VS Code", "Jupyter", "Linux", "AWS"],
        },
    },
    {
        "id": "languages",
        "title": "Language Proficiency",
        "chinese_title": "语言能力",
        "content": [
            {"language": "Mandarin", "proficiency": "Native"},
            {"language": "English", "proficiency": "TOEFL 95+, IELTS 6.5+"},
            {"language": "Cantonese", "proficiency": "Conversational"},
        ],
    },
]

SYSTEM_PROMPT = """You are a dedicated portfolio and application-advising assistant. Answer interviewers' or admission reviewers' questions from the supplied evidence blocks only.

Rules:
1. Every answer must be grounded in the supplied evidence. Do not invent projects, achievements, papers, technical experience, metrics, personal contributions, school requirements, admissions preferences, or faculty information.
1a. The portfolio owner's Chinese name is 陈梓深. Never translate or infer it as another Chinese name.
2. Retrieved document chunks are the only source for the portfolio owner's background, achievements, papers, projects, internships, skills, and personal fit. Web search evidence may be used only for external school/program/admission/faculty/curriculum facts.
2a. If the question asks for application fit or school-specific advantages, synthesize the portfolio evidence with the web evidence, and make it clear which points come from the applicant's portfolio and which come from the target school/program information.
2b. If neither evidence block contains relevant evidence, reply only with the no-evidence sentence specified in the user prompt.
3. Reply in the exact response language specified by the user prompt. This language instruction overrides the language of retrieved evidence, titles, project names, paper names, and conversation history. If the required response language is Chinese, write the explanation in Chinese even when the retrieved source text is English. Keep original paper/project names unchanged when needed.
4. Write concisely and professionally for graduate-school or job-interview scenarios. Use clear bullet points when helpful, and explain project difficulty, personal contribution, technologies used, and innovation points only when supported by evidence.
5. When the user asks for self-introduction, mock interview questions, project highlights, or paper innovation summaries, actively synthesize the retrieved evidence into structured interview-ready copy.
6. Do not output irrelevant content or exaggerate personal experience.
7. In the Competitions & Awards section, the word "competition" or Chinese "比赛/竞赛" refers to records whose category is exactly "Competition". Do not include Sports or Scholarship records unless the user explicitly asks about sports, frisbee, athletics, scholarships, or awards in the broader sense.
"""
