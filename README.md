[![Typing SVG](https://readme-typing-svg.herokuapp.com?size=25&color=0024F7&width=409&lines=Mini+Search+Engine+Project+)](https://git.io/typing-svg)
<hr>
<h1>Chronon:</h1>
<h2>Crawler, Database(mongo), and FrontFace:</h2>
<li>Autocomplete words</p>
<li>Input with voice</p>
<li>Input with check on empty string</p>
<li>Mini pagerank emulation</p>
<li>Crawler with good parse for testing</p>

<p>Pet-project to understand how search engins like Google works</p>

[![Preview](https://github.com/encoreone/Chronon/blob/master/src/Test/preview.gif)]([https://git.io/typing-svg](https://github.com/encoreone/Chronon))


<hr>
<h2>Requirements</h2>
    <li>python 3 / pip</li>
    <li>docker / docker-composer</li>
    <li>mongodb</li>
<hr>
<h2>How to run:</h2>
<h3>1) Install python depens:</h3>
<ul>
    <li>1) git clone this repo</ol>
    <li>2) cd to Chronon dir</ol>
    <li>3) pip install -r requirements.txt</ol>
</ul>

<h3>2) Open docker with mongodb cluster:</h3>
<ul>
    <li>1) cd src/</ol>
    <li>2) sudo docker-compose up</li>
    <strong>with example login and pass for db - root:root<strong>
</ul>

<h3>3) Run crawler:</h3>
<ul>
    <li>1) cd src/Crawler</ol>
    <li>2) python3 crawler.py [url for parse] [depth]</ol>
</ul>

<h3>4) Run webpage:</h3>
<ul>
    <li>1) cd src/Website</ol>
    <li>2) python3 app.py</ol>
</ul>