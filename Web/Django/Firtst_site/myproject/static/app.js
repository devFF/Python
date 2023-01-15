new Vue({
    el: '#orders_app',
    data: {
    orders: []
    },
    created: function () {
        const vm = this;
        axios.get('/api/orders/')
        .then(function (response){
        vm.orders = response.data
        })
    }
}

)