document.addEventListener("DOMContentLoaded", function() {

  const form = document.getElementById("contactForm");

  form.addEventListener("input", function(event) {

    const field = event.target;

    const label = form.querySelector(`label[for="${field.id}"]`);

    if(field.value !== '') {
      label.classList.add('label-up');
    } else {
      label.classList.remove('label-up');
    }

  });

});


