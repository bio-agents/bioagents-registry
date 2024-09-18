	angular.module('iechor_front')
.directive('searchBar', ['Query', 'AgentList', 'Highlighting', 'Attribute', '$state', '$stateParams', '$timeout', 'UsedTerms', '$q', 'filterFilter', 'Domain', '$rootScope', function(Query, AgentList, Highlighting, Attribute, $state, $stateParams, $timeout, UsedTerms, $q, filterFilter, Domain, $rootScope) {
	return {
		restrict: 'A',
		templateUrl: 'components/searchBar/searchBar.html',
		link: function(scope, element, attrs) {

			// reference the Query in the scope
			scope.Query = Query;
			// reference the Attribute in the scope
			scope.Attribute = Attribute;
			scope.AgentList = AgentList;

			var initializing = true

			function updateQuery() {
				Query.current = [];
				for (var prop in $stateParams) {
				// iterate through all parameters, skip 'page'
				if ($stateParams.hasOwnProperty(prop)
					&& !_.includes(['page', 'sort', 'ord', 'domain'], prop)
					&& typeof $stateParams[prop] != 'undefined') {
					// Remove agent id from the query
					if (prop == 'q') {
						var list = $stateParams[prop].split('+');
						for (var i in list) {
							if (_.isEmpty(list[i]) == false) {
								Query.current.push({text:list[i], filter:'everything'});
							}
						}
					} else {
						Query.current.push({text:$stateParams[prop], filter:prop});
					}
				}
				}
				// initial highlighting
				Highlighting.set(Query.current);
			}


			$rootScope.$on('$stateChangeSuccess', function(event, toState, toStateParams, fromState, fromStateParams) {
				if (toState.name !== 'search') { 
					Query.current = [];
					AgentList.refresh();
				}
				else if (toState.name === 'search') {
					updateQuery();
				}
			});

			updateQuery();

			// helper function for getting used terms
			function getUsedTerms(term, params) {
				var d = $q.defer();
				var list = []
				params["usedTermName"] = term;
				UsedTerms.get(params, function(response) {
					d.resolve(response.data);
				});
				return d.promise;
			}

			// necessary for filtering suggestions for the autocomplete
			scope.loadSuggestions = function(term, query) {
				var deferred = $q.defer();
				scope.usedTerms[term].then(function(list) {
					deferred.resolve(filterFilter(list,query));
				})
				return deferred.promise;
			}

			function getSuggestions() {
				// get used terms for typeahead
				scope.usedTerms = {};

				// add query and filtering parameters to refine suggestions
				var params = _.clone($stateParams);
				params['page'] = null;
				params['sort'] = null;
				params['ord'] = null;

				// create promises for all suggestions
				scope.usedTerms['everything'] = getUsedTerms('all', params);
				scope.usedTerms['topic'] = getUsedTerms('topic', params);
				scope.usedTerms['operation'] = getUsedTerms('operation', params);
				scope.usedTerms['input'] = getUsedTerms('input', params);
				scope.usedTerms['output'] = getUsedTerms('output', params);
				scope.usedTerms['agentType'] = getUsedTerms('agentType', params);
				scope.usedTerms['language'] = getUsedTerms('language', params);
				scope.usedTerms['accessibility'] = getUsedTerms('accessibility', params);
				scope.usedTerms['cost'] = getUsedTerms('cost', params);
				scope.usedTerms['license'] = getUsedTerms('license', params);
				scope.usedTerms['credit'] = getUsedTerms('credit', params);
				scope.usedTerms['collectionID'] = getUsedTerms('collectionID', params);
				scope.usedTerms['name'] = getUsedTerms('name', params);  
			}

			// custom object necessary for ngTagsInput
			scope.filter = {};
			// initially selected filter
			scope.filter.selected = 'everything';
			// list of filters to display
			scope.filter.list = [
			"everything",
			"topic",
			"operation",
			"input",
			"output",
			"agentType",
			"language",
			"accessibility",
			"cost",
			"license",
			"credit",
			"collectionID",
			"name"	
			];

			// get initial suggestions
			getSuggestions();

			// when tag is added save the filter and reset it to 'everything'
			scope.tagAdded = function(tag) {
				tag['text'] = scope.normalizeTag(tag);
				tag['filter'] = scope.filter.selected;
				scope.filter.selected = 'everything';
			}

			// remove any unwanted characters from the entered tag
			scope.normalizeTag = function(tag) {
				return tag['text'].replace(/\+/g, "")
			}

			// saving the query and filtering to url
			scope.tagsChanged = function() {
				$rootScope.$emit('search-bar-tags-changed', {});
				$timeout(function() {
					var params =  {};
					params['page'] = 1;
					params['sort'] = $stateParams['sort'];
					if (params['sort'] == undefined) {
						params['sort'] = 'score';
					};
					if (scope.Query.current.length == 0) {
						params['sort'] = undefined;
						params['page'] = undefined;
					};
					params['ord'] = $stateParams['ord'];
					params['domain'] = $stateParams['domain'];
							// add each tag from the search bar to the url
							for (var i in scope.Query.current) {
								// if tag is 'everything' put it under q
								if (scope.Query.current[i].filter == 'everything') {
									// if there already is a 'everything' tag, add new ones separating them with a dash
									if (params['q'] && params['q'].length > 0) {
										params['q'] += "+" + scope.Query.current[i].text;
									} else {
										params['q'] = scope.Query.current[i].text
									}
								} else {
									params[scope.Query.current[i].filter] = scope.Query.current[i].text;
								}
							}
							// update url
							$state.transitionTo('search', params, { notify: true });
							// add query elements to list of terms to highlight
							Highlighting.set(Query.current);
							$timeout(function() {
								// get more refined suggestions
								getSuggestions();
								// refresh agent list
								AgentList.refresh();
							})
						})
			}
		}
	}
}]);