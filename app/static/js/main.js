document.addEventListener('DOMContentLoaded', function() {
    console.log('AI News Website loaded');
    // Example: Toggle mobile navigation
    const navToggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('nav ul');

    if (navToggle) {
        navToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // Add any additional interactive features or functionality
});