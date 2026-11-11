path = r'C:\Users\bigbi\.gemini\antigravity\scratch\ilb-enterprise-pm\index.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

motion_css = """
    /* Emil Kowalski Precision Spring Motion Tokens */
    :root {
      --ease-spring: cubic-bezier(0.16, 1, 0.3, 1);
      --duration-micro: 180ms;
      --duration-drawer: 280ms;
    }

    .tab-view {
      animation: tabFadeIn var(--duration-micro) var(--ease-spring) forwards;
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

    /* Tactile Pin Drop */
    @keyframes pinDropSettle {
      0% { transform: scale(0.3) translateY(-16px); opacity: 0; }
      60% { transform: scale(1.15) translateY(2px); opacity: 1; }
      85% { transform: scale(0.95) translateY(-1px); }
      100% { transform: scale(1.0) translateY(0); opacity: 1; }
    }

    .pin-drop-anim {
      animation: pinDropSettle 240ms var(--ease-spring) forwards;
    }

    /* Accessibility Reduced Motion Override */
    @media (prefers-reduced-motion: reduce) {
      *, ::before, ::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
    }
"""

if '/* Emil Kowalski Precision Spring' not in text:
    text = text.replace('::-webkit-scrollbar-thumb:hover {', motion_css + '\n    ::-webkit-scrollbar-thumb:hover {')
    # Update dropSnagPin pin animation class from animate-bounce to pin-drop-anim
    text = text.replace('animate-bounce', 'pin-drop-anim')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Spring motion tokens & tactile physics applied to index.html.")
else:
    print("Motion tokens already present.")
