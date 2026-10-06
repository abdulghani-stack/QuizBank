"""
Study Material — Theory Content Layer for QuizBank
University of Mumbai T.E. AI & DS (Sem V, 2026-27)

Data structure mirrors SYLLABUS_STRUCTURE hierarchy.
Each topic entry can have:
  - overview         : 1-2 sentence summary
  - concepts         : list of key concept dicts {term, definition}
  - explanation      : detailed paragraph
  - examples         : list of example dicts {title, body}
  - key_points       : list of brief important strings
  - common_mistakes  : list of mistake strings
"""

# ---------------------------------------------------------------------------
# Subject 1: Statistics for Machine Learning and Data Science
# ---------------------------------------------------------------------------
_STATS = {
    "subject": "Statistics for Machine Learning and Data Science",
    "subject_code": "2015111",
    "description": "Covers statistical theory, probability distributions, regression, classification metrics, and Bayesian methods essential for AI/ML engineers.",
    "modules": [
        {
            "module_number": 1,
            "title": "Statistical Foundations, Covariance, and Sampling",
            "description": "Explore types of data, central tendency, dispersion, probability distributions, distance metrics, and sampling strategies.",
            "topics": [
                {
                    "name": "Types of data",
                    "overview": "Data can be categorical (nominal/ordinal) or numerical (interval/ratio). Choosing the right statistical method depends on data type.",
                    "concepts": [
                        {"term": "Nominal Data", "definition": "Categories without order (e.g., Gender, Eye Color)."},
                        {"term": "Ordinal Data", "definition": "Categories with meaningful order but unequal intervals (e.g., Credit Grades AAA, AA, A)."},
                        {"term": "Interval Data", "definition": "Ordered data with equal spacing but no true zero (e.g., Temperature in Celsius)."},
                        {"term": "Ratio Data", "definition": "Interval data with a meaningful zero (e.g., Weight, Height, Transaction Amount)."}
                    ],
                    "explanation": "Understanding data types is the first step in any analysis. Nominal data supports mode only; ordinal data supports median and mode; interval/ratio data support all statistical measures. In ML, data type determines preprocessing: encoding for nominal, scaling for ratio.",
                    "examples": [
                        {"title": "Classification Example", "body": "Customer ID = Nominal. Credit Rating (AAA, AA, A) = Ordinal. Temperature in Celsius = Interval. Transaction Amount = Ratio."}
                    ],
                    "key_points": [
                        "Nominal: no ranking, only categories",
                        "Ordinal: ranked, but gaps are unequal",
                        "Interval: equal gaps, no absolute zero",
                        "Ratio: equal gaps + absolute zero (Kelvin, weight)",
                        "Most ML algorithms need numerical input"
                    ],
                    "common_mistakes": [
                        "Treating ordinal data as interval (assuming equal gaps between ranks)",
                        "Applying mean to ordinal data -- use median instead",
                        "Confusing interval and ratio (Celsius vs Kelvin)"
                    ]
                },
                {
                    "name": "Normal distribution",
                    "overview": "The bell-shaped normal distribution is fundamental to statistics; many ML algorithms assume normality.",
                    "concepts": [
                        {"term": "Mean (mu)", "definition": "Centre of the distribution."},
                        {"term": "Std Dev (sigma)", "definition": "Width/spread of the bell curve."},
                        {"term": "68-95-99.7 Rule", "definition": "68% of data within 1 sigma, 95% within 2 sigma, 99.7% within 3 sigma."},
                        {"term": "Z-score", "definition": "Standardised distance from mean: z = (x - mu) / sigma."}
                    ],
                    "explanation": "A normal distribution N(mu, sigma^2) is symmetric around the mean. Z-scores allow comparison across different scales. In ML, normalization to N(0,1) (StandardScaler) improves gradient descent convergence.",
                    "examples": [
                        {"title": "Z-score", "body": "Height: mu=170cm, sigma=10cm. A person 190cm tall has z = (190-170)/10 = 2.0. They are 2 standard deviations above average."}
                    ],
                    "key_points": [
                        "Symmetric, bell-shaped curve",
                        "Defined entirely by mu and sigma",
                        "Standard Normal: N(0,1)",
                        "Basis for z-tests, t-tests, and linear regression assumptions"
                    ],
                    "common_mistakes": [
                        "Assuming all data is normally distributed without checking",
                        "Confusing population std dev with sample std dev"
                    ]
                },
                {
                    "name": "Covariance",
                    "overview": "Covariance measures how two variables change together; it is the unnormalised form of correlation.",
                    "concepts": [
                        {"term": "Positive Covariance", "definition": "Both variables tend to increase together."},
                        {"term": "Negative Covariance", "definition": "One increases as the other decreases."},
                        {"term": "Covariance Matrix", "definition": "n x n matrix capturing pairwise covariances of n features; used in PCA."}
                    ],
                    "explanation": "Cov(X,Y) = E[(X-muX)(Y-muY)]. Unlike correlation, covariance is not bounded and depends on units. PCA uses the eigendecomposition of the covariance matrix to find principal components.",
                    "examples": [
                        {"title": "Interpretation", "body": "Cov(Study Hours, Exam Score) > 0: more study, higher scores. Cov(Temperature, Heating Bill) < 0: higher temp, lower bill."}
                    ],
                    "key_points": [
                        "Correlation = Cov(X,Y) / (sigmaX * sigmaY) -- normalised to [-1, +1]",
                        "Cov(X,X) = Var(X)"
                    ],
                    "common_mistakes": [
                        "Interpreting high covariance as strong relationship -- it depends on scale",
                        "Forgetting that correlation (not covariance) is scale-independent"
                    ]
                }
            ]
        },
        {
            "module_number": 2,
            "title": "Statistical Inference, Estimation and Resampling",
            "description": "Hypothesis testing, confidence intervals, bootstrap methods, and key statistical tests.",
            "topics": [
                {
                    "name": "Maximum Likelihood Estimation",
                    "overview": "MLE finds parameter values that maximise the probability of observing the given data.",
                    "concepts": [
                        {"term": "Likelihood Function", "definition": "L(theta|data) -- probability of data given parameters theta."},
                        {"term": "Log-Likelihood", "definition": "ln L(theta) -- used for computational simplicity."},
                        {"term": "MLE Estimator", "definition": "theta = argmax L(theta); the parameter that makes data most probable."}
                    ],
                    "explanation": "MLE is the foundation of logistic regression, Naive Bayes, and Gaussian Mixture Models. For normally distributed data, MLE of mean = sample mean. Log-likelihood avoids numerical underflow.",
                    "examples": [
                        {"title": "Coin Flip MLE", "body": "Observe 7 heads in 10 flips. MLE for p = 7/10 = 0.7. The value p=0.7 maximises P(7 heads | p)."}
                    ],
                    "key_points": [
                        "MLE produces consistent and asymptotically efficient estimates",
                        "Cross-entropy loss in neural networks = negative log-likelihood"
                    ],
                    "common_mistakes": [
                        "Confusing MLE with MAP -- MAP includes a Bayesian prior"
                    ]
                },
                {
                    "name": "z-test",
                    "overview": "A z-test is used to test hypotheses about population means when population variance is known and n is large.",
                    "concepts": [
                        {"term": "Null Hypothesis (H0)", "definition": "The claim assumed true until evidence says otherwise."},
                        {"term": "p-value", "definition": "Probability of observing results as extreme as the sample under H0."},
                        {"term": "z-statistic", "definition": "z = (x_bar - mu0) / (sigma / sqrt(n))"}
                    ],
                    "explanation": "Reject H0 if |z| > z_critical (e.g., 1.96 for alpha=0.05, two-tailed). A p-value < 0.05 means results are statistically significant at the 5% level.",
                    "examples": [
                        {"title": "Example", "body": "Claim: mean = 100. Sample: n=50, x_bar=105, sigma=15. z = (105-100)/(15/sqrt(50)) = 2.36. Since 2.36 > 1.96, reject H0."}
                    ],
                    "key_points": [
                        "Use z-test when sigma is known and n >= 30",
                        "Use t-test when sigma is unknown",
                        "Critical values: 1.645 (10%), 1.96 (5%), 2.576 (1%)"
                    ],
                    "common_mistakes": [
                        "Using z-test when population variance is unknown (use t-test)",
                        "Confusing statistical significance with practical significance"
                    ]
                }
            ]
        },
        {
            "module_number": 4,
            "title": "Classification and Supervised Learning",
            "description": "Metrics and algorithms for supervised classification problems.",
            "topics": [
                {
                    "name": "Precision",
                    "overview": "Precision measures the fraction of predicted positives that are actually positive -- a measure of exactness.",
                    "concepts": [
                        {"term": "Precision", "definition": "TP / (TP + FP). Of all predicted positives, how many are truly positive?"},
                        {"term": "Recall (Sensitivity)", "definition": "TP / (TP + FN). Of all actual positives, how many did we detect?"},
                        {"term": "F1-Score", "definition": "Harmonic mean of Precision and Recall: 2*P*R / (P+R)."}
                    ],
                    "explanation": "High precision = few false alarms. High recall = few missed positives. F1 balances both and is preferred for imbalanced datasets.",
                    "examples": [
                        {"title": "Email Spam", "body": "Spam filter: 100 emails, 40 actually spam. Model flags 50 as spam, 35 truly spam. Precision = 35/50 = 70%. Recall = 35/40 = 87.5%."}
                    ],
                    "key_points": [
                        "Precision matters when false positives are costly (e.g., fraud alerts)",
                        "Recall matters when false negatives are costly (e.g., cancer screening)",
                        "F1 is best for imbalanced classes",
                        "ROC-AUC aggregates performance across all thresholds"
                    ],
                    "common_mistakes": [
                        "Using accuracy for imbalanced datasets (use F1/AUC instead)"
                    ]
                },
                {
                    "name": "Random Forest",
                    "overview": "Random Forest is an ensemble of decision trees, each trained on a bootstrap sample with random feature selection.",
                    "concepts": [
                        {"term": "Bootstrap Aggregating (Bagging)", "definition": "Training each tree on a random sample with replacement."},
                        {"term": "Feature Randomness", "definition": "At each split, only a random subset of features is considered (sqrt(n) for classification)."},
                        {"term": "Out-of-Bag (OOB) Error", "definition": "Estimated error using samples not selected in bootstrap -- free validation."}
                    ],
                    "explanation": "By combining many uncorrelated trees, Random Forest reduces variance without increasing bias. Individual trees overfit but their errors cancel in aggregation.",
                    "examples": [
                        {"title": "Feature Importance", "body": "Random Forest trained on medical data ranks Blood Pressure and Age as top features for heart disease prediction."}
                    ],
                    "key_points": [
                        "Ensemble of N decision trees (N typically 100-500)",
                        "Each tree sees ~63.2% of training data (bootstrap)",
                        "Classification: majority vote; Regression: mean of outputs"
                    ],
                    "common_mistakes": [
                        "Using too few trees (underfitting the ensemble)"
                    ]
                }
            ]
        }
    ]
}

# ---------------------------------------------------------------------------
# Subject 2: Artificial Intelligence and Soft Computing
# ---------------------------------------------------------------------------
_AI = {
    "subject": "Artificial Intelligence and Soft Computing",
    "subject_code": "2015112",
    "description": "Covers classical AI, search algorithms, knowledge representation, fuzzy logic, neural networks, and hybrid intelligent systems.",
    "modules": [
        {
            "module_number": 1,
            "title": "Introduction to AI and Soft Computing",
            "description": "Foundations of artificial intelligence, its perspectives, applications, and the principles of soft computing.",
            "topics": [
                {
                    "name": "Artificial Intelligence",
                    "overview": "AI is the simulation of human intelligence in machines enabling them to learn, reason, and act.",
                    "concepts": [
                        {"term": "Strong AI (AGI)", "definition": "Hypothetical AI with general human-level intelligence across all domains."},
                        {"term": "Weak AI (Narrow AI)", "definition": "AI designed for specific tasks (e.g., image classification, chess)."},
                        {"term": "Machine Learning", "definition": "Subset of AI: systems that learn from data without explicit programming."},
                        {"term": "Deep Learning", "definition": "Subset of ML: multi-layered neural networks for complex pattern recognition."}
                    ],
                    "explanation": "AI perspectives range from acting humanly (Turing Test) to thinking rationally (logic-based reasoning). Modern AI is mostly narrow -- excellent at specific tasks but lacking general reasoning. Generative AI (LLMs) represents the cutting edge.",
                    "examples": [
                        {"title": "AI Applications", "body": "Healthcare: disease diagnosis. Finance: fraud detection. NLP: ChatGPT. Robotics: autonomous vehicles. Recommendation: Netflix."}
                    ],
                    "key_points": [
                        "AI includes ML which includes Deep Learning (subset relationship)",
                        "Turing Test: can a machine fool a human into thinking it is human?",
                        "Soft Computing: tolerates imprecision and uncertainty",
                        "Hard Computing: exact, deterministic, rule-based"
                    ],
                    "common_mistakes": [
                        "Equating AI with ML -- ML is just one approach to AI"
                    ]
                },
                {
                    "name": "Soft Computing",
                    "overview": "Soft Computing handles imprecision using fuzzy logic, neural networks, and evolutionary computation.",
                    "concepts": [
                        {"term": "Fuzzy Logic", "definition": "Handles partial truth -- truth values between 0 and 1 instead of binary."},
                        {"term": "Neural Networks", "definition": "Learns complex mappings from data through interconnected artificial neurons."},
                        {"term": "Evolutionary Computation", "definition": "Optimization inspired by biological evolution (Genetic Algorithms)."}
                    ],
                    "explanation": "Hard computing demands exact inputs. Soft computing accepts approximate inputs and produces approximate but useful outputs. A fuzzy thermostat says temperature is somewhat hot rather than requiring an exact threshold.",
                    "examples": [
                        {"title": "Fuzzy vs Hard", "body": "Hard: if temp > 30C turn ON AC. Fuzzy: if temp is hot (membership 0.7) turn AC moderately high (60% capacity)."}
                    ],
                    "key_points": [
                        "Soft Computing constituents: Fuzzy Logic + Neural Networks + Evolutionary Algorithms",
                        "Tolerates imprecision, uncertainty, partial truth"
                    ],
                    "common_mistakes": [
                        "Confusing fuzzy logic with probability -- they model different types of uncertainty"
                    ]
                }
            ]
        },
        {
            "module_number": 2,
            "title": "Solving Problems by Searching",
            "description": "State space representation and search algorithms including uninformed and informed strategies.",
            "topics": [
                {
                    "name": "A* Search",
                    "overview": "A* is an informed search algorithm that finds the shortest path by combining actual cost (g) and heuristic estimate (h).",
                    "concepts": [
                        {"term": "f(n) = g(n) + h(n)", "definition": "Total estimated cost: g=actual cost from start, h=heuristic estimate to goal."},
                        {"term": "Admissible Heuristic", "definition": "h(n) never overestimates actual cost -- guarantees optimality."},
                        {"term": "Consistent Heuristic", "definition": "h(n) <= c(n,n') + h(n') for all edges -- stronger than admissibility."}
                    ],
                    "explanation": "A* expands nodes with the lowest f(n) first. With an admissible heuristic it always finds the optimal solution. Common heuristics: Manhattan distance (grid problems), Euclidean distance. Used in GPS routing and game pathfinding.",
                    "examples": [
                        {"title": "GPS Navigation", "body": "g(n) = actual road distance driven. h(n) = straight-line distance to destination. A* finds the shortest route efficiently."}
                    ],
                    "key_points": [
                        "A* = Dijkstra's algorithm + heuristic guidance",
                        "Optimal and complete with admissible heuristic",
                        "Greedy Best-First uses only h(n) -- faster but not optimal",
                        "BFS: uninformed, optimal for unit costs"
                    ],
                    "common_mistakes": [
                        "Using an inadmissible heuristic -- loses optimality guarantee",
                        "Confusing A* with Greedy Best-First (which ignores g(n))"
                    ]
                },
                {
                    "name": "BFS",
                    "overview": "Breadth-First Search explores all nodes at the current depth before going deeper -- guarantees shortest path in unweighted graphs.",
                    "concepts": [
                        {"term": "Completeness", "definition": "BFS always finds a solution if one exists."},
                        {"term": "Optimality", "definition": "BFS finds the shallowest solution -- optimal for unit costs."},
                        {"term": "Complexity", "definition": "Both time and space O(b^d) where b=branching factor, d=solution depth."}
                    ],
                    "explanation": "BFS uses a queue (FIFO). It is complete and optimal for unweighted problems but impractical for deep state spaces due to memory usage.",
                    "examples": [
                        {"title": "Social Network", "body": "Find all people within 2 connections from Alice. BFS from Alice explores Level 1 (direct friends), then Level 2 (friends of friends)."}
                    ],
                    "key_points": [
                        "Queue-based (FIFO)",
                        "Complete and optimal for unweighted graphs",
                        "DFS uses stack (LIFO), memory efficient but not optimal"
                    ],
                    "common_mistakes": [
                        "Confusing BFS (queue) with DFS (stack)",
                        "Applying BFS to weighted graphs -- use Dijkstra instead"
                    ]
                }
            ]
        },
        {
            "module_number": 4,
            "title": "Fuzzy Set Theory, Fuzzy Rules, Reasoning and Inference",
            "description": "Fuzzy sets, membership functions, fuzzification, defuzzification, and fuzzy inference systems.",
            "topics": [
                {
                    "name": "Fuzzy sets",
                    "overview": "A fuzzy set is a collection of elements with degrees of membership between 0 and 1, allowing partial belonging.",
                    "concepts": [
                        {"term": "Membership Function", "definition": "Function mu_A(x) giving the degree of membership of x in fuzzy set A, ranging from 0 to 1."},
                        {"term": "Fuzzification", "definition": "Converting crisp input values into fuzzy membership degrees."},
                        {"term": "Defuzzification", "definition": "Converting fuzzy output back to a crisp value (e.g., centroid method)."},
                        {"term": "Fuzzy Inference", "definition": "Applying fuzzy IF-THEN rules to map fuzzy inputs to fuzzy outputs."}
                    ],
                    "explanation": "In classical sets, an element either belongs (1) or does not (0). Fuzzy sets allow gradual membership. Temperature 28C might have membership 0.6 in WARM and 0.2 in HOT. Mamdani and Takagi-Sugeno are common fuzzy inference architectures.",
                    "examples": [
                        {"title": "AC Controller", "body": "Rule: IF temperature is HOT AND humidity is HIGH THEN fan speed is VERY HIGH. Temperature 35C has mu_HOT=0.8. Humidity 80% has mu_HIGH=0.9. Fan speed output is defuzzified to 85%."}
                    ],
                    "key_points": [
                        "Classical set: crisp 0 or 1. Fuzzy set: continuous [0,1]",
                        "Fuzzy union: max(mu_A, mu_B). Fuzzy intersection: min(mu_A, mu_B)",
                        "Centroid defuzzification: weighted average of output fuzzy set"
                    ],
                    "common_mistakes": [
                        "Confusing fuzzy membership with probability -- probabilities sum to 1, memberships do not"
                    ]
                }
            ]
        },
        {
            "module_number": 5,
            "title": "Neural Networks",
            "description": "Biological inspiration, perceptrons, backpropagation, and modern neural architectures.",
            "topics": [
                {
                    "name": "Backpropagation",
                    "overview": "Backpropagation computes gradients of the loss function with respect to all weights using the chain rule, enabling efficient weight updates.",
                    "concepts": [
                        {"term": "Chain Rule", "definition": "dL/dw = (dL/da)(da/dz)(dz/dw) -- propagates error gradient backwards through layers."},
                        {"term": "Gradient Descent", "definition": "w = w - alpha * dL/dw -- update weights in direction of steepest descent."},
                        {"term": "Learning Rate", "definition": "Controls step size; too high: diverges; too low: slow convergence."}
                    ],
                    "explanation": "Forward pass: compute predictions. Backward pass: compute gradients from output to input. Vanishing gradient: gradients shrink in deep sigmoid networks -- solved by ReLU and residual connections.",
                    "examples": [
                        {"title": "Two-layer Network", "body": "Input -> Hidden(ReLU) -> Output(Sigmoid). Forward: compute activations. Loss = BCE. Backward: compute dL/dW2 first, then dL/dW1 via chain rule."}
                    ],
                    "key_points": [
                        "Backprop = efficient application of chain rule",
                        "Must store forward-pass activations for backward computation",
                        "Vanishing gradient: use ReLU, batch norm, residual connections"
                    ],
                    "common_mistakes": [
                        "Forgetting to initialise weights properly (all-zero = no learning)",
                        "Using a learning rate that is too large (loss explodes)"
                    ]
                },
                {
                    "name": "Perceptron",
                    "overview": "The perceptron is the simplest neural unit -- a linear classifier that learns by adjusting weights based on misclassifications.",
                    "concepts": [
                        {"term": "Perceptron Learning Rule", "definition": "Delta_w = alpha * (y - y_hat) * x -- update weights when prediction is wrong."},
                        {"term": "Linear Separability", "definition": "Perceptron converges only if data is linearly separable."},
                        {"term": "Activation Function", "definition": "Step function: output 1 if weighted sum >= threshold, else 0."}
                    ],
                    "explanation": "A single perceptron can solve AND and OR but not XOR (not linearly separable). Adding hidden layers (MLP) solves non-linear problems.",
                    "examples": [
                        {"title": "AND Gate", "body": "Perceptron with weights [0.6, 0.6] and threshold 0.9 correctly classifies all AND gate inputs."}
                    ],
                    "key_points": [
                        "Single-layer: can only classify linearly separable data",
                        "MLP: can approximate any continuous function (Universal Approximation Theorem)"
                    ],
                    "common_mistakes": [
                        "Expecting perceptron to learn XOR -- it cannot without hidden layers"
                    ]
                }
            ]
        }
    ]
}

# ---------------------------------------------------------------------------
# Subject 3: Agile Software Development and DevOps
# ---------------------------------------------------------------------------
_DEVOPS = {
    "subject": "Agile Software Development and DevOps",
    "subject_code": "2015113",
    "description": "Covers Agile project management, Git, CI/CD with Jenkins, Docker, Kubernetes, Ansible, Terraform, and DevOps principles.",
    "modules": [
        {
            "module_number": 1,
            "title": "Agile Project Management and DevOps Integration",
            "description": "Scrum framework, Jira, sprints, user stories, and agile lifecycle.",
            "topics": [
                {
                    "name": "Scrum",
                    "overview": "Scrum is an Agile framework for iterative incremental development using time-boxed Sprints and defined roles.",
                    "concepts": [
                        {"term": "Sprint", "definition": "A fixed-length iteration (1-4 weeks) producing a potentially shippable increment."},
                        {"term": "Product Backlog", "definition": "Ordered list of all features and work items for the product."},
                        {"term": "Sprint Backlog", "definition": "Subset of product backlog items selected for the current sprint."},
                        {"term": "Scrum Master", "definition": "Facilitates the process, removes impediments, protects team from interruptions."},
                        {"term": "Product Owner", "definition": "Defines and prioritises backlog; represents stakeholder interests."}
                    ],
                    "explanation": "Scrum ceremonies: Sprint Planning (what to build), Daily Standup (progress + blockers), Sprint Review (demo to stakeholders), Sprint Retrospective (improve process). Velocity: average story points per sprint used for forecasting.",
                    "examples": [
                        {"title": "Sprint Planning", "body": "Team capacity = 40 story points. Product Owner presents top backlog items. Team selects 38 points for sprint goal. Daily standups track progress. Review demos completed features."}
                    ],
                    "key_points": [
                        "Scrum roles: Product Owner, Scrum Master, Development Team",
                        "Kanban vs Scrum: Kanban has no fixed sprints, uses WIP limits",
                        "Burndown chart: tracks remaining work vs time",
                        "Velocity chart: story points completed per sprint"
                    ],
                    "common_mistakes": [
                        "Treating Daily Standup as a status report to manager",
                        "Changing Sprint scope mid-sprint without re-planning"
                    ]
                },
                {
                    "name": "Agile fundamentals",
                    "overview": "Agile is a mindset for iterative, collaborative software development guided by the Agile Manifesto.",
                    "concepts": [
                        {"term": "Agile Manifesto", "definition": "12 principles emphasizing individuals, working software, customer collaboration, and responding to change."},
                        {"term": "User Story", "definition": "As a [user], I want [feature] so that [benefit] -- describes functionality from user perspective."},
                        {"term": "Epic", "definition": "A large user story that spans multiple sprints and is broken into smaller stories."},
                        {"term": "Sprint Review", "definition": "End-of-sprint demo to stakeholders for feedback."}
                    ],
                    "explanation": "Agile values: Individuals over processes, working software over documentation, customer collaboration over contracts, responding to change over following a plan. Agile does not mean no documentation -- just prioritise what matters.",
                    "examples": [
                        {"title": "User Story", "body": "As a student, I want to filter questions by difficulty so that I can focus on hard questions before exams."}
                    ],
                    "key_points": [
                        "Agile Manifesto: 4 values + 12 principles",
                        "Scrum and Kanban are Agile frameworks",
                        "Story Points: relative effort estimation (Fibonacci: 1,2,3,5,8,13...)"
                    ],
                    "common_mistakes": [
                        "Thinking Agile means no planning -- Agile plans continuously at different granularities"
                    ]
                }
            ]
        },
        {
            "module_number": 2,
            "title": "Version Control and Collaboration using Git",
            "description": "Git fundamentals, branching strategies, GitHub collaboration, and CI integration.",
            "topics": [
                {
                    "name": "Git",
                    "overview": "Git is a distributed version control system that tracks changes, enables collaboration, and maintains complete project history.",
                    "concepts": [
                        {"term": "Repository", "definition": "Project folder tracked by Git, containing all history."},
                        {"term": "Commit", "definition": "Snapshot of staged changes with a message."},
                        {"term": "Branch", "definition": "Pointer to a commit; allows parallel development without interference."},
                        {"term": "Merge", "definition": "Integrates changes from one branch into another."},
                        {"term": "Pull Request (PR)", "definition": "Request to merge a feature branch into main -- enables code review."}
                    ],
                    "explanation": "Git Flow: main -> release -> develop -> feature branches. Feature branches are created from develop, merged back via PR. Merge conflicts occur when two branches modify the same lines -- resolved manually.",
                    "examples": [
                        {"title": "Feature Branch Workflow", "body": "git checkout -b feature/login -> make changes -> git add . -> git commit -m Add login page -> git push -> open PR -> code review -> merge to develop."}
                    ],
                    "key_points": [
                        "git clone: copy remote repo locally",
                        "git pull = git fetch + git merge",
                        "git rebase: reapply commits on a new base (cleaner history)",
                        "GitHub Actions: CI/CD triggered by push/PR events"
                    ],
                    "common_mistakes": [
                        "Committing directly to main branch (bypass code review)",
                        "Writing vague commit messages -- use imperative, specific descriptions"
                    ]
                }
            ]
        },
        {
            "module_number": 3,
            "title": "CI/CD Automation using Jenkins and Containerization using Docker",
            "description": "Continuous integration/delivery pipelines with Jenkins and Docker containerization.",
            "topics": [
                {
                    "name": "Docker",
                    "overview": "Docker packages applications and dependencies into portable containers that run consistently across any environment.",
                    "concepts": [
                        {"term": "Image", "definition": "Read-only blueprint for a container (built from Dockerfile)."},
                        {"term": "Container", "definition": "Running instance of an image -- isolated process with its own filesystem."},
                        {"term": "Dockerfile", "definition": "Script of instructions to build a Docker image."},
                        {"term": "Docker Compose", "definition": "Tool for defining and running multi-container applications with a YAML file."},
                        {"term": "Docker Hub", "definition": "Public registry for storing and distributing Docker images."}
                    ],
                    "explanation": "Containers share the host OS kernel but are isolated via namespaces and cgroups -- lighter than VMs. Docker solves the works on my machine problem. Data must be persisted in volumes since containers are ephemeral.",
                    "examples": [
                        {"title": "Simple Dockerfile", "body": "FROM python:3.11-slim | WORKDIR /app | COPY requirements.txt . | RUN pip install -r requirements.txt | COPY . . | CMD python app.py"}
                    ],
                    "key_points": [
                        "Container != VM: containers share OS kernel, VMs have separate OS",
                        "docker ps: list running containers",
                        "Volumes: persist data beyond container lifecycle",
                        "Docker Compose: orchestrates multi-service apps locally"
                    ],
                    "common_mistakes": [
                        "Storing secrets in Dockerfiles (use environment variables)",
                        "Not using .dockerignore -- sending large unnecessary build context"
                    ]
                },
                {
                    "name": "CI/CD",
                    "overview": "Continuous Integration automatically builds and tests code on every commit; Continuous Delivery automates deployment to staging/production.",
                    "concepts": [
                        {"term": "Continuous Integration", "definition": "Automatically build, test, and validate every code change."},
                        {"term": "Continuous Delivery", "definition": "Automated release to staging; production deployment is manual."},
                        {"term": "Continuous Deployment", "definition": "Fully automated deployment to production on every passing build."},
                        {"term": "Pipeline as Code", "definition": "CI/CD pipeline defined in a file (Jenkinsfile) versioned with code."}
                    ],
                    "explanation": "CI/CD reduces integration problems and shortens feedback cycles. A typical Jenkins pipeline: Checkout -> Build -> Unit Tests -> Static Analysis -> Docker Build -> Push -> Deploy -> Integration Tests.",
                    "examples": [
                        {"title": "Jenkinsfile Stages", "body": "pipeline { stages { stage(Build) { sh docker build } stage(Test) { sh pytest tests/ } stage(Deploy) { sh docker-compose up -d } } }"}
                    ],
                    "key_points": [
                        "CI: detect integration bugs early",
                        "CD: ensure code is always deployable",
                        "Webhook: GitHub triggers Jenkins on push events"
                    ],
                    "common_mistakes": [
                        "Long-running tests slowing CI feedback -- parallelize tests"
                    ]
                }
            ]
        },
        {
            "module_number": 4,
            "title": "Configuration Automation, Orchestration and Cloud Provisioning",
            "description": "Ansible playbooks, Kubernetes orchestration, Terraform infrastructure as code.",
            "topics": [
                {
                    "name": "Kubernetes",
                    "overview": "Kubernetes (K8s) is an open-source container orchestration platform that automates deployment, scaling, and management of containerized applications.",
                    "concepts": [
                        {"term": "Pod", "definition": "Smallest deployable unit in K8s -- one or more containers sharing network and storage."},
                        {"term": "Deployment", "definition": "Declarative specification for desired state; K8s maintains the specified number of replicas."},
                        {"term": "Service", "definition": "Stable network endpoint to access Pods (ClusterIP, NodePort, LoadBalancer)."},
                        {"term": "Ingress", "definition": "HTTP/HTTPS routing rules to expose services externally."},
                        {"term": "kubectl", "definition": "CLI tool to interact with Kubernetes cluster."}
                    ],
                    "explanation": "K8s provides self-healing (restarts failed Pods), horizontal scaling, rolling updates, and service discovery. The control plane (API server, scheduler, etcd) manages the cluster; worker nodes run the actual Pods.",
                    "examples": [
                        {"title": "Scale Deployment", "body": "kubectl scale deployment myapp --replicas=5. K8s creates 5 Pod replicas, distributes across nodes, and maintains that count even if Pods crash."}
                    ],
                    "key_points": [
                        "K8s manages containers at scale -- Docker Compose is for local dev",
                        "ReplicaSet ensures specified number of Pod replicas always run",
                        "ConfigMap: store non-secret configuration. Secret: store sensitive data",
                        "Helm: package manager for K8s applications (Helm Charts)"
                    ],
                    "common_mistakes": [
                        "Storing secrets in ConfigMaps -- use Kubernetes Secrets",
                        "Not setting resource limits on Pods -- one Pod can starve others"
                    ]
                },
                {
                    "name": "Ansible",
                    "overview": "Ansible is an agentless automation tool for configuration management, application deployment, and task orchestration.",
                    "concepts": [
                        {"term": "Playbook", "definition": "YAML file defining automation tasks to run on managed hosts."},
                        {"term": "Inventory", "definition": "File listing managed hosts and their groupings."},
                        {"term": "Task", "definition": "A single automation action (install package, copy file, restart service)."},
                        {"term": "Role", "definition": "Reusable collection of tasks, handlers, and templates organized by function."},
                        {"term": "Idempotent", "definition": "Running a playbook multiple times produces the same result as running it once."}
                    ],
                    "explanation": "Ansible connects via SSH (agentless -- no software needed on managed nodes). Playbooks describe desired state using YAML. Idempotency ensures safe re-runs without unintended side effects.",
                    "examples": [
                        {"title": "Simple Playbook", "body": "- hosts: webservers | tasks: | - name: Install nginx | apt: name=nginx state=present | - name: Start nginx | service: name=nginx state=started"}
                    ],
                    "key_points": [
                        "Agentless: connects via SSH or WinRM",
                        "YAML-based: human-readable playbooks",
                        "Idempotent by design"
                    ],
                    "common_mistakes": [
                        "Not testing playbooks with --check (dry run) before applying to production"
                    ]
                }
            ]
        },
        {
            "module_number": 6,
            "title": "DevOps",
            "description": "DevOps principles, practices, culture, and lifecycle.",
            "topics": [
                {
                    "name": "DevOps introduction",
                    "overview": "DevOps is a culture and set of practices that unifies software development (Dev) and IT operations (Ops) to shorten the development lifecycle.",
                    "concepts": [
                        {"term": "7 Cs of DevOps", "definition": "Continuous Planning, Development, Integration, Deployment, Testing, Monitoring, and Feedback."},
                        {"term": "CALMS", "definition": "Culture, Automation, Lean, Measurement, Sharing -- core DevOps principles."},
                        {"term": "Shift Left", "definition": "Moving testing and security earlier in the development process."},
                        {"term": "Mean Time to Recovery (MTTR)", "definition": "Key DevOps metric: how quickly the team recovers from failures."}
                    ],
                    "explanation": "DevOps breaks silos between Dev and Ops teams. Key metrics: Deployment Frequency, Lead Time for Changes, Change Failure Rate, MTTR. Platform Engineering extends DevOps by building internal developer platforms.",
                    "examples": [
                        {"title": "DevOps vs Traditional", "body": "Traditional: 6-month release cycles, separate Dev and Ops teams, manual deployments. DevOps: multiple deployments per day, cross-functional teams, automated pipelines."}
                    ],
                    "key_points": [
                        "DevOps = Culture + Practices + Tools",
                        "Not just automation -- requires cultural change",
                        "Four key DORA metrics: Deployment Frequency, Lead Time, MTTR, Change Failure Rate"
                    ],
                    "common_mistakes": [
                        "Thinking DevOps is just about tools -- culture and collaboration are equally important"
                    ]
                }
            ]
        }
    ]
}


# ---------------------------------------------------------------------------
# Subject 4: Web and Mobile Application Development
# ---------------------------------------------------------------------------
_WEB = {
    "subject": "Web and Mobile Application Development",
    "subject_code": "2015114",
    "description": "Covers REST APIs, React, Kotlin, Flutter, and modern app deployment.",
    "modules": [
        {
            "module_number": 1,
            "title": "Core Web and Mobile Development Concepts",
            "description": "REST APIs, MVC, and full-stack patterns.",
            "topics": [
                {
                    "name": "REST APIs",
                    "overview": "REST is an architectural style for web services using standard HTTP methods.",
                    "concepts": [
                        {"term": "Resource", "definition": "Entity identified by a URI (e.g., /users/42)."},
                        {"term": "HTTP Methods", "definition": "GET (read), POST (create), PUT/PATCH (update), DELETE (remove)."},
                        {"term": "Stateless", "definition": "Each request is independent; no session state on server."},
                        {"term": "Status Codes", "definition": "200 OK, 201 Created, 400 Bad Request, 404 Not Found, 500 Server Error."}
                    ],
                    "explanation": "REST constraints: Client-Server, Stateless, Cacheable, Uniform Interface. GET /api/users/42 returns user 42. POST /api/users creates a user.",
                    "examples": [
                        {"title": "REST vs SOAP", "body": "REST: GET /users/1 returns JSON. SOAP: POST XML envelope. REST is simpler and dominant in modern apps."}
                    ],
                    "key_points": [
                        "REST is an architectural style, not a protocol",
                        "GET, PUT, DELETE are idempotent; POST is not",
                        "Always version APIs: /api/v1/"
                    ],
                    "common_mistakes": [
                        "Using GET for actions that modify data",
                        "Not versioning APIs"
                    ]
                },
                {
                    "name": "MVC",
                    "overview": "Model-View-Controller separates data, UI, and business logic for maintainability.",
                    "concepts": [
                        {"term": "Model", "definition": "Manages data and business logic."},
                        {"term": "View", "definition": "Renders the UI."},
                        {"term": "Controller", "definition": "Handles input, updates model, selects view."}
                    ],
                    "explanation": "MVC separates concerns. MVVM used in React/Vue. MERN: MongoDB + Express + React + Node.",
                    "examples": [{"title": "Django", "body": "Request -> URL router -> View queries Model -> renders Template."}],
                    "key_points": ["Separation of concerns", "Keep business logic in Models not Views"],
                    "common_mistakes": ["Fat views - business logic belongs in models/services"]
                }
            ]
        },
        {
            "module_number": 2,
            "title": "Front-End Development with React",
            "description": "React fundamentals, hooks, state, and deployment.",
            "topics": [
                {
                    "name": "Hooks",
                    "overview": "React Hooks allow functional components to use state and lifecycle features.",
                    "concepts": [
                        {"term": "useState", "definition": "Local state: const [count, setCount] = useState(0)."},
                        {"term": "useEffect", "definition": "Side effects after render; replaces lifecycle methods."},
                        {"term": "useContext", "definition": "Consumes React Context without prop drilling."},
                        {"term": "useRef", "definition": "Mutable value that does not trigger re-render."}
                    ],
                    "explanation": "Hooks introduced React 16.8. Only call at top level, only in React functions. Custom hooks encapsulate reusable stateful logic.",
                    "examples": [{"title": "Fetch", "body": "useEffect(() => { fetch(url).then(r=>r.json()).then(setData); }, []);"}],
                    "key_points": [
                        "useEffect [] = run once on mount",
                        "useEffect [dep] = run on dep change",
                        "Never call hooks conditionally"
                    ],
                    "common_mistakes": ["Missing dependency array causes infinite re-render"]
                },
                {
                    "name": "Components",
                    "overview": "React components are reusable self-contained UI pieces that accept props and return JSX.",
                    "concepts": [
                        {"term": "Props", "definition": "Read-only data from parent to child."},
                        {"term": "State", "definition": "Mutable data; changes trigger re-render."},
                        {"term": "JSX", "definition": "HTML-like syntax in JavaScript."},
                        {"term": "Virtual DOM", "definition": "In-memory DOM; React diffs and updates only changed parts."}
                    ],
                    "explanation": "Functional components with hooks preferred. Props flow down, events bubble up. Lift shared state to nearest ancestor.",
                    "examples": [{"title": "Button", "body": "function Button({label, onClick}) { return <button onClick={onClick}>{label}</button>; }"}],
                    "key_points": ["key prop required for lists", "Single responsibility per component"],
                    "common_mistakes": ["Forgetting key in lists", "Mutating state directly"]
                }
            ]
        },
        {
            "module_number": 5,
            "title": "Flutter and Dart",
            "description": "Flutter framework and Dart language.",
            "topics": [
                {
                    "name": "Flutter",
                    "overview": "Flutter builds natively compiled apps for mobile, web, and desktop from a single Dart codebase.",
                    "concepts": [
                        {"term": "Widget", "definition": "Everything in Flutter is a widget."},
                        {"term": "StatelessWidget", "definition": "Immutable state; rebuilt when parent changes."},
                        {"term": "StatefulWidget", "definition": "Mutable State; setState() triggers rebuild."},
                        {"term": "Widget Tree", "definition": "Hierarchical composition describing the UI."}
                    ],
                    "explanation": "Flutter renders via Skia engine - pixel-perfect across platforms. Hot reload updates UI without losing state.",
                    "examples": [{"title": "Counter", "body": "setState(() { _counter++; }); - rebuilds widget with new count."}],
                    "key_points": ["Single codebase: iOS, Android, Web, Desktop", "Hot reload in development"],
                    "common_mistakes": ["setState on large trees - use granular state managers"]
                }
            ]
        }
    ]
}

# ---------------------------------------------------------------------------
# Subject 5: User Experience Design with VR
# ---------------------------------------------------------------------------
_UX = {
    "subject": "User Experience Design with VR",
    "subject_code": "2015115",
    "description": "UX principles, design lifecycle, prototyping, evaluation, and VR interaction design.",
    "modules": [
        {
            "module_number": 1,
            "title": "Introduction",
            "description": "Interface design fundamentals and Norman design principles.",
            "topics": [
                {
                    "name": "Norman's design principles",
                    "overview": "Don Norman six principles guide creation of intuitive interfaces.",
                    "concepts": [
                        {"term": "Affordance", "definition": "Property signalling how object should be used."},
                        {"term": "Signifier", "definition": "Signal communicating appropriate action."},
                        {"term": "Feedback", "definition": "System response confirming action taken."},
                        {"term": "Mapping", "definition": "Natural relationship between controls and effects."},
                        {"term": "Conceptual Model", "definition": "User mental model - design should match it."},
                        {"term": "Constraints", "definition": "Limitations preventing errors."}
                    ],
                    "explanation": "From The Design of Everyday Things. Gulf of Evaluation: gap between system state and user perception. Gulf of Execution: gap between intent and available actions.",
                    "examples": [{"title": "Stove Mapping", "body": "Bad: square burners with row controls. Good: controls positioned matching burner layout."}],
                    "key_points": ["6 principles: Affordance, Signifier, Feedback, Conceptual Model, Mapping, Constraints"],
                    "common_mistakes": ["Confusing affordance with signifier"]
                }
            ]
        },
        {
            "module_number": 3,
            "title": "UX Design Process",
            "description": "Design thinking, prototyping, and iterative design.",
            "topics": [
                {
                    "name": "Prototyping",
                    "overview": "Prototyping creates models to test concepts with users before implementation.",
                    "concepts": [
                        {"term": "Low-Fi Prototype", "definition": "Paper sketch; fast and cheap."},
                        {"term": "High-Fi Prototype", "definition": "Interactive digital mockup (Figma)."},
                        {"term": "Wireframe", "definition": "Structure layout without visual design."},
                        {"term": "Usability Testing", "definition": "Observing real users to identify pain points."}
                    ],
                    "explanation": "5-user rule: 5 participants reveal ~85% of major problems. Fail fast with low-fi before committing to high-fi.",
                    "examples": [{"title": "Paper Prototype", "body": "Sketch screens on paper. Users tap paper. Reveals navigation issues without coding."}],
                    "key_points": ["Low-fi: validate concept", "High-fi: validate interaction", "Design Thinking: Empathize, Define, Ideate, Prototype, Test"],
                    "common_mistakes": ["Jumping to high-fi too early"]
                }
            ]
        },
        {
            "module_number": 5,
            "title": "Introduction to VR",
            "description": "VR fundamentals, hardware, and interaction design.",
            "topics": [
                {
                    "name": "Virtual Reality",
                    "overview": "VR creates immersive simulated environments via HMDs and motion controllers.",
                    "concepts": [
                        {"term": "Three I of VR", "definition": "Immersion, Interaction, Imagination."},
                        {"term": "HMD", "definition": "Head-Mounted Display with stereoscopic visuals."},
                        {"term": "Presence", "definition": "Subjective feeling of being there."},
                        {"term": "Latency", "definition": "Must be under 20ms to avoid motion sickness."}
                    ],
                    "explanation": "VR needs 90+ FPS and 6DoF tracking. Motion sickness from visual-vestibular mismatch.",
                    "examples": [{"title": "Meta Quest 3", "body": "HMD + touch controllers + inside-out tracking. Used for training, medical, architecture."}],
                    "key_points": ["5 VR Components: HMD, Input, Tracking, GPU, Software", "6DoF: 3 rotational + 3 translational", "AR overlays on real; VR replaces real"],
                    "common_mistakes": ["Confusing AR with VR"]
                }
            ]
        }
    ]
}

# ---------------------------------------------------------------------------
# Subject 6: Computer Network
# ---------------------------------------------------------------------------
_CN = {
    "subject": "Computer Network",
    "subject_code": "2015116",
    "description": "Networking models, protocols, IP addressing, routing, transport layer, and SDN.",
    "modules": [
        {
            "module_number": 1,
            "title": "Introduction to Computer Networks",
            "description": "Network types, OSI/TCP-IP models, and hardware.",
            "topics": [
                {
                    "name": "OSI model",
                    "overview": "The 7-layer OSI model standardises how different network systems communicate.",
                    "concepts": [
                        {"term": "Physical (L1)", "definition": "Raw bit transmission."},
                        {"term": "Data Link (L2)", "definition": "Frame transfer; MAC addresses."},
                        {"term": "Network (L3)", "definition": "IP addressing and routing."},
                        {"term": "Transport (L4)", "definition": "End-to-end delivery; TCP/UDP."},
                        {"term": "Application (L7)", "definition": "HTTP, FTP, DNS, SMTP."}
                    ],
                    "explanation": "Each layer serves the layer above. TCP/IP = 4 layers. Router=L3, Switch=L2, Hub=L1.",
                    "examples": [{"title": "HTTP Journey", "body": "HTTP(L7)->TCP(L4)->IP(L3)->Ethernet(L2)->bits(L1). Reversed at server."}],
                    "key_points": ["Mnemonic: All People Seem To Need Data Processing", "PDUs: bit, frame, packet, segment"],
                    "common_mistakes": ["Thinking TCP/IP has 7 layers (it has 4)"]
                }
            ]
        },
        {
            "module_number": 3,
            "title": "Network Layer",
            "description": "IP addressing, subnetting, routing protocols.",
            "topics": [
                {
                    "name": "Subnetting",
                    "overview": "Subnetting divides a large network into smaller subnetworks.",
                    "concepts": [
                        {"term": "Subnet Mask", "definition": "Identifies network portion (255.255.255.0 = /24)."},
                        {"term": "CIDR", "definition": "192.168.1.0/24 = 24 network bits, 8 host bits."},
                        {"term": "Network Address", "definition": "First address; not assignable."},
                        {"term": "Broadcast", "definition": "Last address; sends to all hosts."},
                        {"term": "Usable Hosts", "definition": "2^(host bits) - 2"}
                    ],
                    "explanation": "/26 = 6 host bits. Hosts = 62. Mask = 255.255.255.192. Block = 64.",
                    "examples": [{"title": "/27 Calculation", "body": "10.0.0.0/27: 5 host bits. Hosts=30. Mask=255.255.255.224. Block=32."}],
                    "key_points": ["/8=Class A, /16=Class B, /24=Class C", "Usable=2^h-2"],
                    "common_mistakes": ["Forgetting to subtract 2 from host count"]
                },
                {
                    "name": "TCP",
                    "overview": "TCP provides reliable ordered delivery between applications over IP.",
                    "concepts": [
                        {"term": "3-Way Handshake", "definition": "SYN->SYN-ACK->ACK establishes connection."},
                        {"term": "Flow Control", "definition": "Sliding window prevents overwhelming receiver."},
                        {"term": "Congestion Control", "definition": "Slow start avoids network congestion."}
                    ],
                    "explanation": "TCP: 3-way handshake then data transfer then 4-way FIN. UDP: connectionless, faster, unreliable.",
                    "examples": [{"title": "TCP vs UDP", "body": "TCP for file downloads. UDP for video calls (latency matters more than drops)."}],
                    "key_points": ["TCP: reliable, ordered", "UDP: low overhead, connectionless"],
                    "common_mistakes": ["UDP is not always worse - it excels for real-time apps"]
                }
            ]
        },
        {
            "module_number": 6,
            "title": "Emerging and Advanced Topics",
            "description": "SDN, NFV, and data center networking.",
            "topics": [
                {
                    "name": "SDN",
                    "overview": "SDN separates control plane from data plane for centralised programmable management.",
                    "concepts": [
                        {"term": "Control Plane", "definition": "Routing decisions."},
                        {"term": "Data Plane", "definition": "Packet forwarding."},
                        {"term": "SDN Controller", "definition": "Centralised management software."},
                        {"term": "OpenFlow", "definition": "Southbound API between controller and devices."}
                    ],
                    "explanation": "Traditional: distributed intelligence per device. SDN: centralised controller; switches become simple forwarders.",
                    "examples": [{"title": "Traffic Engineering", "body": "Controller detects congestion and reprograms switches in real time."}],
                    "key_points": ["Decouples control from data plane", "OpenFlow = southbound API"],
                    "common_mistakes": ["SDN (concept) vs OpenFlow (protocol)"]
                }
            ]
        }
    ]
}

# ---------------------------------------------------------------------------
# Subject 7: Indian Knowledge System
# ---------------------------------------------------------------------------
_IKS = {
    "subject": "Indian Knowledge System",
    "subject_code": "2015511",
    "description": "Ancient Indian contributions in acoustics, mathematics, logic, linguistics, and modern computational relevance.",
    "modules": [
        {
            "module_number": 1,
            "title": "Acoustic Science in Vedic Chanting and Indian Music",
            "description": "Nada, Shruti, frequency, and connections to modern acoustics.",
            "topics": [
                {
                    "name": "Nada",
                    "overview": "Nada is the foundational concept of sound/vibration in Indian music theory.",
                    "concepts": [
                        {"term": "Nada", "definition": "Sound/vibration in Sanskrit."},
                        {"term": "Shruti", "definition": "22 microtones per octave - finer than Western 12."},
                        {"term": "Raga", "definition": "Melodic framework specifying notes and ornamentation."},
                        {"term": "Frequency", "definition": "Vibrations per second (Hz)."}
                    ],
                    "explanation": "Indian music uses 22 shrutis vs Western 12 semitones. Vedic chanting preserves exact pitch and duration for millennia.",
                    "examples": [{"title": "Shruti vs Western", "body": "Western: 12 semitones. Indian: 22 shrutis. Sa=C fixed; others vary by raga."}],
                    "key_points": ["22 Shrutis: finer microtonal system than Western"],
                    "common_mistakes": ["Equating ragas with Western scales"]
                }
            ]
        },
        {
            "module_number": 3,
            "title": "Linguistics, Number Systems and Rainfall Prediction",
            "description": "Panini grammar, Sanskrit NLP, Indian number systems.",
            "topics": [
                {
                    "name": "Indian number system",
                    "overview": "Indian decimal place-value system with zero is the foundation of modern mathematics and computing.",
                    "concepts": [
                        {"term": "Place Value", "definition": "Digit value depends on position."},
                        {"term": "Zero (Shunya)", "definition": "Brahmagupta (628 CE) formalised zero as a number."},
                        {"term": "Decimal System", "definition": "Base-10 positional system."},
                        {"term": "Katapayadi", "definition": "Numbers encoded as Sanskrit consonants."}
                    ],
                    "explanation": "Before place value, additive systems like Roman numerals were unwieldy. Indian system with zero enabled algebra and computing. Arabs transmitted this to Europe.",
                    "examples": [{"title": "Roman vs Decimal", "body": "MCMXCIX = 1999 (complex). 1999 (clear positional). Roman multiplication is impractical."}],
                    "key_points": ["Zero: Brahmagupta 628 CE", "Binary (base-2) uses same positional principle"],
                    "common_mistakes": ["Arabic numerals were invented by Indians, transmitted by Arabs"]
                },
                {
                    "name": "Panini",
                    "overview": "Panini Ashtadhyayi is the world first formal grammar (c.400 BCE).",
                    "concepts": [
                        {"term": "Ashtadhyayi", "definition": "~4000 sutras generating all valid Sanskrit."},
                        {"term": "Sutras", "definition": "Terse grammatical rules."},
                        {"term": "Shiva Sutras", "definition": "Compact phoneme group encoding."}
                    ],
                    "explanation": "Panini grammar is recursive and formal - 2500 years before modern formal language theory. Chomsky Generative Grammar has structural parallels. Sanskrit suits NLP.",
                    "examples": [{"title": "NLP Connection", "body": "Sanskrit 8-case system maps to NLP semantic roles. Low ambiguity ideal for computational processing."}],
                    "key_points": ["Earliest scientific grammar", "BNF grammars in programming are structurally similar"],
                    "common_mistakes": ["Ancient grammars were not informal"]
                }
            ]
        },
        {
            "module_number": 4,
            "title": "Mathematics Foundations in Ancient India and Relevance to IT",
            "description": "Ancient Indian mathematicians and IT relevance.",
            "topics": [
                {
                    "name": "Aryabhata",
                    "overview": "Aryabhata (476-550 CE) pioneered mathematics and astronomy including pi, trig, and Kuttaka algorithm.",
                    "concepts": [
                        {"term": "Aryabhatiya", "definition": "Treatise on arithmetic, algebra, trigonometry."},
                        {"term": "Pi", "definition": "Computed as 3.1416 - accurate to 4 decimal places."},
                        {"term": "Kuttaka", "definition": "Algorithm for ax + by = c - precursor to Extended Euclidean."},
                        {"term": "Trigonometry", "definition": "Defined jya (sine), kotijya (cosine), versine."}
                    ],
                    "explanation": "Kuttaka solves ax+by=c, same as Extended Euclidean used in RSA for modular inverses.",
                    "examples": [{"title": "Kuttaka and RSA", "body": "Kuttaka = ancient Extended Euclidean. RSA uses Extended Euclidean for key generation today."}],
                    "key_points": ["Earth rotates on axis: 499 CE before Copernicus", "Sine table accurate to 4dp"],
                    "common_mistakes": ["Underestimating age and accuracy of ancient Indian mathematics"]
                }
            ]
        }
    ]
}

# ---------------------------------------------------------------------------
# Master Study Material List (all 7 subjects)
# ---------------------------------------------------------------------------
STUDY_MATERIAL = [_STATS, _AI, _DEVOPS, _WEB, _UX, _CN, _IKS]

# Category mapping matching syllabus
_CAT_MAP = {
    "2015111": ("CORE", "Core Course"),
    "2015112": ("CORE", "Core Course"),
    "2015113": ("CORE", "Core Course"),
    "2015114": ("ELECTIVE_1", "Program Elective-I"),
    "2015115": ("ELECTIVE_1", "Program Elective-I"),
    "2015116": ("OTHER", "Other"),
    "2015511": ("OTHER", "Other"),
}

for sub in STUDY_MATERIAL:
    code = sub.get("subject_code", "")
    if code in _CAT_MAP:
        sub["category_type"] = _CAT_MAP[code][0]
        sub["category"] = _CAT_MAP[code][1]


def get_study_material_summary():
    """Returns a high-level summary of all subjects for the Study Hub."""
    summaries = []
    for sub in STUDY_MATERIAL:
        total_modules = len(sub.get("modules", []))
        total_topics = sum(len(m.get("topics", [])) for m in sub.get("modules", []))
        summaries.append({
            "subject": sub["subject"],
            "subject_code": sub["subject_code"],
            "category": sub.get("category", "Core Course"),
            "category_type": sub.get("category_type", "CORE"),
            "description": sub.get("description", ""),
            "total_modules": total_modules,
            "total_topics": total_topics
        })
    return summaries


def get_study_material_by_code(subject_code):
    """Returns the complete study material structure formatted for reader consumption."""
    code_clean = str(subject_code).strip()
    for sub in STUDY_MATERIAL:
        if sub.get("subject_code") == code_clean:
            # Transform modules/topics if necessary to match frontend expectations
            formatted_modules = []
            for m in sub.get("modules", []):
                formatted_topics = []
                for idx, t in enumerate(m.get("topics", [])):
                    # Extract fields whether dict structure or strings
                    topic_title = t.get("name") or t.get("topic_title") or t.get("topic") or f"Topic {idx+1}"
                    summary = t.get("overview") or t.get("summary") or t.get("explanation", "")[:180] + "..."
                    
                    key_concepts = []
                    if "concepts" in t:
                        for c in t["concepts"]:
                            if isinstance(c, dict):
                                key_concepts.append(f"{c.get('term', '')}: {c.get('definition', '')}")
                            else:
                                key_concepts.append(str(c))
                    elif "key_points" in t:
                        key_concepts = t["key_points"]
                    
                    exam_tips = t.get("key_points", []) if "concepts" in t else []
                    
                    formulas = []
                    if "examples" in t:
                        for ex in t["examples"]:
                            if isinstance(ex, dict):
                                formulas.append(f"{ex.get('title', '')}: {ex.get('body', '')}")
                            else:
                                formulas.append(str(ex))
                                
                    mistakes = t.get("common_mistakes", [])

                    formatted_topics.append({
                        "topic_id": f"{m.get('module_number', 1)}-{idx+1}",
                        "topic_title": topic_title,
                        "summary": summary,
                        "key_concepts": key_concepts,
                        "exam_tips": exam_tips,
                        "formulas_and_rules": formulas,
                        "common_mistakes": mistakes
                    })

                formatted_modules.append({
                    "module_number": m.get("module_number", 1),
                    "module_name": m.get("title") or m.get("module") or f"Module {m.get('module_number', 1)}",
                    "description": m.get("description", ""),
                    "topics": formatted_topics
                })

            return {
                "subject": sub["subject"],
                "subject_code": sub["subject_code"],
                "category": sub.get("category", "Core Course"),
                "category_type": sub.get("category_type", "CORE"),
                "description": sub.get("description", ""),
                "modules": formatted_modules
            }
    return None

