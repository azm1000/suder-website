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

  // Reveal on scroll (rect check on load/scroll/resize; robust even where IntersectionObserver is throttled)
  var items=[].slice.call(d.querySelectorAll('.reveal'));
  function revealCheck(){
    if(!items.length) return;
    var vh=w.innerHeight||d.documentElement.clientHeight, keep=[];
    items.forEach(function(el){ var r=el.getBoundingClientRect(); if(r.top < vh*0.94 && r.bottom > 0){ el.classList.add('in'); } else keep.push(el); });
    items=keep;
  }
  if(reduce){ items.forEach(function(el){el.classList.add('in');}); items=[]; }
  else{
    revealCheck(); w.addEventListener('scroll', revealCheck, {passive:true}); w.addEventListener('resize', revealCheck); w.addEventListener('load', revealCheck); setTimeout(revealCheck, 300);
  }

  // Count-up stats
  var counters=[].slice.call(d.querySelectorAll('[data-count]'));
  function runCounter(el){
    var target=parseFloat(el.dataset.count), suffix=el.dataset.suffix||'', start=null, dur=1400; el.textContent='0'+suffix;
    function step(ts){ if(!start) start=ts; var p=Math.min((ts-start)/dur,1); var e=1-Math.pow(1-p,3); el.textContent=Math.round(target*e)+suffix; if(p<1) requestAnimationFrame(step); }
    requestAnimationFrame(step);
  }
  function counterCheck(){
    if(!counters.length) return; var vh=w.innerHeight||d.documentElement.clientHeight, keep=[];
    counters.forEach(function(el){ var r=el.getBoundingClientRect(); if(r.top < vh*0.9 && r.bottom > 0) runCounter(el); else keep.push(el); });
    counters=keep;
  }
  if(!reduce){ counterCheck(); w.addEventListener('scroll', counterCheck, {passive:true}); setTimeout(counterCheck, 300); }

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

  // Hero slideshow (crossfade + slow pan)
  d.querySelectorAll('.hero-slides').forEach(function(box){
    var slides=[].slice.call(box.querySelectorAll('img')); if(slides.length<2) return;
    var hero=box.closest('.hero'), cap=hero&&hero.querySelector('.hero-caption'), i=0, timer=null, iv=parseInt(box.dataset.interval,10)||6500;
    var dots=d.createElement('div'); dots.className='hero-dots';
    slides.forEach(function(s,n){ var b=d.createElement('button'); b.type='button'; b.setAttribute('aria-label','Show image '+(n+1)); b.addEventListener('click',function(){ go(n); restart(); }); dots.appendChild(b); });
    if(hero) hero.appendChild(dots);
    function go(n){ slides[i].classList.remove('active'); dots.children[i].classList.remove('active'); i=n%slides.length; var s=slides[i]; s.classList.add('active'); dots.children[i].classList.add('active');
      if(cap){ cap.style.opacity=0; setTimeout(function(){ cap.textContent=s.dataset.caption||''; cap.style.opacity=1; },400); }
      var nx=slides[(i+1)%slides.length]; if(nx.loading==='lazy'){ nx.loading='eager'; } }
    function restart(){ clearInterval(timer); if(!reduce) timer=setInterval(function(){ go(i+1); }, iv); }
    dots.children[0].classList.add('active'); slides.forEach(function(s,n){ if(n>0 && n<3) s.loading='eager'; });
    restart();
    d.addEventListener('visibilitychange', function(){ if(d.hidden) clearInterval(timer); else restart(); });
  });

  // Current year
  d.querySelectorAll('[data-year]').forEach(function(el){ el.textContent=new Date().getFullYear(); });
})();
