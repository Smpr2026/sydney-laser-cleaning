(() => {
  const EMAIL = 'zap@sydneylasercleaning.com.au';
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('[data-year]').forEach(el => el.textContent = new Date().getFullYear());

  /* nav: solid once you leave the top, burger menu on phones */
  const nav = document.querySelector('.nav'), top = document.getElementById('top-sentinel');
  if (nav && top) new IntersectionObserver(([e]) => nav.classList.toggle('solid', !e.isIntersecting)).observe(top);
  const burger = document.querySelector('.burger');
  if (burger) burger.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    burger.setAttribute('aria-expanded', open);
    burger.querySelector('i').className = open ? 'ph ph-x' : 'ph ph-list';
  });
  document.querySelectorAll('.mmenu a').forEach(a => a.addEventListener('click', () => nav.classList.remove('open')));

  /* reveal on scroll */
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('on'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
  document.querySelectorAll('.rv').forEach(el => io.observe(el));

  /* count-up numbers */
  const cio = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return; cio.unobserve(e.target);
    const el = e.target, to = +el.dataset.count, suf = el.dataset.suffix || '';
    if (reduce) { el.textContent = to + suf; return; }
    const t0 = performance.now();
    (function f(t) { const k = Math.min(1, (t - t0) / 1200); el.textContent = Math.round(to * (1 - Math.pow(1 - k, 4))) + suf; if (k < 1) requestAnimationFrame(f); })(t0);
  }), { threshold: .6 });
  document.querySelectorAll('[data-count]').forEach(el => cio.observe(el));

  /* floating text button appears after the first screen */
  const fab = document.querySelector('.fab');
  if (fab && top) new IntersectionObserver(([e]) => fab.classList.toggle('show', !e.isIntersecting), { rootMargin: '400px 0px 0px 0px' }).observe(top);

  /* quote / hire forms: no server needed, they open a filled-in email or text message */
  document.querySelectorAll('form[data-send]').forEach(form => {
    form.addEventListener('submit', ev => {
      ev.preventDefault();
      let ok = true;
      form.querySelectorAll('[required]').forEach(inp => {
        const f = inp.closest('.field'), bad = !inp.value.trim();
        f && f.classList.toggle('bad', bad); if (bad && ok) { inp.focus(); ok = false; }
      });
      if (!ok) return;
      const data = new FormData(form), lines = [];
      for (const [k, v] of data) if (String(v).trim()) lines.push(`${k}: ${v}`);
      const subject = form.dataset.subject || 'Laser cleaning enquiry';
      const via = (form.querySelector('[name="_via"]:checked') || {}).value || 'email';
      const body = lines.filter(l => !l.startsWith('_via')).join('\n');
      location.href = `mailto:${EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      const done = form.querySelector('.sent'); if (done) done.hidden = false;
    });
    form.querySelectorAll('input,textarea').forEach(inp => inp.addEventListener('input', () => inp.closest('.field')?.classList.remove('bad')));
  });
})();

/* before & after slider: arrows, mouse drag; touch uses native swipe */
(() => {
  document.querySelectorAll('.slider').forEach(sl => {
    const sec = sl.closest('section');
    const step = () => (sl.querySelector('.slide')?.getBoundingClientRect().width || 300) + 18;
    sec.querySelector('.sl-next')?.addEventListener('click', () => sl.scrollBy({ left: step(), behavior: 'smooth' }));
    sec.querySelector('.sl-prev')?.addEventListener('click', () => sl.scrollBy({ left: -step(), behavior: 'smooth' }));
    sl.addEventListener('keydown', e => { if (e.key === 'ArrowRight') sl.scrollBy({ left: step(), behavior: 'smooth' }); if (e.key === 'ArrowLeft') sl.scrollBy({ left: -step(), behavior: 'smooth' }); });
    let down = false, sx = 0, sl0 = 0;
    sl.addEventListener('pointerdown', e => { if (e.pointerType !== 'mouse') return; down = true; sx = e.clientX; sl0 = sl.scrollLeft; sl.setPointerCapture(e.pointerId); sl.classList.add('drag'); });
    sl.addEventListener('pointermove', e => { if (down) sl.scrollLeft = sl0 - (e.clientX - sx); });
    const up = () => { down = false; sl.classList.remove('drag'); };
    sl.addEventListener('pointerup', up); sl.addEventListener('pointercancel', up);
  });
  /* respect reduced motion for the hero video */
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) document.querySelectorAll('video[autoplay]').forEach(v => { v.removeAttribute('autoplay'); v.pause(); v.controls = true; });
})();

/* hero background: play the clips one after another with a slow crossfade */
(() => {
  const box = document.querySelector('.bgv'); if (!box) return;
  const vids = [...box.querySelectorAll('video')];
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) { vids.forEach(v => v.pause()); return; }
  let i = 0;
  const next = () => {
    const cur = vids[i]; i = (i + 1) % vids.length; const nv = vids[i];
    nv.currentTime = 0; nv.play().catch(() => {});
    nv.classList.add('on'); cur.classList.remove('on');
    setTimeout(() => cur.pause(), 1700);
  };
  vids.forEach(v => v.addEventListener('ended', next));
  if (vids.length === 1) vids[0].loop = true;
  /* pause when the hero is off screen to save battery */
  new IntersectionObserver(([e]) => { const v = vids[i]; e.isIntersecting ? v.play().catch(() => {}) : v.pause(); }).observe(box);
})();

/* gallery: filters + lightbox with arrows, keyboard and swipe */
(() => {
  const wall = document.getElementById('gwall'); if (!wall) return;
  const items = [...wall.querySelectorAll('.gi')];
  document.querySelectorAll('.gfilters button').forEach(b => b.addEventListener('click', () => {
    document.querySelectorAll('.gfilters button').forEach(x => x.classList.toggle('on', x === b));
    const f = b.dataset.f;
    items.forEach(it => it.classList.toggle('hide', f !== 'all' && !it.dataset.cat.split(' ').includes(f)));
  }));
  const lb = document.getElementById('lightbox'), media = lb.querySelector('.lb-media'), cap = lb.querySelector('.lb-cap');
  let cur = 0;
  const visible = () => items.filter(it => !it.classList.contains('hide'));
  function show(it) {
    const list = visible(); cur = list.indexOf(it);
    media.innerHTML = '';
    if (it.dataset.kind === 'video') {
      const v = document.createElement('video');
      Object.assign(v, { src: it.dataset.src, controls: true, autoplay: true, muted: true, loop: true, playsInline: true });
      v.setAttribute('playsinline', ''); media.appendChild(v); v.play().catch(() => {});
    } else {
      const im = document.createElement('img'); im.src = it.dataset.src; im.alt = it.dataset.cap; media.appendChild(im);
    }
    cap.textContent = it.dataset.cap;
  }
  const go = d => { const list = visible(); show(list[(cur + d + list.length) % list.length]); };
  items.forEach(it => it.addEventListener('click', () => { show(it); lb.showModal(); }));
  lb.querySelector('.lb-close').onclick = () => lb.close();
  lb.querySelector('.lb-next').onclick = () => go(1);
  lb.querySelector('.lb-prev').onclick = () => go(-1);
  lb.addEventListener('click', e => { if (e.target === lb) lb.close(); });
  lb.addEventListener('close', () => { media.innerHTML = ''; });
  lb.addEventListener('keydown', e => { if (e.key === 'ArrowRight') go(1); if (e.key === 'ArrowLeft') go(-1); });
  let x0 = null;
  lb.addEventListener('touchstart', e => { x0 = e.touches[0].clientX; }, { passive: true });
  lb.addEventListener('touchend', e => { if (x0 === null) return; const dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 50) go(dx < 0 ? 1 : -1); x0 = null; });
})();

/* any video marked data-inview plays only while it's on screen (all pages) */
(() => {
  document.querySelectorAll('video[data-inview]').forEach(v => new IntersectionObserver(([e]) => { e.isIntersecting ? v.play().catch(() => {}) : v.pause(); }, { threshold: .4 }).observe(v));
})();

/* hire availability calendar: booked days come from bookings.js (real bookings only) */
(() => {
  const root = document.getElementById('cal'); if (!root) return;
  const pad = n => String(n).padStart(2, '0');
  const key = d => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
  const booked = new Set();
  (window.SLC_BOOKED || []).forEach(b => {
    if (Array.isArray(b)) { const d = new Date(b[0] + 'T00:00'), e = new Date(b[1] + 'T00:00'); for (; d <= e; d.setDate(d.getDate() + 1)) booked.add(key(d)); }
    else booked.add(b);
  });
  const today = new Date(); today.setHours(0, 0, 0, 0);
  let view = new Date(today.getFullYear(), today.getMonth(), 1), picked = null;
  const start = document.getElementById('h-start');
  const months = () => innerWidth < 760 ? 1 : 2;
  function month(m) {
    const name = m.toLocaleString('en-AU', { month: 'long', year: 'numeric' });
    const first = (new Date(m.getFullYear(), m.getMonth(), 1).getDay() + 6) % 7; // Monday first
    const days = new Date(m.getFullYear(), m.getMonth() + 1, 0).getDate();
    let h = `<div class="mon"><div class="mname">${name}</div><div class="grid7">` + ['M','T','W','T','F','S','S'].map(d => `<span class="dow">${d}</span>`).join('');
    for (let i = 0; i < first; i++) h += '<span></span>';
    for (let d = 1; d <= days; d++) {
      const dt = new Date(m.getFullYear(), m.getMonth(), d), k = key(dt);
      const past = dt < today, isB = booked.has(k);
      const cls = past ? 'past' : isB ? 'booked' : 'free';
      const lbl = `${dt.toLocaleDateString('en-AU', { weekday: 'long', day: 'numeric', month: 'long' })}${isB ? ', booked' : past ? '' : ', available'}`;
      h += `<button type="button" class="day ${cls}${k === picked ? ' pick' : ''}${+dt === +today ? ' today' : ''}" data-k="${k}" ${past || isB ? 'disabled' : ''} aria-label="${lbl}">${d}</button>`;
    }
    return h + '</div></div>';
  }
  function draw() {
    let h = ''; for (let i = 0; i < months(); i++) h += month(new Date(view.getFullYear(), view.getMonth() + i, 1));
    root.innerHTML = h;
    document.getElementById('calPrev').disabled = view <= new Date(today.getFullYear(), today.getMonth(), 1);
  }
  root.addEventListener('click', e => {
    const b = e.target.closest('.day.free'); if (!b) return;
    picked = b.dataset.k; draw();
    if (start) { start.value = picked; start.closest('.field')?.classList.add('flash'); setTimeout(() => start.closest('.field')?.classList.remove('flash'), 1400);
      document.querySelector('.formcard')?.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' }); }
  });
  document.getElementById('calPrev').onclick = () => { view = new Date(view.getFullYear(), view.getMonth() - 1, 1); draw(); };
  document.getElementById('calNext').onclick = () => { view = new Date(view.getFullYear(), view.getMonth() + 1, 1); draw(); };
  let w = innerWidth; addEventListener('resize', () => { if ((innerWidth < 760) !== (w < 760)) { w = innerWidth; draw(); } });
  draw();
})();
