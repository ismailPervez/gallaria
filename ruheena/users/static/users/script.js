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

            const link = modalCard.querySelector('#post-link')
            link.onclick = (e) => {
                e.stopPropagation()
                const imageSrc = e.target.parentElement.parentElement.querySelector('img').src
                navigator.clipboard.writeText(imageSrc);
                const copyMsg = document.getElementById('copy-msg')
                copyMsg.style.opacity = '1'
                setTimeout(() => {
                    copyMsg.style.opacity = '0'
                }, 1000)
            }
        })
    }

    modalContainer.onclick = (e) => {
        modalContainer.style.visibility = 'hidden'
    }
}