function hideComments () {
    $("#comments").hide(1000, function (){
        $("#hide").hide();
        $("#show").show();
    });
}
function showComments () {
    $("#comments").show(1000, function (){
        $("#hide").show();
        $("#show").hide();
    })

}
$(document).ready (function () {
    $("#hide").bind ("click", hideComments);
    $("#show").bind ("click", showComments);
});
