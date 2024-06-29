function product_like(product_id, like_url, login_url) {
    $.ajax({
        url: like_url,
        type: 'get',
        data: {
            'product_id': product_id
        },
        success: function (data) {
            if (data['login_required']) {
                window.location.href = login_url
            } else {
                let like_btn = document.getElementById('like_count_product')
                if (data['liked']) {
                    like_btn.classList.remove('fa-regular')
                    like_btn.classList.add('fa-solid')
                } else {
                    like_btn.classList.remove('fa-solid')
                    like_btn.classList.add('fa-regular')
                }
                let like_count = document.getElementById('like_count')
                like_count.innerText = data['likers_count']

            }

        }
    })
}

function add_to_cart(product_id, add_cart_url, login_url) {

    $.ajax({
            url: add_cart_url,
            type: 'get',
            data: {
                'product_id': product_id,
                'number_order': () => {
                    return document.getElementById('number_order').value
                },

            },
            success: function (data) {
                if (data['login_required']) {
                    window.location.href = login_url
                } else {
                    if (data['add_product']) {
                        let counter_order = document.getElementById('counter_order')
                        let all_cart = data["all_cart"]

                        if (all_cart.length > 0) {
                            for (let p in all_cart) {
                                if ((p == data['product_id']) != "True") {
                                    counter_order.textContent = Number(data['p_all'])
                                    counter_order.classList.remove('hide')
                                    counter_order.classList.add('show_modal_copy')

                                } else {
                                    counter_order.textContent = Number(data['p_all']) + 1
                                    counter_order.classList.remove('hide')
                                    counter_order.classList.add('show_modal_copy')
                                }
                            }
                        } else {
                            counter_order.textContent = Number(data['p_all']) + 1
                            counter_order.classList.remove('hide')
                            counter_order.classList.add('show_modal_copy')
                        }


                        let message = document.getElementById('message')
                        message.innerText = "added product"
                        if (message.classList.contains("hide") || message.classList.contains("hide_modal_copy")) {
                            show_modal_copy();
                        }
                        setTimeout(() => {
                            hide_modal_copy();
                        }, 3000);

                        function show_modal_copy() {
                            message.classList.remove("hide_modal_copy");
                            message.classList.remove("hide");
                            message.classList.add("show_modal_copy");
                        }

                        function hide_modal_copy() {
                            message.classList.add("hide_modal_copy");
                            message.classList.remove("show_modal_copy");
                            message.classList.remove("hide");
                        }

                    } else {
                        let message = document.getElementById('message')
                        message.innerText = "More Than Stock"
                        if (message.classList.contains("hide") || message.classList.contains("hide_modal_copy")) {
                            show_modal_copy();
                        }
                        setTimeout(() => {
                            hide_modal_copy();
                        }, 3000);

                        function show_modal_copy() {
                            message.classList.remove("hide_modal_copy");
                            message.classList.remove("hide");
                            message.classList.add("show_modal_copy");
                        }

                        function hide_modal_copy() {
                            message.classList.add("hide_modal_copy");
                            message.classList.remove("show_modal_copy");
                            message.classList.remove("hide");
                        }
                    }
                }

            }
        }
    )
}


function add_varient_to_cart(selected_var_id, add_varient_cart_url, login_url) {

    $.ajax({
            url: add_varient_cart_url,
            type: 'get',
            data: {
                'selected_var_id': selected_var_id,
                'number_order': () => {
                    return document.getElementById('number_order').value
                },
            },
            success: function (data) {
                if (data['login_required']) {
                    window.location.href = login_url
                } else {
                    if (data['add_product']) {
                        let counter_order = document.getElementById('counter_order')
                        let all_cart = data["all_cart"]

                        if (all_cart.length > 0) {


                            for (let p in all_cart) {
                                if ((p == data['selected_var_id']) != "True") {
                                    counter_order.textContent = Number(data['p_all'])
                                    counter_order.classList.remove('hide')
                                    counter_order.classList.add('show_modal_copy')
                                } else {
                                    counter_order.textContent = Number(data['p_all']) + 1
                                    counter_order.classList.remove('hide')
                                    counter_order.classList.add('show_modal_copy')
                                }
                            }
                        } else {
                            counter_order.textContent = Number(data['p_all']) + 1
                            counter_order.classList.remove('hide')
                            counter_order.classList.add('show_modal_copy')
                        }


                        let message = document.getElementById('message')
                        message.innerText = "added product"
                        if (message.classList.contains("hide") || message.classList.contains("hide_modal_copy")) {
                            show_modal_copy();
                        }
                        setTimeout(() => {
                            hide_modal_copy();
                        }, 3000);

                        function show_modal_copy() {
                            message.classList.remove("hide_modal_copy");
                            message.classList.remove("hide");
                            message.classList.add("show_modal_copy");
                        }

                        function hide_modal_copy() {
                            message.classList.add("hide_modal_copy");
                            message.classList.remove("show_modal_copy");
                            message.classList.remove("hide");
                        }

                    } else {
                        let message = document.getElementById('message')
                        message.innerText = "More Than Stock"
                        if (message.classList.contains("hide") || message.classList.contains("hide_modal_copy")) {
                            show_modal_copy();
                        }
                        setTimeout(() => {
                            hide_modal_copy();
                        }, 3000);

                        function show_modal_copy() {
                            message.classList.remove("hide_modal_copy");
                            message.classList.remove("hide");
                            message.classList.add("show_modal_copy");
                        }

                        function hide_modal_copy() {
                            message.classList.add("hide_modal_copy");
                            message.classList.remove("show_modal_copy");
                            message.classList.remove("hide");
                        }
                    }
                }
            }

        }
    )
}