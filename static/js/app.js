/**
 * QuizBank Application Logic & API Client
 * University of Mumbai T.E. Artificial Intelligence & Data Science (Sem V, 2026-27)
 */

// Global State
const state = {
    currentView: 'questions', // 'dashboard' | 'bank' | 'questions' | 'categories'
    questions: [],
    syllabus: null,
    
    // Filters for Question Bank view
    bankFilters: {
        subject: 'all',
        module: 'all',
        difficulty: 'all',
        questionType: 'all',
        searchQuery: ''
    },

    // Quiz Configuration & Session State
    quizConfig: {
        subject: 'all',
        module: 'all',
        topic: 'all',
        difficulty: 'all',
        count: '20'
    },

    isLoading: true,
    hasError: false,
    errorMessage: '',
    apiHealthy: false,
    apiPing: null,

    // Active Quiz Session
    quiz: {
        pool: [],
        currentIndex: 0,
        selectedOption: null,
        isSubmitted: false,
        score: 0,
        correctCount: 0,
        incorrectCount: 0,
        isFinished: false,
        answers: [] // { question, selected, correct, isCorrect }
    }
};

// DOM References
const DOM = {
    // Views
    viewDashboard: document.getElementById('viewDashboard'),
    viewBank: document.getElementById('viewBank'),
    viewQuestions: document.getElementById('viewQuestions'),
    viewCategories: document.getElementById('viewCategories'),
    headerBreadcrumbCurrent: document.getElementById('headerBreadcrumbCurrent'),

    // Navigation
    navDashboard: document.getElementById('navDashboard'),
    navBank: document.getElementById('navBank'),
    navQuestions: document.getElementById('navQuestions'),
    navCategories: document.getElementById('navCategories'),
    navQuestionCount: document.getElementById('navQuestionCount'),
    navBankCount: document.getElementById('navBankCount'),
    navCategoryCount: document.getElementById('navCategoryCount'),

    // Top Header
    topHeaderSearch: document.getElementById('topHeaderSearch'),
    headerApiPill: document.getElementById('headerApiPill'),

    // Dashboard Elements
    dashTotalQuestions: document.getElementById('dashTotalQuestions'),
    dashCategoriesCount: document.getElementById('dashCategoriesCount'),
    dashModulesCount: document.getElementById('dashModulesCount'),
    dashApiIconWrapper: document.getElementById('dashApiIconWrapper'),
    dashApiIcon: document.getElementById('dashApiIcon'),
    dashApiStatus: document.getElementById('dashApiStatus'),
    dashApiLatency: document.getElementById('dashApiLatency'),
    categoryMiniBars: document.getElementById('categoryMiniBars'),
    difficultyMiniBars: document.getElementById('difficultyMiniBars'),
    typeMiniBars: document.getElementById('typeMiniBars'),
    sysHealthBadge: document.getElementById('sysHealthBadge'),

    // Bank View Filters & Container
    bankSubjectFilter: document.getElementById('bankSubjectFilter'),
    bankModuleFilter: document.getElementById('bankModuleFilter'),
    bankDiffFilter: document.getElementById('bankDiffFilter'),
    bankTypeFilter: document.getElementById('bankTypeFilter'),
    bankQuestionsContainer: document.getElementById('bankQuestionsContainer'),

    // Quiz Config & Tracker
    quizSubjectSelect: document.getElementById('quizSubjectSelect'),
    quizModuleSelect: document.getElementById('quizModuleSelect'),
    quizTopicSelect: document.getElementById('quizTopicSelect'),
    quizDifficultySelect: document.getElementById('quizDifficultySelect'),
    quizCountSelect: document.getElementById('quizCountSelect'),
    quizTrackerCard: document.getElementById('quizTrackerCard'),
    quizProgressText: document.getElementById('quizProgressText'),
    quizProgressPercent: document.getElementById('quizProgressPercent'),
    quizProgressFill: document.getElementById('quizProgressFill'),
    quizScoreText: document.getElementById('quizScoreText'),
    quizCorrectCount: document.getElementById('quizCorrectCount'),
    quizIncorrectCount: document.getElementById('quizIncorrectCount'),
    quizStageContainer: document.getElementById('quizStageContainer'),
    btnRestartQuiz: document.getElementById('btnRestartQuiz'),
    btnOpenNewQuestionModal: document.getElementById('btnOpenNewQuestionModal'),

    // Categories View
    categoriesGrid: document.getElementById('categoriesGrid'),

    // Health UI
    sidebarHealthCard: document.getElementById('sidebarHealthCard'),
    healthIndicator: document.getElementById('healthIndicator'),
    healthStatusText: document.getElementById('healthStatusText'),
    healthPing: document.getElementById('healthPing'),
    refreshHealthBtn: document.getElementById('refreshHealthBtn'),

    // Create Modal
    newQuestionModal: document.getElementById('newQuestionModal'),
    closeModalBtn: document.getElementById('closeModalBtn'),
    cancelModalBtn: document.getElementById('cancelModalBtn'),
    createQuestionForm: document.getElementById('createQuestionForm'),
    modalAlertBanner: document.getElementById('modalAlertBanner'),
    modalAlertMessage: document.getElementById('modalAlertMessage'),
    btnSubmitText: document.getElementById('btnSubmitText'),
    btnSpinner: document.getElementById('btnSpinner'),
    submitQuestionBtn: document.getElementById('submitQuestionBtn'),

    // Form inputs
    inputModalSubject: document.getElementById('inputModalSubject'),
    inputModalModule: document.getElementById('inputModalModule'),
    inputModalTopic: document.getElementById('inputModalTopic'),
    topicDatalist: document.getElementById('topicDatalist'),
    selectDifficulty: document.getElementById('selectDifficulty'),
    selectQuestionType: document.getElementById('selectQuestionType'),
    inputQuestion: document.getElementById('inputQuestion'),
    inputOptionA: document.getElementById('inputOptionA'),
    inputOptionB: document.getElementById('inputOptionB'),
    inputOptionC: document.getElementById('inputOptionC'),
    inputOptionD: document.getElementById('inputOptionD'),
    selectAnswer: document.getElementById('selectAnswer'),
    inputExplanation: document.getElementById('inputExplanation'),

    // View Modal
    viewQuestionModal: document.getElementById('viewQuestionModal'),
    viewModalTitle: document.getElementById('viewModalTitle'),
    viewModalMeta: document.getElementById('viewModalMeta'),
    viewModalBody: document.getElementById('viewModalBody'),
    closeViewModalBtn: document.getElementById('closeViewModalBtn'),
    closeViewModalFooterBtn: document.getElementById('closeViewModalFooterBtn'),

    // Toasts & Mobile Sidebar
    toastContainer: document.getElementById('toastContainer'),
    sidebar: document.getElementById('sidebar'),
    sidebarOverlay: document.getElementById('sidebarOverlay'),
    mobileMenuToggle: document.getElementById('mobileMenuToggle'),
    mobileSidebarClose: document.getElementById('mobileSidebarClose')
};

/* ==========================================================================
   1. API Client Functions
   ========================================================================== */

async function fetchSyllabus() {
    try {
        const res = await fetch('/api/syllabus');
        if (res.ok) {
            state.syllabus = await res.json();
            populateSyllabusDropdowns();
        }
    } catch (e) {
        console.warn('Failed to load syllabus metadata:', e);
    }
}

async function fetchQuestions() {
    state.isLoading = true;
    state.hasError = false;

    try {
        const startTime = performance.now();
        const response = await fetch('/items', {
            method: 'GET',
            headers: { 'Accept': 'application/json' }
        });

        if (!response.ok) {
            throw new Error(`Server returned HTTP ${response.status}`);
        }

        const data = await response.json();
        state.questions = Array.isArray(data) ? data : [];
        state.isLoading = false;
        state.hasError = false;

        renderStats();
        renderDashboardView();
        renderBankView();
        renderCategoriesView();

        if (state.currentView === 'questions') {
            initializeQuiz();
        }

    } catch (err) {
        console.error('Failed to fetch questions:', err);
        state.isLoading = false;
        state.hasError = true;
        state.errorMessage = err.message || 'Unable to connect to QuizBank API';
        renderStats();
        renderDashboardView();
        renderCategoriesView();
        if (state.currentView === 'questions') {
            renderQuizError();
        }
    }
}

async function checkHealth() {
    const startTime = performance.now();
    try {
        const response = await fetch('/health');
        const latency = Math.round(performance.now() - startTime);

        if (response.ok) {
            state.apiHealthy = true;
            state.apiPing = latency;
            updateHealthUI(true, latency);
        } else {
            state.apiHealthy = false;
            state.apiPing = null;
            updateHealthUI(false);
        }
    } catch (err) {
        state.apiHealthy = false;
        state.apiPing = null;
        updateHealthUI(false);
    }
}

async function submitQuestion(payload) {
    setModalSubmitting(true);
    hideModalAlert();

    try {
        const response = await fetch('/items', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const errData = await response.json().catch(() => null);
            throw new Error((errData && errData.error) ? errData.error : `HTTP ${response.status} Failed to create question`);
        }

        setModalSubmitting(false);
        closeQuestionModal();
        showToast('Question Created', 'MCQ added to Mumbai Univ question bank.', 'success');

        await fetchQuestions();
        checkHealth();

    } catch (err) {
        console.error('Failed to submit question:', err);
        setModalSubmitting(false);
        showModalAlert(err.message || 'Failed to add question. Please ensure the backend is running.');
    }
}

/* ==========================================================================
   2. Dropdowns & Syllabus Population
   ========================================================================== */

function populateSyllabusDropdowns() {
    if (!state.syllabus || !state.syllabus.subjects) return;

    const subjects = state.syllabus.subjects;

    // 1. Bank Subject Filter
    if (DOM.bankSubjectFilter) {
        let bankSubHtml = '<option value="all">All Subjects (7)</option>';
        subjects.forEach(s => {
            bankSubHtml += `<option value="${escapeHtml(s.subject)}">${escapeHtml(s.subject)} (${s.subject_code})</option>`;
        });
        DOM.bankSubjectFilter.innerHTML = bankSubHtml;
    }

    // 2. Quiz Subject Filter
    if (DOM.quizSubjectSelect) {
        let quizSubHtml = '<option value="all">All Subjects (Comprehensive)</option>';
        subjects.forEach(s => {
            quizSubHtml += `<option value="${escapeHtml(s.subject)}">${escapeHtml(s.subject)}</option>`;
        });
        DOM.quizSubjectSelect.innerHTML = quizSubHtml;
    }

    // 3. Modal Subject Selector
    if (DOM.inputModalSubject) {
        let modalSubHtml = '<option value="" disabled selected>Select Subject</option>';
        subjects.forEach(s => {
            modalSubHtml += `<option value="${escapeHtml(s.subject)}" data-code="${s.subject_code}">${escapeHtml(s.subject)} (${s.subject_code})</option>`;
        });
        DOM.inputModalSubject.innerHTML = modalSubHtml;
    }

    updateQuizModuleDropdown();
    updateModalModuleDropdown();
}

function updateQuizModuleDropdown() {
    if (!DOM.quizModuleSelect) return;
    const selectedSubName = DOM.quizSubjectSelect ? DOM.quizSubjectSelect.value : 'all';

    let html = '<option value="all">All Modules</option>';
    if (selectedSubName !== 'all' && state.syllabus) {
        const sub = state.syllabus.subjects.find(s => s.subject === selectedSubName);
        if (sub && sub.modules) {
            sub.modules.forEach(m => {
                html += `<option value="${m.module_number}">Module ${m.module_number}: ${escapeHtml(m.module)}</option>`;
            });
        }
    }
    DOM.quizModuleSelect.innerHTML = html;
    updateQuizTopicDropdown();
}

function updateQuizTopicDropdown() {
    if (!DOM.quizTopicSelect) return;
    const selectedSubName = DOM.quizSubjectSelect ? DOM.quizSubjectSelect.value : 'all';
    const selectedModNum = DOM.quizModuleSelect ? DOM.quizModuleSelect.value : 'all';

    let html = '<option value="all">All Topics</option>';
    if (selectedSubName !== 'all' && state.syllabus) {
        const sub = state.syllabus.subjects.find(s => s.subject === selectedSubName);
        if (sub && sub.modules) {
            const modules = selectedModNum !== 'all' 
                ? sub.modules.filter(m => m.module_number === parseInt(selectedModNum))
                : sub.modules;

            const topics = new Set();
            modules.forEach(m => {
                (m.topics || []).forEach(t => topics.add(t));
            });

            Array.from(topics).sort().forEach(t => {
                html += `<option value="${escapeHtml(t)}">${escapeHtml(t)}</option>`;
            });
        }
    }
    DOM.quizTopicSelect.innerHTML = html;
}

function updateBankModuleDropdown() {
    if (!DOM.bankModuleFilter) return;
    const selectedSubName = DOM.bankSubjectFilter ? DOM.bankSubjectFilter.value : 'all';

    let html = '<option value="all">All Modules</option>';
    if (selectedSubName !== 'all' && state.syllabus) {
        const sub = state.syllabus.subjects.find(s => s.subject === selectedSubName);
        if (sub && sub.modules) {
            sub.modules.forEach(m => {
                html += `<option value="${m.module_number}">Module ${m.module_number}: ${escapeHtml(m.module)}</option>`;
            });
        }
    }
    DOM.bankModuleFilter.innerHTML = html;
}

function updateModalModuleDropdown() {
    if (!DOM.inputModalModule || !DOM.inputModalSubject) return;
    const selectedSubName = DOM.inputModalSubject.value;

    let html = '<option value="" disabled selected>Select Module</option>';
    if (selectedSubName && state.syllabus) {
        const sub = state.syllabus.subjects.find(s => s.subject === selectedSubName);
        if (sub && sub.modules) {
            sub.modules.forEach(m => {
                html += `<option value="${m.module_number}" data-name="${escapeHtml(m.module)}">Module ${m.module_number}: ${escapeHtml(m.module)}</option>`;
            });
        }
    }
    DOM.inputModalModule.innerHTML = html;
    updateModalTopicDatalist();
}

function updateModalTopicDatalist() {
    if (!DOM.topicDatalist || !DOM.inputModalSubject) return;
    const selectedSubName = DOM.inputModalSubject.value;
    const selectedModNum = DOM.inputModalModule ? DOM.inputModalModule.value : null;

    let html = '';
    if (selectedSubName && state.syllabus) {
        const sub = state.syllabus.subjects.find(s => s.subject === selectedSubName);
        if (sub && sub.modules) {
            const modules = selectedModNum 
                ? sub.modules.filter(m => m.module_number === parseInt(selectedModNum))
                : sub.modules;

            const topics = new Set();
            modules.forEach(m => {
                (m.topics || []).forEach(t => topics.add(t));
            });

            Array.from(topics).sort().forEach(t => {
                html += `<option value="${escapeHtml(t)}">`;
            });
        }
    }
    DOM.topicDatalist.innerHTML = html;
}

/* ==========================================================================
   3. SPA View Routing & Navigation
   ========================================================================== */

function navigateToView(viewName) {
    const validViews = ['dashboard', 'bank', 'questions', 'categories'];
    let target = viewName ? viewName.toLowerCase().replace('#', '') : 'questions';
    if (!validViews.includes(target)) target = 'questions';

    state.currentView = target;

    // Hide all
    DOM.viewDashboard.style.display = 'none';
    DOM.viewBank.style.display = 'none';
    DOM.viewQuestions.style.display = 'none';
    DOM.viewCategories.style.display = 'none';

    // Unset active nav
    DOM.navDashboard.classList.remove('active');
    DOM.navBank.classList.remove('active');
    DOM.navQuestions.classList.remove('active');
    DOM.navCategories.classList.remove('active');

    if (target === 'dashboard') {
        DOM.viewDashboard.style.display = 'block';
        DOM.navDashboard.classList.add('active');
        DOM.headerBreadcrumbCurrent.textContent = 'Dashboard Overview';
        renderDashboardView();
    } else if (target === 'bank') {
        DOM.viewBank.style.display = 'block';
        DOM.navBank.classList.add('active');
        DOM.headerBreadcrumbCurrent.textContent = 'Question Bank';
        renderBankView();
    } else if (target === 'categories') {
        DOM.viewCategories.style.display = 'block';
        DOM.navCategories.classList.add('active');
        DOM.headerBreadcrumbCurrent.textContent = 'Syllabus & Subjects';
        renderCategoriesView();
    } else {
        DOM.viewQuestions.style.display = 'block';
        DOM.navQuestions.classList.add('active');
        DOM.headerBreadcrumbCurrent.textContent = 'Quiz Mode';
        if (!state.isLoading && state.questions.length > 0 && state.quiz.pool.length === 0) {
            initializeQuiz();
        }
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
    lucide.createIcons();
}

/* ==========================================================================
   4. Dashboard & Stats View Renderers
   ========================================================================== */

function renderStats() {
    const total = state.questions.length;
    if (DOM.navQuestionCount) DOM.navQuestionCount.textContent = total;
    if (DOM.navBankCount) DOM.navBankCount.textContent = total;
    if (DOM.dashTotalQuestions) DOM.dashTotalQuestions.textContent = total;
}

function renderDashboardView() {
    const total = state.questions.length;
    if (DOM.dashTotalQuestions) DOM.dashTotalQuestions.textContent = total;

    // Difficulty breakdown
    if (DOM.difficultyMiniBars) {
        const diffCounts = { easy: 0, medium: 0, hard: 0 };
        state.questions.forEach(q => {
            const d = (q.difficulty || 'medium').toLowerCase();
            diffCounts[d] = (diffCounts[d] || 0) + 1;
        });

        DOM.difficultyMiniBars.innerHTML = Object.entries(diffCounts).map(([d, count]) => {
            const pct = total > 0 ? Math.round((count / total) * 100) : 0;
            return `
                <div class="mini-bar-item" style="margin-bottom: 0.6rem;">
                    <div class="mini-bar-header" style="display: flex; justify-content: space-between; font-size: 0.78rem; margin-bottom: 0.2rem;">
                        <span style="font-weight: 600; text-transform: capitalize;">${d}</span>
                        <span style="color: var(--text-muted);">${count} (${pct}%)</span>
                    </div>
                    <div class="mini-bar-track" style="height: 6px; background: var(--border-subtle); border-radius: 999px; overflow: hidden;">
                        <div class="mini-bar-fill" style="width: ${pct}%; height: 100%; background: ${d === 'easy' ? 'var(--emerald-500)' : d === 'medium' ? 'var(--amber-500)' : 'var(--rose-500)'};"></div>
                    </div>
                </div>
            `;
        }).join('');
    }

    // Question Type Breakdown
    if (DOM.typeMiniBars) {
        const typeCounts = {};
        state.questions.forEach(q => {
            const t = (q.question_type || 'conceptual').toLowerCase();
            typeCounts[t] = (typeCounts[t] || 0) + 1;
        });

        DOM.typeMiniBars.innerHTML = Object.entries(typeCounts).map(([t, count]) => {
            const pct = total > 0 ? Math.round((count / total) * 100) : 0;
            return `
                <div class="mini-bar-item" style="margin-bottom: 0.6rem;">
                    <div class="mini-bar-header" style="display: flex; justify-content: space-between; font-size: 0.78rem; margin-bottom: 0.2rem;">
                        <span style="font-weight: 600; text-transform: capitalize;">${t.replace('_', ' ')}</span>
                        <span style="color: var(--text-muted);">${count} (${pct}%)</span>
                    </div>
                    <div class="mini-bar-track" style="height: 6px; background: var(--border-subtle); border-radius: 999px; overflow: hidden;">
                        <div class="mini-bar-fill" style="width: ${pct}%; height: 100%; background: var(--primary-500);"></div>
                    </div>
                </div>
            `;
        }).join('');
    }

    // Subject Breakdown
    if (DOM.categoryMiniBars) {
        const subCounts = {};
        state.questions.forEach(q => {
            const s = q.subject || 'Other';
            subCounts[s] = (subCounts[s] || 0) + 1;
        });

        DOM.categoryMiniBars.innerHTML = Object.entries(subCounts).map(([sub, count]) => {
            const pct = total > 0 ? Math.round((count / total) * 100) : 0;
            return `
                <div class="mini-bar-item" style="margin-bottom: 0.75rem;">
                    <div class="mini-bar-header" style="display: flex; justify-content: space-between; font-size: 0.8rem; margin-bottom: 0.25rem;">
                        <span style="font-weight: 600; color: var(--text-primary);">${escapeHtml(sub)}</span>
                        <span style="color: var(--text-muted);">${count} Qs</span>
                    </div>
                    <div class="mini-bar-track" style="height: 6px; background: var(--border-subtle); border-radius: 999px; overflow: hidden;">
                        <div class="mini-bar-fill" style="width: ${pct}%; height: 100%; background: var(--primary-600);"></div>
                    </div>
                </div>
            `;
        }).join('');
    }
}

/* ==========================================================================
   5. Question Bank Explorer View
   ========================================================================== */

function renderBankView() {
    const container = DOM.bankQuestionsContainer;
    if (!container) return;

    let filtered = [...state.questions];

    // Subject filter
    const subFilter = DOM.bankSubjectFilter ? DOM.bankSubjectFilter.value : 'all';
    if (subFilter !== 'all') {
        filtered = filtered.filter(q => q.subject === subFilter);
    }

    // Module filter
    const modFilter = DOM.bankModuleFilter ? DOM.bankModuleFilter.value : 'all';
    if (modFilter !== 'all') {
        filtered = filtered.filter(q => q.module_number === parseInt(modFilter));
    }

    // Difficulty filter
    const diffFilter = DOM.bankDiffFilter ? DOM.bankDiffFilter.value : 'all';
    if (diffFilter !== 'all') {
        filtered = filtered.filter(q => (q.difficulty || '').toLowerCase() === diffFilter.toLowerCase());
    }

    // Type filter
    const typeFilter = DOM.bankTypeFilter ? DOM.bankTypeFilter.value : 'all';
    if (typeFilter !== 'all') {
        filtered = filtered.filter(q => (q.question_type || '').toLowerCase() === typeFilter.toLowerCase());
    }

    // Keyword Search Filter
    if (state.bankFilters.searchQuery) {
        const query = state.bankFilters.searchQuery.toLowerCase();
        filtered = filtered.filter(q => 
            (q.question || '').toLowerCase().includes(query) ||
            (q.topic || '').toLowerCase().includes(query) ||
            (q.subject || '').toLowerCase().includes(query) ||
            (q.explanation || '').toLowerCase().includes(query)
        );
    }

    if (filtered.length === 0) {
        container.innerHTML = `
            <div class="state-container" style="padding: 3rem 1rem; background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg);">
                <div class="state-icon-circle empty">
                    <i data-lucide="search-x"></i>
                </div>
                <h4 class="state-title">No questions found</h4>
                <p class="state-desc">No questions in the active bank match the selected filters. Try broadening your criteria.</p>
                <div class="state-actions">
                    <button class="btn btn-secondary" onclick="resetBankFilters()">
                        <i data-lucide="rotate-ccw" class="btn-icon"></i>
                        <span>Reset Filters</span>
                    </button>
                </div>
            </div>
        `;
        lucide.createIcons();
        return;
    }

    container.innerHTML = `
        <div style="font-size: 0.82rem; font-weight: 600; color: var(--text-muted); margin-bottom: 0.75rem;">
            Showing <strong>${filtered.length}</strong> of <strong>${state.questions.length}</strong> total questions
        </div>
    ` + filtered.map(q => {
        const diff = (q.difficulty || 'medium').toLowerCase();
        const qType = (q.question_type || 'conceptual').toLowerCase().replace('_', ' ');
        const subName = q.subject || 'General';
        const modName = q.module_number ? `Mod ${q.module_number}` : '';
        const topicName = q.topic || '';

        return `
            <div class="bank-q-card" onclick="openViewQuestionModalById(${q.id})">
                <div class="bank-q-header">
                    <div class="bank-q-badges">
                        <span class="badge-index">#${q.id}</span>
                        <span class="badge-subject">${escapeHtml(subName)}</span>
                        ${modName ? `<span class="badge-module">${escapeHtml(modName)}</span>` : ''}
                        ${topicName ? `<span class="badge-topic">${escapeHtml(topicName)}</span>` : ''}
                        <span class="badge-type">${escapeHtml(qType)}</span>
                        <span class="badge-difficulty ${diff}">${capitalize(diff)}</span>
                    </div>
                </div>
                <div class="bank-q-text">${escapeHtml(q.question)}</div>
                <div class="bank-q-options-preview">
                    <div class="bank-q-opt-pill ${q.answer === 'A' ? 'correct' : ''}"><strong>A:</strong> ${escapeHtml(q.option_a)}</div>
                    <div class="bank-q-opt-pill ${q.answer === 'B' ? 'correct' : ''}"><strong>B:</strong> ${escapeHtml(q.option_b)}</div>
                    <div class="bank-q-opt-pill ${q.answer === 'C' ? 'correct' : ''}"><strong>C:</strong> ${escapeHtml(q.option_c)}</div>
                    <div class="bank-q-opt-pill ${q.answer === 'D' ? 'correct' : ''}"><strong>D:</strong> ${escapeHtml(q.option_d)}</div>
                </div>
            </div>
        `;
    }).join('');

    lucide.createIcons();
}

function resetBankFilters() {
    if (DOM.bankSubjectFilter) DOM.bankSubjectFilter.value = 'all';
    if (DOM.bankModuleFilter) DOM.bankModuleFilter.value = 'all';
    if (DOM.bankDiffFilter) DOM.bankDiffFilter.value = 'all';
    if (DOM.bankTypeFilter) DOM.bankTypeFilter.value = 'all';
    if (DOM.topHeaderSearch) DOM.topHeaderSearch.value = '';
    state.bankFilters.searchQuery = '';
    renderBankView();
}

/* ==========================================================================
   6. Categories & Syllabus Explorer View
   ========================================================================== */

function renderCategoriesView() {
    const grid = DOM.categoriesGrid;
    if (!grid) return;

    if (!state.syllabus || !state.syllabus.subjects) {
        grid.innerHTML = `<div style="padding: 2rem;">Loading University of Mumbai syllabus structure...</div>`;
        return;
    }

    const categories = [
        { key: 'CORE', title: 'Core Subjects (Compulsory)', badgeClass: 'tag-core' },
        { key: 'ELECTIVE_1', title: 'Program Elective-I (Students choose 1 of 3)', badgeClass: 'tag-elective' },
        { key: 'OTHER', title: 'Other Subjects', badgeClass: 'tag-other' }
    ];

    let html = '';

    categories.forEach(cat => {
        const subjectsInCat = state.syllabus.subjects.filter(s => s.category_type === cat.key);
        if (subjectsInCat.length === 0) return;

        html += `
            <div style="grid-column: 1 / -1; margin-top: 1rem; margin-bottom: 0.5rem;">
                <h3 style="font-size: 1.15rem; font-weight: 700; color: var(--text-primary); display: flex; align-items: center; gap: 0.5rem;">
                    <span>${cat.title}</span>
                </h3>
            </div>
        `;

        subjectsInCat.forEach(s => {
            const subjectQuestions = state.questions.filter(q => q.subject === s.subject);
            const qCount = subjectQuestions.length;

            html += `
                <div class="syllabus-subject-card" style="grid-column: 1 / -1;">
                    <div class="syllabus-subject-header">
                        <div>
                            <span class="syllabus-tag-category ${cat.badgeClass}">${cat.key === 'ELECTIVE_1' ? 'Elective-I' : cat.key}</span>
                            <span style="font-size: 0.78rem; font-weight: 700; color: var(--text-muted); margin-left: 0.5rem;">Course Code: ${s.subject_code}</span>
                            <h3 style="font-size: 1.1rem; font-weight: 800; color: var(--text-primary); margin-top: 0.35rem;">${escapeHtml(s.subject)}</h3>
                        </div>
                        <div style="display: flex; gap: 0.5rem; align-items: center;">
                            <span class="cat-count-pill" style="font-size: 0.8rem; font-weight: 700;">${qCount} Questions</span>
                            <button class="btn btn-secondary btn-sm" onclick="startQuizForSubject('${escapeHtml(s.subject)}')">
                                <i data-lucide="play" class="btn-icon"></i>
                                <span>Quiz Subject</span>
                            </button>
                        </div>
                    </div>

                    <!-- Modules Grid (6 Modules) -->
                    <div class="module-grid">
                        ${s.modules.map(m => {
                            const modQuestions = subjectQuestions.filter(q => q.module_number === m.module_number);
                            return `
                                <div class="module-box">
                                    <div class="module-num-title">MODULE ${m.module_number} (${modQuestions.length} Qs)</div>
                                    <div class="module-name">${escapeHtml(m.module)}</div>
                                    <div style="font-size: 0.72rem; font-weight: 700; color: var(--text-muted); margin-top: 0.5rem;">Topics (${(m.topics || []).length}):</div>
                                    <div class="topic-tags-cloud">
                                        ${(m.topics || []).slice(0, 8).map(t => `
                                            <span class="topic-pill" onclick="startQuizForTopic('${escapeHtml(s.subject)}', ${m.module_number}, '${escapeHtml(t)}')">${escapeHtml(t)}</span>
                                        `).join('')}
                                        ${(m.topics || []).length > 8 ? `<span style="font-size: 0.7rem; color: var(--text-muted); align-self: center;">+${m.topics.length - 8} more</span>` : ''}
                                    </div>
                                </div>
                            `;
                        }).join('')}
                    </div>
                </div>
            `;
        });
    });

    grid.innerHTML = html;
    lucide.createIcons();
}

function startQuizForSubject(subjectName) {
    if (DOM.quizSubjectSelect) DOM.quizSubjectSelect.value = subjectName;
    updateQuizModuleDropdown();
    if (DOM.quizModuleSelect) DOM.quizModuleSelect.value = 'all';
    updateQuizTopicDropdown();
    window.location.hash = '#questions';
    navigateToView('questions');
    initializeQuiz();
}

function startQuizForTopic(subjectName, modNum, topicName) {
    if (DOM.quizSubjectSelect) DOM.quizSubjectSelect.value = subjectName;
    updateQuizModuleDropdown();
    if (DOM.quizModuleSelect) DOM.quizModuleSelect.value = String(modNum);
    updateQuizTopicDropdown();
    if (DOM.quizTopicSelect) DOM.quizTopicSelect.value = topicName;
    window.location.hash = '#questions';
    navigateToView('questions');
    initializeQuiz();
}

/* ==========================================================================
   7. Interactive Quiz Engine
   ========================================================================== */

function initializeQuiz() {
    const subTarget = DOM.quizSubjectSelect ? DOM.quizSubjectSelect.value : 'all';
    const modTarget = DOM.quizModuleSelect ? DOM.quizModuleSelect.value : 'all';
    const topicTarget = DOM.quizTopicSelect ? DOM.quizTopicSelect.value : 'all';
    const diffTarget = DOM.quizDifficultySelect ? DOM.quizDifficultySelect.value : 'all';
    const countTarget = DOM.quizCountSelect ? DOM.quizCountSelect.value : '20';

    let pool = [...state.questions];

    if (subTarget !== 'all') {
        pool = pool.filter(q => q.subject === subTarget);
    }
    if (modTarget !== 'all') {
        pool = pool.filter(q => q.module_number === parseInt(modTarget));
    }
    if (topicTarget !== 'all') {
        pool = pool.filter(q => (q.topic || '').toLowerCase() === topicTarget.toLowerCase());
    }
    if (diffTarget !== 'all') {
        pool = pool.filter(q => (q.difficulty || '').toLowerCase() === diffTarget.toLowerCase());
    }

    // Shuffle pool
    pool = shuffleArray(pool);

    // Limit count
    if (countTarget !== 'all') {
        const count = parseInt(countTarget);
        if (!isNaN(count) && count > 0) {
            pool = pool.slice(0, count);
        }
    }

    state.quiz = {
        pool: pool,
        currentIndex: 0,
        selectedOption: null,
        isSubmitted: false,
        score: 0,
        correctCount: 0,
        incorrectCount: 0,
        isFinished: false,
        answers: []
    };

    updateQuizTracker();
    renderQuizStage();
}

function restartQuiz() {
    initializeQuiz();
    showToast('Quiz Restarted', 'Started a new randomized exam session.', 'info');
}

function shuffleArray(array) {
    const arr = [...array];
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
}

function updateQuizTracker() {
    const quiz = state.quiz;
    const total = quiz.pool.length;
    const answered = quiz.correctCount + quiz.incorrectCount;

    if (DOM.quizProgressText) {
        DOM.quizProgressText.textContent = total > 0 
            ? `Question ${Math.min(quiz.currentIndex + 1, total)} of ${total}`
            : 'No questions configured';
    }

    const percent = total > 0 ? Math.round((answered / total) * 100) : 0;
    if (DOM.quizProgressPercent) DOM.quizProgressPercent.textContent = `${percent}%`;
    if (DOM.quizProgressFill) DOM.quizProgressFill.style.width = `${percent}%`;

    if (DOM.quizScoreText) DOM.quizScoreText.textContent = `${quiz.score} pts`;
    if (DOM.quizCorrectCount) DOM.quizCorrectCount.textContent = quiz.correctCount;
    if (DOM.quizIncorrectCount) DOM.quizIncorrectCount.textContent = quiz.incorrectCount;
}

function renderQuizStage() {
    const container = DOM.quizStageContainer;
    if (!container) return;

    const quiz = state.quiz;

    if (state.isLoading) {
        container.innerHTML = renderQuizSkeleton();
        return;
    }

    if (state.hasError) {
        renderQuizError();
        return;
    }

    if (state.questions.length === 0) {
        container.innerHTML = `
            <div class="quiz-empty-card">
                <div class="state-container">
                    <div class="state-icon-circle empty">
                        <i data-lucide="inbox"></i>
                    </div>
                    <h4 class="state-title">Question Bank is empty</h4>
                    <p class="state-desc">Create questions to begin practicing.</p>
                    <div class="state-actions">
                        <button class="btn btn-primary" onclick="openQuestionModal()">
                            <i data-lucide="plus" class="btn-icon"></i>
                            <span>Create Question</span>
                        </button>
                    </div>
                </div>
            </div>
        `;
        lucide.createIcons();
        return;
    }

    if (quiz.pool.length === 0) {
        container.innerHTML = `
            <div class="quiz-empty-card">
                <div class="state-container">
                    <div class="state-icon-circle empty">
                        <i data-lucide="search-x"></i>
                    </div>
                    <h4 class="state-title">No questions match this selection</h4>
                    <p class="state-desc">No questions found for the chosen subject/module/topic combination. Try choosing 'All Modules' or 'All Difficulties'.</p>
                    <div class="state-actions">
                        <button class="btn btn-secondary" onclick="resetQuizFilters()">
                            <i data-lucide="rotate-ccw" class="btn-icon"></i>
                            <span>Reset Syllabus Target</span>
                        </button>
                    </div>
                </div>
            </div>
        `;
        lucide.createIcons();
        return;
    }

    if (quiz.isFinished) {
        renderQuizResults();
        return;
    }

    renderQuestionPlayer();
}

function resetQuizFilters() {
    if (DOM.quizSubjectSelect) DOM.quizSubjectSelect.value = 'all';
    updateQuizModuleDropdown();
    if (DOM.quizModuleSelect) DOM.quizModuleSelect.value = 'all';
    updateQuizTopicDropdown();
    if (DOM.quizTopicSelect) DOM.quizTopicSelect.value = 'all';
    if (DOM.quizDifficultySelect) DOM.quizDifficultySelect.value = 'all';
    initializeQuiz();
}

function renderQuestionPlayer() {
    const container = DOM.quizStageContainer;
    const quiz = state.quiz;
    const q = quiz.pool[quiz.currentIndex];
    if (!q) return;

    const formattedIndex = String(quiz.currentIndex + 1).padStart(2, '0');
    const totalFormatted = String(quiz.pool.length).padStart(2, '0');
    const subject = q.subject || 'General';
    const topic = q.topic || '';
    const diff = (q.difficulty || 'Medium').toLowerCase();
    const correctAnswer = (q.answer || 'A').toUpperCase();

    const options = [
        { key: 'A', text: q.option_a || '' },
        { key: 'B', text: q.option_b || '' },
        { key: 'C', text: q.option_c || '' },
        { key: 'D', text: q.option_d || '' }
    ];

    let optionsHtml = options.map(opt => {
        let classes = 'quiz-option-btn';
        let iconHtml = '';
        let disabled = '';

        if (quiz.isSubmitted) {
            disabled = 'disabled';
            if (opt.key === correctAnswer) {
                classes += ' quiz-option-correct';
                iconHtml = '<i data-lucide="check-circle-2" class="option-feedback-icon"></i>';
            }
            if (opt.key === quiz.selectedOption && opt.key !== correctAnswer) {
                classes += ' quiz-option-wrong';
                iconHtml = '<i data-lucide="x-circle" class="option-feedback-icon"></i>';
            }
        } else {
            if (opt.key === quiz.selectedOption) {
                classes += ' quiz-option-selected';
            }
        }

        return `
            <button class="${classes}" data-option="${opt.key}" ${disabled} onclick="selectQuizOption('${opt.key}')">
                <span class="quiz-option-letter">${opt.key}</span>
                <span class="quiz-option-text">${escapeHtml(opt.text)}</span>
                ${iconHtml}
            </button>
        `;
    }).join('');

    let feedbackHtml = '';
    if (quiz.isSubmitted) {
        const isCorrect = quiz.selectedOption === correctAnswer;
        const correctOptionText = options.find(o => o.key === correctAnswer)?.text || '';
        const explanation = q.explanation || 'No detailed explanation provided.';

        feedbackHtml = `
            <div class="quiz-feedback ${isCorrect ? 'quiz-feedback-correct' : 'quiz-feedback-wrong'}">
                <div class="quiz-feedback-icon-wrap">
                    <i data-lucide="${isCorrect ? 'check-circle-2' : 'x-circle'}"></i>
                </div>
                <div class="quiz-feedback-content">
                    <div class="quiz-feedback-title">${isCorrect ? 'Correct!' : 'Incorrect'}</div>
                    <div class="quiz-feedback-desc">
                        ${!isCorrect ? `Correct Answer: <strong>Option ${correctAnswer}</strong> — ${escapeHtml(correctOptionText)}<br>` : ''}
                        <strong>Explanation:</strong> ${escapeHtml(explanation)}
                    </div>
                </div>
            </div>
        `;
    }

    const isLastQuestion = quiz.currentIndex >= quiz.pool.length - 1;
    let actionBtns = '';

    if (!quiz.isSubmitted) {
        actionBtns = `
            <button class="btn btn-primary btn-lg quiz-submit-btn" id="quizSubmitBtn"
                onclick="submitQuizAnswer()" ${!quiz.selectedOption ? 'disabled' : ''}>
                <i data-lucide="send" class="btn-icon"></i>
                <span>Submit Answer</span>
            </button>
        `;
    } else {
        actionBtns = `
            <button class="btn btn-primary btn-lg quiz-next-btn" onclick="${isLastQuestion ? 'finishQuiz()' : 'nextQuestion()'}">
                <i data-lucide="${isLastQuestion ? 'flag' : 'arrow-right'}" class="btn-icon"></i>
                <span>${isLastQuestion ? 'View Results' : 'Next Question'}</span>
            </button>
        `;
    }

    container.innerHTML = `
        <div class="quiz-player-card" style="animation: quizCardIn 350ms cubic-bezier(0.16, 1, 0.3, 1);">
            <div class="quiz-question-header">
                <div class="quiz-question-badges">
                    <span class="badge-index">#${formattedIndex} / ${totalFormatted}</span>
                    <span class="badge-subject">${escapeHtml(subject)}</span>
                    ${topic ? `<span class="badge-topic">${escapeHtml(topic)}</span>` : ''}
                    <span class="badge-difficulty ${diff}">${capitalize(diff)}</span>
                </div>
            </div>
            <h3 class="quiz-question-text">${escapeHtml(q.question)}</h3>
            <div class="quiz-options-grid">
                ${optionsHtml}
            </div>
            ${feedbackHtml}
            <div class="quiz-actions-row">
                ${actionBtns}
            </div>
        </div>
    `;

    lucide.createIcons();
}

function selectQuizOption(optKey) {
    if (state.quiz.isSubmitted) return;
    state.quiz.selectedOption = optKey;
    renderQuestionPlayer();
}

function submitQuizAnswer() {
    const quiz = state.quiz;
    if (quiz.isSubmitted || !quiz.selectedOption) return;

    const q = quiz.pool[quiz.currentIndex];
    const correctAnswer = (q.answer || 'A').toUpperCase();
    const isCorrect = quiz.selectedOption === correctAnswer;

    quiz.isSubmitted = true;

    if (isCorrect) {
        quiz.score += 10;
        quiz.correctCount += 1;
    } else {
        quiz.incorrectCount += 1;
    }

    quiz.answers.push({
        questionId: q.id,
        question: q,
        selected: quiz.selectedOption,
        correct: correctAnswer,
        isCorrect: isCorrect
    });

    updateQuizTracker();
    renderQuestionPlayer();

    if (isCorrect) {
        showToast('Correct! +10 pts', `Question ${quiz.currentIndex + 1} answered correctly.`, 'success');
    } else {
        showToast('Incorrect', `The correct answer was Option ${correctAnswer}.`, 'error');
    }
}

function nextQuestion() {
    const quiz = state.quiz;
    quiz.currentIndex += 1;
    quiz.selectedOption = null;
    quiz.isSubmitted = false;

    updateQuizTracker();
    renderQuizStage();
}

function finishQuiz() {
    state.quiz.isFinished = true;
    updateQuizTracker();
    renderQuizStage();
}

function renderQuizResults() {
    const container = DOM.quizStageContainer;
    const quiz = state.quiz;
    const total = quiz.pool.length;
    const percentage = total > 0 ? Math.round((quiz.correctCount / total) * 100) : 0;

    let gradeLabel, gradeColor, gradeIcon, gradeMessage;
    if (percentage >= 90) {
        gradeLabel = 'Outstanding';
        gradeColor = 'emerald';
        gradeIcon = 'trophy';
        gradeMessage = 'Exceptional performance! Mastered Semester V AI&DS syllabus.';
    } else if (percentage >= 70) {
        gradeLabel = 'Great Job';
        gradeColor = 'primary';
        gradeIcon = 'award';
        gradeMessage = 'Solid understanding. Review explanations below for full perfection.';
    } else if (percentage >= 50) {
        gradeLabel = 'Good Effort';
        gradeColor = 'amber';
        gradeIcon = 'target';
        gradeMessage = 'Clear foundation. Revisiting complex modules will improve score.';
    } else {
        gradeLabel = 'Keep Practicing';
        gradeColor = 'rose';
        gradeIcon = 'book-open';
        gradeMessage = 'Review module topics and attempt the quiz again.';
    }

    let reviewHtml = quiz.answers.map((ans, i) => {
        const q = ans.question;
        const icon = ans.isCorrect ? 'check-circle-2' : 'x-circle';
        const colorClass = ans.isCorrect ? 'review-correct' : 'review-wrong';
        return `
            <div class="review-row ${colorClass}" style="flex-direction: column; align-items: flex-start; gap: 0.35rem;">
                <div style="display: flex; align-items: center; gap: 0.5rem; width: 100%;">
                    <div class="review-status-icon"><i data-lucide="${icon}"></i></div>
                    <div class="review-question-text" style="flex: 1;"><strong>Q${i+1}:</strong> ${escapeHtml(q.question)}</div>
                    <div class="review-answer-info">
                        <span class="review-your-answer">Your: <strong>${ans.selected}</strong></span>
                        ${!ans.isCorrect ? `<span class="review-correct-answer">Correct: <strong>${ans.correct}</strong></span>` : ''}
                    </div>
                </div>
                <div style="font-size: 0.78rem; color: var(--text-secondary); margin-left: 1.8rem; background: var(--bg-surface); padding: 0.4rem 0.6rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle); width: calc(100% - 1.8rem);">
                    <strong>Explanation:</strong> ${escapeHtml(q.explanation || 'No explanation.')}
                </div>
            </div>
        `;
    }).join('');

    container.innerHTML = `
        <div class="quiz-results-card" style="animation: quizCardIn 400ms cubic-bezier(0.16, 1, 0.3, 1);">
            <div class="results-hero">
                <div class="results-icon-circle results-icon-${gradeColor}">
                    <i data-lucide="${gradeIcon}"></i>
                </div>
                <h2 class="results-title">${gradeLabel}</h2>
                <p class="results-subtitle">${gradeMessage}</p>
            </div>

            <div class="results-score-ring-section">
                <div class="results-ring-container">
                    <svg class="results-ring" viewBox="0 0 120 120">
                        <circle class="results-ring-bg" cx="60" cy="60" r="52" />
                        <circle class="results-ring-fill results-ring-${gradeColor}"
                            cx="60" cy="60" r="52"
                            stroke-dasharray="${Math.round(2 * Math.PI * 52)}"
                            stroke-dashoffset="${Math.round(2 * Math.PI * 52 * (1 - percentage / 100))}" />
                    </svg>
                    <div class="results-ring-label">
                        <span class="results-ring-percent">${percentage}%</span>
                        <span class="results-ring-sub">Score</span>
                    </div>
                </div>
            </div>

            <div class="results-metrics-grid">
                <div class="results-metric">
                    <div class="results-metric-icon bg-indigo-subtle"><i data-lucide="award" class="text-indigo"></i></div>
                    <div class="results-metric-info">
                        <span class="results-metric-value">${quiz.score}</span>
                        <span class="results-metric-label">Total Points</span>
                    </div>
                </div>
                <div class="results-metric">
                    <div class="results-metric-icon bg-emerald-subtle"><i data-lucide="check-circle-2" class="text-emerald"></i></div>
                    <div class="results-metric-info">
                        <span class="results-metric-value">${quiz.correctCount}</span>
                        <span class="results-metric-label">Correct</span>
                    </div>
                </div>
                <div class="results-metric">
                    <div class="results-metric-icon bg-rose-subtle"><i data-lucide="x-circle" class="text-rose"></i></div>
                    <div class="results-metric-info">
                        <span class="results-metric-value">${quiz.incorrectCount}</span>
                        <span class="results-metric-label">Incorrect</span>
                    </div>
                </div>
                <div class="results-metric">
                    <div class="results-metric-icon bg-violet-subtle"><i data-lucide="list-checks" class="text-violet"></i></div>
                    <div class="results-metric-info">
                        <span class="results-metric-value">${total}</span>
                        <span class="results-metric-label">Questions Attempted</span>
                    </div>
                </div>
            </div>

            <div class="results-actions">
                <button class="btn btn-primary btn-lg" onclick="restartQuiz()">
                    <i data-lucide="rotate-ccw" class="btn-icon"></i>
                    <span>Retry Quiz</span>
                </button>
                <button class="btn btn-secondary btn-lg" onclick="navigateToView('bank')">
                    <i data-lucide="database" class="btn-icon"></i>
                    <span>Explore Question Bank</span>
                </button>
            </div>

            ${quiz.answers.length > 0 ? `
                <div class="results-review-section">
                    <h4 class="review-section-title">
                        <i data-lucide="file-text"></i>
                        <span>Detailed Answer & Explanation Review</span>
                    </h4>
                    <div class="review-list">
                        ${reviewHtml}
                    </div>
                </div>
            ` : ''}
        </div>
    `;

    lucide.createIcons();
}

function renderQuizSkeleton() {
    return `
        <div class="quiz-player-card">
            <div class="skeleton-header" style="margin-bottom: 1rem;">
                <div class="skeleton-line skeleton-badge"></div>
            </div>
            <div class="skeleton-line skeleton-title-1" style="margin-bottom: 0.75rem;"></div>
            <div class="skeleton-line skeleton-title-2" style="margin-bottom: 1.5rem;"></div>
            <div class="skeleton-grid" style="grid-template-columns: 1fr 1fr; gap: 0.75rem;">
                <div class="skeleton-line" style="height: 64px;"></div>
                <div class="skeleton-line" style="height: 64px;"></div>
                <div class="skeleton-line" style="height: 64px;"></div>
                <div class="skeleton-line" style="height: 64px;"></div>
            </div>
        </div>
    `;
}

function renderQuizError() {
    const container = DOM.quizStageContainer;
    if (!container) return;

    container.innerHTML = `
        <div class="quiz-empty-card">
            <div class="state-container">
                <div class="state-icon-circle error">
                    <i data-lucide="wifi-off"></i>
                </div>
                <h4 class="state-title">Unable to connect to QuizBank API</h4>
                <p class="state-desc">Make sure the Flask backend server is running on port 5000 and accessible at <code>/items</code> and <code>/health</code>.</p>
                <div class="state-actions">
                    <button class="btn btn-primary" onclick="retryConnection()">
                        <i data-lucide="refresh-cw" class="btn-icon"></i>
                        <span>Retry Connection</span>
                    </button>
                </div>
            </div>
        </div>
    `;
    lucide.createIcons();
}

/* ==========================================================================
   8. Modals & Detail Views
   ========================================================================== */

function openQuestionModal() {
    DOM.newQuestionModal.classList.add('show');
    DOM.newQuestionModal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    hideModalAlert();
    clearFormErrors();
    if (DOM.inputModalSubject) DOM.inputModalSubject.focus();
}

function closeQuestionModal() {
    DOM.newQuestionModal.classList.remove('show');
    DOM.newQuestionModal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    DOM.createQuestionForm.reset();
    clearFormErrors();
    hideModalAlert();
}

function openViewQuestionModalById(id) {
    const q = state.questions.find(item => item.id === id);
    if (!q) return;

    DOM.viewModalTitle.textContent = q.question;
    DOM.viewModalMeta.textContent = `${q.subject || 'General'} • Module ${q.module_number || 'I'} • ${q.topic || 'General'} • Difficulty: ${q.difficulty || 'Medium'}`;

    const options = [
        { key: 'A', text: q.option_a },
        { key: 'B', text: q.option_b },
        { key: 'C', text: q.option_c },
        { key: 'D', text: q.option_d }
    ];

    const correctAnswer = (q.answer || 'A').toUpperCase();

    DOM.viewModalBody.innerHTML = `
        <div class="view-detail-card">
            <div class="view-options-list">
                ${options.map(opt => `
                    <div class="option-box ${opt.key === correctAnswer ? 'is-correct' : ''}">
                        <span class="option-letter">${opt.key}</span>
                        <span class="option-text">${escapeHtml(opt.text || '')}</span>
                        ${opt.key === correctAnswer ? `<i data-lucide="check" class="correct-check-icon"></i>` : ''}
                    </div>
                `).join('')}
            </div>
            <div style="margin-top: 1rem; padding: 0.85rem; background: var(--primary-50); border: 1px solid var(--primary-200); border-radius: var(--radius-md);">
                <div style="font-size: 0.75rem; font-weight: 700; color: var(--primary-700); text-transform: uppercase; margin-bottom: 0.25rem;">Rationale / Explanation</div>
                <div style="font-size: 0.88rem; color: var(--text-primary); line-height: 1.45;">${escapeHtml(q.explanation || 'No detailed explanation provided.')}</div>
            </div>
        </div>
    `;

    DOM.viewQuestionModal.classList.add('show');
    DOM.viewQuestionModal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    lucide.createIcons();
}

function closeViewQuestionModal() {
    DOM.viewQuestionModal.classList.remove('show');
    DOM.viewQuestionModal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
}

function validateModalForm() {
    let isValid = true;
    clearFormErrors();

    const sub = DOM.inputModalSubject ? DOM.inputModalSubject.value : '';
    const mod = DOM.inputModalModule ? DOM.inputModalModule.value : '';
    const topic = DOM.inputModalTopic ? DOM.inputModalTopic.value.trim() : '';
    const q = DOM.inputQuestion ? DOM.inputQuestion.value.trim() : '';
    const a = DOM.inputOptionA ? DOM.inputOptionA.value.trim() : '';
    const b = DOM.inputOptionB ? DOM.inputOptionB.value.trim() : '';
    const c = DOM.inputOptionC ? DOM.inputOptionC.value.trim() : '';
    const d = DOM.inputOptionD ? DOM.inputOptionD.value.trim() : '';
    const ans = DOM.selectAnswer ? DOM.selectAnswer.value : '';
    const exp = DOM.inputExplanation ? DOM.inputExplanation.value.trim() : '';

    if (!sub) { showFieldError('inputModalSubject', 'errorSubject'); isValid = false; }
    if (!mod) { showFieldError('inputModalModule', 'errorModule'); isValid = false; }
    if (!topic) { showFieldError('inputModalTopic', 'errorTopic'); isValid = false; }
    if (!q) { showFieldError('inputQuestion', 'errorQuestion'); isValid = false; }
    if (!a) { showFieldError('inputOptionA', 'errorOptionA'); isValid = false; }
    if (!b) { showFieldError('inputOptionB', 'errorOptionB'); isValid = false; }
    if (!c) { showFieldError('inputOptionC', 'errorOptionC'); isValid = false; }
    if (!d) { showFieldError('inputOptionD', 'errorOptionD'); isValid = false; }
    if (!ans) { showFieldError('selectAnswer', 'errorAnswer'); isValid = false; }
    if (!exp) { showFieldError('inputExplanation', 'errorExplanation'); isValid = false; }

    return isValid;
}

function showFieldError(inputId, errorId) {
    const input = document.getElementById(inputId);
    const error = document.getElementById(errorId);
    if (input) input.classList.add('is-invalid');
    if (error) error.classList.add('show');
}

function clearFormErrors() {
    document.querySelectorAll('.form-control').forEach(el => el.classList.remove('is-invalid'));
    document.querySelectorAll('.field-error').forEach(el => el.classList.remove('show'));
}

function setModalSubmitting(isSubmitting) {
    DOM.submitQuestionBtn.disabled = isSubmitting;
    DOM.cancelModalBtn.disabled = isSubmitting;
    if (isSubmitting) {
        DOM.btnSpinner.style.display = 'inline-block';
        DOM.btnSubmitText.textContent = 'Saving Question...';
    } else {
        DOM.btnSpinner.style.display = 'none';
        DOM.btnSubmitText.textContent = 'Create Question';
    }
}

function showModalAlert(message) {
    DOM.modalAlertMessage.textContent = message;
    DOM.modalAlertBanner.style.display = 'flex';
}

function hideModalAlert() {
    DOM.modalAlertBanner.style.display = 'none';
}

/* ==========================================================================
   9. Health & Toasts UI
   ========================================================================== */

function updateHealthUI(isHealthy, latency = null) {
    const statusDot = DOM.healthIndicator ? DOM.healthIndicator.querySelector('.status-dot') : null;
    const headerDot = DOM.headerApiPill ? DOM.headerApiPill.querySelector('.status-dot') : null;
    const headerText = DOM.headerApiPill ? DOM.headerApiPill.querySelector('.header-api-text') : null;

    if (isHealthy) {
        if (statusDot) statusDot.className = 'status-dot healthy pulsing';
        if (DOM.healthStatusText) DOM.healthStatusText.textContent = 'API Operational';
        if (DOM.healthPing) DOM.healthPing.textContent = latency ? `${latency} ms` : 'Online';

        if (DOM.headerApiPill) DOM.headerApiPill.className = 'header-api-pill healthy';
        if (headerDot) headerDot.className = 'status-dot healthy';
        if (headerText) headerText.textContent = 'API Operational';

        if (DOM.dashApiIconWrapper) {
            DOM.dashApiIconWrapper.className = 'stat-icon-wrapper bg-emerald-subtle';
            DOM.dashApiIcon.className = 'text-emerald';
            DOM.dashApiStatus.textContent = 'Operational';
            DOM.dashApiLatency.className = 'stat-trend trend-positive';
            DOM.dashApiLatency.textContent = latency ? `${latency} ms` : 'Healthy';
        }
        if (DOM.sysHealthBadge) {
            DOM.sysHealthBadge.className = 'sys-badge healthy';
            DOM.sysHealthBadge.textContent = '● Operational';
        }
    } else {
        if (statusDot) statusDot.className = 'status-dot offline';
        if (DOM.healthStatusText) DOM.healthStatusText.textContent = 'API Offline';
        if (DOM.healthPing) DOM.healthPing.textContent = 'Unavailable';

        if (DOM.headerApiPill) DOM.headerApiPill.className = 'header-api-pill offline';
        if (headerDot) headerDot.className = 'status-dot offline';
        if (headerText) headerText.textContent = 'API Offline';

        if (DOM.dashApiIconWrapper) {
            DOM.dashApiIconWrapper.className = 'stat-icon-wrapper bg-rose-subtle';
            DOM.dashApiIcon.className = 'text-rose';
            DOM.dashApiStatus.textContent = 'Offline';
            DOM.dashApiLatency.className = 'stat-trend trend-negative';
            DOM.dashApiLatency.textContent = 'Unavailable';
        }
        if (DOM.sysHealthBadge) {
            DOM.sysHealthBadge.className = 'sys-badge offline';
            DOM.sysHealthBadge.textContent = '● Offline';
        }
    }
}

function showToast(title, message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;

    let iconName = 'info';
    if (type === 'success') iconName = 'check-circle-2';
    if (type === 'error') iconName = 'alert-circle';

    toast.innerHTML = `
        <div class="toast-icon"><i data-lucide="${iconName}"></i></div>
        <div class="toast-content">
            <div class="toast-title">${escapeHtml(title)}</div>
            <div class="toast-message">${escapeHtml(message)}</div>
        </div>
        <button class="toast-close" aria-label="Close notification" onclick="this.parentElement.remove()">
            <i data-lucide="x"></i>
        </button>
        <div class="toast-progress"></div>
    `;

    DOM.toastContainer.appendChild(toast);
    lucide.createIcons();

    setTimeout(() => {
        if (toast.parentElement) {
            toast.style.animation = 'toastSlideOut 200ms forwards';
            setTimeout(() => toast.remove(), 200);
        }
    }, 4000);
}

/* ==========================================================================
   10. Event Listeners & Setup
   ========================================================================== */

function setupEventListeners() {
    window.addEventListener('hashchange', () => {
        navigateToView(window.location.hash);
    });

    DOM.navDashboard.addEventListener('click', (e) => {
        e.preventDefault();
        window.location.hash = '#dashboard';
        navigateToView('dashboard');
    });

    DOM.navBank.addEventListener('click', (e) => {
        e.preventDefault();
        window.location.hash = '#bank';
        navigateToView('bank');
    });

    DOM.navQuestions.addEventListener('click', (e) => {
        e.preventDefault();
        window.location.hash = '#questions';
        navigateToView('questions');
    });

    DOM.navCategories.addEventListener('click', (e) => {
        e.preventDefault();
        window.location.hash = '#categories';
        navigateToView('categories');
    });

    // Modals
    DOM.btnOpenNewQuestionModal.addEventListener('click', openQuestionModal);
    DOM.closeModalBtn.addEventListener('click', closeQuestionModal);
    DOM.cancelModalBtn.addEventListener('click', closeQuestionModal);

    DOM.closeViewModalBtn.addEventListener('click', closeViewQuestionModal);
    DOM.closeViewModalFooterBtn.addEventListener('click', closeViewQuestionModal);

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeQuestionModal();
            closeViewQuestionModal();
        }
    });

    // Subject dropdown cascading in Modal
    if (DOM.inputModalSubject) {
        DOM.inputModalSubject.addEventListener('change', () => {
            updateModalModuleDropdown();
        });
    }

    if (DOM.inputModalModule) {
        DOM.inputModalModule.addEventListener('change', () => {
            updateModalTopicDatalist();
        });
    }

    // Subject dropdown cascading in Quiz configuration
    if (DOM.quizSubjectSelect) {
        DOM.quizSubjectSelect.addEventListener('change', () => {
            updateQuizModuleDropdown();
        });
    }

    if (DOM.quizModuleSelect) {
        DOM.quizModuleSelect.addEventListener('change', () => {
            updateQuizTopicDropdown();
        });
    }

    // Bank filters
    if (DOM.bankSubjectFilter) {
        DOM.bankSubjectFilter.addEventListener('change', () => {
            updateBankModuleDropdown();
            renderBankView();
        });
    }
    if (DOM.bankModuleFilter) DOM.bankModuleFilter.addEventListener('change', renderBankView);
    if (DOM.bankDiffFilter) DOM.bankDiffFilter.addEventListener('change', renderBankView);
    if (DOM.bankTypeFilter) DOM.bankTypeFilter.addEventListener('change', renderBankView);

    // Global Top Search Bar
    if (DOM.topHeaderSearch) {
        DOM.topHeaderSearch.addEventListener('input', (e) => {
            state.bankFilters.searchQuery = e.target.value;
            if (state.currentView !== 'bank') {
                window.location.hash = '#bank';
                navigateToView('bank');
            } else {
                renderBankView();
            }
        });
    }

    // Modal Form Submission
    DOM.createQuestionForm.addEventListener('submit', (e) => {
        e.preventDefault();
        if (!validateModalForm()) return;

        const subName = DOM.inputModalSubject.value;
        const subOpt = DOM.inputModalSubject.options[DOM.inputModalSubject.selectedIndex];
        const subCode = subOpt ? subOpt.getAttribute('data-code') || '' : '';

        const modNum = parseInt(DOM.inputModalModule.value);
        const modOpt = DOM.inputModalModule.options[DOM.inputModalModule.selectedIndex];
        const modName = modOpt ? modOpt.getAttribute('data-name') || '' : '';

        const payload = {
            subject: subName,
            subject_code: subCode,
            module: modName,
            module_number: modNum,
            topic: DOM.inputModalTopic.value.trim(),
            difficulty: DOM.selectDifficulty.value,
            question_type: DOM.selectQuestionType.value,
            question: DOM.inputQuestion.value.trim(),
            option_a: DOM.inputOptionA.value.trim(),
            option_b: DOM.inputOptionB.value.trim(),
            option_c: DOM.inputOptionC.value.trim(),
            option_d: DOM.inputOptionD.value.trim(),
            answer: DOM.selectAnswer.value,
            explanation: DOM.inputExplanation.value.trim()
        };

        submitQuestion(payload);
    });

    if (DOM.refreshHealthBtn) {
        DOM.refreshHealthBtn.addEventListener('click', checkHealth);
    }

    // Mobile Sidebar
    DOM.mobileMenuToggle.addEventListener('click', () => {
        DOM.sidebar.classList.add('open');
        DOM.sidebarOverlay.classList.add('active');
    });

    DOM.mobileSidebarClose.addEventListener('click', () => {
        DOM.sidebar.classList.remove('open');
        DOM.sidebarOverlay.classList.remove('active');
    });

    DOM.sidebarOverlay.addEventListener('click', () => {
        DOM.sidebar.classList.remove('open');
        DOM.sidebarOverlay.classList.remove('active');
    });
}

function escapeHtml(str) {
    if (!str) return '';
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

function capitalize(str) {
    if (!str) return '';
    return str.charAt(0).toUpperCase() + str.slice(1);
}

// Global Windows Exports
window.openQuestionModal = openQuestionModal;
window.openViewQuestionModalById = openViewQuestionModalById;
window.checkHealth = checkHealth;
window.selectQuizOption = selectQuizOption;
window.submitQuizAnswer = submitQuizAnswer;
window.nextQuestion = nextQuestion;
window.finishQuiz = finishQuiz;
window.restartQuiz = restartQuiz;
window.resetBankFilters = resetBankFilters;
window.resetQuizFilters = resetQuizFilters;
window.initializeQuiz = initializeQuiz;
window.startQuizForSubject = startQuizForSubject;
window.startQuizForTopic = startQuizForTopic;
window.navigateToView = navigateToView;
window.retryConnection = async function() {
    await checkHealth();
    await fetchSyllabus();
    await fetchQuestions();
};

document.addEventListener('DOMContentLoaded', async () => {
    lucide.createIcons();
    setupEventListeners();

    await fetchSyllabus();
    await checkHealth();
    await fetchQuestions();

    const initialHash = window.location.hash || '#questions';
    navigateToView(initialHash);

    setInterval(checkHealth, 20000);
});
