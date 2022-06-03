const blockedForm = document.querySelector('#form');
const searchInput = document.querySelector('#search');


blockedForm.addEventListener('submit', evt => {
    evt.preventDefault();

    if (searchInput.value == '')
        return false
    else if (searchInput.value == ' ')
        return false
    else if (searchInput.value == '  ')
        return false
    else if (searchInput.value == '   ')
        return false
    else if (searchInput.value == '    ')
        return false
    else if (searchInput.value == '     ')
        return false

    blockedForm.submit()
})