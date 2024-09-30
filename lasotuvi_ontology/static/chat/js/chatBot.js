
// $(document).ready(function () {
//     $(".select2_el").select2({
//     });

//     var check = false;
//     //Toggle fullscreen
//     $(".chat-bot-icon").click(function (e) {
//         $(this).children('img').toggleClass('hide');
//         $(this).children('svg').toggleClass('animate');
//         $('.chat-screen').toggleClass('show-chat');
//         $('.chat-mail').addClass('hide');
//         $('.chat-body').removeClass('hide');
//         $('.chat-input').removeClass('hide');
//         $('.chat-header-option').removeClass('hide');
//         if(check){
//             check = true;
//             var hoten = $('#hoten').val()
//             var data = {"sender":"test_user" , "message": `Tên tôi là ${hoten}` };
//             $.ajax({
//                 url: "http://localhost:5005/webhooks/rest/webhook",
//                 method: 'POST',
//                 dataType: 'JSON',
//                 responseType:'application/json',
//                 data: JSON.stringify(data),
//                 success: function (response) {               
//                     console.log(response);
//                     var tag_messenger = $(`<div class="chat-bubble you text-align-left">${response[0]["custom"]["text"]}</div>`)
//                     $('.chat-body').append(tag_messenger);
//                     if(response[0]["custom"].buttons){
//                         $.each(response[0]["custom"].buttons, function(index, button){
//                             var btn = $(`<button class="btn text-align-left" cung-id="${button["cung-id"]}" payload="${button["payload"]}" url="${button["href"]}">${button.title}</button>`);
//                             $('.chat-body').append(btn);
//                         });
//                         var element = document.getElementById('chat-body');
//                         var y = element.scrollHeight;
//                         element.scrollTop = y;  
//                     }
//                 },
//                 error: function (err) { console.log("có lỗi:",err); }
//             });
//         }
        
//     });
//     $('.chat-mail button').click(function () {
//         $('.chat-mail').addClass('hide');
//         $('.chat-body').removeClass('hide');
//         $('.chat-input').removeClass('hide');
//         $('.chat-header-option').removeClass('hide');
//     });
//     $('.end-chat').click(function () {
//         $('.chat-body').addClass('hide');
//         $('.chat-input').addClass('hide');
//         $('.chat-session-end').removeClass('hide');
//         $('.chat-header-option').addClass('hide');
//     });

//     $('.submit-messenger').click(function(){
//         var messenger = $('.input-messenger').val();
//         var tag_messenger = $(`<div class="chat-bubble me">${messenger}</div>`)
//         $('.chat-body').append(tag_messenger)
//         $('.input-messenger').val("");
//         var data = {"sender":"test_user" , "message": messenger}
//         $.ajax({           
//             type: 'POST',
//             url: "http://localhost:5005/webhooks/rest/webhook",
//             dataType: 'json',
//             responseType:'application/json',
//             data: JSON.stringify(data),
//             success: function (response) {               
//                 console.log(response);
//                 var tag_messenger = '';
//                 if(response[0].text){
//                     tag_messenger = $(`<div class="chat-bubble you text-align-left">${response[0].text}</div>`)
//                 }
//                 else{
//                     tag_messenger = $(`<div class="chat-bubble you text-align-left">${response[0]["custom"]["text"]}</div>`)
//                 }
//                 $('.chat-body').append(tag_messenger);
//                 if(response[0]["custom"]){
//                     var href = response[0]["custom"]["custom"]["href"]
//                     var cungId = response[0]["custom"]["custom"]["cung-id"]
//                     var btn = $(`<div class="chat-bubble you text-align-left"><a href="${href}" cung-id="${cungId}">Bấm vào đây để xem lời giải lá số</a></div>`);
//                     $('.chat-body').append(btn);
//                     CungXungChieu(cungId);
//                 }
//                 var element = document.getElementById('chat-body');
//                 var y = element.scrollHeight;
//                 element.scrollTop = y;
//             },
//             error: function (err) { console.log("có lỗi:",err); }
//         });
//     })

//     $('.input-messenger').on('keypress', function(e){
//         if(e.which == 13){
//             var messenger = $('.input-messenger').val();
//             var tag_messenger = $(`<div class="chat-bubble me">${messenger}</div>`)
//             $('.chat-body').append(tag_messenger)
//             $('.input-messenger').val("");
//             var data = {"sender":"tqhuy" , "message": messenger}
//             $.ajax({   
//                 headers: {'X-CSRFToken': 'csrftoken'},
//                 url: "http://localhost:5005/webhooks/rest/webhook",
//                 type: 'POST',
//                 dataType: 'json',
//                 responseType:'application/json',
//                 data: JSON.stringify(data),               
//                 success: function (response) {               
//                     console.log(response);
//                     var tag_messenger = '';
//                     if(response[0].text){
//                         tag_messenger = $(`<div class="chat-bubble you text-align-left">${response[0].text}</div>`)
//                     }
//                     else{
//                         tag_messenger = $(`<div class="chat-bubble you text-align-left">${response[0]["custom"]["text"]}</div>`)
//                     }
//                     $('.chat-body').append(tag_messenger);
//                     if(response[0]["custom"]){
//                         var href = response[0]["custom"]["custom"]["href"]
//                         var cungId = response[0]["custom"]["custom"]["cung-id"]
//                         var btn = $(`<div class="chat-bubble you text-align-left"><a href="${href}" cung-id="${cungId}">Bấm vào đây để xem lời giải lá số</a></div>`);
//                         $('.chat-body').append(btn);
//                         CungXungChieu(cungId);
//                     }  
//                     var element = document.getElementById('chat-body');
//                     var y = element.scrollHeight;
//                     element.scrollTop = y;            
//                 },
//                 error: function (err) { console.log("có lỗi:",err) }
//             });           
//         }        
//     });
// });