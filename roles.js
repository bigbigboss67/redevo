// Role switcher definitions and audience badge styling
const ROLES = {
  all: {
    name: 'All Stakeholders',
    badge: 'Universal Overview',
    desc: 'Complete cross-functional project transparency and governance',
    recommendedTab: 'cockpit'
  },
  developer: {
    name: 'Real Estate Developer',
    badge: 'Executive & Investment',
    desc: 'Capital deployment, GDV yield, off-plan collections, IRR & stage-gates',
    recommendedTab: 'bizdev-engine'
  },
  constructor: {
    name: 'General Contractor',
    badge: 'Site & Field Operations',
    desc: 'WBS schedule, subcontractor SLAs, concrete lab tests, turnstile biometrics',
    recommendedTab: 'contractor-sla'
  },
  architect: {
    name: 'Lead Architect & Engineer',
    badge: 'Design & BIM 4D',
    desc: '3D IFC point cloud, CAD floorplan snagging pins, ±2.8mm LiDAR tolerances',
    recommendedTab: 'digital-twin'
  },
  consultant: {
    name: 'FIDIC Legal & Bank Trustee',
    badge: 'Escrow & Legal Compliance',
    desc: 'FIDIC Clause 20 28-day statutory bar, 4-entity multi-sig escrow tranches',
    recommendedTab: 'escrow'
  },
  buyer: {
    name: 'Villa Buyer / Investor',
    badge: 'VIP Homeowner Portal',
    desc: 'Villa milestone verification, live 4K site cameras, material customization',
    recommendedTab: 'buyer-portal'
  }
};

let activeRole = 'all';

function setStakeholderRole(roleKey) {
  activeRole = roleKey;
  const role = ROLES[roleKey];
  if (!role) return;

  // Update role buttons
  document.querySelectorAll('.role-pill-btn').forEach(btn => {
    btn.classList.remove('bg-amber-500', 'text-slate-950', 'font-bold', 'shadow-sm');
    btn.classList.add('text-slate-600', 'dark:text-slate-300', 'hover:bg-slate-100', 'dark:hover:bg-slate-800');
  });
  const activeBtn = document.getElementById(`role-btn-${roleKey}`);
  if (activeBtn) {
    activeBtn.classList.remove('text-slate-600', 'dark:text-slate-300', 'hover:bg-slate-100', 'dark:hover:bg-slate-800');
    activeBtn.classList.add('bg-amber-500', 'text-slate-950', 'font-bold', 'shadow-sm');
  }

  // Update banner text
  const roleBannerTitle = document.getElementById('role-banner-title');
  const roleBannerDesc = document.getElementById('role-banner-desc');
  const roleBadgeText = document.getElementById('role-badge-text');
  if (roleBannerTitle) roleBannerTitle.innerText = `${role.name} View`;
  if (roleBannerDesc) roleBannerDesc.innerText = role.desc;
  if (roleBadgeText) roleBadgeText.innerText = role.badge;

  // Highlight recommended tab
  if (role.recommendedTab && roleKey !== 'all') {
    switchTab(role.recommendedTab);
  }
}
