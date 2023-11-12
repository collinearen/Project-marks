const siteUrl = '//127.0.0.1:8000/';
const styleUrl = siteUrl + 'static/css/bookmarklet.css';
const minWidth = 250;
const minHeight = 250;
const maxWidth = 1920;
const maxHeight = 1080;

// Загружаем CSS
var head = document.getElementsByTagName('head')[0];  // Get HTML head element
var link = document.createElement('link'); // Create new link Element
link.rel = 'stylesheet'; // set the attributes for link element
link.type = 'text/css';
link.href = styleUrl + '?r=' + Math.floor(Math.random() * 9999999999999999);
head.appendChild(link);  // Append link element to HTML head

// Загружаем HTML-страницу
var body = document.getElementsByTagName('body')[0];
boxHtml = `
  <div id="bookmarklet">
    <a href="#" id="close">&times;</a>
    <h1>Выберите нужное изображение</h1>
    <div class="images"></div>
  </div>`;
body.innerHTML += boxHtml;

function bookmarkletLaunch() {
    bookmarklet = document.getElementById('bookmarklet');
    var imagesFound = bookmarklet.querySelector('.images');

    // Очистить поиск картинок
    imagesFound.innerHTML = '';
    // display bookmarklet
    bookmarklet.style.display = 'block';

    // Закрыть событие
    bookmarklet.querySelector('#close')
        .addEventListener('click', function () {
            bookmarklet.style.display = 'none'
        });

    // Поиск изображений в DOM с релевантными размерами
    images = document.querySelectorAll('img[src$=".jpg"], img[src$=".jpeg"], img[src$=".png"], img[src$=".webp"]');
    images.forEach(image => {
        if (image.naturalWidth >= minWidth
            && image.naturalHeight >= minHeight
            && image.naturalHeight <= maxHeight
            && image.naturalWidth <= maxWidth
        ) {
            var imageFound = document.createElement('img');
            imageFound.src = image.src;
            imagesFound.append(imageFound);
        }
    })

    // Событие выбора картинок по селекторам
    // Дальше перенаправляем на наш сайт с тремя GET-запросами: website_url, title и путь к изображению

    imagesFound.querySelectorAll('img').forEach(image => {
        image.addEventListener('click', function (event) {
            imageSelected = event.target;
            bookmarklet.style.display = 'none';
            window.open(siteUrl + 'images/create/?url='
                + encodeURIComponent(imageSelected.src)
                + '&title='
                + encodeURIComponent(document.title)
                + '&website_url='
                + window.location.href,
                '_blank');
        })
    })
}

// Загружаем
bookmarkletLaunch();
