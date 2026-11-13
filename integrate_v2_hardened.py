import re

path = r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Include audit_ledger.js and executive_lens.js before </body>
script_tags = '''
  <script src="audit_ledger.js"></script>
  <script src="executive_lens.js"></script>
'''
if 'audit_ledger.js' not in html:
    html = html.replace('</body>', script_tags + '\n</body>')

# 2. Add Top Header Traffic Light & Controls
# Look for </header> inside <main>
header_end = html.find('</header>')
if header_end != -1 and 'master-traffic-light' not in html:
    new_header_controls = '''
      <!-- DINO'S MASTER TRAFFIC LIGHT & SOVEREIGN CONTROLS -->
      <div class="flex items-center flex-wrap gap-2.5">
        <div id="master-traffic-light" class="px-3 py-1.5 rounded-full text-xs font-bold flex items-center gap-2 bg-emerald-500/20 text-emerald-600 dark:text-emerald-400 border border-emerald-500/30">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
          <span id="traffic-light-label">SYSTEM HEALTH: NOMINAL // ALL SYSTEMS ON SCHEDULE</span>
        </div>

        <!-- Winter Climate Engine Toggle -->
        <button id="btn-toggle-winter-freeze" onclick="toggleWinterFreezeMode()" 
                class="px-2.5 py-1.5 rounded-xl border border-slate-200 dark:border-white/10 bg-slate-50 dark:bg-white/5 text-[11px] font-semibold text-slate-700 dark:text-slate-300 hover:border-amber-500/50 transition">
          ☀️ Normal Weather (+18°C)
        </button>

        <!-- Plain Language Lens Toggle -->
        <button id="btn-toggle-jargon" onclick="toggleJargonLens()" 
                class="px-2.5 py-1.5 rounded-xl border border-slate-200 dark:border-white/10 bg-slate-50 dark:bg-white/5 text-[11px] font-semibold text-slate-700 dark:text-slate-300 hover:border-amber-500/50 transition">
          👓 Plain Language (Active)
        </button>

        <!-- Quad-Language Switcher -->
        <div class="flex items-center p-0.5 bg-slate-100 dark:bg-white/5 rounded-xl border border-slate-200 dark:border-white/10 text-[10px] font-mono">
          <button id="lang-btn-en" onclick="setPortalLanguage('en')" class="px-2 py-1 rounded-lg bg-amber-500 text-white font-bold transition">EN</button>
          <button id="lang-btn-bs" onclick="setPortalLanguage('bs')" class="px-2 py-1 rounded-lg text-slate-400 hover:text-white transition">BS</button>
          <button id="lang-btn-de" onclick="setPortalLanguage('de')" class="px-2 py-1 rounded-lg text-slate-400 hover:text-white transition">DE</button>
          <button id="lang-btn-ar" onclick="setPortalLanguage('ar')" class="px-2 py-1 rounded-lg text-slate-400 hover:text-white transition">AR</button>
        </div>
      </div>
    '''
    html = html[:header_end] + new_header_controls + '\n    ' + html[header_end:]

# 3. Add Winter Climate Warning Banner right after header
banner_html = '''
    <!-- WINTER CLIMATE CRITICAL NOTICE BANNER -->
    <div id="winter-climate-banner" class="hidden mx-8 mt-4 p-3.5 rounded-2xl bg-red-500/10 border border-red-500/30 text-red-600 dark:text-red-400 text-xs flex items-center justify-between gap-4 animate-in slide-in-from-top duration-200">
      <div class="flex items-center gap-2.5 font-medium">
        <i data-lucide="snowflake" class="w-4 h-4 text-red-500 shrink-0"></i>
        <span id="winter-climate-banner-text">WINTER FREEZE ACTIVE (-7°C): Superstructure concrete locked without thermal curing tent. All pours paused under FIDIC Clause 4.12.</span>
      </div>
      <span class="px-2 py-0.5 rounded font-mono text-[10px] bg-red-500/20 uppercase font-bold shrink-0">FIDIC Clause 8.4 Enforced</span>
    </div>
'''
if 'id="winter-climate-banner"' not in html:
    html = html.replace('</header>', '</header>\n' + banner_html, 1)

# 4. Enhance Tab 5 (Escrow) with SHA-256 Ledger Export & Live Feed
escrow_marker = 'id="view-escrow"'
if escrow_marker in html and 'ledgerExportDocket' not in html:
    escrow_pos = html.find(escrow_marker)
    # Find next section tag or insert inside escrow header
    ledger_btn = '''
        <div class="flex items-center justify-between gap-3 p-4 rounded-2xl bg-amber-500/10 border border-amber-500/30 mb-6">
          <div>
            <div class="text-xs font-bold text-amber-600 dark:text-amber-400 flex items-center gap-1.5">
              <i data-lucide="shield-check" class="w-4 h-4"></i>
              IMMUTABLE FIDIC AUDIT CHAIN // INDEXEDDB SHA-256
            </div>
            <div class="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">
              Every sign-off produces a legally defensible cryptographic block for arbitration before the Chamber of Commerce FBiH.
            </div>
          </div>
          <button onclick="ledgerExportDocket()" class="px-3.5 py-2 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 text-xs font-bold transition flex items-center gap-2 shadow-lg shadow-amber-500/20 shrink-0">
            <i data-lucide="download" class="w-4 h-4"></i>
            Export Verified Docket (JSON)
          </button>
        </div>
    '''
    # insert right after <section id="view-escrow" ... >
    sec_end = html.find('>', escrow_pos)
    html = html[:sec_end+1] + '\n' + ledger_btn + html[sec_end+1:]

# 5. Enhance Tab 9 (Buyer Portal) with Dino's Variation Orders & 1-Click Bank Slip
buyer_marker = 'id="view-buyer-portal"'
if buyer_marker in html and 'generateBankPaymentSlip' not in html:
    buyer_pos = html.find(buyer_marker)
    sec_end = html.find('>', buyer_pos)
    buyer_upgrades = '''
      <!-- DINO'S PLAIN-LANGUAGE OWNER CONTROLS & EPC PAYMENT SLIP -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
        <!-- Variation Order Customizer -->
        <div class="card-inner p-5 space-y-4 lg:col-span-2">
          <div class="flex items-center justify-between border-b border-slate-100 dark:border-white/5 pb-3">
            <div>
              <div class="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-2">
                <i data-lucide="sliders" class="w-4 h-4 text-amber-500"></i>
                Villa K-018 // Interactive Variation Order Engine
              </div>
              <div class="text-xs text-slate-400">Click finishes to automatically recalculate your contract balance and escrow schedule.</div>
            </div>
            <span class="text-xs font-mono px-2 py-0.5 rounded bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 font-bold">Contract Active</span>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
            <label class="flex items-center justify-between p-3 rounded-xl border border-slate-200 dark:border-white/10 hover:border-amber-500/50 cursor-pointer transition">
              <div class="flex items-center gap-2.5">
                <input type="checkbox" onchange="toggleUpgrade('carraraMarble', 6800)" class="rounded text-amber-500 focus:ring-amber-500">
                <span>Porcelanosa Carrara Marble</span>
              </div>
              <span class="font-mono text-amber-500 font-semibold">+€6,800</span>
            </label>

            <label class="flex items-center justify-between p-3 rounded-xl border border-slate-200 dark:border-white/10 hover:border-amber-500/50 cursor-pointer transition">
              <div class="flex items-center gap-2.5">
                <input type="checkbox" onchange="toggleUpgrade('heatedPool', 18500)" class="rounded text-amber-500 focus:ring-amber-500">
                <span>Private Heated Infinity Pool</span>
              </div>
              <span class="font-mono text-amber-500 font-semibold">+€18,500</span>
            </label>

            <label class="flex items-center justify-between p-3 rounded-xl border border-slate-200 dark:border-white/10 hover:border-amber-500/50 cursor-pointer transition">
              <div class="flex items-center gap-2.5">
                <input type="checkbox" onchange="toggleUpgrade('solarGlazing', 9400)" class="rounded text-amber-500 focus:ring-amber-500">
                <span>Schüco BIPV Solar Glazing</span>
              </div>
              <span class="font-mono text-amber-500 font-semibold">+€9,400</span>
            </label>

            <label class="flex items-center justify-between p-3 rounded-xl border border-slate-200 dark:border-white/10 hover:border-amber-500/50 cursor-pointer transition">
              <div class="flex items-center gap-2.5">
                <input type="checkbox" onchange="toggleUpgrade('smartHomeApex', 5200)" class="rounded text-amber-500 focus:ring-amber-500">
                <span>Apex Smart Automation Hub</span>
              </div>
              <span class="font-mono text-amber-500 font-semibold">+€5,200</span>
            </label>
          </div>

          <div class="flex items-center justify-between pt-2 border-t border-slate-100 dark:border-white/5 text-xs">
            <span class="text-slate-400">Selected Upgrades Total: <strong id="buyer-calc-upgrades-total" class="text-amber-500">+€0</strong></span>
            <div class="text-right">
              <span class="text-slate-400">New Contract Value: </span>
              <strong id="buyer-calc-total-price" class="text-base text-slate-900 dark:text-white font-mono font-bold">€450,000</strong>
            </div>
          </div>
        </div>

        <!-- 1-Click Bank Deposit Slip Card -->
        <div class="card-inner p-5 space-y-3.5 flex flex-col justify-between">
          <div>
            <div class="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-2">
              <i data-lucide="receipt" class="w-4 h-4 text-emerald-500"></i>
              Escrow Stage 2 Call // UniCredit
            </div>
            <div class="text-xs text-slate-400 mt-1">Superstructure Milestone reached. 30% stage drawdown authorized by Sinteza Engineer.</div>
            
            <div class="mt-3 p-3 rounded-xl bg-slate-50 dark:bg-white/5 border border-slate-200 dark:border-white/10 font-mono text-xs space-y-1">
              <div class="flex justify-between"><span>Amount Due:</span><strong id="buyer-calc-stage2-val" class="text-emerald-500">€135,000</strong></div>
              <div class="flex justify-between text-[11px] text-slate-400"><span>Trustee:</span><span>UniCredit Mostar</span></div>
              <div class="flex justify-between text-[11px] text-slate-400"><span>IBAN:</span><span>BA39...4455</span></div>
            </div>
          </div>

          <button onclick="generateBankPaymentSlip()" class="w-full py-2.5 px-4 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 text-xs font-bold transition flex items-center justify-center gap-2 shadow-lg shadow-emerald-500/20">
            <i data-lucide="printer" class="w-4 h-4"></i>
            Print Bank Deposit Slip (QR / IBAN)
          </button>
        </div>
      </div>
    '''
    html = html[:sec_end+1] + '\n' + buyer_upgrades + html[sec_end+1:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully upgraded index.html with Aethel Apex v2.0 Hardening!')
