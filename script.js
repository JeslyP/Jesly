/* ============================================================
   Jesly Prosper — Portfolio interactions
   ============================================================ */
(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Theme (dark / light) ---------- */
  const root = document.documentElement;
  const toggle = $("#theme-toggle");
  const saved = (() => { try { return localStorage.getItem("theme"); } catch { return null; } })();
  const systemDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  const applyTheme = (t) => {
    if (t === "dark") root.setAttribute("data-theme", "dark");
    else root.removeAttribute("data-theme");
  };
  applyTheme(saved || (systemDark ? "dark" : "light"));
  toggle?.addEventListener("click", () => {
    const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    applyTheme(next);
    try { localStorage.setItem("theme", next); } catch {}
  });

  /* ---------- Nav: scrolled state, mobile menu, active link ---------- */
  const nav = $(".nav");
  const links = $("#nav-links");
  const burger = $("#nav-burger");
  const onScroll = () => nav.classList.toggle("is-scrolled", window.scrollY > 8);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  burger?.addEventListener("click", () => {
    const open = links.classList.toggle("is-open");
    burger.setAttribute("aria-expanded", String(open));
    burger.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  });
  $$("a", links).forEach((a) =>
    a.addEventListener("click", () => {
      links.classList.remove("is-open");
      burger?.setAttribute("aria-expanded", "false");
    })
  );

  const sections = $$("main section[id]");
  const navAnchors = $$("a[href^='#']", links);
  const spy = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        navAnchors.forEach((a) => a.classList.toggle("is-active", a.getAttribute("href") === `#${e.target.id}`));
      });
    },
    { rootMargin: "-40% 0px -55% 0px" }
  );
  sections.forEach((s) => spy.observe(s));

  /* ---------- Reveal on scroll ---------- */
  const revealEls = $$(".reveal");
  if (prefersReduced || !("IntersectionObserver" in window)) {
    revealEls.forEach((el) => el.classList.add("is-visible"));
  } else {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) { e.target.classList.add("is-visible"); io.unobserve(e.target); }
        });
      },
      { threshold: 0.12 }
    );
    revealEls.forEach((el) => io.observe(el));
  }

  /* ---------- Counters ---------- */
  const counters = $$("[data-count]");
  const runCounter = (el) => {
    const target = Number(el.dataset.count);
    if (prefersReduced) { el.textContent = target; return; }
    const duration = 1400;
    const start = performance.now();
    const tick = (now) => {
      const p = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased);
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  if (prefersReduced) {
    counters.forEach(runCounter);
  } else {
    const cio = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { runCounter(e.target); cio.unobserve(e.target); } });
    }, { threshold: 0.5 });
    counters.forEach((c) => cio.observe(c));
  }

  /* ---------- Typewriter ---------- */
  const typed = $(".typed");
  if (typed && !prefersReduced) {
    let words = [];
    try { words = JSON.parse(typed.dataset.words || "[]"); } catch {}
    if (words.length) {
      let wi = 0, ci = words[0].length, deleting = false;
      const step = () => {
        const word = words[wi];
        if (deleting) {
          ci--;
          typed.textContent = word.slice(0, ci);
          if (ci === 0) { deleting = false; wi = (wi + 1) % words.length; setTimeout(step, 400); return; }
          setTimeout(step, 45);
        } else {
          ci++;
          typed.textContent = word.slice(0, ci);
          if (ci === word.length) { deleting = true; setTimeout(step, 2200); return; }
          setTimeout(step, 80);
        }
      };
      setTimeout(() => { deleting = true; step(); }, 2200);
    }
  }

  /* ---------- Cursor glow + hero card tilt ---------- */
  const glow = $(".cursor-glow");
  const card = $(".hero__card");
  if (!prefersReduced && window.matchMedia("(hover: hover)").matches) {
    window.addEventListener("pointermove", (e) => {
      glow?.style.setProperty("--mx", `${e.clientX}px`);
      glow?.style.setProperty("--my", `${e.clientY}px`);
    }, { passive: true });

    if (card) {
      const wrap = card.parentElement;
      wrap.addEventListener("pointermove", (e) => {
        const r = card.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - 0.5;
        const y = (e.clientY - r.top) / r.height - 0.5;
        card.style.transform = `rotateY(${x * 14}deg) rotateX(${-y * 14}deg)`;
      });
      wrap.addEventListener("pointerleave", () => { card.style.transform = ""; });
    }
  }

  /* ---------- Contact form ---------- */
  const form = $(".contact__form");
  form?.addEventListener("submit", async (e) => {
    const action = form.getAttribute("action") || "";
    if (action.includes("YOUR_FORM_ID")) {
      // Form isn't wired up yet: fall back to a mailto link so nothing is lost.
      e.preventDefault();
      const fd = new FormData(form);
      const subject = encodeURIComponent(`Portfolio message from ${fd.get("name")}`);
      const body = encodeURIComponent(`${fd.get("message")}\n\n— ${fd.get("name")} (${fd.get("email")})`);
      window.location.href = `mailto:jeslyprosper@gmail.com?subject=${subject}&body=${body}`;
      return;
    }
    e.preventDefault();
    const btn = $("button[type=submit]", form);
    const original = btn.textContent;
    btn.textContent = "Sending…";
    btn.disabled = true;
    try {
      const res = await fetch(action, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } });
      if (!res.ok) throw new Error("Request failed");
      form.reset();
      btn.textContent = "Message sent ✓";
      form.classList.add("is-sent");
    } catch {
      btn.textContent = "Something went wrong — try email";
      btn.disabled = false;
      setTimeout(() => { btn.textContent = original; }, 3000);
    }
  });

  /* ---------- Footer year ---------- */
  const year = $("#year");
  if (year) year.textContent = new Date().getFullYear();
})();
