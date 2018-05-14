function insertAfter(newElement, targetElement){
    var p = targetElement.parentNode;
    if (p.lastChild == targetElement) {
        p.appendChild(newElement);
    } else {
        p.insertBefore(newElement, targetElement.nextSibling);
    }
}

/* 
 * 动态创建标记
 */
function preparePlaceholder() {
    if (!document.createElement) return false;
    if (!document.createTextNode) return false;
    if (!document.getElementById) return false;
    if (!document.getElementsByTagName) return false;

    var gallery = document.getElementById('imagegallery');
    if (!gallery) return false;

    var placeholder = document.createElement('img');
    placeholder.setAttribute('id', 'placeholder');
    placeholder.setAttribute(
        'src',
        'https://img.huxiucdn.com/article/cover/201709/21/064153037670.jpg?imageView2/1/w/800/h/600/|imageMogr2/strip/interlace/1/quality/85/format/jpg');
    placeholder.setAttribute('alt', 'My Image Gallery');
    placeholder.setAttribute('width', '400');

    var description = document.createElement('p');
    description.setAttribute('id', 'description');
    var doctext = document.createTextNode('Choose an Image');
    description.appendChild(doctext);

    insertAfter(placeholder, gallery);
    insertAfter(description, placeholder);
}

function showPicPlus(whichpic){
    var placeholder = document.getElementById('placeholder');
    if (!placeholder || placeholder.nodeName != 'IMG') {
        return false;
    }

    var source = whichpic.getAttribute('href');
    placeholder.setAttribute('src', source);

    var description = document.getElementById('description');
    if (description) {
        var text = whichpic.getAttribute('title');
        description.firstChild.nodeValue = text ? text : '========';
    }
    return true;
}

function prepareGallery() {
    if (!document.createElement) return false;
    if (!document.createTextNode) return false;

    var gallery = document.getElementById('imagegallery');
    if (!gallery) {
        return false;
    }
    var links = gallery.getElementsByTagName('a');
    for (var i=0; i < links.length; i++) {
        links[i].onclick = function() {
            return !showPicPlus(this);
        }
    }
}

function addLoadEvent(func) {
    var oldOnload = window.onload;
    if (typeof window.onload != 'function') {
        window.onload = func;
    } else {
        window.onload = function() {
            oldOnload();
            func();
        }
    }
}

// 加载
addLoadEvent(preparePlaceholder);
addLoadEvent(prepareGallery);
