document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from submitting normally

    const formData = new FormData(this);

    // Send the form data using AJAX
    fetch('submit_report.php', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        let message = '';
        if (data.includes('successfully')) {
            message = 'Report submitted successfully!';
            showPopup(message, 'success');
        } else {
            message = 'Failed to send report.';
            showPopup(message, 'error');
        }
    })
    .catch(error => {
        showPopup('An error occurred. Please try again later.', 'error');
    });
});

// Function to show the success or error popup
function showPopup(message, type) {
    const popup = document.createElement('div');
    popup.classList.add('popup', type);
    popup.innerHTML = message;

    document.body.appendChild(popup);

    // Automatically hide the popup after 3 seconds
    setTimeout(() => {
        popup.remove();
    }, 3000);
}
// script.js

// Function to show the popup
function showPopup() {
    document.getElementById('popup-container').style.display = 'flex'; // Show popup
}

// Function to close the popup and redirect to index.php
function closePopup() {
    document.getElementById('popup-container').style.display = 'none'; // Hide popup
    window.location.href = 'index.php'; // Redirect to index.php
}
// Script for toggling the dropdown menu visibility
document.querySelector('.menu-icon').addEventListener('click', function () {
    this.classList.toggle('active');
});