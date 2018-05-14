/*
 * ready(onLoad)
 */
$(function() {
  //some elements..
  var $ps_container = $('#ps_container'),
    $ps_image_wrapper = $ps_container.find('.ps_image_wrapper'),
    $ps_next = $ps_container.find('.ps_next'),
    $ps_prev = $ps_container.find('.ps_prev'),
    $ps_nav = $ps_container.find('.ps_nav'),
    $tooltip = $ps_container.find('.ps_preview'),
    $ps_preview_wrapper = $tooltip.find('.ps_preview_wrapper'),
    $links = $ps_nav.children('li').not($tooltip),
    total_images = $links.length,
    currentHovered = -1,
    current = 0,
    $loader = $('#loader');

  /*check if you are using a browser*/
  console.log('需要加载的图片数量: ', total_images);
  var ie = false;
  if ($.support.msie) {
    ie = true; //you are not!Anyway let's give it a try
  }
  if (!ie) {
    // jQuery: 设置css属性
    $tooltip.css({
      // 设置不透明度
      opacity: 0
    }).show();
  }


  /*
   * first preload images (thumbs and large images)
   * 其中links中包含class=='ps_nav'中的<li>列表
   */
  var loaded = 0;
  $links.each(function(i) {
    var $link = $(this);
    // console.log('Current link:', $link);

    // preload见js/preload.js文件: 
    //    执行preload函数, 预加载图片
    //    传入options, 在preload函数中被调用
    $link.find('a').preload({
      // onComplete是个自定义函数, 并非事件
      onComplete: function() {
        ++loaded;
        console.log('进入加载函数:', loaded);
        if (loaded == total_images) {
          //all images preloaded, show ps_container and initialize events
          $loader.hide();
          // 显示隐藏或者display:none的元素
          $ps_container.show();
          // 使用bind: 为匹配元素绑定事件,处理函数, 绑定多个事件
          // 其中mouseenter/mouseleave仅仅适用于IE, 目前已经符合 HTML 标准
          $links.bind('mouseenter', showTooltip)
            .bind('mouseleave', hideTooltip)
            .bind('click', showImage);
          //navigate through the images
          $ps_next.bind('click', nextImage);
          $ps_prev.bind('click', prevImage);
        }
      }
    });
  });

  function showTooltip() {
    var $link = $(this);
    // 返回link相对于同辈元素的偏移量(第几个元素)
    var idx = $link.index();
    // 获取第一个元素的外部宽度(padding, border, margin)
    var linkOuterWidth = $link.outerWidth();
    // parseFloat解析字符串, 返回浮点型
    var left = parseFloat(idx * linkOuterWidth) - $tooltip.width() / 2 + linkOuterWidth / 2,
      //the thumb image source
      $thumb = $link.find('a').attr('rel'),
      imageLeft;

    //if we are not hovering the current one
    if (currentHovered != idx) {
      //check if we will animate left->right or right->left
      if (currentHovered != -1) {
        if (currentHovered < idx) {
          imageLeft = 75;
        } else {
          imageLeft = -75;
        }
      }
      currentHovered = idx;

      //the next thumb image to be shown in the tooltip
      var $newImage = $('<img/>').css('left', '0px')
        .attr('src', $thumb);

      //if theres more than 1 image 
      //(if we would move the mouse too fast it would probably happen)
      //then remove the oldest one (:last)
      if ($ps_preview_wrapper.children().length > 1)
        $ps_preview_wrapper.children(':last').remove();

      //prepend the new image
      $ps_preview_wrapper.prepend($newImage);

      var $tooltip_imgs = $ps_preview_wrapper.children(),
        tooltip_imgs_count = $tooltip_imgs.length;

      //if theres 2 images on the tooltip
      //animate the current one out, and the new one in
      if (tooltip_imgs_count > 1) {
        $tooltip_imgs.eq(tooltip_imgs_count - 1)
          .stop()
          .animate({
            left: -imageLeft + 'px'
          }, 150, function() {
            //remove the old one
            $(this).remove();
          });
        $tooltip_imgs.eq(0)
          .css('left', imageLeft + 'px')
          .stop()
          .animate({
            left: '0px'
          }, 150);
      }
    }
    //if we are not using a "browser", we just show the tooltip,
    //otherwise we fade it
    //
    if (ie) {
      $tooltip.css('left', left + 'px').show();
    } else {
      $tooltip.stop()
        .animate({
          left: left + 'px',
          opacity: 1
        }, 150);
    }
  }

  function hideTooltip() {
    //hide / fade out the tooltip
    if (ie)
      $tooltip.hide();
    else
      $tooltip.stop()
      .animate({
        opacity: 0
      }, 150);
  }

  /*
   * 将图片展示在ps_image_wrapper中
   */
  function showImage(e) {
    var $link = $(this),
      idx = $link.index(),
      $image = $link.find('a').attr('href'),
      $currentImage = $ps_image_wrapper.find('img'),
      currentImageWidth = $currentImage.width();

    //if we click the current one return
    if (current == idx) return false;

    // 创建一个新的img元素, 宽度一般为636, style: left: 0px
    // 这里必须延迟等待图片加载完成, 否则可能返回0, 需要提前对图片预加载
    var $newImage = $('<img/>').css('left', currentImageWidth + 'px')
      .attr('src', $image);
    // 在开头插入新的图片
    $ps_image_wrapper.prepend($newImage);
    // 获取图片宽度
    var newImageWidth = $newImage.width();
    if (newImageWidth == 0) {
      // 没有加载完全, 避免后续出现问题
      console.log('Zero Width:', newImageWidth, ' Image:', $newImage);
      // 恢复
      $ps_image_wrapper.children(':first').remove();
      return false;
    }

    // 移除上一个(current)元素的class标签
    $links.eq(current).removeClass('selected');
    // 在当前元素中增加class标签
    $link.addClass('selected');

    // 使用伪类选择器, 删除ps_image_wrapper中的最后一个元素, 并在开头插入新元素
    if ($ps_image_wrapper.children().length > 2)
      $ps_image_wrapper.children(':last').remove();
    // current: 表示当前事件触发时, 老的图片下标
    // idx: 当前触发的图片下标
    // 如果current > idx: 查看前面的图片
    if (current > idx) {
      $newImage.css('left', -newImageWidth + 'px');
      currentImageWidth = -newImageWidth;
    }
    console.log('Idx:', idx, ' Current:', current);
    current = idx;

    // stop停止匹配元素正在执行的动画
    // animate: 根据css属性来执行自定义动画, 350表示运行时间
    // $ps_image_wrapper.stop().animate({
    //   width: newImageWidth + 'px'
    // }, 350);
    console.log('New Image Width:', newImageWidth);
    console.log('New Image:', $newImage);
    console.log('Current:', $currentImage);
    console.log('CurrentImageWidth:', currentImageWidth);

    $ps_image_wrapper.css('width', newImageWidth + 'px');
    $newImage.stop().animate({
      left: '0px'
    }, 350);
    $currentImage.stop().animate({
      left: -currentImageWidth + 'px'
    }, 350);

    e.preventDefault();
  }

  function nextImage() {
    // current由showImage来触发, 这是一个闭包
    if (current < total_images) {
      // 自动触发(trigger)li->a的事件回调, 实际上就是showImage函数
      $links.eq(current + 1).trigger('click');
    }
  }

  function prevImage() {
    if (current > 0) {
      // 自动触发li->a的事件回调, 实际上就是showImage函数
      $links.eq(current - 1).trigger('click');
    }
  }
});


// 在 DOM 载入之后执行, 先于onload事件
$(document).ready(function() {
  // 利用animate来执行动画效果, 其中opacity表示透明度
  // 这里对工作经历中->图片进行动画效果, 鼠标悬浮时变淡
  // hover的两个元素, 分别表示进入, 离开时的回调
  $('.projects li figure a img').animate({
    'opacity': 1
  }).hover(function() {
    $(this).animate({
      'opacity': 0.5
    });
  }, function() {
    $(this).animate({
      'opacity': 1
    });
  });

  // 我最近的工作
  $('.zoom img').animate({
    'opacity': 1
  }).hover(function() {
    $(this).animate({
      'opacity': 0.5
    });
  }, function() {
    $(this).animate({
      'opacity': 1
    });
  });

  // 找到work中的rel="work"的图片
  $("a[rel=work]").fancybox({
    'transitionIn': 'elastic',
    'transitionOut': 'elastic',
    'titlePosition': 'over',
    'titleFormat': function(title, currentArray, currentIndex, currentOpts) {
      return '<span id="fancybox-title-over">Image ' + (currentIndex + 1) + ' / ' +
        currentArray.length + (title.length ? ' &nbsp; ' + title : '') + '<\/span>';
    }
  });
  $("a[rel=recent_work]").fancybox({
    'transitionIn': 'elastic',
    'transitionOut': 'elastic',
    'titlePosition': 'over',
    'titleFormat': function(title, currentArray, currentIndex, currentOpts) {
      return '<span id="fancybox-title-over">Image ' + (currentIndex + 1) + ' / ' +
        currentArray.length + (title.length ? ' &nbsp; ' + title : '') + '<\/span>';
    }
  });
});
