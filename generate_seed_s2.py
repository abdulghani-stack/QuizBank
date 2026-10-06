"""
Module by module MCQ generator for Subjects 2, 3, 4, 5, 6, 7.
All questions strictly adhere to Mumbai University AI&DS Sem V syllabus topics, with 10 questions per module across all 6 modules for each subject.
"""

def generate_s2_questions(start_id):
    # Subject 2: Artificial Intelligence and Soft Computing (2015112)
    s_name = "Artificial Intelligence and Soft Computing"
    s_code = "2015112"
    q_id = start_id
    questions = []

    # S2 M1: Introduction to AI & Soft Computing
    m1_name = "Module I - Introduction to AI & Soft Computing"
    s2_m1 = [
        {
            "topic": "Hard Computing vs Soft Computing",
            "question": "Which of the following characteristics fundamentally distinguishes Soft Computing from traditional Hard Computing?",
            "option_a": "Soft Computing is tolerant of imprecision, uncertainty, partial truth, and approximation to achieve tractability and robustness",
            "option_b": "Soft Computing requires strictly binary, crisp, two-valued Boolean logic",
            "option_c": "Hard Computing relies on stochastic gradient optimization and fuzzy reasoning",
            "option_d": "Soft Computing guarantees mathematically exact, deterministic analytical solutions in O(1) time",
            "answer": "A",
            "explanation": "According to Lotfi Zadeh, the guiding principle of soft computing is to exploit tolerance for imprecision, uncertainty, and partial truth to achieve tractability, robustness, and low solution cost.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Soft Computing constituents",
            "question": "What are the primary synergistic constituents that comprise the foundational core of Soft Computing?",
            "option_a": "Fuzzy Logic, Neural Networks, Evolutionary Computation, and Probabilistic Reasoning",
            "option_b": "Propositional Calculus, First-Order Logic, and Graph Theory",
            "option_c": "Relational Databases, SQL Engines, and ETL Pipelines",
            "option_d": "Deterministic Finite Automata and Turing Machines",
            "answer": "A",
            "explanation": "Soft computing brings together Neural Networks (learning/adaptation), Fuzzy Logic (imprecision/reasoning), Evolutionary Algorithms (search/optimization), and Probabilistic Computing (uncertainty).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "ChatGPT-like models",
            "question": "In modern Generative AI and ChatGPT-like large language models, what architectural mechanism enables self-attention across long token contexts?",
            "option_a": "Scaled Dot-Product Attention: Attention(Q, K, V) = softmax((Q K^T) / sqrt(d_k)) V",
            "option_b": "Recurrent hidden state propagation h_t = tanh(W x_t + U h_{t-1})",
            "option_c": "Max pooling over 2D convolutional filter maps",
            "option_d": "Winner-Take-All lateral inhibition competitive layers",
            "answer": "A",
            "explanation": "The Transformer architecture uses Scaled Dot-Product Multi-Head Attention to compute attention weights between queries (Q) and keys (K) to weight values (V) across the sequence.",
            "difficulty": "medium",
            "question_type": "architecture"
        },
        {
            "topic": "Ethical challenges in AI",
            "question": "When deploying an automated AI loan decision system, the model exhibits disparate impact on a protected sub-population due to historical training labels. Which ethical AI pillar is violated?",
            "option_a": "Fairness and Non-discrimination",
            "option_b": "Data Compression Efficiency",
            "option_c": "Inference Latency Optimization",
            "option_d": "Model Quantization Integrity",
            "answer": "A",
            "explanation": "Algorithmic bias originating from historical disparities violates fairness, equity, and non-discrimination principles in responsible AI governance.",
            "difficulty": "easy",
            "question_type": "scenario"
        },
        {
            "topic": "Neuro Computing",
            "question": "How does Neuro Computing mimic biological information processing to perform pattern recognition?",
            "option_a": "Through highly interconnected parallel processing nodes (neurons) that adjust synaptic connection weights based on learning rules",
            "option_b": "Through sequential execution of symbolic IF-THEN rules stored in an expert system database",
            "option_c": "Through rigid procedural algorithms executing on von Neumann single-core processors",
            "option_d": "Through exhaustive branch-and-bound state space graph traversal",
            "answer": "A",
            "explanation": "Neuro computing utilizes distributed representations and connectionist networks where learning occurs via iterative adaptation of synaptic weights.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "AI perspectives",
            "question": "According to Russell & Norvig, AI can be organized into four perspectives. Which category does 'Designing rational agents that act to achieve the best expected outcome' belong to?",
            "option_a": "Acting Rationally",
            "option_b": "Thinking Humanly (Cognitive Modeling)",
            "option_c": "Thinking Rationally (Laws of Thought)",
            "option_d": "Acting Humanly (Turing Test approach)",
            "answer": "A",
            "explanation": "The rational agent approach centers on 'Acting Rationally'—operating autonomously, perceiving environments, and acting to maximize expected performance measures.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Adaptation",
            "question": "Why is adaptation considered a critical characteristic of soft computing systems operating in real-world dynamical environments?",
            "option_a": "It allows the system to continuously adjust internal parameters in response to non-stationary data streams and environmental drift",
            "option_b": "It converts all continuous numeric inputs into hardcoded lookup tables",
            "option_c": "It forces the execution to stop whenever an unexpected outlier is encountered",
            "option_d": "It replaces machine learning models with static deterministic heuristics",
            "answer": "A",
            "explanation": "Adaptation enables soft computing systems to dynamically update connection weights or membership functions when underlying environment statistics shift.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Generative AI",
            "question": "What is the core training objective of a Generative Adversarial Network (GAN) during the minimax game between Generator G and Discriminator D?",
            "option_a": "min_G max_D V(D, G) = E_{x~p_data}[log D(x)] + E_{z~p_z}[log(1 - D(G(z)))]",
            "option_b": "min sum ||y - G(x)||^2 across all labeled test images",
            "option_c": "max mutual information between class labels and hidden layers",
            "option_d": "min number of parameters in the discriminator network",
            "answer": "A",
            "explanation": "GANs optimize a two-player zero-sum minimax objective where D maximizes probability of correctly identifying real vs fake data while G minimizes log(1 - D(G(z))).",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Artificial Intelligence",
            "question": "In the PEAS framework for characterizing task environments in AI agent design, what does the acronym PEAS represent?",
            "option_a": "Performance measure, Environment, Actuators, Sensors",
            "option_b": "Program, Engine, Architecture, System",
            "option_c": "Probability, Evidence, Action, State",
            "option_d": "Perception, Entropy, Automation, Strategy",
            "answer": "A",
            "explanation": "PEAS stands for Performance measure, Environment, Actuators, and Sensors, defining the formal specification of an agent's task environment.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Learning",
            "question": "In machine learning paradigms, what distinguishes Reinforcement Learning from Supervised and Unsupervised Learning?",
            "option_a": "An agent learns optimal action policies through trial-and-error interactions receiving scalar reward/penalty feedback without explicit correct input-output pairs",
            "option_b": "The model is provided with pre-labeled ground truth targets for every training timestep",
            "option_c": "The algorithm strictly finds latent clusters without any feedback signals",
            "option_d": "The model requires backpropagation through a fixed, non-interactive dataset",
            "answer": "A",
            "explanation": "Reinforcement learning learns via evaluative feedback (rewards/penalties) through environment interaction to maximize cumulative return.",
            "difficulty": "medium",
            "question_type": "comparison"
        }
    ]
    for q in s2_m1:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m1_name, "module_number": 1})
        questions.append(q)
        q_id += 1

    # S2 M2: Solving Problems by Searching
    m2_name = "Module II - Solving Problems by Searching"
    s2_m2 = [
        {
            "topic": "A* Search",
            "question": "Under what condition is A* graph search mathematically guaranteed to be complete and optimal?",
            "option_a": "When the heuristic function h(n) is consistent (monotone), which implies admissibility (h(n) <= true cost h*(n))",
            "option_b": "When h(n) = 0 for all nodes",
            "option_c": "When h(n) strictly overestimates the true remaining path cost",
            "option_d": "When step costs are allowed to be negative numbers",
            "answer": "A",
            "explanation": "For graph search (where nodes may be revisited), A* is optimal if h(n) is consistent: h(n) <= c(n, a, n') + h(n'). Consistency guarantees that f(n) non-decreases along any path.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Simulated Annealing",
            "question": "In Simulated Annealing optimization, when evaluating a neighboring state with energy change Delta E = E(next) - E(current) > 0 (worse state in minimization), what is the probability P of accepting this downhill move at temperature T?",
            "option_a": "P = exp(-Delta E / T)",
            "option_b": "P = 0 (worse moves are never accepted)",
            "option_c": "P = 1.0 (all moves are accepted regardless of temperature)",
            "option_d": "P = Delta E / (T * log(T))",
            "answer": "A",
            "explanation": "Simulated Annealing escapes local optima by accepting inferior moves with Boltzmann probability P = exp(-Delta E / T). As temperature T cools towards 0, P decreases.",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "Adversarial Search",
            "question": "In minimax game tree search with Alpha-Beta pruning, what condition triggers an Alpha-Cutoff (pruning remaining child nodes) at a MIN node?",
            "option_a": "When the current node value beta <= alpha (the MAX ancestor already has a guaranteed higher alternative)",
            "option_b": "When the current node value beta >= alpha",
            "option_c": "When alpha reaches positive infinity",
            "option_d": "When the depth of the game tree exceeds 100",
            "answer": "A",
            "explanation": "Alpha is the best value MAX can guarantee; Beta is the best MIN can guarantee. At a MIN node, if beta <= alpha, MAX will never choose this branch, so remaining children are pruned.",
            "difficulty": "hard",
            "question_type": "algorithm_tracing"
        },
        {
            "topic": "Hill Climbing",
            "question": "Which pathological failure mode of standard greedy local Hill Climbing search occurs when all neighboring states have identical heuristic evaluation values?",
            "option_a": "Plateau / Shoulder",
            "option_b": "Ridge",
            "option_c": "Local Maximum",
            "option_d": "Infinite loop due to negative edge cycles",
            "answer": "A",
            "explanation": "A plateau is a flat area of the state space landscape where all neighboring states have the same value, giving hill climbing no gradient direction to climb.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "BFS",
            "question": "For a state space graph with branching factor b and shallowest goal depth d, what are the time complexity and space complexity of Breadth-First Search (BFS)?",
            "option_a": "Time Complexity: O(b^d), Space Complexity: O(b^d)",
            "option_b": "Time Complexity: O(b*d), Space Complexity: O(d)",
            "option_c": "Time Complexity: O(d^b), Space Complexity: O(b)",
            "option_d": "Time Complexity: O(b^d), Space Complexity: O(b*d)",
            "answer": "A",
            "explanation": "BFS stores all generated nodes at depth d in its FIFO frontier queue, resulting in both exponential time O(b^d) and exponential memory O(b^d).",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "DFS",
            "question": "What is the primary memory advantage of Depth-First Search (DFS) over Breadth-First Search (BFS) for a tree search with maximum depth m and branching factor b?",
            "option_a": "DFS requires only linear space O(b*m) because it stores only a single path from root to leaf and unexpanded siblings",
            "option_b": "DFS guarantees finding the shallowest optimal path in all graphs",
            "option_c": "DFS never gets trapped in infinite depth branches",
            "option_d": "DFS has O(1) constant time complexity",
            "answer": "A",
            "explanation": "DFS uses a LIFO stack storing only O(b*m) nodes, whereas BFS must store the entire level O(b^d) which exhausts memory quickly.",
            "difficulty": "easy",
            "question_type": "comparison"
        },
        {
            "topic": "Greedy Best First Search",
            "question": "How does Greedy Best-First Search prioritize node expansion, and why is it not guaranteed to be optimal?",
            "option_a": "It expands the node n with the lowest estimated cost to goal f(n) = h(n), ignoring the path cost g(n) already incurred",
            "option_b": "It evaluates f(n) = g(n) + h(n) on every step",
            "option_c": "It explores all nodes level-by-level uniformly",
            "option_d": "It alternates between MAX and MIN players",
            "answer": "A",
            "explanation": "Greedy Best-First search sets f(n) = h(n). By solely focusing on remaining distance to goal, it can be misled into long, sub-optimal paths because it neglects past cost g(n).",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "State space representation",
            "question": "In the 8-puzzle problem, what constitutes a valid State Space Representation?",
            "option_a": "The 3x3 configuration of 8 numbered tiles and 1 blank space, with valid operators representing sliding the blank Up, Down, Left, Right",
            "option_b": "A list of RGB pixel values of the puzzle board",
            "option_c": "A continuous function mapping time to acceleration",
            "option_d": "An unconstrained graph where any tile can teleport to any coordinate",
            "answer": "A",
            "explanation": "A formal state space representation requires: initial state, goal state description, actions/operators (Up/Down/Left/Right), transition model Result(s, a), and path cost function.",
            "difficulty": "easy",
            "question_type": "scenario"
        },
        {
            "topic": "Problem formulation",
            "question": "In AI problem formulation, what are the five components of a well-defined search problem?",
            "option_a": "Initial state, Actions, Transition model, Goal test, and Path cost",
            "option_b": "Heuristic table, Alpha cutoff, Beta cutoff, Minimax value, Depth limit",
            "option_c": "Input layer, Hidden layer, Output layer, Learning rate, Activation function",
            "option_d": "Fuzzifier, Rule base, Inference engine, Defuzzifier, Universe of discourse",
            "answer": "A",
            "explanation": "A search problem is formally defined by 5 components: Initial state s_0, Actions(s), Transition model Result(s,a), GoalTest(s), and Step cost c(s,a,s').",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Game Playing",
            "question": "In two-player zero-sum deterministic perfect information games (like Chess or Tic-Tac-Toe), what is the relationship between the utility of Player 1 (MAX) and Player 2 (MIN)?",
            "option_a": "Utility_MAX + Utility_MIN = 0 (a gain for MAX is an exact equivalent loss for MIN)",
            "option_b": "Both players cooperate to maximize the sum of utilities",
            "option_c": "Player 1 always receives a strictly positive reward while Player 2 receives 0",
            "option_d": "Utility values are non-deterministic continuous probability distributions",
            "answer": "A",
            "explanation": "Zero-sum games are strictly competitive: total payoffs sum to a constant (zero), meaning any advantage gained by MAX directly corresponds to an equal loss for MIN.",
            "difficulty": "easy",
            "question_type": "conceptual"
        }
    ]
    for q in s2_m2:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m2_name, "module_number": 2})
        questions.append(q)
        q_id += 1

    # S2 M3: Knowledge and Reasoning
    m3_name = "Module III - Knowledge and Reasoning"
    s2_m3 = [
        {
            "topic": "Resolution",
            "question": "In Propositional and First-Order Logic, what is the Resolution Rule of Inference applied to two clauses (A v B) and (~A v C)?",
            "option_a": "B v C (the resolvent obtained by canceling the complementary literals A and ~A)",
            "option_b": "A v B v C",
            "option_c": "~B v ~C",
            "option_d": "A ^ ~A",
            "answer": "A",
            "explanation": "The resolution rule takes two clauses containing complementary literals (A and ~A) and derives their resolvent: from (A v B) and (~A v C), we infer (B v C).",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "Forward Chaining",
            "question": "How does the Forward Chaining inference algorithm operate in a Horn clause knowledge base?",
            "option_a": "It is a data-driven strategy that starts with known facts and applies Modus Ponens repeatedly to derive new conclusions until the goal is reached",
            "option_b": "It is a goal-driven strategy that starts with the query and searches backward for supporting premises",
            "option_c": "It converts all rules into conjunctive normal form and executes resolution refutation",
            "option_d": "It randomly samples truth tables using Monte Carlo search",
            "answer": "A",
            "explanation": "Forward chaining is data-driven: it begins with atomic facts in the KB and fires rules whose premises are satisfied, adding their conclusions to the KB iteratively.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Backward Chaining",
            "question": "In what type of problem domain is Backward Chaining preferred over Forward Chaining?",
            "option_a": "Diagnostic and query-answering systems where a specific hypothesis/goal needs to be verified, avoiding derivation of irrelevant facts",
            "option_b": "Real-time monitoring systems where all possible consequences of incoming sensor data must be computed",
            "option_c": "Domains with no initial goals or queries",
            "option_d": "Environments where Horn clauses are strictly prohibited",
            "answer": "A",
            "explanation": "Backward chaining is goal-directed: it works backward from a specific query, checking sub-goals. This prevents wasting computation deriving irrelevant facts from large data.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "FOPL",
            "question": "Translate the sentence 'Every student in the AI class loves programming' into First-Order Predicate Logic (FOPL):",
            "option_a": "forall x (Student(x) ^ InAIClass(x) -> LovesProgramming(x))",
            "option_b": "exists x (Student(x) ^ InAIClass(x) ^ LovesProgramming(x))",
            "option_c": "forall x (Student(x) v InAIClass(x) v LovesProgramming(x))",
            "option_d": "forall x (Student(x) -> (InAIClass(x) ^ LovesProgramming(x)))",
            "answer": "A",
            "explanation": "Universal quantification ('Every') combined with conditional implication ensures that for any entity x, if x is a student AND in AI class, then x loves programming.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Logical connectives",
            "question": "Given propositional variables P (True) and Q (False), what is the truth value of the formula (P -> Q) <-> (~P v Q)?",
            "option_a": "True (both expressions are logically equivalent Material Implication laws, evaluating to False <-> False = True)",
            "option_b": "False",
            "option_c": "Undefined",
            "option_d": "Contradiction",
            "answer": "A",
            "explanation": "(P -> Q) is equivalent to (~P v Q). With P=T, Q=F: (T -> F) is False, and (~T v F) = (F v F) is False. Thus False <-> False evaluates to True (Tautological equivalence).",
            "difficulty": "easy",
            "question_type": "numerical"
        },
        {
            "topic": "Ontologies",
            "question": "In knowledge representation and Semantic Web reasoning, what role does an Ontology (formalized in OWL/RDF) serve?",
            "option_a": "It provides a formal, explicit specification of a shared conceptualization, defining classes, properties, relations, and axioms for automated reasoning",
            "option_b": "It stores raw binary image files in high-performance cloud storage",
            "option_c": "It compiles Python source code into machine bytecode",
            "option_d": "It replaces relational databases with flat CSV files",
            "answer": "A",
            "explanation": "An ontology formally defines categories, concepts, properties, and relationships between concepts within a domain to facilitate knowledge sharing and automated reasoning.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Uncertain knowledge",
            "question": "Why is classical First-Order Logic insufficient for modeling real-world medical diagnosis compared to probabilistic reasoning?",
            "option_a": "Medical domains involve partial observability, sensor noise, non-deterministic disease outcomes, and immense complexity that monotonic crisp logic cannot handle",
            "option_b": "Medical data contains no categorical variables",
            "option_c": "First-Order Logic cannot represent entities or relations",
            "option_d": "Medical symptoms never correlate with diseases",
            "answer": "A",
            "explanation": "Real-world domains suffer from laziness (too many rules), theoretical ignorance, and practical ignorance (unmeasured tests), necessitating probabilistic degrees of belief P(E|H).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Quantification",
            "question": "According to duality rules in First-Order Logic, what is the logical equivalence of the negated universal statement ~forall x P(x)?",
            "option_a": "exists x ~P(x)",
            "option_b": "forall x ~P(x)",
            "option_c": "~exists x P(x)",
            "option_d": "exists x P(x)",
            "answer": "A",
            "explanation": "De Morgan's laws for quantifiers state: ~forall x P(x) is equivalent to exists x ~P(x) ('Not all x satisfy P' is identical to 'There exists at least one x that does not satisfy P').",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Semantic Web reasoning",
            "question": "In Description Logics used for Semantic Web reasoning, what mechanism detects if an instance can belong to two disjoint classes simultaneously?",
            "option_a": "Consistency checking / Concept satisfiability reasoning",
            "option_b": "Gradient descent backpropagation",
            "option_c": "Max-pooling aggregation",
            "option_d": "K-means centroid recalculation",
            "answer": "A",
            "explanation": "Description logic reasoners (e.g., Pellet, HermiT) perform satisfiability and consistency checks to identify logical contradictions such as membership in disjoint classes.",
            "difficulty": "hard",
            "question_type": "application"
        },
        {
            "topic": "Knowledge Representation Systems",
            "question": "What are the four fundamental properties required of a robust Knowledge Representation System?",
            "option_a": "Representational Adequacy, Inferential Adequacy, Inferential Efficiency, and Acquisitional Efficiency",
            "option_b": "Accuracy, Precision, Recall, and F1-Score",
            "option_c": "Atomicity, Consistency, Isolation, and Durability",
            "option_d": "Bandwidth, Throughput, Latency, and Jitter",
            "answer": "A",
            "explanation": "According to Rich and Knight, KR systems require Representational Adequacy (express all domain knowledge), Inferential Adequacy (manipulate structures to derive new knowledge), Inferential Efficiency, and Acquisitional Efficiency.",
            "difficulty": "hard",
            "question_type": "conceptual"
        }
    ]
    for q in s2_m3:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m3_name, "module_number": 3})
        questions.append(q)
        q_id += 1

    # S2 M4: Fuzzy Set Theory, Fuzzy Rules, Reasoning and Inference
    m4_name = "Module IV - Fuzzy Set Theory, Fuzzy Rules, Reasoning and Inference"
    s2_m4 = [
        {
            "topic": "Fuzzy sets",
            "question": "In classical (crisp) set theory, an element x either belongs to set A (mu_A(x)=1) or does not (mu_A(x)=0). In Fuzzy Set theory, how is membership characterized?",
            "option_a": "By a continuous membership function mu_A(x) taking values in the closed interval [0, 1]",
            "option_b": "By binary Boolean values {0, 1} exclusively",
            "option_c": "By imaginary complex numbers on the unit circle",
            "option_d": "By negative integers representing set exclusion",
            "answer": "A",
            "explanation": "A fuzzy set A in universe of discourse X is characterized by a membership function mu_A: X -> [0, 1], representing the continuous grade of membership of each element.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Defuzzification",
            "question": "What is the most widely utilized defuzzification technique in fuzzy control systems that computes the balance point of the aggregated output fuzzy region?",
            "option_a": "Centroid method (Center of Gravity / Center of Area)",
            "option_b": "Mean of Maxima (MOM)",
            "option_c": "First of Maxima (FOM)",
            "option_d": "Height defuzzification",
            "answer": "A",
            "explanation": "The Centroid method z* = int(z * mu(z) dz) / int(mu(z) dz) calculates the center of gravity of the combined fuzzy area, yielding smooth continuous control outputs.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Membership functions",
            "question": "A triangular membership function is parameterized by (a, b, c) where a = 10, b = 25, c = 40. What is the membership grade mu(20)?",
            "option_a": "mu(20) = (20 - 10) / (25 - 10) = 10 / 15 = 0.67",
            "option_b": "mu(20) = (40 - 20) / (40 - 25) = 20 / 15 = 1.33",
            "option_c": "mu(20) = 0.50",
            "option_d": "mu(20) = 1.00",
            "answer": "A",
            "explanation": "For x in [a, b], mu(x) = (x - a) / (b - a). Here (20 - 10) / (25 - 10) = 10 / 15 = 2/3 approx 0.67.",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "Fuzzy IF-THEN rules",
            "question": "In a Mamdani fuzzy inference system with rule 'IF Temperature is High AND Pressure is Medium THEN Valve is Open', how is the rule firing strength (antecedent conjunction) typically computed?",
            "option_a": "By the Min (T-norm) operator: alpha = min(mu_High(Temp), mu_Medium(Pressure))",
            "option_b": "By the Max (T-conorm) operator: alpha = max(mu_High(Temp), mu_Medium(Pressure))",
            "option_c": "By arithmetic addition: alpha = mu_High(Temp) + mu_Medium(Pressure)",
            "option_d": "By taking the reciprocal difference of memberships",
            "answer": "A",
            "explanation": "Standard Mamdani fuzzy inference models fuzzy AND conjunction using the minimum T-norm operator: min(mu_A(x), mu_B(y)).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Fuzzy inference systems",
            "question": "What is the fundamental architectural difference between a Mamdani Fuzzy Inference System and a Takagi-Sugeno (TSK) Fuzzy Inference System?",
            "option_a": "Mamdani systems have fuzzy set membership functions in the consequent part; Sugeno systems have crisp mathematical functions (linear equations or constants) in the consequent",
            "option_b": "Sugeno systems do not require any input fuzzification",
            "option_c": "Mamdani systems cannot use IF-THEN rules",
            "option_d": "Sugeno systems use neural backpropagation exclusively during inference",
            "answer": "A",
            "explanation": "In Mamdani FIS, consequents are fuzzy sets requiring defuzzification. In Sugeno FIS, rule consequents are crisp functions: z = p*x + q*y + r, defuzzified via weighted average.",
            "difficulty": "medium",
            "question_type": "comparison"
        },
        {
            "topic": "Fuzzification",
            "question": "In a washing machine fuzzy controller, a sensor measures dirt level as 65 NTU. What does the Fuzzification stage do with this measurement?",
            "option_a": "It converts the crisp numerical input (65 NTU) into linguistic membership values across fuzzy sets like 'Medium Dirt' (0.3) and 'High Dirt' (0.7)",
            "option_b": "It directly actuates the electric motor speed to 65 RPM",
            "option_c": "It converts the sensor signal into a binary 0/1 decision",
            "option_d": "It deletes the sensor measurement from controller memory",
            "answer": "A",
            "explanation": "Fuzzification is the mapping from a crisp real-world input value to fuzzy degrees of membership within predefined linguistic term sets.",
            "difficulty": "easy",
            "question_type": "application"
        },
        {
            "topic": "Fuzzy relations",
            "question": "Given two fuzzy relations R on X x Y and S on Y x Z, what is the standard Max-Min composition R o S defined by?",
            "option_a": "mu_{R o S}(x, z) = max_y [ min (mu_R(x, y), mu_S(y, z)) ]",
            "option_b": "mu_{R o S}(x, z) = min_y [ max (mu_R(x, y), mu_S(y, z)) ]",
            "option_c": "mu_{R o S}(x, z) = sum_y [ mu_R(x, y) * mu_S(y, z) ]",
            "option_d": "mu_{R o S}(x, z) = max_y [ mu_R(x, y) + mu_S(y, z) ]",
            "answer": "A",
            "explanation": "The standard Max-Min composition operator combines fuzzy relations across common intermediate universe Y via mu_{R o S}(x, z) = max_{y} { min(mu_R(x,y), mu_S(y,z)) }.",
            "difficulty": "hard",
            "question_type": "numerical"
        },
        {
            "topic": "Features of membership functions",
            "question": "What is the 'Core' of a fuzzy set A, and how does it differ from the 'Support' of A?",
            "option_a": "Core(A) = {x | mu_A(x) = 1.0}; Support(A) = {x | mu_A(x) > 0.0}",
            "option_b": "Core(A) = {x | mu_A(x) > 0.0}; Support(A) = {x | mu_A(x) = 1.0}",
            "option_c": "Core(A) = {x | mu_A(x) = 0.5}; Support(A) = {x | mu_A(x) = 0.0}",
            "option_d": "Core(A) is the area outside the universe of discourse",
            "answer": "A",
            "explanation": "The core consists of all elements with complete membership (mu=1), whereas the support includes all elements with non-zero membership (mu>0).",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Fuzzy reasoning",
            "question": "Under Generalized Modus Ponens (GMP) in fuzzy reasoning, given Premise 1: 'x is A'' and Rule: 'IF x is A THEN y is B', how is the deduced conclusion B' computed?",
            "option_a": "Via compositional rule of inference: B' = A' o (A -> B)",
            "option_b": "B' is always identical to crisp set B",
            "option_c": "B' is computed by taking the algebraic difference B - A'",
            "option_d": "GMP cannot deduce any conclusion if A' is not identical to A",
            "answer": "A",
            "explanation": "Generalized Modus Ponens permits approximate inference where antecedent A' closely resembles A, deriving consequent B' through fuzzy relation composition B' = A' o R.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Fuzzy sets",
            "question": "For two fuzzy sets A and B on universe X with mu_A(x) = 0.7 and mu_B(x) = 0.4 for a specific element x, what are the membership values for (A union B), (A intersect B), and (Complement of A) under Zadeh's standard operators?",
            "option_a": "Union = 0.7, Intersection = 0.4, Complement(A) = 0.3",
            "option_b": "Union = 1.1, Intersection = 0.28, Complement(A) = 0.7",
            "option_c": "Union = 0.4, Intersection = 0.7, Complement(A) = 0.6",
            "option_d": "Union = 0.55, Intersection = 0.55, Complement(A) = 0.0",
            "answer": "A",
            "explanation": "Zadeh operators: Union = max(0.7, 0.4) = 0.7. Intersection = min(0.7, 0.4) = 0.4. Complement = 1 - 0.7 = 0.3.",
            "difficulty": "easy",
            "question_type": "numerical"
        }
    ]
    for q in s2_m4:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m4_name, "module_number": 4})
        questions.append(q)
        q_id += 1

    # S2 M5: Neural Networks
    m5_name = "Module V - Neural Networks"
    s2_m5 = [
        {
            "topic": "Linear separability",
            "question": "Why can a Single-Layer Perceptron successfully solve the logical AND and OR functions but fundamentally fail to solve the XOR (Exclusive OR) function?",
            "option_a": "AND and OR have decision boundaries that are linearly separable by a single hyperplane, whereas XOR points cannot be partitioned by any single straight line",
            "option_b": "XOR has 3 inputs instead of 2",
            "option_c": "Single-layer perceptrons can only output negative numbers",
            "option_d": "XOR requires non-differentiable activation functions",
            "answer": "A",
            "explanation": "Minsky & Papert (1969) proved that single-layer perceptrons can only represent linearly separable functions. XOR requires at least one hidden layer to form a non-linear decision boundary.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Backpropagation",
            "question": "In a Multi-Layer Perceptron (MLP) trained with backpropagation, how is the weight update Delta w_{ij} between layer l-1 and layer l computed using gradient descent?",
            "option_a": "Delta w_{ij} = -eta * (dE / dw_{ij}) = eta * delta_j * a_i, where delta_j is the local error gradient and a_i is the activation of node i",
            "option_b": "Delta w_{ij} = +eta * (w_{ij} / a_i)",
            "option_c": "Delta w_{ij} = max(w_{ij}, a_i) - min(w_{ij}, a_i)",
            "option_d": "Delta w_{ij} = eta * sum(weights) / batch_size",
            "answer": "A",
            "explanation": "Backpropagation applies the chain rule of calculus to compute the gradient of loss E with respect to weights: dE/dw_{ij} = -delta_j * a_i, updating weights in the opposite direction of the gradient.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "McCulloch-Pitts neuron",
            "question": "What is the primary operational rule of a McCulloch-Pitts (M-P) neuron with excitatory inputs x_1, x_2 and an absolute inhibitory input x_inh?",
            "option_a": "If x_inh = 1, output y is strictly 0 regardless of excitatory inputs; otherwise y = 1 if sum(x_i) >= Threshold theta, else 0",
            "option_b": "The inhibitory input increases the activation potential proportionally to theta",
            "option_c": "The output is a continuous sigmoidal value between 0 and 1",
            "option_d": "Weights are continuously updated using the Delta rule",
            "answer": "A",
            "explanation": "In the McCulloch-Pitts model (1943), inhibitory inputs have absolute veto power: if any inhibitory line fires, output is 0. Otherwise it fires if sum of excitatory inputs reaches threshold.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Hebbian learning",
            "question": "What is the neurobiological core principle of Hebbian Learning summarized by Donald Hebb (1949)?",
            "option_a": "'Neurons that fire together, wire together' — the synaptic weight w_{ij} increases proportionally to the simultaneous product of pre-synaptic and post-synaptic activity: Delta w_{ij} = eta * x_i * y_j",
            "option_b": "Synaptic weights decrease whenever both neurons fire simultaneously",
            "option_c": "Error signals are propagated backward from the output layer to hidden layers",
            "option_d": "Only one winning neuron is updated while all others are set to zero",
            "answer": "A",
            "explanation": "Hebb's postulate states that when an axon of cell A excites cell B repeatedly, metabolic changes increase A's efficiency: Delta w_{ij} = eta * x_i * y_j.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Self-Organizing Maps",
            "question": "In Kohonen Self-Organizing Maps (SOM), what competitive learning mechanism produces topology-preserving low-dimensional spatial mappings?",
            "option_a": "Winner-Take-All competition finds the Best Matching Unit (BMU), and topological neighborhood functions update both the BMU and its spatial neighbors",
            "option_b": "Supervised backpropagation of MSE loss through multiple fully connected layers",
            "option_c": "Max-margin hyperplane optimization using Lagrange multipliers",
            "option_d": "Random dropout of 50% of feature maps on every iteration",
            "answer": "A",
            "explanation": "Kohonen SOM uses competitive unsupervised learning: the BMU is found by minimizing Euclidean distance ||x - w_c||, and weights of the BMU and neighbors within radius sigma(t) are updated.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Delta rule",
            "question": "How does Widrow-Hoff Delta Rule (Adaline learning) differ from the original Rosenblatt Perceptron learning rule?",
            "option_a": "The Delta rule computes error based on the linear continuous sum before the activation threshold, while Perceptron computes error based on quantized binary step outputs",
            "option_b": "Adaline requires 10 hidden layers while Perceptron has no layers",
            "option_c": "Delta rule does not use any learning rate parameter",
            "option_d": "Perceptron minimizes MSE loss via continuous gradient descent",
            "answer": "A",
            "explanation": "Adaline (Least Mean Squares) uses the continuous analog output (net = w^T x) to calculate error (y - net), enabling smooth gradient descent along the quadratic error bowl.",
            "difficulty": "medium",
            "question_type": "comparison"
        },
        {
            "topic": "CNN introduction",
            "question": "What two spatial inductive biases in Convolutional Neural Networks (CNNs) dramatically reduce parameter count compared to fully connected MLPs on image data?",
            "option_a": "Local Receptive Fields (spatial locality) and Shared Weights (parameter sharing across feature maps)",
            "option_b": "Recurrent feedback connections and Long Short-Term memory cells",
            "option_c": "Fuzzy membership functions and defuzzification layers",
            "option_d": "Global dense matrix inversions and full covariance estimation",
            "answer": "A",
            "explanation": "CNNs exploit translation invariance and locality in visual data through small shared convolutional kernels, requiring orders of magnitude fewer parameters than dense layers.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "RNN introduction",
            "question": "Why do standard vanilla Recurrent Neural Networks (RNNs) struggle with capturing long-term temporal dependencies when trained with Backpropagation Through Time (BPTT)?",
            "option_a": "Gradients exponentially vanish or explode across repeated matrix multiplications over long time horizons: prod_{t=1}^T W_{hh}",
            "option_b": "RNNs can only process 1 token of input per epoch",
            "option_c": "Hidden state dimensions must be exactly equal to 1",
            "option_d": "RNN loss functions cannot be computed using cross-entropy",
            "answer": "A",
            "explanation": "During BPTT, the gradient chain contains products of transition weight matrices W_{hh}. If eigenvalues > 1 gradients explode; if < 1 they vanish to zero, preventing learning of distant steps.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Learning Vector Quantization",
            "question": "How does Learning Vector Quantization (LVQ) utilize class labels to refine competitive unsupervised prototype vectors?",
            "option_a": "If the winning prototype has the same class label as the input x, it is pulled closer to x; if it has a different class, it is pushed away from x",
            "option_b": "It replaces prototypes with average values of all clusters",
            "option_c": "It uses resolution refutation to prune incorrect prototypes",
            "option_d": "It converts prototype vectors into discrete Boolean truth tables",
            "answer": "A",
            "explanation": "LVQ is supervised: if BMU w_c matches class y, w_c = w_c + eta(x - w_c) (attraction); if classes mismatch, w_c = w_c - eta(x - w_c) (repulsion), carving optimal class boundaries.",
            "difficulty": "hard",
            "question_type": "algorithm_tracing"
        },
        {
            "topic": "Biological neuron",
            "question": "In the biological neuron analog, which biological structures correspond to: inputs, summation/processing, and transmission output in an artificial neuron?",
            "option_a": "Dendrites (inputs), Soma / Cell body (summation), Axon (transmission output)",
            "option_b": "Axon (inputs), Synapse (summation), Dendrites (output)",
            "option_c": "Myelin sheath (inputs), Nucleus (summation), Glial cells (output)",
            "option_d": "Synapse (inputs), Dendrites (summation), Soma (output)",
            "answer": "A",
            "explanation": "Dendrites receive synaptic signals, the Soma integrates electrical post-synaptic potentials, and if threshold is reached, an action potential propagates down the Axon.",
            "difficulty": "easy",
            "question_type": "conceptual"
        }
    ]
    for q in s2_m5:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m5_name, "module_number": 5})
        questions.append(q)
        q_id += 1

    # S2 M6: Hybrid System
    m6_name = "Module VI - Hybrid System"
    s2_m6 = [
        {
            "topic": "ANFIS",
            "question": "In the Adaptive Neuro-Fuzzy Inference System (ANFIS) architecture based on the first-order Takagi-Sugeno model, what occurs in Layer 1 and Layer 4 respectively?",
            "option_a": "Layer 1 generates fuzzy membership grades (premise parameters); Layer 4 computes linear Takagi-Sugeno output functions (consequent parameters: f_i = p_i x + q_i y + r_i)",
            "option_b": "Layer 1 performs defuzzification; Layer 4 performs input normalization",
            "option_c": "Layer 1 evaluates convolutional filters; Layer 4 evaluates max pooling",
            "option_d": "Layer 1 computes centroid defuzzification; Layer 4 performs Hebbian learning",
            "answer": "A",
            "explanation": "ANFIS has 5 layers: L1 fuzzifies inputs with parameterized membership functions (premise params), L2 multiplies firing strengths, L3 normalizes, L4 computes consequent rule outputs, and L5 sums outputs.",
            "difficulty": "hard",
            "question_type": "architecture"
        },
        {
            "topic": "ANFIS",
            "question": "What hybrid learning algorithm is employed in ANFIS to efficiently optimize both premise and consequent parameters?",
            "option_a": "Least Squares Estimation (LSE) in the forward pass for linear consequent parameters, and Gradient Descent (Backpropagation) in the backward pass for non-linear premise parameters",
            "option_b": "Genetic algorithms running exclusively on both forward and backward passes",
            "option_c": "Pure k-means clustering without gradient calculation",
            "option_d": "Simulated annealing on premise parameters and A* search on consequent parameters",
            "answer": "A",
            "explanation": "The hybrid ANFIS learning algorithm holds premise parameters fixed in the forward pass and finds optimal consequent parameters via LSE in one step, then backpropagates error to update premise parameters via gradient descent.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Neuro-Fuzzy systems",
            "question": "Why are Neuro-Fuzzy hybrid systems considered superior to standalone Neural Networks and standalone Fuzzy Systems?",
            "option_a": "They combine the transparent linguistic interpretability of fuzzy IF-THEN rules with the automated data-driven learning/optimization power of neural networks",
            "option_b": "They eliminate all mathematical computations from the control loop",
            "option_c": "They guarantee that model accuracy is always 100% on any dataset",
            "option_d": "They replace microprocessors with analog mechanical circuits",
            "answer": "A",
            "explanation": "Neural networks are black boxes that learn from data; fuzzy systems are white boxes requiring expert rules. Neuro-fuzzy systems merge both: interpretable rule structures learned automatically from numerical data.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Forecasting",
            "question": "In non-linear time series forecasting (such as electrical grid load prediction or financial index forecasting), what advantage does a Neuro-Fuzzy model offer?",
            "option_a": "It captures complex nonlinear seasonal trends while maintaining rule-based explanations for why sudden spikes or troughs are forecasted",
            "option_b": "It requires only 1 data point to predict 10 years of future load",
            "option_c": "It forces all future forecasts to be strictly constant horizontal lines",
            "option_d": "It removes the requirement for time-series feature stationarity checks",
            "answer": "A",
            "explanation": "Neuro-fuzzy forecasting provides universal function approximation for non-linear dynamics while outputting human-auditable fuzzy rules explaining the forecast drivers.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Robotics",
            "question": "In autonomous robotic navigation, how does a hybrid Fuzzy-Neural controller handle obstacle avoidance in unknown cluttered environments?",
            "option_a": "Fuzzy logic manages high-level reactive behavioral rules (e.g. wall following, goal attraction) while neural networks adapt sensor fusion calibrations online",
            "option_b": "The robot halts permanently whenever an obstacle is detected",
            "option_c": "The system replaces physical sensors with random path generators",
            "option_d": "The controller uses crisp lookup tables with fixed static coordinates",
            "answer": "A",
            "explanation": "Fuzzy rules provide robust, smooth reactive control laws under sensor uncertainty, while neural subsystems tune membership parameters dynamically to adapt to different terrain dynamics.",
            "difficulty": "medium",
            "question_type": "scenario"
        },
        {
            "topic": "Industrial control",
            "question": "In complex industrial chemical processes with time delays and non-linear dynamics, why does a Fuzzy-PID hybrid controller outperform a classical linear PID controller?",
            "option_a": "The fuzzy supervisory mechanism dynamically tunes the PID gains (Kp, Ki, Kd) in real-time based on current error and rate of change of error",
            "option_b": "The fuzzy controller ignores all error measurements",
            "option_c": "A classical PID controller cannot be implemented in software",
            "option_d": "The hybrid system converts continuous valve actuators into manual switches",
            "answer": "A",
            "explanation": "Self-tuning Fuzzy PID controllers adjust Kp, Ki, and Kd gains dynamically according to operating point, minimizing overshoot during large transients while eliminating steady-state error.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Comparative analysis",
            "question": "When comparing Fuzzy Systems, Neural Networks, and Genetic Algorithms in hybrid system engineering, what is the complementary capability of each?",
            "option_a": "Fuzzy Systems provide Knowledge Representation; Neural Networks provide Learning/Adaptation; Genetic Algorithms provide Global Optimization",
            "option_b": "Fuzzy Systems provide hardware acceleration; Neural Networks provide cloud storage; Genetic Algorithms provide UI rendering",
            "option_c": "All three systems have identical mathematical equations and capabilities",
            "option_d": "Neural Networks do not support gradient-based learning",
            "answer": "A",
            "explanation": "The standard triad: Fuzzy Logic handles approximate reasoning and knowledge representation, Neural Networks handle connectionist pattern learning, and Genetic Algorithms handle non-differentiable global optimization.",
            "difficulty": "easy",
            "question_type": "comparison"
        },
        {
            "topic": "Governance",
            "question": "In AI governance frameworks for safety-critical systems, why are hybrid neuro-fuzzy models favored over deep black-box architectures?",
            "option_a": "They provide high predictive fidelity with transparent rule-based audit trails essential for regulatory compliance and safety verification",
            "option_b": "They are completely immune to adversarial cyberattacks",
            "option_c": "They do not require any software testing or validation",
            "option_d": "They run without any electrical power consumption",
            "answer": "A",
            "explanation": "Safety regulations (such as medical, aviation, and financial governance) mandate explainability. Neuro-fuzzy systems expose rule sets (IF-THEN) that domain experts and auditors can inspect and verify.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Sustainability",
            "question": "How do hybrid AI systems contribute to environmental sustainability in smart green building energy management?",
            "option_a": "By optimizing HVAC and lighting schedules through predictive thermal modeling, minimizing energy wastage while preserving occupant comfort",
            "option_b": "By shutting down all cooling systems continuously regardless of room temperature",
            "option_c": "By increasing cloud server energy usage to maximum capacity",
            "option_d": "By disabling automated sensors and relying on manual switches",
            "answer": "A",
            "explanation": "Hybrid neuro-fuzzy energy controllers predict thermal loads and solar irradiance, modulating variable-speed chillers and ventilation to minimize kWh consumption while meeting comfort constraints.",
            "difficulty": "easy",
            "question_type": "application"
        },
        {
            "topic": "Hybrid systems",
            "question": "Which categorization correctly represents the three major classes of hybrid intelligent architectures?",
            "option_a": "Sequential (cascade) hybrids, Auxiliary (loosely coupled) hybrids, and Embedded (fully integrated) hybrids",
            "option_b": "Relational, NoSQL, and Graph hybrids",
            "option_c": "Client-side, Server-side, and Peer-to-peer hybrids",
            "option_d": "Monolithic, Microservice, and Serverless hybrids",
            "answer": "A",
            "explanation": "Hybrid systems are classified by integration architecture: Sequential (one technology pre-processes for another), Auxiliary (one sub-system aids another), and Embedded (tight mathematical integration like ANFIS).",
            "difficulty": "hard",
            "question_type": "conceptual"
        }
    ]
    for q in s2_m6:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m6_name, "module_number": 6})
        questions.append(q)
        q_id += 1

    return questions, q_id

if __name__ == "__main__":
    qs, last_id = generate_s2_questions(1)
    print(f"Generated {len(qs)} questions for Subject 2. Last ID: {last_id}")
