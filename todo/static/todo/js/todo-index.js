document.addEventListener("DOMContentLoaded", function() {
  const not_complete_button = document.getElementById("not_complete");
  const complete_button = document.getElementById("complete");

  not_complete_button.addEventListener("click", function() {
    not_complete_button.style.display = "none";
    complete_button.style.display = "block";
  });

  complete_button.addEventListener("click", function() {
    complete_button.style.display = "none";
    not_complete_button.style.display = "block";
  });
});
