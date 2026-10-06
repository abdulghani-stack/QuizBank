"""
Official University of Mumbai T.E. Artificial Intelligence & Data Science Syllabus
Effective from Academic Year 2026-27 (Semester V)
"""

SEMESTER = "Semester V"

SUBJECT_CATEGORIES = {
    "CORE": "Core Subjects",
    "ELECTIVE_1": "Program Elective-I",
    "OTHER": "Other"
}

SYLLABUS_STRUCTURE = [
    {
        "subject": "Statistics for Machine Learning and Data Science",
        "subject_code": "2015111",
        "category_type": "CORE",
        "category_title": "Core Subjects",
        "modules": [
            {
                "module_number": 1,
                "module": "Statistical Foundations, Covariance, and Sampling",
                "topics": [
                    "Types of data", "Categorical data", "Numerical data", "Ordinal data",
                    "Central tendency", "Dispersion", "Skewness", "Kurtosis",
                    "Histograms", "Boxplots", "Scatter plots", "Pair plots",
                    "Normal distribution", "Binomial distribution", "Poisson distribution",
                    "Exponential distribution", "Uniform distribution", "Beta distribution",
                    "Gamma distribution", "Covariance", "Correlation", "Confounding",
                    "Correlation matrices", "Euclidean distance", "Manhattan distance",
                    "Cosine distance", "Simple random sampling", "Stratified sampling",
                    "Cluster sampling", "Central Limit Theorem", "Law of Large Numbers",
                    "Missing value handling", "Outlier treatment", "Encoding", "Normalization"
                ]
            },
            {
                "module_number": 2,
                "module": "Statistical Inference, Estimation & Resampling",
                "topics": [
                    "Point estimates", "Bias", "Variance", "MSE",
                    "Maximum Likelihood Estimation", "Method of Moments", "Confidence intervals",
                    "Mean confidence interval", "Proportion confidence interval", "Variance confidence interval",
                    "z-test", "t-test", "chi-square test", "ANOVA", "Mann-Whitney U",
                    "Kruskal-Wallis", "Bootstrap confidence intervals", "Permutation tests",
                    "Likelihood Ratio Tests", "Bonferroni correction", "FDR", "Monte Carlo simulation"
                ]
            },
            {
                "module_number": 3,
                "module": "Regression Models, Regularization & Nonlinear Models",
                "topics": [
                    "Simple linear regression", "Multiple linear regression", "Model assumptions",
                    "Residual analysis", "Multicollinearity", "VIF", "Leverage", "Cook's distance",
                    "Polynomial regression", "Interaction effects", "Nonlinear regression",
                    "Ridge regression", "Lasso regression", "Elastic Net", "Model selection",
                    "Bias-variance considerations"
                ]
            },
            {
                "module_number": 4,
                "module": "Classification & Supervised Learning",
                "topics": [
                    "Accuracy", "Precision", "Recall", "F1-score", "ROC-AUC",
                    "Precision-Recall curves", "Logistic regression", "Odds ratio",
                    "Decision boundary", "Naive Bayes", "k-NN", "Decision Trees",
                    "Pruning", "Bagging", "Random Forest", "Gradient Boosting", "SVM",
                    "Kernel trick", "SMOTE", "Class weights", "Stratified splits",
                    "Confusion matrix", "Error tradeoffs", "Platt scaling", "Isotonic regression"
                ]
            },
            {
                "module_number": 5,
                "module": "Unsupervised Learning & Dimensionality Reduction",
                "topics": [
                    "PCA", "LDA", "Kernel PCA", "ICA", "K-means", "Hierarchical clustering",
                    "DBSCAN", "Silhouette score", "Davies-Bouldin index", "t-SNE", "UMAP",
                    "Z-score outlier detection", "IQR", "Isolation Forest", "LOF"
                ]
            },
            {
                "module_number": 6,
                "module": "Model Evaluation, Bayesian Inference & Ethics",
                "topics": [
                    "AIC", "BIC", "Bias-variance", "k-fold cross-validation", "LOOCV",
                    "Repeated cross-validation", "Calibration", "Brier score", "Prior",
                    "Likelihood", "Posterior", "MAP", "MLE", "Beta-Bernoulli",
                    "Normal-Normal conjugate priors", "Bayesian Naive Bayes", "SHAP", "LIME",
                    "PDP", "ICE", "Equalized odds", "Demographic parity", "Model bias",
                    "Transparency", "Data ethics"
                ]
            }
        ]
    },
    {
        "subject": "Artificial Intelligence and Soft Computing",
        "subject_code": "2015112",
        "category_type": "CORE",
        "category_title": "Core Subjects",
        "modules": [
            {
                "module_number": 1,
                "module": "Introduction to AI & Soft Computing",
                "topics": [
                    "Artificial Intelligence", "AI perspectives", "AI applications",
                    "Present state of AI", "Soft Computing", "Soft Computing constituents",
                    "Neuro Computing", "Characteristics of Soft Computing",
                    "Hard Computing vs Soft Computing", "Learning", "Adaptation",
                    "Generative AI", "ChatGPT-like models", "Ethical challenges in AI"
                ]
            },
            {
                "module_number": 2,
                "module": "Solving Problems by Searching",
                "topics": [
                    "State space representation", "Problem formulation", "State space search",
                    "DFS", "BFS", "Greedy Best First Search", "A* Search", "Hill Climbing",
                    "Simulated Annealing", "Game Playing", "Adversarial Search"
                ]
            },
            {
                "module_number": 3,
                "module": "Knowledge and Reasoning",
                "topics": [
                    "Knowledge Representation Systems", "Propositional Logic", "Syntax",
                    "Semantics", "Logical connectives", "Predicate Logic", "FOPL",
                    "Quantification", "Inference rules", "Forward Chaining",
                    "Backward Chaining", "Resolution", "Uncertain knowledge",
                    "Random variables", "Prior probability", "Posterior probability",
                    "Ontologies", "Semantic Web reasoning"
                ]
            },
            {
                "module_number": 4,
                "module": "Fuzzy Set Theory, Fuzzy Rules, Reasoning and Inference",
                "topics": [
                    "Fuzzy sets", "Fuzzy relations", "Membership functions",
                    "Features of membership functions", "Fuzzification", "Defuzzification",
                    "Fuzzy IF-THEN rules", "Fuzzy reasoning", "Fuzzy inference systems"
                ]
            },
            {
                "module_number": 5,
                "module": "Neural Networks",
                "topics": [
                    "Biological neuron", "Artificial neuron", "McCulloch-Pitts neuron",
                    "Perceptron", "Single-layer perceptron", "Multi-layer perceptron",
                    "Linear separability", "Delta rule", "Forward propagation",
                    "Backpropagation", "Hebbian learning", "Winner-Take-All",
                    "Self-Organizing Maps", "Learning Vector Quantization",
                    "CNN introduction", "RNN introduction"
                ]
            },
            {
                "module_number": 6,
                "module": "Hybrid System",
                "topics": [
                    "Hybrid systems", "Industrial control", "Robotics", "Forecasting",
                    "ANFIS", "Fuzzy systems", "Neural systems", "Neuro-Fuzzy systems",
                    "Comparative analysis", "Sustainability", "Governance"
                ]
            }
        ]
    },
    {
        "subject": "Agile Software Development and DevOps",
        "subject_code": "2015113",
        "category_type": "CORE",
        "category_title": "Core Subjects",
        "modules": [
            {
                "module_number": 1,
                "module": "Agile Project Management & DevOps Integration",
                "topics": [
                    "Agile fundamentals", "Scrum", "Jira", "Agile project lifecycle",
                    "Epics", "User stories", "Tasks", "Sprints", "Sprint planning",
                    "Assignment", "Tracking", "Jira-CI/CD integration", "Burndown chart",
                    "Velocity chart", "Kanban vs Scrum", "Sprint review", "Retrospective"
                ]
            },
            {
                "module_number": 2,
                "module": "Version Control & Collaboration using Git",
                "topics": [
                    "Git", "GitHub", "clone", "commit", "push", "pull",
                    "Branching", "Merging", "Feature branching", "Git Flow",
                    "Merge conflicts", "GitHub Actions", "GitHub Issues",
                    "GitHub Project Boards", "GitHub Webhooks"
                ]
            },
            {
                "module_number": 3,
                "module": "CI/CD Automation using Jenkins & Containerization using Docker",
                "topics": [
                    "CI/CD", "DevOps pipelines", "Jenkins", "Jenkins installation",
                    "Jenkins jobs", "GitHub webhook integration", "Build", "Test",
                    "Package", "Docker", "Images", "Containers", "Dockerfiles",
                    "Docker Compose", "Multi-service deployment", "Jenkinsfile",
                    "Pipeline as Code", "Docker Hub", "ECR"
                ]
            },
            {
                "module_number": 4,
                "module": "Configuration Automation, Orchestration & Cloud Provisioning",
                "topics": [
                    "Ansible", "Inventory", "Playbooks", "Roles", "Provisioning",
                    "Configuration", "Kubernetes", "Pods", "Deployments", "Services",
                    "Ingress", "Container orchestration", "Terraform", "Providers",
                    "Resources", "State files", "Cloud infrastructure", "Helm Charts",
                    "Terraform Cloud", "Remote state"
                ]
            },
            {
                "module_number": 5,
                "module": "Agile Quality Assurance & Testing",
                "topics": [
                    "Agile metrics", "Agile QA", "Functionality testing", "UI testing",
                    "Performance testing", "Security testing", "Agile testing principles",
                    "Agile Testing Quadrants", "Test Driven Development", "Acceptance testing",
                    "Refactoring", "Agile automation", "Test Automation Pyramid",
                    "Selenium", "Jira case study", "Continuous Testing", "BDD",
                    "Exploratory testing", "Cypress", "Postman", "JMeter"
                ]
            },
            {
                "module_number": 6,
                "module": "DevOps",
                "topics": [
                    "DevOps introduction", "Importance", "Benefits", "DevOps principles",
                    "DevOps practices", "7-Cs of DevOps lifecycle", "Business agility",
                    "Continuous testing", "DevOps tool selection", "Implementation challenges",
                    "Application-to-DevOps mapping", "DevOps assessment", "Open-source DevOps tools",
                    "CI/CD pipelines", "Cloud-based DevOps", "DevOps case studies"
                ]
            }
        ]
    },
    {
        "subject": "Web and Mobile Application Development",
        "subject_code": "2015114",
        "category_type": "ELECTIVE_1",
        "category_title": "Program Elective-I",
        "modules": [
            {
                "module_number": 1,
                "module": "Core Web and Mobile Development Concepts",
                "topics": [
                    "REST APIs", "API architectures", "Architectural principles",
                    "Architectural styles", "MVC", "MVVM", "MERN", "MEAN",
                    "PERN", "Progressive Web Apps"
                ]
            },
            {
                "module_number": 2,
                "module": "Front-End Development with React",
                "topics": [
                    "React foundations", "JSX", "Components", "React DevTools",
                    "Data flow", "Events", "Forms", "Refs", "Styling",
                    "Hooks", "Routing", "Error boundaries", "Deployment",
                    "Project initialization", "Fetching data", "Caching data",
                    "React portals", "Accessibility", "Redux"
                ]
            },
            {
                "module_number": 3,
                "module": "Kotlin Core",
                "topics": [
                    "Kotlin basics", "Variables", "Types", "Conditions", "Functions",
                    "Unit", "Anonymous functions", "Standard functions", "Null safety",
                    "Exceptions", "List", "Set", "Map", "map", "filter", "forEach",
                    "reduce", "fold", "Classes", "Initialization", "Inheritance",
                    "Objects", "Nested classes", "Data classes", "Enum classes",
                    "Operator overloading", "Interfaces", "Abstract classes",
                    "Generics", "Extensions", "Java interoperability"
                ]
            },
            {
                "module_number": 4,
                "module": "Kotlin Backend & Advanced Kotlin",
                "topics": [
                    "Spring Boot", "Database", "ORM", "OAuth2", "JWT", "Sessions",
                    "RBAC", "Microservices", "Deployment", "Testing", "Monitoring",
                    "Scaling", "Annotations", "Reflection", "DSL", "Coroutines",
                    "Ktor", "REST APIs", "Jetpack Compose", "Kotlin Multiplatform"
                ]
            },
            {
                "module_number": 5,
                "module": "Flutter & Dart",
                "topics": [
                    "Flutter", "Flutter architecture", "Widgets", "Gestures", "Dart",
                    "Variables", "Types", "Decisions", "Loops", "Functions", "OOP",
                    "Build visualization", "Exceptions", "Debugging", "Futures",
                    "Async/Await", "Streams", "Layouts", "State management",
                    "Scoped model", "Navigation", "Routing"
                ]
            },
            {
                "module_number": 6,
                "module": "Advanced Flutter Development",
                "topics": [
                    "UI styles", "Assets", "Fonts", "Models", "APIs", "MediaQuery",
                    "Lists", "Grids", "Animations", "Custom UI", "Drawing",
                    "Flutter packages", "Flutter plugins", "REST APIs",
                    "Product Service API", "Firebase", "Firebase Authentication",
                    "Firestore", "AI/ML API integration", "Cloud mobile apps",
                    "Mobile e-commerce"
                ]
            }
        ]
    },
    {
        "subject": "User Experience Design with VR",
        "subject_code": "2015115",
        "category_type": "ELECTIVE_1",
        "category_title": "Program Elective-I",
        "modules": [
            {
                "module_number": 1,
                "module": "Introduction",
                "topics": [
                    "Interface design", "Interface conceptualization", "User cognition",
                    "Core UX elements", "UX elements", "Norman's design principles",
                    "Human perception", "Visual processing"
                ]
            },
            {
                "module_number": 2,
                "module": "UX Design Life Cycle",
                "topics": [
                    "UX", "Ubiquitous interaction", "Usability", "Usability to UX",
                    "Emotional impact", "UX business case", "Roots of usability"
                ]
            },
            {
                "module_number": 3,
                "module": "UX Design Process",
                "topics": [
                    "System concept", "User work activity", "Emotional aspects",
                    "Contextual inquiry", "Data/model driven inquiry", "Contextual analysis",
                    "Interaction design requirements", "Information models",
                    "Information architecture", "Interaction design", "Prototyping",
                    "Design paradigms", "Design thinking", "Personas", "Ideation",
                    "Sketching", "Phenomenology", "Mental models", "Conceptual design",
                    "Wireframes", "Web UX", "Mobile UX", "Prototype testing", "Use-case modelling"
                ]
            },
            {
                "module_number": 4,
                "module": "UX Evolution and Improvement",
                "topics": [
                    "UX goals", "UX metrics", "UX targets", "Formative evaluation",
                    "Summative evaluation", "Evaluation data", "Data collection",
                    "Walkthroughs", "Reviews", "Heuristic evaluation", "UX inspection",
                    "Questionnaires", "Rapid UX evaluation", "Iterative UX improvement",
                    "UX in Agile", "UX in Design Thinking", "UX maturity models"
                ]
            },
            {
                "module_number": 5,
                "module": "Introduction to VR",
                "topics": [
                    "Virtual Reality", "Three I's", "VR history", "Five classic components",
                    "Trackers", "Navigation interfaces", "Gesture interfaces", "Graphics",
                    "3D sound", "Haptics", "Immersive interaction", "Cognitive engagement",
                    "Gesture recognition"
                ]
            },
            {
                "module_number": 6,
                "module": "Applications of Virtual Reality",
                "topics": [
                    "Geometric modelling", "Kinematics", "Physical modelling",
                    "Behaviour modelling", "Model management", "Human factors",
                    "VR methodology", "VR terminology", "User performance"
                ]
            }
        ]
    },
    {
        "subject": "Computer Network",
        "subject_code": "2015116",
        "category_type": "ELECTIVE_1",
        "category_title": "Program Elective-I",
        "modules": [
            {
                "module_number": 1,
                "module": "Introduction to Computer Networks",
                "topics": [
                    "LAN", "MAN", "WAN", "Wireless networks", "Network software",
                    "Protocols", "Network layer design issues", "OSI model", "TCP/IP model",
                    "Network topologies", "Transmission media", "Client-server",
                    "Peer-to-peer", "Hybrid architecture", "Bridge", "Switch",
                    "Router", "Gateway", "Access Point"
                ]
            },
            {
                "module_number": 2,
                "module": "Data Link Layer",
                "topics": [
                    "Data Link Layer", "Services", "Framing", "Error control",
                    "Flow control", "Error detection", "Error correction", "Parity",
                    "Checksum", "Hamming Codes", "CRC", "Unrestricted Simplex",
                    "Stop and Wait", "Sliding Window", "MAC", "Pure ALOHA",
                    "Slotted ALOHA", "CSMA", "CSMA/CD", "CSMA/CA", "WDMA",
                    "IEEE 802.3", "IEEE 802.11"
                ]
            },
            {
                "module_number": 3,
                "module": "Network Layer",
                "topics": [
                    "Network layer design", "Circuit switching", "Message switching",
                    "Packet switching", "IP", "IP classes", "IPv4", "IPv6", "NAT",
                    "Subnetting", "Supernetting", "CIDR", "ARP", "RARP", "ICMP",
                    "IGMP", "Static routing", "Dynamic routing", "Distance Vector",
                    "Link State", "RIP", "OSPF", "BGP", "Count-to-Infinity", "AODV", "DSR"
                ]
            },
            {
                "module_number": 4,
                "module": "Transport Layer",
                "topics": [
                    "Process-to-process delivery", "Transport services", "Socket programming",
                    "Addressing", "Connection establishment", "Connection release",
                    "TCP timers", "TCP state transition", "Flow control", "Buffering",
                    "Multiplexing", "Congestion control", "Slow start", "TCP", "UDP", "QoS"
                ]
            },
            {
                "module_number": 5,
                "module": "Application Layer",
                "topics": [
                    "Web", "HTTP", "Web caching", "DNS", "SMTP", "POP3", "Webmail",
                    "FTP", "TELNET", "DHCP", "SNMP", "Google DNS"
                ]
            },
            {
                "module_number": 6,
                "module": "Emerging & Advanced Topics",
                "topics": [
                    "VPN", "VPN types", "SDN", "Control plane", "Data plane",
                    "OpenFlow", "SDN controllers", "NFV", "NFV benefits",
                    "Data Center Networks", "Fat Tree", "SD-WAN"
                ]
            }
        ]
    },
    {
        "subject": "Indian Knowledge System",
        "subject_code": "2015511",
        "category_type": "OTHER",
        "category_title": "Other",
        "modules": [
            {
                "module_number": 1,
                "module": "Acoustic Science in Vedic Chanting and Indian Music",
                "topics": [
                    "Nāda", "Sound", "Frequency", "Pitch", "Harmonic content",
                    "Shruti", "22 microtones", "Frequency discrimination",
                    "Indian acoustic practices"
                ]
            },
            {
                "module_number": 2,
                "module": "Indian Knowledge and Sustainable/Renewable Energy",
                "topics": [
                    "Ancient Indian energy practices", "Renewable energy knowledge",
                    "Traditional energy systems", "Sustainability", "Modern engineering interpretation"
                ]
            },
            {
                "module_number": 3,
                "module": "Linguistics, Number Systems and Rainfall Prediction",
                "topics": [
                    "Language components", "Pāṇini", "Sanskrit", "Sanskrit NLP",
                    "Indian number system", "Decimal system", "Katapayadi", "Pingala",
                    "Binary", "Calendar", "Panchang", "Nakshatras",
                    "Traditional rainfall indicators", "Natural indicators"
                ]
            },
            {
                "module_number": 4,
                "module": "Mathematics Foundations in Ancient India and Relevance to IT",
                "topics": [
                    "Ancient numeration", "Zero", "Decimal place value", "Aryabhata",
                    "Brahmagupta", "Bhaskara II", "Rule-based mathematical procedures",
                    "Algorithmic thinking", "Modular arithmetic", "Binary representation",
                    "Coding", "Checksums", "Parity", "Cryptography"
                ]
            },
            {
                "module_number": 5,
                "module": "Indian Logic and its Applications in IT",
                "topics": [
                    "IKS and modern technology", "Indian logic", "Language", "Computation",
                    "Knowledge organization", "Data", "Decision-making", "Ethics",
                    "Society", "Sustainability", "Responsible digital systems", "Apps",
                    "Chatbots", "Databases", "Awareness tools", "Nyaya logic",
                    "Paninian grammar", "NLP", "Knowledge classification",
                    "Knowledge graphs", "Indian-language digital tools"
                ]
            },
            {
                "module_number": 6,
                "module": "Sanskrit Grammar and Computational Modules",
                "topics": [
                    "Sanskrit structured language", "Sounds", "Words", "Roots",
                    "Suffixes", "Sandhi", "Sentence structure", "Paninian grammar",
                    "Rule-based systems", "Tokenization", "Morphology", "Parsing",
                    "Language rules", "NLP", "Sanskrit digital tools"
                ]
            }
        ]
    }
]
