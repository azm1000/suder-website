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

  // Slot-machine tagline: reel the practice areas past, then settle on the firm line
  var reels=[];
  d.querySelectorAll('.spin-word[data-spin]').forEach(function(el){
    var words=(el.dataset.spin||'').split('|').filter(Boolean), settle=el.textContent.trim();
    if(!words.length || !settle || reduce) return;
    if(w.innerWidth < (parseInt(el.dataset.spinMin,10)||0)) return;   // too narrow to set on one line
    // Start AND end on the firm line: at rest the reel shows the same words the
    // static markup does, so nothing flashes on load and a re-roll is seamless.
    var items=[settle].concat(words,[settle],[words[0]]);     // settled, one readable pass, settled, then a decoy the bounce reveals
    var sr=d.createElement('span'); sr.className='sr-only'; sr.textContent=settle;
    var reel=d.createElement('span'); reel.className='reel'; reel.setAttribute('aria-hidden','true');
    items.forEach(function(t){ var i=d.createElement('span'); i.textContent=t; reel.appendChild(i); });
    el.textContent=''; el.appendChild(sr); el.appendChild(reel);
    el.classList.add('reeled');        // clipping styles apply only once there is a reel to clip
    reels.push({el:el, reel:reel, n:items.length-2, done:false,     // land on the firm line, not the decoy
                delay:parseInt(el.dataset.spinDelay,10)||260, away:true, last:0});
  });
  // Steps rather than a continuous roll: each word slides in and then STOPS for
  // DWELL. That rest is the only thing that makes the words readable — a reel that
  // never pauses can be slowed forever and still not be read. The last step runs
  // longer and overshoots, so it snaps into the detent like a real reel.
  var SLIDE=140, DWELL=360, BACK=.9, C3=BACK+1, BLUR_K=.09, BLUR_MAX=.55;
  var REARM=4000;                 // scroll away and back after this and it rolls again
  var REPEAT=15000;               // and, sitting still, it rolls again on its own
  function spin(o){
    o.done=true; o.last=Date.now();
    var step=o.reel.getBoundingClientRect().height/(o.n+2), t0=null, prev=0, cycle=SLIDE+DWELL;
    o.reel.style.transform='translate3d(0,0,0)';   // index 0 reads the same as the resting line, so this is invisible
    o.el.classList.add('spinning');
    requestAnimationFrame(function frame(ts){
      if(t0===null) t0=ts;
      var t=ts-t0, k=Math.min(Math.floor(t/cycle), o.n-1), u=t-k*cycle, last=(k===o.n-1), e;
      var p=Math.min(u/(last?SLIDE*1.9:SLIDE),1);
      if(last){ var q=p-1; e=1+C3*q*q*q+BACK*q*q; }   // overshoot, then snap back
      else e=1-Math.pow(1-p,2.2);
      var pos=k+e;
      o.reel.style.transform='translate3d(0,'+(-pos*step).toFixed(2)+'px,0)';
      o.reel.style.filter='blur('+Math.min(BLUR_MAX,Math.abs(pos-prev)*step*BLUR_K).toFixed(2)+'px)';
      prev=pos;
      if(!(last && p>=1)) requestAnimationFrame(frame);
      else { o.reel.style.filter=''; o.el.classList.remove('spinning'); o.done=false; o.last=Date.now(); }
    });
  }
  function spinCheck(){
    if(!reels.length) return;
    var vh=w.innerHeight||d.documentElement.clientHeight;
    reels.forEach(function(o){
      var r=o.el.getBoundingClientRect(), inView=r.top < vh*0.88 && r.bottom > 0;
      if(!inView){ o.away=true; return; }
      if(o.done) return;                                  // already running
      var since = o.last ? Date.now()-o.last : Infinity;
      if(o.away && since >= REARM) o.away=false;          // came back after being properly away
      else if(since < REPEAT){
        // Too soon. Consume a return rather than leaving it armed, or the next
        // stray scroll event fires a roll under the reader.
        o.away=false; return;
      }
      o.done=true;                                        // claim it before the delay elapses
      setTimeout(function(){ o.done=false; spin(o); }, o.delay);
    });
  }
  spinCheck(); w.addEventListener('scroll', spinCheck, {passive:true}); setTimeout(spinCheck, 300);
  // Scroll alone is not enough: a reader who lands on the page and stays put saw
  // it roll once and never again. Tick so it comes round on its own; skip while the
  // tab is hidden, where rAF is paused and the roll would stall mid-word.
  if(reels.length) setInterval(function(){ if(!d.hidden) spinCheck(); }, 1000);

  // Current year
  d.querySelectorAll('[data-year]').forEach(function(el){ el.textContent=new Date().getFullYear(); });
})();
