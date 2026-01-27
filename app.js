/**
 * On load: fetch talents from the API and fill each talent's rank display.
 * Requires the backend to be running (e.g. uvicorn from backend on http://localhost:8000).
 */
const API_BASE = 'http://localhost:8000';

function loadTalents() {
  return fetch(`${API_BASE}/api/talents`)
    .then((res) => {
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return res.json();
    })
    .then((data) => {
      for (const [id, talent] of Object.entries(data)) {
        const nodes = document.querySelectorAll(`.talent-node.${id}`);
        const text = `${talent.current_rank}/${talent.max_rank}`;
        nodes.forEach((node) => {
          const rankEl = node.querySelector('.rank');
          if (rankEl) rankEl.textContent = text;
        });
      }
    })
    .catch((err) => {
      console.warn('Could not load talents from API:', err.message);
      // Page keeps the static HTML values (e.g. 0/5) if fetch fails
    });
}

function getTalentIdFromNode(node) {
  // Talent id is stored as an extra class on the node (e.g. "t1-1")
  for (const cls of node.classList) {
    if (cls !== 'talent-node') {
      return cls;
    }
  }
  return null;
}

function attachTalentClickHandlers() {
  const nodes = document.querySelectorAll('.talent-node');
  nodes.forEach((node) => {
    node.addEventListener('click', () => {
      const talentId = getTalentIdFromNode(node);
      if (!talentId) return;

      fetch(`${API_BASE}/api/talents/${talentId}`, {
        method: 'PATCH',
      })
        .then((res) => {
          if (!res.ok) throw new Error(`HTTP ${res.status}`);
          return res.json();
        })
        .then(() => {
          // After a successful update, refresh all talents from the API
          return loadTalents();
        })
        .catch((err) => {
          console.warn('Could not update talent', talentId, err.message);
        });
    });
  });
}

function initTalents() {
  loadTalents();
  attachTalentClickHandlers();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initTalents);
} else {
  initTalents();
}
