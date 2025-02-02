function group_main () {
  const group_names = document
    .getElementById('group_names')
    .getElementsByTagName('li')

  const names = document
    .getElementsByClassName('names')[0]
    .getElementsByTagName('a')

  hide_names(names)

  Array.from(group_names).forEach(group_name => {
    group_name.addEventListener('click', () => {
      deactivate_group_names(group_names)
      group_name.classList.add('active-group')
      hide_names(names)

      const final_group_name = group_name.getElementsByTagName('div')[0]
      show_names(names, final_group_name.textContent)
    })
  })
}

function hide_names (names) {
  Array.from(names).forEach(name => {
    name.classList.add('d-none')
  })
}

function show_names (names, group) {
  Array.from(names).forEach(my_name => {
    if (my_name.getAttribute('name') == group) {
      my_name.classList.remove('d-none')
    }
  })
}

function deactivate_group_names (group_names) {
  Array.from(group_names).forEach(group_name => {
    group_name.classList.remove('active-group')
  })
}

group_main()
