const sb = document.querySelector('#search');


window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

const rec = new window.SpeechRecognition();
rec.interimResults = true;


let kek = document.createElement('input');

rec.addEventListener('result', (e) => {

    const text = Array.from(e.results)
        .map(results => results[0])
        .map(results => results.transcript)
        .join('');

        kek.innerHTML = text;

    sb.appendChild(kek);

    console.log(text);
})

rec.start();