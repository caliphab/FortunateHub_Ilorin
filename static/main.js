document.addEventListener("DOMContentLoaded", function () {
  // ── AOS ──
  AOS.init({
    duration: 800,
    easing: "ease-in-out",
    once: true,
  });

  // ── SWIPER ──
  const heroSwiper = new Swiper(".heroSwiper", {
    loop: true,
    speed: 800,
    slidesPerView: 1,
    autoHeight: true,
    autoplay: {
      delay: 4000,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    on: {
      slideChangeTransitionStart: function () {
        document.querySelectorAll(".hero-content").forEach((el) => {
          el.classList.remove("animate");
        });
      },
      slideChangeTransitionEnd: function () {
        const activeSlide = document.querySelector(
          ".swiper-slide-active .hero-content",
        );
        if (activeSlide) activeSlide.classList.add("animate");
      },
      init: function () {
        const activeSlide = document.querySelector(
          ".swiper-slide-active .hero-content",
        );
        if (activeSlide) activeSlide.classList.add("animate");
      },
    },
  });

  // ── AUTH MODAL ──
  function switchState(state) {
    document.querySelectorAll(".auth-state").forEach((el) => {
      el.classList.add("auth-state--hidden");
    });
    const target = document.querySelector(`[data-state="${state}"]`);
    if (target) target.classList.remove("auth-state--hidden");
  }

  window.switchState = switchState;

  function openAuth(state = "signin") {
    switchState(state);
    document.getElementById("authOverlay").classList.add("is-open");
  }

  window.openAuth = openAuth;

  function closeAuth() {
    document.getElementById("authOverlay").classList.remove("is-open");
  }

  // Close button
  const authClose = document.getElementById("authClose");
  if (authClose) authClose.addEventListener("click", closeAuth);

  // Close on overlay click
  const authOverlay = document.getElementById("authOverlay");
  if (authOverlay) {
    authOverlay.addEventListener("click", (e) => {
      if (e.target === authOverlay) closeAuth();
    });
  }

  // Nav Sign In
  const openSignin = document.getElementById("openSignin");
  if (openSignin) {
    openSignin.addEventListener("click", (e) => {
      e.preventDefault();
      openAuth("signin");
    });
  }

  // OTP auto-jump
  document.querySelectorAll(".otp-box").forEach((box, i, boxes) => {
    box.addEventListener("input", () => {
      box.classList.toggle("otp-filled", box.value.length === 1);
      if (box.value.length === 1 && i < boxes.length - 1) {
        boxes[i + 1].focus();
      }
    });
    box.addEventListener("keydown", (e) => {
      if (e.key === "Backspace" && !box.value && i > 0) {
        boxes[i - 1].focus();
      }
    });
  });

  // OTP countdown timer
  function startOtpTimer() {
    let seconds = 299;
    const timerEl = document.getElementById("otpTimer");
    if (!timerEl) return;
    const interval = setInterval(() => {
      const m = String(Math.floor(seconds / 60)).padStart(2, "0");
      const s = String(seconds % 60).padStart(2, "0");
      timerEl.textContent = `${m}:${s}`;
      if (seconds-- <= 0) clearInterval(interval);
    }, 1000);
  }

  window.startOtpTimer = startOtpTimer;

  // Password toggle
  window.togglePwd = function (btn) {
    const input = btn.closest(".field-wrap").querySelector(".field-input");
    input.type = input.type === "password" ? "text" : "password";
  };

  // Close with Escape key
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeAuth();
  });
});


