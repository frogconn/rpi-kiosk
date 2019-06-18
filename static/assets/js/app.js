const TPLHome = {
    template: `
<div class="ui grid stackable" style="margin-bottom: 20px;">
    <div class="eight wide column">
        <h2>Main page</h2>
        <div class="ui range" id="volume-range"></div>
    </div>
    <div class="eight wide column" style="display: flex; justify-content: center; align-items: center;">

    </div>

    <div>
        <button class="ui button" style="width: 100%" v-on:click="onPowerOn">Power on.</button>
    </div>
</div>`,
    methods: {
        onPowerOn: function () {
            axios.get('http://127.0.0.1:5000/api/v1/users')
            .then(function (response) {
                // handle success
                console.log(response);
            })
            .catch(function (error) {
                // handle error
                console.log(error);
            })
            .finally(function () {
                // always executed
            });


        }
    },
}

const router = new VueRouter({
    linkActiveClass: 'active',
    routes: [
        { path: '/', component: TPLHome, name: 'home' },
        { path: '*', redirect: '404' }
    ]
});

var vm = new Vue({
    router,
    el: '#app',
    data: {
        alarmIsNotRunning: true
    },

});
