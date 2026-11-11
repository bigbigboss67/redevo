# Architectural Studio Sidebar Layout Re-Architect
import json

with open(r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\coords.json', 'r', encoding='utf-8') as f:
    coords_json = f.read().strip()

with open(r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\view-cockpit.html', 'r', encoding='utf-8') as f:
    cockpit_html = f.read()

with open(r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\view-landmark-buildings.html', 'r', encoding='utf-8') as f:
    landmark_bldgs_html = f.read()

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

sidebar_layout_html = f"""<!DOCTYPE html>
<html lang="en" class="light">
<head>
  <meta charset="UTF-8">
  <link rel="icon" href="favicon.ico">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AETHEL APEX // I LOVE BOSNIA — Architectural OS</title>
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
              obsidian: '#090B0E',
              surface: '#11141D',
              border: 'rgba(255, 255, 255, 0.08)'
            }}
          }}
        }}
      }}
    }}
  </script>
  <style>
    :root {{
      --bg-main: #F8FAFC;
      --bg-sidebar: #FFFFFF;
      --card-bg: #FFFFFF;
      --border-color: #E2E8F0;
      --text-primary: #0F172A;
      --text-muted: #64748B;
      --ease-spring: cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .dark {{
      --bg-main: #07090C;
      --bg-sidebar: #0C0F15;
      --card-bg: #11141D;
      --border-color: rgba(255, 255, 255, 0.08);
      --text-primary: #F1F5F9;
      --text-muted: #94A3B8;
    }}

    body {{
      background-color: var(--bg-main);
      color: var(--text-primary);
      font-family: 'Plus Jakarta Sans', sans-serif;
      overflow-x: hidden;
    }}

    .card-bezel {{
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 1.25rem;
      box-shadow: 0 4px 16px -2px rgba(15, 23, 42, 0.04);
      transition: all 0.2s var(--ease-spring);
    }}

    .card-inner {{
      background: transparent;
    }}

    .tab-view {{
      animation: tabSlideIn 200ms var(--ease-spring) forwards;
    }}

    @keyframes tabSlideIn {{
      from {{ opacity: 0; transform: translateY(4px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .light .text-white {{ color: #0F172A !important; }}
    .light .text-slate-300, .light .text-slate-400 {{ color: #475569 !important; }}
    .light .bg-white\\/\\[0\\.02\\], .light .bg-white\\/\\[0\\.03\\], .light .bg-white\\/5 {{
      background-color: #F1F5F9 !important;
      border-color: #E2E8F0 !important;
    }}
    .light .border-white\\/5, .light .border-white\\/10 {{
      border-color: #E2E8F0 !important;
    }}

    ::-webkit-scrollbar {{ width: 5px; height: 5px; }}
    ::-webkit-scrollbar-track {{ background: transparent; }}
    ::-webkit-scrollbar-thumb {{ background: rgba(148, 163, 184, 0.4); border-radius: 9999px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: #E5A93C; }}

    @media (prefers-reduced-motion: reduce) {{
      *, ::before, ::after {{ animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }}
    }}
  </style>
</head>
<body class="min-h-screen flex antialiased">

  <!-- ================= LEFT COLLAPSIBLE WORKSPACE SIDEBAR ================= -->
  <aside id="main-sidebar" class="w-72 flex-shrink-0 border-r border-slate-200 dark:border-white/10 bg-white dark:bg-[#0C0F15] flex flex-col justify-between h-screen sticky top-0 z-30 transition-all duration-300">
    
    <!-- Sidebar Top: Brand & Project Spec -->
    <div class="p-5 border-b border-slate-200 dark:border-white/10 space-y-3">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-amber-500 to-amber-700 flex items-center justify-center shadow-md flex-shrink-0">
          <i data-lucide="building-2" class="w-5 h-5 text-slate-950 font-black"></i>
        </div>
        <div class="overflow-hidden">
          <h1 class="text-sm font-black tracking-tight text-slate-900 dark:text-white truncate">I LOVE BOSNIA</h1>
          <p class="text-[10px] font-mono text-amber-600 dark:text-amber-400 font-bold uppercase tracking-wider">Breza Highland Enclave</p>
        </div>
      </div>

      <!-- Quick Metrics Pill -->
      <div class="p-2.5 rounded-xl bg-slate-50 dark:bg-white/[0.03] border border-slate-200 dark:border-white/5 space-y-1 font-mono text-[10px]">
        <div class="flex justify-between"><span class="text-slate-500">Master GDV:</span> <strong class="text-amber-500">€97.0M</strong></div>
        <div class="flex justify-between"><span class="text-slate-500">Scope:</span> <span class="text-slate-700 dark:text-slate-300">120 Villas + 5 Bldgs</span></div>
        <div class="flex justify-between"><span class="text-slate-500">Float:</span> <span class="text-emerald-500 font-bold">+11.4d Optimal</span></div>
      </div>
    </div>

    <!-- Sidebar Middle: Vertical Architectural Navigation (Zero Overlap Guaranteed) -->
    <nav class="flex-1 overflow-y-auto p-3 space-y-1">
      <div class="px-3 py-1.5 text-[10px] font-mono font-bold uppercase tracking-wider text-slate-400">Project Modules</div>
      
      <!-- Nav 1: Cockpit -->
      <button onclick="switchTab('cockpit')" id="tab-btn-cockpit" class="nav-tab w-full text-left p-2.5 rounded-xl bg-amber-500/15 text-amber-600 dark:text-amber-400 font-bold transition flex items-center gap-3">
        <i data-lucide="layout-dashboard" class="w-4 h-4 text-amber-500"></i>
        <div class="truncate">
          <div class="text-xs">1. Master Cockpit</div>
          <div class="text-[10px] text-slate-400 font-normal">GDV & Live KPI</div>
        </div>
      </button>

      <!-- Nav 2: 5 Landmark Buildings -->
      <button onclick="switchTab('landmark-buildings')" id="tab-btn-landmark-buildings" class="nav-tab w-full text-left p-2.5 rounded-xl hover:bg-slate-100 dark:hover:bg-white/5 text-slate-600 dark:text-slate-300 transition flex items-center gap-3">
        <i data-lucide="building" class="w-4 h-4 text-rose-500"></i>
        <div class="truncate">
          <div class="text-xs">2. 5 Landmark Buildings</div>
          <div class="text-[10px] text-slate-400 font-normal">Hotel, Clinic & Retail</div>
        </div>
      </button>

      <!-- Nav 3: 120-Plot Villa Matrix -->
      <button onclick="switchTab('matrix')" id="tab-btn-matrix" class="nav-tab w-full text-left p-2.5 rounded-xl hover:bg-slate-100 dark:hover:bg-white/5 text-slate-600 dark:text-slate-300 transition flex items-center gap-3">
        <i data-lucide="heart" class="w-4 h-4 text-rose-500"></i>
        <div class="truncate">
          <div class="text-xs">3. 120 Villa Masterplan</div>
          <div class="text-[10px] text-slate-400 font-normal">I • ♥ • BOSNIA Layout</div>
        </div>
      </button>

      <!-- Nav 4: 3D BIM & Drone LiDAR -->
      <button onclick="switchTab('digital-twin')" id="tab-btn-digital-twin" class="nav-tab w-full text-left p-2.5 rounded-xl hover:bg-slate-100 dark:hover:bg-white/5 text-slate-600 dark:text-slate-300 transition flex items-center gap-3">
        <i data-lucide="box" class="w-4 h-4 text-cyan-500"></i>
        <div class="truncate">
          <div class="text-xs">4. 3D BIM & LiDAR</div>
          <div class="text-[10px] text-slate-400 font-normal">±2.8mm Digital Twin</div>
        </div>
      </button>

      <!-- Nav 5: Escrow Multi-Sig -->
      <button onclick="switchTab('escrow')" id="tab-btn-escrow" class="nav-tab w-full text-left p-2.5 rounded-xl hover:bg-slate-100 dark:hover:bg-white/5 text-slate-600 dark:text-slate-300 transition flex items-center gap-3">
        <i data-lucide="shield-check" class="w-4 h-4 text-emerald-500"></i>
        <div class="truncate">
          <div class="text-xs">5. Escrow Multi-Sig</div>
          <div class="text-[10px] text-slate-400 font-normal">UniCredit & BBI Trust</div>
        </div>
      </button>

      <!-- Nav 6: Field Biometrics -->
      <button onclick="switchTab('contractor-sla')" id="tab-btn-contractor-sla" class="nav-tab w-full text-left p-2.5 rounded-xl hover:bg-slate-100 dark:hover:bg-white/5 text-slate-600 dark:text-slate-300 transition flex items-center gap-3">
        <i data-lucide="fingerprint" class="w-4 h-4 text-purple-500"></i>
        <div class="truncate">
          <div class="text-xs">6. Field Biometrics</div>
          <div class="text-[10px] text-slate-400 font-normal">142 Craftsmen & SLAs</div>
        </div>
      </button>

      <!-- Nav 7: FIDIC Claims -->
      <button onclick="switchTab('fidic-claims')" id="tab-btn-fidic-claims" class="nav-tab w-full text-left p-2.5 rounded-xl hover:bg-slate-100 dark:hover:bg-white/5 text-slate-600 dark:text-slate-300 transition flex items-center gap-3">
        <i data-lucide="file-text" class="w-4 h-4 text-rose-500"></i>
        <div class="truncate">
          <div class="text-xs">7. FIDIC Clause 20</div>
          <div class="text-[10px] text-slate-400 font-normal">28-Day Time-Bar Shield</div>
        </div>
      </button>

      <!-- Nav 8: BizDev OS -->
      <button onclick="switchTab('bizdev-engine')" id="tab-btn-bizdev-engine" class="nav-tab w-full text-left p-2.5 rounded-xl hover:bg-slate-100 dark:hover:bg-white/5 text-slate-600 dark:text-slate-300 transition flex items-center gap-3">
        <i data-lucide="sparkles" class="w-4 h-4 text-amber-500"></i>
        <div class="truncate">
          <div class="text-xs">8. BizDev & Ingestion</div>
          <div class="text-[10px] text-slate-400 font-normal">DCF, Feasibility & CAD</div>
        </div>
      </button>

      <!-- Nav 9: Buyer Portal -->
      <button onclick="switchTab('buyer-portal')" id="tab-btn-buyer-portal" class="nav-tab w-full text-left p-2.5 rounded-xl hover:bg-slate-100 dark:hover:bg-white/5 text-slate-600 dark:text-slate-300 transition flex items-center gap-3">
        <i data-lucide="eye" class="w-4 h-4 text-indigo-500"></i>
        <div class="truncate">
          <div class="text-xs">9. Buyer 360° Portal</div>
          <div class="text-[10px] text-slate-400 font-normal">Live 4K Cam & Finishes</div>
        </div>
      </button>
    </nav>

    <!-- Sidebar Bottom: Theme & Currency Controls -->
    <div class="p-4 border-t border-slate-200 dark:border-white/10 space-y-3">
      <div class="flex items-center justify-between text-xs font-mono">
        <span class="text-slate-400">Currency:</span>
        <div class="flex items-center bg-slate-100 dark:bg-white/5 rounded-lg p-0.5 border border-slate-200 dark:border-white/10">
          <button onclick="setCurrency('EUR')" id="curr-EUR" class="curr-btn px-2 py-0.5 rounded bg-amber-500 text-slate-950 font-bold">€</button>
          <button onclick="setCurrency('BAM')" id="curr-BAM" class="curr-btn px-2 py-0.5 rounded text-slate-500">KM</button>
          <button onclick="setCurrency('USD')" id="curr-USD" class="curr-btn px-2 py-0.5 rounded text-slate-500">$</button>
          <button onclick="setCurrency('AED')" id="curr-AED" class="curr-btn px-2 py-0.5 rounded text-slate-500">AED</button>
        </div>
      </div>

      <button onclick="toggleTheme()" class="w-full py-2 px-3 rounded-xl bg-slate-100 dark:bg-white/5 hover:bg-slate-200 dark:hover:bg-white/10 text-xs font-semibold flex items-center justify-between transition">
        <span class="flex items-center gap-2">
          <i id="theme-icon" data-lucide="moon" class="w-4 h-4 text-amber-500"></i>
          <span id="theme-text">Dark Mode</span>
        </span>
        <span class="text-[10px] font-mono text-slate-400">Toggle</span>
      </button>
    </div>

  </aside>

  <!-- ================= MAIN CONTENT VIEWPORT ================= -->
  <main class="flex-1 flex flex-col min-w-0 h-screen overflow-y-auto">
    
    <!-- Top Thin Utility Bar -->
    <header class="p-4 px-8 border-b border-slate-200 dark:border-white/10 bg-white/70 dark:bg-[#07090C]/70 backdrop-blur-md sticky top-0 z-20 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
      <div class="flex items-center gap-3">
        <span class="text-xs font-mono text-slate-400 uppercase">Role Perspective:</span>
        <div class="flex items-center p-1 bg-slate-100 dark:bg-white/5 rounded-xl border border-slate-200 dark:border-white/10 text-xs font-medium">
          <button onclick="setStakeholderRole('all')" id="role-btn-all" class="role-pill-btn px-3 py-1 rounded-lg bg-amber-500 text-slate-950 font-bold transition">All</button>
          <button onclick="setStakeholderRole('developer')" id="role-btn-developer" class="role-pill-btn px-3 py-1 rounded-lg text-slate-600 dark:text-slate-300 transition">Developer</button>
          <button onclick="setStakeholderRole('constructor')" id="role-btn-constructor" class="role-pill-btn px-3 py-1 rounded-lg text-slate-600 dark:text-slate-300 transition">Constructor</button>
          <button onclick="setStakeholderRole('architect')" id="role-btn-architect" class="role-pill-btn px-3 py-1 rounded-lg text-slate-600 dark:text-slate-300 transition">Architect</button>
          <button onclick="setStakeholderRole('consultant')" id="role-btn-consultant" class="role-pill-btn px-3 py-1 rounded-lg text-slate-600 dark:text-slate-300 transition">FIDIC Legal</button>
          <button onclick="setStakeholderRole('buyer')" id="role-btn-buyer" class="role-pill-btn px-3 py-1 rounded-lg text-slate-600 dark:text-slate-300 transition">Buyer</button>
        </div>
      </div>

      <div class="flex items-center gap-3 text-xs font-mono text-slate-500">
        <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span> Air-Gapped Sovereign Node</span>
        <span>•</span>
        <span>Weather: <strong>12°C Clear</strong></span>
      </div>
    </header>

    <!-- Guided Workflow Step-by-Step Strip -->
    <div class="px-8 pt-5">
      <div id="step-by-step-guide-container" class="card-bezel"></div>
    </div>

    <!-- Active Views Container -->
    <div class="p-8 space-y-6">
      {cockpit_html}
      {landmark_bldgs_html}
      {matrix_html}
      {twin_html}
      {escrow_html}
      {sla_html}
      {fidic_html}
      {bizdev_html}
      {buyer_html}
    </div>

  </main>

  <!-- MODALS & DRAWERS -->
  {modals_html}

  <!-- SCRIPTS -->
  <script src="workflow_guide.js"></script>
  <script src="buildings_engine.js"></script>
  <script>
    const PLOT_COORDINATES = {coords_json};

    function initTheme() {{
      const saved = localStorage.getItem('ilb-theme') || 'light';
      applyTheme(saved);
    }}

    function toggleTheme() {{
      const isDark = document.documentElement.classList.contains('dark');
      applyTheme(isDark ? 'light' : 'dark');
    }}

    function applyTheme(theme) {{
      const html = document.documentElement;
      const themeText = document.getElementById('theme-text');
      const themeIcon = document.getElementById('theme-icon');

      if (theme === 'dark') {{
        html.classList.add('dark');
        html.classList.remove('light');
        if (themeText) themeText.innerText = 'Light Mode';
        if (themeIcon) themeIcon.setAttribute('data-lucide', 'sun');
        localStorage.setItem('ilb-theme', 'dark');
      }} else {{
        html.classList.remove('dark');
        html.classList.add('light');
        if (themeText) themeText.innerText = 'Dark Mode';
        if (themeIcon) themeIcon.setAttribute('data-lucide', 'moon');
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

        let letterCluster = 'S';
        if (plotIdx <= 17) letterCluster = 'I';
        else if (plotIdx <= 39) letterCluster = 'HEART';
        else if (plotIdx <= 79) letterCluster = 'B';
        else letterCluster = 'S';

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
          buaM2: 300,
          letterCluster: letterCluster
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
        card.className = 'group relative p-2.5 rounded-xl bg-slate-50 dark:bg-white/[0.03] border border-slate-200 dark:border-white/5 hover:border-amber-500/50 hover:bg-amber-50/20 dark:hover:bg-white/[0.06] transition cursor-pointer text-left';
        card.onclick = () => inspectPlotDetails(p.id);

        card.innerHTML = `
          <div class="flex items-center justify-between mb-1">
            <span class="font-mono text-xs font-bold text-slate-900 dark:text-white group-hover:text-amber-500 transition">${{p.id}}</span>
            <span class="w-2 h-2 rounded-full ${{p.colorClass}}"></span>
          </div>
          <div class="text-[10px] text-slate-500 dark:text-slate-400 truncate mb-1.5">${{p.stageLabel}}</div>
          <div class="flex items-center justify-between text-[9px] font-mono text-slate-400">
            <span>${{p.milestonePct}}%</span>
            <span class="text-amber-500 font-bold">${{p.letterCluster === 'HEART' ? '♥ LOVE' : p.letterCluster}}</span>
          </div>
          <div class="w-full bg-slate-200 dark:bg-white/10 h-1 rounded-full mt-1.5 overflow-hidden">
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

    function filterByLetter(letter) {{
      document.querySelectorAll('.letter-pill').forEach(btn => {{
        btn.classList.remove('bg-amber-500', 'text-slate-950', 'font-bold');
        btn.classList.add('bg-slate-100', 'dark:bg-white/5', 'text-slate-700', 'dark:text-slate-300');
      }});
      const activeBtn = document.getElementById(`letter-btn-${{letter}}`);
      if (activeBtn) {{
        activeBtn.classList.remove('bg-slate-100', 'dark:bg-white/5', 'text-slate-700', 'dark:text-slate-300');
        activeBtn.classList.add('bg-amber-500', 'text-slate-950', 'font-bold');
      }}

      document.querySelectorAll('.cluster-zone').forEach(z => z.classList.remove('ring-4', 'ring-white', 'scale-105'));
      const labelEl = document.getElementById('active-cluster-label');

      if (letter === 'ALL') {{
        renderPlots(PLOTS);
        if (labelEl) labelEl.innerText = 'All 120 Villas Displayed';
        renderMapPins(PLOTS);
      }} else {{
        const filtered = PLOTS.filter(p => p.letterCluster === letter);
        renderPlots(filtered);
        const overlay = document.getElementById(`cluster-overlay-${{letter}}`);
        if (overlay) overlay.classList.add('ring-4', 'ring-white', 'scale-105');
        if (labelEl) {{
          const desc = letter === 'I' ? "Letter 'I' Formation (001–017) • Valley Entry" :
                       letter === 'HEART' ? "Heart '♥' Formation (018–039) • Core Promenade" :
                       letter === 'B' ? "'B - O' Enclave (040–079) • Hillside Gardens" :
                       "'S - N - I - A' Ridgeline (080–120) • Panoramic Crest";
          labelEl.innerText = desc;
        }}
        renderMapPins(filtered);
      }}
    }}

    function renderMapPins(plotsToRender) {{
      const layer = document.getElementById('map-pins-layer');
      if (!layer) return;
      layer.innerHTML = '';

      plotsToRender.forEach(p => {{
        const coord = PLOT_COORDINATES[String(p.number)];
        if (!coord) return;

        const pin = document.createElement('div');
        pin.className = 'absolute -translate-x-1/2 -translate-y-1/2 pointer-events-auto cursor-pointer group/pin';
        pin.style.left = `${{coord.x}}%`;
        pin.style.top = `${{coord.y}}%`;
        pin.onclick = (e) => {{ e.stopPropagation(); inspectPlotDetails(p.id); }};

        const bgClass = p.letterCluster === 'I' ? 'bg-cyan-400' :
                        p.letterCluster === 'HEART' ? 'bg-rose-500' :
                        p.letterCluster === 'B' ? 'bg-amber-400' : 'bg-emerald-400';

        pin.innerHTML = `
          <div class="relative flex items-center justify-center">
            <span class="w-3.5 h-3.5 rounded-full ${{bgClass}} text-black font-mono text-[8px] font-black flex items-center justify-center shadow-lg border border-black/80 hover:scale-150 transition-transform">
              ${{p.number}}
            </span>
            <div class="absolute bottom-5 left-1/2 -translate-x-1/2 hidden group-hover/pin:flex flex-col items-center z-30 pointer-events-none">
              <span class="px-2 py-0.5 rounded bg-black/90 text-white font-mono text-[9px] whitespace-nowrap shadow-xl border border-white/20">
                ${{p.id}} • ${{p.stageLabel}}
              </span>
            </div>
          </div>
        `;
        layer.appendChild(pin);
      }});
    }}

    function setMasterplanView(mode) {{
      const mapCol = document.getElementById('col-masterplan-map');
      const gridCol = document.getElementById('col-masterplan-grid');

      document.querySelectorAll('#btn-view-split, #btn-view-map, #btn-view-grid').forEach(b => {{
        b.classList.remove('bg-amber-500', 'text-slate-950', 'font-bold');
        b.classList.add('text-slate-600', 'dark:text-slate-400');
      }});

      if (mode === 'split') {{
        document.getElementById('btn-view-split').classList.add('bg-amber-500', 'text-slate-950', 'font-bold');
        mapCol.className = 'lg:col-span-7 space-y-3';
        gridCol.className = 'lg:col-span-5 space-y-3';
        mapCol.classList.remove('hidden');
        gridCol.classList.remove('hidden');
      }} else if (mode === 'map-only') {{
        document.getElementById('btn-view-map').classList.add('bg-amber-500', 'text-slate-950', 'font-bold');
        mapCol.className = 'lg:col-span-12 space-y-3';
        mapCol.classList.remove('hidden');
        gridCol.classList.add('hidden');
      }} else if (mode === 'grid-only') {{
        document.getElementById('btn-view-grid').classList.add('bg-amber-500', 'text-slate-950', 'font-bold');
        gridCol.className = 'lg:col-span-12 space-y-3';
        gridCol.classList.remove('hidden');
        mapCol.classList.add('hidden');
      }}
    }}

    function setStakeholderRole(roleKey) {{
      document.querySelectorAll('.role-pill-btn').forEach(btn => {{
        btn.classList.remove('bg-amber-500', 'text-slate-950', 'font-bold');
        btn.classList.add('text-slate-600', 'dark:text-slate-300');
      }});
      const activeBtn = document.getElementById(`role-btn-${{roleKey}}`);
      if (activeBtn) {{
        activeBtn.classList.remove('text-slate-600', 'dark:text-slate-300');
        activeBtn.classList.add('bg-amber-500', 'text-slate-950', 'font-bold');
      }}

      if (typeof renderWorkflowGuide === 'function') {{
        renderWorkflowGuide(roleKey);
      }}

      const guide = STAKEHOLDER_GUIDES[roleKey] || STAKEHOLDER_GUIDES.all;
      if (guide && guide.steps && guide.steps[0] && roleKey !== 'all') {{
        switchTab(guide.steps[0].targetTab);
      }}
    }}

    function switchTab(viewId) {{
      document.querySelectorAll('.tab-view').forEach(v => v.classList.add('hidden'));
      document.querySelectorAll('.nav-tab').forEach(b => {{
        b.classList.remove('bg-amber-500/15', 'text-amber-600', 'dark:text-amber-400', 'font-bold');
        b.classList.add('text-slate-600', 'dark:text-slate-300');
      }});

      const target = document.getElementById(`view-${{viewId}}`);
      if (target) target.classList.remove('hidden');

      const btn = document.getElementById(`tab-btn-${{viewId}}`);
      if (btn) {{
        btn.classList.add('bg-amber-500/15', 'text-amber-600', 'dark:text-amber-400', 'font-bold');
        btn.classList.remove('text-slate-600', 'dark:text-slate-300');
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
        alert("Universal Multimodal Synthesis Completed!\\n\\n1. Master Scope: 120 Villas + 5 Landmark Buildings synchronized.\\n2. Total GDV: €97.0M (€54.2M Villas + €42.8M Commercial Buildings).\\n3. Architecture: ±2.8mm structural tolerances verified across all sectors.\\n4. WBS Timeframe: Dual-track fast-track (24m Villas / 36m Commercial).\\n5. Sovereign Ledger: Balanced double-entry trial balance (€138,500,000).\\n\\nAll stakeholder views updated.");
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
      pin.innerHTML = `<span class="w-6 h-6 rounded-full bg-emerald-500 text-slate-950 font-mono text-xs font-bold flex items-center justify-center shadow-lg border-2 border-white pin-drop-anim">+</span>`;
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

      const totalGDV = Math.round(97000000 * rate);
      const paid = Math.round(52400000 * rate);
      const escrow = Math.round(28600000 * rate);

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
        ctx.fillStyle = isDark ? '#07090C' : '#F1F5F9';
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
      renderMapPins(PLOTS);
      renderWorkflowGuide('all');
    }});
  </script>
</body>
</html>
"""

with open(r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\index.html', 'w', encoding='utf-8') as f:
    f.write(sidebar_layout_html)
print("Complete Architectural Sidebar Layout Re-Architect Written Successfully!")
