function setvotesfunc(that){
	var original_votes = that.parent().text();
	var finish_button = "<button class=\"btn btn-mini btn-link finishVotes\" type=\"button\"><i class=\"icon-ok\"></i></button>";
	that.parent().html(finish_button + "<input type=\"text\" class=\"span1\" id=\"updateVotes\" value=\"" + original_votes + "\">");
	$(".finishVotes").click(function(){
		var newVotes = {};
		newVotes['container'] = $("#updateVotes").closest("div").prev("h3").text();
		newVotes['link'] = $("#updateVotes").closest("tr").find("a").attr("href");
		newVotes['votes'] = $("#updateVotes").val();
		
		if (newVotes['votes'] > 10 || newVotes['votes'] < 0) {
			var tip_msg = $("<label>推荐指数0-10</label>");
			//alert($("#updateVotes").parent().html());
			tip_msg.insertAfter($("#updateVotes").parent().parent()).fadeIn('slow').animate({opacity: 1.0}, 1000).fadeOut('slow',function() { tip_msg.remove(); })
		}
		else {
			if (original_votes != newVotes['votes']) {
   	            $.ajax({
	            	url:"/ajaxUpdateVotes/",
	            	type: "POST",
	            	data: newVotes,
	            	dataType: "json",
	            	success: function() {}
	            });
			}
			$("#updateVotes").parent().html("<button class=\"btn btn-mini btn-link setvotes\" type=\"button\"><i class=\"icon-ok-sign\"></i></button> " + $("#updateVotes").val());
		}
	});
}


function settipsfunc(that) {
	var original_html = that.parent().text();
	var finish_button = "<button class=\"btn btn-mini btn-link finishtips\" type=\"button\"><i class=\"icon-ok\"></i></button>";
	var replace_html = "<input type=\"text\" id=\"updateTips\" size=50 value=\"" + original_html + "\">" + finish_button;
	that.parent().html(replace_html);
	$(".finishtips").click(function() {
		var newTips = {};
		newTips['container'] = $("#updateTips").closest("div").prev("h3").text();
		newTips['link'] = $("#updateTips").closest("td").prev("td").find("a").attr("href");
		newTips['tips'] = $("#updateTips").val();
		if (original_html != newTips['tips']) {
            $.ajax({
            	url:"/ajaxUpdateTips/",
            	type: "POST",
            	data: newTips,
            	dataType: "json",
            	success: function() {}
            });
		}
		$("#updateTips").parent().html("<button class=\"btn btn-mini btn-link settips\" type=\"button\"><i class=\"icon-ok-sign\"></i></button>" + $("#updateTips").val());
	});
}