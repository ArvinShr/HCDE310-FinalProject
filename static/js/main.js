const slider = document.getElementById("min_rating");
const ratingLabel = document.getElementById("rating-label");

if (slider && ratingLabel) {
  slider.addEventListener("input", () => {
    ratingLabel.textContent = parseFloat(slider.value).toFixed(1);
  });
}

const randomBtn = document.getElementById("random-btn");

if (randomBtn) {
  randomBtn.addEventListener("click", () => {
    const cards = Array.from(document.querySelectorAll(".movie-card"));
    if (cards.length === 0) return;

    cards.forEach(c => c.classList.remove("highlight"));

    const pick = cards[Math.floor(Math.random() * cards.length)];
    pick.classList.add("highlight");
    pick.scrollIntoView({ behavior: "smooth", block: "center" });
  });
}