// Initialize Mermaid diagrams
document.addEventListener('DOMContentLoaded', function() {
  if (typeof mermaid === 'undefined') return;

  // Check for dark mode
  const isDark = document.body.getAttribute('data-md-color-scheme') === 'slate';

  mermaid.initialize({
    startOnLoad: true,
    theme: isDark ? 'dark' : 'default',
    securityLevel: 'loose',
    fontFamily: 'Inter, system-ui, sans-serif',
    flowchart: { curve: 'basis', htmlLabels: true },
    sequence: { showSequenceNumbers: false }
  });

  // Re-render on theme toggle
  const observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(m) {
      if (m.type === 'attributes' && m.attributeName === 'data-md-color-scheme') {
        const newDark = document.body.getAttribute('data-md-color-scheme') === 'slate';
        mermaid.initialize({ theme: newDark ? 'dark' : 'default' });
        document.querySelectorAll('.mermaid').forEach(function(el) {
          if (!el.dataset.original) el.dataset.original = el.textContent;
          el.removeAttribute('data-processed');
          el.innerHTML = el.dataset.original;
        });
        mermaid.run();
      }
    });
  });
  observer.observe(document.body, { attributes: true });
});