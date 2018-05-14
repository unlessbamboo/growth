function createCORSRequest() {
    var xhr = getHttpObject();
    if (typeof XDomainRequest != "undefined") {
        // Otherwise, check if XDomainRequest.
        // XDomainRequest only exists in IE, and is IE's way of making CORS requests.
        xhr = new XDomainRequest();

    } else if (!("withCredentials" in xhr)) {
        // Otherwise, CORS is not supported by the browser.
        xhr = null;
    }
    return xhr;
}


function getImageContent() {
    var request = createCORSRequest();

    if (request) {
        request.open('GET', 'https://www.baidu.com/img/bd_logo1.png', true);
        request.onreadystatechange = function() {
            if (request.readyState == 4) {
                var para = document.createElement('p');
                var text = document.createTextNode(request.responseText);
                
                para.appendChild(text);
                document.getElementById('new').appendChild(para);
            }
        };
        request.send(null);
    } else {
        alert('Sorry, your browser does not support XMLHttpRequest.');
    }
}

addLoadEvent(getImageContent);
