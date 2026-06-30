document.addEventListener('DOMContentLoaded', function () {
    const helloElement = document.querySelector('#hello');
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      helloElement.textContent = data.hello;
    });
});