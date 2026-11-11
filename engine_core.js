<!-- JAVASCRIPT SYSTEM ENGINE -->
  <script>
    const RATES = { EUR: 1.0, BAM: 1.95583, USD: 1.08, AED: 3.96 };
    const CURRENCY_SYMBOLS = { EUR: '€', BAM: 'KM ', USD: '$', AED: 'AED ' };
    let currentCurrency = 'EUR';

    const STAGES = [
      { name: 'fitout', label: 'Luxury Fitout', color: 'bg-emerald-500', count: 20 },
      { name: 'mep', label: 'MEP & Glazing', color: 'bg-cyan-500', count: 25 },
      { name: 'structure', label: 'Superstructure', color: 'bg-blue-500', count: 31 },
      { name: 'foundation', label: 'Foundation Pour', color: 'bg-amber-500', count: 22 },
      { name: 'earthworks', label: 'Geotech Excavation', color: 'bg-rose-500', count: 14 },
      { name: 'prep', label: 'Permit & Prep', color: 'bg-slate-600', count: 8 }
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
    STAGES.forEach(stage => {
      for (let i = 0; i < stage.count; i++) {
        const idNum = String(plotIdx).padStart(3, '0');
        const id = `K-${idNum}`;
        const sub = SUBCONTRACTORS[plotIdx % SUBCONTRACTORS.length];
        const basePrice = 450000 + (plotIdx * 250);
        const milestonePct = stage.name === 'fitout' ? 85 :
                             stage.name === 'mep' ? 65 :
                             stage.name === 'structure' ? 45 :
                             stage.name === 'foundation' ? 25 :
                             stage.name === 'earthworks' ? 10 : 5;

        PLOTS.push({
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
        });
        plotIdx++;
      }
    });

    function renderPlots(plotsToRender) {
      const container = document.getElementById('plots-container');
      if (!container) return;
      container.innerHTML = '';

      plotsToRender.forEach(p => {
        const card = document.createElement('div');
        card.className = `p-2.5 rounded-xl bg-white/[0.02] border border-white/5 hover:border-[#E5A93C]/50 hover:bg-white/[0.05] transition cursor-pointer flex flex-col justify-between group`;
        card.onclick = () => inspectPlotDetails(p.id);

        card.innerHTML = `
          <div class="flex items-center justify-between">
            <span class="text-[11px] font-mono font-bold text-white group-hover:text-[#E5A93C] transition">${p.id}</span>
            <span class="w-2 h-2 rounded-full ${p.colorClass}"></span>
          </div>
          <div class="mt-2 text-[10px] text-slate-400 truncate">${p.stageLabel}</div>
          <div class="mt-1 flex items-center justify-between text-[9px] font-mono text-slate-500">
            <span>${p.milestonePct}%</span>
            <span>300m²</span>
          </div>
        `;
        container.appendChild(card);
      });
    }

    function filterPlots(stage) {
      document.querySelectorAll('.filter-chip').forEach(btn => {
        btn.classList.remove('bg-white/10', 'font-semibold');
        btn.classList.add('bg-white/5');
      });
      event.target.classList.add('bg-white/10', 'font-semibold');

      if (stage === 'all') {
        renderPlots(PLOTS);
      } else {
        renderPlots(PLOTS.filter(p => p.stage === stage));
      }
    }

    function switchTab(viewId) {
      document.querySelectorAll('.tab-view').forEach(v => v.classList.add('hidden'));
      document.querySelectorAll('.nav-tab').forEach(b => {
        b.classList.remove('bg-white/10', 'text-white', 'font-semibold', 'shadow-sm');
        b.classList.add('text-slate-400');
      });

      const target = document.getElementById(`view-${viewId}`) || document.getElementById(viewId);
      if (target) target.classList.remove('hidden');

      const btn = document.getElementById(`tab-btn-${viewId}`);
      if (btn) {
        btn.classList.add('bg-white/10', 'text-white', 'font-semibold', 'shadow-sm');
        btn.classList.remove('text-slate-400');
      }

      if (viewId === 'matrix') {
        renderPlots(PLOTS);
      } else if (viewId === 'digital-twin') {
        initBimCanvas();
      }
    }

    function inspectPlotDetails(plotId) {
      const plot = PLOTS.find(p => p.id === plotId) || PLOTS[17];
      document.getElementById('drawer-plot-badge').innerText = `PLOT ${plot.id}`;
      document.getElementById('drawer-plot-title').innerText = `Villa ${plot.id} // 4-Bedroom Contemporary (300 m² BUA)`;
      document.getElementById('drawer-plot-stage').innerText = plot.stageLabel;
      
      const symbol = CURRENCY_SYMBOLS[currentCurrency];
      const rate = RATES[currentCurrency];
      const priceFormatted = Math.round(plot.priceEUR * rate).toLocaleString();
      const milestoneFormatted = Math.round((plot.priceEUR * (plot.milestonePct / 100)) * rate).toLocaleString();

      document.getElementById('drawer-plot-price').innerText = `${symbol}${priceFormatted}`;
      document.getElementById('drawer-plot-milestone').innerText = `${plot.milestonePct}% (${symbol}${milestoneFormatted})`;

      document.getElementById('plot-drawer').classList.remove('hidden');
    }

    function closePlotDrawer() {
      document.getElementById('plot-drawer').classList.add('hidden');
    }

    function openModal(id) {
      document.getElementById(id).classList.remove('hidden');
    }

    function closeModal(id) {
      document.getElementById(id).classList.add('hidden');
    }

    function triggerAiSynthesis() {
      const banner = document.getElementById('synthesis-banner');
      if (banner) {
        banner.classList.remove('hidden');
        setTimeout(() => {
          alert("AI Document Synthesis Complete!\n\n1. Ingested 148p Feasibility Study + 340MB IFC Architecture.\n2. Generated 7-Phase WBS Critical Path (11.4d Float).\n3. Underwrote DCF Model: €54.2M GDV, 26.4% IRR, €14.85M NPV.\n4. Calibrated 5 Monte Carlo Project Risks.\n5. Structured €54.2M Off-Plan Collections & Escrow Ledger.");
        }, 800);
      }
    }

    function simulateFileUpload() {
      alert("Multimodal File Ingestion Dialog:\nSelect project files (AutoCAD .dwg, Revit/IFC .ifc, Feasibility PDF, Pro-Forma Excel)...\n\nFile validated. Ready for AI project synthesis.");
    }

    function switchBizSubTab(tabId) {
      document.querySelectorAll('.biz-view').forEach(v => v.classList.add('hidden'));
      document.querySelectorAll('.biz-tab').forEach(b => {
        b.classList.remove('bg-white/10', 'text-white', 'font-semibold');
        b.classList.add('text-slate-400');
      });

      const target = document.getElementById(`biz-view-${tabId}`);
      if (target) target.classList.remove('hidden');

      const btn = document.getElementById(`biz-sub-${tabId}`);
      if (btn) {
        btn.classList.add('bg-white/10', 'text-white', 'font-semibold');
        btn.classList.remove('text-slate-400');
      }
    }

    function sendAutomatedTrancheInvoices() {
      alert("Off-Plan Collections Engine:\nDispatched 120 automated milestone collection notices with certified escrow payment vouchers to UniCredit/BBI Trust.");
    }

    function applyValueEngineeringSavings() {
      alert("Value Engineering Savings Applied!\nBaseline construction budget reduced by €1,420,000. Project margin increased to 40.8%.");
      closeModal('ve-modal');
    }

    function update4dSim(month) {
      document.getElementById('sim4d-slider-val').innerText = `Month ${month}`;
      document.getElementById('sim4d-month-text').innerText = `Month ${month} of 24 (Progressive Build)`;
      if (month < 6) {
        document.getElementById('sim4d-image').src = 'assets/images/masterplan_3d_numbered.jpg';
      } else if (month < 16) {
        document.getElementById('sim4d-image').src = 'assets/images/villa_facade_exterior.jpg';
      } else {
        document.getElementById('sim4d-image').src = 'assets/images/villa_facade_dusk.jpg';
      }
    }

    function downloadContractPDF() {
      alert("Exporting FIDIC EPC Silver Book Turnkey Agreement for I LOVE BOSNIA (PDF with e-Signature tokens)... Download complete.");
      closeModal('fidic-modal');
    }

    function approveMilestone() {
      alert("FIDIC Independent Engineer Certification Recorded!\nPayment tranche released to Escrow Sub-Account.");
      closePlotDrawer();
    }

    function generateFidicNotice() {
      alert("FIDIC Sub-Clause 20.2 Notice of Claim drafted. 28-day statutory bar countdown anchored to ledger.");
    }

    function signMunicipal() {
      alert("Breza Municipality Urban Planning Auditor: Signed.\nTranche release certified for 120 villas.");
    }

    function downloadOfficialInspectionCert() {
      alert("Generating Sinteza CAD & FIDIC Independent Inspection Dossier #ILB-2026-04 (PDF)... Download complete.");
    }

    function scheduleSiteVisit() {
      alert("VIP Site Tour Concierge: VIP transport from Sarajevo International Airport (SJJ) booked.");
    }

    function triggerSimulationModal() {
      document.getElementById('sim-modal').classList.remove('hidden');
      document.getElementById('sim-result').classList.add('hidden');
    }

    function runScenario(type) {
      const res = document.getElementById('sim-result');
      res.classList.remove('hidden');
      res.innerHTML = `<strong>SIMULATION COMPLETE:</strong> Critical path float buffer remains resilient (+5.4d).`;
    }

    function dropSnagPin(event) {
      const rect = event.currentTarget.getBoundingClientRect();
      const x = ((event.clientX - rect.left) / rect.width) * 100;
      const y = ((event.clientY - rect.top) / rect.height) * 100;
      
      const layer = document.getElementById('snag-pins-layer');
      const pin = document.createElement('div');
      pin.className = 'absolute -translate-x-1/2 -translate-y-1/2 pointer-events-auto cursor-pointer';
      pin.style.left = `${x.toFixed(1)}%`;
      pin.style.top = `${y.toFixed(1)}%`;
      pin.onclick = (e) => { e.stopPropagation(); inspectPin('NEW-PIN'); };
      pin.innerHTML = `<span class="w-5 h-5 rounded-full bg-emerald-500 text-black font-mono text-[10px] font-bold flex items-center justify-center shadow-lg border border-white animate-bounce">+</span>`;
      layer.appendChild(pin);
      alert(`Native CAD Plan Pin Dropped at [X: ${x.toFixed(1)}%, Y: ${y.toFixed(1)}%]!\nLogged into Internal Sovereign Defect Ledger.`);
    }

    function inspectPin(pinId) {
      document.getElementById('snag-pin-badge').innerText = `${pinId} (SELECTED)`;
      document.getElementById('snag-pin-title').innerText = pinId === 'PIN-01' ? 'Schüco Glazing Seal Gasket Gap' : 'Italian Porcelanosa Tile Edge Alignment';
    }

    function resolveSnagPin(pinId) {
      alert(`Pin ${pinId} Resolved!\nSubcontractor sign-off confirmed by Sinteza Chief Engineer.`);
      document.getElementById('snag-pin-badge').innerText = `${pinId} (RESOLVED)`;
    }

    function setCurrency(curr) {
      currentCurrency = curr;
      document.querySelectorAll('.curr-btn').forEach(b => {
        b.classList.remove('bg-[#E5A93C]', 'text-black', 'font-bold');
        b.classList.add('text-slate-400');
      });
      document.getElementById(`curr-${curr}`).classList.add('bg-[#E5A93C]', 'text-black', 'font-bold');
      document.getElementById(`curr-${curr}`).classList.remove('text-slate-400');

      const rate = RATES[curr];
      const symbol = CURRENCY_SYMBOLS[curr];

      const totalGDV = Math.round(54200000 * rate);
      const paid = Math.round(37070000 * rate);
      const escrow = Math.round(17130000 * rate);

      document.getElementById('kpi-gdv').innerText = `${symbol}${totalGDV.toLocaleString()}`;
      document.getElementById('kpi-paid').innerText = `${symbol}${(paid / 1000000).toFixed(2)}M`;
      document.getElementById('kpi-escrow').innerText = `${symbol}${(escrow / 1000000).toFixed(2)}M`;
      const lockVal = document.getElementById('escrow-locked-val');
      if (lockVal) lockVal.innerText = `${symbol}${escrow.toLocaleString()}`;
    }

    let bimAnimId;
    function initBimCanvas() {
      const canvas = document.getElementById('bim-canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      let angle = 0;

      function renderFrame() {
        ctx.fillStyle = '#050608';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
        ctx.lineWidth = 1;
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2 + 50;

        for (let i = -6; i <= 6; i++) {
          ctx.beginPath();
          ctx.moveTo(centerX + (i * 30) - Math.cos(angle) * 20, centerY + (i * 15));
          ctx.lineTo(centerX + (i * 30) + 180, centerY + (i * 15) - 90);
          ctx.stroke();
        }

        for (let p = 0; p < 60; p++) {
          const px = centerX + Math.cos(angle + p * 0.2) * (100 + (p * 2.5));
          const py = centerY + Math.sin(angle + p * 0.2) * (50 + (p * 1.2)) - (p % 4 * 12);

          ctx.fillStyle = (p % 3 === 0) ? '#10B981' : (p % 3 === 1) ? '#06B6D4' : '#E5A93C';
          ctx.beginPath();
          ctx.arc(px, py, 2.5, 0, Math.PI * 2);
          ctx.fill();

          if (p % 4 === 0) {
            ctx.strokeStyle = 'rgba(229, 169, 60, 0.15)';
            ctx.beginPath();
            ctx.moveTo(px, py);
            ctx.lineTo(px, py + 20);
            ctx.stroke();
          }
        }

        angle += 0.008;
        bimAnimId = requestAnimationFrame(renderFrame);
      }

      if (bimAnimId) cancelAnimationFrame(bimAnimId);
      renderFrame();
    }

    document.addEventListener('DOMContentLoaded', () => {
      lucide.createIcons();
      renderPlots(PLOTS);
    });
  </script>
</body>
</html>
