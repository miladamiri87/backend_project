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


//option of menu for manage account


let detail_profile_personal_detail = document.getElementById('detail_profile_personal_detail')
let detail_profile_billimg = document.getElementById('detail_profile_billimg')
let detail_profile_password = document.getElementById('detail_profile_password')
let personal_information_manage = document.getElementById('personal_information_manage')
let billing_address_manage = document.getElementById('billing_address_manage')
let security_manage = document.getElementById('security_manage')

//active_border_manage

// detail_profile_personal_detail.addEventListener('click', () => {
//     personal_information_manage.classList.toggle('active')
//     billing_address_manage.classList.toggle('hide')
//     security_manage.classList.toggle('hide')
// })

detail_profile_billimg.addEventListener('click', () => {
    detail_profile_billimg.classList.add('active_border_manage')
    detail_profile_personal_detail.classList.remove('active_border_manage')
    detail_profile_password.classList.remove('active_border_manage')


    personal_information_manage.classList.add('hide_option');
    personal_information_manage.classList.remove('active_option');

    billing_address_manage.classList.add('active_option');
    billing_address_manage.classList.remove('hide_option');

    security_manage.classList.add('hide_option');
    security_manage.classList.remove('active_option');

})


detail_profile_personal_detail.addEventListener('click', () => {
    detail_profile_billimg.classList.remove('active_border_manage')
    detail_profile_personal_detail.classList.add('active_border_manage')
    detail_profile_password.classList.remove('active_border_manage')


    personal_information_manage.classList.remove('hide_option');
    personal_information_manage.classList.add('active_option');

    billing_address_manage.classList.remove('active_option');
    billing_address_manage.classList.add('hide_option');

    security_manage.classList.add('hide_option');
    security_manage.classList.remove('active_option');

})



detail_profile_password.addEventListener('click', () => {
    detail_profile_billimg.classList.remove('active_border_manage')
    detail_profile_personal_detail.classList.remove('active_border_manage')
    detail_profile_password.classList.add('active_border_manage')


    personal_information_manage.classList.add('hide_option');
    personal_information_manage.classList.remove('active_option');

    billing_address_manage.classList.remove('active_option');
    billing_address_manage.classList.add('hide_option');

    security_manage.classList.remove('hide_option');
    security_manage.classList.add('active_option');

})