// Portfolio interactivity — mobile nav toggle + scroll reveal.
(function () {
  "use strict";

  // Mobile navigation toggle
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    // Close the menu after following an in-page link
    links.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        links.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  // Scroll reveal — adds .is-visible to .reveal elements as they enter view
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    // No IntersectionObserver — show everything
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  }

  // Section-nav scroll-spy (landing page)
  var sectionNav = document.querySelector(".section-nav");
  if (sectionNav) {
    var navLinks = sectionNav.querySelectorAll("a");
    var linkById = {};
    navLinks.forEach(function (a) {
      linkById[a.getAttribute("href").slice(1)] = a;
    });
    var spiedSections = document.querySelectorAll("main section[id]");
    if ("IntersectionObserver" in window && spiedSections.length) {
      var spy = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting && linkById[entry.target.id]) {
            navLinks.forEach(function (a) { a.classList.remove("is-current"); });
            linkById[entry.target.id].classList.add("is-current");
          }
        });
      }, { rootMargin: "-15% 0px -80% 0px", threshold: 0 });
      spiedSections.forEach(function (s) { spy.observe(s); });
    }
  }
})();
