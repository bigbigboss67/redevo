import os

path = r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Print CSS
print_css = '''
    @media print {
      body { background: #ffffff !important; color: #000000 !important; }
      #main-sidebar, .no-print, button, .role-lens-bar { display: none !important; }
      main { width: 100% !important; max-width: 100% !important; padding: 0 !important; margin: 0 !important; }
      .card-inner, .border { border-color: #cbd5e1 !important; box-shadow: none !important; }
      .tab-view { display: block !important; page-break-after: always; }
      .tab-view.hidden { display: none !important; }
    }
'''

# 2. Command Palette HTML
palette_html = '''
  <!-- GLOBAL COMMAND PALETTE (Ctrl+K) -->
  <div id="command-palette-modal" class="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-sm hidden flex items-start justify-center pt-20 px-4">
    <div class="bg-white dark:bg-slate-900 border border-slate-200 dark:border-white/10 rounded-2xl w-full max-w-xl shadow-2xl overflow-hidden">
      <div class="flex items-center px-4 py-3 border-b border-slate-100 dark:border-white/5 gap-3">
        <i data-lucide="search" class="w-5 h-5 text-slate-400"></i>
        <input id="palette-search-input" type="text" placeholder="Search plots (K-018), 5 buildings, FIDIC claims, escrow..." 
               class="w-full bg-transparent border-none text-sm text-slate-900 dark:text-white focus:outline-none placeholder-slate-400">
        <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-slate-100 dark:bg-white/10 text-slate-500">ESC</span>
      </div>
      <div id="palette-results" class="max-h-80 overflow-y-auto p-2 space-y-1 text-sm">
      </div>
      <div class="px-4 py-2 bg-slate-50 dark:bg-white/5 border-t border-slate-100 dark:border-white/5 text-[11px] text-slate-500 flex justify-between items-center">
        <span>Navigate & click to open</span>
        <span>Esc to close</span>
      </div>
    </div>
  </div>
'''

# 3. Palette JS
palette_js = '''
  <script>
    const PALETTE_ITEMS = [
      { type: 'Building', name: 'Building I // Orthopedic Clinic', tab: 'landmark-buildings', sub: 'bldg-1', desc: 'Medical & Diagnostic Center (3,800 m²)' },
      { type: 'Building', name: 'Building ♥ // Heart Resort & Spa', tab: 'landmark-buildings', sub: 'bldg-2', desc: '5-Star Luxury Resort (8,400 m²)' },
      { type: 'Building', name: 'Building B // Central Mosque & Pavilion', tab: 'landmark-buildings', sub: 'bldg-3', desc: 'Heritage Cultural Center (2,900 m²)' },
      { type: 'Building', name: 'Building O // Olympic Sports & Equestrian', tab: 'landmark-buildings', sub: 'bldg-4', desc: 'Sports Complex & Stables (5,200 m²)' },
      { type: 'Building', name: 'Building SNIA // Artisan Retail Promenade', tab: 'landmark-buildings', sub: 'bldg-5', desc: 'Retail & Gastronomy (4,700 m²)' },
      { type: 'Module', name: '1. Master Cockpit // €97.0M GDV Roll-Up', tab: 'cockpit', desc: 'Executive telemetry & headcount' },
      { type: 'Module', name: '2. 5 Landmark Buildings OS', tab: 'landmark-buildings', desc: 'Heart Hotel, Clinic & Retail Promenades' },
      { type: 'Module', name: '3. 120-Plot Villa Masterplan', tab: 'matrix', desc: 'Hillside topography & 120-plot matrix' },
      { type: 'Module', name: '4. 3D BIM & LiDAR Digital Twin', tab: 'digital-twin', desc: 'Point-cloud inspection & ±2.8mm tolerance' },
      { type: 'Module', name: '5. FIDIC Multi-Sig Escrow Vault', tab: 'escrow', desc: 'UniCredit & BBI 4-party sign-off' },
      { type: 'Module', name: '6. Field Biometrics & SLAs', tab: 'contractor-sla', desc: '142 craftsmen & concrete tests' },
      { type: 'Module', name: '7. FIDIC Clause 20 Claims Register', tab: 'fidic-claims', desc: '28-day statutory notice shield' },
      { type: 'Module', name: '8. BizDev & Ingestion Engine', tab: 'bizdev-engine', desc: 'CAD, DCF pro-forma, Monte Carlo risk' },
      { type: 'Module', name: '9. Buyer 360° Portal // Plot K-018', tab: 'buyer-portal', desc: '4K live stream & finishes customizer' },
      { type: 'Plot', name: 'Plot K-018 // Luxury 4-Bedroom Villa', tab: 'buyer-portal', desc: 'Porcelanosa finishes, 72% completed' }
    ];

    function openCommandPalette() {
      const modal = document.getElementById('command-palette-modal');
      const input = document.getElementById('palette-search-input');
      modal.classList.remove('hidden');
      input.value = '';
      renderPaletteResults('');
      input.focus();
    }

    function closeCommandPalette() {
      const m = document.getElementById('command-palette-modal');
      if (m) m.classList.add('hidden');
    }

    function renderPaletteResults(query) {
      const list = document.getElementById('palette-results');
      if (!list) return;
      const q = (query || '').toLowerCase().trim();
      const filtered = PALETTE_ITEMS.filter(item => 
        item.name.toLowerCase().includes(q) || 
        item.type.toLowerCase().includes(q) || 
        item.desc.toLowerCase().includes(q)
      );

      if (filtered.length === 0) {
        list.innerHTML = '<div class="p-4 text-center text-slate-400 text-xs">No matching assets found.</div>';
        return;
      }

      list.innerHTML = filtered.map(item => `
        <div onclick="selectPaletteItem('${item.tab}', '${item.sub || ''}')" 
             class="p-2.5 rounded-xl hover:bg-slate-100 dark:hover:bg-white/5 cursor-pointer flex items-center justify-between group transition-colors">
          <div class="flex items-center gap-3">
            <span class="text-[10px] font-mono px-2 py-0.5 rounded uppercase font-bold ${
              item.type === 'Building' ? 'bg-amber-500/15 text-amber-600 dark:text-amber-400' :
              item.type === 'Module' ? 'bg-blue-500/15 text-blue-600 dark:text-blue-400' :
              'bg-emerald-500/15 text-emerald-600 dark:text-emerald-400'
            }">${item.type}</span>
            <div>
              <div class="text-xs font-semibold text-slate-800 dark:text-slate-200 group-hover:text-amber-600 dark:group-hover:text-amber-400">${item.name}</div>
              <div class="text-[11px] text-slate-400">${item.desc}</div>
            </div>
          </div>
          <i data-lucide="chevron-right" class="w-4 h-4 text-slate-300"></i>
        </div>
      `).join('');
      if (window.lucide) lucide.createIcons();
    }

    function selectPaletteItem(tab, sub) {
      closeCommandPalette();
      if (typeof switchTab === 'function') switchTab(tab);
      if (sub && typeof inspectBuilding === 'function' && tab === 'landmark-buildings') {
        const id = parseInt(sub.replace('bldg-', ''));
        setTimeout(() => inspectBuilding(id), 100);
      }
    }

    // Global Key Listener for Ctrl+K, Esc, and 1-9
    window.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        openCommandPalette();
      }
      if (e.key === 'Escape') {
        closeCommandPalette();
      }
      if (document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
        const num = parseInt(e.key);
        if (num >= 1 && num <= 9) {
          const tabKeys = ['cockpit', 'landmark-buildings', 'matrix', 'digital-twin', 'escrow', 'contractor-sla', 'fidic-claims', 'bizdev-engine', 'buyer-portal'];
          if (tabKeys[num - 1] && typeof switchTab === 'function') switchTab(tabKeys[num - 1]);
        }
      }
    });

    document.getElementById('palette-search-input')?.addEventListener('input', (e) => {
      renderPaletteResults(e.target.value);
    });

    function exportAuditDossierPDF() {
      window.print();
    }
  </script>
'''

# Sidebar Quick Action Buttons
sidebar_btns = '''
      <!-- QUICK SEARCH & PDF EXPORT -->
      <div class="pt-2 pb-1 space-y-1.5 no-print">
        <button onclick="openCommandPalette()" class="w-full flex items-center justify-between px-3 py-2 rounded-xl border border-slate-200 dark:border-white/10 bg-slate-50/50 dark:bg-white/5 text-xs text-slate-500 hover:border-amber-500/50 transition-colors group">
          <div class="flex items-center gap-2">
            <i data-lucide="search" class="w-3.5 h-3.5 text-slate-400 group-hover:text-amber-500"></i>
            <span>Quick Jump...</span>
          </div>
          <span class="text-[10px] font-mono px-1.5 py-0.5 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-white/10 text-slate-400">Ctrl K</span>
        </button>
        <button onclick="exportAuditDossierPDF()" class="w-full flex items-center justify-between px-3 py-2 rounded-xl border border-slate-200 dark:border-white/10 bg-slate-50/50 dark:bg-white/5 text-xs text-slate-500 hover:text-amber-600 dark:hover:text-amber-400 hover:border-amber-500/50 transition-colors">
          <div class="flex items-center gap-2">
            <i data-lucide="printer" class="w-3.5 h-3.5"></i>
            <span>Export Audit PDF</span>
          </div>
          <span class="text-[10px] font-mono text-slate-400">A4 Print</span>
        </button>
      </div>
'''

if '@media print' not in html:
    html = html.replace('</style>', print_css + '\n</style>', 1)

if 'id="command-palette-modal"' not in html:
    html = html.replace('</body>', palette_html + '\n' + palette_js + '\n</body>', 1)

if 'openCommandPalette' not in html:
    html = html.replace('<!-- NAVIGATION LIST -->', sidebar_btns + '\n      <!-- NAVIGATION LIST -->', 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html successfully!')
