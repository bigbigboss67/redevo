// Universal Interactive Workflow Engine: Step-by-Step Guided Navigation for Non-Professionals
// Bridges Developer, Constructor, Architect, Consultant & Non-Professional Users

const STAKEHOLDER_GUIDES = {
  all: {
    roleTitle: "All Stakeholders // Executive High-Level",
    icon: "globe",
    badge: "Universal Overview",
    audience: "Universal Stakeholder",
    objective: "Track total project delivery, capital allocation, and milestone unlocks across all 120 villas and 5 landmark buildings.",
    steps: [
      {
        stepNum: 1,
        title: "Executive Master Cockpit",
        desc: "Inspect top-level GDV (€97.0M total), collected funds, escrow balance, and live site telemetry.",
        targetTab: "cockpit",
        actionLabel: "Open Cockpit"
      },
      {
        stepNum: 2,
        title: "The 5 Landmark Buildings",
        desc: "Inspect the 5 iconic structures shaped as 'I LOVE BOSNIA' (Clinic, Resort, Mosque, Sports, Village).",
        targetTab: "landmark-buildings",
        actionLabel: "Inspect 5 Buildings"
      },
      {
        stepNum: 3,
        title: "120-Plot Master Layout",
        desc: "View the hillside villa layout forming 'I LOVE BOSNIA' across the Breza hillside.",
        targetTab: "matrix",
        actionLabel: "View Villa Matrix"
      },
      {
        stepNum: 4,
        title: "Sovereign Underwriting & Ingestion",
        desc: "Upload architecture, DCF pro-forma, Monte Carlo risks, and automatic tranche invoicing.",
        targetTab: "bizdev-engine",
        actionLabel: "Launch BizDev OS"
      }
    ]
  },
  architect: {
    roleTitle: "Lead Architect & Design Consultant",
    icon: "compass",
    badge: "Design & Quality Assurance",
    audience: "Architect & Spatial Designer",
    objective: "Verify design compliance, check typographic geometry of the 5 buildings, inspect 3D IFC models, and drop defect pins.",
    steps: [
      {
        stepNum: 1,
        title: "Inspect the 5 'I LOVE BOSNIA' Landmark Buildings",
        desc: "Review structural geometry for the 'I' Clinic, '♥' Heart Hotel, 'B' Mosque, 'O' Arena & 'SNIA' Village.",
        targetTab: "landmark-buildings",
        actionLabel: "Audit 5 Buildings"
      },
      {
        stepNum: 2,
        title: "Review 3D IFC & LiDAR Point Cloud",
        desc: "Examine drone point clouds and ensure foundations match architectural BIM tolerances (±2.8mm).",
        targetTab: "digital-twin",
        actionLabel: "Inspect 3D Twin"
      },
      {
        stepNum: 3,
        title: "Interactive CAD Floorplan Snagging",
        desc: "Drop visual defect pins directly onto the 300m² villa blueprint with 24h contractor SLA timers.",
        targetTab: "bizdev-engine",
        subTab: "snagging-canvas",
        actionLabel: "Drop Defect Pin"
      },
      {
        stepNum: 4,
        title: "AI Value Engineering Verification",
        desc: "Audit the €1.42M specification optimizations without compromising luxury aesthetic standards.",
        targetTab: "bizdev-engine",
        modal: "ve-modal",
        actionLabel: "Open VE Audit"
      }
    ]
  },
  constructor: {
    roleTitle: "General Contractor & Site Superintendent",
    icon: "hard-hat",
    badge: "Field Operations & Safety",
    audience: "Site Manager & Civil Engineer",
    objective: "Oversee site biometrics, manage subcontractor SLAs, coordinate the 5 major buildings, and resolve snag pins.",
    steps: [
      {
        stepNum: 1,
        title: "Monitor Daily Biometrics & Headcount",
        desc: "Check 142 biometrically clocked craftsmen across Ulaz 1–7 gates and subcontractor attendance.",
        targetTab: "contractor-sla",
        actionLabel: "View Field SLAs"
      },
      {
        stepNum: 2,
        title: "Coordinate 5 Major Commercial Buildings",
        desc: "Track raft pours and steel framing across the 'I' Clinic, '♥' Hotel, and 'O' Equestrian Hub.",
        targetTab: "landmark-buildings",
        actionLabel: "View Building Progress"
      },
      {
        stepNum: 3,
        title: "4D Construction Progress Simulation",
        desc: "Scrub the 24-month visual timeline to coordinate subcontractor pour sequences and staging zones.",
        targetTab: "bizdev-engine",
        modal: "sim4d-modal",
        actionLabel: "Run 4D Simulation"
      },
      {
        stepNum: 4,
        title: "Clear Snag Defect Punch Pins",
        desc: "Review open punch pins logged on CAD drawings and sign off contractor completion to release holdbacks.",
        targetTab: "bizdev-engine",
        subTab: "snagging-canvas",
        actionLabel: "Clear Punch Items"
      }
    ]
  },
  developer: {
    roleTitle: "Real Estate Developer & Asset Sponsor",
    icon: "briefcase",
    badge: "Investment & Capital Governance",
    audience: "Developer & Executive Sponsor",
    objective: "Maximize project IRR (26.4%), ensure off-plan collections across villas & commercial buildings, and approve stage-gates.",
    steps: [
      {
        stepNum: 1,
        title: "Executive GDV & Master Portfolio Health",
        desc: "Review €97.0M total GDV (€54.2M Villas + €42.8M 5 Landmark Buildings), 26.4% IRR, and net margins.",
        targetTab: "cockpit",
        actionLabel: "Inspect Portfolio"
      },
      {
        stepNum: 2,
        title: "5 Landmark Buildings Capex & Pre-Leasing",
        desc: "Audit commercial yields and pre-leasing for the Hotel, Medical Clinic, and Retail Crescent.",
        targetTab: "landmark-buildings",
        actionLabel: "Review Commercials"
      },
      {
        stepNum: 3,
        title: "Off-Plan Cash Flow & Collections S-Curve",
        desc: "Trigger automated milestone tranche calls under the 50/50 payment plan (1% EOI, 4% SPA, 40% Build).",
        targetTab: "bizdev-engine",
        subTab: "collections",
        actionLabel: "View S-Curve"
      },
      {
        stepNum: 4,
        title: "Double-Entry Sovereign ERP Trial Balance",
        desc: "Audit the balanced trial balance across villa assets, commercial holdings, and escrow reserves.",
        targetTab: "bizdev-engine",
        subTab: "internal-erp",
        actionLabel: "Audit Ledger"
      }
    ]
  },
  consultant: {
    roleTitle: "FIDIC Engineer, Legal Counsel & Bank Trustee",
    icon: "scale",
    badge: "Escrow & FIDIC Compliance",
    audience: "Independent Engineer & Trustee",
    objective: "Enforce FIDIC Clause 20 28-day claim bar, verify commercial building milestones, and execute multi-sig escrow draws.",
    steps: [
      {
        stepNum: 1,
        title: "FIDIC 4-Entity Multi-Sig Escrow Vault",
        desc: "Review UniCredit/BBI escrow tranches requiring Developer, Engineer, Bank, and Municipality signatures.",
        targetTab: "escrow",
        actionLabel: "Inspect Multi-Sig"
      },
      {
        stepNum: 2,
        title: "Certify 5 Landmark Commercial Milestones",
        desc: "Inspect raft foundations, anchor bolts, and core pours for the 5 'I LOVE BOSNIA' buildings.",
        targetTab: "landmark-buildings",
        actionLabel: "Certify Buildings"
      },
      {
        stepNum: 3,
        title: "FIDIC Sub-Clause 20.2 Time-Bar Guard",
        desc: "Monitor the 28-day statutory notice countdown to prevent contractor claims from becoming time-barred.",
        targetTab: "fidic-claims",
        actionLabel: "Review Claims"
      },
      {
        stepNum: 4,
        title: "Monte Carlo Risk Contingency Simulation",
        desc: "Simulate geotechnical karst risks, winter frost delays, and EUR/BAM currency peg stability.",
        targetTab: "bizdev-engine",
        subTab: "risk-mgmt",
        actionLabel: "Evaluate Risks"
      }
    ]
  },
  buyer: {
    roleTitle: "Villa Buyer & VIP Homeowner",
    icon: "home",
    badge: "Homeowner Experience",
    audience: "Property Buyer / Investor",
    objective: "Track your villa's physical build progress, watch live 4K site cameras, and explore resort amenities.",
    steps: [
      {
        stepNum: 1,
        title: "Explore Resort Amenities & Landmark Buildings",
        desc: "Discover the Heart Hotel, Medical Clinic, Equestrian Center, and Lake Promenade near your villa.",
        targetTab: "landmark-buildings",
        actionLabel: "Explore Resort"
      },
      {
        stepNum: 2,
        title: "Find Your Villa in the Master Plan",
        desc: "Explore your villa's location within the hillside letter formations (I, LOVE, BOSNIA).",
        targetTab: "matrix",
        actionLabel: "Locate My Villa"
      },
      {
        stepNum: 3,
        title: "Buyer 360° VIP Portal & 4K Live Camera",
        desc: "Access your dedicated portal for Plot K-018, view live feeds, and check milestone completion.",
        targetTab: "buyer-portal",
        actionLabel: "Open My Portal"
      },
      {
        stepNum: 4,
        title: "Customize Finishes & Download Inspection Report",
        desc: "Choose between Italian Porcelanosa Marble or Oak, and download your QR-verified inspection report.",
        targetTab: "buyer-portal",
        actionLabel: "VIP Choices"
      }
    ]
  }
};

let currentGuideStepIndex = 0;

function renderWorkflowGuide(roleKey) {
  const guide = STAKEHOLDER_GUIDES[roleKey] || STAKEHOLDER_GUIDES.all;
  const container = document.getElementById('step-by-step-guide-container');
  if (!container) return;

  let stepsHtml = '';
  guide.steps.forEach((step, idx) => {
    stepsHtml += `
      <div class="relative flex-1 p-3.5 rounded-2xl border transition-all duration-300 ${idx === currentGuideStepIndex ? 'bg-amber-500/10 border-amber-500 shadow-md ring-1 ring-amber-500/30' : 'bg-slate-50 dark:bg-white/[0.02] border-slate-200 dark:border-white/5 hover:border-slate-300 dark:hover:border-white/10'}">
        <div class="flex items-center justify-between mb-1.5">
          <span class="inline-flex items-center justify-center w-6 h-6 rounded-full font-mono text-xs font-bold ${idx === currentGuideStepIndex ? 'bg-amber-500 text-slate-950' : 'bg-slate-200 dark:bg-white/10 text-slate-600 dark:text-slate-300'}">
            ${step.stepNum}
          </span>
          <span class="text-[10px] font-mono uppercase tracking-wider text-slate-600 dark:text-slate-300">Step ${step.stepNum} of ${guide.steps.length}</span>
        </div>
        <h4 class="text-xs font-bold text-slate-900 dark:text-white truncate mb-1">${step.title}</h4>
        <p class="text-[11px] text-slate-700 dark:text-slate-300 leading-snug line-clamp-2 mb-3">${step.desc}</p>
        <button onclick="executeGuideStep('${roleKey}', ${idx})" class="w-full py-1.5 px-3 rounded-xl text-xs font-bold font-mono transition flex items-center justify-center gap-1.5 ${idx === currentGuideStepIndex ? 'bg-amber-500 hover:bg-amber-400 text-slate-950 shadow-sm' : 'bg-slate-200 dark:bg-white/10 hover:bg-slate-300 dark:hover:bg-white/20 text-slate-800 dark:text-slate-200'}">
          <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i> ${step.actionLabel}
        </button>
      </div>
    `;
  });

  container.innerHTML = `
    <div class="card-inner p-4 space-y-3">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-2.5 border-b border-slate-100 dark:border-white/5">
        <div class="flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-xl bg-amber-500/20 text-amber-600 dark:text-amber-400 flex items-center justify-center">
            <i data-lucide="${guide.icon}" class="w-4 h-4"></i>
          </div>
          <div>
            <div class="flex items-center gap-2">
              <span class="text-xs font-mono font-bold text-amber-600 dark:text-amber-400 uppercase tracking-wider">GUIDED WALKTHROUGH</span>
              <span class="px-2 py-0.5 rounded-full bg-slate-100 dark:bg-white/5 border border-slate-200 dark:border-white/10 text-[10px] font-mono text-slate-500 dark:text-slate-400">${guide.badge}</span>
            </div>
            <h3 class="text-sm font-bold text-slate-900 dark:text-white">${guide.roleTitle}</h3>
          </div>
        </div>
        <p class="text-xs text-slate-700 dark:text-slate-300 max-w-md sm:text-right font-medium">${guide.objective}</p>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
        ${stepsHtml}
      </div>
    </div>
  `;

  if (window.lucide) lucide.createIcons();
}

function executeGuideStep(roleKey, stepIdx) {
  currentGuideStepIndex = stepIdx;
  const guide = STAKEHOLDER_GUIDES[roleKey] || STAKEHOLDER_GUIDES.all;
  const step = guide.steps[stepIdx];
  if (!step) return;

  // Switch to the target tab
  if (step.targetTab) {
    switchTab(step.targetTab);
  }

  // Switch to sub-tab if specified
  if (step.subTab && typeof switchBizSubTab === 'function') {
    setTimeout(() => {
      switchBizSubTab(step.subTab);
    }, 100);
  }

  // Open modal if specified
  if (step.modal && typeof openModal === 'function') {
    setTimeout(() => {
      openModal(step.modal);
    }, 200);
  }

  // Re-render guide to update active styling
  renderWorkflowGuide(roleKey);
}
