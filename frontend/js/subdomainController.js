// Controllers
angular.module('iechor_front.controllers')
.controller('SubdomainAdminController', ['$scope',  '$stateParams', 'DomainConnection', 'DomainDetailConnection', function($scope, $stateParams, DomainConnection, DomainDetailConnection) {
	var vm = this;
	$scope.isLoadingSubdomains = true;
	$scope.subdomains = [];

	$scope.deleteSubdomainAtIndex = function(index){
		if (confirm("Are you sure you want to remove this subdomain?")){
			// COVID-19 subdomain hack
			if ($scope.subdomains[index].name.toLowerCase() == 'covid-19'){
				alert('Cannot delete the covid-19 subdomain');
				return;
			}
			var deleteSubdomain = $scope.subdomains[index];
			$scope.subdomains.splice(index, 1);
			var deleteResponse = DomainDetailConnection.delete({'domain': deleteSubdomain.name}, function(data) {
				// TODO: Handle repsonses
			}, function(error) {
				// TODO: Handle errors
			});
		}
	}

	vm.loadSubdomains = function() {
		$scope.isLoadingSubdomains = true;
		$scope.subdomains = [];
		var domainResponse = DomainConnection.query({}, function(data) {
			$scope.subdomains = data;
			$scope.isLoadingSubdomains = false;
		}, function(errorData) {
			// TODO: Handle errors
		});
	};

	// Initialization
	vm.loadSubdomains()
}])
.controller('DomainListController', ['$scope', 'DomainDetailConnection', '$state', function($scope, DomainDetailConnection, $state){
	var vm = this;
	$scope.domains = [];
	$scope.domainSearchText = "";
	
	$scope.search_title = true;
	$scope.search_subtitle = true;
	$scope.search_collection = true;
	$scope.search_tags = true;
	$scope.search_description = false;
	$scope.search_agents = false;

	$scope.updateKeys = function(){
		$scope.initialKeys = [
			{
				"name":"domain",
				"weight": 1
			},
			{
				"name":"title",
				"weight": $scope.search_title ? 0.9 : 0
			},
			{
				"name":"sub_title",
				"weight": $scope.search_subtitle ? 0.7 : 0
			},
			{
				"name":"tag",
				"weight": $scope.search_tags ? 0.9 : 0
			},
			{
				"name":"collection",
				"weight": $scope.search_collection ? 0.9 : 0
			}, 
			{
				"name":"description",
				"weight": $scope.search_description ? 0.3 : 0
			},
			{
				"name":"resources.name",
				"weight": $scope.search_agents ? 0.2 : 0
			},
			{
				"name":"resources.bioagentsID",
				"weight": $scope.search_agents ? 0.2 : 0
			}
		];
		
		$scope.fuseSearchKeys = $scope.initialKeys.filter(function(x){
			return x.weight > 0;
		});

		$scope.fuseOptions = {
			threshold: 0.2,
			shouldSort: true,
			minMatchCharLength: 2,
			// location: 0, default 0
			tokenize: true,
			// matchAllTokens: true,
			keys: $scope.fuseSearchKeys 
	
		};
	}

	$scope.updateKeys();

	DomainDetailConnection.query({'domain':'all'}, function(response) {
		$scope.domains = response.data;
		$scope.domains.sort(function(a,b){
			var d_a = a.domain.toLowerCase();
			var d_b = b.domain.toLowerCase();

			if (d_a < d_b) {
				return -1;
			  }
			  if (d_a > d_b) {
				return 1;
			  }
			  return 0; 
		})
		$scope.filteredDomains = $scope.domains;
		$scope.fuse = new Fuse($scope.domains, $scope.fuseOptions);
	});

	$scope.collectionNameClicked = function(collectionName) {
		$state.go('search', {'collectionID': '"'+ collectionName + '"'});
	}

	$scope.domainSearch = function(){
		if ($scope.domainSearchText.length == 0){
			$scope.filteredDomains = $scope.domains;
		}
		else {
			$scope.updateKeys();
			$scope.fuse = new Fuse($scope.domains, $scope.fuseOptions);
			console.log($scope.fuseOptions);
			$scope.filteredDomains = $scope.fuse.search($scope.domainSearchText);
		}
	}


}])
.controller('SubdomainController', ['$scope', '$state',  '$stateParams', 'AgentListOverviewConnection', 'DomainDetailConnection', 'DomainConnection', '$q', 'UsedTerms', function($scope, $state, $stateParams, AgentListOverviewConnection, DomainDetailConnection, DomainConnection, $q, UsedTerms) {
	var vm = this;
	$scope.AgentListOverviewConnection = AgentListOverviewConnection;
	$scope.updating = false;
	$scope.loading = ($stateParams.id != "");
	$scope.agentsPerPageCount = 10; 

	$scope.search = {};
	$scope.search.searchOption = 'name';
	$scope.search.loadingSearchResults = false;
	$scope.search.searchResults = [];
	$scope.search.searchString = '';
	$scope.search.noResults = false;
	$scope.search.currentPage = 1;
	$scope.search.totalPages = 1;

	$scope.subdomain = {};	
	$scope.subdomain.exists = ($stateParams.id != "");
	$scope.subdomain.domain = $stateParams.id;
	$scope.subdomain.title = '';
	$scope.subdomain.subtitle = '';
	$scope.subdomain.description = '';
	$scope.subdomain.agentList = [];
	$scope.subdomain.resources = [];
	$scope.subdomain.tag = [];
	$scope.subdomain.collection = [];
	$scope.subdomain.is_private = true;
	$scope.subdomain.currentPage = 1;
	$scope.subdomain.totalPages = 1;

	$scope.errors = {};
	$scope.errors.general = '';
	$scope.errors.domain = '';
	$scope.errors.loading = '';
	$scope.errors.data = {}


	$scope.response = {};
	$scope.response.general = '';


	$scope.gotoDomain = function(d){
		if (confirm('Make sure to save before leaving the page. Leave?')){
			$state.go('subdomain', {domain: d});
		}
		
	}

	// Handle agent search
	$scope.clearButtonPressed = function() {
		$scope.search.currentPage = 1;
		var searchQuery = {}
		searchQuery[$scope.search.searchOption] = $scope.search.searchString;
		$scope.search.searchResults = [];
	};

	$scope.searchButtonPressed = function() {
		$scope.search.currentPage = 1;
		var searchQuery = {}
		searchQuery[$scope.search.searchOption] = $scope.search.searchString;
		vm.performSearch(searchQuery);
	};

	$scope.agentInSubdomain = function(agentID, versionID) {
		for (var index in $scope.subdomain.resources) {
			var currentAgent = $scope.subdomain.resources[index];
			
			if (currentAgent['bioagentsID'] == agentID){// && currentAgent['versionId'] == versionID) {
				return true;
			}
		}
		return false;
	}

	$scope.addToSubdomain = function(index) {
		var selectedAgent = $scope.search.searchResults[index];
		
		var selectedDict = { "bioagentsID": selectedAgent.bioagentsID, "versionId": selectedAgent.versionId };
		$scope.subdomain.agentList.push(selectedAgent);
		$scope.subdomain.resources.push(selectedDict);
		$scope.subdomain.totalPages = ($scope.subdomain.agentList.length / $scope.agentsPerPageCount) * 10;
	}

	$scope.domainAddButtonClick = function (_what, _where, _isList, _isObject) {
		if (_isList) {
			// if array does not exist create it
			if (typeof _where[_what] == 'undefined') {
				_where[_what] = [];
			}
			// add either an object or string to array
			_where[_what].push(_isObject ? {} : '');
		} else {
			// if object does not exist create it
			if (typeof _where[_what] == 'undefined') {
				_where[_what] = _isObject ? {} : '';
			}
		}
	}

	$scope.removeButtonClick = function (_what, _parent, _index, _event){
		$scope.removeButtonClickAux(_what, _parent, _index, _event);

		if ($scope.errors.data[_what] && $scope.errors.data[_what][_index]){
			$scope.removeButtonClickAux(_what, $scope.errors.data, _index, _event);
		}
		
	}

	// remove attribute or list entry
	$scope.removeButtonClickAux = function (_what, _parent, _index, _event) {
		if (_parent[_what][_index] ? confirm("Are you sure you want to remove this element?") : 1) {
			// remove jstree if exists
			if (_event) {
				$(_event.target).closest('div').find('.jstree').jstree("destroy").remove();
			}
			_parent[_what].splice(_index, 1);
			// if last instance in array delete entire attribute from the software object
			if (_parent[_what].length == 0) {
				delete _parent[_what];
			}
		}
	}

	// used terms (collectionID) for searching in collections
	function getCollectionIDs(){
		var d = $q.defer();
		var params = {
			"usedTermName": "collectionID"
		};
		UsedTerms.get(params, function(response) {
			d.resolve(response.data);
		});
		return d.promise;
	}
	
	$scope.loadCollectionIDs = function(query) {
		return getCollectionIDs().then(function(list) {
			return list.filter(function (str) { return str.toLowerCase().includes(query.toLowerCase()); }).slice(0,10).sort();
		});
	}

	$scope.addAllToSubdomain = function() {
		for (var agent in $scope.search.searchResults) {
			var selectedAgent = $scope.search.searchResults[agent];
			if (selectedAgent.bioagentsID && $scope.agentInSubdomain(selectedAgent.bioagentsID, selectedAgent.versionId) == false) {	
				$scope.subdomain.agentList.push(selectedAgent);
				$scope.subdomain.resources.push({ "bioagentsID": selectedAgent.bioagentsID, "versionId": selectedAgent.versionId });
			}
		}
		$scope.subdomain.totalPages = ($scope.subdomain.agentList.length / $scope.agentsPerPageCount) * 10;
	}

	$scope.removeFromSubdomain = function(index) {
		$scope.subdomain.agentList.splice(index, 1); 
		$scope.subdomain.resources.splice(index, 1);
		$scope.subdomain.totalPages = ($scope.subdomain.agentList.length / $scope.agentsPerPageCount) * 10;
	}

	$scope.saveSubdomain = function() {
		$scope.updating = true;
		$scope.errors.general = '';
		$scope.response.general = '';
		var createResponse = DomainConnection.create(vm.subdomainQuery(), function(data) {
			$scope.subdomain.exists = true;
			$scope.response.general = "Domain '" + $scope.subdomain.domain + "' was created.";
			$scope.updating = false;
		}, function(error) {
			$scope.errors.general = error.data.detail;
			console.log(error);
			$scope.updating = false;
			$scope.errors.data = error.data;
		});
	}

	vm.fetchSubdomain = function() {
		$scope.errors.general = '';
		$scope.response.general = '';
		var updateResponse = DomainDetailConnection.query({'domain': $scope.subdomain.domain}, function(data) {
			$scope.subdomain.title = data.data['title'];
			$scope.subdomain.subtitle = data.data['sub_title'];
			$scope.subdomain.description = data.data['description'];
			for (var index in data.data.resources) {
				var agent = data.data.resources[index];
				agent['bioagentsID'] = agent['bioagentsID'];
				$scope.subdomain.agentList.push(agent);
				$scope.subdomain.resources.push(agent);
			}

			for (var i in data.data.tag){
				$scope.subdomain.tag.push(data.data.tag[i]);
			}
		
			for (var i in data.data.collection){
				$scope.subdomain.collection.push(data.data.collection[i]);
			}

			$scope.subdomain.is_private = data.data.is_private;

			$scope.loading = false;
			$scope.updating = false;
			$scope.subdomain.totalPages = ($scope.subdomain.agentList.length / $scope.agentsPerPageCount) * 10;
		}, function(error) {
			// Handle error
			$scope.errors.loading = 'Data failed to load. Please try to refresh this website. ' + error.data.details;
		});
	}

	$scope.updateSubdomain = function() {
		$scope.updating = true;
		$scope.errors.general = '';
		$scope.response.general = '';
		var updateResponse = DomainDetailConnection.update(vm.subdomainQuery(), function(data) {
			$scope.response.general = "Domain '" + $scope.subdomain.domain + "' was updated with " + $scope.subdomain.resources.length + " entries." ;
			$scope.updating = false;
		}, function(error) {
			$scope.errors.general = error.data.detail;
			$scope.updating = false;
			$scope.errors.data = error.data;
		});
	}

	// remove or replace characters not allowed for subdomains
	// See https://agents.ietf.org/html/rfc952 for guidelines
	$scope.makeSubdomainURLSafe = function(value) {
		$scope.errors.domain = "";
		if (typeof value != 'undefined') {
			var id = value.replace(/[^a-zA-Z0-9_-]*/g,'').replace(/[ ]+/g, '-').replace(/[_]+/g, '-').toLowerCase();
		}
		if (value != id) {
			$scope.errors.domain = "Entered value '" + value + "' has been modified. Only alphanumeric characters and dashes can be used for the subdomain name.";
		}
		$scope.subdomain.domain = id;
	}


	vm.performSearch = function(query) {
		$scope.search.loadingSearchResults = true;
		$scope.search.noResults = false;
		var response = AgentListOverviewConnection.query(query, function() {
			$scope.search.currentPage = 1;
			$scope.search.searchResults = response;
			$scope.search.loadingSearchResults = false;
			$scope.search.totalPages = ($scope.search.searchResults.length / $scope.agentsPerPageCount) * 10;
			if (response.length == 0) {
				$scope.search.noResults = true;
			}
		});
	};

	vm.subdomainQuery = function() {
		return {'domain': $scope.subdomain.domain,
		'title': $scope.subdomain.title,
		'sub_title': $scope.subdomain.subtitle,
		'description': $scope.subdomain.description,
		'resources': $scope.subdomain.resources,
		'tag': $scope.subdomain.tag,
		'collection': $scope.subdomain.collection,
		'is_private': $scope.subdomain.is_private
	};
}

	// Initialization
	if ($scope.loading) {
		vm.fetchSubdomain()
	}
}]);

