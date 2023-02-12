// Show the Modal view for the gallery images // 
const modal = document.getElementById("modal");
const close = document.getElementById("close");
const modalImg = document.getElementById("modalImg");
const caption = document.getElementById("caption");
const myImg = document.querySelectorAll(".gallery-img");
const prevBtn = document.getElementById("prev");
const nextBtn = document.getElementById("next");

let currentIdx = 0;

myImg.forEach((img, idx) => {
  img.addEventListener("click", () => {
    currentIdx = idx;
    showImage(currentIdx);
  });
});

prevBtn.addEventListener("click", () => {
  if (currentIdx === 0) {
    currentIdx = myImg.length - 1;
  } else {
    currentIdx--;
  }

  showImage(currentIdx);
});

nextBtn.addEventListener("click", () => {
  if (currentIdx === myImg.length - 1) {
    currentIdx = 0;
  } else {
    currentIdx++;
  }

  showImage(currentIdx);
});

function showImage(idx) {
  modal.style.display = "block";
  modalImg.src = myImg[idx].src;
  caption.innerHTML = myImg[idx].alt;
}

close.addEventListener("click", () => {
  modal.style.display = "none";
});

// End of Gallery Model JS section //