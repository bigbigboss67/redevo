// Building Inspector Engine for the 5 Landmark I LOVE BOSNIA Buildings

const BUILDINGS_DATA = {
  'bldg-1': {
    badge: "BUILDING 1 // LETTER 'I'",
    badgeClass: "bg-cyan-400/20 text-cyan-600 dark:text-cyan-300",
    title: "The 'I' Medical Wellness & Diagnostic Clinic",
    date: "Q3 2027 (On Schedule)",
    desc: "Monolithic vertical glass pavilion shaped as the letter 'I', serving as the gateway beacon to the Breza resort. Features thermal hydrotherapy pools, cardiology & diagnostic suite, and doctor residences.",
    contractor: "Euro-Asfalt d.o.o.",
    value: "€7,800,000",
    progress: "42%"
  },
  'bldg-2': {
    badge: "BUILDING 2 // HEART '♥' RESORT",
    badgeClass: "bg-rose-500/20 text-rose-500",
    title: "The Heart Luxury Resort & Boutique 5-Star Hotel",
    date: "Q4 2027 (Foundations Underway)",
    desc: "Sculpted in the literal shape of a heart on the mountain ridge. Features 85 panoramic suites, a heart-shaped infinity pool cantilevered over the pine valley, and a suspended glass wedding terrace.",
    contractor: "Sinteza Construction JV",
    value: "€16,400,000",
    progress: "28%"
  },
  'bldg-3': {
    badge: "BUILDING 3 // LETTER 'B'",
    badgeClass: "bg-amber-400/20 text-amber-600 dark:text-amber-400",
    title: "Grand Cultural Center, Library & Mosque Pavilion",
    date: "Q2 2027 (Ahead of Schedule)",
    desc: "An organic geometric pavilion shaped as the letter 'B'. Serves as the spiritual and cultural heart of the resort with a quiet forest mosque, community auditorium, and Bosnian cultural heritage archives.",
    contractor: "Breza Municipal Works",
    value: "€4,200,000",
    progress: "74%"
  },
  'bldg-4': {
    badge: "BUILDING 4 // LETTER 'O'",
    badgeClass: "bg-purple-400/20 text-purple-600 dark:text-purple-400",
    title: "Highland Sports Academy & Equestrian Riding Hall",
    date: "Q3 2027 (Steel Framing)",
    desc: "Circular stadium and stable complex shaped as the letter 'O'. Features scenic indoor horse-riding tracks, clay tennis courts, bouldering gym, and mountain trail bike rental hub.",
    contractor: "Bosna Beton d.d.",
    value: "€5,600,000",
    progress: "51%"
  },
  'bldg-5': {
    badge: "BUILDING 5 // LETTERS 'SNIA'",
    badgeClass: "bg-emerald-400/20 text-emerald-600 dark:text-emerald-400",
    title: "Artisan Mountain Village, Dining Promenade & Retail",
    date: "Q4 2027 (MEP Rough-In)",
    desc: "Terraced lakeside retail and gastronomic crescent shaped as 'S-N-I-A'. Features farm-to-table organic dining, craft bakeries, artisan boutiques, and a floating summer amphitheater.",
    contractor: "Alu-Façade Austria",
    value: "€8,800,000",
    progress: "35%"
  }
};

function selectBuildingDetails(bldgKey) {
  const b = BUILDINGS_DATA[bldgKey];
  if (!b) return;

  // Highlight card
  document.querySelectorAll('.building-card').forEach(c => {
    c.classList.remove('border-2', 'border-amber-500', 'shadow-lg');
  });
  const activeCard = document.getElementById(`card-${bldgKey}`);
  if (activeCard) {
    activeCard.classList.add('border-2', 'border-amber-500', 'shadow-lg');
  }

  // Update inspector panel
  const badgeEl = document.getElementById('inspect-bldg-badge');
  const titleEl = document.getElementById('inspect-bldg-title');
  const dateEl = document.getElementById('inspect-bldg-date');
  const descEl = document.getElementById('inspect-bldg-desc');

  if (badgeEl) {
    badgeEl.innerText = b.badge;
    badgeEl.className = `px-3 py-1 rounded-xl font-mono font-bold text-xs ${b.badgeClass}`;
  }
  if (titleEl) titleEl.innerText = b.title;
  if (dateEl) dateEl.innerText = b.date;
  if (descEl) descEl.innerText = b.desc;
}

function simulateBuildingInspection() {
  alert("Running 5-Building BIM & LiDAR Structural Audit:\n\n1. Building 'I' Clinic: Raft foundation within ±1.6mm tolerance.\n2. Building '♥' Hotel: Excavation 100% complete. Anchor bolts certified.\n3. Building 'B' Mosque: Roof timber trusses installed. Glazing next.\n4. Building 'O' Equestrian: Steel frames assembled.\n5. Building 'SNIA' Retail: MEP piping pass hydrostatic tests.\n\nCombined 5-building milestone verified for FIDIC Escrow certificate.");
}

function certifyBuildingTranche() {
  alert("Commercial Milestone Release Certified!\nIndependent Engineer and UniCredit Trustee tokens applied.\nConstruction tranche recorded in balanced sovereign ERP ledger.");
}
