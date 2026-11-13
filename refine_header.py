import re

path = r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's clean up the top header and move the controls to be ultra-clean:
# In the header, keep it single line flex-wrap:
clean_header = '''
    <!-- Top Thin Utility Bar (Ultra-Slim 48px) -->
    <header class="py-2.5 px-6 border-b border-slate-200 dark:border-white/10 bg-white/80 dark:bg-[#07090C]/80 backdrop-blur-md sticky top-0 z-20 flex items-center justify-between gap-3 flex-wrap">
      <div class="flex items-center gap-2.5">
        <span class="text-[11px] font-mono text-slate-400 uppercase tracking-wider">Role Lens:</span>
        <div class="flex items-center p-0.5 bg-slate-100 dark:bg-white/5 rounded-xl border border-slate-200 dark:border-white/10 text-xs">
          <button onclick="setStakeholderRole('all')" id="role-btn-all" class="role-pill-btn px-2.5 py-1 rounded-lg bg-amber-500 text-slate-950 font-bold transition">All</button>
          <button onclick="setStakeholderRole('developer')" id="role-btn-developer" class="role-pill-btn px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition">Developer</button>
          <button onclick="setStakeholderRole('constructor')" id="role-btn-constructor" class="role-pill-btn px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition">Constructor</button>
          <button onclick="setStakeholderRole('architect')" id="role-btn-architect" class="role-pill-btn px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition">Architect</button>
          <button onclick="setStakeholderRole('consultant')" id="role-btn-consultant" class="role-pill-btn px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition">FIDIC Legal</button>
          <button onclick="setStakeholderRole('buyer')" id="role-btn-buyer" class="role-pill-btn px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition">Buyer</button>
        </div>
      </div>

      <div class="flex items-center gap-2">
        <!-- Master Traffic Light Status -->
        <div id="master-traffic-light" class="px-2.5 py-1 rounded-full text-[11px] font-bold flex items-center gap-1.5 bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 border border-emerald-500/30">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          <span id="traffic-light-label">ALL NOMINAL</span>
        </div>

        <!-- Winter Climate Engine Toggle -->
        <button id="btn-toggle-winter-freeze" onclick="toggleWinterFreezeMode()" 
                class="px-2 py-1 rounded-lg border border-slate-200 dark:border-white/10 bg-slate-50 dark:bg-white/5 text-[11px] font-semibold text-slate-600 dark:text-slate-300 hover:border-amber-500/50 transition">
          ☀️ +18°C
        </button>

        <!-- Plain Language Lens Toggle -->
        <button id="btn-toggle-jargon" onclick="toggleJargonLens()" 
                class="px-2 py-1 rounded-lg border border-slate-200 dark:border-white/10 bg-slate-50 dark:bg-white/5 text-[11px] font-semibold text-slate-600 dark:text-slate-300 hover:border-amber-500/50 transition">
          👓 Plain Lens
        </button>

        <!-- Quad-Language Switcher -->
        <div class="flex items-center p-0.5 bg-slate-100 dark:bg-white/5 rounded-lg border border-slate-200 dark:border-white/10 text-[10px] font-mono">
          <button id="lang-btn-en" onclick="setPortalLanguage('en')" class="px-1.5 py-0.5 rounded bg-amber-500 text-white font-bold transition">EN</button>
          <button id="lang-btn-bs" onclick="setPortalLanguage('bs')" class="px-1.5 py-0.5 rounded text-slate-400 hover:text-white transition">BS</button>
          <button id="lang-btn-de" onclick="setPortalLanguage('de')" class="px-1.5 py-0.5 rounded text-slate-400 hover:text-white transition">DE</button>
          <button id="lang-btn-ar" onclick="setPortalLanguage('ar')" class="px-1.5 py-0.5 rounded text-slate-400 hover:text-white transition">AR</button>
        </div>
      </div>
    </header>
'''

# Replace header block
start_header = html.find('<header')
end_header = html.find('</header>') + len('</header>')
if start_header != -1 and end_header != -1:
    html = html[:start_header] + clean_header + html[end_header:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Clean header applied successfully!')
