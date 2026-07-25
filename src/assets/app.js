/* MLF site behaviour: colour scheme, the package anatomy, section marker. */

(function () {
  "use strict";

  var root = document.documentElement;

  /* ---- colour scheme --------------------------------------------------- */

  function currentTheme() {
    var stored = null;
    try { stored = localStorage.getItem("mlf-theme"); } catch (e) { /* private mode */ }
    if (stored === "light" || stored === "dark") return stored;
    /* This site is dark by default, so the system query is for light. */
    return window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark";
  }

  var themeButton = document.querySelector("[data-theme-toggle]");
  if (themeButton) {
    themeButton.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("mlf-theme", next); } catch (e) { /* private mode */ }
    });
  }

  /* ---- package anatomy -------------------------------------------------- */

  var anatomy = document.querySelector("[data-anatomy]");
  var payload = document.getElementById("anatomy-data");

  if (anatomy && payload) {
    var members = JSON.parse(payload.textContent);
    var rows = Array.prototype.slice.call(anatomy.querySelectorAll("[data-row]"));
    var panelPath = anatomy.querySelector("[data-panel-path]");
    var panelWhat = anatomy.querySelector("[data-panel-what]");
    var feeds = anatomy.querySelector("[data-feeds]");
    var feedsNone = anatomy.querySelector("[data-feeds-none]");
    var labels = JSON.parse(anatomy.getAttribute("data-labels"));

    function show(i) {
      var m = members[i];
      panelPath.textContent = m.path;
      panelWhat.textContent = m.what;

      feeds.innerHTML = "";
      if (m.fp.length) {
        feeds.hidden = false;
        feedsNone.hidden = true;
        m.fp.forEach(function (key) {
          var li = document.createElement("li");
          li.className = "feed";
          li.setAttribute("data-fp", key);
          li.textContent = labels[key];
          feeds.appendChild(li);
        });
      } else {
        feeds.hidden = true;
        feedsNone.hidden = false;
      }

      rows.forEach(function (el, n) {
        el.setAttribute("aria-selected", n === i ? "true" : "false");
      });
    }

    rows.forEach(function (el, n) {
      el.addEventListener("click", function () { show(n); });
      el.addEventListener("mouseenter", function () { show(n); });
      el.addEventListener("focus", function () { show(n); });
    });

    show(0);
  }

  /* ---- section marker --------------------------------------------------- */

  var links = Array.prototype.slice.call(document.querySelectorAll("[data-index-link]"));

  if (links.length && "IntersectionObserver" in window) {
    var byId = {};
    var headings = [];

    links.forEach(function (link) {
      var id = link.getAttribute("href").slice(1);
      var h = document.getElementById(id);
      if (h) { byId[id] = link; headings.push(h); }
    });

    var visible = {};

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { visible[e.target.id] = e.isIntersecting; });

      var active = null;
      for (var i = 0; i < headings.length; i++) {
        if (visible[headings[i].id]) { active = headings[i].id; break; }
      }
      if (!active) return;

      links.forEach(function (l) { l.classList.remove("is-here"); });
      if (byId[active]) byId[active].classList.add("is-here");
    }, { rootMargin: "-80px 0px -70% 0px", threshold: 0 });

    headings.forEach(function (h) { observer.observe(h); });
  }
})();
