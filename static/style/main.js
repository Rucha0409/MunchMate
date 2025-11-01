// show loader during form submit
function showLoader(){ document.getElementById('loader').style.display='block'; }
document.addEventListener('DOMContentLoaded', ()=>{
  // Modal logic
  const modal = document.getElementById('recipeModal');
  const modalBody = document.getElementById('modalBody');
  const closeBtn = document.getElementById('modalClose');
  window.openModal = async function(id){
    modal.style.display='flex';
    modalBody.innerHTML = '<p>Loading recipe…</p>';
    try{
      const res = await fetch('/api/recipe/' + id);
      if(res.ok){
        const data = await res.json();
        modalBody.innerHTML = `<h2>${data.name}</h2>
          <p class="muted">${data.type} • ${data.prep_time}</p>
          <img src="/static/style/img/${data.image}" style="width:100%;max-height:300px;object-fit:cover;border-radius:8px;margin:10px 0;">
          <h4>Ingredients</h4><p>${data.ingredients}</p>
          <h4>Instructions</h4><p>${data.recipe}</p>`;
      } else {
        modalBody.innerHTML = '<p>Recipe not found.</p>';
      }
    } catch(e){
      modalBody.innerHTML = '<p>Failed to load. Try again.</p>';
    }
  }
  closeBtn.onclick = ()=> modal.style.display='none';
  window.onclick = (e)=> { if(e.target === modal) modal.style.display='none'; }

  // Dark mode toggle
  const darkToggle = document.getElementById('darkToggle');
  const root = document.documentElement;
  const saved = localStorage.getItem('munchmate-theme');
  if(saved) root.setAttribute('data-theme', saved);
  darkToggle.onclick = ()=>{
    const current = root.getAttribute('data-theme');
    const next = current === 'dark' ? '' : 'dark';
    if(next) root.setAttribute('data-theme','dark'); else root.removeAttribute('data-theme');
    localStorage.setItem('munchmate-theme', next);
  }
});
