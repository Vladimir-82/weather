function hideCities () {
    $("#cities").hide(1000, function (){
        $("#hide").hide();
        $("#show").show();
    });
}
function showCities () {
    $("#cities").show(1000, function (){
        $("#hide").show();
        $("#show").hide();
    })

}
$(document).ready (function () {
    $("#hide").bind ("click", hideCities);
    $("#show").bind ("click", showCities);
});
