// Initialize AOS
AOS.init({
  duration: 800,
  easing: "ease-in-out",
  once: true
})

// Hero Swiper

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
});



