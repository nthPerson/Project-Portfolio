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

  // Section-nav scroll-spy (landing page) — single source of truth.
  var sectionNav = document.querySelector(".section-nav");
  if (sectionNav) {
    var navLinks = Array.prototype.slice.call(sectionNav.querySelectorAll("a"));
    var spied = Array.prototype.slice.call(document.querySelectorAll("main section[id]"));
    if (navLinks.length && spied.length) {
      var setCurrent = function (id) {
        navLinks.forEach(function (a) {
          a.classList.toggle("is-current", a.getAttribute("href") === "#" + id);
        });
      };
      var updateSpy = function () {
        // At (or near) the page bottom, the final section is always current.
        if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 2) {
          setCurrent(spied[spied.length - 1].id);
          return;
        }
        // Otherwise: the last section whose top has passed a line 30% down the viewport.
        var line = window.scrollY + window.innerHeight * 0.3;
        var currentId = spied[0].id;
        for (var i = 0; i < spied.length; i++) {
          if (spied[i].offsetTop <= line) { currentId = spied[i].id; }
        }
        setCurrent(currentId);
      };
      var ticking = false;
      window.addEventListener("scroll", function () {
        if (!ticking) {
          window.requestAnimationFrame(function () { updateSpy(); ticking = false; });
          ticking = true;
        }
      }, { passive: true });
      window.addEventListener("resize", updateSpy, { passive: true });
      updateSpy();
    }
  }
})();
