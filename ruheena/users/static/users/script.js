window.onload = () => {
    const modalContainer = document.querySelector('.modal-container')
    const modalCard = document.querySelector('.pop-up')

    const cards = document.querySelectorAll('.card img')
    if (cards.length > 0) {
        cards.forEach(card => {
            card.onclick = (e) => {
                modalCard.querySelector('img').src = e.target.src
                modalCard.querySelector('p').textContent = e.target.alt
                modalCard.querySelector('#date').textContent = 'date posted: ' + e.target.dataset.date
                modalCard.querySelector('#author').textContent = 'posted by: ' + e.target.dataset.author
                modalContainer.style.visibility = 'visible'
            }
        })
    }

    modalContainer.onclick = () => {
        modalContainer.style.visibility = 'hidden'
    }
}