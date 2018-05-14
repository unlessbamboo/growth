/*
 * 遍历适配浏览器所有版本, 获取可用的 XMLHttp 对象
 */

function getHttpObject() {
    if (typeof XMLHttpRequest == 'undefined') {
        XMLHttpRequest = function() {
            try {
                return new ActiveXObject('Msxml2.XMLHTTP.6.0');
            } catch (e) {}

            try {
                return new ActiveXObject('Msxml2.XMLHTTP.3.0');
            } catch (e) {}

            try {
                return new ActiveXObject('Msxml2.XMLHTTP');
            } catch (e) {}
            return false;
        }
    }
    return new XMLHttpRequest();
}
