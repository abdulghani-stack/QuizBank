"""
Module by module MCQ generator for:
- Subject 5: User Experience Design with VR (2015115)
- Subject 6: Computer Network (2015116)
- Subject 7: Indian Knowledge System (2015511)
"""

def generate_s5_questions(start_id):
    # Subject 5: User Experience Design with VR (2015115)
    s_name = "User Experience Design with VR"
    s_code = "2015115"
    q_id = start_id
    questions = []

    # S5 M1: Introduction
    m1_name = "Module I - Introduction"
    s5_m1 = [
        {
            "topic": "Norman's design principles",
            "question": "In Don Norman's fundamental design principles for human-centered design, what is an 'Affordance'?",
            "option_a": "The perceived and actual properties of an object that determine how it could possibly be used (e.g. a physical button invites pushing)",
            "option_b": "The total financial cost of developing the user interface",
            "option_c": "The amount of memory consumed by a graphic asset",
            "option_d": "The font size used in navigation breadcrumbs",
            "answer": "A",
            "explanation": "Norman defines affordance as the relationship between a physical object and a person: the properties that indicate what actions are possible (e.g. chairs afford sitting, buttons afford pushing).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Visual processing",
            "question": "Which Gestalt law of visual perception states that human perception tends to group individual elements together if they are enclosed within a shared bounded region?",
            "option_a": "Law of Common Region",
            "option_b": "Law of Proximity",
            "option_c": "Law of Similarity",
            "option_d": "Law of Continuity",
            "answer": "A",
            "explanation": "The Law of Common Region states that elements located within the same closed boundary (such as a card container or border box) are perceived as belonging together.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "User cognition",
            "question": "According to Miller's Law in cognitive psychology and UX information architecture, what is the working memory span of an average human?",
            "option_a": "7 plus or minus 2 chunks of information (5 to 9 chunks)",
            "option_b": "20 to 25 items simultaneously",
            "option_c": "Exactly 1 single binary bit",
            "option_d": "Infinite memory capacity without chunking",
            "answer": "A",
            "explanation": "George A. Miller (1956) showed that short-term memory capacity is 7 +/- 2 chunks, guiding UX designers to chunk complex forms and navigation menus into digestible groups.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Core UX elements",
            "question": "In Jesse James Garrett's 'The Elements of User Experience', what are the five planes of UX from abstract strategy to concrete product?",
            "option_a": "Strategy Plane -> Scope Plane -> Structure Plane -> Skeleton Plane -> Surface Plane",
            "option_b": "HTML Plane -> CSS Plane -> JS Plane -> SQL Plane -> Cloud Plane",
            "option_c": "Idea Plane -> Budget Plane -> Code Plane -> QA Plane -> Sales Plane",
            "option_d": "Wireframe Plane -> Color Plane -> Typography Plane -> Animation Plane -> Launch Plane",
            "answer": "A",
            "explanation": "Garrett's framework moves bottom-up from abstract to concrete: Strategy (user needs/business goals) -> Scope (features) -> Structure (interaction/IA) -> Skeleton (interface/wireframes) -> Surface (visuals).",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Human perception",
            "question": "What is the phenomenon of 'Change Blindness' in human visual perception, and what design guideline does it imply for UX notifications?",
            "option_a": "Users fail to notice visual changes in a scene when their attention is focused elsewhere; important status alerts must use salient motion, contrast, or haptic cues",
            "option_b": "Users can process 1,000 visual changes per second effortlessly",
            "option_c": "Users cannot distinguish between red and green colors in low light",
            "option_d": "Users always memorize the layout of a webpage on first glance",
            "answer": "A",
            "explanation": "Change blindness occurs when changes in visual fields go unnoticed if attention is diverted. Critical UX state changes require focal feedback (animations, badges, toast alerts) to capture awareness.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Interface conceptualization",
            "question": "What is a 'Mental Model' in user interface conceptualization?",
            "option_a": "A user's internal conceptual understanding of how a system works, shaped by prior experiences with real-world objects and other interfaces",
            "option_b": "The physical silicon architecture of the computer CPU",
            "option_c": "The relational database schema diagram stored on the server",
            "option_d": "A 3D CAD drawing of the computer monitor chassis",
            "answer": "A",
            "explanation": "Mental models represent what users believe they know about a system. When the designer's conceptual model mismatches the user's mental model, friction and usability errors occur.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Norman's design principles",
            "question": "When a user pushes a door with a flat brass plate and it opens effortlessly, but pushes a door with a pull-handle and it fails to open, what design violation has occurred in the second door?",
            "option_a": "A 'Norman Door' caused by a false signifier / poor mapping where a pull-handle falsely affords pulling when pushing is required",
            "option_b": "A server side database timeout error",
            "option_c": "A violation of the Fitts' Law index of difficulty",
            "option_d": "A color contrast ratio failure under WCAG 2.1",
            "answer": "A",
            "explanation": "A 'Norman Door' is a classic example of flawed design: physical handles signal 'pull' whereas flat plates signal 'push'. Mismatching physical affordance/signifier causes user failure.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Interface design",
            "question": "According to Fitts's Law in UI/UX interaction design, what determines the time required to rapidly move to and acquire a target on screen?",
            "option_a": "Movement Time is a logarithmic function of target distance (D) divided by target width (W): MT = a + b * log2(2D / W)",
            "option_b": "The total number of colors used in the target button icon",
            "option_c": "The network latency of the web server in milliseconds",
            "option_d": "The operating system kernel scheduler priority",
            "answer": "A",
            "explanation": "Fitts's Law states that larger targets (width W) located closer to the starting cursor/finger position (distance D) are acquired significantly faster and with fewer errors.",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "UX elements",
            "question": "What is the primary difference between User Interface (UI) and User Experience (UX)?",
            "option_a": "UI refers to the specific visual touchpoints, layouts, and typography of the screen; UX encompasses the overall journey, emotional satisfaction, and ease of task completion",
            "option_b": "UI is for software applications while UX is for physical automobiles only",
            "option_c": "UI requires coding while UX is strictly graphic illustration",
            "option_d": "UI and UX are identical synonyms with no distinction",
            "answer": "A",
            "explanation": "UI is the aesthetic and functional presentation layer (screens, buttons, colors); UX is the holistic human experience, usability, utility, and satisfaction across all touchpoints.",
            "difficulty": "easy",
            "question_type": "comparison"
        },
        {
            "topic": "Visual processing",
            "question": "What is the 'F-Shaped Pattern' identified by Nielsen Norman Group in web eye-tracking studies?",
            "option_a": "Users scan web content with two horizontal stripes across the top followed by a short vertical stripe down the left margin, rarely reading full paragraphs line by line",
            "option_b": "Users read every web page in an inverted Z pattern starting from the bottom right",
            "option_c": "Users only look at circular images in the exact center of the page",
            "option_d": "Users scan content diagonally from top right to bottom left exclusively",
            "answer": "A",
            "explanation": "Eye-tracking heatmaps demonstrate that web users scan text-heavy pages in an F-pattern: reading the top headline, scanning a shorter second line, then glancing down the left edge.",
            "difficulty": "easy",
            "question_type": "conceptual"
        }
    ]
    for q in s5_m1:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m1_name, "module_number": 1})
        questions.append(q)
        q_id += 1

    # S5 M2: UX Design Life Cycle
    m2_name = "Module II - UX Design Life Cycle"
    s5_m2 = [
        {
            "topic": "UX",
            "question": "In the UX Design Life Cycle (Hartson & Pyla's Wheel model), what are the four primary iterative lifecycle phases?",
            "option_a": "Analyze (Contextual Inquiry) -> Design (Conceptual/Interaction) -> Prototype (Fidelity) -> Evaluate (Usability Testing)",
            "option_b": "Plan -> Code -> Compile -> Deploy",
            "option_c": "Brainstorm -> Wireframe -> Sell -> Retire",
            "option_d": "Discover -> Pitch -> Profit -> Close",
            "answer": "A",
            "explanation": "The UX Lifecycle Wheel consists of 4 iterative, user-centered activities: Analyze (work activity), Design (interaction design), Prototype (wireframes/mockups), and Evaluate (formative/summative).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Usability",
            "question": "According to ISO 9241-11, what are the three core metrics that define Usability?",
            "option_a": "Effectiveness (accuracy and completeness), Efficiency (resources expended), and Satisfaction (comfort and positive attitudes)",
            "option_b": "Speed, Memory Consumption, and Battery Usage",
            "option_c": "Lines of Code, Code Coverage, and Deployment Frequency",
            "option_d": "Click Through Rate, Revenue per User, and Bounce Rate",
            "answer": "A",
            "explanation": "ISO 9241-11 defines usability as the extent to which a system can be used by specified users to achieve specified goals with Effectiveness, Efficiency, and Satisfaction.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Usability to UX",
            "question": "How did the evolution from classical 'Usability' to modern 'User Experience' (UX) expand the scope of design evaluation?",
            "option_a": "From pragmatic task completion, error rates, and speed (usability) to holistic emotional resonance, joy, aesthetics, brand trust, and long-term engagement (UX)",
            "option_b": "By abandoning all user testing and relying on algorithm predictions",
            "option_c": "By replacing digital screens with physical paper forms",
            "option_d": "By requiring all software to be free of charge",
            "answer": "A",
            "explanation": "Usability focused on pragmatic/functional efficiency ('Can the user do it?'). UX expanded this to hedonic attributes ('How does the user feel while doing it? Delight, aesthetics, meaning').",
            "difficulty": "medium",
            "question_type": "comparison"
        },
        {
            "topic": "Emotional impact",
            "question": "In Don Norman's 'Emotional Design', what are the three levels of cognitive/emotional processing that influence user experience?",
            "option_a": "Visceral Level (subconscious gut reactions to aesthetics), Behavioral Level (usability and pleasure of use), and Reflective Level (conscious meaning, self-image, and pride)",
            "option_b": "Alpha level, Beta level, and Gamma level",
            "option_c": "Hardware level, Firmware level, and Software level",
            "option_d": "Primary level, Secondary level, and Tertiary level",
            "answer": "A",
            "explanation": "Norman's 3 levels: Visceral (immediate sensory impact of form/feel), Behavioral (functional performance and usability in use), Reflective (retrospective contemplation and self-identity).",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "UX business case",
            "question": "How does investing in UX during early analysis and prototyping reduce overall software development costs (the 1:10:100 rule)?",
            "option_a": "Fixing a usability problem costs $1 in design analysis, $10 during active coding, and $100+ after production release due to refactoring, support tickets, and lost customer churn",
            "option_b": "UX eliminates the need for software developers",
            "option_c": "Designers work for 100 times less salary than engineers",
            "option_d": "UX software licenses are 100% tax deductible",
            "answer": "A",
            "explanation": "The 1:10:100 rule (Robert Pressman) shows that catching flaws early during UX wireframing is exponentially cheaper than fixing live software and supporting frustrated end-users.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Ubiquitous interaction",
            "question": "What characterizes 'Ubiquitous Interaction' in modern computing environments?",
            "option_a": "Computation integrated seamlessly into everyday physical environments, wearables, smart home devices, and IoT sensors, moving beyond standard desktop screens",
            "option_b": "Using single desktop computers with CRT monitors in dedicated computer labs",
            "option_c": "Interacting exclusively via punch cards and magnetic tapes",
            "option_d": "A single centralized mainframe terminal serving 500 passive terminals",
            "answer": "A",
            "explanation": "Mark Weiser's vision of Ubiquitous Computing (UbiComp) weaves technology into everyday physical contexts (ambient displays, smartwatches, voice assistants, context-aware devices).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Roots of usability",
            "question": "What historical engineering disciplines formed the foundational roots of modern usability engineering?",
            "option_a": "Ergonomics, Human Factors Engineering, Cognitive Psychology, and Human-Computer Interaction (HCI)",
            "option_b": "Civil engineering and structural concrete testing",
            "option_c": "Quantum physics and optical astronomy",
            "option_d": "Chemical synthesis and petroleum refining",
            "answer": "A",
            "explanation": "Usability evolved from WWII cockpit ergonomics/human factors (preventing pilot error under stress), cognitive psychology, and computer science HCI laboratories (Xerox PARC).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "UX",
            "question": "In the UX design lifecycle, what is the role of an 'Iterative Lifecycle'?",
            "option_a": "Repeated cycles of designing, prototyping, testing with real users, and refining, acknowledging that great UX cannot be achieved in a single linear pass",
            "option_b": "A waterfall process where design is finalized in Month 1 and never altered",
            "option_c": "A method for automatically generating code without human oversight",
            "option_d": "A strategy for releasing untested software directly to production",
            "answer": "A",
            "explanation": "Iterative design continually uncovers user misunderstandings through empirical testing, refining fidelity across progressive sprints to converge on optimal usability.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Usability",
            "question": "What is the 'System Usability Scale' (SUS) and what score indicates an above-average usability benchmark?",
            "option_a": "A 10-item Likert-scale standardized usability questionnaire; a score above 68 is considered above average (Grade C+ / B)",
            "option_b": "A scale from 1 to 5 measuring server network bandwidth",
            "option_c": "A benchmark measuring the number of colors on a web page",
            "option_d": "A metric measuring developer typing speed in words per minute",
            "answer": "A",
            "explanation": "John Brooke's SUS (System Usability Scale) yields a 0-100 composite score based on 10 standardized alternating positive/negative items. The empirical global average benchmark is 68.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Emotional impact",
            "question": "What is the 'Aesthetic-Usability Effect' discovered in UX empirical research (Kurosu & Kashimura / Tractinsky)?",
            "option_a": "Users perceive visually appealing, aesthetically polished designs as significantly more usable and are more forgiving of minor usability glitches",
            "option_b": "Users prefer ugly interfaces because they look more technical",
            "option_c": "Aesthetic quality has zero impact on user emotional perception",
            "option_d": "Complex visual graphics make software 100% bug-free",
            "answer": "A",
            "explanation": "The Aesthetic-Usability Effect demonstrates that attractive interfaces induce positive emotional states, enhancing cognitive flexibility and leading users to perceive products as easier to use.",
            "difficulty": "easy",
            "question_type": "conceptual"
        }
    ]
    for q in s5_m2:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m2_name, "module_number": 2})
        questions.append(q)
        q_id += 1

    # Add S5 M3, M4, M5, M6
    s5_m3_name = "Module III - UX Design Process"
    s5_m3 = [
        {
            "topic": "Personas",
            "question": "In user-centered design, what is a 'Persona' and how should it be constructed?",
            "option_a": "A fictional archetype representing a key user segment, constructed from empirical user research data (interviews, observation) detailing goals, behaviors, and pain points",
            "option_b": "A real individual user's complete private contact information",
            "option_c": "A fictional cartoon character used solely for marketing advertisements",
            "option_d": "An imaginary ideal user invented without conducting any field research",
            "answer": "A",
            "explanation": "Alan Cooper introduced Personas: composite archetypes based on real behavioral patterns discovered during contextual inquiry, helping design teams make empathetic, user-centered decisions.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Contextual inquiry",
            "question": "What are the four core principles of Contextual Inquiry field research (Beyer & Holtzblatt)?",
            "option_a": "Context (in user's natural environment), Partnership (master-apprentice model), Interpretation (shared understanding of actions), and Focus (guiding scope)",
            "option_b": "Speed, Cost, Efficiency, and Scalability",
            "option_c": "Interviewing, Surveying, Rating, and Billing",
            "option_d": "Hypothesis, Experiment, Control, and Publish",
            "answer": "A",
            "explanation": "Contextual Inquiry relies on: Context (observe work where it happens), Partnership (collaborative exploration), Interpretation (validating insights with user), and Focus (clear research bounds).",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Design thinking",
            "question": "What are the five non-linear stages of the Stanford d.school Design Thinking framework?",
            "option_a": "Empathize -> Define -> Ideate -> Prototype -> Test",
            "option_b": "Brainstorm -> Wireframe -> Code -> Deploy -> Monetize",
            "option_c": "Survey -> Pitch -> Build -> Market -> Scale",
            "option_d": "Listen -> Agree -> Contract -> Deliver -> Invoice",
            "answer": "A",
            "explanation": "Design Thinking: Empathize (understand user needs), Define (state problem), Ideate (generate wild ideas), Prototype (build low-fidelity models), Test (evaluate with users).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Information architecture",
            "question": "In information architecture, what is 'Card Sorting' used for?",
            "option_a": "A generative research method where users organize content topics into categories to design intuitive website navigation menus and taxonomies",
            "option_b": "A method for sorting physical poker cards during recreational breaks",
            "option_c": "An algorithm for sorting database records by timestamp",
            "option_d": "A technique for testing mobile screen scratch resistance",
            "answer": "A",
            "explanation": "Card sorting (open or closed) reveals users' mental models: how they group, categorize, and label content, forming the foundation of effective site navigation trees.",
            "difficulty": "easy",
            "question_type": "application"
        },
        {
            "topic": "Wireframes",
            "question": "What is the primary objective of Low-Fidelity Wireframes during the conceptual design phase?",
            "option_a": "To quickly map out structural layout, visual hierarchy, and functional content placement without getting distracted by colors, fonts, and polished visual styling",
            "option_b": "To generate final pixel-perfect assets for App Store submission",
            "option_c": "To write production JavaScript code",
            "option_d": "To test high-fidelity GPU shader animations",
            "answer": "A",
            "explanation": "Low-fidelity wireframes (grayscale, simple boxes) focus discussion on information architecture, workflow, and layout before teams invest time in typography, colors, and high-fidelity mockups.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Prototyping",
            "question": "In UX prototyping methodologies, what is a 'Wizard of Oz' prototype?",
            "option_a": "A prototype where complex autonomous backend logic (e.g. AI/NLP) is simulated in real-time by a hidden human operator while the user believes the system is fully automated",
            "option_b": "A prototype featuring green cartoon animations",
            "option_c": "A fully coded production microservice deployed on AWS",
            "option_d": "A prototype that requires no human testing",
            "answer": "A",
            "explanation": "Wizard of Oz testing tests user reactions to envisioned AI/intelligent systems before writing algorithms: a hidden human ('the wizard') behind the scenes produces responses dynamically.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Mobile UX",
            "question": "In mobile UI design, what is Steven Hoober's 'Thumb Zone' principle?",
            "option_a": "The natural arc reachable by a user's thumb when holding a smartphone with one hand; critical navigation targets should sit in the 'Natural' zone near the screen bottom",
            "option_b": "A fingerprint scanner security area on the back of the phone",
            "option_c": "The top-left corner of large tablet displays",
            "option_d": "A physical rubber case accessory for mobile gaming",
            "answer": "A",
            "explanation": "Over 75% of mobile interactions rely on one thumb. The bottom and center of the screen are effortless ('Natural'), while top corners are 'Hard to Reach', dictating bottom navigation bars.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Use-case modelling",
            "question": "In UX interaction design, how does a 'User Journey Map' differ from a formal UML Use Case Diagram?",
            "option_a": "A Journey Map visualizes the user's emotional experience, thoughts, touchpoints, and frustrations over time across channels, while UML Use Cases capture technical system actors and pre/post conditions",
            "option_b": "Journey Maps only use SQL database tables",
            "option_c": "UML diagrams are written strictly by end-users",
            "option_d": "Journey Maps cannot be shared with stakeholders",
            "answer": "A",
            "explanation": "Journey maps are human-centered and narrative-driven, mapping touchpoints and emotional highs/lows; UML use cases are functional specifications of system boundary interactions.",
            "difficulty": "medium",
            "question_type": "comparison"
        },
        {
            "topic": "Ideation",
            "question": "What is the 'Crazy Eights' fast-sketching exercise commonly conducted in Google Design Sprints?",
            "option_a": "Participants fold a paper into 8 sections and sketch 8 distinct idea variations in 8 minutes (1 minute per sketch) to rapidly push past first obvious solutions",
            "option_b": "Drawing 8 concentric circles to measure visual acuity",
            "option_c": "Writing 8 lines of Python code in 8 seconds",
            "option_d": "Conducting 8-hour usability testing sessions with 8 users",
            "answer": "A",
            "explanation": "Crazy Eights is a core Design Sprint ideation technique: rapid sketching under strict time pressure forces designers to explore divergent, non-obvious solution possibilities.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Conceptual design",
            "question": "What is the purpose of using Metaphors (e.g. desktop, shopping cart, folder) in conceptual UI design?",
            "option_a": "They map unfamiliar digital concepts to familiar real-world objects, allowing users to leverage existing mental models for intuitive interactions",
            "option_b": "They encrypt database tables using poetic language",
            "option_c": "They replace software code with physical hardware models",
            "option_d": "They decrease visual contrast on mobile screens",
            "answer": "A",
            "explanation": "Design metaphors (the desktop, folders, trash can, shopping cart) provide instant conceptual familiarity, reducing cognitive load and accelerating user adoption.",
            "difficulty": "easy",
            "question_type": "conceptual"
        }
    ]
    for q in s5_m3:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": s5_m3_name, "module_number": 3})
        questions.append(q)
        q_id += 1

    # S5 M4: UX Evolution and Improvement
    s5_m4_name = "Module IV - UX Evolution and Improvement"
    s5_m4 = [
        {
            "topic": "Heuristic evaluation",
            "question": "According to Jakob Nielsen's 10 Usability Heuristics, what does 'Visibility of System Status' mandate?",
            "option_a": "The system should always keep users informed about what is going on, through appropriate feedback within reasonable time (e.g. progress bars, loading spinners)",
            "option_b": "All backend source code must be publicly visible on GitHub",
            "option_c": "The computer monitor brightness must remain at 100%",
            "option_d": "All user passwords must be displayed in plaintext",
            "answer": "A",
            "explanation": "Nielsen's 1st Heuristic: systems must provide immediate, clear feedback (e.g. upload progress, active indicators) so users never wonder whether their action registered.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Formative evaluation",
            "question": "What is the defining distinction between Formative Evaluation and Summative Evaluation in UX design?",
            "option_a": "Formative is conducted during development to diagnose usability problems and guide redesign (qualitative); Summative is conducted at completion to assess overall performance against benchmarks (quantitative)",
            "option_b": "Formative is for hardware while Summative is for software",
            "option_c": "Summative is conducted before any design starts",
            "option_d": "Formative testing cannot involve human participants",
            "answer": "A",
            "explanation": "As Robert Stake summarized: 'When the cook tastes the soup, that's formative; when the guests taste the soup, that's summative.' Formative diagnoses problems; summative grades overall success.",
            "difficulty": "medium",
            "question_type": "comparison"
        },
        {
            "topic": "Heuristic evaluation",
            "question": "In Nielsen's research on Usability Inspection, how many expert evaluators are recommended to identify roughly 75-85% of usability problems using Heuristic Evaluation?",
            "option_a": "3 to 5 expert evaluators",
            "option_b": "Exactly 1 evaluator is sufficient for 100% detection",
            "option_c": "At least 500 evaluators must be surveyed",
            "option_d": "Evaluators cannot find usability problems without eye-trackers",
            "answer": "A",
            "explanation": "Nielsen & Landauer demonstrated diminishing returns: 3-5 evaluators find 75-85% of usability violations; beyond 5, additional evaluators find increasingly redundant issues.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "UX metrics",
            "question": "What is 'Task Success Rate' (Completion Rate) in summative usability testing?",
            "option_a": "The percentage of test participants who successfully complete a defined task without critical error: (Successful Completions / Total Attempts) * 100",
            "option_b": "The total number of CPU clock cycles required to compile code",
            "option_c": "The salary bonus paid to software developers upon feature launch",
            "option_d": "The number of lines of CSS styling written per hour",
            "answer": "A",
            "explanation": "Task Success Rate is the fundamental metric of effectiveness: binary 0/1 recording whether participants achieve the task goal successfully without giving up.",
            "difficulty": "easy",
            "question_type": "numerical"
        },
        {
            "topic": "UX in Agile",
            "question": "What is the 'Sprint 0' / 'Dual-Track Agile' approach for integrating UX designers into Agile engineering teams?",
            "option_a": "UX designers work one or two sprints ahead on 'Discovery Track' (research, wireframing, testing) providing validated user stories to developers on the 'Delivery Track'",
            "option_b": "Designers only design software after developers finish writing all backend code",
            "option_c": "Agile teams eliminate all UX design activities to write code faster",
            "option_d": "Developers design wireframes while UX designers manage cloud servers",
            "answer": "A",
            "explanation": "Dual-Track Agile runs Discovery (UX researching/prototyping solutions 1-2 sprints ahead) concurrently with Delivery (developers implementing previously validated stories).",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "UX maturity models",
            "question": "In Nielsen Norman Group's UX Maturity Model, what characterizes an organization at Stage 6 (User-Driven / Embedded UX)?",
            "option_a": "UX research and human-centered design principles drive corporate strategy, investment decisions, product roadmaps, and business metrics across all leadership levels",
            "option_b": "The organization has never heard of UX and has zero designers",
            "option_c": "UX is only used to fix cosmetic icon colors the night before release",
            "option_d": "The organization outsources all design to uncoordinated third parties",
            "answer": "A",
            "explanation": "Stage 6 represents total UX maturity: user-centricity is embedded in executive strategy, continuous user discovery guides product direction, and UX metrics track ROI.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Questionnaires",
            "question": "What is the Single Ease Question (SEQ) administered immediately after a usability testing task?",
            "option_a": "A 1-item 7-point rating scale asking: 'Overall, how difficult or easy was it to complete this task?' (from 1 = Very Difficult to 7 = Very Easy)",
            "option_b": "A 100-question written essay examination",
            "option_c": "A multiple-choice math quiz",
            "option_d": "A survey asking users for their personal credit card numbers",
            "answer": "A",
            "explanation": "The Single Ease Question (SEQ) is a lightweight, standardized post-task measure capturing immediate subjective mental effort (scores >= 5.5 indicate good usability).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Walkthroughs",
            "question": "What is a 'Cognitive Walkthrough' in usability inspection?",
            "option_a": "Evaluators step through action sequences for defined user tasks, answering 4 questions at each step to determine whether a user would know what to do and notice the feedback",
            "option_b": "A physical walk through the company office corridors",
            "option_c": "An automated memory leak analysis running on the server",
            "option_d": "A test evaluating brainwave activity with an MRI scanner",
            "answer": "A",
            "explanation": "Cognitive walkthrough evaluates learnability for first-time users by analyzing: 1. Will user try to achieve right effect? 2. Will they notice correct action? 3. Associate action with effect? 4. See progress?",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Rapid UX evaluation",
            "question": "What is 'RITE' (Rapid Iterative Testing and Evaluation) methodology?",
            "option_a": "Usability testing where discovered flaws with obvious fixes are corrected immediately in the prototype after 1-2 participants, testing the revised solution on subsequent participants in the same week",
            "option_b": "Waiting 12 months after launch before collecting any user feedback",
            "option_c": "Testing only with internal software developers",
            "option_d": "Writing 500-page test reports before making any UI edits",
            "answer": "A",
            "explanation": "RITE (pioneered by Microsoft) enables rapid prototyping: as soon as an issue is identified and fix agreed upon, the prototype is updated immediately to test the remedy with remaining users.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "UX targets",
            "question": "When defining measurable UX Targets for a redesigned checkout flow, which format follows best practice in usability specifications?",
            "option_a": "'90% of novice users shall complete guest checkout in under 90 seconds with zero payment errors on mobile devices'",
            "option_b": "'The checkout flow should look nice and modern'",
            "option_c": "'Users should love our brand'",
            "option_d": "'The webpage must use blue buttons'",
            "answer": "A",
            "explanation": "Valid UX targets must be objective, measurable, and bounded: specifying user profile (novice), task (guest checkout), metric (completion time <= 90s, error rate = 0), and platform.",
            "difficulty": "easy",
            "question_type": "scenario"
        }
    ]
    for q in s5_m4:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": s5_m4_name, "module_number": 4})
        questions.append(q)
        q_id += 1

    # S5 M5: Introduction to VR
    s5_m5_name = "Module V - Introduction to VR"
    s5_m5 = [
        {
            "topic": "Three I's",
            "question": "According to Grigore Burdea, what are the 'Three I's' that define the core essence of Virtual Reality?",
            "option_a": "Immersion, Interaction, and Imagination",
            "option_b": "Input, Interface, and Output",
            "option_c": "Intelligence, Internet, and Infrastructure",
            "option_d": "Iteration, Integration, and Inspection",
            "answer": "A",
            "explanation": "Burdea's VR Triangle defines VR through the 3 I's: Immersion (sensory presence in the virtual world), Interaction (real-time responsiveness to user actions), and Imagination (mind's conceptualization).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Trackers",
            "question": "What is the difference between 3-DoF (Three Degrees of Freedom) and 6-DoF (Six Degrees of Freedom) tracking in VR Head-Mounted Displays (HMDs)?",
            "option_a": "3-DoF tracks rotational movement only (Pitch, Yaw, Roll); 6-DoF tracks both rotational (Pitch, Yaw, Roll) and positional translation (Surge/X, Sway/Y, Heave/Z in physical space)",
            "option_b": "3-DoF supports full room-scale walking while 6-DoF is limited to mobile cardboard",
            "option_c": "6-DoF only tracks eye movements",
            "option_d": "3-DoF uses 6 cameras while 6-DoF uses 3 cameras",
            "answer": "A",
            "explanation": "3-DoF (e.g. basic mobile VR) only registers head orientation (looking around). 6-DoF (e.g. Meta Quest, HTC Vive) registers rotational orientation plus physical translation (walking, crouching, leaning).",
            "difficulty": "easy",
            "question_type": "comparison"
        },
        {
            "topic": "Haptics",
            "question": "In virtual reality hardware interfaces, what is the distinction between 'Tactile Haptics' and 'Kinesthetic (Force Feedback) Haptics'?",
            "option_a": "Tactile haptics stimulates skin receptors (vibrations, surface textures, temperature); Kinesthetic haptics applies physical resistive forces to muscles and joints (weight, mechanical stiffness)",
            "option_b": "Tactile haptics is for audio while Kinesthetic is for video",
            "option_c": "Tactile haptics requires wearing heavy robotic exoskeletons",
            "option_d": "Kinesthetic haptics can only generate sound waves",
            "answer": "A",
            "explanation": "Tactile cues (vibrotactile ERM/LRA actuators) stimulate cutaneous mechanoreceptors in skin. Kinesthetic devices (robotic arms/gloves) resist muscular motion to simulate solid mass and stiffness.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "VR history",
            "question": "Who created the 'Sensorama Simulator' (1962), one of the earliest multi-sensory immersive virtual reality machines featuring 3D stereoscopic visuals, stereo sound, wind fans, and scent aromas?",
            "option_a": "Morton Heilig",
            "option_b": "Ivan Sutherland",
            "option_c": "Jaron Lanier",
            "option_d": "Palmer Luckey",
            "answer": "A",
            "explanation": "Morton Heilig built the Sensorama (1962), a pioneering multi-sensory arcade cabinet displaying 3D wide-angle color motion pictures with binaural audio, motorized vibrations, and aromas.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Five classic components",
            "question": "What are the five classic subsystems of a complete Virtual Reality system architecture?",
            "option_a": "Input devices (trackers/controllers), Output displays (visual/audio/haptic), Software/VR Engine, Database/Virtual World model, and User",
            "option_b": "CPU, RAM, Hard Disk, Power Supply, Motherboard",
            "option_c": "HTML, CSS, JavaScript, WebAssembly, SQL",
            "option_d": "Camera, Microphone, Speaker, Battery, Antenna",
            "answer": "A",
            "explanation": "Classic VR architecture comprises: Inputs (sensors, controllers), Simulation/Graphics Engine, Virtual Environment Model (geometry, physics), Output Displays (HMD, binaural sound, haptics), and the Human User.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "3D sound",
            "question": "How do Head-Related Transfer Functions (HRTFs) enable spatial 3D audio rendering in VR headsets?",
            "option_a": "By filtering audio frequencies based on how sound waves diffract and reflect around a human's unique pinnae (outer ears), head, and torso to encode exact azimuth, elevation, and distance",
            "option_b": "By playing sound at maximum volume in both ears simultaneously",
            "option_c": "By converting stereo sound into mono sound",
            "option_d": "By muting sound whenever the user rotates their head",
            "answer": "A",
            "explanation": "HRTFs mathematically model acoustic filtering caused by human anatomy (interaural time difference ITD, interaural level difference ILD, and spectral pinna cues) to position sounds in 3D space.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Immersive interaction",
            "question": "What is 'Cybersickness' (VR motion sickness) and what is its primary physiological cause according to the Sensory Conflict Theory?",
            "option_a": "A mismatch between visual motion cues perceived by the eyes in VR and the lack of corresponding physical acceleration detected by the vestibular system in the inner ear",
            "option_b": "Eye strain caused exclusively by high screen resolution",
            "option_c": "Allergic reactions to headset foam padding",
            "option_d": "Hearing damage caused by low-frequency haptic vibrations",
            "answer": "A",
            "explanation": "Sensory Conflict Theory states that cybersickness occurs when visual cues indicate movement (e.g. virtual rollercoaster) while the vestibular vestibular system senses the user sitting still.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Gesture recognition",
            "question": "In optical hand-tracking VR systems (e.g. Meta Quest hand tracking), how are pinch gestures and finger poses recognized without physical handheld controllers?",
            "option_a": "Computer vision neural networks process monochrome camera streams to extract 21 3D skeletal joint coordinates per hand in real-time, matching geometric pinch heuristics",
            "option_b": "Radioactive sensors placed inside fingertips",
            "option_c": "Measuring acoustic echoes bounced off the user's palms",
            "option_d": "Physical wires connecting fingers to the computer",
            "answer": "A",
            "explanation": "Inside-out cameras feed deep learning keypoint detection models, tracking 3D positions of 21 hand joints (wrists, knuckles, tips) at high framerates to recognize poses and gestures.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Navigation interfaces",
            "question": "Which virtual locomotion technique is most widely adopted in VR games to minimize cybersickness when navigating large virtual spaces?",
            "option_a": "Teleportation locomotion with parabolic pointer targeting and instant point-to-point transition (or quick fade-to-black)",
            "option_b": "Continuous high-speed smooth sliding with the thumbstick without FOV reduction",
            "option_c": "Forcing the user to run across real physical highways",
            "option_d": "Rotating the entire virtual horizon upside-down every 5 seconds",
            "answer": "A",
            "explanation": "Teleportation eliminates continuous optical flow on the retina while the vestibular system is stationary, effectively preventing visual-vestibular conflict and cybersickness.",
            "difficulty": "easy",
            "question_type": "application"
        },
        {
            "topic": "Graphics",
            "question": "Why is maintaining a high, stable frame rate (e.g. 90Hz to 120Hz) with motion-to-photon latency < 20ms a strict requirement in VR rendering engines?",
            "option_a": "To ensure visual updates track head movements without noticeable lag, preventing disorientation, visual judder, and motion sickness",
            "option_b": "To allow the computer monitor to turn off",
            "option_c": "Because VR headsets cannot display fewer than 200 frames per second",
            "option_d": "To reduce battery power consumption to zero",
            "answer": "A",
            "explanation": "Motion-to-photon latency > 20ms or framerate drops cause perceivable lag between head movement and display redraw, disorienting the visual cortex and inducing severe cybersickness.",
            "difficulty": "easy",
            "question_type": "conceptual"
        }
    ]
    for q in s5_m5:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": s5_m5_name, "module_number": 5})
        questions.append(q)
        q_id += 1

    # S5 M6: Applications of Virtual Reality
    s5_m6_name = "Module VI - Applications of Virtual Reality"
    s5_m6 = [
        {
            "topic": "Human factors",
            "question": "In VR optical design, what is 'Interpupillary Distance' (IPD) and why is physical IPD adjustment critical on VR headsets?",
            "option_a": "The physical distance between the centers of the user's pupils; aligning headset lens centers with eye IPD prevents eye strain, optical distortion, blurriness, and incorrect scale perception",
            "option_b": "The distance between the user's ears for audio rendering",
            "option_c": "The length of the electrical power cable",
            "option_d": "The diameter of the handheld controller trackpad",
            "answer": "A",
            "explanation": "IPD varies across humans (typically 58-72mm). Misaligned lenses cause chromatic aberration, blur, visual fatigue, and inaccurate stereoscopic depth perception.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Physical modelling",
            "question": "In interactive VR simulations (such as surgical or flight simulators), what does the Collision Detection and Physics Engine simulate in real time?",
            "option_a": "Rigid/soft-body dynamics, gravity, friction, deformation, and ray-casting intersections to ensure objects interact realistically without visual mesh interpenetration",
            "option_b": "Compiling C++ source code into bytecode",
            "option_c": "Managing user authentication passwords in SQL",
            "option_d": "Calculating financial cryptocurrency exchange rates",
            "answer": "A",
            "explanation": "Physics engines (PhysX, Havok) compute bounding volume hierarchies (BVH), continuous collision detection, and constraint resolution to simulate mass, restitution, and tissue deformation.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "VR methodology",
            "question": "In VR surgical training simulators, what is the primary pedagogical advantage over traditional textbook and video training?",
            "option_a": "Surgical residents practice complex, high-risk operative procedures with real-time 3D spatial manipulation and force-feedback haptics in a zero-risk, repeatable virtual environment",
            "option_b": "It replaces real human doctors in hospitals immediately",
            "option_c": "It eliminates the need for medical licenses",
            "option_d": "It reduces surgical operating room lighting costs",
            "answer": "A",
            "explanation": "VR surgical simulation provides deliberate practice with authentic procedural fidelity, spatial psychomotor muscle memory, and quantitative error tracking without patient risk.",
            "difficulty": "easy",
            "question_type": "case_study"
        },
        {
            "topic": "Geometric modelling",
            "question": "In real-time VR graphics optimization, what is 'Level of Detail' (LOD) polygon mesh management?",
            "option_a": "Displaying high-polygon 3D meshes when objects are close to the virtual camera, and dynamically swapping to simplified low-polygon meshes as objects move farther away to conserve GPU fill rate",
            "option_b": "Deleting all 3D textures from memory",
            "option_c": "Increasing polygon count to infinity for distant mountains",
            "option_d": "Rendering all objects as wireframe cubes exclusively",
            "answer": "A",
            "explanation": "LOD switches mesh geometry dynamically based on camera distance (screen-space coverage), preserving GPU rasterization budget and maintaining critical 90fps VR framerates.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Kinematics",
            "question": "In VR avatar embodiment, what is 'Inverse Kinematics' (IK)?",
            "option_a": "Calculating the angles and rotations of intermediate skeletal joints (such as elbows and shoulders) based on the known target positions of end-effectors (HMD and hand controllers)",
            "option_b": "Tracking the user's heartbeat and blood pressure",
            "option_c": "Rotating the virtual sun around the planet",
            "option_d": "Inverting the mouse cursor direction",
            "answer": "A",
            "explanation": "VR systems typically track only 3 points (head and 2 hands). Inverse Kinematics mathematically solves joint angles for the full arm/body skeleton to render realistic avatar poses.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Behaviour modelling",
            "question": "In immersive architectural walkthrough VR simulations, how does Behaviour Modelling populate realistic virtual urban spaces?",
            "option_a": "Autonomous Non-Player Character (NPC) agents navigate virtual paths using crowd simulation algorithms (such as Boids flocking and NavMesh pathfinding) with obstacle avoidance",
            "option_b": "By placing static cardboard cutouts of people in buildings",
            "option_c": "By locking the user into a linear camera rail",
            "option_d": "By converting 3D architectural models into 2D spreadsheets",
            "answer": "A",
            "explanation": "Behavior modeling applies steering behaviors, state machines, and pathfinding to simulate realistic crowd movements, vehicular traffic, and environmental dynamics in architectural VR.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "VR terminology",
            "question": "In virtual reality terminology, what is the 'Presence' (Sense of Being There)?",
            "option_a": "The subjective psychological state of feeling physically situated inside the virtual environment rather than in the real physical room where the body resides",
            "option_b": "The total number of pixels on the headset display panel",
            "option_c": "The physical weight of the VR headset measured in grams",
            "option_d": "The Wi-Fi network signal strength indicator",
            "answer": "A",
            "explanation": "Presence is the perceptual illusion of 'being there': when sensory inputs (visual, auditory, vestibular, haptic) are sufficiently compelling that the brain treats the virtual environment as real.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "User performance",
            "question": "When evaluating user performance in VR industrial assembly training, which quantitative metrics assess procedural proficiency?",
            "option_a": "Time to Complete Task (TCT), Error Count / Incorrect Sequence Steps, Gaze Dwell Time on Critical Warnings, and Collision Counts with safety hazards",
            "option_b": "Total lines of code in the VR engine",
            "option_c": "The color temperature of the headset LED display",
            "option_d": "The financial stock price of the VR hardware manufacturer",
            "answer": "A",
            "explanation": "VR training platforms capture granular telemetry: task completion time, accuracy of assembly steps, safety violations, tool collision precision, and situational awareness.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Model management",
            "question": "Why is 'Occlusion Culling' essential in large-scale VR virtual world management?",
            "option_a": "It prevents the GPU from wasting compute resources rendering 3D objects that are completely blocked from the user's view by opaque foreground walls or buildings",
            "option_b": "It renders all hidden objects with transparent neon outlines",
            "option_c": "It deletes all texture maps when the user blinks",
            "option_d": "It disables lighting calculations on the entire scene",
            "answer": "A",
            "explanation": "Occlusion culling identifies objects obscured by occluders (walls/doors) and culls them before the geometry pipeline, saving vertex transformation and pixel shading throughput.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "VR methodology",
            "question": "In virtual reality exposure therapy (VRET) for treating phobias (such as acrophobia or PTSD), how is systematic desensitization administered safely?",
            "option_a": "Clinicians expose patients to controlled, gradual hierarchies of virtual anxiety-inducing stimuli while monitoring physiological vitals in a secure clinical setting",
            "option_b": "By placing patients in extreme terrifying VR environments without supervision",
            "option_c": "By showing 2D cartoon movies on flat television sets",
            "option_d": "By replacing all human therapists with uncalibrated chatbots",
            "answer": "A",
            "explanation": "VRET provides controlled, graduated immersion: clinicians adjust virtual exposure intensity step-by-step while teaching relaxation techniques in a secure environment.",
            "difficulty": "easy",
            "question_type": "case_study"
        }
    ]
    for q in s5_m6:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": s5_m6_name, "module_number": 6})
        questions.append(q)
        q_id += 1

    return questions, q_id

if __name__ == "__main__":
    qs, last_id = generate_s5_questions(1)
    print(f"Generated {len(qs)} questions for Subject 5. Last ID: {last_id}")
