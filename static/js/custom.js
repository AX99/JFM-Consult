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

// Latest comment below
// const form = $('#contactForm');
// form.submit(formHandler);

// function formHandler(e){
//     e.preventDefault();
//     $.ajax({
//         type:'POST',
//         // url: '{% url contact %}',
//         data: $('#contactForm').serialize(),
//         dataType:'json',
//         success: function(data){
//             if (data.msg == 'Success') {
//                 console.log('form ajax working')
//             // $('.messages .alert-success').html(data)
//             }
//         },
//         error: function(data){
//             if (data.msg == 'Error'){
//                 console.log('AJAX Form has errors')
//             }
//         }

//     })
// }


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

// Newsletter popup

$( document ).ready(function() {
    // Get the modal
    var modal = $("#newsletterModal");

    // Get the button that opens the modal
    var btn = $("#myBtn");

    // Get the <span> element that closes the modal
    var span = $(".close");

    // When the user clicks the button, open the modal 
    btn.click(function() {
        modal.show();
    })

    // When the user clicks on <span> (x), close the modal
    span.click(function(){modal.hide()})

    // When the user clicks anywhere outside of the modal, close it
    $(document).click(function(event) {if (event.target == modal) {modal.hide();}})  
});