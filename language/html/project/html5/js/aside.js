/*
 * aside ready
 * 用于侧边栏当前活跃链接的显示
 */
$(function() {
  var menu = $('#sidebar nav ul li');

  menu.each(function(i) {
    $(this).first().bind('click', function() {
      var active = $(this).siblings('li.active');
      // 注意, remove/css用于设置css, 这里需要设置HTML属性
      active.removeAttr('class');
      $(this).attr('class', 'active');
    });
  });
});
