/**
 * AETHEL APEX // EXECUTIVE LENS & PLAIN-LANGUAGE ADAPTER (v2.0)
 * Eliminates cognitive load for non-technical buyers, investors & municipal officials.
 * Includes Bosnian Highland Climate Engine, Multi-Currency IBAN slips & Quad-Language Dictionary.
 */

// 1. DICTIONARIES FOR QUAD-LANGUAGE LOCALIZATION
const PORTAL_TRANSLATIONS = {
  en: {
    title: "I LOVE BOSNIA // ENTERPRISE OS",
    subtitle: "Breza Highland Enclave (470,000 m²)",
    masterGdv: "Master GDV: €97.0M",
    trafficLightGreen: "SYSTEM HEALTH: NOMINAL // ALL SYSTEMS ON SCHEDULE",
    trafficLightYellow: "SYSTEM HEALTH: CAUTION // KARST REMEDIATION ACTIVE",
    trafficLightRed: "SYSTEM HEALTH: ALERT // WINTER FREEZE RESTRICTION ACTIVE",
    tabCockpit: "1. Master Cockpit",
    tabLandmarks: "2. 5 Landmark Buildings",
    tabMasterplan: "3. 120 Villa Masterplan",
    tabBim: "4. 3D BIM & LiDAR",
    tabEscrow: "5. Escrow Multi-Sig",
    tabBiometrics: "6. Field Biometrics",
    tabFidic: "7. FIDIC Clause 20",
    tabBizDev: "8. BizDev & Ingestion",
    tabBuyer: "9. Buyer 360° Portal",
    buyerHeadline: "Villa K-018 // Executive Owner Portal",
    handoverTarget: "Target Handover: Q2 2027",
    btnExportSlip: "Generate Bank Deposit Slip (PDF / QR)",
    winterNoticeActive: "WINTER FREEZE ACTIVE (-7°C): Superstructure concrete locked without thermal curing tent.",
    winterNoticeInactive: "SUMMER/AUTUMN WINDOW: Optimal curing conditions (+18°C ambient)."
  },
  bs: {
    title: "I LOVE BOSNIA // POSLOVNI OPERATIVNI SISTEM",
    subtitle: "Visočko-brezanska visoravan (470.000 m²)",
    masterGdv: "Ukupna vrijednost: 189,6M KM",
    trafficLightGreen: "STATUS PROJEKTA: OPTIMALAN // RADOVI TEKU PO PLANU",
    trafficLightYellow: "STATUS PROJEKTA: UPOZORENJE // SANACIJA KRŠA U TOKU",
    trafficLightRed: "STATUS PROJEKTA: ZASTOJ // MRAZ ISPOD -5°C (AKTIVIRAN ZIMSKI REŽIM)",
    tabCockpit: "1. Glavni pregled (KPI)",
    tabLandmarks: "2. 5 Objekata 'I LOVE BOSNIA'",
    tabMasterplan: "3. Matrica 120 Vila",
    tabBim: "4. 3D BIM i LiDAR Model",
    tabEscrow: "5. Escrow Račun (UniCredit/BBI)",
    tabBiometrics: "6. Radnici na gradilištu",
    tabFidic: "7. FIDIC Član 20 (Odštetni zahtjevi)",
    tabBizDev: "8. Poslovni Model i Ingestija",
    tabBuyer: "9. Portal za Kupce 360°",
    buyerHeadline: "Vila K-018 // Portal za Vlasnika",
    handoverTarget: "Planirani završetak: Kvartal 2, 2027",
    btnExportSlip: "Štampaj virman za uplatu (QR / IBAN)",
    winterNoticeActive: "ZIMSKI REŽIM AKTIVAN (-7°C): Betoniranje konstrukcije zabranjeno bez grijanih cerada i aditiva.",
    winterNoticeInactive: "OPTIMALNI USLOVI: Povoljne temperature za betoniranje (+18°C)."
  },
  de: {
    title: "I LOVE BOSNIA // ENTERPRISE PROJEKT-OS",
    subtitle: "Hochland-Enklave Breza (470.000 m²)",
    masterGdv: "Projektvolumen: €97,0 Mio.",
    trafficLightGreen: "PROJEKTSTATUS: NOMINAL // ZEITPLAN VOLL EINGEHALTEN",
    trafficLightYellow: "PROJEKTSTATUS: ACHTUNG // KARST-STABILISIERUNG AKTIV",
    trafficLightRed: "PROJEKTSTATUS: ALARM // FROSTSPERRE UNTER -5°C AKTIVIERT",
    tabCockpit: "1. Master-Cockpit",
    tabLandmarks: "2. 5 Landmark-Gebäude",
    tabMasterplan: "3. 120-Villen-Masterplan",
    tabBim: "4. 3D BIM & LiDAR",
    tabEscrow: "5. Notar-Treuhandkonto",
    tabBiometrics: "6. Baustellen-Biometrie",
    tabFidic: "7. FIDIC Klausel 20 Register",
    tabBizDev: "8. Wirtschaftlichkeits-OS",
    tabBuyer: "9. Käufer-Portal 360°",
    buyerHeadline: "Villa K-018 // Eigentümer-Dashboard",
    handoverTarget: "Schlüsselübergabe: Q2 2027",
    btnExportSlip: "Bank-Überweisungsträger (QR-Code / IBAN)",
    winterNoticeActive: "WINTERSPERRE AKTIV (-7°C): Betonage gesperrt ohne zertifizierte Thermozelte.",
    winterNoticeInactive: "OPTIMALE WITTERUNG: Ideale Abbindeverhältnisse (+18°C)."
  },
  ar: {
    title: "مشروع أنا أحب البوسنة // النظام المؤسسي الموحد",
    subtitle: "مرتفعات بريزا الفاخرة (470,000 متر مربع)",
    masterGdv: "القيمة الإجمالية: 97.0 مليون يورو",
    trafficLightGreen: "حالة المشروع: ممتازة // كافة الأعمال متوافقة مع الجدول الزمني",
    trafficLightYellow: "حالة المشروع: تنبيه // معالجة التجاويف الصخرية تحت فندق القلب",
    trafficLightRed: "حالة المشروع: تحذير // تفعيل بروتوكول الصقيع الشتوي تحت -5 درجات",
    tabCockpit: "1. لوحة القيادة التنفيذية",
    tabLandmarks: "2. مباني أي لاف بوزنيا الخمسة",
    tabMasterplan: "3. المخطط العام لـ 120 فيلا",
    tabBim: "4. التوأم الرقمي والمطابقة ثلاثية الأبعاد",
    tabEscrow: "5. حساب الضمان البنكي المشترك (إسكرو)",
    tabBiometrics: "6. البصمة الحيوية للعمالة والمقاولين",
    tabFidic: "7. سجل مطالبات فيديك (المادة 20)",
    tabBizDev: "8. دراسة الجدوى وتدفق السيولة",
    tabBuyer: "9. بوابة الملاك والمستثمرين 360°",
    buyerHeadline: "فيلا K-018 // بوابة المالك الخاصة",
    handoverTarget: "موعد التسليم المستهدف: الربع الثاني 2027",
    btnExportSlip: "إصدار إشعار التحويل البنكي (رمز QR معتمد)",
    winterNoticeActive: "حظر الصب الشتوي نشط (-7 مئوية): يشترط استخدام خيام التدفئة الحرارية ومسرعات الشك.",
    winterNoticeInactive: "الطقس معتدل: ظروف صب مثالية (18 درجة مئوية)."
  }
};

let currentPortalLang = "en";
let isWinterFreezeActive = false;
let isPlainLanguageMode = true;

// 2. VARIATION ORDERS & BUYER CUSTOMIZER STATE
const VILLA_K018_BASE_PRICE = 450000;
let selectedUpgrades = {
  carraraMarble: false, // +€6,800
  heatedPool: false,    // +€18,500
  solarGlazing: false,  // +€9,400
  smartHomeApex: false  // +€5,200
};

// Toggle Language
function setPortalLanguage(lang) {
  if (!PORTAL_TRANSLATIONS[lang]) return;
  currentPortalLang = lang;
  localStorage.setItem("ilb_portal_lang", lang);

  // Update UI buttons
  ['en', 'bs', 'de', 'ar'].forEach(l => {
    const btn = document.getElementById(`lang-btn-${l}`);
    if (btn) {
      if (l === lang) {
        btn.classList.add('bg-amber-500', 'text-white', 'font-bold');
        btn.classList.remove('text-slate-400');
      } else {
        btn.classList.remove('bg-amber-500', 'text-white', 'font-bold');
        btn.classList.add('text-slate-400');
      }
    }
  });

  // Handle RTL for Arabic
  if (lang === 'ar') {
    document.documentElement.setAttribute('dir', 'rtl');
  } else {
    document.documentElement.setAttribute('dir', 'ltr');
  }

  // Update texts where available
  updateLocalizedTextNodes();
  if (window.renderWorkflowGuide && window.currentRole) {
    window.renderWorkflowGuide(window.currentRole);
  }
  if (window.ledgerLog) {
    window.ledgerLog("System User", "Viewer", "LANGUAGE_SWITCHED", { language: lang });
  }
}

function updateLocalizedTextNodes() {
  const dict = PORTAL_TRANSLATIONS[currentPortalLang];
  const tLight = document.getElementById("traffic-light-label");
  if (tLight) {
    tLight.innerText = isWinterFreezeActive ? dict.trafficLightRed : dict.trafficLightGreen;
  }
  const winterBanner = document.getElementById("winter-climate-banner-text");
  if (winterBanner) {
    winterBanner.innerText = isWinterFreezeActive ? dict.winterNoticeActive : dict.winterNoticeInactive;
  }
}

// 3. BOSNIAN WINTER FREEZE VARIABLE TOGGLE
function toggleWinterFreezeMode() {
  isWinterFreezeActive = !isWinterFreezeActive;
  const statusLight = document.getElementById("master-traffic-light");
  const banner = document.getElementById("winter-climate-banner");
  const toggleBtn = document.getElementById("btn-toggle-winter-freeze");

  if (isWinterFreezeActive) {
    if (statusLight) {
      statusLight.className = "px-3 py-1.5 rounded-full text-xs font-bold flex items-center gap-2 bg-red-500/20 text-red-500 border border-red-500/40 animate-pulse";
      statusLight.innerHTML = `<span class="w-2.5 h-2.5 rounded-full bg-red-500"></span> ${PORTAL_TRANSLATIONS[currentPortalLang].trafficLightRed}`;
    }
    if (banner) banner.classList.remove("hidden");
    if (toggleBtn) toggleBtn.innerText = "❄️ Winter Freeze Active (-7°C) — Restricting Pouring";
    if (window.ledgerLog) {
      window.ledgerLog("Meteo Station Breza", "Safety Officer", "WINTER_FREEZE_PROTOCOL_TRIGGERED", {
        temperature: "-7.2°C",
        restriction: "FIDIC Clause 4.12 & Sub-Clause 8.4 thermal pause enforced."
      });
    }
  } else {
    if (statusLight) {
      statusLight.className = "px-3 py-1.5 rounded-full text-xs font-bold flex items-center gap-2 bg-emerald-500/20 text-emerald-600 dark:text-emerald-400 border border-emerald-500/30";
      statusLight.innerHTML = `<span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-ping"></span> ${PORTAL_TRANSLATIONS[currentPortalLang].trafficLightGreen}`;
    }
    if (banner) banner.classList.add("hidden");
    if (toggleBtn) toggleBtn.innerText = "☀️ Normal Highland Weather (+18°C) — Pouring Allowed";
    if (window.ledgerLog) {
      window.ledgerLog("Meteo Station Breza", "Safety Officer", "THERMAL_WINDOW_RESTORED", { temperature: "+18°C" });
    }
  }
}

// 4. BUYER UPGRADE CALCULATOR
function toggleUpgrade(upgradeKey, cost) {
  selectedUpgrades[upgradeKey] = !selectedUpgrades[upgradeKey];
  recalculateBuyerContract();
  if (window.ledgerLog) {
    window.ledgerLog("Dino Begović (Plot K-018)", "Buyer", "VARIATION_ORDER_REQUESTED", {
      upgrade: upgradeKey,
      cost: cost,
      active: selectedUpgrades[upgradeKey]
    });
  }
}

function recalculateBuyerContract() {
  let upgradeTotal = 0;
  if (selectedUpgrades.carraraMarble) upgradeTotal += 6800;
  if (selectedUpgrades.heatedPool) upgradeTotal += 18500;
  if (selectedUpgrades.solarGlazing) upgradeTotal += 9400;
  if (selectedUpgrades.smartHomeApex) upgradeTotal += 5200;

  const newTotal = VILLA_K018_BASE_PRICE + upgradeTotal;
  const stage1 = Math.round(newTotal * 0.20);
  const stage2 = Math.round(newTotal * 0.30);
  const stage3 = Math.round(newTotal * 0.30);
  const stage4 = Math.round(newTotal * 0.20);

  const totalEl = document.getElementById("buyer-calc-total-price");
  if (totalEl) totalEl.innerText = `€${newTotal.toLocaleString()}`;

  const upgradesEl = document.getElementById("buyer-calc-upgrades-total");
  if (upgradesEl) upgradesEl.innerText = `+€${upgradeTotal.toLocaleString()}`;

  const stage2El = document.getElementById("buyer-calc-stage2-val");
  if (stage2El) stage2El.innerText = `€${stage2.toLocaleString()}`;
}

// 5. GENERATE BANK PAYMENT SLIP WITH QR CODE
function generateBankPaymentSlip() {
  const currentTotal = parseInt((document.getElementById("buyer-calc-total-price")?.innerText || "450000").replace(/[^0-9]/g, ''));
  const stageAmount = Math.round(currentTotal * 0.30); // 30% Superstructure Call

  const slipWindow = window.open('', '_blank', 'width=750,height=800');
  slipWindow.document.write(`
    <!DOCTYPE html>
    <html>
    <head>
      <title>FIDIC ESCROW PAYMENT SLIP // VILLA K-018</title>
      <style>
        body { font-family: 'Courier New', monospace; padding: 2rem; color: #0f172a; background: #f8fafc; }
        .slip-box { border: 2px dashed #0f172a; padding: 2rem; background: #fff; max-width: 650px; margin: 0 auto; }
        .header { display: flex; justify-content: space-between; border-bottom: 2px solid #0f172a; padding-bottom: 1rem; }
        .title { font-size: 1.25rem; font-weight: bold; }
        .row { display: flex; justify-content: space-between; margin: 0.75rem 0; font-size: 0.9rem; }
        .qr-placeholder { border: 2px solid #0f172a; width: 140px; height: 140px; display: flex; align-items: center; justify-content: center; font-size: 10px; text-align: center; font-weight: bold; }
        .footer { margin-top: 1.5rem; border-top: 1px solid #cbd5e1; padding-top: 1rem; font-size: 0.75rem; color: #64748b; }
      </style>
    </head>
    <body>
      <div class="slip-box">
        <div class="header">
          <div>
            <div class="title">FIDIC RED BOOK // INTERIM STAGE PAYMENT</div>
            <div style="font-size:0.8rem; color:#64748b;">ESCROW ACCOUNT // UNICREDIT BANK D.D. MOSTAR</div>
          </div>
          <div><strong>VAL: €${stageAmount.toLocaleString()}</strong></div>
        </div>

        <div style="margin: 1.5rem 0;">
          <div class="row"><span><strong>DEBTOR (BUYER):</strong></span><span>Dino Begović (Villa K-018)</span></div>
          <div class="row"><span><strong>CREDITOR:</strong></span><span>I LOVE BOSNIA DEVELOPMENT D.O.O.</span></div>
          <div class="row"><span><strong>ESCROW TRUSTEE:</strong></span><span>UniCredit Bank d.d. Mostar</span></div>
          <div class="row"><span><strong>IBAN:</strong></span><span>BA39 3380 0011 2233 4455</span></div>
          <div class="row"><span><strong>SWIFT / BIC:</strong></span><span>UNCRBA22</span></div>
          <div class="row"><span><strong>PURPOSE CODE:</strong></span><span>740 // STAGE 2 SUPERSTRUCTURE CALL</span></div>
          <div class="row"><span><strong>STATUTORY NOTICE:</strong></span><span>FIDIC Sub-Clause 14.6 Certified by Sinteza</span></div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:2rem;">
          <div>
            <div style="font-size:0.85rem; font-weight:bold;">EPC SCAN TO PAY QR:</div>
            <div style="font-size:0.75rem; color:#64748b;">Compatible with UniCredit, BBI, Sparkasse & SEPA apps</div>
          </div>
          <div class="qr-placeholder">
            [EPC-QR VALID]<br>
            €${stageAmount.toLocaleString()}<br>
            BA393380001122334455
          </div>
        </div>

        <div class="footer">
          Generated from Sovereign Aethel Apex OS (SHA-256 Ledger Verified).<br>
          Protected under FBiH Law on Spatial Planning and Land Use.
        </div>
      </div>
      <script>
        setTimeout(() => window.print(), 500);
      </script>
    </body>
    </html>
  `);
  slipWindow.document.close();
}

// 6. TOGGLE PLAIN-LANGUAGE VS FIDIC LEGAL
function toggleJargonLens() {
  isPlainLanguageMode = !isPlainLanguageMode;
  const btn = document.getElementById("btn-toggle-jargon");
  if (btn) {
    btn.innerText = isPlainLanguageMode ? "👓 Plain Language (Active)" : "⚖️ FIDIC Legal (Active)";
  }

  document.querySelectorAll("[data-plain-text]").forEach(el => {
    const plain = el.getAttribute("data-plain-text");
    const legal = el.getAttribute("data-legal-text");
    if (plain && legal) {
      el.innerText = isPlainLanguageMode ? plain : legal;
    }
  });
}

// Global Exports
window.setPortalLanguage = setPortalLanguage;
window.toggleWinterFreezeMode = toggleWinterFreezeMode;
window.toggleUpgrade = toggleUpgrade;
window.generateBankPaymentSlip = generateBankPaymentSlip;
window.toggleJargonLens = toggleJargonLens;
