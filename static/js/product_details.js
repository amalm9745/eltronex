$(document).ready(function(){
    var $leftSlick = $('.slick-left');
    var $rightSlick = $('.slick-right');

    $leftSlick.slick({
        vertical: true,
        verticalSwiping: true,
        dots: false,
        infinite: false,
        arrow: false,
        prevArrow: false,
        nextArrow: false,
        speed: 300,
        slidesToShow: 5,
        slidesToScroll: 1,
        infinite: true,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 5,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: false,
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 4,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });

    $rightSlick.slick({
        dots: false,
        infinite: false,
        arrow: false,
        prevArrow: false,
        nextArrow: false,
        speed: 200,
        slidesToShow: 1,
        slidesToScroll: 1,
        infinite: true,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: false,
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });

    // Add click event listener to left slick images
    $leftSlick.on('click', '.slick-slide', function(){
        var index = $(this).attr('data-slick-index');
        $rightSlick.slick('slickGoTo', parseInt(index));
    });


    // External button functionality
$('.left-btn').click(function() {
            $('.slick-left').slick('slickPrev');
        });

$('.right-btn').click(function() {
    $('.slick-left').slick('slickNext');
});
});



function showContent(contentId) {
    // Hide all content divs
    var contents = document.querySelectorAll('.content');
    contents.forEach(function(content) {
      content.style.display = 'none';
    });
    
    // Show the selected content div
    var selectedContent = document.getElementById(contentId);
    if (selectedContent) {
      selectedContent.style.display = 'block';
    }
  }


//   wishlist button
//   const likeButtons = document.querySelectorAll(".wishlist-icon");

//   likeButtons.forEach((likeButton) => {
//     likeButton.addEventListener("click", () => {
//       likeButton.classList.toggle("wishlist-icon--like");
//     });
//   });


const likeButtons = document.querySelectorAll(".wishlist-icon");

likeButtons.forEach((likeButton) => {
    likeButton.addEventListener("click", () => {
        const variantId = likeButton.dataset.variantId;
        const isLiked = likeButton.classList.contains("wishlist-icon--like");
        const csrftoken = getCookie('csrftoken');

        // Send AJAX request to add or remove product from wishlist
        $.ajax({
            type: "POST",
            url: "/add-to-wishlist/" + variantId + "/",
            data: {
                csrfmiddlewaretoken: csrftoken
            },
            success: function(response) {
                if (response.success) {
                    // Toggle button styling based on whether product is in wishlist or not
                    if (isLiked) {
                        likeButton.classList.remove("wishlist-icon--like");
                    } else {
                        likeButton.classList.add("wishlist-icon--like");
                    }
                } else {
                    // Handle the case where the user is not logged in
                    alert("Please log in to add the product to wishlist.");
                }
            },
            error: function(xhr, errmsg, err) {
                // Handle any errors that occur during the AJAX request
                alert("Error occurred while adding product to wishlist. Please try again later.");
            }
        });
    });
});


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}