$(document).ready(function () {
  setTimeout(function () {
    initTopSwiper();
  }, 100),
    setTimeout(function () {
      initMenuSwiper();
    }, 100);
});

function initTopSwiper() {
  var swiper = new Swiper("#topSwiper", {
    direction: "horizontal",
    loop: true,
    speed: 500,
    autoplay: 2000,
    pagination: ".swiper-pagination",
  });
}

function initMenuSwiper() {
  var swiper = new Swiper("#swiperMenu", {
    slidesPerView: 3,
  });
}
