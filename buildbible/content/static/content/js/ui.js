function isTouchDevice() {
    return (('ontouchstart' in window) ||
        (navigator.maxTouchPoints > 0) ||
        (navigator.msMaxTouchPoints > 0));
}

if (isTouchDevice() === true) {
    (function (window, document) {
        var mainBox = $('#main'),
            menuBox = $('#menu'),
            menuButton = $('#menuLink'),
            body = $('body'),
            htmlBox = $('html');

        var maxTime = 1000, // allow movement if < 1000 ms (1 sec)
            maxDistance = 100, // swipe movement of 50 pixels triggers the swipe

            target = $('body'),
            startX = 0,
            startTime = 0,
            touch = "ontouchend" in document,
            startEvent = (touch) ? 'touchstart' : 'mousedown',
            moveEvent = (touch) ? 'touchmove' : 'mousemove',
            endEvent = (touch) ? 'touchend' : 'mouseup';

        target
            .bind(startEvent, function (e) {
                // prevent image drag (Firefox)
                // e.preventDefault();
                startTime = e.timeStamp;
                startX = e.originalEvent.touches ? e.originalEvent.touches[0].pageX : e.pageX;
            })
            .bind(endEvent, function (e) {
                startTime = 0;
                startX = 0;
            })
            .bind(moveEvent, function (e) {
                // e.preventDefault();
                var currentX = e.originalEvent.touches ? e.originalEvent.touches[0].pageX : e.pageX,
                    currentDistance = (startX === 0) ? 0 : Math.abs(currentX - startX),
                    // allow if movement < 1 sec
                    currentTime = e.timeStamp;
                if (startTime !== 0 && currentTime - startTime < maxTime && currentDistance > maxDistance) {
                    if (currentX < startX) {
                        // swipe left code here
                        if ($(menu).hasClass('active')) {
                            $(menuLink).trigger('click')
                            $(htmlBox).removeClass('active')
                        }

                    }
                    if (currentX > startX) {
                        // swipe right code here
                        if (!$(menu).hasClass('active')) {
                            $(menuLink).trigger('click')
                            $(htmlBox).addClass('active')
                        }
                    }
                    startTime = 0;
                    startX = 0;
                }
            });


        function AddActive() {
            $(body).addClass('active');
            $(htmlBox).addClass('active')
        }

        function RemActive() {
            $(body).removeClass('active');
            $(htmlBox).removeClass('active')
        }

        var layout = document.getElementById('layout'),
            menu = document.getElementById('menu'),
            menuLink = document.getElementById('menuLink'),
            content = document.getElementById('main');


        function toggleClass(element, className) {
            var classes = element.className.split(/\s+/),
                length = classes.length,
                i = 0;

            for (; i < length; i++) {
                if (classes[i] === className) {
                    classes.splice(i, 1);
                    break;
                }
            }
            // The className is not found
            if (length === classes.length) {
                classes.push(className);
            }

            element.className = classes.join(' ');
        }

        function toggleAll(e) {
            var active = 'active';

            e.preventDefault();
            toggleClass(layout, active);
            toggleClass(menu, active);
            toggleClass(menuLink, active);
        }

        menuLink.onclick = function (e) {
            toggleAll(e);
            if (isTouchDevice() === true) {
                if (!$(htmlBox).hasClass('active')) {
                    AddActive();
                } else {
                    RemActive();
                }
            }
        };

    }(this, this.document));
}