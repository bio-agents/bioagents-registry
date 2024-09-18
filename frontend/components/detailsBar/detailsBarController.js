angular.module('iechor_front')
.directive('detailsBar', [function() {
	return {
		restrict: 'A',
		templateUrl: 'components/detailsBar/detailsBar.html',
		link: function(scope, element, attrs) {
			scope.showAgentbar = scope.toState.name == "search";
			scope.$watch(function(){
				return scope.toState.name
			}, function(newVal, oldVal){
    			scope.showAgentbar = (scope.toState.name == "search");
			}) 
		}
	}
}])
.controller('DetailsBarController', ['$rootScope', '$scope', '$state', '$stateParams', function($rootScope, $scope, $state, $stateParams) {
	var vm = this;
}]);