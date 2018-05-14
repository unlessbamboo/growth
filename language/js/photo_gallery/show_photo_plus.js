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
    if (!document.getElementsByTagName) return false;
    if (!document.getElementById) return false;

    var gallery = document.getElementById('imagegallery');
    if (!gallery) {
        return false;
    }
    var links = gallery.getElementsByTagName('a');
    for (var i=0; i < links.length; i++) {
        links[i].onclick = function() {
            return !showPicPlus(this);
        }
        // links[i].onkeydown = links[i].onclick;
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
addLoadEvent(prepareGallery);
