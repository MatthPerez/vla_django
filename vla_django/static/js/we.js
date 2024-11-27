const titles = document.getElementsByTagName('h3')
const meetings = document.getElementsByClassName('meeting')

function we_main () {
  Array.from(titles).forEach((title, index) => {
    title.addEventListener('click', () => {
      deactivateTitles()
      meetings[index].classList.toggle('auto-height')
    })
  })
}

function deactivateTitles () {
  Array.from(titles).forEach(title => {
    title.classList.remove('auto-height')
  })
}

we_main()
