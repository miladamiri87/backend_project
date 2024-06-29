//modal menu

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

// <!-- -- -- -- -- -- -- -- -- -- modal_menu_share  -- -- -- -- -- -- -- -- -- ---->

let modal_option = document.querySelector("#modal_option");
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

