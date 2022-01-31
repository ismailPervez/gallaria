window.onload = () => {
    const modalContainer = document.querySelector('.modal-container')
    const modal = document.querySelector('.pop-up')

    const cards = document.querySelectorAll('.card img')
    if (cards.length > 0) {
        cards.forEach(card => {
            card.onclick = (e) => {
                // console.log(e.target)
                modal.querySelector('img').src = e.target.src
                modal.querySelector('p').textContent = e.target.alt
                modalContainer.style.visibility = 'visible'
            }
        })
    }

    modalContainer.onclick = () => {
        modalContainer.style.visibility = 'hidden'
    }
}