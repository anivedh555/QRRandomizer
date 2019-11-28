$(function(){
    // don't cache ajax or content won't be fresh
    $.ajaxSetup ({
        cache: false
    });
    var ajax_load = "<img src='http://automobiles.honda.com/images/current-offers/small-loading.gif' alt='loading...' />";

    // load() functions
    var loadUrl = "http://fiddle.jshell.net/deborah/pkmvD/show/";
    $("#loadbasic").click(function(){
        $("#result").html(ajax_load).load(loadUrl);
    });

// end  
});