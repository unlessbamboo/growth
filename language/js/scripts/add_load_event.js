/*
 * 将所有欲在 HTML 完整加载后执行的函数添加到队列中, 
 * 之后在onload事件触发时逐个执行
 */

function addLoadEvent(func) {
    var oldonload = window.onload;
    if (typeof window.onload != 'function') {
        window.onload = func;
    } else {
        window.onload = function() {
            oldonload();
            func();
        }
    }
}
