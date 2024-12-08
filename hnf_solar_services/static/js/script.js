let currentSlide = 0;
const slides = document.querySelectorAll('.slideshow img');

function showNextSlide() {
    slides[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add('active');
}

setInterval(showNextSlide, 3000); // Change slide every 3 seconds
