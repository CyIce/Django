$(document).ready(function () {
    $("#button").bind("click", function () {
        $.ajax({
            type: "get",
            url: "/cyice/getJson",
            dataType: "json",
            success: function (data, status) {
                d = data["data"];
                for (let i = 0; i < d.length; i++) {
                    console.log(i);
                    document.write("<p>" + d[i][0] + "</p>")
                }

            }
        });
    });

});