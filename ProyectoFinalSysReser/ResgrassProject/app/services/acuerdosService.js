app


    .factory("acuerdosService", function($resource, apiUrl) {
    var url = apiUrl+"/config/";
    return {

        Categoria: $resource(url + "cancha/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },

        }),
        Agenda: $resource(url + "cancha/:id/", { 'id': '@id' }, {
            "update": { method: 'PUT' },
            "query": {
                method: 'GET',
                isArray: false,
                transformResponse: function(r) {
                    var results = [];
                    var options = {};
                    results = angular.fromJson(r).results ? angular.fromJson(r).results : angular.fromJson(r);
                    options = angular.fromJson(r).options ? angular.fromJson(r).options : {
                        "count": 1,
                        "pages": 1,
                        "page": 1,
                        "range": "all",
                        "previous": null,
                        "page_size": 1,
                        "next": null
                    };
                    return { results: results, options: options };
                }
            }

        }),

        CategoriaSector:$resource(url + "categoria_sector/:id/", { 'id' : '@id' }, {
            "update": { method: 'PUT'},
            "query": {
                method: 'GET',
                isArray: false,
                transformResponse:function(r) {
                    var results =[];
                    var options = {};
                       results = angular.fromJson(r).results ? angular.fromJson(r).results : angular.fromJson(r);
                        options = angular.fromJson(r).options ? angular.fromJson(r).options : {
                        "count": 1,
                        "pages": 1,
                        "page": 1,
                        "range": "all",
                        "previous": null,
                        "page_size": 1,
                        "next": null
                    };
                    return { results: results, options: options };
                    
                }

            }
        }),

/*
====================
service de instituciones
====================
*/
        Instituciones:$resource(url + "cancha/:id/", { 'id' : '@id' }, {
            "update": { method: 'PUT'},
            "query": {
                method: 'GET',
                isArray: false,
                transformResponse:function(r) {
                    var results =[];
                    var options = {};
                       results = angular.fromJson(r).results ? angular.fromJson(r).results : angular.fromJson(r);
                        options = angular.fromJson(r).options ? angular.fromJson(r).options : {
                        "count": 1,
                        "pages": 1,
                        "page": 1,
                        "range": "all",
                        "previous": null,
                        "page_size": 1,
                        "next": null
                    };
                    return { results: results, options: options };
                    
                }

            }
        })
    };
});
