import re

# Read views and modals
with open(r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\view-cockpit.html', 'r', encoding='utf-8') as f:
    cockpit_html = f.read()

with open(r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\view-matrix.html', 'r', encoding='utf-8') as f:
    matrix_html = f.read()

with open(r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\view-digital-twin.html', 'r', encoding='utf-8') as f:
    twin_html = f.read()

with open(r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\view-escrow.html', 'r', encoding='utf-8') as f:
    escrow_html = f.read()

with open(r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\view-contractor-sla.html', 'r', encoding='utf-8') as f:
    sla_html = f.read()

with open(r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\view-fidic-claims.html', 'r', encoding='utf-8') as f:
    fidic_html = f.read()

with open(r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\view-bizdev-engine.html', 'r', encoding='utf-8') as f:
    bizdev_html = f.read()

with open(r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\view-buyer-portal.html', 'r', encoding='utf-8') as f:
    buyer_html = f.read()

with open(r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\modals_and_drawer.html', 'r', encoding='utf-8') as f:
    modals_html = f.read()

full_html = f"""<!DOCTYPE html>
<html lang="en" class="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AETHEL APEX // I LOVE BOSNIA — Universal Enterprise PM & Real Estate OS</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/lucide@latest"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          }},
          colors: {{
            brand: {{
              gold: '#E5A93C',
              'gold-light': '#F7D070',
              'gold-dim': 'rgba(229, 169, 60, 0.15)',
              obsidian: '#090B0E',
              surface: '#11141D',
              'surface-card': '#171B26',
              border: 'rgba(255, 255, 255, 0.08)',
              emerald: '#10B981',
              rose: '#F43F5E',
              amber: '#F59E0B',
              cyan: '#06B6D4'
            }}
          }}
        }}
      }}
    }}
  </script>
  <style>
    /* CSS Root Themes */
    :root {{
      --bg-canvas: #F8FAFC;
      --text-main: #0F172A;
      --card-bg: #FFFFFF;
      --card-border: #E2E8F0;
      --card-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.06);
    }}
    .dark {{
      --bg-canvas: #090B0E;
      --text-main: #F1F5F9;
      --card-bg: #11141D;
      --card-border: rgba(255, 255, 255, 0.08);
      --card-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.6);
    }}

    body {{
      background-color: var(--bg-canvas);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', sans-serif;
      overflow-x: hidden;
      transition: background-color 0.25s ease, color 0.25s ease;
    }}

    .card-bezel {{
      background: rgba(148, 163, 184, 0.1);
      border: 1px solid var(--card-border);
      border-radius: 1.5rem;
      padding: 0.25rem;
      box-shadow: var(--card-shadow);
      transition: all 0.2s ease;
    }}
    .dark .card-bezel {{
      background: rgba(255, 255, 255, 0.03);
    }}

    .card-inner {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: calc(1.5rem - 0.25rem);
      transition: all 0.2s ease;
    }}

    /* Polished typography colors in both modes */
    .light .text-white {{
      color: #0F172A !important;
    }}
    .light .text-slate-300, .light .text-slate-400 {{
      color: #475569 !important;
    }}
    .light .bg-white\\/\\[0\\.02\\], .light .bg-white\\/\\[0\\.03\\], .light .bg-white\\/5 {{
      background-color: #F1F5F9 !important;
      border-color: #E2E8F0 !important;
    }}
    .light .border-white\\/5, .light .border-white\\/10 {{
      border-color: #E2E8F0 !important;
    }}

    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: transparent;
    }}
    ::-webkit-scrollbar-thumb {{
      background: rgba(148, 163, 184, 0.4);
      border-radius: 9999px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #E5A93C;
    }}
  </style>
</head>
<body class="min-h-[100dvh] flex flex-col antialiased selection:bg-[#E5A93C]/30">

  <!-- Ambient Backdrop -->
  <div class="fixed top-0 left-1/2 -translate-x-1/2 w-[1200px] h-[340px] bg-gradient-to-b from-amber-500/10 via-cyan-500/5 to-transparent blur-3xl pointer-events-none -z-10"></div>

  <!-- Main View Container -->
  <div class="w-full max-w-[1700px] mx-auto px-4 sm:px-6 lg:px-8 py-5 space-y-6">

    <!-- UNIVERSAL TOP COMMAND HEADER -->
    <header class="card-bezel sticky top-3 z-40">
      <div class="card-inner px-6 py-4 flex flex-col xl:flex-row items-center justify-between gap-4">
        
        <!-- Left: Logo & Project Info -->
        <div class="flex items-center gap-4 w-full xl:w-auto justify-between xl:justify-start">
          <div class="flex items-center gap-3.5">
            <div class="w-12 h-12 rounded-2xl bg-gradient-to-br from-amber-500 to-amber-700 p-[1px] shadow-lg shadow-amber-500/20 flex-shrink-0">
              <div class="w-full h-full bg-slate-900 rounded-[calc(1rem-1px)] flex items-center justify-center">
                <i data-lucide="building-2" class="w-6 h-6 text-amber-400"></i>
              </div>
            </div>
            <div>
              <div class="flex items-center gap-2">
                <span class="text-xs uppercase tracking-wider font-mono font-bold text-amber-600 dark:text-amber-400">ILB ENTERPRISE OS</span>
                <span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-[11px] font-mono font-semibold text-emerald-700 dark:text-emerald-400">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span> SOVEREIGN INTERNAL STACK
                </span>
              </div>
              <h1 class="text-xl font-bold tracking-tight text-slate-900 dark:text-white flex items-center gap-2">
                I LOVE BOSNIA <span class="text-slate-400 font-light">|</span> 120 Luxury Contemporary Villas
              </h1>
              <p class="text-xs text-slate-500 dark:text-slate-400 font-medium">Breza (Sarajevo North) • 124,480 m² Parcel • 300 m² BUA / Villa • €54.2M GDV</p>
            </div>
          </div>

          <!-- Mobile Theme Toggle -->
          <div class="flex xl:hidden items-center gap-2">
            <button onclick="toggleTheme()" class="p-2 rounded-xl border border-slate-200 dark:border-white/10 bg-slate-100 dark:bg-white/5 text-slate-700 dark:text-slate-200">
              <i id="theme-icon-mobile" data-lucide="moon" class="w-4 h-4"></i>
            </button>
          </div>
        </div>

        <!-- Center: Stakeholder Role Lens Selector -->
        <div class="flex flex-col sm:flex-row items-center gap-2 w-full xl:w-auto">
          <span class="text-xs font-mono font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider flex items-center gap-1.5">
            <i data-lucide="users" class="w-3.5 h-3.5">="text-amber-500"></i> Role Lens:
          </span>
          <div class="flex flex-wrap items-center justify-center p-1 bg-slate-100 dark:bg-slate-900/80 rounded-2xl border border-slate-200 dark:border-white/10 text-xs font-medium">
            <button onclick="setStakeholderRole('all')" id="role-btn-all" class="role-pill-btn px-3 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-bold transition flex items-center gap-1.5">
              <i data-lucide="globe" class="w-3.5 h-3.5"></i> All Roles
            </button>
            <button onclick="setStakeholderRole('developer')" id="role-btn-developer" class="role-pill-btn px-3 py-1.5 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-800 transition flex items-center gap-1.5">
              <i data-lucide="briefcase" class="w-3.5 h-3.5 text-blue-500"></i> Developer
            </button>
            <button onclick="setStakeholderRole('constructor')" id="role-btn-constructor" class="role-pill-btn px-3 py-1.5 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-800 transition flex items-center gap-1.5">
              <i data-lucide="hard-hat" class="w-3.5 h-3.5 text-amber-500"></i> Constructor
            </button>
            <button onclick="setStakeholderRole('architect')" id="role-btn-architect" class="role-pill-btn px-3 py-1.5 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-800 transition flex items-center gap-1.5">
              <i data-lucide="compass" class="w-3.5 h-3.5 text-cyan-500"></i> Architect
            </button>
            <button onclick="setStakeholderRole('consultant')" id="role-btn-consultant" class="role-pill-btn px-3 py-1.5 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-800 transition flex items-center gap-1.5">
              <i data-lucide="scale" class="w-3.5 h-3.5 text-emerald-500"></i> FIDIC Legal
            </button>
            <button onclick="setStakeholderRole('buyer')" id="role-btn-buyer" class="role-pill-btn px-3 py-1.5 rounded-xl text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-800 transition flex items-center gap-1.5">
              <i data-lucide="home" class="w-3.5 h-3.5 text-purple-500"></i> Buyer
            </button>
          </div>
        </div>

        <!-- Right: Currency Switcher & Light/Dark Mode Switcher -->
        <div class="hidden xl:flex items-center gap-3">
          <!-- Currency Toggle -->
          <div class="flex items-center bg-slate-100 dark:bg-slate-900/80 border border-slate-200 dark:border-white/10 rounded-2xl p-1 text-xs font-mono">
            <button onclick="setCurrency('EUR')" id="curr-EUR" class="curr-btn px-2.5 py-1 rounded-xl bg-amber-500 text-slate-950 font-bold transition">EUR €</button>
            <button onclick="setCurrency('BAM')" id="curr-BAM" class="curr-btn px-2.5 py-1 rounded-xl text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition">BAM KM</button>
            <button onclick="setCurrency('USD')" id="curr-USD" class="curr-btn px-2.5 py-1 rounded-xl text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition">USD $</button>
            <button onclick="setCurrency('AED')" id="curr-AED" class="curr-btn px-2.5 py-1 rounded-xl text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition">AED</button>
          </div>

          <!-- Light / Dark Mode Toggle Button -->
          <button onclick="toggleTheme()" id="theme-toggle-btn" class="flex items-center gap-2 px-3 py-2 rounded-2xl bg-slate-100 dark:bg-slate-900/80 border border-slate-200 dark:border-white/10 text-xs font-semibold text-slate-700 dark:text-slate-200 hover:bg-slate-200 dark:hover:bg-slate-800 transition" title="Toggle Light / Dark Mode">
            <i id="theme-icon" data-lucide="moon" class="w-4 h-4 text-amber-500"></i>
            <span id="theme-text">Dark Mode</span>
          </button>
        </div>

      </div>

      <!-- AWARD-WINNING CLEAR NAVIGATION BAR (8 FUNCTIONAL PILLARS WITH DESCRIPTIONS) -->
      <nav class="px-6 pb-4 pt-1 border-t border-slate-100 dark:border-white/5 overflow-x-auto">
        <div class="flex items-center gap-2 min-w-max py-1">
          
          <!-- Tab 1: Cockpit -->
          <button onclick="switchTab('cockpit')" id="tab-btn-cockpit" class="nav-tab group text-left px-3.5 py-2.5 rounded-2xl bg-amber-500/10 border-2 border-amber-500 text-slate-900 dark:text-white transition shadow-sm">
            <div class="flex items-center gap-2">
              <i data-lucide="layout-dashboard" class="w-4 h-4 text-amber-500"></i>
              <span class="text-xs font-bold font-mono">1. Master Cockpit</span>
            </div>
            <p class="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5 max-w-[130px] truncate">GDV, Cash & Live Site KPI</p>
          </button>

          <!-- Tab 2: 120-Plot CAD Matrix -->
          <button onclick="switchTab('matrix')" id="tab-btn-matrix" class="nav-tab group text-left px-3.5 py-2.5 rounded-2xl bg-transparent hover:bg-slate-100 dark:hover:bg-white/5 border border-transparent hover:border-slate-200 dark:hover:border-white/10 text-slate-600 dark:text-slate-300 transition">
            <div class="flex items-center gap-2">
              <i data-lucide="grid" class="w-4 h-4 text-blue-500"></i>
              <span class="text-xs font-bold font-mono">2. 120-Plot Matrix</span>
            </div>
            <p class="text-[10px] text-slate-400 dark:text-slate-500 mt-0.5 max-w-[130px] truncate">All 120 Villa Statuses</p>
          </button>

          <!-- Tab 3: 3D BIM & Drone LiDAR -->
          <button onclick="switchTab('digital-twin')" id="tab-btn-digital-twin" class="nav-tab group text-left px-3.5 py-2.5 rounded-2xl bg-transparent hover:bg-slate-100 dark:hover:bg-white/5 border border-transparent hover:border-slate-200 dark:hover:border-white/10 text-slate-600 dark:text-slate-300 transition">
            <div class="flex items-center gap-2">
              <i data-lucide="box" class="w-4 h-4 text-cyan-500"></i>
              <span class="text-xs font-bold font-mono">3. 3D BIM & LiDAR</span>
            </div>
            <p class="text-[10px] text-slate-400 dark:text-slate-500 mt-0.5 max-w-[130px] truncate">±2.8mm Digital Twin QA</p>
          </button>

          <!-- Tab 4: FIDIC Escrow Multi-Sig -->
          <button onclick="switchTab('escrow')" id="tab-btn-escrow" class="nav-tab group text-left px-3.5 py-2.5 rounded-2xl bg-transparent hover:bg-slate-100 dark:hover:bg-white/5 border border-transparent hover:border-slate-200 dark:hover:border-white/10 text-slate-600 dark:text-slate-300 transition">
            <div class="flex items-center gap-2">
              <i data-lucide="shield-check" class="w-4 h-4 text-emerald-500"></i>
              <span class="text-xs font-bold font-mono">4. Escrow Multi-Sig</span>
            </div>
            <p class="text-[10px] text-slate-400 dark:text-slate-500 mt-0.5 max-w-[130px] truncate">4-Party Vault Governance</p>
          </button>

          <!-- Tab 5: Biometrics & Penalties -->
          <button onclick="switchTab('contractor-sla')" id="tab-btn-contractor-sla" class="nav-tab group text-left px-3.5 py-2.5 rounded-2xl bg-transparent hover:bg-slate-100 dark:hover:bg-white/5 border border-transparent hover:border-slate-200 dark:hover:border-white/10 text-slate-600 dark:text-slate-300 transition">
            <div class="flex items-center gap-2">
              <i data-lucide="fingerprint" class="w-4 h-4 text-purple-500"></i>
              <span class="text-xs font-bold font-mono">5. Field Biometrics</span>
            </div>
            <p class="text-[10px] text-slate-400 dark:text-slate-500 mt-0.5 max-w-[130px] truncate">142 Craftsmen & SLA Clock</p>
          </button>

          <!-- Tab 6: FIDIC Clause 20 Claims -->
          <button onclick="switchTab('fidic-claims')" id="tab-btn-fidic-claims" class="nav-tab group text-left px-3.5 py-2.5 rounded-2xl bg-transparent hover:bg-slate-100 dark:hover:bg-white/5 border border-transparent hover:border-slate-200 dark:hover:border-white/10 text-slate-600 dark:text-slate-300 transition">
            <div class="flex items-center gap-2">
              <i data-lucide="file-text" class="w-4 h-4 text-rose-500"></i>
              <span class="text-xs font-bold font-mono">6. FIDIC Clause 20</span>
            </div>
            <p class="text-[10px] text-slate-400 dark:text-slate-500 mt-0.5 max-w-[130px] truncate">28-Day Claim Bar Protection</p>
          </button>

          <!-- Tab 7: Ingestion & BizDev OS (Highlighted) -->
          <button onclick="switchTab('bizdev-engine')" id="tab-btn-bizdev-engine" class="nav-tab group text-left px-3.5 py-2.5 rounded-2xl bg-amber-500/10 hover:bg-amber-500/20 border border-amber-500/30 text-amber-700 dark:text-amber-400 transition">
            <div class="flex items-center gap-2">
              <i data-lucide="sparkles" class="w-4 h-4 text-amber-500"></i>
              <span class="text-xs font-bold font-mono">7. BizDev & Underwriting</span>
            </div>
            <p class="text-[10px] text-amber-600/80 dark:text-amber-400/80 mt-0.5 max-w-[140px] truncate">DCF, Feasibility & Snagging</p>
          </button>

          <!-- Tab 8: Buyer 360° Portal -->
          <button onclick="switchTab('buyer-portal')" id="tab-btn-buyer-portal" class="nav-tab group text-left px-3.5 py-2.5 rounded-2xl bg-transparent hover:bg-slate-100 dark:hover:bg-white/5 border border-transparent hover:border-slate-200 dark:hover:border-white/10 text-slate-600 dark:text-slate-300 transition">
            <div class="flex items-center gap-2">
              <i data-lucide="eye" class="w-4 h-4 text-indigo-500"></i>
              <span class="text-xs font-bold font-mono">8. Buyer 360° Portal</span>
            </div>
            <p class="text-[10px] text-slate-400 dark:text-slate-500 mt-0.5 max-w-[130px] truncate">Live Camera & Finishes</p>
          </button>

        </div>
      </nav>

      <!-- ROLE EXPLANATION BANNER (CLARIFIES CONTEXT FOR EVERYONE) -->
      <div class="px-6 py-2 bg-slate-50 dark:bg-slate-900/40 border-t border-slate-100 dark:border-white/5 flex flex-col md:flex-row md:items-center justify-between gap-2 text-xs">
        <div class="flex items-center gap-2.5">
          <span class="px-2 py-0.5 rounded-md bg-amber-500 text-slate-950 font-bold font-mono text-[10px]" id="role-badge-text">Universal Overview</span>
          <span class="font-bold text-slate-900 dark:text-white" id="role-banner-title">All Stakeholders View</span>
          <span class="text-slate-400 dark:text-slate-500 hidden sm:inline">•</span>
          <span class="text-slate-600 dark:text-slate-400" id="role-banner-desc">Complete cross-functional project transparency and governance across all 120 villas.</span>
        </div>
        <div class="flex items-center gap-4 text-slate-500 dark:text-slate-400 font-mono text-[11px]">
          <span>Air-Gapped Local Host: <strong class="text-emerald-600 dark:text-emerald-400">127.0.0.1:3456</strong></span>
          <span>Zero External SaaS Dependency</span>
        </div>
      </div>

    </header>

    <!-- CONTENT WRAPPER -->
    <div id="content-views" class="space-y-6">
      {cockpit_html}
      {matrix_html}
      {twin_html}
      {escrow_html}
      {sla_html}
      {fidic_html}
      {bizdev_html}
      {buyer_html}
    </div>

  </div>

  <!-- MODALS & DRAWERS -->
  {modals_html}

  <!-- ROLES & JAVASCRIPT SYSTEM ENGINE -->
  <script src="roles.js"></script>
  <script>
    // Theme Engine: Light & Dark Mode
    function initTheme() {{
      const saved = localStorage.getItem('ilb-theme') || 'light';
      applyTheme(saved);
    }}

    function toggleTheme() {{
      const isDark = document.documentElement.classList.contains('dark');
      const nextTheme = isDark ? 'light' : 'dark';
      applyTheme(nextTheme);
    }}

    function applyTheme(theme) {{
      const html = document.documentElement;
      const themeText = document.getElementById('theme-text');
      const themeIcon = document.getElementById('theme-icon');
      const themeIconMobile = document.getElementById('theme-icon-mobile');

      if (theme === 'dark') {{
        html.classList.add('dark');
        html.classList.remove('light');
        if (themeText) themeText.innerText = 'Light Mode';
        if (themeIcon) themeIcon.setAttribute('data-lucide', 'sun');
        if (themeIconMobile) themeIconMobile.setAttribute('data-lucide', 'sun');
        localStorage.setItem('ilb-theme', 'dark');
      }} else {{
        html.classList.remove('dark');
        html.classList.add('light');
        if (themeText) themeText.innerText = 'Dark Mode';
        if (themeIcon) themeIcon.setAttribute('data-lucide', 'moon');
        if (themeIconMobile) themeIconMobile.setAttribute('data-lucide', 'moon');
        localStorage.setItem('ilb-theme', 'light');
      }}
      if (window.lucide) lucide.createIcons();
    }}

    initTheme();
  </script>
  <script>
    const RATES = {{ EUR: 1.0, BAM: 1.95583, USD: 1.08, AED: 3.96 }};
    const CURRENCY_SYMBOLS = {{ EUR: '€', BAM: 'KM ', USD: '$', AED: 'AED ' }};
    let currentCurrency = 'EUR';

    const STAGES = [
      {{ name: 'fitout', label: 'Luxury Fitout', color: 'bg-emerald-500', count: 20 }},
      {{ name: 'mep', label: 'MEP & Glazing', color: 'bg-cyan-500', count: 25 }},
      {{ name: 'structure', label: 'Superstructure', color: 'bg-blue-500', count: 31 }},
      {{ name: 'foundation', label: 'Foundation Pour', color: 'bg-amber-500', count: 22 }},
      {{ name: 'earthworks', label: 'Geotech Excavation', color: 'bg-rose-500', count: 14 }},
      {{ name: 'prep', label: 'Permit & Prep', color: 'bg-slate-600', count: 8 }}
    ];

    const SUBCONTRACTORS = [
      'Bosna Beton d.d.',
      'Sinteza Construction JV',
      'Euro-Asfalt d.o.o.',
      'Alu-Façade Austria',
      'Breza Municipal Works'
    ];

    const PLOTS = [];
    let plotIdx = 1;
    STAGES.forEach(stage => {{
      for (let i = 0; i < stage.count; i++) {{
        const idNum = String(plotIdx).padStart(3, '0');
        const id = `K-${{idNum}}`;
        const sub = SUBCONTRACTORS[plotIdx % SUBCONTRACTORS.length];
        const basePrice = 450000 + (plotIdx * 250);
        const milestonePct = stage.name === 'fitout' ? 85 :
                             stage.name === 'mep' ? 65 :
                             stage.name === 'structure' ? 45 :
                             stage.name === 'foundation' ? 25 :
                             stage.name === 'earthworks' ? 10 : 5;

        PLOTS.push({{
          id,
          number: plotIdx,
          stage: stage.name,
          stageLabel: stage.label,
          colorClass: stage.color,
          subcontractor: sub,
          priceEUR: basePrice,
          milestonePct: milestonePct,
          landM2: 750 + (plotIdx * 3),
          buaM2: 300
        }});
        plotIdx++;
      }}
    }});

    function renderPlots(plotsToRender) {{
      const container = document.getElementById('plot-grid-container');
      if (!container) return;
      container.innerHTML = '';

      plotsToRender.forEach(p => {{
        const card = document.createElement('div');
        card.className = 'group relative p-3 rounded-2xl bg-slate-50 dark:bg-white/[0.03] border border-slate-200 dark:border-white/5 hover:border-amber-500/50 hover:bg-amber-50/20 dark:hover:bg-white/[0.06] transition cursor-pointer';
        card.onclick = () => inspectPlotDetails(p.id);

        card.innerHTML = `
          <div class="flex items-center justify-between mb-1.5">
            <span class="font-mono text-xs font-bold text-slate-900 dark:text-white group-hover:text-amber-500 transition">${{p.id}}</span>
            <span class="w-2 h-2 rounded-full ${{p.colorClass}}"></span>
          </div>
          <div class="text-[11px] text-slate-500 dark:text-slate-400 truncate mb-2">${{p.stageLabel}}</div>
          <div class="flex items-center justify-between text-[10px] font-mono text-slate-500">
            <span>${{p.milestonePct}}% Complete</span>
            <span>${{p.subcontractor.split(' ')[0]}}</span>
          </div>
          <div class="w-full bg-slate-200 dark:bg-white/10 h-1 rounded-full mt-2 overflow-hidden">
            <div class="${{p.colorClass}} h-full transition-all duration-500" style="width: ${{p.milestonePct}}%"></div>
          </div>
        `;
        container.appendChild(card);
      }});
      const countEl = document.getElementById('visible-plot-count');
      if (countEl) countEl.innerText = `${{plotsToRender.length}} / 120 Villas`;
    }}

    function filterPlots(stage) {{
      document.querySelectorAll('.filter-pill').forEach(btn => {{
        btn.classList.remove('bg-amber-500', 'text-slate-950', 'font-bold');
        btn.classList.add('bg-slate-100', 'dark:bg-white/5', 'text-slate-600', 'dark:text-slate-400');
      }});
      const targetBtn = document.getElementById(`filter-btn-${{stage}}`);
      if (targetBtn) {{
        targetBtn.classList.remove('bg-slate-100', 'dark:bg-white/5', 'text-slate-600', 'dark:text-slate-400');
        targetBtn.classList.add('bg-amber-500', 'text-slate-950', 'font-bold');
      }}

      if (stage === 'all') {{
        renderPlots(PLOTS);
      }} else {{
        renderPlots(PLOTS.filter(p => p.stage === stage));
      }}
    }}

    function switchTab(viewId) {{
      document.querySelectorAll('.tab-view').forEach(v => v.classList.add('hidden'));
      document.querySelectorAll('.nav-tab').forEach(b => {{
        b.classList.remove('bg-amber-500/10', 'border-2', 'border-amber-500', 'text-slate-900', 'dark:text-white', 'shadow-sm');
        b.classList.add('bg-transparent', 'text-slate-600', 'dark:text-slate-300', 'border', 'border-transparent');
      }});

      const target = document.getElementById(`view-${{viewId}}`);
      if (target) target.classList.remove('hidden');

      const btn = document.getElementById(`tab-btn-${{viewId}}`);
      if (btn) {{
        btn.classList.add('bg-amber-500/10', 'border-2', 'border-amber-500', 'text-slate-900', 'dark:text-white', 'shadow-sm');
        btn.classList.remove('bg-transparent', 'text-slate-600', 'dark:text-slate-300', 'border-transparent');
      }}

      if (viewId === 'digital-twin') {{
        setTimeout(initBimCanvas, 50);
      }}
    }}

    function inspectPlotDetails(plotId) {{
      const p = PLOTS.find(item => item.id === plotId);
      if (!p) return;
      document.getElementById('drawer-plot-badge').innerText = p.id;
      document.getElementById('drawer-plot-title').innerText = `Villa ${{p.id}} // 4-Bedroom Contemporary`;
      document.getElementById('drawer-plot-stage').innerText = p.stageLabel;
      document.getElementById('drawer-plot-price').innerText = `€${{p.priceEUR.toLocaleString()}}`;
      document.getElementById('plot-drawer').classList.remove('hidden');
    }}

    function closePlotDrawer() {{
      document.getElementById('plot-drawer').classList.add('hidden');
    }}

    function openModal(modalId) {{
      const m = document.getElementById(modalId);
      if (m) m.classList.remove('hidden');
    }}

    function closeModal(modalId) {{
      const m = document.getElementById(modalId);
      if (m) m.classList.add('hidden');
    }}

    function triggerAiSynthesis() {{
      const btn = document.getElementById('btn-synthesize');
      const pulse = document.getElementById('synthesis-pulse');
      if (btn) btn.innerText = "Parsing CAD & IFC Point Clouds...";
      if (pulse) pulse.classList.remove('hidden');

      setTimeout(() => {{
        if (btn) btn.innerText = "Computing DCF Cash Flows...";
      }}, 700);

      setTimeout(() => {{
        if (btn) btn.innerText = "Running Monte Carlo Risks...";
      }}, 1400);

      setTimeout(() => {{
        if (btn) btn.innerText = "✦ Re-Synthesize All Dossiers";
        if (pulse) pulse.classList.add('hidden');
        alert("Universal Multimodal Synthesis Completed!\\n\\n1. Architecture: 120 Villas mapped with ±2.8mm structural tolerances.\\n2. WBS Timeframe: 24-month critical path calibrated to Breza frost conditions.\\n3. Argus Underwriting: €54.2M GDV, 26.4% IRR, €14.85M NPV verified.\\n4. Sovereign Ledger: Balanced double-entry trial balance (€79,445,000).\\n\\nAll stakeholder views updated.");
      }}, 2100);
    }}

    function simulateFileUpload() {{
      alert("Multimodal File Ingestion Dialog:\\nSelect project files (AutoCAD .dwg, Revit/IFC .ifc, Feasibility PDF, Pro-Forma Excel)...\\n\\nFile validated. Ready for AI project synthesis.");
    }}

    function switchBizSubTab(tabId) {{
      document.querySelectorAll('.biz-view').forEach(v => v.classList.add('hidden'));
      document.querySelectorAll('.biz-tab').forEach(b => {{
        b.classList.remove('bg-amber-500', 'text-slate-950', 'font-bold');
        b.classList.add('bg-slate-100', 'dark:bg-white/5', 'text-slate-600', 'dark:text-slate-400');
      }});

      const target = document.getElementById(`biz-view-${{tabId}}`);
      if (target) target.classList.remove('hidden');

      const btn = document.getElementById(`biz-sub-${{tabId}}`);
      if (btn) {{
        btn.classList.add('bg-amber-500', 'text-slate-950', 'font-bold');
        btn.classList.remove('bg-slate-100', 'dark:bg-white/5', 'text-slate-600', 'dark:text-slate-400');
      }}
    }}

    function sendAutomatedTrancheInvoices() {{
      alert("Off-Plan Collections Engine:\\nDispatched 120 automated milestone collection notices with certified escrow payment vouchers to UniCredit/BBI Trust.");
    }}

    function applyValueEngineeringSavings() {{
      alert("Value Engineering Savings Applied!\\nBaseline construction budget reduced by €1,420,000. Project margin increased to 40.8%.");
      closeModal('ve-modal');
    }}

    function update4dSim(month) {{
      const sliderVal = document.getElementById('sim4d-slider-val');
      const monthText = document.getElementById('sim4d-month-text');
      const img = document.getElementById('sim4d-image');
      if (sliderVal) sliderVal.innerText = `Month ${{month}}`;
      if (monthText) monthText.innerText = `Month ${{month}} of 24 (Progressive Build)`;
      if (img) {{
        if (month < 6) {{
          img.src = 'assets/images/masterplan_3d_numbered.jpg';
        }} else if (month < 16) {{
          img.src = 'assets/images/villa_facade_exterior.jpg';
        }} else {{
          img.src = 'assets/images/villa_facade_dusk.jpg';
        }}
      }}
    }}

    function downloadContractPDF() {{
      alert("Exporting FIDIC EPC Silver Book Turnkey Agreement for I LOVE BOSNIA (PDF with e-Signature tokens)... Download complete.");
      closeModal('fidic-modal');
    }}

    function approveMilestone() {{
      alert("FIDIC Independent Engineer Certification Recorded!\\nPayment tranche released to Escrow Sub-Account.");
      closePlotDrawer();
    }}

    function generateFidicNotice() {{
      alert("FIDIC Sub-Clause 20.2 Notice of Claim drafted. 28-day statutory bar countdown anchored to ledger.");
    }}

    function signMunicipal() {{
      alert("Breza Municipality Urban Planning Auditor: Signed.\\nTranche release certified for 120 villas.");
    }}

    function downloadOfficialInspectionCert() {{
      alert("Downloading Certified Villa Inspection Report (PDF with QR-Verification)... Ready.");
    }}

    function scheduleSiteVisit() {{
      alert("VIP Private Site Tour with Helicopter Transfer from Sarajevo International Airport (SJJ) booked.");
    }}

    function triggerSimulationModal() {{
      const m = document.getElementById('sim-modal');
      const res = document.getElementById('sim-result');
      if (m) m.classList.remove('hidden');
      if (res) res.classList.add('hidden');
    }}

    function runScenario(type) {{
      const res = document.getElementById('sim-result');
      if (res) {{
        res.classList.remove('hidden');
        res.innerHTML = `<strong>SIMULATION COMPLETE:</strong> Critical path float buffer remains resilient (+5.4d).`;
      }}
    }}

    function dropSnagPin(event) {{
      const rect = event.currentTarget.getBoundingClientRect();
      const x = ((event.clientX - rect.left) / rect.width) * 100;
      const y = ((event.clientY - rect.top) / rect.height) * 100;
      
      const layer = document.getElementById('snag-pins-layer');
      if (!layer) return;
      const pin = document.createElement('div');
      pin.className = 'absolute -translate-x-1/2 -translate-y-1/2 pointer-events-auto cursor-pointer';
      pin.style.left = `${{x.toFixed(1)}}%`;
      pin.style.top = `${{y.toFixed(1)}}%`;
      pin.onclick = (e) => {{ e.stopPropagation(); inspectPin('NEW-PIN'); }};
      pin.innerHTML = `<span class="w-6 h-6 rounded-full bg-emerald-500 text-slate-950 font-mono text-xs font-bold flex items-center justify-center shadow-lg border-2 border-white animate-bounce">+</span>`;
      layer.appendChild(pin);
      alert(`Native CAD Plan Pin Dropped at [X: ${{x.toFixed(1)}}%, Y: ${{y.toFixed(1)}}%]!\\nLogged into Internal Sovereign Defect Ledger.`);
    }}

    function inspectPin(pinId) {{
      const badge = document.getElementById('snag-pin-badge');
      const title = document.getElementById('snag-pin-title');
      if (badge) badge.innerText = `${{pinId}} (SELECTED)`;
      if (title) title.innerText = pinId === 'PIN-01' ? 'Schüco Glazing Seal Gasket Gap' : 'Italian Porcelanosa Tile Edge Alignment';
    }}

    function resolveSnagPin(pinId) {{
      alert(`Pin ${{pinId}} Resolved!\\nSubcontractor sign-off confirmed by Sinteza Chief Engineer.`);
      const badge = document.getElementById('snag-pin-badge');
      if (badge) badge.innerText = `${{pinId}} (RESOLVED)`;
    }}

    function setCurrency(curr) {{
      currentCurrency = curr;
      document.querySelectorAll('.curr-btn').forEach(b => {{
        b.classList.remove('bg-amber-500', 'text-slate-950', 'font-bold');
        b.classList.add('text-slate-500', 'dark:text-slate-400');
      }});
      const activeBtn = document.getElementById(`curr-${{curr}}`);
      if (activeBtn) {{
        activeBtn.classList.add('bg-amber-500', 'text-slate-950', 'font-bold');
        activeBtn.classList.remove('text-slate-500', 'dark:text-slate-400');
      }}

      const rate = RATES[curr];
      const symbol = CURRENCY_SYMBOLS[curr];

      const totalGDV = Math.round(54200000 * rate);
      const paid = Math.round(37070000 * rate);
      const escrow = Math.round(17130000 * rate);

      const gdvEl = document.getElementById('kpi-gdv');
      const paidEl = document.getElementById('kpi-paid');
      const escrowEl = document.getElementById('kpi-escrow');
      const lockVal = document.getElementById('escrow-locked-val');

      if (gdvEl) gdvEl.innerText = `${{symbol}}${{totalGDV.toLocaleString()}}`;
      if (paidEl) paidEl.innerText = `${{symbol}}${{(paid / 1000000).toFixed(2)}}M`;
      if (escrowEl) escrowEl.innerText = `${{symbol}}${{(escrow / 1000000).toFixed(2)}}M`;
      if (lockVal) lockVal.innerText = `${{symbol}}${{escrow.toLocaleString()}}`;
    }}

    let bimAnimId;
    function initBimCanvas() {{
      const canvas = document.getElementById('bim-canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      let angle = 0;

      function renderFrame() {{
        const isDark = document.documentElement.classList.contains('dark');
        ctx.fillStyle = isDark ? '#090B0E' : '#F1F5F9';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.strokeStyle = isDark ? 'rgba(255, 255, 255, 0.08)' : 'rgba(0, 0, 0, 0.08)';
        ctx.lineWidth = 1;
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2 + 50;

        for (let i = -6; i <= 6; i++) {{
          ctx.beginPath();
          ctx.moveTo(centerX + (i * 30) - Math.cos(angle) * 20, centerY + (i * 15));
          ctx.lineTo(centerX + (i * 30) + 180, centerY + (i * 15) - 90);
          ctx.stroke();
        }}

        for (let p = 0; p < 60; p++) {{
          const px = centerX + Math.cos(angle + p * 0.2) * (100 + (p * 2.5));
          const py = centerY + Math.sin(angle + p * 0.2) * (50 + (p * 1.2)) - (p % 4 * 12);

          ctx.fillStyle = (p % 3 === 0) ? '#10B981' : (p % 3 === 1) ? '#06B6D4' : '#E5A93C';
          ctx.beginPath();
          ctx.arc(px, py, 3, 0, Math.PI * 2);
          ctx.fill();

          if (p % 4 === 0) {{
            ctx.strokeStyle = isDark ? 'rgba(229, 169, 60, 0.2)' : 'rgba(180, 83, 9, 0.25)';
            ctx.beginPath();
            ctx.moveTo(px, py);
            ctx.lineTo(px, py + 20);
            ctx.stroke();
          }}
        }}

        angle += 0.008;
        bimAnimId = requestAnimationFrame(renderFrame);
      }}

      if (bimAnimId) cancelAnimationFrame(bimAnimId);
      renderFrame();
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      lucide.createIcons();
      renderPlots(PLOTS);
    }});
  </script>
</body>
</html>
"""

with open(r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)
print('Successfully wrote redesigned index.html, size:', len(full_html))
