
  ["name", "email", "message"].forEach(function (field) {
    document.getElementById(`${field}-input`).addEventListener("input", function (event) {
      const label = document.getElementById(`${field}-label`);
      if (event.target.value !== "") {
        label.classList.add("label-up");
      } else {
        label.classList.remove("label-up");
      }
    });
  });


