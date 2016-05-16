angular.module('app').controller('MainController', function(){
    var vm = this;
    vm.title = 'AngularJS Tutorial Example';
    vm.searchInput = '';
    vm.shows = [
        {
            title: 'Movie 1',
            year: 2010,
            favorite: true
        },
        {
            title: 'Movie 2',
            year: 2010,
            favorite: true
        },
        {
            title: 'Movie 3',
            year: 2011,
            favorite: false
        },
        {
            title: 'Movie 4',
            year: 2011,
            favorite: true
        },
        {
            title: 'Movie 5',
            year: 2012,
            favorite: false
        },
        {
            title: 'Movie 6',
            year: 2012,
            favorite: false
        },
        {
            title: 'Movie 7',
            year: 2013,
            favorite: true
        },
        {
            title: 'Movie 8',
            year: 2014,
            favorite: false
        },
        {
            title: 'Movie 9',
            year: 2015,
            favorite: true
        },
        {
            title: 'Movie 10',
            year: 2015,
            favorite: true
        },
    ];
    vm.orders = [
        {
            id: 1,
            title: 'Year Ascending',
            key: 'year',
            reverse: false
        },
        {
            id: 2,
            title: 'Year Descending',
            key: 'year',
            reverse: true  
        },
        {
            id: 3,
            title: 'Title Ascending',
            key: 'title',
            reverse: false
        },
        {
            id: 4,
            title: 'Year Descending',
            key: 'title',
            reverse: true  
        }
    ];
    vm.order = vm.orders[0];

    vm.new = {};
    vm.addShow = function(){
        vm.shows.push(vm.new);
        vm.new = {};
    };
});