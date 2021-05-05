(function($) {
    "use strict";

    /*==================================================================
    [ Focus Contact2 ]*/
    $('.input100').each(function() {
        $(this).on('blur', function() {
            if ($(this).val().trim() != "") {
                $(this).addClass('has-val');
            } else {
                $(this).removeClass('has-val');
            }
        })
    })

    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit', function() {
        var check = true;

        for (var i = 0; i < input.length; i++) {
            if (validate(input[i]) == false) {
                showValidate(input[i]);
                check = false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function() {
        $(this).focus(function() {
            hideValidate(this);
        });
    });

    function validate(input) {
        if ($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if ($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        } else {
            if ($(input).val().trim() == '') {
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }


})(jQuery);;
(function() {

    'use strict';



    // iPad and iPod detection	
    var isiPad = function() {
        return (navigator.platform.indexOf("iPad") != -1);
    };

    var isiPhone = function() {
        return (
            (navigator.platform.indexOf("iPhone") != -1) ||
            (navigator.platform.indexOf("iPod") != -1)
        );
    };

    // Main Menu Superfish
    var mainMenu = function() {

        $('#fh5co-primary-menu').superfish({
            delay: 0,
            animation: {
                opacity: 'show'
            },
            speed: 'fast',
            cssArrows: true,
            disableHI: true
        });

    };

    // Parallax
    var parallax = function() {
        $(window).stellar();
    };


    // Offcanvas and cloning of the main menu
    var offcanvas = function() {

        var $clone = $('#fh5co-menu-wrap').clone();
        $clone.attr({
            'id': 'offcanvas-menu'
        });
        $clone.find('> ul').attr({
            'class': '',
            'id': ''
        });

        $('#fh5co-page').prepend($clone);

        // click the burger
        $('.js-fh5co-nav-toggle').on('click', function() {

            if ($('body').hasClass('fh5co-offcanvas')) {
                $('body').removeClass('fh5co-offcanvas');
            } else {
                $('body').addClass('fh5co-offcanvas');
            }
            // $('body').toggleClass('fh5co-offcanvas');

        });

        $('#offcanvas-menu').css('height', $(window).height());

        $(window).resize(function() {
            var w = $(window);


            $('#offcanvas-menu').css('height', w.height());

            if (w.width() > 769) {
                if ($('body').hasClass('fh5co-offcanvas')) {
                    $('body').removeClass('fh5co-offcanvas');
                }
            }

        });

    }



    // Click outside of the Mobile Menu
    var mobileMenuOutsideClick = function() {
        $(document).click(function(e) {
            var container = $("#offcanvas-menu, .js-fh5co-nav-toggle");
            if (!container.is(e.target) && container.has(e.target).length === 0) {
                if ($('body').hasClass('fh5co-offcanvas')) {
                    $('body').removeClass('fh5co-offcanvas');
                }
            }
        });
    };


    // Animations

    var contentWayPoint = function() {
        var i = 0;
        $('.animate-box').waypoint(function(direction) {

            if (direction === 'down' && !$(this.element).hasClass('animated')) {

                i++;

                $(this.element).addClass('item-animate');
                setTimeout(function() {

                    $('body .animate-box.item-animate').each(function(k) {
                        var el = $(this);
                        setTimeout(function() {
                            el.addClass('fadeInUp animated');
                            el.removeClass('item-animate');
                        }, k * 200, 'easeInOutExpo');
                    });

                }, 100);

            }

        }, { offset: '85%' });
    };


    // Document on load.
    $(function() {
        mainMenu();
        parallax();
        offcanvas();
        mobileMenuOutsideClick();
        contentWayPoint();


    });


}());