"""
Module by module MCQ generator for:
- Subject 4: Web and Mobile Application Development (2015114)
- Subject 5: User Experience Design with VR (2015115)
"""

def generate_s4_questions(start_id):
    # Subject 4: Web and Mobile Application Development (2015114)
    s_name = "Web and Mobile Application Development"
    s_code = "2015114"
    q_id = start_id
    questions = []

    # S4 M1: Core Web and Mobile Development Concepts
    m1_name = "Module I - Core Web and Mobile Development Concepts"
    s4_m1 = [
        {
            "topic": "REST APIs",
            "question": "Which HTTP method should be used for an idempotent operation that replaces an entire existing user resource at `/api/users/42`?",
            "option_a": "PUT",
            "option_b": "POST",
            "option_c": "PATCH",
            "option_d": "CONNECT",
            "answer": "A",
            "explanation": "PUT is idempotent and replaces the target resource completely. POST is non-idempotent (creates new resource), while PATCH applies partial modifications.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "MVC",
            "question": "In the Model-View-Controller (MVC) architectural pattern, what is the specific responsibility of the Controller?",
            "option_a": "It processes incoming user requests, manipulates Model state, and selects the appropriate View to render in response",
            "option_b": "It renders raw HTML and CSS styling directly in the browser DOM",
            "option_c": "It stores database tables and executes physical disk I/O queries",
            "option_d": "It provides hardware graphics acceleration drivers for the GPU",
            "answer": "A",
            "explanation": "The Controller acts as the intermediary: handling HTTP requests/user input, invoking business logic on the Model, and returning the updated View.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Progressive Web Apps",
            "question": "What core component allows a Progressive Web App (PWA) to function offline, intercept network requests, and manage background synchronization?",
            "option_a": "Service Worker (running in a background worker thread separate from the webpage)",
            "option_b": "WebAssembly C++ compiler",
            "option_c": "Canvas 2D rendering context",
            "option_d": "CSS Grid layout engine",
            "answer": "A",
            "explanation": "A Service Worker is a client-side programmable network proxy that intercepts requests, serves cached assets offline via Cache API, and handles push notifications.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "MERN",
            "question": "What technologies constitute the full-stack MERN software stack?",
            "option_a": "MongoDB, Express.js, React, Node.js",
            "option_b": "MySQL, Ember.js, Ruby, Nginx",
            "option_c": "MariaDB, Elixir, React, Next.js",
            "option_d": "Memcached, Erlang, Redis, Neo4j",
            "answer": "A",
            "explanation": "MERN stack: MongoDB (document database), Express.js (backend web framework), React (frontend library), and Node.js (JavaScript runtime engine).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "MVVM",
            "question": "In modern mobile frameworks (such as Android Jetpack and Flutter), what is the key advantage of the Model-View-ViewModel (MVVM) pattern over MVC?",
            "option_a": "The ViewModel exposes observable data streams without holding references to UI Views, surviving configuration changes (like screen rotation) and decoupling UI logic",
            "option_b": "The ViewModel directly executes raw SQL queries inside the UI thread",
            "option_c": "MVVM eliminates the need for data models completely",
            "option_d": "The View can only be written in XML format",
            "answer": "A",
            "explanation": "In MVVM, the ViewModel prepares data for the View via two-way data binding or reactive streams (LiveData/Flow/State), decoupling business state from fragile UI lifecycles.",
            "difficulty": "medium",
            "question_type": "comparison"
        },
        {
            "topic": "Architectural principles",
            "question": "According to Roy Fielding's architectural constraints for REST, what does the 'Stateless' constraint mandate?",
            "option_a": "Every client request to the server must contain all information necessary to understand and process the request, with no session context stored on the server",
            "option_b": "The server must never write any records to persistent database storage",
            "option_c": "The client must re-render the entire web page on every millisecond",
            "option_d": "All responses must have HTTP status code 200 regardless of errors",
            "answer": "A",
            "explanation": "Statelessness requires that no client session context is stored on the server between requests. Session state is kept entirely on the client (e.g. via JWT tokens).",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "MEAN",
            "question": "How does the MEAN stack differ from the MERN stack?",
            "option_a": "MEAN uses Angular as its frontend single-page application framework, whereas MERN uses React",
            "option_b": "MEAN uses MySQL whereas MERN uses MongoDB",
            "option_c": "MEAN uses Apache HTTP Server instead of Node.js",
            "option_d": "MEAN can only run on Linux while MERN only runs on Windows",
            "answer": "A",
            "explanation": "MEAN stands for MongoDB, Express.js, Angular, and Node.js; MERN swaps Angular for React.",
            "difficulty": "easy",
            "question_type": "comparison"
        },
        {
            "topic": "PERN",
            "question": "In the PERN stack, which database management system replaces MongoDB?",
            "option_a": "PostgreSQL (a relational, ACID-compliant object-relational SQL database)",
            "option_b": "Percona Server for MySQL",
            "option_c": "PouchDB local browser database",
            "option_d": "Prometheus time-series database",
            "answer": "A",
            "explanation": "PERN stack consists of PostgreSQL, Express.js, React, and Node.js.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "API architectures",
            "question": "When comparing GraphQL with REST API architecture, what primary problem does GraphQL resolve for mobile clients with limited network bandwidth?",
            "option_a": "Over-fetching (receiving unneeded fields) and Under-fetching (requiring multiple waterfall roundtrips to fetch nested relational data)",
            "option_b": "GraphQL eliminates the need for any backend server",
            "option_c": "GraphQL encrypts data using quantum cryptography",
            "option_d": "REST APIs cannot transfer JSON payloads",
            "answer": "A",
            "explanation": "GraphQL allows clients to request exact fields in a single query document, avoiding over-fetching unnecessary payload fields and under-fetching multiple endpoints.",
            "difficulty": "medium",
            "question_type": "comparison"
        },
        {
            "topic": "Progressive Web Apps",
            "question": "Which configuration file in a PWA provides metadata (such as application name, icons, start_url, theme_color, and display mode) to allow users to install the app to their home screen?",
            "option_a": "Web App Manifest (`manifest.json`)",
            "option_b": "package.json",
            "option_c": "docker-compose.yml",
            "option_d": "tsconfig.json",
            "answer": "A",
            "explanation": "The Web App Manifest (`manifest.json` or `manifest.webmanifest`) tells browsers how the PWA should behave when installed as a native-like standalone application.",
            "difficulty": "easy",
            "question_type": "conceptual"
        }
    ]
    for q in s4_m1:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m1_name, "module_number": 1})
        questions.append(q)
        q_id += 1

    # S4 M2: Front-End Development with React
    m2_name = "Module II - Front-End Development with React"
    s4_m2 = [
        {
            "topic": "Hooks",
            "question": "In React 18, what is the purpose of the `useEffect` hook and what does returning a function from within `useEffect` achieve?",
            "option_a": "It performs side effects (data fetching, subscriptions, DOM mutations); the returned function executes as a cleanup phase when the component unmounts or before re-running the effect",
            "option_b": "It replaces the HTML `<head>` tag with custom script tags",
            "option_c": "It forces synchronous blocking rendering across all components",
            "option_d": "It converts functional components into legacy class components",
            "answer": "A",
            "explanation": "`useEffect(setup, dependencies)` runs asynchronous side effects after paint. Returning a cleanup function allows canceling timers, aborting fetch controllers, or removing event listeners.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "JSX",
            "question": "In React JSX, why must all adjacent elements returned by a component be wrapped in a single parent tag or a Fragment `<>...</>`?",
            "option_a": "Because JSX transpiles to `React.createElement(...)` JavaScript function calls, and a function can only return a single expression/object",
            "option_b": "Because HTML standards prohibit more than one paragraph tag on a web page",
            "option_c": "Because browser CSS engines crash when rendering multiple siblings",
            "option_d": "Because React does not support virtual DOM trees",
            "answer": "A",
            "explanation": "JSX is syntactic sugar for `React.createElement(type, props, ...children)`. A JavaScript return statement can only return a single value, necessitating a enclosing wrapper or `<React.Fragment>`.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Redux",
            "question": "What are the three core principles of Redux state management?",
            "option_a": "1. Single source of truth (one store), 2. State is read-only (changed only by dispatching actions), 3. Changes are made with pure functions (reducers)",
            "option_b": "1. Multiple mutable stores, 2. Direct state mutation, 3. Asynchronous reducers",
            "option_c": "1. Server-side state only, 2. No actions, 3. No reducers",
            "option_d": "1. CSS styling store, 2. DOM element cache, 3. Web worker bridge",
            "answer": "A",
            "explanation": "Redux principles: Single state tree object, immutable state altered strictly by dispatched action objects `{ type, payload }`, and pure reducer functions `(state, action) => newState`.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Data flow",
            "question": "What is meant by 'Unidirectional Data Flow' in React component architecture?",
            "option_a": "Data (state) flows strictly downward from parent to child components via props, and children notify parents of changes by invoking callback functions passed down as props",
            "option_b": "Data flows randomly in all directions through direct global variable mutation",
            "option_c": "Child components automatically overwrite parent component state directly",
            "option_d": "Data can only flow from right to left across browser pixels",
            "answer": "A",
            "explanation": "React enforces top-down (unidirectional) data flow: parents pass props down, and events bubble up via callback handlers, ensuring predictable state transitions and easy debugging.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Refs",
            "question": "When should the `useRef` hook be utilized in React instead of `useState`?",
            "option_a": "When storing a mutable value that persists across renders without triggering a component re-render when mutated (such as accessing direct DOM nodes or timer IDs)",
            "option_b": "When you want the component to immediately re-render on every keystroke",
            "option_c": "When defining global CSS styling variables",
            "option_d": "When executing Redux action creators",
            "answer": "A",
            "explanation": "`useRef(initialValue)` returns a persistent mutable object `{ current: value }`. Mutating `.current` does not trigger a re-render, making it ideal for DOM references and timers.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "React portals",
            "question": "What is the primary use case for `ReactDOM.createPortal(child, container)` in React application development?",
            "option_a": "Rendering a child component into a different DOM node outside the parent component's DOM hierarchy, ideal for modal dialogs, tooltips, and floating menus",
            "option_b": "Transferring React state directly to backend server memory",
            "option_c": "Creating multi-threaded background WebAssembly workers",
            "option_d": "Compiling JSX into native Android Kotlin bytecode",
            "answer": "A",
            "explanation": "Portals allow rendering modals, tooltips, or overlays directly into `document.body` or `#modal-root`, preventing parent CSS `overflow: hidden` or `z-index` clipping.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Error boundaries",
            "question": "How do React Error Boundaries handle runtime JavaScript errors in child component trees?",
            "option_a": "Class components implementing `componentDidCatch` or `static getDerivedStateFromError` catch render errors, log telemetry, and display a fallback UI without crashing the whole app",
            "option_b": "They automatically restart the client computer operating system",
            "option_c": "They silently ignore all network errors without logging",
            "option_d": "They delete the corrupted component from the Git repository",
            "answer": "A",
            "explanation": "Error boundaries catch JavaScript errors anywhere in their child component tree during rendering, lifecycle methods, and constructors, gracefully displaying a fallback UI.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "React DevTools",
            "question": "What primary capabilities do React DevTools provide inside browser inspection panels?",
            "option_a": "Inspecting the live React component hierarchy tree, viewing/editing current Props and State in real-time, and profiling component render performance/re-render causes",
            "option_b": "Editing backend SQL database schema tables directly",
            "option_c": "Generating native iOS IPA binary packages",
            "option_d": "Managing AWS cloud Kubernetes node pools",
            "answer": "A",
            "explanation": "React DevTools extension provides 'Components' tab (inspecting props, state, hooks) and 'Profiler' tab (measuring render times, identifying flamegraphs and wasteful re-renders).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Routing",
            "question": "In React Router v6, how is dynamic route matching configured for a profile page with user ID?",
            "option_a": "`<Route path=\"/user/:id\" element={<UserProfile />} />` and accessed via `const { id } = useParams()`",
            "option_b": "`<Route path=\"/user/?id\" component=\"UserProfile\" />`",
            "option_c": "`<Route url=\"/user/id\" render=\"UserProfile()\" />`",
            "option_d": "`<Route href=\"/user/*\" action=\"open()\" />`",
            "answer": "A",
            "explanation": "React Router v6 uses `<Route path=\"/user/:id\" element={<UserProfile />} />` where `:id` creates a dynamic URL parameter extracted inside the component with the `useParams()` hook.",
            "difficulty": "easy",
            "question_type": "code_debugging"
        },
        {
            "topic": "Accessibility",
            "question": "In accessible front-end development (a11y), what is the purpose of ARIA attributes such as `aria-label`, `aria-expanded`, and `role=\"dialog\"`?",
            "option_a": "To provide semantic assistive technology metadata to screen readers for interactive elements that lack native HTML semantic equivalents",
            "option_b": "To apply high-contrast CSS gradients automatically",
            "option_c": "To speed up JavaScript execution on mobile devices",
            "option_d": "To encrypt user passwords in the DOM tree",
            "answer": "A",
            "explanation": "Accessible Rich Internet Applications (ARIA) attributes convey roles, states, and properties to assistive technologies (screen readers), making dynamic web apps accessible.",
            "difficulty": "easy",
            "question_type": "conceptual"
        }
    ]
    for q in s4_m2:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m2_name, "module_number": 2})
        questions.append(q)
        q_id += 1

    # S4 M3: Kotlin Core
    m3_name = "Module III - Kotlin Core"
    s4_m3 = [
        {
            "topic": "Null safety",
            "question": "In Kotlin, given a nullable string `val name: String? = null`, which safe call or Elvis operator expression safely provides a default value of 'Guest' without causing a NullPointerException?",
            "option_a": "`val displayName = name ?: \"Guest\"`",
            "option_b": "`val displayName = name!!.toUpperCase()`",
            "option_c": "`val displayName = name.length`",
            "option_d": "`val displayName = (String) name`",
            "answer": "A",
            "explanation": "The Elvis operator `?:` evaluates the left-hand expression and returns it if non-null; if null, it evaluates and returns the right-hand fallback expression (\"Guest\").",
            "difficulty": "easy",
            "question_type": "code_debugging"
        },
        {
            "topic": "Data classes",
            "question": "What standard utility functions does the Kotlin compiler automatically generate for a `data class User(val id: Int, val name: String)`?",
            "option_a": "`equals()`, `hashCode()`, `toString()`, `copy()`, and `componentN()` functions for destructuring declarations",
            "option_b": "Only a default zero-argument constructor",
            "option_c": "Thread synchronization locks and mutexes",
            "option_d": "REST API controller endpoints",
            "answer": "A",
            "explanation": "Declaring a `data class` instructs Kotlin to synthesize `equals()`/`hashCode()` based on properties, `toString()`, `component1()...componentN()`, and a `copy()` method.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Extensions",
            "question": "How does Kotlin define an Extension Function that adds a `isEven()` method to the built-in `Int` class without modifying its source code?",
            "option_a": "`fun Int.isEven(): Boolean = this % 2 == 0`",
            "option_b": "`def Int::isEven() { return self % 2 == 0 }`",
            "option_c": "`extend class Int { bool isEven() { return true; } }`",
            "option_d": "`fun isEven(Int): Boolean = true`",
            "answer": "A",
            "explanation": "Kotlin extension function syntax prefixes the function name with the receiver type: `fun <ReceiverType>.<methodName>(params): ReturnType`, accessible via `this`.",
            "difficulty": "medium",
            "question_type": "code_debugging"
        },
        {
            "topic": "Kotlin basics",
            "question": "What is the difference between `val` and `var` in Kotlin variable declarations?",
            "option_a": "`val` defines an immutable (read-only) reference that cannot be reassigned once initialized; `var` defines a mutable variable that can be reassigned",
            "option_b": "`val` is for numeric types while `var` is for strings",
            "option_c": "`val` variables are destroyed immediately after execution of the line",
            "option_d": "`var` constants are evaluated at compile-time exclusively",
            "answer": "A",
            "explanation": "`val` (value) is read-only (equivalent to Java `final`); `var` (variable) is mutable and allows subsequent reassignments of matching type.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "reduce",
            "question": "What is the output of the following Kotlin code snippet?\n`val numbers = listOf(1, 2, 3, 4)\nval result = numbers.fold(10) { acc, num -> acc + num }`",
            "option_a": "20",
            "option_b": "10",
            "option_c": "24",
            "option_d": "14",
            "answer": "A",
            "explanation": "`fold(initial)` takes initial value (10) and accumulates: 10 + 1 = 11; 11 + 2 = 13; 13 + 3 = 16; 16 + 4 = 20.",
            "difficulty": "medium",
            "question_type": "output_based"
        },
        {
            "topic": "Generics",
            "question": "In Kotlin generics, what is the purpose of declaration-site covariance using the `out` modifier (`interface Source<out T>`)?",
            "option_a": "It indicates that `T` is only produced (returned) by members of `Source`, allowing `Source<String>` to safely be a subtype of `Source<Any>`",
            "option_b": "It allows `T` to be used as a parameter type in public setter functions",
            "option_c": "It forces `T` to be an integer type",
            "option_d": "It disables compile-time type checking",
            "answer": "A",
            "explanation": "Declaration-site covariance (`out T`) ensures type parameter T is in 'out' position (produced, not consumed), making `Source<Derived>` a subtype of `Source<Base>`.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "Java interoperability",
            "question": "How does Kotlin achieve 100% two-way interoperability with existing Java code and libraries on the JVM?",
            "option_a": "Kotlin compiles directly to standard Java bytecode (.class files) executing on standard JVM runtimes, allowing seamless calling of Java from Kotlin and Kotlin from Java",
            "option_b": "By embedding a C++ Python bridge emulator inside every class",
            "option_c": "By transpiling all Java libraries into raw JavaScript",
            "option_d": "By converting Java code into machine assembly code before execution",
            "answer": "A",
            "explanation": "Kotlin targets the JVM bytecode specification directly, using standard Java collections and reflection, allowing developers to call existing Java frameworks (Spring, Android SDK) natively.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Objects",
            "question": "In Kotlin, how is the Singleton design pattern natively implemented without boilerplate synchronized methods?",
            "option_a": "By using the `object` declaration keyword (e.g. `object DatabaseManager { ... }`)",
            "option_b": "By creating a `class` with a private constructor and a static instance field",
            "option_c": "By annotating a function with `@Singleton`",
            "option_d": "By declaring variables as `global var`",
            "answer": "A",
            "explanation": "Kotlin's `object` declaration defines a thread-safe, lazily instantiated singleton natively in a single statement without requiring double-checked locking boilerplate.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Operator overloading",
            "question": "In Kotlin, what keyword is required in front of a member or extension function definition to overload an arithmetic operator (such as `+` for `plus()`)?",
            "option_a": "`operator` (e.g. `operator fun plus(other: Point): Point`)",
            "option_b": "`override`",
            "option_c": "`infix`",
            "option_d": "`inline`",
            "answer": "A",
            "explanation": "Kotlin requires the `operator` modifier for predefined member or extension function names (e.g. `plus`, `minus`, `times`, `compareTo`, `get`, `set`) to enable operator syntax.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "map",
            "question": "Given the Kotlin snippet:\n`val list = listOf(\"apple\", \"banana\", \"cherry\")\nval result = list.filter { it.startsWith(\"b\") }.map { it.uppercase() }`\nWhat is `result`?",
            "option_a": "`[\"BANANA\"]`",
            "option_b": "`[\"APPLE\", \"BANANA\", \"CHERRY\"]`",
            "option_c": "`[\"banana\"]`",
            "option_d": "`[]`",
            "answer": "A",
            "explanation": "`filter { it.startsWith(\"b\") }` retains only `\"banana\"`, and `.map { it.uppercase() }` converts it to `\"BANANA\"`.",
            "difficulty": "easy",
            "question_type": "output_based"
        }
    ]
    for q in s4_m3:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m3_name, "module_number": 3})
        questions.append(q)
        q_id += 1

    # S4 M4: Kotlin Backend & Advanced Kotlin
    m4_name = "Module IV - Kotlin Backend & Advanced Kotlin"
    s4_m4 = [
        {
            "topic": "Coroutines",
            "question": "How do Kotlin Coroutines achieve non-blocking asynchronous concurrency without the heavy thread overhead of OS-level threads?",
            "option_a": "Through 'suspend' functions that yield execution and save state at suspension points without blocking the underlying carrier thread, resuming when asynchronous I/O completes",
            "option_b": "By spawning 10,000 physical operating system kernel threads concurrently",
            "option_c": "By running all tasks in a single synchronous blocking loop",
            "option_d": "By converting Kotlin code into separate operating system processes",
            "answer": "A",
            "explanation": "Coroutines are light-weight cooperative threads. Suspend functions compile to state machines that suspend execution without blocking the underlying thread, enabling millions of concurrent jobs.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "JWT",
            "question": "In a Spring Boot Kotlin backend with OAuth2/JWT security, what are the three dot-separated Base64Url-encoded parts of a JSON Web Token?",
            "option_a": "Header (algorithm & token type) . Payload (claims & expiration) . Signature (cryptographic verification hash)",
            "option_b": "Username . Password . DatabaseName",
            "option_c": "PublicKey . PrivateKey . Certificate",
            "option_d": "IPAddress . MACAddress . PortNumber",
            "answer": "A",
            "explanation": "A JWT comprises: Header (e.g. `{\"alg\":\"HS256\",\"typ\":\"JWT\"}`), Payload (claims like `sub`, `exp`, `roles`), and Signature (`HMACSHA256(header + \".\" + payload, secret)`).",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Spring Boot",
            "question": "In Spring Boot with Spring Data JPA in Kotlin, which annotation defines an entity class that maps to a relational database table?",
            "option_a": "`@Entity` and `@Table(name = \"users\")`",
            "option_b": "`@RestController`",
            "option_c": "`@Service`",
            "option_d": "`@Configuration`",
            "answer": "A",
            "explanation": "Jakarta/JPA persistence annotations `@Entity` and `@Table` declare that the class maps to a database table, with `@Id` specifying the primary key.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Jetpack Compose",
            "question": "What is the declarative UI paradigm of Android Jetpack Compose compared to legacy XML-based View layouts?",
            "option_a": "UI is described as pure Kotlin `@Composable` functions that emit UI hierarchies based on current state, automatically recomposing when observable state changes",
            "option_b": "UI is designed strictly using drag-and-drop XML visual designers",
            "option_c": "Jetpack Compose requires rendering web views inside native activities",
            "option_d": "Jetpack Compose can only display static images without animations",
            "answer": "A",
            "explanation": "Jetpack Compose is Android's modern declarative UI toolkit. Developers describe what the UI should look like for a given state; Compose handles UI updates via intelligent recomposition.",
            "difficulty": "medium",
            "question_type": "comparison"
        },
        {
            "topic": "Ktor",
            "question": "What is Ktor in the Kotlin ecosystem?",
            "option_a": "An asynchronous, lightweight web framework built from the ground up by JetBrains using Kotlin Coroutines for building connected microservices and HTTP clients",
            "option_b": "A relational database management engine written in C",
            "option_c": "An Android emulator hardware plugin",
            "option_d": "A CSS preprocessor for WebPack",
            "answer": "A",
            "explanation": "Ktor is a 100% Kotlin-native framework for building asynchronous servers and microservices, using coroutines for I/O and concise Kotlin DSLs for routing and plugins.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Kotlin Multiplatform",
            "question": "What is the core architectural philosophy of Kotlin Multiplatform (KMP) for cross-platform software engineering?",
            "option_a": "Share business logic, networking, data caching, and domain models across Android, iOS, Web, and Desktop while retaining 100% native UI performance on each platform",
            "option_b": "Run a single webview container across all operating systems",
            "option_c": "Recompile iOS Objective-C code into Android Dalvik bytecode",
            "option_d": "Force all mobile platforms to use identical XML UI layouts",
            "answer": "A",
            "explanation": "KMP allows sharing common logic (networking, serialization, business rules) across iOS, Android, Desktop, and Backend while leveraging native UI toolkits (SwiftUI for iOS, Jetpack Compose for Android).",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "DSL",
            "question": "What Kotlin language features combine to enable the creation of type-safe Domain Specific Languages (DSLs) like HTML builders or routing trees?",
            "option_a": "Lambdas with receivers (function literals with receiver), Extension functions, and Infix notation",
            "option_b": "Static global variables and C-style macros",
            "option_c": "Raw pointer arithmetic and memory offsets",
            "option_d": "XML parsing schemas and DOM serializers",
            "answer": "A",
            "explanation": "Higher-order functions with receiver types (e.g. `init: HTML.() -> Unit`) allow method calls inside the lambda to implicitly resolve against the receiver, producing elegant builder DSLs.",
            "difficulty": "hard",
            "question_type": "conceptual"
        },
        {
            "topic": "RBAC",
            "question": "In Role-Based Access Control (RBAC) configured in Spring Security with Kotlin, which annotation method-level secures an endpoint so only users with role 'ADMIN' can invoke it?",
            "option_a": "`@PreAuthorize(\"hasRole('ADMIN')\")`",
            "option_b": "`@PublicAccess`",
            "option_c": "`@EncryptPayload`",
            "option_d": "`@Cacheable`",
            "answer": "A",
            "explanation": "`@PreAuthorize(\"hasRole('ADMIN')\")` evaluates Spring Expression Language (SpEL) before method execution, blocking unauthorized access with HTTP 403 Forbidden.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Microservices",
            "question": "When designing a Kotlin microservice communicating with another service asynchronously, which messaging system pattern avoids distributed transaction deadlocks?",
            "option_a": "The Saga Pattern using message brokers (such as Apache Kafka or RabbitMQ) with compensating transactions",
            "option_b": "Two-Phase Commit (2PC) over synchronous blocking HTTP calls across 50 nodes",
            "option_c": "Directly sharing a single monolithic MySQL database table among all services",
            "option_d": "Polling flat log files via FTP every 24 hours",
            "answer": "A",
            "explanation": "Saga pattern manages distributed transactions across independent microservices via choreographed or orchestrated asynchronous events, using compensating actions for rollbacks.",
            "difficulty": "hard",
            "question_type": "architecture"
        },
        {
            "topic": "Annotations",
            "question": "In Kotlin reflection and annotation processing, what does `@Target(AnnotationTarget.CLASS, AnnotationTarget.FUNCTION)` specify?",
            "option_a": "It restricts the custom annotation so it can only be applied to class definitions and function definitions",
            "option_b": "It compiles the annotated class into machine assembly code",
            "option_c": "It forces the annotated function to execute on a background thread",
            "option_d": "It makes the class visible only to test source sets",
            "answer": "A",
            "explanation": "The `@Target` meta-annotation defines the valid targets (classes, functions, fields, parameters, etc.) to which the custom annotation can be applied.",
            "difficulty": "easy",
            "question_type": "conceptual"
        }
    ]
    for q in s4_m4:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m4_name, "module_number": 4})
        questions.append(q)
        q_id += 1

    # S4 M5: Flutter & Dart
    m5_name = "Module V - Flutter & Dart"
    s4_m5 = [
        {
            "topic": "Flutter architecture",
            "question": "How does Flutter's rendering architecture differ fundamentally from hybrid webview frameworks (Cordova) and bridge-based frameworks (React Native)?",
            "option_a": "Flutter uses its own high-performance C++ graphics engine (Impeller/Skia) to draw every UI pixel directly onto the screen canvas, bypassing OEM platform widgets and JS bridges",
            "option_b": "Flutter converts Dart code into HTML/CSS rendered inside a hidden Safari/Chrome webview",
            "option_c": "Flutter uses a JavaScript-to-Java asynchronous bridge for every button click",
            "option_d": "Flutter can only render static bitmap pictures",
            "answer": "A",
            "explanation": "Flutter renders its own widget tree directly via its graphics engine (Impeller/Skia) down to GPU textures, eliminating the performance bottleneck of JavaScript-native bridges.",
            "difficulty": "medium",
            "question_type": "architecture"
        },
        {
            "topic": "Widgets",
            "question": "In Flutter, what is the core architectural difference between a `StatelessWidget` and a `StatefulWidget`?",
            "option_a": "A `StatelessWidget` is immutable and only depends on its configuration; a `StatefulWidget` maintains a mutable `State` object that triggers UI rebuilds via `setState()`",
            "option_b": "A `StatelessWidget` can only display text while a `StatefulWidget` can only display images",
            "option_c": "`StatelessWidget` runs on the backend server while `StatefulWidget` runs in the browser",
            "option_d": "`StatefulWidget` cannot contain any child widgets",
            "answer": "A",
            "explanation": "Stateless widgets have no internal mutable state. Stateful widgets pair with a `State<T>` object where calling `setState(() { ... })` schedules a rebuild of the widget's subtree.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Async/Await",
            "question": "In Dart, what return type must be declared on an `async` function that eventually returns an integer value?",
            "option_a": "`Future<int>`",
            "option_b": "`int`",
            "option_c": "`Stream<int>`",
            "option_d": "`void`",
            "answer": "A",
            "explanation": "Any Dart function marked `async` wraps its computed result in a `Future<T>`. A function returning an integer asynchronously must declare return type `Future<int>`.",
            "difficulty": "easy",
            "question_type": "code_debugging"
        },
        {
            "topic": "Streams",
            "question": "In Dart and Flutter reactive programming, what is the difference between a `Future` and a `Stream`?",
            "option_a": "A `Future` delivers a single asynchronous value (or error) once in the future; a `Stream` is an asynchronous sequence of multiple data events emitted over time",
            "option_b": "A `Stream` can only transmit raw text strings",
            "option_c": "A `Future` requires a dedicated physical thread for every invocation",
            "option_d": "A `Stream` is strictly synchronous and blocks the UI thread",
            "answer": "A",
            "explanation": "`Future` represents a single upcoming value (like a Promise); `Stream` provides an asynchronous sequence of data events (e.g. continuous sensor readings, chat messages).",
            "difficulty": "medium",
            "question_type": "comparison"
        },
        {
            "topic": "State management",
            "question": "In Flutter state management patterns (Provider, Riverpod, BLoC), what problem does state management solve compared to passing callbacks through widget constructors?",
            "option_a": "It avoids 'prop drilling' through deep widget trees, separating business logic from UI and enabling selective rebuilding of only the specific widgets that depend on updated state",
            "option_b": "It compiles Dart code into native C++ binaries",
            "option_c": "It provides automated cloud database backup",
            "option_d": "It replaces the Flutter layout engine with CSS Flexbox",
            "answer": "A",
            "explanation": "State management decouples business state from widget hierarchy, avoiding passing state down 15 levels of widget constructors and preventing unnecessary top-level rebuilds.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Navigation",
            "question": "In Flutter 3, what is the standard method to navigate to a new screen using Navigator 1.0 imperative API?",
            "option_a": "`Navigator.push(context, MaterialPageRoute(builder: (context) => DetailScreen()));`",
            "option_b": "`window.location.href = '/details';`",
            "option_c": "`Intent intent = new Intent(this, DetailScreen.class);`",
            "option_d": "`Route.open(DetailScreen);`",
            "answer": "A",
            "explanation": "`Navigator.push()` pushes a route onto the Navigator's history stack using `MaterialPageRoute`, which provides standard Android/iOS page transition animations.",
            "difficulty": "easy",
            "question_type": "code_debugging"
        },
        {
            "topic": "Layouts",
            "question": "In Flutter layout rules, what is the golden rule governing how widgets compute their size and position?",
            "option_a": "Constraints go down; Sizes go up; Parent sets position",
            "option_b": "Sizes go down; Constraints go up; Child sets position",
            "option_c": "Every widget chooses its own absolute pixel coordinates independently",
            "option_d": "All widgets must have a fixed width of 300 pixels",
            "answer": "A",
            "explanation": "Flutter layout mantra: Parent passes BoxConstraints (min/max width/height) down to Child; Child determines its own Size within constraints and reports up; Parent positions Child.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Dart",
            "question": "In Dart language syntax, what is the meaning of prefixing an identifier with an underscore `_` (e.g. `class _PrivateHelper` or `int _count`)?",
            "option_a": "The identifier is private to its defining library (file), providing file-level encapsulation",
            "option_b": "The variable is a global constant accessible across all files",
            "option_c": "The variable is stored in flash memory rather than RAM",
            "option_d": "The identifier is a deprecated compiler keyword",
            "answer": "A",
            "explanation": "Dart does not have `public`, `private`, or `protected` keywords. Privacy is library-scoped (file-scoped) and denoted by prefixing the identifier with an underscore `_`.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Gestures",
            "question": "Which widget is commonly wrapped around any non-clickable widget in Flutter to detect user taps, double-taps, long presses, and drag gestures?",
            "option_a": "`GestureDetector` (or `InkWell` for Material ripple effects)",
            "option_b": "`Container`",
            "option_c": "`Padding`",
            "option_d": "`SizedBox`",
            "answer": "A",
            "explanation": "`GestureDetector` listens for pointer events and recognizes semantic gestures (`onTap`, `onDoubleTap`, `onLongPress`, `onPanUpdate`), while `InkWell` adds interactive ink splashes.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Build visualization",
            "question": "In Flutter, why is the `build()` method designed to be cheap, fast, and free of side-effects (like HTTP requests or database writes)?",
            "option_a": "Because the Flutter framework may invoke `build()` every frame (60fps/120fps) during animations, gestures, or layout reflows",
            "option_b": "Because the `build()` method cannot access Dart variables",
            "option_c": "Because HTTP requests can only be made from the `main()` function",
            "option_d": "Because `build()` runs exclusively on backend cloud servers",
            "answer": "A",
            "explanation": "The `build()` method must be purely functional: constructing the widget tree. Triggering side effects (network calls) inside `build()` causes infinite loops and severe frame drops.",
            "difficulty": "medium",
            "question_type": "conceptual"
        }
    ]
    for q in s4_m5:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m5_name, "module_number": 5})
        questions.append(q)
        q_id += 1

    # S4 M6: Advanced Flutter Development
    m6_name = "Module VI - Advanced Flutter Development"
    s4_m6 = [
        {
            "topic": "MediaQuery",
            "question": "In Flutter responsive design, how does a developer determine the current screen orientation and device pixel width to adapt the layout between phone and tablet?",
            "option_a": "`final size = MediaQuery.of(context).size; final isPortrait = MediaQuery.of(context).orientation == Orientation.portrait;`",
            "option_b": "`final width = System.getScreenWidth();`",
            "option_c": "`final size = Screen.dimensions();`",
            "option_d": "`final isPhone = Device.isSmall();`",
            "answer": "A",
            "explanation": "`MediaQuery.of(context)` reads the ambient `MediaQueryData` (screen size, orientation, device pixel ratio, safe area padding) to build adaptive responsive layouts.",
            "difficulty": "easy",
            "question_type": "code_debugging"
        },
        {
            "topic": "Animations",
            "question": "In Flutter explicit animations, what role does an `AnimationController` serve alongside an `Animation<double>` and a `Tween<T>`?",
            "option_a": "`AnimationController` manages the duration and playback (forward, reverse, stop); `Tween` maps the 0.0-1.0 controller progression to desired target values (e.g. Colors, Offsets)",
            "option_b": "`AnimationController` directly encodes video files to MP4 format",
            "option_c": "`Tween` is only used for playing sound effects",
            "option_d": "`AnimationController` can only animate opacity between 0 and 1",
            "answer": "A",
            "explanation": "`AnimationController` drives the animation over a specific `Duration`. A `Tween` (between) defines the interpolation range (e.g. from `Color(red)` to `Color(blue)`).",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Firebase",
            "question": "In a Flutter mobile e-commerce application using Firebase, what is the primary capability of Cloud Firestore?",
            "option_a": "A scalable, cloud-hosted NoSQL document database providing real-time data synchronization across mobile clients via WebSockets and built-in offline data caching",
            "option_b": "A relational SQL engine running on PostgreSQL",
            "option_c": "A compiler for translating Flutter to Kotlin",
            "option_d": "A physical hardware card reader driver",
            "answer": "A",
            "explanation": "Cloud Firestore organizes data into documents and collections, supporting real-time listeners (`snapshots()`), multi-platform offline persistence, and declarative security rules.",
            "difficulty": "easy",
            "question_type": "conceptual"
        },
        {
            "topic": "Custom UI",
            "question": "Which Flutter class is extended to execute low-level custom canvas drawing (such as drawing custom bezier paths, arcs, and gradients) using the `Canvas` and `Paint` objects?",
            "option_a": "`CustomPainter` (used with the `CustomPaint` widget)",
            "option_b": "`WidgetPainter`",
            "option_c": "`CanvasRenderer`",
            "option_d": "`GraphicsBuilder`",
            "answer": "A",
            "explanation": "`CustomPainter` overrides `paint(Canvas canvas, Size size)` and `shouldRepaint(covariant CustomPainter oldDelegate)`, allowing arbitrary 2D vector drawing via Skia/Impeller.",
            "difficulty": "medium",
            "question_type": "conceptual"
        },
        {
            "topic": "Flutter plugins",
            "question": "In Flutter plugin architecture, how does Flutter code communicate with native platform code (Java/Kotlin on Android, Objective-C/Swift on iOS) to access hardware features like camera or Bluetooth?",
            "option_a": "Via Platform Channels (MethodChannel for asynchronous method calls, EventChannel for event streams)",
            "option_b": "Via direct raw C memory pointer sharing across processes",
            "option_c": "Via local HTTP REST servers running inside the phone",
            "option_d": "By transpiling native SDKs into Dart source code on every build",
            "answer": "A",
            "explanation": "Platform Channels serialize messages into binary formats across the platform bridge: `MethodChannel` sends messages from Dart to native host and receives a response asynchronously.",
            "difficulty": "hard",
            "question_type": "architecture"
        },
        {
            "topic": "AI/ML API integration",
            "question": "When integrating an on-device machine learning model (such as an image classification or object detection model) in Flutter, which package is standard for executing quantized TensorFlow Lite models?",
            "option_a": "`tflite_flutter` (running native TensorFlow Lite C API on device)",
            "option_b": "`flutter_react`",
            "option_c": "`flutter_sql`",
            "option_d": "`dart_eval`",
            "answer": "A",
            "explanation": "`tflite_flutter` provides Dart bindings to the TensorFlow Lite C++ library, running hardware-accelerated (GPU/NPU) on-device ML inference with minimal latency.",
            "difficulty": "medium",
            "question_type": "application"
        },
        {
            "topic": "Lists",
            "question": "Why should `ListView.builder` be used instead of standard `ListView(children: [...])` when rendering a list of 10,000 product items in Flutter?",
            "option_a": "`ListView.builder` creates items lazily on-demand only when they scroll into the visible viewport, conserving memory and ensuring 60fps scrolling performance",
            "option_b": "`ListView(children: [...])` cannot display text widgets",
            "option_c": "`ListView.builder` automatically downloads images from cloud servers without network permissions",
            "option_d": "`ListView(children: [...])` is limited to a maximum of 10 items",
            "answer": "A",
            "explanation": "`ListView.builder` uses virtualized lazy loading: building and recycling widget rows only as they become visible on screen, preventing out-of-memory crashes for large datasets.",
            "difficulty": "easy",
            "question_type": "comparison"
        },
        {
            "topic": "Firebase Authentication",
            "question": "In Flutter Firebase Authentication, which stream listens to real-time changes in user sign-in state (login, logout, token refresh)?",
            "option_a": "`FirebaseAuth.instance.authStateChanges()`",
            "option_b": "`FirebaseAuth.instance.getUserState()`",
            "option_c": "`FirebaseAuth.instance.onLoginEvent()`",
            "option_d": "`FirebaseAuth.instance.checkStatus()`",
            "answer": "A",
            "explanation": "`authStateChanges()` emits a `User?` object whenever the user logs in or logs out, commonly consumed by a `StreamBuilder` at app root to switch between Auth and Home screens.",
            "difficulty": "easy",
            "question_type": "code_debugging"
        },
        {
            "topic": "Cloud mobile apps",
            "question": "What architecture pattern is recommended for mobile cloud apps to ensure smooth offline-first user experience during intermittent network connectivity?",
            "option_a": "Local database cache (e.g. SQLite / Hive / Isar) serving as the Single Source of Truth for the UI, with background synchronization to remote REST/GraphQL APIs",
            "option_b": "Freezing the UI screen until network connection is restored",
            "option_c": "Deleting all un-synced user data upon connection loss",
            "option_d": "Running a full Apache Web Server inside the mobile device",
            "answer": "A",
            "explanation": "Offline-first architecture caches remote data locally; UI renders from the local cache immediately while background repository sync workers reconcile changes with remote cloud APIs.",
            "difficulty": "medium",
            "question_type": "architecture"
        },
        {
            "topic": "Mobile e-commerce",
            "question": "In mobile e-commerce checkout flows, what security standard mandates that sensitive credit card details must never touch the merchant's backend server unencrypted?",
            "option_a": "PCI-DSS (Payment Card Industry Data Security Standard) utilizing client-side tokenization via payment gateways (e.g. Stripe, Razorpay SDKs)",
            "option_b": "ISO 9001 Quality Management System",
            "option_c": "IEEE 802.11 Wireless Standard",
            "option_d": "W3C HTML5 Specification",
            "answer": "A",
            "explanation": "PCI-DSS requires client-side SDK tokenization: sensitive card numbers are sent directly from the mobile app to the certified payment gateway, returning a safe ephemeral token to the app.",
            "difficulty": "medium",
            "question_type": "scenario"
        }
    ]
    for q in s4_m6:
        q.update({"id": q_id, "subject": s_name, "subject_code": s_code, "module": m6_name, "module_number": 6})
        questions.append(q)
        q_id += 1

    return questions, q_id

if __name__ == "__main__":
    qs, last_id = generate_s4_questions(1)
    print(f"Generated {len(qs)} questions for Subject 4. Last ID: {last_id}")
