"""
Module by module MCQ generator for:
- Subject 3: Agile Software Development and DevOps (2015113)
- Subject 4: Web and Mobile Application Development (2015114)
- Subject 5: User Experience Design with VR (2015115)
- Subject 6: Computer Network (2015116)
- Subject 7: Indian Knowledge System (2015511)
"""

def generate_s3_questions(start_id):
    # Subject 3: Agile Software Development and DevOps (2015113)
    s_name = "Agile Software Development and DevOps"
    s_code = "2015113"
    q_id = start_id
    questions = []

    # S3 M1: Agile Project Management & DevOps Integration
    m1_name = "Module I - Agile Project Management & DevOps Integration"
    s3_m1 = [
        {
            "topic": "Scrum",
            "question": "In the Scrum framework, who is solely accountable for maximizing the value of the product resulting from the work of the Scrum Team and managing the Product Backlog?",
            "option_a": "The Product Owner",
            "option_b": "The Scrum Master",
            "option_c": "The Lead QA Automation Engineer",
            "option_d": "The External Project Stakeholder",
            "answer": "A",
            "explanation": "The Scrum Guide defines the Product Owner as the single person responsible for maximizing product value and effective Product Backlog management.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Burndown chart",
            "question": "A Sprint Burndown Chart shows the 'Remaining Effort' line trending horizontally above the 'Ideal Effort' line for the first 7 days of a 10-day sprint. What does this diagnostic signal to the team?",
            "option_a": "Work is not completing as planned, indicating blocked tasks, under-estimated scope, or scope creep risking the Sprint Goal",
            "option_b": "The team will finish all sprint commitments 3 days ahead of schedule",
            "option_c": "The CI/CD pipeline has achieved 100% code coverage",
            "option_d": "The sprint backlog has been completely cleared",
            "answer": "A",
            "explanation": "When remaining effort stays high above the ideal line, work is stalled or scope increased, warning the team and Scrum Master to remove impediments immediately.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Kanban vs Scrum",
            "question": "What is the primary operational constraint enforced in Kanban that is not a prescribed mechanism in Scrum?",
            "option_a": "Explicit Work In Progress (WIP) limits per workflow column to optimize continuous flow",
            "option_b": "Fixed-length 2-week timeboxed iterations (sprints)",
            "option_c": "Mandatory daily 15-minute standing meetings",
            "option_d": "Strict separation of Product Owner and Scrum Master roles",
            "answer": "A",
            "explanation": "Kanban is a continuous-flow method driven by Work-In-Progress (WIP) limits on workflow columns, preventing bottlenecks and multitasking without fixed timeboxes.",
            "difficulty": "medium",
            "question_type": "comparison"
        },
        {
            "topic": "User stories",
            "question": "Under the INVEST criteria for agile user stories, what does the acronym INVEST stand for?",
            "option_a": "Independent, Negotiable, Valuable, Estimable, Small, Testable",
            "option_b": "Integrated, Normalized, Verified, Executable, Scalable, Tracked",
            "option_c": "Iterative, Networked, Visualized, Encapsulated, Synchronous, Targeted",
            "option_d": "Immutable, Non-blocking, Versioned, Efficient, Standard, Tested",
            "answer": "A",
            "explanation": "Bill Wake's INVEST criteria for quality user stories: Independent, Negotiable, Valuable, Estimable, Small (fits in a sprint), and Testable.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Jira-CI/CD integration",
            "question": "How does integrating Jira with a Jenkins or GitHub Actions CI/CD pipeline automate agile tracking?",
            "option_a": "Commit messages and branch names containing Jira issue keys (e.g. 'PROJ-102') automatically transition issues, link build statuses, and display deployment environments",
            "option_b": "It converts all user stories into binary executable files",
            "option_c": "It eliminates the need for unit testing in the pipeline",
            "option_d": "It automatically rejects all merge requests without review",
            "answer": "A",
            "explanation": "Referencing the Jira key in Git branches, commits, and pull requests lets CI/CD webhooks update issue states (In Progress, In Review, Done) and show deployment telemetry.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Retrospective",
            "question": "What is the primary objective of the Sprint Retrospective event in Scrum?",
            "option_a": "To inspect how the last sprint went regarding individuals, interactions, processes, and tools, and plan improvements for the next sprint",
            "option_b": "To demonstrate completed product increments to external clients for acceptance",
            "option_c": "To estimate story points for the next three quarters",
            "option_d": "To conduct performance appraisals and assign individual blame",
            "answer": "A",
            "explanation": "The Sprint Retrospective is an internal continuous improvement session where the Scrum Team reviews what went well, what problems arose, and how they were (or were not) solved.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Velocity chart",
            "question": "A Scrum team has completed 28, 32, 30, and 34 story points across their last four 2-week sprints. What is the team's average velocity, and how should it be used for Sprint Planning?",
            "option_a": "Velocity = 31 points; used as a realistic guideline for how much backlog capacity to commit to in the upcoming sprint",
            "option_b": "Velocity = 124 points; the team must commit to 124 points in the next single sprint",
            "option_c": "Velocity = 8 points; indicating the team is under-performing",
            "option_d": "Velocity = 31 points; used to calculate individual developer salaries",
            "answer": "A",
            "explanation": "Average velocity = (28 + 32 + 30 + 34) / 4 = 124 / 4 = 31 story points per sprint, serving as empirical forecasting capacity during Sprint Planning.",
            "difficulty": "medium",
            "question_type": "numerical"
        },
        {
            "topic": "Agile fundamentals",
            "question": "Which statement is one of the four core values explicitly declared in the Agile Manifesto?",
            "option_a": "Working software over comprehensive documentation",
            "option_b": "Following a rigid plan over responding to change",
            "option_c": "Contract negotiation over customer collaboration",
            "option_d": "Processes and tools over individuals and interactions",
            "answer": "A",
            "explanation": "The 4 Agile Manifesto values: Individuals and interactions over processes and tools; Working software over comprehensive documentation; Customer collaboration over contract negotiation; Responding to change over following a plan.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Sprint planning",
            "question": "What are the two primary questions answered during the Sprint Planning event?",
            "option_a": "1. What can be delivered in this Sprint Increment? 2. How will the chosen work get done?",
            "option_b": "1. Who will be promoted? 2. What is the annual corporate budget?",
            "option_c": "1. What bugs occurred 2 years ago? 2. What is the hardware depreciation schedule?",
            "option_d": "1. Which cloud vendor offers the cheapest storage? 2. How to bypass unit tests?",
            "answer": "A",
            "explanation": "Sprint Planning addresses Topic 1: Why is this Sprint valuable? Topic 2: What can be Done this Sprint? Topic 3: How will the chosen work get done?",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Epics",
            "question": "In agile backlog hierarchy, how does an Epic relate to User Stories and Tasks?",
            "option_a": "An Epic is a large body of work that spans multiple sprints and is broken down into smaller, deliverable User Stories, which are further decomposed into technical Tasks",
            "option_b": "An Epic is a single line of source code inside a commit",
            "option_c": "Tasks contain multiple Epics, and User Stories contain projects",
            "option_d": "Epics are only used for defect bug tracking after production deployment",
            "answer": "A",
            "explanation": "Hierarchy: Epic (broad strategic capability across multiple sprints) -> User Story (user-centric functional increment within 1 sprint) -> Task (technical sub-activity).",
            "difficulty": "easy",
            "question_type": "conceptual"
        }
    ]
    for q in s3_m1:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m1_name, "module_number": 1})
        questions.append(q)
        q_id += 1

    # S3 M2: Version Control & Collaboration using Git
    m2_name = "Module II - Version Control & Collaboration using Git"
    s3_m2 = [
        {
            "topic": "Git Flow",
            "question": "In the standard Git Flow branching model, what is the role of the 'develop' branch compared to the 'main' (master) branch?",
            "option_a": "'develop' serves as the integration branch for completed features destined for the next release, while 'main' strictly stores production-ready official release history",
            "option_b": "'develop' is only used for urgent production hotfixes",
            "option_c": "'main' is deleted and recreated on every single commit",
            "option_d": "Developers commit directly to 'main' while 'develop' is read-only",
            "answer": "A",
            "explanation": "In Git Flow, 'main' reflects official production releases tagged with version numbers. 'develop' contains latest delivered development changes and is the parent of feature branches.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Merge conflicts",
            "question": "A developer runs 'git merge feature-auth' into 'develop' and receives 'CONFLICT (content): Merge conflict in server.js'. What has happened and what must be done?",
            "option_a": "Both branches modified the same lines in server.js differently; Git pauses the merge, places conflict markers (<<<<<<<, =======, >>>>>>>), and requires manual resolution before committing",
            "option_b": "Git automatically deletes the file with conflicts and creates a blank replacement",
            "option_c": "The entire Git repository is corrupted and must be re-cloned from scratch",
            "option_d": "The remote server rejected the push due to expired SSH keys",
            "answer": "A",
            "explanation": "Git cannot automatically combine conflicting edits to identical lines. It inserts conflict markers in the file and waits for the developer to edit, stage (git add), and complete the merge commit.",
            "difficulty": "easy",
            "question_type": "application"
        },
        {
            "topic": "GitHub Actions",
            "question": "In a GitHub Actions workflow YAML file (.github/workflows/ci.yml), which trigger block correctly configures the workflow to run on every push and pull request to the 'main' branch?",
            "option_a": "on: [push, pull_request] with branches: [main]",
            "option_b": "trigger: cron('0 0 * * *')",
            "option_c": "execute: on-click-only",
            "option_d": "run-when: build-failure",
            "answer": "A",
            "explanation": "GitHub Actions uses the `on:` event trigger syntax: `on: push: branches: [main]` and `pull_request: branches: [main]` to automate CI pipelines on code change events.",
            "difficulty": "medium",
            "question_type": "code_debugging"
        },
        {
            "topic": "GitHub Webhooks",
            "question": "How do GitHub Webhooks enable real-time event-driven automation with external systems like Jenkins, Jira, or Slack?",
            "option_a": "When a specified event occurs in GitHub (e.g. push, PR opened), GitHub sends an HTTP POST JSON payload to the configured external listener endpoint URL",
            "option_b": "By continuously polling GitHub every 500 milliseconds via synchronous SSH commands",
            "option_c": "By copying the entire Git commit log into an email sent to the server administrator",
            "option_d": "By opening a direct raw database socket to the external host",
            "answer": "A",
            "explanation": "Webhooks allow external integrations via push notifications: GitHub fires HTTP POST requests containing event metadata to subscribed URLs whenever repository triggers occur.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Branching",
            "question": "What Git command creates a new branch called 'feature/payment' and immediately switches the working directory to it?",
            "option_a": "git checkout -b feature/payment  (or git switch -c feature/payment)",
            "option_b": "git branch feature/payment",
            "option_c": "git commit -m 'new branch feature/payment'",
            "option_d": "git merge feature/payment",
            "answer": "A",
            "explanation": "`git checkout -b <branch>` or `git switch -c <branch>` creates the specified branch pointer at HEAD and updates HEAD to point to the new branch.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Feature branching",
            "question": "Why is short-lived feature branching preferred over long-lived feature branches in high-performing continuous delivery teams?",
            "option_a": "Short-lived branches minimize merge conflict complexity and enable continuous code integration into the shared mainline daily",
            "option_b": "Git repositories have a hard limit of 5 total branches",
            "option_c": "Long-lived branches make code reviews impossible to complete",
            "option_d": "Short-lived branches bypass all security scanners",
            "answer": "A",
            "explanation": "Long-lived branches drift significantly from main, leading to 'merge hell'. Short-lived branches merged within 1-2 days keep integration continuous and risk low.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "commit",
            "question": "What is the internal mechanism of a Git commit object?",
            "option_a": "A SHA-1/SHA-256 hash pointing to a tree object (directory snapshot), parent commit hash(es), author/committer metadata, and a log message",
            "option_b": "A delta difference file containing only changed characters without file trees",
            "option_c": "A zip archive of the entire project uploaded to a central server",
            "option_d": "A plain text row in a centralized SQLite database",
            "answer": "A",
            "explanation": "Git commits are immutable directed acyclic graph (DAG) objects referencing the root tree snapshot of the repository, metadata, and pointers to immediate ancestor commits.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "GitHub Project Boards",
            "question": "How do modern GitHub Projects (Boards) integrate with repository workflows to manage team deliverables?",
            "option_a": "They provide flexible Kanban/Table views populated by repository Issues and Pull Requests, with built-in workflow automations that move cards based on PR status",
            "option_b": "They automatically write unit test cases for pull requests",
            "option_c": "They replace the Git version control engine with Subversion",
            "option_d": "They convert markdown documentation into native iOS apps",
            "answer": "A",
            "explanation": "GitHub Projects connect issues and PRs with custom fields, automated status transitions (e.g. In Progress when PR opened, Done when merged), and team workload views.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "pull",
            "question": "What two fundamental Git operations are executed sequentially when a developer runs 'git pull origin main'?",
            "option_a": "git fetch origin main (retrieving remote commits) followed by git merge origin/main (merging them into current local branch)",
            "option_b": "git push origin main followed by git status",
            "option_c": "git checkout main followed by git branch -d main",
            "option_d": "git clone followed by git init",
            "answer": "A",
            "explanation": "`git pull` is a convenience command combining `git fetch` (downloading new objects/refs from remote) and `git merge FETCH_HEAD` (integrating remote changes into current branch).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "GitHub Issues",
            "question": "In open-source and collaborative software development on GitHub, what purpose do Issue Templates serve?",
            "option_a": "They provide structured markdown/YAML forms ensuring issue reporters provide required context such as reproduction steps, environment details, and expected behavior",
            "option_b": "They prevent external users from opening any bug reports",
            "option_c": "They automatically resolve issues without developer intervention",
            "option_d": "They execute performance stress tests on every ticket creation",
            "answer": "A",
            "explanation": "Issue templates (configured in `.github/ISSUE_TEMPLATE/`) standardize bug reports and feature requests, ensuring contributors provide necessary diagnostic reproduction steps.",
            "difficulty": "easy",
            "question_type": "conceptual"
        }
    ]
    for q in s3_m2:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m2_name, "module_number": 2})
        questions.append(q)
        q_id += 1

    # S3 M3: CI/CD Automation using Jenkins & Containerization using Docker
    m3_name = "Module III - CI/CD Automation using Jenkins & Containerization using Docker"
    s3_m3 = [
        {
            "topic": "Pipeline as Code",
            "question": "In a Declarative Jenkinsfile, which block structure defines the sequence of execution stages in Pipeline as Code?",
            "option_a": "pipeline { agent any; stages { stage('Build') { steps { sh 'mvn clean package' } } } }",
            "option_b": "docker { run 'mvn clean package' }",
            "option_c": "workflow { step1: build, step2: test }",
            "option_d": "jenkins_script { execute_all() }",
            "answer": "A",
            "explanation": "Declarative Jenkinsfile syntax begins with the top-level `pipeline {}` block, defining `agent`, and a `stages {}` block containing discrete named `stage {}` sections and `steps {}`.",
            "difficulty": "medium",
            "question_type": "code_debugging"
        },
        {
            "topic": "Dockerfiles",
            "question": "In a Dockerfile for a Node.js microservice, why should 'COPY package*.json ./' and 'RUN npm install' precede 'COPY . .'?",
            "option_a": "To leverage Docker's layer caching mechanism, preventing costly npm install re-execution when only application source code changes",
            "option_b": "Because Docker cannot copy more than 1 file in a single instruction",
            "option_c": "To ensure the node_modules folder is committed into Git",
            "option_d": "Because npm install must execute before the Docker daemon starts",
            "answer": "A",
            "explanation": "Docker caches image layers. Placing dependency manifests and installation before source copy ensures `npm install` layer is reused from cache unless `package.json` changes.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Docker Compose",
            "question": "What is the primary purpose of Docker Compose in multi-service local development and testing environments?",
            "option_a": "To define and run multi-container Docker applications (e.g. web, api, db, redis) using a single declarative YAML configuration file (`compose.yaml`)",
            "option_b": "To replace cloud Kubernetes clusters in multi-region production data centers",
            "option_c": "To compile native C++ binaries into WebAssembly",
            "option_d": "To manage physical Ethernet switches and network hardware",
            "answer": "A",
            "explanation": "Docker Compose coordinates multi-container stacks, creating isolated networks, volume mounts, environment variables, and startup dependencies via `docker compose up`.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Containers",
            "question": "How do Docker containers achieve lightweight process isolation compared to traditional Virtual Machines (VMs)?",
            "option_a": "Containers share the host OS kernel and use Linux kernel namespaces and cgroups for process/resource isolation, avoiding the overhead of guest OS kernels and hypervisors",
            "option_b": "Containers emulate full x86 hardware through software virtualization",
            "option_c": "Containers run as standalone bare-metal operating systems",
            "option_d": "Containers require a dedicated Type-1 hypervisor like VMware ESXi",
            "answer": "A",
            "explanation": "Containers virtualize the OS layer (sharing kernel, isolated via namespaces for PID/IPC/Net and cgroups for CPU/RAM limits), booting in milliseconds with minimal RAM overhead.",
            "difficulty": "medium",
            "question_type": "comparison"
        },
        {
            "topic": "Docker Hub",
            "question": "What CLI command tags a locally built Docker image 'quizbank:1.0' and pushes it to an AWS Elastic Container Registry (ECR) repository?",
            "option_a": "docker tag quizbank:1.0 <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/quizbank:1.0 && docker push <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/quizbank:1.0",
            "option_b": "docker upload quizbank:1.0 to aws-ecr",
            "option_c": "docker commit quizbank:1.0 ecr://production",
            "option_d": "docker deploy quizbank:1.0 --target ecr",
            "answer": "A",
            "explanation": "Pushing to remote registries requires tagging the image with the registry host URI (`docker tag local-image:tag registry-url/image:tag`) followed by `docker push`.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Jenkins jobs",
            "question": "In Jenkins, what is a Multi-Branch Pipeline project type?",
            "option_a": "A pipeline that automatically discovers all branches in a Git repository containing a Jenkinsfile and creates individual pipeline jobs for each branch",
            "option_b": "A job that can only execute on physical hardware nodes",
            "option_c": "A job that compiles code without executing any tests",
            "option_d": "A job that runs exclusively once per year on a cron trigger",
            "answer": "A",
            "explanation": "Multi-branch pipelines scan source control, detecting active branches (e.g. main, PR branches) with a `Jenkinsfile` and provisioning isolated build jobs automatically.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "CI/CD",
            "question": "What is the defining distinction between Continuous Delivery and Continuous Deployment?",
            "option_a": "Continuous Delivery keeps code in a deployable state with automated staging tests but requires manual approval to deploy to Production; Continuous Deployment automatically deploys to Production without manual gatekeeping",
            "option_b": "Continuous Delivery uses Jenkins while Continuous Deployment uses Docker",
            "option_c": "Continuous Deployment only runs unit tests once per month",
            "option_d": "Continuous Delivery cannot be used with cloud providers",
            "answer": "A",
            "explanation": "In Continuous Delivery, every commit that passes automated testing is ready to release, but production rollout requires a human business trigger. In Continuous Deployment, production release is 100% automated.",
            "difficulty": "easy",
            "question_type": "comparison"
        },
        {
            "topic": "Multi-service deployment",
            "question": "In a Docker Compose file defining a web app and a PostgreSQL database, which directive ensures the web container waits for the database container to become healthy before starting?",
            "option_a": "depends_on: db: condition: service_healthy",
            "option_b": "links: [db]",
            "option_c": "wait_for: postgres",
            "option_d": "delay: 60s",
            "answer": "A",
            "explanation": "`depends_on` with `condition: service_healthy` ensures that Docker Compose checks the database's `healthcheck` command before launching the dependent web service.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Jenkins installation",
            "question": "When configuring a distributed Jenkins master-agent architecture, what is the role of the Jenkins Master (Controller) versus Jenkins Agents (Executors)?",
            "option_a": "The Controller manages pipeline scheduling, web UI, and job dispatching; the Agents execute the actual CPU/memory-intensive build, test, and packaging workload",
            "option_b": "The Controller compiles code while Agents only host static documentation",
            "option_c": "Agents manage user authentication and authorization while the Master is idle",
            "option_d": "All builds must execute on the Master node exclusively",
            "answer": "A",
            "explanation": "Offloading build execution to dedicated dynamic worker agents (e.g. Docker agents or Kubernetes pods) preserves Controller responsiveness and scales build capacity.",
            "difficulty": "easy",
            "question_type": "architecture"
        },
        {
            "topic": "Images",
            "question": "Why is multi-stage building in Dockerfiles (e.g. 'FROM golang:1.22 AS builder' and 'FROM alpine:latest') a recommended production practice?",
            "option_a": "It keeps heavy build tools, compilers, and SDKs in the build stage, copying only the compiled binary to a minimal final runtime image to drastically reduce attack surface and image size",
            "option_b": "It allows a single container to run multiple operating systems concurrently",
            "option_c": "It bypasses Docker image licensing fees",
            "option_d": "It forces all source code files to remain unencrypted in production",
            "answer": "A",
            "explanation": "Multi-stage builds separate build environment from runtime, producing tiny (e.g. 15MB) secure production images without SDKs, source code, or compilers.",
            "difficulty": "hard",
            "question_type": "conceptual"
        }
    ]
    for q in s3_m3:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m3_name, "module_number": 3})
        questions.append(q)
        q_id += 1

    # S3 M4: Configuration Automation, Orchestration & Cloud Provisioning
    m4_name = "Module IV - Configuration Automation, Orchestration & Cloud Provisioning"
    s3_m4 = [
        {
            "topic": "Kubernetes",
            "question": "In Kubernetes architecture, what is the smallest deployable atomic compute unit that encapsulates one or more co-located containers sharing storage and network namespaces?",
            "option_a": "Pod",
            "option_b": "ReplicaSet",
            "option_c": "Namespace",
            "option_d": "ClusterNode",
            "answer": "A",
            "explanation": "A Pod is the basic building block in Kubernetes, wrapping one or more tightly coupled containers that share an IP address, port space, and storage volumes.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Ansible",
            "question": "What is the primary architectural advantage of Ansible's agentless design compared to agent-based configuration management tools like Chef or Puppet?",
            "option_a": "It operates over standard OpenSSH and Python on target nodes without requiring background daemons or custom software agents to be pre-installed and managed",
            "option_b": "It can only manage local localhost servers",
            "option_c": "It does not support YAML configuration playbooks",
            "option_d": "It requires physical direct serial cable connections to target nodes",
            "answer": "A",
            "explanation": "Ansible is agentless: control node pushes configuration over standard SSH (Linux) or WinRM (Windows), executing modules and removing temporary scripts automatically.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Terraform",
            "question": "In HashiCorp Terraform, what is the function of the state file (`terraform.tfstate`) and why should it be stored in remote backends (e.g. AWS S3 with DynamoDB locking)?",
            "option_a": "It maps declarative configuration files to real-world provisioned cloud resources; remote backends provide team state sharing, encryption, and state locking to prevent concurrent corruption",
            "option_b": "It compiles HCL code into Java bytecode",
            "option_c": "It stores root administrative passwords in plaintext for developer convenience",
            "option_d": "It replaces Kubernetes Pod controllers",
            "answer": "A",
            "explanation": "Terraform state tracks resource metadata and mappings. Remote backends (S3 + DynamoDB state locking) prevent race conditions when multiple engineers run `terraform apply`.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Services",
            "question": "In Kubernetes, which Service type provides a single external IP address provisioned by a cloud provider (such as AWS ALB or GCP Load Balancer) to route external internet traffic to backend Pods?",
            "option_a": "LoadBalancer",
            "option_b": "ClusterIP",
            "option_c": "NodePort",
            "option_d": "ExternalName",
            "answer": "A",
            "explanation": "ClusterIP is internal only. NodePort exposes a static port on each node. LoadBalancer provisions an external cloud load balancer routing traffic automatically.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Helm Charts",
            "question": "What role does Helm serve in Kubernetes application lifecycle management?",
            "option_a": "It is the package manager for Kubernetes, packaging YAML manifests into reusable, versioned 'Charts' with parameterized values.yaml templates",
            "option_b": "It is a hardware hypervisor for running Linux kernels",
            "option_c": "It monitors server temperatures inside physical data centers",
            "option_d": "It translates Python code into SQL queries",
            "answer": "A",
            "explanation": "Helm packages Kubernetes applications into Charts, enabling templating, variable injection (`values.yaml`), versioned release rollbacks, and dependency management.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Playbooks",
            "question": "What is the key principle of 'Idempotence' in Ansible playbooks?",
            "option_a": "Executing a playbook multiple times produces the exact same desired state on target nodes without unintended side effects or redundant changes if state is already achieved",
            "option_b": "A playbook must reboot all target servers on every run",
            "option_c": "Playbooks can only be run once and then self-destruct",
            "option_d": "All tasks in a playbook execute in random non-deterministic order",
            "answer": "A",
            "explanation": "Idempotency ensures that running an Ansible task once or 100 times results in the same final system state; if a file or package is already in desired state, Ansible takes no action.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Ingress",
            "question": "In Kubernetes, how does an Ingress Controller (e.g. NGINX Ingress) differ from a standard LoadBalancer Service?",
            "option_a": "Ingress operates at Layer 7 (HTTP/HTTPS), providing host-based and path-based routing (e.g. api.domain.com vs web.domain.com) and SSL termination under a single IP",
            "option_b": "Ingress only handles UDP raw packet streaming",
            "option_c": "Ingress replaces all Kubernetes worker nodes",
            "option_d": "Ingress cannot be used with microservices",
            "answer": "A",
            "explanation": "An Ingress Controller evaluates Layer 7 HTTP rules, consolidating routing for dozens of backend services behind a single cloud load balancer IP, saving cloud provider costs.",
            "difficulty": "hard",
            "question_type": "comparison"
        },
        {
            "topic": "Deployments",
            "question": "What Kubernetes controller manages declarative updates for Pods, enabling zero-downtime Rolling Updates and automated Rollbacks?",
            "option_a": "Deployment",
            "option_b": "DaemonSet",
            "option_c": "StatefulSet",
            "option_d": "Job",
            "answer": "A",
            "explanation": "The Deployment controller manages underlying ReplicaSets, rolling out new container image versions gradually (RollingUpdate) while ensuring a minimum number of pods stay healthy.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Providers",
            "question": "In Terraform infrastructure as code, what is a 'Provider' (such as `hashicorp/aws` or `hashicorp/azurerm`)?",
            "option_a": "A plugin that understands API interactions and exposes cloud platform resources (EC2, VPC, S3) and data sources to Terraform engine",
            "option_b": "A developer who writes HCL configuration code",
            "option_c": "A third-party contractor providing hardware hosting",
            "option_d": "A Git repository hosting commit history",
            "answer": "A",
            "explanation": "Providers are plugins that translate declarative HCL resources into REST API calls for specific platforms (AWS, Azure, GCP, Kubernetes, GitHub).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Roles",
            "question": "In Ansible project structure, what is the purpose of organizing automation tasks into 'Roles'?",
            "option_a": "To structure configuration into standardized modular directories (tasks, handlers, templates, files, vars, defaults, meta) for reusability across playbooks",
            "option_b": "To restrict user permissions in the Linux PAM authentication module",
            "option_c": "To compile YAML files into binary executables",
            "option_d": "To encrypt disk drives using AES-256",
            "answer": "A",
            "explanation": "Ansible Roles provide a standardized directory layout for grouping related automation logic, making configurations modular, versionable, and shareable on Ansible Galaxy.",
            "difficulty": "medium",
            "question_type": "conceptual"
        }
    ]
    for q in s3_m4:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m4_name, "module_number": 4})
        questions.append(q)
        q_id += 1

    # S3 M5: Agile Quality Assurance & Testing
    m5_name = "Module V - Agile Quality Assurance & Testing"
    s3_m5 = [
        {
            "topic": "Test Driven Development",
            "question": "What is the precise cycle of steps in Test-Driven Development (TDD) known as 'Red-Green-Refactor'?",
            "option_a": "1. Write a failing automated test (Red), 2. Write minimal code to make test pass (Green), 3. Clean up and optimize code without altering behavior (Refactor)",
            "option_b": "1. Write all production code, 2. Deploy to production, 3. Fix customer bugs",
            "option_c": "1. Run performance tests, 2. Write documentation, 3. Delete unit tests",
            "option_d": "1. Review pull request, 2. Build Docker container, 3. Restart server",
            "answer": "A",
            "explanation": "TDD rhythm: Red (write a unit test that fails because feature doesn't exist yet), Green (write simplest code to pass), Refactor (improve structure, remove duplication, maintain passing tests).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Test Automation Pyramid",
            "question": "According to Mike Cohn's Test Automation Pyramid, what is the recommended distribution of automated tests across tiers?",
            "option_a": "Broad base of fast, cheap Unit Tests at the bottom; moderate layer of Integration/API tests in the middle; small suite of End-to-End UI tests at the top",
            "option_b": "90% End-to-End UI tests, 10% Unit tests, 0% Integration tests (Inverted Ice Cream Cone)",
            "option_c": "Equal 33% split between Unit, UI, and Manual exploratory tests",
            "option_d": "Only manual UI tests with zero automated unit tests",
            "answer": "A",
            "explanation": "The Test Pyramid emphasizes a solid foundation of isolated, instantaneous unit tests, followed by service integration tests, and minimal brittle, slow UI end-to-end tests.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "BDD",
            "question": "In Behavior-Driven Development (BDD), what domain-specific syntax is used in Gherkin feature files to describe user scenarios?",
            "option_a": "Given (pre-conditions), When (user action/trigger), Then (observable expected outcome)",
            "option_b": "SELECT, FROM, WHERE",
            "option_c": "TRY, CATCH, FINALLY",
            "option_d": "IMPORT, DEF, RETURN",
            "answer": "A",
            "explanation": "Gherkin syntax uses Given-When-Then structure: `Given [initial context]`, `When [event occurs]`, `Then [assert expected outcome]`, fostering shared understanding between business and engineering.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Selenium",
            "question": "When developing automated browser UI regression tests using Selenium WebDriver or Cypress, what is a 'Flaky Test' and what is its primary cause?",
            "option_a": "A test that nondeterministically passes or fails on identical code without changes, often caused by race conditions, hardcoded thread sleeps, and asynchronous DOM render delays",
            "option_b": "A test that has 100% code coverage",
            "option_c": "A test that runs exclusively on mobile devices",
            "option_d": "A test that executes faster than 1 millisecond",
            "answer": "A",
            "explanation": "Flaky tests undermine CI trust. They stem from dynamic AJAX rendering, animations, or network timing issues; resolved using explicit dynamic waits rather than static `sleep()` calls.",
            "difficulty": "medium",
            "question_type": "scenario"
        },
        {
            "topic": "Postman",
            "question": "How do QA automation engineers automate REST API regression testing within CI/CD pipelines using Postman?",
            "option_a": "By exporting Postman Collections and executing them headless in CLI pipelines using the Newman test runner, asserting response status codes and JSON schemas",
            "option_b": "By manually clicking the 'Send' button in the Postman desktop GUI for every release",
            "option_c": "By taking screenshots of the Postman window",
            "option_d": "By converting JSON payloads into PDF files",
            "answer": "A",
            "explanation": "Newman is Postman's CLI test runner. It runs collections headlessly in Jenkins/GitHub Actions pipelines, running embedded JavaScript assertions (`pm.test`, `pm.expect`).",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Agile Testing Quadrants",
            "question": "In the Agile Testing Quadrants model (Brian Marick / Lisa Crispin), what is the focus of Quadrant 2 (Q2)?",
            "option_a": "Business-facing tests that support the team (Functional tests, User story tests, Prototypes, Simulations)",
            "option_b": "Technology-facing tests that critique the product (Performance, Load, Security, Scalability testing)",
            "option_c": "Technology-facing tests that support the team (Unit tests, Component tests)",
            "option_d": "Business-facing tests that critique the product (Exploratory testing, Usability testing)",
            "answer": "A",
            "explanation": "Q1 = Technology-facing supporting team (Unit/Integration); Q2 = Business-facing supporting team (Story tests/Acceptance); Q3 = Business-facing critiquing product (Exploratory/Usability); Q4 = Tech-facing critiquing product (Perf/Security).",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "JMeter",
            "question": "In Apache JMeter performance testing, what test plan elements simulate concurrent user traffic and measure throughput/response times?",
            "option_a": "Thread Groups (simulated virtual users), HTTP Request Samplers, and Listeners (aggregate reports/response graphs)",
            "option_b": "DOM Tree Selectors and CSS Style Matchers",
            "option_c": "Git commit hooks and Docker build runners",
            "option_d": "Fuzzy membership engines and Defuzzifiers",
            "answer": "A",
            "explanation": "JMeter organizes load tests into Thread Groups (number of virtual threads/users, ramp-up period, loop count), Samplers (HTTP requests), and Listeners (recording latency and error rates).",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Continuous Testing",
            "question": "Why is Continuous Testing considered an indispensable pillar of the DevOps pipeline?",
            "option_a": "It executes automated tests early, often, and continuously across every pipeline stage, providing instant quality feedback and preventing defect leakage into production",
            "option_b": "It eliminates all software testing activities completely",
            "option_c": "It forces developers to test software manually only on weekends",
            "option_d": "It replaces automated builds with manual binary file transfers",
            "answer": "A",
            "explanation": "Continuous Testing shifts testing left (unit, linting, security scanning on commit; integration on PR; performance/security in staging) to identify defects when they are cheapest to fix.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Security testing",
            "question": "In DevSecOps pipelines, what is the difference between Static Application Security Testing (SAST) and Dynamic Application Security Testing (DAST)?",
            "option_a": "SAST analyzes uncompiled/compiled source code inside-out (white-box) for known vulnerability patterns; DAST attacks running applications outside-in (black-box) over HTTP",
            "option_b": "SAST is performed only in production while DAST is performed during sprint planning",
            "option_c": "SAST requires physical server access while DAST runs without computers",
            "option_d": "DAST tests source code comments while SAST tests hardware cooling fans",
            "answer": "A",
            "explanation": "SAST (e.g. SonarQube, Semgrep) scans code at rest for vulnerabilities (SQL injection, hardcoded secrets). DAST (e.g. OWASP ZAP) probes running apps for runtime flaws.",
            "difficulty": "medium",
            "question_type": "comparison"
        },
        {
            "topic": "Exploratory testing",
            "question": "What is the primary role of manual Exploratory Testing in mature Agile environments with high automated test coverage?",
            "option_a": "Testers apply human intuition, domain creativity, and unscripted investigative probing to discover subtle usability flaws and edge-case behaviors automated scripts miss",
            "option_b": "To mechanically re-execute basic login scripts every day",
            "option_c": "To manually verify mathematical floating-point addition in the database",
            "option_d": "To replace automated unit tests in the CI pipeline",
            "answer": "A",
            "explanation": "Automation handles repetitive verification of known expectations; exploratory testing allows skilled human QA to investigate unknown edge cases, user ergonomics, and complex workflows.",
            "difficulty": "medium",
            "question_type": "conceptual"
        }
    ]
    for q in s3_m5:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m5_name, "module_number": 5})
        questions.append(q)
        q_id += 1

    # S3 M6: DevOps
    m6_name = "Module VI - DevOps"
    s3_m6 = [
        {
            "topic": "7-Cs of DevOps lifecycle",
            "question": "Which sequence correctly represents the 7-Cs of the end-to-end DevOps lifecycle?",
            "option_a": "Continuous Development, Continuous Integration, Continuous Testing, Continuous Monitoring, Continuous Feedback, Continuous Deployment, Continuous Operations",
            "option_b": "Continuous Coding, Continuous Compiling, Continuous Copying, Continuous Clicking, Continuous Caching, Continuous Crashing, Continuous Closing",
            "option_c": "Continuous Contracting, Continuous Charging, Continuous Consulting, Continuous Checking, Continuous Clustering, Continuous Calling, Continuous Cleaning",
            "option_d": "Continuous Calculation, Continuous Correction, Continuous Calibration, Continuous Compression, Continuous Cryptography, Continuous Control, Continuous Conclusion",
            "answer": "A",
            "explanation": "The 7-Cs framework encompasses the cyclical DevOps pipeline: Continuous Development, Integration, Testing, Deployment, Monitoring, Feedback, and Operations.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "DevOps principles",
            "question": "According to Gene Kim's 'The Phoenix Project' and 'The DevOps Handbook', what are 'The Three Ways' governing DevOps principles?",
            "option_a": "1. Flow (Accelerating left-to-right flow of work to customer), 2. Feedback (Amplifying right-to-left fast feedback loops), 3. Continuous Learning and Experimentation",
            "option_b": "1. Waterfall planning, 2. Cost minimization, 3. Outsourcing QA",
            "option_c": "1. Hardware provisioning, 2. Network cabling, 3. Manual deployments",
            "option_d": "1. Code obfuscation, 2. Database sharding, 3. Log deletion",
            "answer": "A",
            "explanation": "The Three Ways: First Way (optimize flow from Dev to Ops), Second Way (fast, constant feedback from Ops to Dev), Third Way (culture of experimentation, high trust, and organizational learning).",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "DevOps assessment",
            "question": "What are the four DORA (DevOps Research and Assessment) key metrics used globally to measure software delivery and operational performance?",
            "option_a": "1. Deployment Frequency, 2. Lead Time for Changes, 3. Change Failure Rate, 4. Mean Time to Restore (MTTR)",
            "option_b": "1. Lines of Code, 2. Number of Commits, 3. Bug Count, 4. Developer Hours Worked",
            "option_c": "1. CPU Usage, 2. RAM Usage, 3. Disk Space, 4. Network Bandwidth",
            "option_d": "1. Story Points, 2. Velocity, 3. Burndown Slope, 4. Sprint Length",
            "answer": "A",
            "explanation": "DORA metrics categorize elite engineering teams: Deployment Frequency (speed), Lead Time for Changes (responsiveness), Change Failure Rate (quality), and MTTR (resilience).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Business agility",
            "question": "How does adopting DevOps practices directly foster organizational Business Agility?",
            "option_a": "By dramatically reducing time-to-market for new features, allowing rapid hypothesis validation with real users and quick pivot capability based on telemetry",
            "option_b": "By eliminating the need for product management and strategic planning",
            "option_c": "By locking the organization into rigid 5-year technology roadmaps",
            "option_d": "By prohibiting changes to production software once deployed",
            "answer": "A",
            "explanation": "DevOps removes silos between Dev and Ops, enabling small batch releases, fast experimentation, quick rollback if needed, and responsiveness to market shifts.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Implementation challenges",
            "question": "What is widely recognized in industry research as the single largest impediment to successful DevOps transformation?",
            "option_a": "Organizational culture, siloed team mentalities, resistance to change, and lack of psychological safety, rather than tooling limitations",
            "option_b": "The lack of open-source software tools",
            "option_c": "The high cost of optical fiber network cables",
            "option_d": "The discontinuation of magnetic tape storage drives",
            "answer": "A",
            "explanation": "DevOps is primarily a cultural transformation: breaking down organizational silos, embracing shared ownership ('you build it, you run it'), blameless post-mortems, and psychological safety.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "DevOps tool selection",
            "question": "When selecting tools for an enterprise DevOps toolchain, why is adherence to open APIs and interoperability standards prioritized over single-vendor monolithic suites?",
            "option_a": "It avoids vendor lock-in and allows teams to integrate best-of-breed modular tools (e.g. Git, Jenkins, Terraform, Kubernetes, Prometheus) across heterogeneous environments",
            "option_b": "Because open-source tools require no software engineers to operate",
            "option_c": "Because monolithic suites cannot run on Linux servers",
            "option_d": "Because single-vendor suites are completely free of charge",
            "answer": "A",
            "explanation": "A composable, API-driven toolchain allows swapping or upgrading individual pipeline components without overhauling the entire software development lifecycle.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Cloud-based DevOps",
            "question": "In cloud-native DevOps architectures, what is 'GitOps' as popularized by tools like ArgoCD and Flux?",
            "option_a": "A paradigm where Git repositories serve as the single source of truth for declarative infrastructure and application state, with automated controllers reconciling cluster state to Git",
            "option_b": "A technique for storing compiled container binary blobs inside Git commit trees",
            "option_c": "A method for manually executing SSH commands to update production servers",
            "option_d": "A specialized Git command that replaces Kubernetes API server",
            "answer": "A",
            "explanation": "GitOps uses Git as the single source of truth. Automated agents (e.g. ArgoCD) pull changes from Git and reconcile the live Kubernetes cluster to match the declared repository state.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "DevOps case studies",
            "question": "In Netflix's classic DevOps case study, what was the primary innovation of the 'Chaos Monkey' tool in their Simian Army suite?",
            "option_a": "It deliberately and randomly terminates production EC2 server instances to ensure software services are architected to withstand unexpected infrastructure failures gracefully",
            "option_b": "It automatically writes unit test cases for junior developers",
            "option_c": "It sends marketing discount emails to random subscribers",
            "option_d": "It mines cryptocurrency during off-peak video streaming hours",
            "answer": "A",
            "explanation": "Chaos Engineering (pioneered by Netflix) proactively introduces controlled failures in production to test system resiliency, verify failovers, and build fault-tolerant distributed architectures.",
            "difficulty": "medium",
            "question_type": "case_study"
        },
        {
            "topic": "CI/CD pipelines",
            "question": "In modern blue-green deployment strategies managed by CI/CD pipelines, how is a new release switched into production with zero downtime?",
            "option_a": "The new version is deployed to an identical idle environment (Green); once validated, the router/load balancer flips incoming traffic from Blue to Green instantaneously",
            "option_b": "All production servers are wiped and re-installed over 4 hours",
            "option_c": "Users are instructed to clear browser cookies and download new browser versions",
            "option_d": "The database is permanently switched to read-only mode",
            "answer": "A",
            "explanation": "Blue-Green deployment provisions two identical environments. Traffic routes to Blue. Green receives the new release. Once health checks pass, traffic flips to Green with instant rollback if issues occur.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Application-to-DevOps mapping",
            "question": "When refactoring a legacy monolithic application for a cloud-native DevOps CI/CD lifecycle, what architectural pattern is standard for decoupling independent deployable services?",
            "option_a": "Microservices Architecture communicating via lightweight REST/gRPC APIs and asynchronous message queues",
            "option_b": "Shared-memory single-process monolithic C++ executable",
            "option_c": "Single global relational database with stored procedures containing all business logic",
            "option_d": "Client-side desktop applications reading raw shared network files",
            "answer": "A",
            "explanation": "Decomposing monoliths into autonomous microservices bounded by business domains allows individual feature teams to build, test, and deploy services independently without coordinated global releases.",
            "difficulty": "easy",
            "question_type": "architecture"
        }
    ]
    for q in s3_m6:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m6_name, "module_number": 6})
        questions.append(q)
        q_id += 1

    return questions, q_id

if __name__ == "__main__":
    qs, last_id = generate_s3_questions(1)
    print(f"Generated {len(qs)} questions for Subject 3. Last ID: {last_id}")
