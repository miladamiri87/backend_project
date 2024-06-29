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

/* //////dot_price///// */

let dot_price_container = document.querySelector(".dot_price_container");
let modal_detail_price = document.getElementById("modal_detail_price");

dot_price_container.addEventListener("mouseenter", () => {
    modal_detail_price.classList.add("show");
    modal_detail_price.classList.remove("hide");
});
dot_price_container.addEventListener("mouseleave", () => {
    modal_detail_price.classList.remove("show");
    modal_detail_price.classList.add("hide");
});

/* //////dot_price2///// */

let dot_price_container2 = document.querySelector(".dot_price_container2");
let modal_detail_price2 = document.getElementById("modal_detail_price2");

dot_price_container2.addEventListener("mouseenter", () => {
    modal_detail_price2.classList.add("show");
    modal_detail_price2.classList.remove("hide");
});
dot_price_container2.addEventListener("mouseleave", () => {
    modal_detail_price2.classList.remove("show");
    modal_detail_price2.classList.add("hide");
});

/* //////dot_price3///// */


let dot_price_container3 = document.querySelector(".dot_price_container3");
let modal_detail_price3 = document.getElementById("modal_detail_price3");

dot_price_container3.addEventListener("mouseenter", () => {
    modal_detail_price3.classList.add("show");
    modal_detail_price3.classList.remove("hide");
});
dot_price_container3.addEventListener("mouseleave", () => {
    modal_detail_price3.classList.remove("show");
    modal_detail_price3.classList.add("hide");
});


/* //////dot_price44///// */


let dot_price_container44 = document.querySelector(".dot_price_container44");
let modal_detail_price44 = document.getElementById("modal_detail_price44");

dot_price_container44.addEventListener("mouseenter", () => {
    modal_detail_price44.classList.add("show");
    modal_detail_price44.classList.remove("hide");
});
dot_price_container44.addEventListener("mouseleave", () => {
    modal_detail_price44.classList.remove("show");
    modal_detail_price44.classList.add("hide");
});


/* //////dot_price_left_half_up///// */

let dot_price_container_left_half_up = document.querySelector(
    ".dot_price_container_left_half_up"
);
let modal_detail_price_left_half_up = document.getElementById(
    "modal_detail_price_left_half_up"
);

dot_price_container_left_half_up.addEventListener("mouseenter", () => {
    modal_detail_price_left_half_up.classList.add("show");
    modal_detail_price_left_half_up.classList.remove("hide");
});
dot_price_container_left_half_up.addEventListener("mouseleave", () => {
    modal_detail_price_left_half_up.classList.remove("show");
    modal_detail_price_left_half_up.classList.add("hide");
});

/* //////dot_price_left_half_buttom///// */

let dot_price_container_left_half_buttom = document.querySelector(
    ".dot_price_container_left_half_buttom"
);
let modal_detail_price_left_half_buttom = document.getElementById(
    "modal_detail_price_left_half_buttom"
);

dot_price_container_left_half_buttom.addEventListener("mouseenter", () => {
    modal_detail_price_left_half_buttom.classList.add("show");
    modal_detail_price_left_half_buttom.classList.remove("hide");
});
dot_price_container_left_half_buttom.addEventListener("mouseleave", () => {
    modal_detail_price_left_half_buttom.classList.remove("show");
    modal_detail_price_left_half_buttom.classList.add("hide");
});

/* //////dot_price_img_half_right///// */

let dot_price_container_img_half_right = document.querySelector(
    ".dot_price_container_img_half_right"
);
let modal_detail_price_img_half_right = document.getElementById(
    "modal_detail_price_img_half_right"
);


/* //////dot_price_img_designed_storing///// */

let dot_price_container_img_designed_storing = document.querySelector(
    ".dot_price_container_img_designed_storing"
);
let modal_detail_price_img_designed_storing = document.getElementById(
    "modal_detail_price_img_designed_storing"
);

dot_price_container_img_designed_storing.addEventListener("mouseenter", () => {
    modal_detail_price_img_designed_storing.classList.add("show");
    modal_detail_price_img_designed_storing.classList.remove("hide");
});
dot_price_container_img_designed_storing.addEventListener("mouseleave", () => {
    modal_detail_price_img_designed_storing.classList.remove("show");
    modal_detail_price_img_designed_storing.classList.add("hide");
});

/* //////dot_price_img_designed_storing2///// */

let dot_price_container_img_designed_storing2 = document.querySelector(
    ".dot_price_container_img_designed_storing2"
);
let modal_detail_price_img_designed_storing2 = document.getElementById(
    "modal_detail_price_img_designed_storing2"
);

dot_price_container_img_designed_storing2.addEventListener("mouseenter", () => {
    modal_detail_price_img_designed_storing2.classList.add("show");
    modal_detail_price_img_designed_storing2.classList.remove("hide");
});
dot_price_container_img_designed_storing2.addEventListener("mouseleave", () => {
    modal_detail_price_img_designed_storing2.classList.remove("show");
    modal_detail_price_img_designed_storing2.classList.add("hide");
});


/* //////dot_price_img_designed_storin4///// */

let dot_price_container_img_designed_storing4 = document.querySelector(
    ".dot_price_container_img_designed_storing4"
);
let modal_detail_price_img_designed_storing4 = document.getElementById(
    "modal_detail_price_img_designed_storing4"
);

dot_price_container_img_designed_storing4.addEventListener("mouseenter", () => {
    modal_detail_price_img_designed_storing4.classList.add("show");
    modal_detail_price_img_designed_storing4.classList.remove("hide");
});
dot_price_container_img_designed_storing4.addEventListener("mouseleave", () => {
    modal_detail_price_img_designed_storing4.classList.remove("show");
    modal_detail_price_img_designed_storing4.classList.add("hide");
});

// <!-- -- -- -- -- -- -- -- -- -- modal_menu_share  -- -- -- -- -- -- -- -- -- ---->

let btn_share_modal = document.querySelector(".btn_share_modal");
let container_menu_modal_sahare = document.querySelector(
    ".container_menu_modal_sahare"
);
let close_icon_modal_share = document.getElementById("close_icon_modal_share");
let bac_menu_right_modal_share = document.querySelector(
    ".bac_menu_right_modal_share"
);
let coppy_link_modal_share = document.querySelector(".coppy_link_modal_share");
let btn_share_modal_coppyeid = document.querySelector(
    ".btn_share_modal_coppyeid"
);
let close_icon_btn_share_modal_coppyeid = document.getElementById(
    "close_icon_btn_share_modal_coppyeid"
);

btn_share_modal.addEventListener("click", () => {
    container_menu_modal_sahare.classList.remove("hide");
    container_menu_modal_sahare.classList.add("show_modal");
    document.querySelector("body").classList.add("freeze_body");

});

close_icon_modal_share.addEventListener("click", () => {
    container_menu_modal_sahare.classList.add("hide");
    container_menu_modal_sahare.classList.remove("show_modal");
    document.querySelector("body").classList.remove("freeze_body");

});

bac_menu_right_modal_share.addEventListener("click", () => {
    container_menu_modal_sahare.classList.add("hide");
    container_menu_modal_sahare.classList.remove("show_modal");
    document.querySelector("body").classList.remove("freeze_body");

});

coppy_link_modal_share.addEventListener("click", () => {
    container_menu_modal_sahare.classList.add("hide");
    container_menu_modal_sahare.classList.remove("show_modal");
    btn_share_modal_coppyeid.classList.remove("hide");
    btn_share_modal_coppyeid.classList.add("show_modal");
});

close_icon_btn_share_modal_coppyeid.addEventListener("click", () => {
    btn_share_modal_coppyeid.classList.remove("show_modal");
    btn_share_modal_coppyeid.classList.add("hide");
});

// <!-- -- -- -- -- -- -- -- -- -- scroll_bar-- -- -- -- -- -- -- -- -- ---->

// <!-- -- -- -- -- -- -- -- -- -- scroll_bar_hover-- -- -- -- -- -- -- -- -- ---->

let all_cards = document.querySelectorAll(".card_scroll");
let container_card = document.querySelector(".container_card_scroll");

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

// <!-- -- -- -- -- -- -- -- -- -- scroll_bar_btn_left_or_right-- -- -- -- -- -- -- -- -- ---->

let arrow_scroll_right = document.getElementById("arrow_scroll_right");
let arrow_scroll_left = document.getElementById("arrow_scroll_left");

arrow_scroll_right.addEventListener("click", () => {
    container_card.scrollLeft += 780;
});

arrow_scroll_left.addEventListener("click", () => {
    container_card.scrollLeft -= 780;
});

// <!-- -- -- -- -- -- -- -- -- -- End_scroll_bar_btn_left_or_right-- -- -- -- -- -- -- -- -- ---->

console.log(container_card.scrollWidth); //kole arze scroll mishe darsorati ke hame ra kenare ham bechine
console.log(container_card.clientWidth); //chizi ke karbar dare mibine
let max_remind_scroll = container_card.scrollWidth - container_card.clientWidth; //chizi ke karbar nemibine

function play_scroll() {
    if (container_card.scrollLeft > max_remind_scroll - 1) {
        container_card.scrollLeft -= max_remind_scroll;
    }
    container_card.scrollLeft += 1;
}

let play = setInterval(play_scroll, 40);

for (let i = 0; i < all_cards.length; i++) {
    all_cards[i].addEventListener("mouseover", () => {
        clearInterval(play);
    });
    all_cards[i].addEventListener("mouseleave", () => {
        return (play = setInterval(play_scroll, 50));
    });
}


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


////////animation Btn_circle
let btn_animation_ = document.querySelectorAll(".btn_animation_");

// btn_animation_.forEach((btn_iter) => {
//     btn_iter.addEventListener("click", function (e) {
//         console.log('salam')
//         let x = e.clientX - e.target.offsetLeft;
//         let y = e.clientY - e.target.offsetTop;
//         let span_animation = document.createElement("span");
//         span_animation.classList.add("span_animation");
//         span_animation.style.left = x + "px";
//         span_animation.style.top = y + "px";
//         this.appendChild(span_animation);
//
//         setTimeout(() => {
//             span_animation.remove();
//         }, 1000);
//     });
// });

// console.log(btn_animation_);

btn_animation_.forEach(bt_iter => {
    bt_iter.addEventListener('click', function (e) {
        console.log('salam')

        let x = e.clientX - e.target.offsetLeft;
        let y = e.clientY - e.target.offsetTop;
        let span_animation = document.createElement("span");
        span_animation.classList.add("span_animation");
        span_animation.style.left = x + "px";
        span_animation.style.top = y + "px";
        this.appendChild(span_animation);

        setTimeout(() => {
            span_animation.remove();
        }, 1000);
    })
})
