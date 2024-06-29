let problems_cart = document.querySelectorAll(".problems_cart");
console.log(problems_cart);

let right_btn = document.getElementById("right_btn");
let left_btn = document.getElementById("left_btn");

let i = 0;
right_btn.addEventListener("click", () => {
    i++;
    remove_class_show();
    if (i >= problems_cart.length) {
        i = 0;
        problems_cart[i].classList.remove("hide");
        problems_cart[i].classList.add("show");
    }

    problems_cart[i].classList.remove("hide");
    problems_cart[i].classList.add("show");

});

left_btn.addEventListener("click", () => {
    i--;
    remove_class_show();
    if (i < 0) {
        i = 2;
        problems_cart[i].classList.remove("hide");
        problems_cart[i].classList.add("show");
    }

    problems_cart[i].classList.remove("hide");
    problems_cart[i].classList.add("show");

});


function remove_class_show() {
    for (let i = 0; i < problems_cart.length; i++) {
        problems_cart[i].classList.add("hide");
        problems_cart[i].classList.remove("show");
    }
}


//close or open modal write a comments reply

let close_icon_modal_measurements = document.getElementById(
    "close_icon_modal_measurements"
);


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


///show modal watch demo

let demo = document.getElementById('demo')
let container_modal_demo = document.querySelector('.container_modal_demo')
let close_btn_watch_demo = document.getElementById('close_btn_watch_demo')


demo.addEventListener('click', () => {
    container_modal_demo.classList.add("active");
    container_modal_demo.classList.remove("hide");
    document.querySelector("body").classList.add("freeze_body");
})


///colse modal profile
close_btn_watch_demo.addEventListener('click', () => {
    container_modal_demo.classList.add("hide");
    container_modal_demo.classList.remove("active");
    document.querySelector("body").classList.remove("freeze_body");
})


// <!-- -- -- -- -- -- -- -- -- -- modal_menu_share  -- -- -- -- -- -- -- -- -- ---->

let social_media_to_contact = document.getElementById("social_media_to_contact");
let container_menu_modal_sahare = document.querySelector(
    ".container_menu_modal_sahare"
);
let close_icon_modal_share = document.getElementById("close_icon_modal_share");
let bac_menu_right_modal_share = document.querySelector(
    ".bac_menu_right_modal_share"
);
let contact_us_share = document.querySelector('.contact_us_share')


social_media_to_contact.addEventListener("click", () => {
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


contact_us_share.addEventListener('click', () => {
    container_menu_modal_sahare.classList.remove("hide");
    container_menu_modal_sahare.classList.add("show_modal");
    document.querySelector("body").classList.add("freeze_body");
})


let to_top_page = document.querySelector('.to_top_page')

window.addEventListener('scroll', () => {
    if (window.pageYOffset >500) {
        to_top_page.classList.add('show_btn_')
        to_top_page.classList.remove('hide_btn_')
    }
    else {
         to_top_page.classList.remove('show_btn_')
        to_top_page.classList.add('hide_btn_')
    }
})




////////type animation

// <!-- -- -- -- -- -- -- -- -- -- type _ animation-- -- -- -- -- -- -- -- -- ---->

let text =
  "AI-Based Architectural Design Platform      ";

function type_animation() {
  for (let i = 0; i < text.length; i++) {
    let text_show = text.slice(0, i);
  }
}

let count_text = 0;
let iteration_text = 0;

(function type_animation() {
  if (count_text < text.length) {
    let text_show = text.slice(0, iteration_text++);
    document.getElementById("titre_sub_main_content").textContent = text_show;
    count_text++;
    setTimeout(type_animation, 100);
    if (count_text === text.length) {
      count_text = 0;
      iteration_text = 0;
    }
  }
})();
