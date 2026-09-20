/* Suder, LLC — site behavior: header, mobile nav, reveal, counters, marquee, filters, forms */
(function(){
  var d=document, w=window;
  var reduce = w.matchMedia && w.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Header: solid after hero, hide on scroll down / show on scroll up
  var header=d.querySelector('.header'); var lastY=0;
  function onScroll(){
    var y=w.scrollY||0;
    if(header){
      header.classList.toggle('solid', y>40 || header.dataset.solid==='1');
      header.classList.toggle('hide', y>400 && y>lastY && !d.body.classList.contains('menu-open'));
    }
    lastY=y;
  }
  onScroll(); w.addEventListener('scroll', onScroll, {passive:true});

  // Mobile nav
  var burger=d.querySelector('.burger'), mnav=d.querySelector('.mobile-nav'), closeBtn=d.querySelector('.mobile-nav .close');
  function toggleMenu(open){ if(!mnav) return; mnav.classList.toggle('open', open); d.body.classList.toggle('menu-open', open); burger&&burger.setAttribute('aria-expanded', open?'true':'false'); }
  burger&&burger.addEventListener('click', function(){ toggleMenu(!mnav.classList.contains('open')); });
  closeBtn&&closeBtn.addEventListener('click', function(){ toggleMenu(false); });
  d.addEventListener('keydown', function(e){ if(e.key==='Escape') toggleMenu(false); });

  // Reveal on scroll
  var items=[].slice.call(d.querySelectorAll('.reveal'));
  if(reduce || !('IntersectionObserver' in w)){ items.forEach(function(el){el.classList.add('in');}); }
  else{
    var io=new IntersectionObserver(function(entries){ entries.forEach(function(en){ if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target);} }); },{rootMargin:'0px 0px -8% 0px',threshold:.08});
    items.forEach(function(el){ io.observe(el); });
  }

  // Count-up stats
  var counters=[].slice.call(d.querySelectorAll('[data-count]'));
  if(counters.length && !reduce && 'IntersectionObserver' in w){
    var cio=new IntersectionObserver(function(entries){ entries.forEach(function(en){ if(!en.isIntersecting) return; var el=en.target; cio.unobserve(el);
      var target=parseFloat(el.dataset.count), suffix=el.dataset.suffix||'', start=null, dur=1400; el.textContent='0'+suffix;
      function step(ts){ if(!start) start=ts; var p=Math.min((ts-start)/dur,1); var e=1-Math.pow(1-p,3); el.textContent=Math.round(target*e)+suffix; if(p<1) requestAnimationFrame(step); }
      requestAnimationFrame(step); }); },{threshold:.5});
    counters.forEach(function(el){ cio.observe(el); });
  }

  // Marquee: duplicate track for seamless loop
  d.querySelectorAll('.marquee-track').forEach(function(t){ t.innerHTML += t.innerHTML; });

  // Results filter
  var chips=d.querySelectorAll('.chip[data-filter]');
  if(chips.length){
    var rows=d.querySelectorAll('.row[data-tags]');
    function apply(f){ chips.forEach(function(c){ c.classList.toggle('active', c.dataset.filter===f); }); rows.forEach(function(r){ r.classList.toggle('hidden', f!=='all' && r.dataset.tags.split(' ').indexOf(f)<0); }); }
    chips.forEach(function(c){ c.addEventListener('click', function(){ apply(c.dataset.filter); history.replaceState(null,'', c.dataset.filter==='all'? location.pathname : '#'+c.dataset.filter); }); });
    var h=location.hash.replace('#',''); var match=[].some.call(chips,function(c){return c.dataset.filter===h;}); apply(match?h:'all');
  }

  // Netlify forms via fetch, with plain POST fallback
  d.querySelectorAll('form[data-netlify]').forEach(function(f){
    f.addEventListener('submit', function(e){
      if(!w.fetch || !w.FormData) return; e.preventDefault();
      var btn=f.querySelector('button[type=submit]'); if(btn){btn.disabled=true; btn.textContent='Sending…';}
      fetch('/', {method:'POST', body:new FormData(f)}).then(function(r){ if(!r.ok) throw new Error(r.status);
        f.style.display='none'; var ok=d.getElementById(f.dataset.ok); if(ok) ok.style.display='block'; })
      .catch(function(){ if(btn){btn.disabled=false; btn.textContent='Send message';} f.submit(); });
    });
  });

  // Current year
  d.querySelectorAll('[data-year]').forEach(function(el){ el.textContent=new Date().getFullYear(); });
})();
