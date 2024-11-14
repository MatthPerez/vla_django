function main_new_vcm () {
  const cursor = document.getElementById('cursor')

  document.addEventListener('mousemove', event => {
    cursor.style.left = `${event.clientX}px`
    cursor.style.top = `${event.clientY}px`
  })
}

main_new_vcm()
