const input = document.querySelector('#search');
const suggestions = document.querySelector('.suggestions ul');
const keywords = [
    'Wikipedia',
    'Wildberries',
    'Winrar',
    'Windows',
	'Википедия',
	'Google',
	'Yandex',
	'Яндекс',
	'Apple',
	'Amazon',
	'Steam',
	'DNS',
	'Днс',
	'Кошки',
	'Собаки',
	'Планеты',
	'Илон Маск',
	'Цвет',
	'Javascript',
	'Поисковая система'
];


function search(str) {
	let results = [];
	const val = str.toLowerCase();

	for (i = 0; i < keywords.length; i++) {
		if (keywords[i].toLowerCase().indexOf(val) > -1) {
			results.push(keywords[i]);
		}
	}

	return results;
}

function searchHandler(e) {
	const inputVal = e.currentTarget.value;
	let results = [];
	if (inputVal.length > 0) {
		results = search(inputVal);
	}
	showSuggestions(results, inputVal);
}

function showSuggestions(results, inputVal) {
    
    suggestions.innerHTML = '';

	if (results.length > 0) {
		for (i = 0; i < results.length; i++) {
			let item = results[i];
			const match = item.match(new RegExp(inputVal, 'i'));
			item = item.replace(match[0], `<strong>${match[0]}</strong>`);
			suggestions.innerHTML += `<li>${item}</li>`;
		}
		suggestions.classList.add('has-suggestions');
	} else {
		results = [];
		suggestions.innerHTML = '';
		suggestions.classList.remove('has-suggestions');
	}
}

function useSuggestion(e) {
	input.value = e.target.innerText;
	input.focus();
	suggestions.innerHTML = '';
	suggestions.classList.remove('has-suggestions');
}

input.addEventListener('keyup', searchHandler);
suggestions.addEventListener('click', useSuggestion);