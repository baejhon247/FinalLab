document.getElementById('learnMoreLink').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default anchor click behavior
    this.classList.toggle('active'); // Toggle the active class
});
