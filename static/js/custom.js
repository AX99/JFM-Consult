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


// Testimonial modal

var more_link = $('#testimonial-block').find('a')
for (let i = 0; i < more_link.length; i++) {
    more_link[i].addEventListener('click', function(){
        var testimonial = this.parentElement.firstElementChild.innerText
        var author = this.parentElement.lastElementChild.innerText
        
        document.getElementById('testimonialAuthor').innerText = author.substring(2)
        document.getElementById('testimonial').innerText = testimonial
})
}