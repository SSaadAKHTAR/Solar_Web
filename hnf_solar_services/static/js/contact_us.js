let slideIndex = 0;

function showSlides() {
    const slides = document.querySelectorAll('.slideshow img');

    // Hide all slides
    slides.forEach(slide => slide.classList.remove('active'));

    // Show the next slide
    slideIndex = (slideIndex + 1) % slides.length;
    slides[slideIndex].classList.add('active');
}

// Change slides every 3 seconds
setInterval(showSlides, 3000);
