// Show the form and hide the contact list
document.getElementById('add-contact-btn').addEventListener('click', function () {
    document.getElementById('contact-list').style.display = 'none';
    document.getElementById('contact-input-container').style.display = 'block';
  });
  
  // Save the new contact and show the contact list again
  document.getElementById('save-contact-btn').addEventListener('click', function () {
    const name = document.getElementById('new-contact-name').value;
    const email = document.getElementById('new-contact-email').value;
    const picturePreviewSrc = document.getElementById('contact-picture-preview').src;
  
    if (name === '' || email === '' || picturePreviewSrc === '#') return;
  
    const contactList = document.getElementById('contact-list');
  
    // Create a new list item
    const newContact = document.createElement('li');
    newContact.classList.add('contact');
  
    newContact.innerHTML = `
      <img src="${picturePreviewSrc}" alt="Profile Picture" class="profile-picture">
      <div class="contact-info">
        <span class="contact-name">${name}</span>
        <span class="contact-email">${email}</span>
        <button class="message-btn">Message</button>
      </div>
    `;
  
    contactList.appendChild(newContact);
  
    document.getElementById('new-contact-name').value = '';
    document.getElementById('new-contact-email').value = '';
    document.getElementById('new-contact-picture').value = '';
    document.getElementById('contact-picture-preview').style.display = 'none';
  
    document.getElementById('contact-list').style.display = 'flex';
    document.getElementById('contact-input-container').style.display = 'none';
  });
  
  // Cancel the new contact and restore the contact list
  document.getElementById('cancel-contact-btn').addEventListener('click', function () {
    document.getElementById('new-contact-name').value = '';
    document.getElementById('new-contact-email').value = '';
    document.getElementById('new-contact-picture').value = '';
    document.getElementById('contact-picture-preview').style.display = 'none';
  
    document.getElementById('contact-list').style.display = 'flex';
    document.getElementById('contact-input-container').style.display = 'none';
  });
  
  // Display image preview when an image is uploaded
  document.getElementById('new-contact-picture').addEventListener('change', function (event) {
    const file = event.target.files[0]; // Get the uploaded file
    const reader = new FileReader();
  
    // Check if a file was uploaded
    if (file) {
      reader.onload = function (e) {
        const preview = document.getElementById('contact-picture-preview'); // Select the preview element
        preview.src = e.target.result; // Set the preview source to the uploaded image
        preview.style.display = 'block'; // Make sure the image is visible
      };
      reader.readAsDataURL(file); // Convert the file into a base64 URL for preview
    }
  });


  document.getElementById('newProfilePhoto').addEventListener('change', function (event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    if (file) {
        reader.onload = function (e) {
            document.getElementById('profilePic').src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
});


  
  // Handle profile picture selection and preview
  document.addEventListener('change', function (event) {
    if (event.target.classList.contains('uploadProfileInput')) {
      const triggerInput = event.target;
      const holder = triggerInput.closest('.pic-holder');
      const wrapper = triggerInput.closest('.profile-pic-wrapper');
      const currentImg = holder.querySelector('.pic').src;
  
      triggerInput.blur();
      const files = triggerInput.files || [];
  
      if (!files.length || !window.FileReader) return;
  
      if (/^image/.test(files[0].type)) {
        const reader = new FileReader();
        reader.readAsDataURL(files[0]);
  
        reader.onloadend = function () {
          holder.classList.add('uploadInProgress');
          holder.querySelector('.pic').src = this.result;
  
          const loader = document.createElement('div');
          loader.classList.add('upload-loader');
          loader.innerHTML =
            '<div class="spinner-border text-primary" role="status"><span class="sr-only">Loading...</span></div>';
          holder.appendChild(loader);
  
          setTimeout(function () {
            holder.classList.remove('uploadInProgress');
            loader.remove();
  
            // Show a snackbar notification when the picture is updated
            const snackbar = document.createElement('div');
            snackbar.className = 'snackbar';
            snackbar.innerText = 'Profile picture updated!';
            wrapper.appendChild(snackbar);
            snackbar.classList.add('show');
            setTimeout(() => snackbar.classList.remove('show'), 3000);
          }, 1500);
        };
      }
    }
  });
  
  function searchContacts() {
    var li = document.getElementsByClassName("contact");
    let input = document.getElementById('search').value
    input = input.toLowerCase();
    let x = document.getElementsByClassName('contact-name');

    for (i = 0; i < x.length; i++) {
        if (!x[i].innerHTML.toLowerCase().includes(input)) {
            x[i].closest('.contact').style.display = "none";
        }
        else {
            x[i].closest('.contact').style.display = "block";
        }
    }
}