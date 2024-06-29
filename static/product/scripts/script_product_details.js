let modal_section = document.getElementById("modal_section_detail");
let product_details = document.getElementById("product_details");
let left_modal_section = document.querySelector(".left_modal_section");

//show modal

product_details.addEventListener("click", () => {
    modal_section.classList.add("active");
    modal_section.classList.remove("hide");
    document.querySelector("body").classList.add("freeze_body");
});

//close modal

left_modal_section.addEventListener("click", () => {
    modal_section.classList.add("hide");
    modal_section.classList.remove("active");
    document.querySelector("body").classList.remove("freeze_body");
});

let close_icon_modal = document.getElementById("close_icon_modal");

close_icon_modal.addEventListener("click", () => {
    modal_section.classList.add("hide");
    modal_section.classList.remove("active");
    document.querySelector("body").classList.remove("freeze_body");
});


//modal_menu
let bac_menu_right = document.querySelector(".bac_menu_right");
let close_icon = document.querySelector(".bx-x");
let menu_icon = document.getElementById("menu_icon");

let container_menu_modal = document.querySelector(".container_menu_modal");

menu_icon.addEventListener("click", () => {
    container_menu_modal.classList.remove("hide");
    container_menu_modal.classList.add("show");
    document.querySelector("body").classList.add("freeze_body");

});

bac_menu_right.addEventListener("click", () => {
    container_menu_modal.classList.add("hide");
    container_menu_modal.classList.remove("show");
    document.querySelector("body").classList.remove("freeze_body");

});

close_icon.addEventListener("click", () => {
    container_menu_modal.classList.add("hide");
    container_menu_modal.classList.remove("show");
    document.querySelector("body").classList.remove("freeze_body");

});


//end modal menu


// <!-- Measurements -->

let modal_section_measurements = document.getElementById(
    "modal_section_measurements"
);
let measurements = document.getElementById("measurements");
let left_modal_section_measurements = document.querySelector(
    ".left_modal_section_measurements"
);


//show modal

measurements.addEventListener("click", () => {
    modal_section_measurements.classList.add("active");
    modal_section_measurements.classList.remove("hide");
    document.querySelector("body").classList.add("freeze_body");
});

//close modal

left_modal_section_measurements.addEventListener("click", () => {
    modal_section_measurements.classList.add("hide");
    modal_section_measurements.classList.remove("active");
    document.querySelector("body").classList.remove("freeze_body");
});


let close_icon_modal_measurements = document.getElementById(
    "close_icon_modal_measurements"
);

close_icon_modal_measurements.addEventListener("click", () => {
    modal_section_measurements.classList.add("hide");
    modal_section_measurements.classList.remove("active");
    document.querySelector("body").classList.remove("freeze_body");
});

//close or open modal packaging in measurements

let btn_packaging_down = document.getElementById("btn_packaging_down");
let packaging_content = document.querySelector(".packaging_content");

btn_packaging_down.addEventListener("click", () => {
    packaging_content.classList.toggle("active");
    packaging_content.classList.toggle("hide");
    btn_packaging_down.classList.toggle("rotate");
});

//close or open modal comments

let comments_btn = document.getElementById("comments_btn");
let modal_section_comments = document.getElementById("modal_section_comments");
let left_modal_section_comments = document.querySelector(
    ".left_modal_section_comments"
);
let close_icon_modal_comments = document.getElementById(
    "close_icon_modal_comments"
);

comments_btn.addEventListener("click", () => {
    modal_section_comments.classList.add("active");
    modal_section_comments.classList.remove("hide");
    document.querySelector("body").classList.add("freeze_body");
});

left_modal_section_comments.addEventListener("click", () => {
    modal_section_comments.classList.remove("active");
    modal_section_comments.classList.add("hide");
    document.querySelector("body").classList.remove("freeze_body");
});

close_icon_modal_comments.addEventListener("click", () => {
    modal_section_comments.classList.remove("active");
    modal_section_comments.classList.add("hide");
    document.querySelector("body").classList.remove("freeze_body");
});

//close or open modal write a comments

let container_for_write_comment = document.querySelector(
    ".container_for_write_comment"
);
let write_comments_btn = document.querySelector('.write_comments')

write_comments_btn.addEventListener('click', () => {
    container_for_write_comment.classList.add('active')
    container_for_write_comment.classList.remove('hide_comment')
})


//close or open modal write a comments reply

let container_for_write_comment_reply = document.querySelectorAll(
    ".container_for_write_comment_reply"
);
let write_comments_reply_btn = document.querySelectorAll('.write_comments_reply')

for (let i = 0; i < write_comments_reply_btn.length; i++) {
    write_comments_reply_btn[i].addEventListener('click', () => {
        container_for_write_comment_reply[i].classList.add('active')
        container_for_write_comment_reply[i].classList.remove('hide_reply')
    })
}


let choose_color_arrow = document.querySelector('.choose_color_arrow')


let modal_section_varient_image = document.getElementById(
    "modal_section_varient_image"
);
let btn_choose_color = document.getElementById("btn_choose_color");

let left_modal_section_varient_image = document.querySelector(
    ".left_modal_section_varient_image"
);


let close_icon_modal_varient_image = document.getElementById(
    "close_icon_modal_varient_image"
);

//show modal
if (btn_choose_color) {


    btn_choose_color.addEventListener("click", () => {

        modal_section_varient_image.classList.add("active");
        modal_section_varient_image.classList.remove("hide");
        document.querySelector("body").classList.add("freeze_body");
    });
}

if (choose_color_arrow) {

    choose_color_arrow.addEventListener("click", () => {
        modal_section_varient_image.classList.add("active");
        modal_section_varient_image.classList.remove("hide");
        document.querySelector("body").classList.add("freeze_body");
    });
}

//close modal
if (left_modal_section_varient_image) {
    left_modal_section_varient_image.addEventListener("click", () => {
        modal_section_varient_image.classList.add("hide");
        modal_section_varient_image.classList.remove("active");
        document.querySelector("body").classList.remove("freeze_body");
    });
}

if (close_icon_modal_varient_image) {

    close_icon_modal_varient_image.addEventListener("click", () => {
        modal_section_varient_image.classList.add("hide");
        modal_section_varient_image.classList.remove("active");
        document.querySelector("body").classList.remove("freeze_body");
    });
}

// <!-- -- -- -- -- -- -- -- -- -- scroll_bar_hover-- -- -- -- -- -- -- -- -- ---->

let all_cards = document.querySelectorAll(".card_scroll");
// let container_card = document.querySelector(".container_card_scroll");

for (let i = 0; i < all_cards.length; i++) {
    all_cards[i].addEventListener("mouseover", (e) => {
        if (e.target.classList.contains("img_up_for_hover")) {
            all_cards[i].children[0].children[0].classList.add(
                "hide_hover_scroll_bar"
            );
            all_cards[i].children[0].children[1].classList.remove(
                "hide_hover_scroll_bar"
            );
            all_cards[i].children[0].children[1].classList.add("show_scroll");
        }
    });

    all_cards[i].addEventListener("mouseout", (e) => {
        if (e.target.classList.contains("img_bottum_for_hover")) {
            all_cards[i].children[0].children[0].classList.add("show_scroll");
            all_cards[i].children[0].children[0].classList.remove(
                "hide_hover_scroll_bar"
            );

            all_cards[i].children[0].children[1].classList.add(
                "hide_hover_scroll_bar"
            );
            all_cards[i].children[0].children[1].classList.remove("show_scroll");
        }
    });
}

// <!-- -- -- -- -- -- -- -- -- -- End_scroll_bar_hover-- -- -- -- -- -- -- -- -- ---->


let logo_profile = document.getElementById('logo_profile')
let modal_section_profile = document.getElementById('modal_section_profile')
let left_modal_section_profile = document.querySelector('.left_modal_section_profile')
let logo_profile_span = document.getElementById('logo_profile_span')


///show modal profile
logo_profile_span.addEventListener('click', () => {
    modal_section_profile.classList.add("active");
    modal_section_profile.classList.remove("hide");
    document.querySelector("body").classList.add("freeze_body");
})

///show modal profile
logo_profile.addEventListener('click', () => {
    modal_section_profile.classList.add("active");
    modal_section_profile.classList.remove("hide");
    document.querySelector("body").classList.add("freeze_body");
})


///colse modal profile
left_modal_section_profile.addEventListener('click', () => {
    modal_section_profile.classList.add("hide");
    modal_section_profile.classList.remove("active");
    document.querySelector("body").classList.remove("freeze_body");
})


let to_top_page = document.querySelector('.to_top_page')

window.addEventListener('scroll', () => {
    if (window.pageYOffset > 500) {
        to_top_page.classList.add('show_btn_')
        to_top_page.classList.remove('hide_btn_')
    } else {
        to_top_page.classList.remove('show_btn_')
        to_top_page.classList.add('hide_btn_')
    }
})






