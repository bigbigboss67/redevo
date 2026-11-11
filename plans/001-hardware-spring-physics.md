# Motion Implementation Plan 001 // Hardware Spring Physics & Tactile Transitions

**Target File:** `C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\index.html`  
**Standard:** Emil Kowalski Precision Motion Curve (`cubic-bezier(0.16, 1, 0.3, 1)`)

---

### Step 1: Add Hardware Spring Motion Tokens to `<style>`
Replace generic CSS transitions with dedicated motion tokens:
```css
/* Emil Kowalski Spring Tokens */
:root {
  --ease-spring: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-out-quad: cubic-bezier(0.25, 1, 0.5, 1);
  --duration-tactile: 180ms;
  --duration-slide: 280ms;
}

/* GPU Composited Tab Transitions */
.tab-view {
  animation: tabFadeIn var(--duration-tactile) var(--ease-spring) forwards;
}

@keyframes tabFadeIn {
  from {
    opacity: 0;
    transform: translateY(4px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Slide-Over Plot Drawer Spring Physics */
#plot-drawer.active-drawer > div {
  transform: translate3d(0, 0, 0);
  transition: transform var(--duration-slide) var(--ease-spring);
}

/* Tactile Snag Pin Drop Animation */
@keyframes pinDropSettle {
  0% { transform: scale(0.3) translateY(-20px); opacity: 0; }
  60% { transform: scale(1.15) translateY(2px); opacity: 1; }
  85% { transform: scale(0.95) translateY(-1px); }
  100% { transform: scale(1.0) translateY(0); }
}

.pin-drop-anim {
  animation: pinDropSettle 240ms var(--ease-spring) forwards;
}

/* Full Accessibility Support */
@media (prefers-reduced-motion: reduce) {
  *, ::before, ::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

### Step 2: Verification Checklist
1. Click between **1. Master Cockpit** and **2. 5 Landmark Buildings** — verify views enter with a 4px spring glide rather than a harsh flash.
2. Click any villa plot card — verify the right slide-over drawer animates smoothly without frame drops.
3. Drop a defect pin on the CAD plan — verify it impacts with a 240ms single tactile spring settlement without infinite looping.
