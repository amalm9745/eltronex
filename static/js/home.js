let nextButton = document.getElementById('next');
let prevButton = document.getElementById('prev');
let carousel = document.querySelector('.carousel');
let listHTML = document.querySelector('.carousel .list');
// let seeMoreButtons = document.querySelectorAll('.seeMore');
// let backButton = document.getElementById('back');


// Function to start automatic carousel slide
const startAutoSlide = () => {
    autoSlideInterval = setInterval(() => {
        showSlider('next');
    }, 15000); // Change slide every 15 seconds
}

// Function to stop automatic carousel slide
const stopAutoSlide = () => {
    clearInterval(autoSlideInterval);
}


nextButton.onclick = function(){
    stopAutoSlide();
    showSlider('next');
    startAutoSlide();
}
prevButton.onclick = function(){
    stopAutoSlide();
    showSlider('prev');
    startAutoSlide();
}
let unAcceppClick;
const showSlider = (type) => {
    nextButton.style.pointerEvents = 'none';
    prevButton.style.pointerEvents = 'none';

    carousel.classList.remove('next', 'prev');
    let items = document.querySelectorAll('.carousel .list .item');
    if(type === 'next'){
        listHTML.appendChild(items[0]);
        carousel.classList.add('next');
    }else{
        listHTML.prepend(items[items.length - 1]);
        carousel.classList.add('prev');
    }
    clearTimeout(unAcceppClick);
    unAcceppClick = setTimeout(()=>{
        nextButton.style.pointerEvents = 'auto';
        prevButton.style.pointerEvents = 'auto';
    }, 2000)
}


// Start automatic slide initially
startAutoSlide();


// seeMoreButtons.forEach((button) => {
//     button.onclick = function(){
//         carousel.classList.remove('next', 'prev');
//         carousel.classList.add('showDetail');
//     }
// });
// backButton.onclick = function(){
//     carousel.classList.remove('showDetail');
// }



//for slick and card



$(document).ready(function(){
  $('.responsive').slick({
dots: false,
infinite: false,
speed: 300,
slidesToShow: 5,
slidesToScroll: 1,
responsive: [
  {
    breakpoint: 1024,
    settings: {
      slidesToShow: 3,
      slidesToScroll: 1,
      infinite: true,
      dots: false
    }
  },
  {
    breakpoint: 600,
    settings: {
      slidesToShow: 2,
      slidesToScroll: 1
    }
  },
  {
    breakpoint: 480,
    settings: {
      slidesToShow: 1,
      slidesToScroll: 1
    }
  }
  // You can unslick at a given breakpoint now by adding:
  // settings: "unslick"
  // instead of a settings object
]
});
});
