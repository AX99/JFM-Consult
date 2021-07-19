// $(document).on('submit', '#contactForm', function(e){
//     e.preventDefault();
    
//     $.ajax({
//         type:'POST',
//         url: '',
//         data: {
//             first_name:$('#first_name').val(),
//             last_name:$('#last_name').val(),
//             email:$('#email').val(),
//             phone:$('#phone').val(),
//             message:$('#message').val(),
//             csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
//         },

//         success: function(data){
//             console.log('working')
//             $('.messages .alert-success').html(data)
//         },
        
//         error: function(data){
//             console.log('NOT WORKING')
//             $('.messages .alert-danger').html(data)



//         }

//         })
        
// });
