function command_main () {
  const buttons = document
    .getElementsByClassName('actions')[0]
    .getElementsByTagName('div')
  const boxes = document.getElementsByClassName('commands')

  hideBoxes(boxes)
  deactivate(buttons)

  Array.from(buttons).forEach((el, index) => {
    el.addEventListener('click', () => {
      deactivate(buttons)
      hideBoxes(boxes)
      boxes[index].classList.remove('d-none')
      el.classList.add('com-active')
    })
  })
}

function deactivate (buttons) {
  Array.from(buttons).forEach(el => {
    el.classList.remove('com-active')
  })
}

function hideBoxes (boxes) {
  Array.from(boxes).forEach(el => {
    el.classList.add('d-none')
  })
}

command_main()
