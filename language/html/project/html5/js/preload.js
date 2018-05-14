/*
the images preload plugin
另见: https://github.com/htmlhero/jQuery.preload
*/
(function($) {
  // 设定preload函数, 其中
  //    $.fn == $.prototype
  //    $.extent 添加类方法, 或者合并多个类变为一个类(就是添加类方法嘛)
  //    $.fn.extent 添加成员函数
  // 实现功能: 预先载入图片, 避免鼠标滑动时的延迟现象(宽度为0, 出现错误)
  $.fn.preload = function(options) {
    // 将两个或者更多对象拼合成一个对象, options为字典, key为函数
    var opts = $.extend({}, $.fn.preload.defaults, options);
    var o = $.meta ? $.extend({}, opts, this.data()) : opts;

    // 1 attr用于设置/返回属性值
    // .each 遍历jQuery对象, 为每个匹配元素执行一个函数
    // 这里表示遍历调用this中的所有对象.
    console.log('This Length:', this);
    return this.each(function() {
      var $e = $(this),
        t = $e.attr('rel'),
        i = $e.attr('href'),
        l = 0;

      // 向('<img/>')中添加load事件, 对象为当前选定的JQuery对象的元素
      // 返回值: jQuery对象
      // l == 2 用于确保<img/>中的href和rel都加载完毕后才触发, 这里使用到闭包
      // 这里会有问题: 当前图片加载完成的, 但是在触发nextImage, 下一组图片未加载
      $('<img/>').on('load', function(i) {
        ++l;
        if (l == 2) o.onComplete();
      }).attr('src', i);

      $('<img/>').on('load', function(i) {
        ++l;
        if (l == 2) o.onComplete();
      }).attr('src', t);
    });
  };

  $.fn.preload.defaults = {
    onComplete: function() {
      return false;
    }
  };
})(jQuery);
