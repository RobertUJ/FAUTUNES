$(document).ready(function(){

			$("#txtBuscar").on("keypress",function(e){
				if(e.keyCode == 13){
					e.preventDefault()
					var codigo = $(this).val();
					var final_codigo = "";
					if(codigo != ""){
						final_codigo = codigo.split(' ').join('+');
						//alert(final_codigo);
						buscame(final_codigo);
					}else{
						// Mensaje que llene la caja de busqueda
						return false;
					}

					
				}
			});
			function buscame(codigo){
				// http://tinysong.com/s/Beethoven?format=json&limit=3&key=APIKey
				var miUrl = "/petition/";
				var token = $("#idToken").val();
			    $("#cuerpo").load(miUrl, { 'cod':codigo,'csrfmiddlewaretoken':token} );
			}


			$(".sTrack").live("click",function(){
				var item = $(this);
				$(".sTrack").removeClass("selec_tr");
				$("#id_track").val(item.attr('track'));
				$("#id_artist").val(item.attr('artist'));
				$("#id_url").val(item.attr('url'));
				$("#id_user").focus();
				item.addClass("selec_tr");
			});




  


});

