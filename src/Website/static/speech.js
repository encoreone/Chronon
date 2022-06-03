const voice = document.querySelector('#voice');
const inputOne = document.querySelector('#search');
const resultForm = document.querySelector('#form');


let promise = voice.addEventListener('click', () => {
    window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    const rec = new window.SpeechRecognition();
    rec.interimResults = true;
        
    rec.addEventListener('result', (e) => {
    
        const text = Array.from(e.results)
            .map(results => results[0])
            .map(results => results.transcript)
            .join('');

        inputOne.value = text

        setTimeout(function () {
            resultForm.submit();
        }, 2000)
    })
    
    rec.start();
})