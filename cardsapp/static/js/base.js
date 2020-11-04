const cards = document.querySelectorAll('.card2');

function transition() {
  if (this.classList.contains('active2')) {
    this.classList.remove('active2')
  } else {
    this.classList.add('active2');
  }
}

cards.forEach(card => card.addEventListener('click', transition));